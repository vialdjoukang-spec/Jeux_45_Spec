# CONTRE_AUDIT_OK — 6_Formules_Criteres_SmarterMedicine

Contre-audit croisé interne terminé le 23.11.2026 03:33 (heure de Zurich).
Verdict : conforme après correction.

Fichiers couverts :
- P21_Formules_et_Criteres_diagnostiques_production_XAi.json (16 formules, 28 critères)
- P22_SmarterMedicine_recommandations_suisses_production_XAi.json (5 entrées de main inchangées + 64 recommandations)

## P21 — chaque formule et chaque critère revérifiés dans la source primaire relue
Formules (expression, coefficients, unités, bornes) : trou anionique (Kraut 2007) ; TA corrigé 0,25 par g/l (Figge 1998) ; TA urinaire (Batlle 1988) ; calcémie corrigée Ca − albumine + 4,0 en mg/100 ml et g/100 ml (Payne 1973), forme SI 0,025 × (40 − albumine) recalculée juste ; natrémie corrigée 2,4 par 100 mg/dl, 4,0 au-delà de 400 mg/dl (Hillier 1999) ; FIB-4 (âge × ASAT)/(plaquettes × √ALAT), 1,45 et 3,25 (Sterling 2006) ; MELD 9,57/3,78/11,2/6,43 et bornes (Kim 2021) ; MELD-Na − Na − 0,025 × MELD × (140 − Na) + 140, Na 125 à 140 (Kim 2008, texte intégral) ; MELD 3.0 tous coefficients, créatinine ≤ 3,0, Na 125 à 137, albumine 1,5 à 3,5 (Kim 2021, texte intégral) ; PaO2/FiO2 et classes de Berlin 2012 ; score z, LIN = −1,64 (Quanjer 2012) ; FENa (Espinel 1976) ; FEUN ≤ 35 %, 89 % contre 48 % (Carvounis 2002) ; GASA 96,7 % contre 55,6 % (Runyon 1992) ; Schwartz au lit 0,413 × taille/créatinine (Schwartz 2009) ; ASM/taille² < 7,0 et < 5,5 kg/m² (EWGSOP2 2019).
Critères (items, points, seuils) : Sepsis-3, choc septique, qSOFA (GCS ≤ 13, 75 %) ; Berlin ; CURB-65 ; Genève révisé (points 1/3/2/2/3/2/3-5/4 ; 8, 28, 74 %) ; Wells (3/3/1,5/1,5/1,5/1/1 ; 2,2 %) ; PERC (8 critères, 1,8 %, spécificité 15 et 27 %) ; Centor (56/32/15/6,5/2,5 %) ; règle canadienne CT tête ; règle canadienne rachis (100 %, 42,5 %) ; NEXUS (99,0/99,8/12,9 %) ; PECARN (100 % ; 99,95 et 96,8 %) ; Ottawa HSA (100 %, 15,3 %) ; ABCD2 (8,1/4,1/1,0 %) ; HEART (2,5/20,3/72,7 %) ; BISAP ; Atlanta révisée ; ACR/EULAR 2022 ACG (5/3/3/2… ; ≥ 6 ; 87,0 et 94,8 %) ; ACR/EULAR 2010 PR (≥ 6/10) ; EULAR/ACR 2019 lupus ; IADPSG (5,1/10,0/8,5 mmol/l) ; EWGSOP2 (27/16 kg, 15 s, 20/15 kg, 0,8 m/s, SPPB ≤ 8, TUG ≥ 20 s, 400 m ≥ 6 min) ; CAM ; syndrome métabolique ; hyponatrémie < 135 mmol/l ; Light (0,5 / 0,6 / deux tiers).
Conversions non imprimées dans les sources (kPa, urée BISAP, glucose, calcémie SI, créatinine) : toutes recalculées, justes, déclarées dans _lot.aVerifier.

Corrections faites (journal corrections.jsonl, tour t10) :
- CURB-65 : « 3 % pour 2 » → « 13 % pour 2 ». Le résumé PubMed de Lim 2003 porte une coquille (valeur inférieure au score 1). 13 % relu dans le tableau 3 de la Saudi Thoracic Society 2025 (PMC12609742), qui reprend Lim 2003.
- Règle canadienne du CT cérébral : « plus de deux vomissements » → « deux vomissements ou plus » ; « âge supérieur à 65 ans » → « 65 ans ou plus » ; « amnésie de plus de 30 minutes » → « 30 minutes ou plus » ; « fracture ouverte » → « fracture ouverte ou embarrure ». Source : tableau 1 de Mata-Mbemba 2016 (PMC4766169), confirmé par Javeed 2024 (PMC11618677).
- Lupus EULAR/ACR 2019 : ajout de la condition « au moins un critère clinique », relue dans Scopes et Md Yusof 2025 (PMC12546666) et Netti 2026 (PMC13409482).
- MELD 3.0 : ajout des bornes Na 125 à 137 mmol/l et albumine 1,5 à 3,5 g/dl (Kim 2021).
- MELD : bornes réécrites mot pour mot (< 1,0 → 1,0 ; créatinine 4,0 après au moins deux dialyses dans la semaine), attribuées à Kim 2021 (et non à Kim 2008).
- Berlin (formule et critère) : bornes précisées (> 200 et ≤ 300 ; > 100 et ≤ 200).
- FIB-4 : phrase tronquée « VIH et le. » → « VIH et le VHC. » ; ajout de la VPN de 90 % et de la sensibilité de 70 % sous 1,45.
- Schwartz : titre tronqué complété (« … children with CKD »).
- Rachis cervical canadien : « absence de douleur médiane » → « absence de sensibilité cervicale médiane à la palpation ».
- _lot.aVerifier : 3 entrées ajoutées (conversions calculées, traçabilité CURB-65, traçabilité CT tête).

## P22 — Smarter Medicine
- `sm --verifier` : 64/64 recommandations mot pour mot.
- Sondage de 15 citations sur smartermedicine.ch, pages lues en ligne le 23.11.2026 : anesthésiologie 2018 n° 3 ; chirurgie 2018 n° 2 ; gastroentérologie 2017 n° 2 ; gynécologie et obstétrique 2022 n° 2 ; infectiologie 2020 n° 2 ; MIG ambulatoire 2014 n° 1 ; MIG ambulatoire 2021 n° 1 ; radiologie 2020 n° 1, 3, 4 et 5 ; céphalées 2026 n° 1 et 2 ; pédiatrie 2024 n° 1 ; endocrinologie et diabétologie 2025 n° 1. Résultat : 15/15 retrouvées mot pour mot, avec la liste et l'année inscrites dans l'en-tête de la page. Un seul écart : l'outil numérote n° 3 le kyste annexiel, qui est le n° 4 sur le site. Le fichier ne cite pas de numéro.
- Les 5 entrées préremplies de main sont inchangées (identité vérifiée). Elles ne sont pas mot pour mot ; le rédacteur l'a déclaré et a proposé les remplacements exacts dans aVerifier. Décision laissée à l'audit externe.
- Aucune correction.

## Réserves
- 16 formules sur ≈ 40 et 28 critères sur ≈ 80. Le reste a été cherché sans être trouvé ; le rédacteur l'a déclaré.
- Les seuils du syndrome métabolique (Alberti 2009) et le seuil du GASA (1,1 g/dl) ne sont pas repris. Les conditions de délai, d'opacités et de PEP de Berlin non plus.
- Les critères de Light ont été relus dans Yang 2025 et non dans l'article original.
- Wells : « absence de diagnostic alternatif » est gardé comme dans le résumé relu.
- Le texte intégral de Lim 2003 et celui de Stiell 2001 n'ont pas pu être téléchargés.
