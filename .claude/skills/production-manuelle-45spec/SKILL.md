---
name: production-manuelle-45spec
description: Produit sans API, pathologie par pathologie, les notions, questions et corrections du jeu 45 Spec au format exact de scripts/produire_notions_questions.py. S'active dès qu'un agent remplace l'API pour une spécialité (« producteur 45 Spec », « agent/45spec-XXX »).
---

# Production manuelle 45 Spec

Pourquoi : l'agent remplace l'appel API ; il doit produire le même JSON, validé par le même valider(), sans gaspiller de tokens.

## Chaîne (une pathologie)
1. Liste les canoniques : `python3 -c "import sys; sys.path.insert(0,'scripts'); import produire_notions_questions as P; [print(c['id'], c['entite']['nom']) for c in P.canoniques('NEU')]"` ; l'ordre de priorité vit dans `projets/45spec/ORDRE_<SPEC>.txt`.
2. Écris une source compacte `projets/45spec/sources_<SPEC>/<CIM>_<nom>.py` (modèle : `sources_NEU/G00.9_meningite.py`) : ID, PLAN, NOTIONS (« rub|nature|poids|S|source|énoncé »), ANGLES, QUESTIONS (dict format/serie/stem/prompt/items/notions/angle/diff/ladder/sources), CORRECTION, AVERIFIER.
3. Lance `python3 scripts/ecrire_manuel.py SOURCE --spec <SPEC>` : il déplie, appelle valider() et ecrire(), puis contrôle formats, couverture (règle 8ter) et poids (règle 5bis).
4. Démasque honnêtement les questions qui nomment la pathologie : `python3 scripts/demasquer_manuel.py SOURCE 8 13 …` ; garde une majorité de vignettes masquées.
5. Par lot de 3 : `python3 scripts/progression_manuel.py <SPEC>`, commit, push sur `agent/45spec-<SPEC>` (jamais main).

## Règles qui font échouer le plus souvent
- Natures et catégories : seules les valeurs des énumérations passent (pas « score », pas « hygiène de vie » comme nature).
- Poids : poids 3 ≤ 15 %, poids 2 ≤ 35 % des notions ; chaque notion de poids ≥ 2 dans ≥ 2 questions d'angles différents.
- Formats : ~14 A (5 options, 1 juste), 4 Kprim (4 énoncés), 2 menus longs (12 à 20 options).
- priseEnCharge : accueil 2-5, étapes 3-8, suivi 2-6, mesuresGenerales ≥ 2.
- Posologies « à vérifier dans l'AIPS » ; référence incertaine → AVERIFIER ; jamais de lieu CNP ni CPCM.

Relais : `ultra-competent-fast-doctor`, `medical-accuracy-100`, `switzerland-medical-professor`, `pipeline-autonomous-builder`.

Signature : AAI (Anthropic AI)
