# Réparations de forme sûres (sans changer le texte) : forme.py <racine> <id>... (AAI)
import sys, json, glob
R=sys.argv[1]; sys.path.insert(0,R+"/scripts")
import produire_notions_questions as P
def ecrit(f,d): open(f,"w",encoding="utf-8").write(json.dumps(d,ensure_ascii=False,indent=1))
for i in sys.argv[2:]:
    for t,sch in (("notions",P.SCH_NOTIONS),("questions",P.SCH_QUESTIONS),("corrections",P.SCH_CORRECTION)):
        for f in glob.glob(f"{R}/content/{t}/*/{i}.json"):
            d=json.load(open(f)); log=[]
            for k,v in list(d.items()):
                if isinstance(v,str) and v.strip()[:1] in "[{" and k in sch["properties"]:
                    try: d[k]=json.loads(v); log.append(f"champ {k} chaîne→JSON")
                    except Exception as e: log.append(f"!! champ {k} chaîne JSON invalide : {e}")
            if t=="corrections" and isinstance(d.get("notions"),list):
                for b in d["notions"]:
                    tb=b.get("tableau") if isinstance(b,dict) else None
                    if isinstance(tb,dict):
                        for li in tb.get("lignes",[]):
                            for j,cell in enumerate(li):
                                if isinstance(cell,list) and cell and all(isinstance(x,str) for x in cell):
                                    li[j]="; ".join(cell); log.append(f"{b.get('id')} cellule liste→texte")
            if t=="corrections" and isinstance(d.get("notions"),list):
                for b in d["notions"]:
                    p=b.get("points") if isinstance(b,dict) else None
                    while isinstance(p,list) and len(p)>5:
                        p[-2]=p[-2].rstrip()+" "+p[-1]; p.pop(); log.append(f"{b.get('id')} points fusionnés (≤ 5)")
            if t=="questions":
                for q in d["questions"]:
                    if len(q.get("notions",[]))>6: log.append(f"{q['id']} notions liées ramenées à 6 ({q['notions'][6:]})"); q["notions"]=q["notions"][:6]
                pr=sch["properties"]["questions"]["items"]["properties"]
                for q in d["questions"]:
                    for k in [k for k in q if k not in pr]:
                        log.append(f"{q['id']} clé hors schéma « {k} » = {str(q[k])[:40]} retirée"); del q[k]
                    po=pr["options"]["items"].get("properties",{})
                    ps=pr["statements"]["items"].get("properties",{})
                    for o in q.get("statements",[]):
                        for k in [k for k in o if ps and k not in ps]:
                            log.append(f"{q['id']} affirmation clé « {k} » = {str(o[k])[:30]} retirée"); del o[k]
                    for o in q.get("options",[]):
                        for k in [k for k in o if po and k not in po]:
                            log.append(f"{q['id']} option clé « {k} » = {str(o[k])[:30]} retirée"); del o[k]
            if log: ecrit(f,d); print(i,t,"|", " ; ".join(sorted(set(log)))[:600])
