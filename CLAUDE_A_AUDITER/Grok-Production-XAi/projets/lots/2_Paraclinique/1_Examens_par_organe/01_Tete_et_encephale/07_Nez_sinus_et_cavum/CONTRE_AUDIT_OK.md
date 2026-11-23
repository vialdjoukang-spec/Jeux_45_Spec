# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 01:07 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P01-07-BIO_Biologie_Nez_sinus_et_cavum_4-examens_production_XAi.json
- 1_Theorie/P01-07-END_Endoscopie_Nez_sinus_et_cavum_2-examens_production_XAi.json
- 1_Theorie/P01-07-FCT_Exploration_fonctionnelle_Nez_sinus_et_cavum_3-examens_production_XAi.json
- 1_Theorie/P01-07-HIS_Anatomopathologie_biopsie_Nez_sinus_et_cavum_1-examens_production_XAi.json
- 1_Theorie/P01-07-IMG_Imagerie_Nez_sinus_et_cavum_2-examens_production_XAi.json
- 2_Pratique/P01-07-BIO-PR_Biologie_Nez_sinus_et_cavum_4-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P01-07-END-PR_Endoscopie_Nez_sinus_et_cavum_2-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P01-07-FCT-PR_Exploration_fonctionnelle_Nez_sinus_et_cavum_3-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P01-07-HIS-PR_Anatomopathologie_biopsie_Nez_sinus_et_cavum_1-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P01-07-IMG-PR_Imagerie_Nez_sinus_et_cavum_2-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- EPOS 2020 : Lund-Kennedy ≥ 2, sensibilité 0,84, spécificité 0,79 face au CT ; Lund-Mackay ≤ 2 exclut, ≥ 5 confirme ; ~18 % d’adultes asymptomatiques avec épaississement muqueux discret ; perte de rehaussement IRM 86 % contre 69 % au CT ; radiographies des sinus plus indiquées ✔
- Oleszkiewicz et al. 2019 (Sniffin’ Sticks) : hyposmie TDI < 30,75 ; anosmie fonctionnelle ≤ 16 ✔
- Heinzerling et al., EAACI 2013 : papule ≥ 3 mm, lecture à 15–20 min ; antihistaminiques de 2e génération arrêtés 7 jours avant ✔
- Bossuyt et al., consensus international 2017 sur les ANCA : immunodosages anti-PR3 et anti-MPO en première intention sans immunofluorescence préalable ; second test si suspicion forte ✔
- OFSP R-06-06 rév. 2 (2018), tableau 1 : sinusite basse dose 6 mGy et 90 mGy·cm, valeur cible 5 mGy et 70 mGy·cm ; massif facial 25 mGy et 420 mGy·cm ✔
- Oakley et al., Int Forum Allergy Rhinol 2016 : glucose non retenu ; transferrine β2 test de confirmation le plus fiable ✔
- Smarter Medicine SSORL 2019 n° 2, smartermedicine.ch ✔

Corrections faites :
- Transferrine β2 (plutotQue) : « Elle remplace le dosage du glucose de l'écoulement, qui ne permet pas de conclure. » (sans source) → « … que la revue d'Oakley et al. (Int Forum Allergy Rhinol, 2016) ne retient pas pour identifier une fuite de LCR. » ; entrée aVerifier correspondante retirée
- Transferrine β2 : referencePour [« Rhinorrhée de LCR »] → [] (vide sur main)
- Smarter Medicine SSORL 2019 n° 2 (2 citations) : format commun avec numéro
- aVerifier IgE spécifiques 0,35 kUA/l : complété (document de position WAO 2020 relu, seuil chiffré non trouvé)
- Dose du CT des sinus : 0,15 mSv gardée (valeur cible R-06-06 basse dose 70 mGy·cm × facteur AAPM, convention du projet) ; OFSP 2018 tableau 16 donne 2,36 mSv pour l’ensemble « massif facial et sinus », noté
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main ; le _lot.aVerifier est ajouté comme dans les autres dépôts ; les « reponse » de défis de plus de 45 caractères sont des réponses rédigées, signalées et non raccourcies.

Réserves conservées dans _lot.aVerifier :
- IgE spécifiques : seuil technique de 0,35 kUA/l sans source suisse (WAO 2020 relu, seuil non trouvé)
- rhinoscopie : sémiologie classique sans source nommée relue
- IRM des sinus et du cavum : significations de la masse rehaussée et de l’extension orbitaire sans source nommée relue
