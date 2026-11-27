---
name: "web-aesthetic-github-toolkit"
description: "Choisit et branche les meilleurs outils esthétiques libres et MAINTENUS trouvés sur GitHub (Open Props, Floating UI, a11y-dialog, Fuse.js, Pagefind, Cytoscape.js, Tufte CSS, Playwright + axe…) pour rendre une page ou un site HTML beau, lisible, accessible et léger, dans la charte de Vial. S'active dès qu'on crée ou embellit une page web, un site, une barre de recherche ou un graphe."
---

# Web-aesthetic-GitHub-toolkit

Une belle page ne s'invente pas à chaque fois : des bibliothèques libres et éprouvées donnent déjà des proportions, des rythmes et des couleurs justes. Ce skill choisit **un petit nombre** d'outils adaptés à la page, puis les plie à la charte de Vial. On n'empile pas les frameworks : on en prend un pour la base et un pour le détail.
Mise à jour du 27.11.2026 d'après la veille sourcée `projets/2_Jeux_Paraclinique/VEILLE_FRONT_ET_IA.md` (Jeux_45_Spec) : Pico CSS, Tippy.js et Shoelace sont archivés ; Animate.css n'est pas sous licence OSI.

## 1. Charte de Vial (prioritaire sur tout outil)
- Le texte de contenu est en Atkinson Hyperlegible (≈ 15 px) ; les titres peuvent prendre une autre police.
- Les fonds sont clairs : bleu ciel, blanc, vert pâle, or pâle ou champagne.
- **Titres, libellés et en-têtes en ROUGE** (repérage d'un coup d'œil) ; **texte en BLEU** quand on le colore (retour de Vial, 27.11.2026).
- **Infobulles : encre blanche pure sur fond sombre.**
- Colonne de lecture contenue, sommaire latéral numéroté ; pas de barre de menu horizontale encombrée.
- Pas d'image SVG pour le contenu (anatomie, imagerie) ; une petite icône d'interface reste permise.
- Squelette minimal : le détail va dans l'infobulle, le développement dans une fenêtre ; une seule fenêtre ouverte.
- Aucun nombre inutile à l'apprenant (ex. positions et points tarifaires) ; aucun QCM montré hors du mode Pratique.

## 2. Boîte à outils (vérifiée le 27.11.2026 ; licence et activité à revérifier avant usage)
| Besoin | Outil (GitHub) | Usage | État |
|---|---|---|---|
| Variables de design | **Open Props** (argyleink/open-props, MIT) | Couleurs, espacements, ombres, rayons, easings surchargés dans un seul `:root` | ✅ base par défaut |
| Infobulles | **Floating UI** (floating-ui/floating-ui, MIT) | Infobulles accessibles sans débordement sur mobile ; remplace Tippy.js (archivé) | ✅ |
| Fenêtres | **a11y-dialog** (KittyGiraudel/a11y-dialog, MIT) | `<dialog>` accessible : focus piégé, Échap, `aria-*` | ✅ |
| Recherche floue d'une liste | **Fuse.js** (krisk/Fuse, Apache-2.0) | Barre de sélection tolérante aux fautes et aux accents | ✅ |
| Recherche plein texte | **Pagefind** (CloudCannon/pagefind, MIT) | Index fragmenté pour des milliers de fiches statiques | ✅ |
| Graphe type Obsidian | **Cytoscape.js** (cytoscape/cytoscape.js, MIT) ; **Sigma.js** au-delà de ~10 000 nœuds | Réseau pathologie ↔ examens ↔ mécanismes | ✅ |
| Lecture longue | **Tufte CSS** (edwardtufte/tufte-css, MIT) | Notes en marge pour les cours denses | ✅ option |
| Tableau de bord | **Tabler** (tabler/tabler, MIT) | Cartes et jauges ; lourd pour une page simple | ⚠️ si besoin réel |
| Composants riches | **Web Awesome** (shoelace-style/webawesome, ex-Shoelace) | Onglets, arbres, combobox sans framework ; lourd pour 3 composants | ⚠️ |
| Animation | CSS natif, `@starting-style`, View Transitions ; **Motion** seulement si nécessaire | Toujours sous `prefers-reduced-motion` | ✅ |
| Contrôle | **Playwright** + **@axe-core/playwright** (MPL-2.0) | Captures 1280 et 380 px, 0 erreur console, contraste AA automatique | ✅ obligatoire |
| ~~Pico CSS~~ | picocss/pico | Archivé (v2.1.1 finale) : ne pas l'adopter pour un nouveau site | ⛔ |
| ~~Animate.css~~ | animate-css/animate.css | Hippocratic License 2.1, non OSI : écarter | ⛔ |
| ~~Tippy.js~~, ~~Shoelace~~ | — | Archivés : Floating UI, Web Awesome | ⛔ |

## 3. Méthode
1. **Classer la page** : cours ou lecture, exercice, tableau de bord, site de consultation (recherche + fiches), ou jeu.
2. **Choisir la base** : Open Props toujours ; Tufte pour une lecture longue ; Tabler seulement pour un vrai tableau de bord ; Fuse.js + Pagefind pour un site de consultation ; Cytoscape.js pour un réseau.
3. **Plier la base à la charte** : un seul bloc `:root` (Atkinson, fond clair, rouge des titres, bleu du texte, infobulle sombre, largeur de colonne).
4. **Hors ligne** : quand la page doit marcher sans Internet, copie le CSS et le JS minifiés dans le dépôt plutôt qu'un lien CDN, avec la version figée.
5. **Mesurer avant de livrer** : capture Playwright à 1280 et 380 px, 0 erreur console, audit axe (contraste AA, rôles, libellés), aucun défilement horizontal.
6. **Chercher plus loin si rien ne convient** : `gh api -X GET search/repositories -f q='topic:classless-css' -f sort=stars` (ou `design-tokens`, `fuzzy-search`, `graph-visualization`). Garde un outil seulement si sa licence est approuvée par l'OSI, s'il n'est pas archivé et s'il a été mis à jour depuis moins de 2 ans.

## 4. Relais
`frontend-design` (direction esthétique ; non installé : anthropics/skills, `skills/frontend-design`), `web-designer-pilot-faithful`, `artifact-design` et `artifact-emulator` (rendu), `interactive-ui-generator` (écran temps réel), `gratis-dashboard-live` (tableaux de bord), `dataviz` (graphiques).

Signature : AAI (Anthropic AI)
