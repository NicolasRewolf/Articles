"""
Markdown → Wix Ricos JSON converter (minimal, ad-hoc pour Cabinet Plouton).

Stdlib uniquement. Supporte :
- H2/H3 (avec ancres {#id})
- Paragraphes
- Listes à puces ET listes ordonnées (1. 2. 3. → ORDERED_LIST)
- Blockquotes (multi-lignes)
- Dividers (---)
- Inline: **bold**, *italic*, [text](url)
- FAQ : H3 sous `## H2 6 — Questions fréquentes` → COLLAPSIBLE_LIST automatique

Convention liens (LEARN-024) et normalisation des URL : déléguées à
`politique_liens`, qui est la source unique partagée avec `lint_pipeline`
(le garde-fou signale et le convertisseur rend d'après la même classification).

`parse_markdown` est fonction de sa seule entrée : les ids de nœuds sont
alloués par un compteur créé à chaque appel. Deux appels sur le même markdown
rendent le même document — c'est ce qui permet de comparer un `ricos.min.json`
stocké à l'article sans toucher aux internes du module (cf. `fraicheur`).

Exclusions par défaut :
- H1
- Sections marquées "## Notes méthodologiques" (et tout ce qui suit)
- Blockquote contenant "Livrable Étape" au début

Le "## Sommaire" est CONVERTI (H2 + liste de liens d'ancrage `[texte](#ancre)`),
les ancres `#ancre` étant traitées comme liens internes (SELF, sans rel). Poser
les ancres cibles sur les H2 via `## Titre {#ancre}`.

Usage :
    python3 scripts/md_to_ricos.py <input.md> > out.json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import NamedTuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scripts import politique_liens  # noqa: E402

# Réexports historiques : la politique de liens vit désormais dans son module.
INTERNAL_DOMAIN = politique_liens.DOMAINE_INTERNE
INTERNAL_BASE = politique_liens.BASE_INTERNE
normalize_url = politique_liens.normaliser


def _link_data(url: str) -> dict:
    """Enveloppe Ricos autour des attributs décidés par `politique_liens`."""
    return {"link": politique_liens.attributs(url)}


# ---------- Helpers id ----------
class _Ids:
    """Allocateur d'ids propre à UN document.

    Il remplace un compteur global de module : `parse_markdown` en crée un à
    chaque appel, donc le même markdown rend toujours le même document. Avant,
    l'appelant devait remettre à zéro `md_to_ricos._counter` — le garde-fou le
    faisait, en passant derrière l'interface.
    """

    def __init__(self) -> None:
        self._n = 0

    def __call__(self, prefix: str = "n") -> str:
        self._n += 1
        return f"{prefix}{self._n}"

# ---------- Inline parsing ----------
# Ordre des patterns : du plus spécifique au plus général
# 1. **[text](url)** → bold + link
# 2. [**text**](url) → idem (variation d'ordre)
# 3. **text**         → bold seul
# 4. [text](url)      → link seul
# 5. *text*           → italic seul
# Motif d'URL partagé avec le garde-fou (cf. politique_liens.MOTIF_URL) : il
# tolère UN niveau de parenthèses internes, sans quoi
# `[wiki](https://fr.wikipedia.org/wiki/Loi_Badinter_(1985))` est tronqué au
# premier « ) » et le lien publié est cassé.
_URL = politique_liens.MOTIF_URL

INLINE_RE = re.compile(
    r"(\*\*\[[^\]]+\]\(" + _URL + r"\)\*\*)"  # **[link](url)**
    r"|(\[\*\*[^*]+\*\*\]\(" + _URL + r"\))"  # [**link**](url)
    r"|(\*\*[^*]+\*\*)"                       # bold
    r"|(\[[^\]]+\]\(" + _URL + r"\))"         # link
    r"|(\*[^*]+\*)"                           # italic
)

_LINK_INNER = re.compile(r"\[([^\]]+)\]\((" + _URL + r")\)")
_BOLD_LINK = re.compile(r"\*\*\[([^\]]+)\]\((" + _URL + r")\)\*\*")
_LINK_BOLD = re.compile(r"\[\*\*([^*]+)\*\*\]\((" + _URL + r")\)")


def parse_inline(text: str) -> list[dict]:
    """Convertit un fragment de texte en liste de TEXT nodes Ricos avec décorations."""
    nodes = []
    pos = 0
    for m in INLINE_RE.finditer(text):
        start, end = m.span()
        if start > pos:
            plain = text[pos:start]
            if plain:
                nodes.append(_text(plain))
        token = m.group(0)
        # 1. **[text](url)** → bold + link
        bl = _BOLD_LINK.match(token)
        if bl:
            txt, url = bl.group(1), bl.group(2)
            nodes.append(_text(txt, bold=True, link=url))
            pos = end
            continue
        # 2. [**text**](url) → bold + link
        lb = _LINK_BOLD.match(token)
        if lb:
            txt, url = lb.group(1), lb.group(2)
            nodes.append(_text(txt, bold=True, link=url))
            pos = end
            continue
        # 3. **text**
        if token.startswith("**") and token.endswith("**"):
            inner = token[2:-2]
            nodes.append(_text(inner, bold=True))
            pos = end
            continue
        # 4. [text](url)
        if token.startswith("["):
            ml = _LINK_INNER.match(token)
            if ml:
                txt, url = ml.group(1), ml.group(2)
                nodes.append(_text(txt, link=url))
                pos = end
                continue
        # 5. *text*
        if token.startswith("*") and token.endswith("*"):
            inner = token[1:-1]
            nodes.append(_text(inner, italic=True))
            pos = end
            continue
        # Fallback (ne devrait pas arriver)
        nodes.append(_text(token))
        pos = end
    if pos < len(text):
        plain = text[pos:]
        if plain:
            nodes.append(_text(plain))
    if not nodes:
        nodes.append(_text(text))
    return nodes


def _text(content: str, *, bold: bool = False, italic: bool = False, link: str | None = None) -> dict:
    decorations = []
    if bold:
        decorations.append({"type": "BOLD"})
    if italic:
        decorations.append({"type": "ITALIC"})
    if link:
        decorations.append({
            "type": "LINK",
            "linkData": _link_data(link),
        })
    return {
        "type": "TEXT",
        "id": "",
        "nodes": [],
        "textData": {"text": content, "decorations": decorations},
    }


# ---------- Node builders ----------
# Chaque constructeur reçoit l'allocateur d'ids du document en cours. L'ordre
# d'allocation est significatif : il fixe la numérotation des `ricos.min.json`
# déjà poussés en draft Wix — ne pas le réordonner.
def P(ids: _Ids, text: str | list[dict]) -> dict:
    if isinstance(text, str):
        children = parse_inline(text)
    else:
        children = text
    node = {
        "type": "PARAGRAPH",
        "id": ids("p"),
        "nodes": children,
        "paragraphData": {},
    }
    return node


def H(ids: _Ids, level: int, text: str, anchor: str | None = None) -> dict:
    return {
        "type": "HEADING",
        "id": anchor or ids("h"),
        "headingData": {"level": level},
        "nodes": parse_inline(text),
    }


def UL(ids: _Ids, items: list[str]) -> dict:
    list_items = []
    for it in items:
        list_items.append({
            "type": "LIST_ITEM",
            "id": ids("li"),
            "nodes": [{
                "type": "PARAGRAPH",
                "id": ids("p"),
                "nodes": parse_inline(it),
                "paragraphData": {},
            }],
        })
    return {
        "type": "BULLETED_LIST",
        "id": ids("ul"),
        "nodes": list_items,
    }


def OL(ids: _Ids, items: list[str]) -> dict:
    list_items = []
    for it in items:
        list_items.append({
            "type": "LIST_ITEM",
            "id": ids("li"),
            "nodes": [{
                "type": "PARAGRAPH",
                "id": ids("p"),
                "nodes": parse_inline(it),
                "paragraphData": {},
            }],
        })
    return {
        "type": "ORDERED_LIST",
        "id": ids("ol"),
        "nodes": list_items,
    }


def BQ(ids: _Ids, paras: list[str]) -> dict:
    children = []
    for p in paras:
        children.append({
            "type": "PARAGRAPH",
            "id": ids("p"),
            "nodes": parse_inline(p),
            "paragraphData": {},
        })
    return {
        "type": "BLOCKQUOTE",
        "id": ids("bq"),
        "nodes": children,
    }


def DIV(ids: _Ids) -> dict:
    return {
        "type": "DIVIDER",
        "id": ids("d"),
        "dividerData": {"lineStyle": "SINGLE", "width": "MEDIUM", "alignment": "CENTER"},
        "nodes": [],
    }


def FAQ(ids: _Ids, qa_pairs: list[tuple[str, list[str]]]) -> dict:
    """Construit un COLLAPSIBLE_LIST à partir de paires (question, paragraphes).

    La réponse est une LISTE de paragraphes : une réponse en plusieurs
    paragraphes restait auparavant hors de l'accordéon (les paragraphes 2+
    remontaient comme nœuds de premier niveau, avant la FAQ).
    """
    items = []
    for q, a in qa_pairs:
        paragraphs = [a] if isinstance(a, str) else list(a)
        if not paragraphs:
            paragraphs = [""]
        items.append({
            "type": "COLLAPSIBLE_ITEM",
            "id": ids("ci"),
            "collapsibleItemData": {},
            "nodes": [
                {
                    "type": "COLLAPSIBLE_ITEM_TITLE",
                    "id": ids("ct"),
                    "nodes": [{
                        "type": "PARAGRAPH",
                        "id": ids("p"),
                        "nodes": parse_inline(q),
                        "paragraphData": {},
                    }],
                },
                {
                    "type": "COLLAPSIBLE_ITEM_BODY",
                    "id": ids("cb"),
                    "nodes": [{
                        "type": "PARAGRAPH",
                        "id": ids("p"),
                        "nodes": parse_inline(par),
                        "paragraphData": {},
                    } for par in paragraphs],
                },
            ],
        })
    return {
        "type": "COLLAPSIBLE_LIST",
        "id": ids("cl"),
        "collapsibleListData": {"initialExpandedItems": "FIRST", "direction": "LTR", "expandOnlyOne": False},
        "nodes": items,
    }


# ---------- Markdown parser ----------
ANCHOR_RE = re.compile(r"\s*\{#([a-z0-9-]+)\}\s*$")

# Préfixes structurels à retirer des titres (marqueurs de plan, pas du contenu visible)
PREFIX_RE = re.compile(r"^H[23]\s*\d+(?:\.\d+)?\s*—\s*")

# Headings à totalement masquer (skip le titre, mais on garde le contenu qui suit)
HIDDEN_HEADINGS = {"intro", "cta final"}


def parse_markdown(md: str) -> list[dict]:
    """Parse markdown → liste de nœuds Ricos top-level.

    Fonction de sa seule entrée : l'allocateur d'ids naît et meurt ici, donc
    deux appels sur le même markdown rendent des nœuds identiques.
    """
    lines = md.split("\n")
    nodes: list[dict] = []
    ids = _Ids()

    i = 0
    in_faq_section = False
    faq_buffer: list[tuple[str, list[str]]] = []
    skip_notes = False  # quand on entre dans "## Notes méthodologiques", on skip tout

    def flush_faq():
        if faq_buffer:
            nodes.append(FAQ(ids, faq_buffer.copy()))
            faq_buffer.clear()

    while i < len(lines):
        if skip_notes:
            break
        line = lines[i].rstrip()

        # Skip blank
        if not line:
            i += 1
            continue

        # H1 → skip (le H1 va dans le title)
        if line.startswith("# ") and not line.startswith("## "):
            i += 1
            continue

        # H2
        if line.startswith("## "):
            txt = line[3:].strip()
            # extraire l'ancre éventuelle
            anchor = None
            m = ANCHOR_RE.search(txt)
            if m:
                anchor = m.group(1)
                txt = ANCHOR_RE.sub("", txt).strip()
            # Strip le préfixe structurel "H2 N — "
            txt = PREFIX_RE.sub("", txt).strip()

            # Détection "Notes méthodologiques" → skip tout ce qui suit
            if "Notes méthodologiques" in txt:
                skip_notes = True
                break

            # (Sommaire désormais converti normalement : H2 + liste de liens d'ancrage)

            # Headings cachés (Intro, CTA final…) : on skip le H2 mais on garde le contenu qui suit
            if txt.lower() in HIDDEN_HEADINGS:
                i += 1
                continue

            # Détection FAQ : "Questions fréquentes"
            if "Questions fréquentes" in txt or "FAQ" in txt.upper():
                in_faq_section = True
                nodes.append(DIV(ids))
                nodes.append(H(ids, 2, txt, anchor=anchor))
                i += 1
                # skip line "(format COLLAPSIBLE_LIST...)"
                while i < len(lines) and lines[i].strip().startswith("*("):
                    i += 1
                continue

            # H2 normal
            flush_faq()
            in_faq_section = False
            if nodes:  # ajouter un divider avant chaque H2 (sauf le 1er)
                nodes.append(DIV(ids))
            nodes.append(H(ids, 2, txt, anchor=anchor))
            i += 1
            continue

        # H3
        if line.startswith("### "):
            txt = line[4:].strip()
            # Anchor potentielle
            anchor = None
            m = ANCHOR_RE.search(txt)
            if m:
                anchor = m.group(1)
                txt = ANCHOR_RE.sub("", txt).strip()
            # Strip le préfixe structurel "H3 N.N — "
            txt_stripped = PREFIX_RE.sub("", txt).strip()
            if not in_faq_section:
                txt = txt_stripped

            if in_faq_section:
                # Le H3 est une question FAQ ; la réponse est TOUT ce qui suit
                # jusqu'à la prochaine question / section (plusieurs paragraphes
                # possibles — ils restaient auparavant hors de l'accordéon).
                question_clean = re.sub(r"^Q\d+\s*—\s*", "", txt)
                i += 1
                paragraphs: list[str] = []
                current: list[str] = []
                while i < len(lines):
                    stripped = lines[i].strip()
                    if stripped.startswith("#") or stripped == "---":
                        break
                    if not stripped:
                        if current:
                            paragraphs.append(" ".join(current))
                            current = []
                        i += 1
                        continue
                    current.append(stripped)
                    i += 1
                if current:
                    paragraphs.append(" ".join(current))
                faq_buffer.append((question_clean, paragraphs))
                continue

            # H3 normal
            nodes.append(H(ids, 3, txt, anchor=anchor))
            i += 1
            continue

        # Divider
        if line.strip() == "---":
            # Skip si déjà un divider précédemment
            if nodes and nodes[-1].get("type") != "DIVIDER":
                # On gère les dividers via les transitions H2 automatiquement.
                # Ici on l'ajoute uniquement si pas suivi immédiatement d'un H2
                next_non_blank = ""
                k = i + 1
                while k < len(lines) and not lines[k].strip():
                    k += 1
                if k < len(lines):
                    next_non_blank = lines[k]
                if not next_non_blank.startswith("## "):
                    nodes.append(DIV(ids))
            i += 1
            continue

        # Blockquote (> ...)
        if line.startswith(">"):
            bq_lines: list[str] = []
            while i < len(lines) and (lines[i].startswith(">") or (lines[i].strip().startswith(">"))):
                lcontent = re.sub(r"^>\s?", "", lines[i])
                bq_lines.append(lcontent)
                i += 1
            # Skip si c'est le bloc "Livrable Étape" ou similar (note de tête)
            full_bq = " ".join(bq_lines)
            if "Livrable Étape" in full_bq:
                continue
            # Segmenter le blockquote en paragraphes (blank line = nouveau para)
            paras: list[str] = []
            current = []
            for bl in bq_lines:
                if not bl.strip():
                    if current:
                        paras.append(" ".join(current).strip())
                        current = []
                else:
                    current.append(bl.strip())
            if current:
                paras.append(" ".join(current).strip())
            if paras:
                nodes.append(BQ(ids, paras))
            continue

        # Liste ordonnée (1. 2. 3.)
        if re.match(r"^\d+\.\s", line):
            ol_items: list[str] = []
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i]):
                item_text = re.sub(r"^\d+\.\s", "", lines[i]).strip()
                i += 1
                while i < len(lines) and lines[i].startswith("  "):
                    item_text += " " + lines[i].strip()
                    i += 1
                ol_items.append(item_text)
            nodes.append(OL(ids, ol_items))
            continue

        # Liste à puces
        if line.startswith("- "):
            items: list[str] = []
            while i < len(lines) and lines[i].startswith("- "):
                item_text = lines[i][2:].strip()
                # continuation possible (lignes indentées)
                i += 1
                while i < len(lines) and lines[i].startswith("  "):
                    item_text += " " + lines[i].strip()
                    i += 1
                items.append(item_text)
            nodes.append(UL(ids, items))
            continue

        # Sinon: paragraphe (peut être multi-ligne jusqu'à blank ou heading/list)
        para_lines = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i].rstrip()
            if not nxt:
                break
            if (nxt.startswith("#") or nxt.startswith("-") or nxt.startswith(">")
                    or nxt.strip() == "---" or re.match(r"^\d+\.\s", nxt)):
                break
            para_lines.append(nxt)
            i += 1
        para_text = " ".join(s.strip() for s in para_lines)
        nodes.append(P(ids, para_text))

    # Flush FAQ si on est encore dedans
    if in_faq_section:
        nodes.append(FAQ(ids, faq_buffer.copy()))

    return nodes


def rendre(md: str) -> dict:
    """Document Ricos complet — exactement ce qui est écrit dans `ricos.min.json`."""
    return {"nodes": parse_markdown(md)}


class Fraicheur(NamedTuple):
    a_jour: bool
    detail: str  # vide si à jour


def fraicheur(article_md: str, stocke: dict) -> Fraicheur:
    """Le Ricos stocké correspond-il encore à l'article ?

    C'est la question que pose le garde-fou, et c'est celle qui aurait évité de
    pousser le draft #10 sans son sommaire. Elle est répondue ici : l'appelant
    n'a plus à re-render lui-même ni à connaître les internes du module.
    """
    attendu = rendre(article_md)
    if stocke == attendu:
        return Fraicheur(True, "")
    n_stocke = len(stocke.get("nodes", []))
    n_attendu = len(attendu["nodes"])
    detail = (f"{n_stocke} nœuds stockés vs {n_attendu} régénérés"
              if n_stocke != n_attendu else "contenu divergent")
    return Fraicheur(False, detail)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_ricos.py <input.md>", file=sys.stderr)
        sys.exit(2)

    md_path = Path(sys.argv[1])
    md = md_path.read_text(encoding="utf-8")
    json.dump(rendre(md), sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
