# Conception — trois modules (non implémentés)

| Module | Plan JSON (source) | Lecture humaine |
|---|---|---|
| Tétrade topo-systémique (+ Psyché) | `plans/tetrade.plan.json` | `html/tetrade.html` · `pdf/tetrade.pdf` |
| Pharmacologie systémique | `plans/pharmacologie.plan.json` | `html/pharmacologie.html` · `pdf/pharmacologie.pdf` |
| Jeux_Examens_Paraclinique | `plans/paraclinique.plan.json` | `html/paraclinique.html` · `pdf/paraclinique.pdf` |

**Chaîne :** `outils/socle.py` + `outils/construire_plans.py` → plans JSON → `outils/rendre_plans.py` (auto-audit de 28 contrôles, HTML, PDF).

```
python conception/outils/construire_plans.py
```
*(Régénérer les plans JSON après une modification.)*

```
python conception/outils/rendre_plans.py
```
*(Auditer les plans, puis produire le HTML et le PDF ; le PDF exige Playwright.)*

## Mise à jour du 2026-11-21
- VIT DIT CAFé est confirmé : les lettres nomment les altérations d'un tissu ou d'un organe.
- Les simulations de prototype sont de vrais rendus 3D (BodyParts3D, three.js) reliés à la manière d'Obsidian ; aucune image n'est en SVG.
- Les organes génitaux externes sont occultés (peau retirée dans une boîte pelvienne).
- Moteur et configurations : `prototypes/moteur/` (régénérer : `build_glb.py`, puis `shot.py <config.json> <sortie.png>`).
- Skills associés : `skills/obsidian-like-complex-network/`, `skills/3d-images-upload-super/`.
