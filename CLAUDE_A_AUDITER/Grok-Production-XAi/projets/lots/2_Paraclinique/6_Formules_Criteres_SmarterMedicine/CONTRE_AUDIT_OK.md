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

## Complément P21 — contre-audit du 23.11.2026, 04:30 (heure de Zurich)
Verdict : conforme après correction. Le fichier contient maintenant 21 formules et 48 critères.

Existant : les 16 formules, les 28 critères, les métadonnées, les 13 entrées d'origine d'aVerifier et les clés de glossaire sont strictement identiques à la version contre-auditée de cette branche, comparés champ par champ. Le complément n'a fait qu'ajouter.

Ajouts revérifiés un par un dans la source relue :
- Formules : Cockcroft-Gault (Durden 2026, tableau 1 ; Di Gioia 2025) ; CKD-EPI 2021 (142, κ 0,7 et 0,9, α −0,241 et −0,302, exposant −1,200, 0,9938 puissance âge, 1,012 ; Durden 2026, Martey 2025, Sedoud 2026, concordants) ; Friedewald (diviseur 5 en mg/dl et 2,2 en mmol/l, limites 150, 200 et 400 mg/dl ; Arrobas Velilla 2023) ; HOMA-IR (/22,5 et /405 ; Moriyama 2025, Snouda 2026) ; APRI (formule et seuil OMS 2015 > 2 ; Mpisa 2026) ; Saravanan 2026 (seuils OMS 2024 « abaissés », sans chiffre).
- Critères : KDIGO 2012, définition et stades (PDF original) ; Duke-ISCVID 2023 (tableaux 1 et 2 originaux) ; McDonald 2017 (Rocca 2024, tableau 2) ; Rome IV (page de la Rome Foundation) ; TG18 cholécystite (Erinanc 2026, Morgan 2025 : 91,2 et 96,9 %) et cholangite (Hudgi 2022, tableau 1) ; Jones 2015 (Rwebembera 2026, Jeong 2024 : VS 60 et 30 mm, CRP 3,0 mg/dl) ; Kawasaki (Rădulescu 2025, Lupu 2025) ; ISSHP 2021 ; Fleischner 2017 (Masci 2026, tableau 2) ; CHA2DS2-VASc (APHRS 2026, tableau 3) ; Glasgow-Blatchford ; Alvarado (WSES 2020 : < 5, 99 %) ; sPESI ; 4T ; Ottawa ; Alberti 2009 (Williams 2024, Dutt 2025) ; GASA 1,1 g/dl (BSG 2021, tableau 1) ; Berlin (Yoon 2026, tableau 1).
- Conversions recalculées, toutes justes : 88,4 µmol/l par mg/dl de créatinine ; 0,0113 pour les triglycérides (1,7 / 2,3 / 4,5 mmol/l) ; 0,1333 kPa par mmHg (18,7/12 ; 17,3/11,3 ; 13,3-14,5 ; 12,0-13,2 ; 40 kPa) ; CRP 3,0 mg/dl = 30 mg/l ; 405 = 22,5 × 18 ; 26,5 µmol/l = 0,3 mg/dl.
- Toutes les références PubMed des sources secondaires correspondent aux textes enregistrés (auteurs et numéro).

Discordances tranchées par le rédacteur, revérifiées :
- Syncope du Glasgow-Blatchford à 2 points : confirmée (Orpen-Palmer 2023 et tableau 2 d'Alali et Barkun 2023). Elsabani 2024, qui imprime 1 point, n'est plus cité.
- Délai des 4T : le tableau 1 original de Lo et al. (2006), relu en texte intégral, dit « < 4 days without recent exposure ». Le texte dit maintenant « en moins de 4 jours ».
- Tour de taille d'Alberti « 94 cm ou plus » : choix gardé (tableau de Dutt 2025 adapté d'Alberti ; Williams 2024 imprime « > »). L'original n'a pas été lu.
- Plaquettes de l'ISSHP : le tableau 1 original de l'ISSHP 2021 (PDF isshp.org) dit « < 150,000/μL », comme Witkowski 2026. Le seuil est maintenant écrit : 150 G/l. Le « < 100 000 » d'Akankwasa 2026 est le seuil de l'ACOG.

Corrections (journal corrections.jsonl, tour t12 ; script audit/athena/t12/corr_t12.py) :
- 4T : la case 0 du délai devient « en moins de 4 jours », et Lo 2006 est cité dans la règle.
- Glasgow-Blatchford : l'urée « plus de 25 » devient « 25 ou plus », d'après le tableau 1 de Laursen et al. (2015), calculé selon l'article original. Une conversion kPa est mise en forme, et Elsabani est remplacé par Alali et Barkun.
- ISSHP 2021 : le seuil de plaquettes et la mention CIVD et hémolyse sont ajoutés. « Dysfonction utéro-placentaire isolée » devient « retard de croissance fœtal isolé » pour l'ACOG, ce que dit le tableau d'Akankwasa. L'original est cité.
- Duke-ISCVID 2023 : trois conditions omises sont rétablies (Coxiella isolée d'une seule hémoculture ; PET-CT au moins 3 mois après l'implantation d'une prothèse ; critère chirurgical seulement sans critère d'imagerie et sans confirmation histologique ou microbiologique).
- McDonald : la phrase sur la révision de 2024 est attribuée à Samara et Ontaneda (2025), qui est ajouté aux sources.
- Ottawa : les éléments étaient formulés comme une « capacité » au lieu de l'« incapacité » de faire quatre pas, et la règle de décision manquait. Les éléments, la zone des 6 cm distaux, la règle (douleur de la zone et l'un des éléments) et les exclusions sont réécrits d'après le guide des règles d'Ottawa des urgences du NHS écossais.
- Glossaire : CIVD et NHS sont ajoutés. aVerifier : 3 entrées du complément mises à jour et 1 entrée de traçabilité ajoutée.

Réserves :
- Plusieurs originaux restent non lus (Lancet, Chest, Circulation, Radiology, NEJM, JAMA). Les formules et critères viennent d'articles en libre accès qui les reproduisent, et l'attribution le dit.
- Jones 2015 : la fièvre n'est pas chiffrée. Les sources se contredisent (Rwebembera imprime > 38,5 et > 38,0 ; le CDC imprime ≥ 38,5 dans les deux populations).
- Le guide d'Ottawa du NHS écossais est un document de service, daté de 2012 et sans auteur nommé.
- Les seuils biologiques de la forme incomplète de Kawasaki, le seuil OMS 2024 de l'APRI et les grades TG18 restent non rédigés, comme le rédacteur l'a déclaré.
