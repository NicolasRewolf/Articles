# Métadonnées Wix — Article #10 Changer d'avocat en cours de procédure

> À renseigner / vérifier dans le panneau SEO de Wix Studio. Article : `etape-4-article.md`.
> Brouillon poussé via l'API Wix Blog (Draft Posts) — voir section « Push Wix » en bas.

## SEO

- **Titre SEO** (≤ 60) : `Changer d'avocat en cours de procédure : vos droits`
- **Méta-description** (≤ 155) : `Changer d'avocat en pleine procédure : c'est votre droit. Dossier, honoraires, aide juridictionnelle — vos recours, par un avocat à Bordeaux.`
- **Slug** (sans accent — LEARN-001) : `changer-d-avocat-en-cours-de-procedure`
- **Excerpt / résumé du post** : `Pouvez-vous changer d'avocat en pleine procédure ? Oui : le mandat est librement révocable. Dessaisissement, récupération du dossier, honoraires dus, aide juridictionnelle et commis d'office — vos droits, avec une lettre type.`

## Catégories Wix (2 — LEARN-041 / reco BRIEF)

- **Ressources et notions juridiques** — `9477320f-5902-40e9-ace3-b0e3b6b8b51f`
- **Droit Pénal** — `8dad2d49-d0e2-40c3-be1c-02baaf57e3cd`

*Article transversal (famille, pénal, victimes, travail). Catégorie thématique = Droit Pénal (flagship cabinet + angle commis d'office unique au pénal). Alternatives possibles si tu préfères : Droit de la famille (`5151e5b0-…`) ou Défense des consommateurs.*

## Tags

changer d'avocat, changer d'avocat en cours de procédure, dessaisissement avocat, changer d'avocat aide juridictionnelle, avocat commis d'office, honoraires avocat, révoquer son avocat, transmission dossier avocat, RIN article 9, contestation honoraires bâtonnier, lettre de dessaisissement, droit pénal, Bordeaux

## Image hero (suggestions — sources libres + alt)

- **Option A (reco)** : photo sobre — une chemise/dossier cartonné qui passe d'une main à une autre, ou une personne à un bureau relisant des documents avec calme. Sources : Unsplash / Pexels (« file folder handover », « person reviewing documents desk »).
  **Alt** : `Transmission d'un dossier entre avocats — changer d'avocat en cours de procédure`
- **Option B** : enveloppe / lettre recommandée posée sur un bureau (évoque la lettre de dessaisissement).
  **Alt** : `Lettre de dessaisissement pour changer d'avocat`

*(Éviter les visuels « conflit » trop chargés — ton sobre, voix main tendue.)*

## Carte des liens (convention rel — LEARN-024)

**Liens internes → `follow` (pas de `rel`, pas de `target="_blank"`)** — URLs absolues `jplouton-avocat.fr` :
- `/honoraires-rendez-vous` (mini-CTA #1 intro, mini-CTA #2 honoraires, CTA final)
- `/defense-penale/droit-penal` (H2.4, commis d'office)
- `/indemnisation-des-victimes/victimes-de-delits-ou-crimes` (CTA final)
- `/post/ma-procédure-judiciaire-n-avance-pas-puis-je-obtenir-une-indemnisation-pour-ce-délai-déraisonnable` (H2.5, délais — slug publié réel, accents URL-encodés dans l'article)

**Liens externes → `target="_blank" rel="noopener noreferrer nofollow"`** :
- `legifrance.gouv.fr/codes/article_lc/LEGIARTI000006445302` (intro + H2.1 — Code civil art. 2004, mandat révocable)
- `legifrance.gouv.fr/jorf/article_jo/JORFARTI000001309281` (H2.2 + H2.3 — RIN art. 9, succession d'avocat)
- `legifrance.gouv.fr/codes/section_lc/JORFTEXT000000356568/LEGISCTA000006145642/` (H2.3 — art. 174-179 décret 27 nov. 1991, contestation honoraires)
- `service-public.gouv.fr/particuliers/vosdroits/F36104` (H2.4 — avocat commis d'office)

*Convention rel appliquée automatiquement dans le Ricos poussé (post-traitement du JSON : internes = `target=SELF` sans rel ; externes = `target=BLANK` + `rel nofollow noopener noreferrer`).*

## JSON-LD FAQPage

→ livré dans le chat (bloc `<script type="application/ld+json">` minifié, FAQPage seul — 10 questions). À coller dans le champ « Marquage structuré » du panneau SEO Wix Studio du draft post.

## Push Wix

- **Méthode** : `POST /blog/v3/draft-posts` (Draft Posts API), `siteId = 0870235c-b92d-4a69-a2f4-25a976ae5f0c`, `memberId = 07454f1f-c54a-4308-b897-19be554db88a` (compte Me Plouton). Statut **brouillon** (non publié) — publication manuelle par Nicolas après relecture.
- `draftPostId` : `c2ba1848-a567-4d86-92b1-bc43454a48bb` (créé le 2026-06-18, statut `UNPUBLISHED`). Vérifié : 54 nœuds Ricos, 10 FAQ, 11 titres, 2 catégories persistés.
- Contenu = Ricos généré via `scripts/md_to_ricos.py` + post-traitement liens rel.

## Refresh

Prochain refresh **M+6 ≈ décembre 2026** (LEARN-046) : vérifier version en vigueur du RIN (consolidations CNB), montants/condition AJ (réformes aide juridictionnelle), et toute évolution jurisprudentielle sur la taxation des honoraires de l'avocat dessaisi.
