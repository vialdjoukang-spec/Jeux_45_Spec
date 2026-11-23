---
name: pipeline-autonomous-builder
description: Construit de bout en bout un pipeline automatique, gratuit à l'usage et relançable : schéma, script, test, GitHub Actions, file de tâches, suivi. S'active dès qu'un travail se répète sur des centaines d'éléments.
---

# Pipeline-Autonomous-builder

## Les 7 étages (toujours)
1. **Cible** : tu écris le schéma de sortie d'abord (JSON Schema) ; il servira d'outil structuré et de validateur.
2. **Sélection** : un script liste les éléments restants, sans doublon (clé canonique), dans l'ordre de valeur.
3. **Production** : appels groupés (Message Batches à moitié prix dès 20 appels), ou script déterministe quand aucune cognition n'est utile.
4. **Validation** : contrôles qui échouent bruyamment (schéma, cohérence, aucune case vide), erreurs écrites dans le fichier produit.
5. **Écriture idempotente** : un élément déjà produit n'est jamais refait ; un registre trace coût et mode.
6. **Orchestration** : GitHub Actions (cron, déclenchement sur push), file de tâches avec budget, reprise après échec, résolution automatique des conflits sur les fichiers de suivi.
7. **Suivi** : jauges recalculées automatiquement, rapport lisible, alerte si un étage bloque.

## Règles
- Tu fais un pilote de 3 éléments, tu l'audites, puis tu lances le lot.
- Tu sépares toujours l'automatique (0 token) du jugement (audit humain ou Claude).

Relais : `i-med-pipeline-builder` (sources médicales), `panoramic-skill-finder` (quoi automatiser).

Signature : AAI (Anthropic AI)
