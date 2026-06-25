# Collecte — Article #6 — Passager victime d'un accident de la route

> Livrable Étape 2 du workflow. Ordre d'attaque LEARN-018 : **B SEO → A juridique → C Plouton → D stats**.
> Date : 2026-05-17. Worktree : `busy-colden-919e63`.

---

## Synthèse exécutive Bloc B (à valider avant A/C/D)

| Indicateur | Valeur | Conclusion |
|---|---|---|
| Head term `indemnisation passager accident voiture` | **0/mois confirmé** par Google Ads (vol non retourné — niveau zéro) | Univers passager direct trop confiné pour viser le head term seul |
| Variante prioritaire `indemnisation accident de la route passager` | **70/mois** (informational, trend yearly -95%) | **Requête sœur centrale** — équivalent volume head term article #4 (vélo : 70/mois également) |
| Univers amont `indemnisation accident de la route` | **720/mois** (MEDIUM, CPC 2,42 €) | **Capture amont prioritaire** — l'angle passager qualifie 100% des cas où le chercheur amont est passager |
| Univers amont `victime accident de la route` | **170/mois** | Cluster cohérent |
| Univers amont `indemnisation accident voiture` / `accident voiture indemnisation` | **110/mois × 2** | Capture intermédiaire |
| SERP top 10 head term passager | 6 cabinets / 2 assureurs / 1 institutionnel / 1 agrégateur / 1 asso | **Concurrence cabinet directe + featured snippet asso (capturable)** |
| Information Gain attendu | 3-4 axes solides | Pivot art. 3 vs 4 + cartographie multi-modale + section décès ayants droit + ancrage Bordeaux/NAQ |

**Décision stratégique** : viser **l'univers sémantique « accident de la route » de A à Z** avec entrée passager comme pivot propriétaire. FAQ + sous-sections multi-cas couvrent le query fan-out (LEARN-053 Doctrine Google).

---

## Bloc B — Données SEO (DataForSEO)

### B.1 — SERP top 10 + PAA + Related Searches

**Appel** : `serp_organic_live_advanced` — keyword `indemnisation passager accident voiture`, location France, language fr, device desktop, depth 20, PAA click depth 2. Date : 2026-05-17.

#### Top 10 organique

| Rang | Domaine | Type | Note |
|---|---|---|---|
| 1 ⭐ | **association-aide-victimes-france.fr** | **FEATURED SNIPPET** + organique #1 | Asso victimes — synthèse classique art. 3 Badinter. Featured snippet **récupérable** avec un encadré définition mieux structuré. |
| 2 | jmp-avocat-indemnisation.fr | Cabinet | Article pédagogique générique |
| 3 | ornikar.com | Assureur courtier | Angle assurance/garantie RC |
| 4 | benezra-victimesdelaroute.fr | Cabinet | Article **18 mai 2025** (récent — fraîcheur) — angle faute inexcusable |
| 5 | avocat-accident-regley.fr | Cabinet (page résultat affaire) | Affaire chiffrée 41 800 € — preuve sociale |
| 6 | *PAA bloc* | — | 8 PAA (voir B.1.bis) |
| 7 | justifit.fr | Agrégateur juridique | **26 février 2026** — angle "bus ou voiture" multi-modal |
| 8 | service-public.gouv.fr | Institutionnel | Page F2677 référence — distinction conducteur/non-conducteur |
| 9 | qivio.fr | Assureur | Angle garantie passager |
| 10 | sanajuris.fr | Cabinet | Générique |
| 11 | gentiliavocat.fr | Cabinet | Liste postes de préjudice |

**Composition SERP** : 6 cabinets / 2 assureurs / 1 institutionnel / 1 agrégateur / 1 asso victimes. **Cabinets dominants → concurrence directe**. Mais **aucun cabinet n'occupe le pivot « asymétrie art. 3 vs 4 » avec rigueur**, aucun ne propose une cartographie multi-modale (voiture/moto/VTC/taxi/car) consolidée.

**Featured snippet capturable** : l'asso aide victimes occupe la position 0 avec un texte générique « réparation intégrale ». Notre Article #6 peut le **déloger** avec un encadré définition mieux structuré citant frontalement art. 3 + n° de pourvoi Cass. 2023 (LEARN-017 citabilité LLM).

#### B.1.bis — PAA observées (8 questions)

| # | Question PAA | Source citée par Google | Exploitable Article #6 ? |
|---|---|---|---|
| 1 | **Un passager peut-il prétendre à une indemnisation ?** | pearsonlegal.co.uk (UK) | **Oui** — Q1 FAQ — réponse française manquante au SERP |
| 2 | **Quelle est la garantie d'un passager ?** | qivio.fr | **Oui** — Q2 FAQ — pivot RC du conducteur où était le passager |
| 3 | **Quels sont les 3 préjudices indemnisés ?** | delbez-joly-avocats.fr | Oui mais flou ("3 préjudices" = phrasing approximatif) — à reformuler en Q proche : *« Quels postes de préjudice peut réclamer un passager ? »* sourcée Dintilhac |
| 4 | **Que se passe-t-il pour un passager lors d'un accident de voiture ?** | bencrump.com (US) | **Oui** — Q4 FAQ — réponse française manquante |
| 5 | Quelle est l'indemnisation pour un passager blessé dans un accident de voiture ? | association-aide-victimes-france.fr | Doublon Q1 — fusionner |
| 6 | **Que se passe-t-il si un passager provoque un accident ?** | joelbieber.com (US) | **Oui** — Q5 FAQ — angle « passager fauteur » jamais traité en français, **forte différenciation** |
| 7 | Quelle est l'indemnisation pour un passager blessé dans un accident de voiture ? (variant) | idem | Doublon — fusionner |
| 8 | **Puis-je faire une réclamation en tant que passager ?** | jmw.co.uk (UK) | **Oui** — Q6 FAQ — angle « droit d'action » |

**Conclusion PAA** : 6 questions distinctes exploitables, dont **4 dont la réponse SERP actuelle est en anglais (UK/US legal)** → gap de réponse française autoritaire **fort**. Réservoir suffisant pour atteindre 8-10 Q FAQ (LEARN-044) avec 2-4 questions complémentaires issues du gap éditorial (cas VTC, enfant, ceinture, conducteur ivre).

#### B.1.ter — Related searches (8 items)

1. **Tableau indemnisation accident** — angle barème/grille (cohérent LEARN-045 anti-AI Overviews → encadré référentiel Dintilhac)
2. **Montant indemnisation accident de voiture non responsable** — variation upstream — confirme appétit pour le chiffré
3. **Assurance passager voiture** — confirme PAA #2
4. **Doit on porter plainte après un accident pour toucher des indemnité** — angle pénal/civil (cf cas alcool / délit de fuite)
5. **Traumatisme psychologique après un accident de voiture indemnisation** — préjudice extra-patrimonial (SSPT — Dintilhac)
6. **Montant indemnisation décès accident route** — confirme angle décès / ayants droit (synergie avec affaire Chaniers 350k€)
7. **Dommage et intérêt accident de voiture** — variation lexicale (langage non-juridique)
8. **Exemple indemnisation accident de la route** — appétit cas chiffrés (synergie avec preuves cabinet 90k/200k/350k/500k/2M€)

---

### B.2 — Volumes head term + cluster amont

**Appels** : `kw_data_google_ads_search_volume` — 2 batchs (20 + 17 keywords). France, fr.

#### Univers passager direct (top suggestions)

| Keyword | Volume mensuel | CPC | Compétition | Intent | Trend yearly |
|---|---|---|---|---|---|
| **`indemnisation accident de la route passager`** | **70** | 1,33 € | MEDIUM | informational | -95% (déclin) |
| `indemnisation passager accident de voiture` | 20 | 1,40 € | MEDIUM | commercial | +50% |
| `accident de voiture passager blessé` | 30 | 1,64 € | MEDIUM | informational | -80% |
| `accident voiture passager assurance` | 10 | — | MEDIUM | commercial | -67% |
| `accident passager sans ceinture` | 10 | — | LOW | informational | stable |
| `accident de portière passager` | 10 | — | LOW | informational | stable |
| Tous autres `passager + accident` testés (head term, moto, VTC, taxi, enfant, FGAO, Badinter…) | **0 retourné** | — | — | — | — |

**Tendance pic saisonnier** : avril-mai-juin = pic structurel (saison conduite). Publication mai 2026 → bon timing.

#### Univers amont `accident de la route` (capture cluster)

| Keyword | Volume mensuel | CPC | Compétition | Intent |
|---|---|---|---|---|
| **`indemnisation accident de la route`** | **720** | 2,42 € | MEDIUM | (mixte) |
| `victime accident de la route` | 170 | 2,03 € | LOW | informational |
| `assurance accident voiture` | 140 | 2,02 € | LOW | commercial |
| `accident voiture indemnisation` / `indemnisation accident voiture` | **110 + 110** | 2,34 € | MEDIUM | (mixte) |
| `indemnisation accident corporel` | 110 | 2,08 € | MEDIUM | mixte |
| `indemnisation accident de voiture` | 50 | 2,84 € | MEDIUM | commercial |
| `indemnisation préjudice corporel voiture` / `indemnisation passager bordeaux` / `avocat accident voiture bordeaux` / `loi badinter passager` / `qui paie en cas d accident de voiture` / `passager accident` / `passager véhicule` / `indemnisation accident` / `qui indemnise le passager` | **0 retourné** | — | — | — |

**Total volume adressable cluster « accident de la route + passager »** : ≈ **70 (direct) + 720 + 170 + 220 + 110 + 50 = 1 340/mois**. Capter ne serait-ce que 5-10 % via l'angle passager = 70-130 visiteurs/mois qualifiés.

#### Comparatif avec article #4 (vélo) — pour calibration

- Article #4 head term `indemnisation accident vélo` : 70/mois, univers amont `accident vélo` : 1 300/mois → l'article a été calibré sur la capture amont.
- Article #6 head term `indemnisation accident de la route passager` : 70/mois, univers amont `indemnisation accident de la route` : 720/mois (univers amont **plus mature** que vélo) → **précédent #4 transférable**.

---

### B.3 — Keyword suggestions (sous-univers passager)

**Appel** : `dataforseo_labs_google_keyword_suggestions` — seed `passager accident`, France/fr, limit 100, filtre `search_volume > 0`, sort vol desc. Date : 2026-05-17.

#### Suggestions exploitables (signal vs bruit)

| Keyword | Volume | Intent | Note |
|---|---|---|---|
| `indemnisation accident de la route passager` | 70 | informational | **TOP** — sœur principale |
| `accident de voiture passager blessé` | 30 | informational | Variante lexicale |
| `indemnisation passager accident de voiture` | 20 | commercial | Variante formelle (KD 12 — facile) |
| `accident voiture passager assurance` | 10 | commercial | Angle assurance |
| `accident passager sans ceinture` | 10 | informational | **Angle ceinture confirmé** |
| `accident de portière passager` | 10 | informational | **Angle portière** (intersection avec article #4 vélo, mais ici côté passager qui descend) |

#### Bruit ignoré

- `stéphane rotenberg accident passager`, `accident a8 passager`, `accident mandelieu passager`, `accident koba la d passager`, `vince zampella accident passager` → actu / célébrités, non-cibles.
- `rêve accident de voiture passager`, `signification rêve accident de voiture passager`, `rever d'un accident de voiture passager` → onirique, non-cibles.
- `accident avion passager aspiré` → aérien, non-cibles.

**Conclusion B.3** : l'univers passager direct est **épuisé** (≤ 70/mois total head + 30+20+10+10+10 long-tail = ~150/mois cumulé adressable direct). Confirme la stratégie *« capture via cluster amont, passager comme pivot propriétaire »*.

---

### B.4 — Keyword ideas (sondage prospectif)

**Appel** : `dataforseo_labs_google_keyword_ideas` — seeds `passager accident` + `indemnisation passager` + `passager voiture accident`, France/fr, limit 100, clickstream activé, filtre `search_volume > 0`.

**Résultat** : sur 100 keywords retournés, **0 contient « passager » ou « indemnisation »**. L'algorithme a clusterisé sur la catégorie large « voiture » et retourné l'univers `location voiture`, `voiture occasion`, `voiture électrique`, `assurance voiture`, etc. — non exploitable.

**Lecture** : l'absence d'élargissement catégoriel **confirme la rareté absolue du sujet** dans la base sémantique Google. Pas d'univers prospectif latent à découvrir. La stratégie reste : (a) capture amont via cluster, (b) profondeur multi-modale + multi-cas à l'intérieur de l'article.

---

### B.5 — Gap analysis formalisée (Information Gain LEARN-039 + LEARN-053)

**Ce que le top 10 SERP fait déjà** (à ne pas reformuler) :
- Loi Badinter en généralité (art. 3 cité)
- « Réparation intégrale » comme formule
- Liste générique des postes de préjudice (souffrances, esthétique, frais médicaux)
- Mention faute inexcusable
- Process général d'indemnisation amiable

**Ce que le top 10 SERP NE FAIT PAS** (notre Information Gain) :

1. **Nommer l'asymétrie art. 3 vs art. 4 frontalement et la traduire en avantage opérationnel** — *« vous êtes protégé même quand votre conducteur a tort »*. Le pivot propriétaire H1.
2. **Cartographier les régimes selon le véhicule** où était le passager : voiture / moto / VTC-Uber / taxi G7 / car interurbain / bus TBM Bordeaux / covoiturage BlaBlaCar / véhicule professionnel / véhicule non assuré (FGAO). Tableau consolidé absent du SERP.
3. **Désamorcer la culpabilité d'actionner un proche** dans l'intro (LEARN-052 réflexe #2) — angle qualitatif sur les peurs émotionnelles du passager.
4. **Section décès / proches ayant droit chiffrée** avec affaires cabinet (Chaniers 350k€ + tétraplégie 2M€). Aucun cabinet en SERP n'illustre cette fourchette.
5. **Cas du passager VTC/Uber** spécifiquement — angle moderne assurance pro/plateforme/conducteur sous-assuré. Absent du SERP français.
6. **Réponses françaises autoritaires sur 4 PAA actuellement en anglais (UK/US)** — capture PAA française manquante.
7. **Ancrage local Bordeaux/Nouvelle-Aquitaine** — `indemnisation passager bordeaux` et `avocat accident voiture bordeaux` à volume non retourné mais intent qualifié + LEARN-042 (signal Google + différenciation cabinet local).
8. **Synthèse cabinet « combien obtenir »** par gravité : 41 800 € (cas SERP #5) → 90k → 200k → 350k → 500k → 2M€ — fourchette propriétaire fondée sur 5+ affaires cabinet, conforme LEARN-048 (synthèse profonde).

**Couverture query fan-out** (LEARN-053) : les PAA + related searches + suggestions seront répondus dans le corps (cartographie multi-modale, encadrés chiffrés, sections cas particuliers) ET dans la FAQ 8-10 Q.

---

### B.6 — Conclusions B (cadre Étape 3)

1. **Stratégie volume** : viser cluster amont (1 340/mois cumulé) via pivot passager, pas head term direct seul.
2. **Pivot propriétaire H1** confirmé : *asymétrie art. 3 vs art. 4*. Aucun concurrent SERP ne l'occupe frontalement.
3. **Information Gain réalisable** : 8 axes différenciants identifiés (vs 6-7 sur article #4 → potentiel équivalent ou supérieur).
4. **Featured snippet récupérable** : encadré définition art. 3 avec n° pourvoi Cass. 2023 dans les 50 premiers mots.
5. **FAQ 8-10 Q** atteignable : 6 PAA + 2-4 questions issues du gap éditorial.
6. **Tendance saisonnière** : publication mai-juin idéale (pic structurel).

---

## Bloc A — Matière juridique (fact-check WebSearch Légifrance — LEARN-026 anti-récidive)

### A.1 — Articles de loi pivots (texte verbatim sourcé Légifrance)

#### Loi n° 85-677 du 5 juillet 1985 dite « loi Badinter »

**Article 3** ([Légifrance LEGIARTI000006839422](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006839422)) — texte verbatim :

> « Les victimes, hormis les conducteurs de véhicules terrestres à moteur, sont indemnisées des dommages résultant des atteintes à leur personne qu'elles ont subis, sans que puisse leur être opposée leur propre faute à l'exception de leur faute inexcusable si elle a été la cause exclusive de l'accident.
>
> Les victimes désignées à l'alinéa précédent, lorsqu'elles sont âgées de moins de seize ans ou de plus de soixante-dix ans, ou lorsque, quel que soit leur âge, elles sont titulaires, au moment de l'accident, d'un titre leur reconnaissant un taux d'incapacité permanente ou d'invalidité au moins égal à 80 p. 100, sont, dans tous les cas, indemnisées des dommages résultant des atteintes à leur personne qu'elles ont subis.
>
> Toutefois, dans les cas visés aux deux alinéas précédents, la victime n'est pas indemnisée par l'auteur de l'accident des dommages résultant des atteintes à sa personne lorsqu'elle a volontairement recherché le dommage qu'elle a subi. »

**Lecture pivot Article #6** : trois alinéas → trois régimes empilés.
- **Alinéa 1** = régime de droit commun du passager (= victime non-conductrice). Faute simple inopposable. Seule exception : faute inexcusable **ET** cause exclusive de l'accident (deux conditions cumulatives).
- **Alinéa 2** = régime ultra-protecteur pour passager <16 ans, >70 ans, ou titulaire d'IT/invalidité ≥80 %. Indemnisation systématique, aucune faute opposable.
- **Alinéa 3** = seule limite — la recherche volontaire du dommage (suicide, mise en scène). Hypothèse rarissime.

**Article 4** ([Légifrance LEGIARTI000006839431](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000006839431)) — texte verbatim :

> « La faute commise par le conducteur du véhicule terrestre à moteur a pour effet de limiter ou d'exclure l'indemnisation des dommages qu'il a subis. »

**Lecture pivot Article #6** : c'est l'**asymétrie centrale**. Le conducteur peut voir son indemnisation réduite ou exclue par sa propre faute (négligence, vitesse, distraction). Le passager, dans le même véhicule, dans le même accident, **n'est pas touché par cet art. 4** — il reste sous art. 3, donc protégé.

**Article 1** ([Légifrance, loi 85-677](https://www.legifrance.gouv.fr/loda/id/LEGITEXT000006068902/)) — extrait :

> Loi applicable « aux victimes d'un accident de la circulation dans lequel est impliqué un véhicule terrestre à moteur ainsi que ses remorques ou semi-remorques, à l'exception des chemins de fer et des tramways circulant sur des voies qui leur sont propres. »

**Lecture pivot Article #6** : la **notion d'implication** suffit (pas besoin de contact direct). Concerne voiture, moto, scooter, VTC, taxi, car, bus, camionnette, véhicule professionnel, etc. Hors champ : train (SNCF), tramway sur voies propres (régime SNCF/RATP/exploitant + Convention de Bruxelles).

#### Code des assurances

**Article L. 211-9** ([Légifrance LEGIARTI000006795446](https://www.legifrance.gouv.fr/affichCodeArticle.do?cidTexte=LEGITEXT000006073984&idArticle=LEGIARTI000006795446)) — synthèse :

- Si responsabilité non contestée + dommage entièrement quantifié → l'assureur garantissant la RC du véhicule présente à la victime **une offre motivée d'indemnisation dans un délai de 3 mois** à compter de la demande.
- Quoi qu'il en soit, **une offre d'indemnisation doit être faite à la victime ayant subi une atteinte à sa personne dans le délai maximum de 8 mois à compter de l'accident**.
- Si responsabilité rejetée/non clairement établie ou dommage non entièrement quantifié → l'assureur présente une **réponse motivée** dans le même délai.
- **Offre provisoire** si l'assureur n'a pas été informé de la consolidation dans les 3 mois suivant l'accident → **offre définitive dans les 5 mois suivant la notification de la consolidation**.
- **En cas de décès** : l'offre est faite aux héritiers et, le cas échéant, au conjoint. Inclut tous éléments indemnisables (matériel inclus si non déjà réglé).

**Articles L. 211-8 à L. 211-25** ([Légifrance LEGISCTA000006174255](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006174255)) — section VI « Procédures d'indemnisation ». Encadrent l'ensemble de la procédure amiable (information victime, droit à un médecin-conseil, droit à un avocat, contestation de l'offre, intérêts moratoires si retard).

**Article L. 421-1** ([Légifrance LEGIARTI000048523697](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048523697)) — FGAO :

- Le Fonds de Garantie des Assurances Obligatoires de dommages indemnise les victimes ou ayants droit de dommages résultant d'un accident survenu en France impliquant un véhicule au sens de l'article L. 211-1.
- Intervient pour les dommages corporels quand le responsable est **inconnu** (délit de fuite avec auteur non identifié) **ou non assuré** (sauf exemption légale).
- Contribution de l'auteur non assuré : 10 % des indemnités restant à sa charge.

### A.2 — Jurisprudences pivots (vérifiées)

#### Faute inexcusable de la victime non-conductrice — référence stricte

**Cass. Assemblée plénière, 10 novembre 1995, n° 94-13.912** ([Légifrance JURITEXT000007034785](https://www.legifrance.gouv.fr/juri/id/JURITEXT000007034785/) + [Juricaf](https://juricaf.org/arret/FRANCE-COURDECASSATION-19951110-9413912)) :

> « Seule est inexcusable au sens de l'article 3 de la loi du 5 juillet 1985 la faute volontaire d'une exceptionnelle gravité exposant sans raison valable son auteur à un danger dont il aurait dû avoir conscience. »

**Lecture pivot Article #6** : référence d'Assemblée plénière (= la plus haute formation de la Cour de cassation), reprise constamment depuis 1995 par la 2ᵉ chambre civile. Définit la faute inexcusable de la victime non-conductrice par **4 critères cumulatifs** : (1) faute volontaire, (2) exceptionnelle gravité, (3) sans raison valable, (4) exposition à un danger dont l'auteur aurait dû avoir conscience. En pratique : le seuil est si élevé que la faute inexcusable du passager est **quasi-jamais retenue**.

#### Cas où la faute inexcusable a été écartée pour le passager

Selon la doctrine constante issue notamment de Cass. Civ. 1ʳᵉ 17 novembre 1993 et confirmée par la 2ᵉ chambre civile, **ne constituent pas une faute inexcusable cause exclusive** :

- le fait pour un passager de ne pas porter sa ceinture de sécurité ;
- le fait de monter dans le véhicule d'un conducteur manifestement en état d'ébriété ;
- le fait d'être soi-même en état d'ébriété au moment de l'accident ;
- le fait de traverser hors passage piéton (cas piéton, applicable par analogie au passager qui descend).

**⚠️ À reconfirmer NotebookLM Nicolas si on cite un n° de pourvoi récent** : besoin d'un arrêt précis Cass. Civ. 2ᵉ 2018-2025 sur passager sans ceinture (verbatim citable). Pour l'instant : fondement art. 3 + AP 1995 suffisent à porter la règle, sans risque d'erreur sur un n° de pourvoi mal mémorisé.

#### Recours de l'assureur contre le passager fautif — exclusion

**Cass. Civ. 2ᵉ, 30 mars 2023, n° 21-17.466** ([Juricaf](https://juricaf.org/arret/FRANCE-COURDECASSATION-20230330-2117466)) — résumé :

- Le 28 avril 2016 : accident mortel impliquant une moto qui dépasse un véhicule. Le passager du véhicule dépassé tend le bras hors la fenêtre pour jeter de la cendre de cigarette, contribuant à l'accident.
- L'assureur du véhicule (PACIFICA) indemnise les ayants droit du motard décédé, puis assigne le passager fautif en intervention forcée pour récupérer les sommes versées.
- **Cass. casse** : la responsabilité civile du passager est garantie par l'assureur du conducteur, qui **n'a aucun recours possible contre le passager même fautif**, l'assureur étant aussi l'assureur du passager au titre de la RC du véhicule.

**Lecture pivot Article #6** : règle utile pour la **PAA #6** (« Que se passe-t-il si un passager provoque un accident ? »). Le passager bénéficie d'une protection patrimoniale double : (a) il est indemnisé en tant que victime sous art. 3, (b) si sa faute cause un dommage à un tiers, **l'assureur du véhicule ne peut pas se retourner contre lui**.

**⚠️ Correction cadrage Étape 1** : j'avais cité par erreur le n° **21-22.866** ; le bon numéro est **21-17.466**. Aucun risque dans le draft puisque la vérification a eu lieu **avant rédaction** (LEARN-026 anti-récidive fonctionne).

#### Enfant passager / personne âgée / handicapée — protection renforcée

Fondement direct : art. 3 al. 2 loi Badinter (cf. A.1 supra). Indemnisation **systématique**, aucune faute opposable (sauf recherche volontaire du dommage al. 3, hypothèse rarissime).

**À reconfirmer si on cite un arrêt précis** sur l'application aux enfants passagers : la doctrine constante ne nécessite pas de pourvoi cité — l'article 3 al. 2 verbatim suffit comme fondement autonome.

### A.3 — Définitions techniques (encadrés définition prêts à rédiger)

| Concept | Définition sourcée |
|---|---|
| **« Victime non-conductrice »** (art. 3 Badinter) | Toute victime d'un accident impliquant un véhicule terrestre à moteur **autre que le conducteur** : piéton, cycliste, passager (peu importe le type de véhicule où il était), occupant d'un véhicule stationné. Bénéficie du régime art. 3 (le plus protecteur). |
| **« Faute inexcusable »** (Cass. AP 10 nov. 1995 n° 94-13.912) | « Faute volontaire d'une exceptionnelle gravité exposant sans raison valable son auteur à un danger dont il aurait dû avoir conscience. » 4 critères cumulatifs. Seuil très élevé — quasi-jamais retenue en pratique pour un passager. |
| **« Cause exclusive de l'accident »** (art. 3 Badinter) | La faute du passager doit avoir provoqué l'accident **à elle seule**, sans aucune autre contribution (du conducteur, d'un tiers, des conditions de route). Si autre facteur contributif → la faute n'est pas « cause exclusive » → reste inopposable. |
| **« Implication d'un véhicule terrestre à moteur »** (art. 1 Badinter) | Suffisance d'un lien matériel avec l'accident, sans nécessité de contact direct. Inclut voiture, moto, scooter, VTC, taxi, car, bus, camionnette, véhicule professionnel, remorque. Exclut train SNCF, tramway sur voies propres. |
| **« Implication suffit »** (Cass. jurisprudence stable) | Un véhicule est « impliqué » dès qu'il intervient à un titre quelconque dans l'accident, même à l'arrêt, même sans contact (ex : portière ouverte, déboîtement, dépassement contraignant). |
| **« Réparation intégrale du préjudice »** (principe directeur) | Le passager doit être remis dans l'état le plus proche de celui où il se trouverait si l'accident n'avait pas eu lieu. Tous postes Dintilhac indemnisables (frais médicaux, perte de revenus, souffrances, esthétique, agrément, sexuel, etc.). |

### A.4 — Procédure et délais clés (à mobiliser en section H2 procédure)

| Étape | Délai légal | Source |
|---|---|---|
| Déclaration de l'accident à l'assureur du véhicule où était le passager | 5 jours ouvrés | Code des assurances L. 113-2 |
| Offre d'indemnisation (provisoire ou définitive) par l'assureur | **8 mois max** à compter de l'accident | L. 211-9 al. 2 |
| Offre définitive si consolidation tardive | **5 mois après notification de la consolidation** | L. 211-9 |
| Prescription de l'action en indemnisation du passager victime corporelle | **10 ans** à compter de la consolidation du dommage | Article 2226 Code civil (action en responsabilité née d'un dommage corporel) |
| Recours FGAO si véhicule non assuré ou auteur inconnu | À engager dans les délais FGAO (1 an à compter de la connaissance du défaut d'assurance pour dommage matériel ; régime spécifique dommage corporel) | L. 421-1 et R. 421-1 et s. Code des assurances |

### A.5 — Identification de l'assureur compétent — règle pivot

**Principe** : la victime passagère est indemnisée par **l'assurance RC obligatoire du véhicule dans lequel elle se trouvait**, peu importe que le conducteur de ce véhicule soit responsable ou non. C'est l'assureur du véhicule transporteur qui pilote l'indemnisation.

**Variantes selon le scénario** (à cartographier en H2 « cas particuliers ») :

| Scénario | Assureur compétent | Source |
|---|---|---|
| Passager d'une voiture, conducteur seul fautif | Assureur du véhicule où était le passager | L. 211-1 et art. 3 Badinter |
| Passager d'une voiture, tiers fautif | Assureur du véhicule transporteur (avance) + recours subrogatoire contre l'assureur du tiers | Mécanique L. 121-12 |
| Passager d'un VTC/Uber/Bolt | Assurance pro flotte du VTC (RC professionnelle obligatoire LOTI) | Code des transports + L. 211-1 |
| Passager d'un taxi | Assurance RC professionnelle du taxi | Code des transports |
| Passager d'un car interurbain / bus | Assurance RC transporteur (Convention Bruxelles si international) | Code des transports |
| Passager d'un véhicule professionnel (employeur) | Assurance du véhicule **+** régime AT-MP si trajet de travail | CSS L. 411-1 et s. |
| Passager d'un véhicule volé ou non assuré | **FGAO** (Fonds de Garantie des Assurances Obligatoires) | L. 421-1 Code des assurances |
| Passager d'un véhicule en covoiturage BlaBlaCar | Assurance du véhicule (RC obligatoire) — pas de différence de régime selon que le conducteur facture | L. 211-1 + circulaire 2014 covoiturage |
| Passager d'une moto/scooter | Assurance du 2RM transporteur (RC obligatoire) | L. 211-1 + art. 3 |

---

## Bloc C — Contexte interne Plouton (lectures Firecrawl 2026-05-17)

### C.1 — Affaires cabinet — lecture détaillée des 4 URLs Nicolas

#### ⚠️ C.1.a — Affaire « supporter nantais » — INCOMPATIBLE avec l'angle Article #6

**URL** : [/post/décès-d-un-supporter-nantais-avant-le-match-fc-nantes-ogc-nice](https://www.jplouton-avocat.fr/post/d%C3%A9c%C3%A8s-d-un-supporter-nantais-avant-le-match-fc-nantes-ogc-nice)

**Constat lecture intégrale** : cet article est intitulé en interne *« Supporter nantais tué à la Beaujoire : défense du chauffeur VTC »*. Le cabinet **défend pénalement le chauffeur VTC mis en examen** pour le décès d'un supporter nantais (coup de couteau, attaque du véhicule par une centaine de personnes, dont individus cagoulés, le 2 décembre 2023 aux abords du stade de la Beaujoire avant FC Nantes / OGC Nice). Les **passagers du VTC** (supporters niçois) ont été pris à parti mais ne sont pas victimes du chauffeur — au contraire, le chauffeur les protégeait.

**Dissonance frontale** :
- Pôle d'expertise : **défense pénale**, pas indemnisation des victimes
- Rôle cabinet : défend l'auteur du coup mortel (le chauffeur VTC)
- Logique : pénal/violences, pas Loi Badinter / accident de la route

**Recommandation Étape 3** : **écarter** cette affaire de l'Article #6. L'inclure créerait un contresens d'angle (article victime → mais affaire défense auteur) qui dégraderait la cohérence du H1 propriétaire *« vous êtes protégé même quand votre conducteur a tort »*. À garder éventuellement comme cross-link prudent dans un futur article sur **défense pénale en marge des accidents de la route** ou **violences sportives**.

**À valider Nicolas** : OK pour écarter, ou tu veux un usage particulier ?

#### ✅ C.1.b — Affaire Chaniers (17) — 350 000 € pour 4 familles de passagers décédés — AFFAIRE PIVOT

**URL** : [/post/accident-mortel-à-chaniers-17-le-cabinet-obtient-près-de-350-000-euros-d-indemnisation-pour-les](https://www.jplouton-avocat.fr/post/accident-mortel-%C3%A0-chaniers-17-le-cabinet-obtient-pr%C3%A8s-de-350-000-euros-d-indemnisation-pour-les)

**Synthèse factuelle (lecture intégrale)** :

- **Date accident** : 26 septembre 2015, aube. **Lieu** : route de La Font du Loup, Chaniers (Charente-Maritime — Nouvelle-Aquitaine 🎯 ancrage local LEARN-042)
- **Contexte** : 5 jeunes hommes, vingtaine d'années, retour de fête après célébration de l'obtention du concours de médecine d'un d'eux. Peugeot 406
- **Mécanique** : conducteur M. A. perd contrôle dans un virage, déporté sur voie opposée, percute de plein fouet véhicule M. M. (sexagénaire de Cognac). Peugeot quitte chaussée, chute dans bois, percute arbre, prend feu
- **Victimes** : **4 passagers décédés piégés dans l'incendie** ; conducteur M. A. éjecté, gravement blessé mais survit ; M. M. et son passager (véhicule percuté) blessés mais pronostic vital non engagé
- **Bataille juridique #1 — identification du conducteur** : M. A. nie initialement, invoque amnésie, désigne un passager décédé. Enquête mécanique prouve qu'il était au volant. Plusieurs mois de déni avant reconnaissance
- **Décision pénale** : 24 octobre 2019 — Tribunal correctionnel reconnaît M. A. coupable d'**homicide involontaire**
- **Décision civile** : **1er mars 2022 — Tribunal correctionnel de Saintes** — **350 000 € aux 4 familles**
- **Mécanisme juridique** : indemnisation prise en charge par **l'assurance du véhicule de M. M.** (le véhicule percuté, NON RESPONSABLE), au titre des **victimes par ricochet** sous Loi Badinter 1985

**Valeur Article #6** : **TOP** — affaire pivot pour 4 sections :

1. **Section décès passagers / ayants droit / victimes par ricochet** (cas archétypal)
2. **Section identification du conducteur** (cas pédagogique : quand toutes les victimes meurent, qui conduisait devient une bataille)
3. **Section articulation pénal/civil** (homicide involontaire → conducteur condamné → intérêts civils → indemnisation)
4. **Section ancrage local NAQ** (Chaniers 17, Charente-Maritime — zone d'intervention cabinet bordelais)

**Usage prévu** : 1-2 mentions étalées (section décès + section pénal/civil) + encadré chiffré (« 350 000 € pour 4 familles, Tribunal correctionnel de Saintes, 1er mars 2022 »).

#### ✅ C.1.c — Affaire Tétraplégie 2 M€ — Artan, passager arrière, Tizac-de-Curton — AFFAIRE PIVOT ABSOLUE

**URL** : [/post/accident-de-la-circulation-indemnisation-à-hauteur-de-2-millions-d-euros-pour-une-victime-tétrapleg](https://www.jplouton-avocat.fr/post/accident-de-la-circulation-indemnisation-%C3%A0-hauteur-de-2-millions-d-euros-pour-une-victime-t%C3%A9trapl%C3%A9g)

**Synthèse factuelle (lecture intégrale)** :

- **Date accident** : 12 décembre 2007. **Lieu** : Tizac-de-Curton (Gironde — **Nouvelle-Aquitaine 🎯**, intersection RD 936)
- **Victime** : **Artan, 41 ans, assis à l'arrière d'un véhicule conduit par un ami**
- **Mécanique** : un fourgon conduit par un homme **sous l'emprise de stupéfiants** grille un stop à l'intersection. Choc violent. **Artan éjecté, gravement blessé → tétraplégie**. Co-passagers également touchés
- **Parcours médical** : coma, hospitalisation **CHU Pellegrin (Bordeaux)**, rééducation **Tour de Gassies (Bruges — Bordeaux Métropole)**, **consolidation médicale** ensuite (citation Me Plouton : *« Rappelons que consolidation ne veut pas dire guérison mais signifie que l'état n'évolue plus »*)
- **Procédure** : action engagée contre **l'assurance du conducteur fautif** (le fourgonniste sous stup)
- **Décision** : **Tribunal de Grande Instance de Nanterre, 10 septembre 2015** — indemnisation **> 2 millions d'euros**, ventilation :
  - **811 161,48 €** : préjudices divers (assistance, aménagements, déficit fonctionnel, douleurs, agrément, sexuel, esthétique)
  - **1 201 293,12 €** : rente viagère trimestrielle (besoins permanents)
- **Indemnisation complémentaire** ultérieure : **> 500 000 €** au titre de l'**assistance tierce personne** initialement réservée par le tribunal
- **Note de contexte** : Artan a été victime d'une **agression à Bordeaux avenue Thiers** 3 mois avant le jugement (élément de vulnérabilité accrue, mais hors-sujet article #6 stricto sensu)

**Valeur Article #6** : **TOP ABSOLUE** — affaire centrale du #6, alignée à 100 % :

- ✅ **Passager arrière** d'un véhicule conduit par un ami → désamorce la culpabilité (LEARN-052 réflexe #2)
- ✅ **Tiers responsable sous stupéfiants** → passerelle parfaite vers `/victimes-de-delits-ou-crimes`
- ✅ **Tétraplégie / haut spectre** → preuve sociale plafond
- ✅ **Ancrage Bordeaux maximal** : CHU Pellegrin + Tour de Gassies + lieu Tizac-de-Curton (33) → LEARN-042 saturé
- ✅ **Fourchette indemnitaire ~2,5 M€** (2 M + 500k complémentaire) → chiffre pivot synthèse profonde LEARN-048
- ✅ **Citation verbatim Me Plouton** sur la consolidation → bio cabinet + voix « nous » LEARN-052
- ✅ **Co-passagers également touchés** → illustre que dans un même véhicule, plusieurs victimes peuvent réclamer

**Usage prévu** : 2-3 mentions étalées (intro storytelling cognitif LEARN-035 + section préjudices graves + CTA final + encadré chiffré « 2 M€ + 500k complémentaire »).

##### Double sourcing presse Sud Ouest (29 sept 2015) — ajout Nicolas 2026-05-17

L'affaire Artan a été couverte par **[Sud Ouest — édition Gironde / Cenon, 29 septembre 2015 (« Un triste pactole après une longue attente »), par Florence Moreau](https://www.sudouest.fr/gironde/cenon/gironde-un-triste-pactole-apres-une-longue-attente-7584053.php)**. Article réservé aux abonnés, avec **photo de Me Julien Plouton** en illustration.

**Apports complémentaires de l'article SO** (à intégrer prudemment Article #6) :

- **Date jugement TGI Nanterre confirmée** : 10 septembre 2015
- **75 % de déficit fonctionnel** (chiffre précis non détaillé dans le post cabinet)
- **Résidence Artan** : **Cenon** (banlieue Bordeaux), dans une **maison aménagée**
- **Verbatim presse Me Plouton** citables au-delà du post cabinet : *« Rappelons que consolidation ne veut pas dire guérison mais signifie que l'état n'évolue plus »* / *« Son préjudice physique est saisissant d'évidence »*
- Précision sur l'isolement post-accident (mère et cousin venus à son chevet)

**Implications stratégiques pour Article #6** :

1. **E-E-A-T renforcé** (LEARN-040) — citation cabinet **+** citation presse régionale = double sourçage externe. Signal d'autorité supplémentaire pour Google/AI Overviews (LEARN-053 doctrine officielle 2026).
2. **Ancrage Bordeaux Métropole saturé** (LEARN-042) — Cenon + Tizac-de-Curton + CHU Pellegrin + Tour de Gassies + (agression Avenue Thiers). **5 ancrages NAQ rien que pour cette affaire** — bien au-delà du minimum 3 LEARN-042.
3. **Storytelling cognitif** (LEARN-035) — la photo + le détail « maison aménagée » + le verbatim presse donnent matière à une ouverture H2 émotionnellement juste, sobre, sans pathos (LEARN-052 garde-fous).
4. **Précaution RGPD/déontologie** — Artan est déjà identifié publiquement par la presse régionale en 2015 (prénom + nationalité + commune). Pas de nouvel acte de publicité créé. **Recommandation Article #6** : citer Artan **par son prénom uniquement**, ne pas répéter sa nationalité (non nécessaire à l'angle juridique de l'article), respecter la sobriété de l'angle voix victime LEARN-052.

#### ✅ C.1.d — Article pilier Loi Badinter — confirmé en cross-link prioritaire cluster

**URL** : [/post/loi-badinter-85-comprendre-vos-droits-à-indemnisation-après-un-accident-de-la-route](https://www.jplouton-avocat.fr/post/loi-badinter-85-comprendre-vos-droits-%C3%A0-indemnisation-apr%C3%A8s-un-accident-de-la-route)

**Synthèse factuelle (lecture intégrale)** : article ressource complet, mis à jour 2025, qui couvre :
- Définition Loi Badinter + conditions d'application (3 conditions : VTAM, accident de la circulation, dommages)
- Droits selon statut : non-conducteurs (piétons, cyclistes, **passagers**) vs conducteurs
- Tableau récapitulatif clair (extrait verbatim) :
  > « Passager | Intégrale sauf recherche volontaire du dommage | La faute peut limiter ou exclure l'indemnisation | Protection renforcée pour les -16 ans, +70 ans et invalides à 80%+ »
- Procédure et délais
- Préjudices Dintilhac
- Évolutions législatives + jurisprudence Cass.

**Valeur Article #6** : **FORT** — délégation profondeur cluster LEARN-047. Notre Article #6 cite l'art. 3 + art. 4 + arrêt AP 1995 mais **délègue le cadre général Badinter au pilier** via 2-3 cross-links (section cadre légal + section procédure + FAQ).

**Usage prévu** : cross-link répété dans (a) section « régime Badinter » (b) section « procédure » (c) FAQ « Qu'est-ce que la loi Badinter ? » (réponse courte + cross-link).

### C.2 — Exploration feed catégorie `/blog/categories/accidents-de-la-route` (Firecrawl)

**Affaires supplémentaires repérées et arbitrées** :

| Affaire | URL | Pertinence Article #6 |
|---|---|---|
| **Angoisse mort imminente 35 210 € (TJ Pau, 22 sept 2025, n°130/2025)** | [/post/accident-mortel-angoisse-mort-imminente-tj-pau](https://www.jplouton-avocat.fr/post/accident-mortel-angoisse-mort-imminente-tj-pau) | **FORT (usage indirect)**. C'est un **piéton** percuté, pas un passager — mais **le préjudice d'angoisse de mort imminente** (20 000 € + 5 000 € préjudice d'attente proches) est exactement la jurisprudence à citer dans la **section postes de préjudice** et la **section décès passager**. Jugement très récent (sept 2025). Réponse parfaite à la related search *« traumatisme psychologique après un accident de voiture indemnisation »*. **À inclure en encadré chiffré ou phrase pivot section préjudices.** |
| **Choc frontal libournais 200k€ — septuagénaire** | [/post/accident-route-septuagenaire-indemnisation-200000-euros](https://www.jplouton-avocat.fr/post/accident-route-septuagenaire-indemnisation-200000-euros) | À sonder si Étape 3 le demande — pertinent si le septuagénaire est passager (régime renforcé art. 3 al. 2 — plus de 70 ans). À fact-check avant usage. |
| **Tétraplégie complémentaire 500k€** | [/post/victime-d-accident-de-la-circulation-et-tetraplegie-indemnisation-complementaire-de-plus-de-500-00](https://www.jplouton-avocat.fr/post/victime-d-accident-de-la-circulation-et-t%C3%A9trapl%C3%A9gie-indemnisation-compl%C3%A9mentaire-de-plus-de-500-00) | **Confirmé suite de l'affaire Artan 2 M€** (C.1.c) — pas une 2ᵉ affaire distincte, c'est la suite. Le total cumulé Artan ≈ 2,5 M€. |
| **Voyage organisé étranger** | [/post/accident-voyage-organise-etranger-responsabilite-agence](https://www.jplouton-avocat.fr/post/accident-voyage-organise-etranger-responsabilite-agence) | **Potentiel** pour la section « passager d'un car de tourisme à l'étranger » (régime Convention de Bruxelles + responsabilité de plein droit de l'agence sous L. 211-16 Code du tourisme). À arbitrer Étape 3 si on développe la section transport collectif. |
| Allianz Tunisie Porsche Cayenne | [/post/porsche-cayenne-accidente-en-tunisie-l-assurance-allianz-condamnee-a-bordeaux-pour-refus-d-indemnis](https://www.jplouton-avocat.fr/post/porsche-cayenne-accident%C3%A9-en-tunisie-l-assurance-allianz-condamn%C3%A9e-%C3%A0-bordeaux-pour-refus-d-indemnis) | À sonder — accident à l'étranger, peut illustrer la mobilisation internationale. Hors-cible probable Article #6 (pas passager). |
| Pretium doloris guide complet | [/post/le-pretium-doloris-guide-complet-pour-les-victimes-d-accidents](https://www.jplouton-avocat.fr/post/le-pretium-doloris-guide-complet-pour-les-victimes-d-accidents) | **MOYEN-FORT (cross-link cluster)** — article ressource sur les souffrances endurées (poste Dintilhac). À placer en cross-link dans la section « postes de préjudice » ou FAQ. |
| Traumatisme crânien accident voiture | [/post/traumatisme-cranien-accident-voiture](https://www.jplouton-avocat.fr/post/traumatisme-cranien-accident-voiture) | **MOYEN (cross-link cluster)** — typique séquelle de passager non ceinturé ou éjecté. À placer en cross-link section « préjudices graves ». |
| Incidence professionnelle Bordeaux | [/post/indemnisation-incidence-professionnelle-accident-route-bordeaux](https://www.jplouton-avocat.fr/post/indemnisation-incidence-professionnelle-accident-route-bordeaux) | **MOYEN (cross-link cluster)** — poste DFP/incidence pro applicable à toute victime route. Cross-link section postes Dintilhac. |
| Piéton renversé / Piéton percuté Bordeaux / Gyropode Arcachon (3 affaires piétons) | (3 URLs) | Cluster non-conducteur — à mentionner brièvement en analogie *« le piéton est sur le même régime art. 3 que vous passager »*. Cross-link unique vers 1 des 3 (Piéton renversé). |
| Affaires moto (3) / fracture pied conductrice | — | Hors-cible direct (conducteurs sous art. 4). Cross-link uniquement vers article ressource interne #1 moto. |
| Homicide routier Le Haillan défense pénale | — | Hors-cible (défense auteur) — même logique d'écart que C.1.a. |

### C.3 — Cross-links cluster (articles ressources Plouton — catégorie « Ressources et notions juridiques »)

#### C.3.a — Articles ressources Plouton publiés (feed catégorie ressources lu 2026-05-17, ajout Nicolas)

| Article ressource | Pertinence Article #6 | Placement prévu |
|---|---|---|
| [**Indemnisation CIVI : guide complet 2025**](https://www.jplouton-avocat.fr/post/indemnisation-civi-2025-guide-complet-pour-les-victimes-d-infractions) | **FORT** — CIVI intervient quand l'auteur de l'infraction (= le conducteur ou tiers fautif) est insolvable/inconnu **et** que l'accident est qualifié pénalement (homicide/blessures involontaires aggravées par alcool/stup). Cas typique : affaire Artan (fourgon sous stup). | Section « cas particuliers / conducteur sous infraction pénale » + FAQ Q dédiée *« CIVI ou FGAO, quelle voie pour un passager si l'assurance ne couvre pas tout ? »* |
| [SARVI : guide complet](https://www.jplouton-avocat.fr/post/sarvi-comment-r%C3%A9cup%C3%A9rer-vos-dommages-et-int%C3%A9r%C3%AAts-apr%C3%A8s-une-condamnation-p%C3%A9nale) | ⚠️ **EXCLU pour accidents de la circulation** (champ d'application SARVI exclut explicitement les accidents de la circulation qui relèvent du FGAO). | **Cross-link prudent uniquement** : si on mentionne SARVI dans la FAQ, c'est pour clarifier *« SARVI ne s'applique pas aux accidents de la circulation — c'est le FGAO et la CIVI qui sont vos voies »*. **Pas de cross-link de recommandation directe.** |
| [**SARVI ou CIVI : guide stratégique**](https://www.jplouton-avocat.fr/post/sarci-ou-civi-indemnisation-victimes) | **MOYEN** — utile au lecteur curieux qui veut comprendre les voies de complément. À placer une fois dans la section FAQ comme cross-link pédagogique. | FAQ ou section « cas particuliers » |
| [**Accident lors d'un voyage organisé à l'étranger : agence responsable de plein droit**](https://www.jplouton-avocat.fr/post/accident-voyage-organise-etranger-responsabilite-agence) | **FORT** — pour la section transport collectif (car de tourisme international, L. 211-16 Code du tourisme = responsabilité de plein droit de l'agence). | H3 « passager d'un car/bus de tourisme à l'étranger » |
| [Auto-entrepreneur victime d'un accident](https://www.jplouton-avocat.fr/post/auto-entrepreneur-victime-d-un-accident-comment-justifier-une-perte-de-revenus-ou-d-exploitation) | **MOYEN** — utile pour passager indépendant (perte d'exploitation post-accident — poste Dintilhac spécifique). | Section postes de préjudice (incidence professionnelle) ou FAQ |
| [Le pretium doloris : guide complet](https://www.jplouton-avocat.fr/post/le-pretium-doloris-guide-complet-pour-les-victimes-d-accidents) | **MOYEN-FORT** — souffrances endurées, poste pivot des préjudices passager grave. | Section postes de préjudice |
| [Traumatisme crânien après accident de voiture](https://www.jplouton-avocat.fr/post/traumatisme-cranien-accident-voiture) | **MOYEN** — séquelle typique du passager non ceinturé ou éjecté (Artan). | Section préjudices graves |
| [Mis en cause, témoin assisté, mis en examen, prévenu ou accusé](https://www.jplouton-avocat.fr/post/mis-en-cause-temoin-assiste-prevenu-accuse-differences) | **MOYEN-OPTIONNEL** — utile si on développe la section « procédure pénale parallèle quand le conducteur est poursuivi ». | Section pénal-civil (optionnel) |
| [Indemnisation ONIAM : conditions, seuil de gravité, procédure](https://www.jplouton-avocat.fr/post/accident-m%C3%A9dical-oniam-dans-quels-cas-pouvez-vous-%C3%AAtre-indemnis%C3%A9) | FAIBLE — ONIAM = accident médical, pas route. À écarter. | — |
| [Responsabilité du fait des choses](https://www.jplouton-avocat.fr/post/responsabilit%C3%A9-du-fait-des-choses-quels-recours-en-cas-de-chute-d-objet-tomb%C3%A9-ou-d-%C3%A9quipement-d%C3%A9f) | FAIBLE direct — chute d'objet, autre régime que Badinter. À écarter sauf si pertinent en cas particulier inattendu. | — |

**Total cross-links cluster ressources retenus** : **6 forts/moyens** (CIVI, SARVI ou CIVI, voyage organisé, auto-entrepreneur, pretium doloris, traumatisme crânien) + 1 optionnel (statuts pénaux) = **6-7 cross-links** vers articles ressources cabinet. Cohérent avec ARTICLE_TEMPLATE.md (4-7 cross-links articles ressources).

#### C.3.b — Articles ressources internes du pipeline

- [01-indemnisation-accident-moto/etape-4-article.md](01-indemnisation-accident-moto/etape-4-article.md) → cross-link dans la section H3 « passager moto » (article #1 a déjà couvert le passager moto en 1 H3 court — délégation profondeur)
- [04-indemnisation-accident-velo/etape-4-article.md](04-indemnisation-accident-velo/etape-4-article.md) → cross-link dans la section « usager vulnérable / FGAO » (analogie cycliste = piéton = passager sous art. 3)

#### C.3.c — Mécanique CIVI vs FGAO pour passager — précision rédactionnelle Article #6

| Voie | Champ d'application pour passager | Quand actionner ? |
|---|---|---|
| **Assureur du véhicule où était le passager** | Cas standard art. 3 Badinter | Toujours en premier (offre 8 mois L. 211-9) |
| **FGAO** (art. L. 421-1 Code des assurances) | Véhicule transporteur **non assuré** OU auteur tiers responsable **inconnu** (délit de fuite) | Si pas d'assureur identifié/solvable. Subsidiaire au régime Badinter. |
| **CIVI** (Commission d'Indemnisation des Victimes d'Infractions, Tribunal Judiciaire) | Si l'accident est **qualifié d'infraction pénale** (homicide ou blessures involontaires aggravées par alcool/stup/délit de fuite) **ET** que l'indemnisation Badinter/FGAO est insuffisante — solidarité nationale | Recours complémentaire, **3 ans à compter de l'infraction**. Cas typique : passager d'un conducteur sous stup où l'assurance bloque/insuffisant. |
| **SARVI** | **EXCLU pour accidents de la circulation** (champ explicitement exclu — relève du FGAO) | Jamais actionnable pour un passager accident route — à clarifier dans FAQ pour le lecteur qui aurait entendu parler du SARVI |

Cette mécanique éclaire la section « cas particuliers / si le conducteur a commis une infraction » et la FAQ.

#### C.3.d — Affaire libournais 200 000 € (bonus arbitré GO) — lecture

[/post/accident-route-septuagenaire-indemnisation-200000-euros](https://www.jplouton-avocat.fr/post/accident-route-septuagenaire-indemnisation-200000-euros)

- **Madame D.**, **au volant** de son véhicule, ceinturée, percutée de face par un conducteur n'ayant pas respecté un STOP. Polytraumatisée membre inférieur droit (fractures fémur, plateau tibial, calcanéum + côtes). Hospitalisation à Libourne.
- Indemnisation totale **236 879,51 €** (négociation amiable post-expertise médicale, novembre 2024).
- ⚠️ **Madame D. est CONDUCTRICE, pas passagère** → **HORS-CIBLE Article #6**.
- **Usage marginal possible** dans Article #6 : (a) en contraste pour illustrer la différence de régime conducteur (art. 4) vs passager (art. 3) — mais Artan déjà bien plus puissant pour ça ; (b) cross-link unique dans la section postes de préjudice comme exemple chiffré de polytraumatisme inférieur indemnisé en NAQ.
- **Recommandation** : **ne pas l'utiliser** dans Article #6 pour ne pas diluer. La garder pour un futur article cluster sur la **conductrice victime d'un refus de priorité**.

### C.4 — Page d'expertise + catégories Wix

- **Page d'expertise principale (CTA)** : [`/indemnisation-des-victimes/accidents-de-la-route`](https://www.jplouton-avocat.fr/indemnisation-des-victimes/accidents-de-la-route)
- **Page d'expertise secondaire** : [`/indemnisation-des-victimes/victimes-de-delits-ou-crimes`](https://www.jplouton-avocat.fr/indemnisation-des-victimes/victimes-de-delits-ou-crimes) (pour cas alcool/stup/délit de fuite/homicide involontaire — affaire Artan et Chaniers)
- **CTA final** : [`/honoraires-rendez-vous`](https://www.jplouton-avocat.fr/honoraires-rendez-vous)

#### Catégories Wix (2 IDs à associer au draft post)

| Catégorie Wix | ID |
|---|---|
| **Ressources et notions juridiques** (catégorie publication articles) | `9477320f-5902-40e9-ace3-b0e3b6b8b51f` |
| **Accidents de la route** (catégorie thématique) | `34cbb933-76d6-4a2e-8048-7624dcbe738d` |

### C.5 — Synthèse C — capital cabinet exploitable Article #6

| Type | Affaire | Montant | Lieu | Usage Article #6 |
|---|---|---|---|---|
| **TOP** | Artan tétraplégie Tizac-de-Curton (33) — **double sourcing post cabinet + presse Sud Ouest 29 sept 2015** | 2 M€ + 500k = **~2,5 M€** ; 75 % DFP | Gironde — Cenon résidence / TGI Nanterre 10 sept 2015 | Intro storytelling + section préjudices graves + CTA final + photo Me Plouton presse |
| **TOP** | Chaniers (17) 4 passagers décédés | **350 000 €** | Charente-Maritime / TC Saintes | Section décès / ayants droit + section pénal-civil |
| **FORT** | Angoisse mort imminente TJ Pau 2025 | 35 210 € (dont 20 000 € poste angoisse + 5 000 € préjudice d'attente) | Pyrénées-Atlantiques | Section postes Dintilhac + jurisprudence récente |
| **PILIER** | Article ressource Loi Badinter | — | — | Cross-link cluster x 2-3 |
| **CROSS-LINK ressources** (Nicolas 2026-05-17) | CIVI 2025, SARVI ou CIVI, Voyage organisé étranger, Auto-entrepreneur, Pretium doloris, Traumatisme crânien, Mis en cause (opt.) | — | — | 6-7 cross-links cluster ressources |
| **CROSS-LINK pipeline** | Article #1 moto + Article #4 vélo | — | — | 2 cross-links pipeline |
| **ÉCARTÉ** | Supporter nantais (défense pénale VTC) | — | — | Incompatible angle Article #6 |

---

## Bloc D — Statistiques officielles (passagers route)

### D.1 — ONISR Chiffres clés 2024 — France métropolitaine (publié 28 mai 2025, **définitifs**)

**Source primaire** : [ONISR — Chiffres clés 2024 définitifs (v4) — PDF publié 28 mai 2025](https://www.onisr.securite-routiere.gouv.fr/sites/default/files/2025-05/2025%2005%2028%20Chiffres%20cles%202024%20definitifs%20v4.pdf) + [Bilan définitif accidentalité routière 2024 (PDF)](https://www.onisr.securite-routiere.gouv.fr/sites/default/files/2025-06/2025%2005%2028_ONISR_Accidentalit%C3%A9_Bilan_d%C3%A9finitif_2024_v2.pdf) — lecture directe du document.

#### Mortalité globale 2024

| Indicateur | Valeur 2024 | Évolution vs 2023 |
|---|---|---|
| Personnes décédées | **3 193** | +26 (+0,8 %) |
| Personnes blessées (total) | 236 000 | +0,3 % |
| Personnes blessées gravement (AIS ≥ 3) | 16 000 | -0,1 % |

#### Répartition des tués 2024 par mode de déplacement

| Catégorie d'usager | Tués 2024 | Évolution vs 2023 | Blessés graves 2024 |
|---|---|---|---|
| **Occupants de voiture** (conducteurs + passagers VL) | **1 518** (48 % du total) | +6 | 4 800 (+1 %) |
| Usagers 2RM (moto/scooter/cyclo) | 720 (22 %) | +14 | 5 100 (-6 %) |
| Piétons | 456 (14 %) | +17 | 2 000 (-1 %) |
| Cyclistes | 224 (7 %) | +3 | 2 600 (+1 %) |
| EDPm (trottinettes électriques, gyropodes) | 45 (1,5 %) | +1 | **830 (+24 %)** |
| Voiturettes | 34 | — | — |
| Véhicules utilitaires (VU) | 120 | — | — |
| Poids lourds (PL) | 30 | — | — |
| **Bus et cars** | **7** | — | — |

**Lecture pivot Article #6** : **48 % des tués sur la route sont des occupants de voiture** (conducteurs + passagers cumulés). Le passager VL est donc statistiquement très exposé — pas un cas marginal.

#### Tués non responsables — part des passagers

Selon ONISR Bilan 2024 (camembert *« Tués non responsables »*) et synthèse [Bilan 2024 ONISR](https://www.onisr.securite-routiere.gouv.fr/en/road-safety-performance/annual-road-safety-reports/2024-road-safety-annual-report) :

> Parmi les personnes décédées **non responsables** de l'accident en 2024 : **26 % sont des piétons, 39 % sont des conducteurs de véhicule, et 36 % sont des passagers**.

**Lecture pivot Article #6** : **36 % des décédés non responsables sont des passagers** — c'est le chiffre hook absolu pour l'intro. Plus d'un tiers des morts non fautifs sur la route sont des personnes qui n'avaient pas les mains sur le volant. **Chiffre pivot de l'asymétrie** : ils ne sont pas conducteurs, ils n'ont rien fait de mal — et pourtant, ils sont morts en presque aussi grand nombre que les conducteurs non responsables.

#### Passager VT (voiture de tourisme) spécifiquement

Sur le camembert ONISR *« Tués non responsables »* (lecture directe page 2 du PDF chiffres clés 2024) :

- **VT passagers : ~26 %** des tués non responsables (= passagers de voiture)
- VT conducteurs : ~20 %
- 2RM conducteurs : ~6 %
- 2RM passagers : ~3 %
- VU-PL passagers : ~1 %
- Cyclistes : ~13 %
- Piétons : ~26 %
- EDPm : ~4 %
- Inconnu : ~9 %

**Croisement avec 1 518 occupants de voiture tués 2024** : ordre de grandeur de **400-500 passagers de voiture tués** sur l'année 2024 en France métropolitaine — chiffre pivot opérationnel.

#### Démographie des passagères / passagers

D'après le camembert ONISR *« VL passagers (distances parcourues) »* page 2 :

- Distances parcourues comme passager VL : **47 % hommes / 53 % femmes**
- Tués VL passagers : **71 % hommes / 29 % femmes** (ratio inversé partiellement — surmortalité masculine)

**Lecture éditoriale** : la passagère type est statistiquement une femme (distances parcourues), mais les tués passagers restent à 71 % des hommes (probablement liés à co-occurrence de prises de risque, hors agglomération, nuit). Permet de désamorcer la culpabilité de la persona femme accompagnant un conjoint conducteur (cas archétypal de l'article #6).

#### Usagers vulnérables (contexte cluster)

> Les usagers vulnérables non motorisés (piétons, cyclistes, EDPm) **et** les 2RM représentent **45 % des décès et 66 % des blessés graves** sur la route en 2024.

**Lecture éditoriale** : utile pour la transition cross-cluster avec articles #1 moto et #4 vélo (rappeler que le passager VT bénéficie du même régime art. 3 que ces usagers vulnérables non-conducteurs).

### D.1.bis — ONISR Bilan provisoire 2025 (publié 30 janvier 2026) — ajout Nicolas 2026-05-17

**Sources primaires** :
- [ONISR — Chiffres clés 2025 provisoires (v3 — PDF, 30 janv. 2026)](https://www.onisr.securite-routiere.gouv.fr/sites/default/files/2026-01/2026%2001%2030%20Chiffres%20cles%202025%20provisoires%20v3.pdf)
- [ONISR — Bilan provisoire 2025 (PDF complet, 30 janv. 2026)](https://www.onisr.securite-routiere.gouv.fr/sites/default/files/2026-01/20260130_Bilan%20provisoire%202025_ONISR.pdf)

**LEARN-020 strictement appliqué** : nous sommes mai 2026, donc entre fin janvier (sortie provisoires N-1) et fin mai (sortie définitifs N-1). **Mention « résultats provisoires » obligatoire** sur tout chiffre 2025 cité. Les définitifs 2025 ne sortiront que ~28 mai 2026 — après publication probable de l'article #6.

#### Mortalité globale 2025 (provisoires, France métropolitaine)

| Indicateur | Valeur 2025 (provisoire) | Évolution vs 2024 définitif |
|---|---|---|
| Personnes décédées | **3 260** (+67) | **+2,1 %** |
| Personnes blessées (total estimé) | 244 000 | +3,4 % |
| Personnes blessées gravement (AIS ≥ 3) | **16 600** | +4,0 % |

#### Répartition des tués 2025 par mode de déplacement

| Catégorie | Tués 2025 (provisoire) | Évolution vs 2024 |
|---|---|---|
| **Occupants de voiture de tourisme (VT)** | **1 563** | +45 (+3 %) |
| Usagers 2RM | 691 | -29 (-4 %) |
| Piétons | 501 | +45 (+10 %) |
| Cyclistes | 234 | +10 (+5 %) |
| EDPm (trottinettes électriques, gyropodes) | 80 | **+35 (+78 %)** |

**Lecture pivot Article #6** : **48 % des tués route 2025 sont des occupants de voiture** (stable vs 2024). 1 563 morts en voiture **dont 837 sans tiers impliqué** — voir matrice ci-dessous.

#### 🎯 Matrice de collision (page 15 du bilan ONISR 2025) — chiffre pivot exclusif

Sur les 1 563 occupants de voiture (VT) tués en 2025 :
- **837 sont décédés dans un accident SANS TIERS impliqué** (53,5 % — perte de contrôle, sortie de route, choc isolé contre un arbre ou un obstacle fixe)
- 386 tués dans un choc contre une autre VT
- 314 tués dans un choc contre un PL/VU
- 22 tués dans un choc contre un 2RM, EDPm, vélo, piéton, autre
- 4 tués dans un choc contre piéton/cycliste/EDPm

**Lecture pivot ÉNORME pour Article #6** : **plus d'1 occupant de voiture sur 2 meurt dans un accident sans autre véhicule impliqué**. Si le passager était dans cette voiture, **il n'y a pas de « tiers responsable » à actionner — seul le conducteur (souvent un proche du passager) a perdu le contrôle**. C'est EXACTEMENT le scénario où le pivot art. 3 vs art. 4 prend tout son sens : le conducteur peut voir son indemnisation réduite par sa propre faute (art. 4), mais le passager reste intégralement indemnisé (art. 3) par l'assureur du même véhicule. **Argument-massue pour l'intro et le H2 1.**

**Citation institutionnelle ONISR verbatim** (page 14 bilan 2025) :
> « En 2025, les occupants de véhicule de tourisme représentent 48 % des décès sur la route ; la part des usagers vulnérables atteint 46 %. […] Les occupants de véhicule de tourisme (VT) représentent désormais moins de la moitié des personnes tuées (48 %). »

Et page 15 :
> « 42 % des décès le sont dans des accidents sans tiers impliqué (sans antagoniste) : 40 % des cyclistes, 42 % des 2RM, **54 % des occupants de VT décèdent dans un accident sans antagoniste.** »

#### Données passager 2RM (page 17 — chiffre rare exploitable)

> « En 2025, 93 % des tués en 2RM (642) sont des hommes. **Parmi les femmes tuées en 2RM, la quasi-totalité l'étaient en motocyclette et près d'une sur trois était passagère.** »

**Lecture Article #6** : à mobiliser dans la section H3 2.1 (passager moto) — illustre que le passager 2RM existe statistiquement et est très exposé (notamment côté femmes).

#### Note méthodo cross-bilan 2024/2025 (LEARN-020)

| Période | Donnée disponible | Statut |
|---|---|---|
| 2024 | Définitifs (publiés 28 mai 2025) | ✅ Solides — utilisables pour chiffres détaillés (% passagers parmi tués non responsables = 36 %, breakdown précis camemberts) |
| 2025 | **Provisoires** (publiés 30 janvier 2026) | ⚠️ Mention « provisoires » obligatoire — utilisables pour les chiffres globaux frais (3 260 tués, 1 563 occupants VT, matrice de collision 54 % sans tiers) |
| 2025 définitifs | À paraître ~28 mai 2026 | ⏳ Si on publie après le 28 mai 2026, on pourra basculer sur les définitifs 2025 |

#### Stratégie Article #6 — quels chiffres utiliser

1. **Chiffre hook intro 2025 fraîcheur** : *« En 2025, 1 563 occupants de voiture sont morts sur les routes de France (résultats provisoires ONISR). »*
2. **Argument-massue post-hook (matrice 2025)** : *« Plus frappant encore : 54 % d'entre eux sont décédés dans des accidents sans tiers impliqué — sortie de route, perte de contrôle. Si vous étiez passager, c'est précisément la situation où la loi vous protège le plus. »*
3. **Chiffre pivot asymétrie (2024 définitif)** : *« Et parmi les décédés non responsables de l'accident en 2024 — dernier chiffre définitif disponible — 36 % étaient des passagers. »* — basculer sur 2025 définitif si publication post-28 mai.
4. **Chiffre 2RM passagères** : *« Près d'une femme tuée en motocyclette sur trois était passagère »* (ONISR 2025 provisoire) — section passager 2RM.

### D.2 — Citation ONISR exploitable verbatim (encadré chiffré intro)

> « En 2024, 1 518 occupants de voiture sont décédés sur les routes de France métropolitaine. **Parmi les personnes décédées non responsables de l'accident, 36 % sont des passagers** — autrement dit plus d'un tiers des morts non fautifs sur la route n'avaient pas les mains sur le volant. »
> *Source : [ONISR — Chiffres clés 2024 définitifs](https://www.onisr.securite-routiere.gouv.fr/sites/default/files/2025-05/2025%2005%2028%20Chiffres%20cles%202024%20definitifs%20v4.pdf), publié 28 mai 2025.*

### D.3 — Données complémentaires (à mobiliser si besoin)

- **Évolution mortalité 1924-2024** : courbe ONISR — pic 18 034 décès en 1972, **3 193 en 2024** (-82 %).
- **Réseaux routiers** : 60 % des tués sur routes hors agglomération (1 924), 32 % en agglomération (1 030), 8 % sur autoroutes (239).
- **Causes principales (présumés responsables en voiture)** : vitesse 35 % (hommes) / 19 % (femmes) ; alcool 28 % / 12 % ; inattention 16 % / 9 % ; stupéfiants 15 % / 7 %.

### D.4 — BAAC Nouvelle-Aquitaine (ancrage local LEARN-042)

**À sonder en complément si Étape 3 valide la pertinence** : [Base de Données Annuelles des Accidents Corporels (BAAC) sur data.gouv.fr](https://www.data.gouv.fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2024/) — extraction filtrée Gironde + Nouvelle-Aquitaine 2024 pour citer un chiffre régional « passager NA tués 2024 ». L'ancrage Bordeaux (LEARN-042) est plus impactant SEO que volume + signal local.

**Note méthodo (LEARN-020)** : nous sommes au **17 mai 2026** → bilan 2025 ONISR encore **provisoire** (sortie attendue fin mai 2026 ; provisoires N-1 disponibles fin janvier). On reste sur les **définitifs 2024** pour rigueur sourçage.

### D.5 — Référentiels non exploités cette fois (réserve)

- **Sécurité Routière** : campagnes ceinture passager arrière (signal social mais pas de chiffre primaire propre).
- **INSEE** : pas d'apport spécifique passager (général route déjà couvert ONISR).
- **DSED Ministère Justice** : contentieux indemnisation accidents — pertinent si on veut chiffrer le nombre d'affaires civiles annuelles. Pas mobilisé tant que pas indispensable au gap.
- **FGAO — rapport annuel** : pour chiffrer la part des accidents passagers indemnisés via FGAO (véhicules non assurés). À sonder en Étape 3 si on développe la section FGAO.

---

## 🛑 Synthèse Étape 2 — récap pour validation Nicolas

### Statut des 4 blocs

| Bloc | Statut | Saillant |
|---|---|---|
| **B — SEO DataForSEO** | ✅ | Univers passager direct ≤ 150/mois adressable ; **univers amont cluster `indemnisation accident de la route` 720/mois** + 4-5 satellites 100-170/mois ; SERP top 10 = 6 cabinets / 2 assureurs / 1 institutionnel ; **featured snippet capturable** ; 6 PAA exploitables (dont 4 réponses actuellement en anglais) ; 8 axes Information Gain ; trend saisonnier favorable mai-juin |
| **A — Matière juridique** | ✅ | Art. 3 + art. 4 + art. 1 Badinter verbatim Légifrance ; **Cass. AP 10 nov. 1995 n° 94-13.912** (faute inexcusable — 4 critères) ; **Cass. Civ. 2ᵉ 30 mars 2023 n° 21-17.466** (recours assureur exclu — correction du n° de pourvoi mémorisé au cadrage) ; L. 211-9 délais 8 mois ; L. 421-1 FGAO ; cartographie 9 scénarios assureur compétent |
| **C — Interne Plouton** | ✅ | **2 affaires pivot ALIGNÉES** (Artan 2,5 M€ Tizac-de-Curton 33 = passager arrière + Chaniers 350k€ = 4 passagers décédés Charente-Maritime) ; **1 affaire complémentaire FORT** (TJ Pau 2025 préjudice angoisse mort imminente) ; pilier Badinter en cross-link prioritaire ; **1 affaire ÉCARTÉE** (supporter nantais = défense pénale VTC, dissonance frontale) ; cross-links cluster #1 moto + #4 vélo + 4-5 articles ressources ; IDs catégories Wix prêts |
| **D — Stats ONISR** | ✅ | **3 193 tués route France 2024** définitifs ; **1 518 occupants de voiture tués** (48 % du total) ; **36 % des tués non responsables sont des passagers** = chiffre hook intro ; **45 % des décès = usagers vulnérables** ; femmes parcourent 53 % des km en VL-passager mais 29 % des décès passagers VL (surmortalité masculine) ; citation institutionnelle verbatim prête |

### Hypothèses Étape 1 — statut

| Hypothèse | Statut |
|---|---|
| Pivot H1 « asymétrie art. 3 vs art. 4 » | ✅ **Confirmée** par texte verbatim + AP 1995 + asymétrie chiffrée ONISR (36 % tués non responsables = passagers) |
| Volume head term direct ≥ 200/mois | ❌ **Infirmée** — head term passager direct ≤ 70/mois (équivalent #4 vélo). **Stratégie pivot validée** : capture via cluster amont 720/mois |
| Présence PAA exploitables | ✅ **Confirmée** — 6 PAA exploitables, dont 4 réponses anglaises (gap français à occuper) |
| Cass. Civ. 2ᵉ 30 mars 2023 sur faute passager | ⚠️ **Précisée** : le n° est **21-17.466** (pas 21-22.866 cité au cadrage). L'arrêt traite du **recours assureur exclu contre passager fautif**, utile pour PAA #6 (« passager fauteur »). Pour la règle « faute passager non opposable », fondement = art. 3 + Cass. AP 1995 verbatim |
| ONISR provisoires/définitifs | ✅ **Définitifs 2024** disponibles (publiés 28 mai 2025) — bilan 2025 encore provisoire (sortie fin mai 2026) — on reste sur définitifs 2024 |
| Cabinet pilier Badinter à jour | ✅ **Confirmé** — article complet 2025 |

### Arbitrages — synthèse finale post-validation Nicolas 2026-05-17

| # | Sujet | Décision finale |
|---|---|---|
| 1 | Affaire supporter nantais | ✅ **Écartée** (Nicolas : « rien à voir, n'intègre pas ») |
| 2 | Affaire TJ Pau 2025 préjudice angoisse mort imminente | ✅ Conservée, usage indirect section postes Dintilhac |
| 3 | Affaire libournais 200k€ | ❌ **Hors-cible** — Madame D. est conductrice (au volant ceinturée), pas passagère. Non utilisée Article #6. Garder pour futur cluster |
| 4 | Section transport collectif (car, bus TBM, BlaBlaCar) | ✅ **H3 dédié** |
| 5 | Section VTC/Uber/taxi | ✅ **H3 dédié** |
| 6 | Encadré fourchette indemnitaire | ✅ Validé — 35k → 350k → 2,5M (cadre propriétaire LEARN-048) |
| 7 | **Citation Artan** | ✅ **Anonymisation Nicolas** : « notre client », « Monsieur A » (pas « Artan ») |
| 8 | **Affaire passager VTC/Uber/taxi privée** | ❌ Pas d'affaire cabinet disponible — on s'appuie sur cadre juridique pur + doctrine (assurance pro VTC, Convention Bruxelles transport, etc.) |
| 9 | **Cluster ressources** (Nicolas a pointé feed catégorie) | ✅ **6-7 cross-links** : CIVI, SARVI ou CIVI guide, Voyage organisé étranger, Auto-entrepreneur, Pretium doloris, Traumatisme crânien + Mis en cause (opt.) |

### Si validation Nicolas → ce que je fais à l'Étape 3

1. H1 final + 3 variantes (pivot art. 3 vs 4 — clause de bon sens LEARN-053 si pas de pivot authentique sur les 3 variantes)
2. Méta-title ≤ 60 + méta-description ≤ 155 + slug sans accent (LEARN-001)
3. Plan H2/H3 détaillé avec objectif/contenu/longueur/justification/sources par section
4. Cartographie multi-modale en H2 (voiture/moto/VTC/taxi/car/covoiturage/non assuré FGAO)
5. Section décès / ayants droit en H2 (Chaniers + jurisprudence Pau)
6. Section postes de préjudice Dintilhac avec fourchette chiffrée (35k → 350k → 2,5M)
7. FAQ 8-10 questions (mix 6 PAA capturées + 2-4 gap éditorial)
8. Stratégie cross-links (cluster #1 moto + #4 vélo + pilier Badinter + 3-4 affaires + 4 ressources cabinet)
9. JSON-LD FAQPage à livrer en chat (LEARN-041 + LEARN-027) — Étape 4

🛑 **STOP** — j'attends ton « OK go Étape 3 » final (tous les arbitrages sont posés ; rien d'ouvert).
