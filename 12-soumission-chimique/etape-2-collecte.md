# Collecte — Soumission chimique (#12)

> Notes brutes, 4 blocs. **Pas encore de rédaction.** Ordre d'attaque : B → A → C → D (LEARN-018).
> Collecte du 2026-08-07. Tout ce qui n'est pas sourcé ici porte un ⚠️ et **ne doit pas être écrit** avant résolution.

---

# Bloc B — Données SEO

## SERP top 10 (`soumission chimique`, France, desktop, 2026-08-07)

| # | Domaine | Nature |
|---|---|---|
| 1 | arretonslesviolences.gouv.fr | institutionnel (État) |
| 2 | fr.wikipedia.org | encyclopédique |
| 3 | addictovigilance.fr | scientifique (réseau addictovigilance) |
| 4 | unistra.fr | université |
| 5 | lecrafs.com | santé publique (Centre de Référence sur les Agressions Facilitées par les Substances) |
| 6 | ameli.fr | assurance maladie |
| 7 | mendorspas.org | associatif |
| 8 | vih.org | santé |
| 9 | drogues-info-service.fr | santé publique (PDF) |

**Gap analysis — le résultat le plus net du pipeline à ce jour.**
Le top 10 est **intégralement sanitaire, scientifique ou associatif**. **Zéro avocat, zéro cabinet, zéro contenu juridique.** Aucune page ne traite : la qualification pénale des faits, la nouvelle définition du consentement, la prescription, ni **l'indemnisation**. Le sujet est traité comme une question de santé publique — jamais comme une question de droits.

→ Ce n'est pas l'« angle mort partiel » de LEARN-059 (avocats présents mais sans l'angle victime) : c'est un **angle mort total**. À verser au journal comme cas-limite.

## AI Overview — et son retard d'une réforme

Google affiche une AI Overview complète (définition, effets, que faire) qui conseille : *« Porter plainte immédiatement dans un commissariat ou une gendarmerie (éviter la simple main courante) pour accéder aux unités médico-judiciaires et aux analyses toxicologiques gratuites. »*

**C'est précisément ce que le décret du 11 décembre 2025 a découplé** : dans les trois territoires de l'expérimentation, les analyses sont prescrites par tout médecin et prises en charge **sans plainte préalable**. La réponse dominante du SERP est donc en retard d'une réforme — et incomplète partout ailleurs, puisqu'elle ignore le différentiel territorial.

**Sources citées par l'AI Overview** (donc pages « citables » à concurrencer) : arretonslesviolences.gouv.fr, Wikipédia, ameli.fr, mendorspas.org, sante.gouv.fr, drogues-info-service.fr.

## People Also Ask

- Qu'est-ce que la soumission chimique sexuelle ?
- Comment détecter la soumission chimique ?
- Qu'est-ce que le protocole de soumission chimique ?
- Soumission chimique prise en charge ?
- Quels sont les signes d'un traumatisme sexuel ?
- Combien de temps les stupéfiants restent-ils dans le sang ?

## Related searches

`Soumission chimique kit` · `pharmacie` · `association` · `test` · `livre` · `chiffres` · `ANSM` · `SOS soumission chimique`

**Lecture** : la demande réelle est massivement **pratique et pré-juridique** (kit, test, pharmacie, détection, délais). Personne ne cherche « avocat » — mais tout le monde cherche ce qui, en droit, conditionne la preuve. C'est l'espace de l'article : **partir de la question pratique, atterrir sur le droit.**

⚠️ **À exploiter, signalé par sante.gouv.fr dans l'AI Overview** : *« Aucun dispositif autonome ne permet de détecter une substance nuisible… Inutiles et dangereux »*. Les requêtes `kit` / `pharmacie` / `test` cherchent donc un produit que l'État déconseille. Répondre franchement à ça rend un vrai service et occupe une question à fort volume. **Vérifier la formulation exacte sur sante.gouv.fr avant de la reprendre.**

## Volumes (rappel Étape 1)

`soumission chimique` 2 400/mo (index 2) · `drogue du violeur` 2 900/mo · `gbl drogue` 720/mo · `test soumission chimique` 40 · long-tail procédurale : aucune donnée Ads.

---

# Bloc A — Matière juridique

> Méthode : `scripts/legifrance.py` (API PISTE) + WebSearch ciblée legifrance.gouv.fr. **Version en vigueur contrôlée par les dates `dateDebut`/`dateFin`, pas par le libellé de statut** (cf. §Alerte outillage en fin de bloc).

## A1. L'infraction spécifique — art. 222-30-1 CP ✅ vérifié

**Statut : VIGUEUR, version du 2018-08-06** (`LEGIARTI000037287345`). Texte intégral :

> « Le fait d'administrer à une personne, à son insu, une substance de nature à altérer son discernement ou le contrôle de ses actes afin de commettre à son égard un viol ou une agression sexuelle est puni de cinq ans d'emprisonnement et de 75 000 € d'amende. Lorsque les faits sont commis sur un mineur de quinze ans ou une personne particulièrement vulnérable, les peines sont portées à sept ans d'emprisonnement et à 100 000 € d'amende. »

**Point capital pour l'article** : l'infraction est **autonome** et **formelle** — elle vise l'administration *« afin de commettre »*. Elle est donc constituée **même si le viol ou l'agression n'a pas été commis, ou n'a pas pu être prouvé**. C'est la réponse juridique directe à « je ne me souviens de rien » : le fait d'avoir été droguée est, en soi, une infraction poursuivable.
*C'est le cœur pédagogique de l'article.*

## A2. La nouvelle définition du consentement — art. 222-22 CP ✅ vérifié

**Loi n° 2025-1057 du 6 novembre 2025** modifiant la définition pénale du viol et des agressions sexuelles (JO du 7 novembre 2025).
**Version en vigueur depuis le 2025-11-08** (`LEGIARTI000052535583`, `dateDebut` 2025-11-08 → `dateFin` 2029-01-01). Texte :

> « Constitue une agression sexuelle tout acte sexuel non consenti commis sur la personne d'autrui ou sur la personne de l'auteur ou, dans les cas prévus par la loi, commis sur un mineur par un majeur. **Au sens de la présente section, le consentement est libre et éclairé, spécifique, préalable et révocable. Il est apprécié au regard des circonstances. Il ne peut être déduit du seul silence ou de la seule absence de réaction de la victime.** Il n'y a pas de consentement si l'acte à caractère sexuel est commis avec violence, contrainte, menace ou surprise, quelle que soit leur nature. […] »

## A3. Le viol — art. 222-23 CP ✅ vérifié (et la nuance que personne ne restitue)

**Version en vigueur depuis le 2025-11-08** :

> « Tout acte de pénétration sexuelle, de quelque nature qu'il soit, ou tout acte bucco-génital **ou bucco-anal** commis sur la personne d'autrui ou sur la personne de l'auteur **par violence, contrainte, menace ou surprise** est un viol. Le viol est puni de quinze ans de réclusion criminelle. »

**⚠️ Nuance à traiter avec précision — c'est là que le contenu grand public se trompe.** L'article 222-23 **n'a pas été réécrit en « acte non consenti »** : la loi de 2025 n'y a inséré que « ou bucco-anal ». C'est l'**article 222-22 qui porte la définition du consentement « au sens de la présente section »** — donc applicable au viol, qui appartient à cette section. Le basculement vers le consentement opère par le chapeau de section, pas par la définition du viol elle-même.

→ **Ne jamais écrire « le viol est désormais défini comme un acte non consenti » sans cette articulation.** Excellente question de FAQ (nuance juridique, LEARN-045 anti-AI Overviews).

## A4. L'administration de substances nuisibles — art. 222-15 CP ✅ vérifié

**Statut : VIGUEUR depuis le 2007-03-07.**

> « L'administration de substances nuisibles ayant porté atteinte à l'intégrité physique ou psychique d'autrui est punie des peines mentionnées aux articles 222-7 à 222-14-1 suivant les distinctions prévues par ces articles. […] »

**Intérêt** : qualification de repli quand l'intention sexuelle n'est pas établie. Les peines sont **calquées sur l'atteinte causée** — donc sur l'**ITT**. → passerelle naturelle vers notre notion publiée `itt-pénale-définition-en-2025`.
⚠️ Le renvoi en cascade (222-7 à 222-14-1) doit être **vulgarisé sans être faussé** : ne pas annoncer un quantum unique.

## A5. Le dispositif de détection — décret et arrêté du 11 décembre 2025 ✅ vérifié

- **Base légale** : article 68 de la **LFSS 2025** (loi n° 2025-199 du 28 février 2025) — expérimentation de **3 ans**.
- **Décret n° 2025-1208 du 11 décembre 2025** : dans les territoires fixés par arrêté, **toute personne qui s'estime victime** d'un état de soumission chimique **ou qui en présente des signes cliniques** peut se voir prescrire **par tout médecin** les examens de biologie médicale de détection. **Prise en charge intégrale par l'assurance maladie, sans dépôt de plainte.**
- **Arrêté du 11 décembre 2025** — **liste des territoires : Hauts-de-France, Île-de-France, Pays de la Loire.** Trois régions, pas une de plus.
- **Laboratoires spécialisés désignés** : CHU de Lille (pôle biologie pathologie génétique, service de toxicologie et génopathies) ; CHU de Nantes (laboratoire de pharmacologie-toxicologie) ; CHU Raymond Poincaré à Garches, AP-HP (laboratoire de pharmacologie-toxicologie).
- **Délais de rendu des résultats** : **28 jours** pour sang et urine, **6 semaines** pour les cheveux.
- Le décret prévoit un **« parcours patient »** permettant de déposer plainte en cas de résultat positif.

> **🎯 PIVOT LOCAL CONFIRMÉ SUR SOURCE PRIMAIRE.** La **Nouvelle-Aquitaine n'est pas dans l'expérimentation.** La mesure annoncée par toute la presse nationale en janvier 2026 **ne s'applique pas à Bordeaux**. Une victime girondine ne peut pas se présenter chez son médecin pour obtenir des analyses remboursées hors plainte : elle reste sur la voie classique (plainte → réquisition judiciaire → UMJ). **C'est l'Information Gain n°1 de l'article, et il est invisible dans 100 % du contenu national.**

⚠️ **Guadeloupe** : annoncée comme extension à venir dans les communications d'ARS, **absente de l'arrêté du 11 décembre 2025**. Ne pas l'écrire comme acquise. **Point de surveillance au refresh M+6.**
⚠️ **À finaliser avant rédaction** : la voie alternative hors territoires expérimentaux (fondement de la réquisition judiciaire, rôle de l'UMJ, prise en charge des frais). C'est la partie la plus utile de l'article pour un lecteur bordelais — elle doit être exacte.

## A6. Prescription ⚠️ à confirmer

- Recodification : une **ordonnance du 19 novembre 2025 recodifie le code de procédure pénale au 1ᵉʳ janvier 2029** (nouvelle numérotation `L1213-…`). Sans effet sur le droit applicable aujourd'hui, mais **explique les statuts `ABROGE_DIFF` / `VIGUEUR_DIFF` datés du 2029-01-01** rencontrés sur plusieurs articles.
- **Confirmé** : viol sur mineur = **30 ans à compter de la majorité** (art. 7 CPP), avec mécanisme de prorogation en cas de nouvelle infraction sur un autre mineur par le même auteur.
- ⚠️ **À confirmer avant rédaction** : viol sur majeur (**20 ans ?**), agression sexuelle (**6 ans ?**), délit de l'art. 222-30-1 (**6 ans ?**), et le point de départ. **Ne rien affirmer sans vérification** — c'est une donnée que le lecteur peut utiliser pour décider d'agir ou non.

## A7. CIVI ⚠️ à confirmer

- **Fondement** : art. **706-3 CPP** (cité dans le post-preuve du cabinet). ⚠️ Vérifier conditions d'éligibilité, délais de saisine, et l'articulation avec le **FGTI**.
- **Principe acquis (source cabinet)** : la CIVI n'est **pas tenue** par les sommes allouées par la juridiction pénale et peut allouer davantage.

## ⚠️ Alerte outillage — LEARN-068 mis à l'épreuve (à verser au journal)

Premier usage réel de l'API Légifrance réactivée. Trois constats :

1. **Faux positif « PAS EN VIGUEUR »** — `legifrance.py code "Code pénal" "222-22"` a rendu la bonne version en l'étiquetant `⚠️ PAS EN VIGUEUR`. Le script ne reconnaît que le libellé `VIGUEUR` ; or la version applicable portait `ABROGE_DIFF` (= abrogation programmée au 2029-01-01) avec `dateDebut` 2025-11-08 ≤ aujourd'hui < `dateFin`. **Un rédacteur pressé aurait écarté le texte en vigueur.**
2. **Faux négatifs** — `222-24`, `222-30` : 3 versions remontées, aucune en vigueur. Jeu de versions incomplet.
3. **Codes et numéros courts non résolus** — `code de procédure pénale` art. `7` et `8` : 0 version.

**Correctif à proposer** (hors périmètre de cet article, décision Nicolas) : sélectionner la version par comparaison `dateDebut ≤ aujourd'hui < dateFin` plutôt que par égalité de chaîne sur `VIGUEUR`, et signaler les jeux de versions incomplets.

---

# Bloc C — Contexte interne Plouton

## Cannibalisation

Inventaire catégorie *Ressources et notions juridiques* du 2026-08-07 : **61 posts**, **aucune notion** sur les violences sexuelles. Détail en [`etape-1-cadrage.md`](etape-1-cadrage.md).

## Posts-preuve — contenus lus (LEARN-063), chiffres fondés

### 1. CIVI Tarbes — indemnisation malgré le suicide de l'auteur (2025-11-17)
`/post/cabinet-plouton-indemnisation-victime-viol-civi-tarbes`

Faits établis par le post : viols commis en **2017** sur **Madame D., 17 ans**, par son responsable hiérarchique dans un supermarché des **Hautes-Pyrénées**. Sidération psychologique, silence pendant des années. **Octobre 2022** : révélation au détour d'une consultation médicale ; le médecin alerte la gendarmerie. **20 mars 2023** : l'auteur se suicide avant son placement en garde à vue — le dossier pénal s'éteint. **Mars 2024** : le cabinet saisit la **CIVI du tribunal judiciaire de Tarbes**.

> ⚠️ **Précision impérative** : la **provision de 10 000 € est obtenue** ; les **~70 000 €** de dommages et intérêts sont **sollicités**, pas acquis. **Ne jamais écrire « le cabinet a obtenu 70 000 € ».** (Sans lecture du `CONTENT_TEXT`, l'erreur était mécanique — LEARN-063 démontré une fois de plus.)

**Pourquoi ce dossier est le bon** : ce n'est pas une soumission chimique, mais la **structure est identique** — parole empêchée, révélation tardive, procès pénal impossible, et réparation quand même. C'est la réponse vécue à la peur n°1 du lecteur.

### 2. CIVI — plus de 130 000 € (2022-03-31)
`/post/victimes-de-viol-incestueux-et-d-agression-sexuelle-le-cabinet-obtient-devant-la-civi-plus-de-130`

Faits établis : viols incestueux et agressions sexuelles commis **entre 2011 et 2013** sur **Z. et T., 11 et 9 ans**, par le grand-père paternel. **Arrêt de la cour d'assises de la Gironde du 7 juin 2019** : 12 ans de réclusion criminelle + suivi socio-judiciaire 5 ans ; **95 000 €** alloués sur intérêts civils. Somme **irrécouvrable** (condamné très âgé, incarcéré). Saisine de la CIVI sur le fondement de l'art. **706-3 CPP** → **plus de 130 000 €** obtenus.

> **Donnée en or, propriétaire et chiffrée** : **95 000 € aux assises → plus de 130 000 € en CIVI.** Démonstration concrète que la CIVI n'est pas tenue par le quantum pénal. Aucun concurrent du top 10 ne peut produire ça.

## Maillage retenu (tous 200, vérifiés le 2026-08-07)

**Money pages** : `/indemnisation-des-victimes/victimes-de-delits-ou-crimes` (principale) · `/defense-penale/violences-conjugales-et-feminicides` (volet conjugal) · `/honoraires-rendez-vous` (CTA).

**Notion↔notion** : `indemnisation-civi-2025-guide-complet-pour-les-victimes-d-infractions` · `sarvi-ou-civi-indemnisation-victimes` · `dépôt-de-plainte-en-france-comment-porter-plainte-efficacement` · `itt-pénale-définition-en-2025` (passerelle A4) · `comment-bien-préparer-mon-dossier-médical`.

**Preuve E-E-A-T** : les deux posts CIVI ci-dessus (lien obligatoire) · `défense-d-une-victime-de-viol-conjugal-devant-la-cour-criminelle-départementale-de-la-seine-maritime` · `défense-d-une-jeune-femme-victime-de-viol-en-réunion` · `proposition-de-loi-inceste-et-imprescriptibilité-le-cabinet-plouton-au-cœur-des-avancées-législati` (autorité législative).

**Écartés** : `acquittement-par-la-cour-d-assises-d-appel` (angle défense) · `contamination-par-le-vih-…-substances-nuisibles` (décision Nicolas 2026-08-07, contexte factuel trop éloigné).

⚠️ **Reprise presse ELLE** (`intervention-de-maître-plouton-dans-l-enquête-elle-sur-l-inceste…`) : **non vérifiée**. LEARN-056 — ne pas revendiquer avant d'avoir confirmé titre, média, date et URL vivante.

---

# Bloc D — Données statistiques

## Ampleur du phénomène — enquête nationale ANSM

Surveillance prospective annuelle du réseau national d'**Addictovigilance**, sous tutelle **ANSM**, pilotée par le **Centre d'Addictovigilance de Paris**.

- **Millésime 2022** (rapport ANSM) : **2 197 déclarations** enregistrées → après évaluation, **1 229 agressions facilitées par des substances** retenues, soit **+69,1 %** par rapport à 2021.
- **Calendrier de publication** : résultats 2023 publiés le **24 novembre 2025** ; résultats **2024 publiés le 10 juillet 2026**.

> ⚠️ **Action obligatoire avant rédaction (LEARN-061)** : extraire les chiffres du **rapport 2024** (le plus récent, publié il y a moins d'un mois) depuis le PDF ANSM, pas depuis une page HTML de synthèse. Citer millésime + URL primaire. Point d'entrée : [ANSM — Résultats d'enquêtes pharmacodépendance-addictovigilance](https://ansm.sante.fr/page/resultats-denquetes-pharmacodependance-addictovigilance).

## Le fait qui contredit l'imaginaire collectif

Les enquêtes nationales successives confirment la **place prépondérante des médicaments psychoactifs sédatifs** — benzodiazépines, antihistaminiques H1, opioïdes, neuroleptiques — et **non du GHB**.

> **Information Gain éditorial** : 2 900 personnes par mois cherchent « drogue du violeur », expression qui désigne dans l'imaginaire le GHB. La réalité documentée est celle de l'armoire à pharmacie. Ce correctif relie nos deux head terms et **change la conduite pratique du lecteur** (quoi faire doser, et pourquoi un « kit » de détection ne sert à rien).
> ⚠️ Formulation exacte et hiérarchie des substances à sourcer sur le rapport 2024 avant rédaction.

## Fenêtres de détection ⚠️ à sourcer

Le décret donne des **délais de rendu** (28 jours sang/urine, 6 semaines cheveux) — **à ne pas confondre avec les fenêtres de détection**, qui sont la donnée utile au lecteur pressé.
L'AI Overview avance « moins de 48 heures dans le sang ou les urines » (source Drogues Info Service). ⚠️ **À sourcer sur un référentiel médico-légal** (CRAFS, SFTA, ANSM) avant toute reprise. L'analyse **capillaire segmentaire**, elle, ouvre une fenêtre de plusieurs semaines à plusieurs mois — c'est **la clé du volet soumission chimique conjugale**. À documenter précisément.

## Ancrage local ⚠️ à chercher

Recherche à mener : signalements ou dispositifs en **Gironde / Nouvelle-Aquitaine** (CHU de Bordeaux, UMJ, centre d'addictovigilance de Bordeaux). Objectif : trois mentions locales minimum (LEARN-042) et un ancrage concret du pivot territorial.

---

# 🛑 STOP — Validation demandée avant Étape 3

**Ce qui est acquis** : le sujet est un angle mort juridique total sur un head term à 2 400/mo quasi sans concurrence ; trois piliers d'Information Gain vérifiés (infraction autonome 222-30-1 · pivot territorial Nouvelle-Aquitaine · 95 000 € → 130 000 € en CIVI) ; matière juridique fondée sur source primaire.

**Ce qui reste à sécuriser avant l'Étape 4** (je m'en charge, mais je préfère que tu saches où sont les trous) : chiffres ANSM 2024, prescription exacte, art. 706-3 CPP, aggravations 222-24/222-30, fenêtres de détection, voie alternative hors régions expérimentales.

**Trois questions :**

1. **Angle confirmé ?** Le fil directeur que je propose : *« vous ne vous souvenez de rien — et le droit, lui, prévoit exactement cette situation »*, avec l'infraction autonome de l'art. 222-30-1 comme colonne vertébrale et l'indemnisation comme issue même sans procès. OK ?
2. **Pivot territorial** : je l'assume franchement (« cette mesure ne s'applique pas encore chez nous, voici ce que ça change ») ? C'est différenciant et honnête, mais ça revient à annoncer une moins-bonne nouvelle aux lecteurs girondins. Ton arbitrage.
3. **Alerte outillage** : je documente le correctif `legifrance.py` dans LEARNINGS et **je n'y touche pas** pendant l'article (règle « maintenance outil ≠ rédaction »), ou tu préfères que je corrige la sélection de version tout de suite, avant de m'appuyer davantage dessus en Étape 4 ?

Sur ton « OK go » → **Étape 3 (plan)** : H1 + 3 variantes, méta-tags, plan H2/H3 justifié sommant à 2 000-2 500 mots, stratégie de liens et stratégie GEO avec FAQ 8-10.
