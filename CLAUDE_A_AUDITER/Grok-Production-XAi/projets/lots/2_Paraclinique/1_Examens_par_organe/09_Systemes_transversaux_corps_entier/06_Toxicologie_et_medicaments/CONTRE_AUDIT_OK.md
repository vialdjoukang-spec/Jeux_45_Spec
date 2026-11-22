# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:10 (heure de Zurich).
Verdict : conforme, sans correction

Fichiers contrôlés :
- 1_Theorie/P09-06_Examens_Toxicologie_et_medicaments_6-examens_production_XAi.json
- 2_Pratique/P09-06-PR_Examens_Toxicologie_et_medicaments_6-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Tox Info Suisse, notice paracétamol : paracétamolémie au plus tôt 4 h après une ingestion unique d'heure connue, lecture sur le nomogramme

Corrections faites :
- aucune

Remarques :
- Pages en ligne sans date (Tox Info chicha, Dr Risch, SFMU/INRS) signalées en entrée à vérifier, conservées.

## Seconde vérification des sources (23.11.2026 00:46, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Vancomycine : AUC/CMI de 400 à 600 | Rybak et al., Clin Infect Dis 2020 | conforme |
| 2 | Paracétamol : traitement au-dessus de 150 mg/l à la 4e heure | SRLF/SFMU 2020 (RFE, PDF srlf.org) | conforme |
| 3 | PEth ≥ 200 ng/ml : consommation chronique excessive | consensus de Bâle 2022 (Luginbühl et al.) | conforme |
| 4 | Méthémoglobinémie : traitement si > 30 % | SFMU, protocole Toxin (seuil confirmé par d'autres sources) | conforme |
| 5 | COHb 1 à 2 % chez le non-fumeur, 5 à 10 % chez le gros fumeur | Tox Info Suisse, page chicha (toxinfo.ch) | conforme |
