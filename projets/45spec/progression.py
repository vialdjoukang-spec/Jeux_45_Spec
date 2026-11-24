"""Régénère projets/45spec/PROGRESSION_<SPEC>.md depuis canoniques() et les fichiers présents (0 token). AAI (Anthropic AI)"""
import sys, os, json
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, R + "/scripts")
import produire_notions_questions as P
S = (sys.argv[1] if len(sys.argv) > 1 else "INF").upper()
RG = json.load(open(os.path.join(R, "content", "pathologies", "RANG_RENDEMENT.json"), encoding="utf-8"))["pathologies"]
SUF = {k.split("__")[-1]: v for k, v in RG.items()}       # fusion INF : l'id canonique change ; on reprend le meilleur rang de ses portes d'entrée
def rg(c):
    if c["id"] in RG: return RG[c["id"]]
    m = [SUF[p["entiteId"].replace(".", "_")] for p in c.get("portes", []) if p["entiteId"].replace(".", "_") in SUF]
    return min(m, key=lambda x: x["rang"]) if m else {}
L = sorted(P.canoniques(S), key=lambda c: (rg(c).get("rang", 10 ** 6), c["freq"], c["id"])); ok = lambda c: all(os.path.exists(P.chemin(e, c)) for e in ("notions", "questions", "correction"))
F = os.path.join(R, "content", "pathologies", f"fusions_{S}.json")
ng = len(json.load(open(F, encoding="utf-8"))["groupes"]) if os.path.exists(F) else 0
lig = [f"# Progression 45 Spec — {S}", "",
       f"Production par l'agent Claude sans appel API (format exact de `scripts/produire_notions_questions.py`), branche `agent/45spec-{S}`.", "",
       f"**{sum(map(ok, L))} / {len(L)} pathologies canoniques produites** (notions + questions + correction), ordre de rendement à l'examen (`content/pathologies/RANG_RENDEMENT.json` : groupe A, puis B, C, D ; rang d'une pathologie fusionnée = meilleur rang de ses portes d'entrée).", "",
       f"Fusions : {ng} groupes dans `content/pathologies/fusions_{S}.json` ; doublons déjà produits archivés dans `projets/45spec/archives_fusion/{S}`.", "",
       "Statut d'audit : en attente (`audit.rejector = null`). Les chiffres incertains portent la mention « à vérifier » dans le champ source.", "",
       "| # | Groupe | Rang | Id | Pathologie | Statut |", "|---|---|---|---|---|---|"]
lig += [f"| {i} | {rg(c).get('groupe', '—')} | {rg(c).get('rang', '—')} | `{c['id']}` | {c['entite']['nom']} | {'produite' if ok(c) else '—'} |" for i, c in enumerate(L, 1)]
open(os.path.join(R, "projets", "45spec", f"PROGRESSION_{S}.md"), "w", encoding="utf-8").write("\n".join(lig + ["", "Signature : AAI (Anthropic AI)", ""]))
print(sum(map(ok, L)), "/", len(L))
