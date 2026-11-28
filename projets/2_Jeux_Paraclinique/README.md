# 2_Jeux_Paraclinique

- `chantier.pdf` : le chantier complet (vision, jeu, évaluation, étapes, deux audits).
- `audit_1.md`, `audit_2.md` : constats et corrections appliquées.

## Ressources du projet dans le dépôt
- `conception/plans/paraclinique.plan.json`
- `conception/pdf/paraclinique.pdf`
- `conception/outils/catalogue_paraclinique.py`
- `conception/donnees/paraclinique/`

## Journal Biologie (branche `paraclinique-biologie-suite`)
- 28.11.2026 · lot 0 : 28 analyses du catalogue déjà couvertes par une fiche existante sont rattachées par synonyme (champ `_rattachements`) ; plan des 112 fiches à créer en 12 lots (`LOTS_BIOLOGIE_SUITE.json`) ; outil de lecture des sources `conception/outils/paraclinique/sources_bio.py` (RPA HUG, AIPS refdata, cache) ; `importer_ex1.py` cartographie sans le dépôt source ; analyses sans fiche 140 → 112 ; audit 101/101 vert.
- 28.11.2026 · lot 1 (hémostase, 10 fiches : facteurs VIII et IX, von Willebrand, antithrombine, protéines C et S, facteur V Leiden, prothrombine G20210A, anticoagulant lupique, anticardiolipine et anti-β2GPI) ; `_creation` et `_rattachements` exemptés du contrôle verbal A5 (métadonnées, comme `_origine`).
- 28.11.2026 · lot 4 (endocrinologie, 10 fiches : anti-TPO, anti-thyroglobuline, TRAb, cortisol libre urinaire, métanéphrines plasmatiques et urinaires, DHEA-S, 17-OH-progestérone, SHBG, AMH) ; phénoxybenzamine absente du corpus AIPS suisse (à vérifier sur compendium.ch).
- 28.11.2026 · lot 3 (digestif et diabète, 10 fiches : élastase fécale, FIT, antigène H. pylori fécal, tests respiratoires à l'urée C13 et à l'hydrogène, insuline, peptide C, cétonémie, glycémie capillaire, calcitonine) ; valeurs du CHUV et de Viollier là où le RPA des HUG n'a pas de fiche.
- 28.11.2026 · lot 2 (hémostase, hématologie, biochimie, 10 fiches : anti-PF4/héparine, bilan de thrombophilie, bilirubine libre, JAK2-CALR-MPL, électrophorèse de l'hémoglobine, homocystéine, CK-MB, magnésium, cuivre urinaire, IgG4) ; absents du corpus AIPS suisse consulté : D-pénicillamine, Wilzin®, Siklos®, gluconate de calcium 10 % injectable (à vérifier sur compendium.ch).
- 28.11.2026 · lot 6 (sérologies infectieuses, 10 fiches : procalcitonine, syphilis, CMV, EBV, toxoplasmose, rubéole, borréliose, IGRA, β-D-glucane, parvovirus B19) ; spiramycine et sulfadiazine absentes du corpus AIPS suisse consulté ; Extencilline® classée « médicament de comparaison étranger » (disponibilité à vérifier).
- 28.11.2026 · lot 5 (endocrinologie et obstétrique, 10 fiches : IGF-1, GH, copeptine, chromogranine A, gastrine, sFlt-1/PlGF, fibronectine fœtale, test de grossesse urinaire, TPNI, HE4) ; Celestone Chronodose® et Adalat® absents du corpus AIPS suisse consulté ; chromogranine A, HE4 et copeptine facturées par analogie (Liste des analyses 01.07.2026).
- 28.11.2026 · lot 7 (microbiologie, 10 fiches : antigènes urinaires pneumocoque et légionelle, test rapide du streptocoque A, microfilaires, sérologies du voyageur, précipitines, coproculture et PCR multiplex, C. difficile, expectorations et tuberculose, PCR Chlamydia et gonocoque, frottis cervical et HPV) ; diéthylcarbamazine, ivermectine et praziquantel absents du corpus AIPS suisse consulté ; ssi.guidelines.ch illisible sans JavaScript.
