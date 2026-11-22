# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:58 (heure de Zurich).
Verdict : conforme, sans correction

Fichiers contrôlés :
- 1_Theorie/P04-04_Examens_Diaphragme_et_muscles_respiratoires_6-examens_production_XAi.json
- 2_Pratique/P04-04-PR_Examens_Diaphragme_et_muscles_respiratoires_6-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Boussuges et al., Chest 2009 (PubMed 19017880) : limites inférieures 0,9 cm (femmes) et 1 cm (hommes) en respiration calme, 1,6 et 1,8 cm au reniflement
- Gibson, Thorax 1989 : mouvement paradoxal unilatéral au reniflement chez 6 % des sujets sains (série d'Alexander, 776 sujets)

Corrections faites :
- aucune

Remarques :
- Seuil de 20 % de Gottesman et McCool (1997) : article original non relu, maintenu en entrée à vérifier.

## Seconde vérification des sources (23.11.2026 00:36, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 1 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Latence du nerf phrénique > 8,0 ms : atteinte démyélinisante | Resman-Gašperšč et Podnar, Muscle Nerve 2008;37:36-41 (PubMed 17763457 ; mise en ligne 2007) | conforme (limite supérieure 8,0 ms) |
| 2 | Excursion : limites 1,0/0,9 cm au calme, 1,8/1,6 cm au reniflement | Boussuges et al., Chest 2009 (PubMed 19017880, résumé) | conforme |
| 3 | PImax ≥ 80/70 cmH2O, SNIP ≥ 70/60 cmH2O écartent une faiblesse | ERS, Laveneziana et al. 2019 (texte, figure 2) | conforme |
| 4 | Radioscopie du diaphragme : dose pouvant dépasser 0,3 mSv | FitzMaurice et al., ERJ Open Res 2022 (texte intégral PMC8862633 : « upwards of 0.3 mSv ») | conforme |
| 5 | Baisse de la CV couchée > 25 % (Se 79 %, Sp 90 %) « selon l'ERS 2019 » | ERS 2019 §1.4.1 (15 % = limite de la normale ; ≥ 30 % si faiblesse bilatérale sévère) ; Fromageot et al., Arch Phys Med Rehabil 2001 (PubMed 11239298 : > 25 %, Se 79 %, Sp 90 %) | ERREUR D'ATTRIBUTION corrigée (3 textes + 2 sources) |
