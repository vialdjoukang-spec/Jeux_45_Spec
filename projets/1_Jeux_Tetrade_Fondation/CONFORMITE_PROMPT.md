# Conformité au prompt épinglé (PROMPT_VIAL.md) — système par système

Généré par `projets/1_Jeux_Tetrade_Fondation/outils/conformite_prompt.py` le 2026-11-28 (0 token). ✅ conforme ; ⚠️ écart mesuré. Les chiffres comptent les sources `conception/outils/<système>/`.

## 1. Exigences propres à chaque système

| Phrase du prompt | cardio | respi | digestif | renal | neuro | endocrino | hemato | infectio | orl | loco | derma | psyche | gyneco | pediatrie |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| « Cela concerne toute les systèmes possibles » ; « on déroule tous les organes du système, de haut en bas » (21.11) | ✅ 14/14 organes | ✅ 11/11 organes | ✅ 13/13 organes | ✅ 6/6 organes | ✅ 13/13 organes | ✅ 10/10 organes | ✅ 7/7 organes | ✅ 5/5 organes | ✅ 9/9 organes | ✅ 11/11 organes | ✅ 6/6 organes | ✅ 7/7 organes | ✅ 7/7 organes | ✅ 5/5 organes |
| « la TETRADE : Anatomie + Physiologie + Sémiologie + Physiopathologie » (chaque organe a ses 4 espaces) | ⚠️ 13/14 | ⚠️ 9/10 | ✅ 12/12 | ✅ 6/6 | ✅ 13/13 | ✅ 10/10 | ✅ 6/6 | ✅ 4/4 | ✅ 5/5 | ✅ 11/11 | ✅ 6/6 | ✅ 7/7 | ✅ 7/7 | ✅ 5/5 |
| « structure en image de taille réduite » (ancre 3D réelle de l'organe) | ⚠️ 12/14 | ✅ 11/11 | ✅ 13/13 | ✅ 6/6 | ⚠️ 12/13 | ⚠️ 9/10 | ⚠️ 3/7 | ⚠️ 1/5 | ✅ 9/9 | ✅ 11/11 | ⚠️ 0/6 | ✅ 7/7 | ✅ 7/7 | ⚠️ 3/5 |
| « anatomie macro » (organes dont l'anatomie en parle, mesure par mots-clés) | ✅ 14/14 | ⚠️ 8/10 | ⚠️ 9/12 | ✅ 6/6 | ⚠️ 10/13 | ⚠️ 8/10 | ✅ 6/6 | ⚠️ 1/4 | ✅ 5/5 | ⚠️ 6/11 | ⚠️ 0/6 | ⚠️ 5/7 | ⚠️ 5/7 | ⚠️ 1/5 |
| « anatomie micro » (organes dont l'anatomie en parle, mesure par mots-clés) | ⚠️ 13/14 | ⚠️ 8/10 | ⚠️ 11/12 | ⚠️ 5/6 | ✅ 13/13 | ✅ 10/10 | ✅ 6/6 | ✅ 4/4 | ✅ 5/5 | ⚠️ 8/11 | ⚠️ 5/6 | ⚠️ 4/7 | ⚠️ 4/7 | ⚠️ 0/5 |
| « vascularisation » (organes dont l'anatomie en parle, mesure par mots-clés) | ✅ 14/14 | ⚠️ 7/10 | ⚠️ 9/12 | ⚠️ 4/6 | ✅ 13/13 | ✅ 10/10 | ✅ 6/6 | ⚠️ 1/4 | ✅ 5/5 | ⚠️ 7/11 | ⚠️ 2/6 | ⚠️ 0/7 | ⚠️ 4/7 | ⚠️ 1/5 |
| « innervation » (organes dont l'anatomie en parle, mesure par mots-clés) | ⚠️ 8/14 | ⚠️ 6/10 | ⚠️ 5/12 | ⚠️ 4/6 | ✅ 13/13 | ✅ 10/10 | ⚠️ 2/6 | ⚠️ 0/4 | ✅ 5/5 | ⚠️ 5/11 | ⚠️ 2/6 | ⚠️ 0/7 | ⚠️ 0/7 | ⚠️ 0/5 |
| « le réseau physiologie : points de départ… schéma évidement » (mots-clés ouvrant une fenêtre de courbe) | ✅ 40/80 | ✅ 20/45 | ✅ 10/47 | ✅ 3/29 | ✅ 4/58 | ✅ 12/54 | ✅ 8/31 | ✅ 2/18 | ✅ 12/24 | ✅ 3/28 | ✅ 1/16 | ⚠️ 0/32 | ⚠️ 0/18 | ⚠️ 0/16 |
| « au temps de l'examen clinique » (temps avec 2–3 signes typiques ou 1 unique) | ⚠️ 25/43 | ⚠️ 18/27 | ⚠️ 28/35 | ✅ 17/17 | ✅ 27/27 | ✅ 30/30 | ✅ 13/13 | ✅ 11/11 | ⚠️ 14/15 | ✅ 30/30 | ✅ 12/12 | ⚠️ 13/14 | ✅ 14/14 | ✅ 10/10 |
| « la technique exacte et le nom dédié du signe (éponyme ?) » (signes à éponyme) | ✅ 3/94 | ✅ 2/52 | ✅ 3/78 | ✅ 1/49 | ✅ 5/81 | ✅ 5/95 | ✅ 1/39 | ⚠️ 0/28 | ✅ 1/46 | ✅ 7/70 | ⚠️ 0/30 | ✅ 1/39 | ⚠️ 0/37 | ⚠️ 0/29 |
| « par survol du symptôme on voit la question à poser et les caractéristiques » (symptômes d'interrogatoire dont l'infobulle formule la question) | ⚠️ 3/29 | ⚠️ 1/22 | ⚠️ 2/30 | ⚠️ 1/21 | ⚠️ 2/12 | ⚠️ 1/33 | ⚠️ 2/19 | ⚠️ 1/11 | ⚠️ 0/17 | ⚠️ 2/21 | ⚠️ 0/4 | ⚠️ 5/15 | ⚠️ 0/13 | ⚠️ 2/5 |
| « La somme évolue vers le syndrome clinique » (circuits symptômes → syndrome → examen) | ✅ 1 circuit(s) | ✅ 1 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) | ⚠️ 0 circuit(s) |
| « un signe paraclinique à préciser (type d'examen) » (pathologies avec Gold standard) | ✅ 57/57 | ✅ 45/45 | ✅ 55/55 | ✅ 35/35 | ✅ 78/78 | ✅ 80/80 | ✅ 45/45 | ✅ 17/17 | ✅ 40/40 | ✅ 57/57 | ✅ 32/32 | ✅ 33/33 | ✅ 33/33 | ✅ 24/24 |
| « le ou les diagnostics… par spécialité » (4 paliers TF/F/U/R ; organes avec un piège rare) | ✅ 14/14/15/14 ; R 14/14 | ✅ 8/16/10/11 ; R 10/10 | ✅ 13/17/13/12 ; R 12/12 | ✅ 7/12/9/7 ; R 6/6 | ✅ 17/24/24/13 ; R 13/13 | ✅ 14/34/17/15 ; R 10/10 | ✅ 8/18/13/6 ; R 6/6 | ✅ 3/5/5/4 ; R 4/4 | ✅ 11/16/8/5 ; R 5/5 | ✅ 13/21/12/11 ; R 11/11 | ✅ 7/14/5/6 ; R 6/6 | ✅ 9/10/7/7 ; R 7/7 | ✅ 9/9/8/7 ; R 7/7 | ✅ 5/8/6/5 ; R 5/5 |
| « tout doit être tellement concis » (cases de plus de 45 caractères) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 |
| Sources : mentions « à vérifier » restantes (règle commune « rien de mémoire ») | ⚠️ 4 | ✅ 0 | ✅ 0 | ⚠️ 1 | ✅ 0 | ⚠️ 1 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ⚠️ 1 | ⚠️ 33 | ⚠️ 23 |

## 2. Exigences du moteur (communes à tous les systèmes)

| Phrase du prompt | État | Preuve |
|---|---|---|
| « un être humain ultra 3D réaliste » | ✅ | Moteur three.js, GLTFLoader, matériaux physiques (reseau3d.html) ; vagin sans source 3D libre, vulve exclue par règle. |
| « Le Manequin 3D… peut être retourné » | ⚠️ | reseau3d.html n'écoute que la molette (zoom) : aucune rotation libre à la souris ou au doigt n'est codée. |
| « des traits… Obsidian connectant les composantes… à un cadre ayant le nom du système » ; traits droits en bus (21.11) | ✅ | Traits droits tracés en canvas (lineTo) depuis le nœud Système. |
| « chaque circuit issu d'un syndrome peut être rétracté ou révélé » | ✅ | Boutons « replier » dans reseau3d.html. |
| « chacun a son bouton qui permet de révéler son arborescence » (Anatomie, Physiologie, Sémiologie) | ✅ | Barre #espaces : un bouton par espace. |
| « la page active continue de s'étendre horizontalement » | ✅ | Colonnes horizontales (largeurColonne, ecartColonne dans tetrade.json). |
| Théorie et Pratique, deux onglets ; recherche mode Organe et mode Examen (22.11) | ⚠️ | Aucun onglet Théorie/Pratique ni recherche Organe/Examen dans reseau3d.html : la pratique vit dans arene.html ; l'intégration reste à faire. |

## 3. Écarts

- Circuits symptômes → syndrome → examen → diagnostics : cardio, respi seulement ; les 12 autres systèmes s'arrêtent aux signes et aux pathologies.
- Détail des écarts mesurés : cardio (questions, innervation) ; respi (questions, innervation) ; digestif (syndromes, questions, innervation) ; renal (syndromes, questions, innervation) ; neuro (syndromes, questions) ; endocrino (syndromes, questions) ; hemato (syndromes, questions, innervation) ; infectio (syndromes, questions, innervation) ; orl (syndromes, questions) ; loco (syndromes, questions, innervation) ; derma (syndromes, questions, innervation) ; psyche (syndromes, questions, innervation) ; gyneco (syndromes, questions, innervation) ; pediatrie (syndromes, questions, innervation).
