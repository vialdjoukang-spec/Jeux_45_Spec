#!/bin/bash
# Reporte une copie relue d'un arbre isolé vers la branche de travail (AAI) : integre_C.sh <worktree> <compact.py relatif> "<libellé>"
set -u
W="$1"; C="$2"; L="$3"; P=/home/user/Jeux_45_Spec
cd "$W" || exit 1
c=$(python3 projets/45spec/couverture_compacte.py "$C"); [ -z "$c" ] || { echo "ARRÊT couverture : $c"; exit 1; }
l=$(PYTHONPATH=projets/45spec python3 projets/45spec/constructeur_agent_45spec.py "$C" | tail -1); echo "$l"
echo "$l" | grep -q 'non couvertes \[\] | err {}$' || { echo "ARRÊT constructeur"; exit 1; }
git add "$C" content/notions content/questions content/corrections && git commit -q -m "45 Spec groupe C, en cours (non fusionné) : $L, relue

Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01JErHPp63XmLeYp7iwrHcDK" || exit 1
git -C "$P" cherry-pick "$(git rev-parse HEAD)" >/dev/null && git -C "$P" push -q origin agent/45spec-C-suite && echo "reportée : $L"
