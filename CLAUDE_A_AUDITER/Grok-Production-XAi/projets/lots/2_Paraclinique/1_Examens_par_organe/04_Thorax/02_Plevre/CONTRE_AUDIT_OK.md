# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:58 (heure de Zurich).
Verdict : conforme, sans correction

Fichiers contrôlés :
- 1_Theorie/P04-02_Examens_Plevre_7-examens_production_XAi.json
- 2_Pratique/P04-02-PR_Examens_Plevre_7-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- ERS/ESTS/EACTS/ESTRO, Opitz et al. 2020 : sensibilité de la thoracoscopie médicale 92 % (1369 patients, 22 séries) ; PET-CT sensibilité 38 % pour N1 et 67 % pour T4
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (smartermedicine.ch)

Corrections faites :
- aucune

Remarques :
- Doses CT calculées sur la directive OFSP R-06-06 : calcul documenté en entrée à vérifier, conservé ; comparateur OFSP 2018 tableau 16 : CT du thorax 3,8 mSv.

## Seconde vérification des sources (23.11.2026 00:36, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | pH pleural de 7,2 ou moins : drainage | BTS, Roberts et al., Thorax 2023 (texte intégral, thorax.bmj.com) | conforme (« pH ≤ 7,2 … ICD should be inserted ») |
| 2 | Épaississement pleural de plus de 1 cm : malignité | BTS 2023 (texte intégral) | conforme (épaississement circonférentiel > 1 cm, nodularité, face médiastinale) |
| 3 | Thoracoscopie médicale : sensibilité d'environ 92 % | Opitz et al., ERS/ESTS/EACTS/ESTRO 2020 (texte intégral, dépôt ULB) | conforme |
| 4 | Thoracoscopie : mortalité 0,34 %, complications majeures 1,8 %, 47 études | Opitz et al. 2020 (texte intégral : « 47 studies including 4756 patients … 0.34% … 1.8% ») | conforme |
| 5 | Radiographie couchée : sensibilité d'environ 50 % pour le pneumothorax | Alrajhi et al., Chest 2012 (résumé) | conforme (50,2 %) |
