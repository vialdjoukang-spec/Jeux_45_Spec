"""Organes 3D réels hors Z-Anatomy / BodyParts3D, un .glb par organe, 0 token.
Deux voies, lues dans organes_ext.json :
  - « maillages » : maillages réels publiés (PLY/STL), pris dans une archive Zenodo distante (lecture partielle HTTP, remotezip) ;
  - « totalseg »  : scanner réel du jeu TotalSegmentator, segmenté par une tâche ouverte (Apache-2.0) de TotalSegmentator ;
  - « volume »    : étiquettes segmentées d'un examen réel (NIfTI), maillées par marching cubes dans le repère du scanner,
                    converties au repère BodyParts3D (mm, Z haut, face vers -Y, gauche du patient vers +X = LPS), lissées (Taubin).
Chaque maillage est allégé (≤ 60 000 faces), centré, écrit dans anatomie3d/<organe>.glb (< 15 Mo) et fusionné dans index.json.
Cache : un organe dont l'empreinte (configuration + taille des fichiers source) n'a pas changé et dont le .glb existe est sauté.
Dépendances : pip install trimesh fast-simplification remotezip nibabel scikit-image
Signature : AAI (Anthropic AI)"""
import hashlib, json, os, subprocess, sys

import numpy as np, trimesh, fast_simplification as fs
from remotezip import RemoteZip

ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
SORTIE = os.path.join(RAC, "conception", "prototypes", "moteur", "anatomie3d")
CONF = json.load(open(os.path.join(ICI, "organes_ext.json"), encoding="utf-8"))
CACHE = os.environ.get("EXT_CACHE", "/tmp/anat_ext"); MAXF = 60000; COUL = [178, 34, 52]


def extraire(url, membre):
    """Extrait un seul membre d'une archive zip distante (requêtes HTTP Range), avec cache disque."""
    base = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest()[:10]); cible = os.path.join(base, membre)
    if not os.path.exists(cible):
        with RemoteZip(url) as z:
            z.extract(membre, base)
    return cible


def volume_vers_maillage(chemin, etiquettes, lissage, flou_mm):
    import nibabel as nib
    from skimage import measure
    im = nib.load(chemin); a = np.asarray(im.dataobj)
    masque = np.isin(a, etiquettes)
    if masque.sum() == 0:
        raise SystemExit(f"{chemin} : aucune des étiquettes {etiquettes}")
    idx = np.argwhere(masque); lo = np.maximum(idx.min(0) - 2, 0); hi = idx.max(0) + 3
    from scipy import ndimage
    sous = np.pad(masque[lo[0]:hi[0], lo[1]:hi[1], lo[2]:hi[2]].astype(np.float32), 1)
    z = np.array(im.header.get_zooms()[:3], float); iso = z.min(); fac = z / iso   # rééchantillonnage isotrope : supprime les marches entre coupes
    sous = ndimage.gaussian_filter(ndimage.zoom(sous, fac, order=1), sigma=np.array(flou_mm, float) / iso)   # flou en mm (x, y, z) : lisse les contours tracés coupe par coupe
    V, F, _, _ = measure.marching_cubes(sous, 0.5)
    V = V / fac - 1 + lo                                             # indices voxel du volume entier
    W = nib.affines.apply_affine(im.affine, V)                       # RAS (mm)
    W = np.c_[-W[:, 0], -W[:, 1], W[:, 2]]                           # RAS → LPS = repère BodyParts3D
    m = trimesh.Trimesh(W, F, process=True)
    trimesh.smoothing.filter_taubin(m, iterations=lissage)
    m.fix_normals()
    vol_ml = float(masque.sum() * abs(np.linalg.det(im.affine[:3, :3])) / 1000)
    return m, vol_ml


CODE = hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:12]   # un changement du script relance tout
IDX = os.path.join(SORTIE, "index.json"); index = json.load(open(IDX, encoding="utf-8"))
os.makedirs(SORTIE, exist_ok=True); fait = 0
for oid, o in CONF["organes"].items():
    emp = hashlib.sha256(json.dumps([o, MAXF, CODE], ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:16]
    chemin = os.path.join(SORTIE, oid + ".glb")
    if index["organes"].get(oid, {}).get("empreinte") == emp and os.path.exists(chemin):
        print(f"{oid} : inchangé (cache)", flush=True); continue
    morceaux, extra = [], {}
    if o["voie"] == "maillages":
        for mb in o["membres"]:
            m = trimesh.load(extraire(o["zip"], mb), force="mesh"); morceaux.append(trimesh.Trimesh(m.vertices, m.faces))
    elif o["voie"] == "volume":
        m, ml = volume_vers_maillage(extraire(o["zip"], o["membre"]), o["etiquettes"], o.get("lissage", 30), o.get("flou_mm", [0.6, 0.6, 0.6]))
        morceaux.append(m); extra["volume_ml"] = round(ml, 1)
    elif o["voie"] == "totalseg":   # scanner réel segmenté par TotalSegmentator (tâche ouverte Apache-2.0), puis maillé
        ct = extraire(o["zip"], o["membre"]); dos = os.path.join(CACHE, "ts_" + o["tache"] + "_" + hashlib.sha1(o["membre"].encode()).hexdigest()[:8])
        etiq = os.path.join(dos, o["classe"] + ".nii.gz")
        if not os.path.exists(etiq):
            subprocess.run(["TotalSegmentator", "-i", ct, "-o", dos, "-ta", o["tache"], "--device", "cpu"], check=True)
        m, ml = volume_vers_maillage(etiq, [1], o.get("lissage", 30), o.get("flou_mm", [0.6, 0.6, 0.6]))
        morceaux.append(m); extra["volume_ml"] = round(ml, 1)
    else:
        raise SystemExit(f"{oid} : voie inconnue {o['voie']}")
    m = trimesh.util.concatenate(morceaux); nf0 = len(m.faces)
    if nf0 > MAXF:
        v, f = fs.simplify(m.vertices.astype(np.float32), m.faces.astype(np.int32), target_reduction=1 - MAXF / nf0); m = trimesh.Trimesh(v, f)
    m.apply_translation(-m.bounds.mean(axis=0))
    m.visual = trimesh.visual.ColorVisuals(m, face_colors=COUL + [255])
    sc = trimesh.Scene(); sc.add_geometry(m, node_name=oid, geom_name=oid); sc.export(chemin)
    mo = os.path.getsize(chemin) / 1e6
    assert mo < 15, f"{oid} : {mo:.1f} Mo ≥ 15 Mo"
    e = {"nom": o["nom"], "statut": "produit", "pieces": len(morceaux), "faces": len(m.faces), "faces_source": nf0,
         "taille_mm": [round(x) for x in m.extents], "source": o["source"], "empreinte": emp, **extra}
    if o.get("note"): e["note"] = o["note"]
    index["organes"][oid] = e; fait += 1
    print(f"{oid} : {len(morceaux)} pièces, {nf0}→{len(m.faces)} faces, {mo:.2f} Mo, {[round(x) for x in m.extents]} mm {extra}", flush=True)
meta = index["_meta"]; sup = meta.get("sources_supplementaires", [])
for s in CONF["_meta"]["sources"]:
    if s not in sup: sup.append(s)
meta["sources_supplementaires"] = sup
json.dump(index, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"organes 3D : {sum(1 for x in index['organes'].values() if x['statut'] == 'produit')} produits ; {fait} nouveaux")
