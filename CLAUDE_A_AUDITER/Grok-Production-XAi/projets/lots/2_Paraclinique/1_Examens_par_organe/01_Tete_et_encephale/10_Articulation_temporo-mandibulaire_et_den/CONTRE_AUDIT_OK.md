# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:46 (heure de Zurich).
Verdict : conforme, transmis sans correction

Fichiers couverts :
- 1_Theorie/P01-10_Examens_Articulation_temporo-mandibulaire_e_4-examens_production_XAi.json
- 2_Pratique/P01-10-PR_Examens_Articulation_temporo-mandibulaire_e_4-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- OFSP 2018 tableau 15 : OPG 0,02 mSv, CBCT 0,2 mSv par acquisition
- Lübbers et al., Swiss Dental Journal 2024 (CBCT) : IRM pour le disque, CBCT pour l'os
- Schiffman et al., DC/TMD 2014 : ouverture ≥ 40 mm
- EFP : saignement au sondage < 10 % des sites, poches ≤ 3 mm

Corrections faites :
- Décision : les sigles ajoutés au glossaire sont gardés ; le rejet « clés ajoutées » du contrôle de forme est un faux positif
- Décision : les citations Smarter Medicine remplacées mot pour mot sont gardées ; vérifiées contre les listes Top 5 publiées
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main, antérieur au _meta actuel du fichier de conception (clés d'audit ajoutées depuis) ; laissé tel quel, la fusion ne reprend pas le _meta du lot.
