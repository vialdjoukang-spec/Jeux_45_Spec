# REPRISE — à lire en entier avant toute action

Dernière mise à jour : 2026-11-21 (soir) · Le système cardiovasculaire est rédigé ; voir §8.
Auteur et décideur : Dr Vial Tato Djoukang (psychiatre, préparation de l'examen fédéral suisse). Langue : français, phrases verbales, jamais nominales.

## 1. Les 4 projets (dossier `projets/`)
| Dossier | Contenu | Production |
|---|---|---|
| `1_Jeux_Tetrade_Fondation` | Anatomie, physiologie, sémiologie, physiopathologie ; Psyché ; pharmacologie systémique (VIT DIT CAFé) | Abonnement (Claude Code) |
| `2_Jeux_Paraclinique` | Examens complémentaires (biologie, imagerie, explorations) | Abonnement |
| `3_Transversal_Discip` | 19 disciplines-outils A → S (Cartographie Renouveau) + 12 lentilles cliniques ; visuel adapté par leçon | Abonnement |
| `4_Jeux_45_Spec` | MedSuisse Arena 45 : les corrections servent de cours | API par lots (200 $/mois) |

Chaque projet contient : `chantier.json`, `.html`, `.pdf`, `audit_1.md`, `audit_2.md`, `README.md`. Classement par coût : `projets/README.md`. Sources : `projets/outils/chantiers.py` → `rendre_chantiers.py`.

**VIT DIT CAFé** (validé par Vial) = les altérations d'un tissu ou d'un organe : Vasculaire, Infectieux, Traumatique, Dégénératif, Inflammatoire, Tumoral, Congénital, Auto-immun, Fonctionnel, Endocrinien.

## 2. Budget et sécurité
- 200 $ par mois de crédits API Claude (ils expirent) : réservés à Jeux_45_Spec. Les autres projets passent par l'abonnement.
- Pipeline : JSON d'abord (schéma + audit), puis des scripts injectent les JSON dans le HTML ; aucune page écrite à la main.
- La clé API ne va JAMAIS dans le dépôt (public) : uniquement `setx ANTHROPIC_API_KEY` sur le PC.
- `#signature-ia` ne se retire qu'avec l'autorisation de Vial. Aucun nom d'IA dans les prompts.
- On archive les fichiers de cours plutôt que de les supprimer (les fichiers de conception obsolètes peuvent être retirés).
- Traquer le gaspillage de tokens : script gratuit avant IA payante.

## 3. Règles d'image (non négociables)
- Vraie 3D (BodyParts3D, puis Z-Anatomy) et vraies images du web ; **jamais de SVG**.
- Organes génitaux externes occultés (discard dans une boîte pelvienne `voile`).
- Anatomie : de l'extérieur vers l'intérieur ; fenêtre de structure à 4 vues au moins ; radio-anatomie **normale** à droite du cliché pathologique (lésions numérotées, repères normaux lettrés).

## 4. Style du réseau (moteur `conception/prototypes/moteur/reseau3d.html`)
- Le côté du premier trait né du corps décide du sens : à droite → tout se développe à droite ; à gauche → à gauche. Le corps glisse du côté opposé.
- Traits **droits**, jamais courbes, ne traversant jamais le corps ; trait horizontal du corps au système, puis longue verticale qui liste les organes de haut en bas.
- Connecteurs en accolade (bus), convergence fan-in, **symétrie parfaite**.
- Cases rectangulaires (pas d'ellipses), 7 thèmes contrastés, texte très contrasté.
- Dévoilement progressif au clic ; un seul bouton ↺ : clic = repli sélectif, double-clic = repli global.
- Sélecteur de lentilles ; onglets des 4 espaces : anatomie, physiologie, sémiologie, physiopathologie.
- Police du contenu : Atkinson Hyperlegible ; taille modérée.

## 5. Systèmes et organes (source unique `conception/outils/systemes.py`)
- Un système déroule **TOUS** ses organes (14 systèmes, 124 organes). Jamais un système réduit à un organe.
- Une seule maison par organe partagé : l'autre système y renvoie (`LIENS` dans `construire_config_tetrade.py`). Ex. : « Circulation pulmonaire » vit dans le cardiovasculaire ; le système porte vit dans le digestif.
- Clic sur un organe → contenu de l'espace actif :
  - Anatomie : macroscopie, microscopie, vascularisation, innervation (+ rapports et projections, embryologie et variantes), en arbre propre ; chaque mot-clé ouvre une **image 3D** de la structure.
  - Physiologie : paramètres du simple au complexe ; chaque mot-clé ouvre une **courbe calculée**, un tracé ou un calculateur (`fenetres.js` : odc, hh, alveolaire, gazometrie, spiro ; wiggers, pv, starling — un seul moteur `hemo()` à élastance variable —, ecg, pa, hemodyn, starling_cap, do2, bernoulli, ips ; 3d). Gaz en kPa ; PA en mmHg (pratique suisse) ; altitude (La Chaux-de-Fonds ≈ 1000 m).
  - Physiopathologie : l'organe débouche sur **4 paliers** — Très fréquentes, Fréquentes, Urgences, Pièges (rares) — puis sur les pathologies (`type` « Diagnostic · … »), chacune avec infobulle 4 rubriques + bilan par visée + traitement (posologie, source). C'est ce qui rend les 4 onglets jouables pour Spec_45.
  - Rédaction : texte compact dans `conception/outils/<systeme>/` (`contenu.txt`, `pathologies.txt`, `glossaire.txt`), lu par `<systeme>.py` à 0 token. Modèle : `cardio/` + `cardio.py`.
- Le gabarit 6 volets d'anatomie / 5 de physiologie **n'est pas universel** : il se réadapte système par système (ex. Psyché : circuits, neurotransmetteurs, fonctions).
- Fichiers : `construire_config_tetrade.py` → `prototypes/moteur/tetrade.json` ; `generer_json.py` → `donnees/tetrade/<systeme>/organes.json` et `organes/<organe>.json`.

## 6. Infobulles et contenu
- **Concision = base non négociable** : la case porte un nom court (≤ 45 caractères) ; détails, courbes et explications longues vont dans l'infobulle ou la fenêtre.
- Infobulle systématique et symétrique sur chaque case (rubriques selon l'espace : `rubriques` dans la config).
- Glossaire : tout sigle ou terme technique (ex. « atypique ») porte sa propre infobulle ; l'apprenant ne quitte jamais l'application.
- Sémiologie : 2 à 3 signes typiques par temps d'examen (un seul seulement si la sémiologie n'en offre qu'un : `uniqueAssume`, dit dans l'infobulle). Signes et symptômes classés typiques / **atypiques en rouge**, à chaque temps d'examen et à l'anamnèse. Expliquer chaque signe d'un syndrome ; dire la confusion possible.
- Sons réels d'auscultation (HLS-CMDS) : galop, crépitants, etc.
- Diagnostic, infobulle du **bilan** : seulement des noms, groupés par visée puis par groupe (› Biologie : … › Score : …) ; chaque nom porte en infobulle le signe recherché et son seuil. Visées : diagnostique (1re intention, puis gold standard) ; extension et retentissement ; étiologique ; suivi des complications ; thérapeutique (si applicable) ; sortie (si hospitalisation).
- Diagnostic, **traitement** : noms seulement ; posologie en infobulle avec source, cascade suisse : AIPS, Compendium, sociétés suisses, sociétés européennes.
- Paraclinique : chaque technique porte son facteur discriminant, son avantage sélectif, l'examen qu'elle remplace et sa limite ; séquences IRM ; Smarter Medicine.
- Les 12 lentilles (pédiatrie, gériatrie, femme/grossesse, chirurgie, psychiatrie…) isolent les particularités dans les zones communes, sans ajouter de contenu.

## 7. Audits (obligatoires, 0 token)
- `python conception/outils/auditer_conception.py` → 30/30 au dernier passage (organes complets, concision, fenêtres existantes, glossaire, typique/atypique, bilan par visée, sons, radio-anatomie, 27 techniques, 19 disciplines A–S, pas de SVG, pas de joker).
- `python conception/outils/auditer_couverture.py` → RÉUSSI.
- `python conception/outils/rendre_plans.py` → audit interne 31/31 par plan, PDF.
- Chaîne complète : `construire_config_tetrade.py` → `construire_plans.py` → `generer_json.py` → `rendre_plans.py` → audits → `projets/outils/chantiers.py` → `rendre_chantiers.py` → commit/push.
- Rendu headless : Playwright + Chromium SwiftShader ; `shot.py "config.json&ouvrir=…&espace=…&fenetre=…&bulle=…&theme=…"`.

## 8. État au 2026-11-21 (soir)
- **Cardiovasculaire rédigé** (validé par Vial : 14 organes, volets adaptés par type, fenêtres) : 14 organes × anatomie + physiologie (≈ 200 mots-clés), 57 pathologies en 4 paliers avec bilan et traitement, 10 fenêtres de courbes testées sans écran (0 erreur JS), 101 sigles au glossaire. À relire par Vial : `conception/outils/cardio/*.txt`.
- Poumon (physiologie, 5 courbes), circuit sémiologique de l'insuffisance cardiaque gauche, pneumonie (cliché + radio-anatomie normale).
- 108 organes « à produire » (`aProduire`), listés mais vides.
- Limites connues : (1) la sémiologie par organe du cardiovasculaire reste à produire (seul le circuit de l'IC gauche existe) ; (2) la fenêtre 3D montre le même modèle (cœur) pour tous les organes : vues 3D par structure à faire ; (3) les posologies portent « à vérifier dans l'AIPS » sauf vérification ponctuelle (tafamidis 61 mg confirmé Swissmedic ; atropine 0,5 mg ERC 2025 / 1 mg AHA 2025).
- Catalogue paraclinique : 66 organes, 601 examens listés (champs à remplir).

## 9. Méthode convenue pour la suite
1. Système par système (cardiovasculaire fait ; prochain : sémiologie cardiovasculaire, puis respiratoire) : proposer la liste des organes, les volets adaptés, les fenêtres de courbes et les 4 paliers de pathologies.
2. Attendre la validation de Vial.
3. Produire le contenu ; audit bloquant après chaque lot ; commit et push.

## 10. En attente
- Pilote Jeux_45_Spec : `python scripts/produire_fiches_claude.py pilote --spec CAR --n 2` (schéma `scripts/schema_fiche.json` : `glossaire` et `examens.items.visee` obligatoires). Vial envoie les 2 fiches pour audit.
- Skill `obsidian-like-complex-network` : les liens droits sont déjà en place dans le compte ; la copie du dépôt est corrigée et synchronisée (nouvelles fenêtres, paliers). Mise à jour du compte proposée le 2026-11-21 (fenêtres + paliers).

## 11. Façon de répondre à Vial
- Réponse directe et brève ; vérité sans complaisance ; critique constructive et un « plus » à chaque proposition.
- Solution la plus économique et efficace proposée une fois, en GRAS MAJUSCULE et en couleur.
- Contenu à apprendre : de la coque vers le centre, avec le pourquoi.
- Commandes de terminal : une seule par bloc, avec son but entre parenthèses.

## 12. Tableau de bord du chantier (lié à Claude)
- Page : https://claude.ai/artifact/N7VUBhFLfp3gq6rTsPt88v (slug `aaf7eb3f-771e-48f5-8164-276c764bd25f`), source `projets/outils/taches.py` + `tableau_de_bord.gabarit.html` → `projets/tableau_de_bord.html` et `projets/taches.json` (185 tâches).
- Répartition : Claude conçoit, audite et polit ; le gros œuvre (volumes, recherche d'images) se fait sur Gemini (4 comptes Pro), Grok, Hydrogen medium, Neon medium.
- Lecture par Claude (outils claude-artifacts) : `db_list` collection `taches` (statut, plateformes, compteRendu), `imports` (métadonnées des JSON importés), `contenus` (texte des JSON en morceaux de 80 000 caractères : champs k, i, n, texte ; recoller par ordre de i).
- Quand Vial dit qu'une tâche est « Envoyé à Claude » : lire ses imports, auditer, corriger, intégrer dans le dépôt, puis passer la tâche en « Validé ».
- Après toute modification de `taches.py` : régénérer, puis republier la page (publish_files avec slug et base_version).
- Paquets de lot : `projets/lots/<projet>/<thème>/<ID>_<contenu explicite>.json` (ex. `2_Paraclinique/1_Examens_par_region/P04_Examens_Thorax_8-organes_102-examens.json`) ; ancien nom `LOT_<tâche>.json` (50 fichiers, générés par `taches.py`) = {"_lot": {...}, "fichiers": {chemin exact: contenu}} ; l'IA de production rend le même objet ; à l'import, chaque chemin se réécrit à sa place dans le dépôt.
- Index de tous les JSON avec liens GitHub et bruts : `INDEX_JSON.md` (régénéré à chaque mise à jour). Les graphes, arbres 3D, régions, index et exercices se calculent par script (T60, P36), jamais par l'IA de production.
- Signature de mes productions : AAI (Anthropic AI), demandée par Vial (champ `_lot.signature`, pied des fichiers .md).
- Paraclinique (22/11) : lots par organe `2_Paraclinique/1_Examens_par_organe/<NN_Région>/P<RR>-<OO>_Examens_<Organe>_<n>-examens.json` (66) ; biologie : `2_Biologie/1_Analyses_individuelles/PB01…PB15` (≈ 300 analyses, source unique des valeurs, catalogue `conception/outils/analyses_biologiques.py`) et `2_Biologie/2_Prelevements_technique/PP01…PP04` ; `3_Explorations_fonctionnelles/<Région>/PF…` ; `4_Endoscopies/<Région>/PE…` ; `5_Imagerie_Images_et_Cas` ; `6_Formules_Criteres_SmarterMedicine`. Chaque examen biologique d'organe porte `analysesRef` (lien automatique, audité).

## 13. Théorie et pratique (22.11.2026, demande de Vial)
- **Théorie** = ce que l'apprenant consulte : l'arbre et le réseau Obsidian fonctionnel (fichiers `conception/donnees/<module>/…`).
- **Pratique** = le jeu lui-même : arène, aventure, stations OSCE, cas-décision. Chaque fichier théorique a un jumeau `conception/donnees/pratique/<même chemin>.json`, une entité par élément, avec des défis typés.
  - Gabarits et modes : `conception/outils/pratique.py` (source unique) ; 703 fichiers pratiques générés.
  - Jeux 45 Spec : sa pratique est la couche 3 (items, `scripts/schema_item.json`).
- **Lots** : `projets/lots/<projet>/<thème>/<région ou système>/<organe ou discipline>/1_Theorie | 2_Pratique/<lot>.json`, profondeur n autorisée par Vial pour la production agentique.
  - Organes de plus de 10 examens coupés par modalité (`_fragment`) ; un organe Tétrade = un lot ; une leçon transversale = un lot.
  - Le lot pratique dépend du lot théorique (il s'appuie sur la théorie remplie).
- **Retours** : `python projets/outils/fusionner_retours.py <fichiers ou dossier>` réassemble (fragments par id), contrôle et écrit `projets/retours/rapport_fusion.md` ; `--essai` n'écrit rien.
- **Diagnostics et prise en charge** : fichier partagé par système proposé à Vial (bilan par visée, lignes de traitement), en attente de sa validation ; il servira la Tétrade, la Paraclinique, la pharmacologie et l'arène de Jeux 45 Spec.

## 14. Jeu final : onglets et recherche (spécification de Vial, 22.11.2026)
- **Théorie et Pratique sont deux onglets distincts** de chaque plateforme de jeu. Leur association dans les lots (`1_Theorie` / `2_Pratique`) sert seulement le travail des agents.
- **Onglet Théorie, deux barres de recherche** (les 3 jeux qui ont une théorie) :
  - **Mode Organe** : la barre sert de sélecteur. L'organe apparaît seul au centre de la page, puis se déplie nœud après nœud : modalités → examens → contenu pédagogique, anomalies élémentaires, syndromes paracliniques, pathologies associées.
  - **Mode Examen** : l'organe en 3D au centre et une seule ligne Obsidian horizontale vers l'examen, avec le même contenu que le mode Organe mais un accès court-circuité. Un examen lié à plusieurs organes propose leurs pastilles.
  - Usage clé : pendant la révision d'un SSP, l'apprenant tape un bilan inconnu et obtient aussitôt paramètres, valeurs normales, anomalies, syndromes et pathologies.
  - La recherche est insensible à la casse et aux accents, et propose toujours des réponses, même mal orthographiées (trigrammes et distance d'édition ; les `synonymes` produits enrichissent les clés).
- **Données** : `conception/donnees/recherche/index.json` (82 organes, environ 1 050 examens et analyses, régénéré par `generer_json.py`).
  - Les champs ajoutés aux examens et aux analyses sont `synonymes`, `aspectNormal`, `parametres` (analyses composites : électrophorèse, formule sanguine, gazométrie), `anomaliesElementaires`, `syndromesParacliniques` et `pathologiesAssociees`.
  - L'électrophorèse des protéines sériques est une fiche d'analyse (famille 08 Immunologie, lot PB08), reliée à 5 organes : sang et hémostase, reins, rachis osseux, os longs, nerfs périphériques.

## Audit de fond des lots XAi (2026-11-22)
- 88 lots fusionnés par champ (ancien format de `Production_XAi/Lots_traites` et de `paraclinique-thorax`, puis nouveau format de `production-xai-a03/a08/a09`) : paraclinique rempli de 2 % à 45 %.
- `projets/outils/audit_fond.py` (0 token, relançable) applique les corrections de Claude, range les notes : `_meta.justificationsAcceptees` (299) et `_meta.aVerifierOuverts` (25), puis publie **`SORTIES_DONNEES_FIABLES/`** : 554 examens sur 820, cœur clinique rempli et aucun doute ouvert. Le jeu charge ce dossier.
- `projets/outils/lots_complement.py` prépare pour Grok `Production_XAi/Lots_a_produire/complement_presentation/` (7 lots, 464 examens, 5 champs de présentation). Retour : `fusionner_retours.py`, puis `audit_fond.py`.
- Les dépôts de Grok arrivent sur des branches `production-xai-*` : Claude les lit directement. Suppression de branches et envoi d'étiquettes refusés depuis la session cloud (HTTP 403) : anciennes branches laissées en place.

## Sémiologie cardiovasculaire (2026-11-22)
- `conception/outils/cardio/semiologie.txt` : 13 organes (le myocarde garde le circuit pilote de l'IC gauche), temps d'examen pertinents par organe, 2 à 3 signes typiques par temps ou un signe unique assumé (`uniqueAssume`), signes atypiques en plus ; infobulle 4 rubriques.
- Les 4 onglets du cardiovasculaire sont jouables : anatomie, physiologie, sémiologie, physiopathologie (4 paliers de pathologies avec bilan et traitement).
- Garde-fou ajouté à `generer_json.py` : la régénération ne peut plus écraser une valeur remplie (fusion conservatrice par id, ref, nom ou position). Avant ce correctif, elle remettait les fichiers paracliniques et les défis à vide.

## Veille GitHub (2026-11-22)
- `.github/workflows/veille.yml` + `projets/outils/veille.py` : toutes les heures et à chaque dépôt, réparation mécanique, fusion, audit de fond, contrôles, publication sur main ; en cas d'échec, seul `CLAUDE_A_AUDITER/RAPPORT_VEILLE.md` est publié. Registre des lots traités : `projets/retours/veille_traites.json` (205 lots existants amorcés).
