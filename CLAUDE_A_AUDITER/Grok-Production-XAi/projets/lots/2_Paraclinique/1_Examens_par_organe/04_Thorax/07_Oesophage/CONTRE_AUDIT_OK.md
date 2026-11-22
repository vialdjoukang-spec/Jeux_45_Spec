# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:58 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P04-07_Examens_Oesophage_8-examens_production_XAi.json
- 2_Pratique/P04-07-PR_Examens_Oesophage_8-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Mönig, Chevallay et al., Rev Med Suisse 2020;16:1292-9 : écho-endoscopie, sensibilité 81 à 92 % et spécificité 94 à 97 % dans les carcinomes avancés T3-T4 ; CT cou-thorax-abdomen pour la catégorie M
- Classification de Chicago 4.0 (Yadlapati et al., 2021) : achalasie de type II, IRP élevée et pressurisation panœsophagienne dans au moins 20 % des déglutitions
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (smartermedicine.ch)

Corrections faites :
- P04-07 — précision : la sensibilité publiée porte sur T3-T4 (texte relu) : « que l'examen évalue avec une sensibilité de 81 à 92 %, selon Mönig et Chevallay (Rev Med Suisse 2020). » → « que l'examen évalue avec une sensibilité de 81 à 92 % pour les tumeurs avancées (T3-T4), selon Mönig et Chevallay (Rev Med Suisse 2020). »

Remarques :
- Doses CT calculées sur la directive OFSP R-06-06 : calcul documenté en entrée à vérifier, conservé ; comparateur OFSP 2018 tableau 16 : CT du thorax 3,8 mSv.

## Seconde vérification des sources (23.11.2026 00:36, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Achalasie de type I : 100 % de déglutitions sans contraction | Chicago 4.0, Yadlapati et al. 2021 | conforme |
| 2 | Achalasie de type II : au moins 20 % de pressurisation panœsophagienne | Chicago 4.0 | conforme |
| 3 | Œsophagite à éosinophiles : muqueuse normale dans environ 30 % des cas | Godat, Schoepfer et Moradpour, Rev Med Suisse 2011;7:1678 | conforme |
| 4 | CT thorax-abdomen-bassin : 610 mGy·cm, 9,2 mSv | OFSP R-06-06 rév. 2, protocole 12 | conforme (610 × 0,015 = 9,15) |
| 5 | CT du cou : 290 mGy·cm | OFSP R-06-06 rév. 2, protocole 4 | conforme |
