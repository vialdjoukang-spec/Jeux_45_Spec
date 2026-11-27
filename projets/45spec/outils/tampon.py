# Tamponne audit.claude dans notions, corrections, questions : tampon.py <racine> <id> <verdict> [à vérifier...] (AAI)
import sys, json, glob
R,i,v=sys.argv[1],sys.argv[2],sys.argv[3]; av=sys.argv[4:]
for t in ("notions","corrections","questions"):
    for f in glob.glob(f"{R}/content/{t}/*/{i}.json"):
        d=json.load(open(f)); a=d.get("audit") or {}
        if not isinstance(a,dict): a={}
        a.setdefault("rejector",None)
        a["claude"]={"verdict":v,"date":"2026-11-26","aVerifier":av,"audit":"AUDIT_V3_B"}
        d["audit"]=a; open(f,"w",encoding="utf-8").write(json.dumps(d,ensure_ascii=False,indent=1))
print(i,v)
