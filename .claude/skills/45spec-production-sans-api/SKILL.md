---
name: 45spec-production-sans-api
description: Produire à la main (agent Claude, sans appel API) les notions, questions et corrections du jeu 45 Spec exactement au format de scripts/produire_notions_questions.py. S'active dès qu'un agent remplace l'API pour une spécialité du jeu 45 Spec (« tu produis toi-même », « sans API », PROGRESSION_<SPEC>.md).
---

# 45 Spec — production sans API

## Pourquoi
Le script `produire_notions_questions.py` valide et écrit trois fichiers par pathologie canonique ; un agent qui écrit le JSON à la main oublie des clés, dépasse les bornes du schéma et couvre mal les notions. L'outil `projets/45spec/agent_ecrire.py` réutilise le même `valider()`, le même `chemin()` et la même structure de sortie ; seule la signature change (`usage._mode = "agent"`).

## Méthode
1. Lister les pathologies par `canoniques("<SPEC>")` (ordre de `selection()` : fréquence puis identifiant). L'identifiant par spécialité peut différer de l'identifiant global (ex. `A41.9__O2_8-E03` contre `A41.9_1__O2_8-E03`) : `agent_ecrire.py` gère les deux.
2. Lire `P.message("notions", c)` pour les rubriques et les portes ; **ne jamais recopier le bruit du gabarit** (ex. « paracétamol 1 g » ou « 1,5–2 L/j » adultes dans des amorces pédiatriques).
3. Écrire un fichier source Python hors du dépôt avec les aides `N`, `notions`, `A`, `K`, `M`, `questions`, `CN`, `PEC`, `correction` (options de type A et menu long marquées `*` pour la juste, mélangées de façon déterministe).
4. Lancer `python projets/45spec/agent_ecrire.py <source.py>` : il valide, écrit et affiche les formats, les notions de poids ≥ 2 sous-couvertes (moins de 2 questions ou un seul angle) et les notions absentes.
5. Corriger jusqu'à zéro alerte : poids 3 ≤ 15 %, poids 2 ≤ 35 %, chaque notion de poids ≥ 2 dans deux questions d'angles différents ; ajouter au besoin un Kprim qui couvre 4 à 6 notions.
6. Commit par lot de 3, push immédiat sur la branche de l'agent, mettre à jour `projets/45spec/PROGRESSION_<SPEC>.md`.

## Pièges connus
- Les pathologies partagées dont le premier code n'est pas la spécialité s'écrivent dans le dossier de l'autre spécialité : les traiter en dernier pour éviter les doublons entre agents.
- Les fichiers de travail en dehors du dépôt doivent porter un nom propre à l'agent : plusieurs agents partagent `/home/claude`.
- Un chiffre incertain porte « à vérifier » dans `source` ; aucune référence inventée.
- Bornes du schéma qui font échouer `valider()` : 6 notions au plus par question ; 4 rubriques, 5 points et 4 sources au plus par notion de correction ; algorithme SSP d'au moins 6 nœuds ; `nature` et `categorie` (non pharmacologique) limitées à leurs énumérations (ex. « diagnostic différentiel », jamais « discriminant » ; « geste ou chirurgie », jamais « ventilation »).
- Une vignette dont `stem + prompt` contient les trois premiers mots longs du nom de l'entité échoue si `diagnosticMasque` vaut vrai : passer `situ="m", masq=False` pour les questions monographiques.
- Ordre de la file : depuis le 24.11.2026, PED suit l'ordre révisé par importance pour l'examen (section de `PROGRESSION_PED.md`), et non plus `selection()`.

Relais : `pipeline-autonomous-builder`, `medical-accuracy-100`, `i-write-so-fast`.

Signature : AAI (Anthropic AI)
