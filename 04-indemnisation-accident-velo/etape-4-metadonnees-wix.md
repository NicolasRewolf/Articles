# Métadonnées Wix — Article #4 : Cycliste renversé

> Livrable Étape 4 / Phase 2 — métadonnées SEO prêtes à coller dans Wix Studio.
> Article #4 du pipeline éditorial Cabinet Plouton.
> Date : 2026-05-13.

---

## 1. H1 (titre du post)

```
Cycliste renversé : preuves à réunir et étapes pour se faire indemniser (2026)
```

**Longueur** : 78 caractères. Affichage Wix Studio sur le post.

---

## 2. Méta-title (≤ 60 caractères — champ SEO Wix)

```
Cycliste renversé : indemnisation, preuves et étapes (2026)
```

**Longueur** : **56 caractères** ✅ (sous le seuil 60).

Contient `cycliste renversé` (synonyme univers amont `accident vélo`, 1 300/mois) + `indemnisation` (head term 70/mois) + signal de fraîcheur `(2026)`.

---

## 3. Méta-description (≤ 155 caractères — champ SEO Wix)

```
Renversé à vélo ? Voici les preuves à figer, vos droits sous Badinter et les étapes jusqu'à indemnisation. Cabinet Plouton, Bordeaux.
```

**Longueur** : **134 caractères** ✅ (sous le seuil 155).

Adressage direct « vous » (LEARN-052), promesse opérationnelle (preuves + étapes), ancrage local Bordeaux.

---

## 4. Slug (sans accent — LEARN-001 obligatoire)

```
cycliste-renverse-preuves-indemnisation
```

**Longueur** : 38 caractères. URL finale :

```
https://www.jplouton-avocat.fr/post/cycliste-renverse-preuves-indemnisation
```

**Vérification** : 0 accent. 0 caractère spécial. Tirets uniquement. Descriptif. Conforme LEARN-001 strict.

---

## 5. Catégories Wix (2 catégories — sélecteur Wix Studio)

| # | Catégorie | ID Wix |
|---|---|---|
| 1 | **Ressources et notions juridiques** | `9477320f-...` *(à vérifier dans Wix Studio — id existant du pipeline)* |
| 2 | **Indemnisation des victimes** *(thématique)* | *(à créer ou réutiliser si existante — sinon utiliser « Accidents de la route »)* |

**Note** : la catégorie thématique peut basculer sur « Accidents de la route » si plus pertinent pour la taxonomie actuelle du site. À arbitrer côté Nicolas lors de l'ingestion Wix.

---

## 6. Tags suggérés (10-15 — champ Tags Wix)

```
cycliste renversé
accident vélo
indemnisation accident vélo
loi Badinter cycliste
preuves accident vélo
expertise médicale
FGAO
vélo électrique
VAE
speed-bike
nomenclature Dintilhac
usager vulnérable
accident vélo Bordeaux
cabinet Plouton
nid de poule cycliste
```

**Total** : 15 tags. Couvrent l'univers sémantique head term + long-tail + spécificités cyclistes + ancrage local + cabinet.

---

## 7. Image hero (à fournir / générer)

**Source recommandée** : photo libre de droits HD horizontale (format 16:9 ou 2:1).

**Sources libres** :
- [Unsplash — « cyclist Bordeaux »](https://unsplash.com/s/photos/cyclist-bordeaux)
- [Pexels — « urban cyclist »](https://www.pexels.com/search/urban%20cyclist/)
- [Wirestock](https://wirestock.io/)

**Brief visuel** :
- Cycliste urbain (vélotaffeur 30-40 ans) en gros plan main + guidon + intersection en arrière-plan.
- Tons sobres, ville européenne (pavés bienvenus — Bordeaux non obligatoire).
- **Pas de visage identifiable** (RGPD + déontologie cabinet).
- **Pas de drame visuel**, pas de sang, pas de pleurs. Ton sobre, professionnel.

**Alt text (champ Wix obligatoire pour accessibilité + SEO)** :

```
Cycliste urbain à l'arrêt à une intersection à Bordeaux — illustration article indemnisation après accident à vélo, Cabinet Plouton.
```

---

## 8. Open Graph (partage social — auto-généré par Wix Studio depuis Méta-title + Méta-description + Image hero)

**Vérification à faire côté Wix Studio panneau SEO** :

- `og:title` = Méta-title ci-dessus (56 c)
- `og:description` = Méta-description ci-dessus (134 c)
- `og:image` = Image hero ci-dessus (idéalement ≥ 1 200 × 630 px)
- `og:url` = URL canonique de l'article
- `og:type` = `article`
- `twitter:card` = `summary_large_image`

**Twitter title fallback** : *« Cycliste renversé : indemnisation, preuves et étapes (2026) — Cabinet Plouton »* (76 c, sous le seuil Twitter de 70 mais lisible).

---

## 9. Schema markup (JSON-LD)

**FAQPage uniquement** — LEARN-041. Les schémas Person (Maître Plouton) et LegalService (Cabinet) sont gérés au niveau du site Wix Studio, **pas de duplication par article**.

**Le bloc `<script type="application/ld+json">` minifié one-liner sera livré DIRECTEMENT dans le chat** (LEARN-027) à la fin de l'Étape 4, à coller dans le champ « Marquage structuré » du panneau SEO Wix Studio du draft post.

**À tester après publication** : [Google Rich Results Test](https://search.google.com/test/rich-results) — vérifier que FAQPage est détecté en plus des schémas globaux Person + LegalService.

---

## 10. Checklist finale 11 points (avant publication)

### Bloc Sourcing & juridique
- [ ] Toutes affirmations juridiques sourcées (Légifrance/Cass.) ou prudemment formulées — **✅ via Bloc A + A.5 NotebookLM**
- [ ] Chaque jurisprudence : n° pourvoi + date + chambre confirmés — **✅** (Cass. 2e civ. 19/06/2025, 21/12/2023, 28/03/2019, 18/03/1998)
- [ ] Fact-check NotebookLM effectué AVANT rédaction — **✅** (5 zones grises levées en A.5)

### Bloc E-E-A-T + Information Gain
- [ ] Au moins 2-3 éléments distinctifs absents du top 10 SERP — **✅ 5 territoires vierges exploités**
- [ ] Bio auteur Maître Plouton en pied d'article — **✅**
- [ ] Date de mise à jour visible en italique — **✅** *« Dernière mise à jour : mai 2026. »*
- [ ] 3 ancrages Bordeaux/Nouvelle-Aquitaine minimum — **✅ 5 ancrages** (intro + CTA final + bio + Pellegrin + TJ Bordeaux)

### Bloc Schema markup
- [ ] JSON-LD FAQPage livré dans le chat (UNIQUEMENT FAQPage) — **livré en fin de message Étape 4**
- [ ] Test passé sur Google Rich Results Test après publication

### Bloc Standards Wix
- [ ] **Slug sans accent** — **✅** `cycliste-renverse-preuves-indemnisation`
- [ ] Liens internes en URL absolue — **✅** tous en `https://www.jplouton-avocat.fr/...`
- [ ] **Convention rel respectée** : internes = pas de `rel` ni `target` ; externes = `target="_blank" rel="noopener noreferrer nofollow"` — **✅** (LEARN-024)
- [ ] Pas de bullets dans blockquotes — **✅** (LEARN-025, prose continue)
- [ ] Alt text sur image hero
- [ ] Méta-title ≤ 60 — **✅ 56 c**
- [ ] Méta-description ≤ 155 — **✅ 134 c**

### Bloc Voix victime / main tendue (LEARN-052)
- [ ] Adressage direct « vous » — **✅** (chassé « la victime »)
- [ ] Reconnaissance du vécu en ouverture des sections critiques — **✅** intro + H2 1 + H2 4 + H2 5
- [ ] Voix cabinet « nous » — **✅** bio + CTA + 5 pipes solution
- [ ] CTAs en invitation humaine — **✅** *« Si vous voulez en parler »* / *« premier échange sans engagement »*
- [ ] Reconnaissance limites du guide — **✅** mini-CTA #1 + CTA final
- [ ] Garde-fous respectés : pas de pathos, pas d'exclamation marketing, pas d'émoji, pas d'urgence factice — **✅**

### Bloc Cluster & maillage
- [ ] 3-5 cross-links cluster sémantique — **✅ 14 cross-links** (5 ressources + 5 affaires + 3 pages expertise + 1 cluster motard)
- [ ] Date de prochain refresh dans commit message (M+6 LEARN-046)

### Bloc Process
- [ ] Livrable markdown (Nicolas copie-colle dans Wix Studio + refait mise en page) — **✅**
- [ ] Commit Git local après ingestion
- [ ] Push GitHub sur confirmation explicite Nicolas

---

## Bonus — Note pour Nicolas lors de l'ingestion Wix

**Conversion markdown → Ricos** (template ARTICLE_TEMPLATE.md p.314-326) :

- Les `## H2` deviennent **HEADING level 2**.
- Les `### H3` deviennent **HEADING level 3**.
- Les `> BLOCKQUOTE` (encadrés définition, ⚠️ alerte, mini-CTAs) deviennent **BLOCKQUOTE Ricos**.
- Les `- listes` deviennent **BULLETED_LIST + LIST_ITEM**.
- Les **2 tableaux** (« qui paie selon le scénario » + « VAE vs speed-bike ») : Wix Studio gère les tables, mais si la conversion est capricieuse, basculer en BULLETED_LIST structuré (1 item par ligne du tableau).
- La **FAQ** (H2 6 — 8 questions) doit être convertie en **COLLAPSIBLE_LIST + ITEM** pour l'effet accordéon.
- Le **séparateur `---`** devient **DIVIDER**.

**Liens** :
- Liens internes (`jplouton-avocat.fr`) : laisser tels quels, Wix les détecte automatiquement.
- Liens externes (Légifrance, ONISR) : déjà au format HTML inline `<a ... target="_blank" rel="noopener noreferrer nofollow">…</a>`, à coller tel quel.

**Date prochain refresh** : à noter dans le commit message Git → **novembre 2026** (LEARN-046 — capte la vague locale Bordeaux d'automne identifiée en B.4).
