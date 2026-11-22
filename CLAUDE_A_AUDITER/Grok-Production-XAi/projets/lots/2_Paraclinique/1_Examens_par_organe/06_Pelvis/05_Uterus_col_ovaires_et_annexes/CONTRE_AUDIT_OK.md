# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:40 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P06-05-BIO_Biologie_Uterus_col_ovaires_et_annexes_5-examens_production_XAi.json
- 1_Theorie/P06-05-END_Endoscopie_Uterus_col_ovaires_et_annexes_3-examens_production_XAi.json
- 1_Theorie/P06-05-HIS_Anatomopathologie_biopsie_Uterus_col_ovaires_et_annexes_3-examens_production_XAi.json
- 1_Theorie/P06-05-IMG_Imagerie_Uterus_col_ovaires_et_annexes_4-examens_production_XAi.json
- 2_Pratique/P06-05-BIO-PR_Biologie_Uterus_col_ovaires_et_annexes_5-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P06-05-END-PR_Endoscopie_Uterus_col_ovaires_et_annexes_3-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P06-05-HIS-PR_Anatomopathologie_biopsie_Uterus_col_ovaires_et_annexes_3-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P06-05-IMG-PR_Imagerie_Uterus_col_ovaires_et_annexes_4-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- HPA-CRCE-012 (Hart et al., 2010) : hystérosalpingographie 0,42 mSv
- Smarter Medicine SSGO 2022 (recommandations 2, 3 et 5) et SSR 2020 (recommandation 4) : texte exact retrouvé

Corrections faites :
- _meta remis à l'identique du squelette de lot de main (le fragment portait la version du fichier de conception, avec trois clés de plus ; la fusion ne reprend pas _meta du lot)
- Sigle R1 ajouté au glossaire
- Décision : les sigles ajoutés au glossaire pour respecter Q7 sont gardés ; le rejet « clés ajoutées » du contrôle de forme est un faux positif
- Décision : les citations Smarter Medicine remplacées mot pour mot sont gardées ; vérifiées contre les listes Top 5 publiées
