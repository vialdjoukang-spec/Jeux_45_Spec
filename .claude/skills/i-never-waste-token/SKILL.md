---
name: i-never-waste-token
description: Va chercher exactement l'extrait utile (texte, chiffre, ligne de code) avec sa source, sans bruit : recherche ciblée, extraits par lignes, index, caches, délégation des lectures volumineuses. S'active pour toute lecture ou recherche d'information.
---

# I-never-waste-Token

## Règles de lecture
1. **Chercher avant de lire** : `grep -n`, `jq`, index ou empreinte d'abord ; tu ne lis que les lignes qui répondent, jamais un gros fichier entier.
2. **Ne jamais relire** un contenu inchangé : tu compares l'empreinte (sha256) ou la date avant de rouvrir.
3. **Extraire, pas résumer** : tu rapportes l'extrait exact, court, avec sa source (chemin et lignes, ou URL et date de consultation).
4. **Déléguer le volumineux** : une recherche large passe par un agent qui ne renvoie que la synthèse et les extraits utiles.

## Règles de recherche web
- Une requête précise de quelques mots, puis une lecture ciblée de la page (consigne qui demande l'extrait exact).
- Pas deux requêtes qui se ressemblent à plus de 80 %.
- Tu caches les réponses réutilisables dans le dépôt (références, glossaires) pour ne plus les rechercher.

## Ce qui reste interdit
Une économie qui ampute un fait médical : si la coupe touche le fond, tu lis davantage.

Relais : `harness-for-work`, `med-text-contractor`.

Signature : AAI (Anthropic AI)
