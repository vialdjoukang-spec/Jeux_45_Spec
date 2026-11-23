---
name: concept-corelator
description: Interprète finement toute courbe, valeur, signe ou examen en le corrélant à la physiopathologie, à la sémiologie, aux trouvailles exploratoires et diagnostiques et à l'approche thérapeutique qu'ils justifient, avec définitions littérales et liens entre disciplines. S'active dès que le champ lexical s'y prête (courbe, valeur, scénario, signe, examen, mécanisme).
---

# Concept-corelator

Ce skill transforme une donnée isolée en un raisonnement clinique relié. Il sert d'abord aux panneaux d'interprétation des fenêtres de courbes (`conception/prototypes/moteur/interpretations.json`), mais il s'applique à toute situation où une valeur ou un signe doit être compris plutôt que récité.

## Structure obligatoire (une entrée par fenêtre et par scénario)
Chaque entrée suit l'ordre de la coque vers le centre et répond à quatre questions, puis relie et définit :
1. **physio — Vers la physiopathologie** : tu expliques quel mécanisme produit ce que montre la courbe dans ce scénario, et pourquoi.
2. **semio — Conséquence sémiologique** : tu dis quels signes et symptômes ce mécanisme produit chez le patient, et par quel lien.
3. **explo — Trouvailles exploratoires et diagnostiques** : tu nommes les examens qui le démontrent, avec les valeurs ou les images attendues et leurs seuils.
4. **ther — Approche thérapeutique justifiée** : tu dis quel traitement découle du mécanisme, avec le pourquoi de chaque geste, ses cibles et les doses usuelles quand elles sont utiles.
5. **liens** : tu donnes 2 à 4 paires `[discipline, lien]` qui montrent comment le même mécanisme réapparaît ailleurs (pharmacologie, radiologie, réanimation, néphrologie…).
6. **def** : tu donnes 2 à 5 paires `[terme, définition littérale]` pour les termes techniques employés.

## Serrement sélectif (Pareto modifiée)
- Tu gardes seulement ce qui change la compréhension ou la décision dans ce contexte précis ; le reste est exclu.
- Tu écris des phrases entièrement verbales, denses, en français ; aucune phrase nominale.
- Chaque champ fait au moins 40 caractères et rarement plus de 400.
- La clé de scénario reprend exactement l'étiquette du bouton de la fenêtre ; « _ » sert quand la fenêtre n'a pas de bouton.

## Exactitude
Tu appliques `medical-accuracy-100` : chaque seuil et chaque dose correspondent aux recommandations actuelles (ESC, KDIGO, ERS, Swissmedic…). En cas de doute, tu écris la valeur prudente et tu signales le point dans `_a_verifier`.

## Référence d'or
L'entrée `ne_ppc` d'`interpretations.json` montre le niveau attendu. Valide toujours par `python3 projets/outils/verifier_interpretations.py`.

Signature : AAI (Anthropic AI)
