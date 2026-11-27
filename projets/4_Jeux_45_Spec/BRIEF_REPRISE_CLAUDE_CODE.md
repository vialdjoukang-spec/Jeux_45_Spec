# BRIEF — Claude Code reprend la main sur Jeux 45 Spec (MedSuisse Arena 45)

> Phrase de lancement : « Lis et exécute projets/4_Jeux_45_Spec/BRIEF_REPRISE_CLAUDE_CODE.md ». Modèle : Opus 5.5, effort Élevé.
> Ordre de Vial : ce jeu ne démarre qu'après la fin de Paraclinique et de la Tétrade, avec une pause d'une heure entre deux jeux (`projets/SEQUENCE_VIAL.md`).

## 1. État mesuré (27.11.2026)
- Jauge : **1 228 / 2 525 pathologies**, **24 548 / 50 500 QCM** (20 par pathologie), soit **49 %** (`projets/JAUGES.md`, régénérée automatiquement).
- Groupes : A 420/500 · A2 15/176 · B 42/439 · **C 122/800** · INF 33/61 · NEU, PED, PSY (voir leur `PROGRESSION_*.md`).
- Point exact de reprise du groupe C : `projets/45spec/REPRISE_C.md` → **R16.2__F1_6-E07** (hépatosplénomégalie), puis R18__S3_2-E03, R23.2__G7-E05, selon `content/pathologies/RANG_RENDEMENT.json`.
- Statut d'audit du groupe C : `audit.rejector = null` → **rien n'est encore audité médicalement**.
- Branches `origin/agent/45spec-C-lot3, lot5, lot7, lot8, lot9` : un commit chacune non fusionné tel quel ; `REPRISE_C.md` les déclare fusionnés. Vérifie par diff de contenu (`git diff origin/main origin/agent/45spec-C-lotN -- content/`) avant de les supprimer ou de les fusionner.

## 2. À lire, dans cet ordre (et rien d'autre avant d'agir)
1. `projets/SEQUENCE_VIAL.md`, puis `PROMPT_JEU_45_SPECIALITES_SUISSE.md` (ou `00_existant/PROMPT_JEU_45_SPECIALITES_SUISSE.md`) : le prompt de Vial, épinglé.
2. `.claude/skills/agent-producteur-45spec/SKILL.md` : méthode, règles de fond, leçons (obligatoire).
3. `.claude/skills/production-45spec-sans-api/`, `production-manuelle-45spec/`, `45spec-production-sans-api/` : variantes ; en cas de conflit, `agent-producteur-45spec` l'emporte.
4. `projets/45spec/REPRISE_C.md` et `PROGRESSION_C.md`.
5. `CANEVAS_GENIE_LOGICIEL.md`, `PROCEDURE_CREDITS_CLAUDE.md` (architecture fiches → réflexes → items).

## 3. Outils (tous dans le dépôt)
| Rôle | Chemin | Commande |
|---|---|---|
| Ordre de production | `projets/45spec/progression.py`, `progression_groupe.py` | `python projets/45spec/progression.py <SPEC>` |
| Écrire une pathologie (forme compacte) | `projets/45spec/compact_C/cNN_<ID>.py` | modèle : `compact_C/c26_R13.py` |
| Construire les 3 fichiers | `projets/45spec/constructeur_agent_45spec.py`, `agent_ecrire.py` | `PYTHONPATH=projets/45spec python projets/45spec/constructeur_agent_45spec.py <compact.py>` |
| Couverture (bloquant) | `projets/45spec/couverture_compacte.py` | `python projets/45spec/couverture_compacte.py <compact.py>` |
| Schémas et `valider()` | `scripts/produire_notions_questions.py`, `scripts/schema_fiche.json`, `scripts/schema_item.json` | — |
| Menus longs (1 à 3 justes) | `projets/45spec/controle_menus_longs.py` | `python projets/45spec/controle_menus_longs.py <SPEC>` |
| Rang de rendement | `scripts/classer_rendement.py` | `python scripts/classer_rendement.py` |
| Arène 45 (decks) | `conception/outils/arene45/construire_arene45.py` → `conception/prototypes/arene45/decks/` | via `controles45.sh` (cache haché) |
| Test sans écran de l'arène | `projets/45spec/outils/test_arene.py` | doit afficher « erreurs: 0 » |
| **Tous les contrôles avant fusion** | `projets/45spec/outils/controles45.sh` | `bash projets/45spec/outils/controles45.sh .` |
| Aides de session (masquage, forme, AIPS…) | `projets/45spec/outils/{masque,forme,aips,qset,val,vueq,digest,tampon,editn,bpq,repare_ssp}.py` | lire l'en-tête de chaque script |

Sorties : `content/notions/<SPEC>/<id>.json`, `content/questions/<SPEC>/<id>.json`, `content/corrections/<SPEC>/<id>.json`.

## 4. Format exact d'une pathologie (non négociable)
- 20 questions : **13–14 type A** (5 options, 1 juste), **4 Kprim** (4 énoncés vrai/faux), **2 menus longs** (12 options, **1 à 3 justes**, énoncé « Choisissez les N… »), une série progressive.
- `m=1` (starting point, diagnostic **masqué**) par défaut ; `m=0` dès qu'une vignette nomme le diagnostic.
- Couverture : chaque notion de poids ≥ 2 apparaît dans **deux questions d'angles différents** ; poids 3 ≤ 15 %, poids 2 ≤ 35 %.
- Natures de notion : uniquement l'énumération `NATURES` ; `surveillance.suivi` ≥ 2 lignes.

## 5. Règles de fond (Vial)
- Sources : SSI, OFSP, Swiss TPH, AIPS (compendium.ch), HUG, CHUV, sociétés suisses d'abord ; puis NICE, ESC, etc. **Jamais de référence inventée.** Doute → « (à vérifier) » dans `source`.
- Chaque posologie : « posologies à vérifier dans l'AIPS (Swissmedic) ».
- Phrases entièrement verbales, contexte suisse ; jamais CNP/CPCM comme lieu d'un cas ; **jamais de contenu de QCM montré à Vial** dans le chat.
- Ne lance **pas** `couverture_notions.py` sur une branche agent (il réécrit les autres spécialités).

## 6. Circuit Git
- Clone privé : `git clone --single-branch --branch agent/45spec-C https://github.com/vialdjoukang-spec/Jeux_45_Spec /home/claude/aai_c45` (crée la branche depuis `main` si elle n'existe plus).
- Un commit par lot de **3 pathologies**, push immédiat sur `agent/45spec-C-lotNN`.
- Fusion sur `main` seulement après `controles45.sh` vert (0 menu fautif, 0 erreur `valider()`, arène « erreurs: 0 »). Jamais de push forcé ; un refus de permission s'arrête et se signale.
- Après chaque lot : `python projets/45spec/progression.py C` puis mise à jour de `REPRISE_C.md` (pathologie suivante).

## 7. Le plus difficile (là où se joue la qualité)
1. **Le volume** : ~1 300 pathologies × 20 questions restent à produire ; la qualité baisse dès qu'on accélère. Garde le rythme de 3 pathologies par lot, avec contrôles.
2. **Le masquage** : une vignette « starting point » ne doit trahir le diagnostic ni dans l'énoncé ni dans les options ; c'est l'erreur la plus fréquente.
3. **Les discordances de sources** (déjà listées dans `REPRISE_C.md` : métoclopramide, atropine 0,5 vs 1 mg, PCR amniotique, etc.) : on cite la source suisse, on signale l'écart, on ne tranche pas de mémoire.
4. **L'audit médical** : rien du groupe C n'est audité (`rejector = null`). L'audit Gemini (`Gemini_cross-check-hard/4_Jeux_45_Spec/`, 289 lots) doit passer avant toute annonce « fini ».

## 8. Rapport à Vial (court, phrases verbales)
Pathologies produites (avant → après), contrôles verts, branches fusionnées, points « à vérifier », skills chargés. Aucun contenu de question dans le rapport.

Signature : AAI (Anthropic AI)
