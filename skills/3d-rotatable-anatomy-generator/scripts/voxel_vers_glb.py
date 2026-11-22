"""Volume voxel (NIfTI .nii/.nii.gz ou DICOM converti) → maillages 3D réels → un .glb rotatif (une structure = un objet nommé).
Usage :
  python voxel_vers_glb.py etiquettes.nii.gz -o organe.glb [--noms noms.json] [--couleurs couleurs.json]
         [--garder 1,2,5] [--lissage 20] [--faces 60000] [--seuil 300 (volume brut, pas d'étiquettes)]
Entrée A : carte d'étiquettes (TotalSegmentator, Medical Segmentation Decathlon, atlas) : un entier par structure.
Entrée B : volume brut (CT en UH) + --seuil : surface d'isovaleur (os ≈ 300 UH, peau ≈ -300 UH).
Chaîne : marching cubes à l'échelle réelle des voxels (mm) → lissage de Taubin (garde le volume) → décimation
quadrique → recentrage → glTF binaire. Aucune image dessinée, aucun SVG : la forme vient du patient scanné.
Signature : AAI (Anthropic AI)"""
import argparse, json, sys
import numpy as np
import nibabel as nib
import trimesh
from skimage import measure

PALETTE = [(0.80, 0.33, 0.30), (0.90, 0.72, 0.55), (0.55, 0.20, 0.25), (0.62, 0.42, 0.70), (0.35, 0.55, 0.80),
           (0.45, 0.70, 0.45), (0.95, 0.85, 0.60), (0.75, 0.55, 0.35), (0.40, 0.75, 0.75), (0.85, 0.55, 0.70)]


def maillage(masque, espacement, lissage, faces):
    if masque.sum() < 20:
        return None
    m = np.pad(masque.astype(np.uint8), 1)
    sommets, tri, normales, _ = measure.marching_cubes(m, 0.5, spacing=espacement)
    mesh = trimesh.Trimesh(sommets, tri, vertex_normals=normales, process=True)
    if lissage:
        trimesh.smoothing.filter_taubin(mesh, iterations=lissage)
    if faces and len(mesh.faces) > faces:
        try:
            mesh = mesh.simplify_quadric_decimation(face_count=faces)
        except Exception:
            pass  # fast_simplification absent : on garde le maillage complet
    mesh.fix_normals()
    return mesh


def main():
    a = argparse.ArgumentParser()
    a.add_argument("volume"); a.add_argument("-o", "--sortie", required=True)
    a.add_argument("--noms"); a.add_argument("--couleurs"); a.add_argument("--garder")
    a.add_argument("--lissage", type=int, default=20); a.add_argument("--faces", type=int, default=60000)
    a.add_argument("--seuil", type=float)
    p = a.parse_args()
    img = nib.as_closest_canonical(nib.load(p.volume))   # orientation RAS : droite, avant, haut
    vol = np.asarray(img.dataobj)
    esp = tuple(float(z) for z in img.header.get_zooms()[:3])
    noms = json.load(open(p.noms, encoding="utf-8")) if p.noms else {}
    couleurs = json.load(open(p.couleurs, encoding="utf-8")) if p.couleurs else {}
    if p.seuil is not None:
        masques = {"surface": vol >= p.seuil}
    else:
        etiq = [int(v) for v in np.unique(vol) if v != 0]
        if p.garder:
            etiq = [e for e in etiq if e in {int(x) for x in p.garder.split(",")}]
        masques = {noms.get(str(e), f"structure_{e}"): vol == e for e in etiq}
    scene, bilan = trimesh.Scene(), []
    for i, (nom, masque) in enumerate(masques.items()):
        m = maillage(masque, esp, p.lissage, p.faces)
        if m is None:
            continue
        c = couleurs.get(nom, PALETTE[i % len(PALETTE)])
        m.visual = trimesh.visual.ColorVisuals(m, face_colors=np.tile((np.array(c) * 255).astype(np.uint8).tolist() + [255], (len(m.faces), 1)))
        scene.add_geometry(m, node_name=nom, geom_name=nom)
        bilan.append((nom, len(m.faces), round(m.volume / 1000, 1)))
    if not bilan:
        sys.exit("aucune structure assez grande pour être maillée")
    scene.apply_translation(-scene.bounds.mean(axis=0))   # centre de rotation au milieu de l'objet
    scene.export(p.sortie, include_normals=True)   # normales incluses : éclairage correct partout
    for nom, f, v in bilan:
        print(f"{nom:35s} {f:7d} faces  {v:8.1f} mL")
    print(f"→ {p.sortie}")


if __name__ == "__main__":
    main()
