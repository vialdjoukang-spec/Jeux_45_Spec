# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:10 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P09-02_Examens_Moelle_osseuse_et_ganglions_6-examens_production_XAi.json
- 2_Pratique/P09-02-PR_Examens_Moelle_osseuse_et_ganglions_6-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Directive OFSP R-06-06 (rév. 2, 2018), relue dans le PDF : thorax-abdomen-bassin 610 mGy·cm
- Consensus européen de Thiele et al. (2005) : grades MF-0 à MF-3 (définitions ajoutées au glossaire)
- ELN 2022 (Döhner et al.) : ≥ 20 métaphases, caryotype complexe ≥ 3 anomalies (Sources sondées au contre-audit indépendant du 22.11 (lecture seule), corrections reprises ici)

Corrections faites :
- P09-02 — sigle absent du glossaire (C3) : « None » → « glossaire[DFG]=Débit de filtration glomérulaire, estimé à partir de la créatinine, en ml/min/1,73 m². »
- P09-02 — sigle absent du glossaire (contre-audit 09-02) : « None » → « glossaire[MF-0]=MF-0 est le grade de la moelle sans fibrose réticulinique notable, selon le consensus européen de Thiele et al. (2005). »
- P09-02 — sigle absent du glossaire (contre-audit 09-02) : « None » → « glossaire[MF-2]=MF-2 est le grade d'une fibrose réticulinique dense et diffuse, avec un collagène focal, selon le consensus européen de Thiele et al. (2005). »
- P09-02 — sigle absent du glossaire (contre-audit 09-02) : « None » → « glossaire[MF-3]=MF-3 est le grade d'une fibrose dense avec du collagène épais, souvent associée à une ostéosclérose, selon le consensus européen de Thiele et al. (2005). »
- P09-02-PR — sigle absent du glossaire (contre-audit 09-02) : « None » → « glossaire[MF-0]=MF-0 est le grade de la moelle sans fibrose réticulinique notable, selon le consensus européen de Thiele et al. (2005). »
- P09-02-PR — sigle absent du glossaire (contre-audit 09-02) : « None » → « glossaire[MF-1]=MF-1 est le grade d'une fibrose réticulinique lâche, sans collagène, selon le consensus européen de Thiele et al. (2005). »
- P09-02-PR — sigle absent du glossaire (contre-audit 09-02) : « None » → « glossaire[MF-3]=MF-3 est le grade d'une fibrose dense avec du collagène épais, souvent associée à une ostéosclérose, selon le consensus européen de Thiele et al. (2005). »
- P09-02 — sigle absent du glossaire (C3) : « None » → « glossaire[TEP-CT]=Tomographie par émission de positons couplée au CT, synonyme de PET-CT. »

## Seconde vérification des sources (23.11.2026 00:46, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Ganglion mesurable au-delà de 1,5 cm ; rate > 13 cm | Cheson et al., classification de Lugano 2014 (PMC4979083) | conforme |
| 2 | Caryotype normal sur au moins 20 métaphases | ELN, Döhner et al. 2022 | conforme |
| 3 | Caryotype complexe (≥ 3 anomalies) : risque défavorable | ELN 2022 | conforme |
| 4 | Plasmocytes clonaux ≥ 10 % : myélome | IMWG 2014 | conforme |
| 5 | CT thorax-abdomen-bassin : 610 mGy·cm, 9,2 mSv | OFSP R-06-06 rév. 2, protocole 12 | conforme |
