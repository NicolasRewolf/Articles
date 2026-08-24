# Métadonnées Wix — Article #15 : harcèlement scolaire

## 1. SEO

- **H1** : Harcèlement scolaire : faire reconnaître la faute et obtenir réparation pour votre enfant
- **Méta-titre** : Harcèlement scolaire : faute et indemnisation de l'enfant
- **Méta-description** : Plainte pénale, responsabilité de l'école ou de l'État, CIVI : les recours concrets pour faire reconnaître la faute et faire indemniser votre enfant.
- **Slug** : harcelement-scolaire-faute-indemnisation

*(Comptages : titre 57 ≤ 60 ; description 149 ≤ 155 ; slug ASCII pur.)*

## 2. Catégories Wix (2)

- Ressources et notions juridiques — `9477320f-5902-40e9-ace3-b0e3b6b8b51f`
- Victimes de délits ou crimes — `a755253f-65a6-49cc-b89e-e10e83840a75`

## 3. Tags

harcèlement scolaire, cyberharcèlement, indemnisation harcèlement scolaire, responsabilité de l'école, faute de l'État, CIVI, victime mineure, porter plainte harcèlement, loi harcèlement scolaire 2022, loi Attal, préjudice moral enfant, ITT, avocat victimes Bordeaux

## 4. Image hero + alt

- **Suggestion** : cartable posé seul dans un couloir d'école vide, ou enfant de dos à l'écart d'un groupe — lumière naturelle, sobre, aucun visage identifiable (mineurs).
- **Alt** : « Enfant seul dans un couloir d'école, cartable au dos — harcèlement scolaire et recours des parents »
- Sources libres : Unsplash/Pexels (`school hallway alone`, `child backpack corridor`).

## 5. Carte des liens

**Internes (follow, URL absolue, sans `rel`)** — 13 :
2 conversion (`/honoraires-rendez-vous` ×2, `/indemnisation-des-victimes/victimes-de-delits-ou-crimes` ×2) · 7 notions (ITT, dépôt de plainte, dossier médical, SARVI-ou-CIVI, guide CIVI, pretium doloris, assigner l'État faute lourde) · 3 affaires (CIVI incendie Bordeaux, CIVI Tarbes mineure, Foulon-Baude) · 2 bio (notre-cabinet, proposition de loi inceste).

**Externes (`target="_blank" rel="noopener noreferrer nofollow"` — appliqué par `md_to_ricos.py`)** — 11 :
Légifrance ×8 (222-33-2-3 ×2, L. 11-1 CJPM, 1242, L. 111-6, L. 911-4, 706-3, 706-5, décret 2023-782) · TA Versailles (communiqué) · DEPP n° 25.43 (PDF) · e-Enfance.

Tous les internes testés HTTP 200 le 2026-08-24 (LEARN-057). Montants/dates des affaires vérifiés dans les posts publiés (LEARN-063) : CIVI Bordeaux 20 659 € ; Tarbes victime mineure (17 ans, faits 2017), CIVI saisie 2024.

## 6. JSON-LD FAQPage

Livré **dans le chat** (bloc code minifié one-liner, 9 questions — LEARN-027/041). À coller dans « Marquage structuré » du panneau SEO Wix du post. Ne pas ajouter Person/LegalService (gérés au niveau site).

## 7. Push Wix

- **Flux** : draft **`UNPUBLISHED`** via API REST (`ExecuteWixAPI`, scope SITE, memberId `07454f1f-c54a-4308-b897-19be554db88a`, seoSlug + 2 categoryIds) — LEARN-064.
- **Garde-fou avant POST** : `nodes.length` cohérent + `faqCount = 9`.
- **draftPostId** : `c6fe0b29-aeb5-4f4c-bf1a-a5fdf3361dd8` — poussé le 2026-08-24 en compaction de transport (44 118 octets, textes identiques au `ricos.min.json` canonique), statut `UNPUBLISHED` vérifié par GET (préfixe de 260/279 textes strictement identique, queue au-delà de la troncature du viewer MCP ; POST atomique accepté).
- Jamais de publication sans ordre explicite.

## 8. Refresh (M+6 : février 2027)

Déclencheurs à vérifier :
- **Nouvelle note DEPP** (données de la journée nationale nov. 2025 — publication attendue courant 2026) → mettre à jour l'encadré chiffré.
- **Recodification CPP au 01/01/2029** : 706-3 / 706-5 portent `ABROGE_DIFF` — surveiller la renumérotation (ordonnance n° 2025-1091).
- Jurisprudence : appels éventuels du jugement TA Versailles 21/03/2025 ; premières décisions publiées sur 222-33-2-3.
- Réforme éventuelle du code de l'éducation (décret harcèlement complémentaire).
