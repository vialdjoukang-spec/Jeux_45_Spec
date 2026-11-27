# Recherche dans BodyParts3D : nom -> FMA, nombre de pièces STL après développement des composites (AAI)
import csv, collections, subprocess, sys, re
B="/tmp/bp3d"; D=B+"/assets/BodyParts3D_data/"
L={x.split("/")[-1][:-4] for x in subprocess.run(["git","-C",B,"ls-tree","-r","--name-only","HEAD"],capture_output=True,text=True).stdout.split() if "/stl/" in x}
ch=collections.defaultdict(set)
for r in csv.reader(open(D+"composite_parts.txt"),delimiter="\t"):
    if len(r)>=3: ch[r[0]].add(r[2])
def ex(i,vu=None):
    vu=vu if vu is not None else set()
    if i in L: return {i}
    o=set()
    for c in ch.get(i,()):
        if c not in vu: vu.add(c); o|=ex(c,vu)
    return o
N=dict(l.rstrip("\n").split("\t")[:2] for l in open(D+"parts_list_e.txt") if l.startswith("FMA"))
for k in sys.argv[1:]:
    print("==",k)
    for f,n in N.items():
        if re.search(k,n,re.I):
            e=ex(f)
            if e: print(f"  {f} {n} [{len(e)}]")
