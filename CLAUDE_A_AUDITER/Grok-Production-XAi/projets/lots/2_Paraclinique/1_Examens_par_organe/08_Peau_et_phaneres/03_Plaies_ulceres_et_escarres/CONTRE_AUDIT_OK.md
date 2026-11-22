# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:10 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P08-03_Examens_Plaies_ulceres_et_escarres_7-examens_production_XAi.json
- 2_Pratique/P08-03-PR_Examens_Plaies_ulceres_et_escarres_7-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- ESUR Guidelines on Contrast Agents v10 (PDF esur.org) : chélates macrocycliques (groupe II) avec prudence si DFG < 30 ml/min, contrôle de l'eGFR non obligatoire, grossesse seulement pour une information diagnostique essentielle, plus petite dose
- Liste Top 5 de la Société suisse d'angiologie (2024) : la recommandation 2 vise la MAOP, d'où le retrait
- Sources sondées au contre-audit indépendant du 22.11 (lecture seule), corrections reprises ici

Corrections faites :
- P08-03 — correction du contre-audit 08-03 (texte relu) : « On contrôle la fonction rénale avant le gadolinium et, pendant la grossesse, on ne l'injecte que s'il est indispensable, selon les recommandations de l'ESUR sur les produits de contraste (version 10, 2018). » → « On choisit un chélate macrocyclique, avec prudence si le DFG est inférieur à 30 ml/min/1,73 m², et, pendant la grossesse, on ne l'injecte que si l'IRM injectée est indispensable, à la plus faible dose, selon les recomman »
- P08-03 — Q4 : recommandation SSA hors sujet (vise la MAOP, pas l'ostéomyélite) ; champ autorisé laissé vide : « « Pas de diagnostic par CT-scan ou IRM pour clarifier une maladie artérielle occlusive périphérique (MAOP) », selon Smarter Medicine, liste Top 5 de la Société suisse d'angiologie (SSA, 2024). » → « None »
- P08-03 — entrée levée : champ laissé vide (recommandation hors sujet) : « conception/donnees/paraclinique/topographie/8_peau_et_phaneres/plaies_ulceres_et_escarres.json › plaies_ulceres_et_escarres__irm › smarterMedicine : la recommandation n° 2 de la SSA (2024) vise le diagnostic d'une artéri » → « None »
- P08-03 — entrée levée : précaution réécrite d'après l'ESUR v10, relue (PDF esur.org) : « conception/donnees/paraclinique/topographie/8_peau_et_phaneres/plaies_ulceres_et_escarres.json › plaies_ulceres_et_escarres__irm › precautions : consignes de l'ESUR (version 10, 2018) sur le gadolinium rappelées de mémoi » → « None »
- P08-03 — sigle absent du glossaire (C3) : « None » → « glossaire[DFG]=Débit de filtration glomérulaire, estimé à partir de la créatinine, en ml/min/1,73 m². »
- P08-03 — libellé > 45 car. : « Artériopathie oblitérante des membres inférieurs » → « Artériopathie des membres inférieurs »

## Seconde vérification des sources (23.11.2026 00:46, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Néoplasie dans 2 % à 10 % des ulcères de jambe | DGPL, Valesky et al. 2024, S2k (texte AWMF/JDDG) | conforme |
| 2 | Biopsie d'un ulcère sans tendance à guérir après 6 semaines | DGPL, Valesky et al. 2024 | conforme |
| 3 | Score de Braden de 10 à 12 : risque élevé | échelle de Braden (formulaire de 1988) | conforme |
| 4 | IPS de 0,9 à 1,3, index orteil-bras ≥ 0,70, ondes triphasiques ou biphasiques : artériopathie peu probable | IWGDF/ESVS/SVS 2023 (iwgdfguidelines.org) | conforme |
| 5 | HbA1c ≥ 6,5 % ou glycémie à jeun ≥ 7,0 mmol/l : diabète | ADA, Standards of Care | conforme |
