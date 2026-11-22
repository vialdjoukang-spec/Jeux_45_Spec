# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:15 (heure de Zurich).
Verdict : conforme, sans correction

Fichiers contrôlés :
- 1_Theorie/P09-10_Examens_Psyche_7-examens_production_XAi.json
- 2_Pratique/P09-10-PR_Examens_Psyche_7-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Blackman et al., JAMA Psychiatry 2023 (PubMed 37436735) : 12 études, 1613 patients, 26,4 % d’anomalies, 5,9 % cliniquement pertinentes, NNA 18
- Recommandations australiennes et néo-zélandaises 2026 (ANZJP, PMC13191067) : bilan de base (FSC, ionogramme, fonctions rénale et hépatique, prolactine, HbA1c, lipides, dépistage urinaire, ECG) ; TSH seulement sur argument clinique ; IRM si début avant 14 ans ou après 40 ans, céphalées, crises, catatonie, signes neurologiques
- Hiemke et al., AGNP 2017 : lithium 0,5–1,2 mmol/l (entretien 0,5–0,8), alerte 1,2 ; clozapine 350–600 ng/ml, alerte 1000
- Pearson, interprétation du MMPI-2 : VRIN > 80 = profil ininterprétable ; note T 65 = 92e percentile (Butcher et Pope 1992)

Corrections faites :
- aucune

## Seconde vérification des sources (23.11.2026 00:49, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | AUDIT : 8 ou plus = consommation à risque ; zone II de 8 à 15, conseil simple | OMS, manuel AUDIT 2001 (Babor et al., iris.who.int) | conforme |
| 2 | AUDIT : seuil abaissable à 7 chez la femme et après 65 ans | OMS, manuel AUDIT 2001 | conforme |
| 3 | Lithium : seuil d'alerte du laboratoire à 1,2 mmol/l | AGNP, Hiemke et al., Pharmacopsychiatry 2017 | conforme |
| 4 | Scores normaux : PHQ-9 < 5, GAD-7 < 5, MoCA ≥ 26 | Kroenke et al. 2001 ; Spitzer et al. 2006 ; Nasreddine et al. 2005 (consignes MoCA) | conforme |
| 5 | MMPI-2 : échelles cliniques sous une note T de 65 = non pathologique | Butcher et Pope, 1992 (PDF de l'article) | conforme |
