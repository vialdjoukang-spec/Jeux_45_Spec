# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:05 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P05-12_Examens_Retroperitoine_5-examens_production_XAi.json
- 2_Pratique/P05-12-PR_Examens_Retroperitoine_5-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Directive OFSP R-06-06 (rév. 2, 2018), tableau 1, relue dans le PDF de l'OFSP : valeurs cibles abdomen-bassin 470, angio-CT abdomen-bassin 450, calculs rénaux 180, thorax-abdomen-bassin 610 mGy·cm
- TARPSWG 2021 ; Berny et al., Research in Diagnostic and Interventional Imaging 2023 (762,5 mGy·cm) ; KDIGO 2012 (Sondage de sources déjà fait au contre-audit indépendant du 22.11 (lecture seule), repris et complété ici)
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (radiologie 2020, angiologie 2024)

Corrections faites :
- P05-12-PR — libellé > 45 car. : « Plaque homogène périaortique, isodense au muscle, uretères déviés en dedans » → « Manchon périaortique et uretères médialisés »
- P05-12-PR — libellé > 45 car. : « Expression de MDM2 par des adipocytes atypiques » → « MDM2 exprimé par des adipocytes atypiques »
- P05-12 — aVerifier précisé (contre-audit 05-12) : « conception/donnees/paraclinique/topographie/5_abdomen/retroperitoine.json › retroperitoine__biopsie_scanoguidee_d_une_masse_retroper › irradiation_mSv : 11,4 mSv = 762,5 mGy·cm (moyenne estimée en analyse multivariable p » → « conception/donnees/paraclinique/topographie/5_abdomen/retroperitoine.json › retroperitoine__biopsie_scanoguidee_d_une_masse_retroper › irradiation_mSv : 11,4 mSv = 762,5 mGy·cm (moyenne estimée en analyse multivariable p »

Remarques :
- Point laissé à la décision de l'audit médical : prelevementRef « biopsies_tissulaires » sur la biopsie scanoguidée (la règle 4.1 réserve ce champ à la biologie).

## Seconde vérification des sources (23.11.2026 00:40, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Hausse de créatinine d'au moins 26,5 µmol/l en 48 h : insuffisance rénale aiguë | KDIGO 2012 | conforme |
| 2 | Biopsie scanoguidée : 762,5 mGy·cm | Berny et al. 2023, enquête française (PMC11265189) | conforme (moyenne ajustée, 141 gestes) |
| 3 | Biopsie scanoguidée : environ 11,4 mSv | calcul 762,5 × 0,015 (AAPM 96) | conforme (11,44) |
| 4 | CT abdomen-bassin : 7,1 mSv | OFSP R-06-06 rév. 2, protocole 8 | conforme |
| 5 | MDM2 : liposarcome bien différencié ou dédifférencié | TARPSWG 2021 | conforme sur le principe (non chiffré) |
