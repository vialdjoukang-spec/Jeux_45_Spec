# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:40 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P06-02_Examens_Prostate_et_vesicules_seminales_6-examens_production_XAi.json
- 2_Pratique/P06-02-PR_Examens_Prostate_et_vesicules_seminales_6-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- RCP Locametz (EMA), section 11 : 0,022 mSv/MBq ; 1,8 à 2,2 MBq/kg, 111 à 259 MBq
- Monnin et al., Z Med Phys 2026 : NRD suisse PET [18F]F-PSMA 3,1 MBq/kg, maximum 260 MBq (en comparaison)
- Smarter Medicine médecine interne générale ambulatoire 2014, recommandation 2 (PSA) : texte exact retrouvé

Corrections faites :
- _meta remis à l'identique du squelette de lot de main (le fragment portait la version du fichier de conception, avec trois clés de plus ; la fusion ne reprend pas _meta du lot)
- PET-PSMA : dose 7,4 mSv gardée (décision : ne pas la remplacer par 8,8 mSv du PET-CT FDG) ; source ajoutée dans le texte (0,022 mSv/MBq pour 154 MBq, RCP Locametz de l'EMA, plus le CT d'atténuation)
- Option QCM et bonneReponse de plus de 45 caractères raccourcies : « Discuter risques et bénéfices avant le PSA »
- Décision : les sigles ajoutés au glossaire pour respecter Q7 sont gardés ; le rejet « clés ajoutées » du contrôle de forme est un faux positif
- Décision : les citations Smarter Medicine remplacées mot pour mot sont gardées ; vérifiées contre les listes Top 5 publiées
