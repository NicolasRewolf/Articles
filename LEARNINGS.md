# LEARNINGS — Journal vivant du pipeline

> Capture chaude post-article. **N'accumule pas indéfiniment** : les learnings stabilisés sont **promus** vers `BRIEF.md` ou `ARTICLE_TEMPLATE.md`, et leur historique est conservé dans `LEARNINGS-archive.md`.
>
> **Cycle de digestion** : avant chaque nouvel article (à partir du #5), revue rapide de ce fichier. Tout ce qui est confirmé sur 2 articles distincts + opérationnel + non encore promu → on l'écrit dans BRIEF/TEMPLATE et on le déplace dans `LEARNINGS-archive.md`.
>
> **Dernière digestion : 2026-06-23** (post #11, assurance perte d'exploitation) — **10 learnings promus** vers BRIEF.md : LEARN-057 (slugs publiés), 059 (angle mort avocat), 060 (faisceau procédure), 061 (PDF détaillé), 062 (version en vigueur), 063 (gate vérif + lire le post), 064 (push Wix fiable), 065 (`md_to_ricos` rel+OL), 066 (sujet CRM), + 2 nouveaux #11 : **067** (affaire-preuve = fondement exact), **068** (chiffre public non sourcé = attribution). **LEARN-056 abandonné** (infirmé). LEARN-054 déjà promu (élagué). Fichier résorbé < 100 lignes. Détail + cartographie : [`LEARNINGS-archive.md`](LEARNINGS-archive.md). **Restent actifs : LEARN-055, LEARN-058.**
>
> Digestions antérieures : 2026-06-01 (post #6), 2026-05-13 (post #4), ingestion LEARN-053 (2026-05-16).

---

## Critère de promotion (rappel)

Un learning est **promu** quand il remplit **≥ 2 conditions sur 3** : (1) confirmé sur ≥ 2 articles distincts ; (2) opérationnel (règle/méthode) ; (3) inutile à relire s'il vit déjà dans BRIEF/TEMPLATE. Sinon : reste ici.

**Destinations** : règle business/workflow/ton/outils → `BRIEF.md` · pattern structurel + checklist → `ARTICLE_TEMPLATE.md` · savoir technique/stratégique → `LEARNINGS-archive.md` · observation fraîche → ci-dessous.

---

## LEARNINGS actifs (en attente de confirmation ou de digestion)

### LEARN-055 — Matrice de collision ONISR (page 15 bilan annuel) = chiffre or pour articles cluster route

**Constat #6** : la matrice « tués selon mode de déplacement et antagoniste » (p. 15 du bilan ONISR) révèle que **54 % des occupants de voiture meurent dans des accidents sans tiers** — chiffre pivot incarnant l'asymétrie art. 3/art. 4 Badinter.

**Statut** : ⚠️ **à nuancer** — utile quand l'angle porte sur la **mortalité** (cluster route), peu applicable sur les sujets « grand blessé survivant » (#7) ou hors cluster route (#8 assurance, #11 perte d'exploitation : n/a). Reste actif ; affiner la formulation (« utile quand l'angle = mortalité routière ») avant promotion.

### LEARN-058 — Sujet de niche à volume quasi nul = actif d'autorité ; repérer le pilier-volume adjacent

**Constat #7** : « indemnisation tétraplégie » ≈ 10/mois (quasi nul), mais « nomenclature dintilhac » = 3 600/mois juste à côté. Décision : garder le sujet de niche comme **pilier d'autorité** (assumer le faible trafic) ET **noter le head term à volume adjacent** comme candidat pilier dédié futur.

**Statut** : la moitié « actif d'autorité premium » est **confortée par #11** (perte d'exploitation = gros enjeu B2B, head term modeste) — désormais couverte par **LEARN-066** (promu). La spécificité de 058 = **repérer le pilier-volume adjacent distinct du sujet** ; ce pattern précis reste à 1 occurrence (#7). Garder actif jusqu'à 2ᵉ confirmation, puis fusionner avec LEARN-066 ou promouvoir.

---

## Procédure de digestion (à reproduire avant chaque nouvel article à partir de #5)

1. **Relire** la section *« LEARNINGS actifs »* ci-dessus.
2. **Pour chaque entrée**, appliquer le critère de promotion (≥ 2/3).
3. **Si confirmé** : écrire la règle dans le fichier cible (BRIEF/TEMPLATE/archive), puis déplacer l'entrée dans `LEARNINGS-archive.md` avec date + destination.
4. **Si non confirmé** : laisser ici avec un horodatage de revue.
5. **Si abandonné** : déplacer dans la section *« Abandonné »* de l'archive avec la raison.

**But final** : `LEARNINGS.md` doit toujours faire **moins de 100 lignes**. S'il dépasse → c'est qu'on n'a pas digéré.
