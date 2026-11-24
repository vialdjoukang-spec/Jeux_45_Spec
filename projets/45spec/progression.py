"""Régénère projets/45spec/PROGRESSION_<SPEC>.md depuis canoniques() et les fichiers présents (0 token). AAI (Anthropic AI)"""
import sys, os, json
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, R + "/scripts")
import produire_notions_questions as P
S = (sys.argv[1] if len(sys.argv) > 1 else "INF").upper()
L = P.canoniques(S); ok = lambda c: all(os.path.exists(P.chemin(e, c)) for e in ("notions", "questions", "correction"))
F = os.path.join(R, "content", "pathologies", f"fusions_{S}.json")
ng = len(json.load(open(F, encoding="utf-8"))["groupes"]) if os.path.exists(F) else 0
lig = [f"# Progression 45 Spec — {S}", "",
       f"Production par l'agent Claude sans appel API (format exact de `scripts/produire_notions_questions.py`), branche `agent/45spec-{S}`.", "",
       f"**{sum(map(ok, L))} / {len(L)} pathologies canoniques produites** (notions + questions + correction), ordre du script (fréquence puis identifiant).", "",
       f"Fusions : {ng} groupes dans `content/pathologies/fusions_{S}.json` ; doublons déjà produits archivés dans `projets/45spec/archives_fusion/{S}`.", "",
       "Statut d'audit : en attente (`audit.rejector = null`). Les chiffres incertains portent la mention « à vérifier » dans le champ source.", "",
       "| # | Id | Pathologie | Statut |", "|---|---|---|---|"]
lig += [f"| {i} | `{c['id']}` | {c['entite']['nom']} | {'produite' if ok(c) else '—'} |" for i, c in enumerate(L, 1)]
open(os.path.join(R, "projets", "45spec", f"PROGRESSION_{S}.md"), "w", encoding="utf-8").write("\n".join(lig + ["", "Signature : AAI (Anthropic AI)", ""]))
print(sum(map(ok, L)), "/", len(L))
