---
name: 3d-images-upload-super
description: Find, fetch, build and render REAL medical visuals — true 3D anatomy (glTF/STL meshes rendered with three.js), real radiographs/CT/MRI/ultrasound/histology images, and real exercise/workout images — then store them with their source URL. Use whenever a page, game, course or prototype needs anatomy, a 3D body or organ, a medical imaging case (raw + annotated), or exercise pictures, and whenever the user rejects drawn or SVG illustrations. Use deep search when a specific image is hard to find.
---

# 3D images_Upload_super

Rule zero: **no SVG, no hand-drawn illustration** for anatomy, imaging or exercises. Real meshes, real clichés, real photos. External genitalia are always occulted on full-body renders.

## 1. Where to get what (fastest first)
| Need | Source | Access |
|---|---|---|
| Whole body / organs 3D | **BodyParts3D** STL by FMA id — github.com/Kevin-Mattheus-Moerman/BodyParts3D (`assets/BodyParts3D_data/stl/FMA*.stl`, map in `composite_parts.txt`) | git (works from sandbox) |
| Richer 3D (muscles, nerves, vessels, labels) | **Z-Anatomy** (github.com/Z-Anatomy), NIH 3D (3d.nih.gov), Sketchfab download API, AnatomyTOOL Open 3D Model | git / web |
| Radiology (Rx, CT, MRI, US) | ieee8023/covid-chestxray-dataset (GitHub, metadata.csv with finding/view/url), **Open-i** NLM API (openi.nlm.nih.gov/services, filter by image type), Radiopaedia, Wikimedia Commons, MedPix, TCIA, NIH ChestX-ray14, MedMNIST | git / web |
| Histology, dermatology, clinical photos | Open-i (PubMed Central figures), Wikimedia Commons, DermNet | web |
| Exercises / workout | **free-exercise-db** (github.com/yuhonas/free-exercise-db, 800+ exercises, images at raw.githubusercontent.com/yuhonas/free-exercise-db/main/dist/exercises/…), wger API, exercises.json | git / web |

Sandbox note: the cloud shell usually reaches only GitHub and package registries. Prefer GitHub-hosted datasets; otherwise use WebSearch/WebFetch to locate, or the user's own computer (device bridge) to download.

**Deep search** (use when the first two searches miss): query by finding + view + modality ("PA chest radiograph right middle lobe pneumonia silhouette sign"), filter Open-i by image type, check dataset `metadata.csv` columns (finding, view, modality), and read the case page to confirm the diagnosis before annotating.

## 2. Pipeline for a real 3D body (bundled scripts)
1. `scripts/expand.py` — expands composite organs (heart, lungs, skull, rib cage…) into the primitive FMA STL files that exist, via `composite_parts.txt`.
2. Fetch only those files (blobless clone, then `git -c gc.auto=0 checkout HEAD --pathspec-from-file=paths.txt`). Never run `git ls-tree -l` on a blobless clone: it downloads every blob.
3. `scripts/build_glb.py` — merges per organ, decimates with `fast-simplification` (skin ≈ 120 k faces, organs ≈ 25 k), colours per organ, exports one `corps.glb` (~11 MB).
4. Render with three.js (`MeshPhysicalMaterial`, ACES tone mapping, hemisphere + 2 directional lights). Skin translucent (opacity 0.15–0.25, `depthWrite:false`).
5. **Genital occultation**: discard skin fragments inside a pelvic box in the fragment shader (BodyParts3D coords, Z up, −Y front: box x −58…58, y −230…−60, z 630…790). No organ mesh of the external genitalia is loaded.
6. Screenshot headless: Chromium `--use-angle=swiftshader --enable-unsafe-swiftshader`, wait for a ready flag, `page.screenshot` (`scripts/shot.py`).
Orientation: camera at −Y looking +Y with up +Z gives the anatomical front view (patient's left on viewer's right).

## 3. Imaging case = two-image window
Store each case as JSON: `clicheBrut {src, url}`, `clicheAnnote {src, reperes[] {n, x, y, rx, ry, texte}}` in original pixel coordinates, `lesions[]`, `diagnostic`, `conduite`. Draw annotations on canvas 2D over the second copy (numbered ellipses, dashed for a sign by absence). Every repère gets one verbal sentence in the numbered legend. Verify laterality markers (L/R) before writing "droit/gauche".

## 4. Upload / storage
- Keep originals untouched; write resized web copies (≤ 1600 px long side, JPEG q85 / WebP).
- Manifest `images.json`: `{id, fichier, url, source, modalite, region, constat}` — the URL lets anyone replace the image later.
- Commit images with the content repo or upload as artifact assets; one manifest per module.

## 5. Check before delivering
Open each rendered PNG: anatomy recognisable, no exposed genitalia, annotations on the right structure and side, captions in verbal sentences, file sizes reasonable.
