# LEARNINGS — Journal vivant du pipeline

> Capture chaude post-article. Les learnings stabilisés sont **promus** vers `BRIEF.md`/`ARTICLE_TEMPLATE.md` puis archivés dans `LEARNINGS-archive.md`. **Cible : < 100 lignes.**
>
> **Dernière digestion : 2026-06-23** (post #11, faute inexcusable). Promus → archive : **LEARN-057** (slugs publiés + test HTTP), **LEARN-063** (lire `CONTENT_TEXT`), **LEARN-064** (push Wix fiable), **LEARN-067** (inventaire catégorie Ressources) ; **LEARN-065** archivé (correctif technique) ; **LEARN-054** élagué. Restent ci-dessous les observations non encore confirmées sur 2 articles distincts.
> Digestions antérieures : 2026-06-15 (#8), 2026-06-01 (#6), 2026-05-13 (#4). Historique complet + cartographie : [`LEARNINGS-archive.md`](LEARNINGS-archive.md).

---

## Critère de promotion
Promu vers BRIEF/TEMPLATE quand **≥ 2 conditions sur 3** : (1) confirmé sur ≥ 2 articles distincts ; (2) opérationnel ; (3) inutile à relire s'il vit déjà ailleurs. Destinations : règle business/workflow → BRIEF ; pattern structurel/checklist → TEMPLATE ; savoir technique/stratégique → archive.

---

## LEARNINGS actifs (en attente de confirmation)

### LEARN-055 — Matrice de collision ONISR (p.15) = chiffre or, mais seulement angle « mortalité »
Utile cluster route axé mortalité (#6) ; n/a pour grand blessé survivant (#7). ⚠️ Affiner « utile quand l'angle porte sur la mortalité » avant promotion.

### LEARN-056 — Double sourcing presse régionale sur affaires cabinet — ❌ vérifier avant de revendiquer
Sur #6, la « reprise Sud Ouest » était en fait la date du post blog (confusion). Toujours **vérifier l'existence réelle** d'une reprise presse avant de l'invoquer. Ne pas promouvoir.

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

## Procédure de digestion (avant chaque nouvel article)
1. Relire « LEARNINGS actifs ». 2. Appliquer le critère de promotion. 3. Si confirmé : écrire la règle dans BRIEF/TEMPLATE + déplacer l'entrée dans `LEARNINGS-archive.md` (date + destination). 4. Sinon : laisser avec horodatage de revue. 5. Abandonné : section « Abandonnés » de l'archive. **But : ce fichier < 100 lignes.**
