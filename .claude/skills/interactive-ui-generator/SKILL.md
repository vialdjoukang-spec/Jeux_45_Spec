---
name: interactive-ui-generator
description: Construit et tient à jour un écran temps réel ÉPINGLÉ dans la discussion (artefact « Data » + base partagée) qui montre pourcentages, agents (nom, périmètre, statut) et circulation des fichiers d'un chantier multi-agents. S'active dès qu'on demande un tableau de bord dynamique, un écran en direct, « voir les agents travailler », le suivi temps réel d'un chantier, ou une interface interactive qui doit rester ouverte à côté du chat.
---

# Interactive-ui-generator

Vial veut **voir** le chantier bouger : les pourcentages qui évoluent, les agents par leur nom, les fichiers qui circulent, sur un écran fixé à côté de la discussion. Une page statique ou un tableau de bord GitHub Pages rafraîchi toutes les 10 minutes ne suffit pas (retour du 27.11.2026 : « i really mean it »). Ce skill donne l'écran vivant ; `gratis-dashboard-live` reste le suivi public, gratuit et durable sur GitHub.

## 1. Architecture (pourquoi elle est vivante)
- **Artefact du type « Data »** (quickstart `intent: "other"`, puis publication avec son `type_url`, `title`, `auto_open: "after_first_write"`). La page est dans le document `files/index.html` de sa base, jamais publiée en fichier.
- **Quatre jeux de données en lignes sauvegardées** (`source: {kind: "store", path}`), lus en direct par la page :
  `data/live/jauges` (quoi, fait, cible, poids, règle) · `data/live/agents` (nom, périmètre, statut, produit) · `data/live/flux` (heure, agent, cible, fichiers, commit, quoi) · `data/live/matrices` (unités de travail).
- **L'orchestrateur écrit** ces lignes avec `ArtifactData` à chaque événement ; la page redessine aussitôt chez tous ceux qui l'ont ouverte. C'est l'écriture, pas un minuteur, qui rend l'écran temps réel : aucun robot ne peut écrire dans la base à ta place.
- **Épingler** : `Artifact action: "pin"` (barre latérale) puis `action: "open"` (panneau à côté du chat), seulement si l'utilisateur l'a demandé.

## 2. Construire (première fois)
1. Lis les fichiers de référence du type (`features.md` § Saved rows, `one-writer.md`, `design-defaults.md`) avec `Artifact action: "read"` et `paths` : la page obéit à la règle « un écrivain par partie » (`<meta name="dash-one-writer">`, éléments `data-draw` vides, marques `data-source`/`data-field`).
2. Pars du modèle `ecran_modele.html` (en-tête avec phrase et grand pourcentage, jauges, tableau des agents, flux des commits, unités). Le pourcentage est un `dash.calc` pondéré, jamais un chiffre tapé.
3. Tiens un registre JSON (jauges, agents, unités) et génère les écritures :
   `python3 .claude/skills/interactive-ui-generator/scripts/generer_ecran.py --registre REG.json --depuis <commit> --sortie DOSSIER --page ecran_modele.html`
   puis passe chaque `writes_N.json` à `ArtifactData action: "batch"` (50 écritures au plus par appel).
4. Lis `data/users/me/check` puis `runs` : `passed` ou un défaut à corriger. Absent, personne n'a la page ouverte : ouvre-la (`open`) et relis.

## 3. Tenir à jour (à chaque événement, sans attendre qu'on le demande)
| Événement | Écriture |
|---|---|
| agent lancé | `data/live/agents/<id>` statut `en_cours` |
| agent rendu | statut `termine`, `produit` chiffré (fiches, moyens, défauts) |
| commit poussé | une ligne `data/live/flux/<nnn>` (relance le script sans `--page`) |
| audit relancé | jauges `fait` mises à jour |
Un `update` sur un document existant exige `if_version` (la version lue ou rendue par la dernière écriture). Un lot refusé n'écrit rien : relis, puis réécris.

## 4. Couleurs et lisibilité (choix de Vial, non négociables)
- Titres, libellés, en-têtes de colonnes : **rouge** (`#b91c1c` clair, `#f87171` sombre), pour les repérer d'un coup d'œil.
- Texte et valeurs : **bleu** (`#1d4ed8` clair, `#93c5fd` sombre).
- Infobulles : **encre blanche pure sur fond sombre** (`#111827`), posées dans le dessin (`position: absolute`), jamais `title`.
- Statuts en pastilles : vert terminé, ambre en cours, gris à faire. Atkinson Hyperlegible ou la police du type ; 400 px de large sans défilement horizontal.
- Le chat reste minimal : l'écran porte le détail.

## 5. Pièges
- Si tu écris hors d'un élément `data-draw` depuis un script → défaut « one-writer » : place les infobulles dans le dessin lui-même.
- Si tu recopies des lignes d'un connecteur dans la base → elles survivent aux droits du lecteur : ici, seules des métadonnées de chantier (comptes, noms d'agents, commits) y vont, jamais de contenu médical ni de secret.
- Si tu annonces « temps réel » sans écrire à chaque événement → l'écran ment : l'heure du dernier flux le montre.
- Outils GitHub repérés (non retenus, à tester seulement sur une machine locale) : `DG-Elom/orchestra-live`, `paxon-yang/claude-agent-tools`, `XXX1694/Vanguard` ; ils lisent les sessions locales de Claude Code et ne s'épinglent pas dans la discussion.

Relais : `gratis-dashboard-live` (suivi public GitHub), `dataviz` (forme des graphiques), `agentic-hurican` (vagues d'agents dont l'écran montre la circulation).

Signature : AAI (Anthropic AI)
