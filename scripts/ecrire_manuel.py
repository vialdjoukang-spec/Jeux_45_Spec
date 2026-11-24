"""Production manuelle (sans API) des notions, questions et corrections du jeu 45 Spec, au format exact de
scripts/produire_notions_questions.py : un agent rédige une source compacte (module Python), ce script la déplie au schéma,
la valide avec valider() du script de production, puis l'écrit avec ecrire() (même chemin, mêmes champs).

Usage : python scripts/ecrire_manuel.py SOURCE.py [--spec NEU] [--etapes notions,questions,correction]
Source compacte : ID (préfixe de l'id canonique), PLAN, NOTIONS (lignes « rub|nature|poids|S|source|énoncé »), ANGLES,
QUESTIONS (via q()), CORRECTION (dict, via nc(), nd(), pec()), AVERIFIER (liste de doutes, écrite dans le champ aVerifier).
Signature : AAI (Anthropic AI)"""
import argparse, json, os, runpy, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import produire_notions_questions as P  # noqa: E402

RUB = dict(def_="definition", epi="epidemiology", bas="basicSciences", ana="anamnesis", exa="clinicalExam", red="presumptionRedFlags",
           gold="workupGoldStandard", alt="workupAlternatives", pos="positiveDiagnosis", acu="acuteManagement", chr="chronicManagement",
           hos="hospitalizationComplications", pro="prognosisDischarge", sur="surveillance", fol="followUpNetwork")
RUB["def"] = "definition"
AUTEUR = "claude-opus-5-5 (production manuelle sans API, agent 45spec)"


def notions(src):
    out = []
    for i, l in enumerate(src["NOTIONS"], 1):
        rub, nat, poids, s, source, enonce = [x.strip() for x in l.split("|", 5)]
        out.append({"id": f"N{i:02d}", "rubrique": RUB.get(rub, rub), "nature": nat, "enonce": enonce, "poids": int(poids),
                    "suisse": s.upper() == "S", "source": source})
    return {"plan": src.get("PLAN", "monographique"), "notions": out, "anglesMorts": src["ANGLES"]}


def _opt(lst):
    o = []
    for k, x in zip("ABCDEFGHIJKLMNOPQRST", lst):
        txt, why = (x.split("||", 1) + [""])[:2]
        ok = txt.strip().startswith("*")
        o.append({"key": k, "text": txt.strip().lstrip("*").strip(), "correct": ok, "why": why.strip()})
    return o


def questions(src):
    out = []
    for i, q in enumerate(src["QUESTIONS"], 1):
        st = []
        if q["format"] == "Kprim":
            for x in q["items"]:
                txt, why = (x.split("||", 1) + [""])[:2]
                v, t = txt.split(":", 1)
                st.append({"text": t.strip(), "true": v.strip().upper() == "V", "why": why.strip()})
        out.append({"id": f"Q{i:02d}", "format": q["format"], "situation": q.get("sit", "starting_point"),
                    "diagnosticMasque": q.get("masque", True),
                    "serie": ({"id": q["serie"][0], "etape": q["serie"][1], "total": q["serie"][2]} if q.get("serie") else None),
                    "stem": q["stem"], "prompt": q["prompt"], "options": [] if q["format"] == "Kprim" else _opt(q["items"]),
                    "statements": st, "notions": q["notions"].split(), "angle": q["angle"], "difficulte": q["diff"],
                    "ladder": dict(zip(("zeroD", "mechanism", "semiology", "discriminant", "decision", "trap", "anchor"), q["ladder"])),
                    "sources": q["sources"] if isinstance(q["sources"], list) else [q["sources"]]})
    return {"questions": out}


def _cell(c):
    return c if isinstance(c, str) else [{"t": t, "i": i} for t, i in c]


def _arbre(a):
    return None if a is None else [{"id": n[0], "parent": n[1], "t": n[2], "i": n[3], "pec": n[4] if len(n) > 4 else None,
                                    "notion": n[5] if len(n) > 5 else None} for n in a]


def correction(src):
    C = src["CORRECTION"]; ns = []
    for i, n in enumerate(C["notions"], 1):
        tab = n.get("tableau")
        ns.append({"id": f"c{i}", "titre": n["titre"], "rubriques": [RUB.get(r, r) for r in n["rub"]], "comment": n["comment"],
                   "tableau": {"colonnes": tab[0], "lignes": [[_cell(c) for c in l] for l in tab[1]]} if tab else None,
                   "arbre": _arbre(n.get("arbre")), "points": n["points"], "sources": n["sources"]})
    pecs = []
    for p in C["pec"]:
        m = p["moyens"]
        cond = lambda x: None if x is None else {"mesuresGenerales": x[0], "etapes": [{"temps": a, "qui": b, "fait": c} for a, b, c in x[1]]}
        pecs.append({"cle": p["cle"], "titre": p["titre"], "but": p["but"],
                     "moyens": {"accueil": m["accueil"],
                                "pharmacologique": [{"molecule": a, "posologie": b, "pourquoi": c, "source": d} for a, b, c, d in m["pharma"]],
                                "nonPharmacologique": [{"categorie": a, "mesure": b, "pourquoi": c} for a, b, c in m["nonpharma"]],
                                "transversal": [{"discipline": a, "apport": b} for a, b in m["transversal"]]},
                     "conduite": {"urgence": cond(p["urgence"]), "horsUrgence": cond(p["horsUrgence"])},
                     "pronostic": p["pronostic"],
                     "surveillance": {"suivi": [{"quoi": a, "quand": b, "cible": c} for a, b, c in p["suivi"]], "sortie": p["sortie"]},
                     "prevention": dict(zip(("primaire", "secondaire", "tertiaire"), p["prevention"]))})
    s = C["ssp"]
    return {"theme": C["theme"], "notions": ns, "ssp": {"code": s["code"], "nom": s["nom"], "officiel": s["officiel"], "algorithme": _arbre(s["algorithme"])},
            "priseEnCharge": pecs}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("source"); ap.add_argument("--spec", default="NEU")
    ap.add_argument("--etapes", default="notions,questions,correction"); ap.add_argument("--force", action="store_true")
    a = ap.parse_args(); src = runpy.run_path(a.source)
    c = [x for x in P.canoniques(a.spec) if x["id"].startswith(src["ID"])]
    if len(c) != 1:
        sys.exit(f"identifiant ambigu ou inconnu : {src['ID']} → {[x['id'] for x in c]}")
    c = c[0]; total = 0
    for et in a.etapes.split(","):
        if et not in src.get("ETAPES", ["notions", "questions", "correction"]):
            continue
        d = {"notions": notions, "questions": questions, "correction": correction}[et](src)
        err = P.valider(et, d, c)
        P.ecrire(et, c, d, {"_mode": "manuel", "agent": "45spec-" + a.spec}, err)
        p = P.chemin(et, c); o = json.load(open(p, encoding="utf-8"))
        o["signature"]["modele"] = AUTEUR; o["aVerifier"] = src.get("AVERIFIER", [])
        json.dump(o, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        n = len(d.get("notions") or d.get("questions") or [])
        print(f"{et} {c['id']} : {n} éléments, {len(err)} erreur(s) {err[:6]}"); total += len(err)
    if "questions" in a.etapes and "QUESTIONS" in src:      # contrôles de couverture (règle 8ter) et d'interdits, hors valider()
        q = questions(src)["questions"]; f = [x["format"] for x in q]; N = notions(src)["notions"]
        print("formats", {k: f.count(k) for k in set(f)}, "séries", sorted({x["serie"]["id"] for x in q if x["serie"]}))
        for x in q:                                          # le jeu annonce « menu long : une à trois réponses »
            if x["format"] == "MenuLong" and not 1 <= sum(o["correct"] for o in x["options"]) <= 3:
                print(f"  {x['id']} : un menu long exige 1 à 3 réponses justes"); total += 1
        nb = len(N); p3 = sum(n["poids"] == 3 for n in N); p2 = sum(n["poids"] == 2 for n in N)
        if p3 > 0.15 * nb or p2 > 0.35 * nb:
            print(f"  poids hors règle 5bis : poids 3 = {p3}/{nb}, poids 2 = {p2}/{nb}"); total += 1
        for n in N:
            qs = [x for x in q if n["id"] in x["notions"]]
            if n["poids"] >= 2 and (len(qs) < 2 or len({x["angle"] for x in qs}) < 2):
                print("  couverture insuffisante", n["id"], n["poids"], [x["id"] + x["angle"][0] for x in qs])
    txt = open(a.source, encoding="utf-8").read()
    for mot in ("CNP", "CPCM", "Centre neuchâtelois"):
        if mot in txt:
            print("  INTERDIT dans la source :", mot); total += 1
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
