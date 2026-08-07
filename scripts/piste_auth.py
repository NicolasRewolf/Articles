"""
PISTE Data Gouv — OAuth client_credentials helper.

Charge la configuration (`.env` du repo **et/ou** variables d'environnement),
récupère un access_token via OAuth2 client_credentials, cache le token sur
disque **par environnement** pour éviter de spammer le endpoint.

Stdlib uniquement (pas de dépendance externe).

Usage en CLI:
    python3 scripts/piste_auth.py            # imprime un token valide
    python3 scripts/piste_auth.py --refresh  # force une nouvelle authentification

Usage en import — `PisteClient` est la surface à utiliser :
    from scripts.piste_auth import PisteClient
    api = PisteClient("/cassation/judilibre/v1.0", label="Judilibre")
    api.get("/search", {"query": "…", "chamber": ["civ2", "crim"]})

Le client absorbe ce que chaque wrapper refaisait à la main : résolution de
l'environnement (UNE fois, à la construction, contre deux relectures de `.env`
par appel auparavant), cache du token, montage de l'URL de service, en-tête
`Authorization`, libellé d'erreur, indice SSL macOS.

`transport` est le seam : `http_json` en production, un transport de test dans
les tests (cf. scripts/test_piste_client.py) — aucun appel réseau n'est requis
pour vérifier ce que les wrappers envoient réellement.

`get_token` / `api_base` / `http_json` restent disponibles pour les usages ad hoc.

Configuration (lue dans .env, surchargeable par les variables d'environnement) :
    PISTE_CLIENT_ID, PISTE_CLIENT_SECRET  — credentials de l'app PISTE
    PISTE_ENV                             — 'prod' (défaut) | 'sandbox'

Note macOS : en cas de `CERTIFICATE_VERIFY_FAILED`, exporter le bundle système
avant l'appel — `export SSL_CERT_FILE=/etc/ssl/cert.pem` (cf. README §Quirks).
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
CACHE_DIR = ROOT / ".cache"

# Marge de sécurité de 10 min (600 s) : le token PISTE dure 1 h, il est donc
# réutilisé pendant ~50 min avant d'être renouvelé.
TOKEN_MARGIN_S = 600

# Environnement par défaut : PROD. La doctrine éditoriale (LEARN-054) exige la
# jurisprudence réelle ; sandbox ne sert qu'à tester l'intégration.
DEFAULT_ENV = "prod"

_ENV_KEYS = ("PISTE_CLIENT_ID", "PISTE_CLIENT_SECRET", "PISTE_ENV")


def _load_env() -> dict:
    """Configuration effective : `.env` du repo, puis surcharge par os.environ.

    Le fichier `.env` est optionnel : les variables d'environnement suffisent.
    C'est ce qui rend les scripts utilisables depuis un worktree git (où `.env`
    n'existe pas) sans dupliquer les credentials.
    """
    env: dict[str, str] = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            env[k.strip()] = v.strip().strip('"').strip("'")
    for key in _ENV_KEYS:
        value = os.environ.get(key)
        if value:
            env[key] = value
    return env


def _env_name(env: dict | None = None) -> str:
    env = env if env is not None else _load_env()
    name = (env.get("PISTE_ENV") or "").strip().lower()
    if not name:
        print(
            f"[piste_auth] PISTE_ENV non défini — utilisation de « {DEFAULT_ENV} » "
            f"(doctrine LEARN-054). Définir PISTE_ENV=sandbox pour les tests.",
            file=sys.stderr,
        )
        return DEFAULT_ENV
    if name not in ("prod", "sandbox"):
        raise RuntimeError(f"PISTE_ENV invalide : {name!r} (attendu 'prod' ou 'sandbox')")
    return name


def _endpoints(env_name: str) -> dict:
    if env_name == "prod":
        return {
            "oauth": "https://oauth.piste.gouv.fr/api/oauth/token",
            "api": "https://api.piste.gouv.fr",
        }
    return {
        "oauth": "https://sandbox-oauth.piste.gouv.fr/api/oauth/token",
        "api": "https://sandbox-api.piste.gouv.fr",
    }


def api_base() -> str:
    return _endpoints(_env_name())["api"]


def _token_cache(env_name: str) -> Path:
    """Un fichier de cache PAR environnement.

    Sans cela, un token sandbox encore valide était resservi contre l'API prod
    après une bascule (401 pendant ~50 min, sans auto-guérison).
    """
    return CACHE_DIR / f"piste_token_{env_name}.json"


def _read_cache(env_name: str) -> dict | None:
    cache_file = _token_cache(env_name)
    if not cache_file.exists():
        return None
    try:
        data = json.loads(cache_file.read_text())
    except (json.JSONDecodeError, OSError):
        return None
    if data.get("piste_env") != env_name:  # ceinture + bretelles
        return None
    if data.get("expires_at", 0) - TOKEN_MARGIN_S > time.time():
        return data
    return None


def _write_cache(env_name: str, token_data: dict) -> None:
    CACHE_DIR.mkdir(exist_ok=True)
    _token_cache(env_name).write_text(json.dumps(token_data, indent=2))


def http_json(
    url: str,
    *,
    data: bytes | None = None,
    headers: dict | None = None,
    method: str = "GET",
    timeout: int = 30,
    label: str = "API",
) -> dict:
    """Appel HTTP JSON avec messages d'erreur actionnables (helper partagé).

    Factorise la logique commune à legifrance.py et judilibre.py, et traite le
    cas `URLError` (dont l'échec SSL macOS) qui sortait auparavant en traceback.
    """
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{label} HTTP {e.code} on {url}: {body}") from e
    except urllib.error.URLError as e:
        hint = ""
        if "CERTIFICATE_VERIFY_FAILED" in str(e.reason):
            hint = (
                " — certificats SSL introuvables : réessayer avec "
                "`export SSL_CERT_FILE=/etc/ssl/cert.pem` (cf. README §Quirks)"
            )
        raise RuntimeError(f"{label} injoignable ({url}) : {e.reason}{hint}") from e


def _obtenir_jeton(
    env: dict,
    env_name: str,
    *,
    force_refresh: bool = False,
    scope: str = "openid",
    transport=None,
    cache: bool = True,
) -> str:
    """access_token valide, à partir d'une configuration DÉJÀ résolue."""
    transport = transport or http_json

    if cache and not force_refresh:
        cached = _read_cache(env_name)
        if cached:
            return cached["access_token"]

    client_id = env.get("PISTE_CLIENT_ID")
    client_secret = env.get("PISTE_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise RuntimeError(
            "PISTE_CLIENT_ID / PISTE_CLIENT_SECRET manquants "
            f"(cherchés dans {ENV_FILE} et dans les variables d'environnement)"
        )

    body = urllib.parse.urlencode(
        {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": scope,
        }
    ).encode("utf-8")

    payload = transport(
        _endpoints(env_name)["oauth"],
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
        timeout=15,
        label=f"OAuth PISTE ({env_name})",
    )

    if "access_token" not in payload:
        raise RuntimeError(f"Réponse OAuth inattendue: {payload}")

    payload["expires_at"] = int(time.time()) + int(payload.get("expires_in", 3600))
    payload["piste_env"] = env_name
    if cache:
        _write_cache(env_name, payload)
    return payload["access_token"]


def get_token(force_refresh: bool = False, scope: str = "openid") -> str:
    """Retourne un access_token valide (cache disque, par environnement)."""
    env = _load_env()
    return _obtenir_jeton(env, _env_name(env), force_refresh=force_refresh, scope=scope)


def _encoder_params(params: dict) -> str:
    """Query string acceptant les params multivalués (la clé est répétée)."""
    items: list[tuple[str, object]] = []
    for k, v in params.items():
        if v is None:
            continue
        if isinstance(v, (list, tuple)):
            items.extend((k, item) for item in v)
        else:
            items.append((k, v))
    return urllib.parse.urlencode(items)


class PisteClient:
    """Accès à UN service PISTE (Judilibre, Légifrance…).

    Un client = un chemin de service. La configuration est résolue à la
    construction, pas à chaque appel : `api_base()` puis `get_token()` relisaient
    `.env` deux fois par requête, et réémettaient deux fois l'avertissement
    « PISTE_ENV non défini ».

    `transport` est le seam. `jeton` court-circuite l'authentification (tests,
    ou jeton obtenu par ailleurs) : dans ce cas ni appel OAuth, ni cache disque.
    """

    def __init__(
        self,
        chemin_service: str,
        *,
        label: str,
        transport=None,
        env: dict | None = None,
        jeton: str | None = None,
        cache: bool = True,
        timeout: int = 30,
    ) -> None:
        self._service = chemin_service.rstrip("/")
        self._label = label
        self._transport = transport or http_json
        self._env = dict(env) if env is not None else _load_env()
        self._nom_env = _env_name(self._env)
        self._base = _endpoints(self._nom_env)["api"]
        self._jeton_fixe = jeton
        self._cache = cache
        self._timeout = timeout

    @property
    def nom_env(self) -> str:
        return self._nom_env

    def url(self, chemin: str) -> str:
        return self._base + self._service + chemin

    def _jeton(self) -> str:
        if self._jeton_fixe is not None:
            return self._jeton_fixe
        return _obtenir_jeton(self._env, self._nom_env,
                              transport=self._transport, cache=self._cache)

    def _entetes(self, **extra: str) -> dict:
        entetes = {"Authorization": f"Bearer {self._jeton()}", "Accept": "application/json"}
        entetes.update(extra)
        return entetes

    def get(self, chemin: str, params: dict | None = None) -> dict:
        url = self.url(chemin)
        if params:
            query = _encoder_params(params)
            if query:
                url += "?" + query
        return self._transport(
            url, headers=self._entetes(), timeout=self._timeout, label=self._label
        )

    def post(self, chemin: str, payload: dict) -> dict:
        return self._transport(
            self.url(chemin),
            data=json.dumps(payload).encode("utf-8"),
            headers=self._entetes(**{"Content-Type": "application/json"}),
            method="POST",
            timeout=self._timeout,
            label=self._label,
        )


if __name__ == "__main__":
    force = "--refresh" in sys.argv
    print(get_token(force_refresh=force))
