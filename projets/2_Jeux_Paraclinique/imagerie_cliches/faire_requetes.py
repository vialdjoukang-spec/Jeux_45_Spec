"""Convertit lots/requetes_NN.txt (lignes « indice | requête 1 ; requête 2 | regex ») en requetes_NN.json, via CIBLES.tsv (liste figée le 28.11.2026).
Usage : python3 faire_requetes.py NN   Signature : AAI (Anthropic AI)"""
import json, os, sys
ICI = os.path.dirname(os.path.abspath(__file__)); n = sys.argv[1]
C = {l.split("\t")[0]: l.rstrip("\n").split("\t") for l in open(os.path.join(ICI, "CIBLES.tsv"), encoding="utf-8")}
R = {}
for l in open(os.path.join(ICI, "lots", f"requetes_{n}.txt"), encoding="utf-8"):
    if not l.strip() or l.startswith("#"):
        continue
    i, q, rx = [x.strip() for x in l.split(" | ")]
    c = C[i]; R[f"{c[1]} | {c[2]} | {c[3]}"] = {"q": [x.strip() for x in q.split(";")], "re": rx, "i": int(i)}
json.dump(R, open(os.path.join(ICI, "lots", f"requetes_{n}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(R), "requêtes")
