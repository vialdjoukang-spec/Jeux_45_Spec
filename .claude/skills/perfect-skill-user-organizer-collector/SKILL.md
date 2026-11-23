---
name: perfect-skill-user-organizer-collector
description: Tient le registre de tous les skills (rôle, déclencheurs, relais), charge le bon skill au bon moment, dote chaque agent de son jeu de skills et supprime les doublons. S'active à chaque lancement d'agent et dès qu'on crée, cherche ou range un skill.
---

# Perfect-skill-user-organizer-collector

## Registre
Tu tiens `.claude/skills/REGISTRE.md` dans chaque dépôt de travail : nom, une ligne de rôle, déclencheurs, relais, date. Il dit à tout agent quel skill charger.

## Dotation des agents
Chaque agent reçoit au minimum : `perfect-skill-user-organizer-collector`, `ultra-competent-fast-doctor`, `autonomous-skill-creator`, `pipeline-autonomous-builder`, `i-never-waste-token`. Tu copies ces skills dans `.claude/skills/` du dépôt et tu les cites dans la mission de l'agent, puis tu ajoutes les skills du métier de la tâche.

## Usage au bon moment
- Au début d'une tâche, tu relis le registre et tu charges les skills dont les déclencheurs correspondent.
- Tu ne charges pas tout : seulement les 2 à 5 skills qui servent la tâche.

## Hygiène
- Un skill = une responsabilité ; deux skills qui se recouvrent se fusionnent (`skill-network-master`).
- Un skill obsolète (décision contraire de l'utilisateur, outil remplacé) se corrige tout de suite, puis tu le signales.

Relais : `skill-network-master`, `autonomous-skill-creator`.

Signature : AAI (Anthropic AI)
