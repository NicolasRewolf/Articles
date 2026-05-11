"""
Markdown → Wix Ricos JSON converter (minimal, ad-hoc pour Cabinet Plouton).

Stdlib uniquement. Supporte :
- H2/H3 (avec ancres {#id})
- Paragraphes
- Listes à puces
- Blockquotes (multi-lignes)
- Dividers (---)
- Inline: **bold**, *italic*, [text](url)
- FAQ : H3 sous `## H2 6 — Questions fréquentes` → COLLAPSIBLE_LIST automatique

Exclusions par défaut :
- H1
- Sections marquées "## Notes méthodologiques" (et tout ce qui suit)
- Blockquote contenant "Livrable Étape" au début
- Section "## Sommaire" (traitée séparément si besoin)

Usage :
    python3 scripts/md_to_ricos.py <input.md> > out.json
"""

from __future__ import annotations

import json
import re
import sys
import uuid
from pathlib import Path

# ---------- Helpers id ----------
_counter = 0
def _id(prefix: str = "n") -> str:
    global _counter
    _counter += 1
    return f"{prefix}{_counter}"

# ---------- Inline parsing ----------
# Ordre des patterns : du plus spécifique au plus général
# 1. **[text](url)** → bold + link
# 2. [**text**](url) → idem (variation d'ordre)
# 3. **text**         → bold seul
# 4. [text](url)      → link seul
# 5. *text*           → italic seul
INLINE_RE = re.compile(
    r"(\*\*\[[^\]]+\]\([^)]+\)\*\*)"  # **[link](url)**
    r"|(\[\*\*[^*]+\*\*\]\([^)]+\))"  # [**link**](url)
    r"|(\*\*[^*]+\*\*)"               # bold
    r"|(\[[^\]]+\]\([^)]+\))"         # link
    r"|(\*[^*]+\*)"                   # italic
)

_LINK_INNER = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD_LINK = re.compile(r"\*\*\[([^\]]+)\]\(([^)]+)\)\*\*")
_LINK_BOLD = re.compile(r"\[\*\*([^*]+)\*\*\]\(([^)]+)\)")


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
            "linkData": {"link": {"url": link, "target": "BLANK"}},
        })
    return {
        "type": "TEXT",
        "id": "",
        "nodes": [],
        "textData": {"text": content, "decorations": decorations},
    }


# ---------- Node builders ----------
def P(text: str | list[dict], anchor: str | None = None) -> dict:
    if isinstance(text, str):
        children = parse_inline(text)
    else:
        children = text
    node = {
        "type": "PARAGRAPH",
        "id": _id("p"),
        "nodes": children,
        "paragraphData": {},
    }
    return node


def H(level: int, text: str, anchor: str | None = None) -> dict:
    return {
        "type": "HEADING",
        "id": anchor or _id("h"),
        "headingData": {"level": level},
        "nodes": parse_inline(text),
    }


def UL(items: list[str]) -> dict:
    list_items = []
    for it in items:
        list_items.append({
            "type": "LIST_ITEM",
            "id": _id("li"),
            "nodes": [{
                "type": "PARAGRAPH",
                "id": _id("p"),
                "nodes": parse_inline(it),
                "paragraphData": {},
            }],
        })
    return {
        "type": "BULLETED_LIST",
        "id": _id("ul"),
        "nodes": list_items,
    }


def BQ(paras: list[str]) -> dict:
    children = []
    for p in paras:
        children.append({
            "type": "PARAGRAPH",
            "id": _id("p"),
            "nodes": parse_inline(p),
            "paragraphData": {},
        })
    return {
        "type": "BLOCKQUOTE",
        "id": _id("bq"),
        "nodes": children,
    }


def DIV() -> dict:
    return {
        "type": "DIVIDER",
        "id": _id("d"),
        "dividerData": {"lineStyle": "SINGLE", "width": "MEDIUM", "alignment": "CENTER"},
        "nodes": [],
    }


def FAQ(qa_pairs: list[tuple[str, str]]) -> dict:
    """Construit un COLLAPSIBLE_LIST à partir de paires (question, réponse)."""
    items = []
    for q, a in qa_pairs:
        items.append({
            "type": "COLLAPSIBLE_ITEM",
            "id": _id("ci"),
            "collapsibleItemData": {},
            "nodes": [
                {
                    "type": "COLLAPSIBLE_ITEM_TITLE",
                    "id": _id("ct"),
                    "nodes": [{
                        "type": "PARAGRAPH",
                        "id": _id("p"),
                        "nodes": parse_inline(q),
                        "paragraphData": {},
                    }],
                },
                {
                    "type": "COLLAPSIBLE_ITEM_BODY",
                    "id": _id("cb"),
                    "nodes": [{
                        "type": "PARAGRAPH",
                        "id": _id("p"),
                        "nodes": parse_inline(a),
                        "paragraphData": {},
                    }],
                },
            ],
        })
    return {
        "type": "COLLAPSIBLE_LIST",
        "id": _id("cl"),
        "collapsibleListData": {"initialExpandedItems": "FIRST", "direction": "LTR", "expandOnlyOne": False},
        "nodes": items,
    }


# ---------- Markdown parser ----------
ANCHOR_RE = re.compile(r"\s*\{#([a-z0-9-]+)\}\s*$")

# Préfixes structurels à retirer des titres (marqueurs de plan, pas du contenu visible)
PREFIX_RE = re.compile(r"^H[23]\s*\d+(?:\.\d+)?\s*—\s*")

# Headings à totalement masquer (skip le titre, mais on garde le contenu qui suit)
HIDDEN_HEADINGS = {"intro", "cta final", "sommaire"}


def parse_markdown(md: str) -> list[dict]:
    """Parse markdown → liste de nœuds Ricos top-level."""
    lines = md.split("\n")
    nodes: list[dict] = []

    i = 0
    in_faq_section = False
    faq_buffer: list[tuple[str, str]] = []
    skip_notes = False  # quand on entre dans "## Notes méthodologiques", on skip tout

    def flush_faq():
        if faq_buffer:
            nodes.append(FAQ(faq_buffer.copy()))
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

            # Skip sommaire (déjà géré séparément)
            if "Sommaire" in txt or "sommaire" in txt.lower():
                # consommer jusqu'au prochain heading ou ---
                i += 1
                while i < len(lines) and not (lines[i].startswith("## ") or lines[i].startswith("---")):
                    i += 1
                continue

            # Headings cachés (Intro, CTA final…) : on skip le H2 mais on garde le contenu qui suit
            if txt.lower() in HIDDEN_HEADINGS:
                i += 1
                continue

            # Détection FAQ : "Questions fréquentes"
            if "Questions fréquentes" in txt or "FAQ" in txt.upper():
                in_faq_section = True
                nodes.append(DIV())
                nodes.append(H(2, txt, anchor=anchor))
                i += 1
                # skip line "(format COLLAPSIBLE_LIST...)"
                while i < len(lines) and lines[i].strip().startswith("*("):
                    i += 1
                continue

            # H2 normal
            flush_faq()
            in_faq_section = False
            if nodes:  # ajouter un divider avant chaque H2 (sauf le 1er)
                nodes.append(DIV())
            nodes.append(H(2, txt, anchor=anchor))
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
                # Le H3 est une question FAQ ; la réponse suit dans le prochain paragraphe
                # Récupérer le H3 comme question
                question = txt
                # Nettoyer le préfixe "Q1 — " etc.
                question_clean = re.sub(r"^Q\d+\s*—\s*", "", question)
                # Avancer
                i += 1
                # Skip blank
                while i < len(lines) and not lines[i].strip():
                    i += 1
                # Récupérer la réponse (un ou plusieurs paragraphes — on prend le premier)
                if i < len(lines) and lines[i].strip() and not lines[i].startswith("#"):
                    answer = lines[i].strip()
                    i += 1
                    # multi-line paragraph: continue while not blank and not #
                    while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and not lines[i].startswith("---"):
                        answer += " " + lines[i].strip()
                        i += 1
                    faq_buffer.append((question_clean, answer))
                else:
                    faq_buffer.append((question_clean, ""))
                continue

            # H3 normal
            nodes.append(H(3, txt, anchor=anchor))
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
                    nodes.append(DIV())
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
                nodes.append(BQ(paras))
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
            nodes.append(UL(items))
            continue

        # Sinon: paragraphe (peut être multi-ligne jusqu'à blank ou heading/list)
        para_lines = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i].rstrip()
            if not nxt:
                break
            if nxt.startswith("#") or nxt.startswith("-") or nxt.startswith(">") or nxt.strip() == "---":
                break
            para_lines.append(nxt)
            i += 1
        para_text = " ".join(s.strip() for s in para_lines)
        nodes.append(P(para_text))

    # Flush FAQ si on est encore dedans
    if in_faq_section:
        nodes.append(FAQ(faq_buffer.copy()))

    return nodes


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 md_to_ricos.py <input.md>", file=sys.stderr)
        sys.exit(2)

    md_path = Path(sys.argv[1])
    md = md_path.read_text(encoding="utf-8")
    nodes = parse_markdown(md)
    rich_content = {"nodes": nodes}
    json.dump(rich_content, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
