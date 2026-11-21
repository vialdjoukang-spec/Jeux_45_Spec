---
name: obsidian-like-complex-network
description: Draw dense, readable Obsidian-style networks (canvas graphs, concept maps, diagnostic circuits, mind maps) with smooth Bézier links leaving node sides, arrowheads, typed colours, and optional anchoring on a real 3D model or a real image. Use whenever the user asks for an "Obsidian-like" graph, a canvas/JSON Canvas, a network of linked notions, a decision tree with curved connections, organ → sign → syndrome → diagnosis circuits, or any connection-heavy visual — even if they don't say "Obsidian". Never draws images in SVG.
---

# Obsidian-like amazing complex Network

Goal: a network that reads like an Obsidian canvas — calm nodes, curved links that leave a node **by one side** and enter the next **by the facing side**, an arrowhead at the arrival, and zero visual chaos even with 50+ links.

## 1. Data first: JSON Canvas 1.0 (open spec, jsoncanvas.org)
Store every network as JSON Canvas, so it opens in Obsidian and in our engine:
```json
{"nodes":[{"id":"coeur","type":"text","text":"Cœur","x":0,"y":0,"width":160,"height":56,"color":"1"}],
 "edges":[{"id":"e1","fromNode":"coeur","fromSide":"right","toNode":"galop","toSide":"left","toEnd":"arrow","label":"auscultation","color":"#ff6b6b"}]}
```
`fromSide`/`toSide` ∈ top|right|bottom|left; `toEnd` arrow by default; colours "1"–"6" or hex. Add our own keys freely (`type`, `organe`, `vers`) — the spec tolerates extensions.

## 2. The link geometry (what makes it look like Obsidian)
A cubic Bézier whose tangents are **perpendicular to the exit side**:
```
P0 = exit point on fromSide        P3 = entry point on toSide
d  = max(60, |P3.x − P0.x| × 0.5)  (vertical sides: use |Δy|)
P1 = P0 + d·normal(fromSide)       P2 = P3 + d·normal(toSide)
```
- Arrowhead: small filled triangle (9 × 9 px) aligned with the final tangent.
- Two nodes in the **same column**: loop out sideways (P1 = P0 + 70·n, P2 = P3 + 70·n), never a straight line through the content.
- Fan-out (one source → many targets, image 2 style): all curves start from the same anchor; spread is automatic because each target has its own P3.
- Stroke 1.5–1.8 px, opacity 0.85, colour = relation type; label (11 px) at the curve midpoint only when it carries meaning.

## 3. Layout rules that kill crossings
1. Columns = levels of reasoning (e.g. organ → sign → syndrome → exam → diagnosis → treatment). Left-to-right reading.
2. Inside a column, **sort nodes by the screen Y of what they point to** (organ projection, parent node). This alone removes most crossings.
3. Spacing: ≥ 40 px between columns' edges; labels never wider than 260 px (wrap).
4. Too many nodes (> 25 visible)? Collapse by default; click expands one circuit; hover highlights the full path from the root.
5. For automatic layouts beyond columns, use **ELK.js** (`layered`, `elk.edgeRouting: SPLINES`) or **dagre**; for exploratory clouds use **d3-force**; for very large graphs (10⁴+ nodes) **sigma.js / Cytoscape.js**. Keep our Bézier renderer for the final drawing.

## 4. Rendering stack (no SVG for images)
- Nodes: HTML (`div`, Atkinson Hyperlegible for text, coloured side border = node type, small uppercase type label above the text).
- Links: **canvas 2D** (`bezierCurveTo`) — light, crisp, no SVG.
- Anchors on a 3D body or a real image: project the 3D point with three.js (`vector.project(camera)`) or use image pixel coordinates × display scale. Dot (4.5 px, white rim) on the anchor.
- Interaction (production): pan + wheel zoom, mini-map bottom-left, "Collapse all" button, legend bottom-right.

## 5. Ready-made engine (bundled)
`scripts/reseau3d.html` + `scripts/shot.py` (also at github.com/vialdjoukang-spec/Jeux_45_Spec/tree/main/skills/obsidian-like-complex-network).
- Config = JSON: `colonnes[] {id, cote:"g"|"d", x, yMin, yMax, noeuds[] {type, texte, couleur, organe?, vers:["colId:index"]}}`, optional `fenetre` (real image window with raw/annotated pair and numbered ellipses), `masquer[]`, camera `cible/dist/fov`.
- Run: `python3 scripts/shot.py config.json out.png` (serves the folder, opens Chromium with SwiftShader WebGL, waits for `document.title==="PRET"`, screenshots 1600 × 1000).
- Needs `three` (npm) next to the page and a `corps.glb` (see skill 3d-images-upload-super) when nodes anchor on organs.

## 6. Quality check before delivering
- Open the PNG and look: no link crosses a label; no arrow points backwards; every node is linked or intentionally isolated.
- Each colour means one relation type, stated in a legend.
- Text in verbal sentences when the user is Vial; no nominal fragments in explanations (labels may stay short).
