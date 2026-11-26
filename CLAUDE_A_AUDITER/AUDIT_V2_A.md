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

## Passage 3 — pathologies 21 à 31 sur 80 (11 pathologies)

Méthode : la pathologie 21 est relue par moi ; les neuf autres sont relues par trois sous-agents avec la même grille (doses, seuils, PEP VIH, CNP/CPCM, masquage des niveaux 4–5, menus longs, « why »). Aucune source primaire n'a été lue en ligne : les doutes sont dans `audit.claude.aVerifier`.

| # | Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|---|
| 21 | K12.0_1 Aphtose buccale récidivante | 🟧 | Corrigé : clé parasite `false_placeholder` (Q18), accords (Q09, Q15), formulation de N05. À vérifier : colchicine en première intention (EULAR 2018 concerne Behçet), aprémilast et thalidomide extrapolés de Behçet, sources de N05 et N08. |
| 22 | K12.0 Aphtose buccale bénigne | 🟧 | Corrigé : Q20 passée à `diagnosticMasque=false` (l'énoncé nomme « aphtes majeurs »), accord de N34. À vérifier : indication suisse de l'aprémilast, doses de colchicine et de prednisone, bêtabloquants (N13), durée de l'aphte mineur (N52). |
| 23 | K12.2 Cellulite / abcès odontogène | 🟧 | Corrigé : clé parasite `correger` (Q20), accord (Q01), « why » de Q06-C. À vérifier : durée d'antibiothérapie 5–7 jours (SSI), fréquence des dents causales (N07). |
| 24 | D69.6_1 Pseudo-thrombopénie à l'EDTA | 🟥→🟧 | Corrigé : `priseEnCharge` collée dans la chaîne `ssp` (JSON malformé), reconstruite ; clé parasite (Q16) ; accord (Q10). À vérifier : part de 15–20 % des thrombopénies fortuites, 0,1–2 % des FSC, facteur citrate. |
| 25 | D72.8 Leucocytose sous corticoïdes ou stress | 🟧 | Corrigé : accords (Q03, Q08), « why » faux de Q20-H (mononucléose), « prophylaxie du pneumocoque » → pneumocystose. À vérifier : seuil de neutrophilie, leucocytes < 30 G/L (N05), seuils de prophylaxie, doses d'hydrocortisone et d'antibiotiques. |
| 26 | D75.1 Polyglobulie secondaire | 🟧 | Corrigé : « why » de Q07-E, accord (Q19). À vérifier : seuil de saignée (Hct 60–65 %), patch nicotinique, critères d'oxygénothérapie (GOLD), tiotropium et varénicline. |
| 27 | D75.8 Thrombocytose réactive | 🟩 | Rien de faux. À vérifier : posologie du fer et du carboxymaltose, fréquences JAK2/CALR/MPL, N18 sans source. |
| 28 | A41.9 Sepsis et choc septique | 🟧 | Corrigé : N39 faux (définition Sepsis-3 du choc), Q11 (niveau 4) nommait le diagnostic, reformulée. À vérifier : contrôle de source en 6–12 h (SSC 2016 contre 2021), mortalités, 7–8 %/h (Kumar), posologies. |
| 29 | R65.2 Choc septique | 🟧 | Corrigé : déclaration de la méningococcie par le médecin au médecin cantonal sous 24 h (N78, Q08, correction) ; source de N26 ; Q03 (noradrénaline en voie centrale). À vérifier : circuit exact de déclaration, hémocultures négatives, posologies. |
| 30 | E43_3 Dénutrition liée à l'âge | 🟩 | Rien à corriger (GLIM, EWGSOP2, MNA-SF, NRS-2002, thiamine, reprise nutritionnelle). À vérifier : prévalences N05–N07, vitamine D 800 UI/j. |
| 31 | E61.1 Carence martiale | 🟧 | Corrigé : clé parasite `false` (Q16), source du seuil de ferritine (< 30 µg/L, la BSG 2021 retient < 45 µg/L), AABB 2023. À vérifier : seuil de ferritine, prévalence suisse N05, N38, acide tranexamique. |

Contrôles du passage : aucun CNP, CPCM ni PEP VIH ; tous les niveaux 4–5 sont masqués ; menus longs à 1–3 justes. `controle_menus_longs.py` CMF, HEM, INT, MIG → 0 menu fautif, 0 erreur de schéma.

Reste à auditer : 49 pathologies (OPH, ORL, MTR, PEA, TOX et autres, de H00.0 à K52.1).

## Passage 4 — pathologies 32 à 41 sur 80 (10 pathologies)

Méthode : trois sous-agents avec la même grille (doses, seuils, PEP VIH, CNP/CPCM, masquage des niveaux 4–5, menus longs, « why », clés parasites) ; vérification finale par moi (JSON valides, champ `audit.claude` rempli). Aucune source primaire lue en ligne : les doutes sont dans `audit.claude.aVerifier`.

| # | Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|---|
| 32 | F32.1_1 Dépression de l'âgé | 🟧 | Corrigé : Q03 (« sans IRM d'emblée » → imagerie si doute ou déficit persistant), « why » de Q20-J. À vérifier : doses d'escitalopram/citalopram > 65 ans, sertraline, lorazépam, art. 426/429 CC, seuils MoCA/GDS/PHQ-9, remboursement de la psychothérapie. |
| 33 | F43.2_1 Trouble de l'adaptation, burn-out | 🟧 | Corrigé : Q04 `diagnosticMasque` vrai, « why » de Q16. À vérifier : articles LPGA/LAI/CO/LACI/CP/LCR et ATF, chiffres AI et suicides, début ≤ 1 mois (CIM-10) contre 3 mois (DSM-5), délai de 3–6 mois pour changer de profession. |
| 34 | H00.0 Orgelet | 🟧 | Corrigé : clé parasite `false` (Q17) ; amoxicilline-clavulanate 875/125 « 2–3×/j » → 2×/j. À vérifier : posologies AIPS (flucloxacilline, amoxicilline-clavulanate IV), schéma pédiatrique, durée 7–10 jours. |
| 35 | H00.1 Chalazion | 🟧 | Corrigé : clé parasite `false` (Q16). À vérifier : tobramycine/dexaméthasone, doxycycline hors AMM, triamcinolone, délai d'adressage (« au-delà d'un mois » contre 4–8 semaines), régression sous compresses. |
| 36 | H01.1 Eczéma ou cellulite palpébrale | 🟧 | Corrigé : amoxicilline-clavulanate de la correction alignée sur 1 g 3×/j (AIPS : 2×/j possible) ; cellules de tableau au schéma. À vérifier : posologie dans la cellulite pré-septale, amoxicilline seule (N43), tacrolimus topique hors AMM, cétirizine 20 mg/j hors AMM. |
| 37 | H02.4 Ptosis | 🟧 | Corrigé : Q04 et Q07 `diagnosticMasque` vrai ; cellules de tableau au schéma. À vérifier : excursion du releveur > 10 mm (BCSC 12–15 mm), garantie de prise en charge LAMal. |
| 38 | H04.1 Sécheresse oculaire | 🟧 | Corrigé : « why » faux de Q07-E (compresses chaudes et glaucome aigu). À vérifier : ciclosporine 0,1 % (Swissmedic), non-remboursement des larmes artificielles. |
| 39 | H10.0 Conjonctivite bactérienne | 🟧 | Corrigé : Q19 (7 notions liées, 6 au plus). À vérifier : ceftriaxone 1 g IM, doxycycline 7 jours (source OFSP), chloramphénicol et azithromycine collyre (AIPS), ceftriaxone néonatale. |
| 40 | H10.1 Conjonctivite allergique | 🟧 | Corrigé : accords (Q02, Q10, Q14). À vérifier : prévalence, calendrier pollinique, collyres (épinastine), immunothérapie 3 ans, Q20 (ulcère en bouclier). |
| 41 | H11.3 Hémorragie sous-conjonctivale | 🟧 | Corrigé : accords (N02, Q07). À vérifier : résorption 10–14 jours, reconsultation à 2–3 semaines, paracétamol et ondansétron (AIPS). |

Contrôles du passage : aucun CNP, CPCM ni PEP VIH ; niveaux 4–5 masqués ; menus longs à 1–3 justes. `controle_menus_longs.py` MTR et OPH → 0 menu fautif ; il reste des erreurs de schéma sur des pathologies OPH non encore auditées (H25.9, H49.2, H52.1, H53.0, H57.0_1…).

Reste à auditer : 39 pathologies (H25.9_1 → K52.1).

## Passage 5 — pathologies 42 à 51 sur 80 (10 pathologies, OPH)

Méthode : trois sous-agents avec la même grille ; JSON revalidés par moi. Aucune source primaire relue en entier en ligne (recherches ponctuelles AAO seulement) : les doutes sont dans `audit.claude.aVerifier`.

| # | Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|---|
| 42 | H16.1 Kératite / lésion cornéenne | 🟧 | Rien de faux relevé. À vérifier : posologies (oxybuprocaïne, ofloxacine, cyclopentolate, ibuprofène, acétazolamide, ondansétron, ciclosporine), durée d'irrigation, N04/Q15 non sourcées. |
| 43 | H25.9_1 Cataracte (glaucome phacomorphique) | 🟧 | Corrigé : pilocarpine déconseillée dans le glaucome phacomorphique. À vérifier : confirmation EGS/AAO, chiffre « plus de la moitié des plus de 70 ans », acuité du permis. |
| 44 | H25.9_2 Cataracte | 🟧 | Corrigé : coquilles (Q01, Q06, Q14, N55), « intracaméral ». À vérifier : prévalences, OAC art. 27, posologies postopératoires. |
| 45 | H25.9 Cataracte | 🟧 | Corrigé : clé `horsUrgence` hors schéma, Q05 (« hier »), consignes Kprim, « intracaméral ». À vérifier : 90 % contre 95 % d'amélioration, endophtalmie < 0,2 %, doses EVS. |
| 46 | H43.8 Décollement postérieur du vitré | 🟧 | Corrigé : contrôle 1–2 semaines puis 4–6 semaines (AAO). À vérifier : posologie mydriatiques, fréquences de déchirure. |
| 47 | H49.2 Paralysie microvasculaire III/VI | 🟧 | Corrigé : `priseEnCharge` restaurée dans `ssp`, « why » de Q02/Q13/Q17, Q07 masqué, « jamais » nuancé. À vérifier : EULAR 2018 contre 2023, pantoprazole, atorvastatine, LCR 15d. |
| 48 | H50.0 Strabisme concomitant | 🟧 | Corrigé : « irréversible après 6–8 ans » nuancé, Q05/Q12 masqués, consignes. À vérifier : cyclopentolate, atropine, seuils PEDIG, remboursements. |
| 49 | H50.9 Pseudostrabisme | 🟧 | Corrigé : sens de refixation faux (Q03-A), Q19 révélait le diagnostic, « why » Q06, Q09-E, accords, catégories. À vérifier : Hirschberg, prévalence, seuil 4 mois, OPAS 12e. |
| 50 | H52.1 Troubles sensoriels méconnus | 🟧 | Corrigé : clé `false`, nature « drapeau rouge », limite « plasticité 7–8 ans » retirée, menus annoncés « une à trois réponses ». À vérifier : cyclopentolate, myopie, MiGeL, seuil OMS 2021. |
| 51 | H53.0 Amblyopie | 🟧 | Corrigé : natures hors énumération, limite « 7–8 ans » retirée (Q04, Q15, N06). À vérifier : délai 24–48 h, atropine, rechute ≈ 25 %, MiGeL. |

Contrôles du passage : aucun CNP, CPCM ni PEP VIH ; niveaux 4–5 masqués ; menus longs à 1–3 justes. `controle_menus_longs.py OPH` → 0 menu fautif ; 1 erreur de schéma restante sur H57.0_1 (pathologie non encore auditée).

Reste à auditer : 29 pathologies (H57.0_1 → K52.1).

## Passage 6 — pathologies 52 à 61 sur 80 (10 pathologies, OPH et ORL)

Méthode : trois sous-agents avec la même grille ; JSON revalidés par moi avec `controle_menus_longs.py`. Aucune source primaire relue en ligne (une recherche ponctuelle sur l'otite externe nécrosante) : les doutes sont dans `audit.claude.aVerifier`.

| # | Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|---|
| 52 | H57.0_1 Mydriase iatrogène topique | 🟧 | Corrigé : seuil d'anisocorie physiologique « ≤ 1 mm » uniformisé, oblique inférieur ajouté (nerf III), clé parasite `si` retirée (Q12-C). À vérifier : doses du glaucome aigu, lorazépam et physostigmine (Tox Info 145), durées de mydriase, sources « EGS 2020 » et sociétés suisses trop vagues. |
| 53 | H57.0 Anisocorie physiologique | 🟧 | Corrigé : phrase ambiguë sur le faux négatif en phase aiguë (c'est l'apraclonidine). À vérifier : « ESO 2021 », aspirine (CADISS, TREAT-CAD), acétazolamide i.v., pilocarpine 0,1 % magistrale, prévalence 15–20 %. |
| 54 | H53.2 Diplopie monoculaire | 🟧 | Corrigé : chiffre « 20–25 % des consultations » retiré (sans source). À vérifier : hyaluronate et ciclosporine (AIPS), LiMA, art. 15d LCR, PPP AAO cataracte, BUT < 10 s. |
| 55 | H60.3 Otite externe aiguë bactérienne | 🟧 | Corrigé : source « IDSA/ESCMID 2020 » inexistante remplacée (consensus multispécialité, J Laryngol Otol 2020), Q07 masqué. À vérifier : référence exacte, ciprofloxacine et gouttes (AIPS). |
| 56 | H60.5_1 Otite externe diffuse aiguë | 🟧 | Corrigé : coquille N31, « why » de Q09 (« triade ») et de Q20-G. À vérifier : spécialité suisse ciprofloxacine-dexaméthasone, nerfs IX–XII contre IX–XI, durées ciprofloxacine et clotrimazole, libellé de discipline. |
| 57 | H66.0 Otite moyenne aiguë perforée | 🟧 | Corrigé : durées d'amoxicilline alignées sur l'AAP 2013 (N46, correction, Q04, Q20), Q08 masqué, coquille Q01, trois blocs de 6 points ramenés à 5 (schéma). À vérifier : durées SSI/SSP, doses des alternatives (AIPS), vaccin antipneumococcique actuel de l'OFSP, taux de fermeture > 90 %. |
| 58 | H81.2 Névrite vestibulaire | 🟧 | Corrigé : source de la prednisone (Strupp 2004 testait la méthylprednisolone) reprécisée. À vérifier : schéma de prednisone, ondansétron et diménhydrinate, thrombolyse (SSN 2023), 9 séances OPAS, HINTS contre IRM précoce. |
| 59 | H93.1 Acouphènes chroniques | 🟧 | Corrigé : accord Q03, « why » de Q14-A, 6 questions passées à `diagnosticMasque` faux (vignette nommant l'acouphène), Q11 masquée (« sifflement »), OSLUM développée. À vérifier : OSLUM 100 dB(A), seuil Suva 85 dB(A), forfait AVS/AI, THI ≥ 58, prednisone 1 mg/kg/j. |
| 60 | J00 Rhinite aiguë virale | 🟧 | Corrigé : clé parasite `__` (conduite.urgence), discipline « S Santé publique » invalide → « N Médecine sociale Prévention OFSP », Q05/Q12/Q13 `diagnosticMasque` faux. À vérifier : décongestionnant 5 contre 5–7 jours, xylométazoline pédiatrique, ibuprofène dès 3 mois, intitulé Smarter medicine. |
| 61 | J00_1 Rhinopharyngite | 🟧 | Corrigé : « 2 à 5 rhumes par an », vignette Q12 complétée, `prevention.tertiaire` remplie. À vérifier : durée de xylométazoline, prévalence de la rhinite allergique (SAPALDIA), millésimes ACCP 2006/CHEST 2016 et ARIA 2019/2020, posologies AIPS, dexchlorphéniramine. |

Contrôles du passage : aucun CNP, CPCM ni PEP VIH ; niveaux 4–5 masqués ; menus longs à 1–3 justes. `controle_menus_longs.py OPH` → 0 menu fautif, 0 erreur de schéma ; `ORL` → 0 menu fautif ; 2 erreurs de schéma restantes sur des pathologies non encore auditées (J02.9 `statements` manquant, J03.9_1 clé `false`).

Reste à auditer : 19 pathologies (E66.1, F06.7, F10.0_1, F32.1_3, F80.8, F82, F90.0_1, F90.0_2, F93.1, G44.4, G72.0, G89.3_1, J01.0, J02.9, J03.0, J03.9, J03.9_1, J38.1, K52.1).
