# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:05 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P05-13_Examens_Veines_caves_et_systeme_porte_8-examens_production_XAi.json
- 2_Pratique/P05-13-PR_Examens_Veines_caves_et_systeme_porte_8-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Directive OFSP R-06-06 (rév. 2, 2018), tableau 1, relue dans le PDF de l'OFSP : valeurs cibles abdomen-bassin 470, angio-CT abdomen-bassin 450, calculs rénaux 180, thorax-abdomen-bassin 610 mGy·cm
- Rapport HPA-CRCE-012 (Hart et al., 2010), annexe, relu dans le PDF : pyélographie rétrograde E103 1,58 mSv (bilatérale 3,09) ; cavographie inférieure 1,33 mSv

Corrections faites :
- P05-13-PR — libellé > 45 car. : « Matériel échogène sans flux dans le tronc porte » → « Matériel échogène sans flux dans la porte »
- P05-13-PR — libellé > 45 car. : « Thrombus hyperdense spontané, lumière non rehaussée » → « Thrombus hyperdense, lumière non rehaussée »
- P05-13-PR — libellé > 45 car. : « Collatérales intrahépatiques en toile d'araignée » → « Collatérales hépatiques en toile d'araignée »
- P05-13-PR — libellé > 45 car. : « Différence entre pression bloquée et pression libre » → « Écart pression bloquée - pression libre »
- P05-13-PR — libellé > 45 car. : « Grandes varices œsophagiennes avec signes rouges » → « Grosses varices œsophagiennes, signes rouges »

Remarques :
- Dose du gradient porte (5,4 mSv, Hari et al. 2017) : calcul documenté en entrée à vérifier, conservé.
