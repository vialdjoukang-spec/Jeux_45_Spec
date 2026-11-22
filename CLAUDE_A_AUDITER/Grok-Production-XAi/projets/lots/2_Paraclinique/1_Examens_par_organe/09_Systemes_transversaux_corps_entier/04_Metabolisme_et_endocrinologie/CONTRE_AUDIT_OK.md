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
