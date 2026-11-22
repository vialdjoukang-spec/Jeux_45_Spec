# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:14 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P07-05_Examens_Cheville_et_pied_9-examens_production_XAi.json
- 2_Pratique/P07-05-PR_Examens_Cheville_et_pied_9-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- OFSP 2018 (Bize et al., v1.4bis) tableau 13 (bassin 1,15 ; membres 0,01 mSv) et tableau 16 (hanche/cuisse 11,0 ; bassin 7,9 ; genou/jambe 2,7 ; pied/cheville 0,06 ; épaule/bras 5,8 mSv)
- Smarter Medicine : swiss orthopaedics 2024 (recommandations 1, 2, 3, 5), SSMIG ambulatoire 2021 (2, 4), Société Suisse de Rhumatologie (4), Société Suisse d'Angiologie 2024 (2) : texte exact retrouvé
- ESC 2024 maladies artérielles périphériques (Mazzolai et al., Eur Heart J 2024;45:3538) : IPS ≤ 0,90 ; > 1,40 artères incompressibles, index orteil-bras ≤ 0,70

Corrections faites :
- 1 citation Smarter Medicine au format commun, texte inchangé
- IPS, limite : « Voir aVerifier : … non chiffré » → seuil d'artères incompressibles > 1,40 et examens de complément, selon ESC 2024 (réserve tranchée) ; glossaire + ESC
- Monofilament, limite : renvoi au guide SSED non téléchargé retiré du texte (réserve gardée dans aVerifier)
- Glossaire IAMI : « texte relu » retiré
- 1 referencePour et 13 options/bonneReponse de plus de 45 caractères raccourcis ; glossaire + T2
- Décision : les sigles ajoutés au glossaire sont gardés ; les citations Smarter Medicine mises au format commun sont gardées (vérifiées mot pour mot)
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main ; la fusion ne reprend pas le _meta du lot
