# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:05 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P05-14-BIO_Biologie_Surrenales_4-examens_production_XAi.json
- 1_Theorie/P05-14-FCT_Exploration_fonctionnelle_Surrenales_5-examens_production_XAi.json
- 1_Theorie/P05-14-IMG_Imagerie_Surrenales_4-examens_production_XAi.json
- 2_Pratique/P05-14-BIO-PR_Biologie_Surrenales_4-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P05-14-FCT-PR_Exploration_fonctionnelle_Surrenales_5-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P05-14-IMG-PR_Imagerie_Surrenales_4-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Directive OFSP de médecine nucléaire (drw-nuk), tableau 1.1, relue dans le PDF de l'OFSP : MAG3 100 MBq 0,7 mSv ; DMSA 120 MBq 1,1 mSv ; MIBG 200 MBq 2,6 mSv
- Fuss et al., Eur J Endocrinol 2018 (656 cathétérismes, dose efficace médiane 6,4 mSv, 3,2 à 29 mSv selon le centre)
- Endocrine Society 2016, insuffisance surrénale primaire, figure 1 : 17-OH-progestérone > 1000 ng/dl (conversion 30 nmol/l vérifiée)
- Directive OFSP R-06-06 (rév. 2, 2018), tableau 1, relue dans le PDF de l'OFSP : valeurs cibles abdomen-bassin 470, angio-CT abdomen-bassin 450, calculs rénaux 180, thorax-abdomen-bassin 610 mGy·cm

Corrections faites :
- P05-14-FCT-PR — libellé > 45 car. : « Cortisol du lendemain sous le seuil de 50 nmol/l » → « Cortisol du lendemain sous 50 nmol/l »
- P05-14-FCT-PR — libellé > 45 car. : « Cortisol salivaire nocturne et cortisol libre urinaire » → « Cortisol salivaire nocturne et urinaire »
- P05-14-FCT-PR — libellé > 45 car. : « Deux marqueurs du rythme et de la sécrétion élevés » → « Deux marqueurs élevés (rythme, sécrétion) »
- P05-14-FCT-PR — libellé > 45 car. : « Aldostérone finale sous 162 pmol/l par LC-MS/MS » → « Aldostérone finale < 162 pmol/l (LC-MS/MS) »
- P05-14-FCT-PR — libellé > 45 car. : « Indice de latéralisation et indice de freination controlatérale » → « Latéralisation et freination controlatérale »
- P05-14-IMG-PR — libellé > 45 car. : « Fixation focale du processus unciné sans masse » → « Fixation focale de l'unciné sans masse »
- P05-14-FCT-PR — nom d'entité rétabli à l'identique du squelette (R1) : « Cortisol salivaire nocturne et urinaire » → « Cortisol salivaire nocturne et cortisol libre urinaire »

## Seconde vérification des sources (23.11.2026 00:40, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Freinage à 1 mg chez tout incidentalome | ESE/ENSAT 2023 | conforme |
| 2 | Masse ≥ 4 cm, hétérogène ou > 20 UH : risque de malignité, discussion pluridisciplinaire | ESE/ENSAT 2023 | conforme |
| 3 | PET au Ga-68 : 0,021 mSv/MBq, 200 MBq au plus | RCP SomaKit TOC (EMA) ; EANM/SNMMI 2019 (100 à 200 MBq) | conforme (4,2 mSv) |
| 4 | CT d'atténuation : valeur cible 270 mGy·cm (25e percentile) | OFSP, directive de médecine nucléaire (drw-nuk.pdf du 23.11.2026, tableau 3.3) | conforme |
| 5 | Dose totale du PET au Ga-68 : environ 8,3 mSv | calcul 4,2 + 4,05 | conforme |
