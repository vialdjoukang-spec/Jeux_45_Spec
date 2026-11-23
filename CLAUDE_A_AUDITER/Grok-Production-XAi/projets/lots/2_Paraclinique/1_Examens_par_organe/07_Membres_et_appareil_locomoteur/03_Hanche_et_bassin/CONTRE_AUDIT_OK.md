# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:14 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P07-03_Examens_Hanche_et_bassin_8-examens_production_XAi.json
- 2_Pratique/P07-03-PR_Examens_Hanche_et_bassin_8-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- OFSP 2018 (Bize et al., v1.4bis) tableau 13 (bassin 1,15 ; membres 0,01 mSv) et tableau 16 (hanche/cuisse 11,0 ; bassin 7,9 ; genou/jambe 2,7 ; pied/cheville 0,06 ; épaule/bras 5,8 mSv)
- Smarter Medicine : swiss orthopaedics 2024 (recommandations 1, 2, 3, 5), SSMIG ambulatoire 2021 (2, 4), Société Suisse de Rhumatologie (4), Société Suisse d'Angiologie 2024 (2) : texte exact retrouvé
- Ziebarth et Liebs, Forum Médical Suisse 2022 (doi 10.4414/fms.2022.09101) : épiphysiolyse, deux incidences, signes de face

Corrections faites :
- 5 citations Smarter Medicine au format commun (guillemets, liste, numéro), texte inchangé
- Renvois internes retirés du contenu (arthro-IRM limite ; radiographie de l'enfant seuil ; 2 champs sources « Signes classiques ; voir aVerifier » → Ziebarth et Liebs, Forum Médical Suisse 2022)
- Seuil de la radiographie de l'enfant complété par les signes de face de l'épiphysiolyse (source relue)
- referencePour et 9 options/bonneReponse de plus de 45 caractères raccourcies ; glossaire + T1, T2
- Réserve CT tranchée : 11,0 mSv gardé (ligne hanche/cuisse du tableau 16) ; bassin 7,9 mSv noté dans aVerifier
- Réserves gardées dans aVerifier : arthro-IRM (narratif ACR), Perthes, pourcentages de Kocher non employés dans le texte
- Décision : les sigles ajoutés au glossaire sont gardés ; les citations Smarter Medicine mises au format commun sont gardées (vérifiées mot pour mot)
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main ; la fusion ne reprend pas le _meta du lot
- Correction post-contrôle (23.11.2026) : referencePour vides rétablis exactement comme sur la conception de origin/main ; rien d'autre modifié ; controle PASS.
