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
import datetime
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


# Nombre de versions candidates qu'on accepte d'aller chercher pour trouver
# celle qui couvre le jour demandé. Borne le coût réseau : au-delà, le jeu de
# versions rendu par la recherche est probablement incomplet de toute façon.
_MAX_VERSIONS_TESTEES = 5


def _aujourdhui() -> str:
    return datetime.date.today().isoformat()


_MOTIF_JOUR = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _en_date(valeur) -> str:
    """Rend « AAAA-MM-JJ » depuis un timestamp Légifrance (ms) ou une date ISO.

    Rend « » sur tout ce qui n'est pas une date lisible. Ne jamais tronquer une
    chaîne inconnue à 10 caractères : elle deviendrait une pseudo-date, comparée
    lexicographiquement comme les autres, et fausserait la sélection de version
    sans rien signaler.
    """
    if valeur is None or valeur == "":
        return ""
    if isinstance(valeur, str):
        jour = valeur[:10]
        return jour if _MOTIF_JOUR.match(jour) else ""
    try:
        horodatage = datetime.datetime.fromtimestamp(int(valeur) / 1000, datetime.timezone.utc)
    except (TypeError, ValueError, OSError, OverflowError):
        return ""
    return horodatage.strftime("%Y-%m-%d")


def _en_vigueur_le(article: dict, jour: str) -> bool:
    """Vrai si la version d'article couvre `jour`, sur les bornes [dateDebut, dateFin[.

    On tranche sur les DATES, jamais sur le libellé `etat`. Une version
    parfaitement applicable peut porter `ABROGE_DIFF` — le libellé signifie
    « abrogation déjà programmée à une date future », pas « plus applicable ».
    C'est le cas de tout le code pénal depuis l'ordonnance du 19 novembre 2025,
    qui recodifie au 2029-01-01 : se fier au libellé faisait écarter le texte en
    vigueur (constaté sur l'art. 222-22 CP pendant la rédaction de l'article #12).
    """
    debut = _en_date(article.get("dateDebut"))
    if not debut or debut > jour:
        return False
    fin = _en_date(article.get("dateFin"))
    return not fin or jour < fin


def _ordonner_candidats(candidats: dict[str, tuple[str, str, str]]) -> list[str]:
    """Ordre d'examen : `VIGUEUR` d'abord, puis la date de version décroissante.

    Garde le chemin rapide d'avant (un article dont une version est explicitement
    en VIGUEUR est résolu en un seul appel) tout en laissant une porte de sortie
    quand aucune version ne porte ce libellé.
    """
    return [
        ident
        for ident, _ in sorted(
            candidats.items(),
            key=lambda kv: (kv[1][1].upper() == "VIGUEUR", kv[1][2]),
            reverse=True,
        )
    ]


def consult_code_article(code_name: str, article_num: str, *,
                         client: PisteClient | None = None) -> dict:
    """Récupère un article d'un code par son numéro lisible.

        consult_code_article("Code de la sécurité sociale", "L. 376-1")

    Rend le même objet que `get_article` (clé `article`, avec `texte`), plus une
    clé `_source` portant le code, le LEGIARTI retenu, son `legalStatus` et sa
    date de version.

    ⚠️ La recherche rend TOUTES les versions successives de l'article, la plupart
    en `legalStatus=MODIFIE` (périmées). Citer une version modifiée serait une
    faute de fond. On retient donc la version qui **couvre la date du jour**, sur
    les bornes `dateDebut`/`dateFin` — et non celle dont le libellé vaut
    littéralement `VIGUEUR` : une version applicable peut porter `ABROGE_DIFF`
    (abrogation programmée à une date future, cf. `_en_vigueur_le`). Si aucune
    version ne couvre le jour, on rend la meilleure candidate en posant
    `_source["en_vigueur"] = False` (à ne pas citer sans vérification).

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

    # On examine les candidates dans l'ordre (VIGUEUR d'abord, puis les plus
    # récentes) et on retient la première qui couvre réellement le jour.
    jour = _aujourdhui()
    ordre = _ordonner_candidats(candidats)
    retenu: tuple[str, dict] | None = None
    couvre = False

    for ident in ordre[:_MAX_VERSIONS_TESTEES]:
        article = get_article(ident, client=api)
        if _en_vigueur_le(article.get("article") or {}, jour):
            retenu, couvre = (ident, article), True
            break
        if retenu is None:
            retenu = (ident, article)  # meilleur défaut : la tête de l'ordre

    ident, article = retenu  # `candidats` non vide ⇒ `retenu` non nul
    titre, statut, date_version = candidats[ident]
    contenu = article.get("article") or {}
    article["_source"] = {"code": titre, "article_id": ident,
                          "legal_status": statut, "date_version": date_version,
                          "date_debut": _en_date(contenu.get("dateDebut")),
                          "date_fin": _en_date(contenu.get("dateFin")),
                          "en_vigueur": couvre, "jour_teste": jour,
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
            jour = src.get("jour_teste", "?")
            marque = "" if src.get("en_vigueur") else f"  ⚠️ NE COUVRE PAS LE {jour}"
            bornes = f"{src.get('date_debut') or '?'} → {src.get('date_fin') or '?'}"
            print(f"{src.get('code', '')} — article {args.article_num}")
            print(f"({src.get('article_id', '')} · {statut} · applicable {bornes} "
                  f"· {src.get('versions_vues', '?')} version(s) vue(s)){marque}\n")
            _afficher_article(result)
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
