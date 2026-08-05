"""
PISTE Data Gouv — OAuth client_credentials helper.

Charge la configuration (`.env` du repo **et/ou** variables d'environnement),
récupère un access_token via OAuth2 client_credentials, cache le token sur
disque **par environnement** pour éviter de spammer le endpoint.

Stdlib uniquement (pas de dépendance externe).

Usage en CLI:
    python3 scripts/piste_auth.py            # imprime un token valide
    python3 scripts/piste_auth.py --refresh  # force une nouvelle authentification

Usage en import:
    from scripts.piste_auth import get_token, api_base, http_json
    token = get_token()
    base = api_base()

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


def get_token(force_refresh: bool = False, scope: str = "openid") -> str:
    """Retourne un access_token valide (cache disque, par environnement)."""
    env = _load_env()
    env_name = _env_name(env)

    if not force_refresh:
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

    payload = http_json(
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
    _write_cache(env_name, payload)
    return payload["access_token"]


if __name__ == "__main__":
    force = "--refresh" in sys.argv
    print(get_token(force_refresh=force))
