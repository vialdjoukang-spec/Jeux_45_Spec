"""COUCHE 2 — Cartes réflexes générées par script, à 0 token, à partir des fiches de raisonnement.

Chaque fiche produit une vingtaine de cartes courtes (5 à 15 s) qui entraînent l'instantanéité :
  PREMIER_GESTE · ORDONNER · DRAPEAU_ACTION · DISCRIMINANT · CHIFFRE · MECANISME · PREMIER_EXAMEN
La correction de chaque carte reprend le « pourquoi » de la fiche et son échelle 0-D → ancre.
Une carte n'est jouable que si sa fiche a reçu audit.rejector = "pass" (option --tout pour ignorer ce filtre en test).

Usage : python scripts/generer_reflexes.py [--tout]
Sortie : content/reflexes/<SPEC>/<entite>.json
"""
import argparse, glob, json, os, random

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHES = os.path.join(RACINE, "content", "fiches")
SORTIE = os.path.join(RACINE, "content", "reflexes")
CODES = {k: v["code"] for k, v in json.load(open(os.path.join(RACINE, "data", "references", "entite_specialites.json"), encoding="utf-8"))["specialites"].items()}


def options(bonne, fausses, rng, n=4):
    pool = [f for f in dict.fromkeys(fausses) if f and f != bonne]
    rng.shuffle(pool)
    opts = [bonne] + pool[: n - 1]
    rng.shuffle(opts)
    return opts if len(opts) >= 3 else None


def cartes(f, voisins, rng):
    nom, L = f["entite"], f["ladder"]
    corr = {"ancre": L["anchor"], "zeroD": L["zeroD"], "mecanisme": L["mechanism"]}
    out = []
    g = f["premiersGestes"]
    autres_gestes = [x["premiersGestes"][0]["action"] for x in voisins if x.get("premiersGestes")]
    o = options(g[0]["action"], [x["action"] for x in g[1:]] + autres_gestes, rng)
    if o:
        out.append({"type": "PREMIER_GESTE", "temps_s": 10, "question": f"Devant « {nom} », que faites-vous EN PREMIER ?",
                    "options": o, "reponse": g[0]["action"], "pourquoi": g[0]["pourquoi"],
                    "piege": "Un geste juste mais placé trop tôt ou trop tard reste une erreur de chronologie.", **corr})
    if len(g) >= 3:
        melange = g[:]; rng.shuffle(melange)
        out.append({"type": "ORDONNER", "temps_s": 20, "question": f"Remettez dans l'ordre la conduite devant « {nom} ».",
                    "elements": [x["action"] for x in melange], "reponse": [x["action"] for x in g],
                    "pourquoi": " ".join(f"{x['ordre']}. {x['pourquoi']}" for x in g), **corr})
    toutes_actions = [d["action"] for d in f["drapeauxRouges"]] + [d["action"] for v in voisins for d in v.get("drapeauxRouges", [])]
    for d in f["drapeauxRouges"]:
        o = options(d["action"], toutes_actions, rng)
        if o:
            out.append({"type": "DRAPEAU_ACTION", "temps_s": 8, "question": f"« {d['signe']} » chez un patient suspect de « {nom} » : que faites-vous ?",
                        "options": o, "reponse": d["action"], "pourquoi": d["signification"], **corr})
    elems = [x["elementQuiTranche"] for x in f["discriminants"]] + [x["elementQuiTranche"] for v in voisins for x in v.get("discriminants", [])]
    for x in f["discriminants"]:
        o = options(x["elementQuiTranche"], elems, rng)
        if o:
            out.append({"type": "DISCRIMINANT", "temps_s": 12, "question": f"Quel élément sépare « {nom} » de « {x['rival']} » ?",
                        "options": o, "reponse": x["elementQuiTranche"], "pourquoi": L["discriminant"], **corr})
    sigs = [c["signification"] for c in f["chiffresCles"]]
    for c in f["chiffresCles"]:
        o = options(c["signification"], sigs + [c2["signification"] for v in voisins for c2 in v.get("chiffresCles", [])], rng)
        if o:
            out.append({"type": "CHIFFRE", "temps_s": 8, "question": f"« {c['valeur']} » dans « {nom} » : que signifie ce chiffre ?",
                        "options": o, "reponse": c["signification"], "source": c["source"], **corr})
    meca = [p["mecanisme"] for p in f["presentation"]["typique"]]
    for p in f["presentation"]["typique"]:
        o = options(p["mecanisme"], meca + [q["mecanisme"] for v in voisins for q in v.get("presentation", {}).get("typique", [])], rng)
        if o:
            out.append({"type": "MECANISME", "temps_s": 12, "question": f"Pourquoi observe-t-on « {p['element']} » dans « {nom} » ?",
                        "options": o, "reponse": p["mecanisme"], "pourquoi": L["semiology"], **corr})
    ex = sorted(f["examens"], key=lambda e: e["ordre"])
    if len(ex) >= 2:
        o = options(ex[0]["examen"], [e["examen"] for e in ex[1:]] + [v["examens"][0]["examen"] for v in voisins if v.get("examens")], rng)
        if o:
            out.append({"type": "PREMIER_EXAMEN", "temps_s": 10, "question": f"Devant « {nom} », quel examen demandez-vous en premier ?",
                        "options": o, "reponse": ex[0]["examen"], "pourquoi": ex[0]["pourquoi"], **corr})
    for k, c in enumerate(out, 1):
        c.update({"id": f"{f['id']}-R{k:02d}", "entityId": f["id"], "ssp": f["ssp"], "specialtyIds": f.get("specialtyIds", []),
                  "notionRefs": f.get("notionRefs", []), "origine": "script (0 token)"})
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--tout", action="store_true"); a = ap.parse_args()
    fiches = [json.load(open(p, encoding="utf-8")) for p in glob.glob(os.path.join(FICHES, "*", "*.json"))]
    if not a.tout:
        fiches = [f for f in fiches if (f.get("audit") or {}).get("rejector") == "pass"]
    par_ssp = {}
    for f in fiches:
        par_ssp.setdefault(f["ssp"], []).append(f)
    total = 0
    for f in fiches:
        rng = random.Random(f["id"])                                # même graine, mêmes cartes : reproductible
        cs = cartes(f, [v for v in par_ssp[f["ssp"]] if v["id"] != f["id"]], rng)
        dossier = os.path.join(SORTIE, CODES.get((f.get("specialtyIds") or ["?"])[0], "SANS_SPEC")); os.makedirs(dossier, exist_ok=True)
        json.dump({"entite": f["entite"], "cartes": cs}, open(os.path.join(dossier, f"{f['id'].replace('.', '_')}.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        total += len(cs)
    print(f"{len(fiches)} fiche(s) → {total} carte(s) réflexes, 0 token.")


if __name__ == "__main__":
    main()
