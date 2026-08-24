# LEARNINGS — Journal vivant du pipeline

> Capture chaude post-article. Les learnings stabilisés sont **promus** vers `BRIEF.md`/`ARTICLE_TEMPLATE.md` puis archivés dans `LEARNINGS-archive.md`. **Cible : < 100 lignes.**
>
> **Dernière digestion : 2026-08-14** (avant l'article #14, cour criminelle départementale). Promus : **LEARN-058**, **LEARN-059 + 070** (fusionnés en typologie de l'angle mort), **LEARN-060**, **LEARN-061**, **LEARN-062 + 069 + 075** (fusionnés en discipline de version Légifrance), **LEARN-071**, **LEARN-072**, **LEARN-073** (correction du plafond de push Wix). Archivés : **LEARN-055**, **LEARN-068**, **LEARN-074**.
> **Constat de méthode issu de cette digestion** : les mentions de maturité portées par les entrées (« *1 article* ») étaient figées à leur date de capture et sous-estimaient la moitié du journal. La maturité se mesure par `grep` au moment de la digestion, jamais sur la mention.
> Digestions antérieures : 2026-08-05 (audit de cohérence, sans article), 2026-06-23 (post #11), 2026-06-01 (#6), 2026-05-13 (#4). *(Le 2026-06-15 était une capture de learnings sur #8, pas une digestion.)* Historique complet + cartographie : [`LEARNINGS-archive.md`](LEARNINGS-archive.md).
>
> Restent ci-dessous les observations **non encore promues** — soit qu'elles ne soient pas confirmées sur 2 articles, soit que leur formulation reste à stabiliser.

---

## Critère de promotion
Promu vers BRIEF/TEMPLATE quand **≥ 2 conditions sur 3** : (1) confirmé sur ≥ 2 articles distincts — **compté par `grep`, pas sur la mention portée par l'entrée** ; (2) opérationnel ; (3) inutile à relire s'il vit déjà ailleurs. Destinations : règle business/workflow → BRIEF ; pattern structurel/checklist → TEMPLATE ; savoir technique/stratégique → archive.

---

## LEARNINGS actifs (en attente de confirmation)

### LEARN-066 — Sujet issu du CSV des prises de contact = mine à pages-carrefour
#10 « changer d'avocat » né du CSV (686 demandes) ; #11 « faute inexcusable » relié à un contact (#575) mais sujet fourni par brief. Demande first-party + volume/concurrence se valident mutuellement. *1 article net — revu 2026-08-14, maintenu actif : ouvrir une section BRIEF sur le sourcing des sujets serait prématuré.*

### LEARN-076 — Google Ads supprime les termes sexuels bruts : `n/d` n'est pas zéro
#14 : « viol », « agression sexuelle », « inceste » seuls → aucune donnée de volume, alors que « violences conjugales » rend 12 100/mo, « féminicide » 5 400/mo, « harcèlement moral » 12 100/mo. Ce n'est donc **pas** un filtrage par sensibilité du sujet, mais par **crudité du terme** : « porter plainte pour agression sexuelle » passe (110/mo) là où « agression sexuelle » est supprimé. Conséquence : sur les infractions sexuelles, la demande se mesure par **proxies procéduraux + SERP/PAA**. Un rédacteur pressé lirait `n/d` comme « personne ne cherche ça » et abandonnerait un sujet à forte demande réelle.
**Déjà mécanisé** : `dataforseo.py volumes` imprime l'avertissement dès qu'un `n/d` apparaît, et la nuance est inscrite en BRIEF §4 Bloc B. *1 article — à reconfirmer sur un second sujet sensible.*

### LEARN-077 — Quatrième configuration d'angle mort : le SERP tenu par l'institutionnel
#14 « cour criminelle départementale » (1 600/mo, `competition_index` 0) : top 10 = cours-appel.justice.fr, Service-Public, France Victimes, Institut Robert Badinter, Wikipédia, Légifrance, Vie-publique, université, Dalloz. **Zéro cabinet.** Mais ce n'est pas l'angle mort *total* de #12 (où le sujet était capté par le sanitaire) : ici le sujet **est** traité juridiquement — simplement jamais par un praticien, et jamais du point de vue de la personne concernée. La typologie promue au BRIEF (aucun / partiel / total) ne couvre pas ce cas. Formulation à stabiliser : le degré se lit à **qui tient le SERP** (praticiens / institutionnels / autre discipline), pas au seul « y a-t-il des avocats ». *Confirmé sur un 2e cas le 2026-08-24 — #15 « harcèlement scolaire » (12 100/mo, index 0, 18 organiques tous institutionnels/associatifs/assureurs) ; nuance observée : la strate procédurale (« porter plainte ») portait, elle, 3 cabinets — le degré peut différer selon la requête du même sujet. **Candidat à promotion à la prochaine digestion.***

### LEARN-079 — `legifrance.py code` a des angles morts de matching : deux échecs reproductibles
#15 : « Code de l'éducation » n'est jamais matché (L111-6 et L911-4 introuvables sous deux graphies, avec et sans accent), alors que « Code de la justice pénale des mineurs » passe ; et l'article « 8 » du CPP n'est pas trouvé (numéro court — 4 780 hits tous codes, zéro match) alors que 706-3/706-5 passent dans le même code. Fallback qui a tenu : WebSearch ciblée `legifrance.gouv.fr` (verbatim + LEGIARTI). À mécaniser dans le script (normalisation du nom de code, gestion des numéros courts) plutôt qu'à documenter en prose. *1 article — signalé, correctif outil à arbitrer par Nicolas.*

### LEARN-080 — `md_to_ricos.py` : un lien à l'intérieur d'un italique n'est pas parsé
#15 : un lien markdown (crochets puis parenthèses) placé **à l'intérieur** d'un segment en italique — le pattern « Source : … » des encadrés chiffrés — sort en markdown brut dans le nœud Ricos, crochets visibles dans Wix. Détection : extraire tous les champs `text` du JSON produit et y chercher un reste de syntaxe de lien — zéro résiduel attendu ; ce contrôle mérite d'entrer dans `lint_pipeline.py` (le lint actuel compare la fraîcheur du ricos, pas la propreté de ses textes). Workaround appliqué : sortir le lien de l'italique, qui ne porte plus que « Source : ». *1 article — parser à étendre, garde-fou à mécaniser.*

### LEARN-078 — Un MCP est un confort, jamais une dépendance
#14 : le serveur MCP `dataforseo` était déclaré en global et absent de la session — sans message d'erreur. Le Bloc B devenait aveugle alors que les credentials étaient sur la machine depuis toujours. Nicolas a refusé d'attaquer l'article outillage incomplet ; le wrapper `scripts/dataforseo.py` (stdlib, credentials résolus dans l'ordre environnement → `.env` → `~/.claude.json`) a levé le blocage en une passe. C'était la dernière source de données du pipeline qui n'existait qu'en MCP — PISTE et Wix avaient déjà leur script ou leur API. **Règle candidate** : toute source qui alimente un livrable doit être atteignable par script local. *1 session — candidat BRIEF §5 à la prochaine digestion.*

---

## Procédure de digestion v2 (avant chaque nouvel article)

> v2 depuis l'audit du 2026-08-05. La v1 s'arrêtait à l'écriture de la règle dans BRIEF/TEMPLATE : **c'est la cause racine de la dérive constatée** (LEARN-064 promu dans le BRIEF le 23/06 mais jamais propagé au README ni au TEMPLATE, qui ont continué à dire l'inverse pendant six semaines). Les étapes 4 à 7 existent pour que cela ne se reproduise pas.

1. **Relire** « LEARNINGS actifs » et appliquer le critère de promotion (≥ 2 conditions sur 3, cf. en tête de fichier). **Compter les articles par `grep`** sur le numéro de learning — la mention portée par l'entrée date de sa capture et sous-estime sa maturité réelle (digestion 2026-08-14).
2. **Promu ?** Écrire la règle **dans sa maison unique** : règle business/workflow → `BRIEF.md` ; chiffre structurel ou pattern de livrable → Cap général / checklist d'`ARTICLE_TEMPLATE.md` ; savoir technique → archive. **Une règle ne s'écrit qu'à un seul endroit** ; partout ailleurs, on pointe vers cette maison.
3. **Archiver** l'entrée dans `LEARNINGS-archive.md` (date + destination exacte, section et numéro), puis la retirer d'ici. Non promu : laisser en annotant « revu AAAA-MM-JJ ». Abandonné : section « Abandonnés » de l'archive.
4. **Propager** — `grep` du mot-clé de la règle sur *tout* le périmètre (repo + dossiers d'articles + mémoire persistante). Chaque écho trouvé est soit supprimé, soit transformé en pointeur vers la maison. **Une règle qui existe en deux exemplaires finira par diverger.**
5. **Rafraîchir le README** (point d'entrée) et la mémoire persistante si la règle les concerne : carte du projet, tableaux d'outils, index des règles non négociables. Ne jamais y recopier la règle — seulement le pointeur. *La mémoire persistante ne se réécrit pas sans arbitrage explicite de Nicolas : signaler, ne pas trancher seul.*
6. **Recompter le Bilan** de l'archive sur sa cartographie (il est vérifié mécaniquement par le lint).
7. **Vérifier** : `python3 scripts/run_tests.py` (toutes les suites) puis `python3 scripts/lint_pipeline.py`. Zéro erreur avant de commiter.

**But : ce fichier < 100 lignes.** Toute règle mécanisable doit finir dans `scripts/lint_pipeline.py`, pas seulement en prose : c'est la seule forme de règle qui ne dérive pas.
