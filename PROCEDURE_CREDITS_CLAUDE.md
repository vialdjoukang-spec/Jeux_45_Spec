# PROCÉDURE — Produire les QCM du jeu en JSON avec les crédits API Claude

> Script : `scripts/produire_items_claude.py`. Schéma : `scripts/schema_item.json`.
> Unité de travail : **1 requête = 1 rubrique d'une entité** de la Cartographie, qui produit autant d'items que son poids.
> Total : **59 390 requêtes, 119 242 items**. Ordre par défaut : **rétrograde, du SSP 248 vers le 001**.
> Économies intégrées : **API Batch** (environ −50 %) et **cache de prompt** (les règles ne sont payées qu'une fois).

## Étapes

| # | Étape | Résultat attendu |
|---|---|---|
| 1 | Installer les bibliothèques Python | Aucune erreur rouge |
| 2 | Créer la clé API et l'enregistrer | Clé visible dans la Console |
| 3 | Fixer une limite de dépense | Limite affichée dans la Console |
| 4 | Mettre le dépôt à jour | `scripts/produire_items_claude.py` présent |
| 5 | **Pilote** : 3 requêtes immédiates | 3 fichiers JSON dans `content/items/G1/…` |
| 6 | Lire les JSON du pilote et le coût réel | Qualité validée, coût par item connu |
| 7 | Lancer un SSP entier en batch | Un identifiant de batch s'affiche |
| 8 | Récupérer les résultats | Fichiers écrits et `registre_production.csv` à jour |
| 9 | Mesurer l'avancement, puis pousser sur GitHub | Pourcentage affiché, commit poussé |

### 1. Bibliothèques
```
python --version
```
*(Vérifier que Python 3.10 ou plus est installé ; sinon, l'installer depuis python.org en cochant « Add to PATH ».)*

```
pip install anthropic jsonschema
```
*(Installer le client de l'API Claude et le validateur de schéma.)*

### 2. Clé API
Crée une clé sur https://platform.claude.com, rubrique **API keys**, puis enregistre-la :
```
setx ANTHROPIC_API_KEY "ta_clé_ici"
```
*(Enregistrer la clé dans Windows ; ferme puis rouvre PowerShell ensuite.)*

🛑 La clé ne va **jamais** dans un fichier du dépôt, qui est public.

### 3. Limite de dépense
Dans la Console, rubrique **Limits** : fixe une limite mensuelle de **200 $**. Le script s'arrête alors de lui-même quand les crédits sont épuisés.

### 4. Dépôt à jour
```
cd "C:\Users\viald\OneDrive\Documents\Jeux_45_Spec"
```
*(Entrer dans le dépôt du jeu.)*

```
git pull
```
*(Récupérer le script et le schéma.)*

### 5. Pilote (3 requêtes immédiates, sans batch)
```
python scripts/produire_items_claude.py pilote --ssp G1 --n 3
```
*(Produire 3 rubriques de G1 pour juger la qualité et le coût.)*

### 6. Vérifier la qualité et le coût
- Ouvre les 3 fichiers de `content/items/G1/…` : énoncés, distracteurs, échelle en 7 marches, sources.
- Ouvre `registre_production.csv` : tokens consommés par requête.
- Lis le coût réel dans la Console, rubrique **Usage**. Le coût par item × 119 242 donne le coût total ; le batch le divise environ par deux.

### 7. Lancer un SSP entier en batch
```
python scripts/produire_items_claude.py soumettre --ssp G1
```
*(Soumettre les 330 rubriques de G1, soit 699 items, en batch.)*

Variantes :
```
python scripts/produire_items_claude.py soumettre --max 2000
```
*(Soumettre les 2000 prochaines rubriques en ordre rétrograde, du SSP 248 vers le 001.)*

```
python scripts/produire_items_claude.py soumettre --priorite --max 2000
```
*(Soumettre d'abord les entités d'urgence, puis les plus fréquentes.)*

### 8. Récupérer
```
python scripts/produire_items_claude.py statut
```
*(Voir l'état des batchs ; attendre « ended », en général moins d'une heure.)*

```
python scripts/produire_items_claude.py recuperer
```
*(Télécharger, valider et écrire les fichiers JSON.)*

Chaque fichier contient `controles.erreurs` : une liste vide signifie que le schéma et les règles A et K' sont respectés. Un fichier qui porte des erreurs est à refaire : supprime-le, puis relance `soumettre`.

### 9. Avancement et sauvegarde
```
python scripts/produire_items_claude.py bilan
```
*(Afficher le pourcentage d'items produits.)*

```
git add content registre_production.csv scripts/batchs.json
```
*(Préparer l'envoi des items produits.)*

```
git commit -m "Items produits par l'API Claude (batch)"
```
*(Enregistrer l'étape.)*

```
git push
```
*(Envoyer sur GitHub.)*

## Règles d'usage
- **Le modèle par défaut est Sonnet** (`claude-sonnet-5-5`). Pour Opus, ajoute `--modele claude-opus-5-5`, mais réserve-le aux rubriques difficiles : il coûte nettement plus.
- **Le script ne refait jamais ce qui existe** : une rubrique déjà écrite est sautée. Tu peux donc le relancer sans risque.
- **Simulation gratuite** : ajoute `--sec` à n'importe quelle commande pour voir ce qui serait envoyé, sans rien payer.
- **REJECTOR_ reste obligatoire** (canevas § 5). Ces items sortent avec `audit.rejector = null`. Un autre fournisseur (Gemini) ou une passe séparée doit vérifier le fond avant l'entrée dans le jeu.
- **Les 200 $ ne couvriront pas les 119 242 items.** Le pilote donne le chiffre exact. Commence donc par les urgences (`--priorite`), car c'est là qu'une erreur coûte le plus, en examen comme en pratique.
