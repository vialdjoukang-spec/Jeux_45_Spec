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
