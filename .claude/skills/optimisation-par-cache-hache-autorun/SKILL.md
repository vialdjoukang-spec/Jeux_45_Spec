---
name: "optimisation-par-cache-hache-autorun"
description: "Ne refait jamais un travail dont les entrées n'ont pas changé : empreinte sha256, saut automatique, relance seule au changement (hooks, GitHub Actions, cron). S'active dès qu'un script, un audit, un appel API ou une lecture se répète."
---

# Optimisation par cache haché, autoRUN

Un travail déterministe produit la même sortie à partir des mêmes entrées. Si on mémorise l'empreinte des entrées, on peut sauter toute ré-exécution inutile et ne relancer que ce qui a vraiment changé. Le gain est réel (tokens, minutes, crédit API), et la qualité ne bouge pas, puisqu'aucune décision n'est prise sur une copie périmée.

Le script se trouve dans github.com/vialdjoukang-spec/Jeux_45_Spec/tree/main/.claude/skills/optimisation-par-cache-hache-autorun/scripts/cache_hache.py. Copie-le s'il n'est pas sur le disque.

## 1. Les trois niveaux de cache (du moins cher au plus cher)
1. **Le calcul local.** Enveloppe chaque script déterministe avec `cache_hache.py`.
   Exemple : `python cache_hache.py -i 'content/**/*.json' -i scripts/construire.py -o sortie/ -- python scripts/construire.py`.
   Le script hache le contenu des entrées, la commande et les variables déclarées (`-e`), puis il vérifie que les sorties existent et n'ont pas été modifiées à la main. Si rien n'a bougé, il saute le travail. Il ne met jamais un échec en cache.
2. **Le réseau.** Mets en cache chaque requête HTTP répétée avec `requests-cache` ou `Hishel`, avec une expiration adaptée à la source : 1 jour pour une recommandation, 1 heure pour un état ou une file. Dans GitHub Actions, utilise `actions/cache` avec une clé `hashFiles(...)`.
3. **Le modèle.** Ne renvoie jamais le même prompt deux fois.
   - Tiens un registre `empreinte(prompt + modèle + version du gabarit) → sortie`.
   - Côté API Anthropic, place le gros contexte fixe en tête et marque-le `cache_control`, pour que le cache de prompt facture la relecture à prix réduit.
   - Mets le volumineux non urgent en Batch.
   - Avant de relancer une file, retire les tâches dont l'empreinte de sortie existe déjà.

## 2. AutoRUN : relancer seul, seulement au changement
- **GitHub Actions** : filtre `paths:` sur les entrées, et une étape `cache_hache.py` qui saute si l'empreinte est connue. Ajoute un `schedule` cron seulement si la source change hors du dépôt.
- **Hook git** `post-merge` ou `pre-commit` : il appelle les tâches enveloppées. Le cache rend l'appel quasi gratuit quand rien n'a changé.
- **Une file d'agents** : chaque tâche porte l'empreinte de ses entrées. Une tâche dont l'empreinte de sortie est déjà enregistrée passe à « fait » sans appel.

## 3. Ce qu'on ne met jamais en cache
- Un résultat dont la justesse dépend du temps (posologie, recommandation, tarif) au-delà de sa durée de validité.
- Une sortie en échec ou partielle.
- Un jugement médical ou éditorial à refaire quand le contexte change : on cache le calcul, pas la décision.

## 4. Preuve et suivi
- `cache_hache.py --etat` liste chaque tâche, sa date, son nombre de fichiers et ses sauts cumulés : c'est la mesure du gain.
- Avant de brancher le cache sur une tâche, prouve-le en 4 cas : premier passage exécuté, second sauté, entrée modifiée relancée, sortie supprimée relancée.
- Versionne le registre `.cache_hache.json` seulement si le cache doit survivre aux clones. Sinon, ajoute-le à `.gitignore`.

## Relais
`harness-gen-network` (réseau de scripts), `i-never-waste-token` (lecture ciblée), `pipeline-autonomous-builder` (workflows), `panoramic-skill-finder` (repérer où brancher le cache).

Signature : AAI (Anthropic AI)