# LEARNINGS — Pipeline éditorial Cabinet Plouton

> Capitalisation transverse. Mise à jour **après chaque article** : ce qui a marché, ce qui a coincé, raccourcis identifiés.

---

## Learnings techniques (Wix)

### LEARN-001 — Slugs sans accent (règle stricte)
**Contexte :** intégration éditoriale Wix Studio.
**Constat :** les accents dans les slugs Wix créent des doublons raw/percent-encoded (`/exemple-d-éclat` vs `/exemple-d-%C3%A9clat`), néfaste SEO (cannibalisation, dilution PageRank).
**Règle :** tous les slugs sans accent. Translittérer (`é → e`, `à → a`, etc.). **Pas d'audit rétro** sur les articles existants — règle pour les nouveaux uniquement (décision Nicolas 2026-05-11).
**Statut :** sauvegardée en mémoire persistante (`feedback_slugs_sans_accent.md`).

### LEARN-002 — HTML/Ricos obligatoire dans l'éditeur Wix (pas de Markdown)
**Contexte :** copier-coller du livrable final dans l'éditeur Wix.
**Constat :** le Markdown ne survit pas au paste dans l'éditeur Wix Studio (formatage cassé, listes éclatées, liens perdus).
**Règle :** livrable final en **HTML balisé** ou **Ricos JSON** via API. Pour les premiers articles, copier-coller direct du Markdown dans Wix Studio fonctionne **mais nécessite que Nicolas refasse la mise en page manuellement** (validé 2026-05-11).

### LEARN-003 — Wix Ricos : 3 patterns d'encadrés validés (test 2026-05-11)
**Testé sur draft test du 11/05/2026 :**
- ✅ **BLOCKQUOTE** = rendu "encadré" (barre verticale + indentation) — usage : définitions, encadrés chiffrés, mini-CTAs inline
- ✅ **DIVIDER** = trait horizontal centré entre sections (`lineStyle: SINGLE, width: MEDIUM, alignment: CENTER`)
- ✅ **COLLAPSIBLE_LIST** = FAQ accordéon (chevron, 1ʳᵉ Q ouverte par défaut) — usage : FAQ structurée pour citabilité LLM
**Note :** ces 3 types fonctionnent via l'API Wix Blog v3 `/draft-posts` en payload Ricos JSON.

### LEARN-004 — Push API Wix : limite pratique sur articles longs
**Contexte :** push d'un article ~2 900 mots via `CallWixSiteAPI` MCP.
**Constat :** le Ricos JSON compact pèse ~58 KB (~14.5K tokens). Lors du push, le body inline du tool call est trop lourd à passer pour un article complet en un seul appel (Read tool plafonne à 25K tokens ; output tokens lourd à produire).
**Fallback validé :** copier-coller le markdown directement dans l'éditeur Wix Studio, puis polissage manuel par Nicolas (qui veut de toute façon refaire la mise en page).
**Piste pour automatiser plus tard :** push API en plusieurs PATCHes cumulatifs avec chunks de richContent, OU script Python qui POSTe via curl en récupérant l'auth Wix d'une manière indirecte (à creuser).

### LEARN-005 — Parser markdown → Ricos (script local)
**Contexte :** `scripts/md_to_ricos.py` créé pour automatiser la conversion.
**Couvert :** H2/H3, paragraphes, listes à puces, blockquotes, dividers, COLLAPSIBLE_LIST auto en FAQ, inline (bold, italic, link, **bold+link** imbriqué).
**Limites identifiées :** les bullets `- ` à l'intérieur des blockquotes ne sont pas reconvertis en BULLETED_LIST (restent en texte brut avec tiret). À traiter dans une v2 du parser si on relance le push API.
**Statut :** parser fonctionnel mais perfectible. Stocké dans `scripts/md_to_ricos.py`.

### LEARN-006 — PISTE OAuth (Légifrance + Judilibre) : vérifier la bonne souscription
**Contexte :** activation API Data Gouv PISTE.
**Constat :** un premier set de credentials (`f8c5...` / `9e51...`) a échoué avec `invalid_client`. Le deuxième set (`bc60...` / `8b68...`) a fonctionné immédiatement.
**Hypothèse :** la première fois, les credentials étaient probablement ceux d'une app non validée ou non souscrite à Judilibre.
**Règle :** récupérer les credentials sur l'écran de **souscription Judilibre Sandbox** spécifiquement, pas sur l'écran général de l'app.
**Statut :** API maintenant fonctionnelle ; scripts `scripts/piste_auth.py`, `scripts/judilibre.py`, `scripts/legifrance.py` opérationnels (modulo problème SSL Python 3.14 macOS — fallback curl OK).

---

## Learnings éditoriaux

### LEARN-007 — Intro : phrase psychologique avant le chiffre brutal
**Contexte :** "decision moment" du lecteur (les premières lignes).
**Constat :** ouvrir sur une vérité psychologique du persona (*"Quand un accident à moto arrive, le choc physique n'est souvent pas le plus dur"*) résonne mieux qu'un chiffre brutal en tête.
**Pattern validé :** phrase psychologique → chiffre brutal sourcé (paragraphe 2) → bullets de promesse → signature autorité cabinet.
**Réutilisable :** sur tous les articles "victime de…" qui touchent à un vécu spécifique (motard, accident travail, victime violence, etc.).

### LEARN-008 — TDM 6 entrées H2 cliquables
**Contexte :** article long-form (>2 000 mots).
**Constat :** une table des matières juste après l'intro améliore (a) la navigation du lecteur en scanning, (b) la citabilité GEO (les LLM scannent la TDM en priorité).
**Pattern :** liste à puces numérotée avec liens d'ancrage `#section-slug`. Chaque H2 cible reçoit un `id` correspondant (à mapper dans le push Ricos ou manuellement dans Wix).

### LEARN-009 — Bullets "Ce que vous allez comprendre" dans l'intro
**Contexte :** signaler la profondeur sans l'imposer au lecteur.
**Constat :** 4 bullets (3-5 selon contenu) qui annoncent les angles clés = mini-sommaire intégré dans l'intro, format scannable, rassurant.
**Réutilisable :** dans tout guide pédagogique.

### LEARN-010 — Formulation cabinet > stat externe non sourcée
**Contexte :** stat « 90 % des victimes transigent pour la moitié » entendue dans le SERP mais sans source primaire.
**Constat :** la page d'expertise Plouton contient déjà la formulation cabinet officielle (*« Les premières offres formulées par les compagnies d'assurance sont presque toujours sous-évaluées »*) qui supplante n'importe quelle stat externe non sourcée.
**Règle :** avant d'abandonner ou de chercher loin une stat externe, **vérifier si la page d'expertise du cabinet contient déjà la formulation interne**. Bonus : cross-link vers la page = sourcing + signal de conversion.

### LEARN-011 — Reformulation pédagogique de concepts juridiques
**Contexte :** présenter la nomenclature Dintilhac à un lecteur non-juriste.
**Constat :** la page d'expertise propose une triade pédagogique imbattable : *« ce que vous ne pouvez plus faire, ce que vous devez désormais payer, ce que vous avez perdu en qualité de vie »*. Vaut tous les jargons techniques.
**Règle :** pour chaque concept juridique central, **chercher s'il existe déjà une reformulation pédagogique cabinet** (page d'expertise, autre article) avant d'en inventer une.

---

## Learnings process / workflow

### LEARN-012 — Volume cible data-driven (Plouton 28j) — RÉVISÉ 2026-05-11
**Contexte :** plan initial visait 4 400 mots ; data Plouton montre médiane top performers = 1 700 mots.
**Constat :** pas de corrélation longueur ↔ trafic sur les top 10 articles ressources Plouton. Pattern lecteur = **scanning** dès qu'on dépasse 1 400 mots.
**Règle (révisée Nicolas 2026-05-11, post article #2) :** cible pragmatique **~2 000-2 500 mots** pour les articles « Ressources et notions juridiques ». Plus court = OK si l'angle le permet ; plus long = à justifier par profondeur distinctive vs concurrence SERP. *Note : cette cible révisée remplace toutes les mentions antérieures de 2 500-2 800 ou 2 800-3 200 mots dans le pipeline.*

### LEARN-013 — Mini-CTA inline #1 post-empathie (hypothèse à valider)
**Contexte :** 0 % conversion observée sur la catégorie "Ressources et notions juridiques" historiquement.
**Hypothèse mise en test :** placer un mini-CTA contextuel **après l'intro** (là où l'empathie du lecteur est maximale) plutôt qu'uniquement en fin d'article = levier de conversion.
**Pattern testé sur article #1 :** *"Vous êtes motard ou proche d'un motard blessé, et ces démarches vous dépassent ? [Parler à un avocat]"*.
**À mesurer :** taux de clic vers `/honoraires-rendez-vous` sur les 28 prochains jours post-publication. **Si validé**, à réutiliser systématiquement.

### LEARN-014 — Wix MCP > grep sitemap pour catégorisation
**Contexte :** identifier les articles ressources existants pour le maillage interne.
**Constat :** grep des slugs `/post/...` du sitemap est approximatif (catégories non visibles). **Wix MCP** (`POST /blog/v3/posts/query` avec filter `categoryIds`) donne la catégorisation officielle et la liste exacte.
**Règle :** systématiquement utiliser Wix MCP pour la cartographie des articles ressources avant le plan H2/H3 (Étape 3).

### LEARN-015 — Workflow Étape 2 : Bloc D (stats officielles) ajouté au brief
**Contexte :** stats ONISR essentielles pour hook chiffré + citabilité GEO.
**Décision (2026-05-11) :** ajout d'un **Bloc D — Données statistiques & rapports officiels** au workflow Étape 2, à côté de A (juridique), B (SEO), C (interne Plouton).
**Sources mobilisables :** data.gouv.fr (BAAC pour route), ONIAM (médical), CNAM-AT (travail), Santé Publique France (vie courante), INSEE/SSMSI (sécurité publique), Ministère Justice DSED (pénal).

---

## Learnings SEO / GEO

### LEARN-016 — FAQPage schema JSON-LD à ajouter manuellement
**Contexte :** le COLLAPSIBLE_LIST natif de Wix ne génère **pas** automatiquement le schema FAQPage.
**Règle :** pour chaque article avec FAQ, livrer un bloc JSON-LD `FAQPage` séparé prêt-à-coller dans le module SEO Wix Studio (ou via widget HTML Embed). Voir `etape-4-faq-schema.json` de chaque article.

### LEARN-017 — Format FAQ pour citabilité LLM
**Pattern validé :**
- Question = formulation naturelle utilisateur (proche des PAA SERP)
- Réponse = **40-80 mots**, commençant par le **concept-clé** (la première phrase doit pouvoir être citée seule par un LLM)
- Sourcing intégré (lien Légifrance / ONISR dans la réponse)

### LEARN-018 — SERP top 10 + PAA + Related = panorama suffisant
**Constat :** pour la gap analysis Étape 2 Bloc B, **un seul appel SERP** avec `depth=20` et `people_also_ask_click_depth=1` donne SERP + PAA + Related searches en une fois. Très économe en crédits DataForSEO.
**Réutilisable :** pas besoin d'enchaîner plusieurs appels pour analyser un sujet.

---

## Learnings juridiques / sourcing

### LEARN-019 — Loi Badinter Article 4 = pivot conducteur VTM (CORRIGÉ 2026-05-11)
**Constat :** pour tout article touchant à un usager **conducteur** de véhicule terrestre à moteur (motard, automobiliste, conducteur poids-lourd…), **l'article 4 est central** : *« La faute commise par le conducteur du véhicule terrestre à moteur a pour effet de limiter ou d'exclure l'indemnisation des dommages qu'il a subis. »* À la différence des passagers/piétons (article 3 — indemnisation intégrale sauf faute inexcusable cause exclusive).
**URL Légifrance Art. 4 :** https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006839431
**À ne pas confondre :** Article 5 Badinter = dommages aux **BIENS** (équipement détruit, véhicule). Article 6 = préjudice par **ricochet** (proches). Article 12 = délai 8 mois offre. Article 16 / L. 211-13 Code assurances = sanction doublement intérêt légal.
**Historique :** sur l'article #1, j'ai initialement écrit "article 5" partout (4 occurrences), erreur juridique grave découverte par le fact-check NotebookLM post-rédaction. Corrigée le 2026-05-11.
**Réutilisable :** sur futurs articles voiture, scooter, camion, etc.

### LEARN-027 — Livraison JSON-LD : directement dans le chat, pas de fichier HTML (durable)
**Contexte :** Nicolas 2026-05-11, après plusieurs allers-retours infructueux pour coller le schema FAQPage dans le champ "Marquage structuré" de Wix Studio.
**Constat :** stocker le JSON-LD dans un fichier `.html` ou `.json` séparé ne marche pas bien — le `<script>` est interprété par les previews, et copier-coller le contenu brut depuis un fichier multiplie les sources d'erreur.
**Règle :** pour le **JSON-LD FAQPage** (et tout autre schema markup destiné à Wix), **livrer le bloc `<script>...</script>` directement dans la réponse chat**, dans un bloc de code Markdown (triple backticks), **JSON minifié one-liner**, avec `type="application/ld+json"` (validé fonctionnel sur Wix Studio).
**Statut :** sauvegardée en mémoire persistante (`feedback_jsonld_directement_dans_chat.md`).

### LEARN-026 — ANTI-RÉCIDIVE : fact-check juridique obligatoire AVANT rédaction (durable, révisé)
**Contexte :** sur l'article #1, j'ai produit 3 erreurs juridiques (art. 5/4, art. 6/5, art. 12/16) parce que j'ai rédigé sans sourcing primaire fiable.
**Règle (durable — révisée 2026-05-11 post nouveau workflow NotebookLM) :**
1. **AVANT de rédiger** une affirmation juridique précise (n° d'article de loi, n° de pourvoi, fondement juridique), confirmer via **au moins une source fiable** (WebSearch ciblée Légifrance/courdecassation.fr/juricaf.org **OU** réponse NotebookLM fournie par Nicolas — LEARN-022 — **OU** document source primaire déposé par Nicolas).
2. **Citer les textes verbatim** en s'appuyant sur les sources confirmées, pas sur extrapolation SERP.
3. **Vérifier 2 fois** chaque numéro d'article cité (idéalement 2 sources convergentes).
4. **Si une affirmation reste non confirmée** → reformulation prudente + `⚠️ À vérifier` (LEARN-049).
5. **Si je doute en cours de rédaction** → demander à Nicolas un cluster NotebookLM orienté sur la zone (LEARN-022) AVANT de figer le texte.
**Ce n'est pas optionnel** — c'est ce que le brief impose au titre de l'anti-hallucination.
**Statut :** sauvegardée en mémoire persistante (`feedback_factcheck_juridique_obligatoire.md`).

### LEARN-020 — ONISR : provisoires fin janvier, définitifs fin mai
**Constat :** l'ONISR publie chaque fin janvier les résultats provisoires de l'année N-1, puis les définitifs fin mai.
**Règle :** entre fin janvier et fin mai, **mentionner explicitement "résultats provisoires"** dans toute citation chiffrée. Au-delà de mai, utiliser les définitifs.

### LEARN-021 — Anti-hallucination : fourchettes prudentes
**Pattern validé :** pour les ordres de grandeur juridiques non sourcés (DFP, PEP, agrément), formuler prudemment : *"indicatives", "généralement", "varie selon", "à titre indicatif"*. **Jamais d'affirmation chiffrée présentée comme barème officiel.**
**Justification :** il n'existe **pas de barème officiel** en France pour les préjudices corporels ; seule la jurisprudence (référentiel Mornet en pratique) sert d'indicateur — par nature variable.

---

## Learnings NotebookLM (workflow validé Nicolas 2026-05-11)

### LEARN-022 — NotebookLM = outil de Nicolas, pas le mien (workflow définitif)
**Contexte :** définition clarifiée par Nicolas après l'article #2.
**Workflow validé** :
1. **NotebookLM est l'outil de Nicolas**, pas un MCP que j'utilise directement (le MCP `notebooklm-mcp` a bugué de manière répétée sur l'article #2 — on l'abandonne sauf si Nicolas confirme partage public).
2. Si **j'ai un doute sur une notion juridique précise** ou si **j'ai besoin de creuser/sécuriser une affirmation** (en Étape 2 collecte, Étape 3 plan, ou Étape 4 rédaction), **je formule une question ciblée à Nicolas** dans le chat.
3. Nicolas **bâtit alors un cluster d'info orienté** sur ma question (dépose les bonnes sources dans NotebookLM, l'interroge, capture la réponse) et **me fournit la synthèse en retour** (texte copier-collé, fichier .md, etc.).
4. **J'ingère la réponse** et la dispatche au bon endroit : sourcing du plan, paragraphe du corps, encadré juridique, FAQ, etc.
5. **Je gère le quand et le si besoin** — pas systématique, uniquement quand ça apporte de la valeur. Pas de question superflue.
**Bénéfice :** Nicolas a la main sur la qualité du cluster d'info, je reste focalisé sur la rédaction, le MCP NotebookLM (qui bugue) est contourné.

### LEARN-023 — Format des demandes NotebookLM à Nicolas
**Format type pour une demande efficace :**
1. **Zone d'incertitude précise** : *« Je dois citer Cass. 1re civ. 23 janv. 2019 sur défaut info chirurgien esthétique mais le n° de pourvoi n'est pas confirmé par mes WebSearch. »*
2. **Question NotebookLM formulée pour Nicolas** : prêt-à-coller dans son interface NotebookLM (en bloc code Markdown, sans retours à la ligne forcés). Voir LEARN-051 pour la mise en forme.
3. **Ce que je vais faire de la réponse** : *« Si confirmé → je cite verbatim avec n° pourvoi dans H2.3 ; si infirmé → je retire l'arrêt et je formule prudemment. »*
**Pattern validé** sur Q5 article #2 (apports SOFCPRE / tourisme médical / diffamation / action de groupe — tous intégrés en A.5-ter et A.5-bis).

### LEARN-049 — Anti-récidive : ne PAS rédiger une affirmation juridique précise sans sourcing fiable (renommé depuis LEARN-022-bis)
**Contexte :** sur l'article #1, j'ai produit 3 erreurs juridiques (art. Badinter confondus) parce que j'ai rédigé sans sourcing primaire. Anti-pattern documenté.
**Règle absolue (durable) :** avant de rédiger une affirmation juridique précise (n° d'article de loi, n° de pourvoi, fondement juridique, citation verbatim), je dois disposer d'**au moins une source fiable** parmi :
- **WebSearch ciblée** `allowed_domains=["legifrance.gouv.fr"]` ou sur courdecassation.fr / juricaf.org
- **Réponse NotebookLM** fournie par Nicolas (LEARN-022)
- **Document source primaire** déposé par Nicolas (PDF ONIAM RA, SOFCPRE, etc.)
**Si AUCUNE source fiable trouvée** :
- Reformulation prudente (« la jurisprudence tend à reconnaître », « en général », « à titre indicatif ») — LEARN-021
- Marquage `⚠️ À vérifier` noir sur blanc dans le draft
- Mention explicite à Nicolas : *« Je ne peux pas confirmer X — veux-tu me préparer un cluster NotebookLM ? »*
**Anti-pattern observé article #2** : j'avais initialement cité Cass. 1re civ. 23 janv. 2019 sur défaut info chirurgien esthétique sans confirmation directe → remplacé en Étape 4 par Cass. 1re civ. 12 juillet 2012 n° 11-17.510 (confirmé) après WebSearch ciblée. Bonne réaction post fact-check, mais aurait pu coûter une erreur juridique.

### LEARN-050 — MCP NotebookLM : abandonné par défaut (compte de service Google différent)
**Contexte :** sur l'article #2, le MCP NotebookLM `notebooklm-mcp` a échoué de manière répétée avec l'erreur *« Could not find NotebookLM chat input. Please ensure the notebook page has loaded correctly. »*
**Diagnostic** : le navigateur headless du MCP utilise probablement un compte Google différent de celui de Nicolas. Sauf à passer le notebook en partage public (*« Anyone with the link »*), l'MCP ne peut pas accéder au notebook.
**Décision Nicolas 2026-05-11** : on n'utilise PAS le MCP NotebookLM par défaut. Le workflow validé (LEARN-022) passe par Nicolas qui copie-colle les réponses du chat NotebookLM dans notre conversation.
**Si on veut un jour ré-essayer** : exiger explicitement le partage public du notebook + tester avec une question courte avant tout.

### LEARN-051 — Format des questions à coller dans NotebookLM (pas de hard wrap)
**Constat 2026-05-11 :** j'avais initialement formaté mes 5 questions NotebookLM avec des retours à la ligne forcés (~65 caractères) — ce qui rendait le copier-coller dégueulasse côté Nicolas (texte cassé dans l'interface web NotebookLM).
**Règle :** lorsque je livre une question à coller dans NotebookLM (LEARN-023), utiliser **un bloc code Markdown avec prose continue, sans retours à la ligne forcés**. NotebookLM gère sa propre mise en forme.
**Anti-pattern à éviter** : `cat <<EOF` style ou wrap à 65/80 caractères.

---

### LEARN-025 — Pas de listes à puces dans les blockquotes Wix (durable)
**Contexte :** observation Nicolas 2026-05-11 lors de la mise en page article #1 dans Wix Studio.
**Constat :** les BULLETED_LIST imbriquées dans BLOCKQUOTE ne sont pas correctement rendues par Wix Ricos (soit pas supportées, soit rendu cassé).
**Règle :** pour les encadrés chiffrés ("Les X en chiffres"), **rédiger en prose continue avec séparateurs** (`;` ou `—`), pas de bullets. Si une liste à puces est nécessaire, la **sortir du blockquote** (bloc séparé au-dessus/en-dessous).
**Statut :** sauvegardée en mémoire persistante (`feedback_pas_de_bullets_dans_blockquote.md`) + intégrée dans le pattern encadré chiffré d'`ARTICLE_TEMPLATE.md`.
**Implication parser :** `scripts/md_to_ricos.py` à faire évoluer pour détecter les `- ` dans les blockquotes et les transformer en prose plutôt que tenter une BULLETED_LIST imbriquée.

### LEARN-024 — Convention `rel` liens internes vs externes (durable)
**Contexte :** instruction Nicolas 2026-05-11.
**Règle :**
- **Liens internes** (`jplouton-avocat.fr/...`) : aucun `rel`, aucun `target="_blank"` → le lien "suit" (follow par défaut) + nav fluide.
- **Liens externes** : `target="_blank"` + `rel="noopener noreferrer nofollow"`.
**Why :** protéger le PageRank interne, ne pas donner d'autorité SEO aux externes, sécurité (`noopener`) + privacy (`noreferrer`) + conserver l'utilisateur sur le site Plouton (nouvel onglet externe).
**Statut :** sauvegardée en mémoire persistante (`feedback_liens_follow_nofollow.md`) + intégrée dans la checklist qualité d'`ARTICLE_TEMPLATE.md`.

---

## Patterns cognitifs (issue notebook "Cognition article" — 2026-05-11)

> Source : notebook NotebookLM dédié au copywriting cognitif. 11 patterns durables intégrés pour structurer la rédaction de tous les articles à partir de #2.

### LEARN-028 — Information Foraging Theory + Théorème de la valeur marginale (paradigme)
**Constat :** le lecteur web n'est pas un "lecteur" mais un "informavore" qui calcule à chaque instant le ratio gain d'information / coût cognitif. Selon le théorème de Charnov, il **quitte la page à la seconde où le taux d'extraction tombe sous la moyenne web**. Pas quand il s'ennuie : quand le rendement marginal chute.
**Implication :** dimensionner l'article en **"patches" qui s'enrichissent en continu**. Chaque ~250 mots doit livrer une nouvelle information à forte valeur (chiffre sourcé, cas concret, citation, implication pratique). Pas de "creux" narratif.
**Règle dérivée :** chaque H2 = au moins 1 chiffre sourcé + 1 cas concret + 1 implication pratique. Pas de section uniquement descriptive.

### LEARN-029 — Front-Loading systématique (règle d'écriture)
**Constat :** lors du balayage vertical du F-pattern, l'œil ne perçoit que les **2-3 premiers mots** de chaque ligne (sous-titres, paragraphes, bullets). Si le mot porteur de sens n'est pas en tête, le lecteur passe à côté.
**Règle :** tous les sous-titres, paragraphes et items de listes commencent par les mots les plus informatifs.
**Exemple :**
- ❌ *« La faute du conducteur est régie par l'article 4 de la loi Badinter… »*
- ✅ *« Article 4 Badinter : la faute du conducteur peut limiter… »*

### LEARN-030 — Règles quantitatives validées par recherche cognitive
**Phrases :**
- **Idéal : 16-20 mots** (équilibre compréhension/effort)
- **Limite haute absolue : 40 mots** (au-delà = surcharge mémoire de travail, perte du sujet)
**Paragraphes :**
- **Idéal : 1-3 phrases** par paragraphe (chunk digeste)
- **Une seule idée par paragraphe** (mémoire de travail = 5-9 chunks max)
**Section :**
- **Pas plus de 5-9 unités d'information** par section avant un saut visuel (encadré, sous-titre, liste)
**À ajouter dans la checklist qualité d'`ARTICLE_TEMPLATE.md`.**

### LEARN-031 — CTA "double-face" (Modèle de Probabilité d'Élaboration)
**Constat :** sur un lecteur en quête d'info gratuite (pas un prospect), un CTA purement promotionnel est rejeté. Reconnaître **explicitement les limites** de l'accompagnement augmente la crédibilité perçue (validé par recherche sur la persuasion).
**Pattern à appliquer sur Mini-CTA #1 (post-empathie) :**
> *« Vous êtes [persona] confronté à [situation] ? Ce guide gratuit couvre 80 % des situations. Pour les 20 % restants — [cas complexes spécifiques] — un avocat fait la vraie différence. [CTA spécifique →] »*
**Pourquoi ça marche :** reconnaît l'utilité de l'article (le lecteur n'est PAS obligé de cliquer), précise pour qui c'est utile (filtre les clients potentiels), montre une humilité qui inspire confiance.
**Hypothèse à mesurer :** ce pattern pourrait débloquer le 0 % conversion observé historiquement sur la catégorie Ressources et notions juridiques.

### LEARN-032 — Théorie de la fluidité de traitement
**Constat :** le cerveau associe la facilité de traitement (perceptuel : contraste, police claire / conceptuel : structure simple, mots familiers) à des **signaux de vérité et de crédibilité**. Le même contenu rédigé "facile" est jugé plus VRAI qu'écrit "difficile".
**Implication design :** notre ton sobre + structure claire + design épuré n'est pas qu'esthétique — c'est un **levier de crédibilité scientifiquement validé**. Confirme la voie Plouton, et justifie de ne JAMAIS basculer vers un design plus "marketing" ou complexe.
**À documenter** comme principe stratégique.

### LEARN-033 — 3 patterns de balayage visuel
| Pattern | Comportement lecteur | Implication design |
|---|---|---|
| **F-Pattern** | Balayage horizontal sur les 2 premiers paragraphes + descente verticale gauche | Info clé dans les 2 premiers paragraphes, front-loading des bordures gauches |
| **Layer-cake Pattern** (sliding readers) | Balayage **uniquement des titres et sous-titres**, ignore le corps | Titres **descriptifs et informatifs** (pas ornementaux) — le lecteur doit pouvoir reconstituer l'article en ne lisant que H2/H3 |
| **Spotted Pattern** (balayage tacheté) | Saute les blocs de texte, cherche les **mots en gras, chiffres, liens** | Gras stratégique (jamais décoratif), chiffres saillants, liens explicites |

Notre article doit servir **les 3 patterns simultanément**.

### LEARN-034 — Données chiffrées du comportement lecteur web
- **25 % du texte lu** en moyenne sur une visite (Nielsen Norman Group)
- **Visite < 1 minute** en moyenne
- **67 % d'abandon de formulaire** sur la moindre friction
- **Commitment Pattern** (lecture profonde) ne s'active que **si le balayage initial convainc** → on conçoit D'ABORD pour le scanner, ensuite pour le lecteur profond
**Implication :** chaque article doit être "scannable seul" — un scanner doit pouvoir extraire les infos clés sans lire le corps.

### LEARN-035 — Storytelling cognitif (détails perceptuels + conceptuels)
**Constat :** un récit intégré au début d'un article modifie l'encodage cérébral et capte mieux l'attention qu'une exposition factuelle.
**Détails à intégrer :**
- **Perceptuels** : faisant appel aux sens (vue, son, toucher) — *« le bruit de la chute… le casque qui roule sur l'asphalte… »*
- **Conceptuels** : faisant appel aux émotions / introspection — *« le moment où vous réalisez que vous n'êtes plus le même… »*
**Application :** notre Intro Version D applique déjà partiellement ce principe (vérité psychologique en phrase 1). À **amplifier** dans les ouvertures de sections H2 cruciales (préjudice esthétique, perte d'agrément, etc.).

### LEARN-036 — Charge d'implication (Need + Search + Evaluation — Laufer & Hulstijn)
**Constat :** pour qu'un concept juridique soit MÉMORISÉ par le lecteur (et pas juste lu en passant), 3 conditions :
1. **Need** : besoin perçu de comprendre ce concept
2. **Search** : mini-effort mental pour saisir le sens (contexte plutôt que définition donnée d'emblée)
3. **Evaluation** : le lecteur compare le concept à sa propre situation
**Implication structure :** dans H2 "Postes de préjudice", au lieu de lister/définir, poser une situation ("vous avez des cicatrices sur le visage") puis amener le lecteur à découvrir le poste qui s'applique (PEP). Active les 3 leviers, génère un encodage profond.

### LEARN-037 — CTAs vagues à proscrire (parfum d'information faible)
**Règle stricte :** bannir absolument *"En savoir plus"*, *"Cliquez ici"*, *"Contact"*. Ces formulations ont un **parfum d'information faible** et n'indiquent pas le bénéfice.
**Pattern à appliquer :**
- ❌ *"En savoir plus"*
- ✅ *"Parler à un avocat spécialisé en accidents de la route"*
- ❌ *"Contact"*
- ✅ *"Demander un premier RDV d'information (gratuit, sans engagement)"*
**À coder dans la checklist qualité d'`ARTICLE_TEMPLATE.md`.**

### LEARN-038 — Bannir le jargon obscur dans les éléments scannés
**Constat :** les titres, sous-titres et libellés de liens sont scannés rapidement. Si le lecteur doit faire un **effort sémantique** pour comprendre le sens, il **l'ignore**.
**Règle :** dans tous les éléments à fort balayage (H2, H3, ancres de liens), utiliser le vocabulaire **du lecteur** (qui n'est pas juriste), pas celui du cabinet. Le jargon technique reste OK dans le corps du paragraphe, **avec une définition immédiate**.
**Exemple :**
- ❌ H3 : « Le préjudice d'affection »
- ✅ H3 : « Ce que perdent vos proches : le préjudice d'affection »

---

## Capitalisation Google Core Updates mars-avril 2026 (source : Lucid Media)

> Source : [Lucid Media — Google March-April 2026 Core Updates](https://www.lucidmedia.co.nz/blog/google-march-april-2026-core-updates/) — audit fait sur article #2, intégré 2026-05-11. 10 learnings durables pour tous les articles à partir de #3.

### LEARN-039 — Information Gain : le signal primaire des Core Updates 2026
**Constat (Lucid Media) :** *« Pages that say what every other top-10 page already says are being demoted. Pages that add a unique angle, a piece of original data, or a first-hand experience are being lifted. »*
**Règle :** chaque article doit contenir **au moins 2-3 éléments distinctifs absents du top 10 SERP** identifiés en Étape 2 (gap analysis). Sans ça, on est désindexé/déclassé. Sur l'article #2, 6 gaps occupés (médecine esthétique, exercice illégal ×10, étape 0 reprise, diffamation datée, tourisme médical, motif officiel ONIAM 44,7 %).
**Procédure Étape 2 enrichie :** dans Bloc B (SEO), formaliser une **section « gap analysis »** (déjà en place — confirmer 5+ gaps occupables, sinon abandonner le sujet ou pivoter).

### LEARN-040 — Bio auteur YMYL obligatoire (E-E-A-T renforcé)
**Constat (Lucid Media) :** *« YMYL sites without verified author credentials… hit hardest »* sur les Core Updates 2026.
**Règle (durable) :** chaque article juridique doit se terminer par un **bloc « À propos de l'auteur »** (~150 mots) reprenant : nom complet + titre (Avocat au Barreau de Bordeaux) + année d'inscription au Barreau (2004) + cursus (EFB + DESS droit affaires + DEA droit européen + master HEC) + appartenances professionnelles (IDC, ADAP, IDA) + années d'expérience + adresse du cabinet + lien vers `/notre-cabinet` + lien vers `/honoraires-rendez-vous`. **Photo HD recommandée** (gérée côté Wix).
**Template prêt-à-coller** : voir `ARTICLE_TEMPLATE.md` section *« Bio auteur Maître Plouton »*.
**Anti-pattern :** signature anonyme *« Cabinet Plouton »* uniquement (article #2 V1 avant correction).

### LEARN-041 — Schema markup : FAQPage uniquement par article (le reste géré côté site Plouton)
**Contexte :** décision Nicolas 2026-05-11.
**Constat :** le site `jplouton-avocat.fr` (Wix Studio) gère déjà au niveau global les schémas d'autorité (Person Maître Plouton, LegalService Cabinet Plouton, navigation). Dupliquer ces schémas dans chaque article créerait du **doublon** (mauvais signal Google) sans bénéfice supplémentaire.
**Règle (durable) :** par article, on livre **uniquement le Schema FAQPage** — bloc `<script type="application/ld+json">` minifié one-liner avec les 8-10 questions de la FAQ (LEARN-044). Pas de `@graph`, pas de Person/LegalService/Article/BreadcrumbList répétés.
**Livraison** : dans le chat (LEARN-027), à coller dans le champ « Marquage structuré » du panneau SEO Wix Studio du draft post.
**À tester** après publication : [Google Rich Results Test](https://search.google.com/test/rich-results) sur l'URL publiée — vérifier que FAQPage est détecté **en plus** des schémas globaux du site (pas en doublon).
**Anti-pattern documenté :** sur l'article #2, j'avais proposé un `@graph` étendu 5 schémas (Person + LegalService + Article + Breadcrumb + FAQPage). À ne PAS reproduire — risque doublon + sources de confusion pour Nicolas (4 fichiers .md modifiés pour rien).

### LEARN-042 — Local-first / Ancrage géographique systématique (GEO 2026)
**Constat (Lucid Media) :** *« Local-first content held up better. Sites that lean into local case studies, local data, and locally relevant examples saw less impact. »*
**Règle (durable Cabinet Plouton) :** chaque article doit inclure **au minimum 3 ancrages locaux Bordeaux/Nouvelle-Aquitaine** :
- 1 mention de la **juridiction compétente** locale (tribunal judiciaire de Bordeaux pour le ressort Gironde/Dordogne/Lot-et-Garonne/Charente, OU cour d'appel de Bordeaux, OU CCI Grand Ouest, OU CIVI Gironde, etc. — selon thématique)
- 1 mention de l'**adresse du cabinet** (45 Cours d'Alsace-et-Lorraine, Bordeaux) — typiquement dans le CTA final
- 1 mention de la **zone d'intervention** (Nouvelle-Aquitaine et au-delà)
**Exemple validé** : article #2 H3.5.2 (CCI Grand Ouest), H3.5.3 (tribunal judiciaire de Bordeaux), CTA final (adresse cabinet).

### LEARN-043 — Date de mise à jour visible (signal fraîcheur)
**Constat (Lucid Media) :** *« Revoir articles classées tous 6 mois (refresh dates) »* — la dateModified visible est un signal positif.
**Règle :** terminer chaque article par une mention italique **« Dernière mise à jour : [mois année]. »** Cohérent avec le `dateModified` du Schema Article (LEARN-041).
**Procédure refresh :** voir LEARN-046 — relecture/mise à jour tous les 6 mois des articles classés top 10.

### LEARN-044 — FAQ 8-10 questions (vs 5-7 précédemment)
**Constat (Lucid Media) :** *« Minimum 8-10 FAQ intégrées »* pour citabilité LLM et AI Overviews maximale.
**Règle (mise à jour) :** la FAQ Plouton passe de **5-7 questions à 8-10 questions** systématiques. Mix : 5 PAA SERP exploitables (DataForSEO Étape 2-B) + 3-5 questions issues des gaps éditoriaux (informations clés que les concurrents ne traitent pas).
**Format inchangé** : réponses 40-80 mots, concept-clé en ouverture (LEARN-017), sourcing intégré.
**Validation article #2** : 9 questions au final (6 initiales + 3 ajoutées en Vague 2 : délai prescription, CCI vs ONIAM, consultation préalable).

### LEARN-045 — AI Overviews : cibler la nuance, pas le factuel simple
**Constat (Lucid Media) :** *« AI Overviews are eating the click… sites are losing clicks not because they ranked lower but because Google answered the question without sending the user through. »*
**Règle stratégique :** privilégier les angles à **nuance juridique non triviale** qu'un AI Overview ne peut pas trancher en 2 lignes :
- ✅ *« Pourquoi l'ONIAM ne vous indemnisera (presque) jamais — sauf si l'acte est réparateur »* (nuance + débat)
- ❌ *« Qu'est-ce que l'ONIAM ? »* (factuel pur — risque AI Overview)
**Pour la FAQ** : préférer les questions de positionnement/arbitrage *(« Puis-je écrire sur Google sans risquer la diffamation ? »)* aux questions définitionnelles (*« Qu'est-ce que la diffamation ? »*).

### LEARN-046 — Refresh articles classés tous les 6 mois (durabilité ranking)
**Constat (Lucid Media) :** *« Cadence réduite : 1 article pilier/mois vs 4 articles légers. »* + *« Revoir articles classées tous 6 mois. »*
**Règle (process pipeline) :** tenir un **calendrier de refresh** des articles publiés. Tous les 6 mois après publication :
1. Vérifier les chiffres datés (ONIAM RA N+1 sorti ? Mornet mis à jour ?)
2. Mettre à jour la `dateModified` (Schema Article) + la mention italique en pied (LEARN-043)
3. Ré-auditer les top 10 SERP (nouveau concurrent ? nouvel angle à occuper ?)
4. Si jurisprudence majeure : ajouter en H2 dédié ou en FAQ
**Stockage :** noter la date de prochain refresh dans le commit message du push initial (`Article #N : refresh prévu YYYY-MM`).

### LEARN-047 — Concentration ressources : 3 deep clusters > 30 shallow
**Constat (Lucid Media) :** *« A site with three deep clusters covering one topic well will outperform a site with thirty shallow clusters. »*
**Implication pipeline Plouton :** plutôt que 24 articles sur 24 sujets disjoints, structurer en **clusters profonds** :
- Cluster 1 : Accidents de la route (article #1 motard + futurs articles automobiliste/piéton/passager)
- Cluster 2 : Erreurs médicales (article #2 chirurgie esthétique + ONIAM/aléa/dossier médical + futurs articles)
- Cluster 3 : Pénal/violences (à construire)
**Règle :** chaque nouvel article doit cross-linker **3-5 articles du même cluster** (déjà publiés) ET être référencé en retour par un article pilier futur. Penser le maillage interne dès l'Étape 3 (plan).

### LEARN-048 — Synthèse profonde = données « originales » substitutives
**Constat (Lucid Media) :** *« Synthesis at depth. Pulling together five disparate sources into a coherent argument »* peut compenser l'absence de données primaires.
**Règle pour les articles en prospection** (sans historique cabinet — V3 article #2) : compenser le manque de cas réels par une **synthèse originale documentée** :
- Agrégation de séries chiffrées éclatées (ex. article #2 : série signalements Ordre 2021→2025 ×10, jamais publiée groupée)
- Cross-tabulation de plusieurs sources officielles (ONIAM + ANSM + DGCCRF + Ordre des médecins dans un même tableau)
- Mise en regard jurisprudence + texte CSP + chiffre ONIAM (sourcing croisé qu'un AI Overview ne peut pas reconstituer)
**Anti-pattern :** copier les chiffres bruts de Wikipedia ou paraphraser un article concurrent — déclassement assuré.

---

## Méta-learning sur le pipeline

### LEARN-META-1 — Une session ≠ tout le workflow
**Constat :** une seule session conversation a permis de boucler tout le workflow 4 étapes pour l'article #1 (cadrage, collecte, plan, rédaction). Les artefacts sont sauvegardés localement et accessibles cross-sessions via la mémoire persistante (`memory/`).
**Pour les articles suivants :** repartir des memos + de `BRIEF.md` + `ARTICLE_TEMPLATE.md` + les learnings ci-dessus. Pas besoin de tout re-expliquer.
