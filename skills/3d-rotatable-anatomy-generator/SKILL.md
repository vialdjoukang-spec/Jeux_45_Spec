---
name: 3d-rotatable-anatomy-generator
description: "Génère de la vraie anatomie 3D rotative (organe, région, corps) à partir de volumes voxel réels de haute qualité (CT, IRM, micro-CT synchrotron, Visible Human) : sources volumiques libres, segmentation, maillage, GLB et visionneuse HTML. S'active dès qu'il faut une anatomie 3D tournable produite à partir de données volumiques, ou quand on cherche où trouver des volumes 3D, même sans le mot « voxel » ; jamais de SVG."
---

# 3D rotatable anatomy generator

Ce skill fabrique une anatomie 3D qu'on tourne à la souris à partir d'un patient ou d'un organe réellement scanné. La forme vient donc du voxel, pas d'un dessin, ce qui garantit des proportions et des rapports anatomiques vrais.

**Relais.** Quand il faut un maillage tout prêt (BodyParts3D, Z-Anatomy), un cliché plat ou une photo, passe la main à `3d-images-upload-super`. Ce skill-ci intervient quand on part d'un **volume** (série de coupes) pour produire la 3D. Il vérifie les faits médicaux affichés avec `medical-accuracy-100` et range les organes selon `organ-catalog-great-master`.

Scripts et visionneuse : github.com/vialdjoukang-spec/Jeux_45_Spec/tree/main/skills/3d-rotatable-anatomy-generator (`scripts/voxel_vers_glb.py`, `assets/visionneuse.html`, `references/sources.md`). Clone ce dossier si les fichiers ne sont pas à côté du skill.

## 1. Choisir la source (de la plus fine à la plus pratique)
Le détail est dans `references/sources.md` (licence, taille, accès). L'essentiel :
- **Human Organ Atlas (ESRF, HiP-CT)** offre des organes entiers jusqu'au niveau cellulaire (≈ 20 µm, zooms à quelques µm), sous CC BY 4.0. C'est la qualité la plus haute, pour un organe isolé.
- **TotalSegmentator (Hôpital universitaire de Bâle)** offre 1 228 CT cliniques avec 117 structures déjà segmentées, plus 616 IRM. C'est la voie la plus rapide pour un organe en situation dans le corps.
- **Visible Human / Visible Korean** offrent des corps entiers en cryosections couleur. On les utilise pour une vue en couleurs réelles.
- **Medical Segmentation Decathlon, IXI, OpenNeuro, BigBrain** couvrent les organes ciblés, l'IRM cérébrale et le cerveau à 20 µm.
- **Si aucune source listée ne couvre la structure**, cherche le volume sur le web (WebSearch « <organe> NIfTI dataset », « micro-CT <organe> open data ») ; après deux recherches vaines, lance le skill `deep-research`. Garde seulement un volume réel avec une licence lisible.

## 2. Chaîne de fabrication
1. **Télécharger.** Le shell du bac à sable n'atteint ni Zenodo ni l'ESRF. Fais donc tourner le téléchargement dans GitHub Actions (Internet gratuit), sur l'ordinateur de l'utilisateur, ou commence par le sous-ensemble de 102 sujets de TotalSegmentator.
2. **Segmenter si le volume est brut.** Lance `pip install TotalSegmentator`, puis `TotalSegmentator -i ct.nii.gz -o seg --ml --fast`. Le mode `--fast` tourne sur CPU ; `--roi_subset` limite le calcul aux organes voulus.
3. **Mailler.** Lance `scripts/voxel_vers_glb.py etiquettes.nii.gz -o organe.glb --noms noms.json --garder 10,11,51`. Le script garde l'échelle réelle en mm, lisse sans réduire le volume (Taubin), allège le maillage et nomme chaque structure. Pour un CT brut sans étiquettes, `--seuil 300` extrait l'os.
4. **Afficher.** Copie `assets/visionneuse.html` à côté du `.glb`, puis ouvre `visionneuse.html?glb=organe.glb&titre=…&source=…`. La page offre la rotation libre ou automatique, les vues de face, de profil et de dessus, l'affichage de chaque structure à la demande et la transparence. Pour montrer le volume lui-même (coupes et rendu volumique), utilise NiiVue (`@niivue/niivue`), qui lit directement le NIfTI dans le navigateur.
5. **Vérifier.** Ouvre une capture de face et une de profil. Contrôle la latéralité sur une structure asymétrique : la pointe du cœur doit être à gauche du patient et le foie à droite. Contrôle aussi les volumes affichés par le script (poumon ≈ 2–3 L, rein ≈ 150 mL).

## 3. Règles
- **Pas de SVG**, jamais, ni de forme dessinée à la main : chaque surface vient d'un voxel réel.
- Occulte toujours les organes génitaux externes : retire leurs étiquettes avec `--garder`, ou coupe le maillage du bassin.
- Écris dans `source=` la provenance exacte et la licence, par exemple « TotalSegmentator v2, sujet s0011 » suivi de la licence lue sur la fiche Zenodo.
- Garde un `.glb` au-dessous de ~15 Mo par organe (option `--faces`), pour qu'il s'ouvre vite sur un téléphone.
- Signe tes productions : AAI (Anthropic AI).

## 4. Dépannage
- Un modèle noir signifie que les normales manquent ; le script les exporte, et la visionneuse les recalcule au besoin.
- Un organe qui apparaît en escalier demande d'augmenter `--lissage` (30–50) ou de partir d'un volume plus fin.
- Si la décimation échoue, installe `fast-simplification` (pip).
