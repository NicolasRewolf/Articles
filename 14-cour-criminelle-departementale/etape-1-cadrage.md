# Étape 1 — Cadrage

**Article #14 — Cour criminelle départementale : ce que la loi du 23 juillet 2026 change pour les victimes de viol**
*Titre de travail — H1 final fixé en Étape 3*
**Date de cadrage : 2026-08-14**
**Origine du sujet :** proposition de Nicolas, sourcée par un post LinkedIn du cabinet CLOT AVOCATS signalant la loi nouvelle.
**Statut : 🟡 EN ATTENTE VALIDATION NICOLAS**

---

## ✅ Arbitrages déjà tranchés (Nicolas, 2026-08-14)

1. **Persona et page de conversion primaire** : `/indemnisation-des-victimes/victimes-de-delits-ou-crimes`. **Arbitrage explicite exigé par BRIEF §4 Étape 1** — le sujet peut servir deux personas opposés (partie civile / personne mise en cause), il ne servira que **la partie civile**. Modulation : voix victime, empathie haute.
2. **2ᵉ catégorie Wix** : *Victimes de délits ou crimes* (`a755253f-65a6-49cc-b89e-e10e83840a75`), en plus de *Ressources et notions juridiques*.
3. **Numérotation** : #14. Le #13 est réservé au WIP « faux conseiller bancaire », à renuméroter et finaliser.

---

## 1. Sujet précis

Guide destiné aux **victimes de viol** sur la juridiction qui jugera leur affaire et sur ce que la **loi n° 2026-651 du 23 juillet 2026 « sur la justice criminelle et le respect des victimes »** modifie concrètement pour elles.

Le cœur de l'article n'est pas la description de la cour criminelle départementale — c'est la question que se pose réellement une victime : **« qui va juger mon agresseur, devant qui vais-je témoigner, et est-ce que cette loi améliore ma place ou seulement les délais de l'institution ? »**

Angle assumé : une loi qui porte « le respect des victimes » dans son intitulé mérite d'être lue **au texte**, poste par poste, pour distinguer ce qu'elle apporte à la partie civile de ce qui relève de la gestion des flux judiciaires. Ni tract, ni communiqué : la lecture d'un praticien.

---

## 2. État du fact-check au cadrage

> ⚠️ **Rien de ce qui suit n'est acquis tant que le Bloc A n'est pas fait.** Le sujet repose sur un texte promulgué il y a trois semaines, postérieur à la base de connaissances du modèle : le risque d'hallucination est maximal et impose une vérification au texte, article par article.

**Vérifié sur source primaire (2026-08-14)**

- **La loi existe.** LOI n° 2026-651 du 23 juillet 2026 *sur la justice criminelle et le respect des victimes* — [JORF n° 0171 du 24 juillet 2026](https://www.legifrance.gouv.fr/jorf/jo/2026/07/24/0171), [JORFTEXT000054470584](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000054470584). *Le titre exact diffère de celui donné par le post LinkedIn (« relative à la justice criminelle et au respect des victimes ») : c'est la version Légifrance qui fait foi.*
- **Art. 181-1 CPP, version applicable du 2026-07-25 au 2029-01-01** (`LEGIARTI000054477961`, statut `ABROGE_DIFF` — abrogation programmée par la recodification du CPP). Récupéré via `legifrance.py code`, qui a retenu la version applicable **sur les dates** malgré l'étiquette (discipline de version, BRIEF §4 Bloc A). Le texte en vigueur vise « un crime puni de quinze ans ou de vingt ans de réclusion criminelle » **sans la condition d'exclusion de la récidive légale**, et prévoit qu'« il ne peut être procédé qu'à une seule prolongation de la détention provisoire ».

**À vérifier au Bloc A — par ordre de priorité**

1. 🔴 **Le texte antérieur de l'art. 181-1 comportait-il bien « commis hors état de récidive légale » ?** C'est le cœur de l'angle : sans cette comparaison de versions, l'affirmation « la CCD juge désormais les récidivistes » n'est pas sourcée. Le script signale 2 versions — les comparer.
2. 🔴 **Assesseurs citoyens dans la composition de la CCD** : mentionné par une recherche Légifrance, **non lu au texte**. Si confirmé, c'est un élément majeur pour une victime (la CCD était critiquée pour l'absence de jury populaire) et probablement le meilleur Information Gain de l'article.
3. 🔴 **Dates d'entrée en vigueur, disposition par disposition** : le post annonce le 23 octobre 2026 ; une recherche Légifrance évoque, pour l'article 1ᵉʳ, « le premier jour du sixième mois suivant la promulgation ». **Les deux ne peuvent pas être vrais simultanément.** Un article publié avant l'entrée en vigueur doit être écrit au futur, avec la date exacte.
4. **Les six autres modifications** annoncées par le post (art. 173-1, 385, 198, 803-11, 115 CPP) : à vérifier une par une, et à écarter de l'article si elles ne concernent que les droits de la défense — hors périmètre du persona retenu.
5. **Ce que la loi contient réellement « pour les victimes »**, au-delà de son titre. Si le volet victimes est mince, le dire — c'est précisément l'angle.
6. **Prescription du viol et imprescriptibilité** : articulation avec l'actualité législative sur l'inceste, où le cabinet est déjà engagé (cf. §7).

**Méthode** : `legifrance.py code` pour chaque article du CPP cité, `--fond LODA_DATE` pour la loi elle-même (LEARN-075). Judilibre au Bloc A, pas après coup — mais base probablement vide sur un texte de trois semaines : le constater en deux requêtes et passer (BRIEF §4 Bloc A).

---

## 3. Intent de recherche

**Informationnel à forte charge émotionnelle, avec une frange transactionnelle** (recherche d'avocat au moment où la date d'audience approche).

Deux moments de vie très différents se croisent sur ces requêtes :

- **La victime dont la plainte est en cours d'instruction** : elle apprend que son affaire ira « en cour criminelle départementale » et ne sait pas ce que c'est. Angoisse dominante : *devoir raconter devant des inconnus*.
- **La victime dont l'affaire est jugée bientôt** : elle cherche le déroulé concret, sa place, ses droits, l'indemnisation.

S'y ajoute une audience secondaire non ciblée mais réelle (proches, étudiants, journalistes) qui ne convertit pas mais consolide l'autorité.

---

## 4. Requête principale

`cour criminelle départementale`

## 5. Pilier-volume adjacent

*(Champ introduit par la digestion du 2026-08-14 — BRIEF §4 Étape 1. Premier usage.)*

**Mesuré le 2026-08-14** (`scripts/dataforseo.py volumes`, France, français) :

| Terme | Volume | Concurrence |
|---|---|---|
| `cour d'assises` | **9 900/mo** | LOW (index 0) |
| `cour criminelle départementale` | **1 600/mo** | LOW (index 0) |
| `jury populaire` | 260/mo | LOW (index 0) |
| `partie civile procès` | 40/mo | LOW (index 4) |
| `déroulement procès assises` | 20/mo | LOW (index 0) |
| `viol` · `agression sexuelle` · `inceste` et dérivés | **`n/d`** | donnée supprimée |

**Lecture.** Le head term n'est **pas** une niche : 1 600 recherches/mois à concurrence nulle, c'est une cible solide et peu disputée. Le pilier-volume adjacent est **`cour d'assises` (9 900/mo)**, six fois plus gros et tout aussi peu disputé → **candidat pilier au backlog**, à traiter séparément et non à absorber ici (le confondre diluerait les deux).

⚠️ **Aucun volume mesurable sur l'axe « viol ».** Google Ads supprime la donnée des termes sexuels bruts — ce n'est pas une absence de demande (cf. LEARN-076). La demande de cet axe se lit donc par proxies (`porter plainte pour agression sexuelle` : 110/mo) et par la SERP, jamais par le volume. **Conséquence de cadrage : le head term porte le trafic, l'axe victime porte la valeur.** L'article doit gagner « cour criminelle départementale » pour être trouvé, et servir la victime pour être utile.

## 6. Requêtes long-tail visées

1. `cour criminelle départementale c'est quoi`
2. `différence cour d'assises cour criminelle départementale`
3. `viol jugé en cour criminelle départementale`
4. `procès viol sans jury populaire`
5. `partie civile cour criminelle départementale`
6. `loi 23 juillet 2026 justice criminelle victimes`
7. `témoigner à un procès pour viol`
8. `délai procès viol après plainte`
9. `appel décision cour criminelle départementale`
10. `indemnisation victime viol procès`

---

## 7. Persona prospect

- **Profil** : femme, 20-45 ans dans la majorité des cas, victime de viol ayant déjà porté plainte, dont le dossier est à l'instruction ou proche du jugement. Souvent accompagnée d'une association, parfois déjà d'un avocat commis.
- **Contexte émotionnel** : **appréhension de l'audience**, pas urgence. Ce n'est pas la sidération du dépôt de plainte (déjà passé) : c'est l'attente, longue, et la peur de la confrontation. Le ton doit refuser le sensationnel absolument.
- **Niveau juridique** : néophyte informé — elle a entendu des mots (« assises », « instruction », « partie civile ») sans en tenir le sens.
- **Ce qu'elle ne demandera jamais explicitement mais cherche** : est-ce que je vais devoir tout raconter en public, et devant qui.

---

## 8. Pages d'expertise cibles

- **Principale (conversion)** : `/indemnisation-des-victimes/victimes-de-delits-ou-crimes`
- **Secondaire (maillage, pas conversion)** : `/defense-penale/proces-criminel` — pour la mécanique d'audience uniquement, sans bascule de persona
- **Contact** : `/honoraires-rendez-vous`

---

## 9. Anti-cannibalisation — inventaire de la catégorie Ressources

Inventaire réalisé au cadrage via Wix API (`categoryId 9477320f-…`) : **61 articles publiés**. *(Règle mémoire + BRIEF §4 Bloc C.)*

**Cannibalisation : aucune.** Rien sur la cour criminelle départementale, la cour d'assises, le déroulé d'un procès criminel ni le viol. Le terrain est vierge dans la catégorie.

**Maillage entrant/sortant identifié** (slugs publiés réels — **à tester en HTTP avant cross-link**, LEARN-057) :

| Article publié | Usage prévu |
|---|---|
| `mis-en-cause-temoin-assiste-prevenu-accuse-differences` | Section « qui est qui à l'audience » — statut d'accusé |
| `indemnisation-civi-2025-guide-complet-pour-les-victimes-d-infractions` | Section indemnisation — CIVI |
| `sarvi-ou-civi-indemnisation-victimes` | Section indemnisation — arbitrage SARVI/CIVI |
| `réforme-de-la-prescription-pénale-comprendre-les-délais-et-les-nouvelles-règles` | Section délais / prescription du viol |
| `dépôt-de-plainte-en-france-comment-porter-plainte-efficacement` | Amont du parcours (lecteur arrivé trop tôt) |
| `itt-pénale-définition-en-2025` | Évaluation du dommage |
| `qu-est-ce-qu-une-période-de-sureté` | Section peine prononcée |
| `contrôle-coercitif-reconnaître-agir` · `demander-une-ordonnance-de-protection-en-2025` | Contexte violences, si le viol est conjugal |

**Preuves cabinet (lien interne obligatoire dès citation — règle mémoire)** :

- `proposition-de-loi-inceste-et-imprescriptibilité-le-cabinet-plouton-au-cœur-des-avancées-législati` — engagement du cabinet dans le travail législatif sur les violences sexuelles.
- `plaidoirie-pour-chahinez` — plaidoirie du cabinet, violences faites aux femmes.

⚠️ Les deux sont à **relire au `CONTENT_TEXT`** avant toute affirmation sur leur contenu (LEARN-063).

---

## 10. Hypothèse de valeur

1. **Fraîcheur décisive.** Une loi promulguée le 23 juillet 2026 dont les décrets et l'entrée en vigueur sont encore devant nous : le corpus web sur le volet *victimes* est presque certainement inexistant à cette date. Fenêtre courte, avantage réel.
2. **Angle mort confirmé, et d'un type inédit** (top 10 relevé le 2026-08-14) : cours-appel.justice.fr, Service-Public, France Victimes, Institut Robert Badinter, Wikipédia, Légifrance, Vie-publique, univ-rouen, Dalloz. **Zéro cabinet d'avocats.** Ce n'est pas l'angle mort *total* de #12 — le sujet est bien traité en droit — mais il l'est exclusivement par l'**institutionnel et l'académique** : jamais par un praticien, jamais du point de vue de la personne concernée. Configuration non prévue par la typologie du BRIEF (cf. LEARN-077).
   **Les PAA confirment le déséquilibre** : « Quelle est la différence entre une cour d'assises et une cour criminelle départementale ? », « Qu'est-ce qu'une cour criminelle départementale ? », « Combien y a-t-il de cours criminelles départementales en France ? », « Quel est le tribunal le plus grave ? » — **intent purement définitionnel**. Personne ne sert la question « et moi, dans tout ça ? ».
   **Prise de Bloc A** : France Victimes ranke 3ᵉ avec le *rapport du comité d'évaluation et de suivi de la cour criminelle départementale* — source primaire à lire.
3. **Question réellement non servie** : « est-ce que ça change quelque chose pour moi ? ». Les contenus existants décrivent une juridiction ; ils ne répondent pas à une personne qui va témoigner.
4. **Autorité de cluster** : l'article devient la tête du parcours pénal-victime déjà couvert en aval (CIVI, SARVI, prescription, ITT) et qui n'avait pas de porte d'entrée « procès ».

---

## 11. Preuve d'originalité

*(Champ obligatoire — nommer un artefact, pas une intention.)*

**Artefact principal : la lecture au texte de la loi n° 2026-651, disposition par disposition, triée selon ce qu'elle change *pour la partie civile*.** Un tableau construit par nous — colonne « ce que dit le texte » / « ce que ça change pour vous » / « date d'entrée en vigueur » — avec le verbatim Légifrance et les bornes d'application obtenus par l'API. Personne ne peut le produire par reformulation d'un communiqué : il suppose de lire les articles du CPP dans leur version applicable.

**Artefact secondaire** : le **contraste titre/contenu** documenté. La loi s'intitule « et le respect des victimes ». Si l'inventaire poste par poste montre que le volet victimes est mince, ou au contraire substantiel, la démonstration chiffrée est originale dans les deux cas — et honnête dans les deux cas.

**Ancrage propriétaire** : l'engagement du cabinet sur l'imprescriptibilité de l'inceste (post publié) donne une légitimité vérifiable à commenter une loi sur les violences sexuelles — ce n'est pas un avis d'opportunité, c'est une position déjà tenue.

⚠️ **Garde-fou** : si le Bloc A révèle que la loi ne contient rien de substantiel pour les victimes **et** que le Bloc B montre un SERP déjà servi, l'artefact tombe et le sujet doit pivoter (vers `cour d'assises` ou `procès pour viol : votre place`). Décision en fin d'Étape 2.

---

## 12. Risques identifiés

| Risque | Traitement |
|---|---|
| **Sujet YMYL maximal** (violences sexuelles + institution judiciaire) | Standard qualité BRIEF §6 sans exception. Zéro sensationnalisme, zéro pathos, aucune promesse de résultat |
| **Texte très récent, hors base de connaissances** | Aucune affirmation sans verbatim Légifrance. Toute zone grise → `⚠️ À vérifier` maintenu jusqu'à la source |
| **Dates d'entrée en vigueur contradictoires** | Bloquant : à trancher au texte avant rédaction. Un article au mauvais temps grammatical est faux |
| **Bascule involontaire de persona** | La mécanique d'audience se raconte du point de vue de la partie civile. Aucune section « stratégie de défense » |
| **Intent du head term ≠ intent de l'article** — les PAA sont définitionnelles, la valeur est victime | Servir les deux : ouverture définitionnelle courte (gagne le head term), profondeur victime ensuite. Ne pas sacrifier l'une à l'autre |
| **Volume de l'axe « viol » non mesurable** (suppression Google Ads) | Traité : proxies + SERP. Ne jamais conclure d'un `n/d` à une absence de demande (LEARN-076) |
| **Récupération polémique** | La source d'origine (post LinkedIn) est militante côté défense. Elle sert de piste, jamais de source. Le texte tranche |

---

## 13. Prochaine étape

🛑 **STOP — validation requise.** À valider : le persona et l'angle, la numérotation #14, et la priorité du fact-check (§2).

Sur « OK go » → **Étape 2**. Le Bloc B est **déjà largement fait** (volumes, SERP top 10, PAA — relevés au cadrage une fois l'outillage DataForSEO réparé) : il restera à élargir le faisceau aux termes de procédure (BRIEF §4 Bloc B) et à relever les *related searches*. L'effort porte donc sur le **Bloc A**, où se joue tout l'article : lecture au texte de la loi n° 2026-651 et de chaque article du CPP modifié.
