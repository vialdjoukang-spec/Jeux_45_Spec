# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:31 (heure de Zurich).
Verdict : conforme, transmis sans correction

Fichiers couverts :
- 1_Theorie/P02-02_Examens_Parathyroides_7-examens_production_XAi.json
- 2_Pratique/P02-02-PR_Examens_Parathyroides_7-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- EANM 2021 imagerie parathyroïdienne, tableau 1 : sestamibi 0,00703 mSv/MBq, 6,3 mSv à 900 MBq ; fluorocholine 0,020 mSv/MBq, 6,0 mSv à 300 MBq
- Smarter Medicine SSMIG ambulatoire 2021 (vitamine D) : texte exact retrouvé

Corrections faites :
- aucune

## Note pour la relecture
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main, antérieur au _meta actuel du fichier de conception (clés d'audit ajoutées depuis) ; laissé tel quel, la fusion ne reprend pas le _meta du lot.
