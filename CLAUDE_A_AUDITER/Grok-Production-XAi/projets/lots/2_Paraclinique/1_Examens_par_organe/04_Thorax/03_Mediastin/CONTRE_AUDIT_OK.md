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
