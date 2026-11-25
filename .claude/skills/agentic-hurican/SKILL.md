---
name: agentic-hurican
description: Déchaîne une production massive par vagues d'agents en parallèle autour d'un œil calme (l'orchestrateur), sans doublon, sans conflit de fusion, avec audit et arrêt d'urgence. S'active dès qu'on veut accélérer fort un gros chantier avec plusieurs agents.
---

# Agentic-Hurican

Un ouragan a un œil immobile et des bandes qui tournent très vite autour de lui. Ici, l'œil est l'orchestrateur : il ne produit rien lui-même, il tient la carte, distribue, contrôle et fusionne. Les bandes sont des vagues d'agents qui produisent en parallèle. La puissance vient des bandes, mais la sécurité vient de l'œil. Sans œil, la vitesse produit des doublons, des conflits de fusion, un disque plein et des erreurs médicales qui passent.

Ce skill naît des leçons du chantier Jeux_45_Spec (novembre 2026) : un producteur unique fusionnait proprement ; plusieurs agents sans couloir se marchaient dessus.

## 1. Avant la tempête (l'œil se forme)
1. Lance `panoramic-skill-finder` : il désigne ce qui se fait par script (0 token) et ce qui demande un agent.
2. Écris **une source unique de l'état** (fichier JSON versionné) : chaque unité de travail porte un id stable, un statut (à faire, réservé, produit, audité, fusionné) et l'empreinte de ses entrées (`optimisation-par-cache-hache-autorun`). Une unité déjà produite ne se reproduit jamais.
3. Découpe le travail en **couloirs disjoints** : une spécialité, un groupe, une catégorie par agent. Deux agents ne partagent jamais un couloir, ni un fichier.
4. Fixe les **plafonds** avec l'utilisateur : nombre d'agents simultanés, budget (abonnement ou crédit API), heure de fin. Tu ne dépasses jamais le plafond que l'utilisateur a fixé, même pour aller plus vite.
5. Vérifie le terrain : espace disque (un clone partiel `--filter=blob:none` par agent, supprimé à la fin), accès réseau aux sources, autorisations en attente.

## 2. Les bandes (vagues d'agents)
- Chaque agent reçoit un prompt complet et autonome : son couloir, sa première unité, ses skills (`perfect-skill-user-organizer-collector`), ses contrôles, sa règle de fusion, l'interdiction du push forcé et l'ordre de s'arrêter et de signaler tout refus au lieu de le contourner.
- Chaque agent travaille dans son propre clone et sur sa propre branche, ou fusionne sur la branche principale par petits lots, après ses contrôles, si l'utilisateur l'a autorisé.
- Un agent enchaîne ses lots sans rapport intermédiaire et rend un seul rapport court à la fin (5 lignes) : il économise le contexte et n'interrompt pas l'œil.
- Quand un agent s'arrête faute de contexte, l'œil lance un agent neuf qui reprend à l'unité suivante du rapport. Après un redémarrage du serveur, l'œil reprend l'agent par message plutôt que d'en créer un double.

## 3. L'œil (contrôle continu)
- **Fusion en file** : les fusions passent une à une, après `pull --rebase` ; une course au push se règle par un nouvel essai, jamais par la force.
- **Audit à deux niveaux** : l'agent fait son autocontrôle mécanique ; l'œil vérifie par script (schéma, comptes, doublons, tests) avant d'accepter. Pour un contenu médical, `medical-accuracy-100` : une source citée doit avoir été lue par l'agent lui-même.
- **Rondes planifiées** (toutes les 2 h) : l'œil vérifie que chaque bande tourne, relance celles qui sont tombées, contrôle la branche principale et publie la progression (`gratis-dashboard-live`).
- **Correction en retour** : chaque erreur trouvée dans un rapport devient une leçon dans le skill des producteurs et une tâche préalable pour l'agent suivant.

## 4. Arrêt d'urgence
Quand l'utilisateur dit « pause » ou « stop » : arrête tous les agents, désactive les rondes planifiées, laisse le travail non fusionné à l'écart (jamais sur la branche principale) et rends l'état en 3 lignes. Rien ne repart sans son accord explicite.

## 5. Ce que l'œil refuse
- Plus d'agents que le plafond fixé par l'utilisateur.
- Deux agents sur le même couloir.
- Une fusion sans contrôle, un push forcé, un refus d'autorisation contourné ou relayé à un autre agent.
- Un contenu qui dépasse le niveau visé pour impressionner.

## Relais
`harness-gen-network` (scripts autour de l'agent), `harness-for-long` (reprise), `panoramic-skill-finder`, `optimisation-par-cache-hache-autorun`, `perfect-skill-user-organizer-collector`, `medical-accuracy-100`, `gratis-dashboard-live`.

Signature : AAI (Anthropic AI)
