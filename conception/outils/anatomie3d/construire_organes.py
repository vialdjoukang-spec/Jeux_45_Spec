"""Organes 3D réels, un fichier .glb par organe (0 token), depuis BodyParts3D (maillages issus de données d'imagerie réelles).
Lit organes_fma.json (organe du réseau → identifiants FMA), développe les composites en pièces primitives, télécharge seulement
ces pièces, les fusionne, les allège (≈ 30 000 faces), les centre et écrit conception/prototypes/moteur/anatomie3d/<organe>.glb
et index.json. Réutilisable par toutes les plateformes. Signature : AAI (Anthropic AI)"""
import csv, collections, json, os, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
SORTIE = os.path.join(RAC, "conception", "prototypes", "moteur", "anatomie3d"); BP = "/tmp/bp3d"; D = BP + "/assets/BodyParts3D_data/"
CONF = json.load(open(os.path.join(ICI, "organes_fma.json"), encoding="utf-8"))
COUL = [178, 34, 52]


def git(*a):
    return subprocess.run(["git", "-C", BP, "-c", "gc.auto=0", *a], check=True, capture_output=True, text=True).stdout


if not os.path.isdir(BP):
    subprocess.run(["git", "clone", "-q", "--filter=blob:none", "--no-checkout", "https://github.com/Kevin-Mattheus-Moerman/BodyParts3D.git", BP], check=True)
git("checkout", "HEAD", "--", "assets/BodyParts3D_data/composite_parts.txt")
L = {x.split("/")[-1][:-4] for x in git("ls-tree", "-r", "--name-only", "HEAD").split() if "/stl/" in x}
ch = collections.defaultdict(set)
for r in csv.reader(open(D + "composite_parts.txt"), delimiter="\t"):
    if len(r) >= 3:
        ch[r[0]].add(r[2])


def ex(i, vu=None):
    vu = vu if vu is not None else set()
    if i in L:
        return {i}
    out = set()
    for c in ch.get(i, ()):
        if c not in vu:
            vu.add(c); out |= ex(c, vu)
    return out


pieces = {oid: sorted(set().union(*[ex(f) for f in o["fma"]])) for oid, o in CONF["organes"].items()}
besoin = sorted({p for v in pieces.values() for p in v if not os.path.exists(f"{D}stl/{p}.stl")})
if besoin:
    open("/tmp/pieces.txt", "w").write("\n".join(f"assets/BodyParts3D_data/stl/{p}.stl" for p in besoin) + "\n")
    git("checkout", "HEAD", "--pathspec-from-file=/tmp/pieces.txt")

import numpy as np, trimesh, fast_simplification as fs  # noqa: E402
os.makedirs(SORTIE, exist_ok=True); index = {}
for oid, ps in pieces.items():
    if not ps:
        index[oid] = {"nom": CONF["organes"][oid]["nom"], "statut": "à produire (pièce absente de BodyParts3D)"}; continue
    m = trimesh.util.concatenate([trimesh.load(f"{D}stl/{p}.stl") for p in ps])
    if CONF["organes"][oid].get("rogner"):   # occultation des organes génitaux externes : faces retirées dans la boîte pelvienne
        (x0, x1), (y0, y1), (z0, z1) = CONF["organes"][oid]["rogner"]; c = m.triangles_center
        m.update_faces(~((c[:, 0] > x0) & (c[:, 0] < x1) & (c[:, 1] > y0) & (c[:, 1] < y1) & (c[:, 2] > z0) & (c[:, 2] < z1))); m.remove_unreferenced_vertices()
    if len(m.faces) > 30000:
        v, f = fs.simplify(m.vertices.astype(np.float32), m.faces.astype(np.int32), target_reduction=1 - 30000 / len(m.faces)); m = trimesh.Trimesh(v, f)
    m.apply_translation(-m.bounds.mean(axis=0))
    m.visual = trimesh.visual.ColorVisuals(m, face_colors=COUL + [255])
    sc = trimesh.Scene(); sc.add_geometry(m, node_name=oid, geom_name=oid); sc.export(os.path.join(SORTIE, oid + ".glb"))
    index[oid] = {"nom": CONF["organes"][oid]["nom"], "statut": "produit", "pieces": len(ps), "faces": len(m.faces),
                  "taille_mm": [round(x) for x in m.extents], "source": CONF["_meta"]["source"]}
    if CONF["organes"][oid].get("note"):
        index[oid]["note"] = CONF["organes"][oid]["note"]
    print(f"{oid} : {len(ps)} pièces, {len(m.faces)} faces", flush=True)
json.dump({"_meta": CONF["_meta"], "organes": index}, open(os.path.join(SORTIE, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"organes 3D : {sum(1 for x in index.values() if x['statut'] == 'produit')} produits / {len(index)}")
