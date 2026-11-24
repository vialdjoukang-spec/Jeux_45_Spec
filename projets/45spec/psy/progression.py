"""Régénère projets/45spec/PROGRESSION_PSY.md depuis le disque (0 token). AAI (Anthropic AI)"""
import os, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import P, R
RG = json.load(open(os.path.join(R, "content", "pathologies", "RANG_RENDEMENT.json"), encoding="utf-8"))["pathologies"]
cs = {c["id"]: c for c in P.canoniques("PSY")}
ORDRE = sorted(cs, key=lambda i: (RG.get(i, {}).get("rang", 10 ** 6), cs[i]["freq"], i))
reste = [i for i in cs if i not in ORDRE]
L = ["# Progression PSY — MedSuisse Arena 45 (production par agent, sans API)", "",
     f"Pathologies canoniques PSY (canoniques() avec fusions) : {len(cs)}. Ordre : champ « rang » de content/pathologies/RANG_RENDEMENT.json (groupes de rendement A → B → C → D).", "",
     "| # | Rang | Groupe | Id | Pathologie | Notions | Questions | Correction |", "|---|---|---|---|---|---|---|---|"]
fait = 0
for k, i in enumerate(ORDRE + reste, 1):
    c = cs[i]; st = []
    for e in ("notions", "questions", "correction"):
        p = P.chemin(e, c)
        if os.path.exists(p):
            d = json.load(open(p, encoding="utf-8"))
            st.append(str(len(d.get("notions") or d.get("questions") or [])) if e != "correction" else "oui")
        else: st.append("—")
    fait += st[2] == "oui"
    g = RG.get(i, {}); L.append(f"| {k} | {g.get('rang', '—')} | {g.get('groupe', '—')} | {i} | {c['entite']['nom'][:70]} | {' | '.join(st)} |")
L[2] += f" Produites : {fait}/{len(cs)}."
L += ["", "Outil : `python projets/45spec/psy/lib.py <id>` (valider() du script + contrôles de Vial : formats, proportions, couverture, lieux interdits).", "", "Signature : AAI (Anthropic AI)"]
F = os.path.join(R, "projets", "45spec", "PROGRESSION_PSY.md")
old = open(F, encoding="utf-8").read() if os.path.exists(F) else ""
if "## Doutes" in old: L = L[:-1] + ["## Doutes" + old.split("## Doutes", 1)[1].rstrip("\n").rsplit("Signature : AAI (Anthropic AI)", 1)[0].rstrip(), "", "Signature : AAI (Anthropic AI)"]
open(F, "w", encoding="utf-8").write("\n".join(L) + "\n")
print(fait, "produites")
