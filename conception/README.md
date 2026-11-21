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

## Mise à jour du 2026-11-21 (soir)
- Infobulle symétrique systématique (4 rubriques : Ce que c'est · Pourquoi ici · Confusion possible · À retenir) sur chaque case.
- 2 ou 3 signes par temps d'examen ; le syndrome nomme son minimum suffisant et ses confusions.
- Sons réels d'auscultation (HLS-CMDS) : galop B3 et crépitants fins dans le prototype.
- Disposition recalculée à chaque clic, parents centrés sur leurs enfants.
- Système nerveux : 24 syndromes majeurs listés (plan Tétrade + donnees/tetrade/neurologique/syndromes.json).
- `outils/generer_json.py` génère TOUS les JSON (202 fichiers : squelettes + exemples réels + schémas) dans `donnees/`, à 0 token.

## Mise à jour : examens complémentaires exhaustifs
- `outils/catalogue_paraclinique.py` : catalogue topographique unique (9 régions, 64 organes, 23 prélèvements, imagerie, biologie, explorations fonctionnelles, endoscopie, anatomopathologie).
- `outils/auditer_couverture.py` : audit bloquant (systèmes reliés, au moins deux modalités par organe, aucun doublon, examens témoins) → `audit/couverture.md`.
- Tétrade : onglet unique « Examens complémentaires » (E9), progression topo-systémique ou topo-organe.
- `audit/audit_amelioration.md` : constats, corrections et reste à faire.

## Mise à jour : navigation par côté, disciplines transversales, discriminants
- Règle du côté : un circuit se développe du côté où le trait né du corps rejoint sa première case.
- Onglet Disciplines transversales : 19 disciplines-outils (A → S) et 12 lentilles cliniques (`outils/transversales.py`).
- Infobulle de diagnostic : bilan en six visées et traitement avec posologie et source.
- Facteur discriminant des techniques d'imagerie, visées du bilan et smarter medicine (`outils/catalogue_paraclinique.py`).
- Fenêtre de clichés : patient (brut / annoté) à gauche, radio-anatomie normale à droite.
- Anatomie : fenêtre de structure 3D à quatre vues (`prototypes/moteur/anatomie.html`).
- Audit global : `outils/auditer_conception.py` → `audit/conception.md`.
