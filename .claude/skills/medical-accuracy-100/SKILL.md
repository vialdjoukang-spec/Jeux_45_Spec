---
name: "medical-accuracy-100"
description: "Rédaction médicale de précision maximale, systématiquement vérifiée et sourcée. S'active d'office dès qu'un sujet relève du champ lexical médical (maladie, symptôme, examen, médicament, posologie, physiologie, recommandation)."
---

# Medical accuracy 100

Le but est qu'aucune affirmation médicale ne repose sur la seule mémoire du modèle. Une précision absolue ne se garantit pas : ce skill la remplace par la règle qui s'en approche le plus, à savoir vérifier, sourcer, et signaler ce qui ne l'est pas. Les sources augmentent aussi la crédibilité de chaque réponse : elles sont donc systématiques, courtes et précises.

## Règles de rédaction
1. **Vérifie avant d'écrire** tout chiffre, seuil, posologie, critère diagnostique, classe de recommandation et toute donnée qui change dans le temps (recommandations, autorisations, tarifs). Utilise d'abord les sources primaires : recommandations des sociétés savantes (ESC, ESVS, EULAR, ERS, KDIGO…), information professionnelle Swissmedic (AIPS, compendium.ch), Liste des analyses OFSP ; puis PubMed, Consensus ou Elicit pour les études.
2. **Préfère la source suisse** quand elle existe (Swissmedic, OFSP, sociétés suisses), puis européenne, puis internationale. Signale un désaccord entre sources, par exemple l'atropine à 0,5 mg selon l'ERC 2025 et à 1 mg selon l'AHA 2025.
3. **Source chaque fait vérifiable** juste après lui, en format court : [Société ou auteur, année, document]. Termine par une liste « Sources » de liens cliquables. Tu reformules au lieu de citer longuement.
4. **Ne fabrique jamais** une référence, un DOI, un chiffre ou une citation. Si tu n'as pas pu vérifier, écris « à vérifier » et dis où vérifier.
5. **Distingue** le fait établi, la recommandation (avec sa classe et son niveau quand ils existent) et l'avis d'expert.
6. **Date** chaque recommandation citée et vérifie qu'aucune version plus récente ne l'a remplacée.
7. **Posologies** : donne la dose, la voie, le rythme, l'adaptation (rein, foie, âge, poids) et la source ; renvoie à l'AIPS pour la version suisse officielle.
8. **Écris en phrases verbales**, concises et claires, jamais nominales.

## Contrôle final
Relis la réponse en cherchant chaque nombre et chaque nom propre : chacun porte sa source ou la mention « à vérifier ».