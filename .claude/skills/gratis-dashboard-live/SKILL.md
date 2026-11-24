---
name: gratis-dashboard-live
description: Construit un tableau de bord de progression live, gratuit et hébergé sur GitHub (Actions + Pages), extrêmement structuré : jauges, sous-jauges, historique, branches en cours, coûts, blocages, prochaine action. S'active dès qu'on parle de suivre une progression, de jauges, de tableau de bord, de « où en est-on », d'avancement d'un projet ou de suivi en direct, même sans le mot « dashboard ».
---

# Gratis-Dashboard-live

Un tableau de bord de progression vaut par trois qualités : il dit vrai (il mesure les fichiers réels, jamais une estimation recopiée), il se met à jour seul, et il ne coûte rien. Ce skill le bâtit sur GitHub, sans serveur ni modèle payant : un robot GitHub Actions mesure le dépôt, écrit des JSON, et une page statique servie par GitHub Pages les affiche.

## 1. Architecture (0 token, 0 franc)
- **Mesure** : `outils/mesurer.py` lit le dépôt (fichiers, statuts d'audit, files de tâches, branches) et écrit `tableau/donnees/*.json`. Chaque chiffre porte sa règle de calcul et le fichier qui le prouve.
- **Robot** : `.github/workflows/tableau.yml`, déclenché par `schedule` (toutes les 5 à 15 minutes ; GitHub peut retarder un cron), par `push` sur les chemins mesurés et par `workflow_dispatch`. Il commite les JSON avec `[skip ci]` pour ne pas boucler.
- **Affichage** : `tableau/index.html`, page statique qui lit les JSON par `fetch` et se rafraîchit seule (toutes les 60 s). Publication par GitHub Pages (dossier `/tableau` ou branche `gh-pages`) ; dépôt public requis pour Pages gratuit, sinon proposer l'artifact Claude ou Cloudflare Pages.
- **Historique** : `tableau/donnees/historique.jsonl`, une ligne par mesure quand une valeur change, pour tracer les courbes.

## 2. Niveau de détail attendu (coque → centre)
1. **Bandeau** : verdict en une phrase verbale, jauge globale, date de dernière mesure (et alerte si elle date de plus d'une heure : le robot est en panne).
2. **Un bloc par chantier** : jauge, critères pondérés (fait / cible / poids, cliquables vers la règle et les fichiers), tendance sur 24 h et 7 jours, vitesse et date d'achèvement projetée (régression linéaire simple sur l'historique, expliquée en infobulle).
3. **Grille fine** : sous-unités × groupes (ex. spécialités × groupes de rendement), cellules colorées par taux, total en marge.
4. **Travail en cours** : branches ouvertes, dernier commit, éléments produits non encore fusionnés, file de tâches et état.
5. **Coûts** : dépense par source, plafond, reste ; mettre en évidence ce que le compteur ne voit pas.
6. **Blocages et décisions en attente** : liste courte, avec qui peut débloquer.
7. **Journal** : 20 derniers événements (fusion, audit, échec de workflow).

## 3. Règles de présentation
Police Atkinson Hyperlegible pour le texte, fond clair (bleu ciel par défaut), colonne contenue avec sommaire latéral numéroté, couleurs douces et accessibles (relais `color-theme-graphic-expert`), graphiques en canvas sans SVG décoratif, chaque chiffre expliqué en infobulle, phrases verbales. Jamais de contenu confidentiel (questions d'examen, secrets) dans les JSON publiés.

## 4. Vérifier avant d'annoncer
1. Lancer `mesurer.py` en local et comparer deux chiffres au décompte manuel des fichiers.
2. Déclencher le workflow (`gh workflow run`) et lire son journal : succès et commit des JSON.
3. Ouvrir la page (Playwright sans écran) : 0 erreur JS, capture lue.
4. Donner l'URL publique et dire à quelle fréquence elle se met à jour.

## 5. Si GitHub Pages n'est pas possible
Proposer, dans cet ordre : publier `index.html` comme artifact Claude republié à chaque ronde ; Cloudflare Pages relié au dépôt (gratuit, dépôt privé accepté) ; à défaut, `JAUGES.md` rendu par GitHub.

Relais : `pipeline-autonomous-builder` (workflow), `dataviz` (forme des graphiques), `harness-for-long` (rondes qui lisent le tableau).

Signature : AAI (Anthropic AI)
