"""Tests stdlib de la sélection de version Légifrance.

Ces tests couvrent le geste le plus dangereux du wrapper : **choisir laquelle des
versions successives d'un article de code on va citer**. Se tromper ici ne
produit pas une erreur visible, mais un verbatim faux dans un article publié.

Régression fondatrice (article #12, 2026-08-07) : l'art. 222-22 du code pénal,
réécrit par la loi n° 2025-1057 du 6 novembre 2025, était rendu avec la mention
« PAS EN VIGUEUR » alors qu'il s'appliquait bel et bien. Cause : la sélection
comparait le libellé `legalStatus` à la chaîne « VIGUEUR », or la version
applicable portait `ABROGE_DIFF` — c'est-à-dire « abrogation déjà programmée au
2029-01-01 » (recodification du CPP par l'ordonnance du 19 novembre 2025), et
non « plus applicable ». La sélection se fait désormais sur les bornes de dates.

Aucun appel réseau : on teste les fonctions pures.

Lancer : python3 scripts/test_legifrance.py
"""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from scripts import legifrance as lf  # noqa: E402

# 2025-11-08 et 2029-01-01 en millisecondes (le format que rend l'API DILA).
MS_2025_11_08 = 1762560000000
MS_2029_01_01 = 1861920000000


def test_en_date_accepte_les_deux_formats():
    """L'API rend tantôt un timestamp ms, tantôt une date ISO."""
    assert lf._en_date(MS_2025_11_08) == "2025-11-08"
    assert lf._en_date("2025-11-08") == "2025-11-08"
    assert lf._en_date("2025-11-08T00:00:00.000Z") == "2025-11-08"
    for vide in (None, "", "pas une date", object()):
        assert lf._en_date(vide) == "", vide
    print("OK _en_date — timestamp ms, ISO, et valeurs illisibles neutralisees")


def test_abroge_diff_reste_en_vigueur():
    """Régression #12 : le libellé ne décide pas, les bornes décident."""
    art_222_22 = {"etat": "ABROGE_DIFF",
                  "dateDebut": MS_2025_11_08, "dateFin": MS_2029_01_01}
    assert lf._en_vigueur_le(art_222_22, "2026-08-07") is True
    assert lf._en_vigueur_le(art_222_22, "2025-11-08") is True   # borne basse incluse
    assert lf._en_vigueur_le(art_222_22, "2025-11-07") is False  # veille de l'entrée en vigueur
    assert lf._en_vigueur_le(art_222_22, "2029-01-01") is False  # borne haute exclue
    print("OK _en_vigueur_le — ABROGE_DIFF applicable, bornes [debut, fin[")


def test_version_future_pas_encore_applicable():
    """Le pendant : `VIGUEUR_DIFF` ne s'applique pas avant sa date de début."""
    future = {"etat": "VIGUEUR_DIFF", "dateDebut": MS_2029_01_01, "dateFin": None}
    assert lf._en_vigueur_le(future, "2026-08-07") is False
    assert lf._en_vigueur_le(future, "2029-06-01") is True
    print("OK _en_vigueur_le — VIGUEUR_DIFF inapplicable avant sa date de debut")


def test_sans_date_debut_jamais_retenu():
    """Pas de date de début exploitable ⇒ on ne peut rien affirmer."""
    assert lf._en_vigueur_le({"etat": "VIGUEUR"}, "2026-08-07") is False
    assert lf._en_vigueur_le({}, "2026-08-07") is False
    print("OK _en_vigueur_le — absence de dateDebut = non retenu")


def test_ordre_vigueur_puis_plus_recent():
    """Le chemin rapide est préservé : une VIGUEUR explicite passe en tête."""
    candidats = {
        "OLD": ("Code pénal", "MODIFIE", "2021-04-23"),
        "NEW": ("Code pénal", "MODIFIE", "2025-11-08"),
        "ENV": ("Code pénal", "VIGUEUR", "2018-08-06"),
    }
    assert lf._ordonner_candidats(candidats)[0] == "ENV"
    print("OK _ordonner_candidats — VIGUEUR en tete malgre une date plus ancienne")


def test_ordre_sans_vigueur_prend_la_plus_recente():
    """Cas #12 : aucune VIGUEUR — la plus récente devient la tête de l'ordre."""
    candidats = {
        "V2021": ("Code pénal", "MODIFIE", "2021-04-23"),
        "V2025": ("Code pénal", "ABROGE_DIFF", "2025-11-08"),
        "V2010": ("Code pénal", "MODIFIE", "2010-07-11"),
    }
    assert lf._ordonner_candidats(candidats) == ["V2025", "V2021", "V2010"]
    print("OK _ordonner_candidats — a defaut de VIGUEUR, date de version decroissante")


if __name__ == "__main__":
    test_en_date_accepte_les_deux_formats()
    test_abroge_diff_reste_en_vigueur()
    test_version_future_pas_encore_applicable()
    test_sans_date_debut_jamais_retenu()
    test_ordre_vigueur_puis_plus_recent()
    test_ordre_sans_vigueur_prend_la_plus_recente()
    print("\nTOUS LES TESTS PASSENT")
