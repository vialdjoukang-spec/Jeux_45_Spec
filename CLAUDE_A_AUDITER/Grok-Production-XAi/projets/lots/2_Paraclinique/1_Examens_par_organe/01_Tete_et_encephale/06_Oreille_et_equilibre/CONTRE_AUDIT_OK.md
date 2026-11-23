# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 01:07 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P01-06-BIO_Biologie_Oreille_et_equilibre_2-examens_production_XAi.json
- 1_Theorie/P01-06-FCT_Exploration_fonctionnelle_Oreille_et_equilibre_9-examens_production_XAi.json
- 1_Theorie/P01-06-IMG_Imagerie_Oreille_et_equilibre_3-examens_production_XAi.json
- 2_Pratique/P01-06-BIO-PR_Biologie_Oreille_et_equilibre_2-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P01-06-FCT-PR_Exploration_fonctionnelle_Oreille_et_equilibre_9-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P01-06-IMG-PR_Imagerie_Oreille_et_equilibre_3-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Strupp et al., Bárány Society 2022 (vestibulopathie unilatérale aiguë) : gain du vHIT < 0,7 ; asymétrie calorique > 25 % (formule de Jongkees) ✔
- Strupp et al., Bárány Society 2017 (vestibulopathie bilatérale) : somme des vitesses calorique < 6 °/s de chaque côté ✔
- Nakashima et al. 2009 : hydrops vestibulaire > 33 %, significatif > 50 % ✔
- NICE NG98 (2018) : asymétrie ≥ 15 dB sur deux fréquences voisines (0,5 à 8 kHz) → IRM ; surdité brusque < 30 jours → avis dans les 24 h ✔
- Niu et al., AJNR 2010 : CT hélicoïdal du rocher, dose efficace 0,803 mSv ✔
- Rosenfeld et al., AAO-HNS 2014 (otite externe aiguë) : Pseudomonas aeruginosa 20 à 60 %, Staphylococcus aureus 10 à 70 % ✔
- OFSP R-06-06 rév. 2 (2018), tableau pédiatrique : rochers 20 mGy et 110 mGy·cm avant 1,5 an ; 30 mGy et 200 mGy·cm dès 1,5 an ✔
- Smarter Medicine SSORL 2019 n° 4 et n° 5 ; SSINF 2020 n° 2, smartermedicine.ch ✔

Corrections faites :
- Smarter Medicine (4 citations) : format commun avec numéro (SSORL 2019 n° 4 ×2, n° 5 ; SSINF 2020 n° 2) ; Borrelia : paraphrase « … » figure parmi les interventions à éviter, car elle ne permet pas de conclure à une activité de la maladie » → « « Réalisation d’une sérologie Borrelia sans symptômes spécifiques. », selon Smarter Medicine, liste Top 5 de la Société suisse d’infectiologie (SSINF, 2020), recommandation 2. »
- IRM de l’oreille interne : referencePour [« Hydrops endolymphatique »] → [] (vide sur main)
- Dose du CT des rochers : 0,8 mSv (Niu et al. 2010, valeur acceptée sur main) gardée ; R-06-06 n’a pas de ligne adulte pour le rocher (valeurs pédiatriques seules, relues) ; OFSP 2018 tableau 16 n’a pas de ligne rocher (neurocrâne 2,36 mSv)
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main ; le _lot.aVerifier est ajouté comme dans les autres dépôts ; les « reponse » de défis de plus de 45 caractères sont des réponses rédigées, signalées et non raccourcies.

Réserves conservées dans _lot.aVerifier (doutes honnêtes du rédacteur, non résolus dans ce contre-audit) :
- sérologies de la surdité brusque : interprétation tréponémique/non tréponémique et conduite chez la femme enceinte sans source nommée relue
- otoscopie : description du tympan normal sans source nommée relue
- CT des rochers : significations radiologiques classiques sans source nommée relue
