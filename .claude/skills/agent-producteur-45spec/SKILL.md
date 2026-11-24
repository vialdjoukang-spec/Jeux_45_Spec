---
name: agent-producteur-45spec
description: Produit, sans appel à l'API Anthropic, les notions, questions et corrections du jeu 45 Spec au format exact de scripts/produire_notions_questions.py. S'active dès qu'un agent remplace l'API pour une spécialité (branche agent/45spec-<SPEC>).
---

# Agent-producteur-45spec

## Pourquoi
L'agent écrit lui-même le contenu que le script demanderait à l'API ; il doit donc respecter les mêmes schémas, la même fonction `valider()` et les mêmes règles de couverture, sinon les fichiers ne passent ni l'audit ni `couverture_notions.py`.

## Méthode
1. Liste les pathologies avec `canoniques("<SPEC>")` (ordre fréquence puis id) et saute celles dont les trois fichiers existent.
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

Relais : `ultra-competent-fast-doctor`, `medical-accuracy-100`, `i-write-so-fast`.

Signature : AAI (Anthropic AI)
