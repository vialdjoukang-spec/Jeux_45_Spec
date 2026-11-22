---
name: obsidian-like-data-mode
description: Turns any data structure — a folder tree of JSON files, production lots, a catalogue, a schema or one big JSON — into an Obsidian-like interactive network (straight bus links, progressive reveal, tooltips with path, counts, status and GitHub link, search, 7 themes, JSON Canvas export). Use it whenever the user wants to SEE how data, files, lots, folders, catalogues or a segmentation are organised, asks for an Obsidian-like map of a dataset or repository, or wants to check a data architecture before production — even if they only say "montre-moi la structure", "réseau de mes JSON" or "carte des lots".
---

# Obsidian-like data mode

The sister skill `obsidian-like-complex-network` draws clinical reasoning on a 3D body. This one draws **data**: folders, files, lots and the items inside them. There is no body here; the root sits on the left and the structure unfolds to the right, one column per level.

Why it helps: a person who distributes production lots across several AI accounts must see at a glance where each fragment lives, how big it is and what it contains. A network makes holes, duplicates and unbalanced lots visible in seconds, which a file explorer hides.

## 0. Where the engine lives
The scripts and the page template are in the repository: github.com/vialdjoukang-spec/Jeux_45_Spec/tree/main/skills/obsidian-like-data-mode
- `scripts/data_vers_reseau.py` builds the network ; `scripts/capturer.py` takes a PNG with Playwright + Chromium.
- `assets/reseau_donnees.html` is the page template the script fills.

When they are not on disk, clone the repository (`git clone https://github.com/vialdjoukang-spec/Jeux_45_Spec`), or fetch these three files from raw.githubusercontent.com. Keep `scripts/` and `assets/` side by side.

## 1. Build the network (zero token, one command)
```
python scripts/data_vers_reseau.py <dossier|fichier.json> -o reseau.html \
  --titre "Paraclinique — segmentation des lots" \
  --niveaux "Thème,Région ou famille,Lot" \
  --grouper-par modalite --type-par modalite --contenu 2 \
  --github https://github.com/<user>/<repo>/blob/main/ --racine-depot <repo> \
  --canvas reseau.canvas --signature "AAI (Anthropic AI)"
```
- `--niveaux` names the column of each folder depth: the type label and colour of a box come from it. Name the levels in the user's words, such as Projet, Thème or Région.
- `--contenu N` opens JSON files N levels deep:
  - a production lot (`{"_lot", "fichiers"}`) shows its files ; a lot with a single file shows that file's content directly ;
  - lists named `examens`, `analyses`, `elements`, `lecons` or `noeuds` show one box per item, with its `nom` as label.
- `--type-par <champ>` colours items by one of their fields, for example `modalite`, which separates Imagerie, Biologie and Endoscopie.
- `--canvas` also writes a JSON Canvas 1.0 file that opens in Obsidian.
- The page is self-contained: data inline, Atkinson Hyperlegible for text, no SVG.

## 2. What the page does
- **Stable tree:** a parent keeps its place and its children start at its height, so opening a box only pushes what lies below it. The clicked box never moves on screen, and folding a box keeps the memory of what was open beneath it, so reopening restores the same view.
- **Progressive reveal:** at load only the root and its first level show. A click unfolds a box and a second click folds it.
- **No explosion:** `--grouper-par modalite` inserts one box per group (Imagerie, Biologie…) between a file and its items, so a 30-item list unfolds in two short steps.
- **One ↺ button:** a click folds the last opened circuit, and a double-click folds everything.
- **Navigation:**
  - « Tout déplier » unfolds every box, and « Cadrer » fits the visible network to the screen ;
  - the wheel pans, and Ctrl + wheel zooms ;
  - a drag on the background moves the view.
- **Links:** straight bus links (parent → horizontal → vertical bar → arrow into each child), one colour per child type, with a legend at the bottom right.
- **Tooltip on hover:**
  - for a folder: its path and number of JSON files ;
  - for a file: its path, size and content, plus the task, title and signature when it is a lot, and a GitHub link ;
  - for an item: its filled fields.
- **Search box:** it unfolds the path to every match and outlines the match.
- **Other controls:** a theme button cycles seven backgrounds, and the counter shows visible nodes out of total nodes.
- **URL hash:** `#tout` opens everything, `#ouvrir=<id>` opens a node and frames it, and `#theme=nuit` sets the theme. Ids are paths from the root `R`, for example `R/2_Biologie/1_Analyses_individuelles/PB05_….json`.

## 3. Check before delivering
1. Capture two views with `python scripts/capturer.py reseau.html vue.png ["ouvrir=<id>"]`: the closed root, then one deep path. Then read the PNGs.
2. Check that no label overlaps, that every arrow points into a box, and that the legend lists only the types present.
3. Check that the counts in the boxes match the source (number of JSON files, examens, analyses).
4. Say in one sentence, using verbal phrasing, what the network reveals: lot sizes, empty folders, imbalance.

## 4. Deliver
Publish the HTML as an artifact when the user will come back to it. Also keep the HTML and the `.canvas` beside the data in the repository, so the map is regenerated with the data.
