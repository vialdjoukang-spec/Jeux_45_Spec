#!/bin/bash
# Contrôles avant fusion 45 Spec (AAI). Usage : controles45.sh <racine>
cd "$1" || exit 1
t=0; for s in $(ls content/questions); do [ -d content/questions/$s ] || continue; r=$(python projets/45spec/controle_menus_longs.py $s 2>&1 | tail -1); echo "$s $r" | grep -v "fautifs : 0 | erreurs valider() : 0" ; done
python scripts/classer_rendement.py | tail -2
python .claude/skills/optimisation-par-cache-hache-autorun/scripts/cache_hache.py -n arene45 -i 'content/**/*.json' -i conception/outils/arene45/construire_arene45.py -o conception/prototypes/arene45/decks -- python conception/outils/arene45/construire_arene45.py | tail -2
python3 projets/45spec/outils/test_arene.py "$1" | tail -3
