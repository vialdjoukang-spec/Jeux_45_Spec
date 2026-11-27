# Remplace des notions d'une forme compacte par clé : editn.py <fichier> <fichier_json {cle: [rub,nature,poids,suisse,src_expr,enonce]}> (AAI)
import sys, json, re
f, j = sys.argv[1], sys.argv[2]
s = open(f, encoding="utf-8").read(); D = json.load(open(j, encoding="utf-8"))
for k, (rub, nat, p, sw, src, en) in D.items():
    pat = re.compile(r'^\("' + re.escape(k) + r'",.*\),\s*$', re.M)
    assert len(pat.findall(s)) == 1, k
    new = '("%s","%s","%s",%d,%d,%s,%s),' % (k, rub, nat, p, sw, src, json.dumps(en, ensure_ascii=False))
    s = pat.sub(lambda m: new, s)
open(f, "w", encoding="utf-8").write(s); print("ok", len(D))
