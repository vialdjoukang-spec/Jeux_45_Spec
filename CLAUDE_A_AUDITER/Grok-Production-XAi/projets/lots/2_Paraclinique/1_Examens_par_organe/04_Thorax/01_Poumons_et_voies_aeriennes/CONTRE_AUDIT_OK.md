# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:58 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P04-01-BIO_Biologie_Poumons_et_voies_aeriennes_9-examens_production_XAi.json
- 1_Theorie/P04-01-END_Endoscopie_Poumons_et_voies_aeriennes_3-examens_production_XAi.json
- 1_Theorie/P04-01-FCT_Exploration_fonctionnelle_Poumons_et_voies_aeriennes_9-examens_production_XAi.json
- 1_Theorie/P04-01-HIS_Anatomopathologie_biopsie_Poumons_et_voies_aeriennes_4-examens_production_XAi.json
- 1_Theorie/P04-01-IMG_Imagerie_Poumons_et_voies_aeriennes_7-examens_production_XAi.json
- 2_Pratique/P04-01-BIO-PR_Biologie_Poumons_et_voies_aeriennes_9-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-01-END-PR_Endoscopie_Poumons_et_voies_aeriennes_3-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-01-FCT-PR_Exploration_fonctionnelle_Poumons_et_voies_aeriennes_9-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-01-HIS-PR_Anatomopathologie_biopsie_Poumons_et_voies_aeriennes_4-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P04-01-IMG-PR_Imagerie_Poumons_et_voies_aeriennes_7-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Enquête OFSP 2018 sur l'exposition de la population suisse (Bize et al., version 1.4bis, 2020), tableaux 13 et 16, relue dans le PDF : radiographie du thorax 0,045 mSv
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (smartermedicine.ch) : SSMI 2017, SSMIG 2014 et 2023, oncologie médicale 2024

Corrections faites :
- P04-01-HIS-PR — libellé > 45 car. : « Fibrose hétérogène avec foyers fibroblastiques » → « Fibrose hétérogène, foyers fibroblastiques »
- P04-01-IMG-PR — libellé > 45 car. : « Opacité alvéolaire systématisée avec bronchogramme aérien » → « Opacité systématisée avec bronchogramme »
- P04-01-IMG-PR — libellé > 45 car. : « Rayon de miel sous-pleural basal et bronchectasies de traction » → « Rayon de miel et bronchectasies de traction »
- P04-01-IMG-PR — libellé > 45 car. : « Défauts de perfusion segmentaires bien ventilés » → « Défauts perfusionnels segmentaires ventilés »
- P04-01-IMG — sigle absent du glossaire (C3) : « None » → « glossaire[TEP-CT]=Tomographie par émission de positons couplée au CT, synonyme de PET-CT. »

Remarques :
- Doses CT calculées sur la directive OFSP R-06-06 : calcul documenté en entrée à vérifier, conservé ; comparateur OFSP 2018 tableau 16 : CT du thorax 3,8 mSv.

## Seconde vérification des sources (23.11.2026 00:36, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Échographie : sensibilité d'environ 91 % pour le pneumothorax | Alrajhi et al., Chest 2012 (PubMed 21868468, résumé) | conforme (90,9 %) |
| 2 | Mortalité hospitalière après biopsie chirurgicale : 1,7 % programmée, 16 % non programmée | Hutchinson et al., Am J Respir Crit Care Med 2016 (PubMed 26646481, résumé) | conforme (1,7 % / 16,0 %) |
| 3 | IgE totales d'au moins 500 UI/ml parmi les critères de l'ABPA | ISHAM, Agarwal et al., Eur Respir J 2024 (PubMed 38423624, résumé) | conforme (≥ 500 IU/ml) |
| 4 | PaO2 inférieure à 8 kPa : hypoxémie cliniquement significative | BTS, O'Driscoll et al., Thorax 2008 (cité par des sources secondaires ; texte BTS non rouvert) | conforme, avec réserve sur l'accès au texte |
| 5 | Dépistage par CT basse dose : environ 20 % de mortalité par cancer du poumon en moins | Swiss Cancer Screening Committee, recommandation de novembre 2022 (site cancerscreeningcommittee.ch, extrait du rapport) | conforme (réduction relative de 20 %) |
