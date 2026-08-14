# Métadonnées Wix Studio — Article #14

> À coller dans le panneau SEO Wix Studio. Slug sans accent. 2 catégories systématiques.

## 1. Panneau SEO Wix Studio

- **H1 (titre de l'article)** : Cour criminelle départementale : ce que la loi du 23 juillet 2026 change pour les victimes de viol
- **Titre SEO (≤60)** : Cour criminelle départementale : la réforme 2026 | Plouton
- **Slug** : `cour-criminelle-departementale-victimes-viol`
- **URL publiée** : `https://www.jplouton-avocat.fr/post/cour-criminelle-departementale-victimes-viol`
- **Meta description (≤155)** : La loi du 23 juillet 2026 étend la compétence de la cour criminelle départementale. Ce qui change pour les victimes de viol, expliqué par un avocat.
- **Excerpt / chapô** : Depuis le 25 juillet 2026, cette cour de cinq magistrats sans jury juge aussi les crimes commis en récidive. Ce que la loi change pour vous, texte à l'appui.

## 2. Catégories Wix (2)

- **Ressources et notions juridiques** — `9477320f-5902-40e9-ace3-b0e3b6b8b51f`
- **Victimes de délits ou crimes** — `a755253f-65a6-49cc-b89e-e10e83840a75`

## 3. Tags (14, séparés par des virgules)

cour criminelle départementale, cour d'assises, viol, victime de viol, partie civile, loi 23 juillet 2026, procès criminel, jury populaire, justice restaurative, aide juridictionnelle, détention provisoire, avocat victime, Bordeaux, Nouvelle-Aquitaine

## 4. Image hero

- **Visuel** : une salle d'audience vide, bancs et estrade, lumière naturelle et cadrage large. Registre sobre et institutionnel. Sources libres : Unsplash / Pexels (« courtroom », « tribunal », « palais de justice »).
- **À proscrire absolument** : toute image évoquant une agression, une silhouette recroquevillée, une main tendue dans l'ombre, ou un visage flouté. Le sujet impose la retenue — l'illustration porte sur la juridiction, jamais sur les faits.
- **Alt text** : `Salle d'audience d'une cour criminelle départementale, où sont jugés les crimes punis de quinze ou vingt ans de réclusion`

## 5. Carte des liens

**Internes** (pas de `rel`, pas de `target` — appliqué automatiquement par `md_to_ricos.py`) :

| Cible | Section |
|---|---|
| `/honoraires-rendez-vous` | Mini-CTA #1 + CTA final |
| `/indemnisation-des-victimes/victimes-de-delits-ou-crimes` | H2 5 (encadré) |
| `/defense-penale/proces-criminel` | H2 3 |
| `/post/mis-en-cause-temoin-assiste-prevenu-accuse-differences` | H2 1 |
| `/post/réforme-de-la-prescription-pénale-…` | H2 1 |
| `/post/dépôt-de-plainte-en-france-…` | H2 5.1 |
| `/post/itt-pénale-définition-en-2025` | H2 5.2 |
| `/post/indemnisation-civi-2025-…` | H2 5.3 |
| `/post/sarvi-ou-civi-indemnisation-victimes` | H2 5.3 |
| `/post/proposition-de-loi-inceste-et-imprescriptibilité-…` | Bio auteur |

**Externes** (`target="_blank" rel="noopener noreferrer nofollow"`, appliqué automatiquement) : Légifrance (loi n° 2026-651, loi organique n° 2026-650, art. 181-1, art. 380-17, art. 10-1-1, section CCD), Conseil constitutionnel (décision n° 2026-909 DC), Assemblée nationale (rapport n° 1687).

🔴 **Avant publication** : tester tous les liens internes en HTTP (anti-404). Les slugs accentués sont des slugs publiés réels, percent-encodés par le parser.

## 6. JSON-LD FAQPage

**Livré dans le chat** (bloc `<script type="application/ld+json">` minifié one-liner), à coller dans le champ « Marquage structuré » du panneau SEO Wix Studio. Pas de fichier séparé. FAQPage uniquement — Person et LegalService sont gérés au niveau du site.

## 7. Push Wix

- **Statut** : `UNPUBLISHED` (draft), jamais publié sans ordre explicite.
- **`draftPostId`** : *(à renseigner après le push)*
- **Garde-fou** : contrôler `nodes.length` et `faqCount` avant POST, puis vérifier par `GET …/draft-posts/{id}`.

## 8. Refresh

**Échéance M+6 : février 2027.**

Déclencheurs de fond spécifiques à cet article — l'un suffit à commander une réécriture :

- **1ᵉʳ janvier 2027** : entrée en vigueur de l'art. 15-3-2-2 CPP (information sur l'avocat dès la plainte). L'article passe alors du futur au présent.
- **23 octobre 2026** : entrée en vigueur de l'article 9 de la loi.
- Sort du volet organique : si un avocat honoraire peut siéger comme assesseur en CCD, le H2 3 change.
- Première jurisprudence de cassation sur la compétence élargie (base Judilibre vide à ce jour).
- Publication de données post-2023 sur l'activité des CCD (ministère de la Justice / DSED).
- Horizon 2029 : recodification du code de procédure pénale — tous les articles cités portent `ABROGE_DIFF` au 1ᵉʳ janvier 2029.
