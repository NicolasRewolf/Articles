# Métadonnées Wix — Article #6 — Passager victime d'un accident de la route

> Livrable Étape 4 du workflow — section SEO prête à coller dans Wix Studio.
> Date : 2026-05-17.

---

## 1. H1 (titre visible de l'article)

```
Passager victime d'un accident de la route : pourquoi vous êtes protégé même quand votre conducteur a tort
```

**Longueur** : 110 caractères (non contraint pour le H1).

---

## 2. Méta-title (panneau SEO Wix — champ « Titre de la page »)

```
Passager d'un accident de la route : vos droits Badinter
```

**Longueur** : 56 caractères (sous la limite Google ~60 char).

---

## 3. Méta-description (panneau SEO Wix — champ « Description de la page »)

```
Passager victime d'un accident ? Vous êtes protégé par la loi Badinter même si votre conducteur a tort. Vos droits, démarches et indemnisation à Bordeaux.
```

**Longueur** : 155 caractères (à la limite Google).

---

## 4. Slug (panneau SEO Wix — champ « URL de la page »)

```
indemnisation-passager-accident-route
```

**Longueur** : 37 caractères. URL finale :

```
https://www.jplouton-avocat.fr/post/indemnisation-passager-accident-route
```

**Sans accent strict** (LEARN-001). Distinct des slugs existants — pas de risque de doublon ni de cannibalisation avec l'article pilier `loi-badinter-85-...`.

---

## 5. Catégories Wix (2 catégories simultanées — coche dans le panneau Catégories du draft)

| Catégorie | ID Wix |
|---|---|
| **Ressources et notions juridiques** (catégorie publication articles) | `9477320f-5902-40e9-ace3-b0e3b6b8b51f` |
| **Accidents de la route** (catégorie thématique) | `34cbb933-76d6-4a2e-8048-7624dcbe738d` |

---

## 6. Tags suggérés (10-15 — panneau Tags Wix)

```
passager, loi badinter, article 3 badinter, accident de la route, accident voiture, indemnisation passager, victime non conductrice, faute inexcusable, FGAO, CIVI, tétraplégie, ayants droit, assurance auto, Bordeaux, Nouvelle-Aquitaine
```

15 tags. Mix : juridique pointu (loi badinter, article 3, faute inexcusable, FGAO, CIVI), profil victime (passager, victime non conductrice, ayants droit, tétraplégie), thématique (accident de la route, accident voiture, assurance auto), local (Bordeaux, Nouvelle-Aquitaine).

---

## 7. Image hero suggérée + alt text

**Brief création** : vue de l'intérieur d'une voiture côté passager arrière, ceinture visible, route floue à travers le pare-brise. Style sobre, naturel — banque image libre type Unsplash / Pexels. Éviter le visuel « accident dramatique » (LEARN-052 — pas de pathos).

**Alt text** :

```
Vue depuis la place passager arrière d'une voiture circulant sur une route — illustration article indemnisation passager d'accident
```

**Image optionnelle secondaire** (cartographie multi-modale H2 2) :

- Visuel : pictogrammes véhicules (voiture, moto, VTC, taxi, bus) en strip horizontal sobre
- Alt : « Pictogrammes des véhicules concernés par l'indemnisation passager : voiture, moto, VTC, taxi, bus »

---

## 8. Open Graph + Twitter Card (panneau Partage social Wix)

| Champ | Valeur |
|---|---|
| **OG Title** | Identique au méta-title : *« Passager d'un accident de la route : vos droits Badinter »* |
| **OG Description** | Identique à la méta-description : *« Passager victime d'un accident ? Vous êtes protégé par la loi Badinter même si votre conducteur a tort. Vos droits, démarches et indemnisation à Bordeaux. »* |
| **OG Image** | Image hero du post (Wix gère automatiquement le rendu) |
| **Twitter Card** | `summary_large_image` (par défaut Wix) |

---

## 9. Schema markup — JSON-LD FAQPage

⚠️ **Livré directement dans le chat** (bloc code minifié one-liner) à coller dans le champ « Marquage structuré » du panneau SEO Wix Studio du draft post (LEARN-027 + LEARN-041 — FAQPage uniquement par article ; Person + LegalService gérés au niveau site Wix).

**Vérification après publication** : passer l'URL publiée dans [Google Rich Results Test](https://search.google.com/test/rich-results) — vérifier que FAQPage est détecté en plus des schémas globaux du site.

---

## 10. Checklist finale 11 points (à passer juste avant publication)

- [ ] **H1** copié-collé tel quel dans le titre Wix (110 char OK)
- [ ] **Méta-title** ≤ 60 char dans le panneau SEO (56 char ✅)
- [ ] **Méta-description** ≤ 155 char dans le panneau SEO (155 char ✅ — à la limite)
- [ ] **Slug** `indemnisation-passager-accident-route` sans accent (LEARN-001 ✅)
- [ ] **2 catégories Wix** cochées : `Ressources et notions juridiques` + `Accidents de la route`
- [ ] **Tags** (15) saisis dans le panneau Tags
- [ ] **Image hero** uploadée + **alt text** complet ; nom de fichier sans accent (ex : `passager-accident-route-hero.jpg`)
- [ ] **Liens internes** convertis en URLs absolues `https://www.jplouton-avocat.fr/...`, sans `rel`, sans `target` (LEARN-024 — convention follow par défaut)
- [ ] **Liens externes** (Légifrance, Cour de cassation, ONISR, Sud Ouest) avec `target="_blank"` (coché dans Wix Studio à la sélection du lien) ET `rel="noopener noreferrer nofollow"` (à appliquer manuellement dans le panneau SEO du lien)
- [ ] **JSON-LD FAQPage** collé dans le champ « Marquage structuré » du panneau SEO Wix
- [ ] **Date de mise à jour visible** *« Dernière mise à jour : mai 2026. »* en italique en pied (LEARN-043) — cohérente avec le `dateModified` du Schema géré au niveau site

---

## Conventions de mise en forme Ricos (rappel — LEARN-024 + LEARN-025)

| Élément | Pattern Wix Ricos |
|---|---|
| Titres | HEADING level 2 et 3 — pas de markdown H4+ dans cet article |
| Paragraphes | PARAGRAPH classique avec décorations BOLD, ITALIC, LINK |
| Encadrés (définitions + chiffrés + mini-CTAs) | **BLOCKQUOTE** — convertir les `>` markdown en blocs BLOCKQUOTE Ricos |
| Listes à puces du sommaire / bullets intro / FAQ items | BULLETED_LIST + LIST_ITEM |
| FAQ collapsibles | **COLLAPSIBLE_LIST** + ITEMS — convertir le H2 6 + ses H3 questions en accordéon natif Wix |
| Séparateurs | DIVIDER entre les H2 |
| Liens internes | Pas de `rel`, pas de `target="_blank"` — convention follow par défaut |
| Liens externes (Légifrance, ONISR, Cour de cassation, Sud Ouest) | `target="_blank"` + `rel="noopener noreferrer nofollow"` |
| **Pas de bullets dans blockquotes** (LEARN-025) | Encadrés chiffrés rédigés en prose continue — déjà appliqué dans le markdown |

---

## Récap synthèse Étape 4

| Livrable | Statut | Format |
|---|---|---|
| `etape-4-article.md` | ✅ Livré (~4 150 mots ; voir alerte taille ci-dessous) | Markdown source |
| `etape-4-metadonnees-wix.md` | ✅ Présent fichier | Markdown — 10 sections SEO |
| JSON-LD FAQPage | ⏭️ À livrer dans le chat | Bloc code minifié one-liner |

**⚠️ Alerte taille** : article à ~4 150 mots vs cible BRIEF 2 000-2 500. **Dans la moyenne du pipeline** (#1 : 4 285 / #2 : 5 235 / #3 : 5 736 / #4 : 3 903 mots). Nicolas tranche entre (a) garder en l'état, (b) réduire à ~3 800 (cohérent #4), (c) réduire à 2 500 strict (gros travail de coupe — FAQ + H2 3 + H2 4 principalement).
