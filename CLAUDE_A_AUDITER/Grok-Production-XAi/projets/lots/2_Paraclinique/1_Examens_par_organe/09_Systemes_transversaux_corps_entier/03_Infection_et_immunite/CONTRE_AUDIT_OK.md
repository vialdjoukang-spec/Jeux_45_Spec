# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:10 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P09-03-BIO_Biologie_Infection_et_immunite_13-examens_production_XAi.json
- 1_Theorie/P09-03-FCT_Exploration_fonctionnelle_Infection_et_immunite_1-examens_production_XAi.json
- 2_Pratique/P09-03-BIO-PR_Biologie_Infection_et_immunite_13-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P09-03-FCT-PR_Exploration_fonctionnelle_Infection_et_immunite_1-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- EORTC/MSGERC 2020 (Donnelly et al.) : β-D-glucane ≥ 80 ng/l dans 2 sérums, critère de candidose invasive ou de pneumocystose probable, pas d'aspergillose
- Sepsis-3 ; ESID 2019 ; OMS 2022 (Sources sondées au contre-audit indépendant du 22.11 (lecture seule), corrections reprises ici)

Corrections faites :
- P09-03-BIO — correction du contre-audit 09-03 (texte relu) : « et un β-D-glucane ≥ 80 ng/l dans au moins 2 sérums consécutifs, constituent des critères mycologiques d'infection fongique invasive probable, selon les définitions EORTC/MSGERC (Donnelly et al., 2020). » → « constituent des critères mycologiques d'aspergillose probable, alors qu'un β-D-glucane ≥ 80 ng/l dans au moins 2 sérums consécutifs ne compte que pour une candidose invasive ou une pneumocystose probable, selon les défin »
- P09-03-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[ADN]=Acide désoxyribonucléique, support de l'information génétique. »
- P09-03-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[C2]=Deuxième fraction du complément, voie classique. »
- P09-03-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[C3]=Troisième fraction du complément, commune aux voies classique et alterne. »
- P09-03-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[C4]=Quatrième fraction du complément, voie classique. »
- P09-03-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[CH50]=Activité hémolytique totale de la voie classique du complément. »
- P09-03-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[VHA]=Virus de l'hépatite A. »
- P09-03-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[VHD]=Virus de l'hépatite D (delta). »
- P09-03-BIO — sigle absent du glossaire (C3) : « None » → « glossaire[VHE]=Virus de l'hépatite E. »
- P09-03-BIO-PR — sigle absent du glossaire (C3) : « None » → « glossaire[C2]=Deuxième fraction du complément, voie classique. »
- P09-03-BIO-PR — sigle absent du glossaire (C3) : « None » → « glossaire[C3]=Troisième fraction du complément, commune aux voies classique et alterne. »
- P09-03-BIO-PR — sigle absent du glossaire (C3) : « None » → « glossaire[C4]=Quatrième fraction du complément, voie classique. »
- P09-03-BIO-PR — sigle absent du glossaire (C3) : « None » → « glossaire[CH50]=Activité hémolytique totale de la voie classique du complément. »

## Seconde vérification des sources (23.11.2026 00:46, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Choc septique : lactate > 2 mmol/l sous vasopresseurs pour une PAM ≥ 65 mmHg | Sepsis-3, Singer et al. 2016 (PMC4968574) | conforme |
| 2 | Test VIH combiné : fenêtre de 6 semaines | directive suisse de dépistage du VIH 2025 (PDF virology.uzh.ch) | conforme |
| 3 | Tryptase pendant la réaction ou dans les 4 h, puis valeur de base | Valent et al. (formule 20 % + 2) | conforme |
| 4 | Parasitémie > 2 % chez le non-immun : critère de gravité | HUG, stratégie paludisme 2021 (PDF hug.ch) | conforme |
| 5 | Hémoglobine < 70 g/l : critère de gravité | HUG, stratégie paludisme 2021 | conforme |
