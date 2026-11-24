#!/usr/bin/env bash
# Contrôles de l'audit médical (étape 2 de AUDIT_MEDICAL_CLAUDE.md), enveloppés par le cache haché :
# un contrôle dont les entrées, le script et les sorties n'ont pas bougé est sauté ; un échec n'est jamais mis en cache.
# non_perte.py n'est pas mis en cache : il compare à origin/main, état extérieur au dépôt local.
# Usage : bash projets/outils/controles_caches.sh [--forcer]      Signature : AAI (Anthropic AI)
set -e
cd "$(git rev-parse --show-toplevel)"
C="python3 .claude/skills/optimisation-par-cache-hache-autorun/scripts/cache_hache.py $1"
$C --nom audit_fond -i 'conception/donnees/paraclinique/topographie/**/*.json' -i projets/outils/audit_fond.py \
   -o SORTIES_DONNEES_FIABLES -- python3 projets/outils/audit_fond.py
$C --nom lots_complement -i 'SORTIES_DONNEES_FIABLES/**/*.json' -i projets/outils/lots_complement.py \
   -o Production_XAi/Lots_a_produire/complement_presentation -- python3 projets/outils/lots_complement.py
$C --nom auditer_conception -i 'conception/donnees/**/*.json' -i 'conception/prototypes/moteur/*' -i 'conception/html/*.html' \
   -i 'conception/plans/*.plan.json' -i 'conception/outils/*.py' -o conception/audit/conception.md -- python3 conception/outils/auditer_conception.py
$C --nom auditer_couverture -i 'conception/outils/*.py' -i 'conception/prototypes/moteur/*.json' \
   -o conception/audit/couverture.md -o conception/audit/couverture.json -- python3 conception/outils/auditer_couverture.py
python3 projets/outils/non_perte.py origin/main | tail -3
