# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:14 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P07-06-BIO_Biologie_Os_longs_et_squelette_3-examens_production_XAi.json
- 1_Theorie/P07-06-HIS_Anatomopathologie_biopsie_Os_longs_et_squelette_1-examens_production_XAi.json
- 1_Theorie/P07-06-IMG_Imagerie_Os_longs_et_squelette_8-examens_production_XAi.json
- 2_Pratique/P07-06-BIO-PR_Biologie_Os_longs_et_squelette_3-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P07-06-HIS-PR_Anatomopathologie_biopsie_Os_longs_et_squelette_1-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P07-06-IMG-PR_Imagerie_Os_longs_et_squelette_8-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- OFSP 2018 (Bize et al., v1.4bis) tableau 13 (bassin 1,15 ; membres 0,01 mSv) et tableau 16 (hanche/cuisse 11,0 ; bassin 7,9 ; genou/jambe 2,7 ; pied/cheville 0,06 ; épaule/bras 5,8 mSv)
- Smarter Medicine : swiss orthopaedics 2024 (recommandations 1, 2, 3, 5), SSMIG ambulatoire 2021 (2, 4), Société Suisse de Rhumatologie (4), Société Suisse d'Angiologie 2024 (2) : texte exact retrouvé
- OFSP 2018 tableau 18 : système osseux (107,6 + 36,8) man.Sv, 3,1/1000 → 5,47 mSv par séance (calcul revérifié)
- OFSP/Commission fédérale de l'alimentation 2012, vitamine D : carence < 50 nmol/l, sévère < 25 nmol/l
- IMWG 2014 (Rajkumar et al., Lancet Oncol 2014) : rapport kappa/lambda normal 0,26-1,65 ; rapport ≥ 100 avec chaîne impliquée ≥ 100 mg/l

Corrections faites :
- 6 citations Smarter Medicine au format commun, texte inchangé
- Environ 30 renvois internes retirés du contenu livré (« voir aVerifier », « non relu », « à confirmer ») dans BIO, IMG, BIO-PR et IMG-PR ; textes réécrits sans affirmation nouvelle non sourcée
- Électrophorèse : seuil kappa/lambda 0,26-1,65 et événement définissant le myélome ajoutés selon l'IMWG 2014 (réserve tranchée) ; 3 champs sources « Voir aVerifier » → IMWG 2014 ; glossaire + IMWG
- CT : la dose par segment (tableau 16) remplace le renvoi interne ; bilan du squelette : irradiation_mSv 3.0599999999999996 → 3.06
- DXA : « Blake et al.. » → « Blake et al. »
- 2 referencePour/synonymes et 17 options/bonneReponse de plus de 45 caractères raccourcis ; glossaire + T2
- Réserves gardées dans aVerifier : CTX/P1NP, doses CT, scintigraphie, PET-CT, DXA, bilan du squelette, atlas d'âge osseux
- Décision : les sigles ajoutés au glossaire sont gardés ; les citations Smarter Medicine mises au format commun sont gardées (vérifiées mot pour mot)
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main ; la fusion ne reprend pas le _meta du lot
- Correction post-contrôle (23.11.2026) : referencePour vides rétablis exactement comme sur la conception de origin/main ; rien d'autre modifié ; controle PASS.
