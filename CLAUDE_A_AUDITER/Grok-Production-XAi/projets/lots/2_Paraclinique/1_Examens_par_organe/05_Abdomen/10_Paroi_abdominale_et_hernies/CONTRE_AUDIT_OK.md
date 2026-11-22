# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:05 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P05-10_Examens_Paroi_abdominale_et_hernies_4-examens_production_XAi.json
- 2_Pratique/P05-10-PR_Examens_Paroi_abdominale_et_hernies_4-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Directive OFSP R-06-06 (rév. 2, 2018), tableau 1, relue dans le PDF de l'OFSP : valeurs cibles abdomen-bassin 470, angio-CT abdomen-bassin 450, calculs rénaux 180, thorax-abdomen-bassin 610 mGy·cm
- WSES 2017 (Birindelli et al.) et HerniaSurge 2018 (Sondage de sources déjà fait au contre-audit indépendant du 22.11 (lecture seule), repris et complété ici)
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (radiologie 2020, angiologie 2024)

Corrections faites :
- P05-10-PR — libellé > 45 car. : « Sac herniaire graisseux qui franchit l'orifice inguinal profond » → « Sac graisseux franchissant l'orifice profond »
- P05-10-PR — libellé > 45 car. : « Paroi de l'anse herniée peu rehaussée, liquide dans le sac » → « Anse herniée peu rehaussée, liquide du sac »
- P05-10-PR — libellé > 45 car. : « Tuméfaction sous le ligament inguinal, en dedans de la veine fémorale » → « Masse sous-inguinale médiale à la veine »
