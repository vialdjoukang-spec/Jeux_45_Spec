# Ébauche du jeu MedSuisse Arena 45 (fixée le 23.11.2026 pour ne rien perdre)

Ce document fige l'inspiration et la structure du jeu. Il complète `CANEVAS_GENIE_LOGICIEL.md` (règles détaillées) et `projets/4_Jeux_45_Spec/chantier.json` (étapes). Les 45 arènes sont déjà ébauchées en données : `content/arenes/<CODE>/arene.json` (script `scripts/ebaucher_arenes.py`, 0 token).

## 1. Ce que le jeu est, et ce qu'il n'est pas
- Le jeu est une **arène de résolution de problèmes cliniques** dans 45 spécialités suisses. Il prépare l'examen fédéral (QCM de type A et K', OSCE).
- Le jeu **n'a pas de cours** : la **correction commentée** tient lieu de cours. Les cours longs restent dans les SSP (Cartographie Renouveau) ; la Tétrade, la Paraclinique et le Transversal gardent leurs propres jeux.
- Le jeu ne suit **pas** la structure en réseau de la Tétrade : il suit la Cartographie Renouveau, entité par entité, rubrique par rubrique.

## 2. Structure (de la coque vers le centre)
1. **45 arènes**, une par spécialité, chacune avec son son et son effet (`data/references/sons_fx_45_spec.json`).
2. **Tuiles cachées** : chaque entité de la Cartographie devient une tuile (4 121 tuiles, car une entité peut ouvrir plusieurs arènes). Le joueur la révèle en réussissant ses questions trois fois, à intervalles espacés (FSRS).
3. **Paliers** : les tuiles se rangent des très fréquentes aux rares, avec les urgences entre les deux.
4. **Rubriques** : chaque tuile porte 15 à 17 rubriques de notions pondérées (définition, sciences fondamentales, physiopathologie, anamnèse, examen, drapeaux rouges, examen de référence, prise en charge aiguë et chronique, surveillance, pronostic, réseau…).
5. **Questions** : une notion de poids n exige au moins n questions ; 30 % au moins portent sur le zéro-D (définition, sciences fondamentales, physiopathologie) ; chaque tuile a un cas long en 6 étapes. Cible : environ 123 500 questions.
6. **Correction en 7 marches** : zéro-D → mécanisme → sémiologie → discriminant → décision → piège → ancre. Chaque option fausse reçoit son explication.

## 3. Modes de jeu
- **Arène** : duels chronométrés, du réflexe (premier geste) au raisonnement (vignette longue).
- **Aventure** : une carte par spécialité ; chaque poste correspond à un palier.
- **Puzzles** : ordonner les premiers gestes, choisir le discriminant, repérer le drapeau rouge, retrouver le chiffre clé.
- **Interface** : icônes avec infobulle « pourquoi », barre supérieure réduite, sigles définis en infobulle, présentations atypiques en rouge.

## 4. Fil de production continue
```
Cartographie Renouveau (data/ssp, 3 975 entités, 119 242 notions)
  ══> Ébauche des 45 arènes (scripts/ebaucher_arenes.py, 0 token)
  ══> Fiches de raisonnement, couche 1 (scripts/produire_fiches_claude.py, API en lot, −50 %)
  ══> Vérification des chiffres et des sources (pipeline i-Med : AIPS, sociétés suisses, PubMed ; deux sources concordantes ou une source primaire)
  ══> Audit médical de Claude (branche veille/audit-medical, chaque heure) ══> main
  ══> Cartes réflexes, couche 2 (scripts/generer_reflexes.py, 0 token)
  ══> Questions A et K', couche 3 (scripts/produire_items_claude.py, API en lot, à partir de la fiche validée)
  ══> Double contrôle par scripts A et B, puis audit REJECTOR_
  ══> Assemblage du jeu (arènes, aventure, FSRS, sons) ══> GitHub Pages
```
Chaque flèche tourne seule : l'ouvrier (`.github/workflows/ouvrier.yml`) prend la tâche suivante de `projets/ouvrier/FILE_PROCESSUS.json` toutes les 30 minutes, sous plafond de dépense.

## 5. Budget (décision de Vial du 23.11.2026)
- Le crédit API mensuel vaut 200 USD et n'est pas cumulable ; le jeu en utilise **au plus la moitié** chaque mois (`plafond_total_usd` = 100).
- Prix en lot de Sonnet 5.5 : 1 USD par million de tokens d'entrée et 5 USD par million de tokens de sortie. Une fiche coûte donc de l'ordre de quelques centimes ; le pilote mesure le coût réel avant toute série.
- Ordre de dépense : toutes les fiches d'abord (source de vérité), arène par arène, des très fréquentes aux rares ; puis les questions des arènes prioritaires (cardiologie, médecine interne, urgences, psychiatrie).

## 6. Points à vérifier dans les données (relevés pendant l'ébauche)
- Certaines entités portent une strate étonnante dans la Cartographie (par exemple « Asystolie sur hypoxie prolongée » classée très fréquente) : la fiche corrigera la fréquence et le signalera.
- Certaines entités se doublent presque (par exemple deux entrées d'extrasystoles bénignes) : l'audit les fusionnera avant de produire leurs questions.

## 7. Prochaines étapes
1. Pilote : 2 fiches de cardiologie (tâche `j45_pilote_fiches` de la file), audit, ajustement de la consigne.
2. Série : fiches de cardiologie en lot, puis les autres arènes.
3. Réflexes par script, dès les premières fiches validées.
4. Questions de la cardiologie, puis des autres arènes, dans la limite du budget.

Signature : AAI (Anthropic AI)
