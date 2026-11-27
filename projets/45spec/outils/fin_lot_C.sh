#!/bin/bash
# Fin de lot du groupe C (AAI) : contrôles par forme compacte, commit, fusion de main, controles45.sh, push de la branche, fusion sur main seulement si tout est vert.
# Usage : fin_lot_C.sh "<message de commit>" <compact1.py> [<compact2.py> ...]   (jamais de push forcé)
set -u
cd "$(git rev-parse --show-toplevel)" || exit 1
B=agent/45spec-C-suite
[ "$(git branch --show-current)" = "$B" ] || { echo "ARRÊT : branche courante $(git branch --show-current)"; exit 1; }
msg="$1"; shift
for f in "$@"; do
  c=$(python3 projets/45spec/couverture_compacte.py "$f"); [ -z "$c" ] || { echo "ARRÊT couverture $f : $c"; exit 1; }
  l=$(PYTHONPATH=projets/45spec python3 projets/45spec/constructeur_agent_45spec.py "$f" | tail -1); echo "$l"
  echo "$l" | grep -q 'non couvertes \[\] | err {}$' || { echo "ARRÊT constructeur $f"; exit 1; }
  n=$(grep -o '"d":[45]' "$f" | wc -l); [ "$n" -ge 5 ] || { echo "ARRÊT : $f n'a que $n questions d 4-5"; exit 1; }
done
git add -A projets/45spec content conception && git commit -q -m "$msg" || { echo "ARRÊT : commit"; exit 1; }
git pull -q --no-rebase --no-edit origin main || { echo "ARRÊT : fusion de main dans la branche"; exit 1; }
out=$(bash projets/45spec/outils/controles45.sh . 2>&1); echo "$out" | grep -v '^127.0.0.1' | tail -5
if echo "$out" | grep -q "fautifs" || ! echo "$out" | grep -q "^erreurs: 0"; then echo "CONTRÔLES ROUGES : pas de fusion sur main"; git push -q -u origin "$B"; exit 2; fi
SP=$(sed -n '1p' projets/45spec/PROGRESSION_C.md | sed 's/.*groupe C ; //; s/)$//; s/, /,/g')
python3 projets/45spec/progression_groupe.py C C "$SP"
git add -A projets/45spec content conception; git diff --cached --quiet || git commit -q -m "$msg — rang, arène et progression régénérés"
git push -q -u origin "$B" || { echo "ARRÊT : push de la branche refusé"; exit 3; }
for i in 1 2 3 4; do
  git checkout -q main && git pull -q --no-rebase --no-edit origin main && git merge -q --no-edit "$B" && git push -q origin main && { ok=1; break; }
  ok=0; sleep $((2**i))
done
git checkout -q "$B"; [ "$ok" = 1 ] || { echo "ARRÊT : fusion ou push sur main refusé"; exit 4; }
git merge -q --ff-only main; git push -q origin "$B"
echo "LOT FUSIONNÉ SUR MAIN : $(git log --oneline -1 main | cut -c1-90)"
