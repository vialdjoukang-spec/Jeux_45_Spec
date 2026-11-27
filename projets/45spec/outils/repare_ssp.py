# Répare un champ chaîne JSON qui avale les clés suivantes (sans changer le texte) : repare_ssp.py <fichier> <champ> (AAI)
import sys, json, re
f, champ = sys.argv[1], sys.argv[2]
d = json.load(open(f)); s = d[champ]
o, i = json.JSONDecoder().raw_decode(s)
reste = s[i:].strip()
reste = re.sub(r'^,\s*', '', reste)
reste = re.sub(r'"(\w+)">\s*\[', r'"\1":[', reste)
extra = json.loads("{" + reste + "}")
n = {}
for k, v in d.items():
    n[k] = o if k == champ else v
    if k == "notions":
        for k2, v2 in extra.items(): n[k2] = v2
for k2, v2 in extra.items():
    if k2 not in n: n[k2] = v2
open(f, "w", encoding="utf-8").write(json.dumps(n, ensure_ascii=False, indent=1))
print("ok", f, "clés récupérées", list(extra))
