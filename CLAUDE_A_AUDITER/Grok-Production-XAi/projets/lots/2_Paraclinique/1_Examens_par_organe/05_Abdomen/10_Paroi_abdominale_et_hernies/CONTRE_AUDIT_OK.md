# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:05 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P05-10_Examens_Paroi_abdominale_et_hernies_4-examens_production_XAi.json
- 2_Pratique/P05-10-PR_Examens_Paroi_abdominale_et_hernies_4-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Directive OFSP R-06-06 (rév. 2, 2018), tableau 1, relue dans le PDF de l'OFSP : valeurs cibles abdomen-bassin 470, angio-CT abdomen-bassin 450, calculs rénaux 180, thorax-abdomen-bassin 610 mGy·cm
- WSES 2017 (Birindelli et al.) et HerniaSurge 2018 (Sondage de sources déjà fait au contre-audit indépendant du 22.11 (lecture seule), repris et complété ici)
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (radiologie 2020, angiologie 2024)

Corrections faites :
- P05-10-PR — libellé > 45 car. : « Sac herniaire graisseux qui franchit l'orifice inguinal profond » → « Sac graisseux franchissant l'orifice profond »
- P05-10-PR — libellé > 45 car. : « Paroi de l'anse herniée peu rehaussée, liquide dans le sac » → « Anse herniée peu rehaussée, liquide du sac »
- P05-10-PR — libellé > 45 car. : « Tuméfaction sous le ligament inguinal, en dedans de la veine fémorale » → « Masse sous-inguinale médiale à la veine »

## Seconde vérification des sources (23.11.2026 00:40, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Rehaussement pariétal diminué : sensibilité 56 %, spécificité 94 % | WSES, mise à jour 2017 (World J Emerg Surg, texte Springer ; étude de Jancelewicz) | conforme |
| 2 | Examen de l'aine : sensibilité 0,745, spécificité 0,963 | HerniaSurge Group 2018 (cité par des sources secondaires) | conforme |
| 3 | Diastasis des grands droits : écart de plus de 2 cm | EHS, Br J Surg 2021;108:1189 (PubMed 34595502) | conforme |
| 4 | CT abdomen-bassin : 7,1 mSv | OFSP R-06-06 rév. 2, protocole 8 | conforme |
| 5 | Signes du CT injecté, lactate, CPK et D-dimères prédisent l'étranglement (grade 1C) | WSES, mise à jour 2017 (texte Springer) | conforme |
