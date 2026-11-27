#!/usr/bin/env python3
"""Contrôle de cohérence (0 token) : une même pathologie, présente dans plusieurs fiches flash,
doit porter la même épidémiologie (mêmes nombres, même série). Liste les divergences.
Usage : python conception/outils/paraclinique/controle_coherence.py"""
import glob, json, os, re, collections, unicodedata
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))); os.chdir(R)
def cle(t):
    t = unicodedata.normalize("NFKD", t.lower()); t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", t).strip()
def nombres(e):
    return tuple(sorted(set(re.sub(r"[\s  ']", "", m) for m in re.findall(r"\d[\d\s  ',.]*\d|\d", e))))
G = collections.defaultdict(list)
for f in sorted(glob.glob("conception/donnees/paraclinique/fiches_flash/*.json")):
    for k, v in json.load(open(f)).items():
        if k.startswith("_") or not isinstance(v, dict) or not v.get("epi") or "à vérifier" in v["epi"][:40]:
            continue
        G[cle(k)].append((os.path.basename(f)[:-5], k, v["epi"]))
n = 0
for c, L in sorted(G.items()):
    if len({nombres(e) for _, _, e in L}) > 1:
        n += 1
        print(f"\n■ {L[0][1]}")
        for st, k, e in L:
            print(f"   {st:40} {e[:150]}")
print(f"\n{n} pathologies à épidémiologie divergente")
