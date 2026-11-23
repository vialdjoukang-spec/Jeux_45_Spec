"""Contrôle des interprétations corrélées des courbes (0 token) : chaque fenêtre et chacun de ses scénarios ont une entrée complète.
Sortie : liste des manques ; code 1 si une entrée existante est incomplète ou mal formée. Signature : AAI (Anthropic AI)"""
import json, os, re, sys
RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MOT = os.path.join(RAC, "conception", "prototypes", "moteur")
s = open(os.path.join(MOT, "fenetres.js"), encoding="utf-8").read()
parts = re.split(r"(?:^|[\n,{]) ?([a-z_0-9]+)\(C\)\{", s)
SC = {}
for k in range(1, len(parts), 2):
    m = re.search(r"boutons\(C,\[\[(.*?)\]\],", parts[k + 1], re.S)
    SC[parts[k]] = re.findall(r"\['([^']+)',", "[[" + m.group(1) + "]]") if m else ["_"]
SC.pop("inconnu", None); SC.pop("panneau", None)
I = json.load(open(os.path.join(MOT, "interpretations.json"), encoding="utf-8"))
manque, faute = [], []
for f, scs in SC.items():
    for sc in scs:
        e = (I.get(f) or {}).get(sc)
        if not e:
            manque.append(f"{f} / {sc}"); continue
        for c in ("physio", "semio", "explo", "ther"):
            if not isinstance(e.get(c), str) or len(e[c]) < 40:
                faute.append(f"{f} / {sc} : champ {c} absent ou trop court")
        if not e.get("def"):
            faute.append(f"{f} / {sc} : aucune définition")
tot = sum(len(v) for v in SC.values())
print(f"interprétations : {tot - len(manque)} / {tot} entrées ; {len(faute)} défaut(s)")
for x in faute[:30]: print(" 🟥", x)
if "--manques" in sys.argv: print("\n".join(" · " + x for x in manque))
sys.exit(1 if faute else 0)
