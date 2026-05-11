"""
Judilibre (Cour de Cassation) — wrapper minimal.

Docs API: https://api.piste.gouv.fr/cassation/judilibre/v1.0/
Sandbox : https://sandbox-api.piste.gouv.fr/cassation/judilibre/v1.0/

Stdlib uniquement.

Usage en CLI:
    python3 scripts/judilibre.py search "indemnisation moto" --size 5
    python3 scripts/judilibre.py decision <decision_id>

Usage en import:
    from scripts.judilibre import search, get_decision
    hits = search("préjudice esthétique motard", size=10)
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.piste_auth import api_base, get_token  # noqa: E402

JUDILIBRE_PATH = "/cassation/judilibre/v1.0"


def _request(path: str, params: dict | None = None) -> dict:
    base = api_base() + JUDILIBRE_PATH
    url = base + path
    if params:
        # On accepte les params multivalués (listes) en répétant la clé.
        items = []
        for k, v in params.items():
            if v is None:
                continue
            if isinstance(v, (list, tuple)):
                for item in v:
                    items.append((k, item))
            else:
                items.append((k, v))
        url += "?" + urllib.parse.urlencode(items)

    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {get_token()}",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Judilibre HTTP {e.code} on {url}: {body}") from e


def search(
    query: str,
    *,
    size: int = 10,
    sort: str = "score",
    jurisdiction: list[str] | None = None,
    chamber: list[str] | None = None,
    date_start: str | None = None,
    date_end: str | None = None,
    publication: list[str] | None = None,
) -> dict:
    """
    Recherche full-text sur Judilibre.
    - query: chaîne de recherche
    - size: nb de résultats (max 50)
    - sort: 'score'|'date_asc'|'date_desc'
    - jurisdiction: ex ['cc'] pour Cour de cassation
    - chamber: ex ['civ1', 'civ2', 'crim', 'soc']
    - date_start / date_end: 'YYYY-MM-DD'
    - publication: ex ['b'] (bulletin), ['r'] (rapport)
    """
    return _request(
        "/search",
        {
            "query": query,
            "page_size": size,
            "sort": sort,
            "jurisdiction": jurisdiction,
            "chamber": chamber,
            "date_start": date_start,
            "date_end": date_end,
            "publication": publication,
        },
    )


def get_decision(decision_id: str) -> dict:
    """Récupère le contenu complet d'une décision par son ID."""
    return _request("/decision", {"id": decision_id})


def taxonomy(key: str) -> dict:
    """Liste les valeurs possibles d'un facet (jurisdiction, chamber, publication, ...)."""
    return _request("/taxonomy", {"id": key})


def _format_hit(hit: dict) -> str:
    juridiction = hit.get("jurisdiction") or hit.get("juridiction") or ""
    chambre = hit.get("chamber", "")
    date = hit.get("decision_date", "")
    num = hit.get("number", "")
    titles = hit.get("titles") or []
    title_str = " — ".join(
        [t.get("title", "") for t in titles if isinstance(t, dict)][:2]
    )
    summary = (hit.get("summary") or "")[:280].replace("\n", " ")
    return (
        f"[{juridiction} {chambre} {date} n°{num}] {title_str}\n  → {summary}…"
    )


def _cli() -> None:
    p = argparse.ArgumentParser(description="Judilibre CLI (Cour de Cassation)")
    sub = p.add_subparsers(dest="cmd", required=True)

    ps = sub.add_parser("search", help="Recherche full-text")
    ps.add_argument("query")
    ps.add_argument("--size", type=int, default=5)
    ps.add_argument("--sort", default="score")
    ps.add_argument("--chamber", action="append")
    ps.add_argument("--from", dest="date_start")
    ps.add_argument("--to", dest="date_end")
    ps.add_argument("--raw", action="store_true", help="Sort le JSON brut")

    pd = sub.add_parser("decision", help="Récupère une décision par ID")
    pd.add_argument("id")
    pd.add_argument("--raw", action="store_true")

    pt = sub.add_parser("taxonomy", help="Liste les valeurs d'un facet")
    pt.add_argument("key")

    args = p.parse_args()

    if args.cmd == "search":
        result = search(
            args.query,
            size=args.size,
            sort=args.sort,
            chamber=args.chamber,
            date_start=args.date_start,
            date_end=args.date_end,
        )
        if args.raw:
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return
        total = result.get("total", 0)
        results = result.get("results", [])
        print(f"# Judilibre — {total} hits (affichage : {len(results)})\n")
        for i, hit in enumerate(results, 1):
            print(f"{i}. {_format_hit(hit)}\n")

    elif args.cmd == "decision":
        result = get_decision(args.id)
        if args.raw:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(
                f"{result.get('jurisdiction','')} {result.get('chamber','')} "
                f"{result.get('decision_date','')} n°{result.get('number','')}\n"
            )
            print(result.get("text", "")[:2000])

    elif args.cmd == "taxonomy":
        result = taxonomy(args.key)
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    _cli()
