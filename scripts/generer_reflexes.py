"""COUCHE 2 — Cartes réflexes générées par script, à 0 token, à partir des fiches de raisonnement.

Chaque fiche produit une vingtaine de cartes courtes (5 à 15 s) qui entraînent l'instantanéité :
  PREMIER_GESTE · ORDONNER · DRAPEAU_ACTION · DISCRIMINANT · CHIFFRE · MECANISME · PREMIER_EXAMEN
Chaque option porte son explication propre (pourquoi elle est juste, ou quelle erreur elle incarne),
calculée depuis la fiche ; la correction se termine par l'échelle 0-D → ancre de la fiche.
Une carte n'est jouable que si sa fiche a reçu audit.rejector = "pass" (option --tout pour ignorer ce filtre en test).

Usage : python scripts/generer_reflexes.py [--tout]
Sortie : content/reflexes/<SPEC>/<entite>.json
"""
import argparse, glob, json, os, random

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FICHES = os.path.join(RACINE, "content", "fiches")
SORTIE = os.path.join(RACINE, "content", "reflexes")
CODES = {k: v["code"] for k, v in json.load(open(os.path.join(RACINE, "data", "references", "entite_specialites.json"), encoding="utf-8"))["specialites"].items()}


def options(bonne, fausses, rng, n=4, why_bonne="", why_faux=None):
    """Retourne des options commentées : chaque option porte « correct » et son « why » propre.
    why_faux : dict texte_faux -> explication (calculée depuis la fiche) ; défaut générique si absent."""
    pool = [f for f in dict.fromkeys(fausses) if f and f != bonne]
    rng.shuffle(pool)
    textes = [bonne] + pool[: n - 1]
    if len(textes) < 3:
        return None
    rng.shuffle(textes)
    why_faux = why_faux or {}
    return [{"text": t, "correct": t == bonne,
             "why": why_bonne if t == bonne else why_faux.get(t, "Cette réponse ne correspond pas à cette entité dans ce contexte.")}
            for t in textes]


def cartes(f, voisins, rng):
    nom, L = f["entite"], f["ladder"]
    corr = {"ancre": L["anchor"], "zeroD": L["zeroD"], "mecanisme": L["mechanism"]}
    out = []
    g = f["premiersGestes"]
    autres = {x["premiersGestes"][0]["action"]: x for x in voisins if x.get("premiersGestes")}
    wf = {x["action"]: f"Ce geste est juste, mais il vient au rang {x['ordre']} et non en premier : {x['pourquoi']}" for x in g[1:]}
    for act, v in autres.items():
        wf.setdefault(act, f"Ce geste vient en premier devant « {v['entite']} », pas ici. "
                      + next((d["elementQuiTranche"] for d in f["discriminants"] if d["rival"].lower() in v["entite"].lower() or v["entite"].lower() in d["rival"].lower()),
                             "Les deux entités se distinguent par leurs discriminants."))
    o = options(g[0]["action"], [x["action"] for x in g[1:]] + list(autres), rng, why_bonne=g[0]["pourquoi"], why_faux=wf)
    if o:
        out.append({"type": "PREMIER_GESTE", "temps_s": 10, "question": f"Devant « {nom} », que faites-vous EN PREMIER ?",
                    "options": o, "pourquoi": g[0]["pourquoi"],
                    "piege": "Un geste juste mais placé trop tôt ou trop tard reste une erreur de chronologie.", **corr})
    if len(g) >= 3:
        melange = g[:]; rng.shuffle(melange)
        out.append({"type": "ORDONNER", "temps_s": 20, "question": f"Remettez dans l'ordre la conduite devant « {nom} ».",
                    "elements": [x["action"] for x in melange], "reponse": [x["action"] for x in g],
                    "pourquoi": " ".join(f"{x['ordre']}. {x['pourquoi']}" for x in g), **corr})
    toutes_actions = [d["action"] for d in f["drapeauxRouges"]] + [d["action"] for v in voisins for d in v.get("drapeauxRouges", [])]
    src = {x["action"]: x for x in f["drapeauxRouges"]}
    for d in f["drapeauxRouges"]:
        wf = {a: (f"Cette action répond à un autre drapeau (« {src[a]['signe']} »), pas à celui-ci." if a in src else "Cette action relève d'une autre entité du SSP.") for a in toutes_actions}
        o = options(d["action"], toutes_actions, rng, why_bonne=d["signification"], why_faux=wf)
        if o:
            out.append({"type": "DRAPEAU_ACTION", "temps_s": 8, "question": f"« {d['signe']} » chez un patient suspect de « {nom} » : que faites-vous ?",
                        "options": o, "pourquoi": d["signification"], **corr})
    elems = [x["elementQuiTranche"] for x in f["discriminants"]] + [x["elementQuiTranche"] for v in voisins for x in v.get("discriminants", [])]
    rival_de = {y["elementQuiTranche"]: y["rival"] for y in f["discriminants"]}
    for x in f["discriminants"]:
        wf = {e: (f"Cet élément sépare « {nom} » de « {rival_de[e]} », et non de « {x['rival']} »." if e in rival_de else "Cet élément concerne une autre paire d'entités.") for e in elems}
        o = options(x["elementQuiTranche"], elems, rng, why_bonne=L["discriminant"], why_faux=wf)
        if o:
            out.append({"type": "DISCRIMINANT", "temps_s": 12, "question": f"Quel élément sépare « {nom} » de « {x['rival']} » ?",
                        "options": o, "pourquoi": L["discriminant"], **corr})
    sigs = [c["signification"] for c in f["chiffresCles"]]
    val_de = {c2["signification"]: c2["valeur"] for c2 in f["chiffresCles"]}
    for c in f["chiffresCles"]:
        autres_sig = sigs + [c2["signification"] for v in voisins for c2 in v.get("chiffresCles", [])]
        wf = {t: (f"Cette signification correspond à la valeur « {val_de[t]} », pas à « {c['valeur']} »." if t in val_de else "Cette signification appartient à une autre entité.") for t in autres_sig}
        o = options(c["signification"], autres_sig, rng, why_bonne=f"{c['signification']} (source : {c['source']})", why_faux=wf)
        if o:
            out.append({"type": "CHIFFRE", "temps_s": 8, "question": f"« {c['valeur']} » dans « {nom} » : que signifie ce chiffre ?",
                        "options": o, "source": c["source"], **corr})
    meca = [p["mecanisme"] for p in f["presentation"]["typique"]]
    elt_de = {q["mecanisme"]: q["element"] for q in f["presentation"]["typique"]}
    for p in f["presentation"]["typique"]:
        autres_m = meca + [q["mecanisme"] for v in voisins for q in v.get("presentation", {}).get("typique", [])]
        wf = {t: (f"Ce mécanisme explique « {elt_de[t]} », pas « {p['element']} »." if t in elt_de else "Ce mécanisme appartient à une autre entité.") for t in autres_m}
        o = options(p["mecanisme"], autres_m, rng, why_bonne=p["mecanisme"], why_faux=wf)
        if o:
            out.append({"type": "MECANISME", "temps_s": 12, "question": f"Pourquoi observe-t-on « {p['element']} » dans « {nom} » ?",
                        "options": o, "pourquoi": L["semiology"], **corr})
    ex = sorted(f["examens"], key=lambda e: e["ordre"])
    if len(ex) >= 2:
        wf = {e["examen"]: f"Cet examen vient au rang {e['ordre']} : {e['pourquoi']}" for e in ex[1:]}
        o = options(ex[0]["examen"], [e["examen"] for e in ex[1:]] + [v["examens"][0]["examen"] for v in voisins if v.get("examens")], rng,
                    why_bonne=ex[0]["pourquoi"], why_faux=wf)
        if o:
            out.append({"type": "PREMIER_EXAMEN", "temps_s": 10, "question": f"Devant « {nom} », quel examen demandez-vous en premier ?",
                        "options": o, "pourquoi": ex[0]["pourquoi"], **corr})
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
