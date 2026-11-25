#!/usr/bin/env python3
"""Construit les JSON destinés à Gemini (catalogue officiel + SSP+ v2). 0 token. Signature : AAI (Anthropic AI)"""
import json,os,sys,collections
OUT=sys.argv[1] if len(sys.argv)>1 else 'data/gemini_qcm'
os.makedirs(OUT,exist_ok=True)
idx=json.load(open('data/ssp/INDEX.json'))
v2=[x for x in json.load(open('projets/ssp_plus/ssp_plus_v2.json')) if x.get('code')]
LIB={'G':'Plaintes générales (G)','S':'Symptômes et signes (S)','F':'Résultats d\'examens — findings (F)','O':'Situations cliniques et prévention (O)'}
NOM={'G':'SSP_G_plaintes_generales','S':'SSP_S_symptomes_signes','F':'SSP_F_resultats_examens','O':'SSP_O_situations_cliniques'}
off=collections.defaultdict(list)
for e in idx['ssp']:
    d=json.load(open(e['fichier']));c=d['ssp'][0]
    off[c].append({'code':d['ssp'],'lot':d['lot'],'nom':d['nom'],'circuit':d['circuit'],
      'groupesSystemes':[{'systeme':g['system'],'nbEtiologies':g['count'],'mnemonique':g.get('mnemonic')} for g in d['groupesSystemes']],
      'diagnosticsDifferentiels':[{'id':x['id'],'nom':x['nom'],'cim10':x.get('cim10'),'systeme':x.get('systeme'),'strate':x.get('strate'),'urgence':x.get('urgence'),'note':x.get('note'),
         'notionsMaitrise':[{'rubrique':n['rubrique'],'poids':n['poids'],'notion':n['amorce']} for n in x['notions']]} for x in d['entites']]})
plus=collections.defaultdict(list)
for x in v2:
    plus[x['categorie']].append({k:x.get(k) for k in ('code','ancienCode','statut','parentOfficiel','intitule','intituleEN','typeDepart','pourquoi','diagnosticsDifferentiels','sources')})
LEG={'codePlus':"Un SSP+ porte « (+) » à droite de son code. G : la numérotation continue après G16 (G17(+), G18(+)…). S, F, O : elle continue après le dernier numéro officiel du groupe parent (S1.24(+) suit S1.23). Un SSP+ n'est jamais un SSP du catalogue officiel.",
 'strate':{'TF':'très fréquent','F':'fréquent','MF':'moins fréquent','R':'rare (piège classique)','null':'non renseignée'},
 'poids':{'3':'notion indispensable','2':'notion importante','1':'notion d\'appui'},
 'circuit':{'MONOGRAPHIQUE':'le SSP mène surtout à une entité dominante','NON_MONOGRAPHIQUE':'le SSP ouvre un vrai diagnostic différentiel'}}
def ecrire(nom,cat,offs,pl,partie=None):
    doc={'titre':nom.replace('_',' ')+(f' — partie {partie}' if partie else ''),'categorie':LIB[cat],
     'contexte':f"Catalogue officiel PROFILES 2023 de l'examen fédéral suisse de médecine, catégorie {LIB[cat]} : chaque SSP officiel avec ses diagnostics différentiels (CIM-10, strate, urgence) et les notions pondérées à maîtriser. La section sspPlus donne les points de départ hors catalogue ({cat}+), rattachés à un SSP officiel de même lettre, avec leurs diagnostics différentiels (sans notions détaillées).",
     'source':'Cartographie Renouveau et projets/ssp_plus/ssp_plus_v2.json (dépôt Jeux_45_Spec), contexte clinique suisse. Signature : AAI (Anthropic AI)','version':'2026-11-25','legende':LEG,
     'compteurs':{'sspOfficiels':len(offs),'diagnosticsDifferentiels':sum(len(s['diagnosticsDifferentiels']) for s in offs),'notionsMaitrise':sum(len(x['notionsMaitrise']) for s in offs for x in s['diagnosticsDifferentiels']),'sspPlus':len(pl)},
     'sspOfficiels':offs,'sspPlus':pl}
    p=os.path.join(OUT,nom+'.json');json.dump(doc,open(p,'w'),ensure_ascii=False,separators=(',',':'))
    print(p,doc['compteurs'],round(os.path.getsize(p)/3.6e6,2),'M tokens env.')
for c in 'GFO': ecrire(NOM[c]+'_et_'+c+'+',c,off[c],plus[c])
# S coupé en deux : groupes S1–S4 / S5–S9 (aucun SSP coupé de ses SSP+)
grp=lambda code:int(code[1:].split('.')[0].split('(')[0])
for i,(a,b) in enumerate(((1,4),(5,9)),1):
    ecrire(f"{NOM['S']}_et_S+_partie{i}_S{a}-S{b}",'S',[s for s in off['S'] if a<=grp(s['code'])<=b],[p for p in plus['S'] if a<=grp(p['code'])<=b],f"{i} (S{a} à S{b})")
