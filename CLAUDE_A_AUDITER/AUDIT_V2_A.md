# Audit V2 groupe A — journal (80 pathologies produites par l'API)

Légende : 🟩 juste (réserves éventuelles notées) · 🟧 corrigé ou à vérifier · 🟥 rejeté.
Méthode : relecture complète des notions chiffrées, des posologies et des questions (réponses justes, menus longs 1 à 3 justes, diagnostic masqué des niveaux 4–5), puis contrôle mécanique `controle_menus_longs.py`.
Limite assumée : la lecture en ligne des sources primaires a échoué (PubMed renvoie une page de cookies) ; les seuils et doses ont été confrontés aux recommandations connues (ESC/ESVS, IDSA, ECIL-5, EASL, ARIA/EAACI, ASCRS, HerniaSurge, AIPS), et chaque doute est noté « à vérifier » dans le champ `audit.claude.aVerifier` des fichiers.
Contrôles transversaux sur les 80 : aucun CNP ni CPCM ; aucune mention de PEP VIH (règle des 48 h sans objet dans ces fichiers) ; 17 questions de niveau 4–5 non masquées recensées, à traiter pathologie par pathologie.

## Passage 1 — pathologies 1 à 10 sur 80

| # | Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|---|
| 1 | D84.8 Immunodépression iatrogène | 🟧 | Corrigé : durée de la prophylaxie anti-VHB précisée « après l'arrêt de l'immunosuppression » (EASL 2017) ; aciclovir i.v. ophtalmique limité à l'immunodéprimé (notion, correction, « why » de Q08). À vérifier : N04 (première cause d'immunodépression acquise, source absente). |
| 2 | J30.4 Rhinite allergique | 🟩 | Q11 (niveau 4) : diagnostic non nommé, `diagnosticMasque` passé à vrai. |
| 3 | J34.3 Hypertrophie des cornets | 🟩 | À vérifier : disponibilité suisse de l'association azélastine-fluticasone (AIPS). |
| 4 | I70.2_2 Ischémie critique chronique | 🟩 | À vérifier : pronostic à 1 an (amputation ≈ 25 %, mortalité ≈ 20 %) variable selon TASC II et ESC. |
| 5 | I73.8_2 Raynaud primaire, acrocyanose | 🟩 | Forme : clé `mesuresGénérales` hors schéma retirée. Hors AMM déjà signalé. |
| 6 | I83.0 Ulcère veineux | 🟩 | À vérifier : taux de cicatrisation à 6 mois (≈ 70 %). |
| 7 | I83.9_1 Varices, insuffisance veineuse | 🟩 | Forme : 31 cellules de tableau enveloppées pour respecter le schéma. À vérifier : polidocanol en grossesse (contre-indication relative). |
| 8 | K42.9 Hernie pariétale réductible | 🟩 | À vérifier : prophylaxie antibiotique (Swissnoso 2018) et énoxaparine, à ne pas rendre systématiques. |
| 9 | K56.4 Fécalome | 🟩 | Forme : deux notions de nature « surveillance » reclassées. À vérifier : définition du signe de Gersuny. |
| 10 | K60.0 Fissure anale | 🟩 | Source ASCRS harmonisée sur 2017 ; nature « suisse » corrigée en « contexte suisse ». À vérifier : référence ESGE 2020. |

Contrôles : `controle_menus_longs.py` ALL, ANG, CHI → 0 menu fautif ; reste 1 erreur de schéma sur K60.2 (correction sans `priseEnCharge`, pathologie 11 du prochain passage). Les spécialités CMF, HEM, MIG, OPH, ORL, PEA, TOX affichent encore des erreurs de schéma sur des pathologies non auditées (traitées aux passages suivants).

## Passage 2 — pathologies 11 à 20 sur 80

| # | Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|---|
| 11 | K60.2 Fissure anale | 🟧 | Corrigé : `ssp` était une chaîne mal formée qui avalait `priseEnCharge` (schéma restauré, 3 plans) ; sources ASCRS harmonisées sur 2017 ; dose de toxine botulique « 10–20 UI » retirée (non confirmée) ; accord « indurée ». À vérifier : dose de toxine (RCP), trinitrine 0,4 % et diltiazem/nifédipine topiques en Suisse (AIPS), taux de guérison (70–80 % ici, ≈ 50 % dans K60.0), aciclovir et pénicilline benzathine face aux recommandations suisses. |
| 12 | K64.5_1 Hémorroïdes thrombosées / fissure | 🟧 | Corrigé : seuil non sourcé « douleur de plus de deux semaines » (N59, Q16) remplacé par « au-delà de l'évolution attendue » (cohérent avec la résorption en 2–4 semaines). À vérifier : seuil de reconsultation (ASCRS), ibuprofène dès la 20e semaine de grossesse et paracétamol 3 g/j (AIPS), trinitrine 0,2–0,4 % et nifédipine (statut suisse). |
| 13 | H92.0 Otalgie | 🟧 | Corrigé : « why » de Q15-G contradictoire avec son statut de distracteur ; « drainage l'abcès » → « draine ». À vérifier : N05 (≈ 50 % des otalgies à tympan normal, sans source), N59 (réévaluation à 2 semaines), Q13 (OPG d'emblée pour une dysfonction temporo-mandibulaire, discutable). |
| 14 | K00.7 Dentition (poussée dentaire) | 🟩 | Corrigé : bloc de correction à 5 rubriques scindé en deux (schéma : 4 au plus). Paracétamol 10–15 mg/kg et NICE NG143 conformes. À vérifier : fluor du dentifrice du nourrisson et âge du 1er contrôle (SSO), N33 (salicylés, belladone), fenêtre de 8 jours de Macknin 2000. |
| 15 | K02.9_1 Carie de la petite enfance | 🟧 | Corrigé : deux fautes de grammaire. À vérifier : dentifrice ≈ 500 ppm avant 6 ans et 1re visite vers 2 ans (SSO), doses pédiatriques paracétamol/ibuprofène et amoxicilline-clavulanate (AIPS). |
| 16 | K02.9 Caries profondes, restaurations défectueuses | 🟧 | Corrigé : `ssp` mal formé qui avalait `priseEnCharge` (schéma restauré). Q19 (niveau 4) masquée. À vérifier : ibuprofène « contre-indiqué au 3e trimestre » (AIPS : seconde moitié de la grossesse), doxycycline en prophylaxie d'endocardite (ESC 2023), source de N35. |
| 17 | K04.7_1 Fluxion dentaire | 🟧 | Corrigé : N51 (« sepsis, première cause de décès » non étayé) reformulé ; Q07 (niveau 4) `diagnosticMasque` passé à vrai ; `ssp` mal formé qui avalait `priseEnCharge` (réparé par moi après l'audit). À vérifier : AINS et aggravation (N48), clindamycine seule en allergie IgE (Q12, SSI), art. 31 LAMal / OPAS (N08). |
| 18 | K04.7 Pulpite, abcès péri-apical | 🟧 | Corrigé : clé parasite `false_placeholder` (Q15) ; « drainage l'abcès » → « draine ». À vérifier : AINS en grossesse (N44, AIPS), N05 (≈ 2 milliards de caries non traitées, GBD 2017 ≈ 2,3). |
| 19 | K05.3 Maladie parodontale chronique | 🟧 | Corrigé : seuil de l'étape 3 (≥ 6 mm ou saignante ≥ 4 mm) ; paracétamol chiffré (≥ 50 kg : 1 g, max 4 g/j ; < 50 kg : 15 mg/kg, max 60 mg/kg/j) ; formule vague « dose selon Fagerström » remplacée par un schéma chiffré. À vérifier : métronidazole 500 mg contre 400 mg ×3 (EFP S3), schéma nicotinique (AIPS), PSR/PSI (SSO), OPAS, AINS et cellulite (Q06). |
| 20 | K07.6 Dysfonction temporo-mandibulaire | 🟩 | Corrigé : paracétamol chiffré. Seuils DC/TMD, prednisone 40–60 mg/j dans l'artérite à cellules géantes et rappels dT conformes. À vérifier : N51 (Cochrane 2018, année), N52 (9 séances de physiothérapie, OPAS art. 5), amitriptyline 10–25 mg hors AMM. |

Contrôles transversaux du passage : aucun CNP, CPCM ni PEP VIH dans les dix pathologies ; tous les niveaux 4–5 sont masqués ; tous les menus longs ont 1 à 3 justes. Limite inchangée : aucune source primaire lue en ligne (accès bloqué) ; les seuils ont été confrontés aux recommandations connues et les doutes sont dans `audit.claude.aVerifier`.
`controle_menus_longs.py` : ALL, ANG, CHI → 0 menu fautif, 0 erreur de schéma ; CMF → 0 menu fautif ; 2 erreurs de schéma restantes sur K12.0_1 et K12.2 (pathologies 21 et suivantes, au prochain passage).

Reste à auditer : pathologies 21 à 80 (K12.0_1 → K52.1).
