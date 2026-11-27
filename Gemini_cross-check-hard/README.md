# Gemini_cross-check-hard — audit croisé externe

| Fichier | Rôle |
|---|---|
| `PROMPT_GEMINI.md` | Consignes à donner à Gemini 4 Neon dans Antigravity (phrase de lancement en tête). |
| `SKILL.md` | Méthode d'audit : liste de contrôle, sources suisses, pièges. |
| `outils/preparer_lots.py` | Régénère les manifestes de lots (0 token, empreintes sha256). |
| `outils/SCHEMA_RAPPORT.json` | Format obligatoire d'un rapport. |
| `outils/valider_rapports.py` | Contrôle mécanique des rapports (schéma, preuve, péremption). |
| `<jeu>/MANIFESTE_LOTS.json` | Lots à auditer pour ce jeu. |
| `<jeu>/rapports/` | Rapports de Gemini (seul dossier où il écrit, avec `SYNTHESE.md`). |

Jeux : `1_Tetrade` · `2_Paraclinique/{Imagerie,Biologie,Explorations}` · `3_Transversal` · `4_Jeux_45_Spec`.

Circuit : Gemini audite → `valider_rapports.py` → Claude corrige le contenu, constat par constat, en citant l'identifiant du constat → Vial valide.
