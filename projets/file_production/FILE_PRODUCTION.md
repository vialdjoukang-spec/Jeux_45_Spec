# File de production — 5 chantiers hors 45 Spec

Mesure automatique du 28.11.2026 07:11. Progression d'ensemble : **99 %**.

| # | Chantier | Branche | Modèle | Fait | Cible | % | État | Session | PR |
|---|---|---|---|---:|---:|---:|---|---|---|
| 1 | Paraclinique · Biologie | `paraclinique-biologie-suite` | opus (effort élevé) | 140 | 140 | 100 | fusionne | session_01JErHPt6t1Rq93UxLLPbFY1 | 61 |
| 2 | Paraclinique · Explorations | `paraclinique-explorations-audit` | fable | 174 | 174 | 100 | fusionne | session_01JErHPqC8BLUjU4FqKCoiSJ | 59 |
| 3 | Paraclinique · Imagerie | `paraclinique-imagerie-cliches` | opus (effort élevé) | 1448 | 1474 | 98 | en_cours | session_01JErHPqMi8t8YaE849wKRjG | 60 |
| 4 | Tétrade | `tetrade-finition` | opus (effort élevé) | 604 | 613 | 98 | fusionne | session_01JErHPt9L625h92GXWwGqF5 | 57 |
| 5 | Transversal | `transversal-audit` | fable | 248 | 248 | 100 | fusionne | session_01JErHPpPrbzdWGZrNVsRn9R | 56 |

Unités mesurées : 1 = fiches rédigées sur les 140 sans fiche ; 2 = fiches au statut AUDITÉ ; 3 = entités avec cliché (jauge) ; 4 = « à vérifier » levés sur 613 ; 5 = lots audités du manifeste.

- Chantier 1 : Fusionné le 28.11 (audit 213/213 fiches vertes, épidémiologies conformes, non-perte à 0). Les 140 analyses sont traitées : 112 fiches créées, 28 rattachées à une fiche existante.
- Chantier 2 : Fusionné le 28.11 après rétablissement de l'entrée de glossaire ICSD-3 (non-perte à 0, trois contrôles Paraclinique verts). 174/174 fiches relues : 8 🟥, 33 🟧, 46 🟨.
- Chantier 3 : La jauge ne compte que les entités avec au moins un cliché. État déclaré par la session le 28.11 à 06:55 : lot 9 en cours, 660 clichés pathologiques et 126 normaux encore manquants.
- Chantier 4 : Fusionné le 28.11 (34/34, non-perte à 0). 9 « à vérifier » gardés avec le lieu où vérifier (EAU 2025, BTS 2023, ESMO, SSGO, SwissPedDose…). Écarts de conformité listés dans CONFORMITE_PROMPT.md : circuits symptôme → syndrome → examen absents de 12 systèmes, pas de « question à poser », mannequin 3D non retournable.
- Chantier 5 : Fusionné le 28.11 (rapports valides, non-perte à 0). 6 🟥 et 36 des 38 🟧 corrigés ; 466 points non vérifiés listés dans les rapports ; AIPS intégrale inaccessible (posologies confrontées au résumé compendium.ch). Titre de S1-03 (Échelle suisse de triage à 4 degrés, non 5) à corriger hors couloir.

Signature : AAI (Anthropic AI)
