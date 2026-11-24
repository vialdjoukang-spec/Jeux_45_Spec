"""Constructeur agent (sans API) : forme compacte -> 3 fichiers au format exact de produire_notions_questions.py. AAI (Anthropic AI)"""
import sys, os, json, datetime as dt, importlib.util, collections
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); sys.path.insert(0, R + "/scripts")
import produire_notions_questions as P
IDX = {c["id"]: c for sp in os.environ.get("SPECS", "INF").split(",") for c in P.canoniques(sp)}   # SPECS=URO,HEM,… (agent multi-spécialités)
MOD = "claude-opus-5-5"

def nodes(L):
    return [{"id": a, "parent": b, "t": t, "i": i, "pec": p, "notion": n} for a, b, t, i, p, n in L]

def pec(cle, titre, but, accueil, ph, nph, tr, urg, hu, prono, suivi, sortie, prev):
    E = lambda x: None if x is None else {"mesuresGenerales": x[0], "etapes": [{"temps": a, "qui": b, "fait": c} for a, b, c in x[1]]}
    return {"cle": cle, "titre": titre, "but": but,
            "moyens": {"accueil": accueil, "pharmacologique": [{"molecule": a, "posologie": b, "pourquoi": c, "source": d} for a, b, c, d in ph],
                       "nonPharmacologique": [{"categorie": a, "mesure": b, "pourquoi": c} for a, b, c in nph],
                       "transversal": [{"discipline": a, "apport": b} for a, b in tr]},
            "conduite": {"urgence": E(urg), "horsUrgence": E(hu)}, "pronostic": prono,
            "surveillance": {"suivi": [{"quoi": a, "quand": b, "cible": c} for a, b, c in suivi], "sortie": sortie},
            "prevention": {"primaire": prev[0], "secondaire": prev[1], "tertiaire": prev[2]}}

def cel(x):
    return [{"t": a, "i": b} for a, b in x] if isinstance(x, list) else x

def menus_longs_hors_format(qs):
    """Contrôle 0 token : un menu long garde 1 à 3 réponses justes (le jeu l'annonce au joueur)."""
    return [f"{q['id']} : un menu long exige 1 à 3 réponses justes ({k} trouvées)"
            for q in qs if q["format"] == "MenuLong" and not 1 <= (k := sum(o["correct"] for o in q["options"])) <= 3]


def build(path):
    spec = importlib.util.spec_from_file_location("m", path); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    c = IDX[m.ID]
    dn = {"plan": getattr(m, "PLAN", "monographique"),
          "notions": [{"id": f"N{i+1:02d}", "rubrique": r, "nature": na, "enonce": e, "poids": p, "suisse": bool(s), "source": so}
                      for i, (r, na, p, s, so, e) in enumerate(m.N)], "anglesMorts": m.AM}
    qs = []
    for i, q in enumerate(m.Q):
        f = q["f"]; o = q["o"]
        qs.append({"id": f"Q{i+1:02d}", "format": f, "situation": "starting_point" if q.get("m", 1) else "monographique",
                   "diagnosticMasque": bool(q.get("m", 1)),
                   "serie": None if not q.get("s") else {"id": q["s"][0], "etape": q["s"][1], "total": q["s"][2]},
                   "stem": q["st"], "prompt": q["p"],
                   "options": [] if f == "Kprim" else [{"key": chr(65 + k), "text": t, "correct": bool(v), "why": w} for k, (v, t, w) in enumerate(o)],
                   "statements": [{"text": t, "true": bool(v), "why": w} for v, t, w in o] if f == "Kprim" else [],
                   "notions": [f"N{n:02d}" for n in q["n"]], "angle": q["a"], "difficulte": q["d"],
                   "ladder": dict(zip(("zeroD", "mechanism", "semiology", "discriminant", "decision", "trap", "anchor"), q["l"])),
                   "sources": q["src"] if isinstance(q["src"], list) else [q["src"]]})
    dq = {"questions": qs}
    C = m.C
    dc = {"theme": C["theme"],
          "notions": [{"id": f"c{i+1}", "titre": x["titre"], "rubriques": x["rub"], "comment": x["comment"],
                       "tableau": None if not x.get("tab") else {"colonnes": x["tab"][0], "lignes": [[cel(v) for v in l] for l in x["tab"][1]]},
                       "arbre": nodes(x["arbre"]) if x.get("arbre") else None, "points": x["points"], "sources": x["sources"]}
                      for i, x in enumerate(C["notions"])],
          "ssp": {"code": C["ssp"][0], "nom": C["ssp"][1], "officiel": C["ssp"][2], "algorithme": nodes(C["ssp"][3])},
          "priseEnCharge": C["pec"]}
    errs = {}
    for etape, d in (("notions", dn), ("correction", dc)):
        errs[etape] = P.valider(etape, d, c)
    # questions : valider() relit le fichier de notions -> écrire notions d'abord
    ecrire("notions", c, dn, errs["notions"])
    errs["questions"] = P.valider("questions", dq, c)
    errs["questions"] += menus_longs_hors_format(qs)   # le jeu annonce « menu long : une à trois réponses »
    # couverture (même règle que couverture_notions.py, avant audit)
    par = collections.defaultdict(list)
    for q in qs:
        for n in q["notions"]: par[n].append((q["id"], q["angle"]))
    faibles = []
    for n in dn["notions"]:
        L = par.get(n["id"], []); ang = {a for _, a in L}
        assez = bool(L) if n["poids"] == 1 else (len(L) >= 2 and len(ang) >= 2)
        n["couverture"] = {"questions": [i for i, _ in L], "cochee": False, "enAttente": assez}
        if not assez: faibles.append(n["id"])
    ecrire("notions", c, dn, errs["notions"], keep=True)
    ecrire("questions", c, dq, errs["questions"]); ecrire("correction", c, dc, errs["correction"])
    fm = collections.Counter(q["format"] for q in qs); pw = collections.Counter(n["poids"] for n in dn["notions"])
    print(m.ID, "| N", len(dn["notions"]), dict(pw), "| Q", len(qs), dict(fm), "| non couvertes", faibles, "| err", {k: v for k, v in errs.items() if v})
    return errs, faibles

def ecrire(etape, c, d, err, keep=False):
    p = P.chemin(etape, c); os.makedirs(os.path.dirname(p), exist_ok=True)
    if etape == "notions" and not keep:
        for n in d["notions"]: n["couverture"] = {"questions": [], "cochee": False}
    out = {"id": c["id"], "portes": c.get("portes", []), "entite": c["entite"]["nom"], "cim10": c["entite"].get("cim10"), "ssp": c["ssp"],
           "specialites": c["codes"], "circuit": c["circuit"], **d, "controles": {"erreurs": err},
           "usage": {"_mode": "agent_sans_api", "note": "Produit directement par l'agent Claude, sans appel à l'API Anthropic."},
           "signature": {"date": dt.datetime.now().isoformat(timespec="seconds"), "modele": MOD, "auteur": "AAI (Anthropic AI)"},
           "audit": {"rejector": None, "claude": None}}
    json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    for a in sys.argv[1:]: build(a)
