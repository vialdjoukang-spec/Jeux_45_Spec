# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:31 (heure de Zurich).
Verdict : conforme, transmis sans correction

Fichiers couverts :
- 1_Theorie/P05-01-BIO_Biologie_Foie_10-examens_production_XAi.json
- 1_Theorie/P05-01-FCT_Exploration_fonctionnelle_Foie_1-examens_production_XAi.json
- 1_Theorie/P05-01-HIS_Anatomopathologie_biopsie_Foie_1-examens_production_XAi.json
- 1_Theorie/P05-01-IMG_Imagerie_Foie_6-examens_production_XAi.json
- 2_Pratique/P05-01-BIO-PR_Biologie_Foie_10-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P05-01-FCT-PR_Exploration_fonctionnelle_Foie_1-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P05-01-HIS-PR_Anatomopathologie_biopsie_Foie_1-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P05-01-IMG-PR_Imagerie_Foie_6-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Hari et al., Liver Int 2017 : dose médiane 5,4 mSv
- BSG 2020 biopsie hépatique : carotte ≥ 20 mm, 11 espaces portes, voie transveineuse si INR > 1,4 ou plaquettes < 50 G/l
- OFSP R-06-06 rév. 2 (2018) : foie multiphasique 960 mGy·cm
- EASL-ERN 2025 Wilson : céruloplasmine < 0,1 g/l, cuivre urinaire > 1,6 µmol/24 h, jusqu'à 20 % de céruloplasmine normale

Corrections faites :
- aucune

## Note pour la relecture
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main, antérieur au _meta actuel du fichier de conception (clés d'audit ajoutées depuis) ; laissé tel quel, la fusion ne reprend pas le _meta du lot.
