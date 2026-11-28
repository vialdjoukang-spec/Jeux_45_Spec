"""Mesure exacte des clichés manquants de l'Imagerie de Paraclinique (0 token, sans réseau).
Lit le réseau construit (conception/prototypes/paraclinique/donnees/reseau_imagerie.json, à régénérer d'abord par
construire_jeu_paraclinique.py) et la topographie ; écrit ETAT_CLICHES.json à côté de ce script.
Unité de travail : (organe, pathologie, modalité) — un dossier d'atlas sert tous les examens de cette modalité.
Usage : python3 projets/2_Jeux_Paraclinique/imagerie_cliches/mesurer_cliches.py   Signature : AAI (Anthropic AI)"""
import json, os, re, glob, unicodedata, datetime, collections
ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
P = os.path.join(RAC, "conception", "donnees", "paraclinique")
sa = lambda s: "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")
cle = lambda s: re.sub(r"[^a-z0-9]+", "_", sa(s))[:48].strip("_")
R = json.load(open(os.path.join(RAC, "conception/prototypes/paraclinique/donnees/reseau_imagerie.json"), encoding="utf-8"))
N = {x["id"]: x for x in R["noeuds"]}
EX = {}
for f in glob.glob(os.path.join(P, "topographie", "*", "*.json")):
    d = json.load(open(f, encoding="utf-8"))
    for e in d.get("examens", []):
        EX[e["id"]] = (os.path.basename(os.path.dirname(f)), os.path.basename(f)[:-5], e)
LIENS = {f[:-5]: json.load(open(os.path.join(P, "atlas_liens", f), encoding="utf-8")) for f in os.listdir(os.path.join(P, "atlas_liens"))}

def remonte(x, nature):
    while x and x["nature"] != nature:
        x = N.get((x.get("de") or [None])[0])
    return x

U = collections.OrderedDict()
for x in R["noeuds"]:
    if x["nature"] != "Pathologie":
        continue
    reg, stem, e = EX[x["exRef"]]
    suf = x["id"].rsplit("__", 1)[1]
    p = next((q["pathologie"] for q in e.get("pathologiesAssociees", []) if cle(q["pathologie"])[:30] == suf), None)
    mod = remonte(x, "Modalité")["texte"]
    k = (stem, p, mod)
    u = U.setdefault(k, {"organe": stem, "region": reg, "pathologie": p, "modalite": mod, "examens": [], "noeuds": 0,
                         "lien": LIENS.get(stem, {}).get(p), "patho": False, "normal": False})
    u["noeuds"] += 1; u["examens"].append(e["nom"])
    if x.get("cliches"):
        u["patho"] = True; u["normal"] = bool(x["cliches"].get("normal"))
for u in U.values():
    u["examens"] = sorted(set(u["examens"]))
    u["etat"] = "complet" if u["patho"] and u["normal"] else ("normal manquant" if u["patho"] else "patho manquant")
L = list(U.values())
nd = collections.Counter(); ud = collections.Counter()
for x in R["noeuds"]:
    if x["nature"] == "Pathologie":
        nd["total"] += 1; nd["patho_manquant"] += bool(x.get("clichesAProduire")); nd["normal_manquant"] += bool(x.get("cliches") and not x["cliches"].get("normal"))
for u in L:
    ud[u["etat"]] += 1
etat = {"_meta": {"role": "État mesuré des clichés de l'Imagerie (couloir 3, branche paraclinique-imagerie-cliches).", "mesure_le": datetime.date.today().isoformat(),
                  "script": "projets/2_Jeux_Paraclinique/imagerie_cliches/mesurer_cliches.py", "signature": "AAI (Anthropic AI)"},
        "noeuds_pathologie": dict(nd), "unites_organe_pathologie_modalite": {"total": len(L), **dict(ud)},
        "par_modalite": {m: dict(collections.Counter(u["etat"] for u in L if u["modalite"] == m)) for m in sorted({u["modalite"] for u in L})},
        "unites": L}
json.dump(etat, open(os.path.join(ICI, "ETAT_CLICHES.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps({k: etat[k] for k in ("noeuds_pathologie", "unites_organe_pathologie_modalite", "par_modalite")}, ensure_ascii=False, indent=1))
