# PROCÉDURE — Produire le jeu en JSON avec les crédits API Claude

## Architecture en 3 couches (la moins coûteuse pour la plus haute qualité)

| Couche | Fichiers JSON | Produit par | Coût | Rôle pédagogique |
|---|---|---|---|---|
| **1. Fiches de raisonnement** | `content/fiches/<SPEC>/<entité>.json` (3 975) | API Claude, Sonnet, Batch | **Payant, une fois par entité** | La source unique de vérité : quoi faire **en premier**, puis ensuite ; drapeaux rouges ; discriminants ; examens et traitement dans l'ordre ; chiffres clés sourcés ; échelle 0-D → ancre ; pièges. |
| **2. Cartes réflexes** | `content/reflexes/<SPEC>/<entité>.json` (environ 20 par fiche, soit environ 80 000) | Script `generer_reflexes.py` | **0 token** | L'instantanéité : premier geste, ordonner la conduite, drapeau → action, discriminant, chiffre, mécanisme, premier examen (5 à 20 s par carte). |
| **3. Vignettes riches A / K'** | `content/items/<SPEC>/<entité>/<rubrique>.json` | API Claude, à partir de la fiche validée | Payant, en option, par priorité | Le raisonnement long, au format de l'examen fédéral. |

**Pourquoi cette architecture**
- On paie le savoir **une seule fois** (la fiche), puis on le décline gratuitement en réflexes.
- **REJECTOR_ vérifie 3 975 fiches** au lieu de 119 242 items. Toutes les cartes dérivées héritent d'un fond vérifié.
- Le jeu reste cohérent : une carte réflexe ne peut jamais contredire sa fiche.

**Ordre de production :** spécialité par spécialité, **du plus banal au plus rare** : très fréquent → fréquent → urgences → peu fréquent → rare. Les entités banales forment les réflexes du quotidien ; un raisonnement compris sur elles se transfère au reste.

## Étapes

| # | Étape | Résultat attendu |
|---|---|---|
| 1 | Installer les bibliothèques | Aucune erreur rouge |
| 2 | Créer et enregistrer la clé API | Clé visible dans la Console |
| 3 | Fixer une limite de 200 $ dans la Console (Limits) | Limite affichée |
| 4 | Mettre le dépôt à jour | Les scripts sont présents |
| 5 | **Pilote** : 2 fiches immédiates | 2 fichiers dans `content/fiches/CAR/` |
| 6 | Lire les 2 fiches et le coût réel (Console, Usage) | Qualité validée, coût par fiche connu |
| 7 | Lancer une spécialité en batch | Un identifiant de batch s'affiche |
| 8 | Récupérer les fiches | `registre_fiches.csv` à jour |
| 9 | Faire auditer les fiches par REJECTOR_ | `audit.rejector = "pass"` dans chaque fiche validée |
| 10 | Générer les réflexes (0 token) | Cartes dans `content/reflexes/` |
| 11 | Pousser sur GitHub | Commit visible |

### 1. Bibliothèques
```
pip install anthropic jsonschema
```
*(Installer le client de l'API Claude et le validateur de schéma.)*

### 2. Clé API (créée sur https://platform.claude.com, rubrique API keys)
```
setx ANTHROPIC_API_KEY "ta_clé_ici"
```
*(Enregistrer la clé dans Windows ; rouvre ensuite PowerShell.)*

🛑 La clé ne va jamais dans un fichier du dépôt public.

### 4. Dépôt à jour
```
cd "C:\Users\viald\OneDrive\Documents\Jeux_45_Spec"
```
*(Entrer dans le dépôt.)*

```
git pull
```
*(Récupérer les scripts.)*

### 5. Pilote
```
python scripts/produire_fiches_claude.py pilote --spec CAR --n 2
```
*(Produire tout de suite 2 fiches de cardiologie, les plus banales d'abord.)*

### 7. Batch d'une spécialité
```
python scripts/produire_fiches_claude.py soumettre --spec CAR
```
*(Soumettre les 175 fiches de cardiologie en batch, environ −50 %.)*

```
python scripts/produire_fiches_claude.py soumettre --max 500
```
*(Variante : soumettre les 500 prochaines fiches, toutes spécialités confondues, du plus banal au plus rare.)*

### 8. Récupération
```
python scripts/produire_fiches_claude.py statut
```
*(Voir l'état des batchs ; attendre « ended ».)*

```
python scripts/produire_fiches_claude.py recuperer
```
*(Écrire et valider les fiches.)*

```
python scripts/produire_fiches_claude.py bilan
```
*(Afficher l'avancement, par niveau de fréquence.)*

### 10. Réflexes (0 token, uniquement sur les fiches validées par REJECTOR_)
```
python scripts/generer_reflexes.py
```
*(Générer les cartes réflexes à partir des fiches validées.)*

### 3 (optionnel). Vignettes riches, à partir des fiches
```
python scripts/produire_items_claude.py soumettre --spec CAR
```
*(Produire les vignettes A/K' des entités de cardiologie dont la fiche existe.)*

### 11. Sauvegarde
```
git add content registre_fiches.csv scripts/batchs_fiches.json
```
*(Préparer l'envoi des fiches et des cartes.)*

```
git commit -m "Fiches et réflexes produits"
```
*(Enregistrer l'étape.)*

```
git push
```
*(Envoyer sur GitHub.)*

## Règles
- **Le modèle par défaut est Sonnet.** Ajoute `--modele claude-opus-5-5` uniquement pour les fiches qui échouent ou que tu juges faibles.
- **Rien n'est refait deux fois** : une fiche existante est sautée.
- **Simulation gratuite** : ajoute `--sec` à n'importe quelle commande.
- **Une fiche dont `controles.erreurs` n'est pas vide est à refaire** : supprime-la, puis relance `soumettre`.
- **REJECTOR_ est obligatoire** avant la génération des réflexes ; `generer_reflexes.py` ignore les fiches non validées.
- **Budget :** le pilote donne le coût réel d'une fiche. Multiplie-le par 3 975, puis divise par deux pour le batch : tu sauras ce que couvrent tes 200 $. Les fiches passent avant les vignettes.
