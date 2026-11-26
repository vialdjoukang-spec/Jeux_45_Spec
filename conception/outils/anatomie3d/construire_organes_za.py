"""Organes 3D réels depuis Z-Anatomy (FBX du dépôt Unity-app_Z-Anatomy, CC BY-SA 4.0) et BodyParts3D, un .glb par organe, 0 token.
Lit organes_za.json, télécharge les FBX nécessaires, applique la hiérarchie de transformation, convertit au repère BodyParts3D
(mm, Z vers le haut, face vers -Y, gauche du patient vers +X), allège (≤ 60 000 faces), centre, écrit anatomie3d/<organe>.glb
et fusionne les entrées dans index.json. Les organes déjà dans index.json avec la même empreinte sont sautés (cache).
Signature : AAI (Anthropic AI)"""
import hashlib, json, os, re, subprocess, sys, urllib.request

ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
sys.path.insert(0, ICI)
SORTIE = os.path.join(RAC, "conception", "prototypes", "moteur", "anatomie3d")
CONF = json.load(open(os.path.join(ICI, "organes_za.json"), encoding="utf-8"))
CACHE = os.environ.get("ZA_CACHE", "/tmp/za"); BP = "/tmp/bp3d"; MAXF = 60000; COUL = [178, 34, 52]
URL = "https://raw.githubusercontent.com/Z-Anatomy/Unity-app_Z-Anatomy/HEAD/Resources/Models/FBX/%s.fbx"

import numpy as np, trimesh, fast_simplification as fs  # noqa: E402
import fbxlite  # noqa: E402

_FBX = {}
def fbx(cle):
    if cle not in _FBX:
        p = os.path.join(CACHE, CONF["fichiers"][cle] + ".fbx")
        if not os.path.exists(p):
            os.makedirs(CACHE, exist_ok=True); urllib.request.urlretrieve(URL % CONF["fichiers"][cle], p)
        _FBX[cle] = fbxlite.lire_monde(p)
    return _FBX[cle]

def choisir(cle, motifs, exclure):
    out = []
    for nom, (V, F) in fbx(cle).items():
        if len(F) > 12 and any(re.search(m, nom) for m in motifs) and not any(re.search(x, nom) for x in exclure):
            out.append((nom, V, F))
    return out

def vers_bp3d(V):   # Z-Anatomy : cm, Y haut, face +Z, gauche patient +X  →  BodyParts3D : mm, Z haut, face -Y
    return np.c_[V[:, 0], -V[:, 2], V[:, 1]] * 10.0

def bp_stl(i):
    f = f"{BP}/assets/BodyParts3D_data/stl/{i}.stl"
    if not os.path.exists(f):
        subprocess.run(["git", "-C", BP, "-c", "gc.auto=0", "checkout", "HEAD", "--", f"assets/BodyParts3D_data/stl/{i}.stl"], check=True)
    return trimesh.load(f)

if not os.path.isdir(BP) and any("bp" in o for o in CONF["organes"].values()):
    subprocess.run(["git", "clone", "-q", "--filter=blob:none", "--no-checkout", "https://github.com/Kevin-Mattheus-Moerman/BodyParts3D.git", BP], check=True)

IDX = os.path.join(SORTIE, "index.json"); index = json.load(open(IDX, encoding="utf-8"))
os.makedirs(SORTIE, exist_ok=True); fait = 0
for oid, o in CONF["organes"].items():
    morceaux, noms = [], []
    src = CONF["_meta"]["source_za"]
    if "bp" in o:
        ms = [bp_stl(i) for i in o["bp"]]; noms = list(o["bp"]); src = CONF["_meta"]["source_bp"]
        morceaux = [trimesh.Trimesh(m.vertices, m.faces) for m in ms]
        if "fichier" in o or "multi" in o: src = CONF["_meta"]["source_za"] + " ; " + CONF["_meta"]["source_bp"]
    if "bp" not in o or "fichier" in o or "multi" in o:
        for cle, mot in ([(o["fichier"], None)] if "fichier" in o else []) + [tuple(x) for x in o.get("multi", [])]:
            sel = choisir(cle, o["noms"] if mot is None else [mot], o.get("exclure", [".j$"]) if mot is None else [r"\.j$"])
            for nom, V, F in sel:
                morceaux.append(trimesh.Trimesh(vers_bp3d(V), F)); noms.append(cle + ":" + nom)
    emp = hashlib.sha256(json.dumps([sorted(noms), [len(m.faces) for m in morceaux], MAXF], ensure_ascii=False).encode()).hexdigest()[:16]
    if not morceaux:
        print(f"{oid} : AUCUN maillage trouvé", flush=True); continue
    if index["organes"].get(oid, {}).get("empreinte") == emp and os.path.exists(os.path.join(SORTIE, oid + ".glb")):
        print(f"{oid} : inchangé (cache)", flush=True); continue
    m = trimesh.util.concatenate(morceaux); nf0 = len(m.faces)
    if nf0 > MAXF:
        v, f = fs.simplify(m.vertices.astype(np.float32), m.faces.astype(np.int32), target_reduction=1 - MAXF / nf0); m = trimesh.Trimesh(v, f)
    m.apply_translation(-m.bounds.mean(axis=0))
    m.visual = trimesh.visual.ColorVisuals(m, face_colors=COUL + [255])
    sc = trimesh.Scene(); sc.add_geometry(m, node_name=oid, geom_name=oid); chemin = os.path.join(SORTIE, oid + ".glb"); sc.export(chemin)
    mo = os.path.getsize(chemin) / 1e6
    assert mo < 15, f"{oid} : {mo:.1f} Mo ≥ 15 Mo"
    e = {"nom": o["nom"], "statut": "produit", "pieces": len(morceaux), "faces": len(m.faces), "faces_source": nf0,
         "taille_mm": [round(x) for x in m.extents], "source": src, "empreinte": emp}
    if o.get("note"): e["note"] = o["note"]
    index["organes"][oid] = e; fait += 1
    print(f"{oid} : {len(morceaux)} pièces, {nf0}→{len(m.faces)} faces, {mo:.1f} Mo, {[round(x) for x in m.extents]} mm", flush=True)
meta = index["_meta"]; meta["sources_supplementaires"] = [CONF["_meta"]["source_za"]]; meta["exclus"] = meta.get("exclus", "") 
json.dump(index, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"organes 3D : {sum(1 for x in index['organes'].values() if x['statut'] == 'produit')} produits ; {fait} nouveaux")
