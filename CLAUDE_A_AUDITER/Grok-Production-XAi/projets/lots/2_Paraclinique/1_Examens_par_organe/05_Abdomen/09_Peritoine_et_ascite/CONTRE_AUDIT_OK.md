# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:05 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P05-09_Examens_Peritoine_et_ascite_5-examens_production_XAi.json
- 2_Pratique/P05-09-PR_Examens_Peritoine_et_ascite_5-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Directive OFSP R-06-06 (rév. 2, 2018), tableau 1, relue dans le PDF de l'OFSP : valeurs cibles abdomen-bassin 470, angio-CT abdomen-bassin 450, calculs rénaux 180, thorax-abdomen-bassin 610 mGy·cm
- BSG 2021 (Aithal et al.) et EASL 2018 : seuils relus (Sondage de sources déjà fait au contre-audit indépendant du 22.11 (lecture seule), repris et complété ici)

Corrections faites :
- P05-09 — orthographe (contre-audit 05-09) : « recessus de Morison » → « récessus de Morison »
- P05-09-PR — orthographe (contre-audit 05-09) : « Un abcès péri-colique » → « Un abcès péricolique »

## Seconde vérification des sources (23.11.2026 00:40, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Rendement de la cytologie de 0 % à 96,7 % selon le siège | BSG, Aithal et al., Gut 2021 (PubMed 33067334 ; texte BSG) | conforme |
| 2 | SAAG inférieur à 11 g/l : maladie péritonéale | AASLD, Biggins et al., Hepatology 2021 (SAAG < 1,1 g/dl) | conforme |
| 3 | Échographie : seuil de détection d'environ 200 ml | EFSUMB, Course Book 2e éd., chapitre E-FAST (efsumb.org) | conforme |
| 4 | CT abdomen-bassin : 470 mGy·cm, 7,1 mSv | OFSP R-06-06 rév. 2, protocole 8 (PDF du 23.11.2026) | conforme (470 × 0,015 = 7,05) |
| 5 | Stratégie conditionnelle (CT après échographie négative) : 6 % de situations urgentes manquées | WSES 2021, parcours des infections intra-abdominales (World J Emerg Surg, citant Lameris et al., BMJ 2009) | conforme |
