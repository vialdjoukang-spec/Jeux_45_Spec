# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:58 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P04-01-BIO_Biologie_Poumons_et_voies_aeriennes_9-examens_production_XAi.json
- 1_Theorie/P04-01-END_Endoscopie_Poumons_et_voies_aeriennes_3-examens_production_XAi.json
- 1_Theorie/P04-01-FCT_Exploration_fonctionnelle_Poumons_et_voies_aeriennes_9-examens_production_XAi.json
- 1_Theorie/P04-01-HIS_Anatomopathologie_biopsie_Poumons_et_voies_aeriennes_4-examens_production_XAi.json
- 1_Theorie/P04-01-IMG_Imagerie_Poumons_et_voies_aeriennes_7-examens_production_XAi.json
- 2_Pratique/P04-01-BIO-PR_Biologie_Poumons_et_voies_aeriennes_9-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-01-END-PR_Endoscopie_Poumons_et_voies_aeriennes_3-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-01-FCT-PR_Exploration_fonctionnelle_Poumons_et_voies_aeriennes_9-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-01-HIS-PR_Anatomopathologie_biopsie_Poumons_et_voies_aeriennes_4-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-01-IMG-PR_Imagerie_Poumons_et_voies_aeriennes_7-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Enquête OFSP 2018 sur l'exposition de la population suisse (Bize et al., version 1.4bis, 2020), tableaux 13 et 16, relue dans le PDF : radiographie du thorax 0,045 mSv
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (smartermedicine.ch) : SSMI 2017, SSMIG 2014 et 2023, oncologie médicale 2024

Corrections faites :
- P04-01-HIS-PR — libellé > 45 car. : « Fibrose hétérogène avec foyers fibroblastiques » → « Fibrose hétérogène, foyers fibroblastiques »
- P04-01-IMG-PR — libellé > 45 car. : « Opacité alvéolaire systématisée avec bronchogramme aérien » → « Opacité systématisée avec bronchogramme »
- P04-01-IMG-PR — libellé > 45 car. : « Rayon de miel sous-pleural basal et bronchectasies de traction » → « Rayon de miel et bronchectasies de traction »
- P04-01-IMG-PR — libellé > 45 car. : « Défauts de perfusion segmentaires bien ventilés » → « Défauts perfusionnels segmentaires ventilés »
- P04-01-IMG — sigle absent du glossaire (C3) : « None » → « glossaire[TEP-CT]=Tomographie par émission de positons couplée au CT, synonyme de PET-CT. »

Remarques :
- Doses CT calculées sur la directive OFSP R-06-06 : calcul documenté en entrée à vérifier, conservé ; comparateur OFSP 2018 tableau 16 : CT du thorax 3,8 mSv.
