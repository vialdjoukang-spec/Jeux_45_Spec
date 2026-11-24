# REPRISE — à lire en entier avant toute action

Dernière mise à jour : 2026-11-22 · Le digestif et hépatobiliaire est rédigé ; voir la section « Digestif » en fin de fichier.
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
1. Système par système (cardiovasculaire, respiratoire, digestif, rénal, neurologique, endocrinien, hématologique, infectieux, locomoteur et dermatologique faits ; prochain : ophtalmologique et ORL) selon le skill `systeme-jouable-builder`.
2. Depuis le 2026-11-22 (soir), Vial donne son accord d'office pour ce projet : Claude produit sans attendre de validation et l'informe ensuite.
3. Audit bloquant après chaque lot ; commit et push.

## 10. En attente
- Pilote Jeux_45_Spec : `python scripts/produire_fiches_claude.py pilote --spec CAR --n 2` (schéma `scripts/schema_fiche.json` : `glossaire` et `examens.items.visee` obligatoires). Vial envoie les 2 fiches pour audit.
- Skill `obsidian-like-complex-network` : les liens droits sont déjà en place dans le compte ; la copie du dépôt est corrigée et synchronisée (nouvelles fenêtres, paliers). Mise à jour du compte proposée le 2026-11-21 (fenêtres + paliers).

## Blocages et décisions en attente (lu par le tableau de bord `tableau/`)
Format obligatoire, une ligne par point : `- [qui peut débloquer] ce qu'il faut faire`. Retirer la ligne dès que le point est réglé ; le robot `tableau.yml` la publie en 10 minutes.
- [Vial] Décider du catalogue pédiatrique : 6 pathologies majeures manquent encore en version enfant (ronde du 24.11, 13:20).
- [Vial] Trancher le cas des entités deuil et divorce, partagées entre plusieurs spécialités.
- [Vial] Dire si F30.1 reste une pathologie monographique.
- [Vial] Fermer l'issue GitHub #30, qui signale une fausse alerte de la veille.
- [Crédit API] La file API reste en pause jusqu'au nouveau crédit annoncé jeudi 26.11 ; la V2 attend ce crédit.
- [Claude] Reporter sur main le correctif de rang (meilleur rang des portes, branche agent/45spec-INF), puis relancer scripts/classer_rendement.py.
- [Claude] Régénérer les 5 corrections restantes de la vague 1 (E11.9, I49.5, I75.0, E87.6, B18.9).
- [Claude] Auditer puis fusionner les branches agent/45spec-INF, agent/45spec-NEU, agent/45spec-PED et agent/45spec-A.

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
- `.github/workflows/veille.yml` + `veille.py` + `cadence.py` : réveil toutes les 5 min, curseur adaptatif 5–60 min selon les lots reçus, déclenchement immédiat sur dépôt main. Réparation, fusion et contrôles sur la branche `veille/audit-medical` seulement ; file d'attente `CLAUDE_A_AUDITER/EN_ATTENTE_AUDIT_MEDICAL.json`. Registre : `projets/retours/veille_traites.json`.
- Décision de Vial (non discutable) : Claude reste garant du contenu médical. Une tâche planifiée Claude vérifie la branche, audite médicalement (`projets/outils/AUDIT_MEDICAL_CLAUDE.md`), corrige, puis ouvre et fusionne la PR vers main.

## Moteur de système générique et respiratoire (2026-11-23)
- `conception/outils/systeme_source.py` lit n'importe quel dossier de système (contenu, semiologie, pathologies, glossaire, temps) ; `systemes_rediges.py` est le registre (dossier, préfixe d'identifiant, couleur, identifiants stables). Ajouter un système = un dossier de textes + une ligne au registre. `cardio.py` reste un simple pont de compatibilité.
- Respiratoire rédigé (`conception/outils/respi/`) : 10 organes (la circulation pulmonaire reste dans le cardiovasculaire), sémiologie de 9 organes (le poumon garde son circuit pilote de pneumonie), 41 pathologies en 4 paliers, 41 sigles. La physiologie historique du poumon (volets ph0–ph4) est migrée dans la source ; la régulation part vers l'organe « Centres respiratoires et chémorécepteurs ».
- Pharynx : rédigé côté respiratoire ; le pharynx digestif deviendra un lien vers lui (comme la circulation pulmonaire).
- Nouvelles fenêtres testées sans écran (0 erreur) : `voies_centrales` (obstacles fixes et variables, Poiseuille), `compliance` (poumon, paroi, CRF ; fibrose, emphysème, obésité, pneumothorax), `vq` (shunt, espace mort, FiO₂).
- `projets/retours/migrations_ids.json` déclare les renommages d'identifiants assumés pour la garde `non_perte.py`.
- `.github/workflows/regeneration.yml` : toute modification des sources sur main régénère réseau, JSON et sorties fiables, puis lance les contrôles ; il publie seulement si tout passe (rapport `CLAUDE_A_AUDITER/RAPPORT_REGENERATION.md`).

## Ouvrier en chaîne par l'API Anthropic (2026-11-23)
- Vial a un crédit API Anthropic de 200 USD qui expire le 27.11.2026 (non cumulable ; nouveau crédit à cette date). Secret GitHub : `ANTHROPIC_API_KEY`.
- `projets/ouvrier/FILE_PROCESSUS.json` : file de tâches (état, essais, modèle, budget). `file.py` répartit le crédit restant sur les jours restants (plafond journalier, réserve de 8 USD) et journalise chaque dollar dans `depense.json`.
- `.github/workflows/ouvrier.yml` : toutes les 30 min, prend la tâche suivante, lance Claude Code en mode non interactif (`--max-budget-usd`), publie sur `veille/audit-medical`. L'audit médical horaire reste le verrou avant main. Rapport : `projets/ouvrier/RAPPORT_OUVRIER.md`.
- Haiku pour le volume (compléments de présentation), Sonnet pour les systèmes (rénal, neurologique, endocrinien). Le digestif est produit par une tâche planifiée séparée.
- Les skills utiles au travail automatique sont copiés dans `.claude/skills/` du dépôt.

## Digestif (2026-11-22, tâche planifiée)
- Le système « Digestif & hépatobiliaire » est jouable : `conception/outils/digestif/` (contenu, sémiologie, pathologies, glossaire, temps) ; registre `systemes_rediges.py` (préfixe `dg_`, couleur `#c98a2b`).
- 12 organes rédigés en anatomie, physiologie et sémiologie (7 temps d'examen, dont le toucher rectal) ; 54 pathologies en 4 paliers, avec bilan par visée (gold standard compris), traitements dosés et source datée.
- Le pharynx digestif renvoie au respiratoire (`LIENS` dans `construire_config_tetrade.py`) ; l'ischémie mésentérique aiguë reste au cardiovasculaire.
- Nouvelles fenêtres canvas testées sans écran (0 erreur JS) : `hepato_r` (rapport R), `meld` (MELD et MELD-Na en unités SI), `porte` (GPVH, loi d'Ohm, seuils de Baveno VII), `osmo` (trou osmotique fécal). Les fenêtres `gazometrie` et `starling_cap` sont réutilisées.
- Les 12 renommages `org_digest_*` → `dg_*` sont déclarés dans `projets/retours/migrations_ids.json`. Audits : conception 34/34, couverture réussie, non-perte OK.
- Reste à faire :
  - Vial relit `digestif/pathologies.txt`.
  - Points à vérifier dans l'AIPS : statut suisse de l'élafibranor et du seladelpar (cholangite biliaire primitive) ; pâte de triamcinolone buccale ; norfloxacine (la ciprofloxacine est proposée en alternative).
  - Doses tirées de la pratique courante, à recouper : IPP du Zollinger-Ellison ; thiamine à forte dose.
  - Les volets « Embryologie et variantes » restent vides pour la plupart des organes.

## 45 Spec : production lancée (2026-11-23, nuit)
- Décision de Vial : Sonnet 5.5 ; au plus la moitié du crédit mensuel (100 USD). Ébauche des 45 arènes : `content/arenes/` (`scripts/ebaucher_arenes.py`) et `content/arenes/EBAUCHE_JEU_45_SPEC.md`.
- Fiches : consigne resserrée (≈ 9 000 tokens de sortie, complètes) ; 2 fiches pilotes de cardiologie auditées « pass » (sources ESC 2024 et 2023 ajoutées) ; 44 cartes réflexes générées à 0 token. Lot de 173 fiches de cardiologie envoyé (msgbatch_01CZYim7ZgfZqNEL2WYvVWYX), récupéré par la tâche `j45_recup_CAR`.
- Questions : seules les fiches auditées « pass » servent de base (`produire_items_claude.py`). Pilote Sonnet : 6 questions de qualité, ≈ 0,08 USD par requête en direct, ≈ 0,04 USD en lot. Pilote Haiku : structure invalide, arrêté.
- Coût estimé des questions : ≈ 120 USD en lot pour toute la cardiologie (≈ 2 975 requêtes) ; le jeu entier (≈ 123 500 questions) dépasse largement le plafond mensuel : il faut choisir les rubriques et les arènes prioritaires mois par mois.

## Rénal & uro-génital (2026-11-23, ouvrier automatique)
- Le système « Rénal & uro-génital » est jouable : `conception/outils/renal/` (contenu, sémiologie, pathologies, glossaire, temps) ; registre `systemes_rediges.py` (préfixe `rn_`, couleur `#b8960f`).
- 6 organes rédigés en anatomie, physiologie et sémiologie (reins, uretères, vessie, urètre, prostate, testicules) ; 35 pathologies en 4 paliers avec bilan par visée (gold standard compris), traitements dosés et source datée (KDIGO 2021 et 2024, EAU 2024, CDC 2021).
- Nouvelles fenêtres canvas testées sans écran (0 erreur JS) : `dfg` (CKD-EPI 2021, stades KDIGO) et `fena` (fraction d'excrétion du sodium) ; `gazometrie` est réutilisée pour la compensation rénale.
- Les 6 renommages `org_renal__*` → `rn_*` sont déclarés dans `projets/retours/migrations_ids.json`. Audits : conception 34/34, couverture réussie, non-perte OK.
- Reste à faire :
  - Vial relit `renal/pathologies.txt`.
  - À vérifier dans l'AIPS : statut suisse du budésonide à libération ciblée (néphropathie à IgA), du cyclosilicate sodique de zirconium et du pivmécillinam ; doses de rituximab et de cyclophosphamide à confirmer avec un néphrologue.
  - Les volets « Embryologie et variantes » restent vides ; les uro-génitaux féminins vivent au système gynéco-obstétrical, la néphrologie de l'enfant (reflux, valves urétrales) reste à ajouter au pédiatrique.
  - Le jeu 3D montre un seul modèle pour tous les organes (limite connue).

## Neurologique (2026-11-23, ouvrier automatique)
- Le système « Neurologique » est jouable : `conception/outils/neuro/` (contenu, sémiologie, pathologies, glossaire, temps) ; registre `systemes_rediges.py` (préfixe `ne_`, couleur `#8e5cc4`).
- 13 organes rédigés en anatomie, physiologie et sémiologie ; 78 pathologies en 4 paliers avec bilan par visée (gold standard compris), traitements dosés et source datée (ESO 2021 et 2023, AHA/ASA 2022 et 2023, ESCMID 2016, EFNS 2010, EAN/PNS 2023, MDS 2015, ILAE 2017, ESC 2018).
- « Système limbique et hypothalamus » ne rédige que le limbique ; l'hypothalamus et ses axes restent à l'endocrinien (renvoi dans l'organe).
- Nouvelles fenêtres canvas testées sans écran (0 erreur JS) : `ne_ppc` (PPC = PAM − PIC, autorégulation), `ne_glasgow` (score de Glasgow), `ne_conduction` (vitesse de conduction, démyélinisation et atteinte axonale).
- Les 13 renommages `org_neurol_*` → `ne_*` sont déclarés dans `projets/retours/migrations_ids.json`. Audits : conception 34/34, couverture réussie, non-perte OK.
- Reste à faire :
  - Vial relit `neuro/pathologies.txt`.
  - À vérifier dans l'AIPS : statut suisse de la ténectéplase (AVC), de l'amifampridine (Lambert-Eaton), de l'hémine, de l'andexanet alfa et du vaccin recombinant du zona ; dose de la nimodipine dans le syndrome de vasoconstriction (avis d'expert).
  - Les volets « Embryologie et variantes » restent vides ; la 3D montre un seul modèle pour tous les organes ; les anticorps anti-amyloïde (Alzheimer) ne sont pas traités faute de statut suisse vérifié.

## Endocrinien & métabolique (2026-11-23, ouvrier automatique)
- Le système « Endocrinien & métabolique » est jouable : `conception/outils/endocrino/` (contenu, sémiologie, pathologies, glossaire, temps) ; registre `systemes_rediges.py` (préfixe `en_`, couleur `#d9731a`). « Hypothalamus et hypophyse » a sa maison ici ; le pancréas endocrine reste distinct du pancréas exocrine du digestif.
- 10 organes rédigés en anatomie, physiologie et sémiologie (9 temps d'examen, dont l'examen du pied et le champ visuel) ; 80 pathologies en 4 paliers avec bilan par visée (gold standard compris), traitements dosés et source datée (ATA 2014 et 2015 et 2016, ETA 2018 et 2023, Endocrine Society 2008 à 2019, ESE/ENSAT 2018 et 2023, ESE/ES 2024, ADA 2025, consensus ADA/EASD 2024, ESC/EAS 2019, KDIGO 2017, IWGDF 2023, ESHRE 2024, Teede 2023, NICE CG32, ESPEN/GLIM).
- Nouvelles fenêtres canvas testées sans écran (0 erreur JS, 5 modèles, tous les scénarios et les valeurs extrêmes des curseurs) : `en_tsh_t4` (rétrocontrôle TSH–T4 libre), `en_glycemie` (seuils, HOMA-IR, glycémie moyenne estimée), `en_calcium` (courbe PTH–calcium ionisé, calcium corrigé), `en_cortisol` (rythme circadien, freinage à la dexaméthasone), `en_adh` (osmolalité, hormone antidiurétique, diurèse).
- Les 10 renommages `org_endocr_*` → `en_*` sont déclarés dans `projets/retours/migrations_ids.json`. Audits : conception 34/34, couverture réussie, non-perte OK. Une relecture médicale indépendante (agent sans contexte) a relevé 9 points, tous corrigés (CD3 du DiGeorge, source de l'hypothyroïdie, seuil de potassium de l'état hyperosmolaire, Lp(a), cortisolurie, etc.).
- Reste à faire :
  - Vial relit `endocrino/pathologies.txt`.
  - À vérifier dans l'AIPS : statut suisse de la métyrapone, de la métréleptine, du sélpercatinib et du burosumab (indications), de l'aripiprazole en association ; doses de dexaméthasone et de chimiothérapie renvoyées à l'oncologue.
  - Audit médical Claude (2026-11-23) : seuils de cortisol de l'insuffisance aux corticoïdes alignés sur ESE/Endocrine Society 2024 (< 150, 150–300, > 300 nmol/l) ; insuffisance ovarienne prématurée alignée sur ESHRE 2024 (un seul dosage de FSH > 25 UI/l, prévalence 3,5 %) ; chirurgie bariatrique alignée sur les critères suisses SMOB 2023 ; nom AVP-D ajouté au diabète insipide central. L'hypopituitarisme et l'Addison gardent le seuil de 140 nmol/l d'Endocrine Society 2016.
  - Les volets « Embryologie et variantes » restent vides ; la 3D montre un seul modèle pour tous les organes ; les gonades et le métabolisme osseux renvoient pour l'anatomie au gynéco-obstétrical, au rénal et au locomoteur ; l'endocrinologie pédiatrique (croissance, hyperplasie congénitale classique) reste à compléter au pédiatrique.

## Nuit du 23 au 24.11.2026 — répartition décidée par Vial (22:38)
- **API Anthropic (crédit 200 USD, plafond 192, sans répartition journalière)** : 45 Spec. Vague 1 = END, CAR, PNE, NEP, GAS (386 pathologies : notions → questions → corrections en lots uniques), puis T3, T4, puis vague 2 bornée (NEU, PSY, MIG, INF, 60 pathologies) jusqu'à épuisement. Nouveau crédit attendu jeudi.
- **Agent sur abonnement (sous-agent de Claude)** : Transversal, 228 leçons A → S (S, F, Q d'abord), branche `agent/transversal`, audit par Claude avant fusion sur main.
- **Claude (abonnement)** : Paraclinique (F3 clichés : 352 entités vides relancées ; analyses chiffrées déclarées « sans objet »), audit médical, fusion des branches, republication des arènes, rapport de progression le 24.11 au matin.
- Outils clés : `scripts/produire_notions_questions.py` (notions | questions | correction), `conception/prototypes/commun/correction.js`, `projets/JAUGES.md` (jauges toutes les 5 min).

## 24.11.2026 00:31 — consigne de Vial : continuer sans interruption jusqu'à l'achèvement des 4 jeux
- Si le crédit API s'épuise : reprise dans 48 h (nouveau crédit API + forfait ULTRA).
- Agents sur abonnement, chacun doté des 5 skills (perfect-skill-user-organizer-collector, ultra-competent-fast-doctor, autonomous-skill-creator, pipeline-autonomous-builder, i-never-waste-token ; registre `.claude/skills/REGISTRE.md`) :
  - rédacteur Transversal (C → R) et auditeur Transversal (S, F, Q, A, B ; 109 points) sur `agent/transversal` ; Claude fusionne sur main après l'audit ;
  - constructeur Tétrade (hématologie-oncologie, puis infectieux-immunitaire) sur `agent/tetrade`.
- API : 45 Spec, vague 1 puis vague 2 jusqu'au plafond de 192 USD.
- Claude : Paraclinique (clichés), audits, fusions, rondes de nuit toutes les 2 h, rapport à 07:30.

## Hématologique & oncologique (2026-11-24, agent Tétrade, branche `agent/tetrade`)
- Le système « Hématologique & oncologique » est jouable : `conception/outils/hemato/` (contenu, sémiologie, pathologies, glossaire, temps) ; registre `systemes_rediges.py` (préfixe `he_`, couleur `#a33`).
- 6 organes rédigés en anatomie, physiologie et sémiologie (5 temps d'examen) ; le **thymus** garde sa maison dans l'endocrinien et devient un renvoi (`LIENS` dans `construire_config_tetrade.py`).
- 45 pathologies en 4 paliers (8 TF, 18 F, 13 U, 6 R), bilan par visée (gold standard compris), traitements dosés, source datée ; l'oncologie y entre par les urgences (lyse tumorale, neutropénie fébrile, syndrome cave supérieur, leucémies aiguës) et par les métastases ganglionnaires.
- Nouveau champ facultatif `aVerifier:` dans `pathologies.txt` (lu par `systeme_source.py`, stocké dans la bulle) : il porte chaque doute au lieu d'une affirmation ; 13 pathologies en portent un.
- Nouvelles fenêtres canvas testées sans écran (0 erreur JS, tous les scénarios et les valeurs extrêmes) : `he_anemie` (VGM × réticulocytes, indice de Mentzer), `he_fer` (ferritine, saturation, CRP ; seuils du consensus suisse 2019), `he_coag` (plaquettes, TP, TCA, fibrinogène, D-dimères ; score ISTH de CIVD). `odc` et `do2` sont réutilisées. Interprétations corrélées ajoutées (20 scénarios), à auditer.
- Les 6 renommages `org_hemato_*` → `he_*` sont déclarés dans `projets/retours/migrations_ids.json`. Audits : conception 34/34, couverture réussie, non-perte OK, interprétations 0 défaut.
- Anomalie préexistante sur main (non corrigée ici) : `generer_json.py` dédoublonne l'analyse IGRA (apostrophe droite ou courbe) dans `2_cou/ganglions_cervicaux.json`, et `non_perte.py` le compte comme une perte ; l'agent a restauré ces 2 fichiers depuis main avant chaque commit.
- Reste à faire : audit médical de Claude (`hemato/pathologies.txt`, interprétations `he_*`), puis relecture de Vial ; points `aVerifier` listés dans `projets/1_Jeux_Tetrade_Fondation/PROGRESSION_AGENT.md`.

## Locomoteur & rhumatologique (2026-11-24, agent Tétrade, branche `agent/tetrade-loco`)
- Le système « Locomoteur & rhumatologique » est jouable : `conception/outils/loco/` ; registre (préfixe `lo_`, couleur `#6b7280`).
- 11 organes rédigés, 6 temps d'examen, 70 signes ; 57 pathologies (13 TF, 21 F, 12 U, 11 R), 24 points `aVerifier`.
- Renvois sans doublon : ostéoporose, ostéomalacie, Paget (Endocrinien) ; radiculopathies, spondylodiscite, canal carpien (Neurologique) ; artérite à cellules géantes (Cardiovasculaire) ; Still, fasciite nécrosante (Infectieux).
- Nouvelles fenêtres canvas `lo_synovie` (liquide articulaire) et `lo_ck` (cinétique des CK), testées sans écran, 0 erreur JS ; 13 interprétations ; 11 renommages `org_locomo_*` → `lo_*` déclarés.
- Reste à faire : audit médical de Claude puis fusion ; détail dans `projets/1_Jeux_Tetrade_Fondation/PROGRESSION_AGENT.md` (section 9).

## Dermatologique (2026-11-24, agent Tétrade, branche `agent/tetrade-loco`)
- Le système « Dermatologique » est jouable : `conception/outils/derma/` ; registre (préfixe `de_`, couleur `#b07a5a`).
- 6 organes, 5 temps d'examen, 30 signes ; 32 pathologies (7 TF, 14 F, 5 U, 6 R), 12 points `aVerifier` ; fenêtre `de_brulure` (Parkland) testée, 0 erreur JS.
- L'érysipèle (Infectieux) renvoie vers Dermatologique pour ses portes d'entrée ; 6 renommages `org_dermat_*` → `de_*` déclarés.

## Infectieux & immunitaire (2026-11-24, agent Tétrade, branche `agent/tetrade`)
- Le système « Infectieux & immunitaire » est jouable : `conception/outils/infectio/` ; registre (préfixe `ii_`, couleur `#16897b`).
- 4 organes rédigés (barrières, immunité innée, immunité adaptative, complément), 4 temps d'examen ; « Organes lymphoïdes » renvoie vers ses maisons (moelle, rate, ganglions : hématologique ; thymus : endocrinien ; MALT décrit aux barrières).
- 17 pathologies en 4 paliers (3 TF, 5 F, 5 U, 4 R ; le complément n'a pas de palier « très fréquent ») ; le choc septique (cardiovasculaire), les méningites (neurologique), la fièvre méditerranéenne familiale et l'angio-œdème bradykinique aux IEC restent dans leurs maisons.
- Nouvelle fenêtre `ii_anticorps` (IgM et IgG, réponse primaire et secondaire, déficit humoral), testée sans écran, 0 erreur JS ; 4 interprétations.
- Les 4 renommages `org_infect_*` → `ii_*` sont déclarés dans `migrations_ids.json`.

## 24.11 06:40 — Ronde 4
- Vague 1 API (END, CAR, PNE, NEP, GAS) : 318 notions, 317 séries de questions (6 337 QCM : 70 % A, 20 % Kprim, 10 % menu long, formats conformes), 317 corrections récupérées sur veille/audit-medical. Contrôle mécanique OK ; échantillon médical de 3 questions juste.
- 14 corrections sans `priseEnCharge` (PNE J98.6, J69.0 ; GAS K22.7, K31.8, K90.9 ; CAR I86.1, I21.9, I95.0 ; END E66.2, E23.2, C73_1, E83.5, E83.4, E10.8) : à reprendre (T4).
- Bug corrigé : file.py cherchait le suivi dans scripts/scripts/ → END_N_recup bloqué.
- Jauge 45 Spec : compte désormais content/questions (cible 2 675).
- Agents de l'abonnement arrêtés par Vial vers 04:50 : ne pas relancer sans son accord.

## T3 : priseEnCharge des fiches existantes (24.11, ouvrier)
- Mode « pec » de `scripts/produire_fiches_claude.py` : `pec_pilote`, `pec_soumettre`, `pec_recuperer`, `pec_bilan` ; il demande seulement le bloc priseEnCharge (schéma commun), le répare en forme (moyens rendu en texte), l'insère sans toucher au reste et remet `audit.rejector` à null.
- Test direct sur 2 fiches (CAR) réussi ; lot de 154 fiches soumis (msgbatch_014L4teTsJAY3oBSZvVHdT16, suivi dans `batchs_fiches.json`, mode pec). Récupération : `pec_recuperer` au passage suivant.
- 151 fiches rejetées avec erreurs de forme restent exclues : T4 les reprend en entier avec priseEnCharge (`--inclure-rejets` les ajouterait).

## 24.11 11:50 — Reprise sur l'abonnement (décision de Vial 11:23 : « puise dans l'abonnement, renouvelé dans 48 h »)
- API en pause (V2 bloquée) jusqu'au nouveau crédit ; coût réel vague 1 ≈ 155 USD / 192 (lots batch non comptés dans depense.json).
- Fusionné sur main : veille examen fédéral (veille/, conception/prototypes/veille, commun/suivi.js) ; vague 1 auditée (40 pathologies, ≈ 0,4 % d'erreur, rapport projets/4_Jeux_45_Spec/AUDIT_VAGUE1.md).
- Arène 45 allégée : corrections par pathologie chargées à la demande (decks/<SPEC>/<id>.json).
- Reste vague 1 : 5 corrections à régénérer (E11.9, I49.5, I75.0, E87.6, B18.9).
- Agents en cours : 45 Spec PSY, NEU, INF, PED (branches agent/45spec-*), Tétrade (agent/tetrade-arene, -3d, -sys-*).
- Skills des agents : 1, 2, 4, 5, 7, 8 + medical-accuracy-100 ; 3 et 6 ajoutés par message à 11:50. Issue GitHub #30 (fausse alerte veille) à fermer par Vial.

## 24.11 13:20 — Ronde abonnement
- Tétrade : 5 branches auditées (lot 4) fusionnées → jauge 94 %.
- 45 Spec : classement par rendement (scripts/classer_rendement.py, RANG_RENDEMENT.json, groupes A/B/C/D) ; file API repointée sur --groupe A --max 400 (en pause jusqu'au crédit de jeudi).
- Défaut connu : une pathologie fusionnée sur branche change d'id et perd son rang ; corrigé sur agent/45spec-INF (meilleur rang des portes) → à reporter sur main à la fusion, puis relancer classer_rendement.py.
- Agents en cours : PSY, NEU, INF (production), agent/45spec-A (groupe A des autres spécialités), auditeur des 4 branches (AUDIT_AGENTS_1.md) ; PED réorienté (reste B/C/D seulement).
- Décisions en attente de Vial : catalogue pédiatrique (6 pathologies majeures absentes en version enfant) ; deuil/divorce partagés ; F30.1 monographique.
- Défaut connu : une pathologie fusionnée sur branche change d'id et perd son rang ; corrigé sur agent/45spec-INF (meilleur rang des portes) → à reporter sur main à la fusion, puis relancer classer_rendement.py.
- Agents en cours : PSY, NEU, INF (production), agent/45spec-A (groupe A des autres spécialités), auditeur des 4 branches (AUDIT_AGENTS_1.md) ; PED réorienté (reste B/C/D seulement).
- Décisions en attente de Vial : catalogue pédiatrique (6 pathologies majeures absentes en version enfant) ; deuil/divorce partagés ; F30.1 monographique.

## 24.11 14:30 — Décision de Vial : production 45 Spec ralentie à 1 agent jusqu'à jeudi
- Producteur unique : agent/45spec-A, file continue (groupe A entier dans l'ordre du rang, puis B) ; il fusionne lui-même sur main après chaque lot de 3, avec contrôles (valider, menus longs, classer_rendement, arène 45). À relancer dès qu'il s'arrête.
- Agents A2, B, NEU arrêtés ; un auditeur audite leurs branches (et PSY, reprise des 5 corrections vague 1) puis fusionne lui-même sur main (AUDIT_AGENTS_2.md).
- API : groupe A en pause jusqu'au crédit de jeudi.
