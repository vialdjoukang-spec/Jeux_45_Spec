# Audit V3 groupe B — journal (pathologies produites par l'API, ordre du rang de rendement)

Légende : 🟩 juste (réserves notées) · 🟧 corrigé ou à vérifier · 🟥 rejeté (reste hors de main).
Méthode : contrôle mécanique de chaque pathologie (JSON, CNP/CPCM, PEP VIH, menus longs 1–3 justes, « why » de chaque option, diagnostic masqué des niveaux 4–5), puis relecture médicale des notions, des réponses justes et des posologies ; sources primaires lues en ligne lorsque citées « Vérifié » (AIPS compendium.ch, PubMed, OFSP/CFIST). Les points non relus portent « à vérifier » dans `audit.claude.aVerifier`.
Contrôle transversal PEP VIH : la CFIST (recommandations du 7.11.2025, expositions professionnelles et non professionnelles, bag.admin.ch) fixe la limite à 48 h (début visé dans les 4 h, durée 4 semaines). Cinq pathologies du groupe B portent encore « 72 h » : Z11.3__O6_5-E04, B20_primo_infection_vih___O7_12-E13, T14.9__O6_4-E12, T74.2_2__O2_3-E04, A60.0__S3_5-E16 (à corriger lors de leur lot).

## Lot 1 — rangs 505 à 514

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| L29.0__S3_5-E03 | 🟧 | Corrigé : exemption de franchise du dépistage colorectal limitée aux programmes cantonaux ; Q14 (d4 qui nomme le diagnostic) passée en d3. Vérifié : mébendazole 100 mg dose unique répétée à 2 semaines (AIPS Vermox), hydroxyzine 25 mg le soir (AIPS Atarax), capsaïcine 0,006 % (Lysy, Gut 2003, PMID 12912865). À vérifier : OPAS 12e, café décaféiné, prévalence et ratio H/F. |
| L30.5__S6_3-E08 | 🟩 | Forme : cellule de tableau mal enveloppée (schéma) corrigée. Aucune erreur médicale retenue. Vérifié : critère ≥ 3 macules hypomélaniques ≥ 5 mm (consensus international sclérose tubéreuse 2012). À vérifier : prévalence 5 % et pic 3–16 ans. |
| L50.0_1__S1_21-E03 | 🟧 | Corrigé : deux « why » qui faisaient de 3 jours un maximum de corticothérapie (EAACI 2022 : cure courte). Vérifié : prévalence vie entière ≈ 20 % (EAACI/GA²LEN 2022, PMID 34536239) ; bilastine 20 mg à jeun, adrénaline IM 0,01 mg/kg max 0,5 mg. À vérifier : durée de cure, fenêtre de la tryptase. |
| L50.0__G9-E03 | 🟧 | Notions et correction justes ; questions absentes (à produire). Vérifié : définitions < 6 semaines, prévalence ≈ 20 % (EAACI/GA²LEN 2022, PMID 34536239). À vérifier : fenêtre de la tryptase. |
| L50.9__S6_9-E01 | 🟩 | Aucune erreur retenue : omalizumab 300 mg/4 sem., ciclosporine ≤ 5 mg/kg/j, UAS7 (0 ; 1–6 ; 7–15 ; 16–27 ; 28–42), UCT ≥ 12, corticoïde ≤ 10 jours concordent avec EAACI/GA²LEN 2022. À vérifier : tryptase. |
| L60.0__S6_8-E02 | 🟩 | Aucune erreur retenue ; rappels dT 25/45/65 ans conformes au plan suisse. À vérifier : adrénaline au bloc digital, taux de guérison. |
| L64.9__S6_6-E01 | 🟩 | Aucune erreur retenue : finastéride 1 mg/j et PSA à doubler, DHEAS > 700 µg/dL, spironolactone 100–200 mg/j hors indication. À vérifier : seuil de testostérone (harmoniser avec L68.0), forme féminine du minoxidil (AIPS). |
| L65.0__S6_6-E02 | 🟩 | Aucune erreur retenue (pull test > 10 %, délai 2–4 mois, forme chronique > 6 mois). À vérifier : ferritine cible. |
| L68.0__S6_6-E04 | 🟧 | Corrigé : Q17 (Kprim d4 non masqué) passée en d3. Vérifié contre les seuils Endocrine Society 2018 / PCOS 2023 : DHEAS 19 µmol/L, 17-OHP > 6 nmol/L, ≥ 20 follicules ou ≥ 10 mL, pas d'échographie < 8 ans après la ménarche. À vérifier : seuil de testostérone. |
| L71.8__G7-E02 | 🟩 | Aucune erreur retenue (ROSCO 2017, brimonidine 0,33 %, ivermectine 1 % arrêt à 3 mois, 5-HIAA, tryptase > 20 ng/mL). À vérifier : AIPS non relues. |

Contrôles lot 1 : `controle_menus_longs.py DER` → 0 menu fautif (12 erreurs `valider()` restantes sur des pathologies DER non encore auditées). Réparations de forme hors lot (JSON imbriqué en chaîne, virgules finales, `.slice(0,1)`) : priseEnCharge de Z50.1__O7_14-E01, O26.8__O1_4-E01, R60.9__G12-E03 ; notions de N89.8__S4_18-E03 et Z80.9__O4_7-E03. La construction de l'arène échoue encore sur la branche de veille à cause de 18 corrections du groupe B dont un champ (`ssp` ou `notions`) est une chaîne JSON invalide qui avale les clés suivantes (M17.9__G10-E03, Z30.0__S4_8-E01, O92.1__O1_6-E02, M85.8__F2_20-E02, R49.0_1__S7_4-E03, Z56.6__O6_4-E03, O99.1__F2_25-E03, O36.8__O2_7-E02, E16.2_1__S9_9-E13, D55.0__F2_16-E17, A60.0__S3_5-E16, R20.2__S7_9-E05, R68.3__F1_4-E04, Z63.6__O3_6-E12, R06.4__O7_8-E05, R23.1__F1_17-E03, H34.1__S1_2-E11, G10__O7_25-E06) : à régénérer ou à réparer à la main (🟥 tant qu'elles restent mal formées). Les contrôles d'arène (construction + test sans écran) se font donc sur la branche de portage vers main.

## Lot 2 — rangs 515 à 524

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| L71.9__S6_9-E03 | 🟩 | Aucune erreur retenue. Vérifié : doxycycline 40 mg/j (Oracea, AIPS : rosacée papulo-pustuleuse dès 18 ans, à jeun). À vérifier : AIPS des topiques. |
| L72.0__G2-E03 | 🟩 | Forme : clé « false_placeholder » hors schéma retirée (Q17). Aucune erreur retenue (drainage sans exérèse en phase aiguë, exérèse à froid, Gardner/APC). |
| L74.5__G1-E01 | 🟧 | Corrigé : Q17 (d4 qui nomme l'entité) passée en d3. Vérifié : Botox autorisé en Suisse pour l'hyperhidrose axillaire primaire > 18 ans (AIPS). Critères de Hornberger (≥ 6 mois, ≥ 2/6) conformes. À vérifier : dose de 50 U, seuil gravimétrique. |
| L80__S6_3-E01 | 🟧 | Corrigé : Q20 (d4 qui nomme le diagnostic) passée en d3. Aucune erreur médicale retenue (UVB-TL01 311 nm, TSH à tous les adultes, TRuE-V ≈ 30 % F-VASI75 à 24 semaines). À vérifier : statut suisse du ruxolitinib et du tacrolimus. |
| L81.0__S6_3-E04 | 🟩 | Forme : clé vide « mesuresGénérales » hors schéma retirée. Aucune erreur retenue (excision diagnostique à 2 mm, acide azélaïque en grossesse). À vérifier : statut de l'hydroquinone. |
| L81.1__S6_3-E03 | 🟧 | Corrigé : Q13 (d4 qui nomme le diagnostic) passée en d3. Aucune erreur médicale retenue (trithérapie de Kligman, écran teinté aux oxydes de fer). À vérifier : acide tranexamique, statut de l'hydroquinone. |
| L85.3__G9-E02 | 🟩 | Aucune erreur retenue (urée 5–10 %, bilan du prurit chronique > 6 semaines, mise en garde PRISCUS). |
| L89.0__O3_5-E01 | 🟧 | Corrigé : Q20 (menu long d4 dont l'énoncé nomme le stade en négatif) passée en d3. Seuils conformes à EPUAP/NPIAP/PPPIA 2019 : Braden ≤ 18, Norton ≤ 14, 30–35 kcal/kg/j et 1,25–1,5 g/kg/j de protéines. |
| L89.1__O3_5-E02 | 🟩 | Aucune erreur retenue (catégorie 2 sans fibrine, NaCl 0,9 %, milieu humide, apports EPUAP 2019). |
| L89.9__S6_4-E04 | 🟩 | Aucune erreur retenue (catégories NPIAP/EPUAP 2019, Braden ≤ 18, probe-to-bone). |

Contrôles lot 2 : `controle_menus_longs.py` DER et CPL → 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage.

## Lot 3 — rangs 525 à 534

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| M05.9__S5_3-E02 | 🟩 | Aucune erreur retenue (ACR/EULAR 2010 ≥ 6/10, DAS28 < 2,6 / > 5,1, SDAI ≤ 3,3, CDAI ≤ 2,8, facteur 1,5 du risque CV, prudence anti-JAK). À vérifier : AIPS du méthotrexate. |
| M10.0__S5_6-E02 | 🟧 | Forme : bloc c9 ramené à 5 points (fusion de deux points de suivi). Corrigé : Q13 (menu long d4 dont la vignette livre les cristaux d'urate) passée en d3. Aucune erreur médicale retenue (cibles < 360 / < 300 µmol/L, prednisone 30–35 mg 3–5 j, allopurinol 100 mg/j titré, HLA-B*58:01). À vérifier : AIPS de la colchicine, seuil d'hyperuricémie. |
| M15.1__S5_3-E01 | 🟧 | Corrigé : Q19 (menu long d4 qui nomme l'arthrose digitale) passée en d3. Aucune erreur médicale retenue (EULAR 2018 : AINS topiques en premier, orthèse de rhizarthrose). |
| M16.1__S7_2-E01 | 🟩 | Forme : clé « si » hors schéma retirée (Q08). Aucune erreur médicale retenue (critères NICE ≥ 45 ans, critères de Kocher, thromboprophylaxie 35 j après PTH, céfazoline préopératoire). |
| M17.0__S5_6-E01 | 🟩 | Aucune erreur retenue (liquide mécanique < 2000/mm³, AINS topiques en premier, perte de poids ≥ 5 %). |
| M17.9__G10-E03 | 🟧 | Corrigé (forme) : la correction était mal formée (« ssp » réduit à « G10 », « notions » en chaîne avalant ssp et priseEnCharge) ; structure reconstruite sans changer le texte ; clé « false » hors schéma retirée (Q16). Aucune erreur médicale retenue dans les notions relues. |
| M19.9__F2_4-E03 | 🟩 | Aucune erreur retenue (prévalence radiologique > 50 % après 65 ans, critères cliniques NICE, AINS topiques, perte de poids 5–10 %). |
| M20.1__S5_3-E03 | 🟧 | Corrigé : Q14 (d4 qui nomme le hallux valgus) passée en d3. Aucune erreur médicale retenue (IPS < 0,9 / > 1,3 et pression d'orteil, monofilament 10 g, IWGDF 2023). |
| M40.2__S5_1-E04 | 🟧 | Corrigé : Q03, Q04 et Q20 (d4, vignettes sans le nom de l'entité) marquées « diagnostic masqué ». Aucune erreur médicale retenue (Genant, calcium 1000 mg + vitamine D 800 UI, contre-indication du romosozumab après infarctus/AVC). À vérifier : AIPS, seuils FRAX. |
| M41.5__S5_1-E02 | 🟩 | Aucune erreur retenue (Cobb ≥ 10° avec rotation pour la scoliose vraie, test d'Adams, cales, justification radioprotection). |

Contrôles lot 3 : `controle_menus_longs.py` ORT et RHU → 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage.

## Lot 4 — rangs 535 à 544

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| M47.8_1__S5_2-E03 | 🟧 | Corrigé : Q20 (d4 qui nomme l'entité) passée en d3. Aucune erreur médicale retenue (branches médianes de deux niveaux, critères de Revel, Smarter Medicine 6 semaines). |
| M47.8__S1_16-E02 | 🟧 | Forme : Q03 portait 7 notions (maximum 6) ; N18, couverte par deux autres questions, retirée de Q03. Aucune erreur médicale retenue (Spurling spécifique, IRM si myélopathie ou échec à 6 semaines, mise en garde des infiltrations transforaminales). |
| M53.8__S5_1-E10 | 🟩 | Aucune erreur retenue (Scheuermann ≥ 5° sur 3 vertèbres, OLT 3, 150 min/sem.). |
| M54.1_1__S7_9-E03 | 🟩 | Aucune erreur retenue. Chiffres concordants avec les sources citées : incidence 83/100 000 et pic 50–54 ans (Radhakrishnan 1994), Lasègue 91 %/26 % et croisé 29 %/88 % (Devillé 2000), Brinjikji 2015, détection précoce AI dès 30 jours. |
| M54.2__S1_16-E01 | 🟩 | Aucune erreur retenue (Canadian C-spine rule, PPR > 45 min, paracétamol ≤ 4 g/j, ibuprofène 400 mg ×3). |
| M54.5_2__O7_2-E02 | 🟧 | Corrigé : Q10 (d4 dont la vignette nomme l'incapacité pour lombalgie, refus de `valider()`) passée en d3 non masquée. Vérifié dans le droit cité : LAI art. 28 (incapacité moyenne ≥ 40 % pendant un an), détection précoce dès 30 jours, CO art. 336c (30/90/180 jours). |
| M54.5_3__O7_21-E02 | 🟧 | Corrigé : Q10 (d4 qui nomme l'acupuncture) passée en d3. Aucune erreur médicale retenue (seuil de pertinence −30 %, IMMPACT 2008). |
| M62.8_3__O3_3-E02 | 🟩 | Aucune erreur retenue : seuils EWGSOP2 2019 exacts (SARC-F ≥ 4, préhension < 27/16 kg, ASM < 20/15 kg, ASM/taille² < 7,0/6,0 kg/m²) ; protéines 1,0–1,5 g/kg/j (ESPEN), vitamine D 800 UI dès 60 ans (OFSP). |
| M79.1__S5_4-E02 | 🟩 | Forme : clé vide « mesuresGénérales » hors schéma retirée. Aucune erreur médicale retenue (début à 12–24 h, pic 24–72 h). |
| M85.8__F2_20-E02 | 🟧 | Corrigé (forme) : correction mal formée (« ssp » en chaîne avalant priseEnCharge, « ">» » à la place de « ": ») reconstruite sans changer le texte. Corrigé : Q11 marquée masquée, Q14 (d4 qui nomme l'ostéopénie) passée en d3. Seuils OMS, Z-score ≤ −2,0, alendronate 70 mg/sem., zolédronate 5 mg/an, dénosumab 60 mg/6 mois, vitamine D 800 UI conformes. |

Contrôles lot 4 : `controle_menus_longs.py RHU` → 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage.

## Lot 5 — rangs 545 à 554

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| M94.0_1__S2_12-E01 | 🟩 | Aucune erreur retenue (exclusion d'une cause viscérale avant 40 ans de facteurs de risque, réévaluation à 3–4 semaines). |
| N14.2__F2_12-E03 | 🟩 | Forme : clé « false » hors schéma retirée (Q16) ; bloc c9 ramené à 5 points. Aucune erreur retenue : KDIGO 2012 (≥ 26,5 µmol/L en 48 h, ×1,5 en 7 j, stade 3), EXTRIP lithium > 4,0 mmol/L avec IR, vancomycine AUC/CMI 400–600, Tox Info 145. |
| N18.9__O3_4-E03 | 🟩 | Aucune erreur retenue : KDIGO 2024 (G3a–G5, A1–A3), metformine CI < 30 et ≤ 1000 mg/j à 30–44, dabigatran CI < 30, iSGLT2 dès DFG 20, finérénone si K ≤ 5,0. |
| N30.0_1__S4_2-E01 | 🟩 | Aucune erreur retenue : fosfomycine 3 g dose unique, nitrofurantoïne retard 100 mg ×2/j 5 j, cotrimoxazole 3 j en 2e ligne (SSI) ; Bent 2002 (≈ 90 %). |
| N30.0_2__S4_7-E02 | 🟩 | Aucune erreur retenue (SSI : fosfomycine, nitrofurantoïne 5 j ; cystite de l'homme 7 j ; ceftriaxone 2 g IV ; pyélonéphrite 7 j). Alerte mécanique de Q06 (« douloureuse ») : faux positif, la vignette décrit la prostate. |
| N34.1__S4_3-E02 | 🟧 | Corrigé : Q19 (menu long d4 qui nomme l'urétrite) passée en d3. Aucune erreur médicale retenue : ceftriaxone 1 g dose unique, doxycycline 100 mg ×2/j 7 j, Mycoplasma genitalium séquentiel, PCR de contrôle ≥ 2 semaines (IUSTI). |
| N39.4__S4_14-E02 | 🟩 | Forme : 71 notions (max. 70) → N69 (pronostic, non utilisée) fusionnée dans N68 ; natures « surveillance » remplacées par « décision ». Aucune erreur retenue. Vérifié : mirabégron 25 mg/j puis 50 mg/j (AIPS Betmiga, Brevier) ; solifénacine 5–10 mg ; polyurie nocturne > 33 % (ICS). |
| N46__S4_4-E02 | 🟧 | Corrigé : Q11 (d4 dont la vignette donne l'azoospermie non obstructive confirmée) passée en d3. Valeurs de référence OMS 2021 exactes (16 M/mL, 30 % progressive, 1,4 mL, 39 M) ; orchidopexie 6–12 mois, au plus tard 18 mois. |
| N47.1__F1_2-E02 | 🟩 | Forme : cellules de tableau mal enveloppées (c1) corrigées. Aucune erreur retenue (rétractabilité 4 % / 50 % / 90 %, abstention chez le petit enfant asymptomatique, succès > 80 % des dermocorticoïdes). |
| N48.4__S4_10-E01 | 🟩 | Forme : natures « surveillance » remplacées par « décision » ; « arbre » manquant ajouté (c3). Aucune erreur retenue : sildénafil 50 mg (25–100), tadalafil 10–20 mg ou 2,5–5 mg/j, testostérone < 8 / 8–12 nmol/L, hématocrite > 54 %, Princeton III. |

Contrôles lot 5 : `controle_menus_longs.py` RHU, TOX, URO → 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage.

## Lot 6 — rangs 555 à 564

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| N60.0__S2_3-E04 | 🟩 | Forme : nature « classification » hors énumération remplacée par « critère » (N20). Aucune erreur médicale retenue (BI-RADS 2/3/4, échographie avant 40 ans). |
| N60.1__S2_3-E01 | 🟩 | Forme : clé « false_placeholder » retirée (Q18). Aucune erreur médicale retenue (BI-RADS 3 ≤ 2 %, microbiopsie si BI-RADS 4–5). |
| N76.0__S4_18-E01 | 🟧 | Forme : « arbre » manquant ajouté (c4, c5, c7) ; rubrique followUpNetwork déplacée de c8 (5 rubriques) vers c7. Corrigé : Q12 (d4 qui nomme la vaginose) passée en d3. Aucune erreur médicale retenue : Amsel 3/4, Nugent ≥ 7, métronidazole 500 mg ×2/j 7 j, clindamycine crème 2 %, récidive ≥ 3/an (CDC 2021). |
| N81.1__S4_16-E01 | 🟩 | Aucune erreur retenue : POP-Q (Bump 1996), Hendrix 2002 (34/19/14 %), Olsen 1997 (11 %). |
| N81.2__S4_16-E02 | 🟧 | Forme : natures « surveillance » remplacées (N41, N57) ; bloc c4 ramené à 5 points. Corrigé : Q10 et Q18 (d4 qui nomment l'hystérocèle) passées en d3. Aucune erreur médicale retenue (POP-Q, Olsen 1997 : 11 % et ≈ 30 % de réopérations). |
| N81.6_1__S4_16-E03 | 🟩 | Aucune erreur retenue (POP-Q, fibres 25–30 g/j, dépistage colorectal 50–69 ans). |
| N87.9__F2_10-E01 | 🟧 | Corrigé : calendrier de dépistage obsolète (« deux frottis annuels puis tous les 3 ans ») remplacé par l'avis d'experts SSGO n° 50 lu en ligne (cytologie tous les 3 ans de 21 à 29 ans ; cytologie ou HPV tous les 3 ans de 30 à 70 ans), dans 5 passages ; Q10 (d4, vignette sans le nom de l'entité) marquée masquée. Forme : rubrique « prevention » hors énumération remplacée (N45). ASCCP 2019 et ESGO 2022 conformes. |
| N89.8__S4_18-E03 | 🟩 | Forme : Q11 (vignette qui nomme le diagnostic) marquée non masquée ; clé « false » retirée (Q18 ; la valeur juste « true: false » est conservée). Aucune erreur médicale retenue (whiff test, PCR CT/NG si < 25 ans ou nouveau partenaire). |
| N91.1_1__O1_9-E02 | 🟩 | Aucune erreur retenue (aménorrhée secondaire 3/6 mois, ≥ 20 follicules ou ≥ 10 mL, IVG dans les 12 semaines, test au progestatif). |
| N93.8__S4_17-E02 | 🟧 | Corrigé : calendrier de dépistage du col obsolète remplacé par l'avis d'experts SSGO n° 50 (frottis tous les 3 ans dès 21 ans), dans 4 passages. Forme : nature « surveillance » (N63) et clé « false » (Q18) corrigées. FIGO 2018 (24–38 j, ≤ 8 j), biopsie ≥ 45 ans, PBAC > 100 conformes. |

Contrôles lot 6 : `controle_menus_longs.py` des spécialités du lot → 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage. Source lue : SSGO, avis d'experts n° 50 (sggg.ch).

## Lot 7 — rangs 565 à 574

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| O13__O1_4-E03 | 🟩 | Forme : bloc c8 ramené à 5 points. Aucune erreur médicale retenue : ISSHP 2021 (≥ 140/90 après 20 SA, ≥ 160/110 sévère, PCR ≥ 30 mg/mmol, cible diastolique 85), sFlt-1/PlGF < 38 (Zeisler 2016), aspirine 100–150 mg avant 16 SA, LAMal sans franchise dès la 13e semaine. |
| O23.4__O1_4-E04 | 🟩 | Aucune erreur retenue (fosfomycine 3 g, nitrofurantoïne évitée à 36–38 SA, ECBU de contrôle, SGB → antibioprophylaxie per-partum). |
| O26.8_1__O1_7-E05 | 🟩 | Forme : clé « false » retirée (Q17). Aucune erreur médicale retenue (PA devant toute épigastralgie après 20 SA). |
| O26.8__O1_4-E01 | 🟧 | Forme : priseEnCharge réparée (lot 1). Corrigé : Q12 (d4, vignette sans le nom de l'entité) marquée masquée. Aucune erreur médicale retenue (ISSHP 2021, volume plasmatique +40–50 %). |
| O36.0__F2_17-E01 | 🟩 | Aucune erreur retenue : anti-D 300 µg à 28 SA et dans les 72 h (encore utile au-delà), 300 µg ≈ 15 mL d'hématies fœtales, Doppler ACM dès 16–18 SA. |
| O36.5__O2_7-E01 | 🟧 | Corrigé : Q16 (d4 qui nomme le RCIU) passée en d3. Aucune erreur médicale retenue (bétaméthasone 12 mg ×2, MgSO₄ < 32 SA, transfert niveau III < 32 SA ou < 1500 g). |
| O36.8__O2_7-E02 | 🟧 | Corrigé (forme) : le champ « notions » de la correction était une chaîne JSON invalide (6 lignes de tableau ouvertes par « [{ » au lieu de « [[{ ») ; structure reconstruite sans changer le texte ; clé « false » retirée d'une Kprim. Aucune erreur médicale retenue (RCOG 2011, CTG ≥ 20 min dès 28 SA, mort-né ≥ 22 SA ou 500 g, allocation dès 23 semaines). |
| O47.9__O1_4-E02 | 🟧 | Corrigé : Q13 (d4 qui nomme les contractions irrégulières) passée en d3. Aucune erreur médicale retenue (fibronectine < 50 ng/mL, col < 25 mm, ≥ 4 CU/20 min). |
| O62.1__O1_5-E01 | 🟧 | Corrigé : Q14 (d4 dont la vignette dit « col stagnant ») passée en d3 non masquée ; Q19 (vignette sans le nom) marquée masquée. Aucune erreur médicale retenue (ACOG/SMFM 2014 : phase active 6 cm, arrêt 4 h/6 h ; carbétocine 100 µg ; suivi sage-femme 56 jours). |
| O64.0__O1_5-E02 | 🟧 | Corrigé : Q20 (menu long d4 qui nomme la variété postérieure persistante) passée en d3. Aucune erreur médicale retenue (15–20 % / 5 %, 2e phase prolongée 3 h/2 h sous péridurale, ventouse abandonnée après 3 tractions, CI < 34 SA). |

Contrôles lot 7 : `controle_menus_longs.py GYN` → 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage.
