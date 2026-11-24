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
- 13–14 type A (5 options, 1 juste), 4 Kprim (4 énoncés), 2 menus longs (12 options) ; une série progressive de 3–4 étapes.
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

Relais : `ultra-competent-fast-doctor`, `medical-accuracy-100`, `i-write-so-fast`.

Signature : AAI (Anthropic AI)
