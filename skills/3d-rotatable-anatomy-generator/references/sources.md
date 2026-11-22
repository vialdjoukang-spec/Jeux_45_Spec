# Sources de volumes 3D réels (voxel) — où les trouver

| Source | Contenu | Résolution | Licence | Accès |
|---|---|---|---|---|
| Human Organ Atlas (ESRF/UCL) — human-organ-atlas.esrf.fr | Organes entiers (cerveau, cœur, poumon, rein, foie, rate…) en HiP-CT | ≈ 20 µm l'organe entier, zooms jusqu'à ~2 µm | CC BY 4.0 | Portail de téléchargement, visionneuse Neuroglancer |
| TotalSegmentator CT v2 — zenodo.org/records/10047292 | 1 228 CT cliniques, 117 structures segmentées (organes, os, muscles, vaisseaux) | CT clinique (~1–1,5 mm) | Libre (voir la fiche Zenodo) | 23,6 Go ; sous-ensemble de 102 sujets disponible |
| TotalSegmentator IRM v2 — zenodo.org/records/14710732 | 616 IRM, 50 structures | IRM clinique | Libre (voir la fiche Zenodo) | 5,1 Go |
| Outil TotalSegmentator — github.com/wasserth/TotalSegmentator | Segmente n'importe quel CT/IRM NIfTI ou DICOM | — | Apache 2.0 (outil) | `pip install TotalSegmentator` |
| Visible Human Project (NLM) | Corps entiers homme et femme : cryosections couleur, CT, IRM | 0,33 mm (femme) | Libre d'usage (NLM) | Serveurs NLM |
| Visible Korean | Corps entier, cryosections couleur et segmentations | 0,2 mm | Sur demande | KISTI |
| Medical Segmentation Decathlon | 10 tâches (foie, cœur, poumon, pancréas, prostate, rate, côlon, hippocampe…) | Clinique | CC BY-SA 4.0 | medicaldecathlon.com |
| IXI | ~600 IRM cérébrales de sujets sains | 1 mm | CC BY-SA 3.0 | brain-development.org |
| BigBrain | Cerveau humain entier en histologie 3D | 20 µm | Libre (EBRAINS) | bigbrainproject.org |
| OpenNeuro | Milliers d'IRM cérébrales (BIDS) | Variable | Majoritairement CC0 | openneuro.org (S3 public) |
| TCIA | CT/IRM/PET de patients oncologiques | Clinique | Variable selon la collection | cancerimagingarchive.net |

## Visionneuses navigateur (gratuites)
- **three.js + GLTFLoader** pour les maillages GLB rotatifs : c'est la visionneuse fournie dans `assets/`.
- **NiiVue** (BSD-2) pour le rendu volumique, les coupes et les maillages en superposition ; il lit NIfTI, DICOM, STL et OBJ.
- **Neuroglancer** (Apache 2.0) pour les volumes géants multi-échelles (Human Organ Atlas).
- **VolView / vtk.js** pour le rendu volumique « cinématique » dans le navigateur.

Vérifie toujours la licence sur la fiche officielle avant publication : elle prime sur ce tableau.
