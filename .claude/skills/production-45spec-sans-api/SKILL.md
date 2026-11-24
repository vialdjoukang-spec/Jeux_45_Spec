---
name: production-45spec-sans-api
description: Produit à la main, sans appeler l'API Anthropic, les notions, questions et corrections du jeu 45 Spec (schémas de scripts/produire_notions_questions.py) pour une spécialité. S'active dès qu'un agent « remplace l'API » pour une spécialité du jeu MedSuisse Arena 45.
---

# Production 45 Spec sans API

## Pourquoi
Écrire les JSON complets à la main coûte deux à trois fois plus de tokens et produit des erreurs de schéma. Un module Python compact par pathologie, déployé par un outil commun, garde exactement la sortie du script (valider(), ecrire()) pour un coût minimal.

## Outil
- `projets/45spec/psy/lib.py` (modèle validé sur PSY) : helpers `notions()`, `A()`, `K()`, `M()`, `C()`, `cours()`, `pec()` ; `python lib.py <id>` valide puis écrit les trois fichiers.
- Contrôles ajoutés à valider() : proportions A/Kprim/MenuLong (≈ 13/3/2 sur 18), couverture (chaque notion de poids ≥ 2 citée par ≥ 2 questions d'angles différents), poids 3 ≤ 15 % et poids 2 ≤ 35 %, au moins une série, lieux interdits (CNP, CPCM), disciplines transversales A→S conformes à `data/references/transversales_19_et_systemes.json`.
- `progression.py` régénère `projets/45spec/PROGRESSION_<SPEC>.md` depuis le disque.
- Pour une autre spécialité : copier `lib.py` et `progression.py`, changer le code de spécialité et l'ordre.

## Méthode par pathologie
1. Lire les portes d'entrée (`canoniques()`), pas le message entier.
2. Planifier AVANT d'écrire : ~29 notions (4 de poids 3, 10 de poids 2), puis 18 questions en assignant les notions et les angles, pour passer la couverture du premier coup.
3. Diagnostic masqué : ne jamais réunir dans une vignette masquée les trois premiers mots de plus de 4 lettres du nom de l'entité.
4. Posologies : « à vérifier dans l'AIPS » ; référence incertaine : ne pas l'inventer.
5. Commit + push toutes les 3 pathologies sur la branche agent, jamais sur main.

Relais : `psych-ultra-ch`, `medical-accuracy-100`, `pipeline-autonomous-builder`.

Signature : AAI (Anthropic AI)
