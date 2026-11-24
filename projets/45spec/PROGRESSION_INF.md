# Progression 45 Spec — INF (Infectiologie)

Production par l'agent Claude sans appel API (format exact de `scripts/produire_notions_questions.py`), branche `agent/45spec-INF`.

**12 / 82 pathologies canoniques produites** (notions + questions + correction), ordre du script (fréquence puis identifiant).

Statut d'audit : en attente (`audit.rejector = null`). Les chiffres incertains portent la mention « à vérifier » dans le champ source.

| # | Id | Pathologie | Statut |
|---|---|---|---|
| 1 | `A08.4__G5-E02` | Gastro-entérite aiguë virale | produite |
| 2 | `A09.0__F2_8-E02` | Gastro-entérite infectieuse (bactérienne ou virale) | produite |
| 3 | `A09.9__S3_1-E01` | Gastro-entérite aiguë infectieuse | produite |
| 4 | `A49.9__F2_19-E01` | Infection bactérienne communautaire aiguë (pneumonie, pyélonéphrite, érysipèle) | produite |
| 5 | `A69.2_1__S5_6-E08` | Arthrite de Lyme (borréliose tardive) | produite |
| 6 | `B00.1__S6_1-E03` | Herpès labial ou génital (HSV-1 / HSV-2) | produite |
| 7 | `B24_1__O7_6-E02` | Infection par le VIH contrôlée ou nouvellement diagnostiquée | produite |
| 8 | `B30.9__S1_17-E01` | Conjonctivite aiguë virale (adénovirus) | produite |
| 9 | `B34.9_1__F2_19-E02` | Infection virale aiguë (lymphocytose ou leucopénie transitoire) | produite |
| 10 | `B34.9__S5_4-E01` | Myalgies virales aiguës (grippe, entérovirus, COVID-19) | produite |
| 11 | `B37.0_1__S6_1-E01` | Candidose buccale (muguet) et vulvo-vaginale | produite |
| 12 | `B37.0__S1_9-E02` | Candidose oropharyngée (muguet buccal, perlèche) | produite |
| 13 | `B37.2__S6_9-E04` | Intertrigo candidosique ou dermatophytique des grands plis | — |
| 14 | `B37.3__S4_18-E02` | Vulvo-vaginite candidosique (mycose à Candida albicans) | — |
| 15 | `A04.5__S3_9-E06` | Colite infectieuse aiguë dysentérique ou IST rectale (Campylobacter, Shigella, EIEC, Chlamydia/gonocoque) | — |
| 16 | `A04.7__F2_8-E08` | Infection à Clostridioides difficile | — |
| 17 | `A07.1__F2_8-E07` | Giardiase (lambliase intestinale) | — |
| 18 | `A38__S6_9-E09` | Scarlatine / exanthème infectieux toxinique bénin de l'enfant | — |
| 19 | `A46__G6-E06` | Érysipèle de la face (dermohypodermite bactérienne aiguë) | — |
| 20 | `A69.2__S1_4-E06` | Neuroborréliose de Lyme avec paralysie faciale périphérique (uni- ou bilatérale) | — |
| 21 | `B08.5__S1_19-E06` | Herpangine ou syndrome pieds-mains-bouche (Coxsackievirus) | — |
| 22 | `B26.9__S1_21-E05` | Parotidite aiguë virale (oreillons) ou bactérienne suppurée | — |
| 23 | `B27.0__F2_5-E04` | Mononucléose infectieuse (EBV) | — |
| 24 | `B27.9_1__G6-E07` | Infection à virus Epstein-Barr / Cytomégalovirus | — |
| 25 | `B37.8_2__O1_6-E05` | Candidose mammaire et mamelonnaire (muguet du couple mère-enfant) | — |
| 26 | `B80__F2_8-E12` | Oxyurose (entérobiase à Enterobius vermicularis) | — |
| 27 | `B95.6__O7_9-E06` | Portage ou infection nosocomiale à bactérie multirésistante (SARM, BLSE, EPC) | — |
| 28 | `A02.0__S3_8-E13` | Entérocolite infectieuse invasive sévère avec sepsis ou déshydratation hypovolémique (Salmonella, Campylobacter, Shigella) | — |
| 29 | `A03.9__F2_8-E16` | Dysenterie bacillaire sévère (Shigella / STEC) | — |
| 30 | `A05.1_1__F1_11-E16` | Syndrome de Guillain-Barré bulbaire ou botulisme aigu | — |
| 31 | `A05.1__O2_11-E13` | Botulisme (paralysie descendante aiguë symétrique avec troubles visuels/secs) | — |
| 32 | `A15.0__G1-E09` | Tuberculose pulmonaire active (sueurs nocturnes) | — |
| 33 | `A35__S1_11-E09` | Tétanos céphalique ou généralisé (trismus inaugural) | — |
| 34 | `A36.0__S1_19-E15` | Diphtérie pharyngée (angine pseudomembraneuse toxique) | — |
| 35 | `A39.2__F1_4-E12` | Purpura fulminans (méningococcémie / sepsis fulminant) | — |
| 36 | `A40.3__O7_6-E12` | Sepsis fulminant chez le patient asplénique (OPSI) | — |
| 37 | `A41.0__O1_6-E15` | Sepsis maternel sur mastite ou endométrite associée | — |
| 38 | `A41.8__G4-E20` | Sepsis sévère occulte du sujet âgé | — |
| 39 | `A41.9_1__O7_16-E14` | Infection active non contrôlée avant pose de prothèse ou implant | — |
| 40 | `A41.9__O4_6-E12` | Sepsis urogénital post-biopsie prostatique (après dépistage PSA) | — |
| 41 | `A46_1__G12-E18` | Érysipèle / dermo-hypodermite aiguë bactérienne du membre inférieur | — |
| 42 | `A46_2__S6_4-E12` | Érysipèle / cellulite aiguë fébrile sur ulcère ou plaie | — |
| 43 | `A48.3__F2_19-E16` | Syndrome de choc toxique (staphylococcique ou streptococcique) | — |
| 44 | `A52.1_2__O7_12-E14` | Neurosyphilis aiguë ou syphilis oculaire/otique | — |
| 45 | `B00.0__S6_7-E15` | Eczéma herpéticum (syndrome de Kaposi-Juliusberg) | — |
| 46 | `B00.4__F1_9-E16` | Encéphalite infectieuse aiguë (encéphalite herpétique HSV-1) | — |
| 47 | `B00.5__S1_17-E14` | Kératite dendritique herpétique (HSV-1) | — |
| 48 | `B05.9__S6_9-E15` | Rougeole (exanthème morbilliforme descendant fébrile avec catarrhe) | — |
| 49 | `B23.0__O7_12-E13` | Syndrome rétroviral aigu sévère (primo-infection VIH) | — |
| 50 | `B25.8__O2_4-E15` | Infection disséminée après vaccin vivant atténué chez un immunodéprimé méconnu (SCID / VIH) | — |
| 51 | `B25.9__O7_20-E12` | Infection opportuniste grave chez patient transplanté (CMV, Pneumocystis, aspergillose) | — |
| 52 | `B46.1__S1_14-E13` | Sinusite fongique invasive aiguë (mucormycose, aspergillose invasive) | — |
| 53 | `B58.2__O7_6-E13` | Toxoplasmose cérébrale ou méningite à cryptocoque chez le patient VIH sévèrement immunodéprimé | — |
| 54 | `B59_1__O7_6-E14` | Pneumocystose aiguë hypoxémiante avec détresse respiratoire | — |
| 55 | `A15.6__F2_18-E10` | Pleurésie tuberculeuse | — |
| 56 | `A15.9_1__O7_15-E08` | Arrêt prématuré d'antibiothérapie ou de tuberculostatiques | — |
| 57 | `A15.9__F1_8-E09` | Tuberculose pulmonaire ou infection chronique évolutive (VIH) | — |
| 58 | `A18.1__S4_3-E08` | Pyurie stérile sur tuberculose urogénitale | — |
| 59 | `A37.0__S2_6-E08` | Coqueluche de l'adulte (Bordetella pertussis) | — |
| 60 | `A49.3__O7_12-E09` | Infection à Mycoplasma genitalium résistante | — |
| 61 | `A69.1__S1_19-E05` | Angine de Vincent (angine ulcéronécrotique fusospirillaire) | — |
| 62 | `B20__S1_19-E08` | Primo-infection VIH (syndrome rétroviral aigu) | — |
| 63 | `B24_2__O7_15-E07` | Inobservance aux antirétroviraux (VIH) avec risque de résistance | — |
| 64 | `B26.0__S4_9-E08` | Orchite ourlienne (oreillons) | — |
| 65 | `B27.9__G5-E09` | Mononucléose infectieuse (primo-infection EBV) | — |
| 66 | `B37.0_2__O5_3-E08` | Soins de bouche palliatifs et xérostomie / candidose oropharyngée | — |
| 67 | `B37.8__S1_7-E09` | Candidose œsophagienne (immunodéprimé, corticothérapie inhalée) | — |
| 68 | `B58.8__G2-E11` | Toxoplasmose ganglionnaire acquise | — |
| 69 | `B59__O7_6-E05` | Pneumocystose pulmonaire (Pneumocystis jirovecii) subaiguë | — |
| 70 | `B83.9__F2_5-E09` | Helminthiases et parasitoses tissulaires | — |
| 71 | `A28.1__G2-E13` | Maladie des griffes du chat (Bartonella henselae) | — |
| 72 | `A31.1__S6_4-E09` | Ulcère de Buruli / ecthyma / infection cutanée atypique à mycobactérie | — |
| 73 | `A48.1__O7_9-E09` | Légionellose nosocomiale (réseau d'eau hospitalier) | — |
| 74 | `A52.1_1__F1_12-E09` | Pupille d'Argyll-Robertson (neurosyphilis) | — |
| 75 | `A52.1__S7_7-E09` | Neurosyphilis / encéphalopathie VIH (troubles cognitifs infectieux chroniques) | — |
| 76 | `A81.0__F1_9-E12` | Démence rapidement progressive (encéphalite auto-immune, Creutzfeldt-Jakob) | — |
| 77 | `B24__G16-E14` | Infection par le VIH au stade avancé / SIDA | — |
| 78 | `B37.8_1__S2_8-E09` | Œsophagite infectieuse (Candida albicans, HSV, CMV) | — |
| 79 | `B44.0__O7_9-E10` | Aspergillose pulmonaire invasive nosocomiale | — |
| 80 | `B44.8__S2_10-E09` | Aspergillose bronchopulmonaire allergique (ABPA) | — |
| 81 | `B44.9__O7_6-E09` | Infections fongiques invasives (aspergillose, candidémie, cryptococcose) | — |
| 82 | `B75__S5_4-E10` | Trichinellose / myosite infectieuse parasitaire ou bactérienne | — |

Signature : AAI (Anthropic AI)
