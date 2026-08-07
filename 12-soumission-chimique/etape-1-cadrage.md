# Cadrage — Soumission chimique (#12)

> Sujet fourni par Nicolas le 2026-08-07 : *« Soumission chimique : ce que la loi permet quand la victime ne se souvient de rien »*.
> Contexte de production : **régulière** (1 des 4 du mois) → workflow 4 étapes classique avec STOP.
> Ce livrable cadre l'angle, tranche l'arbitrage de persona, vérifie la cannibalisation et le maillage, et liste les affirmations juridiques à fact-checker en Étape 2. **Rien de juridique n'est affirmé ici sans marqueur de vérification.**

---

## Origine du sujet & signal de départ

- **Sujet imposé par brief** (pas issu du CSV des prises de contact — cf. LEARN-066, non applicable ici).
- **Timing exceptionnel** : le droit applicable a bougé **deux fois en cinq semaines**, et les deux fois précisément sur la situation du titre (« la victime ne se souvient de rien ») :
  1. **Loi publiée au JO du 7 novembre 2025** — le **non-consentement** entre dans la définition pénale du viol et des agressions sexuelles (art. 222-22 CP réécrit). ⚠️ *Numéro de loi et rédaction exacte à confirmer sur Légifrance en Étape 2.*
  2. **Décret du 11 décembre 2025**, en vigueur au **1ᵉʳ janvier 2026** — remboursement par l'Assurance maladie des analyses toxicologiques de détection d'une soumission chimique **sans dépôt de plainte préalable** (expérimentation 3 ans issue de la LFSS 2025). ⚠️ *Numéro de décret, base légale et périmètre à confirmer en Étape 2.*
- **Conséquence éditoriale** : quasiment tout le contenu en ligne antérieur à 2026 est **périmé sur les deux points qui comptent le plus**. C'est la fenêtre de fraîcheur qui justifie l'article maintenant.

## Intention de recherche

- **Type** : **informationnelle dominante** avec un versant **urgence-action** rare dans notre pipeline. Une partie du trafic cherche *quoi faire dans les heures qui suivent* (fenêtres de détection sang/urine/cheveux), pas seulement « c'est quoi ».
- **Second versant, transactionnel** : « et si l'auteur n'est jamais identifié / jamais condamné, ai-je quand même droit à quelque chose ? » → terrain CIVI, cœur de métier du cabinet.
- **Profil de SERP attendu** : hypothèse d'**angle mort avocat** (LEARN-059) — un `competition_index` de **2** sur 2 400 recherches/mois signale que personne n'achète ce terrain, ce qui accompagne souvent une SERP tenue par le sanitaire (ARS, ameli, CRAFS, presse) plutôt que par le juridique. **À confirmer sur le top 10 en Bloc B** — c'est la vérification qui décide de l'angle.

## Requête principale (head term)

`soumission chimique` — **2 400/mois, competition LOW (index 2)**.
**Saisonnalité forte à noter** : pic à **6 600** (février 2026) et 5 400 (janvier 2026), retour à 1 300-1 600 depuis avril. Le pic colle à l'entrée en vigueur du 1ᵉʳ janvier 2026 et à sa couverture presse → **le sujet est piloté par l'actualité**, ce qui plaide pour un contenu de fond durable + une discipline de refresh (LEARN-046).

**Head term concurrent à arbitrer** : `drogue du violeur` — **2 900/mois, LOW**, et **plus stable** (2 400-3 600 sur 12 mois, sans pic). Terme profane. → Recommandation : **cibler `soumission chimique` en H1/slug** (terme juridique et médical, celui du code pénal et du décret) et **capter `drogue du violeur` en H2/lexique** dans le corps, plutôt que d'en faire un article séparé (l'anti-scaled-content-abuse du BRIEF §6 interdit un article par variante).

## Requêtes long-tail

Mesurées via Google Ads (2 batches de 10, cf. LEARN-060) :

| Requête | Volume/mois |
|---|---|
| `drogue du violeur` | 2 900 |
| `soumission chimique` | 2 400 |
| `gbl drogue` | 720 |
| `test soumission chimique` | 40 (pic à 110 en janvier 2026) |
| `analyse toxicologique cheveux` | 20 |
| `victime soumission chimique` | 10 |
| `loi soumission chimique` | 10 |
| `depistage soumission chimique` | 10 |
| `ghb`, `porter plainte viol`, `plainte pour viol`, `prescription viol`, `indemnisation victime viol`, `avocat victime de viol`, `consentement viol loi`, `symptomes soumission chimique`, `soumission chimique preuve`, `administration de substance à l'insu`, `kit soumission chimique` | **aucune donnée retournée** |

**Lecture** : configuration proche de LEARN-058 — le head term porte tout, la long-tail de *procédure* est invisible dans les données Ads. Ça ne veut pas dire qu'elle n'existe pas : elle vit dans les **PAA et related searches**, à récolter en Bloc B (`serp_organic_live_advanced` avec `people_also_ask_click_depth`). **Ne pas conclure sur la long-tail avant le Bloc B.**

## Persona

**Persona principal — la personne qui a un trou.** Elle se réveille avec une amnésie partielle ou totale, un doute, parfois des indices physiques. Contexte émotionnel : **sidération + honte + urgence**, et surtout **le doute sur sa propre parole** (« et si j'avais juste trop bu ? »). C'est le registre le plus délicat du pipeline à ce jour : la personne n'est pas sûre d'être victime, donc elle ne se sent pas légitime à agir.

**Persona secondaire — l'entourage.** Ami, colocataire, parent qui cherche à la place de la victime, souvent dans les premières heures. Cible réelle pour la partie « fenêtres de détection ».

**Persona tertiaire — la soumission chimique conjugale, dans la durée.** Configuration où l'administration est répétée par un proche. Registre différent : pas d'urgence horaire, mais durée, emprise et preuve par analyse capillaire segmentaire. À traiter en section dédiée, sobrement.

**Niveau juridique** : néophyte total. Le point pédagogique central : **soumission chimique n'est pas une infraction en soi** — c'est un mode opératoire qui déclenche selon les cas plusieurs qualifications distinctes. ⚠️ *Formulation à valider en Étape 2, c'est le pivot du plan.*

## Arbitrage de persona (sujet mixte — BRIEF §4)

Le sujet peut servir une persona victime **et** une persona mise en cause (« je suis accusé d'avoir drogué quelqu'un »). **Arbitrage tranché : voix victime exclusivement.** L'article est cadré par sa page d'expertise cible `/indemnisation-des-victimes/victimes-de-delits-ou-crimes` → modulation victimes, empathie haute et sobre. Le versant défense pénale est **hors périmètre** de cet article ; s'il intéresse, il fera l'objet d'un article distinct. *→ Point à confirmer par Nicolas (question 3 du STOP).*

## Pages d'expertise cibles

| Rôle | URL | Statut HTTP |
|---|---|---|
| **Money page principale** | `/indemnisation-des-victimes/victimes-de-delits-ou-crimes` | ✅ 200 |
| **Money page secondaire** (volet conjugal) | `/defense-penale/violences-conjugales-et-feminicides` | ✅ 200 |
| **CTA rendez-vous** | `/honoraires-rendez-vous` | ✅ 200 |

**Catégories Wix** : *Ressources et notions juridiques* (`9477320f-…`) + *Victimes de délits ou crimes* (`a755253f-…`).

---

## Hypothèse de valeur — Information Gain

Trois éléments distinctifs, dont deux sont **propriétaires** au sens de la doctrine Google AI Search 2026 (BRIEF §6).

**1. Le pivot local — et il est fort.** L'expérimentation de remboursement sans plainte n'est déployée **que dans certaines régions** : Hauts-de-France, Île-de-France, Pays de la Loire, puis Guadeloupe. **La Nouvelle-Aquitaine n'y figure pas.** Autrement dit, la mesure que toute la presse nationale a annoncée en janvier 2026 **ne s'applique pas à Bordeaux** — et personne n'écrit ce que ça change concrètement pour une victime girondine (qui prescrit, qui paie, comment obtenir quand même les analyses, quelle voie alternative par réquisition judiciaire ou UMJ). C'est un différentiel juridique réel, local, et invisible dans le contenu national.
⚠️ **Vérification impérative en Étape 2** : la liste exacte des régions et la date de chaque extension doivent être lues dans le décret sur Légifrance, pas dans la presse. Si la Nouvelle-Aquitaine a été ajoutée depuis, **ce pivot tombe** et l'angle bascule sur le point 2. *(Source presse repérée au cadrage, à remplacer par la source primaire.)*

**2. La preuve E-E-A-T native : l'indemnisation sans condamnation.** Le cabinet répond déjà, dossiers publiés à l'appui, à **la peur n°1 de cette persona** — « et si l'auteur n'est jamais retrouvé, jamais jugé, jamais condamné ? ». Deux résultats : indemnisation CIVI obtenue **malgré le suicide de l'auteur** (`/post/cabinet-plouton-indemnisation-victime-viol-civi-tarbes`) et **plus de 130 000 €** devant la CIVI pour des victimes de viol et d'agression sexuelle (`/post/victimes-de-viol-incestueux-et-d-agression-sexuelle-le-cabinet-obtient-devant-la-civi-plus-de-130`). C'est exactement la configuration de la soumission chimique, où la preuve manque et où l'auteur reste souvent inconnu. **La démonstration « indemnisation possible sans condamnation » est le cœur citable de l'article** — et aucun contenu concurrent généraliste ne l'apporte avec des résultats réels.

> **Écarté au cadrage (décision Nicolas, 2026-08-07)** : le dossier `contamination-par-le-vih-délit-d-administration-de-substances-nuisibles` (2010) partage la qualification pivot (art. 222-15 CP) mais **pas le contexte factuel** — transmission du VIH, ni soumission chimique, ni amnésie, ni infraction sexuelle par administration. Le rapprochement serait juridiquement exact et éditorialement bancal. **Pas de pilier, pas de lien.**

**3. La synthèse profonde (LEARN-048)** : croiser en un seul tableau **fenêtre de détection biologique × qualification pénale possible × voie d'indemnisation**, là où le contenu existant traite ces trois plans séparément (sanitaire d'un côté, pénal de l'autre, indemnisation nulle part). Agrégation = donnée originale substitutive.

**Garde-fou honnêteté** : les points 1 et 3 reposent sur des vérifications non faites à ce stade. Si le Bloc B révèle que la SERP est déjà tenue par des avocats avec l'angle victime + CIVI, il faudra **pivoter ou abandonner** (BRIEF §6 : « sans gap démontrable, abandonner ou pivoter le sujet »).

---

## Cannibalisation — inventaire catégorie « Ressources et notions juridiques »

Scan API Wix du **2026-08-07** (categoryId `9477320f-…`) : **61 posts publiés** (contre 57 au scan du 23/06 — 4 notions ajoutées depuis).

**Cannibalisation : nulle.** Aucune notion « soumission chimique », « GHB », « viol », « agression sexuelle » ni « consentement » dans la catégorie. Le sous-cluster *violences sexuelles* est **vide côté notions**, alors que le blog compte des dizaines d'affaires publiées sur ce terrain. #12 comble un trou structurel : il devient la **page-carrefour** qui manque au-dessus des affaires.

**Maillage notion↔notion retenu** (tous vérifiés 200) :

| Rôle dans #12 | Cible |
|---|---|
| Indemnisation sans condamnation (H2 cœur) | `/post/indemnisation-civi-2025-guide-complet-pour-les-victimes-d-infractions` |
| Arbitrage CIVI / SARVI | `/post/sarvi-ou-civi-indemnisation-victimes` |
| Comment porter plainte (H2 procédure) | `/post/dépôt-de-plainte-en-france-comment-porter-plainte-efficacement` |
| ITT pénale — qualification et enjeu | `/post/itt-pénale-définition-en-2025` |
| Expertise médicale (préparer son dossier) | `/post/comment-bien-préparer-mon-dossier-médical` |

## Affaires du cabinet — liens internes obligatoires (règle mémoire #8)

Toute mention de ces dossiers, **FAQ et encadrés inclus**, porte un lien vers le post. Ancre neutre, anonymisation conservée. Lecture du `CONTENT_TEXT` en Bloc C (LEARN-063) avant de fonder tout motif, montant ou date.

| Rôle | Cible | Statut |
|---|---|---|
| **Indemnisation malgré l'absence de condamnation** (auteur suicidé) — *pilier E-E-A-T* | `/post/cabinet-plouton-indemnisation-victime-viol-civi-tarbes` | ✅ 200 |
| **Montant CIVI > 130 000 €** | `/post/victimes-de-viol-incestueux-et-d-agression-sexuelle-le-cabinet-obtient-devant-la-civi-plus-de-130` | ✅ 200 |
| Viol conjugal — cour criminelle départementale | `/post/défense-d-une-victime-de-viol-conjugal-devant-la-cour-criminelle-départementale-de-la-seine-maritime` | ✅ 200 |
| Viol en réunion — partie civile | `/post/défense-d-une-jeune-femme-victime-de-viol-en-réunion` | ✅ 200 |
| **Autorité législative** — travaux inceste/imprescriptibilité | `/post/proposition-de-loi-inceste-et-imprescriptibilité-le-cabinet-plouton-au-cœur-des-avancées-législati` | ✅ 200 |

⚠️ **À ne pas mobiliser** : `/post/acquittement-par-la-cour-d-assises-d-appel` (acquittement viol, défense ADN) — angle défense, opposé à la voix de cet article. Et `/post/contamination-par-le-vih-délit-d-administration-de-substances-nuisibles` — écarté au cadrage (contexte factuel trop éloigné, cf. §Hypothèse de valeur).
⚠️ **Reprise presse ELLE** (`/post/intervention-de-maître-plouton-dans-l-enquête-elle-sur-l-inceste…`) : atout d'autorité potentiel, mais **LEARN-056** impose de confirmer l'article de presse réel (titre, média, date, URL vivante) avant toute revendication. À traiter en Bloc C.

---

## Affirmations juridiques à FACT-CHECKER en Étape 2

Anti-hallucination : **rien de ce qui suit n'est acquis**. WebSearch ciblée Légifrance / courdecassation.fr / juricaf.org en premier recours, puis `scripts/legifrance.py code "…" "…"` (contrôle automatique de la version **en vigueur**, LEARN-062 + LEARN-068) et Judilibre. NotebookLM via Nicolas en backup si doute persistant.

1. **Art. 222-30-1 CP** — infraction d'administration d'une substance à l'insu en vue de commettre un viol ou une agression sexuelle : rédaction exacte, quantum, date de création, version en vigueur.
2. **Art. 222-15 CP** — administration de substances nuisibles : périmètre, peines, articulation avec le 222-30-1 (c'est l'articulation qui fonde la qualification pivot du plan).
3. **Loi du 7 novembre 2025** (non-consentement) — numéro exact, articles modifiés (222-22 et suivants), **rédaction littérale de la définition du consentement** (libre, éclairé, spécifique, préalable, révocable) et de la clause « ne peut être déduit du seul silence ».
4. **Effet juridique de l'inconscience / de l'amnésie** sur la caractérisation : la nouvelle définition dit-elle explicitement quelque chose de la personne endormie, inconsciente ou sous emprise d'une substance ? **Point décisif du titre — à ne surtout pas extrapoler.**
5. **Circonstance aggravante** d'administration de substance sur les infractions sexuelles (viol aggravé) : article et quantum.
6. **Décret du 11 décembre 2025** + base LFSS 2025 : numéros, article de rattachement, **liste exhaustive des régions et calendrier d'extension**, durée de l'expérimentation, périmètre des analyses prises en charge (sang/urines/cheveux), rôle du « parcours patient ».
7. **Voie alternative hors régions expérimentales** : réquisition judiciaire, UMJ, prise en charge des frais d'analyse — quel fondement, qui prescrit, qui paie. *(Pierre angulaire du pivot local.)*
8. **Prescription** de l'action publique : viol (majeur / mineur), agression sexuelle, administration de substances nuisibles — délais et points de départ.
9. **CIVI** — conditions d'accès, délais de saisine, indemnisation **en l'absence de condamnation ou d'auteur identifié**, plafonds éventuels. Vérifier la cohérence avec la notion CIVI déjà publiée.
10. **Valeur probatoire de l'analyse capillaire segmentaire** et fenêtres de détection : à sourcer sur référentiel médico-légal officiel (ANSM, SFTA, CRAFS ou rapport ministériel), **pas sur la presse** — donnée chiffrée = source primaire + millésime (BRIEF §6).

## Points de vigilance éditoriale

- **Registre.** Sujet à haute charge. Empathie haute mais **sobre** ; zéro pathos, zéro emphase (garde-fous BRIEF §2). La phrase la plus utile de l'article sera probablement la plus simple : le doute sur soi ne disqualifie pas la parole.
- **Aucune information exploitable par un auteur.** L'article traite des droits de la victime et de la preuve ; il ne décrit ni substances, ni doses, ni modes d'administration.
- **Pas de commentaire d'affaire médiatique.** Le procès de Mazan et l'affaire Pelicot ont installé le sujet dans le débat public, mais l'article n'est pas une chronique judiciaire : au plus une mention contextuelle sourcée, si elle sert la pédagogie.
- **Fraîcheur.** Sujet piloté par l'actualité + expérimentation de 3 ans en cours d'extension → **refresh à M+6 impératif** (LEARN-046), avec surveillance de la liste des régions.

---

## ✅ Arbitrages validés — Nicolas, 2026-08-07

1. **H1 / slug / title validés en l'état** :
   - H1 : *Soumission chimique : ce que la loi permet quand la victime ne se souvient de rien*
   - slug : `soumission-chimique-victime-preuve-recours`
   - title (≤ 60) : *Soumission chimique : vos droits sans souvenir des faits* (57 c.)
2. **Head term** : `soumission chimique` en H1/slug ; `drogue du violeur` (2 900/mo) capté dans le corps et le lexique. **Pas d'article séparé.**
3. **Persona** : **voix victime exclusive**. Volet « mis en cause » hors périmètre, renvoyé à un éventuel article distinct.
4. **Périmètre** : la **soumission chimique conjugale** (durée, emprise, analyse capillaire segmentaire) **reste dans cet article**, en section dédiée.
5. **Dossier VIH / substances nuisibles (2010)** : **écarté** — contexte factuel trop éloigné (cf. §Hypothèse de valeur). Le pilier E-E-A-T repose sur les deux dossiers CIVI.

→ Étape 2 (collecte) lancée le 2026-08-07, en commençant par le **Bloc B** (SERP top 10 + PAA + related searches via DataForSEO) pour confirmer ou casser l'hypothèse d'angle mort avocat, puis Bloc A (fact-check des 10 points ci-dessus, dont la liste des régions du décret), Bloc C (lecture des posts-preuve) et Bloc D (chiffres officiels sur l'ampleur du phénomène).
