#!/usr/bin/env python3
"""
lint_pipeline.py — garde-fou mécanique du pipeline éditorial Plouton.

Raison d'être : une règle qui ne vit qu'en prose finit par dériver. La règle
« tags séparés par des virgules » a été violée sur 5 articles consécutifs avant
d'être outillée. Tout ce qui est vérifiable par une machine est vérifié ici.

Usage :
    python3 scripts/lint_pipeline.py                  # tout le repo
    python3 scripts/lint_pipeline.py 11-slug-article/ # un dossier d'article
    python3 scripts/lint_pipeline.py --strict         # les avertissements deviennent bloquants

Sortie : code 0 si aucune ERREUR, 1 sinon. Les AVERTISSEMENTS n'échouent pas
(sauf --strict) : ils signalent ce qui mérite un œil sans bloquer la livraison.

Stdlib uniquement.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts import md_to_ricos, politique_liens  # noqa: E402

# Documents de gouvernance soumis aux contrôles de forme.
DOCS = ["README.md", "BRIEF.md", "ARTICLE_TEMPLATE.md",
        "LEARNINGS.md", "LEARNINGS-archive.md"]

# Documents où un compteur figé ou une date en dur est interdit : ils dérivent
# à chaque digestion (audit 2026-08-05, issues A-03 / A-07 / A-19).
DOCS_SANS_COMPTEUR = ["README.md", "BRIEF.md", "ARTICLE_TEMPLATE.md"]

# Articles ANTÉRIEURS aux décisions du 2026-08-05 : contrôlés en avertissement
# seulement (politique repo « pas d'audit rétro » — ils sont publiés).
# Tout dossier absent de cette liste est ACTIF : ses écarts sont des ERREURS.
LEGACY = {
    "01-indemnisation-accident-moto",
    "02-indemnisation-chirurgie-esthetique-ratee",
    "03-arnaques-en-ligne",
    "04-indemnisation-accident-velo",
    "05-indemnisation-passager-accident",
    "07-indemnisation-victime-tetraplegique",
    "08-sinistre-habitation-assurance",
    "09-pension-alimentaire",
    "08-indemnisation-morsure-chien",  # gelé — réécriture prévue (décision 2026-08-05)
}

MAX_TITLE = 60
MAX_DESC = 155
FAQ_MIN, FAQ_MAX = 8, 10
TAGS_MIN, TAGS_MAX = 10, 15

ARTICLE_DIR_RE = re.compile(r"^\d{2}-[a-z0-9-]+$")


class Rapport:
    def __init__(self) -> None:
        self.erreurs: list[str] = []
        self.avertissements: list[str] = []

    def erreur(self, ou: str, msg: str) -> None:
        self.erreurs.append(f"{ou} — {msg}")

    def avertir(self, ou: str, msg: str) -> None:
        self.avertissements.append(f"{ou} — {msg}")

    def signaler(self, bloquant: bool, ou: str, msg: str) -> None:
        (self.erreur if bloquant else self.avertir)(ou, msg)


# --------------------------------------------------------------------------
# Helpers d'extraction (formats hétérogènes d'un article à l'autre)
# --------------------------------------------------------------------------

def _champ(texte: str, *noms: str) -> str | None:
    """Récupère `**Nom …** … : valeur` quelle que soit la ponctuation autour."""
    for nom in noms:
        motif = re.compile(
            r"^\s*[-*]?\s*\*\*" + nom + r"[^*]*\*\*[^:\n]*:\s*(.+?)\s*$",
            re.M | re.I,
        )
        m = motif.search(texte)
        if m:
            return m.group(1).strip().strip("`").strip()
    return None


def _section(texte: str, motif_titre: str) -> str | None:
    """Contenu d'une section `## …Titre…` jusqu'au prochain `##`.

    Le motif est cherché n'importe où dans la ligne de titre : les articles
    écrivent aussi bien « ## Questions fréquentes » que « ## H2 6 — Questions
    fréquentes » (préfixe structurel de plan).
    """
    m = re.search(r"^##+\s*.*" + motif_titre + r".*$", texte, re.M | re.I)
    if not m:
        return None
    suite = texte[m.end():]
    fin = re.search(r"^##\s", suite, re.M)
    return suite[: fin.start()] if fin else suite


def _hors_blocs_code(texte: str) -> str:
    """Retire les blocs de code : leurs placeholders ne sont pas de vrais liens."""
    return re.sub(r"^ {0,3}(`{3,}).*?^ {0,3}\1\s*$", "", texte, flags=re.S | re.M)


def _sans_accent(s: str) -> bool:
    return not any(unicodedata.combining(c) for c in unicodedata.normalize("NFD", s))


def _headings(md: str, niveau: int = 2) -> list[str]:
    return re.findall(r"^" + "#" * niveau + r"\s+(.+?)\s*$", md, re.M)


# --------------------------------------------------------------------------
# Contrôles — documents de gouvernance
# --------------------------------------------------------------------------

def verifier_fences(chemin: Path, rap: Rapport) -> None:
    """Fences CommonMark équilibrées (une fence imbriquée cassait le rendu du TEMPLATE)."""
    ouverte = None
    for n, ligne in enumerate(chemin.read_text().split("\n"), 1):
        m = re.match(r"^ {0,3}(`{3,})(.*)$", ligne)
        if not m:
            continue
        ticks, info = len(m.group(1)), m.group(2).strip()
        if ouverte is None:
            ouverte = (ticks, n)
        elif ticks >= ouverte[0] and not info:
            ouverte = None
    if ouverte:
        rap.erreur(chemin.name, f"bloc de code ouvert ligne {ouverte[1]} et jamais fermé "
                                f"(imbrication : utiliser 4 backticks pour la fence externe)")


def verifier_tables(chemin: Path, rap: Rapport) -> None:
    """Toutes les lignes d'une table doivent avoir le même nombre de cellules."""
    lignes = chemin.read_text().split("\n")
    bloc: list[tuple[int, str]] = []

    def controler(bloc):
        if len(bloc) < 2:
            return
        comptes = {}
        for n, l in bloc:
            comptes.setdefault(l.count("|"), []).append(n)
        if len(comptes) > 1:
            detail = " ; ".join(f"{k} pipes lignes {v[:3]}" for k, v in comptes.items())
            rap.erreur(chemin.name, f"table markdown mal formée ({detail})")

    for n, l in enumerate(lignes, 1):
        if l.strip().startswith("|"):
            bloc.append((n, l))
        else:
            controler(bloc)
            bloc = []
    controler(bloc)


def verifier_liens_fichiers(chemin: Path, rap: Rapport) -> None:
    """Les liens markdown relatifs pointent vers des fichiers existants."""
    for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", _hors_blocs_code(chemin.read_text())):
        cible = m.group(1).split("#")[0].strip()
        if not cible or cible.startswith(("http://", "https://", "mailto:", "~", "/")):
            continue
        if not (ROOT / cible).exists():
            rap.erreur(chemin.name, f"lien vers un fichier inexistant : {cible}")


def verifier_bilan_archive(rap: Rapport) -> None:
    """Le Bilan de l'archive doit correspondre au décompte réel de sa cartographie.

    Seul endroit du repo où un compteur est autorisé — parce qu'il est ici
    dérivé de la table qui le précède, et vérifié mécaniquement.
    """
    chemin = ROOT / "LEARNINGS-archive.md"
    if not chemin.exists():
        return
    texte = chemin.read_text()
    reel = {"promu": 0, "archivé": 0}
    for _, _, statut in re.findall(r"^\|\s*(LEARN-[\w-]+)\s*\|([^|]*)\|([^|]*)\|", texte, re.M):
        s = statut.replace("*", "").strip().upper()
        if s.startswith("PROMU"):
            reel["promu"] += 1
        elif "ARCHIVÉ" in s:
            reel["archivé"] += 1

    m = re.search(r"\*\*Bilan[^\n]*?\*\*\s*:\s*\*\*(\d+)\s+promus\*\*,\s*\*\*(\d+)\s+archivés\*\*", texte)
    if not m:
        rap.avertir("LEARNINGS-archive.md", "Bilan introuvable ou format non reconnu "
                                            "(attendu : « **N promus**, **M archivés** »)")
        return
    annonce = (int(m.group(1)), int(m.group(2)))
    if annonce != (reel["promu"], reel["archivé"]):
        rap.erreur("LEARNINGS-archive.md",
                   f"Bilan faux : annonce {annonce[0]} promus / {annonce[1]} archivés, "
                   f"la cartographie en compte {reel['promu']} / {reel['archivé']}")


def verifier_compteurs_figes(chemin: Path, rap: Rapport) -> None:
    """Compteurs et dates en dur : ils mentent dès la digestion suivante."""
    texte = chemin.read_text()
    motifs = [
        (r"\b\d+\s+learnings?\s+(?:promus|audités)", "compteur de learnings en dur"),
        (r"\b\d+\s+règles?\s+durables?", "compteur de règles mémoire en dur"),
        (r"\b\d+\s+(?:entrées|savoirs)\s+techniques?", "compteur d'entrées d'archive en dur"),
        (r"Derni[èe]re mise à jour\s*:\s*20\d\d-\d\d-\d\d", "date de mise à jour en dur"),
    ]
    for n, ligne in enumerate(texte.split("\n"), 1):
        for motif, libelle in motifs:
            if re.search(motif, ligne, re.I):
                rap.erreur(chemin.name, f"ligne {n} : {libelle} — renvoyer vers la source "
                                        f"(cartographie d'archive, mémoire, ou `git log`)")


# --------------------------------------------------------------------------
# Contrôles — dossier d'article
# --------------------------------------------------------------------------

def verifier_metadonnees(dossier: Path, bloquant: bool, rap: Rapport) -> None:
    fichier = dossier / "etape-4-metadonnees-wix.md"
    ou = f"{dossier.name}/{fichier.name}"
    if not fichier.exists():
        rap.signaler(bloquant, dossier.name, "livrable etape-4-metadonnees-wix.md manquant")
        return
    texte = fichier.read_text()

    titre = _champ(texte, "Titre SEO", "Méta-titre", "Meta title", "Titre")
    if titre is None:
        rap.signaler(bloquant, ou, "titre SEO introuvable")
    elif len(titre) > MAX_TITLE:
        rap.signaler(bloquant, ou, f"titre SEO : {len(titre)} caractères (max {MAX_TITLE})")

    desc = _champ(texte, "Meta description", "Méta-description", "Description")
    if desc is None:
        rap.signaler(bloquant, ou, "méta-description introuvable")
    elif len(desc) > MAX_DESC:
        rap.signaler(bloquant, ou, f"méta-description : {len(desc)} caractères (max {MAX_DESC})")

    slug = _champ(texte, "Slug")
    if slug is None:
        rap.signaler(bloquant, ou, "slug introuvable")
    elif not _sans_accent(slug):
        rap.signaler(bloquant, ou, f"slug accentué : {slug!r} (règle mémoire : slugs sans accent)")

    bloc_tags = _section(texte, r"Tags")
    if bloc_tags is None:
        rap.signaler(bloquant, ou, "section Tags introuvable")
    else:
        ligne = next((l.strip() for l in bloc_tags.split("\n")
                      if l.strip() and not l.strip().startswith(("*", ">", "-"))), "")
        if "·" in ligne:
            rap.signaler(bloquant, ou, "tags séparés par des middots « · » — "
                                       "règle mémoire : CSV (virgules) pour copier-coller direct")
        elif ligne:
            n = len([t for t in ligne.split(",") if t.strip()])
            if not (TAGS_MIN <= n <= TAGS_MAX):
                rap.signaler(bloquant, ou, f"{n} tags (attendu {TAGS_MIN}-{TAGS_MAX})")

    for motif, libelle in [(r"Cat[ée]gorie", "Catégories"), (r"Image", "Image hero"),
                           (r"(JSON-LD|Refresh)", "JSON-LD / Refresh")]:
        if _section(texte, motif) is None:
            rap.avertir(ou, f"section « {libelle} » absente (format 8 sections, décision 2026-08-05)")


def verifier_article(dossier: Path, bloquant: bool, rap: Rapport) -> None:
    fichier = dossier / "etape-4-article.md"
    ou = f"{dossier.name}/{fichier.name}"
    if not fichier.exists():
        rap.signaler(bloquant, dossier.name, "livrable etape-4-article.md manquant")
        return
    texte = fichier.read_text()

    # Politique de liens (LEARN-024) — jugée par le module qui rend le Ricos,
    # pas par une regex parallèle qui divergeait de lui.
    groupes: dict[str, tuple[str, int, str]] = {}
    for m in re.finditer(politique_liens.MOTIF_LIEN, _hors_blocs_code(texte)):
        url = m.group(1)
        for c in politique_liens.constats(url):
            gravite, n, exemple = groupes.get(c.message, (c.gravite, 0, url))
            groupes[c.message] = (gravite, n + 1, exemple)
    for message, (gravite, n, exemple) in groupes.items():
        detail = f"{n} lien(s) — {message} — ex. {exemple}"
        if gravite == "erreur":
            rap.signaler(bloquant, ou, detail)
        else:
            rap.avertir(ou, detail)

    # Bio auteur (E-E-A-T, LEARN-040)
    if "À propos de l'auteur" not in texte:
        rap.signaler(bloquant, ou, "bloc « À propos de l'auteur » absent (bio obligatoire, LEARN-040)")

    # Date de mise à jour visible (LEARN-043)
    if not re.search(r"(Derni[èe]re mise à jour|Mis à jour le)", texte, re.I):
        rap.signaler(bloquant, ou, "date de mise à jour visible absente (LEARN-043)")

    # Pas de bullets dans blockquote (LEARN-025)
    if re.search(r"^>\s*[-*]\s+", texte, re.M):
        rap.signaler(bloquant, ou, "liste à puces dans un blockquote (LEARN-025 : prose continue)")

    # FAQ : nombre, position, présence dans la TDM
    h2 = _headings(texte, 2)
    idx_faq = next((i for i, t in enumerate(h2)
                    if re.search(r"(questions fréquentes|FAQ)", t, re.I)), None)
    if idx_faq is None:
        rap.signaler(bloquant, ou, "aucun H2 de FAQ trouvé")
    else:
        bloc = _section(texte, r"(Questions fréquentes|FAQ)")
        n_q = len(_headings(bloc or "", 3))
        if not (FAQ_MIN <= n_q <= FAQ_MAX):
            rap.signaler(bloquant, ou, f"FAQ : {n_q} questions (attendu {FAQ_MIN}-{FAQ_MAX}, LEARN-044)")
        # Seuls un CTA final / une conclusion / la bio peuvent suivre la FAQ.
        apres_faq = h2[idx_faq + 1:]
        intrus = [t for t in apres_faq
                  if not re.search(r"(CTA|conclusion|propos de l'auteur|auteur)", t, re.I)]
        if intrus:
            rap.signaler(bloquant, ou, f"la FAQ doit être le dernier H2 de contenu ; "
                                       f"elle est suivie de « {intrus[0]} » (décision 2026-08-05)")
        # La signature / date de mise à jour clôt l'article : elle ne peut pas
        # précéder la FAQ (cas #11 : FAQ rejetée après la signature).
        m_date = re.search(r"(Derni[èe]re mise à jour|Mis à jour le)", texte, re.I)
        m_faq = re.search(r"^##+\s*.*(questions fréquentes|FAQ).*$", texte, re.M | re.I)
        if m_date and m_faq and m_date.start() < m_faq.start():
            rap.signaler(bloquant, ou, "la date de mise à jour / signature précède la FAQ — "
                                       "elle doit clore l'article (FAQ, puis CTA final, puis bio + date)")
        sommaire = _section(texte, r"Sommaire")
        if sommaire and not re.search(r"(questions fréquentes|FAQ)", sommaire, re.I):
            rap.signaler(bloquant, ou, "la FAQ est absente du sommaire (décision 2026-08-05)")

    # Sommaire : une entrée par H2 (hors H2 masqués Intro/CTA)
    sommaire = _section(texte, r"Sommaire")
    if sommaire is None:
        rap.signaler(bloquant, ou, "sommaire (TDM) absent")
    else:
        ancres = re.findall(r"\]\(#([a-z0-9-]+)\)", sommaire)
        cibles = re.findall(r"^##\s+.*\{#([a-z0-9-]+)\}", texte, re.M)
        for a in ancres:
            if a not in cibles:
                rap.signaler(bloquant, ou, f"lien de sommaire vers l'ancre #{a} sans H2 correspondant")

    # Mini-CTAs : blockquotes contenant un lien vers le site (heuristique → avertissement)
    blocs_cta = [b for b in re.findall(r"(?:^>.*\n?)+", texte, re.M)
                 if "jplouton-avocat.fr" in b]
    if len(blocs_cta) < 2:
        rap.avertir(ou, f"{len(blocs_cta)} mini-CTA(s) inline détecté(s) en blockquote "
                        f"(attendu 2 + 1 CTA final — décision 2026-08-05)")


def verifier_ricos(dossier: Path, bloquant: bool, rap: Rapport) -> None:
    """Le ricos poussé doit correspondre à la version courante de l'article.

    C'est ce contrôle qui aurait évité de pousser le draft #10 sans son sommaire.
    La comparaison elle-même appartient au convertisseur (`md_to_ricos.fraicheur`).
    """
    art = dossier / "etape-4-article.md"
    ricos = dossier / "ricos.min.json"
    ou = f"{dossier.name}/ricos.min.json"
    if not ricos.exists():
        if not LEGACY.intersection({dossier.name}):
            rap.avertir(dossier.name, "ricos.min.json absent (livrable Étape 4 depuis la décision 2026-08-05)")
        return
    if not art.exists():
        return
    try:
        stocke = json.loads(ricos.read_text())
    except json.JSONDecodeError as e:
        rap.erreur(ou, f"JSON invalide : {e}")
        return
    etat = md_to_ricos.fraicheur(art.read_text(encoding="utf-8"), stocke)
    if not etat.a_jour:
        rap.signaler(bloquant, ou, f"obsolète par rapport à etape-4-article.md ({etat.detail}) — "
                                   f"régénérer puis resynchroniser le draft Wix")


def verifier_livrables(dossier: Path, bloquant: bool, rap: Rapport) -> None:
    for nom in ["etape-1-cadrage.md", "etape-2-collecte.md", "etape-3-plan.md"]:
        if not (dossier / nom).exists():
            rap.signaler(bloquant, dossier.name, f"livrable {nom} manquant")


# --------------------------------------------------------------------------
# Contrôles — repo
# --------------------------------------------------------------------------

def verifier_repo(rap: Rapport) -> None:
    prefixes: dict[str, list[str]] = {}
    for d in sorted(ROOT.iterdir()):
        if d.is_dir() and ARTICLE_DIR_RE.match(d.name):
            prefixes.setdefault(d.name[:2], []).append(d.name)
    for num, noms in prefixes.items():
        if len(noms) > 1:
            gelés = [n for n in noms if n in LEGACY]
            msg = f"préfixe {num} utilisé par {len(noms)} dossiers : {', '.join(noms)}"
            if len(gelés) == len(noms):
                rap.avertir("repo", msg + " — collision connue et documentée (README §Exceptions)")
            else:
                rap.erreur("repo", msg + " — renuméroter avant publication")

    gitignore = ROOT / ".gitignore"
    if gitignore.exists() and ".env" not in gitignore.read_text():
        rap.erreur(".gitignore", "`.env` n'est pas ignoré — risque de fuite de credentials")


# --------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(description="Garde-fou mécanique du pipeline éditorial Plouton")
    p.add_argument("cible", nargs="?", help="dossier d'article à vérifier (défaut : tout le repo)")
    p.add_argument("--strict", action="store_true", help="les avertissements deviennent bloquants")
    args = p.parse_args()

    rap = Rapport()

    if args.cible:
        dossiers = [Path(args.cible).resolve()]
        if not dossiers[0].is_dir():
            print(f"Dossier introuvable : {args.cible}", file=sys.stderr)
            return 2
    else:
        dossiers = [d for d in sorted(ROOT.iterdir())
                    if d.is_dir() and ARTICLE_DIR_RE.match(d.name)]
        for nom in DOCS:
            chemin = ROOT / nom
            if not chemin.exists():
                rap.erreur(nom, "document de gouvernance manquant")
                continue
            verifier_fences(chemin, rap)
            verifier_tables(chemin, rap)
            verifier_liens_fichiers(chemin, rap)
            if nom in DOCS_SANS_COMPTEUR:
                verifier_compteurs_figes(chemin, rap)
        verifier_bilan_archive(rap)
        verifier_repo(rap)

    for d in dossiers:
        bloquant = d.name not in LEGACY
        verifier_livrables(d, bloquant, rap)
        verifier_metadonnees(d, bloquant, rap)
        verifier_article(d, bloquant, rap)
        verifier_ricos(d, bloquant, rap)

    for msg in rap.avertissements:
        print(f"  AVERTISSEMENT  {msg}")
    for msg in rap.erreurs:
        print(f"  ERREUR         {msg}")

    n_e, n_a = len(rap.erreurs), len(rap.avertissements)
    print(f"\n{n_e} erreur(s), {n_a} avertissement(s).")
    if n_e == 0 and (n_a == 0 or not args.strict):
        print("Lint OK.")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
