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
