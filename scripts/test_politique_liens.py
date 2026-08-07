"""Tests stdlib de la politique de liens (LEARN-024).

Ces tests protègent désormais les DEUX callers : le convertisseur qui rend le
Ricos et le garde-fou qui signale. Avant, la finesse de classification n'était
couverte que du côté rendu.

Lancer : python3 scripts/test_politique_liens.py
"""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from scripts import politique_liens as pl  # noqa: E402


def test_classification_par_hostname():
    """Régression A-37 : une URL EXTERNE contenant la chaîne du domaine reste externe."""
    assert pl.classer("https://www.jplouton-avocat.fr/ok") == pl.INTERNE
    assert pl.classer("https://jplouton-avocat.fr/ok") == pl.INTERNE
    for piege in ("https://webcache.example.com/jplouton-avocat.fr/page",
                  "https://not-jplouton-avocat.fr.evil.example/p"):
        assert pl.classer(piege) == pl.EXTERNE, piege
    assert pl.classer("#ancre") == pl.ANCRE
    print("OK classer — hostname, pas sous-chaine ; ancre distinguee")


def test_normalisation():
    """Régressions A-38 (accents) et divergence #10/#11 (relatif vs absolu)."""
    assert pl.normaliser("/mon-post") == "https://www.jplouton-avocat.fr/mon-post"
    assert pl.normaliser("#sommaire") == "#sommaire"
    encode = "https://www.jplouton-avocat.fr/post/dossier-m%C3%A9dical"
    assert pl.normaliser("/post/dossier-médical") == encode
    assert pl.normaliser(encode) == encode, "le percent-encodage doit etre idempotent"
    print("OK normaliser — relatif absolutise, accents encodes une seule fois")


def test_attributs_rel():
    interne = pl.attributs("https://www.jplouton-avocat.fr/x")
    assert interne["target"] == "SELF" and "rel" not in interne, interne

    ancre = pl.attributs("#faq")
    assert ancre["target"] == "SELF" and "rel" not in ancre, ancre

    externe = pl.attributs("https://www.legifrance.gouv.fr/z")
    assert externe["target"] == "BLANK", externe
    assert externe["rel"] == {"nofollow": True, "noopener": True, "noreferrer": True}, externe
    print("OK attributs — interne SELF sans rel, externe BLANK + nofollow/noopener/noreferrer")


def test_constat_lien_relatif():
    """La règle que le garde-fou appliquait avec sa propre regex."""
    trouves = pl.constats("/mon-post")
    assert len(trouves) == 1, trouves
    assert trouves[0].gravite == "erreur", trouves
    assert "relatif" in trouves[0].message, trouves

    assert pl.constats("https://www.jplouton-avocat.fr/mon-post") == []
    assert pl.constats("https://www.legifrance.gouv.fr/z") == []
    print("OK constats — lien interne relatif = erreur, URL absolue = rien a dire")


def test_constat_piege_domaine():
    """Le contrôle que le garde-fou ne POUVAIT pas faire avant."""
    trouves = pl.constats("https://webcache.example.com/jplouton-avocat.fr/page")
    assert len(trouves) == 1, trouves
    assert trouves[0].gravite == "avertissement", trouves
    assert "autre hôte" in trouves[0].message, trouves
    print("OK constats — URL qui imite le domaine interne : signalee")


def test_constats_ignore_ancres_et_mailto():
    for u in ("#sommaire", "mailto:contact@example.fr", "tel:+33500000000", ""):
        assert pl.constats(u) == [], u
    print("OK constats — ancres, mailto et tel hors perimetre")


def test_motif_lien_tolere_les_parentheses():
    """Régression A-39 : l'URL était tronquée au premier « ) »."""
    import re
    md = "Voir [la loi](https://fr.wikipedia.org/wiki/Loi_Badinter_(1985)) ici."
    urls = re.findall(pl.MOTIF_LIEN, md)
    assert urls == ["https://fr.wikipedia.org/wiki/Loi_Badinter_(1985)"], urls
    print("OK motif — un niveau de parentheses internes tolere")


if __name__ == "__main__":
    test_classification_par_hostname()
    test_normalisation()
    test_attributs_rel()
    test_constat_lien_relatif()
    test_constat_piege_domaine()
    test_constats_ignore_ancres_et_mailto()
    test_motif_lien_tolere_les_parentheses()
    print("\nTOUS LES TESTS PASSENT")
