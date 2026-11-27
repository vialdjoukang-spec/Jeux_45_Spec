# Vérifie qu'aucune question sans m=0 ne nomme les mots interdits dans st/p (AAI)
import sys, importlib.util, re
sys.path.insert(0,'projets/45spec')
s=importlib.util.spec_from_file_location("m",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
mots=[w.lower() for w in sys.argv[2:]]
for i,q in enumerate(m.Q,1):
    if q.get("m",1)==0: continue
    t=(q["st"]+" "+q["p"]).lower()
    for w in mots:
        if w in t: print("Q",i,"d",q["d"],"contient",w)
print("d45 masqués:",sum(1 for q in m.Q if q["d"]>=4 and "m" not in q),"| d12:",sum(1 for q in m.Q if q["d"]<=2))
