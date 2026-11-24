"""Production PSY du jeu 45 Spec sans appel API : l'agent écrit un module compact par pathologie (src/<id>.py),
lib.py le déploie dans les schémas de scripts/produire_notions_questions.py, valide avec valider() puis écrit avec ecrire().
Usage : python projets/45spec/psy/lib.py <id> [<id>…]     Signature : AAI (Anthropic AI)"""
import importlib.util, os, re, sys, json
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(R, "scripts"))
import produire_notions_questions as P  # noqa: E402
P.MODELE = "claude-opus-5-5 (agent, sans API)"
RUB = dict(zip("def epi bas ana cli red gold alt pos acu chr hos pro sur fol".split(), P.RUBRIQUES))


def notions(rows):
    """rows : (rub, nature, poids, suisse 0/1, source, énoncé)"""
    return [{"id": f"N{i:02d}", "rubrique": RUB.get(r, r), "nature": n, "enonce": e, "poids": p, "suisse": bool(s), "source": src}
            for i, (r, n, p, s, src, e) in enumerate(rows, 1)]


def _lad(s):
    v = [x.strip() for x in s.split("|")]; assert len(v) == 7, s
    return dict(zip(("zeroD", "mechanism", "semiology", "discriminant", "decision", "trap", "anchor"), v))


def _serie(s):
    if not s: return None
    i, e, t = s.split("/"); return {"id": i, "etape": int(e), "total": int(t)}


def _base(fmt, sit, serie, stem, prompt, no, angle, dif, lad, src, masque=True):
    return {"format": fmt, "situation": {"sp": "starting_point", "mono": "monographique"}[sit], "diagnosticMasque": masque,
            "serie": _serie(serie), "stem": stem, "prompt": prompt, "options": [], "statements": [],
            "notions": [f"N{int(x):02d}" for x in str(no).split()], "angle": angle, "difficulte": dif, "ladder": _lad(lad), "sources": [src]}


def A(sit, serie, stem, prompt, opts, no, angle, dif, lad, src, masque=True):
    """opts : liste de (texte, why) ; la juste commence par '*'."""
    q = _base("A", sit, serie, stem, prompt, no, angle, dif, lad, src, masque)
    q["options"] = [{"key": "ABCDE"[i], "text": t.lstrip("*"), "correct": t.startswith("*"), "why": w} for i, (t, w) in enumerate(opts)]
    return q


def M(sit, serie, stem, prompt, opts, no, angle, dif, lad, src, masque=True):
    q = _base("MenuLong", sit, serie, stem, prompt, no, angle, dif, lad, src, masque)
    q["options"] = [{"key": chr(65 + i), "text": t.lstrip("*"), "correct": t.startswith("*"), "why": w} for i, (t, w) in enumerate(opts)]
    return q


def K(sit, serie, stem, prompt, st, no, angle, dif, lad, src, masque=True):
    """st : liste de (texte, vrai 0/1, why)"""
    q = _base("Kprim", sit, serie, stem, prompt, no, angle, dif, lad, src, masque)
    q["statements"] = [{"text": t, "true": bool(v), "why": w} for t, v, w in st]
    return q


def C(t, i):
    return [{"t": t, "i": i}]


def nd(rows):
    """rows : (id, parent, t, i, pec, notion)"""
    return [{"id": a, "parent": b, "t": t, "i": i, "pec": p, "notion": n} for a, b, t, i, p, n in rows]


def cours(cid, titre, rubs, comment, points, sources, tableau=None, arbre=None):
    return {"id": cid, "titre": titre, "rubriques": [RUB.get(r, r) for r in rubs.split()], "comment": comment,
            "tableau": tableau, "arbre": nd(arbre) if arbre else None, "points": points, "sources": sources}


def pec(cle, titre, but, accueil, pharma, nonpharma, transv, urg, hors, pronostic, suivi, sortie, prev):
    """pharma : (molécule, posologie, pourquoi, source) ; nonpharma : (catégorie, mesure, pourquoi) ; transv : (discipline, apport)
    urg/hors : None ou (mesuresGenerales, [(temps, qui, fait)]) ; suivi : (quoi, quand, cible) ; prev : (primaire, secondaire, tertiaire)"""
    cd = lambda x: None if x is None else {"mesuresGenerales": x[0], "etapes": [{"temps": a, "qui": b, "fait": c} for a, b, c in x[1]]}
    return {"cle": cle, "titre": titre, "but": but, "moyens": {
        "accueil": accueil, "pharmacologique": [dict(zip(("molecule", "posologie", "pourquoi", "source"), x)) for x in pharma],
        "nonPharmacologique": [dict(zip(("categorie", "mesure", "pourquoi"), x)) for x in nonpharma],
        "transversal": [dict(zip(("discipline", "apport"), x)) for x in transv]},
        "conduite": {"urgence": cd(urg), "horsUrgence": cd(hors)}, "pronostic": pronostic,
        "surveillance": {"suivi": [dict(zip(("quoi", "quand", "cible"), x)) for x in suivi], "sortie": sortie},
        "prevention": dict(zip(("primaire", "secondaire", "tertiaire"), prev))}


def controles_vial(nt, qs, cor):
    err = []; fm = [q["format"] for q in qs["questions"]]
    txt = json.dumps([nt, qs, cor], ensure_ascii=False)
    if re.search(r"\b(CNP|CPCM)\b|Chaux-de-Fonds", txt): err.append("lieu interdit (CNP/CPCM)")
    n = len(fm); a, k, m = fm.count("A") / n, fm.count("Kprim") / n, fm.count("MenuLong") / n
    if not (0.6 <= a <= 0.8 and 0.12 <= k <= 0.28 and 0.05 <= m <= 0.15): err.append(f"proportions A/K/M {a:.2f}/{k:.2f}/{m:.2f}")
    cit = {}
    for q in qs["questions"]:
        for x in q["notions"]: cit.setdefault(x, set()).add((q["id"], q["angle"]))
    for x in nt["notions"]:
        c = cit.get(x["id"], set())
        if x["poids"] >= 2 and (len(c) < 2 or len({a for _, a in c}) < 2): err.append(f"couverture {x['id']} (poids {x['poids']}) : {sorted(c)}")
    p = [x["poids"] for x in nt["notions"]]
    if p.count(3) > 0.15 * len(p) + 0.01 or p.count(2) > 0.35 * len(p) + 0.01: err.append(f"poids 3/2 : {p.count(3)}/{p.count(2)} sur {len(p)}")
    if not any(q["serie"] for q in qs["questions"]): err.append("aucune série")
    return err


def produire(pid, ecrire=True):
    cs = {c["id"]: c for c in P.canoniques("PSY")}; c = cs[pid]
    sp = importlib.util.spec_from_file_location("m", os.path.join(os.path.dirname(__file__), "src", pid.replace(".", "_") + ".py"))
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    nt = {"plan": m.PLAN, "notions": notions(m.NOTIONS), "anglesMorts": m.ANGLES}
    qs = {"questions": [{"id": f"Q{i:02d}", **q} for i, q in enumerate(m.QUESTIONS, 1)]}
    qs["questions"] = [{k: q[k] for k in P.QUESTION["properties"]} for q in qs["questions"]]
    cor = m.CORRECTION
    e1 = P.valider("notions", nt, c)
    if e1: return {"notions": e1}
    usage = {"_mode": "agent", "api": False, "modele": P.MODELE}
    P.ecrire("notions", c, nt, usage, e1)  # valider('questions') lit les notions sur disque
    e2 = P.valider("questions", qs, c); e3 = P.valider("correction", cor, c); ev = controles_vial(nt, qs, cor)
    if e2 or e3 or ev or not ecrire:
        os.remove(P.chemin("notions", c)); return {"questions": e2, "correction": e3, "vial": ev}
    P.ecrire("questions", c, qs, usage, e2); P.ecrire("correction", c, cor, usage, e3)
    fm = [q["format"] for q in qs["questions"]]
    return {"ok": f"{len(nt['notions'])} notions, {len(fm)} questions (A {fm.count('A')}, Kprim {fm.count('Kprim')}, MenuLong {fm.count('MenuLong')}), {len(cor['notions'])} cours, {len(cor['priseEnCharge'])} pec"}


if __name__ == "__main__":
    for pid in sys.argv[1:]:
        print(pid, json.dumps(produire(pid), ensure_ascii=False, indent=0))
