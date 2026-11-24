"""Marque des questions d'une source compacte comme monographiques (diagnostic nommé) : masque=False, sit="monographique".
Usage : python scripts/demasquer_manuel.py SOURCE.py 3 7 12   — Signature : AAI (Anthropic AI)"""
import re, sys
p, nums = sys.argv[1], {int(x) for x in sys.argv[2:]}
s = open(p, encoding="utf-8").read(); i0 = s.index("QUESTIONS = ["); i1 = s.index("\nCORRECTION")
k = [0]
def f(m):
    k[0] += 1
    return m.group(0) + ('masque=False, sit="monographique", ' if k[0] in nums and "masque=" not in s[m.end():m.end() + 40] else "")
q = re.sub(r"^dict\(", f, s[i0:i1], flags=re.M)
open(p, "w", encoding="utf-8").write(s[:i0] + q + s[i1:]); print(k[0], "questions,", len(nums), "démasquées")
