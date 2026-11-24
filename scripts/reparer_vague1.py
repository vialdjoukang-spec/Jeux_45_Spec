"""Réparation de forme (0 token) des fichiers de la vague 1 du 45 Spec : clés parasites, clés mal orthographiées,
listes trop longues, cellules mal typées, arbre rangé dans le tableau. Ne touche jamais au fond médical.

Usage : python scripts/reparer_vague1.py [--specs END,CAR,PNE,NEP,GAS,ALL] [--sec]
Signature : AAI (Anthropic AI)"""
import argparse, glob, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import produire_notions_questions as P  # noqa: E402

R = P.R
RENOMME = {"prévention": "prevention", "mesuresGénérales": "mesuresGenerales", " nonPharmacologique": "nonPharmacologique",
           " source": "source", "whyd": None, "whyl": None, "worthy": None, "si": None, "fl": None, "false": None, "false_placeholder": None}


def nettoyer(x):
    """Renomme ou supprime récursivement les clés parasites."""
    if isinstance(x, dict):
        out = {}
        for k, v in x.items():
            k2 = RENOMME.get(k, k)
            if k2 is None or (k2 in out and k != k2):
                continue
            out[k2] = nettoyer(v)
        return out
    if isinstance(x, list):
        return [nettoyer(v) for v in x]
    return x


def cellule(c):
    if isinstance(c, str):
        return c
    if isinstance(c, dict):
        return [c]
    if all(isinstance(v, dict) for v in c):
        return c
    if all(isinstance(v, str) for v in c):
        return " ; ".join(c)
    plat = []
    for v in c:
        plat += v if isinstance(v, list) else [v]
    return [v if isinstance(v, dict) else {"t": v, "i": ""} for v in plat]


def reparer_questions(d):
    n = 0
    for q in d["questions"]:
        if len(q["notions"]) > 6:
            q["notions"] = q["notions"][:6]; n += 1
        for x in q["options"]:
            for k in list(x):
                if k not in ("key", "text", "correct", "why"):
                    del x[k]; n += 1
        for x in q["statements"]:
            for k in list(x):
                if k not in ("text", "true", "why"):
                    del x[k]; n += 1
    return n


def reparer_correction(d):
    d2 = nettoyer({k: d[k] for k in ("theme", "notions", "ssp", "priseEnCharge") if k in d}); d.update(d2)
    for no in d["notions"]:
        t = no.get("tableau")
        if isinstance(t, dict) and "arbre" in t:
            no.setdefault("arbre", t.pop("arbre"))
        no.setdefault("arbre", None); no.setdefault("tableau", None)
        if isinstance(no["arbre"], dict) or (isinstance(no["arbre"], list) and len(no["arbre"]) < 3):
            no["arbre"] = None
        if no["tableau"]:
            ncol = len(no["tableau"]["colonnes"])
            for i, ligne in enumerate(no["tableau"]["lignes"]):
                ligne2 = []
                for c in ligne:
                    if isinstance(c, list) and len(c) > 1 and isinstance(c[0], str) and any(isinstance(v, list) for v in c) and len(ligne) - 1 + len(c) <= ncol:
                        ligne2 += [cellule(v) for v in c]
                    else:
                        ligne2.append(cellule(c))
                no["tableau"]["lignes"][i] = ligne2
        if len(no["points"]) > 5:
            no["points"] = no["points"][:4] + [" ".join(no["points"][4:])]
        if not no["points"]:
            no["points"] = [no["comment"]]
        if len(no["rubriques"]) > 4:
            no["rubriques"] = no["rubriques"][:4]
        if len(no["sources"]) > 4:
            no["sources"] = no["sources"][:3] + ["; ".join(no["sources"][3:])]
    for p in d.get("priseEnCharge", []):
        c = p.get("conduite", {})
        u = c.get("urgence")
        if isinstance(u, dict) and "horsUrgence" in u:
            hu = u.pop("horsUrgence")
            if not c.get("horsUrgence"):
                c["horsUrgence"] = hu
        for nb in p.get("moyens", {}).get("nonPharmacologique", []):
            if "molecule" in nb:
                del nb["molecule"]


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--specs", default="END,CAR,PNE,NEP,GAS,ALL"); ap.add_argument("--sec", action="store_true")
    a = ap.parse_args()
    for sp in a.specs.split(","):
        for f in sorted(glob.glob(os.path.join(R, "content", "questions", sp, "*.json"))):
            d = json.load(open(f, encoding="utf-8")); n = reparer_questions(d)
            if n:
                print("questions", sp, os.path.basename(f), n)
                if not a.sec:
                    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        for f in sorted(glob.glob(os.path.join(R, "content", "corrections", sp, "*.json"))):
            d = json.load(open(f, encoding="utf-8")); avant = json.dumps(d, ensure_ascii=False); reparer_correction(d)
            if json.dumps(d, ensure_ascii=False) != avant:
                print("correction", sp, os.path.basename(f))
                if not a.sec:
                    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
