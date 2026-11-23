#!/usr/bin/env python3
"""Compare les ancres vérifiables de deux versions d'un texte (0 token).
Usage : python ancres.py avant.txt apres.txt
Ancres : nombres (+unité), sigles, noms propres, négations, conditions, liens causaux, modaux, URL.
Sortie : bilan de volume et liste des ancres perdues (code de sortie 1 si perte)."""
import re, sys, unicodedata
from collections import Counter

MOTS = {
 "negation": r"\b(ne|n'|pas|jamais|aucun\w*|sans|ni|not|never|no|without)\b",
 "condition": r"\b(si|sauf|seulement|uniquement|lorsque|quand|à condition|tant que|if|unless|only|except|when)\b",
 "cause": r"\b(parce que|car|donc|ainsi|d'où|puisque|because|therefore|hence|since|thus)\b",
 "modal": r"\b(peut|peuvent|doit|doivent|devrait|pourrait|probablement|toujours|may|might|must|should|always|likely)\b",
}

def norm(t): return unicodedata.normalize("NFC", t)

def ancres(t):
    t = norm(t)
    a = Counter()
    for m in re.finditer(r"\d+(?:[.,]\d+)?(?:x/j|x/sem|\s?(?:%|‰|(?:[mµnk]?(?:g|L|l|mol|Eq|UI|U)|mmHg|cm|mm|m|kg|h|min|s|j|ans?|CHF|€|\$|°C)(?:/(?:[mµk]?(?:g|L|l)|kg|min|h|j|m²|1\.73\s?m²))*)\b)?", t):
        a["nb:" + re.sub(r"\s", "", m.group()).replace(",", ".")] += 1
    for m in re.finditer(r"\b[A-ZÉÈ]{2,}[A-Z0-9-]*\b", t): a["sigle:" + m.group()] += 1
    for m in re.finditer(r"(?<![.!?]\s)(?<!^)\b[A-ZÉÈ][a-zéèêàâîôûç]+(?:[- ][A-ZÉÈ][a-zéèêàâîôûç]+)*", t, re.M):
        a["nom:" + m.group()] += 1
    for m in re.finditer(r"https?://\S+", t): a["url:" + m.group()] += 1
    for k, rx in MOTS.items():
        n = len(re.findall(rx, t, re.I))
        if n: a[k] = n
    return a

def main(av, ap):
    A, B = (open(p, encoding="utf-8").read() for p in (av, ap))
    a, b = ancres(A), ancres(B)
    wa, wb = len(A.split()), len(B.split())
    perdu = {k: a[k] - b.get(k, 0) for k in a if not k.startswith(tuple(MOTS)) and b.get(k, 0) == 0}
    baisse = {k: (a[k], b.get(k, 0)) for k in MOTS if a.get(k, 0) > b.get(k, 0)}
    print(f"Volume : {wa} → {wb} mots ({(wb - wa) / max(wa, 1):+.0%})")
    print(f"Ancres conservées : {sum(1 for k in a if b.get(k))}/{len(a)}")
    for k in sorted(perdu): print("  PERDUE  ", k)
    for k, (x, y) in baisse.items(): print(f"  À VÉRIFIER  {k} : {x} → {y} (une suppression peut changer le sens)")
    sys.exit(1 if perdu else 0)

if __name__ == "__main__":
    if len(sys.argv) != 3: sys.exit(__doc__)
    main(*sys.argv[1:])
