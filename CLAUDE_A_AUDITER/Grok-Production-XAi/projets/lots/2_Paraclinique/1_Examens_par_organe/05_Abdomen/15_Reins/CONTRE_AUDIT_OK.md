# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:05 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P05-15-BIO_Biologie_Reins_10-examens_production_XAi.json
- 1_Theorie/P05-15-HIS_Anatomopathologie_biopsie_Reins_1-examens_production_XAi.json
- 1_Theorie/P05-15-IMG_Imagerie_Reins_7-examens_production_XAi.json
- 2_Pratique/P05-15-BIO-PR_Biologie_Reins_10-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P05-15-HIS-PR_Anatomopathologie_biopsie_Reins_1-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P05-15-IMG-PR_Imagerie_Reins_7-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Directive OFSP R-06-06 (rév. 2, 2018), tableau 1, relue dans le PDF de l'OFSP : valeurs cibles abdomen-bassin 470, angio-CT abdomen-bassin 450, calculs rénaux 180, thorax-abdomen-bassin 610 mGy·cm
- Directive OFSP de médecine nucléaire (drw-nuk), tableau 1.1, relue dans le PDF de l'OFSP : MAG3 100 MBq 0,7 mSv ; DMSA 120 MBq 1,1 mSv ; MIBG 200 MBq 2,6 mSv
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (radiologie 2020, angiologie 2024)

Corrections faites :
- P05-15-BIO-PR — libellé > 45 car. : « Sodium urinaire et fraction excrétée du sodium » → « Sodium urinaire et fraction excrétée »
- P05-15-BIO-PR — libellé > 45 car. : « Analyse du calcul par spectroscopie infrarouge » → « Spectroscopie infrarouge du calcul »

Remarques :
- Uro-CT 14,1 mSv : deux acquisitions à la valeur cible abdomen-bassin, calcul documenté, conservé.
