# LEARNINGS — Journal vivant du pipeline

> Capture chaude post-article. Les learnings stabilisés sont **promus** vers `BRIEF.md`/`ARTICLE_TEMPLATE.md` puis archivés dans `LEARNINGS-archive.md`. **Cible : < 100 lignes.**
>
> **Dernière digestion : 2026-08-05** (audit de cohérence du pipeline, sans article). Promu → archive : **LEARN-056** (reprise presse : atout réel, à vérifier avant de la revendiquer). Erratum de destinations 057/063/067 (BRIEF **§4**, pas §2) et création de la section « Abandonnés ».
> Digestion précédente : 2026-06-23 (post #11) — promus **LEARN-057** (slugs publiés + test HTTP), **LEARN-063** (lire `CONTENT_TEXT`), **LEARN-064** (push Wix fiable), **LEARN-067** (inventaire catégorie Ressources) ; **LEARN-065** archivé ; **LEARN-054** élagué.
> Digestions antérieures : 2026-06-01 (#6), 2026-05-13 (#4). *(Le 2026-06-15 était une capture de learnings sur #8, pas une digestion : aucune promotion appliquée ce jour-là.)* Historique complet + cartographie : [`LEARNINGS-archive.md`](LEARNINGS-archive.md).
>
> Restent ci-dessous les observations **non encore promues** — soit qu'elles ne soient pas confirmées sur 2 articles, soit que leur formulation reste à stabiliser.

---

## Critère de promotion
Promu vers BRIEF/TEMPLATE quand **≥ 2 conditions sur 3** : (1) confirmé sur ≥ 2 articles distincts ; (2) opérationnel ; (3) inutile à relire s'il vit déjà ailleurs. Destinations : règle business/workflow → BRIEF ; pattern structurel/checklist → TEMPLATE ; savoir technique/stratégique → archive.

---

## LEARNINGS actifs (en attente de confirmation)

### LEARN-055 — Matrice de collision ONISR (p.15) = chiffre or, mais seulement angle « mortalité »
Utile cluster route axé mortalité (#6) ; n/a pour grand blessé survivant (#7). ⚠️ Affiner « utile quand l'angle porte sur la mortalité » avant promotion.

### LEARN-058 — Sujet de niche à volume nul = actif d'autorité ; repérer le pilier-volume adjacent
#7 : « tétraplégie » ~10/mo mais « nomenclature dintilhac » 3 600/mo juste à côté. Cadrer le sujet niche comme actif d'autorité + noter le head term adjacent pour un pilier futur. *1 article.*

### LEARN-059 — « Angle mort avocat » dans le SERP = Information Gain — à nuancer (partiel)
#8 : top 10 sans avocat (signal fort). #11 : avocats présents mais **aucun avec l'angle victime + montants réels + pénal** → « angle mort partiel ». Repérer l'absence d'avocat *côté demandeur avec preuves*, pas seulement l'absence d'avocat. *2 articles, formulation à stabiliser.*

### LEARN-060 — Élargir le faisceau de volumes aux termes de PROCÉDURE révèle des head terms cachés
#8 : « médiateur assurance » 6 600/mo trouvé via les termes transversaux de recours. `kw_data_google_ads_search_volume` plafonne à 10/appel → batcher. *1 article.*

### LEARN-061 — Stats : citer le PDF détaillé, pas la page HTML « chiffres clés » (qui arrondit)
#8 : France Assureurs 44 %/4 % (HTML) vs 43,7 %/3,6 % (PDF). Sourcer le PDF/rapport (décimales + millésime). *1 article.* (Note technique pypdf en archive.)

### LEARN-062 — Légifrance : contrôler la version EN VIGUEUR (date + réforme récente)
#8 : L125-2 modifié peu avant rédaction. #11 : L452-2 a une version en vigueur 2026-06-01 (réforme LFSS 2025 post ass. plén. 2023) → formulation prudente sur le calcul de la rente. Vérifier date de version + réforme récente. *2 articles — candidat promotion prochaine digestion.*

### LEARN-066 — Sujet issu du CSV des prises de contact = mine à pages-carrefour
#10 « changer d'avocat » né du CSV (686 demandes) ; #11 « faute inexcusable » relié à un contact (#575) mais sujet fourni par brief. Demande first-party + volume/concurrence se valident mutuellement. *1-2 articles.*

---

## Procédure de digestion v2 (avant chaque nouvel article)

> v2 depuis l'audit du 2026-08-05. La v1 s'arrêtait à l'écriture de la règle dans BRIEF/TEMPLATE : **c'est la cause racine de la dérive constatée** (LEARN-064 promu dans le BRIEF le 23/06 mais jamais propagé au README ni au TEMPLATE, qui ont continué à dire l'inverse pendant six semaines). Les étapes 4 à 7 existent pour que cela ne se reproduise pas.

1. **Relire** « LEARNINGS actifs » et appliquer le critère de promotion (≥ 2 conditions sur 3, cf. en tête de fichier).
2. **Promu ?** Écrire la règle **dans sa maison unique** : règle business/workflow → `BRIEF.md` ; chiffre structurel ou pattern de livrable → Cap général / checklist d'`ARTICLE_TEMPLATE.md` ; savoir technique → archive. **Une règle ne s'écrit qu'à un seul endroit** ; partout ailleurs, on pointe vers cette maison.
3. **Archiver** l'entrée dans `LEARNINGS-archive.md` (date + destination exacte, section et numéro), puis la retirer d'ici. Non promu : laisser en annotant « revu AAAA-MM-JJ ». Abandonné : section « Abandonnés » de l'archive.
4. **Propager** — `grep` du mot-clé de la règle sur *tout* le périmètre (repo + dossiers d'articles + mémoire persistante). Chaque écho trouvé est soit supprimé, soit transformé en pointeur vers la maison. **Une règle qui existe en deux exemplaires finira par diverger.**
5. **Rafraîchir le README** (point d'entrée) et la mémoire persistante si la règle les concerne : carte du projet, tableaux d'outils, index des règles non négociables. Ne jamais y recopier la règle — seulement le pointeur.
6. **Recompter le Bilan** de l'archive sur sa cartographie (il est vérifié mécaniquement par le lint).
7. **Vérifier** : `python3 scripts/test_md_to_ricos.py` puis `python3 scripts/lint_pipeline.py`. Zéro erreur avant de commiter.

**But : ce fichier < 100 lignes.** Toute règle mécanisable doit finir dans `scripts/lint_pipeline.py`, pas seulement en prose : c'est la seule forme de règle qui ne dérive pas.
