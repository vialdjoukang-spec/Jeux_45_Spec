# Fiche canonique d'une pathologie et voisines déjà produites (0 token) : fiche.py <id> (AAI)
import sys, os, json, glob
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))); sys.path.insert(0, R + "/scripts")
import produire_notions_questions as P
I = {c["id"]: c for c in P.canoniques(None)}
c = I[sys.argv[1]]
print(json.dumps(c, ensure_ascii=False, indent=1))
pre = (c["entite"].get("cim10") or "")[:3]
print("\n== Voisines déjà produites (même CIM-10 à 3 caractères ou même SSP) : prendre un angle non couvert ==")
for f in sorted(glob.glob(R + "/content/corrections/*/*.json")):
    k = os.path.basename(f)[:-5]
    if k == c["id"] or k not in I: continue
    v = I[k]
    if (pre and (v["entite"].get("cim10") or "").startswith(pre)) or v["ssp"] == c["ssp"]:
        print("-", k, "|", os.path.basename(os.path.dirname(f)), "|", v["entite"]["nom"], "|", json.load(open(f, encoding="utf-8")).get("theme", "")[:260])
