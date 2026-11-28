"""Apparie un cliché normal (déjà dans l'atlas local ou dans normaux.json) aux dossiers de l'atlas qui n'en ont pas.
Lit APPARIEMENTS_NORMAUX.json {dossier: {"de": "IMG-xxx" (normal d'un autre dossier) | "N:<clé normaux.json>", "pourquoi": "..."}} ;
réécrit atlas_liens/<organe>.json en forme {"atlas": id, "normal": {img, source, licence, auteur}}. Idempotent. Signature : AAI (Anthropic AI)"""
import json, os
ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
P = os.path.join(RAC, "conception", "donnees", "paraclinique"); M = os.path.join(P, "atlas", "manifest")
AP = json.load(open(os.path.join(ICI, "APPARIEMENTS_NORMAUX.json"), encoding="utf-8"))
NO = json.load(open(os.path.join(ICI, "normaux.json"), encoding="utf-8")) if os.path.exists(os.path.join(ICI, "normaux.json")) else {}
def normal_de(src):
    if src.startswith("N:"):
        n = NO[src[2:]]
    else:
        n = json.load(open(os.path.join(M, src + ".json"), encoding="utf-8"))["normal"]
    return {"img": "atlas/" + n["file"].replace("images/", ""), "source": n.get("source_url"), "licence": n.get("license"), "auteur": n.get("author"),
            "modalite": n.get("modality"), "region": n.get("region"), "plan": n.get("plane"), "apparie_depuis": src}
nb = 0
for f in sorted(os.listdir(os.path.join(P, "atlas_liens"))):
    fp = os.path.join(P, "atlas_liens", f); L = json.load(open(fp, encoding="utf-8")); ch = False
    for k, v in L.items():
        if k.startswith("_"):
            continue
        vs = v if isinstance(v, list) else [v]; out = []
        for x in vs:
            i = x.get("atlas") if isinstance(x, dict) else x
            if i in AP and not (isinstance(x, dict) and x.get("normal")):
                x = {"atlas": i, "normal": dict(normal_de(AP[i]["de"]), pourquoi=AP[i]["pourquoi"])}; ch = True; nb += 1
            out.append(x)
        L[k] = out if isinstance(v, list) else out[0]
    if ch:
        json.dump(L, open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(nb, "liens appariés")
