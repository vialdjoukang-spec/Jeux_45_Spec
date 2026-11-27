# Modifie des questions : qset.py <racine> <id> Q10:d3 Q04:m ... (d3 = difficulté 3 ; m = diagnosticMasque true) (AAI)
import sys, json, glob
R,i=sys.argv[1],sys.argv[2]; f=glob.glob(f"{R}/content/questions/*/{i}.json")[0]; d=json.load(open(f))
Q={q["id"]:q for q in d["questions"]}
for a in sys.argv[3:]:
    k,v=a.split(":")
    if v.startswith("d"): Q[k]["difficulte"]=int(v[1:])
    elif v=="m": Q[k]["diagnosticMasque"]=True
    elif v=="M": Q[k]["diagnosticMasque"]=False
    print(i,k,v)
open(f,"w",encoding="utf-8").write(json.dumps(d,ensure_ascii=False,indent=1))
