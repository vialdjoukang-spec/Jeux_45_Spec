# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:58 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P04-08-BIO_Biologie_Seins_4-examens_production_XAi.json
- 1_Theorie/P04-08-HIS_Anatomopathologie_biopsie_Seins_4-examens_production_XAi.json
- 1_Theorie/P04-08-IMG_Imagerie_Seins_5-examens_production_XAi.json
- 2_Pratique/P04-08-BIO-PR_Biologie_Seins_4-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-08-HIS-PR_Anatomopathologie_biopsie_Seins_4-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-08-IMG-PR_Imagerie_Seins_5-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Enquête OFSP 2018 sur l'exposition de la population suisse (Bize et al., version 1.4bis, 2020), tableau 14, relue dans le PDF : mammographie 0,36 mSv (diagnostique et de dépistage)
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (smartermedicine.ch)

Corrections faites :
- P04-08-HIS-PR — libellé > 45 car. : « Intensité et complétude du marquage membranaire » → « Intensité et complétude du marquage »
- P04-08-IMG — R4 : dose alignée sur l'enquête OFSP 2018, tableau 14 (mammographie 0,36 mSv) : « seins__mammographie.irradiation_mSv=0.4 » → « 0.36 »
- P04-08-IMG — R4 : dose alignée sur l'enquête OFSP 2018, tableau 14 (mammographie 0,36 mSv) : « seins__tomosynthese.irradiation_mSv=0.4 » → « 0.36 »
- P04-08-HIS — R4 : dose alignée sur l'enquête OFSP 2018, tableau 14 (mammographie 0,36 mSv) : « seins__macrobiopsie_stereotaxique.irradiation_mSv=0.4 » → « 0.36 »
- P04-08-IMG — R4 : dose alignée sur l'enquête OFSP 2018, tableau 14 (mammographie 0,36 mSv) : « On la réserve aux indications reconnues, car selon l'OFSP une mammographie délivre environ 0,4 mSv, soit 20 fois une radiographie des poumons. » → « On la réserve aux indications reconnues, car une mammographie délivre en moyenne 0,36 mSv selon l'enquête 2018 de l'OFSP (tableau 14). »
- P04-08-IMG — R4 : dose alignée sur l'enquête OFSP 2018, tableau 14 (mammographie 0,36 mSv) : « Elle irradie le sein comme une mammographie, et on lui applique les mêmes règles de justification, avec un ordre de grandeur de 0,4 mSv donné par l'OFSP pour la mammographie. » → « Elle irradie le sein comme une mammographie, et on lui applique les mêmes règles de justification, avec l'ordre de grandeur de 0,36 mSv que l'enquête 2018 de l'OFSP (tableau 14) donne pour la mammographie. »
- P04-08-IMG-PR — R4 : dose alignée sur l'enquête OFSP 2018, tableau 14 (mammographie 0,36 mSv) : « La tomosynthèse irradie le sein comme une mammographie, avec un ordre de grandeur de 0,4 mSv donné par l'OFSP pour la mammographie. » → « La tomosynthèse irradie le sein comme une mammographie, avec l'ordre de grandeur de 0,36 mSv que l'OFSP donne pour la mammographie (enquête 2018). »
- P04-08-IMG — R4 : dose alignée sur l'enquête OFSP 2018, tableau 14 (mammographie 0,36 mSv) : « conception/donnees/paraclinique/topographie/4_thorax/seins.json › seins__mammographie › irradiation_mSv : 0,4 mSv : valeur typique de l'OFSP pour une « Aufnahme der weiblichen Brust » (page « Strahlendosen in der Medizin » → « conception/donnees/paraclinique/topographie/4_thorax/seins.json › seins__mammographie › irradiation_mSv : 0,36 mSv, dose moyenne de la mammographie (diagnostique et de dépistage) du tableau 14 de l'enquête OFSP 2018 (Biz »
- P04-08-IMG — R4 : dose alignée sur l'enquête OFSP 2018, tableau 14 (mammographie 0,36 mSv) : « conception/donnees/paraclinique/topographie/4_thorax/seins.json › seins__tomosynthese › irradiation_mSv : 0,4 mSv repris de la valeur OFSP de la mammographie ; aucune dose efficace propre à la tomosynthèse n'a été relue  » → « conception/donnees/paraclinique/topographie/4_thorax/seins.json › seins__tomosynthese › irradiation_mSv : 0,36 mSv repris de la mammographie (OFSP 2018, tableau 14) ; aucune dose efficace propre à la tomosynthèse n'a été »
- P04-08-HIS — R4 : dose alignée sur l'enquête OFSP 2018, tableau 14 (mammographie 0,36 mSv) : « conception/donnees/paraclinique/topographie/4_thorax/seins.json › seins__macrobiopsie_stereotaxique › irradiation_mSv : 0,4 mSv retenu comme ordre de grandeur (valeur OFSP de la mammographie) ; aucune dose efficace de la » → « conception/donnees/paraclinique/topographie/4_thorax/seins.json › seins__macrobiopsie_stereotaxique › irradiation_mSv : 0,36 mSv retenu comme ordre de grandeur (mammographie, OFSP 2018, tableau 14) ; aucune dose efficace »

## Seconde vérification des sources (23.11.2026 00:36, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Mammographie : 0,36 mSv | OFSP 2018, tableau 14 (PDF téléchargé le 23.11.2026, identique à la copie de travail) | conforme |
| 2 | Récepteurs aux œstrogènes : au moins 1 % de noyaux marqués | ASCO/CAP, Allison et al., J Clin Oncol 2020 (PubMed 31928404, résumé) | conforme |
| 3 | Fixation : formol en moins d'une heure, de 6 à 72 heures | ASCO/CAP (recommandations de fixation) | conforme |
| 4 | Avant 30 ans, masse palpable : échographie d'abord | ACR, masses palpables du sein 2022 | conforme |
| 5 | Kyste simple : catégorie 2 ; kyste compliqué isolé : catégorie 3 | ACR BI-RADS 2013 | conforme |
