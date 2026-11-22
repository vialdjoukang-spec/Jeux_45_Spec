# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:58 (heure de Zurich).
Verdict : conforme, sans correction

Fichiers contrôlés :
- 1_Theorie/P04-09_Examens_Paroi_thoracique_et_cotes_6-examens_production_XAi.json
- 2_Pratique/P04-09-PR_Examens_Paroi_thoracique_et_cotes_6-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Enquête OFSP 2018 sur l'exposition de la population suisse (Bize et al., version 1.4bis, 2020), tableaux 13 et 16, relue dans le PDF : thorax 0,045 mSv
- Proulx et Zryd, Am Fam Physician 2009;80:617-20 : syndrome de Tietze, jonction unique tuméfiée, surtout 2e et 3e côtes ; chondrite costale sur plusieurs jonctions, sans tuméfaction

Corrections faites :
- aucune

Remarques :
- Doses CT calculées sur la directive OFSP R-06-06 : calcul documenté en entrée à vérifier, conservé ; comparateur OFSP 2018 tableau 16 : CT du thorax 3,8 mSv.

## Seconde vérification des sources (23.11.2026 00:36, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Échographie : sensibilité 89,3 %, spécificité 98,4 % par rapport au CT | Ann Emerg Med 2022;79:529-539 (PubMed 35461720, résumé) | conforme |
| 2 | Scintigraphie : normalisation 79 % à 1 an, 93 % à 2 ans, 100 % à 3 ans | ACR, fractures de côtes 2018 (texte du document ACR) | conforme |
| 3 | Scintigraphie positive dans les 24 heures | ACR 2018 | conforme |
| 4 | Échographie : 13 minutes en moyenne | ACR 2018 (citant Hurley) | conforme |
| 5 | CT thoracique : environ 2,9 mSv à la valeur cible | OFSP R-06-06 rév. 2, protocole 6 (210 mGy·cm × 0,014) | conforme |
