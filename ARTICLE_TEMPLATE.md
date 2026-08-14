# ARTICLE_TEMPLATE — Structure réutilisable affinée

> Squelette des livrables du workflow 4 étapes. **Affiné après chaque article** sur la base des patterns qui ont marché.
> Historique des mises à jour : `git log --oneline -- ARTICLE_TEMPLATE.md` (pas de date en dur — elle mentait ; audit 2026-08-05).

---

## Cap général (validé sur article #1 + patterns cognitifs notebook 2026-05-11)

| Paramètre | Valeur cible |
|---|---|
| **Volume** | **2 000-2 500 mots** (révisé Nicolas 2026-05-11 post article #2 — concision > longueur ; médiane Plouton 28j = 1 700 ; profondeur distinctive justifie un peu plus mais pas excessif). **Réaffirmé 2026-06-01 (option b LEARN-META-2)** : cible tenue par une **passe de compression active** en Étape 4, pas par relâchement de la cible. |
| **Structure** | 1 H1 + 1 intro + 1 TDM + **5-6 H2** + ~8-12 H3 + **FAQ 8-10 Q (= dernier H2, avant le CTA final)** + CTA final + **bio auteur** + date de mise à jour. Ordre verrouillé par la décision Nicolas 2026-08-05. |
| **Encadrés** | 3-6 définitions (BLOCKQUOTE) + 1-2 encadrés chiffrés (BLOCKQUOTE) + 1-2 encadrés alerte (BLOCKQUOTE débutant par « Attention… » — **sans émoji**, garde-fou LEARN-052) |
| **Liens internes** | 1 lien tous les ~250 mots — **2-3** vers pages expertise/CTA + **4-7** vers articles ressources cluster + **2-4** vers affaires cabinet (preuves). **Seule maison des fourchettes** (la checklist et la table y renvoient — audit 2026-08-05). |
| **CTA** | 3 au total (Nicolas gère le placement final lors de l'ingestion Wix) : mini-CTA inline #1 post-intro, mini-CTA inline #2 dans le corps, CTA final |
| **Ton** | Sobre, empathique, précision juridique, anti-marketing — **voix « main tendue » LEARN-052** (adressage direct au « vous », reconnaissance avant info, voix cabinet « nous », CTAs invitation humaine, modulation selon victime/défense pénale) |
| **Sourcing** | Chaque chiffre = millésime + source primaire ; chaque article de loi = lien Légifrance, **version applicable tranchée par `legifrance.py`** (discipline de version : BRIEF.md §4 Bloc A) ; **chaque jurisprudence = n° de pourvoi + date + chambre confirmés** (LEARN-026), vérifiés via **Judilibre PROD** (LEARN-054) |
| **Information Gain (LEARN-039)** | **Au moins 2-3 éléments distinctifs absents du top 10 SERP** — sans quoi l'article est déclassé. Identifier en Bloc B (gap analysis). |
| **Bio auteur (LEARN-040)** | Bloc « À propos de l'auteur » obligatoire en pied d'article (E-E-A-T YMYL). Template en bas du fichier. |
| **Local-first (LEARN-042)** | Au moins **3 ancrages Bordeaux/Nouvelle-Aquitaine** (juridiction locale + adresse cabinet + zone d'intervention). |
| **Date update visible (LEARN-043)** | Italique en pied : *« Dernière mise à jour : [mois année]. »* |
| **Densité info (LEARN-028)** | Chaque H2 = 1 chiffre sourcé + 1 cas concret + 1 implication pratique. Pas de creux narratif. *Exception : H2 sur concept juridique abstrait sans données disponibles → 1 implication pratique suffit. Ne jamais forcer un chiffre sans source primaire.* |
| **Phrases (LEARN-030)** | 16-20 mots idéal, **JAMAIS > 40 mots** |
| **Paragraphes (LEARN-030)** | 1-3 phrases, **1 seule idée** par paragraphe |
| **Front-loading (LEARN-029)** | Tous H2/H3/paragraphes/bullets commencent par les **2-3 mots les plus porteurs de sens** |

## Pattern Mini-CTA #1 "double-face" (LEARN-031 + LEARN-052)

Reconnaître les limites du guide = crédibilité renforcée.

**Format combiné LEARN-031 + voix victime LEARN-052** :

> **Vous traversez [situation difficile / vécu spécifique du persona] ?**
> Ce guide couvre [80 % des situations / la plupart des cas que nous voyons au cabinet]. Vous pouvez avancer seul sur la plupart des étapes.
> Pour les [20 % restants / cas complexes spécifiques] — [exemple concret : *contestation d'expertise, lien de causalité fragile, refus ONIAM, séquelles graves*] — **vous n'êtes pas obligé de rester seul**. C'est exactement à ce moment-là qu'un avocat fait la différence.
> [CTA invitation humaine — *« Si vous voulez en parler »* / *« Premier échange sans engagement »* / *« Faire le point avec un avocat »* — pas "En savoir plus" / "Contact" / "Faire évaluer mon dossier" trop service]

---

## Voix victime / main tendue (LEARN-052 — durable, tous articles)

→ Règles complètes (7 réflexes, garde-fous, modulation selon victime/défense/contrats) dans **BRIEF.md §2**. Checklist de contrôle en fin de fichier.

---

## Étape 1 — Cadrage stratégique (template)

```markdown
# Cadrage — [Titre de travail]

## Sujet
[Titre de travail provisoire]

## Intention de recherche
- **Type** : informationnelle / commerciale / navigationnelle / mixte
- **Justification** : [observée dans SERP via DataForSEO ; mention de l'intent classifié]

## Requête principale
`[head term]`

## Pilier-volume adjacent
[À remplir si le head term est de niche (volume nul ou marginal) — cf. BRIEF.md §4 Étape 1.
Nommer le head term voisin à fort volume et son volume mesuré : il devient un candidat
du backlog, et il justifie d'assumer cet article comme actif d'autorité plutôt que comme pilier.
Sans objet si le head term porte déjà le volume.]

## Requêtes long-tail (5–10)
1. `[long-tail 1]`
2. …

## Persona prospect
- **Profil** : [qui tape ces requêtes]
- **Contexte émotionnel** : urgence / prise de conscience / recherche prestataire / curiosité
- **Niveau juridique** : néophyte / informé / averti

## Page(s) d'expertise cible(s)
- Page principale (CTA) : [/url]
- Pages secondaires : [/url2]

## Hypothèse de valeur
[Pourquoi cet article peut performer. Gap concurrentiel observé en SERP. Intent mal servi.]

## Preuve d'originalité
[OBLIGATOIRE — nommer l'artefact qui n'existe nulle part ailleurs, pas une intention.
Catalogue des sources d'originalité déjà éprouvées :
- affaire cabinet réelle avec montant obtenu (+ lien interne vers le post d'affaire) ;
- **angle mort total** — le sujet est capté par une autre discipline et jamais traité en droits (typologie des trois degrés : BRIEF.md §4 Bloc B) ;
- périmètre territorial d'un dispositif national vérifié dans l'arrêté, pas dans la presse (LEARN-071) ;
- fiche destinée aux professionnels plutôt que la page grand public (réflexe de sourcing : BRIEF.md §4 Bloc D) ;
- donnée calculée ou agrégée par nous, tableau construit, outil/calculateur.
Champ vide après le Bloc B = pivoter ou abandonner le sujet. Cf. BRIEF.md §6
« Standard qualité YMYL » règle 3 : un article aussi bon que la concurrence vaut Medium.]
```

---

## Étape 2 — Collecte (template — 4 blocs)

```markdown
# Collecte — [Titre]

## Bloc A — Matière juridique
### Articles de loi
- [Article XXX du Code XXX](URL Légifrance) — résumé synthétique
### Jurisprudence (via PISTE Judilibre)
- [Cass. XX, JJ/MM/AAAA, n° XX.XXX](URL Judilibre) — apport principal
### Procédures, délais, formes
- [Délai] : [valeur] — source : [URL]
### Définitions techniques sourcées

## Bloc B — Données SEO (DataForSEO MCP)
### SERP top 10
| Rang | Domaine | Type | Note |
### PAA observées
### Volumes / intent / backlinks moyens
### Gap analysis (ce que personne ne traite)

## Bloc C — Contexte interne Plouton (Wix MCP)
### Inventaire catégorie Ressources (obligatoire — consigne 2026-06-23)
- Query `ExecuteWixAPI` posts `categoryId 9477320f-…` → liste publiée → décision cannibalisation + maillage notion↔notion. Tester les liens retenus en **HTTP** (anti-404, LEARN-057).
### Catégorie de publication
- Catégorie 1 (publication) : Ressources et notions juridiques (id `9477320f-…`)
- Catégorie 2 (thématique) : [variable selon sujet]
### Affaires cabinet pertinentes
- [URL post] — [angle utilisé pour preuve sociale]
### Articles ressources connexes pour cross-link sortant
- [URL post] — [section où l'utiliser]
### Page d'expertise pour sourcing interne
- [/expertise/url] — citation cabinet exploitable

## Bloc D — Statistiques officielles
| Chiffre | Valeur | Millésime | Source primaire | Usage prévu |
```

---

## Étape 3 — Plan justifié (template affiné)

````markdown
# Plan d'article — [Titre]

## Méta-données

### H1 retenu
**[Pose une question implicite OU annonce une différenciation explicite]**
*Exemple validé sur article #1 : "Accident de moto : pourquoi votre indemnisation diffère de celle d'un automobiliste (guide AAAA)"*

### 3 variantes H1 alternatives (traçabilité)
- [H1-B]
- [H1-C]
- [H1-D]

### Méta-title (≤ 60 char)
### Méta-description (≤ 155 char)
### Slug (sans accent — LEARN-001)
### Catégorisation Wix : 2 catégories (publication + thématique)
### Tags suggérés

---

## Plan H2/H3 justifié

**Budget de longueur (LEARN-META-2 option b — 2026-06-01)** : la somme des longueurs indicatives de toutes les sections doit tomber dans **2 000-2 500 mots**. Si le plan budgète plus → élaguer des H3 ou fusionner des sections dès maintenant, ne pas reporter toute la coupe sur la passe de compression Étape 4.

### Intro (~200-250 mots) — Pattern Version D (validé) + voix victime LEARN-052
**Structure cognitive optimisée + main tendue :**
1. **Phrase psychologique d'ouverture en adressage direct** (vérité du persona, « vous » — pas « la victime ») — résonne immédiatement
2. **Reconnaissance du vécu avant le chiffre** (LEARN-052 réflexe #2) — 1 phrase qui acte la confusion/détresse, avant d'asséner la statistique. Exemple : *« On vous a parlé de X, de Y, peut-être de Z — sans qu'on vous explique vraiment qui fait quoi. C'est normal de s'y perdre. »*
3. **Chiffre brutal sourcé** (paragraphe 2 — autorité + légitimation, mais après la reconnaissance)
4. **Bullets "Ce que ce guide vous apporte"** (4 items — mini-sommaire intégré, scannable, en adressage « vous »)
5. **Signature autorité cabinet en voix « nous »** (LEARN-052 réflexe #3) — *« Nous accompagnons depuis vingt ans des personnes qui traversent ce que vous traversez aujourd'hui. »* (1 ligne en italique — ancrage E-E-A-T)

### Mini-CTA inline #1 (post-intro) — Pattern « double-face » LEARN-031 + voix victime LEARN-052
Format BLOCKQUOTE :
> **Mini-CTA**
> Vous traversez [situation difficile / vécu spécifique du persona] ? Ce guide couvre la plupart des cas en autonomie. Pour les situations complexes — [exemple concret : contestation d'expertise, refus ONIAM, lien fragile] — **vous n'êtes pas obligé de rester seul**. [CTA invitation humaine : *« Si vous voulez en parler »* / *« Premier échange sans engagement »*](URL contact).

### TDM (juste après l'intro)
- **Une entrée par H2 de l'article, FAQ comprise** (5-6 H2 de corps + la FAQ = dernier H2), avec liens d'ancrage `#section-slug`
- Chaque H2 cible reçoit son ancre via `## Titre {#section-slug}` (le lien `#…` est traité comme interne SELF)
- **Depuis 2026-06-23, `md_to_ricos.py` CONVERTIT le sommaire** (auparavant supprimé à la bascule Ricos) → la TDM est poussée dans le draft Wix ; Nicolas fait la mise en page
- Format liste à puces

*Squelette générique, valable pour les **3 familles d'expertise** du BRIEF (indemnisation des victimes, défense pénale, contrats & personnes). Les intitulés se réécrivent avec le vocabulaire du lecteur — ce sont des rôles de section, pas des titres à recopier.*

### H2 1 — Contextualisation (pourquoi ce sujet appelle un traitement spécifique)
- Encadré chiffré (BLOCKQUOTE, **prose continue — pas de bullets**, LEARN-025)
- Transition vers le cadre légal

### H2 2 — Cadre légal sourcé
- 3-4 H3 selon les textes mobilisés
- Encadrés définition (BLOCKQUOTE) pour les concepts juridiques clés
- Cross-link vers l'article pilier du cluster

### H2 3 — Cœur différenciant (la profondeur distinctive — Information Gain LEARN-039)
- 4-6 H3 sur ce qui est absent du top 10 SERP
- Cross-links sortants vers les articles ressources existants (délégation de profondeur)
- Lien vers une affaire cabinet en preuve

### H2 4 — Cas particuliers et situations limites (2-4 H3)
- Exploite le cluster sémantique (cross-links variés)
- Lien affaire cabinet en preuve

### H2 5 — Démarches et procédure (3 H3) — par quoi commencer, devant qui, dans quel délai

**Déclinaisons du H2 5 par famille** (exemples, pas un carcan) :

| Famille | H3 typiques |
|---|---|
| Indemnisation des victimes | Expertise médicale (cross-link « dossier médical ») · Offre de l'assureur (cross-link page d'expertise) · Contentieux (lien affaire) |
| Défense pénale | Garde à vue et enquête · Instruction ou comparution · Audience et voies de recours |
| Contrats & personnes | Démarche amiable et mise en demeure · Saisine compétente (JAF, médiateur, tribunal) · Exécution de la décision |

### Mini-CTA inline #2 (vers le milieu du corps)
> Pour aller plus loin sur [thématique], consultez [notre page d'expertise dédiée](URL).

*Nicolas gère le placement final des mini-CTAs lors de l'ingestion Wix — fournir simplement les 3 CTAs (post-intro, milieu, final) dans l'article.*

### Dernier H2 — FAQ (COLLAPSIBLE_LIST) — **8-10 questions** (LEARN-044)
- **8-10 questions** systématiques (révisé Lucid Media — vs 5-7 précédemment)
- Mix : 5 PAA SERP exploitables (Bloc B Étape 2) + 3-5 questions issues des gaps éditoriaux
- **Privilégier les questions à nuance juridique** (LEARN-045 — anti-AI Overviews) : *« Puis-je écrire X sur Google sans risque ? »*, *« Quelle est la différence entre A et B ? »*, *« Dans quel délai dois-je agir ? »*
- Chaque réponse : **40-80 mots**, **concept-clé en ouverture** (LEARN-017 citabilité LLM)
- Sourcing intégré (lien Légifrance/ONISR dans la réponse quand pertinent)

### CTA final (~100 mots)
- Phrase de bascule empathique
- Présentation courte cabinet + **ancrage local Bordeaux/Nouvelle-Aquitaine** (LEARN-042)
- Lien fort vers `/honoraires-rendez-vous` ou page expertise

### Bio auteur (LEARN-040) — bloc OBLIGATOIRE en pied d'article
Format **BLOCKQUOTE** ~150 mots :

```markdown
---

## À propos de l'auteur

> **Maître Julien Plouton** — avocat au Barreau de Bordeaux, a prêté serment en 2004 après une formation à l'École de Formation du Barreau de Paris (EFB). Diplômé d'un **DESS en droit des affaires et fiscalité**, d'un **DEA en droit européen** et d'un **master spécialisé HEC en droit et management international**, il a fondé le **Cabinet Plouton en 2009**, situé au 45 Cours d'Alsace-et-Lorraine à Bordeaux.
>
> Il est membre de l'**Institut du Dommage Corporel (IDC)**, de l'**Association des Avocats Pénalistes (ADAP)** et de l'**Institut du Droit des Affaires du Barreau de Bordeaux (IDA)**. Depuis plus de vingt ans, il accompagne [adapter selon le sujet de l'article — ex. les victimes d'erreurs médicales / d'accidents de la route / les personnes mises en cause en matière pénale] en Nouvelle-Aquitaine et au-delà.
>
> [En savoir plus sur le cabinet](https://www.jplouton-avocat.fr/notre-cabinet) • [Demander un premier rendez-vous](https://www.jplouton-avocat.fr/honoraires-rendez-vous)

*Dernière mise à jour : [mois année].*
```

**À adapter par article** : uniquement la phrase « il accompagne [thématique] » et la date. Le reste est immuable.

---

## Stratégie de liens internes

| Type | Cible | Quantité indicative |
|---|---|---|
| Pages d'expertise (CTA) | `/indemnisation-...` ou `/defense-...` ou `/droit-...` | 2-3 |
| Page contact | `/honoraires-rendez-vous` | 1 (CTA final) |
| Articles ressources (cluster) | autres articles `/post/` de la catégorie Ressources | 4-7 |
| Affaires cabinet (preuves) | `/post/` cas réels | 2-4 |

> **Règle absolue (Nicolas 2026-06-02) :** **toute affaire réelle du cabinet citée** dans l'article — y compris en **FAQ** et en **encadré** — reçoit **automatiquement** un lien interne vers son post `/post/...`. Ancre neutre autorisée (anonymisation du texte conservée) ; récupérer le **slug publié réel via Wix MCP**, jamais deviner ni supposer qu'un article du repo est en ligne.

---

## Stratégie GEO (citabilité LLM)

- **Encadrés définitions** (BLOCKQUOTE) — un par concept juridique central
- **Encadré chiffré** (BLOCKQUOTE avec titre gras + bullets) — pour le hook chiffré principal
- **Listes ordonnées** — pour les sections "Les X étapes de...", "Les Y postes de..."
- **FAQ COLLAPSIBLE_LIST** — **8-10 Q&A** (LEARN-044)
- **JSON-LD FAQPage** — bloc séparé prêt-à-coller dans module SEO Wix (le COLLAPSIBLE_LIST natif ne génère pas le schema automatiquement)
````

---

## Étape 4 — Livrables OBLIGATOIRES (ne rien zapper)

Chaque article #N doit produire dans son dossier `0N-slug-article/` :

1. **`etape-4-article.md`** — article complet en markdown (source de travail et d'archive ; entrée de `md_to_ricos.py` ; liens internes en URL absolue)
2. **`etape-4-metadonnees-wix.md`** — **OBLIGATOIRE, NE PAS ZAPPER** — **8 sections** (format stabilisé #10, décision Nicolas 2026-08-05) : **SEO** (H1, méta-title ≤ 60, méta-description ≤ 155, slug sans accent), **Catégories Wix** (2 IDs : Ressources et notions juridiques + thématique — reco BRIEF/README, *pas* LEARN-041 qui concerne le schema FAQPage), **Tags** (10-15, **séparés par des virgules — jamais de middot ·**, règle mémoire), **Image hero + alt**, **Carte des liens** (internes sans rel / externes nofollow), **JSON-LD FAQPage** (renvoi : livré dans le chat), **Push Wix** (`draftPostId` + statut + garde-fou), **Refresh** (date M+6 + déclencheurs).
3. **`ricos.min.json`** — sortie de `python3 scripts/md_to_ricos.py etape-4-article.md`, minifiée, poussée en **draft `UNPUBLISHED`** via `ExecuteWixAPI` (flux par défaut LEARN-064 — décision 2026-08-05). Garde-fou `nodes.length`/`faqCount` avant POST, vérif `GET …/draft-posts/{id}` après. **À régénérer + resynchroniser à chaque modification de l'article** (anti-drift : le draft #10 avait perdu sa TDM).
4. **JSON-LD FAQPage** — **livré DIRECTEMENT dans le chat** (bloc code Markdown, JSON minifié one-liner, avec `type="application/ld+json"`). **PAS de fichier `.json` ou `.html` séparé** (LEARN-027 — validé : Wix Studio rejette les fichiers HTML pour ce champ, copier-coller depuis le chat est l'unique méthode fiable).
5. *(optionnel)* **`etape-4-corrections-rouge.html`** — visualisation rouge des passages modifiés si fact-check post-rédaction a entraîné des corrections.

## Étape 4 — Fact-check juridique obligatoire AVANT rédaction (LEARN-026 + LEARN-049 anti-récidive)

**Règle non négociable :** toute affirmation juridique précise doit être sourcée AVANT rédaction.

**Procédure AVANT de rédiger chaque affirmation juridique précise** (n° d'article, n° de pourvoi, fondement, citation verbatim) :

1. **WebSearch ciblée** d'abord : `allowed_domains=["legifrance.gouv.fr"]` pour les articles de loi ; recherche libre courdecassation.fr / juricaf.org pour les arrêts. C'est la voie la plus rapide.
2. **Si WebSearch ne suffit pas / contradictoire / pas confirmé** → **demander à Nicolas un cluster NotebookLM orienté** (LEARN-022) :
   - Formuler une question précise (LEARN-051 — pas de hard wrap)
   - Préciser ce que je ferai de la réponse (LEARN-023)
   - Attendre la synthèse Nicolas → ingérer et dispatcher dans le draft
3. **Vérifier 2 fois** chaque numéro d'article cité (idéalement 2 sources convergentes — WebSearch + NotebookLM).
4. **Si toujours non confirmé** → reformulation prudente (LEARN-021) + `⚠️ À vérifier` noir sur blanc dans le draft.

**Bon réflexe** : grouper jusqu'à 5 zones d'incertitude en **une seule demande NotebookLM** à Nicolas (économise les allers-retours). Prioriser les questions dont une erreur serait une affirmation juridique fausse.

## Étape 4 — Procédure de livraison fin de rédaction

À la fin de la rédaction Étape 4, **présenter à Nicolas en un seul message** avec ce format :

````
🛑 Étape 4 — Phase 1 (rédaction) terminée.

Livrables :
1. 📄 etape-4-article.md — article complet (~2 000-2 500 mots)
2. 📄 etape-4-metadonnees-wix.md — 8 sections SEO prêtes à coller
3. 📄 ricos.min.json — draft Wix UNPUBLISHED poussé (draftPostId dans les métadonnées)
4. JSON-LD FAQPage ci-dessous (à coller dans le champ "Marquage 
   structuré" du panneau SEO Wix Studio du post) :

   ```
   <script type="application/ld+json">{...JSON minifié one-liner...}</script>
   ```

Récap fact-check : [N WebSearch ciblées + M demandes NotebookLM Nicolas]
Sources mobilisées : [résumé bref]

Push : draft UNPUBLISHED via API (LEARN-064, flux par défaut).
Fallback : copier-coller markdown par Nicolas (LEARN-002 + LEARN-004).
````

**Ne JAMAIS finir l'Étape 4 sans avoir produit les 4 livrables ci-dessus.**

## Étape 4 — Article HTML/Ricos Wix-ready (template)

### Patterns Ricos validés (test 2026-05-11 dans Wix Studio)

```
HEADING (level 2, 3)        → titres
PARAGRAPH                    → paragraphes (avec décorations BOLD/ITALIC/LINK)
BULLETED_LIST + LIST_ITEM    → listes
BLOCKQUOTE                   → encadrés (définition, chiffré, mini-CTA)
DIVIDER                      → séparateurs (entre H2)
COLLAPSIBLE_LIST + ITEMs     → FAQ accordéon
```

### Pattern HTML (fallback copier-coller — le flux par défaut est le push API, cf. livrable 3)

```html
<h2 id="section-slug">[H2 title]</h2>
<p>[paragraphe avec <strong>gras</strong>, <em>italique</em>,
   <!-- Lien INTERNE : pas de rel, pas de target -->
   <a href="https://www.jplouton-avocat.fr/page-cible">lien interne</a>,
   <!-- Lien EXTERNE : target blank + rel complet -->
   <a href="https://www.legifrance.gouv.fr/..." target="_blank" rel="noopener noreferrer nofollow">lien externe</a>
]</p>

<!-- Encadré définition -->
<blockquote>
  <p><strong>Définition. [Terme]</strong> — [définition sourcée]. (<a href="URL" target="_blank" rel="noopener noreferrer nofollow">Texte complet sur Légifrance</a>.)</p>
</blockquote>

<!-- Encadré chiffré (LEARN-025 : PAS de listes à puces dans blockquote, prose continue uniquement) -->
<blockquote>
  <p><strong>[Titre encadré]</strong></p>
  <p><strong>[chiffre]</strong> [contexte] ; <strong>[chiffre]</strong> [contexte] ; <strong>[chiffre]</strong> [contexte] ; et <strong>[chiffre]</strong> [contexte].</p>
  <p><em>Source : <a href="URL" target="_blank" rel="noopener noreferrer nofollow">[Source ONISR / Légifrance / Dintilhac]</a>.</em></p>
</blockquote>
<!-- Si vraiment besoin d'une liste visible : sortir la liste DU blockquote (bloc séparé en BULLETED_LIST natif) -->
<blockquote>
  <p><strong>[Titre encadré]</strong></p>
  <p><em>Source : <a href="URL" target="_blank" rel="noopener noreferrer nofollow">[Source]</a>.</em></p>
</blockquote>
<ul>
  <li><strong>[chiffre]</strong> [contexte]</li>
  <li><strong>[chiffre]</strong> [contexte]</li>
</ul>

<!-- Mini-CTA inline -->
<blockquote>
  <p><strong>Mini-CTA</strong></p>
  <p>[Question empathique]. <a href="https://www.jplouton-avocat.fr/honoraires-rendez-vous">Parler à un avocat</a>.</p>
</blockquote>

<!-- FAQ (sera converti en COLLAPSIBLE_LIST côté Wix Studio) -->
<h3>[Question 1]</h3>
<p>[Réponse 40-80 mots commençant par concept-clé.]</p>

<!-- CTA final -->
<p>[Phrase empathique de bascule.]</p>
<p><strong>[<a href="https://www.jplouton-avocat.fr/honoraires-rendez-vous">Prendre rendez-vous avec le Cabinet Plouton</a>]</strong> — Bordeaux, plus de 20 ans d'expérience.</p>
```

### Bloc JSON-LD FAQPage (LEARN-041 — UNIQUEMENT FAQPage par article)

Les schémas Person, LegalService et Article sont gérés au niveau du site Wix Studio — **ne pas dupliquer** dans chaque article (risque doublon + signal négatif Google).

**Livré directement dans le chat** (LEARN-027) en 1 seul bloc `<script type="application/ld+json">` minifié one-liner, contenant uniquement les 8-10 questions de la FAQ (LEARN-044). À coller dans le champ « Marquage structuré » du panneau SEO Wix Studio du draft post.

**Squelette type** :

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Q1 text",
     "acceptedAnswer": {"@type": "Answer", "text": "Réponse 40-80 mots, concept-clé en ouverture (LEARN-017)"}},
    ...
  ]
}
```

**À tester après publication** : [Google Rich Results Test](https://search.google.com/test/rich-results) — vérifier que FAQPage est détecté **en plus** des schémas globaux du site (Person + LegalService gérés côté Wix Studio).

### Métadonnées prêtes à coller (Étape 4)

- **Titre** : [méta-title ≤ 60 char]
- **Description** : [méta-description ≤ 155 char]
- **Slug** : [slug-sans-accent]
- **Tags** : [tag1, tag2, tag3]
- **Catégories** : Ressources et notions juridiques + [thématique]
- **Image hero** : [source / brief alt text]

---

## Checklist qualité (à passer avant push)

> **Convention de sévérité.** Les items marqués **🔴** sont des **portes bloquantes** : un seul manquement suffit à déclasser l'article, quel que soit le reste — c'est la règle 2 du *Standard qualité YMYL* (BRIEF.md §6). On ne pousse pas un article dont une porte 🔴 est ouverte. Les autres items sont des optimisations : on les vise tous, mais leur absence ne bloque pas la publication.

### Bloc Sourcing & juridique
- [ ] Toutes les affirmations juridiques sourcées (Légifrance/Judilibre) ou prudemment formulées
- [ ] 🔴 `⚠️ À vérifier` retiré ou résolu *(contrôlé par le lint)*
- [ ] 🔴 **Chaque jurisprudence** = n° de pourvoi + date + chambre **confirmés** (LEARN-026)
- [ ] 🔴 **Fact-check effectué AVANT rédaction** sur chaque zone juridique précise : WebSearch ciblée en 1er recours, NotebookLM via Nicolas si non confirmé (LEARN-026 + LEARN-049 — procédure « Fact-check » ci-dessus)

### Bloc Information Gain & E-E-A-T (Lucid Media 2026)
- [ ] 🔴 **Preuve d'originalité tenue** : l'artefact nommé en Étape 1 est bien présent dans l'article publié (pas seulement annoncé au cadrage)
- [ ] **Au moins 2-3 éléments distinctifs absents du top 10 SERP** (LEARN-039 — gap analysis formalisée Bloc B)
- [ ] 🔴 **Bio auteur Maître Plouton** en pied d'article (LEARN-040) — bloc ~150 mots avec EFB/cabinet 2009/IDC/ADAP/IDA/adresse
- [ ] 🔴 **Aucun claim exagéré** sur le cabinet ou l'auteur — la bio porte du **vérifiable** (barreau, serment, mentions de spécialisation, publications), jamais des adjectifs. *« E-E-A-T assessments should be based on the MC itself, reputation research, verifiable credentials — not just claims of "I'm an expert!" »* (Guidelines §5.6, p. 63 : une info exagérée sur soi-même = Low)
- [ ] 🔴 **Titre et H1 ni exagérés ni trompeurs** — le titre fait partie du Main Content : un titre survendu par rapport au contenu suffit à faire Low (Guidelines §5.2, p. 60). Proscrit : « ce que votre assureur ne veut pas que vous sachiez », superlatifs, promesses chiffrées non tenues dans le corps *(signalé par le lint)*
- [ ] **Date de mise à jour visible** en italique en pied (LEARN-043) — cohérente avec Schema `dateModified`
- [ ] **3 ancrages Bordeaux/Nouvelle-Aquitaine** minimum (LEARN-042) : juridiction locale + adresse cabinet + zone d'intervention
- [ ] 🔴 **Chaque affaire cabinet citée porte un lien interne** vers son post `/post/...` (FAQ + encadrés inclus) — règle stricte 2026-06-02 ; ancre neutre OK, slug réel via Wix MCP

### Bloc Schema markup
- [ ] **JSON-LD FAQPage** livré dans le chat (LEARN-041 — UNIQUEMENT FAQPage par article ; Person/LegalService gérés au niveau site Wix)
- [ ] Test passé sur [Google Rich Results Test](https://search.google.com/test/rich-results) après publication

### Bloc Standards Wix
- [ ] **Slug sans accent** (LEARN-001 — règle stricte)
- [ ] **HTML/Ricos** propre, pas de markdown résiduel dans le contenu final
- [ ] Liens internes en **URL absolue** (`https://www.jplouton-avocat.fr/...`)
- [ ] **Convention `rel` respectée** : internes = pas de `rel` + pas de `target="_blank"` ; externes = `target="_blank" rel="noopener noreferrer nofollow"` (LEARN-024)
- [ ] **Pas de bullets dans blockquotes Wix** (LEARN-025 — prose continue uniquement)
- [ ] Alt text sur toutes les images
- [ ] Méta-title ≤ 60 caractères
- [ ] Méta-description ≤ 155 caractères (comptage réel, pas « ~155 »)
- [ ] **Tags séparés par des virgules** (10-15, jamais de middot ·) — règle mémoire, violée 5× avant l'audit 2026-08-05

### Bloc UX & cognitif
- [ ] **Phrases ≤ 40 mots max, idéal 16-20** (LEARN-030 — relire et raccourcir les phrases longues)
- [ ] **Paragraphes ≤ 3 phrases, 1 seule idée par paragraphe** (LEARN-030)
- [ ] **Front-loading appliqué** sur tous les H2/H3/bullets : les 2-3 premiers mots portent le sens (LEARN-029)
- [ ] **Densité info** : chaque H2 contient au moins 1 chiffre sourcé + 1 cas concret + 1 implication pratique (LEARN-028 — pas de creux narratif)
- [ ] **Pas de jargon obscur** dans les éléments scannés (H2, H3, ancres) — vocabulaire du lecteur, pas du cabinet (LEARN-038)
- [ ] **Storytelling cognitif** en ouverture d'au moins 1 section H2 critique (LEARN-035)

### Bloc Structure & CTA
- [ ] 🔴 **Réponse utile dans le premier écran** — l'intro reconnaît le vécu puis répond ; aucun développement de contexte ne s'interpose entre le H1 et la première information actionnable. Le *filler* placé avant le contenu utile est un motif de Low à lui seul (Guidelines §5.2.2, p. 62 : *« place the most helpful and essential MC near the top »*)
- [ ] **Volume final 2 000-2 500 mots** (LEARN-META-2 option b — décision 2026-06-01) — passe de compression effectuée si le draft dépassait ; densité info (LEARN-028) et Information Gain (LEARN-039) préservés
- [ ] **FAQ 8-10 questions** (LEARN-044 — vs 5-7 précédemment) — mix PAA + questions issues des gaps
- [ ] **FAQ placée en dernier H2, avant le CTA final**, et présente dans la TDM (décision Nicolas 2026-08-05)
- [ ] FAQ privilégie **questions à nuance juridique** (LEARN-045 — anti-AI Overviews)
- [ ] **CTAs conformes au Cap général** : 2 mini-CTAs inline (#1 post-intro, #2 corps) + 1 CTA final (décision Nicolas 2026-08-05)
- [ ] **CTAs spécifiques** : zéro libellé vague (pas de « En savoir plus » / « Cliquez ici » / « Contact ») — LEARN-037
- [ ] **Mini-CTA #1 « double-face »** appliqué (reconnaît les limites du guide, précise pour qui un avocat est utile) — LEARN-031

### Bloc Voix victime / main tendue (LEARN-052 — durable, tous articles)
- [ ] **Adressage direct « vous »** — chasser les *« la victime »* / *« l'intéressé »* / *« le demandeur »* en 3ᵉ personne (sauf citations légales)
- [ ] **Reconnaissance du vécu** avant l'info en ouverture d'au moins 2-3 sections critiques (intro + 1-2 H2 sensibles)
- [ ] **Voix cabinet « nous »** — *« Nous accompagnons »* dans bio + CTA final + intro (pas systématiquement « Le Cabinet Plouton »)
- [ ] **CTAs en invitation humaine** — *« Si vous voulez en parler »* / *« Premier échange sans engagement »* (pas *« Faire évaluer mon dossier »* trop service)
- [ ] **Reconnaissance des limites du guide** au moins une fois (mini-CTA #1 ou CTA final) — *« Aucun guide ne remplace l'écoute d'un dossier réel. »*
- [ ] **Lexique actif** — *« Vous avez le droit de »* / *« Vous pouvez »* > *« Il est possible de »*
- [ ] **Phrases-ponts humaines** entre sections (au moins 2 transitions où l'auteur acte qu'il s'adresse à un humain)
- [ ] **Garde-fous respectés** : pas de pathos, pas d'exclamation marketing, pas d'émoji, pas d'urgence factice, pas d'étoiles ⭐
- [ ] **Modulation selon le sujet** : victime = empathie haute ; défense pénale = empathie modulée + présomption d'innocence ; contrats/famille = empathie sobre

### Bloc Cluster & maillage interne
- [ ] **Maillage cluster conforme au Cap général** (fourchettes uniques définies au Cap — LEARN-047 : 3 deep clusters > 30 shallow)
- [ ] Date de prochain refresh notée dans le commit message (LEARN-046 — refresh tous les 6 mois)

### Bloc Doctrine Google AI Search 2026 (officielle — ingérée 2026-05-16)
Source : [Google Search Central — AI Optimization Guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide). Cf. BRIEF.md §6 *Doctrine Google AI Search 2026* pour le détail.

- [ ] **Unique Point of View** clair dès le H1 — pas un *« comment se faire indemniser »* qui pourrait être posé par n'importe quel cabinet. Pivot propriétaire obligatoire (cas cabinet, jurisprudence nommée 2024-2025, angle local NAQ, donnée chiffrée propre, contraste juridique précis).
- [ ] **Non-commodity content** : ce que Google appelle *« commodity content »* (synthèse générique reformulée) est dévalorisé. Vérifier que **au moins 1 H2** porte une perspective propriétaire qui ne pourrait pas exister sans l'expérience cabinet.
- [ ] **Couverture du query fan-out** : PAA et related searches (Bloc B) répondus dans le corps ET dans la FAQ — pas uniquement la requête head term.
- [ ] **Main content visuellement distinguable** des éléments annexes (sidebar, related posts Wix, footer). Vérifier sur l'aperçu Wix mobile + desktop.
- [ ] **Pas de chunking artificiel** : phrases courtes oui (LEARN-030), mais pas de fragmentation pour "AI-friendly".
- [ ] **Pas de fichiers ou markup spéciaux IA** : pas de `llms.txt`, pas de structured data inventée. Seul **FAQPage** est gardé (cohérent avec LEARN-041, utile pour rich results normaux).
- [ ] **Anti-scaled-content** : ne pas dupliquer ce sujet en plusieurs micro-articles. Si plusieurs angles → 1 pilier dense (cohérent avec LEARN-047).

### Bloc Process
- [ ] **Draft Wix poussé par API** (flux par défaut LEARN-064) : `ricos.min.json` régénéré depuis la version finale de l'article, garde-fou `nodes.length`/`faqCount`, draft `UNPUBLISHED` vérifié par GET. Fallback : copier-coller markdown par Nicolas (LEARN-002/004).
- [ ] **Lint passé** : `python3 scripts/lint_pipeline.py 0N-slug-article/` sans erreur
- [ ] Mise à jour `LEARNINGS.md` post-publication si nouveau learning identifié
- [ ] Mise à jour `ARTICLE_TEMPLATE.md` si nouveau pattern identifié
- [ ] **Commit Git local** : `git add -A`, vérifier que `.env` n'est PAS staged, puis `git commit -m "Article #N : slug"` (pas de `&&`)
- [ ] **Push GitHub** vers `origin/main` (`git push origin main`) — **sur confirmation explicite Nicolas uniquement** (voir mémoire `reference_repo_github.md`)
