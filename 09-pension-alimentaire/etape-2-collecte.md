# Collecte — Pension alimentaire (#09)

> Étape 2 du pipeline (collecte & analyse). Socle : DataForSEO (SERP + volumes, 16/06/2026) · 678 messages du formulaire de contact (mars 2025 → 15 juin 2026) · mapping Wix (13 posts famille publiés) · WebSearch ciblée Légifrance / service-public / sécurité sociale. **Notes brutes sourcées — pas de rédaction.** STOP + validation avant Étape 3.
>
> Ordre LEARN-018 : Bloc B en premier. Jurisprudence Judilibre + extraction PDF CNAF au précis = programmées Étape 4.

---

## BLOC B — SEO (demande, SERP, gap)

### Volumes (Google FR, DataForSEO, juin 2026)

**Cœur « calcul/montant » — fort volume, COMMODITY, gov-owned (à couvrir court, pas cibler) :**
| Requête | Vol/mo | KD |
|---|---|---|
| pension alimentaire | 40 500 | 49 |
| pension alimentaire caf | 27 100 | 7 |
| **aripa** | **74 000 (+82 %/an)** | 7 |
| calcul pension alimentaire | 9 900 | 24 |
| simulateur pension alimentaire | 9 900 | 10 |
| barème pension alimentaire | 5 400 | 3 |
| pension alimentaire garde alternée | 3 600 | — |
| tableau pension alimentaire | 3 600 | 17 |
| montant pension alimentaire | 2 900 | 9 |
| pension alimentaire impôt | 2 400 (pic +238 %) | 17 |
| pension alimentaire jusqu'à quel âge | 1 300 | 8 |

**Faisceau « recours / impayé / pénal » — volume moyen, CONCURRENCE QUASI NULLE, angle mort avocat (LA cible) :**
| Requête | Vol/mo | KD |
|---|---|---|
| nouvelle loi pension alimentaire non payée | 1 600 | **2** |
| non paiement pension alimentaire | 880 | 7 |
| pension alimentaire non payée | 880 | — |
| minimum pension alimentaire | 720 | 9 |
| révision pension alimentaire | 320 | 7 |
| saisie sur salaire pension alimentaire | 210 | 2 |
| recouvrement / plainte abandon de famille | 170 / 170 | 4 / — |
| pension alimentaire impayée / arriéré | 110 / 110 | — |
| huissier / paiement direct / titre exécutoire | 110 / 90 / 90 | 3 / 8 / — |
| délit d'abandon de famille | 70 | — |
| comment ne plus payer / suppression / arriérés | 70 / 50 / 50 | — |

**Adjacents à capter en sections :** prestation compensatoire 5 400 (KD 27) · médiation familiale 4 400 · allocation de soutien familial 3 600 · devoir de secours 590.
**Non chiffré DataForSEO :** `abandon de famille` (dédoublonné — fort en PAA/backlinks, à traiter comme tête de section pénale).

### SERP — qui rank

- **`pension alimentaire`** : 100 % institutionnel (Service-Public F991, CAF/ARIPA, Justice.fr + **simulateur officiel**, impots.gouv) + Wikipédia (knowledge graph). Verrou total.
- **`pension alimentaire non payée`** : Service-Public F1249 + CAF/ARIPA + **commissaires de justice** (huissiers, « 300 000 familles ») + **annuaires/agrégateurs d'avocats** (trouvervotreavocat, justifit, monexpertdudroit) + vidéos (YouTube, TikTok `@maitrebem`). **Zéro cabinet réel** prenant le parti du créancier en profondeur (LEARN-059 confirmé). Pénal au cœur (« plainte abandon de famille », « 2 ans / 15 000 € »).

### PAA / questions réelles (à couvrir en corps + FAQ — query fan-out)

- « Comment faire quand le père ne paye pas la pension ? » → plainte abandon de famille (> 2 mois).
- « Comment récupérer une pension impayée ? » → ARIPA, recouvrement employeur/banque sans huissier préalable.
- « Quelle sanction pour non-paiement ? » → 2 ans / 15 000 €.
- « Quelle pension pour un salaire de 2 000 € ? » / « montant moyen par enfant ? » (≈ 170 €/mois/enfant cité) — calcul.
- « Quelle est la nouvelle loi sur les pensions non payées ? » → **curiosité réforme à démystifier**.
- Related : ARIPA · non payée 1 mois/2 mois · modèle de lettre · non payée depuis 10 ans · enfant majeur.

### Gap analysis (Information Gain — LEARN-039)

Top 10 = commodity institutionnel + huissiers + annuaires. **Aucune perspective avocat-pénaliste côté parent.** Éléments distinctifs disponibles, absents du SERP :
1. **L'ARIPA à double tranchant** (aide créancier / piège débiteur depuis l'automaticité 2023) — tiré des 678 verbatims.
2. **Le levier pénal (227-3) expliqué par un pénaliste** + le fait que 227-3 vise aussi le non-versement à l'ARIPA.
3. **Démystification de la « nouvelle loi »** (vraie réforme ARIPA 2023 + plafonds fiscaux LF 2026 vs rumeur « défiscalisation 4 000 € »).
4. **Chaîne complète sourcée** amiable → mise en demeure → ARIPA/ASF → paiement direct → saisie → pénal, avec seuils (2 mois, 5 ans, ASF 200,78 €) — agrégation substitutive (LEARN-048).

---

## BLOC A — Juridique (fondation, sourcé Légifrance / service-public)

### Pénal — l'ancre du pivot
- **Art. 227-3 C. pén.** (abandon de famille) : défaut de paiement, **> 2 mois**, d'une pension fixée par décision de justice → **2 ans d'emprisonnement + 15 000 €**. Le texte vise **aussi** le non-versement à l'**organisme d'intermédiation (ARIPA) > 2 mois** (mêmes peines). Version en vigueur **LEGIARTI000044629406** → [Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044629406). Section [abandon de famille 227-3 à 227-4-1](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006165318).
- ⚠️ Cibles Judilibre (Étape 4) : élément intentionnel (mauvaise foi) ; **l'impossibilité réelle de payer = cause d'exonération** ; point de départ du délai.

### Civil — fixation, forme, révision, durée
- **Art. 371-2 C. civ.** : chaque parent contribue à l'entretien et l'éducation **à proportion de ses ressources, de celles de l'autre parent, et des besoins de l'enfant** ; obligation **ne cessant pas de plein droit à la majorité**. → [LEGIARTI000039778192](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039778192).
- **Art. 373-2-2 C. civ.** : en cas de séparation, la contribution prend la forme d'une **pension alimentaire** versée à l'autre parent (intègre les modalités IFPA). → [LEGIARTI000044629469](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044629469).
- **Art. 373-2-13 C. civ.** : décisions/conventions **modifiables à tout moment** par le juge → **fondement de la révision** (créancier ↑ comme débiteur ↓). → [Légifrance](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006426770).
- **Calcul** : table de référence indicative du ministère de la Justice (méthode : revenu du débiteur − minimum vital, × taux selon nb d'enfants et mode de garde) ; **renvoi au simulateur officiel** ([service-public](https://www.service-public.gouv.fr/simulateur/calcul/pension-alimentaire), [justice.fr](https://www.justice.fr/simulateurs/pension-alimentaire)) — **ne pas reproduire** (anti-commodity). Minimum vital ≈ RSA (montant exact ⚠️ à confirmer Étape 4).

### Recouvrement — la chaîne (cœur du pivot)
1. **Amiable / mise en demeure** (LRAR).
2. **Intermédiation financière ARIPA (IFPA)** : **automatique depuis le 1ᵉʳ janvier 2023** pour toute séparation/décision fixant une pension dans un titre exécutoire ; ARIPA collecte auprès du débiteur et reverse au créancier. Refus possible d'un commun accord ou par le juge ; **obligatoire (sans refus) en cas de violences conjugales**. Base : CSS art. **R582-5 s.** ([LEGISCTA000042384268](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000042384268/2021-05-25)) ; [service-public F36407](https://www.service-public.gouv.fr/particuliers/vosdroits/F36407) ; [ARIPA](https://pension-alimentaire.caf.fr/l-intermediation-financiere).
3. **ASF (allocation de soutien familial)** : **200,78 €/mois/enfant** (parent isolé) / 267,63 € (enfant recueilli), au **1ᵉʳ avril 2026**. Versée quand la pension est en cours de fixation, faible **ou impayée**. **ASF-avance** : la CAF/MSA avance puis **recouvre auprès du débiteur**. → [service-public F815](https://www.service-public.gouv.fr/particuliers/vosdroits/F815) + [ARIPA ASF](https://pension-alimentaire.caf.fr/usagers/aides-et-demarches/allocation-de-soutien-familial).
4. **Paiement direct / saisie** (employeur, banque, tiers détenteurs), sans recours préalable à un huissier via l'ARIPA.
5. **Pénal** : plainte pour **abandon de famille** (227-3) après > 2 mois.

### Prescription
- **Art. 2224 C. civ.** : actions personnelles **5 ans** → arriérés recouvrables **jusqu'à 5 ans en arrière** ; **interruption** par citation/commandement/saisie (relance 5 ans). → [LEGIARTI000019017112](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019017112).

### Fiscalité (démystification — Information Gain)
- **Loi de finances 2026** (revenus 2025) : le parent qui **verse déduit** (plafond enfant majeur **6 855 €** ; **13 710 €** si enfant chargé de famille ; **forfait logement-nourriture 4 075 €** si l'enfant majeur vit chez lui) ; le bénéficiaire **déclare**. → [service-public A15453](https://www.service-public.gouv.fr/particuliers/actualites/A15453) + [F2](https://www.service-public.gouv.fr/particuliers/vosdroits/F2) + [economie.gouv.fr](https://www.economie.gouv.fr/particuliers/impots-et-fiscalite/gerer-mon-impot-sur-le-revenu/impot-tout-savoir-sur-la-deduction-des-pensions-alimentaires).
- ⚠️ **Rumeur PAA à corriger** : « le parent qui reçoit n'est plus imposé jusqu'à 4 000 €/enfant » = **confusion** avec le forfait d'hébergement **4 075 €** (enfant majeur logé). Pas de défiscalisation de la pension reçue.

### Disambiguation (périmètre Nicolas : enfant + pension entre époux)
- **Pension au titre du devoir de secours** entre époux pendant la procédure : art. **212 / 255 C. civ.** (à confirmer Étape 4).
- **Prestation compensatoire** (post-divorce, capital/rente, ≠ pension) : art. **270 s. C. civ.** (à confirmer Étape 4). → tie-in affaire cabinet (cf. Bloc C).

---

## BLOC C — Interne Plouton (mapping Wix vérifié)

### Pages d'expertise cibles (conversion)
- Principale : `/droit-des-contrats-et-des-personnes/droit-de-la-famille`
- Pivot pénal : `/defense-penale/droit-penal`
- Connexe séparation : `/droit-des-contrats-et-des-personnes/droit-de-la-famille/avocat-divorce-bordeaux`
- Connexe sensible (lien discret) : `/defense-penale/violences-conjugales-et-feminicides`
- CTA contact : `/honoraires-rendez-vous`

### Posts famille publiés (13 — slugs vérifiés Wix MCP ; URLs canoniques sans `?cooked_*`)
**Preuves maîtresses :**
- `prestation-compensatoire-notre-cabinet-obtient-le-rejet-de-deux-demandes-devant-le-jaf-de-bordeaux` (2026) — rejet de demandes de 18 k / 50 k € au JAF de Bordeaux → **section pension entre époux / prestation compensatoire**.
- `non-representation-enfant-defense-strategie-avocat` — **cousin pénal** de l'abandon de famille (atteinte aux obligations familiales) → **pont pénal∩famille**.

**« Voir aussi » crédibilité famille locale (garde/résidence/protection) :**
- `garde-alternée-la-mère-obtient-le-rejet-de-la-demande-présentée-par-le-père` ; `divorce-le-père-obtient-la-garde-de-son-fils-pour-cause-d-éloignement-géographique-de-la-mère` ; `divorce-obtention-d-un-droit-de-visite-et-d-hébergement-classique-pour-le-père-malgré-le-refus-de-l` ; `droit-visite-mediatise-interet-enfant-cabinet-plouton` ; `droit-de-visite-et-ordonnance-de-protection-notre-cabinet-défend-le-maintien-du-lien-père-enfant`.
- Volet violences (lien discret seulement) : `ordonnance-protection-violences-conjugales-cas-pratique-bordeaux` ; `ordonnance-de-protection-un-bouclier-contre-les-violences-sous-alcool` ; `tribunal-judiciaire-une-ordonnance-de-protection-délivrée-pour-des-violences-psychologiques` ; `affaire-chahinez-daoud-...`.
- ⚠️ Slugs avec accents → **URL-encoder** au linking (LEARN-057).

### Gap interne
**Aucun** post cabinet sur pension impayée / recouvrement / abandon de famille (confirmé par Nicolas : le droit de la famille « ordinaire » ne fait pas un post). → le pilier comble un trou interne ; **preuve impayé/abandon de famille = matière publique + verbatims** (pas d'affaire cabinet disponible).

### Matière propriétaire — 678 messages de contact
- **Famille = 113 (16,7 %)**, 2ᵉ motif derrière le pénal (137 / 20,2 %). L'abandon de famille relie les deux viviers.
- Personas mixtes : créancier lésé (CAF/ARIPA insuffisante, « combats pour faire valoir mes droits ») · fixation (« à combien doit s'élever la pension ? ») · débiteur de bonne foi (licenciement → veut réviser, **en conflit avec l'ARIPA** qui réclame l'ancien montant).
- Nombreux dossiers à l'**aide juridictionnelle** (solvabilité mixte). Recoupements **violences intrafamiliales** (tact).
- Verbatims anonymisés (RGPD) → illustrations de l'article, jamais de PII.

---

## BLOC D — Stats (Information Gain + citabilité)

Source primaire : **CNAF, *L'Essentiel* n°222 (2024)** — [PDF](https://www.caf.fr/sites/default/files/medias/cnaf/Nous_connaitre/Recherche_et_statistiques/Essentiel/222_2024_ESSENTIEL_Intermediation_financi_PA__CNAF.pdf) (extraction au précis = Étape 4, LEARN-061) ; [Sécurité sociale — évaluation 2.4](https://evaluation.securite-sociale.fr/home/famille/24-ameliorer-le-recouvrement-des.html).

- **Taux de recouvrement ARIPA** : 62,5 % (2017) → **70 % fin 2023** → **~30 % des impayés non recouvrés**.
- **353 546** demandes d'intermédiation déposées · **193 870** parents ayant reçu ≥ 1 paiement intermédié (fin 2023 ; chiffres mécaniquement supérieurs depuis l'automaticité 2023 → réactualiser).
- La pension = **18 % en moyenne des ressources des familles monoparentales**.
- Ampleur des impayés : **~30 %** (ordre de grandeur, rapport public 2016 — à dater explicitement).
- ASF : **200,78 €/mois/enfant** (1ᵉʳ avril 2026) — filet plancher.
- ⚠️ Millésimes à afficher ; viser chiffres 2024/2025 si dispo au moment de rédiger (refresh M+6 — LEARN-046).

### Ancrage local (LEARN-042 — min. 3 mentions Bordeaux/NAQ)
JAF / Tribunal judiciaire de **Bordeaux** (juridiction + affaire prestation compensatoire) · cabinet Bordeaux (Cours d'Alsace-et-Lorraine) · zone d'intervention Nouvelle-Aquitaine.

---

## Synthèse → implications Étape 3 (plan)

- **Angle confirmé** : pilier *notion* enfant (+ clarif pension entre époux/prestation compensatoire), **pivot non-paiement → abandon de famille**. Calcul/barème **court** (renvoi simulateur). Budget-mots sur impayé/pénal.
- **H1 direction** : pivot « recours/impayé » (pas « calcul »). 3 variantes en Étape 3, filtre anti-commodity.
- **Information Gain (≥ 4 éléments)** : ARIPA double tranchant · 227-3 par un pénaliste · démystification « nouvelle loi »/fiscal · chaîne recouvrement sourcée avec seuils · données cabinet Bordeaux.
- **FAQ 8-10 (LEARN-044/045)** : cibler la nuance (2 mois → plainte ? ; garde alternée → pension ? ; ARIPA refusable ? ; arriérés sur combien d'années ? ; enfant majeur ? ; débiteur qui ne peut plus payer ? ; pension ≠ prestation compensatoire ?).
- **À finaliser Étape 4** : extraction PDF CNAF (chiffres précis) · arrêts Judilibre PROD (3 cibles ci-dessus) · n° articles 212/255/270 · minimum vital.

---

*Collecte établie le 2026-06-16. En attente de validation Nicolas avant Étape 3 (plan).*
