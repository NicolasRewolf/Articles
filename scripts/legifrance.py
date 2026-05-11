"""
Légifrance (DILA) — wrapper minimal.

Docs API: https://api.piste.gouv.fr/dila/legifrance/lf-engine-app/
Sandbox : https://sandbox-api.piste.gouv.fr/dila/legifrance/lf-engine-app/

Particularité : Légifrance utilise POST + JSON pour la quasi totalité de ses
endpoints (contrairement à Judilibre qui est en GET). Stdlib uniquement.

Usage en CLI:
    python3 scripts/legifrance.py search "loi badinter" --fond LODA_DATE
    python3 scripts/legifrance.py article LEGIARTI000006905746
    python3 scripts/legifrance.py code "Code de la sécurité sociale" "L. 376-1"

Usage en import:
    from scripts.legifrance import search, get_article, consult_code_article
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.piste_auth import api_base, get_token  # noqa: E402

LEGIFRANCE_PATH = "/dila/legifrance/lf-engine-app"


def _post(path: str, payload: dict) -> dict:
    url = api_base() + LEGIFRANCE_PATH + path
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            "Authorization": f"Bearer {get_token()}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body_err = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Légifrance HTTP {e.code} on {url}: {body_err}") from e


def search(
    query: str,
    *,
    fond: str = "CODE_DATE",
    page_size: int = 10,
    page_number: int = 1,
    sort: str = "PERTINENCE",
) -> dict:
    """
    Recherche full-text sur un fonds documentaire.
    - fond: 'CODE_DATE' (codes en vigueur) | 'LODA_DATE' (lois) | 'JURI'
            | 'CETAT' (Conseil d'État) | 'CONSTIT' (Conseil constit) etc.
    - page_size: nb résultats par page
    """
    payload = {
        "recherche": {
            "champs": [
                {
                    "typeChamp": "ALL",
                    "criteres": [
                        {
                            "typeRecherche": "EXACTE" if '"' in query else "UN_DES_MOTS",
                            "valeur": query.strip('"'),
                            "operateur": "ET",
                        }
                    ],
                    "operateur": "ET",
                }
            ],
            "filtres": [{"facette": "DATE_VERSION", "singleDate": None}],
            "pageNumber": page_number,
            "pageSize": page_size,
            "operateur": "ET",
            "sort": sort,
            "typePagination": "DEFAUT",
        },
        "fond": fond,
    }
    return _post("/search", payload)


def get_article(article_id: str) -> dict:
    """Récupère un article par son ID Légifrance (LEGIARTI… / KALIARTI… / etc.)."""
    return _post("/consult/getArticle", {"id": article_id})


def consult_code_article(code_name: str, article_num: str) -> dict:
    """
    Récupère un article d'un code par son numéro lisible.
    Exemple: consult_code_article("Code de la sécurité sociale", "L. 376-1")
    """
    return _post(
        "/consult/code",
        {"textTitle": code_name, "searchedString": article_num},
    )


def _format_hit(hit: dict) -> str:
    title = hit.get("title") or hit.get("titre") or ""
    nature = hit.get("nature") or ""
    date = hit.get("date") or hit.get("date_publi") or ""
    article_id = (
        hit.get("id")
        or (hit.get("sections", [{}])[0].get("id") if hit.get("sections") else "")
    )
    return f"[{nature} {date}] {title}\n  id={article_id}"


def _cli() -> None:
    p = argparse.ArgumentParser(description="Légifrance CLI (DILA)")
    sub = p.add_subparsers(dest="cmd", required=True)

    ps = sub.add_parser("search", help="Recherche full-text")
    ps.add_argument("query")
    ps.add_argument("--fond", default="CODE_DATE",
                    help="CODE_DATE | LODA_DATE | JURI | CETAT | CONSTIT")
    ps.add_argument("--size", type=int, default=10)
    ps.add_argument("--raw", action="store_true")

    pa = sub.add_parser("article", help="Récupère un article par ID Légifrance")
    pa.add_argument("article_id")
    pa.add_argument("--raw", action="store_true")

    pc = sub.add_parser("code", help="Récupère un article d'un code")
    pc.add_argument("code_name", help='ex: "Code de la sécurité sociale"')
    pc.add_argument("article_num", help='ex: "L. 376-1"')
    pc.add_argument("--raw", action="store_true")

    args = p.parse_args()

    if args.cmd == "search":
        result = search(args.query, fond=args.fond, page_size=args.size)
        if args.raw:
            print(json.dumps(result, ensure_ascii=False, indent=2))
            return
        total = result.get("totalResultNumber") or result.get("total", 0)
        results = result.get("results") or []
        print(f"# Légifrance ({args.fond}) — {total} hits (affichage : {len(results)})\n")
        for i, hit in enumerate(results, 1):
            print(f"{i}. {_format_hit(hit)}\n")

    elif args.cmd == "article":
        result = get_article(args.article_id)
        if args.raw:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            article = result.get("article") or {}
            print(f"{article.get('title', '(sans titre)')}\n")
            print(article.get("texte", "(pas de texte)")[:3000])

    elif args.cmd == "code":
        result = consult_code_article(args.code_name, args.article_num)
        if args.raw:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2)[:3000])


if __name__ == "__main__":
    _cli()
