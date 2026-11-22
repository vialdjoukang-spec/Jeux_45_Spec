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
