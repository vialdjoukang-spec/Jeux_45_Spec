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
