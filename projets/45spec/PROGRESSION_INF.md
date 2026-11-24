# Progression 45 Spec — INF

Production par l'agent Claude sans appel API (format exact de `scripts/produire_notions_questions.py`), branche `agent/45spec-INF`.

**24 / 61 pathologies canoniques produites** (notions + questions + correction), ordre de rendement à l'examen (`content/pathologies/RANG_RENDEMENT.json` : groupe A, puis B, C, D ; rang d'une pathologie fusionnée = meilleur rang de ses portes d'entrée).

Fusions : 15 groupes dans `content/pathologies/fusions_INF.json` ; doublons déjà produits archivés dans `projets/45spec/archives_fusion/INF`.

Statut d'audit : en attente (`audit.rejector = null`). Les chiffres incertains portent la mention « à vérifier » dans le champ source.

| # | Groupe | Rang | Id | Pathologie | Statut |
|---|---|---|---|---|---|
| 1 | A | 71 | `A04.7__F2_8-E08` | Infection à Clostridioides difficile | produite |
| 2 | A | 119 | `A46_erysipele_dermohypod__G12-E18` | Érysipèle (dermohypodermite bactérienne aiguë non nécrosante) | produite |
| 3 | A | 126 | `A15.0_tuberculose_pulmonai__F1_8-E09` | Tuberculose pulmonaire active | produite |
| 4 | A | 187 | `A48.3__F2_19-E16` | Syndrome de choc toxique (staphylococcique ou streptococcique) | produite |
| 5 | A | 209 | `A09.0_gastro_enterite_aigu__F2_8-E02` | Gastro-entérite aiguë infectieuse (virale ou bactérienne) | produite |
| 6 | A | 211 | `A49.9__F2_19-E01` | Infection bactérienne communautaire aiguë (pneumonie, pyélonéphrite, érysipèle) | produite |
| 7 | A | 213 | `A69.2_1__S5_6-E08` | Arthrite de Lyme (borréliose tardive) | produite |
| 8 | A | 214 | `B34.9_infection_virale_aig__F2_19-E02` | Infection virale aiguë non spécifique (myalgies, cytopénies transitoires) | produite |
| 9 | A | 313 | `A05.1_botulisme__F1_11-E16` | Botulisme | produite |
| 10 | A | 314 | `A35__S1_11-E09` | Tétanos céphalique ou généralisé (trismus inaugural) | — |
| 11 | A | 357 | `B00.1__S6_1-E03` | Herpès labial ou génital (HSV-1 / HSV-2) | produite |
| 12 | A | 358 | `B24_1__O7_6-E02` | Infection par le VIH contrôlée ou nouvellement diagnostiquée | produite |
| 13 | A | 359 | `B30.9__S1_17-E01` | Conjonctivite aiguë virale (adénovirus) | produite |
| 14 | A | 363 | `B37.0_candidose_muqueuse_s__O5_3-E08` | Candidose muqueuse superficielle (muguet oropharyngé, vulvo-vaginite) | produite |
| 15 | A | 365 | `B37.2__S6_9-E04` | Intertrigo candidosique ou dermatophytique des grands plis | produite |
| 16 | B | 737 | `B27.0_mononucleose_infecti__F2_5-E04` | Mononucléose infectieuse (EBV) et syndrome mononucléosique à CMV | produite |
| 17 | B | 753 | `A39.2__F1_4-E12` | Purpura fulminans (méningococcémie / sepsis fulminant) | — |
| 18 | B | 755 | `B00.4__F1_9-E16` | Encéphalite infectieuse aiguë (encéphalite herpétique HSV-1) | — |
| 19 | B | 756 | `B00.5__S1_17-E14` | Kératite dendritique herpétique (HSV-1) | — |
| 20 | B | 850 | `A07.1__F2_8-E07` | Giardiase (lambliase intestinale) | produite |
| 21 | B | 855 | `B80__F2_8-E12` | Oxyurose (entérobiase à Enterobius vermicularis) | produite |
| 22 | B | 930 | `A03.9_enterocolite_bacteri__F2_8-E16` | Entérocolite bactérienne invasive sévère (Salmonella, Shigella, STEC) | — |
| 23 | B | 934 | `A36.0__S1_19-E15` | Diphtérie pharyngée (angine pseudomembraneuse toxique) | — |
| 24 | B | 935 | `A40.3__O7_6-E12` | Sepsis fulminant chez le patient asplénique (OPSI) | — |
| 25 | B | 936 | `A41.0__O1_6-E15` | Sepsis maternel sur mastite ou endométrite associée | — |
| 26 | B | 938 | `A41.8_sepsis_et_choc_septi__G4-E20` | Sepsis et choc septique de l'adulte | — |
| 27 | B | 940 | `A41.9__O7_16-E14` | Infection active non contrôlée avant pose de prothèse ou implant | — |
| 28 | B | 943 | `A52.1_neurosyphilis_y_comp__F1_12-E09` | Neurosyphilis (y compris syphilis oculaire et otique) | — |
| 29 | B | 950 | `B00.0__S6_7-E15` | Eczéma herpéticum (syndrome de Kaposi-Juliusberg) | — |
| 30 | B | 951 | `B05.9__S6_9-E15` | Rougeole (exanthème morbilliforme descendant fébrile avec catarrhe) | — |
| 31 | B | 952 | `B20_primo_infection_vih___O7_12-E13` | Primo-infection VIH (syndrome rétroviral aigu) | — |
| 32 | B | 953 | `B25.8__O2_4-E15` | Infection disséminée après vaccin vivant atténué chez un immunodéprimé méconnu (SCID / VIH) | — |
| 33 | B | 954 | `B25.9__O7_20-E12` | Infection opportuniste grave chez patient transplanté (CMV, Pneumocystis, aspergillose) | — |
| 34 | B | 957 | `B46.1__S1_14-E13` | Sinusite fongique invasive aiguë (mucormycose, aspergillose invasive) | — |
| 35 | B | 959 | `B58.2__O7_6-E13` | Toxoplasmose cérébrale ou méningite à cryptocoque chez le patient VIH sévèrement immunodéprimé | — |
| 36 | B | 960 | `B59_pneumocystose_pulmon__O7_6-E05` | Pneumocystose pulmonaire | — |
| 37 | C | 1512 | `A04.5__S3_9-E06` | Colite infectieuse aiguë dysentérique ou IST rectale (Campylobacter, Shigella, EIEC, Chlamydia/gonocoque) | produite |
| 38 | C | 1513 | `A38__S6_9-E09` | Scarlatine / exanthème infectieux toxinique bénin de l'enfant | produite |
| 39 | C | 1516 | `A69.2__S1_4-E06` | Neuroborréliose de Lyme avec paralysie faciale périphérique (uni- ou bilatérale) | produite |
| 40 | C | 1518 | `B08.5__S1_19-E06` | Herpangine ou syndrome pieds-mains-bouche (Coxsackievirus) | produite |
| 41 | C | 1522 | `B26.0_oreillons_parotidite__S1_21-E05` | Oreillons (parotidite, orchite ourlienne) | produite |
| 42 | C | 1527 | `B37.8__O1_6-E05` | Candidose mammaire et mamelonnaire (muguet du couple mère-enfant) | produite |
| 43 | C | 1530 | `B95.6__O7_9-E06` | Portage ou infection nosocomiale à bactérie multirésistante (SARM, BLSE, EPC) | produite |
| 44 | D | 1939 | `A15.6__F2_18-E10` | Pleurésie tuberculeuse | — |
| 45 | D | 1940 | `A15.9__O7_15-E08` | Arrêt prématuré d'antibiothérapie ou de tuberculostatiques | — |
| 46 | D | 1942 | `A18.1__S4_3-E08` | Pyurie stérile sur tuberculose urogénitale | — |
| 47 | D | 1943 | `A37.0__S2_6-E08` | Coqueluche de l'adulte (Bordetella pertussis) | — |
| 48 | D | 1944 | `A49.3__O7_12-E09` | Infection à Mycoplasma genitalium résistante | — |
| 49 | D | 1948 | `A69.1__S1_19-E05` | Angine de Vincent (angine ulcéronécrotique fusospirillaire) | — |
| 50 | D | 1952 | `B24_2__O7_15-E07` | Inobservance aux antirétroviraux (VIH) avec risque de résistance | — |
| 51 | D | 1956 | `B37.8_candidose_sophagienn__S1_7-E09` | Candidose œsophagienne | — |
| 52 | D | 1957 | `B58.8__G2-E11` | Toxoplasmose ganglionnaire acquise | — |
| 53 | D | 1961 | `B83.9__F2_5-E09` | Helminthiases et parasitoses tissulaires | — |
| 54 | D | 2374 | `A28.1__G2-E13` | Maladie des griffes du chat (Bartonella henselae) | — |
| 55 | D | 2375 | `A31.1__S6_4-E09` | Ulcère de Buruli / ecthyma / infection cutanée atypique à mycobactérie | — |
| 56 | D | 2376 | `A48.1__O7_9-E09` | Légionellose nosocomiale (réseau d'eau hospitalier) | — |
| 57 | D | 2383 | `A81.0__F1_9-E12` | Démence rapidement progressive (encéphalite auto-immune, Creutzfeldt-Jakob) | — |
| 58 | D | 2384 | `B24__G16-E14` | Infection par le VIH au stade avancé / SIDA | — |
| 59 | D | 2385 | `B44.9_infections_fongiques__O7_6-E09` | Infections fongiques invasives (aspergillose invasive, candidémie) | — |
| 60 | D | 2386 | `B44.8__S2_10-E09` | Aspergillose bronchopulmonaire allergique (ABPA) | — |
| 61 | D | 2389 | `B75__S5_4-E10` | Trichinellose / myosite infectieuse parasitaire ou bactérienne | — |

Signature : AAI (Anthropic AI)
