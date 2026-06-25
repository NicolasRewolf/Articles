# Métadonnées SEO — Article #1
## Prêtes à coller dans Wix Studio

> Toutes les méta-données du post à renseigner dans Wix Studio (post → Paramètres SEO).
> Validées en Étape 3, à appliquer maintenant en Étape 4.

---

## 1. Titre H1 (champ "Titre du post" Wix)

**Accident de moto : pourquoi votre indemnisation diffère de celle d'un automobiliste (guide 2026)**

→ 110 caractères. C'est le titre éditorial principal de l'article.

---

## 2. Méta-title (onglet SEO Wix → "Titre SEO")

**Indemnisation accident moto : guide motard 2026**

→ **49 caractères**. Laisse de la marge pour le suffixe Wix automatique (« | Cabinet Plouton » si configuré côté site).

⚠️ Si Wix ajoute « | Cabinet Plouton » automatiquement, le total devient ~70 char → un poil long. Surveiller. Si Wix coupe à 60 dans le SERP, retirer le suffixe au niveau global Wix ou raccourcir manuellement à : **« Indemnisation accident moto : guide motard »** (44 char).

---

## 3. Méta-description (onglet SEO Wix → "Description SEO")

**Loi Badinter, postes de préjudice, équipement détruit : ce qui change vraiment pour un motard blessé. Guide 2026 par le Cabinet Plouton (Bordeaux).**

→ **149 caractères**. Sous le seuil Google de 155-160. Mentionne 3 sous-thèmes différenciants + millésime + cabinet + géo.

---

## 4. Slug (URL du post — onglet SEO Wix → "Slug")

**`indemnisation-accident-moto-motard`**

→ 33 caractères, **ASCII pur** (sans accent — règle LEARN-001 stricte), contient les mots-clés majeurs.

**URL finale prévue :**
`https://www.jplouton-avocat.fr/post/indemnisation-accident-moto-motard`

⚠️ **Distinct du slug existant** `loi-badinter-85-comprendre-vos-droits...` → pas de risque de doublon ni de cannibalisation.

---

## 5. Catégories Wix (onglet "Catégories" du post)

Le post doit être tagué dans les **DEUX catégories** suivantes :

| Catégorie | ID interne Wix |
|---|---|
| **Ressources et notions juridiques** | `9477320f-5902-40e9-ace3-b0e3b6b8b51f` |
| **Accidents de la route** | `34cbb933-76d6-4a2e-8048-7624dcbe738d` |

---

## 6. Tags / mots-clés (onglet "Tags" du post)

À ajouter dans la section Tags de Wix (espace séparé ou virgule, selon UI Wix) :

```
loi-badinter
indemnisation
accident-moto
motard
postes-prejudice
dintilhac
pretium-doloris
prejudice-agrement
dfp
deficit-fonctionnel-permanent
prejudice-esthetique
brulures-glissade
equipement-moto
garantie-conducteur
2025
```

---

## 7. Image hero (onglet "Image en vedette")

**Suggestion** : photo authentique sobre — moto immobilisée après accident, perspective sur le casque ou l'équipement endommagé, **sans visage identifiable**, sans pathos appuyé.

**Alt text obligatoire** :
> *Motard blessé : indemnisation après un accident — casque et équipement sur le bord de route, illustration article guide 2026 Cabinet Plouton*

→ Si tu utilises une banque d'images libres : Unsplash, Pexels, recherche `motorcycle accident`, `helmet road`. Privilégier les images **non dramatiques** (pas de blessures visibles, pas de sirènes) — cohérent avec le ton sobre.

---

## 8. Open Graph (Wix → Réseaux sociaux)

Si Wix expose ces champs séparément (parfois sous "Partage social") :

| Champ | Valeur |
|---|---|
| **og:title** | Accident de moto : pourquoi votre indemnisation diffère (Cabinet Plouton) |
| **og:description** | 575 motocyclistes tués en 2025. Loi Badinter, postes de préjudice, équipement : guide complet par le Cabinet Plouton, avocat à Bordeaux. |
| **og:image** | Même image que l'image hero |
| **og:type** | article |

---

## 9. Schema markup (onglet "Marquage structuré" ou widget HTML Embed)

### 9.a) `BlogPosting` (auto par Wix mais à vérifier)

Wix Studio génère habituellement automatiquement le schema `BlogPosting`. Vérifier sur la page publiée via [https://validator.schema.org/](https://validator.schema.org/) que les champs suivants sont bien remplis : `headline`, `datePublished`, `author`, `publisher`, `image`, `mainEntityOfPage`.

### 9.b) `FAQPage` (à coller manuellement)

Le COLLAPSIBLE_LIST de Wix **ne génère pas automatiquement** le schema FAQPage. Coller le JSON-LD complet présent dans **[`etape-4-faq-schema.json`](etape-4-faq-schema.json)** dans le module SEO Wix (champ "Custom code" ou "Additional tags") ou via un widget HTML Embed positionné en bas de page.

---

## 10. Checklist finale avant publication

- [ ] H1 collé dans le champ Titre du post
- [ ] Méta-title (49 char) collé dans champ Titre SEO
- [ ] Méta-description (149 char) collée dans champ Description SEO
- [ ] Slug `indemnisation-accident-moto-motard` appliqué (sans accent)
- [ ] 2 catégories cochées (Ressources et notions juridiques + Accidents de la route)
- [ ] 15 tags ajoutés
- [ ] Image hero choisie + alt text renseigné
- [ ] JSON-LD FAQPage collé (module SEO ou HTML Embed)
- [ ] Liens externes (Légifrance / ONISR / Judilibre / data.gouv) : **target="_blank" + rel="noopener noreferrer nofollow"** (LEARN-024)
- [ ] Liens internes (`/post/...`, `/indemnisation-...`) : pas de target="_blank", pas de rel (follow par défaut)
- [ ] Post en mode **draft** (UNPUBLISHED) jusqu'à validation finale
