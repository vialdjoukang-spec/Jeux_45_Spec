---
name: obsidian-like-complex-network
description: Draw dense, readable Obsidian-style networks (canvas graphs, concept maps, diagnostic circuits, mind maps) with straight horizontal links and bracket/bus connectors (fan-in convergence, perfect symmetry), arrowheads, typed colours, and optional anchoring on a real 3D model or a real image. Use whenever the user asks for an "Obsidian-like" graph, a canvas/JSON Canvas, a network of linked notions, a decision tree, organ → sign → syndrome → diagnosis circuits, or any connection-heavy visual — even if they don't say "Obsidian". Never draws images in SVG.
---

# Obsidian-like amazing complex Network

Goal: a network that reads like an Obsidian canvas — calm nodes, **straight** links (bracket/bus connectors) that leave a node **by one side** and enter the next **by the facing side**, an arrowhead at the arrival, and zero visual chaos even with 50+ links.

## 1. Data first: JSON Canvas 1.0 (open spec, jsoncanvas.org)
Store every network as JSON Canvas, so it opens in Obsidian and in our engine:
```json
{"nodes":[{"id":"coeur","type":"text","text":"Cœur","x":0,"y":0,"width":160,"height":56,"color":"1"}],
 "edges":[{"id":"e1","fromNode":"coeur","fromSide":"right","toNode":"galop","toSide":"left","toEnd":"arrow","label":"auscultation","color":"#ff6b6b"}]}
```
`fromSide`/`toSide` ∈ top|right|bottom|left; `toEnd` arrow by default; colours "1"–"6" or hex. Add our own keys freely (`type`, `organe`, `vers`) — the spec tolerates extensions.

## 2. Link geometry — house style (bracket / bus, straight)
- **Fan-out bus**: parent → short horizontal → **vertical bar** that groups its children (placed symmetrically around the parent) → short horizontal with arrowhead into each child. Bar at parent edge + 0.32·gap; small dot where the parent line meets the bar.
- **Fan-in bus (convergence)**: several parents → horizontals → **one vertical bar** (child edge − 0.3·gap) → one horizontal arrow into the entity.
- **Nothing crosses the body**, except the start from an organ: a **horizontal** segment to the silhouette edge, then horizontal or oblique to the first box.
- Boxes: rounded rectangles (7 px), equal width per column, 5 px coloured border on the body side, uppercase type label in the type colour, "+" when children are hidden. Opaque cards and near-black text (white on dark themes): text must dominate the background.
- Obsidian Bézier curves (tangents ⟂ exit side, JSON Canvas fromSide/toSide) only when the user asks for curves.

## 3. Layout and interaction
1. Columns = levels of reasoning (organ → sign → syndrome → exam → diagnosis → treatment), placed **outside the body silhouette**, on the organ's side.
2. **Perfect symmetry**: organ boxes sit at the organ's screen height; a child of several parents sits at their **mean height**; siblings of one parent share the same height (min-height = tallest box of the column) and **one global step** (tallest box + 14 px), centred exactly on the parent's horizontal; collisions move a sibling group **as one rigid block**, the gap split on both sides.
3. **Progressive reveal**: at start only body-anchored nodes show; click an ellipse → its children appear; click again → they retract.
4. **One reset button, two outcomes**: click = selective reset (retract the last opened circuit), double-click = global reset (everything retracts).
5. **Theme button**: cycles 7 contrasted backgrounds — white, sky blue, champagne, gold, mint, night, anthracite (CSS variables, soft radial halo behind the body).
5b. Column width auto-fits the viewport (min 118 px) so the whole network stays visible.
6. Very large graphs: ELK.js / dagre for layered layout, d3-force for clouds, sigma.js / Cytoscape.js beyond 10⁴ nodes — keep the straight convergent renderer for the final drawing.

## 3b. Tooltips, sounds, thresholds (medical networks)
- **Systematic tooltip** on every box (sign, symptom, syndrome, exam step, exam, diagnosis): a fixed frame of 4 rubrics in the same order — *Ce que c'est · Pourquoi ici · Confusion possible · À retenir* — one verbal sentence each, comparable length (perfect symmetry). Data: `bulle {def, pourquoi, confusion, retenir}`.
- **Sounds**: auscultation signs carry `son` (real recording, MP3) → 🔊 on the box + "▶ Écouter" in the tooltip. Source: HLS-CMDS (github.com/Torabiy/HLS-CMDS, S3, S4, murmurs, fine/coarse crackles, wheezes, rub).
- **Thresholds**: 2–3 signs per examination step (one is never enough); the syndrome tooltip names its minimum sufficient set and any confusing sign from a neighbouring syndrome.
- **Dynamic layout**: recompute positions on every click from visible boxes only (tidy tree: each parent centred on its children block).

## 4. Rendering stack (no SVG for images)
- Nodes: HTML (`div`, Atkinson Hyperlegible for text, coloured side border = node type, small uppercase type label above the text).
- Links: **canvas 2D**, straight bus segments — light, crisp, no SVG (`bezierCurveTo` only if curves are explicitly requested).
- Anchors on a 3D body or a real image: project the 3D point with three.js (`vector.project(camera)`) or use image pixel coordinates × display scale. Dot (4.5 px, white rim) on the anchor.
- Interaction (production): pan + wheel zoom, mini-map bottom-left, "Collapse all" button, legend bottom-right.

## 5. Ready-made engine (bundled)
`scripts/reseau3d.html` + `scripts/shot.py` (also at github.com/vialdjoukang-spec/Jeux_45_Spec/tree/main/skills/obsidian-like-complex-network).
- Camera: `cible/dist/fov`, `masquer[]`, `voile` (pelvic occlusion box).
- Config v2: `noeuds[] {id, type, texte, couleur, organe?, cote?, de:[parentIds], col?, y0?}`, `fenetres[] {de, x, y, w, img, annotations[]}`, `theme`. URL hash: `config.json&tout` (all open), `&sauf=id`, `&theme=or`, `&capture` (no transitions).
- Systems → organs: a root `nature:"Système"` lists ALL its organs (never one); boxes hold short names only (≤ 45 chars), detail in tooltip or window.
- Spaces: `espace` on a node (`anatomie|physiologie|semiologie|physiopathologie`) shows it only under that tab; `rubriques` per space set tooltip fields; `aProduire:true` marks backlog.
- Windows: `fenetre` on a node opens `scripts/fenetres.js` → `3d` (real 3D view); lung: `odc`, `hh`, `alveolaire`, `gazometrie`, `spiro`; cardiovascular: `wiggers`, `pv`, `starling` (one shared time-varying-elastance engine `hemo()`), `ecg`, `pa`, `hemodyn`, `starling_cap`, `do2`, `bernoulli`, `ips`. Computed curves, sliders and scenario buttons; gases in kPa, blood pressure in mmHg (Swiss practice). Never hand-drawn curves.
- Pathologies: under an organ, in the `physiopathologie` space, 4 tiers (`nature:"Palier"`: Très fréquentes, Fréquentes, Urgences, Pièges) → `type:"Diagnostic · …"` nodes whose `bulle` carries `bilan{visée:{groupe:[[nom, signe et seuil]]}}`, `traitement[[nom, posologie]]` and `source`. `rubriques` on a node wins over its `espace` for the tooltip frame.
- More URL params: `&ouvrir=id1,id2`, `&espace=physiologie`, `&fenetre=nodeId`, `&bulle=nodeId`, `&lentille=PED`. Wheel pans long organ lists.
- Run: `python3 scripts/shot.py config.json out.png` (serves the folder, opens Chromium with SwiftShader WebGL, waits for `document.title==="PRET"`, screenshots 1600 × 1000).
- Needs `three` (npm) next to the page and a `corps.glb` (see skill 3d-images-upload-super) when nodes anchor on organs.

## 6. Quality check before delivering
- Open the PNG and look: no link crosses a label; no arrow points backwards; every node is linked or intentionally isolated.
- Each colour means one relation type, stated in a legend.
- Text in verbal sentences when the user is Vial; no nominal fragments in explanations (labels may stay short).
