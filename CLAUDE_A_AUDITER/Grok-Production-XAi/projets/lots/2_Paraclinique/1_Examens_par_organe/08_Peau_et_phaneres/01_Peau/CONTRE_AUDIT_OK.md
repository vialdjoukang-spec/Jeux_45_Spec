# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:10 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P08-01-BIO_Biologie_Peau_4-examens_production_XAi.json
- 1_Theorie/P08-01-FCT_Exploration_fonctionnelle_Peau_4-examens_production_XAi.json
- 1_Theorie/P08-01-HIS_Anatomopathologie_biopsie_Peau_2-examens_production_XAi.json
- 1_Theorie/P08-01-IMG_Imagerie_Peau_3-examens_production_XAi.json
- 2_Pratique/P08-01-BIO-PR_Biologie_Peau_4-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P08-01-FCT-PR_Exploration_fonctionnelle_Peau_4-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P08-01-HIS-PR_Anatomopathologie_biopsie_Peau_2-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P08-01-IMG-PR_Imagerie_Peau_3-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Liste Top 5 Smarter Medicine de la SSDV (2020), smartermedicine.ch : citations comparées mot pour mot (items 1, 3, 4, 5)
- Sources sondées au contre-audit indépendant du 22.11 (lecture seule), corrections reprises ici

Corrections faites :
- P08-01-BIO — correction du contre-audit 08-01 (texte relu) : « On n'entreprend un traitement antifongique systémique pour une mycose des ongles suspectée que si un champignon a été mis en évidence, selon Smarter Medicine, liste Top 5 de la Société suisse de dermatologie et vénéréolo » → « « N'effectuer un traitement antifongique systémique en cas de mycoses des ongles suspectées que si un champignon est détecté. », selon Smarter Medicine, liste Top 5 de la Société suisse de dermatologie et vénéréologie (S »
- P08-01-BIO — correction du contre-audit 08-01 (texte relu) : « On ne fait pas de sérologie pour diagnostiquer une infection cutanée à HSV, selon Smarter Medicine, liste Top 5 de la Société suisse de dermatologie et vénéréologie (SSDV, 2020). » → « « Éviter les tests sérologiques pour le diagnostic des infections cutanées par le virus de l'herpès simplex. », selon Smarter Medicine, liste Top 5 de la Société suisse de dermatologie et vénéréologie (SSDV, 2020). »
- P08-01-HIS — correction du contre-audit 08-01 (texte relu) : « On n'interrompt pas l'anticoagulation pour une intervention de chirurgie cutanée, selon Smarter Medicine, liste Top 5 de la Société suisse de dermatologie et vénéréologie (SSDV, 2020). » → « « Ne pas interrompre l'anticoagulation dans les procédures dermatochirurgicales. », selon Smarter Medicine, liste Top 5 de la Société suisse de dermatologie et vénéréologie (SSDV, 2020). »
- P08-01-HIS — correction du contre-audit 08-01 (texte relu) : « On renonce à l'antibioprophylaxie périopératoire pour une chirurgie cutanée sans facteur de risque supplémentaire, selon Smarter Medicine, liste Top 5 de la Société suisse de dermatologie et vénéréologie (SSDV, 2020). » → « « Renoncer à la prophylaxie antibiotique périopératoire pour les opérations de la peau sans facteurs de risque supplémentaires. », selon Smarter Medicine, liste Top 5 de la Société suisse de dermatologie et vénéréologie  »
- P08-01-BIO-PR — libellé > 45 car. : « Immunofluorescence indirecte et ELISA anti-BP180 » → « IFI et ELISA anti-BP180 »
- P08-01-HIS-PR — libellé > 45 car. : « Biopsie au punch avec immunofluorescence directe » → « Biopsie au punch avec IFD »
- P08-01-HIS-PR — sigle absent du glossaire (C3) : « None » → « glossaire[IFD]=Immunofluorescence directe, sur biopsie, qui montre des dépôts d'anticorps ou de complément dans le tissu. »
- P08-01-BIO-PR — sigle absent du glossaire (C3) : « None » → « glossaire[IFI]=Immunofluorescence indirecte, sur coupe ou cellule, qui détecte des anticorps circulants. »
