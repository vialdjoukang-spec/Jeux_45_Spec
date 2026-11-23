# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 01:48 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/PB01_Analyses_Hematologie_31-analyses_production_XAi.json (31 analyses)
- 2_Pratique/PB01-PR_Analyses_Hematologie_31-analyses_PRATIQUE_production_XAi.json (62 défis)

Contrôles : structure identique au squelette de main (clés, ordre, id, nom, _meta, organes, prelevement), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, mots de production, renvois internes (outil controle : PASS 2/2) ; défis : type interpreter / preanalytique, mode parmi les 3 modes du _meta, niveau-points cohérents, tempsSec 30–90, reponse ≤ 45 car. (le squelette n'a pas d'options de QCM).

Valeurs revérifiées contre les sources (texte local + en ligne), plus de 60 :
- CHUV, Laboratoire central d'hématologie, intervalles adultes (applicable 30.06.2026) : Hb H 133–177 / F 117–157 g/l ; Ht H 40–52 / F 35–47 % ; érythrocytes H 4,4–5,8 / F 3,8–5,2 T/l ; VGM 81–99 fl ; TCMH 27–34 pg ; CCMH 310–360 g/l ; RDW 11–15 % ; réticulocytes 20–120 G/l (5–15 ‰) ; plaquettes 150–350 G/l ; leucocytes 4–10 G/l ; neutrophiles 1,8–7,5 ; lymphocytes 1,5–4,0 ; monocytes 0,2–0,8 ; éosinophiles 0,05–0,3 ; basophiles 0,01–0,05 G/l ; VS H < 10 / F < 20 mm/h.
- Catalogue CHUV : VS tube gris foncé 2 ml rempli au trait, stable 2 h ambiant, délai < 24 h ; schistocytes stables 6 h ; ferritine : arrêt du fer 15 jours ; cytométrie : héparine de lithium 7,5 ml, 24 h ambiant.
- HUG, répertoire : FS (2663) tube mauve 2 ml, délai 24 h, enfant Hb 90–225, Ht 28–67, érythrocytes 2,7–6,6, TCMH 23–40, CCMH 280–380, VGM 68–126, plaquettes adulte 150–450 G/l ; répartition (2670) enfant neutrophiles 1,0–21,0, éosinophiles 0–1,0, basophiles 0–0,1, monocytes 0–1,79, lymphocytes 1,3–17,0, leucocytes 3,75–34 G/l, non segmentés 0–0,5 ; VS (2672) 0–15 / 0–20 avant 50 ans, 0–20 / 0–30 après ; ferritine (3907) H 11–342 / F 7–171 µg/l ; fer-transferrine (3863) fer H 8–33 / F 5–30, enfant 7–18 et 9–22 µmol/l, saturation 0,07–0,51, transferrine H 41–83 / F 44–87 µmol/l, à jeun, tube vert 2 ml ; bilirubine (3852) totale 6,8–25, enfant 0–5 et 0–10 µmol/l, conjuguée dosée si totale ≥ 22 ; haptoglobine (3968) 412–1693 mg/l, > 1 an idem ; holo-TC (3906) 37,5–188, dosée si B12 148–221 pmol/l ; groupe + RAI (2949) tube mauve 6 ml, 1–4 h, validité 96 h.
- Ars Medici 19/2025 : Hb < 80 g/l adressage immédiat, < 65 g/l menace vitale ; Hb > 180 g/l ou Ht > 55 % immédiat ; Ht > 60 % sévère ; neutrophiles < 0,5 G/l + fièvre = urgence ; leucocytose > 30 G/l sans infection, lymphocytose > 5 G/l : avis rapide ; leucocytose > 50 G/l + symptômes B / organomégalie : immédiat ; plaquettes < 25 G/l très sévère, > 1000 G/l immédiat.
- OMS 2024 (seuils d'Hb) : 105 / 110 / 115 / 120 g/l chez l'enfant, 110 / 105 / 110 g/l aux 3 trimestres, 120 / 130 g/l chez l'adulte de 15 à 65 ans, altitude + 4 / + 8 / + 11 g/l.
- mediX 2023 (B12) : < 150 pmol/l critique, 150–250 zone grise, acide méthylmalonique > 270 nmol/l, VGM > 98 fl, résection iléale ; mediX 2022 (fer) : ferritine < 15 / 15–30 µg/l, saturation ≤ 20 %.
- Revue médicale suisse 2020 (répartition leucocytaire) : agranulocytose < 0,5 G/l, éosinophilie 0,7–1,5 et hyperéosinophilie ≥ 1,5 (sévère > 5) G/l, basophilie > 0,1 G/l, lymphopénie < 1 G/l, neutropénie ethnique bénigne ; RMS 2020 (anémie aux urgences) : haptoglobine < 0,1 g/l, Coombs hors transfusion de moins de 4 mois.
- ACR/EULAR 2022 : VS ≥ 50 mm/h ou CRP ≥ 10 mg/l = + 3 points, âge ≥ 50 ans, classement à 6 points.
- SSGO avis n° 94 (2026) : ‰ d'érythrocytes fœtaux × 5 = ml ; 10 µg d'anti-D par ml.
- BSH 2023 (en ligne) : HbA2 ≥ 3,5 % avec TCMH < 27 pg ; > 4 % TCMH normale ; < 3,5 % possible (β+ légères) ; delta-thalassémie masquante ; ≥ 8 % Lepore ; > 15 % HbE ; HbF ≥ 5 % (δβ) et ≥ 10 % (HPFH) ; alpha-thalassémie à HbA2 normale.
- Heil et al., Ann Clin Biochem 2019 (en ligne) : holotranscobalamine 37–188 pmol/l.
- Recommandations ASMT / Transfusion CRS Suisse, version 14 du 01.02.2026 (en ligne) : deux déterminations sur prélèvements indépendants (§ 4.2.1), validité 96 h (§ 4.3), groupes O, A, B, AB et discordance non interprétable (§ 5.1.2), anticorps cliniquement significatifs : concentrés antigène-négatifs (§ 5.5).

Corrections faites (54, journal machine audit/athena/corrections.jsonl) :
- Hb sujet âgé : « l'OMS garde les seuils adultes » (non dit par l'OMS 2024) → seuils définis de 15 à 65 ans, données manquantes au-delà.
- Holotranscobalamine : « probablement en pmol/l » (supposition) → 37,5–188 pmol/l sourcé (HUG + Heil 2019).
- B12 : seuil de 270 nmol/l rattaché à l'acide méthylmalonique (phrase sans sujet).
- Typage : discordance ABO « interdit la transfusion du groupe trouvé » (non textuel) → « empêche d'interpréter le groupe » ; deux prélèvements indépendants ; source ajoutée à la bulle et au défi.
- Coombs : « mélange les hématies » (non textuel) → formulation de la RMS 2020 (théorie + défi, « génotypage » non sourcé retiré).
- 23 champs « Les laboratoires relus (…) ne publient pas » ou « aucun intervalle n'est publié » → laboratoires nommés, sans formule de processus.
- 3 défis : source « intervalles CHUV » remplacée par « catalogue des analyses CHUV » (fait tiré de la fiche).
- aVerifier : 14 entrées mises à jour (8 organes, parametres, holo-TC, Hb sujet âgé, résection iléale (textuelle en fait), alpha-thalassémie (retrouvée), ASMT relue).

Rédacteur : honnête. Les reprises non relues (ASMT, OMS sujet âgé, unité holo-TC) étaient déclarées dans aVerifier et PRET.md.

## PB02-PB03

Contre-audit croisé interne terminé le 23.11.2026 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/PB02_Analyses_Hemostase_18-analyses_production_XAi.json (18 analyses)
- 1_Theorie/PB03_Analyses_Electrolytes_Rein_Acide-base_22-analyses_production_XAi.json (22 analyses)
- 2_Pratique/PB02-PR_Analyses_Hemostase_18-analyses_PRATIQUE_production_XAi.json (36 défis)
- 2_Pratique/PB03-PR_Analyses_Electrolytes_Rein_Acide-base_22-analyses_PRATIQUE_production_XAi.json (44 défis)

Contrôles : mêmes que pour PB01 (outil controle : PASS 4/4, 2 avertissements SOURCE_RÉPÉTÉE vérifiés : tableau 1 de la BSH 2022 et fiche HUG 2730) ; défis : niveau-points, tempsSec 30–90, reponse ≤ 45 car., valeurs cohérentes avec la théorie.

Valeurs revérifiées contre les sources, PB02 (plus de 40) :
- HUG, répertoire : Quick ≥ 70 % (2725), aPTT 26–37 s (2714), fibrinogène 2,0–4,0 et 1,5–4,0 g/l de 0 à 18 ans (2723), anti-Xa HNF 0,3–0,7, HBPM 2×/j 0,5–1,0, 1×/j 0,8–1,6 UI/ml (2712, 9485, 9486), antithrombine ≥ 80 % (≥ 40 / ≥ 50 % avant 3 mois, 2717), facteur VIII et VWF 50–150 % (≥ 80 / 70 / 60 % avant 1 an, 2721, 2722), facteur IX ≥ 70 % (≥ 20 / 40 / 50 %, 5376), protéine C ≥ 70 % après 14 ans (2729), protéine S H ≥ 70 %, F ≥ 55 % puis ≥ 65 % après 50 ans, TP normal requis (2730) ; délais 7 j, 21 j, 48 h (anti-PF4), 72 h (génétique, consentement LAGH) ; repos 15 min, ABO, substitution 48 h ; double centrifugation de l'anticoagulant lupique au-delà de 4 h.
- CHUV : TP 75–125 %, aPTT 24–38 s, TT 15–18 s, fibrinogène 1,9–4,1 g/l ; tube citraté 3 ml ; anti-Xa 3 à 5 h après l'injection ; délais < 24 h, < 1 semaine, < 1 mois ; signature du médecin pour la génétique.
- EHRA 2021 (texte intégral PMC) : TT normal exclut le dabigatran ; aPTT normal exclut un taux supra-thérapeutique ; anti-Xa nulle exclut un taux pertinent ; effet des xabans sur le TP selon le réactif ; dTT et écarine pour quantifier.
- CHEST 2012 : anti-Xa 0,6–1,0 UI/ml à 4 h (2×/j), pic 3 à 5 h, demi-vie prolongée et accumulation en insuffisance rénale.
- Marcoumar : INR 2,0–3,0, valve mécanique 2,0–3,5 ; brochure HUG : INR 1,0 sans traitement, 2,5–3,5 valve mitrale.
- WFH 2020 : < 1 %, 1–5 %, 5–< 40 % ; ASH 2021 : VWF < 0,30 ou < 0,50 avec saignement, rapport < 0,7 ; ASH 2018 : recommandations 2.7 et 2.8 ; BSH 2022 : tableau 1 (causes de baisse et fausses hausses), × 15, < 0,5 %, 5 % FVL, 12 semaines, 6 semaines après la grossesse, 3 mois d'anticoagulation ; ACR/EULAR 2023 : 3 + 3 points ; ADJUST-PE : 500 µg/l, âge × 10 dès 50 ans ; Rossaint 2023 : Clauss ≤ 1,5 g/l (recommandation 29) ; Soma-Pillay 2016 : fibrinogène + 50 %, VIII, IX, X augmentés, antithrombine et protéine S abaissées.
- Score de CIVD ISTH 2001 : barème vérifié dans sa reproduction par Levi et al. (Br J Haematol 2009, tableau II), identique à Stago (plaquettes < 100 = 1, < 50 = 2 ; marqueurs de fibrine 2 / 3 ; TP + 3 à 6 s = 1, > 6 s = 2 ; fibrinogène < 1 g/l = 1 ; ≥ 5 = CIVD patente). L'original n'a pas pu être téléchargé.

Valeurs revérifiées contre les sources, PB03 (plus de 45) :
- USZ (préanalytique, alarmes au 22.12.2025) : Na 120 / 155, K 2,8 / 6,2, Cl 75 / 125, Ca 1,75 / 3, Ca ionisé 0,8 / 1,6, Mg 0,4 / 2, phosphate 0,32, urate 773 µmol/l, osmolalité 240 / 330 mmol/kg, lactate 4, COHb 0,25, MetHb 0,2 ; lipémie, poing serré, délai > 30 min, gazométrie dans les 15 min, bulles d'air.
- Bâle 2023 (gazométrie) : pH 7,35–7,45 (veineux 7,32–7,43), PaO2 > 10,6 kPa avant 80 ans et > 8,0 kPa après, PaCO2 H 4,66–6,38 / F 4,26–5,99 kPa, bicarbonate H 22,2–28,3 / F 21,2–27,0 (veineux 21–28), excès de base − 2 à + 3, oxyhémoglobine 90–95 %, MetHb < 1,5 %, COHb < 1,5 %, Na 136–145, K 3,4–4,5, Cl 98–107, Ca ionisé 1,15–1,33, lactate veineux 0,5–2,2, SvO2 70–80 %.
- HUG : Na 136–144, K 3,6–4,6, Cl 96–107, CO2 total 21–28,5, Ca 2,20–2,52, phosphate 0,80–1,45 (et pédiatrie), Mg 0,59–0,83, créatinine H 62–106 / F 44–80 (et pédiatrie), urée 3,2–7,5, cystatine C 0,65–1,24 / 0,81–1,64, urate H 286–518 / F 155–476, lactate 0,4–1,9 (transport dans l'heure), osmolalité 280–295 et formule.
- KDIGO 2012 : + 26,5 µmol/l en 48 h, × 1,5 en 7 jours ; KDIGO 2024 : G1–G5 (< 15), DFG créatinine-cystatine C, facteurs non rénaux de la cystatine C.
- Soma-Pillay 2016 : créatinine 44,2 µmol/l, urée 3,2 mmol/l, osmolalité − 10 mOsm/kg, bicarbonate 18–22, pH 7,40–7,47, PaCO2 3,6–4,3 kPa, PaO2 12,6–14,0 kPa, excès de base inchangé.
- Sepsis-3 : lactate > 2 mmol/l sous vasopresseurs ; RMS : hypokaliémie < 3,5 et 2,5–3, hypophosphatémie 0,32–0,80 et < 0,32, hypocalcémie 1,12 et 2,20, HPT + 0,25 mmol/l, TAN > 16, FE Mg > 2 %, PvCO2 7,3 → PaCO2 5,8–7,6 kPa, COHb > 10 / 15 %, demi-vie 4–5 h, lactate > 10 et cyanure ; SFMU : MetHb < 2 %, traitement si symptômes ou > 30 % ; EULAR 2016 : < 360 et < 300 µmol/l ; Tox Info : COHb 1–2 %, 5–10 % chez le gros fumeur.

Corrections faites (68, journal machine audit/athena/corrections.jsonl) :
- PB02, attributions fausses (8) : INR > 3 « hors valve mécanique » (la brochure HUG met la valve aortique dans 2,0–3,0) ; héparine de l'aPTT attribuée à la fiche HUG 2714 ; causes de l'aPTT allongé attribuées à l'ISTH 2020 (c'est la WFH 2020) ; héparine du TT attribuée au catalogue CHUV ; « la génétique se fait à tout moment, même sous anticoagulant » attribué à la BSH 2022 (introuvable), dans 4 champs et 1 défi (FVL-2, réécrit sur le consentement HUG).
- PB02, champs faux : « diminution » de l'aPTT et du TT qui ne donnaient pas de cause ; « grossesse » du TP et de l'aPTT qui ne parlaient pas de la grossesse ; fibrinogène < 1,9 g/l « fait chercher une consommation » sans source ; « plus rare » (homozygotie) non sourcé ; mention « repris par Stago » retirée (5 champs).
- PB03 : « sécrétion inappropriée d'ADH » attribuée à la RMS 2025 (absente du résumé) → grossesse (Soma-Pillay) ; « mêmes catégories G chez l'enfant » → équation pédiatrique CKiD (KDIGO 2024) ; intervalles de Bâle précisés « en gazométrie » ; 5 champs « grossesse » qui ne parlaient pas de la grossesse ; intervalles gravidiques chiffrés ajoutés (pH, PaO2, PaCO2, excès de base inchangé).
- Défis : aPTT-1, aPTT-2, VWF-2, bilan-2 et PaCO2-1 alignés sur les sources.
- aVerifier : 16 entrées mises à jour.

Rédacteur : honnête. Il avait déclaré lui-même la lecture du score ISTH via Stago, les résumés seuls (RMS, Spasovski) et l'absence de PaCO2 gravidique chiffrée ; les attributions « génétique à tout moment » et ADH n'étaient pas déclarées, mais elles relèvent de l'erreur de lecture et non de la dissimulation.

## PB04-PB05

Contre-audit croisé interne terminé le 23.11.2026 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/PB04_Analyses_Foie_Pancreas_Digestif_29-analyses_production_XAi.json (29 analyses)
- 1_Theorie/PB05_Analyses_Cardiaque_Vasculaire_Lipides_14-analyses_production_XAi.json (14 analyses)
- 2_Pratique/PB04-PR_Analyses_Foie_Pancreas_Digestif_29-analyses_PRATIQUE_production_XAi.json (58 défis)
- 2_Pratique/PB05-PR_Analyses_Cardiaque_Vasculaire_Lipides_14-analyses_PRATIQUE_production_XAi.json (28 défis)

Contrôles : outil controle PASS 4/4 (19 avertissements d'unité mg/dl, tous accompagnés de l'unité SI ou cités tels que la source) ; script de concordance chiffre ↔ source nommée : PB04 270 propositions chiffrées concordantes, PB05 130, écarts restants tous vérifiés à la main ; 295 chiffres attribués aux HUG recomparés aux fiches HUG rechargées en ligne le 23.11.2026 (295/295 retrouvés) ; défis : réponse ≤ 45 car., valeurs cohérentes avec la théorie et l'âge du cas.

Valeurs revérifiées contre les sources, PB04 (plus de 40) :
- HUG, répertoire (fiches en ligne) : ALAT, ASAT, GGT par sexe ; PAL 24,8–102 U/l adulte, 129–417 de 11 à 13 ans, 57–254 de 14 à 16 ans ; bilirubine totale 6,8–25, conjuguée 0,49–9,5 µmol/l et tranches pédiatriques (0–2,4 de 2 à 9 ans, 0–5,2 de 14 à 16 ans), conjuguée dosée si totale ≥ 22 µmol/l ; albumine 35–48 g/l ; protéines totales 61–79 g/l ; préalbumine 223–380 mg/l ; ammoniémie 11–35 (0–140 chez le nouveau-né), transport sur glace ; lipase 13–60 U/l ; amylase 31–108 U/l ; céruloplasmine 0,17–0,46 g/l ; AAT 0,87–1,93 g/l ; élastase > 200 et < 100 µg/g ; blocage de 48 h des sérologies.
- USZ (préanalytique) : garrot prolongé (bilirubine ↑, GGT ↓), position couchée/debout jusqu'à 10 % sur les protéines totales, hémolyse (ASAT, LDH, CK), récipient sans métal pour la cuprurie, alarme ammoniémie 80 µmol/l.
- EASL-ERN 2025 Wilson (tableau 6 relu en -layout) : cuprurie normale < 40 µg (0,65 µmol) enfant et < 100 µg (1,6 µmol) adulte, forte suspicion > 100 µg ; céruloplasmine 20–40 mg/dl, Wilson < 10 mg/dl ; traitement maintenu pendant la grossesse (2.7.1).
- EASL 2023 grossesse (tableau 2) : bilirubine totale 4–16, 3–13, 3–14 µmol/l par trimestre.
- Hao 2016 : IgG4 ≥ 1,35 g/l ; ESPGHAN 2020 : IgA < 0,2 g/l après 3 ans ; Lucerne : IgG4 0,03–2,01 g/l et interférences (hémolyse, lipémie, ictère, facteurs rhumatoïdes), calprotectine (AINS, selles sanglantes, granulopénie) ; recommandation européenne 2022 : + 20 ppm, 10–15 % de non-excréteurs d'H2 ; ERS 2017 : CRP simultanée pour l'AAT ; HUG 2017 : échographie abdominale « étape essentielle », demi-vie de l'albumine ~3 semaines.
- Nouvelles sources : Fatoux 2025 (Clinique de La Source) albumine 56–66 %, causes d'hypo- et d'hyperprotidémie ; Viollier cuivre urinaire 3 jours, 2 fois par semaine.

Valeurs revérifiées contre les sources, PB05 (plus de 30) :
- ESC 2023, données supplémentaires (tableau S4) : TnT Elecsys < 5 (douleur > 3 h) / < 12 avec Δ1h < 3 / ≥ 52 ou Δ ≥ 5 ng/l ; TnI Architect < 4 / < 5 avec Δ < 2 / ≥ 64 ou Δ ≥ 6 ng/l ; seuils propres au dosage, valables quel que soit l'âge, le sexe et la fonction rénale ; définition de l'infarctus (hausse et/ou baisse, au moins une valeur > 99e percentile).
- CHUV : TnT < 14 ng/l dès 1 an ; CK-MB < 6 % de la CK totale ; HUG : TnT 99e percentile, CK H 47–222 / F 33–187 U/l, CK-MB 5–19, homocystéine 7,0–22,3 µmol/l, NT-proBNP 300 / 450 / 900 / 1800 ng/l, Lp(a) > 300 mg/l, bilan lipidique 2021 (≥ 5 mmol/l, HDL ≤ 1 mmol/l).
- Medics : homocystéine < 12,0 µmol/l, + ~10 %/h sans séparation en 30 min, causes (CBS, MTHFR, B6/B12/folates, insuffisance rénale, méthotrexate, phénytoïne) ; CK-MB « herzmuskelspezifisch » ; myoglobine F 25–58 / M 28–72, hausse < 3 h, pic 4–12 h, normale vers 24 h ; apoB F 0,60–1,41 / H 0,66–1,44 g/l.
- RMS 2020 (rhabdomyolyse) : seuils 1000–5000 U/l, mortalité jusqu'à 60 % (facteurs cumulés dont pic > 40 000), demi-vie de la myoglobine 2–4 h ; Soma-Pillay 2016 : ANP + 40 % au 3e trimestre, HDL + 15 % au-dessus des valeurs hors grossesse, LDL + 50 % à terme ; medix 2023 : homocystéine normalisée en 3 mois après substitution de B12.

Corrections faites (60, journal machine audit/athena/corrections.jsonl, tour t9) :
- Causes déduites remplacées par des causes lues : protéines totales (diminution attribuée aux HUG, « fraction majeure » absente de la fiche), CK-MB (diminution et défi ck_mb-1), homocystéine (diminution).
- Erreurs de sens : HDL bas « au 3e trimestre » (il reste 15 % au-dessus) ; hausse de 40 % de l'ANP présentée pour le NT-proBNP et le BNP ; CK > 40 000 « risque qui s'additionne » (la RMS parle de mortalité quand les facteurs s'additionnent).
- Attributions : myoglobine « 24 h » (Medics, pas la RMS) ; quatrième définition universelle 2018 citée alors que seule sa synthèse (Cardiol J 2021) avait été lue (6 champs).
- Troponine hs : dépendance au dosage formulée (99e percentile, seuils propres au dosage, ESC 2023) ; 5 champs de la TnI qui ne parlaient que de la fiche CHUV.
- Phrases sur les sources ou hors sujet (« ne publient pas de valeur d'alarme », « ne décrivent pas de cause », « ne signalent pas d'interférence », « aucun seuil gravidique n'y figure ») remplacées par du contenu (12 champs).
- Défi phosphatase_alcaline-2 : PAL 320 U/l à 15 ans hors de l'intervalle HUG 14–16 ans (57–254) ; âge passé à 12 ans (129–417).
- aVerifier : 6 entrées réglées retirées, 4 ajoutées, 1 mise à jour.

Réserves : Medics (privé, partenaire de l'Inselspital) et Hôpital cantonal de Lucerne conservés et déclarés : les fiches CHUV et HUG rechargées ne donnent pas de valeur pour apoB, Lp(a) pédiatrique, myoglobine, IgA, IgG4, calprotectine ni cuprurie ; Fatoux 2025 (Clinique de La Source) et Viollier sont privés ; ESC 2023 lu dans ses données supplémentaires, texte principal bloqué.

Rédacteur : honnête. Les chiffres concordent avec ses sources (y compris la cuprurie, que l'extraction texte rendait douteuse) ; il avait déclaré dans aVerifier les causes déduites (protéines totales, CK-MB, homocystéine) et la synthèse de la définition universelle ; non déclarés : l'ANP lu comme BNP, le HDL gravidique, la distorsion du seuil de 40 000 et l'incohérence de PAL-2, qui relèvent de l'erreur de lecture.
