"""Coche les notions couvertes (0 token). Une notion de poids 1 est cochée dès qu'une question auditée l'explore ; une notion de
poids 2 ou 3 l'est quand au moins deux questions auditées l'explorent sous deux angles différents (direct, application, piège).
« En attente » compte les mêmes règles avant l'audit. Écrit la couverture dans chaque fichier de notions et content/notions/COUVERTURE.json.
Signature : AAI (Anthropic AI)"""
import collections, glob, json, os

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); os.chdir(R)
tot = collections.defaultdict(lambda: collections.Counter())
for fn in sorted(glob.glob("content/notions/*/*.json")):
    N = json.load(open(fn, encoding="utf-8")); fq = fn.replace("content/notions", "content/questions")
    Q = json.load(open(fq, encoding="utf-8")) if os.path.exists(fq) else {"questions": [], "audit": {}}
    valide = (Q.get("audit") or {}).get("rejector") == "pass"
    par = collections.defaultdict(list)
    for q in Q["questions"]:
        for n in q.get("notions", []):
            par[n].append((q["id"], q.get("angle")))
    spec = fn.split(os.sep)[2]
    for n in N["notions"]:
        qs = par.get(n["id"], []); angles = {a for _, a in qs}
        assez = bool(qs) if n["poids"] == 1 else (len(qs) >= 2 and len(angles) >= 2)
        n["couverture"] = {"questions": [i for i, _ in qs], "cochee": bool(assez and valide), "enAttente": bool(assez and not valide)}
        t = tot[spec]; t["notions"] += 1; t["cochees"] += n["couverture"]["cochee"]; t["enAttente"] += n["couverture"]["enAttente"]
    tot[spec]["entites"] += 1; tot[spec]["questions"] += len(Q["questions"])
    json.dump(N, open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump({k: dict(v) for k, v in tot.items()}, open("content/notions/COUVERTURE.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1) if tot else None
for k, v in sorted(tot.items()):
    print(f"{k} : {v['entites']} pathologies, {v['notions']} notions, {v['cochees']} cochées, {v['enAttente']} en attente d'audit, {v['questions']} questions")
