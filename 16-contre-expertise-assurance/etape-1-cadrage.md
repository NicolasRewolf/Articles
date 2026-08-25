# Cadrage — Contre-expertise d'assurance : contester le rapport de l'expert

> Étape 1 du pipeline. Sujet et critère de sélection fournis par Nicolas le 2026-08-25 : **« choisi en fonction du volume de recherche le plus élevé »**. Toutes les mesures ci-dessous sont du 2026-08-25 (DataForSEO, Google FR, location 2250, langue fr). STOP + validation requise avant Étape 2.

---

## Sujet

**Contre-expertise d'assurance : contester le rapport de l'expert.**

**Périmètre tranché** (Nicolas a répondu « je sais pas » ; arbitrage pris ici, à confirmer au STOP) : l'article est transversal **sur le mécanisme**, pas sur le type de sinistre. Dominante **assurance de biens** (habitation, auto, professionnel) + un pan **corporel** (expertise médicale). Ce n'est pas un compromis éditorial, c'est ce que la SERP fait déjà : `association-aide-victimes-france.fr — « Comment contester une expertise médicale ? »` sort en **position 6 sur `contre expertise assurance`** et en **position 1 sur `expertise contradictoire`**, et la PAA de `expert d'assuré` contient « Comment éviter les pièges lors d'une expertise médicale ? ». Google traite ce champ lexical comme un seul ; le découper nous ferait perdre du terrain sans rien protéger.

---

## Intention de recherche

- **Type** : mixte — informationnelle dominante, avec une strate commerciale réelle et chère.
- **Justification** : les CPC du champ sont hauts et homogènes (3,59 € à 5,34 € sur les termes de contestation ; jusqu'à **7,72 €** sur `contre expertise dégât des eaux`), ce qui signale un intent prestataire solvable. Mais les acheteurs de ce clic sont les **experts d'assuré**, pas les avocats — la SERP le confirme (voir Hypothèse de valeur). L'intent que nous servons est celui d'aval : « le rapport est tombé, il me sous-indemnise, qu'est-ce que je peux lui opposer ».

---

## Qualification des requêtes candidates

Mesures du 2026-08-25. État du chercheur lu sur la SERP et les PAA réelles (3 SERP relevées : `expert d'assuré`, `contre expertise assurance`, `expertise contradictoire`).

| Requête candidate | Volume | CPC | État du chercheur | Commentaire |
|---|---|---|---|---|
| `expert d'assuré` | **1 300/mo** | 4,19 € | **cherche une définition** (+ métier) | **Le maximum du champ, et un piège.** 4 des 20 organiques sont des **fiches métier** (Onisep, Apec, ISC Paris, je-change-de-metier) : une part du volume veut *devenir* expert. Le reste cherche à *recruter* un expert — un service qui n'est pas le nôtre. PAA : « Quel est son rôle ? », « Quel est le tarif ? ». |
| `expert assurance` / `expertise assurance` | 1 000/mo | 3,90 € | cherche une définition | Encore plus générique. Même dérive métier. |
| `expertise médicale` | 720/mo | 1,33 € | s'informe | CPC bas = intent peu solvable. Adjacent à notre pan corporel, pas une porte. |
| `expertise contradictoire` | 590/mo | 4,07 € | **s'informe** (lexique) | Top 20 tenu par des **lexiques d'assureurs** (Allianz, AXA, Direct Assurance) et des définitions (litige.fr, Capital). PAA définitionnelles : « Qui paie ? », « Qu'est-ce que la convocation ? ». Bon adjuvant, mauvaise porte. |
| **`contre-expertise` / `contre expertise assurance`** | **480 + 320/mo** | 4,61 € / 3,59 € | **problème en cours** | **La porte.** PAA : « **Que faire si je ne suis pas d'accord avec l'expertise de mon assurance ?** », « Quel est le coût d'une contre-expertise ? ». Presse conso saisie du grief (Le Monde, Que Choisir) = signal de litige vécu, pas de curiosité. |
| `contre expertise assurance habitation` | 90/mo | **5,34 €** | problème en cours | MEDIUM 57 — le seul endroit du champ où la concurrence paie vraiment. Sinistré bloqué. |
| `contre expertise médicale` | 210/mo | 1,96 € | problème en cours | Notre pan corporel. Rapport en main, séquelles sous-évaluées. |
| `contre expertise dégât des eaux` | 50/mo | **7,72 €** | problème en cours | HIGH 67. CPC le plus élevé du champ : le litige est mûr. |
| `demander une contre-expertise` | 50/mo | 2,35 € | problème en cours | Le chercheur sait déjà ce qu'il veut faire. |
| `convocation expertise assurance` | 20/mo | n/d | problème en cours | Amont immédiat : la convocation est reçue, l'expertise n'a pas eu lieu. |
| `pas d'accord avec l'expert de l'assurance` | 10/mo | n/d | problème en cours | Formulation brute du grief. Volume résiduel car agrégé dans les têtes. |

**Verdict** : `GO`

**Arbitrage sur le head term — à valider explicitement.** Le critère donné est le volume, et le volume maximal du champ est `expert d'assuré` (1 300/mo). La SERP dit que ce volume est composite : fiches métier + recherche d'un prestataire concurrent. Le retenir en H1 reproduirait exactement le schéma de **#02** (`chirurgie esthétique ratée`, 1 600/mo → 762 impressions, 1 clic, 1 contact en trois mois) et de **#07** (entré par `indemnisation tétraplégie`, ressorti sur `tétraplégique c'est quoi`).

L'arbitrage retenu applique le critère volume sans reproduire l'erreur : **`contre-expertise assurance` en requête principale** (cluster contre-expertise ≈ 800/mo, état « problème en cours », et c'est littéralement le sujet formulé par Nicolas), et **`expert d'assuré` capté par un H2 porteur dédié** dans le corps — « Faut-il prendre un expert d'assuré ? ce qu'il fait, ce qu'il coûte, ce qu'il ne peut pas faire ». On va chercher les 1 300/mo, on ne les met simplement pas dans le titre.

> Si Nicolas préfère le head term brut, l'alternative est écrite : H1 sur `expert d'assuré`, article recentré sur le choix d'un expert privé. Coût assumé : on écrit une page de comparaison de prestataires que nous ne sommes pas, et l'objectif contact tombe. Décision au STOP.

**Persona visé, et mot qui écarte l'autre** — le champ est réversible sur trois axes, c'est le sujet le plus polysémique du pipeline à ce jour :

- visé = **l'assuré sinistré en désaccord avec le rapport** ;
- écartés = (a) le **candidat au métier** d'expert en assurances, (b) le **professionnel** qui cherche un confrère expert, (c) le simple curieux d'une définition ;
- le H1 le dit par « **contester** » + un possessif d'assuré (« **votre** assureur », « **votre** indemnisation »). Un H1 en « L'expert d'assuré : rôle et missions » attirerait exactement les trois personas écartés. Cette contrainte devient impérative à l'Étape 3.

---

## Requête principale

`contre-expertise assurance` — **cluster ≈ 800/mo** (`contre-expertise` 480 + `contre expertise assurance` 320), état **problème en cours**, CPC 3,59–4,61 €.

---

## Pilier-volume adjacent

`expert d'assuré` — **1 300/mo, LOW (index 25), CPC 4,19 €**. Traité **dans** cet article par un H2 porteur, pas en H1 (voir arbitrage). Inscrit au backlog comme candidat à un article dédié **si** la mesure M+3 montre que le H2 capte sans convertir : le sujet « choisir et payer un expert d'assuré » est un article de comparaison de prestataires, pas un article de cabinet.

Second candidat backlog : `expertise contradictoire` (590/mo, CPC 4,07 €) — actuellement tenu par les lexiques d'assureurs, donc facile à prendre, mais définitionnel.

---

## Requêtes long-tail (issues des PAA relevées, 3 SERP)

1. `que faire si je ne suis pas d'accord avec l'expertise de mon assurance`
2. `qui paie la contre-expertise` / `quel est le coût d'une contre-expertise`
3. `qui doit payer l'expert d'assureur`
4. `quel est le tarif d'un expert d'assuré`
5. `est-il nécessaire de prendre un expert d'assuré`
6. `qu'est-ce que la convocation à une expertise contradictoire`
7. `quel est le délai de réponse d'un expert en assurance`
8. `pourquoi mon assurance mandate un expert`
9. `comment contester une expertise médicale`
10. `comment éviter les pièges lors d'une expertise médicale`

---

## Persona prospect

- **Profil** : assuré (particulier propriétaire/locataire, ou dirigeant de TPE) qui a subi un sinistre, a reçu la visite de l'expert mandaté par son assureur, et tient un rapport ou une proposition d'indemnisation qu'il juge très en dessous de sa perte réelle. Il découvre à ce moment-là que l'expert qui l'a reçu chez lui est payé par la partie adverse.
- **Contexte émotionnel** : **sentiment d'injustice procédurale** plus que détresse. Il ne conteste pas seulement un montant, il conteste d'avoir été jugé par quelqu'un qui n'était pas neutre. Se sent piégé par un vocabulaire qu'il n'a pas choisi (contradictoire, tierce expertise, vétusté, valeur d'usage).
- **Niveau juridique** : néophyte. Confond expertise amiable et expertise judiciaire ; croit que le rapport de l'expert « fait foi » ; ignore qu'il peut refuser de signer, et ignore surtout ce que son propre contrat prévoit déjà en matière de frais de contre-expertise.
- **Persona écarté** : le candidat au métier d'expert en assurances (4 fiches métier au top 20 de `expert d'assuré`) et le professionnel de l'expertise. Aucun contenu ne leur est destiné.

---

## Page(s) d'expertise cible(s)

- **Principale (CTA)** : `/droit-des-contrats-et-des-personnes/droit-assurances-particuliers-professionnels`
- **Secondaires** : `/indemnisation-des-victimes/accidents-de-la-route` (pan corporel / expertise médicale après accident)
- **Contact** : `/honoraires-rendez-vous` (CTA final)

---

## Hypothèse de valeur

1. **Zéro avocat sur les trois requêtes têtes.** Top 20 de `expert d'assuré`, top 19 de `contre expertise assurance`, top 19 de `expertise contradictoire` : aucun cabinet côté assuré. Ce qui tient la SERP, ce sont **les experts d'assuré eux-mêmes** (Galtier, mon-contre-expert, expertise-sinistre, expert-d-assure, CFEIB, COTRANEX), **les assureurs** (Luko, Groupama, Allianz, AXA, Matmut, Macif, Abeille, Cardif, Direct Assurance), la **presse conso** (Le Monde, Que Choisir, Capital) et les **comparateurs** (lesfurets, mes-allocs, hyperassur, Ornikar). Configuration **LEARN-077** : le sujet *est* traité, mais jamais par un praticien du contentieux, et jamais du point de vue de ce qu'on peut **opposer juridiquement**.
2. **Les deux camps qui tiennent la SERP ont un intérêt à ne pas répondre à la question.** L'assureur ne dira pas que son expert n'est pas neutre. L'expert d'assuré ne dira pas dans quels cas sa prestation ne changera rien — il la vend. La question « le rapport a-t-il une valeur devant le juge ? » n'a donc de réponse honnête que chez un tiers, et ce tiers est un avocat.
3. **Le CPC finance la démonstration** : 4,19 € à 7,72 € sur ce champ, payés par des experts privés. Un contenu organique qui répond mieux qu'eux capte un trafic qu'ils achètent cher.
4. **Maillage prêt et cluster déjà dense** — le site porte 62 notions dont un pan assurance complet (sinistre habitation, perte d'exploitation, sinistre auto) et tout le cluster dommage corporel (Badinter, pretium doloris, dossier médical, ITT).

---

## Preuve d'originalité

**Artefact** : le **tableau des quatre statuts d'expertise**, avec pour chacun sa **valeur probatoire réelle** — le point que ni l'assureur ni l'expert privé ne publie.

| Statut | Qui la déclenche | Qui la paie | Ce qu'elle vaut devant le juge |
|---|---|---|---|
| Expertise unilatérale de l'assureur | l'assureur | l'assureur | ⚠️ à établir en Étape 2 |
| Expertise amiable contradictoire | l'assuré (son expert face à celui de l'assureur) | ⚠️ selon contrat | ⚠️ à établir |
| Tierce expertise (clause d'arbitrage du contrat) | les deux experts en désaccord | ⚠️ souvent partagée | ⚠️ à établir |
| Expertise judiciaire (référé, art. 145 CPC) | le juge | l'avancée par le demandeur | ⚠️ à établir |

Chaque case marquée est un point de **fact-check obligatoire en Étape 2 Bloc A** (Code des assurances, Code de procédure civile, jurisprudence Cass. civ. 2e / 3e sur la valeur de l'expertise amiable non contradictoire). Aucune ligne ne sera écrite sans source — la thèse même de l'article repose sur ce tableau, donc une approximation ici ruinerait la pièce.

**Second artefact candidat** : la **clause « frais de contre-expertise »** que beaucoup de contrats MRH prévoient déjà (souvent plafonnée à un pourcentage du montant du sinistre) et que l'assuré ignore posséder. Vérification contractuelle à mener en Étape 2 — si elle se confirme, c'est l'information la plus actionnable de l'article, et personne ne la met en avant.

**Renfort interne** : affaires cabinet en droit des assurances à identifier au Bloc C (lien interne obligatoire si citée).

---

## Bloc C anticipé — inventaire catégorie Ressources (fait au cadrage, 2026-08-25)

**62 notions publiées** (query `categoryId 9477320f-…`, endpoint `GET /blog/v3/posts`).

**Cannibalisation identifiée — un cas, à arbitrer.** [`sinistre-habitation-recours-assurance`](https://www.jplouton-avocat.fr/post/sinistre-habitation-recours-assurance) (article #8, publié 2026-07) porte déjà un **H3 « Contester l'expertise »**, une **FAQ « Qui paie la contre-expertise ? »** et le **tag `contre-expertise`**. Son cadrage revendiquait explicitement `contre expertise assurance` et `contester expertise assurance` en head terms secondaires.

**Arbitrage proposé — architecture pilier / satellite** :
- **#8 reste le pilier du grief** : « mon assureur refuse / traîne / sous-indemnise », entrées par type de sinistre (dégât des eaux, incendie, CatNat, fissures), garanties, prescription biennale.
- **#16 devient le satellite du mécanisme** : « le rapport d'expertise », entrées par les termes d'expertise. Il ne doit **jamais** se titrer sur « sinistre habitation » ni sur « assureur refuse ».
- **Action à valider** : réduire le H3 « Contester l'expertise » de #8 à un paragraphe court + lien vers #16. Cela suppose d'éditer un article publié — **décision Nicolas**, pas la mienne.
- **Réserve honnête** : #8 a un mois et sa **mesure M+3 n'est pas échue** (~2026-10). On découpe donc son territoire avant de savoir ce qu'il capte. Si le M+3 montre que #8 rankait précisément sur les termes d'expertise, l'arbitrage devra être rejoué.

**Shortlist de maillage** (slugs publiés réels — liens à tester en HTTP avant usage) :

| Slug | Rôle dans l'article |
|---|---|
| `sinistre-habitation-recours-assurance` | pilier amont — le grief global |
| `assurance-perte-exploitation-refus-calcul-recours` | volet professionnel du chiffrage contesté |
| `sinistre-automobile-mon-assurance-de-véhicule-me-réclame-la-preuve-achat` | volet auto — preuve opposée par l'assureur |
| `comment-bien-préparer-mon-dossier-médical` | **amont direct du pan corporel** — « J'ai RDV pour une expertise médicale » |
| `le-pretium-doloris-guide-complet-pour-les-victimes-d-accidents` | poste de préjudice sous-évalué en expertise médicale |
| `loi-badinter-85-comprendre-vos-droits-à-indemnisation-après-un-accident-de-la-route` | cadre de l'offre de l'assureur, pan corporel |
| `traumatisme-cranien-accident-voiture` | cas d'école de séquelles minorées par l'expert |
| `responsabilité-du-fait-des-choses-quels-recours-en-cas-de-chute-d-objet-tombé-ou-d-équipement-déf` | fondement de responsabilité voisin |

**Catégories Wix de publication (2)** : Ressources et notions juridiques `9477320f-…` + Droit des assurances `edd6c343-05a3-4bf9-929e-527fad068557`.

---

## Note de méthode — deux observations pour LEARNINGS

1. **Les accents changent le volume.** `expert d'assuré` rend **1 300/mo**, `expert d assure` (sans accent) **320/mo** : Google Ads les traite comme deux mots-clés distincts. Toute mesure de champ doit être faite en graphie accentuée, sinon on sous-estime d'un facteur 4. À mécaniser dans `dataforseo.py` (avertissement si un mot-clé accentuable est passé sans accent).
2. **Cinquième configuration d'angle mort (extension LEARN-077)** : SERP tenue par **les prestataires du service concurrent**. Ce n'est ni l'institutionnel (#14, #15) ni le sanitaire (#12) : ici ce sont des entreprises privées qui vendent la prestation adjacente et qui ont un intérêt commercial à ne pas répondre à la question de fond. Le degré se lit à *qui a intérêt au silence*.

---
*Livrable Étape 1 — 2026-08-25. STOP : validation Nicolas requise avant Étape 2 (collecte).*
*Mesure M+3 : à programmer trois mois après la première impression GSC.*
