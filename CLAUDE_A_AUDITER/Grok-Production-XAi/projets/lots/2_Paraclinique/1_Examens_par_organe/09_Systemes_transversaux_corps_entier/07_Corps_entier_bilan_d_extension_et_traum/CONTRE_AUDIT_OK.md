# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:15 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P09-07_Examens_Corps_entier_bilan_d_extension_et_t_6-examens_production_XAi.json
- 2_Pratique/P09-07-PR_Examens_Corps_entier_bilan_d_extension_et_t_6-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Smarter Medicine, Société suisse d’oncologie médicale 2024, recommandation 4 (smartermedicine.ch) : citation identique mot pour mot ; le texte parle de preuves insuffisantes pour la détection précoce des récidives
- Smarter Medicine, Société Suisse de Chirurgie 2018 : citation identique mot pour mot
- OFSP R-06-06 rév. 2 (PDF) : valeurs cibles crâne 750, colonne cervicale 300, thorax-abdomen-bassin 610 mGy·cm ; somme recalculée 12,5 mSv
- Mettler et al., Radiology 2008 : leucocytes marqués au Tc-99m, 740 MBq, 8,1 mSv (0,011 mSv/MBq)
- PET-CT 8,8 mSv : valeur retenue par le projet

Corrections faites :
- P09-07-PR — fond : la liste SSOM 2024 parle de preuves insuffisantes, pas de survie (contre-audit 09-07) : « Un PET de routine ne prolonge pas la survie dans cette situation et expose aux faux positifs inflammatoires. » → « Les preuves sont insuffisantes pour détecter tôt une récidive par un PET de routine dans cette situation, et l’examen expose aux faux positifs, aux examens invasifs et au surtraitement. »
- P09-07-PR — cohérence du cas (motocycliste) (contre-audit 09-07) : « après une chute à haute énergie ; » → « après un accident de moto à haute énergie ; »

Remarques :
- Les visées « therapeutique » de la scintigraphie aux leucocytes et du PET restent à l’appréciation de l’audit médical.

## Seconde vérification des sources (23.11.2026 00:49, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | eFAST : spécificité de 94 à 100 %, sensibilité de 28 à 100 % | directive S3 Polytrauma de la DGU (texte long 187-023, degum.de), citée aussi par raducation.de | conforme |
| 2 | Myélome : plus d'une lésion focale d'au moins 5 mm à l'IRM | Rajkumar et al., Lancet Oncol 2014 (critères IMWG) | conforme |
| 3 | Lésion unique, infiltration diffuse ou doute : contrôle IRM en 3 à 6 mois | Rajkumar et al., Lancet Oncol 2014 | conforme |
| 4 | TEP-CT : hyperfixation seule insuffisante, ostéolyse d'au moins 5 mm requise sur le CT | Rajkumar et al., Lancet Oncol 2014 | conforme |
| 5 | Porteurs d'un variant TP53 : IRM corps entier sans gadolinium chaque année | Frebourg et al., Eur J Hum Genet 2020 (ERN GENTURIS) et fiche rapide GENTURIS | conforme |
