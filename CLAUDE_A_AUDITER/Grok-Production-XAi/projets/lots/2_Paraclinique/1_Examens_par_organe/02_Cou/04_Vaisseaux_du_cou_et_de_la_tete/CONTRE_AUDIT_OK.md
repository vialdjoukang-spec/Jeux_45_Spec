# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:49 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P02-04_Examens_Vaisseaux_du_cou_et_de_la_tete_8-examens_production_XAi.json
- 2_Pratique/P02-04-PR_Examens_Vaisseaux_du_cou_et_de_la_tete_8-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Ruediger et al. 2022 : 825 biopsies de l'artère temporale, 21 % positives
- ACR/EULAR 2022 (artérite à cellules géantes) : halo ou biopsie 5 points, seuil 6 points ; VS ≥ 50 mm/h ou CRP ≥ 10 mg/l
- STOP 1998 : seuil de 200 cm/s au doppler transcrânien
- SRU 2003 : sténose ≥ 70 % avec plaque et lumière rétrécie
- Smarter Medicine neurologie 2018 : texte exact retrouvé

Corrections faites :
- Citation Smarter Medicine (neurologie 2018, recommandation 2) mise au format commun ; texte vérifié mot pour mot
- Décision : les sigles ajoutés au glossaire sont gardés ; le rejet « clés ajoutées » du contrôle de forme est un faux positif
- Décision : les citations Smarter Medicine remplacées mot pour mot sont gardées ; vérifiées contre les listes Top 5 publiées
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main, antérieur au _meta actuel du fichier de conception (clés d'audit ajoutées depuis) ; laissé tel quel, la fusion ne reprend pas le _meta du lot.
