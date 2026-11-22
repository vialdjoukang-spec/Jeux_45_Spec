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

## Seconde vérification des sources (23.11.2026 00:40, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 1 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Microhématurie : au moins 3 hématies par champ | AUA/SUFU 2020 | conforme |
| 2 | Uro-CT : sensibilité groupée 92 %, spécificité 95 % | EAU, carcinome urothélial de la voie excrétrice supérieure (uroweb.org, chapitre diagnostic) | conforme |
| 3 | Biopsie rénale : au moins 8 à 10 glomérules | KDIGO 2021, maladies glomérulaires | conforme |
| 4 | Risque de lésion rénale due au contraste sous 30 ml/min/1,73 m² | ESUR 2025 (esur.org) | conforme |
| 5 | Rapport réno-aortique de 3,5 pour une sténose de plus de 60 %, « selon l'ESVS 2025 » | valeur confirmée par d'autres sources (ERBP/ESH 2023) ; non trouvée dans l'ESVS 2025 | non trouvé (source nommée) : ajouté à _lot.aVerifier |
