# Test comparatif — mêmes 10 pathologies (TEST_COMPARATIF.json), 27.11.2026

| | Gemini 4 Neon (medium, API) | Claude Fable 5.2 (Claude Code) |
|---|---|---|
| Constats | 58 (4 🟥 · 22 🟧 · 23 🟨 · 9 🟦) | 95 (2 🟥 · 21 🟧 · 60 🟨 · 12 🟦) |
| Recherches web réelles | **0 sur 10 lots** (journal couts.jsonl), malgré la consigne | liens datés du 27.11 sur 91/95 constats (non comptables) |
| Confiance déclarée | 57 « certaine », 1 « à confirmer » | 58 certaine · 29 probable · 8 à confirmer |
| Coût / durée | 3,11 $ · ~2 min par lot | forfait Claude · non mesuré |

## Constats graves recoupés
| Lot | Erreur | Gemini | Fable | Vérifié par Claude |
|---|---|---|---|---|
| MIG Z00.1 | « Grenzsteine der Entwicklung » attribués au mauvais auteur (Michaelis, Tübingen) | 🟥 | 🟥 | à confirmer (lecture du lien bloquée sans approbation) |
| HEM D69.0 | Kprim : « plaquettes normales excluent… » coté vrai pour la leucémie | 🟥 | 🟧 | — |
| LEG Y69.1 | Posologie de protamine non conforme à l'AIPS suisse | 🟥 | 🟧 | — |
| OPH H00.0 | Flucloxacilline orale non commercialisée en Suisse | 🟧 | 🟥 | à confirmer (compendium.ch) |
| CPE K56.1 | Antécédent d'invagination = contre-indication à Rotarix | 🟥 | 🟧 partiel | **confirmé** : EMA, RCP Rotarix § 4.3 |

## Lecture
- Les deux trouvent les mêmes erreurs graves ; ils diffèrent surtout sur la gravité attribuée.
- Fable produit davantage de constats mineurs et nuance mieux sa confiance ; Gemini affiche « certaine » sans avoir fait de recherche web.
- Chaque constat reste à vérifier dans sa source avant correction.
