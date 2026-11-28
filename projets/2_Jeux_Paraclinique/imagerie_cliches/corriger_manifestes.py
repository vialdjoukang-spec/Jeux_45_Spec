"""Corrige après contrôle visuel le type de cliché, la séquence ou le plan d'un dossier IMC, et trace l'observation.
Usage : python3 corriger_manifestes.py <fichier.json {IMC-xxxx: {cliche?, plan?, vu: "observation"}}>   Signature : AAI (Anthropic AI)"""
import json, os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); M = os.path.join(ICI, "..", "..", "..", "conception", "donnees", "paraclinique", "atlas", "manifest")
for i, v in json.load(open(sys.argv[1], encoding="utf-8")).items():
    f = os.path.join(M, i + ".json")
    if not os.path.exists(f):
        continue
    m = json.load(open(f, encoding="utf-8"))
    if v.get("cliche"):
        m["cliche"] = v["cliche"]; m["patho"]["modality"], m["patho"]["sequence"] = v["cliche"].split(" — ")[0], v["cliche"].split(" — ")[-1]
    if v.get("plan"):
        m["patho"]["plane"] = v["plan"]
    if v.get("vu") and "Contrôle visuel" not in m["pair_match"]:
        m["pair_match"] += f" Contrôle visuel du 28.11.2026 : {v['vu']}."
    json.dump(m, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("corrigé")
