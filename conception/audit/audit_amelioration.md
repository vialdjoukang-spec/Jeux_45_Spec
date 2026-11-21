# Audit d'amélioration et de correction — 2026-11-21 (soir)

Contrôles automatiques : `auditer_conception.py` (20/20), `auditer_couverture.py` (réussi), 3 plans à 31/31.

## Constats corrigés
| # | Constat | Correction |
|---|---|---|
| 1 | Le prototype ne développait les circuits que vers la droite. | La règle du côté est appliquée : le circuit des poumons se développe à gauche, le corps glisse à droite ; le circuit du cœur se développe à droite. |
| 2 | Quatre cases d'organes n'avaient pas d'infobulle (encéphale, foie, reins, bassin). | Leurs infobulles sont rédigées ; l'audit bloque désormais toute case sans infobulle. |
| 3 | Les cases du prototype Paraclinique n'avaient pas d'infobulle. | Les 10 cases ont maintenant leur infobulle à quatre rubriques. |
| 4 | Un temps d'examen (percussion de la condensation) n'offre qu'un signe valide. | Le signe reste seul, il est marqué « uniqueAssume », et son infobulle le dit : aucun signe n'est inventé pour remplir. |
| 5 | Le générateur produisait des fichiers aux noms génériques (« <lettre>.json », « <organe>.json »). | Ces modèles ne sont plus écrits ; l'audit refuse tout nom générique. |
| 6 | La fenêtre de clichés ne montrait pas l'anatomie normale. | À droite, une radiographie normale réelle porte 8 repères lettrés ; à gauche, un bouton bascule le cliché du patient entre brut et annoté. |
| 7 | Une classe CSS de l'image normale entrait en conflit avec celle des cases. | Les classes sont renommées. |
| 8 | Les cases cachées réapparaissaient quand une lentille était active. | Une case cachée reste invisible, quelle que soit la lentille. |
| 9 | Du code de dessin SVG abandonné restait dans le rendu des plans. | Il est supprimé. |
| 10 | D'anciennes images de prototype ne servaient plus. | Elles sont supprimées ; le dossier `donnees/` est régénéré à neuf. |

## Ajouts faits immédiatement (à valider)
| # | Ajout | Pourquoi |
|---|---|---|
| A | Onglet « Disciplines transversales » : 19 disciplines-outils (A → S, avec sous-onglets et leçons de la Cartographie) et 12 lentilles cliniques. | Les lentilles isolent ce qui est propre à une discipline dans les zones communes. |
| B | Sélecteur de lentille dans le prototype, pastille sur les cases concernées, ligne « Particularité » dans l'infobulle. | La lentille montre en un clic ce qui change chez l'enfant, la personne âgée ou la femme enceinte. |
| C | Infobulle de diagnostic : bilan en six visées (diagnostique, étiologique, retentissement, complications, rémission, sortie) et traitement avec posologie et source. | La répétition fixe la connaissance d'un onglet à l'autre. |
| D | Facteur discriminant de 27 techniques et séquences (IRM : T1, T2, FLAIR, diffusion/ADC, SWI, gadolinium, STIR, angio, cholangio, perfusion, corps entier). | Tu dois savoir quel examen demander, et pourquoi lui plutôt qu'un autre. |
| E | Smarter medicine : 5 recommandations suisses amorcées, dont une marquée « à vérifier ». | Elles freinent la surprescription. |
| F | Fenêtre de structure anatomique en 3D réelle, à quatre vues, avec la crosse aortique renforcée et la radio-anatomie correspondante. | L'anatomie vue sous plusieurs angles prépare la lecture des images. |
| G | Un son réel de plus (crépitants localisés de la pneumonie). | La pneumonie et l'insuffisance cardiaque se distinguent aussi à l'oreille. |

## Reste à faire
| # | Point | Prochaine action |
|---|---|---|
| 1 | Posologies pédiatriques de la pneumonie | À vérifier dans les recommandations suisses avant de les écrire. |
| 2 | Recommandations smarter medicine complètes | Recopier les listes officielles depuis smartermedicine.ch. |
| 3 | Champs `discriminant`, `avantageSelectif` et `visees` des 601 examens du catalogue | Production système par système avec Claude Code, puis contrôle par REJECTOR_. |
| 4 | Modèles 3D plus fins (muscles, nerfs, couches de la tête) | Ajouter Z-Anatomy au pipeline 3D. |
