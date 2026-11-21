# REPRISE — à lire en entier avant toute action

Dernière mise à jour : 2026-11-21 · Commit de référence : 985ab5d puis celui qui ajoute ce fichier.
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
- Un système déroule **TOUS** ses organes (14 systèmes, 123 organes). Jamais un système réduit à un organe.
- Clic sur un organe → contenu de l'espace actif :
  - Anatomie : macroscopie, microscopie, vascularisation, innervation (+ rapports et projections, embryologie et variantes), en arbre propre ; chaque mot-clé ouvre une **image 3D** de la structure.
  - Physiologie : paramètres du simple au complexe ; chaque mot-clé ouvre une **courbe calculée**, un tracé ou un calculateur (`fenetres.js` : odc, hh, alveolaire, gazometrie, spiro, 3d). Unités SI en kPa ; altitude (La Chaux-de-Fonds ≈ 1000 m).
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

## 8. État au 2026-11-21
- Rédigés : cœur (anatomie), poumon (physiologie, 5 courbes), circuit sémiologique de l'insuffisance cardiaque gauche, pneumonie (cliché + radio-anatomie normale).
- 121 organes « à produire » (`aProduire`), listés mais vides.
- Catalogue paraclinique : 66 organes, 601 examens listés (champs à remplir).

## 9. Méthode convenue pour la suite
1. Système par système (cardiovasculaire, puis respiratoire) : proposer la liste des organes, les volets adaptés et les fenêtres de courbes à créer (ex. ECG, Frank-Starling, boucle pression-volume, clairance/DFG, potentiel d'action, axes hormonaux).
2. Attendre la validation de Vial.
3. Produire le contenu ; audit bloquant après chaque lot ; commit et push.

## 10. En attente
- Pilote Jeux_45_Spec : `python scripts/produire_fiches_claude.py pilote --spec CAR --n 2` (schéma `scripts/schema_fiche.json` : `glossaire` et `examens.items.visee` obligatoires). Vial envoie les 2 fiches pour audit.
- Le skill `obsidian-like-complex-network` du compte de Vial décrit encore des liens courbes : proposer sa mise à jour depuis la copie du dépôt (`skills/obsidian-like-complex-network/`).

## 11. Façon de répondre à Vial
- Réponse directe et brève ; vérité sans complaisance ; critique constructive et un « plus » à chaque proposition.
- Solution la plus économique et efficace proposée une fois, en GRAS MAJUSCULE et en couleur.
- Contenu à apprendre : de la coque vers le centre, avec le pourquoi.
- Commandes de terminal : une seule par bloc, avec son but entre parenthèses.
