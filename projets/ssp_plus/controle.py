#!/usr/bin/env python3
"""Contrôles mécaniques de ssp_plus_v2.json : doit afficher 0 erreur."""
import json, re, pathlib, collections, sys

R = pathlib.Path(__file__).resolve().parents[2]
off = {o["ssp"] for o in json.load(open(R / "data/ssp/INDEX.json"))["ssp"]}
v2 = json.load(open(R / "projets/ssp_plus/ssp_plus_v2.json", encoding="utf-8"))
STATUTS = {"garde", "deplace", "fusionne_dans", "retire_doublon_catalogue", "ajoute"}
err = []
actifs = [e for e in v2 if e["statut"] in ("garde", "deplace", "ajoute")]
codes = [e["code"] for e in actifs]
for c, n in collections.Counter(codes).items():
    if n > 1: err.append(f"code en double : {c}")
for e in v2:
    s, c, p, a = e["statut"], e["code"], e["parentOfficiel"], e["ancienCode"] or e["intitule"]
    if s not in STATUTS: err.append(f"{a} : statut inconnu {s}")
    if not e.get("justification"): err.append(f"{a} : justification absente")
    if s in ("garde", "deplace", "ajoute"):
        if not c.endswith("(+)"): err.append(f"{a} : code sans (+) : {c}")
        if c.replace("(+)", "") in off: err.append(f"{a} : code identique à un officiel : {c}")
        if p not in off: err.append(f"{a} : parent inconnu {p}")
        if c[:1] != p[:1] or e["categorie"] != p[:1]: err.append(f"{a} : lettre du code/catégorie ≠ parent ({c}, {e['categorie']}, {p})")
        if not re.fullmatch(r"(G\d+|[SFO]\d+\.\d+)\(\+\)", c): err.append(f"{a} : format de code invalide {c}")
        if not c.startswith("G") and c.split(".")[0] != p.split(".")[0]: err.append(f"{a} : groupe du code ≠ groupe du parent")
    else:
        if c: err.append(f"{a} : un SSP+ retiré ou fusionné ne porte pas de code")
    if s == "ajoute" and not e.get("sources"): err.append(f"{a} : ajout sans source")
    if s == "retire_doublon_catalogue" and e.get("doublonDe") not in off: err.append(f"{a} : doublonDe invalide")
    if s == "fusionne_dans" and e.get("fusionneDans", "").split(" ")[0] not in codes: err.append(f"{a} : cible de fusion inactive")
    if a.startswith("F-") and s == "deplace" and e["categorie"] != "F" and "ARBITRER" not in e["justification"]:
        err.append(f"{a} : résultat d'examen sorti de F sans arbitrage")
print("Comptes par statut :", dict(sorted(collections.Counter(e["statut"] for e in v2).items())))
print("Actifs par catégorie :", dict(sorted(collections.Counter(e["categorie"] for e in actifs).items())))
sans = sorted(off - {e["parentOfficiel"] for e in actifs}, key=lambda x: (x[0], [int(n) for n in re.findall(r"\d+", x)]))
print(f"Officiels sans SSP+ actif ({len(sans)}) :", ", ".join(sans))
print(f"{len(err)} erreur(s)")
for x in err: print(" -", x)
sys.exit(1 if err else 0)
