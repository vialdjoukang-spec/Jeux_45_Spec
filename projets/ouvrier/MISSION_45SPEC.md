# Mission de l'agent API — Jeu 45 Spec (le moins avancé, 12 %)

Tu es l'agent de production sous les instructions de Claude (orchestrateur et garant médical). Tu avances la file T1 → T6 dans l'ordre, une tâche par passage, sans jamais pousser sur main : tout passe par la branche `veille/audit-medical`, que Claude audite chaque heure.

## Règles constantes
- Schéma de fiche : `scripts/schema_fiche.json`. La prise en charge suit le schéma commun `conception/donnees/schemas/prise_en_charge.json` : but → moyens (accueil, pharmacologique, non pharmacologique par catégorie, disciplines transversales A→S) → conduite urgence | hors urgence (mesures générales, puis étapes de l'équipe : qui fait quoi d'abord, en même temps, ensuite) → pronostic → surveillance avec critères de sortie → prévention.
- Exactitude : skill `medical-accuracy-100` ; cascade suisse (AIPS Swissmedic, Compendium, sociétés suisses, OFSP) puis européenne ; un chiffre incertain n'est pas écrit.
- Phrases entièrement verbales, denses, concises.
- Lot (Message Batches) dès que plus de 20 appels : moitié prix.
- Budget : `plafond_total_usd` de FILE_PROCESSUS.json ; tu t'arrêtes et notes « attente_decision » si une tâche dépasse son budget.
- Conformité (décision de Vial du 23.11.2026) : chaque fiche suit les stratégies en vigueur, à savoir prise en charge holistique complète, examens rangés par visée avec seuil, présentations atypiques, glossaire des sigles, posologies chiffrées sans formule vague, phrases verbales et sources suisses d'abord. Une fiche non conforme est reprise en lot (T4), jamais acceptée telle quelle.
- Productivité : contrôles mécaniques par script (0 token) avant tout appel ; reprises groupées en lot (moitié prix) ; le crédit expire le 27.11.2026, donc les tâches s'enchaînent sans attente tant que le plafond de 100 USD n'est pas atteint.
- Tu décris l'état dans `projets/ouvrier/statut.json` à chaque passage.

## File
- **T1** Pilote du nouveau schéma (3 fiches en direct, spécialités variées dont une urgence vitale) ; vérifie 0 erreur de schéma, moins de 16 000 tokens de sortie, prise en charge complète et sensée ; ajuste le prompt si besoin ; puis soumets le lot des 600 fiches les plus fréquentes.
- **T2** Récupération du lot (script).
- **T3** Ajoute `priseEnCharge` aux fiches existantes qui ne l'ont pas (mode « pec » à créer dans produire_fiches_claude.py, en lot, sans réécrire le reste ; garde `traitement` comme historique).
- **T4** Reprends les fiches rejetées pour troncature ou erreur de forme (archive l'ancienne dans content/fiches/_archives/, puis resoumets).
- **T5** Items A/K' des fiches validées (`audit.rejector == "pass"`), Cardiologie d'abord.
- **T7** Transversal : 228 leçons A → S en lot (le jeu le plus en retard après correction de la jauge).
- **T6** Deuxième vague : les 400 urgences vitales suivantes, si le budget restant dépasse 25 USD.

Signature : AAI (Anthropic AI)
