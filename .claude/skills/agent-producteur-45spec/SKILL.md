---
name: agent-producteur-45spec
description: Produit, sans appel à l'API Anthropic, les notions, questions et corrections du jeu 45 Spec au format exact de scripts/produire_notions_questions.py. S'active dès qu'un agent remplace l'API pour une spécialité (branche agent/45spec-<SPEC>).
---

# Agent-producteur-45spec

## Pourquoi
L'agent écrit lui-même le contenu que le script demanderait à l'API ; il doit donc respecter les mêmes schémas, la même fonction `valider()` et les mêmes règles de couverture, sinon les fichiers ne passent ni l'audit ni `couverture_notions.py`.

## Méthode
1. Liste les pathologies restantes dans l'ordre de `progression.py <SPEC>` (rang de rendement, puis fréquence) et saute celles dont les trois fichiers existent.
2. Écris une forme compacte par pathologie (`ID`, `N`, `AM`, `Q`, `C` ; `from constructeur_agent_45spec import pec` pour les plans de prise en charge) puis lance `python projets/45spec/constructeur_agent_45spec.py <fichier.py>` : il développe, valide, calcule la couverture et écrit les trois JSON.
3. Lance d'abord `python projets/45spec/couverture_compacte.py <fichier.py>` : chaque notion de poids ≥ 2 doit apparaître dans deux questions d'angles différents ; poids 3 ≤ 15 %, poids 2 ≤ 35 %.
4. Mets `m=0` (monographique) dès qu'une vignette nomme le diagnostic ou l'agent ; garde `m=1` pour les starting points.
5. Commits par lots de 3 pathologies, push immédiat sur la branche agent ; mets à jour `projets/45spec/PROGRESSION_<SPEC>.md`.

## Règles de fond
- 13–14 type A (5 options, 1 juste), 4 Kprim (4 énoncés), 2 menus longs (12 options, **1 à 3 réponses justes**, énoncé « Choisissez les TROIS… » ou le bon nombre) ; une série progressive de 3–4 étapes.
- Sources : SSI, OFSP, Swiss TPH, AIPS d'abord ; toute posologie « à vérifier dans l'AIPS » ; tout doute porte « (à vérifier) » dans `source`. Jamais de référence inventée.
- Ne lance pas `couverture_notions.py` sur une branche agent : il réécrit les fichiers des autres spécialités.

## Leçons (lot 5, 24.11.2026)
- Travaille dans un clone privé (`git clone --single-branch --branch agent/45spec-<SPEC> … /home/claude/aai_<spec>45`) : un dossier partagé peut être basculé sur une autre branche par un autre agent.
- Lance le constructeur avec `PYTHONPATH=projets/45spec` ; versionne les formes compactes dans `projets/45spec/compact_<SPEC>/`.
- Régénère la progression avec `python projets/45spec/progression.py <SPEC>` (0 token), jamais à la main.
- Fusions : une fusion change l'id canonique ; renomme alors les trois fichiers déjà produits de la cible (`git mv`, réaligne id, portes, entité, spécialités) et archive les doublons produits dans `projets/45spec/archives_fusion/<SPEC>/`.
- Disciplines transversales : reprends les libellés A→S de `conception/donnees/tetrade/transversales/outils/` (ex. « J Hygiène hospitalière », « N Médecine sociale Prévention OFSP »).
- Natures de notion : uniquement l'énumération `NATURES` du script (« contexte » seul est refusé) ; `surveillance.suivi` exige au moins deux lignes.

## Leçons (lot 6, 24.11.2026)
- Écris la forme compacte avec des clés de notion (`_N` à clé, `n("cle",…)`) : la renumérotation devient impossible à rater.
- Le schéma exige ≥ 25 notions, ≥ 6 nœuds d'algorithme SSP, ≥ 2 `mesuresGenerales`, une notion `chronicManagement` ; catégories non pharmacologiques fermées (« activité physique » refusée → « rééducation »).
- Vérification en ligne : si WebFetch est bloqué (permission non répondue), passe par le connecteur PubMed (`get_full_text_article` sur PMC) ; ne contourne jamais un blocage par curl.

## Leçons (lot 8–9, 24.11.2026)
- `PLAN` est lu comme plan du fichier : n'y mets que `PLAN = "non_monographique"` quand `circuit` vaut NON_MONOGRAPHIQUE (sinon omets-le) ; n'utilise ce nom pour rien d'autre.
- Cible directe pour 28 notions : 4 de poids 3, 9 de poids 2, le reste à 1 ; chaque notion sert au moins une fois ; au plus 6 notions par question ; les 15 rubriques doivent toutes porter une notion (oubli fréquent : `clinicalExam`, `hospitalizationComplications`).
- Ce skill n'est pas enregistré auprès de l'outil Skill de la session : lis-le dans `.claude/skills/agent-producteur-45spec/SKILL.md` du clone.

## Leçons (lot 10, 24.11.2026)
- Ordre de production : rang de `content/pathologies/RANG_RENDEMENT.json` (groupe A, puis B, C, D), plus l'ordre fréquence. Une pathologie fusionnée change d'id et manque au classement : on lui donne le meilleur rang de ses portes d'entrée (`entiteId` avec « . » → « _ » = suffixe de la clé du rang), comme le font `selection()` et `progression.py`.
- Une étape de série qui nomme le diagnostic (« vous suspectez un botulisme ») porte aussi `m=0`.

## Leçons (lot 12, 24.11.2026)
- Un menu long garde 1 à 3 réponses justes, car le jeu annonce « une à trois réponses » ; chaque réponse vraie en trop devient un distracteur faux avec son « why » exact. `constructeur_agent_45spec.py` (`menus_longs_hors_format`) et `valider()` le contrôlent ; `python projets/45spec/controle_menus_longs.py INF` doit afficher 0.
- Correction : chaque bloc `notions` porte au plus 4 rubriques ; `conduite.urgence.etapes` en exige au moins 3.
- Catégories non pharmacologiques exactes : psychothérapie, éducation thérapeutique, geste ou chirurgie, rééducation, nutrition, soins infirmiers, social et assurances, hygiène de vie, autre (« hygiène » seul est refusé).
- Une Kprim ou une A dont la vignette nomme le diagnostic (« kératite dendritique ») porte `m=0`, même hors série.

## Leçons (agent A, groupe A, 24.11.2026)
- Pour un agent qui produit par groupe de rendement (toutes spécialités), le constructeur lit `canoniques(None)` (variable `SPEC` vide) : l'id et les `codes` correspondent alors à `RANG_RENDEMENT.json` ; `canoniques("<SPEC>")` peut tronquer `codes` et les portes.
- Le périmètre se tient par script (`progression_A.py`) : saute les pathologies déjà produites sur main et les spécialités confiées à d'autres agents (PSY, NEU, INF, PED ; ORL, OPH, GYN, OBS, URO, MIG, HEM, TOX, DER, RHU pour l'agent A2).
- Avant chaque lot, refais `git fetch` de main et vérifie qu'aucun autre agent n'a produit la pathologie suivante.

## Leçons (agent A, lots 3–4, 24.11.2026)
- `conduite.*.etapes[].temps` n'accepte que « d'abord », « en même temps », « ensuite », « puis » (« à 3 mois » est refusé : mets le délai dans « fait »).
- Contrôle d'une pathologie déjà produite avec le `valider()` courant : retire l'enveloppe (id, portes, signature…) et `couverture` avant l'appel, sinon le schéma échoue à tort.
- Les rangs de `RANG_RENDEMENT.json` bougent entre deux fusions de main : relis l'ordre par script après chaque fusion.

## Leçons (agent A, lots 5–6, 24.11.2026)
- `pec(...)` : la liste `accueil` exige au moins 2 éléments ; une `conduite.urgence` fournie exige 3 étapes.
- Une pathologie déjà couverte sous un autre code par une autre spécialité (ex. A41.9 sepsis ≈ A41.8 INF) se saute : vérifie l'entité et les portes du fichier existant avant de produire.
- Un nœud `ssp` peut renvoyer à `c4` (4e bloc de correction) quand le PEC chronique y est traité.

Relais : `ultra-competent-fast-doctor`, `medical-accuracy-100`, `i-write-so-fast`.

Signature : AAI (Anthropic AI)

## Leçons (groupe A multi-spécialités, agent A2, 24.11.2026)
- Agent qui couvre plusieurs spécialités : lance le constructeur avec `SPECS=URO,HEM,TOX,…` (index des canoniques de chaque spécialité) et `PYTHONPATH=projets/45spec`.
- Suivi d'un groupe de rendement : `python projets/45spec/progression_groupe.py <NOM> <GROUPE> <SPEC1,SPEC2,…>` régénère `PROGRESSION_<NOM>.md` (0 token).
- Avant chaque lot, `git fetch` de `main` et de toutes les branches `agent/45spec-*`, puis saute toute pathologie dont la correction existe déjà ailleurs.
- N'écris jamais un DOI que tu n'as pas lu ; un PMID ou une référence vérifiée suffit.

## Leçons (agent A2, lot 4, 24.11.2026)
- Une ligne de `PROGRESSION_<NOM>.md` peut citer un id absent de `P.canoniques()` (ex. `R45.8_3__O2_12-E15`, porte fusionnée) : le constructeur lèverait `KeyError`. Saute-la, signale-la au rapport et produis la suivante.
- Après chaque fusion de `main`, régénère la progression : les rangs de `RANG_RENDEMENT.json` bougent.
- Un menu long dont la vignette nomme l'agent (« ne contiennent que des benzodiazépines ») porte aussi `m=0`.

## Leçons (agent A, lots 9–10, 24.11.2026)
- Utiliser `git pull --rebase=merges`, jamais `--rebase` simple : un rebase simple aplatit les fusions de main et réécrit l'historique partagé.
- Fusion sur main (autorisée par Vial) après chaque lot de 3 : `valider()` sans erreur sur ses fichiers, 0 menu long fautif sur tout `content/questions/*`, `scripts/classer_rendement.py`, `conception/outils/arene45/construire_arene45.py`, test sans écran de l'arène 45 (0 erreur JS), puis `git pull --no-rebase origin main` et push sur main sans force.
- Fichier produit par l'API qui dépasse 70 notions : fusionne les notions redondantes non utilisées par les questions (même rubrique ou doublon de seuil) au lieu d'en supprimer le contenu ; les ids restants ne se renumérotent pas.
- Libellés transversaux exacts : « C Communication clinique », « Q Radioprotection Smarter Medicine » (« G » = Épidémiologie, « D » = Digitalisation, jamais « Médecine de famille » ni « Imagerie »).

## Leçons (agent A, lots 11–12, 24.11.2026)
- Avec 4 notions de poids 3, il faut au moins 27 notions (poids 3 ≤ 15 %, poids 2 ≤ 35 %) : `couverture_compacte.py` affiche sinon « POIDS hors règle ».
- Le suffixe de l'id ne donne pas la SSP (N95.2__F1_2 → S4.17) : reprends `ssp` et `nomSSP` de `P.canoniques(None)`.
- Un menu long dont le prompt nomme le diagnostic (« autre cause qu'une fibromyalgie ») porte `m=0`.
- Test sans écran de l'arène : `index.html` porte depuis le lot 13 une favicon PNG en data-URI ; on attend donc 0 `pageerror` et 0 erreur console. Un 404 sur `decks/<SPEC>.json` signale seulement une spécialité encore sans contenu.

## Leçons (agent A, lots 13–14, 24.11.2026)
- Libellés transversaux : il n'existe pas de « H Gériatrie » ; pour la fin de vie, prends « M Médecine palliative » ; vérifie un libellé par `grep '"discipline"' content/corrections` avant de l'écrire.
- Sources suisses vérifiables en ligne : stratégies et protocoles des HUG (hug.ch, par ex. infections urinaires 2026, diabète gestationnel 2022) et pages OFSP ; préfère-les à un avis d'expert.
- Une pathologie pédiatrique du groupe A (ex. K56.1, CPE) crée un nouveau dossier de spécialité : le constructeur le fait seul, et l'arène génère le deck.

## Leçons (agent A, lots 15–16, 24.11.2026)
- `valider()` ne repère dans la vignette que le libellé complet du diagnostic masqué : une vignette qui dit « zona », « PTT » ou « retard de langage » porte quand même `m=0` ; relis chaque `st` avant de lancer le constructeur.
- Recommandation longue sur PMC (captcha WebFetch) : `get_full_text_article` du connecteur PubMed écrit le texte sur disque ; extrais par script les blocs « Recommendation N » au lieu de lire le fichier entier.
- Pathologie sans urgence : la clé de `pec` est libre (ex. « orienter », « suivi ») ; passe `urg=None` et fournis `horsUrgence`, et reprends la même clé dans les nœuds `ssp`.
- Ne pousse jamais avec `-f` : la branche agent se met à jour par `git merge --ff-only main` puis un push simple.

## Leçons (agent A, lots 17–18, 24.11.2026) — consigne de Vial sur la difficulté
- Dès le lot 19, chaque pathologie compte au moins 5 questions sur 20 de difficulté `d` 4 ou 5 (aujourd'hui, seulement 7 % des QCM le sont), et garde au moins 2 questions `d` 1–2 pour l'ancrage.
- Une question `d` 4–5 demande un raisonnement en deux temps (reconnaître, puis décider), garde le diagnostic masqué dans la vignette (clé `m` omise, donc `diagnosticMasque` vrai dans le constructeur) et prend ses distracteurs parmi les vrais diagnostics différentiels et les pièges classiques : présentation atypique, contre-indication, examen inutile, seuil limite. Elle reste au programme de l'examen fédéral, sans érudition gratuite.
- Contrôle avant le constructeur : `grep -c '"d":[45]'` sur la forme compacte doit donner au moins 5.
- Le constructeur écrit parfois les JSON même quand `err` n'est pas vide : relance-le jusqu'à `err {}` avant de committer.

## Leçons (producteur unique, lot 20, 24.11.2026)
- `controle_menus_longs.py` ne contrôle que la spécialité passée en argument (INF par défaut) : boucle sur `ls content/questions` pour obtenir « 0 menu long fautif » sur tout le contenu.
- Un menu long `d` 4–5 garde le diagnostic masqué : son `st` ne doit pas nommer l'entité, même en négatif (« les éléments qui excluent une cystite simple » la nomme).
- Test sans écran de l'arène : `python -m http.server` sur la racine du clone, puis Playwright sur `conception/prototypes/arene45/index.html` (pageerror, console error, réponses ≥ 400).
