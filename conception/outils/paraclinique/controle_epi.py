#!/usr/bin/env python3
"""Contrôle mécanique (0 token) des épidémiologies des fiches flash d'imagerie.
Règle : toute épidémiologie qui contient un chiffre doit citer sa source dans la même ligne
(organisme ou auteur + année, ou DOI/PMID/URL) ; « à vérifier » est permis s'il dit où vérifier.
Usage : python conception/outils/paraclinique/controle_epi.py [stem ...]  → code 1 si une ligne viole la règle."""
import glob, json, os, re, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))); os.chdir(R)
CIT = re.compile(r"(doi|pmid|https?://|\b(19|20)\d{2}\b)", re.I)
CHIFFRE = re.compile(r"\d")
cibles = sys.argv[1:]
mauvais = pleines = suisses = 0
for f in sorted(glob.glob("conception/donnees/paraclinique/fiches_flash/*.json")):
    st = os.path.basename(f)[:-5]
    if cibles and st not in cibles:
        continue
    for k, v in json.load(open(f)).items():
        if k.startswith("_") or not isinstance(v, dict):
            continue
        e = (v.get("epi") or "").strip()
        if not e or "à produire" in e:
            continue
        if "à vérifier" in e and not re.search(r"(OFS|Obsan|NICER|ONEC|OFSP|PubMed|registre|société|guidelines|recommandation|\bdans\b)", e, re.I):
            print(f"{st} | {k} | « à vérifier » sans lieu de vérification"); mauvais += 1; continue
        if CHIFFRE.search(e) and not CIT.search(e + " " + str(v.get("source", ""))):
            print(f"{st} | {k} | chiffre sans source : {e[:90]}"); mauvais += 1; continue
        pleines += 1
        suisses += bool(re.search(r"(Suisse|suisse|OFS|Obsan|NICER|ONEC|OFSP|CH\b)", e))
print(f"épidémiologies valides {pleines} (dont suisses {suisses}) ; non conformes {mauvais}")
sys.exit(1 if mauvais else 0)
