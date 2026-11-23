---
name: autonomous-skill-creator
description: Repère seul les procédures qui reviennent et les transforme en skill propre, sans doublon, rangé où les agents le liront. S'active dès qu'une manipulation se répète deux fois ou qu'un agent manque d'une méthode.
---

# Autonomous-skill-creator

## Quand créer un skill
Une procédure mérite un skill si elle revient, si elle suit une méthode non triviale, et si un modèle sans consigne la ferait moins bien. Une seule occurrence ne suffit pas.

## Méthode
1. **Extraire** la procédure de l'historique : étapes, outils, erreurs commises, corrections de l'utilisateur.
2. **Vérifier le recouvrement** avec les skills existants (`skill-network-master`) : s'il y en a un voisin, tu proposes de l'enrichir plutôt que d'en créer un second.
3. **Écrire** le SKILL.md : nom en kebab-case, description qui dit QUAND l'activer (déclencheurs larges), corps à l'impératif qui explique le POURQUOI de chaque règle, relais vers les skills voisins, moins de 150 lignes.
4. **Ranger** : dans une session avec l'utilisateur, tu le proposes par la carte de proposition de skills ; dans un agent de production, tu l'écris dans `.claude/skills/<nom>/SKILL.md` du dépôt et tu le cites dans la mission de l'agent.
5. **Tester** sur le cas réel qui l'a fait naître ; tu corriges la consigne qui a échoué.

Relais : `perfect-skill-user-organizer-collector` (registre), `skill-network-master` (anti-doublon).

Signature : AAI (Anthropic AI)
