# Audit médical Tétrade : systèmes hématologique et infectieux (2026-11-24)

Claude a relu chaque chiffre, seuil, dose, voie, rythme et chaque palier (TF/F/U/R) de 45 pathologies hématologiques, de 17 pathologies infectieuses et immunitaires, de leurs organes, signes et glossaires, et des 24 scénarios des interprétations `he_anemie`, `he_fer`, `he_coag` et `ii_anticorps`. Les 22 champs `aVerifier` ont été confrontés aux sources primaires. Les paliers restent tous justes : aucun reclassement.

## 1. Bilan par système

| Système | Vérifiées | Corrigées | Doutes résolus | Doutes restants |
|---|---|---|---|---|
| Hématologique et oncologique (45 pathologies, 6 organes, glossaire) | 45 | 15 pathologies + contenu (réserve médullaire) + glossaire (SLiM ; PCV, PCV20, PCV21 ajoutés) | 11 sur 14 | 3 |
| Infectieux et immunitaire (17 pathologies, 4 organes, glossaire) | 17 | 8 pathologies + contenu (voie des lectines, CH50) + sémiologie (qSOFA) + glossaire (AP50, MASP ajoutés) | 4 sur 8 | 4 |
| Interprétations `he_` et `ii_` (4 fenêtres, 24 scénarios) | 24 | 3 | sans objet | 0 ; `_meta.statut` : **AUDITÉ** |

## 2. Erreurs de fond corrigées

| Pathologie ou élément | Erreur | Correction | Source |
|---|---|---|---|
| Syndrome myélodysplasique | Époétine limitée à 40 000 U/semaine ; darbépoétine « toutes les 2 semaines » | Époétine 30 000 à 80 000 U/semaine ou darbépoétine 150 à 300 µg/semaine ; ajout du luspatercept après échec des ASE (MDS-RS) | ESMO 2021 (Fenaux) ; Swissmedic Reblozyl n° 69592 |
| Carence en vitamine B12 | Entretien IM « chaque mois » sans préciser la molécule | Hydroxocobalamine 1 mg 3×/semaine 2 semaines, puis tous les 3 mois (tous les 2 mois si atteinte neurologique) | BSH 2014 (Devalia, Br J Haematol 166:496) |
| Nécrolyse épidermique toxique | Ciclosporine « 3 à 5 mg/kg pendant 7 jours » | 3 mg/kg/j per os 10 jours, puis décroissance sur 1 mois | Valeyrie-Allanore, Br J Dermatol 2010;163:847 |
| Purpura fulminans méningococcique | Fenêtre « dans les 24 heures » présentée comme limite ; déclaration sans délai | Dose de ciprofloxacine 20 mg/kg (max 500 mg) ; rifampicine en alternative ; idéalement 24 h, au plus 10 jours ; déclaration de la suspicion en 24 h au médecin cantonal et à l'OFSP | OFSP Bulletin 4/2025 (20.01.2025) |
| Asplénie | Vaccin pneumococcique sans valence ; intervalles méningocoques imprécis | PCV21 (18–64 ans à risque ; PCV21 ou PCV20 dès 65 ans) ; ACWY 2 doses à 1–2 mois ; B 2 doses à 2 mois ; rappels tous les 5 ans ; B hors indication et non remboursé après 24 ans | OFSP/CFV PCV (état 01.07.2026) ; OFSP Bulletin 7/2024 |
| Réaction transfusionnelle hémolytique | Recommandation BSH 2012 citée comme en vigueur | BSH 2023 (Soutar) remplace Tinegate 2012 | Br J Haematol 2023;201:832 |
| Hémoglobinurie paroxystique nocturne | Inhibiteurs proximaux absents | Pegcetacoplan (autorisé 23.03.2023) et iptacopan (29.08.2024) après réponse insuffisante au C5 | Swissmedic SwissPAR Aspaveli, Fabhalta |
| Neutropénie isolée « modérée » | Plage 0,5–1,5 G/l contraire aux seuils du contenu (modérée = 0,5–1,0) | Plage nommée « légère à modérée » ; chiffres Duffy ajoutés | Merz, Blood Adv 2023;7:317 |
| Lymphome B diffus | Pola-R-CHP « IPI élevé » | IPI de 2 à 5 (critère de POLARIX) | Tilly, N Engl J Med 2022 |
| Complément (contenu) | Voie des lectines « active directement C3 » | La voie des lectines active C4 et C2 par les MASP ; seule la voie alterne active directement C3 ; AP50 ajouté au raisonnement CH50 | Physiologie du complément (fait établi) |
| Moelle (contenu) | Réserve de « 10 jours » de neutrophiles, production « triplée » | Réserve de quelques jours, production multipliée plusieurs fois | Fait établi ; chiffre précis non retenu faute de source lue |
| Glossaire SLiM | « lésion focale à l'IRM » | « plus d'une lésion focale » | IMWG 2014 |
| qSOFA (sémiologie) | « dépasse 22 » | « atteint 22 ou plus » | Sepsis-3 2016 |
| Références erronées | Gibson « Hematology ASH Educ 2014 » ; Merz « Blood » ; Andrès « Expert Opin Drug Saf » ; Becker « Clin J Sport Med » ; ISA-EHA « 2022 » | Blood 2014;124:1251 ; Blood Adv 2023 ; J Clin Med 2019;8:1351 ; Sports Health 2014;6:232 ; Amyloid 2023;30:3 (en ligne 2022) | PubMed |
| Interprétations | `he_fer` « le fer oral n'est pas absorbé » ; seuils IC attribués à « ESC 2023 » ; `he_anemie` anémie rénale « sous 30 ml/min » | « mal absorbé (hepcidine) » ; ESC 2021 reprise en 2023 ; anémie fréquente dès 60 et surtout sous 30 ml/min | ESC 2021/2023 ; KDIGO |

Corrections de forme : un double espace et un « : » mal placé (neutropénie), une précision de déclaration OFSP dans « retenir ».

## 3. Les 22 doutes `aVerifier`

| # | Pathologie | Résultat | Source |
|---|---|---|---|
| 1 | Syndrome myélodysplasique | Doses résolues ; luspatercept autorisé ; **reste** : remboursement (LS) non trouvé | ESMO 2021 ; Swissmedic |
| 2 | Amylose AL | Résolu : Wechalekar, Amyloid 2023;30:3-17 | PubMed 35838162 |
| 3 | Anémie ferriprive | Résolu : phosphate contrôlé si doses élevées répétées ou facteur de risque, sans rythme fixé | Swissmedic Vigilance-News 2019 |
| 4 | Carence en B12 | Hydroxocobalamine résolue ; **reste** : rythme suisse de la cyanocobalamine (AIPS inaccessible) | BSH 2014 |
| 5 | Crise drépanocytaire | Résolu : antalgie en 30 min après le tri (60 min après l'enregistrement), réévaluation 15–30 min, O₂ si SpO₂ < 95 % | NHLBI 2014 (texte intégral) |
| 6 | Réaction transfusionnelle | Résolu : BSH 2023 (Soutar) | PubMed 37211954 |
| 7 | HPN | Résolu : Aspaveli 2023, Fabhalta 2024 | Swissmedic |
| 8 | Neutropénie isolée | Résolu : Merz, Blood Adv 2023 | PubMed 35994632 |
| 9 | Agranulocytose | Référence corrigée ; **reste** : prise en charge du G-CSF (AIPS et LS illisibles) ; aucun essai randomisé sur la mortalité | Andrès, J Clin Med 2019 |
| 10 | PTI | Résolu : ASH 2026 lue (Cuker, Blood Adv 2026;10:7076) | PubMed 42617047 |
| 11 | Hémophilie A acquise | Résolu : émicizumab hors indication en Suisse (AIPS : hémophilie congénitale) | Swissmedic Hemlibra 2018 |
| 12 | Asplénie | Résolu : PCV21, intervalles méningocoques | OFSP/CFV 2026 ; OFSP 2024 |
| 13 | Infarctus splénique | Résolu : Brett, JAMA Intern Med 2020;180:1125 | PubMed 32658244 |
| 14 | Kikuchi-Fujimoto | Résolu : Dumas, Medicine 2014;93:372 | PubMed 25500707 |
| 15 | Érysipèle | **Reste** : ssi.guidelines.ch inaccessible depuis la session | — |
| 16 | Choc toxique | Bénéfice chiffré ajouté (méta-analyse) ; **reste** : dose d'IgIV absente des résumés | Parks, CID 2018 ; Darenberg, CID 2003 |
| 17 | Urticaire aiguë | Résolu : la recommandation fixe 10 jours au plus, sans dose | EAACI 2021 |
| 18 | Maladie de Still | **Reste** : indication et remboursement de l'anakinra (AIPS inaccessible) | — |
| 19 | Mononucléose | Résolu : Dunmire 2015 confirmé ; Becker publié dans Sports Health 2014 | PubMed 26424648, 24790693 |
| 20 | Nécrolyse épidermique | Dose corrigée ; **reste** (formulé) : aucun essai randomisé ne prouve l'efficacité | Valeyrie-Allanore 2010 |
| 21 | Angio-œdème héréditaire | Résolu : Takhzyro (2019) et Orladeyo (2022) autorisés et admis sur la LS | Swissmedic ; OFSP |
| 22 | Purpura fulminans | Résolu : 24 h, schéma de chimioprophylaxie OFSP | OFSP Bulletin 4/2025 |

Bilan : 15 doutes résolus, 7 restent avec leur raison précise (1, 4, 9, 15, 16, 18, 20).

## 4. Sources inaccessibles depuis la session (à lire par un humain)

- compendium.ch et swissmedicinfo.ch (AIPS) : le proxy de la session a refusé l'accès ; aucune posologie n'a donc été confirmée dans l'AIPS, et toutes gardent la mention « à vérifier dans l'AIPS ».
- ssi.guidelines.ch (recommandation suisse sur l'érysipèle) et ch.oddb.org : accès refusé.

## 5. Chaîne relancée après correction

Fusion de `origin/main` (lot transversal 2), puis `construire_config_tetrade.py`, `construire_plans.py`, `generer_json.py`, `rendre_plans.py` (31/31), `auditer_conception.py` **34/34**, `auditer_couverture.py` **RÉUSSI**, `non_perte.py` **OK**, `verifier_interpretations.py` **142/142, 0 défaut**. `2_cou/ganglions_cervicaux.json` a été restauré depuis main (défaut IGRA connu) ; le bruit de `trans_s_s4_01.json` et des PDF n'a pas été commité.

Défaut d'outillage découvert : `construire_config_tetrade.py` et `generer_json.py` gardent un champ `aVerifier` retiré de la source (fusion conservatrice). Claude a retiré à la main les 15 champs résolus des JSON d'organes et du graphe ; un correctif de l'outil reste conseillé.

## Lot 2 (locomoteur, dermatologique) — 2026-11-24

Claude a relu, avec la même méthode, les 57 pathologies locomotrices et les 32 pathologies dermatologiques, leurs 17 organes, leurs signes, mots-clés et glossaires, et les 17 scénarios des interprétations `lo_synovie`, `lo_ck` et `de_brulure`. Chaque référence citée a été retrouvée dans PubMed ou sur le site de l'éditeur ; aucune n'était inventée, mais six étaient mal attribuées ou dépassées. Les paliers TF/F/U/R restent justes : aucun reclassement.

### L2.1 Bilan

| Système | Vérifiées | Corrigées | Doutes résolus | Doutes restants |
|---|---|---|---|---|
| Locomoteur et rhumatologique (57 pathologies, 11 organes, glossaire) | 57 | 23 pathologies (dont 5 où seul le doute est précisé) + contenu (rythme scapulo-huméral) + sémiologie (Schober) + glossaire (AO ; 9 sigles ajoutés) | 14 sur 24 | 10 |
| Dermatologique (32 pathologies, 6 organes, glossaire) | 32 | 12 pathologies (dont 2 où seul le doute est précisé) + glossaire (ROSCO, PTCH1 ; PCDS ajouté) | 3 sur 12 (6 autres réduits à un seul point précis) | 9 |
| Interprétations `lo_` et `de_` (3 fenêtres, 17 scénarios) | 17 | 2 | sans objet | 0 ; `_meta.statut` : **AUDITÉ** |

### L2.2 Erreurs de fond corrigées

| Pathologie ou élément | Erreur | Correction | Source |
|---|---|---|---|
| Traumatisme du rachis cervical | PAM « au-dessus de 85 à 90 mmHg » ; AO Spine 2017 | PAM entre 75-80 et 90-95 mmHg pendant 3 à 7 jours ; décompression dans les 24 h | AO Spine-Praxis 2024 (Kwon, Global Spine J) |
| Fracture du plancher de l'orbite | Amoxicilline-clavulanate prophylactique | Aucune antibioprophylaxie systématique (pas de bénéfice, plus de diarrhées) | Gheza 2018 ; Delaplain, Surg Infect 2020 |
| Rupture du tendon d'Achille | Énoxaparine pendant toute l'immobilisation | Pas de prophylaxie systématique ; réservée au haut risque | POT-CAST (van Adrichem, NEJM 2017) |
| Crise de goutte | Saturation de l'urate « 360 µmol/l » (c'est la cible) ; colchicine sans plafond ; prednisone 5 jours | Saturation ≈ 400 µmol/l (6,8 mg/dl) ; au plus 2 mg le 1er jour et 6 mg par crise ; prednisone 3 à 5 jours ; dépistage HLA-B*58:01 précisé | EULAR 2016 ; ACR 2020 ; information suisse Colctab |
| Mélanome | Ganglion sentinelle « dès 0,8 mm ou ulcération » ; suivi suisse absent | Ganglion sentinelle dès 1 mm, discuté de 0,8 à 1 mm avec facteur de risque ; schéma de suivi suisse ajouté | Swiss guidelines 2025 (Mangana, Swiss Med Wkly 2025;155:4210) |
| Brûlure étendue | « formule de Parkland, 2 à 4 ml/kg » | Parkland = 4 ml ; beaucoup de centres débutent à 2 ml ; diurèse cible ≈ 0,5 ml/kg/h | ISBI 2016 |
| Lombalgie commune | Paracétamol absent du raisonnement | Paracétamol jamais seul (pas mieux qu'un placebo), en réserve d'un AINS | Guideline suisse mednetbern 2019 ; Wertli et Steurer 2018 |
| Fibromyalgie | Duloxétine « selon l'indication autorisée » | Hors indication en Europe (refus de l'EMA pour la prégabaline, 2009) | EMA/CHMP 23.07.2009 |
| Pelade | Baricitinib seul | Baricitinib (adulte, depuis mai 2023) ou ritlécitinib dès 12 ans (Swissmedic, 03.02.2025) | Swissmedic, résumé Litfulo |
| Arthrite septique | Durée de 2 semaines généralisée | Non-infériorité démontrée surtout pour la main et le poignet | Gjika, Ann Rheum Dis 2019 |
| Luxation postérieure de l'épaule | « inaperçue dans la moitié des cas » (chiffre non sourcé) | « souvent inaperçue au premier examen » | Robinson, J Bone Joint Surg Am 2005 |
| Rythme scapulo-huméral (contenu) | 1° d'omoplate pour 2° d'élévation du bras | 1° pour 2° de mouvement gléno-huméral, soit un tiers de l'élévation | Fait établi (rapport 2:1 d'Inman) |
| Indice de Schober (sémiologie) | Augmentation « de moins de 4 cm » | Moins de 5 cm (la normale atteint 5 cm ou plus) | Fait établi |
| Sclérodermie | Rituximab absent de l'atteinte pulmonaire ; EULAR 2017 | Rituximab ajouté ; EULAR 2023 | Del Galdo, Ann Rheum Dis 2025;84:29 |
| Références dépassées ou mal attribuées | AAOS coiffe 2019 ; SVGO 2020 ; HS S1 2015 « EuroGuiDerm » ; WMS 2019 ; Perez « Rev Med Suisse » ; Uçkay « essai de durée » ; ROSCO « 2019 » sans année de parution ; « BOA 2015 » | AAOS 2025 ; SVGO 2026 (Swiss Med Wkly 2026;156:5700) ; S2k EHSF 2025 ; WMS 2024 ; J Antimicrob Chemother 2010 ; Mayo Clin Proc 2017 (bursectomie + 7 j) ; Br J Dermatol 2020 ; BESS/BOA (Rangan, Shoulder Elbow 2015) | PubMed ; éditeurs |
| Glossaire | AO « née à Davos » ; ROSCO « a défini en 2019 » ; PTCH1 « sa mutation active » | Fondée en 1958, établie à Davos ; phénotypes 2017, mise à jour 2019 ; mutation inactivatrice qui lève le frein | Faits établis |
| Interprétations | `de_brulure` « grand brûlé : au-delà de la moitié du corps » (seuil présenté comme une définition) ; `lo_synovie` hémarthrose « en moins de 2 heures » (limite stricte) | « par exemple plus de la moitié du corps » ; « dans les premières heures (souvent moins de 2 heures) » | Avis d'expert |

Corrections de forme : réduction de l'épaule sans la manœuvre de Kocher (rotation externe lente ou Milch), sources des bursites mises au format court.

### L2.3 Les 36 doutes `aVerifier`

| # | Pathologie | Résultat | Source |
|---|---|---|---|
| 1 | Plancher de l'orbite | Résolu : pas d'antibioprophylaxie systématique | Medwave 2018 ; Surg Infect 2020 |
| 2 | Lombalgie commune | Résolu : guideline suisse lue ; paracétamol jamais seul | mednetbern 2019 (FMH) ; Internist 2018 |
| 3 | Cervicalgie commune | Résolu : recommandation OPTIMa, Eur Spine J 2016;25:2000 | PubMed 26984876 |
| 4 | Tassement ostéoporotique | Résolu : SVGO 2026 | Swiss Med Wkly 2026;156:5700 |
| 5 | Rachis cervical | Résolu : PAM 75-80 à 90-95 mmHg, 3 à 7 jours | PubMed 38526930 |
| 6 | Coiffe des rotateurs | Résolu : AAOS 2025 ; ondes de choc efficaces dans la calcification | AAOS 28.08.2025 ; PubMed 24733195 |
| 7 | Capsulite rétractile | Résolu : Rangan, Shoulder Elbow 2015 | PubMed 27582992 |
| 8 | Luxation antérieure | **Reste** : aucune recommandation ne fixe la durée d'immobilisation ; revue Cochrane non retrouvée | — |
| 9 | Luxation postérieure | Résolu : Robinson, JBJS Am 2005;87:639 | PubMed 15741636 |
| 10 | Phlegmon des gaines | **Reste** : ssi.guidelines.ch inaccessible ; durée selon l'infectiologue | — |
| 11 | SDRC | **Reste** : néridronate enregistré seulement en Italie (2015) ; statut suisse non vérifiable | Ciaffi, Pharmaceuticals 2024 |
| 12 | Ostéonécrose fémorale | Résolu : Yoon, J Arthroplasty 2020;35:933 | PubMed 31866252 |
| 13 | Rupture d'Achille | Résolu : POT-CAST | PubMed 27959702 |
| 14 | Ostéite du pied diabétique | **Reste** : IWGDF/IDSA 2023 confirmée, texte intégral et SSI non lus | PubMed 37779457 |
| 15 | Fracture ouverte | **Reste** : EAST 2011 confirmée, texte intégral non lu | PubMed 21610369 |
| 16 | Crise de goutte | Résolu : Colctab 1 mg (2 mg le 1er jour, 6 mg par crise) ; HLA-B*58:01 selon ACR 2020 | Information suisse ; PubMed 32391934 |
| 17 | Arthrite septique | **Reste** : recommandation SSI inaccessible | — |
| 18 | Arthrite de Lyme | **Reste** : recommandations suisses (SSI) inaccessibles | — |
| 19 | Fibromyalgie | **Reste** (réduit) : refus EMA confirmé ; AIPS suisse illisible | EMA 2009 |
| 20 | Rhabdomyolyse | **Reste** : débit de diurèse et bicarbonates fondés sur des données faibles | Bosch, NEJM 2009 |
| 21 | Myosite inflammatoire | **Reste** (réduit) : BSR 2022 trouvée, texte non lu | PubMed 35355064 |
| 22 | Bursite mécanique | Résolu : Baumbach, Arch Orthop Trauma Surg 2014;134:359 | PubMed 24305696 |
| 23 | Bursite septique | Résolu : Perez 2010 (JAC) ; Uçkay 2017 (Mayo Clin Proc) | PubMed 20197288, 28602435 |
| 24 | Fluoroquinolones | Résolu : Swissmedic HPC du 16.12.2024 | swissmedic.ch |
| 25 | Psoriasis | Résolu : EuroGuiDerm 2020/2021, version vivante | PubMed 33349983, 33547728 |
| 26 | Mélanome | Résolu : recommandations suisses 2025 | PubMed 40811146 |
| 27 | Eczéma herpeticum | **Reste** : aucune source ne fixe la dose du valaciclovir | PCDS |
| 28 | Brûlure étendue | **Reste** : protocoles des centres suisses non publiés | — |
| 29 | Sclérodermie | Résolu : EULAR 2023 (Ann Rheum Dis 2025) | PubMed 39874231 |
| 30 | Alopécie androgénétique | **Reste** : statut du minoxidil oral en Suisse (AIPS inaccessible) | — |
| 31 | Pelade | **Reste** (réduit) : autorisations confirmées ; remboursement non vérifiable | Swissmedic 2025 |
| 32 | Acné | **Reste** (réduit) : mise à jour 2026 trouvée, texte intégral non lu | PubMed 41847993 |
| 33 | Hyperhidrose | **Reste** (réduit) : référence confirmée ; remboursement non vérifiable | PubMed 30710603 |
| 34 | Coup de chaleur | **Reste** (réduit) : WMS 2024 confirmée ; température d'arrêt non lue | PubMed 38425235 |
| 35 | Lichen plan buccal | **Reste** : aucune recommandation européenne lue | — |
| 36 | Érythème polymorphe majeur | **Reste** : place des corticoïdes non tranchée | — |

Bilan : 17 doutes résolus, 19 restent avec leur raison précise (dont 7 réduits à un seul point).

### L2.4 Outillage corrigé

`generer_json.py` gardait un `aVerifier` retiré de la source (fusion conservatrice). La nouvelle fonction `aligner_aVerifier` fait foi à `pathologies.txt` : elle retire ou remplace le doute d'une bulle seulement quand son nom et sa définition coïncident avec une pathologie de la source, pour ne jamais toucher un doute d'un autre système. Le test `conception/outils/tests/test_aligner_aVerifier.py` le vérifie (4 assertions). Effet mesuré : le graphe exemple passe de 43 à 26 `aVerifier` (les 17 résolus), sans perte ailleurs. `construire_config_tetrade.py` relit la source à chaque passage et n'avait pas ce défaut.

### L2.5 Chaîne relancée

Fusion de `origin/main` (hémato, infectio, Transversal ; conflits de `tetrade.json` et du statut des interprétations résolus par union), puis `construire_config_tetrade.py`, `construire_plans.py`, `generer_json.py`, `rendre_plans.py` (31/31), `audit_fond.py`, `auditer_conception.py` **34/34**, `auditer_couverture.py` **RÉUSSI**, `non_perte.py` **OK**, `verifier_interpretations.py` **159/159, 0 défaut**. `2_cou/ganglions_cervicaux.json` a été restauré depuis main (défaut IGRA connu).

Sources inaccessibles depuis la session : compendium.ch, swissmedicinfo.ch, ssi.guidelines.ch, la liste des spécialités (OFSP) ; toutes les posologies gardent « à vérifier dans l'AIPS ».

Signature : AAI (Anthropic AI)

## Lot 3 (ophtalmologique et ORL) — 2026-11-24

Claude a relu, avec la même méthode, les 40 pathologies du système ophtalmologique et ORL, ses 5 organes rédigés, ses 46 signes, ses temps d'examen et son glossaire, les 5 pathologies ajoutées aux maisons respiratoire et digestive, et les 18 scénarios des interprétations `or_refraction`, `or_pio` et `or_audio` (ainsi que les modèles des 3 fenêtres : équation de Goldmann, accommodation de Hofstetter, grades OMS 2021). Chaque référence datée a été retrouvée dans PubMed ou chez l'éditeur ; aucune n'était inventée, mais deux étaient dépassées (EURETINA 2014, TFOS DEWS II).

### L3.1 Bilan

| Système | Vérifiées | Corrigées | Doutes résolus | Doutes restants |
|---|---|---|---|---|
| Ophtalmologique et ORL (40 pathologies, 5 organes, signes, glossaire) | 40 | 10 pathologies + 1 reclassement (sécheresse oculaire F → TF) + glossaire (THEIA, TenCRAOS ajoutés) | 6 sur 18 (6 autres réduits à un seul point précis) | 12 |
| Ajouts des maisons (respiratoire 4, digestif 1) | 5 | 1 (polypose : mométasone, dupilumab) + glossaire respiratoire (SNOT-22 ajouté) | 1 sur 1 | 0 |
| Interprétations `or_` (3 fenêtres, 18 scénarios) | 18 | 0 | sans objet | 0 ; `_meta.statut` : **AUDITÉ** |

### L3.2 Erreurs de fond corrigées

| Pathologie ou élément | Erreur | Correction | Source |
|---|---|---|---|
| Occlusion de l'artère centrale de la rétine | « La rétine meurt en environ 90 minutes » ; thrombolyse IV « discutée dans les 4,5 heures » | Aucune lésion décelable à 97 min, lésions massives et irréversibles vers 240 min ; deux essais randomisés négatifs (alteplase, ténectéplase avec plus d'hémorragies) : thrombolyse réservée aux études ou au protocole local | Hayreh, Exp Eye Res 2004;78:723 ; THEIA, Lancet Neurol 2025 ; TenCRAOS, N Engl J Med 2026;394:442 |
| Dégénérescence maculaire | EURETINA 2014 ; « une injection par mois au départ, puis espacée » | EURETINA 2026 ; charge de 3 à 4 injections mensuelles, puis treat-and-extend guidé par l'OCT | Loewenstein, Ophthalmologica 2026 |
| Sécheresse oculaire | TFOS DEWS II cité comme en vigueur ; palier F | TFOS DEWS III (2025) ; palier TF (prévalence de 5 à 50 %) | Am J Ophthalmol 2025 ; Stapleton, Ocul Surf 2017 |
| Orbitopathie basedowienne | Téprotumumab absent (statut inconnu) | Autorisé par Swissmedic le 30.04.2025 (n° 69795) : 8 perfusions toutes les 3 semaines ; surveiller glycémie et audition | Swissmedic, nouvelles autorisations |
| Névrite vestibulaire | Méthylprednisolone présentée sans nuance | Récupération calorique plus rapide à 1 mois, sans bénéfice démontré sur les symptômes ni à 12 mois | Cochrane 2011 (Fishman) ; Otolaryngol Head Neck Surg 2021 |
| Hémianopsie homonyme | « près d'un AVC sur trois touche le champ visuel » (chiffre non sourcé) | 20 à 57 % selon les séries | Pollock, Cochrane 2019 |
| Polypose nasosinusienne | Mométasone « 2 pulvérisations 2 fois par jour » d'emblée | 100 µg par narine 1 fois par jour, 2 fois si réponse insuffisante ; limitation suisse du dupilumab ajoutée | Information harmonisée EMA (art. 30) ; LS 01.08.2023 (via formulaire de garantie) |
| Otite externe aiguë | Spécialité suisse inconnue | Ciprofloxacine 2 mg/ml + hydrocortisone 10 mg/ml, 3 gouttes 2 fois par jour 7 jours, dès 2 ans | compendium.ch (24.11.2026) |
| Traumatisme sonore | Seuil Suva « 85 dB(A) par jour » non vérifié | Contrôle auditif Suva (Audiomobil) au-delà de 85 dB en moyenne annuelle | suva.ch |
| Ischémie du nerf optique | 15 % de l'œil adelphe non sourcé | 14,7 % en 5,1 ans médians | Newman, Am J Ophthalmol 2002 |

Corrections de forme : « céftazidime » → « ceftazidime » ; 9 sigles d'infobulle non définis : 3 ajoutés au glossaire (THEIA, TenCRAOS, SNOT-22), 6 réécrits en toutes lettres.

### L3.3 Les 19 doutes `aVerifier`

| # | Pathologie | Résultat | Source |
|---|---|---|---|
| 1 | Sécheresse oculaire | Résolu : DEWS III remplace DEWS II | Am J Ophthalmol 2025 (doi 10.1016/j.ajo.2025.09.035) |
| 2 | DMLA | Résolu : mise à jour EURETINA 2026 | PubMed 42862818 |
| 3 | Occlusion de l'artère centrale | Résolu : thrombolyse sans bénéfice démontré | PubMed 41109232, 41604638 |
| 4 | Ischémie du nerf optique | Résolu : 14,7 % | PubMed 12208242 |
| 5 | Névrite vestibulaire | Résolu : pas de bénéfice à long terme | PubMed 21563170, 33525978 |
| 6 | Otite externe | Résolu : spécialité suisse lue | compendium.ch |
| 7 | Polypose (dupilumab) | Résolu : LS depuis le 01.08.2023, critères listés | formulaire de garantie (texte LS non lu directement) |
| 8 | Orbitopathie | Réduit : autorisation confirmée ; **reste** le remboursement | Swissmedic 30.04.2025 |
| 9 | Leber | Réduit : Raxone autorisé le 01.03.2024 dès 12 ans ; **reste** le remboursement | Swissmedic n° 68063 |
| 10 | Myopie | Réduit : atropine 0,01 % autorisée dans l'UE ; **reste** le statut suisse | EMA (Ryjunea) |
| 11 | Kératite amibienne | Réduit : polihexanide 0,08 % autorisé dans l'UE ; **reste** le statut suisse | EMA (Akantior) |
| 12 | Traumatisme sonore | Réduit : seuil Suva lu ; **reste** les corticoïdes (avis d'expert) | suva.ch |
| 13 | Blépharite | Réduit : l'AAO ne fixe pas de dose ; **reste** la dose (hors indication en Suisse) | AAO PPP 2023-2024 |
| 14 | Rétinopathie diabétique | **Reste** : recommandation suisse introuvable en ligne | — |
| 15 | Dacryocystite | **Reste** : aucune recommandation trouvée | — |
| 16 | Cellulite orbitaire | **Reste** : ssi.guidelines.ch inaccessible | — |
| 17 | Otite moyenne (adulte) | **Reste** : source suisse pédiatrique seulement | Paediatrica 2023 |
| 18 | Mastoïdite | **Reste** : avis d'expert | — |
| 19 | Otite externe nécrosante | **Reste** : avis d'expert | — |

Bilan : 7 doutes résolus, 12 restent avec leur raison précise (dont 6 réduits à un seul point). Paliers : 39 justes, 1 reclassé ; le système compte désormais 11 TF, 16 F, 8 U et 5 R.

### L3.4 Chaîne relancée

Fusion de `origin/main` (locomoteur, dermatologique, correctif `aligner_aVerifier`) : `systemes_rediges.py`, `fenetres.js`, `migrations_ids.json` et `interpretations.json` résolus par union des deux versions ; `tetrade.json`, graphe et sémiologie exemples, `conception.md` repris de main puis régénérés ; `CLAUDE_A_AUDITER/RAPPORT_AUTO.md` identique à main. Puis `construire_config_tetrade.py` (3563 nœuds), `construire_plans.py`, `generer_json.py`, `rendre_plans.py` (31/31), `audit_fond.py` (0 correction), `auditer_conception.py` **34/34**, `auditer_couverture.py` **RÉUSSI**, `non_perte.py` **OK** (après restauration des deux `2_cou/ganglions_cervicaux.json` depuis main), `verifier_interpretations.py` **177/177, 0 défaut**, `test_aligner_aVerifier.py` **OK** (4 assertions). Les 12 `aVerifier` restants figurent seuls dans les JSON d'organes : les doutes résolus ont bien été purgés.

Sources inaccessibles depuis la session : swissmedicinfo.ch, ssi.guidelines.ch, la Liste des spécialités (OFSP) ; compendium.ch a répondu cette fois. Les autres posologies gardent « à vérifier dans l'AIPS ».

Signature : AAI (Anthropic AI)

## Lot 4 (arène Tétrade, 108 questions) — 2026-11-24

Claude a relu les 108 questions des 11 paquets (`conception/donnees/tetrade/arene/*.txt`) : chaque réponse juste, chaque explication des distracteurs, chaque dose, seuil et critère. Les points demandés ont été vérifiés : adrénaline IM 0,5 mg chez l'adulte, répétable après 5 min (EAACI 2021) ; formule de Parkland 4 ml × kg × % surface, moitié en 8 h depuis la brûlure ; FENa < 1 % (fonctionnelle) contre > 2 % (nécrose tubulaire) ; CRB-65 = 4 (pression basse comptée dès une diastolique ≤ 60 mmHg) ; critères de Light (protéines 0,64 > 0,5 ; LDH > 2/3 de la limite sérique) ; score 4T élevé (chute > 50 %, J5–J10, thrombose, pas d'autre cause). Toutes les réponses justes restent justes ; aucune question n'a changé de réponse.

### L4.1 Bilan

| Paquet | Questions | Corrigées | Doutes restants |
|---|---|---|---|
| Cardio | 12 | 1 (FA : score) | 0 |
| Derma | 7 | 1 (Parkland : surface comptée) | 0 |
| Rénal | 10 | 1 (FENa sous diurétique) | 0 |
| Digestif | 11 | 1 (hémorragie non variqueuse) | 0 |
| Endocrino, hémato, infectio, loco, neuro, ORL, respi | 68 | 0 | 0 |

### L4.2 Erreurs de fond corrigées

| Question | Erreur | Correction | Source |
|---|---|---|---|
| Cardio 07 (FA) | CHA2DS2-VASc = 4 avec le sexe féminin | CHA2DS2-VA (ESC 2024, sans le sexe) = 3 ; anticoagulation recommandée dès 2 | Van Gelder et al., ESC 2024 AF, Eur Heart J 2024 ; ACC, Ten points to remember (17.09.2024) |
| Derma 03 (Parkland) | « surface au deuxième degré profond et plus » | Tout le deuxième degré (superficiel et profond) et le troisième degré ; seul le premier degré est exclu | ABLS/ISBI, définition de la surface brûlée |
| Rénal 01 (IRA) | « en l'absence de diurétique de l'anse » alors que la patiente prend un thiazide | Tout diurétique élève la FENa ; une FENa basse sous thiazide reste parlante ; sinon, FEurée < 35 % | physiologie rénale ; avis d'expert |
| Digestif 03 (ulcère) | Transfusion libérale qui « augmente la pression portale » dans une hémorragie non variqueuse | Elle augmente la mortalité et les récidives ; cible 70 à 80 g/l | Villanueva, N Engl J Med 2013 ; ESGE 2021 |

Vérifications sans correction, utiles à noter : l'andexanet alfa (Ondexxya®) est bien autorisé par Swissmedic depuis le 02.12.2020 pour les hémorragies menaçantes sous apixaban ou rivaroxaban ; le seuil de 3,5 mmol/l de potassium avant l'insuline dans l'acidocétose correspond au consensus ADA/EASD/JBDS 2024.

### L4.3 Chaîne relancée

`construire_arenes.py` (11 paquets Tétrade régénérés), puis `construire_config_tetrade.py`, `construire_plans.py`, `generer_json.py`, `rendre_plans.py` (31/31), `audit_fond.py` (0 correction), `auditer_conception.py` **34/34**, `auditer_couverture.py` **RÉUSSI**, `non_perte.py` **OK** (après restauration connue des deux `2_cou/ganglions_cervicaux.json`), `verifier_interpretations.py` **177/177, 0 défaut**, `test_arene_tetrade.py` **108 questions, 0 erreur**, `test_aligner_aVerifier.py` **OK**.

### L4.4 Branche 3D (contrôle sans médecine)

Les 30 organes ajoutés par `agent/tetrade-3d` portent des noms fidèles à leurs identifiants FMA (vérifiés dans `parts_list_e.txt` de BodyParts3D : poumon → artère et veines pulmonaires, lobes cérébraux, amygdale, hippocampe, noyaux gris, thymus, rate, sternum, os coxal, globe oculaire, voies optiques, os et muscles). Aucun organe n'inclut de maillage génital (testicules exclus ; le pénis n'a pas de maillage) ; la boîte de rognage de la peau (x ±58, y −230 à −60, z 630 à 790 mm) couvre toute la saillie génitale (testicules à z 690–719, saillie maximale y −206), et le rendu de contrôle ne montre aucun reste. Seule remarque de forme : l'identifiant `org_infect_organes_lymphoides_moelle_thym` évoque la moelle, mais le maillage ne contient que le thymus et la rate, comme sa note le dit. Branche jugée prête, sans modification.
## Lot 4 (Psyché) — 2026-11-24

Claude a relu, avec la méthode des lots 1 à 3, les 33 pathologies du système Psyché (7 organes), leur sémiologie, leur contenu et leur glossaire. Chaque dose, seuil, critère et référence datée a été confronté aux sources suisses d'abord (Swissmedic, OFSP, Tox Info Suisse, SGAD, SSAM), puis européennes et PubMed. Aucune référence n'était inventée ; trois étaient dépassées ou introuvables.

### L4.1 Bilan

| Système | Vérifiées | Corrigées | Doutes résolus | Doutes restants |
|---|---|---|---|---|
| Psyché (33 pathologies, 7 organes, sémiologie, glossaire) | 33 | 9 pathologies + glossaire (AMCS, CIM-11, HUG, SGAD, SGBP, TAO ajoutés) | 5 sur 9 (3 autres réduits à un seul point) | 4 |

Paliers : les 33 restent tels quels (9 TF, 10 F, 7 U, 7 R). Deux paliers TF se lisent comme relatifs à leur organe et non à la population générale : la psychose induite par le cannabis et l'hyperphagie boulimique ; Claude les garde, faute d'un meilleur candidat TF dans ces organes, et les signale.

### L4.2 Erreurs de fond corrigées

| Pathologie | Erreur | Correction | Source |
|---|---|---|---|
| TDAH de l'adulte | « symptômes avant 12 ans » attribué au code CIM-10 F90.0 | La CIM-10 exige un début avant 7 ans ; la CIM-11 et le DSM-5 admettent 12 ans | OMS, CIM-10 (critères de recherche F90) ; CIM-11 6A05 |
| Syndrome anticholinergique | Physostigmine sans dose ni statut | Anticholium® non autorisé en Suisse, stocké par les centres régionaux ; 0,5–1 mg IV lente, répétable toutes les 15 min, jusqu'à 2 mg | Liste des antidotes 2022/2023 (Bulletin OFSP 45/22) |
| Épisode dépressif | Recommandation suisse 2016 présentée comme en vigueur | Mise à jour SGAD/SGBP/SSPP 2024 | Ars Medici 17/2024 ; Brühl et Kawohl, Ther Umsch 2026;83:14 (PubMed 41878757) |
| Anorexie mentale | « le taux de mortalité le plus élevé » | « l'un des taux les plus élevés » (les troubles liés aux opioïdes rivalisent) | avis d'expert, formulation prudente |
| Narcolepsie de type 1 | Modafinil « 100–200 mg » | 200 mg le matin (100 mg chez le sujet âgé), au plus 400 mg/j | information du produit ; à vérifier dans l'AIPS |
| Dépendance au tabac | Champix® présenté comme disponible | Autorisation suisse radiée le 07.06.2024 | Swissmedic, fiche Champix® |
| Trouble de l'usage de l'alcool | Recommandation SSAM citée sans titre (introuvable) | Remplacée par une source suisse lue : stratégie alcool HUG 2021 | HUG, SMPR 2021 |
| Trouble de l'usage des opioïdes | Recommandations OFSP/SSAM sans titre ni année | « Recommandations médicales relatives au TAO du syndrome de dépendance aux opioïdes », SSAM 2020 | fr.ch (document cantonal) |
| Trouble de symptôme somatique | « avis d'expert » seul | Recommandation S3 germanophone (avec Bâle) | Roenneberg, Dtsch Arztebl Int 2019 (PubMed 31554544) |

### L4.3 Les 9 doutes `aVerifier`

| # | Pathologie | Résultat | Source |
|---|---|---|---|
| 1 | Syndrome anticholinergique | Résolu : dose et statut de la physostigmine | Liste des antidotes OFSP 2022/2023 |
| 2 | Jambes sans repos | Résolu : J Clin Sleep Med 2025;21:137-152 (en ligne en 2024) | PubMed 39324694 |
| 3 | Trouble de symptôme somatique | Résolu : S3 2019 | PubMed 31554544 |
| 4 | Alcool | Résolu par remplacement de la source | HUG 2021 |
| 5 | Opioïdes | Résolu : SSAM 2020 | fr.ch |
| 6 | TDAH | Réduit : conditions Swissmedic lues ; **reste** le remboursement (LS) | Swissmedic 2012 |
| 7 | Dépression | Réduit : mise à jour 2024 confirmée ; **reste** la lecture du texte intégral | Ars Medici 2024 ; PubMed 41878757 |
| 8 | Tabac | Réduit : Champix® radié ; **reste** l'existence d'un générique suisse | Swissmedic |
| 9 | Hyperphagie boulimique | **Reste** : indication suisse de la lisdexamfétamine introuvable (compendium.ch muet) | — |

### L4.4 Chaîne relancée

`construire_config_tetrade.py` (3762 nœuds), `construire_plans.py`, `generer_json.py`, `rendre_plans.py` (31/31), `audit_fond.py` (0 correction), `auditer_conception.py` **34/34** (après ajout de 6 sigles), `auditer_couverture.py` **RÉUSSI**, `non_perte.py` **OK** (après restauration connue des deux `2_cou/ganglions_cervicaux.json`), `verifier_interpretations.py` **177/177, 0 défaut**, `test_aligner_aVerifier.py` **OK**. Les 4 `aVerifier` restants figurent seuls dans les JSON d'organes.

Signature : AAI (Anthropic AI)
