# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:05 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P05-11_Examens_Aorte_abdominale_et_vaisseaux_diges_6-examens_production_XAi.json
- 2_Pratique/P05-11-PR_Examens_Aorte_abdominale_et_vaisseaux_diges_6-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Directive OFSP R-06-06 (rév. 2, 2018), tableau 1, relue dans le PDF de l'OFSP : valeurs cibles abdomen-bassin 470, angio-CT abdomen-bassin 450, calculs rénaux 180, thorax-abdomen-bassin 610 mGy·cm
- ESVS 2024 (anévrismes) et ESVS 2025 (artères mésentériques et rénales) ; HPA-CRCE-012, angiographie mésentérique (Sondage de sources déjà fait au contre-audit indépendant du 22.11 (lecture seule), repris et complété ici)
- Citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses publiées (radiologie 2020, angiologie 2024)

Corrections faites :
- P05-11-PR — libellé > 45 car. : « Défect endoluminal arrondi à quelques centimètres de l'ostium » → « Défect endoluminal arrondi près de l'ostium »
- P05-11-PR — libellé > 45 car. : « Accélération focale avec rapport rénal/aortique élevé » → « Accélération focale et rapport rénal élevé »
- P05-11-PR — libellé > 45 car. : « Succession de sténoses et de dilatations dans le tiers moyen » → « Sténoses et dilatations du tiers moyen »
- P05-11-PR — libellé > 45 car. : « Spasme diffus des branches, aspect en chapelet » → « Spasme diffus des branches en chapelet »
