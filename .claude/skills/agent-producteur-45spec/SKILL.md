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

## Leçons (producteur unique, lots 23–24, 24.11.2026)
- `couverture_compacte.py` n'affiche rien quand tout est conforme ; seul le constructeur affiche le bilan (`err {}`).
- Le schéma refuse un `pourquoi` de `pec` trop court (« Ils protègent l'os. ») : écris une phrase complète d'au moins une dizaine de mots.
- Question `d` 4–5 sur une intoxication : ne nomme pas l'agent dans le `st` (« traitée par un thymorégulateur », « comprimés prescrits par son psychiatre ») ; si l'agent doit être nommé, mets `m=0` et une difficulté ≤ 3.
- Un nom canonique peut doubler un fichier existant (S27.0 « pneumothorax compressif » ≈ CTH J93.0) alors que ses portes visent une autre entité (pneumothorax traumatique simple) : produis-la sous l'angle de la porte non couverte au lieu de la sauter, et signale-le au rapport.
- Une vignette `d` 4–5 ne paraphrase pas non plus le libellé entre parenthèses du nom canonique (« thrombose des veines sus-hépatiques » pour Budd-Chiari) : décris les constatations, pas l'entité.
- Vérifie toujours l'année de la recommandation par PubMed : une version plus récente peut exister (EASL maladies vasculaires du foie 2016 → 2025, PMID 41224629).

## Leçons (producteur unique, lots 26–27, 24.11.2026)
- Une question A `d` 4–5 garde aussi son `p` (prompt) sans le diagnostic : « en cas d'annexe tordue » ou « origine médicamenteuse avec nécrose de l'épiderme » le révèlent ; écris « votre hypothèse principale ».
- Une étape de série vue au bloc (« annexe tordue sur trois tours ») nomme le diagnostic : `m=0` et `d` ≤ 3.
- `couverture_compacte.py` affiche « Nxx p1 [] » quand une notion de poids 1 ne sert à aucune question : rattache-la à une question proche avant le constructeur.
- Entité voisine déjà produite (S27.1 → J94.2, O00.1 → O00.9) : prends l'angle de la porte non couverte (iatrogène et réanimation hémostatique ; GEU non rompue, méthotrexate, échec contraceptif).

## Leçons (producteur unique, lot 29, 24.11.2026)
- Test sans écran de l'arène (autorisé par Vial le 24.11, « Test et fusionne ») : lance-le en premier plan avec `python3 /home/claude/outils/test_arene.py <racine du clone>` ; le script sert la racine dans son propre processus, ouvre l'arène dans Playwright et doit afficher « erreurs: 0 ». Aucun serveur en arrière-plan ; si le test est refusé, ne le contourne pas : pousse le lot sur `agent/45spec-A-lotNN` et signale-le.
- Porte « nourrisson » d'une pathologie adulte (T67.0, O2.8) : place-la dans une question A sans nommer le diagnostic, en gardant `d` 3.
- Entité voisine déjà produite (A54.0 gonocoque ↔ A56.0 chlamydia) : prends l'angle propre au germe (Gram, culture avant traitement, résistance, contrôle de guérison, déclaration clinique OFSP).

## Leçons (producteur unique, lot 30, 24.11.2026)
- Libellé transversal des urgences : « S Urgences vitales Triage 144 REGA » ; « I » désigne la génétique médicale, jamais les soins intensifs.
- Une vignette `d` 4–5 ne doit pas trahir le diagnostic par un adjectif d'antécédent (« utérus polymyomateux connu ») : écris « plusieurs masses bénignes connues ».
- Porte d'entrée « kyste synovial » ou « hernie » d'une pathologie bénigne de la peau : place-la en distracteur ou en question de diagnostic différentiel, sans nommer l'entité dans le `st`.

## Leçons (producteur unique, vérification du lot 31, 24.11.2026)
- Ne cite jamais une notice que tu n'as pas ouverte : ouvre la notice PubMed (`get_article_metadata`) puis le texte (PMC, ou le PDF officiel trouvé par WebSearch) avant d'écrire chaque seuil ; quand PMC ne livre pas le texte (`full_text` vide), passe par WebFetch sur la page PMC ou le PDF de la société savante.
- Une revue citée ne couvre que ce qu'elle dit : Weiss 2019 recommande le fer oral en cas d'inflammation légère et le fer IV après 2 semaines d'échec, pas « le fer IV si l'inflammation est active » ; cette indication relève d'une autre source (ECCO 2015 pour les MICI actives).
- Une recommandation peut avoir été remplacée : KDIGO anémie 2012 → KDIGO 2026 (document officiel sur kdigo.org, résumé PMID 41485807) ; cite le document officiel et vérifie les écarts internes (bilan martial en hémodialyse : 1 à 3 mois dans le texte, chaque mois dans la figure).
- Contrôles avant fusion en une commande : un script local (menus longs sur toutes les spécialités, `classer_rendement.py`, arène sous `cache_hache.py`, `test_arene.py`) évite les oublis ; `.cache_hache.json` reste dans `.gitignore`.

## Leçons (producteur unique, lots 32–33, 24.11.2026)
- Une forme compacte laissée non suivie par un producteur arrêté (ex. `a94_D69_2.py`) se reprend, mais on rouvre chaque notice citée : un abstract qui ne contient pas l'affirmation (siège des lésions, émollients) oblige à changer de source (DermNet, page officielle) ou à écrire « Expert ».
- Un PMID tiré de mémoire peut pointer vers un autre article (Sanders 2010 → lettre sur la mort subite du nourrisson) : vérifie le titre renvoyé par `get_article_metadata` avant de l'écrire.
- Sources suisses ouvrables en ligne : OFSP 2012 « Carence en vitamine D » (edi.admin.ch), OSAV apports vitamine D (blv.admin.ch), OFSP « Faits et chiffres : tabac » (bag.admin.ch) ; NICE CG158 se lit sur nice.org.uk (WebFetch).
- eutils.ncbi.nlm.nih.gov est refusé par le proxy : passe par le connecteur PubMed, sans contourner.
- `couverture_compacte.py` signale aussi une notice de poids 2–3 couverte deux fois sous le même angle : ajoute-la à une question d'un autre angle (piège ou application) plutôt que de changer l'angle d'une question juste.

## Leçons (producteur unique, lots 34–36, 24.11.2026)
- `pec(...)` accepte une liste pharmacologique vide `[]` pour une pathologie sans médicament utile (VPPB, presbyacousie, dysphonie) : n'invente pas de molécule pour remplir le champ.
- Sources lisibles par WebFetch : recommandations NICE (`nice.org.uk/guidance/ngXX/chapter/recommendations`), PDF AAO repéré par WebSearch, résumés AFP (« Rapid Evidence Review », « Practice Guidelines ») qui reprennent les recommandations AAP ou ACC/AHA ; cite alors l'AFP comme résumé, avec la recommandation d'origine.
- Sources suisses lisibles : LiMA chapitre 25 (OFSP, modifications au 01.07.2024), mémento AVS 3.07 appareils auditifs (ahv-iv.ch), SSML/SSO facultés visuelles et OAC (sgrm.ch), stratégie HUG « fièvre au retour de voyage », formulaire OFSP de déclaration du paludisme, portail PME (kmu.admin.ch) pour l'absence d'un parent d'enfant malade.
- Le site escardio.org refuse WebFetch (robots) et PMC renvoie parfois un captcha : passe par `get_full_text_article` (commentaire PMC d'une recommandation) ou par un résumé ACC ou AFP, sans contourner.
- Deux versions d'une même liste peuvent diverger (JMF 2003 : 8 otites ; JMF 2024 : 4 otites) : cite la version la plus récente lue.
- Une pathologie NON_MONOGRAPHIQUE garde des vignettes `d` 4–5 masquées ; nommer une autre maladie (paludisme chez un voyageur) ne démasque pas l'entité canonique.

## Leçons (producteur unique, vérification ESC 2024 de I73.9, 24.11.2026)
- Une recommandation se cite d'après son propre texte, jamais d'après un commentaire, un résumé ACC ou AFP : I73.9 citait l'ESC 2024 d'après un commentaire, avec des classes et des niveaux non relus et un « 25 % » d'IPS normal absent du texte.
- L'ESC 2024 (PMID 39210722) se lit par WebFetch sur academic.oup.com (`/eurheartj/article/45/36/3538/7738955`, 857 000 caractères, pages par `offset` de 100 000 ; le texte PAD tient entre 100 000 et 200 000) ; les tableaux de recommandations n'y apparaissent pas en texte : n'écris donc ni classe ni niveau que tu n'as pas lus.
- Un « risque élevé d'amputation » ne vaut pas pour la claudication (ESC 2024 : 1 % d'amputations majeures contre 9 % dans l'ischémie menaçante).

## Leçons (producteur unique, lot 37, 24.11.2026)
- Sources ORL lisibles : stratégie HUG « IVRS » 2021 (PDF hug.ch par WebFetch : durée, signes d'alarme, critères de sinusite bactérienne, Centor, doses d'antalgiques) ; résumé PubMed des recommandations AAO-HNSF (rhinite allergique 2015, amygdalectomie 2019) et AAP (SAOS de l'enfant 2012), dont les « action statements » figurent en entier ; résumé exécutif EPOS 2020 par WebFetch sur scispace.com.
- Un PMID tiré de mémoire pour un consensus AAO-HNSF (septoplastie) pointait vers un article d'anthropologie : n'utilise que les PMID renvoyés par `search_articles`.
- Une porte d'entrée nommée par un symptôme qui reprend le libellé (« nez bouché » pour l'obstruction nasale chronique) reste acceptable dans une vignette `d` 4–5 si la question porte sur une autre décision (rhinite médicamenteuse, alarme unilatérale).

## Leçons (producteur unique, lot 38, 24.11.2026)
- Deux canoniques voisins (K40.9_1 hernie inguinale de l'homme, K40.9 hernie inguinale ou ombilicale) : le second prend l'angle de ses portes non couvertes (hernie fémorale de la femme, hernie ombilicale, diastase, Spiegel, cirrhose, grossesse, dialyse).
- Sources de paroi lisibles en texte intégral par `get_full_text_article` : HerniaSurge 2018 (PMC5809582, « Summary for general practitioners » à extraire par script), mise à jour 2023 (PMC10588975, tableaux « Recommendation » en texte), EHS/AHS 2020 circonstances particulières (PMC7093793) ; NICE CG49 se lit sur `nice.org.uk/guidance/cg49/chapter/Recommendations`.
- Après un redémarrage du serveur, vérifie `git status` et `git log origin/main` : les JSON déjà construits mais non suivis se gardent, il suffit de relancer les contrôles avant le commit.

## Leçons (producteur unique, lot 39, 24.11.2026)
- Chemins NICE sensibles à la casse : NG12 se lit sur `.../ng12/chapter/recommendations-organised-by-site-of-cancer` (minuscules), CG153 sur `.../cg153/chapter/Recommendations` (R majuscule) ; si une variante renvoie une erreur ou une page tronquée, essaie l'autre.
- Sources lisibles : ESCP 2020 hémorroïdes (manuscrit accepté sur scispace.com, recommandations 1.1–5.9), DermNet (`/topics/morbilliform-drug-reaction`, `/topics/chronic-plaque-psoriasis`), Swissmedic « Pharmacovigilance » (déclaration ElViS), communiqué de la Ligue contre le cancer du 12.06.2025 (dépistage colorectal remboursé de 50 à 74 ans).
- Le dépistage colorectal suisse va désormais jusqu'à 74 ans (OPAS, 1er juillet 2025) : ne recopie plus « 50–69 ans ».
- Entité voisine déjà produite (K64.9 grades et thrombose) : K64.8 prend l'angle de la rectorragie (FIT, seuil de 10 µg/g, anémie ferriprive, anticoagulants, varices rectales).
- Un « éruption maculopapuleuse » dans la vignette paraphrase « exanthème maculopapuleux » : décris les lésions (« petites taches rosées, un peu surélevées »).
- `controle_menus_longs.py <SPEC>` affiche « menus longs fautifs : 0 | erreurs valider() : 0 » : filtre cette chaîne pour ne voir que les spécialités fautives.

## Leçons (producteur unique, lot 40, 24.11.2026)
- La casse des chemins NICE varie d'une recommandation à l'autre : NG198 répond en minuscules (`/chapter/recommendations`), NG100 et CG153 avec une majuscule ; essaie les deux avant de conclure à un blocage.
- SOSORT 2016 (scoliose, PMID 29435499) se lit en texte intégral par `get_full_text_article` (PMC5795289) ; extrais par motif (Adams, scoliomètre, IRM, rapport filles-garçons) au lieu de lire 185 000 caractères.
- Une vignette `d` 4–5 sur un effet du méthotrexate ne cite pas l'indication par son nom (« pour une polyarthrite ») quand la pathologie canonique est la polyarthrite : écris « pour une maladie articulaire ».
- Pathologie NON_MONOGRAPHIQUE sans médicament (M41.1) : `PLAN = "non_monographique"` et liste pharmacologique vide `[]` passent `valider()`.

## Leçons (producteur unique, lot 41, 24.11.2026)
- Sources lisibles par WebFetch : NICE NG118 (lithiase) et NG123 (incontinence de la femme) sur `/chapter/Recommendations` ; EAU Urolithiasis 2026 en version de poche (PDF cloudfront lié depuis uroweb.org ; les chapitres HTML répondent « Not found ») ; SVGO 2020 sur `smw.ch/article/doi/smw.2020.20352` ; RCP ANSM d'une molécule (posologie, mode de prise, contre-indications) quand l'AIPS suisse ne s'ouvre pas, avec « version suisse à vérifier dans l'AIPS ».
- Fedlex (OPAS) ne s'affiche pas sans JavaScript : un remboursement LAMal non lu (DXA, nombre de séances de physiothérapie) s'écrit « à vérifier dans l'OPAS ».
- Une page WebFetch peut tronquer une liste (NICE 1.5.2) : n'écris pas les options manquantes, cite seulement celles lues.
- Contrôle du masquage en 0 token : un petit script qui charge la forme compacte et cherche les mots interdits dans `st` et `p` des questions sans `m` (et compte les `d` 4–5 masqués) évite une relecture manuelle.
- Les decks de l'arène (`conception/prototypes/arene45/decks/<SPEC>.json`, `decks/<SPEC>/<id>.json`, `specs.json`) sont suivis par git : ajoute `conception` au commit, sinon `git pull --rebase` refuse de tourner.
- Deux canoniques voisins de la même entité (N40.0 HBP au toucher rectal, N40 HBP décompensée) se répartissent par porte : symptômes, toucher rectal et traitement médical pour le premier ; rétention aiguë, hématurie, indications et choix chirurgicaux pour le second.

## Leçons (producteur unique, reprise du lot 43, 25.11.2026)
- Un lot laissé non suivi peut différer de la consigne de reprise (annoncé M81.0, trouvé N84.0, N94.3, N94.4) : fie-toi à `git status` et à `git log`, pas au message.
- RCOG Green-top 48 (SPM, PMID 27900828, sans résumé ni PMC) se lit en PDF complet par WebFetch (copie repérée par WebSearch) : recommandations et grades lisibles, algorithme compris (ISRS à faible dose, estradiol 100 µg + progestatif, GnRH en 3e ligne).
- Vue de relecture en 0 token : un script qui imprime `st`, `p`, `d`, `m` et les options vraies de chaque question (filtrer « — Faux. ») suffit pour auditer un lot hérité.

## Leçons (producteur unique, lot 44, 25.11.2026)
- Sources lisibles : NICE NG23 (ménopause) sur `/chapter/recommendations` en minuscules (la majuscule renvoie une erreur) ; brochure HUG « traitement hormonal de la ménopause » 2019 (PDF hug.ch) ; avis d'experts SSGO n° 78 « IG médicamenteuse » 2022 (PDF vd.ch, posologies et suivi) ; page HUG « Lois et délais légaux des IVG » (12 SA, moins de 16 ans).
- La bibliothèque NCBI (Bookshelf) et l'IRIS de l'OMS renvoient un captcha ou une page HTML : passe par une source suisse équivalente plutôt que par une recommandation OMS non lue.
- WebFetch refuse une URL jamais vue (provenance) : fais d'abord un WebSearch qui la renvoie.
- Discordance à signaler dans la notion : NAMS 2023 ne recommande ni plantes ni soja, NICE NG23 admet que les isoflavones peuvent aider avec une sécurité incertaine.
- Sujet d'une demande (IVG) : les vignettes `d` 4–5 masquées disent « grossesse non prévue » et « comprimés prescrits », jamais le geste ni les molécules.

## Leçons (producteur unique, lot 45, 25.11.2026)
- Sources lisibles : RCOG Green-top 69 (2024) en PDF complet sur rightdecisions.scot.nhs.uk (WebFetch, 134 000 caractères ; l'annexe des doses manque) ; CMAJ 2021 « Carence en fer et anémie ferriprive durant la grossesse » en français (PMC8568089) ; Mohr 2022, cohorte bernoise de rétention urinaire du post-partum (PMC9206615, définitions et protocole) ; Cochrane 2020 sur les tranchées (résumé, PMID 33078388).
- La recommandation BSH 2020 (fer et grossesse, PMID 31578718) n'a ni résumé ni PMC, et le dépôt QMUL est bloqué : ne la cite pas, prends une source lue (CMAJ 2021).
- Une forme compacte peut assigner `src` en boucle (`for _q in Q: _q["src"] = X`) puis corriger quelques questions : plus sûr qu'une liste `_SRC` de 20 éléments mal alignée.
- Un menu long sur des facteurs de risque doit exclure des distracteurs les autres facteurs connus (primiparité, travail long, césarienne) : sinon il gagne une réponse juste de trop.

## Leçons (producteur unique, lot 46, 25.11.2026)
- ESC 2019 tachycardies supraventriculaires (PMID 31504425, sans PMC) se lit en PDF complet sur le dépôt de l'Université de Berne (boris.unibe.ch, repéré par WebSearch) ; la section « tachycardie sinusale » (tableau des causes, TSI, POTS, réentrée sinusale) se trouve entre les offsets 100 000 et 200 000.
- MASCC/ESMO 2023 antiémétiques : les volets « haut risque » (PMC10739516) et « plusieurs jours, haute dose et percée » (PMC10725845) se lisent en entier par `get_full_text_article` ; les volets « risque modéré » et « non pharmacologique » n'ont qu'un résumé lisible : cite-les comme « résumé lu ».
- AFP 2016 sur les adénopathies a une mise à jour AFP 2025 (Falk et al.) : lis les deux ; seule la version 2016 décrit l'aine (jusqu'à 2 cm chez l'adulte sain, lymphomes rarement inguinaux).
- Pages CDC 2021 des IST (`cdc.gov/std/treatment-guidelines/lgv.htm`, `p-and-s-syphilis.htm`) se lisent par WebFetch après un WebSearch ; elles donnent schémas, partenaires et suivi sérologique.
- Une pathologie NON_MONOGRAPHIQUE de soins de support (R11.2) garde des vignettes `d` 4–5 masquées en prenant pour réponse une autre cause (métastase cérébrale, constipation, hypercalcémie) : c'est le piège classique de l'examen.
- Natures : « contexte suisse » exige `suisse=1` ; pour une notion non suisse, prends « terrain particulier ».

## Leçons (producteur unique, lot 47, 25.11.2026)
- Sources lisibles : consensus d'Amsterdam 2022 sur la commotion (BJSM, sans PMC) en PDF complet sur un site public repéré par WebSearch ; guide SIRA 2014 du coup du lapin (PDF sira.nsw.gov.au : grades QTF, recommandations gradées, seuils NDI, IES > 25) ; résumés des règles canadiennes du scanner cérébral (PMID 11356436) et du rachis cervical (PMID 11597285) ; résumé AAO-HNSF 2017 de la masse cervicale (PMID 28891406), dont les énoncés d'action figurent en entier.
- Une règle de décision se prête bien aux questions `d` 4–5 : le facteur de haut risque (âge ≥ 65 ans) piège le candidat qui teste d'abord la rotation ou se fie au Glasgow à 15.
- Le guide SIRA contredit sa propre table 5 (âge, radiologie) : cite les recommandations numérotées, pas la table.

## Leçons (producteur unique, lot 48, 25.11.2026)
- Quand WebFetch attend une permission sans réponse, ne relance aucun appel qui en demande : reste sur le connecteur PubMed (résumés, PMC) ; un résumé d'étude princeps (Seaberg 1991, Roser 1999, Maigne 2000) suffit pour un chiffre précis, à citer « résumé lu ».
- `get_full_text_article` peut renvoyer `full_text` vide (Ochsner J, PMC3963058) : n'utilise alors que le résumé.
- Traumatologie bénigne (S20.2, S30.0, S60.1) : les questions `d` 4–5 se construisent sur le diagnostic grave caché derrière la lésion banale (rate, fracture pathologique, syndrome coronarien, queue de cheval, fracture du sacrum par insuffisance, chordome, mélanome unguéal, fracture ouverte de P3).

## Leçons (producteur unique, lot 49, 25.11.2026)
- Accès direct ajouté par Vial au bac à sable : ncbi.nlm.nih.gov, swissmedicinfo.ch, compendium.ch, bag.admin.ch, kdigo.org. En pratique, `curl` sur pubmed.ncbi.nlm.nih.gov et pmc.ncbi.nlm.nih.gov renvoie une page JavaScript ou un reCAPTCHA : garde le connecteur PubMed (`get_article_metadata`, `get_full_text_article`) pour les résumés et les textes PMC.
- swissmedicinfo.ch est une application JavaScript sans API publique lisible ; compendium.ch répond en JSON à `POST /search/searchproducts` (`{"SearchType":"Product","Input":{"q":"<nom>","limit":20}}`) et sert le résumé « Brevier » sur `/product/<n>/mpro`. Script : `/home/claude/outils/aips.py <nom> [motifs]`. Le Brevier n'est pas l'AIPS complète : cite-le « Compendium.ch, résumé (Brevier) … ; AIPS complète à vérifier ».
- Sources lisibles par WebFetch : règle d'Ottawa (ECAT de l'ACI NSW, aci.health.nsw.gov.au) ; AFP 2007 Heim « Foreign bodies in the ear, nose, and throat » (cotes SORT C) ; MSD Manual « External Ear Obstructions » (revue mai 2026) ; RUG HUG « Brûlures » 28.05.2024 (degrés, règle de 20, seuils d'avis 3–5 % au 2e degré profond, Parkland au-delà de 20 %) ; décision MHS « brûlures graves » du 22.06.2010 (PDF chuv.ch).
- Brûlure, corps étranger : une vignette `d` 4–5 masquée décrit l'agent et les constatations (huile, poils qui s'arrachent, disque métallique) sans « brûlure », « degré », « corps étranger » ni « conduit auditif » ; un calcul de Parkland qui cite le degré prend `m=0` et `d` 3.

## Leçons (producteur unique, révision des sources du lot 48, 25.11.2026)
- Une conduite tirée d'un avis d'expert peut contredire la preuve : la fracture ouverte de P3 ne demande pas d'antibiotique prophylactique (Metcalfe 2016, PMID 26329883 ; Stevenson 2003, PMID 12954243), et la plaie du lit relève souvent de l'observation (AFP 2025 « Fingertip Injuries ») ; cherche une source avant d'écrire une conduite « évidente ».
- Sources lisibles : plan de vaccination suisse 2026 en PDF direct sur bag.admin.ch (tableau 10 du tétanos : écrasement et brûlure grave = risque élevé ; rappel dT si dernière dose ≥ 10 ans entre 26 et 64 ans, ≥ 5 ans sinon) ; page OFSP de la LAA (8 heures par semaine pour les accidents non professionnels) ; voie nationale britannique de suspicion de queue de cheval (GIRFT 2023, IRM dans les 4 heures, toucher rectal non nécessaire) ; Andersen 2022 sur la coccygodynie en texte intégral (PMC9393997).
- Outil 0 token : `/home/claude/outils/editn.py <forme> <json>` remplace des notions par clé (rubrique, nature, poids, suisse, expression de source, énoncé) sans toucher aux questions.

## Leçons (producteur unique, lot 50, 25.11.2026)
- Sources lisibles : Paal 2022 « Accidental Hypothermia: 2021 Update » en texte intégral (PMC8744717 : stades, système suisse révisé, ECLS, arrêt cardiaque sous 30 °C) ; Obsan bulletin 8/2024 (958 suicides en 2022, méthodes par sexe, 14 137 hospitalisations) ; fiche DGS Vaud 2022 « Décès de cause non naturelle ou indéterminée » ; notices bernoises sur l'art. 314c/314d CC (kja.dij.be.ch) et sur le PAFA (kesb.dij.be.ch, notice 066) ; page ge.ch « Le signalement » (art. 443 CC : levée du secret avant l'avis) ; page OFJ « Aide aux victimes » (142 depuis le 1er mai 2026) ; NICE NG225 « Rationale and impact ».
- Piège juridique utile aux questions `d` 4–5 : l'avis à l'APEA pour un adulte exige la levée du secret médical, alors que l'art. 314c al. 2 CC permet au médecin d'aviser sans levée pour un enfant ; les médecins sont exclus de l'obligation de l'art. 314d.
- Une fiche voisine déjà produite (T42.4_1, coma toxique et flumazénil) laisse à T42.4 l'angle du froid : mesure centrale, système suisse faussé par l'intoxication, mobilisation douce, critères ECLS, chocs et adrénaline sous 30 °C.
- Suicide (X61) : angle médico-légal (légiste, police, ministère public, préservation des lieux) et évaluation du survivant (pas d'échelle de risque, suivi à 48 heures, ASSIP, limitation des moyens) ; aucune dose ni méthode.
- Après un refus de permission WebFetch, ne relance que des URL déjà renvoyées par un WebSearch : elles passent sans nouvelle demande.

## Leçons (producteur unique, lot 51, 25.11.2026)
- Sources lisibles : plan de vaccination suisse 2026 en PDF direct (bag.admin.ch, `pdftotext -layout` puis grep : schéma 2 + 1, RORV 9/12 mois, rotavirus, VRS, Ag HBs, contre-indications p. 43, rattrapage) ; critères internationaux de l'ECG de l'athlète (Drezner 2017, PDF complet sur acsep.org.au) ; Albiński 2022 (SMW, proposition suisse d'évaluation cardiovasculaire du jeune sportif, smw.ch par WebFetch) ; NICE CG164 (`/chapter/Recommendations`) ; NICE DG27 seulement en `nice.org.uk/guidance/DG27/chapter/1-recommendations` (les autres casses échouent) ; BSG 2020 hérédité colorectale (PMC7034349) ; texte de la LAGH (état 01.12.2022) en PDF sur curml.ch.
- `get_article_metadata` renvoie des centaines d'auteurs pour un consortium (Kuchenbaecker) : demande un PMID à la fois et ne relis pas la notice deux fois.
- Pathologie « acte » (certificat, conseil, vaccination) : la vignette `d` 4–5 masquée ne contient pas le libellé de l'acte (« certificat », « aptitude », « BRCA », « Lynch », « plan de vaccination », « vaccination de base ») ; elle décrit la situation et la décision. Passe `masque.py` avec ces mots.
- Une série dont l'étape 2 nomme le gène ou l'acte prend `m=0` même si l'étape 1 reste masquée.

## Leçons (producteur unique, lot 52, 25.11.2026)
- Sources lisibles : avis d'experts SSGO n° 33 « Conseil pré-conceptionnel » 2010 (PDF sggg.ch) ; fiche SSN « Les folates » 2026 (valeurs OSAV 2022 ; 400 µg au moins 4 semaines avant) — discordance à signaler avec la SSGO 2010 (2 à 3 mois avant) ; Cochrane 2015 acide folique (PMID 26662928) ; page OFSP « Interprétariat communautaire » ; document CHUV 2015 sur l'interprétariat (service national 0842 442 442, à revérifier) ; Flores 2012 (PMID 22424655) ; brochure palliative.ch 2024 sur le Spiritual Care (STIV-RePer, NASCA, kit d'indicateurs) ; Monod 2010 SDAT (PMID 21144024) ; Kissane 2001 démoralisation (PMID 11324179).
- N'écris jamais un premier auteur que tu n'as pas lu : cite alors le titre, la revue et le PMID seuls.
- Les rapports OFSP anciens (acide folique 2002) servent pour un fait stable (fermeture du tube neural J15–J28), pas pour une posologie.
- `curl` sur une ressource NICE en `/resources/...pdf` renvoie une page HTML : vérifie `file` avant `pdftotext`.

## Leçons (producteur unique, lot 53, 25.11.2026)
- Un bloc de correction accepte au plus 4 sources (`sources` : 1 à 4) ; une cinquième fait échouer le schéma (« SCHEMA: [...] »).
- `/home/claude/outils/aips.py` écrit dans `/tmp/src/` : crée ce dossier (`mkdir -p /tmp/src`) après un redémarrage, sinon le script échoue après la recherche.
- Sources lisibles : NICE CG76 (adhésion) sur `/chapter/Recommendations` (la page `1-Guidance` ne donne que l'introduction) ; NICE NG234 sur `/chapter/Recommendations` (minuscules : erreur) ; NICE NG239 (B12) en PDF direct par `curl` (lien `/resources/...-pdf-66143904531397`, repéré par WebSearch) ; convention LOA V de pharmaSuisse (PDF, art. 6 semainier : ≥ 3 médicaments, sur prescription, au plus 1×/semaine ; le Polymedikations-Check n'y figure plus) ; page OFSP « participation aux coûts » (300 CHF, 10 %, 700 CHF, 40 %) ; NHS Highland TAM441 (folates) ; EHA-ESMO 2021 myélome en texte intégral (PMC7861652, soins de support seulement en annexe) ; Rajkumar 2024 (PMC11404783, critères IMWG chiffrés, prophylaxies).
- Une recommandation de NICE peut contredire une autre sur un même symptôme (fatigue seule : pas de dosage des folates selon NHS Highland, mais signe possible de carence en B12 selon NG239) : formule la question sur la vitamine précise.
- Pathologie « comportement » (non-adhésion) : la vignette `d` 4–5 masquée décrit les constatations (boîtes scellées, déséquilibre inexpliqué, renouvellements manqués) sans « adhésion » ni « observance » ; la porte financière (O7.4) se traite par la franchise et la quote-part.

## Leçons (producteur unique, lot 54, 25.11.2026)
- Sources lisibles : NICE NG88 et NG73 en PDF direct par `curl` (liens `/resources/...pdf` repérés par WebSearch ; vérifier `file`) ; consensus MUSA révisé 2022 (PMID 34587658, résumé : signes directs et indirects) ; aide-mémoire OMS MGF du 31.01.2025 (types 1–4, complications) ; page OFSP « Mesures contre les MGF » (24 600 femmes, art. 124 CP depuis juillet 2012, Réseau suisse contre l'excision) ; Lettre de protection contre l'excision 01.12.2023 (6 mois à 10 ans, acte à l'étranger punissable, expulsion 5–15 ans) ; Bazzoun 2026 (SMW 5171, texte HTML par `download/5171/6771?inline=1`) ; CDC 2021 « Neurosyphilis, Ocular Syphilis, and Otosyphilis » et « Syphilis » (WebFetch après WebSearch) ; formulaire OFSP de déclaration clinique de la syphilis (une semaine, médecin cantonal).
- Une copie de recommandation hébergée par un tiers (glowm.com, hse.ie) peut renvoyer du HTML ou du JavaScript au lieu du PDF : vérifie `file`, puis passe à une autre source lue sans contourner.
- Un item de questionnaire de connaissances (Bazzoun 2026) n'est pas une recommandation : cite-le « item de connaissance, à vérifier dans une recommandation ».
- Vignette `d` 4–5 sur la syphilis : écris « les deux tests sérologiques demandés » et décris les pupilles sans « Argyll Robertson », sinon `m=0`.

## Leçons (producteur unique, lot 55, 25.11.2026)
- `get_full_text_article` renvoie désormais le texte entier dans le contexte (plus sur disque) : pour une recommandation longue, préfère WebFetch sur la page PMC avec une consigne ciblée (« quote verbatim the recommendations on… ») ; PMC répond sans captcha à WebFetch (IDSA 2017 diarrhées PMC5850553, SEOM 2018 PMC6339667, Iba 2019 PMC6603393).
- `/home/claude/outils/aips.py` prend le premier produit trouvé : pour une molécule générique (pipéracilline-tazobactam), passe le nom commercial complet (« Piperacillin Tazob Sandoz 4.5 »), sinon le script s'arrête sans résumé.
- La limitation LS du Compendium (Soliris : garantie de paiement, ADAMTS13 > 5 %, STEC négatif, renouvellement à 6 mois puis chaque année) fournit une notion suisse solide pour les médicaments orphelins.
- Sources lisibles : formulaire OFSP EHEC (déclaration clinique en 24 heures au médecin cantonal, incubation 2–10 jours) et aperçu OFSP des déclarations obligatoires du 15.12.2025 (PDF bag.admin.ch) ; Wada 2014 (J Intensive Care, PDF biomedcentral : synthèse BCSH, JSTH, SISET et ISTH sur la CIVD ; le seuil de fibrinogène y porte une coquille « g/dl ») ; NICE CG151 sur `/chapter/Recommendations`. La copie BCSH 2009 sur confluence renvoie du HTML.
- Deux recommandations peuvent diverger sur une durée (NICE CG151 : arrêt à la réponse ; SEOM 2018 : au moins 7 jours) : écris chaque énoncé avec sa source au lieu de trancher.
- Entité voisine déjà produite (M31.1, MAT) : D59.3 prend l'angle de la forme post-diarrhéique de l'enfant, du pneumocoque et du complément ; D65 prend l'angle de la coagulation consommée qui la distingue de la MAT.

## Leçons (producteur unique, lot 56, 25.11.2026)
- NICE NG158 (TEV) : la page `/chapter/recommendations` échoue par WebFetch ; le PDF complet (`/resources/...-pdf-66141847001797`, repéré par WebSearch) se lit par `curl` puis `pdftotext` (Wells, échographie < 4 h, AOD, 3 mois, thrombophilie 1.9.x, glossaire « provoked » qui inclut CHC et THM).
- Source suisse lisible sur la contraception combinée : handout SSGO 2013 de Merki-Feld et al. (PDF hug.ch : check-list, lévonorgestrel moins thrombogène, contre-indications absolues dont l'antécédent de TEV et la migraine avec aura) ; HPC Swissmedic du 23.08.2013 (check-list à chaque consultation).
- WSES 2020 appendicite (PMC7386163) se lit en PDF complet sur wjes.biomedcentral.com ; extrais les « Statement » et « Recommendation » par `grep -A4`. Le PDF de Thorax (BTS 2023) renvoie du HTML par `curl` : seule la page article par WebFetch a donné le résumé des recommandations, sans conseils d'avion ni de plongée (écrits « à vérifier »).
- Une permission WebFetch sans réponse bloque aussi les variantes d'URL (pmc.ncbi.nlm.nih.gov au lieu de www.ncbi.nlm.nih.gov/pmc) : n'appelle que l'URL exacte renvoyée par WebSearch.
- Une vignette `d` 4–5 sur une TEV décrit la jambe ou la dyspnée sans « thrombose », « embolie » ni « caillot » ; une question qui cite l'antécédent prend `m=0` et `d` 3.

## Leçons (producteur unique, lot 57, 25.11.2026)
- Sources lisibles en texte intégral par `get_full_text_article` : Bologna 2017 occlusion sur brides (PMC6006983, tableau 5 des recommandations), WSES 2017 urgences du cancer colorectal (PMC6090779, énoncés 1.1–4.1), MASCC 2022 occlusion maligne (PMC9046338, tableau 3), WSES 2017 infections intra-abdominales (PMC5504840, 110 000 caractères : extrais les « (Recommendation » par grep). Un texte de plus de 50 000 caractères arrive sur disque : `json.loads` puis grep.
- liguecancer.ch se lit par `curl` (page « Dépistage du cancer du côlon ») : vérifie soi-même une source suisse reprise d'un lot précédent au lieu de la recopier.
- Le Brevier du Compendium fournit des pièges suisses utiles : l'occlusion maligne n'est pas une indication de Sandostatin, et la notice de Buscopan contre-indique l'iléus obstructif, alors que la MASCC en discute l'usage palliatif.
- `get_article_metadata` sur une recommandation WSES renvoie des dizaines d'auteurs : préfère `convert_article_ids` pour obtenir le PMC, et cite le titre sans premier auteur si tu ne l'as pas lu.
- Trois canoniques voisins d'occlusion (K56.6_3, K56.6, K56.2 volvulus) se répartissent ainsi : brides et cancer colique sténosant ; occlusion maligne palliative (NON_MONOGRAPHIQUE) ; volvulus.
