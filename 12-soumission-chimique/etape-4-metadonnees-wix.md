# Métadonnées Wix — Soumission chimique (#12)

## Panneau SEO Wix Studio
- **Titre SEO (≤60)** : Soumission chimique : vos droits sans souvenir des faits
- **Slug** : `soumission-chimique-victime-preuve-recours`
- **URL publiée** : `https://www.jplouton-avocat.fr/post/soumission-chimique-victime-preuve-recours`
- **Meta description (≤155)** : Droguée à votre insu ? L'administration d'une substance est une infraction en soi. Preuves, délais, plainte et indemnisation : ce que dit la loi.
- **Excerpt / chapô** : Ne pas se souvenir n'est pas l'exception : c'est le résultat recherché. Le code pénal punit l'administration d'une substance à l'insu d'une personne, même si l'agression n'est pas prouvée. Preuves, délais et indemnisation, expliqués pas à pas.

## Catégories (2 — taguer les deux)
- Ressources et notions juridiques — `9477320f-5902-40e9-ace3-b0e3b6b8b51f`
- Victimes de délits ou crimes — `a755253f-65a6-49cc-b89e-e10e83840a75`

## Tags suggérés
soumission chimique, drogue du violeur, GHB, agression sexuelle, viol, consentement, analyse toxicologique, analyse capillaire, CIVI, indemnisation victime, preuve pénale, porter plainte, prescription pénale, violences sexuelles, avocat Bordeaux

## Image hero (à fournir)
- Suggestion : verre abandonné sur une table dans une lumière froide, ou couloir d'appartement au petit matin — **sobre, sans visage, sans mise en scène de l'agression**. Éviter tout cliché « pilule dans le verre » qui réduit le sujet au GHB, alors que les médicaments sédatifs dominent.
- **Alt** : « Soumission chimique — droits, preuves et recours de la victime ».

## Carte des liens
- **Internes (19 liens SELF, sans `rel`, sans `target`)** : dont 6 ancres de sommaire. Pages d'expertise : `/indemnisation-des-victimes/victimes-de-delits-ou-crimes`. Contact : `/honoraires-rendez-vous` (×3). Ressources : `itt-pénale-définition-en-2025`, `dépôt-de-plainte-en-france-comment-porter-plainte-efficacement`, `indemnisation-civi-2025-guide-complet-pour-les-victimes-d-infractions`, `sarvi-ou-civi-indemnisation-victimes`. Affaires cabinet (lien obligatoire) : `cabinet-plouton-indemnisation-victime-viol-civi-tarbes` (×2, corps + FAQ), `victimes-de-viol-incestueux-et-d-agression-sexuelle-le-cabinet-obtient-devant-la-civi-plus-de-130`, `proposition-de-loi-inceste-et-imprescriptibilité-…` (bio). Cabinet : `/notre-cabinet`.
- **Externes (9 liens `target="_blank" rel="noopener noreferrer nofollow"`)** : Légifrance (art. 222-30-1, art. 222-22, art. 7 CPP, art. 8 CPP, art. 706-5 CPP, loi n° 2025-1057, décret n° 2025-1208, arrêté du 11 décembre 2025) et ANSM (rapport d'enquête 2024, PDF).

## Push API (LEARN-064)
- `memberId` (auteur Me Plouton) : `07454f1f-c54a-4308-b897-19be554db88a`
- `siteId` : `0870235c-b92d-4a69-a2f4-25a976ae5f0c` (scope SITE obligatoire)
- `seoSlug` : `soumission-chimique-victime-preuve-recours`
- `richContent` : `ricos.min.json` (51 Ko ; garde-fou : **80 nœuds**, 20 titres, **10 questions de FAQ**, 19 liens internes SELF, 9 externes BLANK+rel).
- `draftPostId` : **`a1a259ee-4bdd-44bb-9987-6e649b026ed6`** — poussé le 2026-08-07, statut **`UNPUBLISHED`** vérifié par `GET`.
- **Contrôle après POST** : 80 nœuds envoyés / 80 relus, FAQ 10 envoyée / 10 relue, 2 `categoryIds` posés. ✅
- *Note de transport* : le payload a été envoyé dans une forme **compactée** (champs vides `id:""`, `nodes:[]`, `decorations:[]`, `paragraphData:{}` retirés) — 42 Ko au lieu de 51. Document **strictement identique** (258 nœuds de texte, contenu vérifié égal) ; `ricos.min.json` reste la forme canonique attendue par le lint.

## ⚠️ À vérifier dans Wix Studio avant publication — le slug
L'API a bien enregistré `seoSlug` = `soumission-chimique-victime-preuve-recours`, mais l'URL de prévisualisation rendue par le `GET` est dérivée du **titre** : `/post/soumission-chimique-ce-que-la-loi-permet-quand-la-victime-ne-se-souvient-de-rien`. **Ouvrir le panneau SEO du brouillon et confirmer que l'URL publiée sera bien le slug court** avant de publier.

## JSON-LD FAQPage
Bloc `application/ld+json` (**10 questions**) livré **dans le chat** (règle mémoire : jamais de fichier HTML intermédiaire). À coller dans le champ « Marquage structuré » du panneau SEO Wix Studio. Source des Q/R : section « Questions fréquentes » de l'article.

## Refresh (LEARN-046)
- **Prochain refresh : février 2027** (M+6 après la rédaction d'août 2026).
- **Déclencheurs à surveiller en priorité** :
  - **Périmètre de l'expérimentation** — l'arrêté du 11 décembre 2025 ne vise que Hauts-de-France, Île-de-France et Pays de la Loire. Une **extension à la Guadeloupe est annoncée mais non inscrite**, et une généralisation est possible après le rapport d'évaluation. **Si la Nouvelle-Aquitaine entre dans le dispositif, le H2 « À Bordeaux, la mesure de 2026 ne s'applique pas » devient faux et doit être réécrit en priorité.**
  - **Chiffres ANSM** — l'article cite l'enquête **2024** (publiée le 10 juillet 2026). Passer au millésime 2025 dès publication.
  - **Recodification du code de procédure pénale au 1ᵉʳ janvier 2029** (ordonnance du 19 novembre 2025) : les articles 7, 8, 706-3 et 706-5 changeront de numérotation. Sans effet avant cette date, mais à anticiper.
  - **Article 222-22 du code pénal** — version applicable jusqu'au 2029-01-01 ; vérifier qu'aucune loi intermédiaire ne l'a modifiée.
  - **Première jurisprudence** rendue sur le fondement de la loi n° 2025-1057 du 6 novembre 2025 (définition du consentement) : à intégrer dès qu'elle existe.
