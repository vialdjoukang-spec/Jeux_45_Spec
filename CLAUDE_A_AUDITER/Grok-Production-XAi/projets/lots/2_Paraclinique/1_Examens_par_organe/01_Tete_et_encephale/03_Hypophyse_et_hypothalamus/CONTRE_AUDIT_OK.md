# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 01:07 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P01-03-BIO_Biologie_Hypophyse_et_hypothalamus_6-examens_production_XAi.json
- 1_Theorie/P01-03-FCT_Exploration_fonctionnelle_Hypophyse_et_hypothalamus_5-examens_production_XAi.json
- 1_Theorie/P01-03-IMG_Imagerie_Hypophyse_et_hypothalamus_1-examens_production_XAi.json
- 2_Pratique/P01-03-BIO-PR_Biologie_Hypophyse_et_hypothalamus_6-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P01-03-FCT-PR_Exploration_fonctionnelle_Hypophyse_et_hypothalamus_5-examens_PRATIQUE_production_XAi.json
- 2_Pratique/P01-03-IMG-PR_Imagerie_Hypophyse_et_hypothalamus_1-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Petersenn et al., Pituitary Society 2023 (Nat Rev Endocrinol) : ≤ 200 µg/l (ng/ml) fait envisager d’autres causes ; dilution au 1/100 devant un adénome géant ; répéter le dosage si < 5 fois la LSN ✔
- Giustina et al., Pituitary 2024 : IGF-1 > 1,3 fois la LSN pour l’âge confirme l’acromégalie chez un patient aux signes typiques ✔
- Bhasin et al., Endocrine Society 2018 : limite inférieure harmonisée de la testostérone totale 264 ng/dl, soit 9,2 nmol/l ✔
- Winzeler et al., Lancet 2019 : copeptine ≤ 3,8 pmol/l à 60 min après arginine (précision 93 %) ✔
- Refardt et al., NEJM 2023 (CARGOx) : précision 74,4 % (arginine) contre 95,6 % (sérum salé hypertonique) ✔
- AACE 2019 (déficit en GH de l’adulte) : test d’hypoglycémie insulinique, glycémie < 2,2 mmol/l (40 mg/dl), pic de GH ≤ 5 µg/l ✔
- Smarter Medicine SSED 2025, recommandations 2 (lévothyroxine) et 5 (testostérone), smartermedicine.ch ✔

Corrections faites :
- Smarter Medicine SSED 2025 (2 citations) : format commun, point final dans la citation et numéro ajoutés (recommandations 2 et 5) ; texte vérifié mot pour mot en ligne
- P01-03-BIO-PR : glossaire + TPO (sigle employé, absent)
- Constat : l’IRM dit « négative chez environ un tiers » et « détecte environ la moitié des microadénomes » (Fleseriu 2021) ; non revérifié, laissé
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main ; le _lot.aVerifier est ajouté comme dans les autres dépôts ; les « reponse » de défis de plus de 45 caractères sont des réponses rédigées, signalées et non raccourcies.
