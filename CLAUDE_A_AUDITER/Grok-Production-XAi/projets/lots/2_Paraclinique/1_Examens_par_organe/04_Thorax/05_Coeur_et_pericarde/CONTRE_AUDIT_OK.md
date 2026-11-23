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

## Seconde vérification des sources (23.11.2026 00:36, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 6 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 1 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | VO2 max ≤ 12 ml/kg/min sous bêtabloquant, ≤ 14 sans | ISHLT, Mehra et al. 2016 (texte ishlt.org) | conforme |
| 2 | ECG dans les 10 minutes | ESC 2023, syndromes coronariens aigus (extraits secondaires) | conforme |
| 3 | HbA1c ≥ 6,5 % : diabète | ADA, Standards of Care 2025 | conforme |
| 4 | Potassium ≥ 6,5 mmol/l : hyperkaliémie sévère | ERC 2021, circonstances particulières (texte Resuscitation) | conforme |
| 5 | FFR ≤ 0,80 : sténose ischémiante | ESC 2024, syndromes coronariens chroniques (extraits) | conforme |
| 6 | NT-proBNP < 125 / BNP < 35 ng/l hors aigu ; 300 / 100 en aigu | Vivaldo et al., Rev Med Suisse 2021 : non rouvert ; valeurs identiques aux seuils de l'ESC | non trouvé (source nommée) : ajouté à _lot.aVerifier |
- Correction post-contrôle (23.11.2026) : 3 radioAnatomieNormale de plus de 45 caractères raccourcies en gardant le sens (segmentation du VG en 17 segments, myocarde sans fixation de FDG, coronaire droite et interventriculaire postérieure séparées) ; rien d'autre modifié ; controle PASS.
