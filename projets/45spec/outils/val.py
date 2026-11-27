# Erreurs de schéma détaillées (chemin), comme controle_menus_longs : val.py <racine> <id>... (AAI)
import sys, json, glob
R=sys.argv[1]; sys.path.insert(0,R+"/scripts")
import produire_notions_questions as P, jsonschema
for i in sys.argv[2:]:
  for t,et,sch in (("notions","notions",P.SCH_NOTIONS),("questions","questions",P.SCH_QUESTIONS),("corrections","correction",P.SCH_CORRECTION)):
    for f in glob.glob(f"{R}/content/{t}/*/{i}.json"):
        d=json.load(open(f)); d={k:v for k,v in d.items() if k in sch["properties"]}
        if t=="notions":
            pr=sch["properties"]["notions"]["items"]["properties"]; d["notions"]=[{k:v for k,v in x.items() if k in pr} for x in d["notions"]]
        es=list(jsonschema.Draft7Validator(sch).iter_errors(d))
        for e in es[:6]:
            print(i,t,list(e.absolute_path),e.message[:120])
        if not es:
            sp=f.split("/")[-2]; c={"codes":[sp],"id":i,"entite":{"nom":json.load(open(f))["entite"]}}
            for m in P.valider(et,d,c): print(i,t,"valider:",m[:160])
