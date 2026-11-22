# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:40 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P06-01-BIO_Biologie_Vessie_et_uretre_3-examens_production_XAi.json
- 1_Theorie/P06-01-END_Endoscopie_Vessie_et_uretre_1-examens_production_XAi.json
- 1_Theorie/P06-01-FCT_Exploration_fonctionnelle_Vessie_et_uretre_3-examens_production_XAi.json
- 1_Theorie/P06-01-HIS_Anatomopathologie_biopsie_Vessie_et_uretre_1-examens_production_XAi.json
- 1_Theorie/P06-01-IMG_Imagerie_Vessie_et_uretre_4-examens_production_XAi.json
- 2_Pratique/P06-01-BIO-PR_Biologie_Vessie_et_uretre_3-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P06-01-END-PR_Endoscopie_Vessie_et_uretre_1-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P06-01-FCT-PR_Exploration_fonctionnelle_Vessie_et_uretre_3-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P06-01-HIS-PR_Anatomopathologie_biopsie_Vessie_et_uretre_1-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P06-01-IMG-PR_Imagerie_Vessie_et_uretre_4-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- OFSP R-06-06 révision 2 (2018) : abdomen-bassin, valeur cible 470 mGy·cm ; uro-CT 14,1 mSv = 2 acquisitions × 470 × 0,015
- HPA-CRCE-012 (Hart et al., 2010) : urétrographie 1,3 mSv
- Smarter Medicine SSGO 2022 (recommandation 1) et SSR 2020 (recommandations 2 et 3) : texte exact retrouvé

Corrections faites :
- _meta remis à l'identique du squelette de lot de main (le fragment portait la version du fichier de conception, avec trois clés de plus ; la fusion ne reprend pas _meta du lot)
- Synonyme de plus de 45 caractères raccourci : « PCR des infections sexuelles »
- Décision : les sigles ajoutés au glossaire pour respecter Q7 sont gardés ; le rejet « clés ajoutées » du contrôle de forme est un faux positif
- Décision : les citations Smarter Medicine remplacées mot pour mot sont gardées ; vérifiées contre les listes Top 5 publiées
