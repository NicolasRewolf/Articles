"""
PISTE Data Gouv — OAuth client_credentials helper.

Charge .env, récupère un access_token via OAuth2 client_credentials,
cache le token sur disque pour éviter de spammer le endpoint.

Stdlib uniquement (pas de dépendance externe).

Usage en CLI:
    python3 scripts/piste_auth.py        # imprime un token valide

Usage en import:
    from scripts.piste_auth import get_token, api_base
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    base = api_base()
"""

from __future__ import annotations

import json
import os
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
CACHE_DIR = ROOT / ".cache"
TOKEN_CACHE = CACHE_DIR / "piste_token.json"

# 50 min — token PISTE dure 1h, marge de sécurité
TOKEN_MARGIN_S = 600


def _load_env() -> dict:
    """Lit .env en mode simple KEY=VALUE."""
    env = {}
    if not ENV_FILE.exists():
        raise RuntimeError(f".env introuvable: {ENV_FILE}")
    for line in ENV_FILE.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        env[k.strip()] = v.strip().strip('"').strip("'")
    return env


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
    env = _load_env()
    return _endpoints(env.get("PISTE_ENV", "sandbox"))["api"]


def _read_cache() -> dict | None:
    if not TOKEN_CACHE.exists():
        return None
    try:
        data = json.loads(TOKEN_CACHE.read_text())
        if data.get("expires_at", 0) - TOKEN_MARGIN_S > time.time():
            return data
    except (json.JSONDecodeError, OSError):
        return None
    return None


def _write_cache(token_data: dict) -> None:
    CACHE_DIR.mkdir(exist_ok=True)
    TOKEN_CACHE.write_text(json.dumps(token_data, indent=2))


def get_token(force_refresh: bool = False, scope: str = "openid") -> str:
    """Retourne un access_token valide (cache disk-side)."""
    if not force_refresh:
        cached = _read_cache()
        if cached:
            return cached["access_token"]

    env = _load_env()
    client_id = env.get("PISTE_CLIENT_ID")
    client_secret = env.get("PISTE_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise RuntimeError("PISTE_CLIENT_ID / PISTE_CLIENT_SECRET manquants dans .env")

    endpoint = _endpoints(env.get("PISTE_ENV", "sandbox"))["oauth"]
    body = urllib.parse.urlencode(
        {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": scope,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        endpoint,
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        msg = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OAuth PISTE HTTP {e.code}: {msg}") from e

    if "access_token" not in payload:
        raise RuntimeError(f"Réponse OAuth inattendue: {payload}")

    payload["expires_at"] = int(time.time()) + int(payload.get("expires_in", 3600))
    _write_cache(payload)
    return payload["access_token"]


if __name__ == "__main__":
    force = "--refresh" in sys.argv
    print(get_token(force_refresh=force))
