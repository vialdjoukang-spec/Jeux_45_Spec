# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:10 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P09-04-BIO_Biologie_Metabolisme_et_endocrinologie_7-examens_production_XAi.json
- 1_Theorie/P09-04-FCT_Exploration_fonctionnelle_Metabolisme_et_endocrinologie_4-examens_production_XAi.json
- 2_Pratique/P09-04-BIO-PR_Biologie_Metabolisme_et_endocrinologie_7-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P09-04-FCT-PR_Exploration_fonctionnelle_Metabolisme_et_endocrinologie_4-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- ADA, Standards of Care in Diabetes 2025, section 2 : HbA1c ≥ 6,5 % ou glycémie à jeun ≥ 126 mg/dl (7,0 mmol/l) ; prédiabète HbA1c 5,7 à 6,4 % ou 100 à 125 mg/dl (5,6 à 6,9 mmol/l) ; jeûne d'au moins 8 h
- Liste Top 5 Smarter Medicine de gériatrie : citation HbA1c remise mot pour mot

Corrections faites :
- P09-04-BIO — Q4 : citation alignée mot pour mot sur la liste gériatrie : « âgées ; un contrôle modéré » → « âgées; un contrôle modéré »
- P09-04-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[GAD]=Décarboxylase de l'acide glutamique, cible des auto-anticorps anti-GAD du diabète auto-immun. »
- P09-04-BIO-PR — sigle absent du glossaire (C3) : « None » → « glossaire[GAD]=Décarboxylase de l'acide glutamique, cible des auto-anticorps anti-GAD du diabète auto-immun. »

## Seconde vérification des sources (23.11.2026 00:46, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | LDL mesuré directement si triglycérides > 4,6 mmol/l | USZ, guideline Dyslipidämie 2026 (PDF hausarztmedizin.uzh.ch : « TG-Konzentration >4,6 mmol/l ») | conforme |
| 2 | Très haut risque : LDL < 1,4 mmol/l | USZ 2026 (même PDF) | conforme |
| 3 | NRS 2002 ≥ 3 : risque nutritionnel | Schuetz et al., Lancet 2019 (EFFORT) | conforme |
| 4 | Épreuve de jeûne jusqu'à 72 h | Endocrine Society, Cryer et al. 2009 | conforme |
| 5 | HGPO : 75 g, glycémie à jeun, à 1 h et à 2 h | SSGO, avis d'experts n° 81 (2023) | conforme sur la procédure (texte SSGO non rouvert) |
