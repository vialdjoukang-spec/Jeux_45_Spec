# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:10 (heure de Zurich).
Verdict : conforme, sans correction

Fichiers contrôlés :
- 1_Theorie/P09-05_Examens_Genetique_5-examens_production_XAi.json
- 2_Pratique/P09-05-PR_Examens_Genetique_5-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Miller et al., Am J Hum Genet 2010 (PubMed 20466091) : rendement de la puce à ADN 15 à 20 %, contre environ 3 % pour le caryotype

Corrections faites :
- aucune

Remarques :
- Résolution des sondes FISH (100 kb, Miller 2010) : texte intégral non accessible pendant le contre-audit, non relu.

## Seconde vérification des sources (23.11.2026 00:46, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 1 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Puce à ADN : cause trouvée chez 15 à 20 % | Miller et al., Am J Hum Genet 2010 (PMC2869000) | conforme |
| 2 | Caryotype : environ 3 % hors trisomie 21 | Miller et al. 2010 | conforme |
| 3 | Caryotype : manque souvent les déséquilibres de 5 à 10 Mb | Miller et al. 2010 | conforme |
| 4 | Exome ou génome : rendement de 28 à 68 % | Malinowski et al. 2020 (cité par des revues) | conforme, avec réserve sur l'accès au texte |
| 5 | Plus de 99 % des variations bénignes sont héritées | non trouvé chez Miller et al. ; trouvé dans un guide ACPA 2025 | non trouvé (source nommée) : ajouté à _lot.aVerifier |
