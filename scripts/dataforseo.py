"""
DataForSEO — wrapper minimal (volumes, SERP, solde).

Docs API : https://docs.dataforseo.com/v3/

Pourquoi ce script existe : le serveur MCP `dataforseo` n'est pas chargé dans
toutes les sessions (il dépend d'un `npx` qui peut échouer silencieusement), et
le Bloc B du workflow devient alors aveugle — ni volumes, ni PAA, ni SERP. Les
credentials, eux, sont bien présents sur la machine. Un wrapper stdlib rend la
donnée accessible quel que soit l'état du MCP, comme `judilibre.py` et
`legifrance.py` le font pour PISTE.

Stdlib uniquement (pas de dépendance externe).

Usage en CLI :
    python3 scripts/dataforseo.py solde
    python3 scripts/dataforseo.py volumes "cour criminelle départementale" "cour d'assises"
    python3 scripts/dataforseo.py serp "cour criminelle départementale" --paa 2

Usage en import :
    from scripts.dataforseo import volumes, serp
    data = volumes(["cour d'assises", "porter plainte pour viol"])

Configuration — résolution des credentials, dans cet ordre :
    1. variables d'environnement DATAFORSEO_USERNAME / DATAFORSEO_PASSWORD
    2. fichier `.env` du repo (mêmes clés)
    3. configuration Claude Code `~/.claude.json` (bloc mcpServers.dataforseo.env)

Le point 3 évite de dupliquer des credentials qui existent déjà sur la machine,
et rend le script utilisable depuis un worktree git (où `.env` n'existe pas).

Note macOS : `http_json` porte déjà l'indice SSL (`export SSL_CERT_FILE=…`,
cf. README §Quirks) — ce script hérite du même traitement d'erreur.

⚠️ Ces appels sont FACTURÉS. `solde` est gratuit et sert de test de connexion.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.piste_auth import http_json  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
CLAUDE_CONFIG = Path.home() / ".claude.json"

BASE = "https://api.dataforseo.com/v3"

# France / français — le pipeline ne cible aucun autre marché.
LOCATION_DEFAUT = 2250
LANGUE_DEFAUT = "fr"

# Taille de lot pour les volumes. L'endpoint Google Ads accepte de larges lots ;
# la limite de 10 relevée à l'usage venait du serveur MCP, pas de l'API.
# Conservateur par défaut : un lot trop gros échoue en bloc, plusieurs lots non.
LOT_VOLUMES = 100


# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

def _depuis_env_file() -> dict:
    valeurs: dict[str, str] = {}
    if not ENV_FILE.exists():
        return valeurs
    for ligne in ENV_FILE.read_text().splitlines():
        ligne = ligne.strip()
        if not ligne or ligne.startswith("#") or "=" not in ligne:
            continue
        cle, _, val = ligne.partition("=")
        valeurs[cle.strip()] = val.strip().strip('"').strip("'")
    return valeurs


def _depuis_claude_config() -> dict:
    """Credentials déjà posés pour le serveur MCP `dataforseo`."""
    if not CLAUDE_CONFIG.exists():
        return {}
    try:
        config = json.loads(CLAUDE_CONFIG.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    serveur = (config.get("mcpServers") or {}).get("dataforseo") or {}
    return dict(serveur.get("env") or {})


def resoudre_credentials(sources: list[dict] | None = None) -> tuple[str, str]:
    """(login, mot de passe) — première source qui porte les deux clés.

    `sources` est le seam de test : par défaut, l'ordre documenté en tête de
    module (environnement, puis `.env`, puis configuration Claude Code).
    """
    if sources is None:
        sources = [dict(os.environ), _depuis_env_file(), _depuis_claude_config()]
    for source in sources:
        login = source.get("DATAFORSEO_USERNAME") or source.get("DATAFORSEO_LOGIN")
        mdp = source.get("DATAFORSEO_PASSWORD")
        if login and mdp:
            return login, mdp
    raise RuntimeError(
        "DATAFORSEO_USERNAME / DATAFORSEO_PASSWORD introuvables — cherchés dans "
        f"les variables d'environnement, {ENV_FILE}, puis {CLAUDE_CONFIG} "
        "(bloc mcpServers.dataforseo.env)."
    )


def _entetes(credentials: tuple[str, str] | None = None) -> dict:
    login, mdp = credentials or resoudre_credentials()
    jeton = base64.b64encode(f"{login}:{mdp}".encode()).decode()
    return {"Authorization": f"Basic {jeton}", "Content-Type": "application/json"}


# --------------------------------------------------------------------------
# Appels
# --------------------------------------------------------------------------

def _post(chemin: str, payload: list | dict, *, transport=None,
          credentials=None, timeout: int = 120) -> dict:
    transport = transport or http_json
    return transport(
        BASE + chemin,
        data=json.dumps(payload).encode("utf-8"),
        headers=_entetes(credentials),
        method="POST",
        timeout=timeout,
        label="DataForSEO",
    )


def _get(chemin: str, *, transport=None, credentials=None, timeout: int = 30) -> dict:
    transport = transport or http_json
    return transport(BASE + chemin, headers=_entetes(credentials),
                     timeout=timeout, label="DataForSEO")


def _resultats(reponse: dict) -> list:
    """Résultats de la première tâche, avec erreurs API remontées en clair.

    L'API répond HTTP 200 même quand la tâche échoue : le statut utile est
    `status_code` (20000 = OK), pas le code HTTP. Sans ce contrôle, un échec
    ressort en liste vide et se confond avec « aucune donnée ».
    """
    if reponse.get("status_code") != 20000:
        raise RuntimeError(f"DataForSEO {reponse.get('status_code')} : "
                           f"{reponse.get('status_message')}")
    taches = reponse.get("tasks") or []
    if not taches:
        return []
    tache = taches[0]
    if tache.get("status_code") != 20000:
        raise RuntimeError(f"DataForSEO tâche {tache.get('status_code')} : "
                           f"{tache.get('status_message')}")
    return tache.get("result") or []


def lots(items: list, taille: int = LOT_VOLUMES) -> list[list]:
    """Découpe en lots de `taille` (le dernier peut être plus court)."""
    if taille < 1:
        raise ValueError("taille de lot < 1")
    return [items[i:i + taille] for i in range(0, len(items), taille)]


def solde(*, transport=None, credentials=None) -> dict:
    """Solde et informations de compte (endpoint GRATUIT)."""
    resultat = _resultats(_get("/appendix/user_data",
                               transport=transport, credentials=credentials))
    return resultat[0] if resultat else {}


def volumes(mots_cles: list[str], *, location: int = LOCATION_DEFAUT,
            langue: str = LANGUE_DEFAUT, taille_lot: int = LOT_VOLUMES,
            transport=None, credentials=None) -> list[dict]:
    """Volumes de recherche Google Ads, par lots. FACTURÉ."""
    sortie: list[dict] = []
    for lot in lots(mots_cles, taille_lot):
        payload = [{"keywords": lot, "location_code": location,
                    "language_code": langue}]
        reponse = _post("/keywords_data/google_ads/search_volume/live", payload,
                        transport=transport, credentials=credentials)
        sortie.extend(_resultats(reponse))
    return sortie


def serp(requete: str, *, location: int = LOCATION_DEFAUT,
         langue: str = LANGUE_DEFAUT, profondeur_paa: int = 1,
         nombre: int = 20, transport=None, credentials=None) -> dict:
    """SERP organique + People Also Ask. FACTURÉ."""
    payload = [{"keyword": requete, "location_code": location,
                "language_code": langue, "device": "desktop",
                "depth": nombre, "people_also_ask_click_depth": profondeur_paa}]
    resultat = _resultats(_post("/serp/google/organic/live/advanced", payload,
                                transport=transport, credentials=credentials))
    return resultat[0] if resultat else {}


# --------------------------------------------------------------------------
# Mise en forme
# --------------------------------------------------------------------------

def ligne_volume(item: dict) -> str:
    """Une ligne lisible par mot-clé, volumes manquants explicites."""
    volume = item.get("search_volume")
    volume_txt = "n/d" if volume is None else f"{volume:,}".replace(",", " ")
    indice = item.get("competition_index")
    indice_txt = "n/d" if indice is None else str(indice)
    cpc = item.get("cpc")
    cpc_txt = "n/d" if cpc is None else f"{cpc:.2f}"
    return (f"{volume_txt:>9}/mo · concurrence {item.get('competition') or 'n/d':<8} "
            f"(index {indice_txt:>3}) · CPC {cpc_txt:>5} € · {item.get('keyword')}")


def extraire_serp(resultat: dict) -> dict:
    """Organiques et PAA d'un résultat SERP, sous une forme exploitable.

    Les blocs SERP mélangent les types (`organic`, `people_also_ask`, `video`…) ;
    le Bloc B a besoin des deux premiers, séparés.
    """
    organiques: list[dict] = []
    paa: list[str] = []
    for bloc in resultat.get("items") or []:
        type_bloc = bloc.get("type")
        if type_bloc == "organic":
            organiques.append({
                "rang": bloc.get("rank_group"),
                "domaine": bloc.get("domain"),
                "titre": bloc.get("title"),
                "url": bloc.get("url"),
            })
        elif type_bloc == "people_also_ask":
            for question in bloc.get("items") or []:
                titre = question.get("title")
                if titre:
                    paa.append(titre)
        elif type_bloc == "people_also_ask_element":
            titre = bloc.get("title")
            if titre:
                paa.append(titre)
    return {"requete": resultat.get("keyword"),
            "total": resultat.get("se_results_count"),
            "organiques": organiques, "paa": paa}


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def _cli() -> None:
    p = argparse.ArgumentParser(description="DataForSEO CLI (volumes, SERP, solde)")
    sous = p.add_subparsers(dest="cmd", required=True)

    sous.add_parser("solde", help="solde du compte (gratuit)")

    pv = sous.add_parser("volumes", help="volumes de recherche (FACTURÉ)")
    pv.add_argument("mots_cles", nargs="+")
    pv.add_argument("--lot", type=int, default=LOT_VOLUMES)
    pv.add_argument("--location", type=int, default=LOCATION_DEFAUT)
    pv.add_argument("--langue", default=LANGUE_DEFAUT)
    pv.add_argument("--raw", action="store_true")

    ps = sous.add_parser("serp", help="SERP organique + PAA (FACTURÉ)")
    ps.add_argument("requete")
    ps.add_argument("--paa", type=int, default=1, help="profondeur People Also Ask (1-4)")
    ps.add_argument("--nombre", type=int, default=20)
    ps.add_argument("--location", type=int, default=LOCATION_DEFAUT)
    ps.add_argument("--langue", default=LANGUE_DEFAUT)
    ps.add_argument("--raw", action="store_true")

    args = p.parse_args()

    if args.cmd == "solde":
        compte = solde()
        argent = compte.get("money") or {}
        print(f"compte : {compte.get('login')}")
        print(f"solde  : {argent.get('balance')} $")
        return

    if args.cmd == "volumes":
        items = volumes(args.mots_cles, location=args.location,
                        langue=args.langue, taille_lot=args.lot)
        if args.raw:
            print(json.dumps(items, ensure_ascii=False, indent=2))
            return
        items.sort(key=lambda i: (i.get("search_volume") or 0), reverse=True)
        print(f"# Volumes — {len(items)} mot(s)-clé(s), "
              f"location {args.location}, langue {args.langue}\n")
        for item in items:
            print(ligne_volume(item))
        if any(i.get("search_volume") is None for i in items):
            print("\n⚠️  « n/d » n'est PAS un volume nul : Google Ads supprime la donnée "
                  "de certains termes,\n    notamment les termes sexuels bruts "
                  "(« agression sexuelle », « inceste », « viol »).\n"
                  "    Mesurer la demande par proxies procéduraux "
                  "(« porter plainte pour … ») et par la SERP.")
        return

    if args.cmd == "serp":
        resultat = serp(args.requete, location=args.location, langue=args.langue,
                        profondeur_paa=args.paa, nombre=args.nombre)
        if args.raw:
            print(json.dumps(resultat, ensure_ascii=False, indent=2))
            return
        vue = extraire_serp(resultat)
        print(f"# SERP — « {vue['requete']} » ({vue['total']} résultats estimés)\n")
        print("## Organiques")
        for o in vue["organiques"]:
            print(f"{str(o['rang']):>3}. {o['domaine']} — {o['titre']}")
            print(f"     {o['url']}")
        print(f"\n## People Also Ask ({len(vue['paa'])})")
        for question in vue["paa"]:
            print(f"- {question}")


if __name__ == "__main__":
    _cli()
