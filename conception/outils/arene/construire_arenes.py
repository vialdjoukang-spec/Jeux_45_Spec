"""Moteur d'arène commun — paquets de questions (0 token). Rassemble, au format unique de l'arène, les cas des 4 jeux :
Paraclinique (conception/donnees/paraclinique/cas/**), 45 Spec (content/items/<SPEC>/** : formats A et Kprim), et plus tard
Tétrade et Transversal. Écrit conception/prototypes/moteur/arenes/<paquet>.json et arenes/index.json. Signature : AAI (Anthropic AI)"""
import collections, glob, json, os

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))); os.chdir(R)
OUT = "conception/prototypes/moteur/arenes"; os.makedirs(OUT, exist_ok=True)
MARCHES = ["zeroD", "mechanism", "semiology", "discriminant", "decision", "trap", "anchor"]
FR = {"mecanisme": "mechanism", "semiologie": "semiology", "piege": "trap", "ancre": "anchor"}


def echelle(d):
    d = {FR.get(k, k): v for k, v in (d or {}).items()}
    return [[m, d[m]] for m in MARCHES if d.get(m)]


def q(id_, fmt, titre, stem, prompt, opts, corr, src, origine):
    return {"id": id_, "format": fmt, "titre": titre, "stem": stem, "prompt": prompt, "options": opts, "echelle": echelle(corr), "sources": src, "origine": origine}


paquets = collections.defaultdict(list); noms = {}
for f in sorted(glob.glob("conception/donnees/paraclinique/cas/**/*.json", recursive=True)):
    c = json.load(open(f, encoding="utf-8")); p = "paraclinique_" + os.path.basename(os.path.dirname(f))
    noms[p] = f"Paraclinique — le bon examen ({os.path.basename(os.path.dirname(f))})"
    paquets[p].append(q(c["id"], c["format"], c["titre"], c["stem"], c["prompt"],
                        [{"k": o["key"], "t": o["text"], "ok": o["correct"], "why": o["why"]} for o in c["options"]], c.get("correction"), c.get("sources"), f))
for f in sorted(glob.glob("content/items/*/**/*.json", recursive=True)):
    d = json.load(open(f, encoding="utf-8")); spec = f.split(os.sep)[2]; p = "45spec_" + spec; noms[p] = f"45 Spec — arène {spec}"
    for i, it in enumerate(d.get("items", [])):
        if (it.get("audit") or {}).get("rejector") == "rejet":
            continue
        if it["format"] == "A":
            opts = [{"k": o["key"], "t": o["text"], "ok": o["correct"], "why": o.get("why", "")} for o in it["options"]]
        elif it["format"] in ("Kprim", "Kprime"):
            opts = [{"k": str(j + 1), "t": s["text"], "ok": s["true"], "why": s.get("why", "")} for j, s in enumerate(it["statements"])]
        else:
            continue
        paquets[p].append(q(it.get("id") or f"{d['entite']}_{i}", "Kprim" if it["format"].startswith("K") else "A", d["entite"], it["stem"], it["prompt"],
                            opts, it.get("ladder"), it.get("sources"), f))
for f in sorted(glob.glob("conception/donnees/tetrade/transversales/lecons/*/*.json")):   # Transversal : QCM des leçons auditées
    d = json.load(open(f, encoding="utf-8"))
    if (d.get("_meta") or {}).get("statut") != "AUDITÉ":
        continue
    p = "transversal_" + d.get("lettre", os.path.basename(os.path.dirname(f))); noms[p] = f"Transversal — lettre {d.get('lettre', '')}"
    for i, it in enumerate(d.get("items", [])):
        ex, br, op = it.get("explicationParOption") or {}, it.get("bonneReponse"), it.get("options") or []
        if isinstance(br, list):
            opts = [{"k": str(j + 1), "t": t, "ok": bool(br[j]), "why": ex.get(str(j + 1), "")} for j, t in enumerate(op)]; fmt = "Kprim"
        else:
            opts = [{"k": chr(65 + j), "t": t, "ok": chr(65 + j) == br, "why": ex.get(chr(65 + j), "")} for j, t in enumerate(op)]; fmt = "A"
        if len(opts) < 2 or not any(o["ok"] for o in opts):
            continue
        paquets[p].append(q(f"{d['id']}_{i + 1}", fmt, d["titre"], it.get("enonce", ""), "", opts, None, (d.get("_meta") or {}).get("sources"), f))
CORR = {os.path.basename(f)[:-5]: json.load(open(f, encoding="utf-8")) for f in glob.glob("conception/donnees/corrections/*.json")}
for L in paquets.values():                     # correction enrichie : thème, notions abordées (cours en fenêtre), SSP et algorithme
    for q in L:
        ent = os.path.basename(os.path.dirname(q["origine"])); c = CORR.get(ent)
        if c:
            rub = q["id"].split("__")[-1].split("-")[0] if "__" in q["id"] else ""
            ns = [n for n in c["notions"] if rub in n.get("rubriques", [])] or c["notions"]
            q["correction"] = {"theme": c["theme"], "ssp": c["ssp"], "notions": ns, "autres": [n for n in c["notions"] if n not in ns], "pec": c.get("pec", {})}
idx = []
for p, L in sorted(paquets.items()):
    json.dump({"nom": noms[p], "questions": L}, open(f"{OUT}/{p}.json", "w", encoding="utf-8"), ensure_ascii=False)
    idx.append({"paquet": p, "nom": noms[p], "n": len(L)})
json.dump(idx, open(f"{OUT}/index.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
G = {k: v for k, v in json.load(open("conception/donnees/glossaire_sigles.json", encoding="utf-8")).items() if not k.startswith("_")}
json.dump(G, open(f"{OUT}/sigles.json", "w", encoding="utf-8"), ensure_ascii=False)
print("arènes :", ", ".join(f"{x['paquet']} ({x['n']})" for x in idx))
