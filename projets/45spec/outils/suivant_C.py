# Pathologies suivantes du groupe C, non produites, dans l'ordre du rang à partir d'un rang donné, puis retour au début (0 token) : suivant_C.py [n] [rang_depart] (AAI)
import sys, os, json, glob
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
n = int(sys.argv[1]) if len(sys.argv) > 1 else 3; dep = int(sys.argv[2]) if len(sys.argv) > 2 else 1722
RG = json.load(open(R + "/content/pathologies/RANG_RENDEMENT.json", encoding="utf-8"))["pathologies"]
L = sorted((v["rang"], k, v) for k, v in RG.items() if v["groupe"] == "C")
L = [x for x in L if x[0] >= dep] + [x for x in L if x[0] < dep]
ok = lambda k: all(glob.glob(f"{R}/content/{e}/*/{k}.json") for e in ("notions", "questions", "corrections"))
T = [x for x in L if not ok(x[1])]
print("restantes", len(T), "/", len(L))
for r, k, v in T[:n]: print(r, k, v["codes"][0], "|", v["nom"])
