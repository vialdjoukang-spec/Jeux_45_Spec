# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:10 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P09-01-BIO_Biologie_Sang_et_hemostase_11-examens_production_XAi.json
- 1_Theorie/P09-01-FCT_Exploration_fonctionnelle_Sang_et_hemostase_2-examens_production_XAi.json
- 2_Pratique/P09-01-BIO-PR_Biologie_Sang_et_hemostase_11-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P09-01-FCT-PR_Exploration_fonctionnelle_Sang_et_hemostase_2-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- BJA Education 2022, « Point-of-care viscoelastic testing » : ROTEM/TEG standard peu sensibles à l'aspirine, aux anti-P2Y12, à la maladie de von Willebrand et aux AOD à faible concentration (source désormais nommée)
- Sources sondées au contre-audit indépendant du 22.11 (lecture seule), corrections reprises ici

Corrections faites :
- P09-01-FCT — correction du contre-audit 09-01 (texte relu) : « Elle détecte mal l’effet de l’aspirine, des inhibiteurs plaquettaires du récepteur à l’ADP, des anticoagulants oraux directs à faible concentration et de la maladie de von Willebrand. » → « Elle détecte mal l’effet de l’aspirine, des inhibiteurs plaquettaires du récepteur à l’ADP, des anticoagulants oraux directs à faible concentration et de la maladie de von Willebrand, selon la revue « Point-of-care visco »
- P09-01-FCT — sigle absent du glossaire (C3) : « None » → « glossaire[BJA]=British Journal of Anaesthesia, revue britannique d'anesthésie. »
- P09-01-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[CD10]=Antigène de différenciation des lymphocytes B immatures (CALLA), recherché en cytométrie de flux. »
- P09-01-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[CD19]=Antigène de surface de la lignée lymphocytaire B, recherché en cytométrie de flux. »
- P09-01-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[CD22]=Antigène de surface des lymphocytes B, recherché en cytométrie de flux. »
- P09-01-BIO-PR — sigle absent du glossaire (C3) : « None » → « glossaire[CD10]=Antigène de différenciation des lymphocytes B immatures (CALLA), recherché en cytométrie de flux. »
- P09-01-BIO-PR — sigle absent du glossaire (C3) : « None » → « glossaire[CD19]=Antigène de surface de la lignée lymphocytaire B, recherché en cytométrie de flux. »
- P09-01-BIO-PR — sigle absent du glossaire (C3) : « None » → « glossaire[CD22]=Antigène de surface des lymphocytes B, recherché en cytométrie de flux. »

## Seconde vérification des sources (23.11.2026 00:46, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 1 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Ferritine de 30 à 50 µg/l avec saturation < 20 % : carence probable | étude Delphi suisse 2019 (Swiss Med Wkly, PubMed 31269223) | conforme |
| 2 | Fibrinogène de Clauss ≤ 1,5 g/l : substitution | ESAIC 2023, saignement périopératoire sévère | conforme |
| 3 | Lymphocytes B ≥ 5 × 10⁹/l pendant au moins 3 mois : LLC | iwCLL, Hallek et al. | conforme |
| 4 | VWF < 0,30 UI/ml : maladie de von Willebrand de type 1 | ASH/ISTH/NHF/WFH 2021 (PMC7805340) | conforme |
| 5 | Score HEMOSTOP ≥ 2 | Lovey et Stalder, Hôpital du Valais 2024 : non trouvé | non trouvé : ajouté à _lot.aVerifier |
