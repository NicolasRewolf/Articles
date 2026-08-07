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
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts.piste_auth import PisteClient  # noqa: E402

LEGIFRANCE_PATH = "/dila/legifrance/lf-engine-app"

_CLIENT: PisteClient | None = None


def _api(client: PisteClient | None = None) -> PisteClient:
    """Client Légifrance — celui fourni, sinon celui du process (construit une fois)."""
    global _CLIENT
    if client is not None:
        return client
    if _CLIENT is None:
        _CLIENT = PisteClient(LEGIFRANCE_PATH, label="Légifrance")
    return _CLIENT


def search(
    query: str,
    *,
    fond: str = "CODE_DATE",
    page_size: int = 10,
    page_number: int = 1,
    sort: str = "PERTINENCE",
    client: PisteClient | None = None,
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
            # Pas de bloc `filtres` : un `{"facette": "DATE_VERSION", "singleDate": null}`
            # faisait répondre 500 au backend DILA (« exception non gérée »). Pour filtrer
            # sur une date de version, passer un timestamp en millisecondes — jamais null.
            "pageNumber": page_number,
            "pageSize": page_size,
            "operateur": "ET",
            "sort": sort,
            "typePagination": "DEFAUT",
        },
        "fond": fond,
    }
    return _api(client).post("/search", payload)


def get_article(article_id: str, *, client: PisteClient | None = None) -> dict:
    """Récupère un article par son ID Légifrance (LEGIARTI… / KALIARTI… / etc.)."""
    return _api(client).post("/consult/getArticle", {"id": article_id})


def _normaliser_num(num: str) -> str:
    """« L. 376-1 » → « L376-1 » (forme attendue par la facette NUM_ARTICLE)."""
    return re.sub(r"[\s.]", "", num or "")


def consult_code_article(code_name: str, article_num: str, *,
                         client: PisteClient | None = None) -> dict:
    """Récupère un article d'un code par son numéro lisible.

        consult_code_article("Code de la sécurité sociale", "L. 376-1")

    Rend le même objet que `get_article` (clé `article`, avec `texte`), plus une
    clé `_source` portant le code, le LEGIARTI retenu, son `legalStatus` et sa
    date de version.

    ⚠️ La recherche rend TOUTES les versions successives de l'article, la plupart
    en `legalStatus=MODIFIE` (périmées). On retient la version en **VIGUEUR**, la
    plus récente — citer une version modifiée serait une faute de fond. Si aucune
    version en vigueur n'est trouvée, on rend la plus récente en signalant son
    statut dans `_source` (à ne pas citer sans vérification).

    L'endpoint `/consult/code` de PISTE répond 500 sur toutes les formes de
    payload essayées (validé contre l'API prod le 2026-08-07 : `{textTitle,
    searchedString}` comme `{textId, date}`). On passe donc par le chemin qui
    fonctionne : recherche par facette NUM_ARTICLE sur le fond CODE_DATE pour
    résoudre le LEGIARTI, puis `get_article`.

    Lève `LookupError` si aucun article ne correspond au couple (code, numéro).
    """
    api = _api(client)
    reponse = api.post("/search", {
        "recherche": {
            "champs": [{
                "typeChamp": "NUM_ARTICLE",
                "criteres": [{"typeRecherche": "EXACTE",
                              "valeur": _normaliser_num(article_num),
                              "operateur": "ET"}],
                "operateur": "ET",
            }],
            "pageNumber": 1,
            "pageSize": 50,
            "operateur": "ET",
            "sort": "PERTINENCE",
            "typePagination": "DEFAUT",
        },
        "fond": "CODE_DATE",
    })

    cible = _demarquer(code_name).strip().lower()
    attendu = _normaliser_num(article_num)
    candidats: dict[str, tuple[str, str, str]] = {}  # id → (code, legalStatus, dateVersion)

    for hit in reponse.get("results") or []:
        titres = hit.get("titles") or []
        titre = _demarquer(titres[0].get("title", "")).strip() if titres else ""
        if cible not in titre.lower():
            continue
        for section in hit.get("sections") or []:
            date_version = (section.get("dateVersion") or "")[:10]
            for extrait in section.get("extracts") or []:
                if _normaliser_num(_demarquer(extrait.get("title", ""))) != attendu:
                    continue
                ident = extrait.get("id")
                if not ident:
                    continue
                statut = extrait.get("legalStatus") or ""
                connu = candidats.get(ident)
                # On garde la date de version la plus récente vue pour cet id.
                if connu is None or date_version > connu[2]:
                    candidats[ident] = (titre, statut, date_version)

    if not candidats:
        raise LookupError(
            f"Aucun article « {article_num} » trouvé dans « {code_name} » "
            f"({reponse.get('totalResultNumber', 0)} résultats pour ce numéro, tous codes confondus)"
        )

    # VIGUEUR d'abord, puis version la plus récente.
    ident, (titre, statut, date_version) = max(
        candidats.items(),
        key=lambda kv: (kv[1][1].upper() == "VIGUEUR", kv[1][2]),
    )
    article = get_article(ident, client=api)
    article["_source"] = {"code": titre, "article_id": ident,
                          "legal_status": statut, "date_version": date_version,
                          "versions_vues": len(candidats)}
    return article


def _demarquer(s: str) -> str:
    """Retire le surlignage `<mark>…</mark>` que l'API pose sur les termes trouvés."""
    return re.sub(r"</?mark>", "", s or "")


def _afficher_article(reponse: dict) -> None:
    """Titre + texte d'un article, balises HTML retirées (le verbatim se cite tel quel)."""
    article = reponse.get("article") or {}
    titre = article.get("title") or article.get("num") or "(sans titre)"
    texte = re.sub(r"<[^>]+>", "", article.get("texte") or "(pas de texte)")
    print(f"{titre}\n")
    print(texte.strip()[:3000])


def _format_hit(hit: dict) -> str:
    """Une ligne par texte trouvé + les LEGIARTI des articles qui matchent.

    Ce sont ces identifiants qu'on repasse à `legifrance.py article <id>` pour
    obtenir le verbatim — c'est le geste du fact-check (LEARN-026).
    """
    titres = hit.get("titles") or []
    titre = _demarquer(titres[0].get("title", "")) if titres else "(sans titre)"
    nature = hit.get("nature") or ""
    etat = hit.get("etat") or ""
    date = (hit.get("date") or "")[:10]

    # Les articles concernés vivent dans sections[].extracts[]
    articles: list[str] = []
    for section in hit.get("sections") or []:
        for extrait in section.get("extracts") or []:
            num = _demarquer(extrait.get("title", "")).strip()
            ident = extrait.get("id", "")
            if ident:
                articles.append(f"art. {num} → {ident}" if num else ident)

    lignes = [f"[{nature} {date} · {etat}] {titre}"]
    for a in articles[:5]:
        lignes.append(f"    {a}")
    reste = len(articles) - 5
    if reste > 0:
        lignes.append(f"    … et {reste} autre(s) article(s)")
    return "\n".join(lignes)


def _cli() -> int:
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
            _afficher_article(result)

    elif args.cmd == "code":
        try:
            result = consult_code_article(args.code_name, args.article_num)
        except LookupError as e:
            print(e, file=sys.stderr)
            return 1
        if args.raw:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            src = result.get("_source", {})
            statut = src.get("legal_status", "?")
            marque = "" if statut.upper() == "VIGUEUR" else "  ⚠️ PAS EN VIGUEUR"
            print(f"{src.get('code', '')} — article {args.article_num}")
            print(f"({src.get('article_id', '')} · {statut} · version {src.get('date_version', '?')} "
                  f"· {src.get('versions_vues', '?')} version(s) vue(s)){marque}\n")
            _afficher_article(result)
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
