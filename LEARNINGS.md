# LEARNINGS — Journal vivant du pipeline

> Capture chaude post-article. **N'accumule pas indéfiniment** : les learnings stabilisés sont **promus** vers `BRIEF.md` ou `ARTICLE_TEMPLATE.md`, et leur historique est conservé dans `LEARNINGS-archive.md`.
>
> **Cycle de digestion** : avant chaque nouvel article (à partir du #5), revue rapide de ce fichier. Tout ce qui est confirmé sur 2 articles distincts + opérationnel + non encore promu → on l'écrit dans BRIEF/TEMPLATE et on déplace ici dans `LEARNINGS-archive.md`.
>
> **Dernière digestion : 2026-06-01** (post article #6, passager) — LEARN-020 promu (BRIEF §4 Bloc D), LEARN-META-2 tranché (option b : cible 2 000-2 500 maintenue + passe de compression industrialisée, BRIEF §4 Étape 4 + TEMPLATE), LEARN-META-1 dédupliqué et retiré de l'actif. Digestions antérieures : 2026-05-13 (post #4, cycliste) + ingestion LEARN-053 le 2026-05-16 (Doctrine Google AI Search 2026). 51 learnings promus vers BRIEF/TEMPLATE, 7 archivés comme savoirs techniques/stratégiques. Voir [`LEARNINGS-archive.md`](LEARNINGS-archive.md) pour l'historique complet et la cartographie des destinations.

---

## Critère de promotion (rappel)

Un learning est **promu** vers BRIEF.md ou ARTICLE_TEMPLATE.md quand il remplit **au moins 2 conditions sur 3** :

1. **Confirmé** sur au moins 2 articles distincts (pattern, pas anomalie d'un cas).
2. **Opérationnel** (règle ou méthode, pas observation philosophique).
3. **Inutile à lire 2 fois** s'il vit déjà dans le brief ou le template.

Sinon : reste ici jusqu'à confirmation ou abandon.

**Destinations** :

| Type de learning | Destination |
|---|---|
| Règle business + workflow + ton + outils | `BRIEF.md` |
| Pattern structurel d'article + checklist qualité | `ARTICLE_TEMPLATE.md` |
| Savoir technique récurrent OU principe stratégique | `LEARNINGS-archive.md` (référence consultable) |
| Observation fraîche non encore stabilisée | reste ici, dans **LEARNINGS actifs** ci-dessous |

---

## LEARNINGS actifs (en attente de confirmation ou de digestion)

### LEARN-054 — Judilibre PROD via PISTE = source de référence pour la jurisprudence Cass.

**Constat article #6** : la sandbox PISTE est limitée (token sandbox + recherches partielles) ; **Judilibre PROD** donne accès à : verbatims complets des arrêts, vérification des n° de pourvoi, recherche d'arrêts récents (2018-2025) qui solidifient la doctrine ancienne. Sur l'article #6, a permis d'ajouter Civ. 2ᵉ 28 mars 2019 n° 18-14.125 (cassation d'une faute inexcusable cycliste — transposable passager) + Civ. 2ᵉ 24 nov 2022 n° 20-23.462 (FGAO/CIVI exclusion). Verbatim Civ. 2ᵉ 30 mars 2023 n° 21-17.466 intégré FAQ.

**Règle opérationnelle** : Bloc A Étape 2 → systématiquement (a) WebSearch Légifrance pour le texte des articles + (b) **Judilibre PROD** pour les arrêts cités (recherche par n° de pourvoi + récupération verbatim motivation).

**Setup technique** : credentials prod PISTE dans `.env` (gitignored) ; SSL_CERT_FILE=certifi pour Python 3.14 macOS ; `python3 scripts/judilibre.py search "..." --sort score` (pas `date_desc` — invalide en prod, utiliser `score|scorepub|date`).

**Pourquoi pas encore promu** : confirmé sur 1 article (#6). À tester sur #7 — si validation, promotion en BRIEF.md §5 + ARTICLE_TEMPLATE.md.

### LEARN-055 — Matrice de collision ONISR (page 15 bilan annuel) = chiffre or pour articles cluster route

**Constat article #6** : la matrice de collision « tués selon mode de déplacement et antagoniste principal » (page 15 bilan ONISR annuel) révèle que **54 % des occupants de voiture meurent dans des accidents sans tiers impliqué** (sortie de route, perte de contrôle). C'est devenu le chiffre pivot le plus puissant de l'article (intro + H1.2) — incarne directement l'asymétrie art. 3/art. 4 Badinter.

**Règle** : Bloc D Étape 2 → toujours consulter la matrice de collision page 15 du bilan ONISR (en plus des chiffres clés synthétiques). Utile pour tous les articles cluster « Accidents de la route ».

**Pourquoi pas encore promu** : trouvaille tactique #6. À tester sur le prochain article cluster route.

### LEARN-056 — Double sourcing presse régionale sur affaires cabinet = signal E-E-A-T externe

**Constat article #6** : l'affaire Monsieur A. (tétraplégie 2,5 M€) a été couverte par Sud Ouest le 29 sept 2015. La double citation **post cabinet + article presse** renforce considérablement l'autorité (citation tierce indépendante + photo Me Plouton incluse). LEARN-040 E-E-A-T renforcé Lucid Media 2026.

**Règle** : Bloc C Étape 2 → pour chaque affaire cabinet « top tier » identifiée, **rechercher si elle a été reprise en presse régionale** (Sud Ouest, France 3 NAQ, 20 Minutes Bordeaux, presse spécialisée). Si oui, double sourcing dans le draft.

**Pourquoi pas encore promu** : observation #6. À répliquer sur le prochain article avec affaire cabinet « top tier ».

---

## Procédure de digestion (à reproduire avant chaque nouvel article à partir de #5)

1. **Relire** la section *« LEARNINGS actifs »* + *« À surveiller »* ci-dessus.
2. **Pour chaque entrée**, appliquer le critère de promotion (3 conditions).
3. **Si confirmé** :
   - Identifier la destination (BRIEF.md / ARTICLE_TEMPLATE.md / LEARNINGS-archive.md).
   - Écrire le contenu de la règle dans le fichier cible (pas juste la référence).
   - Déplacer l'entrée originale dans `LEARNINGS-archive.md` avec la date de promotion et la destination.
4. **Si non confirmé** : laisser dans la section actifs, avec un horodatage de revue (« revu 2026-XX-XX, à reconsidérer prochaine fois »).
5. **Si abandonné** : déplacer dans une section *« Abandonnés »* de l'archive avec la raison.

**But final** : `LEARNINGS.md` doit toujours faire **moins de 100 lignes**. S'il dépasse → c'est qu'on n'a pas digéré.
