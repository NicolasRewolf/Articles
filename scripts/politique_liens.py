"""
Politique de liens (LEARN-024) — source unique pour le RENDU et le CONTRÔLE.

Raison d'être : la règle « internes follow / externes nofollow + noreferrer »
existait en deux exemplaires. Le convertisseur la classait finement (comparaison
sur le hostname, pièges `webcache…/jplouton-avocat.fr/…` couverts par un test) ;
le garde-fou en contrôlait un *proxy* avec sa propre regex, et rejetait une
écriture (`](/mon-post)`) que le convertisseur absolutisait sans broncher.
Deux modules, deux verdicts sur le même lien.

Ici, un seul : `md_to_ricos` rend à travers ce module, `lint_pipeline` signale
à travers ce module.

Stdlib uniquement.

Surcharges d'environnement (noms historiques conservés) :
    RICOS_INTERNAL_DOMAIN — domaine considéré interne (défaut jplouton-avocat.fr)
    RICOS_INTERNAL_BASE   — base d'absolutisation des liens écrits en relatif
"""

from __future__ import annotations

import os
import urllib.parse
from typing import NamedTuple

DOMAINE_INTERNE = os.environ.get("RICOS_INTERNAL_DOMAIN", "jplouton-avocat.fr")
BASE_INTERNE = os.environ.get("RICOS_INTERNAL_BASE", "https://www.jplouton-avocat.fr")

INTERNE = "INTERNE"
EXTERNE = "EXTERNE"
ANCRE = "ANCRE"

# Motif d'URL d'un lien markdown, tolérant UN niveau de parenthèses internes :
# sans cela `[wiki](https://fr.wikipedia.org/wiki/Loi_Badinter_(1985))` est
# tronqué au premier « ) ». Partagé par le convertisseur et le garde-fou, pour
# qu'ils voient exactement le même ensemble de liens.
MOTIF_URL = r"(?:[^()\s]|\([^()]*\))+"
MOTIF_LIEN = r"\[[^\]]*\]\((" + MOTIF_URL + r")\)"

# Schémas qui ne décrivent pas une page du site : ni normalisés, ni contrôlés.
_SCHEMES_HORS_PAGE = ("mailto:", "tel:")


class Constat(NamedTuple):
    """Ce qui cloche dans un lien, tel qu'il est ÉCRIT dans le markdown.

    `gravite` vaut « erreur » ou « avertissement » : c'est la gravité par
    défaut de la règle. L'appelant reste libre de la rabaisser (articles
    legacy, p. ex.).
    """

    gravite: str
    message: str


def _hote(url: str) -> str:
    return (urllib.parse.urlparse(url).hostname or "").lower()


def est_hote_interne(url: str, domaine: str | None = None) -> bool:
    """Vrai si l'URL pointe vers le domaine interne — comparaison sur le HOSTNAME.

    Un test par sous-chaîne (`DOMAINE_INTERNE in url`) classait « interne » toute
    URL externe contenant la chaîne (cache, annuaire, `not-jplouton-avocat.fr.x`),
    donc publiée en follow sans rel — violation silencieuse de LEARN-024.
    """
    hote = _hote(url)
    if not hote:
        return False
    domaine = (domaine or DOMAINE_INTERNE).lower()
    return hote == domaine or hote.endswith("." + domaine)


def _encoder_non_ascii(url: str) -> str:
    """Percent-encode les caractères non-ASCII (accents), le reste intact.

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


def normaliser(url: str) -> str:
    """Normalise une URL avant écriture dans le Ricos.

    - ancre `#…` : inchangée (lien intra-page)
    - chemin relatif `/…` : absolutisé sur BASE_INTERNE (checklist TEMPLATE :
      « liens internes en URL absolue »)
    - accents : percent-encodés
    """
    url = url.strip()
    if url.startswith("#"):
        return url
    if url.startswith("/"):
        url = BASE_INTERNE.rstrip("/") + url
    return _encoder_non_ascii(url)


def classer(url: str) -> str:
    """ANCRE | INTERNE | EXTERNE, sur l'URL déjà normalisée."""
    if url.startswith("#"):
        return ANCRE
    return INTERNE if est_hote_interne(url) else EXTERNE


def attributs(url: str) -> dict:
    """Attributs de lien à publier, selon LEARN-024.

    Interne (ou ancre) → SELF, sans rel. Externe → BLANK + nofollow/noopener/noreferrer.
    """
    url = normaliser(url)
    if classer(url) in (ANCRE, INTERNE):
        return {"url": url, "target": "SELF"}
    return {
        "url": url,
        "target": "BLANK",
        "rel": {"nofollow": True, "noopener": True, "noreferrer": True},
    }


def constats(url_brute: str) -> list[Constat]:
    """Ce qui cloche dans un lien tel qu'il est écrit dans le markdown.

    Les messages ne contiennent PAS l'URL : l'appelant agrège par message et
    ajoute son propre exemple.
    """
    u = (url_brute or "").strip()
    if not u or u.startswith("#") or u.startswith(_SCHEMES_HORS_PAGE):
        return []

    trouves: list[Constat] = []

    if u.startswith("/"):
        trouves.append(Constat("erreur", "lien interne en relatif (attendu URL absolue)"))

    normalisee = normaliser(u)
    if classer(normalisee) == EXTERNE and DOMAINE_INTERNE.lower() in normalisee.lower():
        trouves.append(Constat(
            "avertissement",
            "URL contenant le domaine interne mais pointant vers un autre hôte — "
            "sera publiée en externe (nofollow), vérifier que c'est voulu",
        ))

    return trouves
