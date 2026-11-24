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

# Tétrade : questions de raisonnement écrites en texte (conception/donnees/tetrade/arene/<dossier>.txt), adossées à une
# pathologie rédigée du système (sa ligne « s » devient la source) ; un titre ne trahit jamais le diagnostic.
import re as _re, sys as _sys
sys_path = "conception/outils"; _sys.path.insert(0, sys_path)
from systemes_rediges import REDIGES as _RED
_NOMSYS = {c["dossier"]: s for s, c in _RED.items()}
_GENERIQUES = {"aiguë", "aigu", "chronique", "syndrome", "maladie", "primaire", "primitive", "secondaire", "grave", "sévère", "commune", "simple"}
def _sources_patho(dossier):
    S, nom = {}, None
    for l in open(f"conception/outils/{dossier}/pathologies.txt", encoding="utf-8"):
        if l.startswith("@ "): nom = l.split("|", 1)[1].strip()
        elif l.startswith("s ") and nom: S[nom] = l[2:].strip()
    return S
_err = []
for f in sorted(glob.glob("conception/donnees/tetrade/arene/*.txt")):
    dos = os.path.basename(f)[:-4]; P = _sources_patho(dos); p = "tetrade_" + dos
    noms[p] = f"Tétrade — {_NOMSYS.get(dos, dos)} (raisonnement clinique)"; cur = None
    def _fin(c):
        if not c: return
        o, ok = c["options"], sum(x["ok"] for x in c["options"])
        if c["format"] == "A" and (len(o) != 5 or ok != 1): _err.append(f"{c['id']} : un type A demande 5 options dont 1 juste")
        if c["format"] == "Kprim" and len(o) != 4: _err.append(f"{c['id']} : un Kprim demande 4 affirmations")
        if any(not x["why"] for x in o) or not c["stem"]: _err.append(f"{c['id']} : énoncé ou explication vide")
        if c["_x"] not in P: _err.append(f"{c['id']} : pathologie inconnue « {c['_x']} » dans {dos}/pathologies.txt")
        mots = [m for m in _re.findall(r"[\wÀ-ÿ'-]{6,}", c["_x"].lower()) if m not in _GENERIQUES]
        if any(m in c["titre"].lower() for m in mots): _err.append(f"{c['id']} : le titre trahit le diagnostic")
        src = P.get(c["_x"], ""); x = c.pop("_x"); lien = c.pop("_i", None)
        c["origine"] = f"conception/outils/{dos}/pathologies.txt#{x}" + (f" · courbe {lien}" if lien else "")
        c["sources"] = [src] if src else []
        paquets[p].append(c)
    for l in open(f, encoding="utf-8"):
        l = l.rstrip("\n")
        if l.startswith("## "):
            _fin(cur); i_, fm, ti = [x.strip() for x in l[3:].split("|", 2)]
            cur = q(f"{p}_{i_}", "Kprim" if fm == "K" else "A", ti, "", "", [], None, None, ""); cur["_x"] = ""
        elif cur is None or not l.strip() or l.startswith("#"): continue
        elif l.startswith("S "): cur["stem"] = l[2:]
        elif l.startswith("P "): cur["prompt"] = l[2:]
        elif l[:2] in ("+ ", "- "):
            t, w = (l[2:].split(" || ", 1) + [""])[:2]; n = len(cur["options"])
            cur["options"].append({"k": str(n + 1) if cur["format"] == "Kprim" else "ABCDE"[n], "t": t.strip(), "ok": l[0] == "+", "why": w.strip()})
        elif l.startswith("C "):
            m = [x.strip() for x in l[2:].split(" || ")]; cur["echelle"] = [[k, v] for k, v in zip(["mechanism", "discriminant", "anchor"], m) if v]
        elif l.startswith("X "): cur["_x"] = l[2:].strip()
        elif l.startswith("I "): cur["_i"] = l[2:].strip()
    _fin(cur)
if _err:
    raise SystemExit("Arène Tétrade — erreurs :\n" + "\n".join(_err))
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
