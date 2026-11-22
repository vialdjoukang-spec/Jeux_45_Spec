# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:22 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P03-01-BIO_Biologie_Rachis_osseux_4-examens_production_XAi.json
- 1_Theorie/P03-01-FCT_Exploration_fonctionnelle_Rachis_osseux_1-examens_production_XAi.json
- 1_Theorie/P03-01-HIS_Anatomopathologie_biopsie_Rachis_osseux_1-examens_production_XAi.json
- 1_Theorie/P03-01-IMG_Imagerie_Rachis_osseux_7-examens_production_XAi.json
- 2_Pratique/P03-01-BIO-PR_Biologie_Rachis_osseux_4-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P03-01-FCT-PR_Exploration_fonctionnelle_Rachis_osseux_1-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P03-01-HIS-PR_Anatomopathologie_biopsie_Rachis_osseux_1-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P03-01-IMG-PR_Imagerie_Rachis_osseux_7-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- OFSP 2018 tableau 13 (colonne 1,6 mSv) et tableau 16 (CT de la colonne 10,7 mSv)
- OFSP 2018 tableau 18 : système osseux 107,6 man.Sv (radiopharmaceutiques) + 36,8 man.Sv (CT), 3,1/1000 séances
- Smarter Medicine SSMIG ambulatoire 2014 (1) et 2021 (4), Société Suisse de Rhumatologie (4) : texte exact retrouvé

Corrections faites :
- 3 citations Smarter Medicine au format commun (guillemets, liste, numéro), texte inchangé
- Glossaire + GT (gamma-GT)
- Décision : les sigles ajoutés au glossaire sont gardés
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main ; la fusion ne reprend pas le _meta du lot
- Point transversal pour la relecture : la scintigraphie osseuse vaut ici 4,1 mSv (part radiopharmaceutique seule, méthode déclarée) et 5,5 mSv en 07-06 (radiopharmaceutique + CT des SPECT/CT) ; même tableau 18, deux conventions ; à harmoniser
- Réserves gardées dans aVerifier : IDSA 2015, EOS, Schober, IMWG en résumé, DXA
