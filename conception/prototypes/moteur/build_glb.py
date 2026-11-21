import json,trimesh,numpy as np,fast_simplification as fs
R=json.load(open('/tmp/w/parts.json')); S='/tmp/bp3d/assets/BodyParts3D_data/stl/'
COL={"peau":[232,190,170,255],"coeur":[178,34,52,255],"poumon_d":[214,120,130,255],"poumon_g":[214,120,130,255],"foie":[122,46,36,255],"estomac":[214,150,120,255],"reins":[150,50,40,255],"cerveau":[230,180,175,255],"rate":[110,40,70,255],"pancreas":[235,190,120,255],"grele":[228,170,150,255],"colon":[200,140,110,255],"vessie":[220,190,110,255],"aorte":[200,30,40,255],"diaphragme":[170,70,70,255],"oesophage":[200,120,110,255],"trachee":[220,210,200,255],"crane":[238,230,210,255],"cage":[238,230,210,255],"bassin":[238,230,210,255],"rachis":[238,230,210,255],"femur":[238,230,210,255],"humerus":[238,230,210,255]}
TGT={"peau":120000,"cerveau":40000}
sc=trimesh.Scene(); meta={}
for k,ps in R.items():
    ms=[trimesh.load(S+p+'.stl') for p in ps]
    m=trimesh.util.concatenate(ms)
    t=TGT.get(k,25000)
    if len(m.faces)>t:
        v,f=fs.simplify(m.vertices.astype(np.float32),m.faces.astype(np.int32),target_reduction=1-t/len(m.faces))
        m=trimesh.Trimesh(v,f)
    m.visual=trimesh.visual.ColorVisuals(m,face_colors=COL[k])
    sc.add_geometry(m,node_name=k,geom_name=k); meta[k]=[m.bounds.tolist(),len(m.faces)]
sc.export('/tmp/w/corps.glb'); json.dump(meta,open('/tmp/w/meta.json','w'))
import os;print(os.path.getsize('/tmp/w/corps.glb')/1e6,'MB'); print({k:v[1] for k,v in meta.items()}); print('peau',meta['peau'][0])
