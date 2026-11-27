# Veille : front statique et IA médicales spécialisées

**Objet** : le site de révision de biologie médicale (sélection de pathologies → bilan biologique, fiches à 3 temps, posologies AIPS), statique, gratuit, hébergé sur GitHub Pages.
**Date de vérification** : 27.11.2026.
**Skills chargés** : `anthropic-skills:web-aesthetic-github-toolkit`, `anthropic-skills:github-skills-novelty-finder-expert`, `medical-accuracy-100`.

**Méthode et limites**
- J'ai pris les étoiles, la licence et la date du dernier *push* avec `gh api -X GET search/repositories -f q='repo:…'`. La session bloque l'endpoint `repos/…`. Les dernières versions viennent du registre npm (`registry.npmjs.org`), avec leur date de publication.
- J'ai vérifié les IA avec WebSearch. WebFetch est bloqué par le réseau de la session : je n'ai donc ouvert directement aucune page d'éditeur. Je marque « à vérifier » toute donnée qui ne repose que sur une page d'éditeur ou d'un concurrent.

---

## 1. Outils GitHub pour le front

### 1.1 Constats qui changent les recommandations habituelles
- **Pico CSS est archivé.** Son README indique que la v2.1.1 est la dernière version et que le dépôt n'accepte plus d'issues, de PR ni de versions. Le CDN et le site restent en ligne ([picocss/pico](https://github.com/picocss/pico)). Il ne faut donc pas l'adopter pour un nouveau site, même si le skill `web-aesthetic-github-toolkit` le recommande encore.
- **Animate.css** n'est pas sous licence MIT. Son fichier LICENSE est la *Hippocratic License 2.1*, une licence éthique non approuvée par l'OSI ([LICENSE](https://github.com/animate-css/animate.css/blob/main/LICENSE)). Elle échoue au critère de licence du skill `github-skills-novelty-finder-expert` : il vaut mieux l'écarter.
- **Tippy.js** est archivé. Son auteur le remplace par **Floating UI**.
- **Shoelace** est archivé. Il est devenu **Web Awesome**.
- **Eleventy** a changé de nom : le dépôt s'appelle désormais `11ty/buildawesome` (« Build Awesome (Eleventy) »). La version stable reste `@11ty/eleventy` 3.1.8. Le nouveau paquet `@awesome.me/buildawesome` n'existe qu'en 0.0.3, avec une 4.0.0-alpha.12.
- Le dépôt construit déjà le site en Python (`conception/outils/paraclinique/construire_site_biologie.py`). Un générateur de site statique n'est donc **pas indispensable**. Les bibliothèques ci-dessous se copient telles quelles dans `assets/`, sans étape de build Node.

### 1.2 Inventaire vérifié

| Outil | Rôle précis dans CE site | ★ | Dernière version (date) | Licence | Activité | Verdict | Lien |
|---|---|---|---|---|---|---|---|
| **Pagefind** | Recherche plein texte sur les milliers de fiches HTML générées. L'index est découpé en fragments, et le navigateur ne charge que les fragments utiles (moins de 300 kB pour 10 000 pages selon la doc). Une interface web-component est fournie. | 5 586 | 1.6.0 (01.11.2026) | MIT | push 26.11.2026 | 🟩 | [Pagefind/pagefind](https://github.com/Pagefind/pagefind) |
| **Fuse.js** | Recherche floue dans le **sélecteur de pathologies**, sur un petit JSON en mémoire. Elle tolère les fautes (« hypokaliemie », « Addisson ») et pondère les champs nom, synonymes et système. | 20 539 | 7.5.0 (13.07.2026) | Apache-2.0 | push 24.11.2026 | 🟩 | [krisk/Fuse](https://github.com/krisk/Fuse) |
| MiniSearch | Alternative à Fuse : index inversé, préfixes et flou, plus rapide au-delà de quelques milliers d'entrées | 6 213 | 7.2.0 (16.09.2025) | MIT | push 16.09.2025 | 🟧 (peu actif depuis 14 mois) | [lucaong/minisearch](https://github.com/lucaong/minisearch) |
| FlexSearch | Recherche plein texte très rapide côté client | 13 822 | 0.8.212 (06.09.2025) | Apache-2.0 | push 28.06.2026 | 🟧 (API complexe, toujours en 0.x) | [nextapps-de/flexsearch](https://github.com/nextapps-de/flexsearch) |
| uFuzzy | Recherche floue minuscule pour des listes courtes | 3 045 | — | MIT | push 08.09.2026 | 🟧 | [leeoniya/uFuzzy](https://github.com/leeoniya/uFuzzy) |
| Lunr.js | Ancien standard de la recherche statique | 9 198 | — | MIT | push 31.07.2024 | 🟥 (inactif) | [olivernn/lunr.js](https://github.com/olivernn/lunr.js) |
| **Cytoscape.js** | **Graphe de type Obsidian** pathologie ↔ analyses ↔ mécanismes. Il offre des layouts riches, des sélecteurs de style et des événements de clic qui ouvrent une fiche. Il tient sans peine quelques milliers de nœuds. | 11 313 | 3.35.0 (10.11.2026) | MIT | push 10.11.2026 | 🟩 | [cytoscape/cytoscape.js](https://github.com/cytoscape/cytoscape.js) |
| Sigma.js (+ graphology) | Graphe en WebGL pour plus de 10 000 nœuds, quand le réseau complet devient trop lourd pour Cytoscape | 12 255 / 1 774 | 4.0.6 (10.11.2026) / 0.26.0 | MIT | push 10.11.2026 | 🟩 (réserve) | [jacomyal/sigma.js](https://github.com/jacomyal/sigma.js) · [graphology](https://github.com/graphology/graphology) |
| force-graph | Graphe force 2D sur canvas, le plus proche du rendu Obsidian, avec très peu de code | 2 175 | 1.52.1 (27.11.2026) | MIT | push 27.11.2026 | 🟩 (alternative simple) | [vasturiano/force-graph](https://github.com/vasturiano/force-graph) |
| **Open Props** | Variables CSS (couleurs, espacements, ombres, rayons, easings) surchargées dans un seul `:root` pour appliquer la charte de Vial | 5 588 | 1.7.23 (31.01.2026) | MIT | push 11.10.2026 | 🟩 | [argyleink/open-props](https://github.com/argyleink/open-props) |
| Tufte CSS | Fiches longues avec notes en marge (temps 2 et 3 des fiches) | 6 597 | 1.9.0 (25.06.2026) | MIT | push 24.06.2026 | 🟩 (option) | [edwardtufte/tufte-css](https://github.com/edwardtufte/tufte-css) |
| Pico CSS | Base classless | 16 805 | 2.1.1 (15.03.2025, **finale**) | MIT | **archivé** | 🟥 | [picocss/pico](https://github.com/picocss/pico) |
| Tabler | Tableau de progression du joueur (cartes, jauges) | 42 143 | @tabler/core 1.7.5 (12.11.2026) | MIT | push 27.11.2026 | 🟧 (lourd pour ce site) | [tabler/tabler](https://github.com/tabler/tabler) |
| **Floating UI** | Infobulles accessibles (seuils, définitions) positionnées sans débordement sur mobile | 32 826 | @floating-ui/dom 1.8.0 (11.07.2026) | MIT | push 12.11.2026 | 🟩 | [floating-ui/floating-ui](https://github.com/floating-ui/floating-ui) |
| a11y-dialog | Fenêtres modales accessibles (focus piégé, Échap, `aria-*`) autour de `<dialog>` | 2 490 | 8.1.5 (06.02.2026) | MIT | push 23.11.2026 | 🟩 | [KittyGiraudel/a11y-dialog](https://github.com/KittyGiraudel/a11y-dialog) |
| Web Awesome (ex-Shoelace) | Composants web complets (onglets, arbres, combobox) sans framework | 1 415 | 3.15.0 (17.11.2026) | MIT (cœur) | push 24.11.2026 | 🟧 (gros si l'on n'utilise que 3 composants) | [shoelace-style/webawesome](https://github.com/shoelace-style/webawesome) |
| CSS anchor positioning polyfill | Fait marcher l'API native d'ancrage CSS (infobulles sans JS) dans les navigateurs en retard | 491 | 0.10.2 (18.08.2026) | BSD-3-Clause | push 23.11.2026 | 🟧 | [oddbird/css-anchor-positioning](https://github.com/oddbird/css-anchor-positioning) |
| Alpine.js | État léger de l'interface (pathologies cochées, temps 1/2/3 révélés) écrit dans le HTML | 32 043 | 3.17.5 (20.10.2026) | MIT | push 04.11.2026 | 🟩 (option) | [alpinejs/alpine](https://github.com/alpinejs/alpine) |
| Motion | Animations sobres (apparition d'une fiche, retour juste/faux) qui respectent `prefers-reduced-motion` | 35 631 | 14.14.0 (13.11.2026) | MIT | push 26.11.2026 | 🟧 (le CSS natif et les View Transitions suffisent souvent) | [motiondivision/motion](https://github.com/motiondivision/motion) |
| anime.js | Animation JS (timelines) | 75 127 | 4.5.0 (22.06.2026) | MIT | push 02.11.2026 | 🟧 | [juliangarnier/anime](https://github.com/juliangarnier/anime) |
| Animate.css | Classes d'animation | 83 074 | — | **Hippocratic 2.1** | push 29.07.2024 | 🟥 | [animate-css/animate.css](https://github.com/animate-css/animate.css) |
| swup | Transitions de page sur un site multipage | 5 257 | — | MIT | push 03.11.2026 | 🟧 | [swup/swup](https://github.com/swup/swup) |
| Eleventy / Build Awesome | Générateur statique piloté par les données : une page par entrée JSON (*pagination*), sans framework client | 20 065 | @11ty/eleventy 3.1.8 (03.11.2026) | MIT | push 27.11.2026 | 🟩 (si l'on remplace le générateur Python) | [11ty/buildawesome](https://github.com/11ty/buildawesome) |
| Astro (+ Starlight) | Générateur orienté contenu (*content collections* typées, îlots JS) | 64 260 | astro 7.4.13 (18.11.2026) ; @astrojs/starlight 0.43.2 | MIT (LICENSE ; GitHub affiche NOASSERTION) | push 27.11.2026 | 🟧 (plus lourd qu'Eleventy pour ce besoin) | [withastro/astro](https://github.com/withastro/astro) |
| Hugo | Générateur en Go, le plus rapide sur des dizaines de milliers de pages | 90 583 | hugo-bin 0.167.0 | Apache-2.0 | push 27.11.2026 | 🟧 (gabarits Go moins lisibles) | [gohugoio/hugo](https://github.com/gohugoio/hugo) |
| **Playwright** | Tests visuels (`toHaveScreenshot`) à 380 px et à 1280 px, parcours du jeu, contrôle de la console | 101 182 | @playwright/test 1.65.1 (13.11.2026) | Apache-2.0 | push 27.11.2026 | 🟩 | [microsoft/playwright](https://github.com/microsoft/playwright) |
| **axe-core** (+ @axe-core/playwright) | Audit d'accessibilité automatique (contraste AA, rôles, libellés) dans les tests Playwright | 7 894 | 4.14.1 (16.11.2026 / 24.11.2026) | MPL-2.0 | push 25.11.2026 | 🟩 | [dequelabs/axe-core](https://github.com/dequelabs/axe-core) |
| Lighthouse CI | Budget de performance et d'accessibilité dans GitHub Actions | 7 165 | @lhci/cli 0.16.1 (11.11.2026) | Apache-2.0 | push 17.11.2026 | 🟧 (option) | [GoogleChrome/lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci) |
| reg-suit | Comparaison visuelle d'images en CI | 1 310 | — | MIT | push 25.11.2026 | 🟧 (Playwright suffit) | [reg-viz/reg-suit](https://github.com/reg-viz/reg-suit) |
| htmx | Interactions via le serveur | 49 664 | 2.0.11 | 0BSD | push 20.11.2026 | 🟥 (inutile sur un site sans serveur) | [bigskysoftware/htmx](https://github.com/bigskysoftware/htmx) |

### 1.3 Pile recommandée (7 outils, tous gratuits et compatibles GitHub Pages)
1. **Open Props** sert de base de variables, complétée d'une feuille CSS maison aux couleurs de la charte de Vial (Atkinson Hyperlegible, fonds clairs). Il remplace Pico, archivé, sans imposer de design.
2. **Fuse.js** alimente le sélecteur de pathologies : il tolère les fautes et pondère les champs, et la liste reste petite et en mémoire.
3. **Pagefind** cherche dans tout le site. Son index fragmenté tient des milliers de fiches sans charger un gros JSON, et l'index se génère après le build Python (`npx pagefind --site site/`).
4. **Cytoscape.js** dessine le graphe pathologie ↔ analyses, à la manière d'Obsidian. Il est mûr et sous licence MIT, et ses layouts et styles conviennent aux réseaux sémantiques. Sigma.js prend le relais seulement si le graphe complet dépasse environ 10 000 nœuds.
5. **Floating UI** gère les infobulles et **a11y-dialog** les fenêtres : on obtient ainsi un squelette minimal, avec le détail en infobulle et le développement en fenêtre, accessible au clavier.
6. **Playwright** et **@axe-core/playwright** vérifient chaque version : captures à 380 px et à 1280 px, zéro erreur console, contraste AA.
7. Le **générateur Python existant** reste en place. On ne passe à **Eleventy 3.x** que s'il devient difficile à maintenir, car sa pagination « une page par objet JSON » correspond exactement au besoin.

Pour l'animation, je n'ajoute aucune bibliothèque : CSS natif, `@starting-style` et View Transitions suffisent, sous `prefers-reduced-motion`. Motion n'entre en jeu que si le besoin le justifie.

---

## 2. Skills

### 2.1 Skills disponibles dans cette session et utiles au front (noms exacts)

| Skill | Usage pour ce site |
|---|---|
| `anthropic-skills:web-aesthetic-github-toolkit` | Choisir la base CSS et plier les outils à la charte de Vial. **Il cite encore Pico et Animate.css : voir §1.1.** |
| `anthropic-skills:web-designer-pilot-faithful` | Direction visuelle fidèle à la charte |
| `anthropic-skills:web-artifacts-builder` | Prototypes multi-composants (React, Tailwind, shadcn) en artefact claude.ai |
| `dataviz` | Courbes, jauges, couleurs de séries (cinétiques, valeurs de référence) |
| `artifact-design` | Contrat de page et thème clair/sombre des artefacts |
| `artifact-diagramming` | Schémas de mécanismes inline lisibles (interface seulement, pas d'anatomie en SVG) |
| `artifact-capabilities` | Pages publiées qui gardent un état (progression partagée) |
| `anthropic-skills:artifact-emulator` | Voir un artefact comme l'utilisateur (Playwright) |
| `anthropic-skills:obsidian-like-complex-network` | Graphe de notions façon Obsidian |
| `anthropic-skills:obsidian-like-data-mode` | Données du graphe (nœuds, liens) |
| `gratis-dashboard-live` / `anthropic-skills:gratis-dashboard-live` | Tableau de progression gratuit (Actions et Pages) |
| `interactive-ui-generator` | Écran temps réel épinglé pour suivre le chantier |
| `run` | Lancer le site en local et le capturer |
| `anthropic-skills:github-skills-novelty-finder-expert` | Évaluer et empaqueter un nouvel outil |
| `anthropic-skills:panoramic-skill-finder`, `perfect-skill-user-organizer-collector` | Brancher et ranger les skills sans doublon |
| `anthropic-skills:french-language-best-writer` | Microcopie française de l'interface |
| `medical-workout`, `concept-corelator`, `medical-accuracy-100` | Contenu des fiches (catalogue d'examens, corrélations, sources) |
| `code-review`, `simplify`, `security-review` | Revue du code du site |

### 2.2 Skills manquants et où les trouver (liens vérifiés le 27.11.2026)

| Skill manquant | Pourquoi | Où |
|---|---|---|
| `frontend-design` | Direction esthétique : typographie, refus des gabarits génériques. **Le skill `web-aesthetic-github-toolkit` y renvoie alors qu'il n'est pas installé.** | [anthropics/skills · skills/frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) |
| `webapp-testing` | Tests Playwright d'une application locale : captures, logs console | [anthropics/skills · skills/webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) |
| `theme-factory` | Thèmes de couleurs et de polices appliqués à une page | [anthropics/skills · skills/theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory) |
| Audit d'accessibilité (axe-core) | Aucun skill dédié trouvé. Il faudrait **le créer** (`skill-creator`) sur la base `@axe-core/playwright`. | — |
| Recherche statique (Pagefind/Fuse) | Aucun skill trouvé : à créer après un premier essai réel | — |
| *UI/UX Pro Max* (communautaire) | « Design intelligence » UI/UX, MIT, 154 969 ★. Il faut **lire le code avant usage** : popularité soudaine, risque de bruit. | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) |

Catalogues pour chercher plus loin :
- [anthropics/skills](https://github.com/anthropics/skills) : 201 337 ★, skills officiels. Chaque skill porte ses propres termes de licence (`LICENSE.txt`).
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) : MIT, 37 589 ★.
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) : 80 444 ★, sans licence déclarée.
- [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) : 15 956 ★.
- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) : 58 920 ★.

---

## 3. IA spécialisées (biologie clinique, interprétation, diagnostic différentiel, posologie)

**Règle « sources suisses d'abord »** (`medical-accuracy-100`) : aucune de ces IA n'est une source suisse. AMBOSS AI Mode dit s'appuyer sur des « selected US guidelines ». Les autres sont américaines ou britanniques. Elles servent donc à **explorer** (diagnostic différentiel, explication, recherche bibliographique), **jamais** à fixer une posologie ou un seuil. La posologie vient de l'information professionnelle Swissmedic, et les analyses de la Liste des analyses de l'OFSP.

### 3.1 Tableau (vérifié le 27.11.2026)

| Nom | Spécialité | Force | Limite | Accès en Suisse / prix | Lien |
|---|---|---|---|---|---|
| **AMBOSS AI Mode (LiSA)** | Questions cliniques et apprentissage (*AI Mode Learning*, lancé en février 2026) | Recherche sur un contenu curé (base AMBOSS, recommandations, médicaments). Selon AMBOSS, elle arrive 1re (F1 86,15 %) au benchmark NOHARM Stanford–Harvard (ARISE), devant OpenEvidence, Doximity et Glass. AMBOSS dit ne pas avoir financé l'étude. | Le classement vient du communiqué AMBOSS (juillet 2026), qui cite une version révisée **non vérifiée** du preprint [arXiv:2512.01241](https://arxiv.org/abs/2512.01241). Recommandations surtout américaines. Fonctions qui « peuvent différer selon le pays ». | AI Mode inclus dans l'abonnement selon AMBOSS. Boutique allemande : 25 €/mois ou 198 €/an pour un médecin. **Prix en CHF et disponibilité du mode clinique en Suisse : à vérifier.** | [amboss.com/int/clinical-ai-mode](https://www.amboss.com/int/clinical-ai-mode) |
| **OpenEvidence** | Réponses cliniques sourcées sur la littérature | Très utilisée aux États-Unis. Partenariat avec Anthropic annoncé en septembre 2026 (Reuters) pour une diffusion mondiale. | Plusieurs sources secondaires concordent : **retrait de l'UE et du Royaume-Uni les 27–28.04.2026** (incertitude liée à l'AI Act), avec géoblocage. Je n'ai trouvé aucun communiqué primaire. Le *NPI* américain est requis pour la vérification. | **Suisse : à vérifier.** Un concurrent (drinfo.ai) écrit que la Suisse ne figure pas dans la liste d'exclusion, sans confirmation pratique. Gratuit pour les cliniciens américains vérifiés. | [openevidence.com](https://www.openevidence.com) |
| **Isabel DDx Companion** | Générateur de diagnostic différentiel (DDSS) | Outil dédié au diagnostic différentiel depuis plus de 20 ans, distribué par EBSCO. Essai gratuit de 30 jours. | Les 96 % de « top-10 accuracy » sont une **affirmation de l'éditeur**. Aucune validation indépendante de 2026 trouvée. Ce n'est pas un moteur de recommandations. | Individuel : 149 $/an ou **139 € TTC/an** (pages non datées, à vérifier). Vente en € ouverte à l'Europe. Suisse : probable, à vérifier. | [isabelhealthcare.com](https://www.isabelhealthcare.com/products) |
| **Glass Health** | Diagnostic différentiel classé et plan de prise en charge à partir d'un cas | Pensé pour le raisonnement clinique : il produit diagnostic différentiel, examens et plan. | Outil de conseil, non autorisé par la FDA comme dispositif diagnostique. Tarifs incohérents entre sources (Pro 90 $, Max 200 $ : non vérifiés). | Gratuit pour les cliniciens américains vérifiés par NPI. **Accès hors États-Unis : à vérifier** (aucune source trouvée). | [glass.health](https://glass.health) |
| **UpToDate Expert AI** | IA générative sur le contenu UpToDate | Contenu expert relu. Chaque réponse montre ses hypothèses, sa source et son raisonnement. Lancement annoncé le 24.09.2025. | **Aucun pays européen cité.** Accès individuel aux États-Unis et au Canada (Pro Plus). Ailleurs, accès Enterprise dans quelques pays (Australie, Canada, Hong Kong, Corée…). | **Suisse : non disponible à titre individuel selon les pages consultées.** Accès institutionnel (hôpital universitaire) à vérifier. | [wolterskluwer.com · UpToDate Expert AI](https://www.wolterskluwer.com/en/solutions/uptodate/uptodate-expert-ai) |
| **DynaMedex · Dyna AI** | IA (RAG) sur DynaMed et Micromedex (médicaments) | Couple maladie et médicament (posologie, sécurité, extension prévue début 2026). *Dyna AI Mode* lancé le 11.02.2026. | Option payante. Commercialisée aux États-Unis, **non disponible dans l'UE** selon le communiqué de décembre 2025. Posologies américaines. | **Suisse : à vérifier.** Essai limité pour les cliniciens américains. | [EBSCO · Dyna AI Mode](https://about.ebsco.com/news-center/press-releases/ebsco-clinical-decisions-launches-dyna-ai-mode) |
| **DR.INFO** (Synduct, Munich) | Recherche clinique sourcée, positionnée sur l'Europe | Se déclare **marquée CE (MDR, classe I)** et hébergée dans l'UE. Pilote Cureus 2026 (n = 29) cité par un tiers. | Le marquage CE et l'étude ne sont confirmés que par l'éditeur ou un concurrent : **à vérifier sur EUDAMED**. | Europe. Suisse et prix : à vérifier. | [iatrox.com · revue DR.INFO](https://www.iatrox.com/blog/dr-info-ai-review) (secondaire) |
| **Consensus** (Medical Mode) | Recherche dans la littérature évaluée par les pairs | Le *Medical Mode* filtre environ 50 000 recommandations et 8 millions d'articles de grandes revues. **Déjà connecté à cette session (MCP `Consensus`).** | Il ne remplace pas une recommandation suisse. Tarifs incohérents entre agrégateurs (Pro de 10 à 20 $/mois). | Web, accessible depuis la Suisse. Prix exact : voir consensus.app/pricing. | [consensus.app](https://consensus.app/home/features/medical-ooh/) |
| **Elicit** | Revue de littérature, extraction de données, revues systématiques | Extraction structurée sur des articles et des essais. **Déjà connecté à cette session (MCP `Elicit`).** | Littérature seulement, pas de posologie. Tarifs 2026 changeants (un plan supprimé en septembre 2026 selon CostBench). | Web, accessible depuis la Suisse. Prix : voir elicit.com/pricing. | [elicit.com](https://elicit.com) |
| Lab Tests Online | Explication grand public des analyses | — | **Le site n'existe plus sous ce nom** : il est devenu Testing.com le 09.11.2021 (OneCare Media) et vend des tests aux consommateurs américains. Contenu orienté patient et États-Unis. | Gratuit, mais **non recommandé comme source** du jeu | [testing.com/about-us](https://www.testing.com/about-us/) |
| BMJ Best Practice | Aide à la décision | Contenu structuré. Utilisé par Google DeepMind (AMIE) pour évaluer une IA. | **Aucune IA générative pour les utilisateurs vérifiée.** BMJ publie surtout des comparatifs à son avantage. | Abonnement (prix non vérifié) | [bestpractice.bmj.com](https://bestpractice.bmj.com/info/blog/) |

### 3.2 Sources suisses (ce ne sont pas des IA, mais elles priment)

| Source | Rôle dans le jeu | Statut vérifié | Lien |
|---|---|---|---|
| **swissmedicinfo-pro.ch** / swissmedicinfo.ch | Information professionnelle officielle des médicaments : **posologies AIPS** | Le manuel Refdata AIPS v1.5 (28.02.2026) cite ces deux adresses. Une notice HPC de Swissmedic annonce une plateforme centrale depuis le 01.11.2026, mais la même page porte la mention « fiktives Beispiel, erstellt mit Hilfe von KI » : **date à vérifier**. | [swissmedic.ch · HPC](https://www.swissmedic.ch/swissmedic/fr/home/medicaments-a-usage-humain/surveillance-du-marche/health-professional-communication--hpc-/hpc-wichtige-information-von-swissmedic.html) · [Refdata AIPS](https://refdata.ch/images/SIMIS/Modul_AIPS_V1%20de.pdf) |
| **compendium.ch** (HCI Solutions, Galenica) | Compendium suisse des médicaments, gratuit pour les prestataires suisses (fiche App Store) | Galenica a présenté un « nouveau compendium » en 2026. **Aucune fonction d'IA trouvée** (non vérifiée). | [compendium.ch](https://compendium.ch/fr/news/28825) · [Galenica](https://report.galenica.com/hyr26/en?p=950) |
| **Liste des analyses (OFSP)** | Positions et remboursement des analyses du bilan biologique | Édition au 01.07.2026 (RO 2026 336). Nouvelle position 1779.00 (PlGF). Révision tarifaire transAL en cours. | [bag.admin.ch · LA](https://www.bag.admin.ch/fr/liste-des-analyses-la) |

### 3.3 Les 3 IA les plus utiles pour Vial
1. **AMBOSS AI Mode** est accessible depuis la Suisse avec un abonnement AMBOSS, en allemand et en anglais. Son contenu est curé, il est le mieux classé au benchmark NOHARM (selon l'éditeur), et son mode *Learning* colle à un jeu de révision. Il faut recouper chaque recommandation avec la source suisse.
2. **Consensus et Elicit** sont **déjà branchés dans les sessions Claude**. Les agents producteurs peuvent donc sourcer automatiquement les fiches (études, recommandations) sans coût d'intégration.
3. **Isabel DDx Companion** est un générateur de diagnostic différentiel dédié et s'achète à titre individuel en euros. Il sert à contrôler que chaque bilan « pathologie → analyses » couvre les diagnostics différentiels attendus.

OpenEvidence serait un bon candidat, mais son accès depuis la Suisse reste incertain depuis le retrait UE/UK d'avril 2026. **Pour toute posologie : swissmedicinfo-pro.ch ou compendium.ch, sans exception.**

---

## Sources
- GitHub (API `search/repositories`, 27.11.2026) : liens par outil dans les tableaux du §1. Registre npm : `https://registry.npmjs.org/<paquet>`.
- [Pico CSS README (arrêt de maintenance)](https://github.com/picocss/pico) · [Animate.css LICENSE](https://github.com/animate-css/animate.css/blob/main/LICENSE) · [Build Awesome (Eleventy)](https://github.com/11ty/buildawesome)
- [anthropics/skills](https://github.com/anthropics/skills)
- [AMBOSS clinical AI mode](https://www.amboss.com/int/clinical-ai-mode) · [AMBOSS NOHARM](https://www.amboss.com/int/int-newsroom/noharm) · [AMBOSS Preise](https://www.amboss.com/de/preise) · [arXiv:2512.01241 NOHARM](https://arxiv.org/abs/2512.01241)
- [OpenEvidence et Suisse (drinfo.ai, concurrent)](https://www.drinfo.ai/compare/openevidence-alternative-switzerland) · [Retrait UE/UK (medic24.ro)](https://medic24.ro/openevidence-has-withdrawn-from-the-european-union-and-the-united-kingdom-what-this-means-for-physicians-using-clinical-ai/) · [Anthropic–OpenEvidence (KSL/Reuters)](https://www.ksl.com/article/51627326/exclusive-anthropic-openevidence-partner-to-bring-medical-ai-worldwide)
- [Isabel pricing](https://isabelhealthcare.com/home/pricing) · [Glass Health](https://glass.health/resources/best-clinical-decision-support) · [UpToDate Expert AI (24.09.2025)](https://wolterskluwer.com/en/news/uptodate-expert-ai-genai-clinical-decision-support) · [UpToDate Expert AI (disponibilité)](https://www.wolterskluwer.com/en-gb/solutions/uptodate/uptodate-expert-ai)
- [EBSCO Dyna AI Mode](https://about.ebsco.com/news-center/press-releases/ebsco-clinical-decisions-launches-dyna-ai-mode) · [Dyna AI dosage (déc. 2025)](https://about.ebsco.com/news-center/press-releases/dyna-ai-streamline-point-care-decisions-integrated-dosing-and-medication)
- [Consensus Medical](https://consensus.app/home/features/medical-ooh/) · [Elicit (changement de tarif, CostBench)](https://costbench.com/changelog/elicit-research-plan-removed-2026-09/)
- [ADLM · Lab Tests Online](https://myadlm.org/advocacy-and-outreach/Lab-Tests-Online) · [Testing.com](https://www.testing.com/about-us/)
- [OFSP Liste des analyses](https://www.bag.admin.ch/fr/liste-des-analyses-la) · [Swissmedic HPC](https://www.swissmedic.ch/swissmedic/de/home/humanarzneimittel/marktueberwachung/health-professional-communication--hpc-/hpc-wichtige-information-von-swissmedic.html) · [compendium.ch](https://compendium.ch/fr/news/28825)
