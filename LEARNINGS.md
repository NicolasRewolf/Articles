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
**Désormais outillé (2026-08-07, cf. LEARN-068)** : `scripts/legifrance.py code "<Code>" "<n°>"` retient automatiquement la version en VIGUEUR et affiche `⚠️ PAS EN VIGUEUR` sinon. La vigilance humaine reste requise sur la *réforme récente* (une version en vigueur peut être toute fraîche), mais le choix de version ne dépend plus de l'œil.

### LEARN-066 — Sujet issu du CSV des prises de contact = mine à pages-carrefour
#10 « changer d'avocat » né du CSV (686 demandes) ; #11 « faute inexcusable » relié à un contact (#575) mais sujet fourni par brief. Demande first-party + volume/concurrence se valident mutuellement. *1-2 articles.*


### LEARN-068 — API Légifrance : jamais souscrite, et 3 bugs que le 403 masquait
L'app PISTE **« Clear »** (PROD, client_id du `.env`) n'était abonnée qu'à JUDILIBRE : **tout** endpoint Légifrance répondait 403 — y compris `ping`, alors qu'un chemin inexistant rend 404 (donc refus délibéré de la passerelle, pas un bug de payload). Ni les credentials ni le scope n'étaient en cause : PISTE accorde `openid resource.READ` quoi qu'on demande. Souscription cochée le **2026-08-07** (Applications → Clear → Modifier → API Légifrance) ; **aucune CGU à accepter**, la souscription a suffi. L'`APP_SANDBOX_…` est créée d'office par PISTE, en SANDBOX, avec un autre client_id — inerte pour nous (et explication probable de l'`invalid_client` de LEARN-006 : credentials sandbox essayés contre la prod).
**Ce que l'accès a révélé, invisible tant que tout était en 403** : (1) le payload de `search` portait `"filtres": [{"facette":"DATE_VERSION","singleDate":null}]` → 500 systématique du backend DILA ; (2) `_format_hit` lisait des clés inexistantes → résultats vides ; (3) `/consult/code` répond 500 sur toute forme de payload — cassé côté DILA, contourné via la facette `NUM_ARTICLE` sur `CODE_DATE` puis `getArticle`. Les trois sont corrigés.
**Le piège de fond** : la recherche rend **toutes les versions successives** d'un article, majoritairement en `legalStatus=MODIFIE`. Une implémentation naïve renvoyait pour `CSS L. 376-1` une version **de 2015 abrogée**. Voir LEARN-062 : c'est désormais le script qui tranche. *1 session outil — à confirmer sur un article réel avant promotion vers BRIEF §5.*
### LEARN-069 — Légifrance : la version applicable se choisit sur les DATES, jamais sur le libellé
#12 : `legifrance.py code "Code pénal" "222-22"` a rendu la bonne version en l'étiquetant `⚠️ PAS EN VIGUEUR`. Le script ne reconnaissait que le libellé `VIGUEUR` ; la version applicable portait **`ABROGE_DIFF`** — c'est-à-dire « abrogation déjà programmée », ici au 2029-01-01 par la **recodification du CPP (ordonnance du 19 novembre 2025)**. Or `dateDebut` 2025-11-08 ≤ aujourd'hui < `dateFin`. **Un rédacteur pressé écartait le texte en vigueur.**
**Corrigé et outillé le 2026-08-07** : sélection par `dateDebut ≤ jour < dateFin`, affichage de la fenêtre d'application, et `scripts/test_legifrance.py` créé (la suite ne couvrait pas ce script). Limites subsistantes : jeux de versions incomplets sur certains articles (`222-24`, `222-30` → 0 version en vigueur trouvée) et numéros courts non résolus (CPP art. 7 et 8). *1 article — confirmer sur #13 avant promotion vers BRIEF §5.*

### LEARN-070 — L'angle mort peut être TOTAL quand le sujet est capté par une autre discipline
#12 « soumission chimique » : les 10 résultats organiques sont sanitaires, scientifiques ou associatifs (arretonslesviolences, Wikipédia, addictovigilance, CRAFS, ameli, mendorspas, vih.org). **Aucun contenu juridique**, ni qualification, ni prescription, ni indemnisation. Le SERP traite le sujet en santé publique, jamais en droits. Va plus loin que LEARN-059 (« angle mort partiel ») : chercher les sujets **captés par une autre discipline** — c'est là que le gap est maximal. Signal repérable en amont : `competition_index` très bas (2) sur un volume élevé (2 400/mo). *1 article.*

### LEARN-071 — Un dispositif national déployé par territoires = pivot local à fort Information Gain
#12 : l'expérimentation « soumission chimique » (art. 68 LFSS 2025) ne couvre que 3 régions, adossées à un laboratoire chacune — la Nouvelle-Aquitaine en est exclue. La mesure annoncée par toute la presse **ne s'applique pas à Bordeaux**. Réflexe à systématiser sur toute expérimentation LFSS/santé/justice : **vérifier le périmètre territorial dans l'arrêté**, pas dans la presse, et en faire un H2 si le cabinet est hors dispositif. Corollaire : inscrire l'entrée éventuelle de la NAQ comme déclencheur de refresh prioritaire. *1 article.*

### LEARN-072 — Chercher la fiche destinée aux PROFESSIONNELS, pas la page grand public
#12 : la donnée la plus actionnable de l'article (**5 jours** pour sang/urine, **jusqu'à 6 mois** pour les cheveux, prélèvements conservés **3 ans** pour contre-expertise) vient de la fiche de synthèse des conseils régionaux de l'**Ordre des médecins** (janvier 2026), pas des pages grand public qui répètent « moins de 48 heures ». Sur tout sujet à protocole, chercher la fiche praticien. *1 article.*

### LEARN-073 — Le vrai plafond du push Wix, c'est le transport, pas l'API
#12 : `ricos.min.json` = **51 Ko** (contre 45 Ko pour #11) — très loin de la limite API de 400 Ko, mais **au-delà de ce qu'une lecture de fichier rend d'un coup**, donc impossible à embarquer tel quel dans `ExecuteWixAPI`. Contournement validé : **compaction sémantique** avant envoi (retrait de `id:""`, `nodes:[]`, `decorations:[]`, `paragraphData:{}`) → **42 Ko, −19 %**, document strictement identique (contrôle : égalité des nœuds de texte). `ricos.min.json` reste la forme canonique attendue par le lint. *1 article.*
**Quirk associé** : `sante.gouv.fr` bloque WebFetch (écran CAPTCHA Cegedim), comme Légifrance. Passer par WebSearch ou par les pages ARS régionales.

---

## Procédure de digestion v2 (avant chaque nouvel article)

> v2 depuis l'audit du 2026-08-05. La v1 s'arrêtait à l'écriture de la règle dans BRIEF/TEMPLATE : **c'est la cause racine de la dérive constatée** (LEARN-064 promu dans le BRIEF le 23/06 mais jamais propagé au README ni au TEMPLATE, qui ont continué à dire l'inverse pendant six semaines). Les étapes 4 à 7 existent pour que cela ne se reproduise pas.

1. **Relire** « LEARNINGS actifs » et appliquer le critère de promotion (≥ 2 conditions sur 3, cf. en tête de fichier).
2. **Promu ?** Écrire la règle **dans sa maison unique** : règle business/workflow → `BRIEF.md` ; chiffre structurel ou pattern de livrable → Cap général / checklist d'`ARTICLE_TEMPLATE.md` ; savoir technique → archive. **Une règle ne s'écrit qu'à un seul endroit** ; partout ailleurs, on pointe vers cette maison.
3. **Archiver** l'entrée dans `LEARNINGS-archive.md` (date + destination exacte, section et numéro), puis la retirer d'ici. Non promu : laisser en annotant « revu AAAA-MM-JJ ». Abandonné : section « Abandonnés » de l'archive.
4. **Propager** — `grep` du mot-clé de la règle sur *tout* le périmètre (repo + dossiers d'articles + mémoire persistante). Chaque écho trouvé est soit supprimé, soit transformé en pointeur vers la maison. **Une règle qui existe en deux exemplaires finira par diverger.**
5. **Rafraîchir le README** (point d'entrée) et la mémoire persistante si la règle les concerne : carte du projet, tableaux d'outils, index des règles non négociables. Ne jamais y recopier la règle — seulement le pointeur.
6. **Recompter le Bilan** de l'archive sur sa cartographie (il est vérifié mécaniquement par le lint).
7. **Vérifier** : `python3 scripts/run_tests.py` (toutes les suites) puis `python3 scripts/lint_pipeline.py`. Zéro erreur avant de commiter.

**But : ce fichier < 100 lignes.** Toute règle mécanisable doit finir dans `scripts/lint_pipeline.py`, pas seulement en prose : c'est la seule forme de règle qui ne dérive pas.
