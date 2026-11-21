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
