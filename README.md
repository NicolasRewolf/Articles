# Pipeline éditorial — Cabinet Plouton

> **Tu démarres une session Claude Code sur ce projet ? Lis ce fichier en premier.**
> Tu as ici tout le contexte opérationnel pour produire un article sans perdre de temps.

---

## Quick Start

Ce projet est un **pipeline éditorial SEO/GEO** pour le Cabinet Plouton (avocat pénaliste & défense des victimes, Bordeaux — [jplouton-avocat.fr](https://www.jplouton-avocat.fr)). Cible : **24+ articles** dans la catégorie *"Ressources et notions juridiques"*, workflow agile en **4 étapes** avec STOP+validation entre chaque.

**Pour démarrer un article :**
1. L'utilisateur (Nicolas) écrit : *"Article #N — sujet : [X]"*
2. Tu poses 3 questions minimales de cadrage (sujet précis, expertise cible, cadence)
3. Tu attaques l'**Étape 1**

**À lire avant d'attaquer** :
- [`BRIEF.md`](BRIEF.md) — brief utilisateur intégral (workflow détaillé, ton, critères qualité)
- [`ARTICLE_TEMPLATE.md`](ARTICLE_TEMPLATE.md) — structure des livrables, checklist qualité (bio auteur, JSON-LD FAQPage seul, FAQ 8-10)
- [`LEARNINGS.md`](LEARNINGS.md) — **journal vivant**. Observations fraîches non encore stabilisées + procédure de digestion à reproduire avant chaque nouvel article (date de la dernière digestion en tête du fichier).
- [`LEARNINGS-archive.md`](LEARNINGS-archive.md) — **historique des learnings promus** vers BRIEF/TEMPLATE, avec la cartographie des destinations + les savoirs techniques/stratégiques préservés comme référence consultable. *(Comptes et plages de numéros : voir la cartographie elle-même — ce README ne duplique aucun chiffre, ils dérivaient à chaque digestion.)*
- `MEMORY.md` (auto-chargée en système prompt) — règles durables non négociables. **Source unique : `~/.claude/projects/-Users-nicolas-Desktop-Articles/memory/`** ; le rappel plus bas est un index de lecture, pas une copie normative.

**Gouvernance des 4 fichiers** :

| Fichier | Rôle | Mise à jour |
|---|---|---|
| `BRIEF.md` | Règles durables business + ton + workflow + outils. Auto-suffisant. | Rare, validation Nicolas obligatoire. |
| `ARTICLE_TEMPLATE.md` | Squelette structurel des livrables + checklist qualité. Auto-suffisant. | Modérée, à chaque évolution structurelle confirmée. |
| `LEARNINGS.md` | Journal vivant — observations fraîches en attente de promotion. **Vise < 100 lignes**. | Post-article + digestion avant chaque nouvel article. |
| `LEARNINGS-archive.md` | Historique append-only des learnings promus + savoirs techniques préservés. | Append seulement (jamais éditer le passé). |

**Critère de promotion** : défini une seule fois, en tête de [`LEARNINGS.md`](LEARNINGS.md) (**≥ 2 conditions sur 3**), avec la procédure de digestion en pied du même fichier. Ne pas le reformuler ici — c'est ainsi que les deux versions avaient divergé.

---

## Carte du projet

```
~/Desktop/Articles/
├── README.md                 ← TU ES ICI (point d'entrée : carte + pointeurs, aucune règle)
├── BRIEF.md                  ← brief utilisateur (workflow 4 étapes, ton, outils) — la constitution
├── ARTICLE_TEMPLATE.md       ← structure des livrables + Cap général (maison des chiffres structurels)
├── LEARNINGS.md              ← journal vivant (< 100 lignes) — observations fraîches non promues
├── LEARNINGS-archive.md      ← historique append-only des learnings promus + savoirs préservés
├── .env                      ← credentials PISTE Data Gouv (GITIGNORED)
├── .env.example              ← template des variables d'environnement
├── .gitignore                ← exclusions
├── scripts/                  ← helpers Python (stdlib only)
│   ├── piste_auth.py         ← client PISTE : OAuth + appels (`PisteClient`)
│   ├── legifrance.py         ← wrapper Légifrance API
│   ├── judilibre.py          ← wrapper Judilibre API
│   ├── dataforseo.py         ← wrapper DataForSEO (volumes, SERP, PAA, solde)
│   ├── politique_liens.py    ← convention de liens LEARN-024 — source unique
│   │                            partagée par le rendu Ricos et le garde-fou
│   ├── md_to_ricos.py        ← parser markdown → Ricos JSON (push Wix)
│   ├── lint_pipeline.py      ← garde-fou : vérifie les règles mécanisables (cf. §Garde-fous)
│   ├── run_tests.py          ← lance toutes les suites (`python3 scripts/run_tests.py`)
│   └── test_*.py             ← suites de tests (stdlib, aucun appel réseau)
└── NN-slug-article/          ← un dossier par article (NN = numéro chronologique, slug sans accent)
    ├── etape-1-cadrage.md    ← livrable Étape 1
    ├── etape-2-collecte.md   ← livrable Étape 2
    ├── etape-3-plan.md       ← livrable Étape 3
    ├── etape-4-article.md    ← livrable Étape 4 (article complet)
    ├── etape-4-metadonnees-wix.md  ← méta SEO prêtes à coller (8 sections)
    ├── ricos.min.json        ← livrable Étape 4 : contenu Ricos poussé en draft Wix
    └── (optionnels) inventaire-categorie-ressources.md (Bloc C), etape2-raw/, sources-a-exploiter.md
```

**Exceptions connues de l'arborescence** (ne pas s'en étonner) : pas de dossier `06-` (renumérotation 06→05, commit `a10dffa`) ; deux dossiers `08-` coexistent — `08-sinistre-habitation-assurance` est l'article #8 publié, `08-indemnisation-morsure-chien` est **gelé** (article à réécrire, renumérotation au moment de la reprise — décision Nicolas 2026-08-05) ; `01-.../etape-4-faq-schema-paste.html` est un **reliquat pré-LEARN-027** conservé comme archive, il ne préfigure aucun livrable (le JSON-LD se livre dans le chat).

---

## Workflow 4 étapes — synthèse 1 page

| Étape | Livrable | Outils principaux | STOP attendu |
|---|---|---|---|
| **1 — Cadrage** | `etape-1-cadrage.md` (sujet, intent, persona, long-tail, page cible, hypothèse de valeur) | WebSearch, DataForSEO (light) | Oui — validation H1/persona/page cible |
| **2 — Collecte** | `etape-2-collecte.md` (4 blocs : A juridique, B SEO, C interne, D stats) | WebSearch ciblée + PISTE (Judilibre/Légifrance), DataForSEO, Wix MCP (dont inventaire catégorie Ressources), data.gouv (MCP `datagouv` ou API ouverte) | Oui — décision angle confirmé sur data SERP |
| **3 — Plan** | `etape-3-plan.md` (H1+variantes, méta-tags, slug, plan H2/H3 justifié, stratégie liens, stratégie GEO) | — (rédaction du plan) | Oui — validation plan + intro + TDM + volume |
| **4 — Rédaction + push** | `etape-4-article.md` + `etape-4-metadonnees-wix.md` + `ricos.min.json` + JSON-LD FAQ (livré dans le chat) | WebSearch ciblée + API PISTE (fact-check), `md_to_ricos.py` + Wix MCP (push draft), `lint_pipeline.py`, Git/GitHub | Oui — validation finale avant push Wix + GitHub |

**Règle d'or** : à chaque fin d'étape, livrable produit → STOP → validation explicite Nicolas ("OK go") → étape suivante. **Une action à la fois**, pas de chaînage `&&`, pas de parallélisation suggérée sans accord.

---

## Tableau MCPs → étapes

À charger via `ToolSearch` au moment opportun :

| Étape | Outil | Usage |
|---|---|---|
| **2-A** Juridique | WebSearch ciblée | `allowed_domains=["legifrance.gouv.fr"]` + courdecassation.fr + juricaf.org — **1er recours fact-check** |
| **2-A** Juridique | scripts locaux | `python3 scripts/judilibre.py search "..."` (jurisprudence) et `python3 scripts/legifrance.py code "<Code>" "<n°>"` / `search --fond LODA_DATE` (textes) — via Bash. **Discipline de version : BRIEF.md §4 Bloc A** |
| **2-B** SEO | **scripts locaux** | `python3 scripts/dataforseo.py solde` (gratuit) · `volumes "kw1" "kw2" …` · `serp "requête" --paa 2` — **chemin par défaut**, indépendant de l'état du MCP |
| **2-B** SEO | DataForSEO MCP *(secours)* | `mcp__dataforseo__serp_organic_live_advanced` (avec PAA), `kw_data_google_ads_search_volume`, `dataforseo_labs_google_keyword_overview` — **à ne pas attendre** : le serveur n'est pas chargé dans toutes les sessions |
| **2-C** Interne Plouton | Wix MCP | `mcp__cde94955-..._CallWixSiteAPI` (query categories + posts) |
| **2-C** Interne Plouton | curl Bash | scrape HTML brut + parse JSON-LD pour extraire détails affaires cabinet |
| **2-D** Stats | MCP `datagouv` (`https://mcp.data.gouv.fr/mcp`, scope user depuis le 2026-08-24) | outils `mcp__datagouv__*` (recherche + query datasets) ; **fallback sans MCP** : API ouverte `https://www.data.gouv.fr/api/1/` en curl (LEARN-078) |
| **2-D** Stats | WebFetch | sources officielles (ONISR, ONIAM, INSEE, etc.) |
| **3-4** Fact-check obligatoire (LEARN-026 + LEARN-049 anti-récidive) | WebSearch ciblée + **API PISTE** (`legifrance.py` / `judilibre.py`) en contrôle | Avant chaque affirmation juridique précise (n° article, n° pourvoi, fondement) ; si non confirmé → reformulation prudente + `⚠️ À vérifier` |
| **4** Ingestion Wix | `md_to_ricos.py` + Wix MCP (`ExecuteWixAPI`) | **Push API draft = flux par défaut** : markdown → `ricos.min.json` minifié → POST en draft **`UNPUBLISHED`** (scope SITE), garde-fou `nodes.length`/`faqCount` avant POST + vérif `GET`. Détail : BRIEF.md §4 (LEARN-064). Fallback : copier-coller markdown par Nicolas (LEARN-002/004) |
| **4** Contrôle qualité | scripts locaux | `python3 scripts/lint_pipeline.py NN-slug-article/` avant livraison et avant commit |
| **4** Git/GitHub | Bash | `git add -A`, `git commit`, `git push origin main` (sur confirmation explicite) |

---

## Règles non négociables (index de lecture — la source est la mémoire persistante)

Auto-chargées en début de session via `MEMORY.md`. **Source unique et normative : `~/.claude/projects/-Users-nicolas-Desktop-Articles/memory/`** — cette liste est un index de rappel, à resynchroniser à chaque digestion (elle avait dérivé, figée à 6 règles alors que la mémoire en portait davantage).

1. **Slugs sans accent** — règle stricte pour les nouveaux articles Wix (translittération obligatoire). Pas d'audit rétro.
2. **Liens internes follow / externes nofollow** — internes (`jplouton-avocat.fr/...`) = pas de `rel`, pas de `target="_blank"`. Externes = `target="_blank" rel="noopener noreferrer nofollow"`.
3. **Pas de bullets dans blockquotes Wix** — listes à puces interdites dans citations. Encadrés chiffrés en prose continue (séparateurs `;` ou `—`).
4. **Fact-check juridique obligatoire AVANT rédaction** — toute affirmation juridique précise (n° article, jurisprudence) validée d'abord via WebSearch ciblée (Légifrance/courdecassation.fr/juricaf.org) + contrôle API PISTE (`scripts/legifrance.py`, `scripts/judilibre.py`) ; si non confirmé → reformulation prudente + `⚠️ À vérifier`. *(NotebookLM retiré du protocole le 2026-08-24 — décision Nicolas.)*
5. **JSON-LD livré dans le chat** — schemas markup Wix (FAQPage, etc.) livrés en bloc code Markdown dans la conversation, minifié one-liner, avec `type="application/ld+json"`. Pas de fichier HTML intermédiaire.
6. **Repo Git/GitHub** — `~/Desktop/Articles` lié à `github.com/NicolasRewolf/Articles.git`. Commit après chaque article. Push **sur confirmation explicite uniquement** (jamais auto).
7. **Voix victime / main tendue** — 7 réflexes opérationnels (BRIEF.md §2), modulés selon victime / défense pénale / contrats-famille. Précision juridique non négociable.
8. **Affaire cabinet citée = lien interne obligatoire** — toute mention d'une affaire réelle (cas, montant obtenu, « nos dossiers »), FAQ et encadrés inclus, porte un lien vers son post. Ancre neutre OK ; slug publié réel via Wix MCP.
9. **Inventaire de la catégorie Ressources avant chaque article** — query Wix par `categoryId 9477320f-…` au cadrage : anti-cannibalisation + maillage notion↔notion.
10. **Tags en CSV (virgules)** — jamais de middot `·`, pour un copier-coller direct dans Wix.

---

## Garde-fous mécaniques (`scripts/lint_pipeline.py`)

Les règles **mécanisables** ne vivent pas seulement en prose : elles sont vérifiées par un script. Une règle en prose finit toujours par dériver (la règle « tags en virgules » a été violée sur 5 articles consécutifs avant d'être outillée).

```bash
python3 scripts/lint_pipeline.py
```

Sans argument, le lint vérifie **tout le repo** (docs de gouvernance + tous les dossiers d'articles) ; avec un chemin (`python3 scripts/lint_pipeline.py 11-faute-inexcusable-employeur/`), il ne vérifie que ce dossier.

**Quand le lancer** : en fin d'Étape 4 avant de livrer, et avant chaque commit d'article. Il sort en code 1 si une règle est violée. Ce qu'il couvre (détail et messages dans le script) : longueurs méta, slug sans accent, format et nombre de tags, liens internes absolus, bio auteur présente, FAQ (nombre de questions, position, présence dans la TDM), CTAs, cohérence `ricos.min.json` ↔ article, équilibre des fences markdown, unicité des préfixes de dossiers, absence de compteurs figés dans la documentation.

---

## Quirks & workarounds connus

| Friction | Workaround validé |
|---|---|
| **Python 3.14 macOS — SSL CERTIFICATE_VERIFY_FAILED** sur les scripts `scripts/*.py` | **Workaround unique (ce tableau fait foi)** : exporter le bundle de certificats système avant l'appel — `export SSL_CERT_FILE=/etc/ssl/cert.pem` (stdlib, aucune dépendance tierce). Si la friction persiste : fallback **curl + python3 inline** depuis Bash. *Ne pas utiliser `SSL_CERT_FILE=certifi` : `certifi` est un package tiers et la valeur attendue est un chemin de fichier PEM.* |
| **Légifrance bloque WebFetch / curl** (Cloudflare anti-bot) | Passer par l'**API** : `scripts/legifrance.py code` (codes) ou `search --fond LODA_DATE` (lois/décrets/arrêtés) — souscription active depuis le 2026-08-07, elle donne le verbatim **et** les bornes d'application. **WebSearch avec `allowed_domains=["legifrance.gouv.fr"]`** reste le recours rapide de confirmation. Discipline de version obligatoire : BRIEF.md §4 Bloc A. |
| **Taille du push Wix** | Le plafond n'est pas l'API (400 Ko/post, jamais atteint) mais le **transport** : ce qu'une lecture de fichier rend d'un coup pour être embarqué dans `ExecuteWixAPI`. Les articles ont grossi et franchissent désormais ce seuil (LEARN-073). **Workaround : compaction sémantique avant envoi** — procédure dans BRIEF.md §4 « Push Wix ». *L'ancien diagnostic « échec > 25K tokens » était une limite de corps d'appel outil, pas de l'API.* En dernier recours : copier-coller markdown dans Wix Studio. |
| **`sante.gouv.fr` bloque WebFetch** (écran CAPTCHA Cegedim), comme Légifrance | Passer par WebSearch ou par les pages ARS régionales (LEARN-073). |
| **Le serveur MCP `dataforseo` n'est pas chargé dans toutes les sessions** (déclaré en global, mais dépend d'un `npx` qui peut échouer sans message) | Ne pas l'attendre : `python3 scripts/dataforseo.py` fait le même travail à partir des credentials déjà présents sur la machine. Tester avec `solde` (gratuit) avant toute commande facturée. |
| **Wix Studio rejette `<script>...</script>` pour JSON-LD avec erreur de format** | **Livrer le bloc dans le chat** (bloc code Markdown), minifié one-liner avec `type="application/ld+json"`. |
| **Slugs accents existants sur le site Plouton** | Ne PAS auditer (décision Nicolas 2026-05-11). Règle slug-sans-accent uniquement pour les NOUVEAUX articles. |

---

## Procédure type — démarrer l'article #N

```
1. Nicolas écrit : "Article #N — sujet : [X]"
2. Tu réponds avec 3 questions de cadrage minimales (via AskUserQuestion ou texte) :
   - Sujet précis ou angle (s'il veut challenger)
   - Famille d'expertise cible (parmi les 14 pages d'expertise)
   - Cadence / contexte (test, production régulière, sprint)
3. Sur ses réponses → tu lances Étape 1.
4. STOP fin Étape 1 → validation → Étape 2.
5. Bloc B en premier (SERP+volumes+PAA via DataForSEO) → ça résout souvent l'incertitude sur l'angle.
6. STOP fin Étape 2 → validation → Étape 3.
7. Étape 3 : plan H2/H3 + intro Version D + TDM + mini-CTAs.
8. STOP fin Étape 3 → validation → Étape 4.
9. Étape 4 :
   a. Fact-check juridique d'abord via WebSearch ciblée (Légifrance/courdecassation.fr/juricaf.org) + contrôle API PISTE (`legifrance.py` / `judilibre.py`).
   b. Si non confirmé → reformulation prudente + `⚠️ À vérifier` (LEARN-021 + LEARN-049), signalé à Nicolas.
   c. Produire les 4 livrables Étape 4 (article.md + metadonnees-wix.md + ricos.min.json + JSON-LD FAQPage dans le chat).
   d. Lancer `python3 scripts/lint_pipeline.py NN-slug-article/` et corriger toute erreur avant de livrer.
   e. Pousser le draft Wix **`UNPUBLISHED`** par API (flux par défaut, BRIEF §4) ; fallback copier-coller markdown si l'API échoue.
   f. Méta-données SEO renseignées via le panneau SEO Wix Studio (slug, titre, description, **2 catégories** = Ressources et notions juridiques + thématique, tags, image hero + alt, JSON-LD FAQPage).
   g. Mise à jour LEARNINGS.md + ARTICLE_TEMPLATE.md si nouveau pattern.
10. Commit Git local : `git add -A`, vérifier que `.env` n'est pas inclus, puis `git commit -m "Article #N : slug"` (+ mention refresh prévu M+6 — LEARN-046). Pas de chaînage `&&`.
11. Push GitHub sur "OK push" explicite uniquement (`git push origin main`).
```

---

## Pages d'expertise cibles

→ Liste complète des 14 URLs dans **[BRIEF.md §2](BRIEF.md)**. Page conversion principale : `/honoraires-rendez-vous`.

---

## Catégories Wix Blog (pour publication)

| Catégorie | ID Wix |
|---|---|
| **Ressources et notions juridiques** (catégorie cible publication articles) | `9477320f-5902-40e9-ace3-b0e3b6b8b51f` |
| **Accidents de la route** | `34cbb933-76d6-4a2e-8048-7624dcbe738d` |
| **Victimes de délits ou crimes** | `a755253f-65a6-49cc-b89e-e10e83840a75` |
| **Droit Pénal** | `8dad2d49-d0e2-40c3-be1c-02baaf57e3cd` |
| **Procès criminels** | `c730402c-de41-413e-be71-88fc00a0f741` |
| **Violences Conjugales et féminicides** | `857f17e1-837b-4665-a80a-2f3baa9c5262` |
| **Trafic de stupéfiants** | `bfd9c9df-cddc-4a53-b903-c98c089c8523` |
| **Droit pénal des affaires** | `d504fbe1-e1c9-4df1-9189-963e0856e816` |
| **Accidents et erreurs médicales** | `0c769ec1-307b-413a-bcce-7b4e5d546c4b` |
| **Droit et accidents du travail** | `ed75e638-104d-42ec-8e85-7ddb79e0928b` |
| **Accidents de la vie courante** | `8bc927f8-b437-4bcd-939b-b31f17f23c08` |
| **Droit des assurances** | `edd6c343-05a3-4bf9-929e-527fad068557` |
| **Défense des consommateurs** | `93bcfb5b-f451-4804-9d43-ec04e287b44d` |
| **Droit de la famille** | `5151e5b0-01a7-4622-838b-cf615dcd6ce4` |

Le **Site ID Wix** du Cabinet Plouton : `0870235c-b92d-4a69-a2f4-25a976ae5f0c`.

Recommandation : taguer chaque article dans **2 catégories simultanées** (= Ressources et notions juridiques + la catégorie thématique).

---

## Volume cible & ton

→ Règles complètes dans **[BRIEF.md §2-3](BRIEF.md)** (ton éditorial, volume, cadence, voix victime, clusters) et **[ARTICLE_TEMPLATE.md](ARTICLE_TEMPLATE.md)** (Cap général + checklist qualité).

---

## En cas de doute

- Lis **`BRIEF.md`** pour le détail des règles business + workflow.
- Lis **`ARTICLE_TEMPLATE.md`** pour la structure des livrables + checklist qualité.
- Consulte **`LEARNINGS-archive.md`** pour comprendre le *pourquoi* d'une règle (chaque entrée est horodatée et liée à un article précis).
- Consulte **`LEARNINGS.md`** pour les observations fraîches en attente de digestion.
- Consulte **`~/.claude/projects/-Users-nicolas-Desktop-Articles/memory/MEMORY.md`** + les feedback files pour les règles durables auto-chargées (hors repo).
- Pose la question à Nicolas plutôt que d'extrapoler.

**Anti-hallucination** : ne JAMAIS inventer une donnée juridique. Toujours sourcer ou marquer ⚠️.

---

*Historique des mises à jour : `git log --oneline -- README.md`. Pas de date en dur ici — elle mentait (audit 2026-08-05). Le rafraîchissement de ce fichier fait désormais partie de la procédure de digestion (pied de `LEARNINGS.md`).*
