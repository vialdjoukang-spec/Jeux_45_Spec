# BRIEF — Onglet Biologie du jeu Paraclinique (à coller tel quel dans Claude Code)

> Modèle : **Claude Opus 5.5** pour toute la construction. Contre-audit final d'un échantillon de 10 % des fiches : Opus 5.5 dans une session neuve (ou Fable 5.2 si Vial l'accorde ; il raisonne plus finement mais coûte plusieurs fois plus et n'est pas plus rapide).
> Spécification machine : `projets/2_Jeux_Paraclinique/BRIEF_BIOLOGIE.json` (fait foi en cas de doute).

## 0. Mission
Tu construis l'onglet **Biologie** du jeu Paraclinique, sur la branche **`paraclinique-biologie`** du dépôt `vialdjoukang-spec/Jeux_45_Spec`. Tu ne fusionnes sur `main` qu'après le feu vert de Vial. Tu ne touches pas à l'onglet Imagerie, que cinq agents radiologues complètent en ce moment sur `main`.

## 1. Lire avant toute ligne (dans cet ordre)
1. `projets/2_Jeux_Paraclinique/PROMPT_VIAL.md` : le prompt de Vial, épinglé, et surtout sa section « Biologie ».
2. `organigramme-examen-federal/Claude/_progression/CAHIER_ARCHITECTURE_v2.md` : § 0 (règles), § 5 (biologie médicale), § 5.1 (gabarit de fiche), § 5.2 (passerelles), § 7 (cartographie).
3. Le modèle préconstruit : 101 fiches `organigramme-examen-federal/Claude/_progression/donnees/examens/EX-1-*.json` (toutes audit-ok, voir `audits/BIO_RESUME.md`), plus les captures `captures/bio_fiche_1280.png` et `bio_calculs_1280.png`.
4. L'existant de Jeux_45_Spec :
   - `conception/donnees/paraclinique/biologie/` (prélèvements, analyses) ;
   - `criteres.json`, `calculs.json` ;
   - le constructeur `conception/outils/paraclinique/construire_jeu_paraclinique.py`, lignes 551 à 620 environ (PREL, ANAB, familles) ;
   - la page `conception/prototypes/paraclinique/` (jeu.js, avec ses fonctions rubHtml, ficheFlash, ouvrirFen et terme).

## 2. Chaîne exigée (aucun niveau ajouté, aucun retiré)
**Prélèvement (matrice)** → **Examen** → fiche à 3 temps (Indications · L'examen · Interprétation) → **Diagnostic** → **Traitement avec posologie**.
- Les matrices sont dans cet ordre : sang et buvard ; moelle ; urines ; LCR ; selles ; sérosités et liquide synovial ; respiratoire et ORL ; génital et fœto-maternel ; salive, sueur, calculs et peau.
- Une bascule « par système » réordonne les mêmes fiches.
- La discipline (cytologie-hématologie, hémostase, biochimie, immuno-hormonologie, microbiologie, pharmaco-toxicologie) reste un axe secondaire, montré par une couleur et un filtre.
- L'unité de base est un examen ou une lignée, jamais un « bilan » vague.

## 3. Gabarit de fiche (identique partout)
| Bloc | Contenu |
|---|---|
| En-tête | Le nom exact, les synonymes, les systèmes, le prélèvement et ses conditions (tube, jeûne, horaire, transport), et le bon usage suisse (Liste des analyses OFSP, Smarter Medicine). |
| Temps 1 — Indications | Urgence · diagnostic et étiologie · dépistage et bilan préthérapeutique · suivi · **ne pas demander**. |
| Temps 2 — L'examen | Un paramètre par ligne : la valeur normale avec son unité SI, l'anomalie avec son seuil, le seuil d'alerte. |
| Calculs | La formule, son usage, un exemple résolu et la source, avec un calculateur actif dans la page (calculs.js). |
| Temps 3 — Interprétation | L'anomalie chiffrée → les anomalies associées, présentes ou à rechercher → le syndrome (anamnèse et status) → la confirmation, puis le **diagnostic**. |
| **Traitement** (exigence de Vial, absente des fiches EX-1) | Le but ; les moyens généraux (spécifiques) ; la **posologie** avec dose, voie, rythme et adaptation rénale ou hépatique, ainsi que la mention « vérifier dans l'AIPS (Swissmedic) ». |
| Pièges | « Si… → conséquence » ; un moyen mnémotechnique dès qu'il y a au moins 3 entités. |
| Sources et passerelles | Les sources sont datées, avec la date de lecture. Chaque passerelle donne son type, sa fiche cible et sa raison. |

## 4. Méthode (0 token d'abord, cognition ensuite)
1. **Créer la branche :** `git checkout -b paraclinique-biologie`.
2. **Importer le modèle (script, 0 token).** Écris `conception/outils/paraclinique/importer_ex1.py` : il copie les 101 fiches EX-1 dans `conception/donnees/paraclinique/biologie/fiches/`, sans réécrire leur contenu. Il ajoute `_origine` (dépôt, chemin, commit) et range chaque fiche par matrice, d'après `entree_primaire`.
3. **Cartographier les trous (script).** Le même script liste, pour chaque fiche :
   - les blocs vides ;
   - l'absence du bloc Traitement ;
   - les analyses de `biologie/analyses/*.json` qui n'ont pas encore de fiche.
   Il écrit tout cela dans `projets/2_Jeux_Paraclinique/FILE_BIOLOGIE.json`, avec un statut à faire, en cours ou fait par fiche.
4. **Construire le rendu.** Le constructeur lit `biologie/fiches/` et produit la chaîne de § 2. Chaque fiche s'ouvre dans la fenêtre centrée avec ses rubriques au survol. Les calculateurs de `calculs.json` et `criteres.json` (Kass, ascite, liquide synovial, etc.) s'ouvrent au clic.
5. **Remplir.** Lance 4 agents au plus, chacun sur un lot de matrices exclusif. Ils ajoutent le bloc Traitement et posologie, puis les fiches manquantes. Chaque fait vient d'une source lue : AIPS (compendium.ch), HUG, CHUV, sociétés suisses, puis ESC, EASL, KDIGO, IDSA, puis PubMed (MCP). Sans source lue, écris « à vérifier » et dis où vérifier.
6. **Auditer.** L'audit mécanique doit être vert sur toutes les fiches (voir le § 5). Fais ensuite le contre-audit médical d'un échantillon de 10 % par une session neuve.
7. **Prouver.** Fais une capture Playwright à 1280 et à 380 px pour une fiche par matrice, avec 0 erreur dans la console. Committe les captures dans `projets/2_Jeux_Paraclinique/captures/biologie/`.
8. **Livrer.** Ouvre une PR de `paraclinique-biologie` vers `main`. Écris dans sa description :
   - le tableau de conformité, phrase du prompt par phrase du prompt ;
   - les captures ;
   - ce qui reste « à vérifier ».
   Tu ne fusionnes pas sans le feu vert de Vial.

## 5. Audit mécanique (bloquant, `auditer_biologie.py`)
- Chaque fiche contient les 8 blocs du § 3, et un bloc absent porte « à produire ».
- Chaque valeur chiffrée (normale, seuil, alerte, dose) porte une source.
- Chaque posologie se termine par le renvoi à l'AIPS.
- Les unités sont SI suisses (mmol/l, µmol/l, g/l, kPa).
- Aucune phrase nominale dans les rubriques : le contrôle cherche un verbe conjugué.
- Aucun identifiant n'est dupliqué, et chaque passerelle pointe vers une fiche qui existe.
- `non_perte` : aucune valeur remplie ne disparaît d'une génération à l'autre.

## 6. Règles de Vial (non négociables)
- Les phrases sont entièrement verbales, avec le tutoiement de l'apprenant et le contexte suisse.
- Le texte est en Atkinson Hyperlegible, d'environ 15 px, sur un fond clair. Une seule fenêtre est ouverte à la fois. Le détail va dans l'infobulle et le développement dans une fenêtre.
- Les couleurs ont un sens fixe : bleu pour le normal, rouge pour la pathologie, vert pour le traitement.
- Les sigles sont développés dans le libellé et expliqués au survol. Jamais de SVG pour une image.
- Rien n'est écrit de mémoire. Aucun contenu QCM n'est montré. Aucun contenu médical non audité n'arrive sur `main`.
- Jamais de push forcé, et jamais de contournement d'un refus de permission.
- Les commits sont en français, un par lot, et se terminent par les lignes d'attribution de la session.

## 7. Rapport final à l'orchestrateur
1. Le nombre de fiches importées, complétées et créées.
2. L'audit mécanique, avec le nombre de fiches vertes sur le total.
3. L'échantillon contre-audité et les corrections faites.
4. Ce qui reste « à vérifier », avec l'endroit où le vérifier.
5. Le lien de la PR et les captures.
6. Les skills chargés : au moins skills-are-oxygen-vital, medical-accuracy-100, switzerland-medical-professor, ultra-competent-fast-doctor, all-context-ultrasystematic, web-designer-pilot-faithful, obsidian-like-complex-network, optimisation-par-cache-hache-autorun, always-twice-check-before-delivery.

Signature : AAI (Anthropic AI)
