# LEARNINGS — Journal vivant du pipeline

> Capture chaude post-article. **N'accumule pas indéfiniment** : les learnings stabilisés sont **promus** vers `BRIEF.md` ou `ARTICLE_TEMPLATE.md`, et leur historique est conservé dans `LEARNINGS-archive.md`.
>
> **Cycle de digestion** : avant chaque nouvel article (à partir du #5), revue rapide de ce fichier. Tout ce qui est confirmé sur 2 articles distincts + opérationnel + non encore promu → on l'écrit dans BRIEF/TEMPLATE et on déplace ici dans `LEARNINGS-archive.md`.
>
> **Dernière digestion : 2026-06-01** (post article #6, passager) — LEARN-020 promu (BRIEF §4 Bloc D), LEARN-META-2 tranché (option b : cible 2 000-2 500 maintenue + passe de compression industrialisée, BRIEF §4 Étape 4 + TEMPLATE), LEARN-META-1 dédupliqué et retiré de l'actif. Digestions antérieures : 2026-05-13 (post #4, cycliste) + ingestion LEARN-053 le 2026-05-16 (Doctrine Google AI Search 2026). 51 learnings promus vers BRIEF/TEMPLATE, 7 archivés comme savoirs techniques/stratégiques. Voir [`LEARNINGS-archive.md`](LEARNINGS-archive.md) pour l'historique complet et la cartographie des destinations.
>
> **Capture post-#7 : 2026-06-02** — LEARN-054 ✅ **promu** (BRIEF §5 + TEMPLATE sourcing + archive), LEARN-055 ⚠️ nuancé, LEARN-056 ❌ infirmé ; ajout LEARN-057 (vérifier les slugs Wix publiés avant cross-link) + LEARN-058 (sujet de niche = actif d'autorité + pilier-volume adjacent).
>
> **Capture post-#8 : 2026-06-04** (sinistre habitation, recours contre l'assureur) — LEARN-057 ✅ **confirmé #7+#8** (slugs des affaires via **export CSV du blog**) → à promouvoir ; ajout LEARN-059 (« angle mort avocat » dans le SERP = Information Gain) + LEARN-060 (faisceau de volumes élargi aux termes de procédure = head terms cachés). LEARN-055 et 058 revus : n/a sur #8 (assurance hors cluster route ; sujet à volume réel). Réorg repo **résolue** (commit a10dffa) → prochain article = **#09**.
>
> **Capture post-#8 (finition Desktop) : 2026-06-15** — session de vérification live (article amorcé sur iPad sans MCP, finalisé ici avec tous les outils). Ajout **LEARN-061** (PDF détaillé > page HTML synthèse pour les stats), **LEARN-062** (Légifrance : version en vigueur, pas que le n°), **LEARN-063** (gate de vérification hors-MCP + lire le corps du post). Note technique pypdf → archive. **LEARN-054** (Judilibre PROD) et **LEARN-057** (slugs Wix) ré-exercés/confirmés → à promouvoir digestion #09. *NB : fichier repassé > 100 lignes — résorption prévue à la digestion #09 (promotion 054/057 + archivage).*
>
> **Capture post-#10 : 2026-06-18** (changer d'avocat en cours de procédure — run autonome de bout en bout, sans STOP, mandat explicite Nicolas) — ajout **LEARN-064** (push Wix draft via API REST = opérationnel/fiable, ≠ « fragile »), **LEARN-065** (2 correctifs `md_to_ricos.py` : listes numérotées + convention rel), **LEARN-066** (sujet issu du CSV des prises de contact = mine à pages-carrefour). Article #10 poussé en draft `UNPUBLISHED` (`c2ba1848-a567-4d86-92b1-bc43454a48bb`) + vérifié (54 nœuds / 10 FAQ persistés).

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

**Statut : ✅ PROMU (2026-06-02)** — confirmé sur #6 + #7 (arrêts PCH #7 : Cass. 2ᵉ civ. 2 juill. 2015 n° 14-19.797 + 6 févr. 2020 n° 18-19.518). Promu vers **BRIEF.md §5** (Judilibre PROD) + **ARTICLE_TEMPLATE.md** (sourcing) + cartographie d'archive. *(Bloc à élaguer de l'actif à la prochaine digestion.)*

### LEARN-055 — Matrice de collision ONISR (page 15 bilan annuel) = chiffre or pour articles cluster route

**Constat article #6** : la matrice de collision « tués selon mode de déplacement et antagoniste principal » (page 15 bilan ONISR annuel) révèle que **54 % des occupants de voiture meurent dans des accidents sans tiers impliqué** (sortie de route, perte de contrôle). C'est devenu le chiffre pivot le plus puissant de l'article (intro + H1.2) — incarne directement l'asymétrie art. 3/art. 4 Badinter.

**Règle** : Bloc D Étape 2 → toujours consulter la matrice de collision page 15 du bilan ONISR (en plus des chiffres clés synthétiques). Utile pour tous les articles cluster « Accidents de la route ».

**Statut post-#7 (2026-06-02)** : ⚠️ **à nuancer** — sur #7 (tétraplégie = grand blessé *survivant*), la matrice (qui décrit les *tués* par mode) s'est révélée **peu applicable** ; le chiffre cœur était l'épidémiologie médullaire, pas la mortalité. Utile pour les articles cluster route « mortalité », pas « grand handicap / grand blessé ». Reste actif ; affiner la formulation (« utile quand l'angle porte sur la mortalité ») avant promotion.

### LEARN-056 — Double sourcing presse régionale sur affaires cabinet = signal E-E-A-T externe

**Constat article #6** : l'affaire Monsieur A. (tétraplégie 2,5 M€) a été couverte par Sud Ouest le 29 sept 2015. La double citation **post cabinet + article presse** renforce considérablement l'autorité (citation tierce indépendante + photo Me Plouton incluse). LEARN-040 E-E-A-T renforcé Lucid Media 2026.

**Règle** : Bloc C Étape 2 → pour chaque affaire cabinet « top tier » identifiée, **rechercher si elle a été reprise en presse régionale** (Sud Ouest, France 3 NAQ, 20 Minutes Bordeaux, presse spécialisée). Si oui, double sourcing dans le draft.

**Statut post-#7 (2026-06-02)** : ❌ **non confirmé — et partiellement infirmé**. L'affaire « top tier » du #7 est précisément *Monsieur A. / Artan* : la recherche dédiée n'a trouvé **aucune reprise presse vérifiable**. Le « Sud Ouest 29 sept. 2015 » de l'observation #6 correspond en réalité à la **date de publication du post blog cabinet**, pas à un article de presse → probable confusion date post ↔ date presse. **Ne pas promouvoir.** Reformulation : toujours **vérifier l'existence réelle** d'une reprise presse (recherche dédiée) avant de la revendiquer ; ne pas confondre date de publication d'un post et reprise tierce.

### LEARN-057 — Vérifier les slugs/URLs PUBLIÉS via Wix MCP avant tout cross-link

**Constat article #7** : les guides du repo #1 moto / #4 vélo / #6 passager **n'étaient pas publiés** sur le site (vérifié Wix MCP — requête de la catégorie « Ressources et notions juridiques » = 53 posts ; seuls #2 chirurgie + #3 arnaques en ligne en faisaient partie). Les linker aurait créé des **liens morts (404)**. À l'inverse, le vrai cluster live était plus riche : pilier `loi-badinter-85`, voisins `traumatisme-cranien-accident-voiture`, `pieton-renverse`, `echelle-de-glasgow`. Bonus : un slug réel ≠ supposé (ressource SARVI = `sarvi-ou-civi-...`, pas `sarci-`).

**Règle** : en Bloc C, **interroger le Blog Wix via MCP** (`POST /blog/v3/posts/query` fieldset `URL`, ou List Posts filtré par `categoryIds`) pour récupérer les **slugs publiés réels** AVANT d'écrire les cross-links. Ne jamais supposer qu'un article présent dans le repo local est en ligne.

**✅ Confirmé #7 + #8** — sur #8, slugs réels des affaires récupérés via **export CSV du blog** fourni par Nicolas (colonne `Post Page URL` = publié ; accents à URL-encoder). Règle élargie : récupérer les slugs publiés via **Wix MCP _ou_ export CSV du blog** avant cross-link. **À promouvoir prochaine digestion** → BRIEF.md (tableau MCPs §2-C) + ARTICLE_TEMPLATE.md (Bloc C).

### LEARN-058 — Sujet de niche à volume quasi nul = actif d'autorité ; repérer le pilier-volume adjacent

**Constat article #7** : « indemnisation tétraplégie » ≈ **10/mois** (quasi nul), mais « nomenclature dintilhac » = **3 600/mois** (concurrence quasi nulle) juste à côté. Décision Nicolas : garder #7 comme **pilier de niche** (autorité + conversion + citation IA assumées, pas trafic) et **noter le head term à volume comme candidat pilier dédié futur** (1 sujet = 1 page).

**Règle** : quand le head term du sujet est minuscule mais l'intent/valeur élevés (dossiers graves), cadrer l'article comme **actif d'autorité** (assumer le faible trafic, le dire explicitement à Nicolas) ET, via le gap analysis Bloc B, **identifier le head term à volume adjacent** pour un pilier dédié futur.

**Pourquoi pas encore promu** : 1 article (#7).

### LEARN-059 — « Angle mort avocat » dans le SERP = signal Information Gain fort

**Constat article #8** : sur les 3 requêtes (`dégât des eaux assurance`, `contre expertise assurance`, `maison fissurée que faire`), le top 10 était **100 % acteurs commerciaux** (assureurs, comparateurs, contre-experts, médias) — **zéro avocat** prenant le parti de l'assuré. Pour un sujet « litige / recours », ce profil = Information Gain quasi garanti (perspective avocat : leviers procéduraux, jurisprudence, défense du demandeur).

**Règle** : en Bloc B, repérer si le top 10 est **dépourvu d'avocats côté demandeur** → fort signal de gap exploitable. *Pas encore promu : 1 article (#8).*

### LEARN-060 — Élargir le faisceau de volumes aux termes de PROCÉDURE révèle des head terms cachés

**Constat article #8** : en mesurant aussi les termes **transversaux de procédure / recours** (médiateur, mise en demeure, référé, prescription, barème) et pas seulement le sujet, on a trouvé `médiateur assurance` = **6 600/mo, concurrence nulle** — head term de section bien plus puissant que le sujet lui-même (`dégât des eaux` 1 300). *Technique : `kw_data_google_ads_search_volume` plafonne à **10 résultats par appel** → batcher par 10.* Pas encore promu : 1 article (#8).

### LEARN-061 — Stats institutionnelles : citer le PDF détaillé, pas la page HTML « chiffres clés » (qui arrondit)

**Constat #8** : la landing page France Assureurs affichait **44 % / 4 %** ; le **PDF** de la même publication (*« L'assurance habitation en 2024 »*, 1er août 2025) donnait les décimales exactes **43,7 % / 3,6 % / 2 391 M€ / 2 042 M€ / 4,9 Md€ dont 2,6 habitation**. J'allais « corriger » des chiffres qui étaient en fait justes.

**Règle** : en Bloc D, pour toute donnée chiffrée précise, sourcer le **PDF/rapport détaillé** (décimales + tableaux + millésime) et y pointer le lien, pas la page de synthèse arrondie. *Pas encore promu : 1 article (#8).*

### LEARN-062 — Légifrance : contrôler la version EN VIGUEUR (date + réforme récente), pas seulement le n° d'article

**Constat #8** : **L125-2** (délais cat-nat) modifié par **LOI n° 2026-403 du 26 mai 2026**, 3 semaines avant rédaction. Le n° et le contenu semblaient bons, mais une réforme récente crée une nouvelle version (nouveau LEGIARTI) — un lien figé peut pointer une version périmée.

**Règle** : à chaque article cité, vérifier la **date de version en vigueur** + chercher une réforme récente ; pointer le lien sur la version applicable. Renforce LEARN-026 (anti-hallucination) et alimente le refresh M+6 (LEARN-046). *Pas encore promu : 1 article (#8).*

### LEARN-063 — Article amorcé hors-MCP → pass de vérification intégral non négociable avant publish

**Constat #8** : draft rédigé sur iPad sans MCP/API, puis vérifié à 100 % ici — **Judilibre** (n° pourvoi), **Wix** (slug publié + **corps du post**), **Légifrance** (versions), **stats** (source primaire), **DataForSEO** (reconfirm). Résultat : **0 correction factuelle nécessaire** (les claims précises ont toutes tenu).

**Règle** : le drafting peut se faire partout, mais le **gate de vérification avant publication reste obligatoire** (confirme LEARN-026/049). Extension de **LEARN-057** : ne pas seulement vérifier que le slug résout — **lire le `CONTENT_TEXT` du post** (API Wix) pour fonder les claims des encadrés-preuve (motif, date, RG de l'affaire). *Pas encore promu : 1 article (#8).*

### LEARN-064 — Push Wix draft via API REST = OPÉRATIONNEL et fiable (réviser la note « fragile »)

**Constat #10** : le push d'un article complet en **draft** via `POST /blog/v3/draft-posts` a parfaitement fonctionné. Méthode validée de bout en bout :
1. `python3 scripts/md_to_ricos.py article.md` → Ricos JSON, puis **minifier** (`separators=(',',':')`).
2. Embarquer le JSON comme **littéral JS** dans `ExecuteWixAPI`, avec **garde-fou avant POST** (`nodes.length` + `faqCount` attendus ; abort sinon → jamais de draft corrompu).
3. Champs `draftPost` : `title`, `memberId` (**requis** ; `07454f1f-c54a-4308-b897-19be554db88a` = compte Me Plouton), `categoryIds` (2), `excerpt`, **`seoSlug`** (settable, maxLength 100), `richContent`.
4. **Scope SITE obligatoire** : passer `siteId` sur ExecuteWixAPI, sinon **403** (l'appel partait en scope account).
5. Vérif post-push : `GET /blog/v3/draft-posts/{id}?fieldsets=RICH_CONTENT`.

**Chiffres** : #10 = 39 Ko de Ricos ≈ **9,7K tokens** (très en-dessous du plafond tool-call ~25K ; la **vraie** limite API est 400 Ko/post). Draft `c2ba1848…` créé `UNPUBLISHED`, 54 nœuds / 10 FAQ / 11 titres / 2 catégories vérifiés. → **La note README « push API facultatif et fragile (>25K tokens) » est à réviser** : fiable pour un article 2 000-2 500 mots minifié. *Pas encore promu : 1 article (#10).*

### LEARN-065 — `md_to_ricos.py` : 2 correctifs ✅ APPLIQUÉS (2026-06-18)

**Constat #10** : (a) **Listes numérotées** `1. 2. 3.` NON converties en `ORDERED_LIST` — dans la **version committée**, le builder `OL()` ET le handler de boucle manquaient (la version 508 lignes du working dir principal les avait, mais pas le commit) → fall-through en paragraphe run-on « 1. … 2. … 3. ». (b) **Convention rel non gérée** : `_text()` mettait TOUS les liens en `target=BLANK` sans `rel`, violant LEARN-024.

**Correctif appliqué** (script + `scripts/test_md_to_ricos.py`) : ajout du builder `OL()` (`ORDERED_LIST`) + handler `^\d+\.\s` dans `parse_markdown` (placé avant les puces) + rupture de paragraphe sur `^\d+\.\s` ; helper `_link_data()` appelé par `_text()` → interne (`INTERNAL_DOMAIN`, défaut `jplouton-avocat.fr`, surchargeable par env `RICOS_INTERNAL_DOMAIN`, ou URL relative `/`) = `target=SELF` sans `rel` ; externe = `target=BLANK` + `rel{nofollow,noopener,noreferrer}`. **Vérifié** : 3 tests unitaires verts + non-régression article #10 (2 `BULLETED_LIST`, **8 internes SELF / 6 externes BLANK+rel**, 0 run-on). → le **post-traitement manuel des liens n'est plus nécessaire**. *Pas encore promu : 1 article (#10). NB : réconcilier avec l'éventuelle WIP du working dir principal au merge.*

### LEARN-066 — Sujet issu du CSV des prises de contact = mine à pages-carrefour

**Constat #10** : le sujet « changer d'avocat » est né de l'analyse du **CSV des formulaires de contact** (686 demandes) : 12 demandes à intention nette, **transversales à toutes les expertises**. Croisé avec DataForSEO (cluster ≈ 1 200/mo, concurrence basse) → page-carrefour hire-ready qui maille vers tous les métiers. **Pattern** : demande first-party (CRM) + volume/concurrence (SEO) se valident mutuellement ; idéal pour les **sujets méta/procéduraux transversaux** (changer d'avocat, délais, honoraires, aide juridictionnelle…). Prolonge LEARN-059/060. *Pas encore promu : 1 article (#10).*

### À surveiller — structure repo (résolu 2026-06-03)

Réorg **committée** (`a10dffa`) : `Articles créés/` = archive des articles publiés (01-05) ; **#07 et #08 à la racine** ; **prochain article = #09**. Le maillage interne s'appuie sur le **site publié** (export CSV / Wix MCP), jamais sur l'arbo locale.

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
