# Audit médical des branches agents du 45 Spec (A, A2, PSY fin)

Date : 2026-11-24 · Branches : `agent/45spec-A` (18 pathologies), `agent/45spec-A2` (12), `agent/45spec-PSY` (6 dernières : F45.8_1, F63.3, F05.9_2, F10.0, F14.0, F31.6) · Auditeur : Claude (AAI)
Méthode : celle de `AUDIT_AGENTS_1.md`. L'audit contrôle d'abord tous les fichiers avec `scripts/audit_vague1.py` et `valider()`, puis il vérifie un échantillon en ligne.

## Verdict

| Branche | Verdict | Raison |
|---|---|---|
| A | **Fusionnable** | 0 anomalie mécanique après correction ; 1 imprécision corrigée dans l'échantillon. |
| A2 | **Fusionnable** | 0 anomalie mécanique ; 2 imprécisions corrigées dans l'échantillon. |
| PSY (6 dernières) | **Fusionnable** | 0 anomalie mécanique ; 0 erreur dans l'échantillon. |

## 1. Contrôles mécaniques (tous les fichiers ajoutés par chaque branche)

| Contrôle | A (18 fichiers, 360 QCM) | A2 (12, 240) | PSY (6, 120) |
|---|---|---|---|
| Ratio A / Kprim / menu long | 70 / 20 / 10 % | 70 / 20 / 10 % | 70 / 20 / 10 % |
| Type A, Kprim, explications, sources, notions, CNP/CPCM | conforme | conforme | conforme |
| Correction validée par `valider()` | conforme | conforme | conforme |
| Menu long à 1–3 réponses justes | conforme (36/36) | conforme (24/24) | conforme (12/12) |
| Diagnostic masqué nommé | 5 → 0 | 0 | 0 |

Les 5 fuites de A (ANG I87.1 Q19, CHI K40.3 Q11, CPL M72.6 Q09 et Q19, CTH J93.0 Q19) nomment l'entité dans la question, comme le veut leur objectif pédagogique. Elles passent donc en `diagnosticMasque: false`, comme dans la vague 1. Le contrôle « 1 à 3 justes » ajouté après l'audit 1 fonctionne : aucun menu long ne dépasse 3 réponses justes.

## 2. Audit médical par échantillon

L'audit a vérifié la réponse juste de chaque type A et de chaque menu long, les 4 affirmations de chaque Kprim, puis les seuils et les posologies de la `priseEnCharge`.

| Branche | Pathologies auditées | QCM vérifiés | Erreurs ou imprécisions | Corrigées |
|---|---|---|---|---|
| A | T74.1_4 violence conjugale, I60.9 HSA, J93.0 pneumothorax suffocant, S72.0 fracture du fémur proximal, C50.9 cancer du sein, F90.0 TDAH | 120 | 1 | oui |
| A2 | Z30.0_3 contraception d'urgence, T39.1 paracétamol, D50.9 anémie ferriprive, T58 CO, R33 globe vésical chronique, Z60.4 harcèlement scolaire | 120 | 2 | oui |
| PSY | F10.0 collègue sous influence, F14.0 délire agité sur cocaïne, F31.6 état mixte | 60 | 0 | ras |

Au total, l'échantillon contient 3 imprécisions et aucune réponse juste fausse sur 300 QCM.

**Corrections apportées**
- **A, ONC C50.9 Q06** : la réponse disait que les programmes de dépistage mammographique existent « surtout en Suisse romande ». Or plusieurs cantons alémaniques en ont un aussi (notamment BS et SG, selon Swiss Cancer Screening). L'option dit maintenant que les programmes sont cantonaux, qu'ils ne couvrent pas tous les cantons et qu'ils invitent les femmes dès 50 ans tous les deux ans.
- **A2, URO R33 Q16** : l'affirmation « on change un cathéter sus-pubien tous les trois mois » était déclarée fausse. Or l'intervalle dépend du matériau et du fabricant, et trois mois correspond à une pratique courante. L'affirmation est remplacée par une affirmation fausse sans ambiguïté : le cathéter ne se change jamais.
- **A2, TOX T39.1 Q13** : la vignette citait un « comprimé de tramadol-codéine », une association qui n'existe pas. Elle cite maintenant des comprimés de tramadol.

**Points vérifiés en ligne (tous justes)**
- **Art. 50 LEI** : l'al. 2 let. a cite la violence domestique comme raison personnelle majeure. La teneur révisée par la LF du 14.6.2024 est entrée en vigueur le 01.01.2025, et sa liste d'indices comprend les rapports médicaux (Fedlex, via juriup.ch, consulté le 24.11.2026).
- **Tox Info Suisse, paracétamol (février 2024)** : le schéma de N-acétylcystéine compte deux poches, soit 200 mg/kg en 4 h puis 100 mg/kg en 16 h (300 mg/kg en 20 h). Le traitement se poursuit à 6,25 mg/kg/h avec un contrôle toutes les 12 h. On l'arrête si les transaminases restent sous 2 fois la norme, avec une paracétamolémie sous 10 mg/L après une forte ingestion. Entre 8 et 24 h, on commence la NAC dans tous les cas. Au-delà de 36 h, elle n'est pas indiquée si les transaminases restent sous 2 fois la norme. La NAC peut élever un peu l'INR. Les QCM concordent avec tous ces points.
- **IENK 2026** : au-delà de 70 kg ou d'un IMC de 26, le DIU au cuivre passe en premier, puis l'UPA à dose standard ; le LNG 3 mg reste hors autorisation. Avec un inducteur, le DIU passe en premier, puis le LNG 3 mg ; l'UPA à double dose n'est pas recommandé. Pendant l'allaitement, le LNG est le premier choix. Après un vomissement dans les 3 h, la patiente reprend une dose. Après l'UPA, elle attend 5 jours avant toute contraception hormonale. Si les règles manquent 3 semaines ou plus, elle fait un test de grossesse. La remise en pharmacie n'est pas anonyme et se fait en personne. Les QCM concordent avec tous ces points.
- **CANMAT/ISBD 2021, caractéristiques mixtes** : aucun agent n'est en première ligne. En deuxième ligne, on trouve l'aripiprazole, l'asénapine, la cariprazine et le divalproex pour la manie, ainsi que la cariprazine et la lurasidone pour la dépression. La CIM-10 F31.6 exige au moins 2 semaines.
- La nimodipine se donne à 60 mg toutes les 4 h pendant 21 jours, et la décompression se fait au 4e–5e espace intercostal sur la ligne médio-axillaire (ATLS). Le méthylphénidate se prescrit sur ordonnance de stupéfiants, et l'AI le prend en charge par le ch. 404 OIC avant 9 ans révolus. Le taux légal d'alcool est de 0,5 ‰, et la LPMéd art. 40 let. a s'applique. McLellan 2008 trouve 78,7 % des médecins en exercice à 5 ans.

Les 15 pathologies auditées portent `audit.rejector = "pass"` dans leurs trois fichiers (questions, notions et correction). Les posologies vérifiées perdent la mention « à vérifier dans l'AIPS » : nimodipine, tamoxifène, létrozole, vitamine D, NAC, UPA et LNG.

## Points à vérifier (non bloquants)

- ORT S72.0 : la mention « zolédronate 3 ans au plus » reste à confronter à l'AIPS et à l'ASCO/SVGO, car la durée dépend du risque résiduel.
- ONC C50.9 Q15 : le chiffre de 6550 cas par an reste à confronter à la dernière publication NICER/OFS.
- MIG Z60.4 Q08 : le chiffre HBSC 2022 (environ 6 %) reste à confronter au rapport suisse d'Addiction Suisse.
- F31.6 Q19 : le DSM-5-TR n'inclut pas l'agitation psychomotrice dans les caractéristiques mixtes, alors que la CIM et la clinique l'admettent. La réponse reste juste dans le cadre de la CIM.

Signature : AAI (Anthropic AI)

## Addendum (24.11.2026, après l'arrêt des producteurs)

| Branche | Nouveaux fichiers | Contrôle mécanique | Audit médical | Erreurs | Verdict |
|---|---|---|---|---|---|
| A2 (lot 5 : Z53.2_3, H05.0, T18.1) | 3 (15 au total) | 0 anomalie sur 300 QCM | Z53.2_3, T18.1 (CC art. 378, 379, 426, 429, 439 ; ESGE 2016) | 0 | **Fusionnable** |
| B (K64.9, K71.9, L01.0) | 3 | 0 anomalie sur 60 QCM | K64.9, K71.9 (OPAS art. 12e, EASL DILI 2019, LPTh art. 59) | 0 | **Fusionnable** |
| NEU (G04.9_1, G12.0, G25.5, G37.2, G37.3, G47.5) | 6 | 0 anomalie sur 120 QCM | G37.2 (ESE 2014), G04.9_1 (Annegers 1987, FEBSTAT), G12.0 (dépistage néonatal SMA dès le 01.07.2024, OFSP) | 0 | **Fusionnable** |
| reprise (E11.9, I49.5, I75.0, E87.6, B18.9 ; CAR I35.0 Q11) | 5 corrections | `valider()` sans erreur ; END, CAR, NEP et GAS : 0 anomalie sur 5637 QCM | rédaction auditée | 6 corrigées | **Fusionnable** |

Les marques `audit.rejector = "pass"` de B et de NEU n'ont pas été poussées, car l'auditeur n'avait pas l'autorisation de pousser sur ces branches. Les fusions sur main restent à faire par une session autorisée.

Signature : AAI (Anthropic AI)
