"""Régénère projets/45spec/PROGRESSION_PSY.md depuis le disque (0 token). AAI (Anthropic AI)"""
import os, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import P, R
ORDRE = """F32.1__G4-E01 F10.4__F1_15-E09 F41.1__G1-E03 F43.1__O6_3-E05 F41.0__S2_1-E07 F50.0__F1_8-E03 F23.9__O2_2-E14 F30.1_1__O6_8-E14
F10.2__S9_13-E02 F03__S9_3-E02 F53.1__O1_2-E15 F42.2__S9_10-E01 F43.2__O5_5-E01 F32.3__S9_5-E12 F60.3__O6_8-E07 F05.9_syndrome_confusionne__F1_9-E13
F20.9__S9_3-E07 F44.4_trouble_neurologique__O7_8-E04 F45.1__O7_8-E01 F51.0__G11-E01 F13.2__S9_13-E04 F31.3__O6_8-E05 F06.1__S9_3-E14 F40.1__S9_7-E04 F50.2__O2_6-E05""".split()
cs = {c["id"]: c for c in P.canoniques("PSY")}
reste = [i for i in cs if i not in ORDRE]
L = ["# Progression PSY — MedSuisse Arena 45 (production par agent, sans API)", "",
     f"Pathologies canoniques PSY (canoniques() avec fusions) : {len(cs)}. Ordre : importance pour l'examen fédéral, puis ordre du script.", "",
     "| # | Id | Pathologie | Notions | Questions | Correction |", "|---|---|---|---|---|---|"]
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
    L.append(f"| {k} | {i} | {c['entite']['nom'][:70]} | {' | '.join(st)} |")
L[2] += f" Produites : {fait}/{len(cs)}."
L += ["", "Outil : `python projets/45spec/psy/lib.py <id>` (valider() du script + contrôles de Vial : formats, proportions, couverture, lieux interdits).", "", "Signature : AAI (Anthropic AI)"]
F = os.path.join(R, "projets", "45spec", "PROGRESSION_PSY.md")
old = open(F, encoding="utf-8").read() if os.path.exists(F) else ""
if "## Doutes" in old: L = L[:-1] + ["## Doutes" + old.split("## Doutes", 1)[1].rstrip("\n").rsplit("Signature : AAI (Anthropic AI)", 1)[0].rstrip(), "", "Signature : AAI (Anthropic AI)"]
open(F, "w", encoding="utf-8").write("\n".join(L) + "\n")
print(fait, "produites")
