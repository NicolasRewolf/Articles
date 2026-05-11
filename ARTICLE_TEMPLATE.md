# ARTICLE_TEMPLATE — Structure réutilisable affinée

> Squelette des livrables du workflow 4 étapes. **Affiné après chaque article** sur la base des patterns qui ont marché.
> Dernière mise à jour : 2026-05-11 (post article #1 — Motard blessé indemnisation).

---

## Cap général (validé sur article #1 + patterns cognitifs notebook 2026-05-11)

| Paramètre | Valeur cible |
|---|---|
| **Volume** | 2 500-2 800 mots (data-driven Plouton 28j — médiane top performers = 1 700, cible un peu au-dessus quand profondeur distinctive justifiée) |
| **Structure** | 1 H1 + 1 intro + 1 TDM + 5-7 H2 + ~10-15 H3 + FAQ 5-7 Q + CTA final |
| **Encadrés** | 3-6 définitions (BLOCKQUOTE) + 1-2 encadrés chiffrés (BLOCKQUOTE) |
| **Liens internes** | 1 lien tous les ~250 mots — 3 vers pages expertise/CTA + 4-7 vers articles ressources cluster + 2-4 vers affaires cabinet (preuves) |
| **CTA** | 3 au total : mini-CTA inline #1 (post-intro), mini-CTA inline #2 (milieu), CTA final |
| **Ton** | Sobre, empathique, précision juridique, anti-marketing |
| **Sourcing** | Chaque chiffre = millésime + source primaire ; chaque article de loi = lien Légifrance |
| **Densité info (LEARN-028)** | Chaque H2 = 1 chiffre sourcé + 1 cas concret + 1 implication pratique. Pas de creux narratif. |
| **Phrases (LEARN-030)** | 16-20 mots idéal, **JAMAIS > 40 mots** |
| **Paragraphes (LEARN-030)** | 1-3 phrases, **1 seule idée** par paragraphe |
| **Front-loading (LEARN-029)** | Tous H2/H3/paragraphes/bullets commencent par les **2-3 mots les plus porteurs de sens** |

## Pattern Mini-CTA #1 "double-face" (LEARN-031)

Reconnaître les limites = +crédibilité (Modèle de Probabilité d'Élaboration). Pourrait débloquer le 0 % conversion observé historiquement.

**Format** :

> **Vous êtes [persona] confronté à [situation] ?**
> Ce guide gratuit couvre [80 % des situations / la plupart des cas].
> Pour les [20 % restants / cas complexes spécifiques] — [exemple concret : *contestation d'expertise, faute opposée par l'assureur, séquelles graves*] — un avocat fait la vraie différence.
> [CTA spécifique — pas "En savoir plus" ou "Contact" → "Parler à un avocat en accidents de la route" / "Demander un premier RDV d'information"]

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

```markdown
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

### Intro (~200-250 mots) — Pattern Version D (validé)
**Structure cognitive optimisée :**
1. **Phrase psychologique d'ouverture** (vérité du persona — résonne immédiatement)
2. **Chiffre brutal sourcé** (paragraphe 2 — autorité + légitimation)
3. **Bullets "Ce que vous allez comprendre"** (4 items — mini-sommaire intégré, scannable)
4. **Signature autorité cabinet** (1 ligne en italique — ancrage E-E-A-T)

### Mini-CTA inline #1 (post-intro) — Pattern validé article #1
Format BLOCKQUOTE :
> **Mini-CTA**
> [Question empathique : "Vous êtes [persona] confronté à [situation], et ces démarches vous dépassent ?"]
> Le Cabinet Plouton accompagne [thématique] depuis plus de 20 ans. [Parler à un avocat](URL contact).

### TDM (juste après l'intro)
- 5-7 entrées H2 avec liens d'ancrage `#section-slug`
- Chaque H2 reçoit son `id` correspondant
- Format liste à puces numérotée

### H2 1 — Contextualisation thématique (pourquoi le sujet est spécifique)
- Encadré chiffré (BLOCKQUOTE avec titre gras + bullets)
- Transition vers cadre légal

### H2 2 — Cadre légal sourcé
- 3-4 H3 selon les articles de loi mobilisés
- Encadrés définition (BLOCKQUOTE) pour concepts juridiques clés
- Cross-link vers article pilier ressources (cluster sémantique)

### H2 3 — Section CŒUR DIFFÉRENCIANTE (la profondeur distinctive)
- 4-6 H3 sur les éléments distinctifs
- Cross-links sortants vers articles ressources existants (délégation profondeur)
- Lien vers affaire cabinet "haut spectre" en preuve sociale

### H2 4 — Cas particuliers (2-4 H3)
- Exploite le cluster sémantique (cross-links variés)
- Lien affaire cabinet en preuve

### H2 5 — Procédure (3 H3)
- Expertise médicale (cross-link "dossier médical")
- Offre assureur (cross-link page d'expertise + formulation cabinet)
- Contentieux (lien affaire contentieuse)

### Mini-CTA inline #2 (après H2 5)
> Pour aller plus loin sur [thématique], consultez [notre page d'expertise dédiée](URL).

### H2 6 — FAQ (COLLAPSIBLE_LIST)
- 5-7 questions
- Chaque réponse : **40-80 mots**, **concept-clé en ouverture** (citabilité LLM)
- Sourcing intégré (lien Légifrance/ONISR dans la réponse quand pertinent)

### CTA final (~100 mots)
- Phrase de bascule empathique
- Présentation courte cabinet
- Lien fort vers `/honoraires-rendez-vous` ou page expertise

---

## Stratégie de liens internes

| Type | Cible | Quantité indicative |
|---|---|---|
| Pages d'expertise (CTA) | `/indemnisation-...` ou `/defense-...` ou `/droit-...` | 2-3 |
| Page contact | `/honoraires-rendez-vous` | 1 (CTA final) |
| Articles ressources (cluster) | autres articles `/post/` de la catégorie Ressources | 4-7 |
| Affaires cabinet (preuves) | `/post/` cas réels | 2-4 |

---

## Stratégie GEO (citabilité LLM)

- **Encadrés définitions** (BLOCKQUOTE) — un par concept juridique central
- **Encadré chiffré** (BLOCKQUOTE avec titre gras + bullets) — pour le hook chiffré principal
- **Listes ordonnées** — pour les sections "Les X étapes de...", "Les Y postes de..."
- **FAQ COLLAPSIBLE_LIST** — 5-7 Q&A
- **JSON-LD FAQPage** — bloc séparé prêt-à-coller dans module SEO Wix (le COLLAPSIBLE_LIST natif ne génère pas le schema automatiquement)
```

---

## Étape 4 — Livrables OBLIGATOIRES (ne rien zapper)

Chaque article #N doit produire dans son dossier `0N-slug-article/` :

1. **`etape-4-article.md`** — article complet en markdown (lecture/archive + copier-coller Wix Studio par Nicolas)
2. **`etape-4-metadonnees-wix.md`** — **OBLIGATOIRE, NE PAS ZAPPER** — 10 sections prêtes à coller : H1, méta-title ≤ 60, méta-description ≤ 155, slug sans accent, **catégories Wix (2 IDs : Ressources et notions juridiques + thématique)**, tags (10-15), image hero + alt, Open Graph, schema markup, checklist finale 11 points. *(Erreur observée sur article #1 : oublié au début, ajouté en correction sur question explicite de Nicolas.)*
3. **JSON-LD FAQPage** — **livré DIRECTEMENT dans le chat** (bloc code Markdown, JSON minifié one-liner, avec `type="application/ld+json"`). **PAS de fichier `.json` ou `.html` séparé** (LEARN-027 — validé : Wix Studio rejette les fichiers HTML pour ce champ, copier-coller depuis le chat est l'unique méthode fiable).
4. *(optionnel)* **`etape-4-corrections-rouge.html`** — visualisation rouge des passages modifiés si fact-check post-rédaction a entraîné des corrections.

## Étape 4 — Fact-check NotebookLM obligatoire AVANT rédaction (LEARN-026 anti-récidive)

**Règle non négociable issue de l'article #1 :** sur l'article #1, j'ai produit 3 erreurs juridiques (Art. 4 confondu avec Art. 5, Art. 5 confondu avec Art. 6, Art. 12 confondu avec Art. 16) parce que j'ai rédigé sans interroger NotebookLM. Anti-pattern documenté, à ne plus reproduire.

**Procédure AVANT de rédiger chaque section juridique :**

1. **Vérifier que le notebook NotebookLM est rempli** sur le sujet de l'article. Si VIDE → alerter Nicolas, attendre qu'il dépose les sources, OU rédiger en mode "fourchettes prudentes" sans affirmations chiffrées précises.
2. **Pour chaque numéro d'article de loi cité** → `ask_question` NotebookLM pour confirmer (numéro exact + texte verbatim + URL LEGIARTI).
3. **Pour chaque jurisprudence citée** → `ask_question` pour confirmer (numéro de pourvoi + date + chambre + apport).
4. **Pour chaque fondement juridique attribué** → `ask_question` pour confirmer (ne JAMAIS extrapoler à partir de SERP top 10).
5. **Si l'article est central pour l'argumentation** → double-check via WebSearch ciblée `allowed_domains=["legifrance.gouv.fr"]` pour obtenir l'URL LEGIARTI exacte.

→ NotebookLM (5 questions max, regrouper si possible). C'est la règle qui a sauvé l'article #1 du désastre juridique.

## Étape 4 — Procédure de livraison fin de rédaction

À la fin de la rédaction Étape 4, **présenter à Nicolas en un seul message** avec ce format :

```
🛑 Étape 4 — Phase 1 (rédaction) terminée. STOP avant push API.

Livrables :
1. 📄 etape-4-article.md — article complet (~2 600-2 800 mots)
2. 📄 etape-4-metadonnees-wix.md — 10 sections SEO prêtes à coller
3. JSON-LD FAQPage ci-dessous (copier-coller dans le champ "Marquage 
   structuré" du panneau SEO Wix Studio du post) :

   ```
   <script type="application/ld+json">{...JSON minifié one-liner...}</script>
   ```

Récap fact-check NotebookLM : [N questions posées, M corrections appliquées]
Sources mobilisées : [résumé bref]

Sur "OK push" → je crée le draft Wix via API en status UNPUBLISHED.
```

**Ne JAMAIS finir l'Étape 4 sans avoir produit les 3 livrables ci-dessus.**

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

### Pattern HTML (si copier-coller markdown au lieu de push API)

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
  <p><strong>Définition. [Terme]</strong> — [définition sourcée]. (<a href="URL">Texte complet sur Légifrance</a>.)</p>
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

### Bloc JSON-LD FAQPage (à coller dans le module SEO Wix)

Voir `etape-4-faq-schema.json` de chaque article. Structure :

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Q1 text",
     "acceptedAnswer": {"@type": "Answer", "text": "Réponse 40-80 mots"}},
    ...
  ]
}
```

### Métadonnées prêtes à coller (Étape 4)

- **Titre** : [méta-title ≤ 60 char]
- **Description** : [méta-description ≤ 155 char]
- **Slug** : [slug-sans-accent]
- **Tags** : [tag1, tag2, tag3]
- **Catégories** : Ressources et notions juridiques + [thématique]
- **Image hero** : [source / brief alt text]

---

## Checklist qualité (à passer avant push)

- [ ] Toutes les affirmations juridiques sourcées (Légifrance/Judilibre) ou prudemment formulées
- [ ] `⚠️ À vérifier` retiré ou résolu
- [ ] **Slug sans accent** (LEARN-001 — règle stricte)
- [ ] **HTML/Ricos** propre, pas de markdown résiduel dans le contenu final
- [ ] Liens internes en **URL absolue** (`https://www.jplouton-avocat.fr/...`)
- [ ] **Convention `rel` respectée** : internes = pas de `rel` (follow par défaut) + pas de `target="_blank"` ; externes = `target="_blank" rel="noopener noreferrer nofollow"` (voir mémoire `feedback_liens_follow_nofollow.md`)
- [ ] Alt text sur toutes les images
- [ ] FAQ en fin d'article (avec JSON-LD séparé prêt à coller)
- [ ] Au moins 1 lien vers page d'expertise + 1 CTA final + 1-2 mini-CTAs inline
- [ ] Méta-title ≤ 60 caractères
- [ ] Méta-description ≤ 155 caractères
- [ ] **Phrases ≤ 40 mots max, idéal 16-20** (LEARN-030 — relire et raccourcir les phrases longues)
- [ ] **Paragraphes ≤ 3 phrases, 1 seule idée par paragraphe** (LEARN-030)
- [ ] **Front-loading appliqué** sur tous les H2/H3/bullets : les 2-3 premiers mots portent le sens (LEARN-029)
- [ ] **Densité info** : chaque H2 contient au moins 1 chiffre sourcé + 1 cas concret + 1 implication pratique (LEARN-028 — pas de creux narratif)
- [ ] **CTAs spécifiques** : zéro libellé vague (pas de « En savoir plus » / « Cliquez ici » / « Contact ») — LEARN-037
- [ ] **Pas de jargon obscur** dans les éléments scannés (H2, H3, ancres) — vocabulaire du lecteur, pas du cabinet (LEARN-038)
- [ ] **Mini-CTA #1 "double-face"** appliqué (reconnaît les limites du guide, précise pour qui un avocat est utile) — LEARN-031
- [ ] **Storytelling cognitif** en ouverture d'au moins 1 section H2 critique (détails perceptuels ou conceptuels) — LEARN-035
- [ ] **Push draft only** (UNPUBLISHED) — jamais de publication directe sans validation explicite Nicolas
- [ ] Mise à jour `LEARNINGS.md` post-publication
- [ ] Mise à jour `ARTICLE_TEMPLATE.md` si nouveau pattern identifié
- [ ] **Commit Git local** (`git add -A && git commit -m "Article #N : slug"`) — vérifier que `.env` n'est PAS staged
- [ ] **Push GitHub** vers `origin/main` (`git push origin main`) — **sur confirmation explicite Nicolas uniquement** (voir mémoire `reference_repo_github.md`)
