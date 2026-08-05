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

Convention liens (LEARN-024) appliquée automatiquement par `_link_data` :
- interne (hostname == INTERNAL_DOMAIN ou sous-domaine, défaut « jplouton-avocat.fr »,
  URL relative « / », ancre « # ») → target SELF, sans rel
- externe → target BLANK + rel { nofollow, noopener, noreferrer }
La comparaison se fait sur le HOSTNAME parsé (pas par sous-chaîne).

Normalisation appliquée à chaque URL (`normalize_url`) :
- lien relatif « /… » → absolutisé sur INTERNAL_BASE (checklist TEMPLATE)
- accents → percent-encodés (idempotent : une URL déjà encodée ne l'est pas deux fois)
- ancre « #… » → laissée telle quelle

Surcharges d'environnement : RICOS_INTERNAL_DOMAIN, RICOS_INTERNAL_BASE.

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
import os
import re
import sys
import urllib.parse
from pathlib import Path

# Domaine considéré « interne » pour la convention rel (LEARN-024).
# Surchargeable via la variable d'environnement RICOS_INTERNAL_DOMAIN.
INTERNAL_DOMAIN = os.environ.get("RICOS_INTERNAL_DOMAIN", "jplouton-avocat.fr")
# Base utilisée pour absolutiser les liens internes écrits en relatif.
INTERNAL_BASE = os.environ.get("RICOS_INTERNAL_BASE", "https://www.jplouton-avocat.fr")


def _is_internal_host(url: str) -> bool:
    """Vrai si l'URL pointe vers le domaine interne — comparaison sur le HOSTNAME.

    Un test par sous-chaîne (`INTERNAL_DOMAIN in url`) classait « interne » toute
    URL externe contenant la chaîne (cache, annuaire, `not-jplouton-avocat.fr.x`),
    donc publiée en follow sans rel — violation silencieuse de LEARN-024.
    """
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    if not host:
        return False
    domain = INTERNAL_DOMAIN.lower()
    return host == domain or host.endswith("." + domain)


def _encode_non_ascii(url: str) -> str:
    """Percent-encode les caractères non-ASCII (accents) en laissant le reste intact.

    Idempotent : une URL déjà encodée (`%C3%A9`) n'est pas ré-encodée, contrairement
    à `quote()` qui transformerait `%` en `%25`.
    """
    out = []
    for ch in url:
        if ord(ch) < 128:
            out.append(ch)
        else:
            out.append("".join(f"%{b:02X}" for b in ch.encode("utf-8")))
    return "".join(out)


def normalize_url(url: str) -> str:
    """Normalise une URL de lien avant écriture dans le Ricos.

    - ancre `#…` : inchangée (lien intra-page)
    - chemin relatif `/…` : absolutisé sur INTERNAL_BASE (checklist TEMPLATE :
      « liens internes en URL absolue ») — c'était la source de la divergence
      entre #10 (absolu) et #11 (relatif)
    - accents : percent-encodés
    """
    url = url.strip()
    if url.startswith("#"):
        return url
    if url.startswith("/"):
        url = INTERNAL_BASE.rstrip("/") + url
    return _encode_non_ascii(url)


def _link_data(url: str) -> dict:
    """Convention rel (LEARN-024) : lien interne (domaine INTERNAL_DOMAIN, URL
    relative « / » ou ancre « # ») → target SELF sans rel ; lien externe →
    target BLANK + rel nofollow/noopener/noreferrer."""
    url = normalize_url(url)
    is_internal = url.startswith("#") or _is_internal_host(url)
    if is_internal:
        return {"link": {"url": url, "target": "SELF"}}
    return {"link": {"url": url, "target": "BLANK",
                     "rel": {"nofollow": True, "noopener": True, "noreferrer": True}}}


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
# URL tolérant UN niveau de parenthèses internes : sans cela
# `[wiki](https://fr.wikipedia.org/wiki/Loi_Badinter_(1985))` était tronqué au
# premier « ) » et le lien publié était cassé.
_URL = r"(?:[^()\s]|\([^()]*\))+"

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


def OL(items: list[str]) -> dict:
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
        "type": "ORDERED_LIST",
        "id": _id("ol"),
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


def FAQ(qa_pairs: list[tuple[str, list[str]]]) -> dict:
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
                        "nodes": parse_inline(par),
                        "paragraphData": {},
                    } for par in paragraphs],
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
HIDDEN_HEADINGS = {"intro", "cta final"}


def parse_markdown(md: str) -> list[dict]:
    """Parse markdown → liste de nœuds Ricos top-level."""
    lines = md.split("\n")
    nodes: list[dict] = []

    i = 0
    in_faq_section = False
    faq_buffer: list[tuple[str, list[str]]] = []
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

            # (Sommaire désormais converti normalement : H2 + liste de liens d'ancrage)

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
            nodes.append(OL(ol_items))
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
            if (nxt.startswith("#") or nxt.startswith("-") or nxt.startswith(">")
                    or nxt.strip() == "---" or re.match(r"^\d+\.\s", nxt)):
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
