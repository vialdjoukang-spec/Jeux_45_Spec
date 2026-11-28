# Audit des explorations fonctionnelles — synthèse (28.11.2026)

**174 fiches** : 124 « AUDITÉ » · 50 « AUDITÉ — à vérifier ». 819 vérifications sourcées consignées, 88 constats, 72 points à vérifier.

Chaque preuve est un extrait de 25 mots au plus, retrouvé mot pour mot par script dans la source lue le 28.11.2026 (rapports `LOT_<n>.json`).

## Constats par gravité

| Gravité | Constats | Corrections appliquées |
|---|---|---|
| 🟥 critique | 8 | 8 |
| 🟧 majeur | 33 | 30 |
| 🟨 mineur | 46 | 34 |
| 🟦 forme | 1 | 1 |

## Par lot (15 fiches, ordre alphabétique)

| Lot | Fiches | Vérifications | 🟥 | 🟧 | 🟨 | 🟦 | AUDITÉ | AUDITÉ — à vérifier | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| LOT_1 | 15 | 70 | 0 | 0 | 1 | 0 | 9 | 6 | 🟨 mineurs seulement |
| LOT_2 | 15 | 64 | 0 | 7 | 1 | 0 | 8 | 7 | 🟧 majeurs |
| LOT_3 | 15 | 72 | 2 | 3 | 1 | 1 | 11 | 4 | 🟥 critique |
| LOT_4 | 15 | 61 | 0 | 2 | 6 | 0 | 9 | 6 | 🟧 majeurs |
| LOT_5 | 15 | 72 | 1 | 2 | 6 | 0 | 11 | 4 | 🟥 critique |
| LOT_6 | 15 | 95 | 0 | 1 | 8 | 0 | 9 | 6 | 🟧 majeurs |
| LOT_7 | 15 | 72 | 1 | 3 | 4 | 0 | 14 | 1 | 🟥 critique |
| LOT_8 | 15 | 67 | 0 | 6 | 3 | 0 | 13 | 2 | 🟧 majeurs |
| LOT_9 | 15 | 70 | 0 | 3 | 6 | 0 | 14 | 1 | 🟧 majeurs |
| LOT_10 | 15 | 61 | 1 | 2 | 5 | 0 | 10 | 5 | 🟥 critique |
| LOT_11 | 15 | 66 | 3 | 3 | 2 | 0 | 8 | 7 | 🟥 critique |
| LOT_12 | 9 | 49 | 0 | 1 | 3 | 0 | 8 | 1 | 🟧 majeurs |

## Constats 🟥 et 🟧

| Id | G | Fiche | Problème | Corrigé | Source lue |
|---|---|---|---|---|---|
| LOT_2-001 | 🟧 | `calorimetrie_indirecte` | La fiche cite quatre fois la recommandation ESPEN de 2019, que l'ESPEN a raccourcie et partiellement révisée en 2023 (Singer et al., Clin Nutr 2023;42:1671). Les chiffres (70 %, 80 à 100 %, 60 %) sont inchangés dans la version de  | oui | ESPEN, Singer et al. (guide pratique partiellement révisé) (2023) |
| LOT_2-003 | 🟧 | `capnographie` | La fiche attribue tout son contenu aux recommandations ERC 2021, exactes sur le fond (vérifiées), mais remplacées par les recommandations ERC 2025 (Soar et al., Resuscitation 2025;215 Suppl 1:110769). Le texte intégral de 2025 n'a | non (probable) | ERC 2025, Soar et al. (résumé PubMed) (2025) |
| LOT_2-004 | 🟧 | `coloscopie_totale_avec_biopsies` | La date d'entrée en vigueur est fausse : la teneur actuelle de l'article 12e lettre d (50 à 74 ans) résulte de l'ordonnance du DFI du 4 juin 2025 et vaut depuis le 1er juillet 2025 (RO 2025 419). Le 1er juillet 2026 n'est que la d | oui | OPAS (RS 832.112.31), art. 12e let. d, état au 1er juillet 2026 (2026) |
| LOT_2-005 | 🟧 | `colposcopie` | L'avis d'experts n° 50 (2018) est remplacé depuis le 30 juin 2026 par l'avis d'experts n° 97 de la SSGO (Empfehlungen für die Gebärmutterhalskrebsvorsorge, avec algorithmes de juin 2026). La fiche cite cinq fois l'avis remplacé. | oui | SSGO, avis d'experts n° 97, Empfehlungen für die Gebärmutterhalskrebsv (2026) |
| LOT_2-006 | 🟧 | `colposcopie` | La règle « écart de plus de deux niveaux » vient de l'avis n° 50 remplacé. L'algorithme 7 de l'avis n° 97 (page en image, lue visuellement, sans texte extractible) prévoit, après un frottis ASC-H ou HSIL avec colposcopie et histol | oui | SSGO, algorithmes de l'avis d'experts n° 97 (2026) |
| LOT_2-007 | 🟧 | `courbes_de_croissance` | Depuis le 15 juin 2026, pédiatrie suisse recommande de nouvelles courbes de croissance nationales (Swiss Growth References 2025) qui remplacent celles de 2011 (Braegger et al.). Les seuils du surpoids et de l'obésité ne sont plus  | oui | pédiatrie suisse, communiqué sur les nouvelles courbes de croissance (2026) |
| LOT_2-008 | 🟧 | `courbes_de_croissance` | La phrase présente les courbes de 2011 comme la référence actuelle, alors que pédiatrie suisse les déclare dépassées et recommande de nouvelles courbes depuis le 15 juin 2026. | oui | pédiatrie suisse, communiqué sur les nouvelles courbes de croissance (2026) |
| LOT_3-001 | 🟥 | `ecg_12_derivations_en_moins_de_10_minute` | L'article de Vivaldo et al. (Rev Med Suisse 2021;17(728):424-428) traite de l'insuffisance cardiaque ; son seul passage sur l'ECG (cité en preuve) ne dit rien de l'infarctus ni du syndrome coronarien aigu. L'affirmation est médica | oui | Rev Med Suisse, Vivaldo et al., Insuffisance cardiaque en 2021 (2021) |
| LOT_3-002 | 🟥 | `ecg_12_derivations` | Vivaldo et al. écrivent seulement que l'ECG est aspécifique et que plus de 90 % des insuffisants cardiaques n'ont pas un ECG normal ; ils ne disent pas qu'un tracé normal n'exclut ni un syndrome coronarien ni une cardiomyopathie. | oui | Rev Med Suisse, Vivaldo et al., Insuffisance cardiaque en 2021 (2021) |
| LOT_3-003 | 🟧 | `ebus_avec_ponction_ganglionnaire` | La recommandation ESGE/ERS/ESTS de 2015 (Vilmann et al.) est remplacée par la recommandation ERS/ESGE/ESTS 2026 (Korevaar et al., Eur Respir J 2026;68:2600097), qui ne recommande plus la médiastinoscopie de complément après une en | oui | ERS/ESGE/ESTS, Korevaar et al., Eur Respir J (résumé PubMed) (2026) |
| LOT_3-004 | 🟧 | `ebus_et_eus` | Même recommandation de 2015 remplacée par la version ERS/ESGE/ESTS 2026 (Korevaar et al.), qui ne recommande plus la médiastinoscopie de complément après une endosonographie négative. Le point 3 de l'interprétation portait la même | oui | ERS/ESGE/ESTS, Korevaar et al., Eur Respir J (résumé PubMed) (2026) |
| LOT_3-006 | 🟧 | `echelle_de_depression_geriatrique` | La page de cotation de Yesavage (Stanford) écrit « Scores > 10 » : le seuil est strictement supérieur à 10, et non « 10 ou plus ». La borne fausse figurait à trois endroits. | oui | Université Stanford, Yesavage, GDS Short Form English Scoring (page en ligne, consultée en 2026) |
| LOT_4-003 | 🟧 | `echo_endoscopie_oesophagienne` | L'article cité (Castro Soares et al., Rev Med Suisse 2015;11:1587) ne décrit aucun aspect écho-endoscopique : les mots « épaississement » et « musculeuse » n'y figurent pas. Il dit seulement qu'une suspicion de pseudo-achalasie im | oui | Castro Soares et al., Rev Med Suisse (2015) |
| LOT_4-005 | 🟧 | `enmg_du_nerf_phrenique` | Chen et al. (25 sujets sains, 50 nerfs) rapportent une latence moyenne de 6,54 ms (écart-type 0,77), non de 7,44 ms. Avec 7,44 ms, la moyenne normale frôle la limite supérieure de 8,0 ms et fausse la lecture d'un tracé. Le texte d | oui | Clin Pract, valeurs de référence du nerf phrénique (tableau comparatif (2025) |
| LOT_5-001 | 🟥 | `examen_de_la_sensibilite_perineale_et_du` | L'article cité (Mazzola et Motamed, Rev Med Suisse 2013, relu en entier) ne décrit pas ce tableau : il ne mentionne ni anesthésie en selle ni trouble vésical, seulement l'examen de la sensibilité périanale et glutéale et du tonus  | oui | HUG, Service de médecine de premier recours, stratégie Lombalgie aiguë (2022) |
| LOT_5-002 | 🟧 | `examen_de_la_sensibilite_perineale_et_du` | La fiche ne dit pas qu'un examen périnéal normal n'exclut pas un syndrome de la queue de cheval : le GIRFT (2023), cité par la fiche, l'écrit expressément. L'omission expose à une fausse réassurance devant une urgence chirurgicale | oui | GIRFT et NHS England, National Suspected Cauda Equina Syndrome Pathway (2023) |
| LOT_5-008 | 🟧 | `fond_d_oeil` | L'AAO a publié une édition 2025 de ce PPP (Wallace et al., Ophthalmology 2026), qui remplace celle de 2020. Le texte intégral de l'édition 2025 n'a pas pu être lu : il n'est pas prouvé qu'elle reprend la phrase citée, donc le mill | non (probable) | AAO, Comprehensive Adult Medical Eye Evaluation PPP 2025 (page de prés (2025) |
| LOT_6-005 | 🟧 | `lampe_a_fente` | Le PPP 2020 (Chuck et al., Ophthalmology 2021) est remplacé par le PPP 2025 (Wallace et al., Ophthalmology 2026, mis en ligne en février 2026). Le texte intégral 2025 n'a pas pu être lu (aaojournal.org 403) : la reprise du même co | non (probable) | AAO, Comprehensive Adult Medical Eye Evaluation PPP (page officielle) (2025) |
| LOT_7-001 | 🟥 | `oesophagogastroduodenoscopie_avec_biopsi` | Attribution fausse : l'article de Soares et al. ne décrit pas cet aspect endoscopique (œsophage dilaté avec stase, cardia serré). Il dit seulement que l'endoscopie est indispensable pour éliminer les diagnostics différentiels et p | oui | Soares et al., Rev Med Suisse (2015) |
| LOT_7-002 | 🟧 | `mediastinoscopie` | La recommandation de 2015 est remplacée par la recommandation ERS/ESGE/ESTS de 2026 (Korevaar et al., Eur Respir J 2026;68:2600097), qui ne recommande plus la médiastinoscopie de complément après une échoendoscopie négative. | oui | ERS/ESGE/ESTS, Korevaar et al., Eur Respir J (résumé PubMed) (2026) |
| LOT_7-003 | 🟧 | `mediastinoscopie` | Même recommandation obsolète : la place « après une endosonographie négative » n'est plus recommandée en 2026 ; l'échoendoscopie est recommandée plutôt que la médiastinoscopie. | oui | ERS/ESGE/ESTS, Korevaar et al., Eur Respir J (résumé PubMed) (2026) |
| LOT_7-004 | 🟧 | `manometrie_oesophagienne_haute_resolutio` | Définitions de glossaire fausses pour des sigles homonymes : dans cette fiche, II et III désignent les types d'achalasie de la classification de Chicago, non un rapport d'ophtalmologie ni un nerf crânien. L'infobulle affichait don | oui | Classification de Chicago 4.0, Yadlapati et al., Neurogastroenterol Mo (2021) |
| LOT_8-001 | 🟧 | `peak_flow` | La fiche cite trois fois le rapport GINA 2024, remplacé par les rapports 2025 puis 2026 (Strategy Report 2026 publié en mai 2026). Le seuil de 10 % chez l'adulte, la durée d'une à deux semaines et la référence à la meilleure valeu | oui | GINA, Global Strategy for Asthma Management and Prevention (Strategy R (2026) |
| LOT_8-002 | 🟧 | `ph_metrie_et_impedancemetrie_de_24_h` | Les trois citations renvoient au consensus de Lyon de 2018, remplacé par le consensus de Lyon 2.0 (Gyawali et al., Gut 2024). Les seuils (plus de 6 % : reflux prouvé ; moins de 4 % : normal ; hypersensibilité si exposition normale | oui | Consensus de Lyon 2.0, Gyawali et al., Gut (2024) |
| LOT_8-003 | 🟧 | `ph_metrie_et_impedancemetrie_de_24_h` | La fiche reprend fidèlement une imprécision de l'article cité (« score de corrélation pH-symptômes […] (score de Demeester) »), mais la définition est fausse : le score de DeMeester est un score composite de six paramètres d'expos | oui | Lata et al., Gastroenterol Rep (Oxf) (2023) |
| LOT_8-004 | 🟧 | `panendoscopie_orl` | La 5e édition des recommandations britanniques (Mackenzie et al., 2016) est remplacée par la 6e édition (Homer et Winter, J Laryngol Otol 2024), qui ne se borne plus à constater le peu de preuves : elle recommande de ne pas biopsi | oui | Head and Neck Cancer: UK National Multidisciplinary Guidelines, Sixth  (2024) |
| LOT_8-006 | 🟧 | `potentiels_evoques_somesthesiques` | La fiche présente les PES comme l'examen de référence de la radiculopathie sensitive, puis écrit à la phrase suivante que leur utilité diagnostique dans la sciatique est généralement jugée faible : le niveau d'indication est faux  | oui | Pape, Eldevik et Vandvik, Eur Spine J (résumé) (2002) |
| LOT_8-007 | 🟧 | `potentiels_evoques_somesthesiques_et_mot` | Les potentiels évoqués ne sont pas l'examen de référence de la myélopathie cervicale : selon la source citée par la fiche (WFNS, 2019), ils apportent une information complémentaire à la clinique et à la neuro-imagerie et ne donnen | oui | WFNS Spine Committee, Zileli et al., Neurospine (2019) |
| LOT_9-001 | 🟧 | `rectosigmoidoscopie` | La date d'entrée en vigueur est fausse : la teneur actuelle de l'art. 12e let. d OPAS est en vigueur depuis le 1er juillet 2025 (RO 2025 419) ; le 1er juillet 2026 n'est que la date d'état du texte consolidé. | oui | OPAS (RS 832.112.31), art. 12e let. d, état le 1er juillet 2026, Fedle (2026) |
| LOT_9-002 | 🟧 | `spirometrie_avec_test_de_bronchodilatati` | Le rapport GOLD 2025 est remplacé : le rapport GOLD 2027 (publié en novembre 2026) est la version en vigueur ; le critère (VEMS/CVF < 0,7 après bronchodilatateur) y est inchangé. | oui | GOLD, Global Strategy for Prevention, Diagnosis and Management of COPD (2026) |
| LOT_9-003 | 🟧 | `spirometrie_avec_test_de_bronchodilatati` | Le rapport GINA 2024 est remplacé : le rapport GINA 2026 est la version en vigueur ; il maintient explicitement le critère d'au moins 12 % et 200 ml face au critère ERS/ATS 2022. | oui | GINA, Global Strategy for Asthma Management and Prevention (2026) |
| LOT_10-001 | 🟥 | `test_anesthesique_sous_acromial` | Attribution fausse répétée six fois. La source existe et elle est bien datée, mais elle ne consacre qu'une ligne au test (« Event. test d'infiltration sous-acromiale par des anesthésiques locaux (test de Neer) », § 5.2) : elle ne  | oui | Ligue suisse contre le rhumatisme, Update Rhumatologie 2026 « Douleurs (2026) |
| LOT_10-002 | 🟧 | `test_de_stimulation_a_l_arginine_copepti` | La fiche ne donne que le seuil unique de 3,8 pmol/l (Winzeler 2019), dont l'essai de validation CARGOx, qu'elle cite, montre la précision insuffisante (74,4 %). Le même essai propose deux seuils de décision à haute spécificité (au | oui | Refardt et al., N Engl J Med (résumé PubMed) (2023) |
| LOT_10-003 | 🟧 | `test_de_schirmer` | Le rapport TFOS DEWS II (2017) a été révisé par le rapport TFOS DEWS III (Wolffsohn et al., Am J Ophthalmol 2025), que la fiche ignore. La version 2025 décrit le test de Schirmer comme un test invasif du volume lacrymal et n'en re | oui | TFOS DEWS III: Diagnostic Methodology, Wolffsohn et al., Am J Ophthalm (2025) |
| LOT_11-001 | 🟥 | `test_de_stimulation_a_la_secretine` | Attribution fausse : la recommandation UEG 2025 dit l'inverse (énoncé 2.6) : les tests directs ne doivent pas servir au diagnostic de l'insuffisance pancréatique exocrine en pratique clinique, car ils mesurent la sécrétion et non  | oui | UEG, Dominguez-Muñoz et al., European guidelines for the diagnosis and (2025) |
| LOT_11-002 | 🟥 | `test_de_stimulation_a_la_secretine` | Même attribution fausse : selon l'UEG 2025, les tests directs invasifs ne s'appliquent pas au diagnostic de l'insuffisance pancréatique exocrine. | oui | UEG, Dominguez-Muñoz et al., European guidelines for the diagnosis and (2025) |
| LOT_11-004 | 🟧 | `tests_de_provocation` | La fiche ne cite aucune contre-indication de l'épreuve, alors que le test avec le médicament suspect est contre-indiqué après une toxidermie grave (syndrome de Stevens-Johnson, nécrolyse épidermique toxique, DRESS, PEAG) selon la  | oui | Barbaud et al., EAACI/ENDA position paper on drug provocation testing, (2024) |
| LOT_11-006 | 🟧 | `tests_iteratifs_de_latence_d_endormissem` | La classification citée (ICSD-3, 2014) est remplacée par son texte révisé, l'ICSD-3-TR (AASM, 2023), version en vigueur ; les seuils du test (latence ≤ 8 minutes, au moins 2 SOREMP) y sont inchangés. | oui | Present and Future of Central Disorders of Hypersomnolence, J Sleep Re (2025) |
| LOT_11-007 | 🟥 | `trichogramme` | Attribution fausse : pour Serrano-Falcón et al., l'effluvium anagène montre des cheveux anagènes normaux au trichogramme, et les cheveux dystrophiques sont fréquents dans l'alopécie androgénétique ou après un arrachage incorrect. | oui | Serrano-Falcón et al., Hair and Scalp Evaluation: The Trichogram, Acta (2013) |
| LOT_11-008 | 🟧 | `trichogramme` | Argument diagnostique contraire à la source de la fiche : dans l'effluvium anagène, le test de traction est fortement positif et le trichogramme montre une prédominance de cheveux anagènes normaux. | oui | Serrano-Falcón et al., Hair and Scalp Evaluation: The Trichogram, Acta (2013) |
| LOT_12-001 | 🟧 | `video_head_impulse_test` | La fiche laisse croire qu'un vHIT anormal écarte l'AVC. La Bárány Society précise qu'un petit infarctus cérébelleux (flocculus) peut aussi donner un test d'impulsion pathologique : un test anormal n'exclut pas un AVC, diagnostic à | oui | Strupp et al., Bárány Society, J Vestib Res 2022 (2022) |

## Familles d'erreurs récurrentes

- **Attribution fausse** : une source réelle (souvent un article de la Revue Médicale Suisse ou une ligue) est citée pour une phrase qu'elle ne contient pas ; le fond médical est en général exact.
- **Recommandation remplacée** : version 2025-2026 parue après la rédaction (GINA 2026, GOLD 2027, Lyon 2.0, ERS/ESGE/ESTS 2026, SSGO n° 97, courbes de croissance suisses 2026, ESPEN 2023).
- **Glossaire homonyme** : sigle défini pour un autre domaine (II, III, T1, C5, ACR, GAD, AAO).
- **« Examen de référence » abusif** et **omission « un examen normal n'exclut pas »** pour un diagnostic à ne pas manquer.
- **Date d'entrée en vigueur suisse** confondue avec la date d'état du texte consolidé (art. 12e let. d OPAS).

## Points à vérifier (72)

- `actimetrie` — Durée de 7 à 14 jours d'actimétrie avant un TILE, attribuée à Smith et al. (AASM, 2018) : le résumé confirme l'indication mais pas la durée. → Smith et al., J Clin Sleep Med 2018;14(7):1231-1237, texte intégral (PMC6040807, doi 10.5664/jcsm.7230), et protocole TILE de l'AASM (Krahn et al., 2021)
- `actimetrie` — L'actimétrie serait « souvent plus sensible qu’un agenda seul » et « peut s’écarter de la polysomnographie », affirmations attribuées à Smith et al. (AASM, 2018). → Smith et al., J Clin Sleep Med 2018;14(7):1231-1237, texte intégral, sections insomnie et hypersomnolence
- `acuite_visuelle` — L'acuité visuelle « se mesure à chaque visite de suivi », selon l'AAO (PPP décollement postérieur du vitré et déchirures rétiniennes, 2024) : la source existe et date de 2024, le passage n'a pas été l → AAO PPP 2024, Ophthalmology 2025;132(4):P163-P196, section Follow-up evaluation (aao.org, doi 10.1016/j.ophtha.2024.12.023)
- `acuite_visuelle` — Le champ visuel et l'examen du nerf optique « font partie du bilan initial du glaucome », selon l'EGS (6e édition, 2025) : la source existe et date de 2025, le passage n'a pas été lu. → EGS, Terminology and guidelines for glaucoma, 6th Edition, Br J Ophthalmol 2025;109(Suppl 1), chapitre sur l'examen du patient
- `agenda_du_sommeil` — Rôle de l'agenda du sommeil associé à l'actimétrie et écarts agenda/actimétrie/polysomnographie, attribués à Smith et al. (AASM, 2018) : le résumé ne parle pas de l'agenda. → Smith et al., J Clin Sleep Med 2018;14(7):1231-1237, texte intégral (PMC6040807)
- `anuscopie` — Affirmations attribuées à l'ESCP 2020 (voir tout le canal anal pour diagnostiquer et classer ; écarter une autre pathologie anale ; coexistence possible d'un cancer ou d'une MICI) : la source existe e → van Tol et al., European Society of ColoProctology: guideline for haemorrhoidal disease, Colorectal Dis 2020;22:650-662, section « symptoms, diagnosis and classification » (doi 10.1111/codi.14975)
- `bilan_de_deglutition` — Descriptions de la vidéofluoroscopie et de la FEES (résidus, stase des sécrétions, phases vues par chaque examen) attribuées à « ESO et ESSD, 2021 » : la source existe et date de 2021, le détail n'a p → Dziewas et al., ESO and ESSD guideline for the diagnosis and treatment of post-stroke dysphagia, Eur Stroke J 2021;6(3):LXXXIX-CXV, partie « dysphagia assessment » (PMC8564153)
- `bilan_neuropsychologique` — Seuil MoCA de 26 points attribué à « Swiss Memory Clinics 2024 » : le chapitre 5 lu ne donne pas de seuil fixe (constat LOT_1-001). → Recommandations de Swiss Memory Clinics pour le diagnostic des troubles cognitifs – mise à jour, Praxis 2025;114(4):127-136 (doi 10.23785/PRAXIS.2025.04.002), partie tests neuropsychologiques
- `capacite_de_diffusion_du_co` — « Selon l'ERS/ATS (Stanojevic et al., 2022), une DLCO inférieure à la LIN, corrigée pour l'hémoglobine, est anormale » : seuil non relu dans le texte intégral (le résumé ne le donne pas). → Stanojevic S et al., Eur Respir J 2022;60:2101499, section sur l'interprétation de la DLCO (limites 5e percentile, z-score).
- `capnographie` — Maintien, dans les recommandations ERC 2025, du critère « tracé de CO2 persistant après six ventilations », du seuil pronostique de 1,33 kPa et de l'absence de seuil d'arrêt. → ERC Guidelines 2025 Adult Advanced Life Support (Soar et al., Resuscitation 2025;215 Suppl 1:110769), sections « Airway and ventilation » et « Waveform capnography during ALS » ; liens depuis erc.edu.
- `cardiotocographie` — « Le consensus FIGO de 2015 prévoit une réévaluation au moins toutes les 30 minutes » : non retrouvé dans les sources lues. → Ayres-de-Campos D et al., FIGO consensus guidelines on intrapartum fetal monitoring: Cardiotocography, Int J Gynecol Obstet 2015;131:13-24, section « Clinical decision ».
- `cardiotocographie` — Durée de la variabilité réduite (plus de 50 minutes) : confirmée par une source secondaire, mais une autre source secondaire (PMC5139811) écrit « >15 min » ; à trancher sur le tableau 1 du texte origi → Ayres-de-Campos D et al., Int J Gynecol Obstet 2015;131:13-24, tableau 1.
- `catheterisme_des_veines_surrenaliennes` — Attribution des seuils chiffrés (indice de latéralisation ≥ 4 et < 3, freination controlatérale < 1, sélectivité) au texte même de la recommandation Endocrine Society 2025 : valeurs confirmées par des → Adler GK et al., Primary Aldosteronism: An Endocrine Society Clinical Practice Guideline, J Clin Endocrinol Metab 2025, remarques techniques sur le cathétérisme des veines surrénaliennes.
- `colposcopie` — Contenu des algorithmes 7 (ASC-H/HSIL : colposcopie dans les 6 semaines, biopsie, curetage endocervical si zone de transformation de type 3, colloque multidisciplinaire si colposcopie et histologie no → SSGO, « Algorithmen zum Expertenbrief Empfehlungen für die Gebärmutterhalskrebsvorsorge », juin 2026, pages 7 et 8 (sggg.ch, Expertenbriefe, n° 97) ; version française de l'avis à paraître.
- `controle_de_pacemaker_et_de_defibrillate` — Attribution à « l'ESC (stimulation cardiaque, 2021) » des énoncés techniques (seuil qui monte, impédance très basse = rupture d'isolant, impédance très haute = fracture, indicateur de remplacement) :  → Glikson M et al., 2021 ESC Guidelines on cardiac pacing and cardiac resynchronization therapy, Eur Heart J 2021;42:3427-3520, section sur le suivi des dispositifs et données supplémentaires.
- `cortisol_salivaire_nocturne_et_cortisol_` — Énoncés attribués à l'ESE/ENSAT 2023 sur le cortisol salivaire nocturne et le cortisol libre urinaire (le plus souvent dans l'intervalle de référence sans Cushing patent ; un résultat pathologique ind → Fassnacht M et al., Eur J Endocrinol 2023;189:G1-G42, chapitre sur l'évaluation de l'excès de cortisol (recommandations sur la MACS).
- `cpre_avec_brossage` — « Selon l'ESGE 2025, une cytologie négative n'exclut pas un cancer » et reprise par l'ESGE 2025 des chiffres 40 % / 66 % (21 études) : seul le résumé de l'ESGE 2025 a été lu ; les chiffres sont prouvé → Facciorusso et al., Diagnostic work-up of bile duct strictures: ESGE Guideline, Endoscopy 2025;57(2):166-185, doi 10.1055/a-2481-7048, section sur les prélèvements par CPRE
- `ecg_12_derivations` — « pendant au moins 30 secondes, posent le diagnostic selon l'ESC (fibrillation auriculaire, 2024) » : la durée de 30 s est la définition de consensus (prouvée par une source secondaire), mais le libel → Van Gelder et al., 2024 ESC Guidelines for the management of atrial fibrillation, Eur Heart J 2024;45:3314-3414, tableau des définitions (« clinical AF »)
- `ecg_12_derivations` — « un bloc complet, qui relève d'une stimulation, selon l'ESC (stimulation cardiaque, 2021) » : attribution non relue dans le texte de la recommandation. → Glikson et al., 2021 ESC Guidelines on cardiac pacing and cardiac resynchronization therapy, Eur Heart J 2021;42:3427-3520, section 5.2 (bloc auriculo-ventriculaire)
- `ecg_12_derivations_en_moins_de_10_minute` — « On le répète si les symptômes reviennent ou si le diagnostic reste incertain, selon l'ESC (syndromes coronariens aigus, 2023) » : non relu dans le texte de la recommandation. → Byrne et al., 2023 ESC Guidelines for the management of acute coronary syndromes, Eur Heart J 2023;44:3720-3826, section 3.2 (électrocardiogramme)
- `ecg_12_derivations_en_moins_de_10_minute` — « ce bloc complet relève d'une stimulation, selon l'ESC (stimulation cardiaque, 2021) » : attribution non relue. → Glikson et al., 2021 ESC Guidelines on cardiac pacing, Eur Heart J 2021;42:3427-3520, section 5.2
- `echelle_d_epworth` — Attributions à la SSSSC (2017) : score d'Epworth ≥ 15 ou index d'apnées-hypopnées > 30/h non maîtrisé → centre accrédité et test de maintien de l'éveil ; un score bas n'exclut pas une somnolence au vo → Mathis J, Kohler M, Hemmeter UM, Seeger R. Fahreignung bei Tagesschläfrigkeit (recommandations SSSSC), Swiss Medical Forum 2017;17(20):442-447 ; site swiss-sleep.ch
- `echelle_d_epworth` — Attributions à la SSSSC (2020) : seuil > 10 retenu, avec un index d'apnées-hypopnées > 5/h, dans la définition épidémiologique du syndrome ; somnolence mal corrélée à l'index. Le seuil > 10 lui-même e → Document SSSSC de 2020 sur les apnées du sommeil (référence à préciser dans la fiche), site swiss-sleep.ch, rubrique recommandations
- `echo_endoscopie` — Attribution « Selon l'ESMO 2022 » des chiffres 91 %/77 %, 82 %/41 %, 49 % et du rôle pour le stade N : les chiffres sont exacts (méta-analyse de Nie et al., 2017, relue), mais le texte ESMO n'a pas pu → Lordick et al., Gastric cancer: ESMO Clinical Practice Guideline, Ann Oncol 2022;33:1005, section « Staging and risk assessment » (annalsofoncology.org, PMID 35914639)
- `echo_endoscopie_rectale` — Attributions « selon l'ESMO 2025 » : écho-endoscopie recommandée pour distinguer cT1 de cT2 ; mésorectum et compartiment latéral mal évalués ; non recommandée pour le re-stadage après traitement néoad → Hofheinz et al., Localised rectal cancer: ESMO Clinical Practice Guideline, Ann Oncol 2025;36 (PMID 40412553), section « Staging and risk assessment »
- `electroneuromyographie` — Chiffres attribués à Cho et al. 2010 : sensibilité 47,8 % et spécificité 87,5 % (fibrillations d'un myotome) ; sensibilité 30,4 % et spécificité 100 % (quatre muscles paravertébraux ou plus) ; niveaux → Cho SC et al., Muscle Nerve 2010;42:276-82, texte intégral (doi 10.1002/mus.21759), tableaux des études de classe II
- `enmg` — Toutes les attributions « selon Ochsner et Kuntzer (Correspondances en Nerf et Muscle, 2004 ; CHUV, Lausanne) », dont le critère de positivité et « la recherche d'un bloc de conduction est souvent vai → Ochsner F, Kuntzer T, Correspondances en Nerf et Muscle 2004 (Edimark) ; à défaut Ochsner et al., Rev Med Suisse 2022;18:794-8, texte intégral (revmed.ch, accès abonné)
- `enmg` — Attribution « selon la Ligue suisse contre le rhumatisme (update Douleurs de l'épaule, 2026) » pour le syndrome de Parsonage et Turner. → Ligue suisse contre le rhumatisme, publication destinée aux professionnels « update Douleurs de l'épaule » (ligues-rhumatisme.ch, rubrique Professionnels)
- `enregistreur_d_evenements_et_moniteur_im` — Attributions « selon l'ESC (syncope, 2018) » : rythme sinusal pendant le symptôme écarte une cause rythmique ; asystolie pendant la syncope = diagnostic et indication de stimulation ; tachycardie vent → Brignole et al., 2018 ESC Guidelines for the diagnosis and management of syncope, Eur Heart J 2018;39:1883, sections 4.2.4 (monitorage ECG) et 5.4 (stimulation)
- `enteroscopie_a_double_ballon` — Attribution à l'ECCO-ESGAR-ESP-IBUS 2025 : examen complet du grêle chez 44 à 80 % des patients dans les centres expérimentés ; retrait d'un corps étranger. → Kucharzik et al., ECCO-ESGAR-ESP-IBUS Guideline on Diagnostics and Monitoring of Patients with IBD, Part 1, J Crohns Colitis 2025 (PMID 40741688), section sur l'entéroscopie assistée
- `examen_des_nerfs_craniens` — Quatre attributions aux critères de pertinence de l'ACR (neuropathies crâniennes, mise à jour 2022) : atteinte du front = périphérique, front épargné = supranucléaire, signes associés = tronc cérébral → ACR Appropriateness Criteria Cranial Neuropathy: 2022 Update, J Am Coll Radiol 2022;19(11S):S266-S303 (PMID 36436957), section sur le nerf facial (variante VII) ; texte narratif sur acsearch.acr.org/d
- `fond_d_oeil` — Hémorragies, exsudats ou œdème papillaire rendent l'examen positif chez l'hypertendu, selon les recommandations ESC 2024 sur l'hypertension. → McEvoy et al., 2024 ESC Guidelines for the management of elevated blood pressure and hypertension, Eur Heart J 2024;45:3912-4018, section sur l'atteinte d'organes liée à l'hypertension (fond d'œil) ; 
- `fond_d_oeil` — Le segment postérieur révèle des signes d'hypertension, de diabète, d'infection, de vascularite et d'hypertension intracrânienne, selon l'AAO (PPP, 2020) ; une édition 2025 existe (constat LOT_5-008). → AAO, Comprehensive Adult Medical Eye Evaluation PPP 2025 (Wallace et al., Ophthalmology 2026, PMID 41670577), section « Fundus examination »
- `fond_d_oeil` — L'autofluorescence et l'échographie aident à distinguer les drusens enfouis, selon le consortium ODDS (2018) (constat LOT_5-009). → Malmqvist et al., The Optic Disc Drusen Studies Consortium Recommendations for Diagnosis of Optic Disc Drusen Using Optical Coherence Tomography, J Neuroophthalmol 2018;38(3):299-307 (PMID 29095768), 
- `gastroscopie_avec_biopsies` — Selon Maastricht VI (2022) : au moins deux biopsies de l'antre et deux du fundus (la fiche écrit « fundus », l'ESGE écrit « corps »), dans des pots séparés ; une biopsie de l'incisure permet le stade  → Malfertheiner et al., Management of Helicobacter pylori infection: the Maastricht VI/Florence consensus report, Gut 2022;71:1724-1762 (PMID 35944925), groupe de travail 2 (diagnostic), énoncés sur les
- `gastroscopie_avec_biopsies` — Selon Maastricht VI (2022), la gastrite atrophique se classe par OLGA ou OLGIM. → Même document (Gut 2022;71:1724-1762), énoncés sur la stadification histologique
- `gonioscopie` — Contact irido-trabéculaire sur au moins 180° = angle à risque de fermeture, selon l'EGS, 6e édition (2025) : définition vérifiée dans la 5e édition (2020) et dans le PPP de l'AAO, mais le texte de la  → European Glaucoma Society, Terminology and Guidelines for Glaucoma, 6th Edition, Br J Ophthalmol 2025;109(Suppl 1):1-212 (PMID 41026937), chapitre 2, classification de la fermeture primitive de l'angl
- `gonioscopie` — Indentation, pièce sombre et faisceau court de 1 mm, selon l'AAO (PPP fermeture primitive de l'angle, 2025) : phrases vérifiées mot pour mot dans l'édition approuvée en 2015, la page de l'édition 2025 → AAO, Primary Angle-Closure Disease Preferred Practice Pattern 2025 (Gedde et al., Ophthalmology 2026, PMID 41665581), section « Gonioscopy »
- `index_de_pression_systolique_et_tcpo2` — Attribution du seuil IPS ≤ 0,9 à la ligne directrice S2k de la DGPL sur l'ulcère veineux (Valesky et al., 2024) ; argument « Ulcère mixte : IPS entre 0,5 et 0,9 » (diagnostics[1]) non attribué. La val → AWMF, registre 037-009, version longue du 22.01.2024 (register.awmf.org/assets/guidelines/037-009l_S2k_Diagnostik-Therapie-Ulcus-cruris-venosum__2024-01.pdf), chapitre diagnostic artériel ; ou J Dtsch
- `lampe_a_fente` — Les deux phrases attribuées au PPP de l'AAO « 2020 » : le PPP 2025 (Wallace et al.) l'a remplacé ; vérifier qu'il décrit toujours les structures examinées à la lampe à fente et la limite derrière l'ir → AAO, Comprehensive Adult Medical Eye Evaluation PPP 2025, Ophthalmology 2026;133(4):P202-P236, doi 10.1016/j.ophtha.2025.12.031, section « Examination »
- `lampe_a_fente` — Seuil « plus d'une cellule » : le tableau SUN original donne le grade 0 pour moins d'une cellule et 0,5+ pour 1 à 5 cellules (lu seulement dans une source secondaire). → Jabs et al., Am J Ophthalmol 2005;140:509-516, tableau de gradation des cellules de chambre antérieure (PMC8935739)
- `lampe_de_wood` — Attribution à Klatte et al. (2015) de la fluorescence bleutée de la peau normale due au collagène du derme (fait confirmé par une autre revue). → Klatte JL et al., J Eur Acad Dermatol Venereol 2015;29:842-847, doi 10.1111/jdv.12860, section sur les principes de la fluorescence
- `lampe_de_wood` — Attribution à la BAD (Fuller et al., 2014) : la lampe de Wood reste négative dans la plupart des teignes à Trichophyton (fait confirmé par Dyer et Foy 2022). → Fuller LC et al., Br J Dermatol 2014;171:454-463, doi 10.1111/bjd.13196, section « Diagnosis – Wood's light »
- `laparoscopie_diagnostique` — Place de la laparoscopie avec ou sans biopsie péritonéale dans la branche SAAG < 11 g/l de l'approche diagnostique de l'AASLD 2021 (après cytologie, mycobactéries ou ADA, imagerie). → Biggins SW et al., Hepatology 2021;74:1014-1048, doi 10.1002/hep.31884, figure de l'approche diagnostique de l'ascite
- `laparoscopie_diagnostique` — « L'EASL 2018 ne la mentionne pas dans le bilan standard de l'ascite liée à une cirrhose » : affirmation d'absence, à contrôler sur le texte intégral. → EASL Clinical Practice Guidelines for the management of patients with decompensated cirrhosis, J Hepatol 2018;69:406-460, doi 10.1016/j.jhep.2018.03.024, chapitre ascite
- `laryngoscopie_avant_et_apres_thyroidecto` — Quatre phrases attribuées à l'ATA 2015 : paralysie récurrentielle devant une corde immobile, compensation par l'autre corde avec voix normale, paralysie bilatérale exposant à la trachéotomie, corde im → Haugen BR et al., Thyroid 2016;26:1-133 (PMC4739132), recommandations sur l'évaluation préopératoire de la voix et la laryngoscopie
- `manoeuvre_de_dix_hallpike` — Rotation de la tête de 45° attribuée à la Bárány Society (von Brevern et al., 2015) : valeur non retrouvée dans les textes libres lus (latence, durée et direction du nystagmus sont confirmées). → von Brevern M et al., J Vestib Res 2015;25:105-117, doi 10.3233/VES-150553, notes du critère « canalolithiase du canal postérieur » ; à défaut AAO-HNSF, Bhattacharyya et al. 2017, description de la ma
- `manometrie_anorectale` — « Selon l'ESNM 2019, un trouble fonctionnel de la défécation ne se diagnostique pas sur un seul test : il faut au moins deux examens d'évacuation anormaux. » → Serra J et al., European society of neurogastroenterology and motility guidelines on functional constipation in adults, Neurogastroenterol Motil 2020;32:e13762 (doi:10.1111/nmo.13762), section sur les
- `manometrie_anorectale` — Attribution à l'ESNM 2019 de « un tracé de dyssynergie peut se voir chez des volontaires sains, à cause de la position peu physiologique, de la gêne ou de la crainte d'une incontinence » (le fait lui- → Serra J et al., Neurogastroenterol Motil 2020;32:e13762 (doi:10.1111/nmo.13762), section « anorectal manometry »
- `pachymetrie` — La cornée centrale mesure en moyenne 556 µm chez les sujets d'origine européenne, selon l'AAO (PPP glaucome primitif à angle ouvert, 2025). → AAO, Primary Open-Angle Glaucoma Preferred Practice Pattern 2025 (Gedde et al., Ophthalmology 2026;133(4):P1-P103, doi 10.1016/j.ophtha.2025.12.029), section « Central corneal thickness measurement ».
- `pachymetrie` — Une cornée fine, ou amincie après chirurgie réfractive, fait sous-estimer la pression au tonomètre de Goldmann, selon l'AAO (PPP 2025). → Même document AAO PPP 2025, sections « Central corneal thickness measurement » et « Intraocular pressure measurement ».
- `pachymetrie` — La pachymétrie n'apporte qu'un facteur de risque et ne pose aucun diagnostic, selon l'European Glaucoma Society (6e édition, 2025). → EGS, Terminology and guidelines for glaucoma, 6th Edition, Br J Ophthalmol 2025;109(Suppl 1):1-212 (doi 10.1136/bjophthalmol-2025-egsguidelines), chapitre sur l'examen du patient (pachymétrie).
- `plethysmographie` — Selon l'ERS/ATS (Stanojevic et al., 2022), une CPT inférieure à la LIN (5e percentile) définit le trouble ventilatoire restrictif ; une CPT supérieure à la LSN fait suspecter une distension ; un rappo → Stanojevic S et al., ERS/ATS technical standard on interpretive strategies for routine lung function tests, Eur Respir J 2022;60:2101499 (doi 10.1183/13993003.01499-2021), sections sur les volumes pul
- `refraction` — Définition de l'amétropie attribuée à l'AAO (rayons parallèles non focalisés sur la rétine de l'œil qui n'accommode pas) : la date « mise à jour 2025 » est vérifiée, mais la phrase elle-même n'a pas p → AAO, Refractive Errors Preferred Practice Pattern 2022 (mise à jour octobre 2025), section des définitions ; PDF sur aaojournal.org (Ophthalmology 2023;130:P1-P60, DOI 10.1016/j.ophtha.2022.10.031).
- `temps_de_saignement` — Non-occlusion rapportée au-delà de 300 s ; allongement sur collagène-épinéphrine sous aspirine ; allongement sur les deux cartouches dans la maladie de von Willebrand ; plaquettes < 100 G/l ou hématoc → Hayward CP et al., J Thromb Haemost 2006;4:312-9 (doi:10.1111/j.1538-7836.2006.01771.x), section « Results and discussion » et tableaux 1 et 2
- `temps_de_transit_colique` — Attributions à l'ESNM 2019 : marqueurs radio-opaques examen de référence du transit oro-anal, peu coûteux et disponible ; au moins la moitié des constipés fonctionnels sans trouble de l'évacuation ont → Serra J et al., European society of neurogastroenterology and motility guidelines on functional constipation in adults, Neurogastroenterol Motil 2020;32:e13762 (doi:10.1111/nmo.13762), énoncés sur le 
- `test_au_synacthene` — Attribution à « l'Endocrine Society 2016 » de : le test n'est pas le meilleur test d'une insuffisance secondaire récente, car la surrénale peut encore répondre. → Fleseriu M et al., Hormonal Replacement in Hypopituitarism in Adults: An Endocrine Society Clinical Practice Guideline, J Clin Endocrinol Metab 2016;101:3888-3921 (doi:10.1210/jc.2016-2118), section s
- `test_de_provocation_bronchique` — Attribution à l'ERS (Coates et al., 2017) du seuil PD20 > 400 µg et de la gradation de l'hyperréactivité (limite de 100 à 400 µg d'après une source secondaire, constat LOT_10-006) ; absence dans la fi → Coates AL et al., ERS technical standard on bronchial challenge testing, Eur Respir J 2017;49:1601526 (doi:10.1183/13993003.01526-2016), tableau d'interprétation de la PD20 et tableau des contre-indic
- `test_de_provocation_bronchique` — Disponibilité suisse de la méthacholine pour inhalation : aucune autorisation Swissmedic trouvée (produit à signaler s'il n'est disponible qu'en préparation hospitalière ou à l'importation). → swissmedicinfo.ch et compendium.ch, recherche « méthacholine » / « Provocholine »
- `test_de_schirmer` — Attribution au guide AAO-HNSF (Baugh et al., 2013) de la phrase « un Schirmer bas s'ajoute à une fermeture palpébrale incomplète » : le résumé lu ne mentionne que la protection oculaire en cas de ferm → Baugh RF et al., Clinical practice guideline: Bell's palsy, Otolaryngol Head Neck Surg 2013;149(3 Suppl):S1-27 (doi:10.1177/0194599813505967), énoncé 9 « Eye care »
- `test_de_stimulation_a_la_secretine` — Disponibilité en Suisse d'une sécrétine à usage diagnostique (aucune préparation autorisée repérée ; la recommandation UEG 2025 signale elle-même l'indisponibilité de la sécrétine dans de nombreux pay → AIPS Swissmedic (swissmedicinfo.ch), recherche par principe actif « sécrétine » ; pharmacie hospitalière HUG/CHUV
- `tests_de_personnalite_standardises` — Attribution à Butcher et Pope (1992) du seuil T ≥ 65 comme cliniquement significatif ; équivalence T 65 = 92e percentile attribuée à Pearson. → Butcher JN, Pope KS. Seven issues in conducting forensic assessments. Ethics Behav 1992 (kspope.com/assess/butcher.php) ; manuel MMPI-2 (Butcher et al., 2001), chapitre sur les notes T uniformes
- `tests_de_personnalite_standardises` — Borne de l'échelle VRIN : la fiche écrit « supérieure à 80 » ; une source secondaire lue (pmc:PMC11728051) retient un profil valide pour un T-score < 80, donc invalide dès 80 (≥ 80). → Manuel MMPI-2 (Butcher et al., 2001), échelles de validité ; diapositives de formation de l'University of Minnesota Press « Interpretation of MMPI-2 Validity Scales »
- `tests_de_personnalite_standardises` — Niveau de lecture requis « de sixième année » attribué à Pearson (la fiche produit Pearson lue ne le mentionne pas). → Manuel MMPI-2 (Butcher et al., 2001), conditions de passation ; fiche produit Pearson
- `tests_iteratifs_de_latence_d_endormissem` — Chiffres attribués à Littner et al. (2005) : sensibilité 0,78 et spécificité 0,93 de deux SOREMP ou plus ; latence des narcoleptiques 3,0 ± 3,1 minutes (une source secondaire lue, pmc:PMC4121261, donn → Littner MR et al. Practice parameters for clinical use of the MSLT and the MWT. Sleep 2005;28(1):113-21, section 4 ; Arand D et al. Sleep 2005;28(1):123-44
- `thoracoscopie` — Attribution à Opitz et al. (2020, ERS/ESTS/EACTS/ESTRO) des chiffres 92 %, 0,34 %, 1,8 % et 47 études : les chiffres sont exacts, mais leur origine est l'analyse groupée de la BTS 2010 (Rahman et al.) → Opitz I et al. Eur J Cardiothorac Surg 2020;58:1-24 (doi 10.1093/ejcts/ezaa158), section diagnostic ; Rahman NM et al. Thorax 2010;65(Suppl 2):ii54-60
- `thoracoscopie` — Cloisons fibrineuses traduisant un épanchement infecté ou ancien, selon la BTS (Roberts et al., 2023). → Roberts ME et al. British Thoracic Society Guideline for pleural disease. Thorax 2023;78(Suppl 3):s1-s42, section infection pleurale
- `thromboelastographie` — Faible détection de l'aspirine, des inhibiteurs du récepteur à l'ADP, des anticoagulants oraux directs à faible concentration et de la maladie de von Willebrand, selon BJA Education (2022). → Wells M, Raja M, Rahman S. Point-of-care viscoelastic testing. BJA Educ 2022;22(11):416-423 (PMC9596284), section limites
- `thromboelastographie` — Seuils ESAIC 2023 (≤ 1,5 g/l ; A5 > 12 mm) confirmés dans une source secondaire seulement ; à relire dans le texte original. → Kietaibl S et al. Eur J Anaesthesiol 2023;40:226-304 (doi 10.1097/EJA.0000000000001803), recommandations sur le fibrinogène et l'hémorragie du post-partum
- `timed_up_and_go_et_test_de_tinetti` — Borne de la vitesse de marche : la fiche écrit « 0,8 m/s ou moins » (≤) d'après Blain et al. (2023) ; le texte des recommandations mondiales 2022 lu écrit « < 0,8 m/s ». → Blain H et al. Geriatr Psychol Neuropsychiatr Vieil 2023;21(2):149-160 (doi 10.1684/pnv.2023.1108), algorithme de stratification ; Montero-Odasso et al. Age Ageing 2022, figure de l'algorithme
- `tonometrie` — Formulations attribuées à la 6e édition EGS (2025) : limite de 21 mmHg à deux écarts-types, seul facteur de risque traitable, pression normale n'excluant pas le glaucome ; vérifiées dans la 5e édition → European Glaucoma Society, Terminology and guidelines for glaucoma, 6th Edition, Br J Ophthalmol 2025;109(Suppl 1):1-212 (PMID 41026937), chapitre II.1.1
- `video_eeg` — Attribution à la recommandation ILAE-IFCN 2022 (Tatum et al.) des phrases « le diagnostic repose sur l'enregistrement d'un événement typique, avec ou sans corrélat EEG épileptique », « elle confirme u → Tatum WO et al., Epilepsia 2022;63(2):290-315, doi:10.1111/epi.16977 (ou Clin Neurophysiol 2022;134:111-128, doi:10.1016/j.clinph.2021.07.016), sections « Indications » et « Recommendations » ; texte 

## Sites bloqués (refus notés, non contournés)

- aao-hnsfjournals.onlinelibrary.wiley.com (403)
- aasm.org (403)
- academic.oup.com (403 (constaté au brief ; contourné par les dépôts institutionnels FLORE et ORBi))
- academic.oup.com (403) ×7
- acsearch.acr.org (200 (page applicative sans texte lisible))
- bjo.bmj.com (429) ×4
- boris-portal.unibe.ch (200 (page anti-robot Anubis, non lue))
- boris.unibe.ch (200 mais page anti-robot Anubis (cache inutilisable, non cité))
- compendium.ch (200 (contenu chargé par JavaScript, illisible))
- content.iospress.com (403)
- easl.eu (000 (délai))
- econtent.hogrefe.com (403)
- erj.ersjournals.com (403) ×5
- gettingitrightfirsttime.co.uk (200 (redirigé vers une page interactive sans le texte ; PDF lu sur spinal.co.uk))
- gut.bmj.com (403)
- hal.science (200 (page anti-robot Anubis, article non servi))
- hal.science (200 (page anti-robot Anubis, non lue))
- iris.who.int (200 (page JavaScript sans contenu ; copie OPS lue à la place))
- iris.who.int (200 (page JavaScript sans le PDF)) ×2
- jcsm.aasm.org (404)
- journals.lww.com (403) ×2
- journals.sagepub.com (403) ×2
- kspope.com (404)
- medicalforum.ch (000)
- medicalforum.ch (502 (hôte injoignable))
- obgyn.onlinelibrary.wiley.com (403)
- onlinelibrary.wiley.com (403) ×5
- pmc.ncbi.nlm.nih.gov (200 (page anti-robot, texte illisible))
- pmc.ncbi.nlm.nih.gov (200 (page sans contenu lisible))
- pmc.ncbi.nlm.nih.gov (200 mais page reCAPTCHA)
- pmid:5455571 (Jerger 1970, notice PubMed (sans résumé)
- portal.findresearcher.sdu.dk (403)
- publications.ersnet.org (403) ×2
- pure.amsterdamumc.nl (403)
- pure.au.dk (403)
- pure.eur.nl (403)
- register.awmf.org (200 mais page anti-robot Anubis (cache inutilisable, non cité))
- repositori.upf.edu (200 (page anti-robot, texte illisible ; non citée))
- research.birmingham.ac.uk (403)
- research.rug.nl (403)
- search.informit.org (403)
- smf.swisshealthweb.ch (502 (hôte injoignable))
- smf.swisshealthweb.ch (502)
- thorax.bmj.com (403)
- www.aaojournal.org (403) ×5
- www.aasld.org (410)
- www.annalsofoncology.org (403) ×2
- www.clinicalnutritionjournal.com (403)
- www.cprguidelines.eu (526)
- www.ebi.ac.uk (500 (article hors sous-ensemble libre ; idem PMC11090185, PMC5042313))
- www.ebi.ac.uk (500 (repli BioC NCBI lu))
- www.ebi.ac.uk (500 (repli BioC NCBI réussi)) ×2
- www.ebi.ac.uk (500) ×18
- www.endocrinepractice.org (403)
- www.escardio.org (403) ×4
- www.esge.com (404)
- www.esmo.org (200 sans contenu (page rendue par script))
- www.esmoopen.com (403)
- www.figo.org (403)
- www.hug-ge.ch (000 (pas de réponse ; lu sur www.hug.ch))
- www.ilae.org (403)
- www.journal-of-hepatology.eu (403)
- www.jthjournal.org (403)
- www.jto.org (403)
- www.liebertpub.com (403)
- www.ncbi.nlm.nih.gov (200 (page CAPTCHA, contenu non servi))
- www.ncbi.nlm.nih.gov (200 (page de contrôle reCAPTCHA, contenu non lu))
- www.ncbi.nlm.nih.gov (200 (page de contrôle reCAPTCHA, non lue))
- www.ncbi.nlm.nih.gov (200 (page reCAPTCHA))
- www.ncbi.nlm.nih.gov (200 (page reCAPTCHA, texte illisible)) ×2
- www.ncbi.nlm.nih.gov (200 (page sans contenu lisible))
- www.ncbi.nlm.nih.gov (200 (texte non lu par l'outil))
- www.ncbi.nlm.nih.gov (200 mais page reCAPTCHA)
- www.ncbi.nlm.nih.gov (non lu par l'outil (texte vide))
- www.ncbi.nlm.nih.gov (page non lisible (contenu vide))
- www.resuscitationjournal.com (403)
- www.sciencedirect.com (403)
- www.swiss-sleep.ch (000 (connexion réinitialisée))
- www.tara.tcd.ie (403)
- www.thieme-connect.de (200 (page anti-robot ; contourné par le PDF officiel esge.com))
- www.thieme-connect.de (200 (page de défi anti-robot, texte illisible))
- www.thieme-connect.de (200 (page vide sans JavaScript ; texte lu sur esge.com))
- www.thoracic.org (404)
- www.thyroid.org (403)
- www.upress.umn.edu (403)
- www.zora.uzh.ch (200 (page anti-robot Anubis, entrée de cache 214827ece64fad92 à ne pas citer))
- www.zora.uzh.ch (200 sans texte intégral (fichier non déposé))
- www.zora.uzh.ch (401)

## Skills chargés

medical-accuracy-100 · i-never-waste-token · medical-workout
