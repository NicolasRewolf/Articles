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
- [`LEARNINGS.md`](LEARNINGS.md) — **journal vivant** (allégé après digestion 2026-05-13). Contient les observations fraîches non encore stabilisées + la procédure de digestion à reproduire avant chaque nouvel article.
- [`LEARNINGS-archive.md`](LEARNINGS-archive.md) — **historique des 49 learnings promus** (LEARN-001 à LEARN-052) vers BRIEF/TEMPLATE, avec cartographie complète des destinations + 7 entrées techniques/stratégiques préservées comme référence consultable.
- `MEMORY.md` (auto-chargée en système prompt) — 6 règles durables non négociables.

**Gouvernance des 4 fichiers** (post-digestion 2026-05-13) :

| Fichier | Rôle | Mise à jour |
|---|---|---|
| `BRIEF.md` | Règles durables business + ton + workflow + outils. Auto-suffisant. | Rare, validation Nicolas obligatoire. |
| `ARTICLE_TEMPLATE.md` | Squelette structurel des livrables + checklist qualité. Auto-suffisant. | Modérée, à chaque évolution structurelle confirmée. |
| `LEARNINGS.md` | Journal vivant — observations fraîches en attente de promotion. **Vise < 100 lignes**. | Post-article + digestion avant chaque nouvel article. |
| `LEARNINGS-archive.md` | Historique append-only des learnings promus + savoirs techniques préservés. | Append seulement (jamais éditer le passé). |

**Critère de promotion** : un learning passe de `LEARNINGS.md` aux fichiers de règles quand il est (1) confirmé sur 2 articles distincts, (2) opérationnel, et (3) inutile à lire deux fois s'il vit déjà ailleurs. Procédure détaillée en pied de `LEARNINGS.md`.

---

## Carte du projet

```
~/Desktop/Articles/
├── README.md                 ← TU ES ICI (point d'entrée)
├── BRIEF.md                  ← brief utilisateur (workflow 4 étapes)
├── ARTICLE_TEMPLATE.md       ← structure réutilisable (à affiner après chaque article)
├── LEARNINGS.md              ← journal vivant (< 100 lignes) — observations fraîches non promues
├── LEARNINGS-archive.md      ← historique des 49 learnings promus + 7 savoirs techniques préservés
├── .env                      ← credentials PISTE Data Gouv (GITIGNORED)
├── .env.example              ← template
├── .gitignore                ← exclusions
├── scripts/                  ← helpers Python (stdlib only)
│   ├── piste_auth.py         ← OAuth PISTE (Légifrance + Judilibre)
│   ├── legifrance.py         ← wrapper Légifrance API
│   ├── judilibre.py          ← wrapper Judilibre API
│   └── md_to_ricos.py        ← parser markdown → Ricos JSON (push Wix)
└── 0N-slug-article/          ← un dossier par article (N = numéro, slug = sans accent)
    ├── etape-1-cadrage.md    ← livrable Étape 1
    ├── etape-2-collecte.md   ← livrable Étape 2
    ├── etape-3-plan.md       ← livrable Étape 3
    ├── etape-4-article.md    ← livrable Étape 4 (article complet)
    └── etape-4-metadonnees-wix.md  ← méta SEO prêtes à coller
```

---

## Workflow 4 étapes — synthèse 1 page

| Étape | Livrable | Outils principaux | STOP attendu |
|---|---|---|---|
| **1 — Cadrage** | `etape-1-cadrage.md` (sujet, intent, persona, long-tail, page cible, hypothèse de valeur) | WebSearch, DataForSEO (light) | Oui — validation H1/persona/page cible |
| **2 — Collecte** | `etape-2-collecte.md` (4 blocs : A juridique, B SEO, C interne, D stats) | NotebookLM, PISTE, DataForSEO, Wix MCP, data.gouv MCP | Oui — décision angle confirmé sur data SERP |
| **3 — Plan** | `etape-3-plan.md` (H1+variantes, méta-tags, slug, plan H2/H3 justifié, stratégie liens, stratégie GEO) | — (rédaction du plan) | Oui — validation plan + intro + TDM + volume |
| **4 — Rédaction + push** | `etape-4-article.md` + `etape-4-metadonnees-wix.md` + JSON-LD FAQ (livré dans le chat) | NotebookLM `ask_question` (fact-check obligatoire), Wix MCP (push draft), Git/GitHub | Oui — validation finale avant push Wix + GitHub |

**Règle d'or** : à chaque fin d'étape, livrable produit → STOP → validation explicite Nicolas ("OK go") → étape suivante. **Une action à la fois**, pas de chaînage `&&`, pas de parallélisation suggérée sans accord.

---

## Tableau MCPs → étapes

À charger via `ToolSearch` au moment opportun :

| Étape | Outil | Usage |
|---|---|---|
| **2-A** Juridique | WebSearch ciblée | `allowed_domains=["legifrance.gouv.fr"]` + courdecassation.fr + juricaf.org — **1er recours fact-check** |
| **2-A** Juridique | scripts locaux | `python3 scripts/judilibre.py search "..."` (via Bash) |
| **2-A** Juridique | **NotebookLM via Nicolas** (LEARN-022) | Si WebSearch ne suffit pas : Claude formule la question → Nicolas la pose à NotebookLM → Claude ingère la réponse. **PAS via MCP** par défaut (LEARN-050) |
| **2-B** SEO | DataForSEO MCP | `mcp__dataforseo__serp_organic_live_advanced` (avec PAA), `kw_data_google_ads_search_volume`, `dataforseo_labs_google_keyword_overview` |
| **2-C** Interne Plouton | Wix MCP | `mcp__cde94955-..._CallWixSiteAPI` (query categories + posts) |
| **2-C** Interne Plouton | curl Bash | scrape HTML brut + parse JSON-LD pour extraire détails affaires cabinet |
| **2-D** Stats | data.gouv.fr MCP | `mcp__33cdbda6-..._search_datasets`, `list_dataset_resources`, `query_resource_data` |
| **2-D** Stats | WebFetch | sources officielles (ONISR, ONIAM, INSEE, etc.) |
| **3-4** Fact-check obligatoire (LEARN-026 + LEARN-049 anti-récidive) | WebSearch ciblée d'abord, **NotebookLM via Nicolas en backup** | Avant chaque affirmation juridique précise (n° article, n° pourvoi, fondement) |
| **4** Ingestion Wix | **Copier-coller manuel par Nicolas** (LEARN-002 + LEARN-004) | Push API facultatif et fragile (échec > 25K tokens) |
| **4** Git/GitHub | Bash | `git add -A`, `git commit`, `git push origin main` (sur confirmation explicite) |

---

## Règles non négociables (rappel des mémoires persistantes)

Auto-chargées en début de session via `MEMORY.md`. Détails dans `~/.claude/projects/-Users-nicolas-Desktop-Articles/memory/`.

1. **Slugs sans accent** — règle stricte pour les nouveaux articles Wix (translittération obligatoire). Pas d'audit rétro.
2. **Liens internes follow / externes nofollow** — internes (`jplouton-avocat.fr/...`) = pas de `rel`, pas de `target="_blank"`. Externes = `target="_blank" rel="noopener noreferrer nofollow"`.
3. **Pas de bullets dans blockquotes Wix** — listes à puces interdites dans citations. Encadrés chiffrés en prose continue (séparateurs `;` ou `—`).
4. **Fact-check juridique obligatoire AVANT rédaction** — toute affirmation juridique précise (n° article, jurisprudence) validée d'abord via WebSearch ciblée (Légifrance/courdecassation.fr/juricaf.org), puis NotebookLM via Nicolas si doute ou source manquante.
5. **JSON-LD livré dans le chat** — schemas markup Wix (FAQPage, etc.) livrés en bloc code Markdown dans la conversation, minifié one-liner, avec `type="application/ld+json"`. Pas de fichier HTML intermédiaire.
6. **Repo Git/GitHub** — `~/Desktop/Articles` lié à `github.com/NicolasRewolf/Articles.git`. Commit après chaque article. Push **sur confirmation explicite uniquement** (jamais auto).

---

## Quirks & workarounds connus

| Friction | Workaround validé |
|---|---|
| **Python 3.14 macOS — SSL CERTIFICATE_VERIFY_FAILED** sur les scripts `scripts/piste_auth.py` etc. | Fallback **curl + python3 inline** depuis Bash (auth via les vars d'env de `.env`). Le système keychain macOS fonctionne via curl. |
| **Légifrance bloque WebFetch / curl** (Cloudflare anti-bot) | Pour vérifier un article de loi : **WebSearch avec `allowed_domains=["legifrance.gouv.fr"]`** OU passer par **NotebookLM `ask_question`** sur le rapport / texte intégré dans le notebook. |
| **Wix API push richContent > 25K tokens** échoue (limite tool call body) | Fallback : copier-coller markdown manuellement dans l'éditeur Wix Studio (Nicolas refait la mise en page). |
| **Wix Studio rejette `<script>...</script>` pour JSON-LD avec erreur de format** | **Livrer le bloc dans le chat** (bloc code Markdown), minifié one-liner avec `type="application/ld+json"`. |
| **NotebookLM ask_question : timeout 30s sur 1ère requête** (warm-up browser headless) | Augmenter via `browser_options: {"timeout_ms": 120000}` ou retry. |
| **NotebookLM ask_question : tooltip de citation bloque le clic** sur sessions longues | Lancer une **nouvelle session** (omettre `session_id` ou en générer un nouveau). |
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
   a. Fact-check juridique d'abord via WebSearch ciblée (Légifrance/courdecassation.fr/juricaf.org).
   b. **Si je doute** sur une notion ou un n° de pourvoi : formuler une question à Nicolas (LEARN-022) → il bâtit un cluster NotebookLM orienté → me fournit la réponse → j'ingère et dispatche dans le draft.
   c. Si toujours non confirmé → reformulation prudente + `⚠️ À vérifier` (LEARN-021 + LEARN-049).
   d. Produire les 3 livrables Étape 4 (article.md + metadonnees-wix.md + JSON-LD FAQPage dans le chat).
   e. Nicolas copie-colle le markdown dans Wix Studio et refait la mise en page (LEARN-002 + LEARN-004).
   f. Méta-données SEO renseignées via le panneau SEO Wix Studio (slug, titre, description, **2 catégories** = Ressources et notions juridiques + thématique, tags, image hero + alt, JSON-LD FAQPage).
   g. Mise à jour LEARNINGS.md + ARTICLE_TEMPLATE.md si nouveau pattern.
10. Commit Git local : `git add -A`, vérifier que `.env` n'est pas inclus, puis `git commit -m "Article #N : slug"` (+ mention refresh prévu M+6 — LEARN-046). Pas de chaînage `&&`.
11. Push GitHub sur "OK push" explicite uniquement (`git push origin main`).
```

---

## Pages d'expertise cibles (pour CTA conversion)

**Défense pénale (5)** :
- `/defense-penale/droit-penal`
- `/defense-penale/trafic-de-stupefiant`
- `/defense-penale/proces-criminel`
- `/defense-penale/droit-penal-des-affaires`
- `/defense-penale/violences-conjugales-et-feminicides`

**Indemnisation des victimes (5)** :
- `/indemnisation-des-victimes/victimes-de-delits-ou-crimes`
- `/indemnisation-des-victimes/accidents-de-la-route`
- `/indemnisation-des-victimes/droit-et-accidents-du-travail`
- `/indemnisation-des-victimes/accidents-et-erreurs-medicales`
- `/indemnisation-des-victimes/accidents-de-la-vie-courante`

**Droit des contrats et des personnes (4)** :
- `/droit-des-contrats-et-des-personnes/droit-assurances-particuliers-professionnels`
- `/droit-des-contrats-et-des-personnes/droit-de-la-famille`
- `/droit-des-contrats-et-des-personnes/defense-des-consommateurs`
- `/droit-des-contrats-et-des-personnes/droit-de-la-famille/avocat-divorce-bordeaux`

**Page conversion principale** : `/honoraires-rendez-vous`

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

## Volume cible & ton (rappel learnings — révisé Nicolas 2026-05-11)

- **2 000-2 500 mots** (révisé post article #2 — concision > longueur ; médiane Plouton 28j = 1 700, on vise un peu au-dessus pour la profondeur distinctive).
- **5-6 H2** (TDM = tous les H2 cliquables) + ~8-12 H3.
- **2 catégories Wix systématiques** : *Ressources et notions juridiques* + une catégorie thématique reliée au sujet.
- **Ton sobre + empathique**, anti-marketing. Pas de "appel maintenant", pas d'étoiles Google, pas d'urgence factice.
- **Voix « main tendue » LEARN-052** (durable, à partir article #4) : adressage direct « vous » / reconnaissance du vécu avant info / voix cabinet « nous » / CTAs invitation humaine / lexique actif / modulation victime vs défense pénale. Voir BRIEF.md section Ton éditorial + ARTICLE_TEMPLATE.md bloc dédié + checklist.
- **Persona** : visiteur en quête d'info juridique, souvent en détresse post-accident. Empathie d'abord.
- **3 CTA** : 1 mini-CTA post-intro, 1 mini-CTA dans le corps, 1 CTA final. *Nicolas gère le placement final lors de l'ingestion Wix — on fournit les 3 sans s'obsesser sur leur position exacte.*
- **Bio auteur Maître Plouton OBLIGATOIRE** en pied d'article (LEARN-040 E-E-A-T YMYL).
- **3 ancrages locaux Bordeaux/Nouvelle-Aquitaine** minimum (LEARN-042).
- **FAQ 8-10 questions** (LEARN-044).
- **Schema FAQPage seul** par article (LEARN-041 — les autres schémas sont gérés au niveau du site Plouton).
- **Date de mise à jour visible** en italique en pied (LEARN-043).
- **Sourcing rigoureux** : chaque chiffre = millésime + URL primaire. Chaque article de loi = lien Légifrance. Chaque jurisprudence = n° de pourvoi + date + chambre.
- **Anti-hallucination (LEARN-049)** : fourchettes prudentes ("indicatives", "généralement", "varie") quand pas de source primaire trouvée. ⚠️ `À vérifier` noir sur blanc si doute. Si je doute → demander à Nicolas un cluster NotebookLM (LEARN-022).
- **Information Gain (LEARN-039)** : au moins 2-3 éléments distinctifs absents du top 10 SERP. Sans gap démontrable → abandonner ou pivoter.
- **Clusters profonds (LEARN-047)** : 3 clusters (Route / Erreurs médicales / Pénal) plutôt que 24 articles disjoints. Cross-linking intra-cluster systématique.
- **Refresh durabilité (LEARN-046)** : tous les 6 mois après publication.
- **Doctrine Google AI Search 2026 (LEARN-053, ingérée 2026-05-16)** : pas de stratégie GEO/AEO séparée — c'est du SEO appliqué au retrieval IA (RAG + Query Fan-Out). Unique Point of View obligatoire dès le H1 (anti-commodity). Mythbusting officiel Google : `llms.txt` pas requis, chunking artificiel pas requis, structured data pas requis pour AI mais utile pour rich results (on garde FAQPage seul). Détail dans [BRIEF.md §6](BRIEF.md) et [ARTICLE_TEMPLATE.md checklist](ARTICLE_TEMPLATE.md). Source officielle : [Google Search Central — AI Optimization Guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).

---

## En cas de doute

- Lis **`BRIEF.md`** pour le détail des règles business + workflow.
- Lis **`ARTICLE_TEMPLATE.md`** pour la structure des livrables + checklist qualité.
- Consulte **`LEARNINGS-archive.md`** pour comprendre le *pourquoi* d'une règle (chaque entrée est horodatée et liée à un article précis).
- Consulte **`LEARNINGS.md`** pour les observations fraîches en attente de digestion.
- Consulte **`memory/MEMORY.md`** + les feedback files pour les règles durables auto-chargées.
- Pose la question à Nicolas plutôt que d'extrapoler.

**Anti-hallucination** : ne JAMAIS inventer une donnée juridique. Toujours sourcer ou marquer ⚠️.

---

*Dernière mise à jour : 2026-05-16 (ingestion Doctrine Google AI Search 2026 — LEARN-053 promu dans BRIEF.md §6 + ARTICLE_TEMPLATE.md checklist + LEARNINGS-archive.md).*
