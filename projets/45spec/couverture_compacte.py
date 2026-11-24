"""Contrôle de couverture d une forme compacte 45 Spec (0 token). AAI (Anthropic AI)"""
import importlib.util,sys,collections
sp=importlib.util.spec_from_file_location("m",sys.argv[1]);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
par=collections.defaultdict(list)
for i,q in enumerate(m.Q):
    for n in q["n"]: par[n].append((i+1,q["a"]))
for k,(r,na,p,*_ ) in enumerate(m.N,1):
    L=par[k];ok=bool(L) if p==1 else (len(L)>=2 and len({a for _,a in L})>=2)
    if not ok: print(f"N{k:02d} p{p} {L}")
import collections as C2
w=C2.Counter(n[2] for n in m.N); t=len(m.N)
if w[3]>0.15*t or w[2]>0.35*t: print("POIDS hors règle",dict(w),t)
