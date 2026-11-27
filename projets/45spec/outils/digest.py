# Digest compact d'une pathologie pour audit (AAI) : digest.py <racine> <id> [<id>...]
import sys, json, re, glob, os
R=sys.argv[1]
def charge(t,i):
    f=glob.glob(f"{R}/content/{t}/*/{i}.json")
    return (json.load(open(f[0])),f[0]) if f else (None,None)
def chaines(x):
    if isinstance(x,str): yield x
    elif isinstance(x,dict):
        for k,v in x.items():
            if k in("couverture","audit","controles","usage","signature","ladder"): continue
            yield from chaines(v)
    elif isinstance(x,list):
        for v in x: yield from chaines(v)
num=re.compile(r"\d")
for i in sys.argv[2:]:
    n,fn=charge("notions",i); c,fc=charge("corrections",i); q,fq=charge("questions",i)
    print(f"##### {i} | {n['entite'] if n else '?'}")
    tout=" ".join(chaines(n))+" ".join(chaines(c))+" ".join(chaines(q))
    for mot in ("CNP","CPCM","72 h","72 heures","SSP+",".svg"):
        if mot in tout: print("!! contient",mot)
    for t,d in (("N",n),("C",c),("Q",q)):
        for k,v in d.items():
            if isinstance(v,str) and v.strip().startswith(("[","{")): print("!! champ chaîne JSON",t,k)
    vus=set()
    print("-- notions")
    for x in n["notions"]:
        e=x["enonce"]
        if num.search(e) or x.get("nature") in("posologie","molécule","seuil","chiffre"):
            print(f" {x['id']} {e[:260]}"); vus.add(e[:60])
    print("-- PEC posologies")
    pec=c.get("priseEnCharge")
    if isinstance(pec,list):
        for b in pec:
            if not isinstance(b,dict): continue
            ph=(b.get("moyens") or {}).get("pharmacologique",[]) if isinstance(b.get("moyens"),dict) else []
            for m in ph if isinstance(ph,list) else []:
                if isinstance(m,dict): print(f" {m.get('molecule','')[:70]} :: {str(m.get('posologie',''))[:200]}")
    print("-- autres chiffres correction (nouveaux)")
    k=0
    for s in chaines(c.get("notions")):
        for ph in re.split(r"(?<=[.;])\s+",s):
            if num.search(ph) and len(ph)>30 and ph[:60] not in vus and k<5:
                vus.add(ph[:60]); print("  ·",ph[:200]); k+=1
    print("-- questions d>=4")
    for x in q["questions"]:
        if x.get("difficulte",0)>=4:
            print(f" {x['id']} d{x['difficulte']} {x['format']} m={x.get('diagnosticMasque')} | {x['stem'][:150]} || {x['prompt'][:90]}")
