# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:58 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P04-03-BIO_Biologie_Mediastin_4-examens_production_XAi.json
- 1_Theorie/P04-03-END_Endoscopie_Mediastin_2-examens_production_XAi.json
- 1_Theorie/P04-03-HIS_Anatomopathologie_biopsie_Mediastin_2-examens_production_XAi.json
- 1_Theorie/P04-03-IMG_Imagerie_Mediastin_3-examens_production_XAi.json
- 2_Pratique/P04-03-BIO-PR_Biologie_Mediastin_4-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-03-END-PR_Endoscopie_Mediastin_2-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-03-HIS-PR_Anatomopathologie_biopsie_Mediastin_2-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-03-IMG-PR_Imagerie_Mediastin_3-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- ECA sérique dans la sarcoïdose : sensibilité 22 à 86 %, spécificité 54 à 95 % (Kraaijvanger et al., Front Immunol 2020, et synthèses citant ces séries) ; ATS 2020 (Crouser) : ECA élevée comme élément d'appui seulement
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (smartermedicine.ch)

Corrections faites :
- P04-03-IMG — libellé > 45 car. : « Imagerie par résonance magnétique médiastinale » → « Résonance magnétique médiastinale »
- P04-03-BIO-PR — libellé > 45 car. : « ECA en appoint, avec une preuve histologique si nécessaire » → « ECA en appoint, histologie si nécessaire »
- P04-03-HIS-PR — libellé > 45 car. : « Biopsie tissulaire de la masse ou d'un ganglion » → « Biopsie de la masse ou d'un ganglion »
- P04-03-IMG-PR — libellé > 45 car. : « IRM médiastinale avec séquences en opposition de phase » → « IRM avec séquences en opposition de phase »

Remarques :
- Doses CT calculées sur la directive OFSP R-06-06 : calcul documenté en entrée à vérifier, conservé ; comparateur OFSP 2018 tableau 16 : CT du thorax 3,8 mSv.

## Seconde vérification des sources (23.11.2026 00:36, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | EBUS/EUS : stations 4R, 4L et 7 au minimum | ESGE/ERS/ESTS, Vilmann et al. 2015 (PubMed 26062074, notice) | conforme sur le principe (résumé consulté ; liste des stations non lue dans le résumé) |
| 2 | Glycémie ≥ 11 mmol/l : reporter le PET-CT | EANM, Boellaard et al. 2015 (texte de la procédure, Springer/SNMMI) | conforme |
| 3 | PET-CT au FDG : environ 8,8 mSv | OFSP, directive de médecine nucléaire (drw-nuk.pdf, téléchargé le 23.11.2026) et valeur retenue de 8,8 mSv | conforme |
| 4 | CT thoracique : 210 mGy·cm, environ 2,9 mSv | OFSP R-06-06 rév. 2 du 15.06.2018, tableau 1, protocole 6 (PDF téléchargé le 23.11.2026) | conforme (210 × 0,014 = 2,94) |
| 5 | LDH > 1,5 × la normale : pronostic intermédiaire des TGNS | IGCCCG 1997 (critères publiés : LDH 1,5 à 10 × N) | conforme |
