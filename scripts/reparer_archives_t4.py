"""Réparation de forme 0 token des fiches archivées T4 : aucune phrase médicale n'est écrite ni retirée."""
import json,glob,jsonschema,sys,collections
S=json.load(open('scripts/schema_fiche.json')); P=S['properties']; META={'id','ssp','entite','cim10','specialtyIds','notionRefs','poidsNotions','controles','signature','audit','motif_archive','traitement'}
def parse(v):
    if isinstance(v,str) and v.strip()[:1] in '[{':
        for fin in ("","}","]}","]","\"}]","\"}"):
            try: return json.loads(v.strip()+fin)
            except ValueError: pass
    return v
def rep(d):
    for k in list(d):
        if k in META: continue
        d[k]=parse(d[k])
        if k.strip()!=k and k.strip() in P and k.strip() not in d: d[k.strip()]=d.pop(k)
    pr=d.get('presentation')
    if isinstance(pr,dict):
        if 'atypique' in pr: pr['atypique']=parse(pr['atypique'])
        if pr.get('atypique')=='' : pass
        if 'atypique' not in pr and 'atypique' in d: pr['atypique']=d.pop('atypique')
    if isinstance(pr,dict):
        for k in list(pr):
            if k.strip()!=k and k.strip() not in pr: pr[k.strip()]=pr.pop(k)
    for n in d.get('notionsCouvertes') or []:
        if isinstance(n,dict) and 'développement' in n and 'developpement' not in n: n['developpement']=n.pop('développement')
    for g in d.get('drapeauxRouges') or []:
        if isinstance(g,dict) and 'ordre' in g and 'ordre' not in P['drapeauxRouges'].get('items',{}).get('properties',{}): g.pop('ordre')
    return d
res=collections.Counter(); reste=collections.Counter(); ok=[]
for p in sorted(glob.glob('content/fiches/_archives/*/*.json')):
    d=json.load(open(p)); rep(d)
    core={k:v for k,v in d.items() if k not in META}
    es=list(jsonschema.Draft7Validator(S).iter_errors(core))
    manq=[k for k in S['required'] if k not in core]
    if not es: ok.append(p); res['valide']+=1
    elif manq: res['tronquee']+=1
    else: res['forme']+=1; [reste.__setitem__((str(list(e.path)[:2]),e.message[:80]),reste[(str(list(e.path)[:2]),e.message[:80])]+1) for e in es]
    if '--ecrire' in sys.argv and not es: json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(dict(res)); [print(v,k) for k,v in reste.most_common(15)]
pass
