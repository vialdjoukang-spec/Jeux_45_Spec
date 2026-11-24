"""Régénère projets/45spec/PROGRESSION_A.md : groupe A de RANG_RENDEMENT.json, périmètre de l'agent A (0 token). AAI (Anthropic AI)"""
import os, json, glob
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RG = json.load(open(os.path.join(R, "content", "pathologies", "RANG_RENDEMENT.json"), encoding="utf-8"))["pathologies"]
AUTRES = set()  # 24.11.2026 14:27 : agent A seul producteur, tout le groupe A
A2 = set()  # agent A2 arrêté le 24.11.2026
ok = lambda k, v: all(os.path.exists(os.path.join(R, "content", d, v["codes"][0], k + ".json")) for d in ("notions", "questions", "corrections"))
L = sorted((v["rang"], k, v) for k, v in RG.items() if v.get("groupe") == "A")
lig = ["# Progression 45 Spec — groupe A (agent A)", "",
       "Production sans API, branche `agent/45spec-A`, ordre du champ « rang » de `content/pathologies/RANG_RENDEMENT.json`.",
       f"Hors périmètre : première spécialité dans {sorted(AUTRES)} (autres agents) ou {sorted(A2)} (agent A2).", "",
       "| Rang | Id | Pathologie | Spéc. | Statut |", "|---|---|---|---|---|"]
n = p = 0
for r, k, v in L:
    s = v["codes"][0]
    if s in AUTRES or s in A2: continue
    n += 1; f = ok(k, v); p += f
    lig.append(f"| {r} | `{k}` | {v['nom']} | {s} | {'produite' if f else '—'} |")
lig[3:3] = [f"**{p} / {n} pathologies du périmètre produites.**", ""]
open(os.path.join(R, "projets", "45spec", "PROGRESSION_A.md"), "w", encoding="utf-8").write("\n".join(lig + ["", "Signature : AAI (Anthropic AI)", ""]))
print(p, "/", n)
