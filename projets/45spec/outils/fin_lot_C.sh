#!/bin/bash
# Fin de lot du groupe C (AAI). Travaille dans un arbre de fusion séparé et propre : seuls les fichiers COMMITTÉS sur la branche comptent,
# les fichiers en cours d'écriture dans l'arbre principal n'entrent ni dans les contrôles ni dans main.
# Usage (depuis l'arbre principal, lot relu et committé) : fin_lot_C.sh "<message>" <compact1.py> [<compact2.py> ...]   — jamais de push forcé.
set -u
P=$(git rev-parse --show-toplevel); B=agent/45spec-C-suite; F=${FUSION:-/home/user/.fusion_45spec_C}
[ "$(git -C "$P" branch --show-current)" = "$B" ] || { echo "ARRÊT : branche courante $(git -C "$P" branch --show-current)"; exit 1; }
msg="$1"; shift
git -C "$P" push -q -u origin "$B" || { echo "ARRÊT : push de la branche refusé"; exit 3; }
[ -d "$F" ] || git -C "$P" worktree add -q --detach "$F" "$B" || exit 1
cd "$F" && git fetch -q origin "$B" main && git checkout -q --detach "origin/$B" && git merge -q --no-edit origin/main || { echo "ARRÊT : fusion de main dans la branche"; exit 1; }
for f in "$@"; do
  c=$(python3 projets/45spec/couverture_compacte.py "$f"); [ -z "$c" ] || { echo "ARRÊT couverture $f : $c"; exit 1; }
  l=$(PYTHONPATH=projets/45spec python3 projets/45spec/constructeur_agent_45spec.py "$f" | tail -1); echo "$l"
  echo "$l" | grep -q 'non couvertes \[\] | err {}$' || { echo "ARRÊT constructeur $f"; exit 1; }
  n=$(grep -o '"d":[45]' "$f" | wc -l); [ "$n" -ge 5 ] || { echo "ARRÊT : $f n'a que $n questions d 4-5"; exit 1; }
done
out=$(bash projets/45spec/outils/controles45.sh . 2>&1); echo "$out" | grep -v '^127.0.0.1' | tail -5
if echo "$out" | grep -q "fautifs" || ! echo "$out" | grep -q "^erreurs: 0"; then echo "CONTRÔLES ROUGES : pas de fusion sur main"; exit 2; fi
SP=$(sed -n '1p' projets/45spec/PROGRESSION_C.md | sed 's/.*groupe C ; //; s/)$//; s/, /,/g')
python3 projets/45spec/progression_groupe.py C C "$SP"
git add -A projets/45spec content conception; git diff --cached --quiet || git commit -q -m "$msg" || { echo "ARRÊT : commit"; exit 1; }
ok=0
for i in 1 2 3 4; do
  git push -q origin "HEAD:refs/heads/$B" "HEAD:refs/heads/main" && { ok=1; break; }
  sleep $((2**i)); git fetch -q origin main && git merge -q --no-edit origin/main || break
done
[ "$ok" = 1 ] || { echo "ARRÊT : push sur main ou sur la branche refusé"; exit 4; }
git -C "$P" pull -q --ff-only origin "$B" || echo "ATTENTION : l'arbre principal n'a pas pu avancer en fast-forward"
python3 projets/45spec/outils/barre_C.py 30
echo "LOT FUSIONNÉ SUR MAIN : $(git log --oneline -1 | cut -c1-100)"
