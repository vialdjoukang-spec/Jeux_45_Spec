# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:17 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P07-09_Examens_Muscles_8-examens_production_XAi.json
- 2_Pratique/P07-09-PR_Examens_Muscles_8-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Smarter Medicine : Société Suisse de Rhumatologie (recommandations 1, 2, 3) et SSMIG ambulatoire 2021 (recommandation 2) : texte exact retrouvé
- Cabral et al., Disease-a-Month 2020 (résumé) : CK > 1000 U/l ou ≥ 5 fois la normale — texte conservé contrôlé
- Lazarou, Revue Médicale Suisse 2021 : vignettes CK N < 222 U/l (référence de laboratoire) — texte conservé contrôlé

Corrections faites :
- 1 citation Smarter Medicine au format commun, texte inchangé
- 17 anomalieTypique (étiquettes de 94 à 238 caractères, avec source dans l'étiquette) raccourcies à ≤ 45 caractères ; sources conservées dans les champs rédigés
- 7 options/bonneReponse de plus de 45 caractères raccourcies
- IRM seuil et génétique limite : renvois « textes relus » retirés du contenu
- Décision : les sigles ajoutés au glossaire sont gardés ; les citations Smarter Medicine mises au format commun sont gardées (vérifiées mot pour mot)
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main ; la fusion ne reprend pas le _meta du lot
- Réserves gardées dans aVerifier : CK, anticorps, génétique, échographie
