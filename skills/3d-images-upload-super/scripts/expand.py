import csv,collections,subprocess,json,sys
D='/tmp/bp3d/assets/BodyParts3D_data/'
L=set(x.split('/')[-1][:-4] for x in subprocess.run(['git','-C','/tmp/bp3d','ls-tree','-r','--name-only','HEAD'],capture_output=True,text=True).stdout.split() if '/stl/' in x)
ch=collections.defaultdict(set)
for r in csv.reader(open(D+'composite_parts.txt'),delimiter='\t'):
    if len(r)>=3: ch[r[0]].add(r[2])
def ex(i,seen=None):
    seen=seen or set()
    if i in L: return {i}
    out=set()
    for c in ch.get(i,()):
        if c not in seen: seen.add(c); out|=ex(c,seen)
    return out
G={"peau":"FMA7163","coeur":"FMA7088","poumon_d":"FMA7309","poumon_g":"FMA7310","foie":"FMA7197","estomac":"FMA7148","reins":"FMA7203","cerveau":"FMA50801","rate":"FMA7196","pancreas":"FMA7198","grele":"FMA7200","colon":"FMA7201","vessie":"FMA15900","aorte":"FMA3734","diaphragme":"FMA13295","oesophage":"FMA7131","trachee":"FMA7394","crane":"FMA46565","cage":"FMA7480","bassin":"FMA9578","rachis":"FMA13478","femur":"FMA9611","humerus":"FMA13303"}
R={k:sorted(ex(v)) for k,v in G.items()}
json.dump(R,open('/tmp/w/parts.json','w'))
for k,v in R.items(): print(k,len(v))
print(sum(len(v) for v in R.values()))
