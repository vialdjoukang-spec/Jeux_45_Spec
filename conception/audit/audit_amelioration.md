# Audit d'amélioration et de correction — 2026-11-21

| # | Constat | Gravité | Action |
|---|---|---|---|
| 1 | Les examens complémentaires étaient listés par onglet, sans référentiel commun : des oublis restaient possibles. | Haute | Un catalogue topographique unique a été créé (`outils/catalogue_paraclinique.py`) : 9 régions, 64 organes, 23 prélèvements, 5 modalités. |
| 2 | L'audit de couverture a trouvé un organe à une seule modalité (vaisseaux du cou). | Moyenne | L'organe devient « Vaisseaux du cou et de la tête » : échographie temporale, PET des gros vaisseaux, VS/CRP, Doppler transcrânien, biopsie de l'artère temporale. |
| 3 | L'audit a trouvé 8 organes rattachés à aucun système de la Tétrade. | Moyenne | Chaque organe est désormais rattaché à un système. |
| 4 | La Tétrade citait les examens dans plusieurs espaces. | Moyenne | Un onglet unique, « Examens complémentaires » (E9), regroupe les examens en progression topo-systémique ou topo-organe. Anatomie et Physiologie y renvoient. |
| 5 | La description du prototype de Paraclinique parlait encore d'ascite alors que l'image montre l'imagerie thoracique. | Basse | Le texte est aligné sur l'image. |
| 6 | L'index des JSON comptait deux fois les fichiers réécrits. | Basse | Les doublons sont retirés (422 fichiers distincts). |
| 7 | Le circuit de la Tétrade garde un nœud « examen clé » (NT-proBNP · échocardiographie). | Choix assumé | Ce nœud ferme le raisonnement ; un clic ouvre l'onglet Examens complémentaires pour la liste complète. |
| 8 | Les prototypes Pharmacologie et Paraclinique n'ont pas encore leurs infobulles. | À faire (implémentation) | La règle est écrite dans les plans ; les schémas refusent une case sans infobulle. |
| 9 | Les fiches d'examens contiennent les noms, pas encore les indications, les valeurs et les infobulles. | À faire (production) | Remplissage système par système, puis contrôle par REJECTOR_. |
| 10 | Une question reste ouverte : le système « Pédiatrique » reste-t-il séparé, ou l'âge devient-il une dimension transversale ? | À trancher | Décision de Vial attendue. |

**Contrôles automatiques :** les 3 plans réussissent 31 contrôles sur 31 ; l'audit de couverture réussit (14 systèmes reliés, aucun doublon, 101 examens témoins présents).
