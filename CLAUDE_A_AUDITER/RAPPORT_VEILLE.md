<<<<<<< HEAD
# Veille automatique — 2026-11-22 22:18
=======
# Veille automatique — 2026-11-22 23:34
>>>>>>> origin/main

1 nouveau(x) lot(s) : 0 fusionné(s), 1 refusé(s) ou partiel(s).

## Lots
- 🟥 `CLAUDE_A_AUDITER/EN_ATTENTE_AUDIT_MEDICAL.json` (HEAD) : illisible même après réparation ('list' object has no attribute 'get')

## Contrôles après fusion
<<<<<<< HEAD
- Audit de fond : {'corrections': 0, 'acceptees': 323, 'ouvertes': 1, 'fiables': 578, 'examens': 820, 'aCompleter': 487}
- Lots de complément : 487 examens à compléter, lots dans Production_XAi/Lots_a_produire/complement_presentation
- Audit de conception : RÉUSSI 34/34
- Audit de couverture : RÉUSSI {'regions': 9, 'organes': 82, 'prelevements': 23, 'Imagerie': 292, 'Biologie': 280, 'Exploration fonctionnelle': 151, 'Endoscopie': 35, 'Anatomopathologie / biopsie': 62}
=======
- Audit de conception : RÉUSSI 34/34
- Audit de couverture : RÉUSSI {'regions': 9, 'organes': 82, 'prelevements': 23, 'Imagerie': 292, 'Biologie': 280, 'Exploration fonctionnelle': 151, 'Endoscopie': 35, 'Anatomopathologie / biopsie': 62}
- Non-perte face à main : non-perte : OK (0 fichier(s) en perte)
>>>>>>> origin/main

Les lots réparés attendent sur la branche `veille/audit-medical`. Claude les audite médicalement, corrige, puis ouvre et fusionne la PR vers main. Rien n'arrive sur main sans cet audit.

Signature : AAI (Anthropic AI)
