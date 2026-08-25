# Métadonnées Wix — Article #16 : contre-expertise d'assurance

## 1. SEO

- **H1** : Contre-expertise d'assurance : contester le rapport de l'expert et faire réévaluer votre indemnisation
- **Méta-titre** : Contre-expertise assurance : contester le rapport
- **Méta-description** : L'expert est mandaté par votre assureur. Contre-expertise, tierce expertise, référé : ce que chaque voie vaut devant le juge. Avocat à Bordeaux.
- **Slug** : contre-expertise-assurance-contester-rapport-expert

*(Comptages : titre 49 ≤ 60 ; description 144 ≤ 155 ; slug ASCII pur.)*

## 2. Catégories Wix (2)

- Ressources et notions juridiques — `9477320f-5902-40e9-ace3-b0e3b6b8b51f` *(publication)*
- Droit des assurances — `edd6c343-05a3-4bf9-929e-527fad068557` *(thématique)*

## 3. Tags

contre-expertise, expertise d'assurance, expert d'assuré, expertise contradictoire, tierce expertise, expertise judiciaire, référé article 145, rapport d'expertise, sous-indemnisation, expertise médicale, médecin expert, litige assurance, Bordeaux

*(13 tags, séparés par des virgules — copier-coller direct dans Wix.)*

## 4. Image hero + alt

- **Brief image** : photo sobre et réaliste d'une scène d'expertise après sinistre — un expert en veste, mètre ou tablette à la main, relevant des dégâts dans un intérieur (mur taché, plafond marqué), lumière naturelle. Le cadrage doit montrer **l'assuré en retrait**, spectateur de l'évaluation : c'est le sujet de l'article. Éviter les visuels d'assurance génériques (poignée de main, parapluie, maquette de maison) et les mises en scène dramatiques.
- **Alt** : Expert mandaté par l'assurance relevant des dégâts dans un logement, sous le regard de l'assuré

**Open Graph** — og:title : Contre-expertise d'assurance : contester le rapport de l'expert · og:description : L'expert est choisi et payé par votre assureur. Ce que vaut chaque type d'expertise devant le juge, et comment faire réévaluer votre indemnisation. · og:image : image hero 1200×630 · og:type : article

## 5. Carte des liens

**Internes (13)** — pages : `/droit-des-contrats-et-des-personnes/droit-assurances-particuliers-professionnels`, `/indemnisation-des-victimes/accidents-de-la-route`, `/honoraires-rendez-vous` (×3 : mini-CTA, conclusion, bio), `/notre-cabinet`. Ressources : `sinistre-habitation-recours-assurance` (×2), `assurance-perte-exploitation-refus-calcul-recours`, `comment-bien-préparer-mon-dossier-médical`, `le-pretium-doloris-guide-complet-pour-les-victimes-d-accidents`, `loi-badinter-85-comprendre-vos-droits-à-indemnisation-après-un-accident-de-la-route`. Affaire cabinet : `victime-d-accident-de-la-circulation-et-tétraplégie-indemnisation-complémentaire-de-plus-de-500-00`.

Tous testés en HTTP 200 au Bloc C (LEARN-057). Pas de `rel`, pas de `target` sur les internes.

**Externes (11)** — Légifrance (art. 145 CPC, L. 114-1, L. 125-2, L. 211-9, L. 211-10, L. 211-13, arrêts 11-18.710 et 23-22.803), Service-Public F3075 (×2), Médiation de l'Assurance (PDF). Tous en `target="_blank" rel="noopener noreferrer nofollow"`.

## 6. JSON-LD FAQPage

Livré dans le chat en bloc `<script type="application/ld+json">` minifié one-liner (LEARN-027 + LEARN-041) → coller dans le champ « Marquage structuré » du panneau SEO Wix Studio. **FAQPage uniquement** : Person et LegalService sont gérés au niveau du site, ne pas dupliquer.

## 7. Push Wix

`ricos.min.json` — 74 nœuds, 9 questions de FAQ, 53 Ko. Draft **`UNPUBLISHED`**, scope SITE, `memberId` `07454f1f-…`, `seoSlug` réglé, 2 `categoryIds`.

⚠️ **53 Ko dépasse le seuil de transport observé** (LEARN-073 : #12 bloqué à 51 Ko). Compaction sémantique avant envoi si l'embarquement échoue — retrait de `id:""`, `nodes:[]`, `decorations:[]`, `paragraphData:{}`, contrôle par égalité des nœuds de texte. `ricos.min.json` reste la forme canonique attendue par le lint.

## 8. Refresh (M+6 : février 2027)

- **Cass. civ. 3e, 8 janvier 2026, n° 23-22.803** : surveiller une **confirmation en matière assurantielle** de la solution rendue en construction. Si un arrêt statue sur une clause de tierce expertise d'un contrat d'assurance, la réserve de transposition du H2 3 tombe et la section se réécrit en affirmation.
- **La Médiation de l'Assurance** : rapport 2025 attendu vers août 2026, puis 2026 vers août 2027 → mettre à jour l'encadré chiffré (saisines, part « contestation d'expertise »).
- **Code des assurances, art. L. 125-2** : version en vigueur depuis le 28 mai 2026 — vérifier qu'aucune modification n'est intervenue sur les délais CatNat.
- **Décret n° 2025-619 du 8 juillet 2025** (compétence exclusive du tribunal du lieu de l'immeuble, art. 145 CPC) : guetter les premières décisions d'application.
- **Cass. civ. 1re, 15 octobre 2025, n° 24-15.281** (exception du fait établi et non discuté) : suivre son éventuelle extension.

## 9. Mesure M+3

**Mesure M+3 : à programmer trois mois après la première impression GSC** (jamais à partir de la date de publication Wix — antidatable).

- Requête d'entrée à relever en priorité : `contre expertise assurance` (état « problème en cours », qualification Étape 1).
- Titres porteurs à contrôler : *Demander une expertise judiciaire : le référé de l'article 145* (cluster 3 160/mo), *Faut-il prendre un expert d'assuré ?* (2 170/mo), *Les quatre statuts d'expertise* (1 940/mo).
- Point de vigilance : vérifier si le H2 « expert d'assuré » capte **sans convertir** — c'est la condition posée à l'Étape 1 pour arbitrer un article dédié, ou pour conclure que le head term à 1 300/mo n'était pas le nôtre.
