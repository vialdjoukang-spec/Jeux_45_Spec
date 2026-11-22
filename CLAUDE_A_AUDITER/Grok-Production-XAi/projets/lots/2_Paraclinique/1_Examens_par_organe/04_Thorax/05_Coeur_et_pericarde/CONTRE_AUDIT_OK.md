# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:58 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P04-05-BIO_Biologie_Coeur_et_pericarde_8-examens_production_XAi.json
- 1_Theorie/P04-05-FCT_Exploration_fonctionnelle_Coeur_et_pericarde_10-examens_production_XAi.json
- 1_Theorie/P04-05-HIS_Anatomopathologie_biopsie_Coeur_et_pericarde_1-examens_production_XAi.json
- 1_Theorie/P04-05-IMG_Imagerie_Coeur_et_pericarde_10-examens_production_XAi.json
- 2_Pratique/P04-05-BIO-PR_Biologie_Coeur_et_pericarde_8-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-05-FCT-PR_Exploration_fonctionnelle_Coeur_et_pericarde_10-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-05-HIS-PR_Anatomopathologie_biopsie_Coeur_et_pericarde_1-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-05-IMG-PR_Imagerie_Coeur_et_pericarde_10-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- ESC/ERS 2022, hypertension pulmonaire : PAPm > 20 mmHg au repos, PAPO ≤ 15 mmHg, RVP > 2 unités Wood
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (smartermedicine.ch)

Corrections faites :
- P04-05-BIO-PR — libellé > 45 car. : « Trois paires d'hémocultures avant antibiotique » → « 3 paires d'hémocultures avant antibiotique »

Remarques :
- Doses CT calculées sur la directive OFSP R-06-06 : calcul documenté en entrée à vérifier, conservé ; comparateur OFSP 2018 tableau 16 : CT du thorax 3,8 mSv.
