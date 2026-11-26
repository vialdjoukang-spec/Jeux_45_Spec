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

## Lot 8 — rangs 575 à 584

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| O70.1__O1_2-E03 | 🟧 | Corrigé : Q12 (d4 qui nomme la déchirure du 2e degré) passée en d3. Aucune erreur médicale retenue (RCOG GTG 29 : 3a/3b/3c/4 ; miction dans les 6 h ; sage-femme 56 jours ; LAMal maternité). |
| O80.0__O1_2-E01 | 🟩 | Aucune erreur retenue : terme 37+0–41+6, phase active 5 cm (OMS) / 6 cm (ACOG), SGB 35–37 SA, ocytocine 5 UI IV ou 10 UI IM, délivrance ≤ 30 min, anti-D 300 µg, vitamine K 2 mg à J0, J4 et S4 (SSP). |
| O92.1__O1_6-E02 | 🟧 | Corrigé (forme) : « ssp » de la correction était une chaîne mal formée (« ">» à la place de « ": ») ; structure reconstruite sans changer le texte. Aucune erreur médicale retenue (paracétamol, ibuprofène compatibles, mupirocine 2 %, ABM #26). |
| O92.4__O1_6-E03 | 🟩 | Aucune erreur retenue (perte ≤ 7–10 %, prise 20–30 g/j, lactogenèse II à 30–72 h, 8–12 tétées/24 h, natrémie > 145 mmol/L). |
| O92.7__O1_6-E01 | 🟩 | Aucune erreur retenue (ABM protocole 20 : 8–12 tétées, pression inverse, fébricule < 38,5 °C < 24 h). |
| O99.1__F2_25-E03 | 🟧 | Corrigé (forme) : champ « notions » de la correction en chaîne JSON invalide (code JavaScript dans une cellule) reconstruit ; rubrique nulle de N35 remplacée par positiveDiagnosis. Aucune erreur médicale retenue : < 150 G/L, rarement < 70 G/L, HELLP selon Tennessee (≤ 100 G/L, ASAT ≥ 70, LDH ≥ 600), neuraxiale sûre ≥ 70 G/L. |
| Q87.4_1__O7_23-E03 | 🟧 | Corrigé : Q12, Q13 et Q16 (d4 qui nomment le syndrome de Marfan) passées en d3. Aucune erreur médicale retenue (25 % de novo, Gand révisée, surveillance annuelle). |
| R03.0__F1_1-E03 | 🟩 | Forme : « arbre » manquant ajouté (c4). Aucune erreur médicale retenue : ESH 2023 (MAPA < 130/80, jour < 135/85, nuit < 120/70 ; automesure < 135/85 ; MAPA valide ≥ 70 %). |
| R04.0__S1_5-E01 | 🟧 | Forme : trois Kprim portaient 5 énoncés (maximum 4) ; un énoncé redondant retiré de chacune (Q16, Q17 : vrai ; Q18 : faux sur l'antibiothérapie, déjà traité en N40). Aucune erreur médicale retenue (AAO-HNSF 2020 : 90 % antérieures, 60 %/6 %, compression 10–15 min). |
| R06.0__O5_3-E02 | 🟩 | Aucune erreur retenue : morphine 2,5–5 mg PO /4 h chez le naïf, SC à 1/2–1/3 de la dose orale, midazolam 1–2,5 mg SC en complément (ASCO 2021). |

Contrôles lot 8 : `controle_menus_longs.py` des spécialités du lot → 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage.

## Lot 9 — rangs 585 à 594

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| R06.8__S1_18-E01 | 🟩 | Aucune erreur retenue : apnée ≥ 10 s, hypopnée ≥ 30 % avec désaturation 3 % ou micro-éveil (AASM), HypnoLaus (IAH ≥ 15 : ≈ 50 % des hommes, 23 % des femmes), STOP-BANG ≥ 3. |
| R07.3__S2_5-E01 | 🟩 | Forme : nature « surveillance » remplacée (N48). Aucune erreur médicale retenue (ECG dans les 10 min, troponine hs 0/1 h, paracétamol ≤ 4 g/j). |
| R09.8__O5_3-E03 | 🟧 | Forme : bloc c3 ramené à 5 points. Corrigé : Q04 (d4, vignette sans le nom de l'entité) marquée masquée. Aucune erreur médicale retenue (40–50 % des mourants, Bennett 2002). |
| R11.2_1__O5_4-E02 | 🟩 | Forme : cinq cellules de tableau mal enveloppées corrigées (c2). Aucune erreur médicale retenue : métoclopramide ≤ 30 mg/j (EMA), halopéridol 0,5–2 mg, dexaméthasone 4–8 mg. |
| R14__S3_2-E01 | 🟩 | Aucune erreur retenue (Rome IV, FODMAP 4–6 semaines encadré, probiotiques 4 semaines). |
| R15.9__S3_4-E02 | 🟧 | Forme : bloc c9 ramené à 5 points. Corrigé : Q14 (d4 dont la vignette livre la lésion obstétricale) passée en d3. Aucune erreur médicale retenue (RCOG 3a/3b/3c/4, OASIS ≈ 3 % au Royaume-Uni, neuromodulation sacrée après échec). |
| R17__F1_4-E01 | 🟧 | Corrigé : Q19 (d4, vignette sans le nom de l'entité) marquée masquée. Aucune erreur médicale retenue : loi de Hy, Maddrey ≥ 32 et prednisolone 40 mg 28 j, Tokyo 2018 (4–7 j après drainage), AINS rectal 100 mg avant CPRE, Gilbert < 20 % de conjuguée. |
| R18_1__F1_6-E02 | 🟧 | Corrigé : Q12 et Q20 (d4 qui nomment l'ascite cirrhotique) passées en d3 ; Q19 marquée masquée. Seuils EASL 2018 exacts : SAAG ≥ 11 g/L, protides > 25 g/L, PNN ≥ 250, albumine 1,5 g/kg J1 et 1 g/kg J3, 8 g/L au-delà de 5 L, GPVH ≥ 10 mmHg. |
| R19.6__F1_13-E01 | 🟩 | Aucune erreur retenue (85–90 % d'origine intra-orale, test organoleptique, chlorhexidine ≤ 2 semaines). |
| R20.2__S7_9-E05 | 🟧 | Corrigé (forme) : « ssp » de la correction était une chaîne JSON qui avalait priseEnCharge ; structure reconstruite sans changer le texte. Aucune erreur médicale retenue : calcium ionisé 1,15–1,30 mmol/L, Trousseau 3 min, gluconate de calcium 10 % 10–20 mL en 10 min (ESE 2015). |

Contrôles lot 9 : `controle_menus_longs.py` des spécialités du lot → 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage.

## Lot 10 — rangs 595 à 604

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| R23.1__F1_17-E03 | 🟥 | Rejet : la correction produite par l'API est tronquée (« ssp » en chaîne réparé, mais aucune priseEnCharge) et ne passe pas le schéma. Forme réparée sur veille : ssp, clé « false » (Q16), rubriques de c8 réparties. Contenu médical relu sans erreur (seuils OMS de l'anémie, ferritine < 15 µg/L). Reste hors de main. |
| R25.1__S7_3-E03 | 🟩 | Forme : Q12 (vignette qui nomme le diagnostic) marquée non masquée. Aucune erreur retenue : lithiémie résiduelle à 12 h et toxicité > 1,5 mmol/L, valproatémie 50–100 mg/L, glucose 15–20 g, propranolol 10–40 mg ponctuel. Alerte mécanique de Q11 (« tremblement », symptôme d'appel) : laissée. |
| R25.3__S7_10-E04 | 🟩 | Forme : bloc c8 ramené à 4 rubriques (deux rubriques déplacées vers c7). Aucune erreur médicale retenue (fasciculations chez ≈ 70 % des adultes sains). |
| R26.8_1__O3_6-E02 | 🟧 | Corrigé : notion N32 vide (« placeholder », rubrique « diagnostic_placeholder », non utilisée) supprimée ; Q14 (d4, vignette sans le nom de l'entité) marquée masquée. Aucune erreur médicale retenue (hypotension orthostatique ≥ 20/10 mmHg à 3 min, appui unipodal < 5 s). |
| R27.0__S7_1-E03 | 🟧 | Corrigé : Q17 (Kprim d4 qui nomme l'ataxie sensitive) passée en d3. Aucune erreur médicale retenue : hydroxocobalamine 1 mg IM un jour sur deux puis tous les 2 mois, B12 orale 1000–2000 µg, zone grise 150–250 pmol/L, monofilament 10 g. |
| R29.6__S7_1-E01 | 🟩 | Aucune erreur retenue (30 % / 50 % de chuteurs, TUG > 12–14 s, Tinetti 1988, exercice −23 %, vitamine D 800 UI dès 60 ans). |
| R47.0__S7_4-E01 | 🟩 | Aucune erreur retenue : altéplase 0,9 mg/kg (max 90 mg, 10 % en bolus) dans les 4,5 h, PA < 185/110 puis < 180/105, AOD < 48 h, INR > 1,7, thrombectomie jusqu'à 24 h selon l'imagerie, Engelter 2006 (30 %). |
| R47.1__S7_4-E02 | 🟧 | Forme : 77 notions (max. 70) → 7 notions non utilisées fusionnées dans une voisine de même rubrique. Corrigé : Q07 (d4, vignette sans le nom de l'entité) marquée masquée. Aucune erreur médicale retenue : riluzole 50 mg ×2/j, IgIV 2 g/kg, règle 20-30-40, décrément > 10 % à 3 Hz. |
| R49.0_1__S7_4-E03 | 🟥 | Rejet : correction non lisible par le schéma (« notions » en chaîne JSON invalide malgré réparation automatique ; « ssp » réparé). Contenu relu sans erreur (AAO-HNS 2018 : laryngoscopie au-delà de 4 semaines ou d'emblée si alarme). Reste hors de main. |
| R49.0__S1_3-E02 | 🟧 | Forme : clé « key » hors schéma retirée d'un énoncé (Q11). Corrigé : Q20 (d4, vignette sans le nom de l'entité) marquée masquée. Aucune erreur médicale retenue. |

Contrôles lot 10 : 0 menu fautif ; 0 erreur `valider()` sur les 8 pathologies 🟩/🟧 ; les 2 🟥 (R23.1, R49.0_1) gardent une erreur de schéma et restent hors de main.

## Lot 11 — rangs 605 à 614

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| R52.1__O5_3-E01 | 🟩 | Aucune erreur retenue : fentanyl transmuqueux seulement si ≥ 60 mg/j de morphine orale, paracétamol ≤ 3 g/j si cachexie, congé de proche aidant 3 jours par événement et 10 jours par an (CO art. 329h). |
| R53__O2_11-E02 | 🟩 | Aucune erreur retenue : déshydratation 3–5 / 6–9 / ≥ 10 %, Step-by-Step (PCT ≥ 0,5 ng/mL, CRP > 20 mg/L, ≤ 21 jours hospitalisé), bolus 10–20 mL/kg. |
| R54_3__O7_24-E01 | 🟩 | Aucune erreur retenue (Collard 2012 : 10–15 % fragiles, ≈ 40 % préfragiles ; GDS-15 > 5 ; protéines 1,0–1,2 g/kg/j ; vitamine D 800 UI dès 60 ans). |
| R55_3__F1_19-E01 | 🟩 | Aucune erreur retenue : ESC 2018 (lever actif 1 et 3 min, ≥ 20/10 mmHg ou PAS < 90, massage sinocarotidien > 40 ans avec pause ≥ 3 s, tilt-test), règle de San Francisco. Alerte mécanique de Q11 (« syncope », symptôme d'appel) : laissée. |
| R55_4__F1_19-E03 | 🟩 | Aucune erreur retenue (hypotension post-prandiale ≥ 20 mmHg dans les 2 h, ESC 2018). |
| R55__S7_1-E09 | 🟩 | Forme : clé « false » retirée (Q15). Aucune erreur médicale retenue (pooling 500–800 mL, arrêt du flux 6–8 s, règle CHESS, tilt-test avec trinitrine 400 µg). |
| R60.0_1__F1_16-E03 | 🟩 | Aucune erreur retenue : œdème sous amlodipine ≈ 10 % à 10 mg contre ≈ 3 % à 5 mg ; déchallenge et régression en 1–3 semaines. |
| R60.9__G12-E03 | 🟧 | Forme : priseEnCharge réparée au lot 1. Aucune erreur médicale retenue (amlodipine dose-dépendante, demi-vie 30–50 h, prégabaline et pioglitazone 1–10 %). |
| R62.0__O2_11-E01 | 🟧 | Forme : Q01 et Q17 portaient 7 notions (max. 6) ; une notion couverte ailleurs retirée de chacune. Aucune erreur médicale retenue (pas de marche à 18 mois → avis neuropédiatrique ; âge corrigé jusqu'à 24 mois). |
| R62.8_1__O2_1-E03 | 🟥 | Rejet : questions tronquées par l'API (8 questions, une question A sans réponse juste) ; ne passe pas le schéma. Reste hors de main. |

Contrôles lot 11 : 0 menu fautif ; 0 erreur `valider()` sur les 9 pathologies 🟩/🟧 ; R62.8_1 (🟥) reste hors de main.

## Lot 12 — rangs 615 à 624

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| R62.8__O2_1-E02 | 🟩 | Forme : Q08 (vignette qui nomme le diagnostic) marquée non masquée. Aucune erreur retenue (taille cible ± 6,5 cm, intervalle ± 8,5 cm, vitesse prépubertaire 4–7 cm/an, 2,3 % sous −2 DS). |
| R64__F1_8-E02 | 🟩 | Aucune erreur retenue : Fearon 2011 (> 5 % en 6 mois ou > 2 % si IMC < 20 ou sarcopénie ; précachexie ; réfractaire < 3 mois), préhension < 27/16 kg, nutrition entérale si < 60 % des besoins 1–2 semaines (ESPEN). |
| R68.0__G8-E03 | 🟩 | Forme : bloc c8 ramené à 5 points. Aucune erreur médicale retenue (stades suisses HT I–IV, irritabilité myocardique < 30 °C, CK > 5 × N). |
| R73.0_1__O4_7-E02 | 🟧 | Forme : clé « si » retirée (Q13). Corrigé : Q04 et Q12 (d4 qui nomment le prédiabète) passées en d3. Seuils exacts : ADA (5,6–6,9 mmol/L ; HbA1c 5,7–6,4 % ; 7,8–11,0 à 2 h), OMS 6,1 ; DPP −58 % / −31 %, DPPOS −27 % / −18 %, DPS −58 % ; dépistage asiatique dès IMC 23. |
| R73.0__F2_9-E02 | 🟧 | Corrigé : Q19 (menu long d4 qui nomme le prédiabète) passée en d3. Aucune erreur médicale retenue (ADA 2024, OMS 6,1–6,9 mmol/L, 5–10 %/an, tour de taille ≥ 94/80 cm). |
| R79.9__O4_4-E02 | 🟩 | Aucune erreur retenue (1 − 0,95²⁰ ≈ 64 %, valeur de référence 2,77 × √(CVa² + CVi²), valeurs critiques). |
| R80.9__F2_24-E02 | 🟩 | Forme : clé « si » retirée (Q09). Aucune erreur médicale retenue (RAC ≥ 3 mg/mmol, > 150 mg/24 h, néphrotique > 3,5 g/24 h, contrôle à 2–4 semaines, KDIGO 2024). |
| R82.9__F2_15-E02 | 🟩 | Aucune erreur retenue (analyse dans les 2 h ou 4 °C, ≥ 10⁵ UFC/mL ou ≥ 10³ chez la femme symptomatique). |
| S01.0__S8_7-E03 | 🟧 | Corrigé : délais de rappel antitétanique donnés sans l'âge ; précisés selon le tableau 10 du Plan de vaccination suisse 2026 lu en ligne (26–64 ans : ≥ 20 / ≥ 10 ans ; < 26 et ≥ 65 ans : ≥ 10 / ≥ 5 ans), dans 5 passages ; les réponses justes restent justes. Aucune autre erreur retenue (PECARN, anticoagulé → scanner, TEN-4-FACESp, fils J7–J10). |
| S01.8__S8_9-E02 | 🟧 | Corrigé : seuil antitétanique des plaies à risque (« > 10 ans ») précisé selon l'âge d'après le tableau 10 du Plan de vaccination suisse 2026 lu en ligne (≥ 10 ans de 26 à 64 ans, ≥ 5 ans avant 26 ans et dès 65 ans), dans 3 passages ; réponses inchangées. Aucune autre erreur retenue (irrigation à l'eau du robinet, fermeture primaire ≤ 6–8 h aux membres et ≈ 24 h au visage). |

Contrôles lot 12 : 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage. Source lue : Plan de vaccination suisse 2026, tableau 10 (bag.admin.ch).

## Lot 13 — rangs 625 à 634

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| S06.0__S8_7-E01 | 🟩 | Aucune erreur retenue (Canadian CT Head Rule, < 1 % de neurochirurgie, seuil bas sous antiagrégant ou intoxication). |
| S22.0__S8_10-E02 | 🟧 | Corrigé : Q12, Q13, Q14 et Q20 (d4 dont la vignette nomme l'ostéoporose ou le tassement) passées en d3 ; Q12 non masquée. Aucune erreur médicale retenue (Genant, zolédronate 5 mg/an −70 %, alendronate 70 mg/sem., CI si ClCr < 35, perte de taille 4 cm / 2 cm). |
| S29.0__S2_12-E02 | 🟩 | Aucune erreur retenue (paracétamol ≤ 4 g/j, ibuprofène 400 mg ×3 bref). |
| S30.1__S8_1-E01 | 🟧 | Corrigé : délai de rappel antitétanique d'une plaie propre mineure (« > 10 ans ») faux de 26 à 64 ans ; aligné sur le tableau 10 du Plan de vaccination suisse 2026 (≥ 20 ans de 26 à 64 ans, ≥ 10 ans aux autres âges). Aucune autre erreur retenue (WSES, morphine titrée 2–3 mg/5 min). |
| S52.5__S8_8-E02 | 🟩 | Forme : bloc c3 ramené à 5 points. Aucune erreur médicale retenue (inclinaison 22–23°, hauteur 11–12 mm, pente 11°, critères de Lafontaine, seuils d'acceptabilité). |
| S53.0__S8_4-E02 | 🟩 | Forme : bloc c8 ramené à 5 points et à 4 rubriques (followUpNetwork déplacé vers c7). Aucune erreur médicale retenue (paracétamol 15 mg/kg, réévaluation à 24–48 h). |
| S70.1__S8_3-E01 | 🟩 | Aucune erreur retenue (gravité par flexion du genou, ΔP < 30 mmHg pour le syndrome des loges, myosite ossifiante à 3–4 semaines). |
| S76.3__O4_1-E03 | 🟩 | Forme : « horsUrgence » placé dans « urgence » déplacé au bon niveau (plan 4). Aucune erreur médicale retenue (échographie à 48–72 h, reprise selon le grade, force ≥ 90 %). |
| T14.1_1__S8_9-E01 | 🟧 | Corrigé : délais de rappel antitétanique précisés selon l'âge (tableau 10 du Plan de vaccination suisse 2026) dans 4 passages ; réponses inchangées. Forme : natures « surveillance » remplacées (N45, N47). Aucune autre erreur retenue (lidocaïne 4,5 / 7 mg/kg, eau du robinet). |
| T14.1__S8_6-E03 | 🟧 | Corrigé : délais de rappel antitétanique précisés selon l'âge (tableau 10 du Plan de vaccination suisse 2026). Forme : bloc c8 ramené à 5 points. Aucune autre erreur retenue (bois radiotransparent, contrôle à 48–72 h). |

Contrôles lot 13 : 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage.

## Lot 14 — rangs 635 à 644

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| T15.0__S8_6-E01 | 🟩 | Forme : trois clés vides « mesuresGénérales » hors schéma normalisées. Aucune erreur médicale retenue (anneau de rouille, contrôle à 24–48 h, cicatrisation 24–72 h). Alerte mécanique de Q19 (« cornéen ») : la vignette décrit une plaie perforante, laissée. |
| T30.1__S8_2-E01 | 🟩 | Aucune erreur retenue (refroidissement 15–20 °C pendant 15–20 min, paume ≈ 1 %, règle des 9, réévaluation à 24–48 h). |
| T45.5_1__O7_22-E03 | 🟧 | Corrigé : Q14 (d4, vignette sans le nom de l'entité) marquée masquée. Aucune erreur médicale retenue (ISTH, CYP2C9, INR > 5 / > 9, cible 2–3, dabigatran 80 % rénal). |
| T50.9_3__S9_9-E03 | 🟧 | Corrigé : Q09 (d4 dont la vignette nomme les agents ingérés) passée en d3. Aucune erreur médicale retenue (corticoïdes > 40 mg/j, lithium 0,6–0,8 mmol/L, halopéridol 0,5–1 mg hors Parkinson et démence à corps de Lewy). |
| T50.9__S7_5-E06 | 🟩 | Forme : clé vide « molécule » en double retirée (plan 1). Aucune erreur médicale retenue (carbamazépine 4–12 mg/L, phénytoïne 10–20 mg/L, lithium 0,6–0,8 mmol/L, Tox Info 145). |
| T51.0__G7-E03 | 🟩 | Aucune erreur retenue (ALDH2*2 chez 30–40 % des Asiatiques de l'Est, adrénaline IM 0,3–0,5 mg). |
| T74.0_1__O3_1-E01 | 🟧 | Forme : clé « false » retirée (Q15). Corrigé : Q09 (d4 qui nomme la négligence) passée en d3 ; Q13 marquée masquée. Aucune erreur médicale retenue (congé de proche aidant 3 jours par événement, 10 par an). |
| T74.0__O2_3-E02 | 🟧 | Corrigé : Q04 (d4, vignette sans le nom de l'entité) marquée masquée. Aucune erreur médicale retenue. |
| T74.1_5__O2_3-E01 | 🟥 | Rejet : questions tronquées par l'API (8 questions au lieu de 20, une question A sans réponse juste) ; ne passe pas le schéma. Reste hors de main. |
| T74.3_2__O6_3-E02 | 🟩 | Aucune erreur retenue (≈ 27 % de violences par un partenaire, PHQ-9 / GAD-7 ≥ 10). |

Contrôles lot 14 : 0 menu fautif ; 0 erreur `valider()` sur les 9 pathologies 🟩/🟧 ; T74.1_5 (🟥) reste hors de main.

## Lot 15 — rangs 645 à 654

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| T75.1_1__S8_5-E01 | 🟩 | Aucune erreur retenue (Szpilman grades 1–2, SpO₂ ≥ 95 %, surveillance 4–6 h, O₂ si < 94 %, ERC 2021). |
| T78.1__O7_7-E03 | 🟧 | Forme : natures « surveillance » remplacées (N59–N61). Corrigé : Q12 (d4 dont la vignette nomme l'anaphylaxie) passée en d3. Aucune erreur médicale retenue (tryptase 30 min–2 h, seuil 20 % + 2 µg/L, alpha-gal 3–6 h). |
| T79.3__S6_4-E05 | 🟧 | Corrigé (erreur de fond) : Q05 donnait comme juste un rappel antitétanique chez un homme de 40 ans avec plaie souillée et dernier rappel à 7 ans ; selon le tableau 10 du Plan de vaccination suisse 2026 (26–64 ans, plaie à risque : rappel si ≥ 10 ans), aucune dose n'était due. Vignette portée à « 12 ans », distracteur D et « why » alignés, notions N45 et N46 corrigées (seuils par âge). Aucune autre erreur retenue (ISO ≤ 30 j, antibiotique si érythème > 5 cm ou T > 38,5 °C, 5–7 j). |
| T81.0_1__S8_12-E02 | 🟧 | Corrigé : Q03 (d4 dont la vignette nomme l'hématome) passée en d3. Aucune erreur médicale retenue (BARC 3a, protamine 1 mg/100 UI, résorption 2–3 semaines). |
| T81.4__O7_9-E03 | 🟩 | Aucune erreur retenue (définitions CDC des ISO, Swissnoso, antibioprophylaxie ≤ 60 min, 120 min pour vancomycine et quinolones). |
| T88.1__O2_4-E02 | 🟩 | Forme : nature « drapeau rouge » hors énumération remplacée (N19). Aucune erreur médicale retenue (ROR : fièvre 5–15 %, éruption ≈ 5 % ; convulsion à J5–J12 ; nourrisson < 3 mois fébrile → bilan). |
| T88.5__G8-E02 | 🟩 | Forme : clé « false » retirée (Q16). Aucune erreur médicale retenue (< 36 °C, plage interseuil 0,2 → 4 °C, chute de 1–1,5 °C la première heure). |
| V89.2__G13-E03 | 🟧 | Corrigé : Q09 et Q11 (d4 dont la vignette nomme l'accident) passées en d3. Aucune erreur médicale retenue : décès à 30 jours (statistique suisse), limites THC 1,5 µg/L et 15 µg/L (cocaïne, morphine, amphétamines), contrôle médical dès 75 ans tous les 2 ans. |
| W19__G13-E02 | 🟩 | Aucune erreur retenue (lividités et rigidité, acide tranexamique 1 g + 1 g/8 h dans les 3 h, LAA ≥ 8 h/sem., La Main Tendue 143). |
| X70.0__G13-E01 | 🟩 | Aucune erreur retenue (survivant : 24 h de surveillance, angio-scanner cervical, avis psychiatrique). |

Contrôles lot 15 : 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage.

## Lot 16 — rangs 655 à 664

| Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|
| X78__S9_12-E01 | 🟩 | Aucune erreur retenue (DSM-5 ≥ 5 jours sur un an, CP 321, CC 314c et 426, psychothérapie psychologique LAMal depuis juillet 2022). |
| Y69_1__O7_5-E01 | 🟩 | Aucune erreur retenue (OMS « Medication Without Harm » −50 %, annonce à Swissmedic, information transparente). Alerte mécanique de Q09 (« erreur ») : thème de la question, laissée. |
| Z00.0_1__O7_18-E03 | 🟧 | Forme : Q11 et Q19 (vignettes qui nomment l'entité) marquées non masquées. Corrigé : âge du dépistage colorectal remboursé porté de 50–69 à 50–74 ans (OPAS, en vigueur le 1.7.2025, communiqué de la Ligue suisse contre le cancer lu en ligne) et exemption de franchise limitée aux programmes cantonaux (10 passages) ; calendrier du col obsolète remplacé par l'avis SSGO n° 50 (4 passages). |
| Z00.0__O4_4-E01 | 🟧 | Corrigé : âge du dépistage colorectal remboursé porté de 50–69 à 50–74 ans (OPAS au 1.7.2025), 4 passages. Aucune autre erreur retenue (AUDIT-C ≥ 4/≥ 3, SCORE2 bas risque, lipides dès 40/50 ans). |
| Z00.1__O2_12-E01 | 🟧 | Corrigé : Q19 (d4, vignette sans le nom de l'entité) marquée masquée. Aucune erreur médicale retenue (perte ≤ 7–10 %, poids ×2 à 4–5 mois et ×3 à 12 mois, couverture ROR ≥ 95 %, Grenzsteine de Largo). |
| Z01.8_1__O7_10-E02 | 🟧 | Vérifié : remboursement du dépistage colorectal jusqu'à 74 ans depuis le 1.7.2025 (Ligue suisse contre le cancer). Corrigé : exemption de franchise limitée aux programmes cantonaux. Aucune autre erreur retenue (consentement éclairé, directives anticipées). |
| Z01.8_2__O7_16-E01 | 🟧 | Corrigé : Q08 (d4, vignette sans le nom de l'entité) marquée masquée. Aucune erreur médicale retenue (< 4 MET, risque chirurgical < 1 / 1–5 / > 5 %, jeûne 6/8/2 h, ESC 2022). |
| Z01.8_3__O7_16-E02 | 🟩 | Aucune erreur retenue (1 MET = 3,5 mL/kg/min, < 4 MET, report ≥ 60 jours après infarctus, RCRI de Lee 0,4/0,9/6,6/11 %). |
| Z02.7_2__O7_17-E01 | 🟩 | Aucune erreur retenue (définitions LPGA de l'incapacité et de l'accident, LAA 80 % dès le 3e jour). Alerte mécanique de Q10 (« certificat ») : thème de la question, laissée. |
| Z02.7_3__O7_17-E03 | 🟩 | Aucune erreur retenue (rente AI après un an d'incapacité moyenne ≥ 40 %, limitations fonctionnelles, facteurs psychosociaux exclus). |

Correctif rétroactif (lots 1, 6 et 9) : L29.0__S3_5-E03, N81.6_1__S4_16-E03, R14__S3_2-E01 et R15.9__S3_4-E02 donnaient le dépistage colorectal remboursé « de 50 à 69 ans » ; l'OPAS l'étend à 74 ans depuis le 1.7.2025 (programmes cantonaux). Âge et mention de franchise corrigés et reportés sur main avec ce lot. Le même chiffre obsolète subsiste dans Z12.1__O4_6-E01, Z53.8__O7_11-E03, Z80.9__O4_7-E03 et K57.3__G6-E05 (non encore audités).

Contrôles lot 16 : 0 menu fautif, 0 erreur `valider()` sur les pathologies du lot ; arène et test sans écran sur la branche de portage.

## Bilan au 26.11.2026 (arrêt de la session AAI)

- Pathologies auditées : 160 (rangs 505 à 664), dont 156 🟩/🟧 portées sur main et 4 🟥 restées hors de main (R23.1__F1_17-E03, R49.0_1__S7_4-E03, R62.8_1__O2_1-E03, T74.1_5__O2_3-E01 : fichiers tronqués ou mal formés, à régénérer).
- Reste à auditer : 248 pathologies du groupe B (à partir du rang 665, X… à Z… puis les ids hors classement), dans l'ordre de `content/pathologies/RANG_RENDEMENT.json`.
- Erreurs systématiques repérées, à corriger lors des lots suivants :
  1. PEP VIH « 72 h » au lieu de 48 h (CFIST 2025) : Z11.3__O6_5-E04, B20_primo_infection_vih___O7_12-E13, T14.9__O6_4-E12, T74.2_2__O2_3-E04, A60.0__S3_5-E16 (vignettes à relire, car certaines réponses dépendent du délai).
  2. Rappel antitétanique sans l'âge (tableau 10 du Plan de vaccination suisse 2026 : 26–64 ans ≥ 20/≥ 10 ans ; < 26 et ≥ 65 ans ≥ 10/≥ 5 ans) : à rechercher dans toute plaie ou brûlure restante.
  3. Dépistage colorectal remboursé « 50–69 ans » au lieu de 50–74 ans depuis le 1.7.2025 : Z12.1__O4_6-E01, Z53.8__O7_11-E03, Z80.9__O4_7-E03, K57.3__G6-E05.
  4. Calendrier du col « deux frottis annuels puis tous les 3 ans » (obsolète, SSGO n° 50).
  5. Corrections API mal formées (champ en chaîne JSON) qui empêchent la construction de l'arène sur la branche de veille : Z30.0__S4_8-E01, O36.8 réparée, D55.0__F2_16-E17, A60.0__S3_5-E16, R68.3__F1_4-E04, Z63.6__O3_6-E12, R06.4__O7_8-E05, H34.1__S1_2-E11, G10__O7_25-E06, Z56.6__O6_4-E03, E16.2_1__S9_9-E13, O36.8 et R49.0_1 (voir lot 1) ; outils de réparation : `repssp` et reconstruction par `json.loads` après retrait des virgules finales.
- Outils utilisés (hors dépôt, /home/claude/audB_tools) : audit.py (contrôle mécanique + digest), autofix.py, schema.py, rubbal.py, cap70.py, trim6.py, repssp.py, ccr74.py, fix.py (journal + champ `audit.claude`), porter.sh (portage + contrôles).

Signature : AAI (Anthropic AI)
