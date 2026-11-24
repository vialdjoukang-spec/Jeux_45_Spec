"""Classe les pathologies canoniques du 45 Spec par rendement à l'examen fédéral (0 token).
Score = fréquence (palier 1 = 10 points … palier 5 = 2) + urgence (3) + nombre de SSP qui y mènent (1 par SSP, plafond 6).
Groupes de poids : A = 500 premières, B = 500 suivantes, C = 800 suivantes, D = le reste.
Sortie : content/pathologies/RANG_RENDEMENT.json ; produire_notions_questions.py l'utilise (--groupe A, tri par score)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import produire_notions_questions as P

def score(c):
    return (6 - c["freq"]) * 2 + (3 if c["urgent"] else 0) + min(len(c["portes"]), 6)

cs = sorted(P.canoniques(), key=lambda c: (-score(c), c["freq"], c["id"]))
bornes = [("A", 500), ("B", 1000), ("C", 1800)]
out = {}
for i, c in enumerate(cs):
    g = next((n for n, b in bornes if i < b), "D")
    out[c["id"]] = {"rang": i + 1, "score": score(c), "groupe": g, "nom": c["entite"]["nom"], "codes": c["codes"][:3],
                    "fait": os.path.exists(P.chemin("correction", c))}
res = {"_meta": {"regle": __doc__.strip().splitlines()[1], "total": len(out),
                 "groupes": {g: {"total": sum(1 for v in out.values() if v["groupe"] == g), "faits": sum(1 for v in out.values() if v["groupe"] == g and v["fait"])} for g in "ABCD"}},
       "pathologies": out}
json.dump(res, open(os.path.join(P.R, "content", "pathologies", "RANG_RENDEMENT.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(json.dumps(res["_meta"]["groupes"]))
