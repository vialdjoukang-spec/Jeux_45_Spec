"""Audit mécanique exhaustif de la vague 1 du 45 Spec (notions, questions, corrections), 0 token.

Usage : python scripts/audit_vague1.py [--specs END,CAR,PNE,NEP,GAS] [--json sortie.json]
Contrôles : formats (A = 5 options dont 1 juste ; Kprim = 4 affirmations ; menu long 12–20 options dont 1–3 justes),
ratio des formats, « why » présent partout, diagnostic masqué absent de la vignette et de la question, notions citées
existantes, sources présentes, correction complète (notions, SSP, priseEnCharge) validée par valider(), aucun lieu
CNP/CPCM. Signature : AAI (Anthropic AI)"""
import argparse, glob, json, os, re, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import produire_notions_questions as P  # noqa: E402

R = P.R
REVUS = set(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "audit_vague1_revus.json"), encoding="utf-8"))["revus"]) \
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "audit_vague1_revus.json")) else set()
INTERDITS = re.compile(r"\bCNP\b|\bCPCM\b|neuch[âa]telois de psychiatrie|Pr[ée]fargier|Perreux", re.I)
VIDE = {"de", "du", "la", "le", "les", "des", "et", "ou", "sur", "avec", "sans", "par", "aigue", "aigu", "chronique",
        "syndrome", "maladie", "severe", "primaire", "secondaire", "autres", "autre", "non", "precisee", "precise", "type"}


def mots_cles(nom):
    return [m for m in P.cle(re.sub(r"\(.*?\)", "", nom)).split() if len(m) > 4 and m not in VIDE]


def auditer(specs):
    rap = defaultdict(lambda: {"fichiers": 0, "questions": 0, "formats": Counter(), "erreurs": []})
    for sp in specs:
        r = rap[sp]
        for fq in sorted(glob.glob(os.path.join(R, "content", "questions", sp, "*.json"))):
            base = os.path.basename(fq); r["fichiers"] += 1
            dq = json.load(open(fq, encoding="utf-8"))
            fn = os.path.join(R, "content", "notions", sp, base); fc = os.path.join(R, "content", "corrections", sp, base)
            c = {"codes": [sp], "id": base[:-5], "entite": {"nom": dq["entite"]}}
            nid = {n["id"] for n in json.load(open(fn, encoding="utf-8"))["notions"]} if os.path.exists(fn) else set()
            if not nid:
                r["erreurs"].append((base, "notions absentes"))
            mk = mots_cles(dq["entite"])
            for q in dq["questions"]:
                r["questions"] += 1; f = q["format"]; r["formats"][f] += 1
                o = q["options"]; s = q["statements"]; k = sum(x["correct"] for x in o)
                e = lambda m: r["erreurs"].append((base, f"{q['id']} {m}"))
                if f == "A" and (len(o) != 5 or k != 1 or s):
                    e(f"type A : {len(o)} options, {k} juste(s)")
                if f == "Kprim" and (len(s) != 4 or o):
                    e(f"Kprim : {len(s)} affirmations")
                if f == "MenuLong" and (not 12 <= len(o) <= 20 or not 1 <= k <= 3):
                    e(f"menu long : {len(o)} options, {k} juste(s)")
                if any(not (x.get("why") or "").strip() for x in o + s):
                    e("option sans explication")
                if len({x["text"].strip().lower() for x in o}) != len(o):
                    e("options en double")
                txt = P.cle(q["stem"] + " " + q["prompt"])
                if f"{base}|{q['id']}" not in REVUS and q["diagnosticMasque"] and mk and (all(m in txt for m in mk) or (len(mk) == 1 and mk[0] in txt)):
                    e(f"diagnostic masqué nommé ({' '.join(mk)})")
                if set(q["notions"]) - nid:
                    e(f"notions inconnues {sorted(set(q['notions']) - nid)}")
                if not q.get("sources"):
                    e("sans source")
                if INTERDITS.search(json.dumps(q, ensure_ascii=False)):
                    e("lieu interdit (CNP/CPCM)")
            err = P.valider("questions", {k2: dq[k2] for k2 in ("questions",)}, c)
            for x in err:
                if "diagnostic masqué" not in x:
                    r["erreurs"].append((base, "valider : " + x))
            if not os.path.exists(fc):
                r["erreurs"].append((base, "correction absente")); continue
            dc = json.load(open(fc, encoding="utf-8"))
            corps = {k2: dc[k2] for k2 in ("theme", "notions", "ssp", "priseEnCharge") if k2 in dc}
            for x in P.valider("correction", corps, c):
                r["erreurs"].append((base, "correction : " + x))
            if INTERDITS.search(json.dumps(dc, ensure_ascii=False)) or INTERDITS.search(json.dumps(dq.get("stem", ""), ensure_ascii=False)):
                r["erreurs"].append((base, "correction : lieu interdit (CNP/CPCM)"))
    return rap


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--specs", default="END,CAR,PNE,NEP,GAS"); ap.add_argument("--json")
    a = ap.parse_args(); rap = auditer(a.specs.split(","))
    tot = Counter()
    for sp, r in rap.items():
        n = r["questions"] or 1; fm = r["formats"]
        print(f"{sp} : {r['fichiers']} fichiers, {r['questions']} QCM ; A {100*fm['A']/n:.0f} % · Kprim {100*fm['Kprim']/n:.0f} % · "
              f"menu long {100*fm['MenuLong']/n:.0f} % ; {len(r['erreurs'])} anomalie(s)")
        tot.update({"q": r["questions"], "e": len(r["erreurs"])})
        for b, m in r["erreurs"][:400]:
            print("  ", b, ":", m)
    print(f"TOTAL : {tot['q']} QCM, {tot['e']} anomalie(s)")
    if a.json:
        json.dump({sp: {**r, "formats": dict(r["formats"])} for sp, r in rap.items()}, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
