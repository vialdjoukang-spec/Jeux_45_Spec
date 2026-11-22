# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:15 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P09-09_Examens_Sommeil_et_vigilance_7-examens_production_XAi.json
- 2_Pratique/P09-09-PR_Examens_Sommeil_et_vigilance_7-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Berry et al., AASM 2012 (PubMed 23066376) : apnée = baisse du signal ≥ 90 % ; hypopnée = baisse ≥ 30 %

Corrections faites :
- P09-09-PR — ambiguïté levée (contre-audit 09-09) : « Dans une apnée centrale, les sangles sont plates elles aussi, » → « Dans une apnée centrale, les sangles thoraco-abdominales restent plates, faute d’effort, »

## Seconde vérification des sources (23.11.2026 00:49, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Hypopnée : baisse du flux d'au moins 30 % pendant 10 s avec désaturation de 3 % ou éveil | Berry et al., J Clin Sleep Med 2012 (PMC3459210) | conforme |
| 2 | Apnée obstructive : baisse du flux d'au moins 90 % pendant 10 s ou plus, effort persistant | Berry et al., J Clin Sleep Med 2012 | conforme |
| 3 | Narcolepsie : latence moyenne de 8 min ou moins et au moins deux SOREMP | ICSD-3 de l'AASM (critères, matériel AASM) | conforme |
| 4 | Chauffeur professionnel : aucun endormissement avant 34 min au test de maintien de l'éveil ; résultat limite à répéter | recommandation suisse sur la somnolence diurne, Forum Med Suisse 2017;17(20):442-447 (sgrm.ch, PDF) | conforme |
| 5 | Polygraphie : au moins 4 heures interprétables ; IAH de 5/h ou moins normal (pathologique > 5/h) | recommandations SSSSC apnées-hypopnées, version FR du 17.06.2020 (swiss-sleep.ch, PDF) | conforme |
