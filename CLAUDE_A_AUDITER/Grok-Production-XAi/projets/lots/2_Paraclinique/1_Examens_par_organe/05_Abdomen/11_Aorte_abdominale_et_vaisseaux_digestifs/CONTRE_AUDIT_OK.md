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

## Seconde vérification des sources (23.11.2026 00:40, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Dépistage unique chez l'homme de 65 à 75 ans fumeur ou ancien fumeur (grade B) | EviPrev 2021 (tableau des recommandations, eviprev.ch) | conforme |
| 2 | Femmes fumeuses de 65 à 75 ans : données insuffisantes | EviPrev 2021 | conforme |
| 3 | Anévrisme : diamètre d'au moins 30 mm | ESVS 2024 (Eur J Vasc Endovasc Surg) | conforme |
| 4 | Surveillance annuelle de 40 à 49 mm chez l'homme | ESVS 2024 | conforme |
| 5 | Angio-CT abdominal : 450 mGy·cm, 6,75 mSv | OFSP R-06-06 rév. 2, protocole 11 (angiographie CT abdomen-bassin) | conforme |
