"""Écriture sans API des notions, questions et corrections du jeu 45 Spec par un agent Claude.
Même schéma, même valider() et même chemin que scripts/produire_notions_questions.py ; seule la signature change.
Usage : python projets/45spec/agent_ecrire.py <fichier_pathologie.py> [notions|questions|correction|tout]
Le fichier de pathologie définit ID (identifiant canonique), puis NOT (liste N), QS (liste A/K/M) et COR (dict).
Signature : AAI (Anthropic AI)"""
import datetime as dt, json, os, random, runpy, sys

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, "scripts"))
import produire_notions_questions as P  # noqa: E402

MODELE = "claude-opus-5-5 (agent 45spec, production sans API)"
RUB = dict(zip("def epi bas ana exa red gold alt pos acu chr hos pro sur fol".split(), P.RUBRIQUES))


# ---------- notions ----------
def N(rub, nature, poids, suisse, source, enonce):
    return {"rubrique": RUB.get(rub, rub), "nature": nature, "enonce": enonce, "poids": poids, "suisse": bool(suisse), "source": source}


def notions(liste, plan="monographique", angles=()):
    return {"plan": plan, "notions": [{"id": f"N{i:02d}", **n} for i, n in enumerate(liste, 1)], "anglesMorts": list(angles)}


# ---------- questions ----------
def _ids(s):
    return [f"N{int(x):02d}" for x in str(s).split()]


def _lad(l):
    return dict(zip(("zeroD", "mechanism", "semiology", "discriminant", "decision", "trap", "anchor"), l))


def _opts(opts, seed):
    o = list(opts); random.Random(seed).shuffle(o)
    return [{"key": chr(65 + i), "text": t.lstrip("*"), "correct": t.startswith("*"), "why": w} for i, (t, w) in enumerate(o)]


def _q(fmt, stem, prompt, notions, angle, diff, ladder, src, situ, masq, serie, options=(), statements=()):
    return {"format": fmt, "situation": "starting_point" if situ == "s" else "monographique", "diagnosticMasque": masq,
            "serie": None if not serie else {"id": serie[0], "etape": serie[1], "total": serie[2]}, "stem": stem, "prompt": prompt,
            "options": list(options), "statements": list(statements), "notions": _ids(notions), "angle": angle, "difficulte": diff,
            "ladder": _lad(ladder), "sources": [src]}


def A(stem, prompt, opts, notions, angle, diff, ladder, src, situ="s", masq=True, serie=None):
    return _q("A", stem, prompt, notions, angle, diff, ladder, src, situ, masq, serie, options=opts)


def M(stem, prompt, opts, notions, angle, diff, ladder, src, situ="s", masq=True, serie=None):
    return _q("MenuLong", stem, prompt, notions, angle, diff, ladder, src, situ, masq, serie, options=opts)


def K(stem, prompt, stmts, notions, angle, diff, ladder, src, situ="s", masq=True, serie=None):
    return _q("Kprim", stem, prompt, notions, angle, diff, ladder, src, situ, masq, serie,
              statements=[{"text": t, "true": v, "why": w} for t, v, w in stmts])


def questions(qs):
    out = []
    for i, q in enumerate(qs, 1):
        q = {"id": f"Q{i:02d}", **q}
        if q["format"] != "Kprim":
            q["options"] = _opts(q["options"], q["id"] + q["stem"][:20])
        out.append(q)
    return {"questions": out}


# ---------- correction ----------
def nd(id, parent, t, i, pec=None, notion=None):
    return {"id": id, "parent": parent, "t": t, "i": i, "pec": pec, "notion": notion}


def cell(x):
    if isinstance(x, str):
        return x
    if isinstance(x, tuple):
        x = [x]
    return [{"t": t, "i": i} for t, i in x]


def CN(id, titre, rubs, comment, points, sources, tableau=None, arbre=None):
    return {"id": id, "titre": titre, "rubriques": [RUB.get(r, r) for r in rubs.split()], "comment": comment,
            "tableau": None if not tableau else {"colonnes": tableau[0], "lignes": [[cell(c) for c in l] for l in tableau[1]]},
            "arbre": [nd(*x) for x in arbre] if arbre else None, "points": points, "sources": sources}


def _cond(c):
    if not c:
        return None
    mg, et = c
    return {"mesuresGenerales": mg, "etapes": [{"temps": t, "qui": q, "fait": f} for t, q, f in et]}


def PEC(cle, titre, but, accueil, pharma, nonph, trans, urg, hors, pronostic, suivi, sortie, prev):
    return {"cle": cle, "titre": titre, "but": but,
            "moyens": {"accueil": accueil, "pharmacologique": [{"molecule": m, "posologie": p, "pourquoi": w, "source": s} for m, p, w, s in pharma],
                       "nonPharmacologique": [{"categorie": c, "mesure": m, "pourquoi": w} for c, m, w in nonph],
                       "transversal": [{"discipline": d, "apport": a} for d, a in trans]},
            "conduite": {"urgence": _cond(urg), "horsUrgence": _cond(hors)}, "pronostic": pronostic,
            "surveillance": {"suivi": [{"quoi": q, "quand": w, "cible": c} for q, w, c in suivi], "sortie": sortie},
            "prevention": {"primaire": prev[0], "secondaire": prev[1], "tertiaire": prev[2]}}


def correction(theme, cns, ssp, pecs):
    code, nom, officiel, algo = ssp
    return {"theme": theme, "notions": cns, "ssp": {"code": code, "nom": nom, "officiel": officiel, "algorithme": [nd(*x) for x in algo]},
            "priseEnCharge": pecs}


# ---------- écriture ----------
def ecrire(etape, c, d, err):
    p = P.chemin(etape, c); os.makedirs(os.path.dirname(p), exist_ok=True)
    if etape == "notions":
        for n in d["notions"]:
            n["couverture"] = {"questions": [], "cochee": False}
    out = {"id": c["id"], "portes": c.get("portes", []), "entite": c["entite"]["nom"], "cim10": c["entite"].get("cim10"), "ssp": c["ssp"],
           "specialites": c["codes"], "circuit": c["circuit"], **d, "controles": {"erreurs": err},
           "usage": {"_mode": "agent", "api": False},
           "signature": {"date": dt.datetime.now().isoformat(timespec="seconds"), "modele": MODELE, "auteur": "AAI (Anthropic AI)"},
           "audit": {"rejector": None, "claude": None}}
    json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return p


def couverture(qd, nd_):
    poids = {n["id"]: n["poids"] for n in nd_["notions"]}; vu = {}
    for q in qd["questions"]:
        for n in q["notions"]:
            vu.setdefault(n, set()).add(q["angle"]); vu.setdefault(n + "#", []).append(q["id"])
    faibles = [n for n, p in poids.items() if p >= 2 and (len(vu.get(n + "#", [])) < 2 or len(vu.get(n, ())) < 2)]
    absentes = [n for n in poids if n not in vu]
    fm = {f: sum(q["format"] == f for q in qd["questions"]) for f in ("A", "Kprim", "MenuLong")}
    return faibles, absentes, fm


def parts_poids(d):
    """Règle 5bis du prompt : poids 3 ≤ 15 % et poids 2 ≤ 35 % des notions ; bloque l'écriture si dépassé."""
    n = len(d["notions"]) or 1; e = []
    for p, plafond in ((3, 0.15), (2, 0.35)):
        k = sum(x["poids"] == p for x in d["notions"])
        if k > plafond * n:
            e.append(f"poids {p} : {k}/{n} notions ({k / n:.0%}) > {plafond:.0%} (au plus {int(plafond * n)})")
    return e


def main(fichier, quoi="tout"):
    g = runpy.run_path(fichier, init_globals={k: v for k, v in globals().items() if k[:1].isupper() or k in ("nd", "notions", "questions", "correction", "cell")})
    idx = {c["id"]: c for c in P.canoniques()}
    if g["ID"] not in idx:                     # identifiant calculé par spécialité, comme selection() --spec
        idx.update({c["id"]: c for c in P.canoniques(g.get("SPEC", os.environ.get("SPEC", "PED")))})
    c = idx[g["ID"]]; ok = True
    for etape, cle_ in (("notions", "NOT"), ("questions", "QS"), ("correction", "COR")):
        if quoi not in ("tout", etape) or cle_ not in g:
            continue
        d = g[cle_]
        err = P.valider(etape, d, c)
        if etape == "notions" and not err:
            err = parts_poids(d)
        if err:
            ok = False; print(etape, "ERREURS :", *err, sep="\n  ")
            if etape == "notions":
                break                          # sans notions écrites, questions et correction ne peuvent pas se valider
            continue
        p = ecrire(etape, c, d, err); print(etape, "OK →", os.path.relpath(p, R))
        if etape == "notions":
            print("  notions :", len(d["notions"]), "poids3 :", sum(n["poids"] == 3 for n in d["notions"]), "poids2 :", sum(n["poids"] == 2 for n in d["notions"]))
        if etape == "questions":
            f, a, fm = couverture(d, json.load(open(P.chemin("notions", c), encoding="utf-8")))
            print("  formats :", fm, "| poids≥2 sous-couvertes :", f, "| notions absentes :", a)
    return ok


if __name__ == "__main__":
    sys.exit(0 if main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "tout") else 1)
