# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:05 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P05-16_Examens_Ureteres_9-examens_production_XAi.json
- 2_Pratique/P05-16-PR_Examens_Ureteres_9-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Directive OFSP R-06-06 (rév. 2, 2018), tableau 1, relue dans le PDF de l'OFSP : valeurs cibles abdomen-bassin 470, angio-CT abdomen-bassin 450, calculs rénaux 180, thorax-abdomen-bassin 610 mGy·cm
- Directive OFSP de médecine nucléaire (drw-nuk), tableau 1.1, relue dans le PDF de l'OFSP : MAG3 100 MBq 0,7 mSv ; DMSA 120 MBq 1,1 mSv ; MIBG 200 MBq 2,6 mSv
- Rapport HPA-CRCE-012 (Hart et al., 2010), annexe, relu dans le PDF : pyélographie rétrograde E103 1,58 mSv (bilatérale 3,09) ; cavographie inférieure 1,33 mSv

Corrections faites :
- P05-16-PR — libellé > 45 car. : « Culture d'urine et hémocultures avant l'antibiotique » → « Uroculture et hémocultures avant antibiotique »

Remarques :
- Éditions EAU et AUA/SUFU signalées en entrée à vérifier par le rédacteur, conservées.

## Seconde vérification des sources (23.11.2026 00:40, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Microhématurie : au moins 3 hématies par champ à fort grossissement | AUA/SUFU 2020 | conforme |
| 2 | Hausse d'au moins 26,5 µmol/l en 48 h | KDIGO 2012 | conforme |
| 3 | Metformine arrêtée à l'injection, DFGe contrôlé dans les 48 h | ESUR 2025 | conforme |
| 4 | Uro-CT : 2 × 7,05 = 14,1 mSv | OFSP R-06-06 rév. 2, protocole 8 | conforme (calcul) |
| 5 | Uro-CT : sensibilité 92 %, spécificité 95 % | EAU UTUC (uroweb.org) | conforme |
