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

## PB06-PB07

Contre-audit croisé interne terminé le 23.11.2026 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/PB06_Analyses_Diabete_Thyroide_Phosphocalcique_20-analyses_production_XAi.json (20 analyses)
- 1_Theorie/PB07_Analyses_Inflammation_Infection_Microbiologie_24-analyses_production_XAi.json (24 analyses)
- 2_Pratique/PB06-PR_Analyses_Diabete_Thyroide_Phosphocalcique_20-analyses_PRATIQUE_production_XAi.json (40 défis)
- 2_Pratique/PB07-PR_Analyses_Inflammation_Infection_Microbiologie_24-analyses_PRATIQUE_production_XAi.json (48 défis)

Contrôles : outil controle PASS 4/4 (16 avertissements « source répétée », relus) ; structure identique au squelette de main (ids, noms, clés, _meta, organes, prélèvement) ; script de concordance chiffre ↔ source nommée (fiche HUG propre à chaque analyse) : PB06 263 propositions chiffrées concordantes, PB07 197, PB06-PR 31, PB07-PR 18 ; seul écart restant : 200 pmol/l, conversion déclarée de 0,2 nmol/l (Endocrine Society 2009) ; 468/468 chiffres attribués aux HUG retrouvés sur les fiches HUG réextraites le 23.11.2026 ; défis : 88/88 réponses ≤ 45 car., valeurs cohérentes avec l'intervalle de l'âge et du sexe cités.

Réextraction HUG : l'extracteur précédent vidait les valeurs qui suivent « < ». Les 57 fiches citées ont été rechargées avec l'extracteur corrigé. Valeurs « < x » retrouvées : CRP < 10,0 mg/l (3877, déclarée introuvable), thyroglobuline < 0,2 µg/l après thyroïdectomie (5901, déclarée introuvable), PCT < 0,5 µg/l (3940), syphilis index < 1 (3010) et RPR titre < 1 (5486), galactomannane ≤ 0,49 négatif (5049), BDG < 7,00 pg/ml (10276, déjà juste), 25-OH-vitamine D < 25 nmol/l (3979, déjà juste), glucose ≤ 6 jours 2,5–6,5 mmol/l (3826, déjà juste). Aucune autre valeur mal lue.

Valeurs revérifiées contre les sources, PB06 (plus de 60) :
- HUG : glucose 4,1–6,0 (adulte), 3,1–6,5 (7 jours–16 ans), 2,5–6,5 mmol/l (≤ 6 jours), délai 1 h/8 h ; HbA1c 3–6 % (9,3–42,1 mmol/mol), 1×/6 semaines, interférences ; insuline 2,6–24,9 mUI/l, hémolyse, coagulation 5–10 min puis glace ; peptide C 370–1470 pmol/l (5e–95e percentile), jeûne depuis la veille ; TSH 0,27–4,20, algorithme 0,4/6,0 mUI/l ; T4L 12,0–22,0, T4 totale 66–181 nmol/l, T3L 3,1–6,8, T3 totale 1,3–3,10 nmol/l ; Tg par âge (6,4–173 … 1,4–38,5 µg/l), récupération 80–120 %, < 0,2 µg/l après thyroïdectomie, 10 semaines si échantillon radioactif ; PTH 1,1–6,8 pmol/l, EDTA, 7–10 h ; 25-OH-D ≥ 75 / 50–75 / 25–50 / < 25 (adulte), > 50 / 25–50 / < 25 (enfant), remboursement dès 65 ans ; CTX et P1NP féminins ; PAL osseuse H 5,7–32,9 / F 4,7–27,1 et 5 tranches pédiatriques.
- Inselspital (Cobas PRO, v21.0 du 25.06.2026) : P1NP homme > 18 ans 13,9–85,5 µg/l et tranches pédiatriques ; CTX 319–1750 ng/l de 0 à 6 ans et tranches masculines.
- Medics : anti-TPO < 5,61 UI/ml (Hashimoto jusqu'à 90 %, Basedow 70 %, 8 h / 3 j) ; anti-Tg < 4,11 UI/ml (50–80 % / 30–50 %) ; TRAK < 3,10 UI/l (24 h / 12 j, passage placentaire) ; calcitonine F < 6,40 / H < 9,52 ng/l.
- ADA 2026 (sections 2 et 6) : ≥ 7,0 / ≥ 11,1 / HbA1c ≥ 6,5 %, prédiabète 5,7–6,4 %, 7,8–11,0 à 2 h, grossesse 5,1 / 10,0 / 8,5 ; niveaux 1 et 2 (< 3,9 / < 3,0) ; recontrôle à 15 min ; peptide C < 200 pmol/l, pas dans les 2 semaines d'une urgence hyperglycémique ; carence martiale ↑ HbA1c, renouvellement érythrocytaire ↓.
- Consensus ADA 2024 : β-OHB ≥ 3,0 mmol/l, pH < 7,3 ou HCO3 < 18, glucose ≥ 11,1 ; acidocétose euglycémique « approximately 10% » relu mot pour mot.
- Endocrine Society 2009 : 3,0 mmol/l, insuline ≥ 3 µU/ml (18 pmol/l), peptide C ≥ 0,2 nmol/l, β-OHB ≤ 2,7 ; RMS 2013 : 4,5 mmol/l, 2,8–3 mmol/l, glucomètres ; mediX 2025 : 5,6–6,9, cibles 6,5–7,0 % et 8,0–9 %, HGPO réservée à la grossesse (phrase du guide).
- ETA 2013 : rythme circadien (nadir l'après-midi, + 30 % le soir), 4,0–7,0 mU/l après 80 ans, > 10 mU/l avant 65–70 ans, contrôle à 2–3 mois ; ETA 2014 : 0,1–2,5 / 0,2–3,0 / 0,3–3,0–3,5, hCG, hypothyroxinémie (2,5e percentile), auto-anticorps 50 % et > 80 %, anti-Tg isolés 5 % ; ETA 2018 (résumé) : TRAb, 12–18 mois de méthimazole ; ATA 2015 : < 40 / < 15 pg/ml (enfant), > 500 et > 150 pg/ml, masse de cellules C, causes d'hypercalcitoninémie ; CHUV : IPP, 30 min, 1×/semaine.
- RMS 2015 : adénome, HHF (PTH peu élevée ou normale, hypocalciurie), 25-OH-D > 50 / > 75 ; RMS 2023 : causes secondaires ; Khan 2022 (résumé) : PTH > 10 pg/ml (1,05 pmol/l) à 12–24 h, > 12 mois ; RMS 2019 : rebond du dénosumab sur deux ans.

Valeurs revérifiées contre les sources, PB07 (plus de 50) :
- CRP : HUG < 10,0 mg/l ; Inselspital < 5 mg/l (F/M, tous âges) ; recommandation luxembourgeoise 2026 : × 100 en 24 h, demi-vie ~20 h, normalisation en 3–4 jours, baisse < 50 % au 4e jour, facteurs de variabilité.
- PCT : HUG < 0,5 µg/l, < 0,5 n'exclut pas une infection locale, > 2 µg/l ; CHUV 0,5 / 2 / 10 µg/l, voies respiratoires, < 6 h.
- IDSA/ASM 2024 : contamination < 3 % (cible 1 %), 20–30 ml par série ; CMV 36 % (6–11 ans) / > 90 % (≥ 80 ans) ; hétérophiles 6–10 jours, faux négatifs ~10 % ; toxoplasmose 22 % sans IgG ; rubéole immunité à vie, × 4 ; érythème migrant 70–80 % ; syphilis baisse de 4 fois ; dengue NS1, IgM 3–5 jours.
- EACS 12.0 (2023) : < 50 copies/ml ≥ 6 mois, CD4 ≥ 200/µl ou ≥ 15 % pour les vaccins vivants, < 100/µl antigène cryptococcique, rapport CD4/CD8.
- HUG : BDG < 7,00 / ≥ 7,00 pg/ml ; galactomannane ≤ 0,49 / ≥ 0,5, confirmation LFA ; délais et blocage de 48 h des sérologies ; microfilaires 10–14 h et 22–24 h ; CHUV : hémocultures 8–10 ml, IGRA 14 h, antigènes urinaires 24/48 h, Schistosoma 10–14 h.
- EFNS 2010 et ATS/JRS/ALAT 2020 (résumés) : attributions ramenées à ce que disent les résumés.

Corrections faites (72 lignes, journal machine audit/athena/corrections.jsonl, tour t11 ; script rejouable audit/athena/bio/corr_pb0607.py) :
- Valeurs « < x » perdues à l'extraction intégrées : CRP (HUG + Inselspital à la place de la seule source luxembourgeoise, 7 champs), thyroglobuline après thyroïdectomie (3 champs + défi), PCT (2 champs), syphilis (4 champs), galactomannane ≤ 0,49 (théorie + défi).
- Déduction retirée : baisse de la T3 libre dans l'hypothyroïdie manifeste (non écrite par l'ETA 2013), remplacée par l'algorithme HUG.
- Plus fort que la source : « distinguent le mieux » (PAL osseuse, résumé : « most promise », 2 champs) ; « sous 150 pg/ml, on surveille sans imagerie » (absent de l'ATA 2015) ; « une absence d'exposition n'exclut pas » (absent du résumé ATS/JRS/ALAT) ; « sort des bornes » (TSH, l'algorithme HUG utilise 0,4 et 6,0) ; attribution conjointe HUG/Medics resserrée (récupération de la Tg).
- Source mal nommée : « mise à jour IOF-IFCC » → consensus de l'ESCEO, de l'IOF et de l'IFCC (Bhattoa et al., 2025), fichier copié sous son vrai nom ; ESCEO ajouté aux glossaires.
- Phrases sur les sources remplacées par du contenu : P1NP homme et enfant, CTX enfant (Inselspital), parvovirus (délai), hémocultures (« dans le catalogue »).
- Borne calculée « 3,8 » remplacée par la formulation ADA ; pourquoiFaux sans source du P1NP sourcé.
- aVerifier : 5 entrées mises à jour, 1 ajoutée.

Réserves : Medics (privé, Berne) conservé pour anti-TPO, anti-Tg, TRAK et calcitonine ; aucune valeur chiffrée dans les fiches HUG, CHUV ni dans le PDF Inselspital de chimie clinique. Précipitines : aucune fiche suisse dédiée accessible (HUG 7128, 8116, 9178 : 404 ; 7129 : 403) ; le tube vient de la fiche CHUV Aspergillus fumigatus FEIA et reste déclaré « à confirmer ». CD4 : aucun intervalle chiffré HUG ni CHUV ; seuils cliniques EACS seulement. ETA 2018, Khan 2022, ESCEO-IOF-IFCC 2025, EFNS 2010 et ATS/JRS/ALAT 2020 lus en résumé seulement. Deux bornes CRP différentes (HUG < 10,0 ; Inselspital < 5) sont citées côte à côte. 25-OH-vitamine D : pas de seuil de toxicité dans les sources ouvertes (déclaré).

Rédacteur : honnête. Toutes les réserves signalées étaient exactes et déclarées dans aVerifier, y compris la perte de la valeur CRP et de la valeur Tg à l'extraction ; l'acidocétose euglycémique ~10 % est juste ; aucune valeur inventée. Erreurs relevées : une baisse de T3 déduite (déclarée), quatre formulations plus fortes que la source, une source mal nommée.

## Recontrôle HUG « < » (PB01-PB05, théorie)

L'ancien extracteur des fiches HUG vidait les valeurs écrites « < x » ou « <= x ». Les 96 fiches HUG utilisées pour les PB01-PB05 ont été réextraites avec l'extracteur corrigé (91 lisibles ; 5 numéros n'existent plus : 404). 32 contiennent une valeur « < » : 28 ont demandé une correction ; 4 étaient déjà justes (lactate 3807 et 3935 « dans l'heure », NT-proBNP 3939, test respiratoire 140).

Corrections (54 lignes, journal audit/athena/corrections.jsonl, tour t14 ; script audit/athena/t14/corr_t14.py), rien d'autre n'a changé :
- Valeurs manquées : haptoglobine < 180 / < 2270 mg/l (3968), B12 < 100 pmol/l déficitaire (3906), fer < 1 mois (3863), anticardiolipine IgG < 14 / IgM < 19 U/ml (2715) et anti-β2GPI IgG < 17 / IgM < 12 U/ml (2710), temps de thrombine ratio < 1,2 (8898), D-dimères < 500 ng/ml (2718), troponine T < 14 ng/l (3936), CK-MB < 10 % de la CK (9109), apoB < 1,0 g/l (10944), calprotectine < 600 à < 50 µg/g selon l'âge (6936).
- Lignes néonatales « ≤ 14 jours » (ou « ≤ 1 an », « ≤ 3 mois », « < 30 jours », « < 6 jours ») : créatinine, urée, phosphate, urates, ASAT, ALAT, GGT, PAL, bilirubines, albumine, amylase, préalbumine, céruloplasmine, CK, ammonium.
- Phrase fausse : Kleihauer « pas d'érythrocytes fœtaux attendus » → < 1 ‱ (6966) ; anticoagulant lupique : transport en moins de 4 h (2716).
- aVerifier : 4 entrées rectifiées (lignes néonatales ASAT/ALAT, calprotectine « sans valeur », D-dimères pédiatriques, apoB pédiatrique).
- Pratiques : aucun défi touché.
