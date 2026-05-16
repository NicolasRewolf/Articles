# LEARNINGS — Journal vivant du pipeline

> Capture chaude post-article. **N'accumule pas indéfiniment** : les learnings stabilisés sont **promus** vers `BRIEF.md` ou `ARTICLE_TEMPLATE.md`, et leur historique est conservé dans `LEARNINGS-archive.md`.
>
> **Cycle de digestion** : avant chaque nouvel article (à partir du #5), revue rapide de ce fichier. Tout ce qui est confirmé sur 2 articles distincts + opérationnel + non encore promu → on l'écrit dans BRIEF/TEMPLATE et on déplace ici dans `LEARNINGS-archive.md`.
>
> **Dernière digestion : 2026-05-13** (post article #4, cycliste renversé) + **ingestion LEARN-053 le 2026-05-16** (Doctrine Google AI Search 2026). 50 learnings promus vers BRIEF/TEMPLATE, 7 archivés comme savoirs techniques/stratégiques. Voir [`LEARNINGS-archive.md`](LEARNINGS-archive.md) pour l'historique complet et la cartographie des destinations.

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

### LEARN-020 — ONISR : provisoires fin janvier, définitifs fin mai

**Constat** : l'ONISR publie chaque fin janvier les résultats provisoires de l'année N-1, puis les définitifs fin mai.

**Règle** : entre fin janvier et fin mai, mentionner explicitement « résultats provisoires » dans toute citation chiffrée. Au-delà de mai, utiliser les définitifs.

**Pourquoi pas promu** : règle saisonnière vivante, à garder en main pour rappel ponctuel lors des collectes. Promotion possible en BRIEF.md §4 (Bloc D Étape 2) si elle se vérifie sur 2-3 articles supplémentaires touchant à l'ONISR.

### LEARN-META-1 — Une session ≠ tout le workflow

**Constat** : une seule session conversation a permis de boucler tout le workflow 4 étapes pour l'article #1 (cadrage, collecte, plan, rédaction). Les artefacts sont sauvegardés localement et accessibles cross-sessions via la mémoire persistante (`memory/`).

**Pour les articles suivants** : repartir des memos + `BRIEF.md` + `ARTICLE_TEMPLATE.md` + `LEARNINGS-archive.md`. Pas besoin de tout re-expliquer.

**Pourquoi pas promu** : méta-observation utile mais non opérationnelle (pas une règle à appliquer). Pourrait migrer vers `README.md` si on en crée un dédié au pipeline.

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
