# SSP+ v2 — revue des 1094 points de départ hors catalogue

`ssp_plus_v2.json` s'ajoute au travail existant ; aucun fichier de `data/ssp_etendus`, `content/` ou `conception/` n'a changé.

## Règles appliquées
1. Un SSP+ ne double jamais un SSP officiel : s'il le reformule, il est retiré (`retire_doublon_catalogue`, champ `doublonDe`). Un qualificatif générique (âge seul, « sévère », « accidentel ») ne suffit pas ; une durée, un caractère ou un signe associé discriminant suffit.
2. Notation : `G17(+)`… après G16 ; pour S, F et O, la numérotation continue après le dernier officiel du groupe parent (S4.18 → `S4.19(+)`).
3. La catégorie suit la nature (G plainte générale, S symptôme ou signe, F résultat d'examen, O situation) ; le parent porte la même lettre (`deplace` sinon).
4. Deux SSP+ qui se doublent fusionnent (`fusionne_dans`, champ `fusionneDans` = code gardé).
5. On n'ajoute (`ajoute`) que ce qu'une source lue appuie.

## Fichiers
- `decisions_v2.tsv` : chaque arbitrage manuel, avec sa justification en une ligne.
- `ajouts_v2.json` : les ajouts et leurs sources.
- `numeroter.py` : construit `ssp_plus_v2.json` et attribue les codes (ordre du parent, puis ancien ordre).
- `controle.py` : contrôles mécaniques ; il doit afficher 0 erreur.

## Comptes (1097 entrées)
| Statut | n |
|---|---|
| garde | 736 |
| deplace | 274 |
| retire_doublon_catalogue | 65 |
| fusionne_dans | 19 |
| ajoute | 3 |

Actifs par catégorie : G 53, S 349, F 518, O 93.

## Points ouverts pour Vial
- 15 résultats d'exploration fonctionnelle (EMG, audiométrie, pH-métrie…) restent en S : aucun SSP F officiel ne couvre leur modalité (justification « À ARBITRER »).
- 23 intitulés sont des diagnostics plutôt que des points de départ (justification « Intitulé diagnostique ») : ils sont gardés et signalés pour reformulation.
- Plusieurs parents F sont des ancrages faute de mieux (F2.14 pour les hormones non thyroïdiennes, F2.19 pour la microbiologie) : la justification le dit.

Relance : `python3 projets/ssp_plus/numeroter.py` puis `python3 projets/ssp_plus/controle.py`.

Signature : AAI (Anthropic AI)


## ANNULÉ (Vial, 25.11.2026)
Le projet SSP+ est annulé : seul le catalogue officiel compte. Ces fichiers restent en archive ; aucun QCM n’avait été produit sur un SSP+.
