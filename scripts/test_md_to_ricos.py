"""Tests stdlib pour md_to_ricos.py.

Lancer : python3 scripts/test_md_to_ricos.py
(aucune dépendance ; exit 0 si tout passe)
"""
from __future__ import annotations

import importlib.util
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("md2ricos", HERE / "md_to_ricos.py")
m = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(m)


def _of_type(nodes, t):
    return [n for n in nodes if n.get("type") == t]


def _links(node):
    found = []

    def walk(n):
        if isinstance(n, dict):
            for d in n.get("textData", {}).get("decorations", []):
                if d.get("type") == "LINK":
                    found.append(d["linkData"]["link"])
            for v in n.values():
                walk(v)
        elif isinstance(n, list):
            for x in n:
                walk(x)

    walk(node)
    return found


def test_ordered_list():
    md = (
        "## Section\n\n"
        "Phrase avant la liste.\n\n"
        "1. **Un.** Texte un.\n"
        "2. **Deux.** Texte deux.\n"
        "3. **Trois.** Texte trois.\n\n"
        "Phrase apres la liste.\n"
    )
    nodes = m.parse_markdown(md)
    ols = _of_type(nodes, "ORDERED_LIST")
    assert len(ols) == 1, f"attendu 1 ORDERED_LIST, obtenu {len(ols)}"
    items = ols[0]["nodes"]
    assert len(items) == 3, f"attendu 3 LIST_ITEM, obtenu {len(items)}"
    assert all(it["type"] == "LIST_ITEM" for it in items)
    # pas de run-on paragraphe avec '1. ' inline
    assert not any("1. " in (t.get("textData", {}) or {}).get("text", "")
                   for n in _of_type(nodes, "PARAGRAPH") for t in n["nodes"]), "run-on '1.' detecte"
    print("OK ordered_list — 1 ORDERED_LIST a 3 LIST_ITEM, aucun run-on")


def test_bulleted_still_works():
    nodes = m.parse_markdown("## S\n\n- a\n- b\n")
    uls = _of_type(nodes, "BULLETED_LIST")
    assert len(uls) == 1 and len(uls[0]["nodes"]) == 2, "BULLETED_LIST cassee"
    print("OK bulleted_list — toujours fonctionnel (regression)")


def test_rel_convention():
    md = (
        "## S\n\n"
        "Un [interne absolu](https://www.jplouton-avocat.fr/x), "
        "un [interne relatif](/y) et "
        "un [externe](https://www.legifrance.gouv.fr/z).\n"
    )
    nodes = m.parse_markdown(md)
    by_url = {l["url"]: l for l in _links(nodes[-1])}

    abs_int = by_url["https://www.jplouton-avocat.fr/x"]
    assert abs_int["target"] == "SELF" and "rel" not in abs_int, abs_int

    rel_int = by_url["/y"]
    assert rel_int["target"] == "SELF" and "rel" not in rel_int, rel_int

    ext = by_url["https://www.legifrance.gouv.fr/z"]
    assert ext["target"] == "BLANK", ext
    assert ext["rel"] == {"nofollow": True, "noopener": True, "noreferrer": True}, ext
    print("OK rel — interne=SELF/sans-rel, externe=BLANK+nofollow/noopener/noreferrer")


def test_sommaire_et_ancres():
    md = (
        "## Sommaire\n\n"
        "- [Définition](#definition)\n"
        "- [Procédure](#procedure)\n\n"
        "## Définition {#definition}\n\n"
        "Texte un.\n\n"
        "## Procédure {#procedure}\n\n"
        "Texte deux.\n"
    )
    nodes = m.parse_markdown(md)
    headings = _of_type(nodes, "HEADING")
    titles = ["".join(t["textData"]["text"] for t in h["nodes"]) for h in headings]
    assert "Sommaire" in titles, f"titre Sommaire absent (non converti): {titles}"
    ids = {h["id"] for h in headings}
    assert "definition" in ids and "procedure" in ids, f"ancres cibles manquantes sur les H2: {ids}"
    assert _of_type(nodes, "BULLETED_LIST"), "sommaire non converti en liste"
    anchor_links = [l for l in _links(nodes) if l["url"].startswith("#")]
    assert len(anchor_links) == 2, f"attendu 2 liens d'ancrage, obtenu {len(anchor_links)}"
    assert all(l["target"] == "SELF" and "rel" not in l for l in anchor_links), anchor_links
    print("OK sommaire — H2 conservé, ancres posées sur les H2, liens #ancre internes SELF")


if __name__ == "__main__":
    test_ordered_list()
    test_bulleted_still_works()
    test_rel_convention()
    test_sommaire_et_ancres()
    print("\nTOUS LES TESTS PASSENT")
