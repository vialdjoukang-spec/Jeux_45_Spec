# Barre de progression du groupe C pour le chat (0 token) : barre_C.py [largeur] (AAI)
import sys, os, json, glob
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
w = int(sys.argv[1]) if len(sys.argv) > 1 else 40
RG = json.load(open(R + "/content/pathologies/RANG_RENDEMENT.json", encoding="utf-8"))["pathologies"]
L = [k for k, v in RG.items() if v["groupe"] == "C"]
f = sum(1 for k in L if all(glob.glob(f"{R}/content/{e}/*/{k}.json") for e in ("notions", "questions", "corrections")))
n = round(w * f / len(L))
print(f"Groupe C  [{'█' * n}{'░' * (w - n)}]  {f} / {len(L)}  ({100 * f / len(L):.1f} %)  ·  QCM {f * 20} / {len(L) * 20}")
