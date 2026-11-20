# CANEVAS DE GÉNIE LOGICIEL — MedSuisse Arena 45 (version 2)

> **Statut :** exécutoire. **Lecteur :** tout agent IA chargé de produire, auditer ou affiner le jeu.
> **Ordre d'exécution :** l'agent de production exécute, puis l'agent d'affinage reprend la liste `HANDOFF_AFFINAGE.md`.
> **Principe :** le jeu fait **échouer** le candidat pour lui **apprendre**, de la science fondamentale (zéro-D) jusqu'à la décision clinique suisse. Il vise une rétention à vie.
> **Règle de lecture :** les règles sont numérotées (`R-xx`) et les blocages marqués 🛑. Une règle 🛑 non respectée interdit de passer à l'étape suivante.

---

## SOMMAIRE
- **§ 0.** Identification et signature (🛑 avant toute action)
- **§ 1.** Contenu du dépôt et sources de vérité
- **§ 2.** Architecture logicielle
- **§ 3.** Modèle de données (schémas)
- **§ 4.** Production exhaustive des QCM
- **§ 5.** REJECTOR_ : l'agent de vérification médicale
- **§ 6.** Agents, `/teamwork` et portes
- **§ 7.** Règles locales par zone, et feuille de règles
- **§ 8.** Psychologie de l'engagement
- **§ 9.** Frontend
- **§ 10.** Sons et effets par spécialité
- **§ 11.** Disciplines transversales : les 19 casquettes
- **§ 12.** Audits obligatoires avant livraison
- **§ 13.** Plan d'exécution par phases
- **§ 14.** Liste des blocages
- **§ 15.** Passation à l'agent d'affinage

---

## § 0. IDENTIFICATION ET SIGNATURE — 🛑 AVANT TOUTE ACTION
- **R-00.1 🛑** Ta première réponse donne, et rien ne la précède : **HEURE DE DÉBUT** (AAAA-MM-JJ HH:MM, Europe/Zurich), **MODÈLE** (ton nom de modèle exact) et **PLATEFORME** (l'outil d'où tu opères). Tu ajoutes la même ligne à `IDENTIFICATION_AGENTS.md`.
- **R-00.2 🛑** Si tu ignores avec certitude ton modèle ou ta plateforme, tu le dis et tu t'arrêtes.
- **R-00.3 🛑** Chaque fichier HTML produit ou modifié porte, juste avant `</body>`, ce bloc fixé en bas à droite de toutes les pages, en **GRAS MAJUSCULE** :
  ```html
  <div id="signature-ia" style="position:fixed;right:12px;bottom:10px;z-index:9999;background:#fff;border:2px solid #000;padding:4px 10px;font:700 12px/1.3 Arial,sans-serif;text-transform:uppercase;color:#000">DÉBUT : AAAA-MM-JJ HH:MM (EUROPE/ZURICH) · MODÈLE : <NOM> · PLATEFORME : <PLATEFORME></div>
  ```
- **R-00.4 🛑** Seul Vial autorise le retrait de ce bloc. Un agent qui reprend un fichier ajoute sa ligne sous la précédente et n'efface rien.
- **R-00.5** Chaque item de QCM porte aussi sa signature dans le champ `signature` (§ 3.2). Chaque message de commit la porte également.

---

## § 1. CONTENU DU DÉPÔT ET SOURCES DE VÉRITÉ
| Chemin | Contenu | Usage |
|---|---|---|
| `00_existant/jeu_45_specialites_suisse.html` | Jeu v1 (4,5 Mo, 1 fichier) | Point de départ : réutilise son ossature, ne la recopie pas. |
| `00_existant/PROMPT_JEU_45_SPECIALITES_SUISSE.md` | Cahier initial | Ce canevas le complète. En cas de conflit, **le canevas l'emporte**. |
| `00_existant/game_data/` | manifest, couverture, veille suisse | Format de la veille à conserver. |
| `01_audit/AUDIT_MedSuisse_Arena_45.html` | Audit de la v1 | Liste des défauts à corriger, à lire en premier. |
| `data/ssp/INDEX.json` | 248 SSP : entités, notions pondérées | Pilote la production. |
| `data/ssp/SSP_nnn_<code>.json` | Par SSP : **toutes** les entités (3 975, et pas seulement 10 DD), présentation clinique typique et atypique, notions par rubrique avec leur poids | **Source de vérité du contenu.** Les phrases de gabarit (8 036) en sont déjà retirées. |
| `data/references/catalogue_248.json` | Code, nom et circuit des 248 SSP | Référence officielle. |
| `data/references/transversales_19_et_systemes.json` | 19 transversales (leçons, sous-icônes, SSP liés) et 13 systèmes | Contenu transversal. |
| `data/references/game_payload_v1.json` | Données de la v1 (45 spécialités, 3 954 tuiles, 15 cas, 559 duels) | Migration. |
| `data/references/sons_fx_45_spec.json` | Son et effet propres à chaque spécialité | § 10. |
| `data/references/aips_corpus_index.json` | Index AIPS Swissmedic | Vérification des posologies (§ 5). |

**Chiffres pilotes :** 248 SSP · 3 975 entités · **119 242 notions pondérées** · 45 spécialités · 19 transversales.

---

## § 2. ARCHITECTURE LOGICIELLE
### 2.1 Pile technique (gratuite, statique, hébergée sur GitHub Pages)
| Brique | Choix | Raison |
|---|---|---|
| Animations | GSAP (gratuit) + CSS | Les séquences de victoire et de déblocage sont fluides. |
| Audio | Tone.js | La synthèse évite tout fichier sous licence. |
| Build | Vite + TypeScript strict | Le build est rapide, et le typage empêche les erreurs de schéma. |
| Données | JSON par spécialité, chargé à la demande | Le premier écran se charge en moins de 2 s. |
| Infobulles | Floating UI | Le positionnement reste fiable au survol, au tap et au focus. |
| Interface | Preact (3 Ko) + Signals | Le jeu est réactif sans peser. |
| Particules | tsParticles | Les effets propres à chaque spécialité s'affichent sur Canvas. |
| Répétition espacée | `ts-fsrs` (FSRS v5) | La planification se fait **par notion**. |
| Stockage | IndexedDB via Dexie | La progression reste locale, avec export et import chiffrés. |
| Tests | Vitest, Playwright, axe-core, Lighthouse CI | Ce sont les portes du § 12. |
| Validation | Zod (exécution) + JSON Schema (CI) | Un item invalide n'entre jamais dans le jeu. |

### 2.2 Modules (ordre alphabétique)
| Module | Responsabilité | Fichier |
|---|---|---|
| `audio` | Charger le profil sonore de la spécialité, gérer le volume et la coupure | `src/audio/` |
| `bossEngine` | Dérouler les cas longs à étapes | `src/engine/boss.ts` |
| `correctionLadder` | Afficher l'échelle de correction en 7 marches, avec prédiction | `src/ui/Ladder.tsx` |
| `duelEngine` | Mener un duel chronométré de 60 à 90 s | `src/engine/duel.ts` |
| `examMode` | Mener un examen blanc (60 % A, 40 % K', chronométré) | `src/engine/exam.ts` |
| `fogGrid` | Afficher la grille en brouillard de guerre et le score de notions par tuile | `src/ui/FogGrid.tsx` |
| `fx` | Jouer les effets de la spécialité active | `src/fx/` |
| `iconRegistry` | Associer chaque icône à sa raison d'être (§ 9.1) | `src/ui/icons.ts` |
| `localRules` | Afficher les règles locales de chaque zone (§ 7) | `src/rules/` |
| `masteryFacets` | Suivre la maîtrise en 7 facettes par notion | `src/engine/mastery.ts` |
| `psychometrics` | Calculer la difficulté et la discrimination de chaque item | `src/engine/psychometrics.ts` |
| `scheduler` | Planifier les révisions avec FSRS par notion | `src/engine/scheduler.ts` |
| `sessionGuard` | Plafonner les sessions et produire le bilan de fin | `src/engine/session.ts` |
| `storage` | Gérer Dexie, l'export et l'import chiffrés | `src/storage/` |
| `swissWatch` | Afficher les cartes de veille suisse | `src/ui/Watch.tsx` |
| `topBar` | Gérer la barre supérieure basse ou escamotable (§ 9.2) | `src/ui/TopBar.tsx` |

### 2.3 Arborescence cible
```
src/ (engine, ui, audio, fx, rules, storage, schemas)
content/items/<SPEC_xx>/<SSP>/<entite>.json     ← produits, validés
content/rules/<zone>.json                        ← règles locales
scripts/ (produce, auditA, auditB, rejector, build_index)
tests/ (unit, e2e, a11y)
.github/workflows/ (ci.yml, content-gate.yml, daily-items.yml, swiss-watch.yml)
```

---

## § 3. MODÈLE DE DONNÉES
### 3.1 Règles
- **R-03.1 🛑** Chaque item référence au moins une notion de `data/ssp/*.json`, par `notionRefs` au format `<ssp>/<entité>/<rubrique>`.
- **R-03.2 🛑** Un item de type A a 5 options et 1 bonne réponse. Un item K' a 4 affirmations, chacune vraie ou fausse, et le barème K' suisse s'applique : 4 justes donnent 1 point, 3 justes donnent ½ point, sinon 0.
- **R-03.3 🛑** Les 7 champs de `ladder` sont tous remplis et propres à l'item.
- **R-03.4 🛑** Chaque distracteur porte un `errorType` et une justification qui nomme l'erreur et la corrige.

### 3.2 Schéma d'un item
```json
{
  "id": "G1-E01-basicSciences-K01",
  "ssp": "G1", "entityId": "G1-E01", "specialtyId": "SPEC_14", "transversalIds": ["TRANS_B"],
  "notionRefs": ["G1/G1-E01/basicSciences"],
  "rubric": "basicSciences", "pillar": "Sciences fondamentales", "stratum": 3,
  "format": "Kprim", "difficulty": 3,
  "stem": "…", "prompt": "…",
  "options":    [{"key":"A","text":"…","correct":false,"errorType":"confusion_mecanisme","why":"…"}],
  "statements": [{"text":"…","true":true,"why":"…"}],
  "ladder": {"zeroD":"…","mechanism":"…","semiology":"…","discriminant":"…","decision":"…","trap":"…","anchor":"…"},
  "media": [{"type":"image","src":"media/…webp","license":"CC BY 4.0","author":"…","sourceUrl":"…","annotated":true}],
  "sources": [{"level":"AIPS|Compendium|CH|EU","ref":"sb-aips-12345","date":"2026-10-08"}],
  "variants": ["id-variante-1","id-variante-2"],
  "signature": {"start":"…","model":"…","platform":"…"},
  "audit": {"A":"pass","B":"pass","rejector":"pass","human":null}
}
```
**Types d'erreur des distracteurs (ordre alphabétique) :** `chronologie_inversee`, `confusion_entite_voisine`, `confusion_mecanisme`, `contre_indication_ignoree`, `examen_inutile`, `posologie_fausse`, `seuil_mal_retenu`, `urgence_sous_estimee`.

---

## § 4. PRODUCTION EXHAUSTIVE DES QCM
- **R-04.1 🛑 Exhaustivité.** Une notion de poids ×n engendre au moins n items. **Cible : environ 120 000 items** pour les 3 975 entités. Les items existants (559 duels et 60 questions de cas) sont réécrits selon ce canevas, pas simplement conservés.
- **R-04.2 Ordre de production :** strate 1 (urgences vitales) → strate 2 → strate 3 → strate 4, et à l'intérieur d'une strate, par spécialité, de la plus pauvre en items à la plus riche.
- **R-04.3 🛑 Format :** 60 % de type A, 40 % de K', par entité.
- **R-04.4 🛑 Zéro-D :** au moins 30 % des items d'une entité portent sur les rubriques `definition`, `basicSciences` ou `pathophysiology`.
- **R-04.5 Cas longs :** chaque entité a au moins 1 cas long en 6 étapes (vignette → anamnèse → examen → examens complémentaires → décision → suivi). Chaque étape contient 2 items.
- **R-04.6 Variantes :** chaque notion apparaît sous au moins 3 présentations (âge, contexte, porte d'entrée), pour que le savoir se transfère.
- **R-04.7 Images :** les images réelles proviennent de Wikimedia Commons, d'OpenStax ou d'articles en CC BY. Le cliché brut et le cliché annoté sont juxtaposés, avec l'attribution complète. **Aucune image dessinée par IA pour l'anatomie ou la sémiologie.** Le nombre d'images n'est pas limité.
- **R-04.8 🛑 Phrases verbales :** chaque phrase des énoncés, justifications et marches contient un verbe conjugué.
- **R-04.9 🛑 Zéro gabarit :** deux justifications ne se ressemblent jamais à plus de 50 % (MinHash).
- **R-04.10 Échelle de correction (7 marches, toujours dans cet ordre) :**

| Marche | Question à laquelle elle répond | Exemple (hyperhidrose focale primaire) |
|---|---|---|
| 0-D | Quelle science fondamentale rend l'entité possible ? | Les glandes eccrines reçoivent une innervation sympathique **cholinergique** (ACh sur récepteurs M3). |
| 1. Mécanisme | Comment la perturbation naît-elle et s'installe-t-elle ? | Une hyperexcitabilité sympathique centrale stimule ces glandes au-delà du besoin thermique. |
| 2. Sémiologie | Pourquoi chaque signe découle-t-il du mécanisme ? | La sudation s'arrête la nuit, car le tonus sympathique émotionnel baisse pendant le sommeil. |
| 3. Discriminant | Qu'est-ce qui sépare l'entité de ses rivales ? | Des sueurs **nocturnes** orientent au contraire vers une cause secondaire (tuberculose, lymphome). |
| 4. Décision | Quelle conduite suisse s'impose, et dans quel ordre ? | Chlorure d'aluminium → ionophorèse → toxine botulique A → anticholinergique oral. |
| 5. Piège | Quelle erreur le distracteur choisi incarnait-il ? | Lancer un bilan biologique étendu devant une forme typique : c'est un examen inutile. |
| 6. Ancre | Quelle phrase ou image condense la notion pour la vie ? | « Mains mouillées le jour, sèches la nuit : c'est primaire. » |

---

## § 5. REJECTOR_ — AGENT IA DE VÉRIFICATION MÉDICALE (OBLIGATOIRE)
- **R-05.1 🛑** `REJECTOR_` est un **agent IA distinct** de l'agent producteur : autre instance et, si possible, autre fournisseur. Aucun item ne passe sans son verdict `pass`.
- **R-05.2** Il est **intransigeant sur le fond** : chiffre, seuil, critère, posologie, contre-indication, mécanisme, ordre de conduite, source.
- **R-05.3** Il est **tolérant sur la forme** : style, longueur ou ordre des phrases. Il signale ces défauts en `warn` sans rejeter l'item.
- **R-05.4** Il travaille **à l'aveugle** : il ne voit ni le raisonnement du producteur ni le verdict d'un autre auditeur.
- **R-05.5** Il vérifie dans cet ordre : (1) les notions citées concordent avec `data/ssp` ; (2) chaque posologie concorde avec l'AIPS, sinon avec la cascade Compendium, puis les sociétés suisses, puis les sociétés européennes ; (3) chaque chiffre concorde avec sa source ; (4) la bonne réponse est unique pour un item A, et les 4 affirmations sont exactes pour un K' ; (5) la marche « Décision » respecte la pratique suisse.
- **R-05.6** Son verdict prend la forme d'un JSON par item :
  ```json
  {"itemId":"…","verdict":"pass|reject|warn","codes":["F-POSO"],"preuve":"extrait de la source","correction":"…","signature":{…}}
  ```
- **Codes de rejet sur le fond (ordre alphabétique) :** `F-CHIFFRE` chiffre faux · `F-CI` contre-indication omise · `F-CONDUITE` ordre ou conduite erronés · `F-MECA` mécanisme faux · `F-MULTI` plusieurs bonnes réponses · `F-NOTION` notion absente ou mal rattachée · `F-POSO` posologie fausse · `F-SOURCE` source absente ou invérifiable.
- **Codes d'avertissement sur la forme :** `W-LONG` trop long · `W-NOMINAL` phrase nominale (bloquante seulement si elle se répète) · `W-STYLE` style.
- **R-05.7 🛑** Un taux de rejet supérieur à 10 % sur un lot renvoie tout le lot en production.
- **R-05.8** Le contre-audit par script (§ 12.2) s'ajoute à REJECTOR_ et ne le remplace jamais.

---

## § 6. AGENTS, `/teamwork` ET PORTES
### 6.1 Agents (ordre alphabétique)
| Agent | Rôle | Entrée → sortie |
|---|---|---|
| `ARCHITECTE` | Il écrit le code de § 2 et les tests. | Canevas → `src/`, `tests/` |
| `AUDITEUR_A11Y` | Il vérifie le contraste, le clavier et les lecteurs d'écran. | Build → rapport axe |
| `AUDITEUR_FONCTIONNEL` | Il joue chaque zone de bout en bout (Playwright). | Build → rapport e2e |
| `AUDITEUR_PSY` | Il évalue l'engagement et ses garde-fous (§ 8). | Build + métriques → rapport |
| `ICONOGRAPHE` | Il cherche les images sous licence libre et les annote. | Item → `media/` + attribution |
| `ORCHESTRATEUR` | Il découpe le travail en vagues, lance les agents et tient `SUIVI.csv`. | `INDEX.json` → plan des vagues |
| `PRODUCTEUR_<SPEC>` | Il produit les items d'une spécialité. | `data/ssp` → `content/items/` |
| `REJECTOR_` | Il vérifie le fond (§ 5). | Items → verdicts |
| `SOUND_FX` | Il implémente § 10. | JSON → `src/audio`, `src/fx` |
| `TRANSVERSAL_<A…S>` | Il produit les items de sa discipline (§ 11). | Leçons → items |

### 6.2 `/teamwork`
- **R-06.1** L'ORCHESTRATEUR lance les agents en **vagues parallèles** : 1 spécialité par PRODUCTEUR, 5 spécialités par vague.
- **R-06.2** Un producteur ne vérifie jamais ses propres items. REJECTOR_ et les scripts A et B s'en chargent.
- **R-06.3** Chaque vague se termine par un commit signé et la mise à jour de `SUIVI.csv` : `vague;spec;ssp;items;rejets;couverture_notions;agent`.

### 6.3 Portes (un lot ne passe qu'à 100 %)
| Porte | Contrôle | Outil |
|---|---|---|
| P0 | Identification et signature présentes | Script |
| P1 | Le schéma est valide | Zod + `ajv` |
| P2 | La couverture des notions est confirmée par A et par B | BM25 + bge-m3 |
| P3 | Zéro gabarit, zéro phrase nominale répétée | MinHash + spaCy |
| P4 | REJECTOR_ rend `pass` | Agent IA |
| P5 | Les audits du § 12 sont verts | CI |

---

## § 7. RÈGLES LOCALES PAR ZONE, ET FEUILLE DE RÈGLES
- **R-07.1 🛑** Chaque zone affiche un bouton « ? » qui ouvre **ses** règles : 3 phrases verbales au plus, et 1 exemple.
- **R-07.2** La page « Feuille de règles » reprend toutes les règles locales, dans l'ordre du parcours, du début à la fin.
- **R-07.3** Les règles vivent dans `content/rules/<zone>.json`, au format `{zone, regles[], exemple}`.

| Zone (ordre du parcours) | Règle locale | Exemple |
|---|---|---|
| 1. Accueil | Tu choisis une arène ou tu lances un cas aléatoire. Le jeu ne te montre jamais le diagnostic avant ta réponse. | « Cas aléatoire » tire une vignette de fièvre chez un voyageur, sans rien en dire de plus. |
| 2. Arène (spécialité) | Chaque tuile cachée est une entité à découvrir. Tu la révèles en réussissant ses items. | En Cardiologie, la tuile « Endocardite » s'ouvre après 3 réussites espacées. |
| 3. Grille en brouillard | La grille monte des urgences vitales (en bas) vers les entités rares (en haut). Chaque tuile affiche ses notions maîtrisées sur le total. | « Hyperhidrose primaire : 14 / 26 ». |
| 4. Duel | Tu réponds en 90 s au plus. Une erreur dangereuse coûte 3 fois plus qu'une erreur mineure. | Si tu oublies d'éliminer une dissection avant d'anticoaguler, tu subis une pénalité de sécurité. |
| 5. Correction en échelle | Après une erreur, tu prédis la marche suivante avant de la lire. Une prédiction juste te rend la moitié des points perdus. | Tu prédis « innervation cholinergique » avant que la marche 0-D s'affiche. |
| 6. Revanche | Tu rejoues aussitôt une variante de la même notion. La réussir rapporte le double. | Même notion, mais chez une patiente de 74 ans. |
| 7. Révision du jour | Le jeu te propose les notions dont FSRS juge l'oubli imminent. | Il te rappelle « Critères de Hornberger », vus il y a 9 jours. |
| 8. Boss de SSP | Le boss se débloque à 60 % de maîtrise du SSP. Il enchaîne 6 étapes, et chacune dépend de la précédente. | Le boss « Transpiration anormale » mène du triage au suivi. |
| 9. Examen blanc | 60 % de type A, 40 % de K', chronométré, au barème fédéral. Les corrections n'apparaissent qu'à la fin. | 50 questions en 75 minutes. |
| 10. Transversales | Chaque cas porte une question de droit, d'éthique ou d'assurance liée à sa situation. | « Qui finance ce transport en ambulance ? » (LAMal ou LAA). |
| 11. Veille suisse | Les cartes résument les nouveautés officielles (OFSP, Swissmedic, Smarter Medicine). | Une nouvelle recommandation vaccinale de l'OFSP apparaît. |
| 12. Profil et statistiques | Tu vois tes notions maîtrisées, oubliées et à risque, par spécialité. | « Endocrinologie : 61 % maîtrisé, 12 notions à revoir. » |
| 13. Paramètres | Tu règles le volume, les effets, la durée de session et l'export. | Tu coupes les sons en garde. |

---

## § 8. PSYCHOLOGIE DE L'ENGAGEMENT (ordre alphabétique)
| Levier | Réglage précis | Effet | Garde-fou |
|---|---|---|---|
| Bilan de fin de session | Il liste les notions gagnées, perdues et à revoir demain. | La session se clôt sur un sentiment de progrès. | Il ne culpabilise jamais. |
| Boss de SSP | Il se débloque à 60 % de maîtrise. | Il oblige à intégrer les connaissances. | Il reste rejouable sans pénalité. |
| Effet de génération | Le joueur prédit la marche suivante avant de la lire. | La mémorisation devient plus profonde. | Une mauvaise prédiction ne retire aucun point. |
| Indice de sécurité patient | Une erreur dangereuse coûte ×3. | Le joueur hiérarchise selon le danger. | La correction explique pourquoi l'erreur était dangereuse. |
| Mutation de présentation | Chaque notion revient sous 3 présentations. | Le savoir se transfère. | — |
| Plafond de session | 12 minutes par défaut, réglable de 5 à 30. | Le joueur évite l'épuisement. | Une pause est proposée, jamais imposée. |
| Récompense variable | Un cas rare-critique surgit au hasard (1 sur 12), avec un bonus de ×3. | Le joueur anticipe. | Pas de pièce, pas d'achat. |
| Récompense de la reprise | Corriger une erreur passée rapporte ×2. | L'échec cesse d'être vécu comme une perte. | — |
| Répétition espacée | FSRS par notion, avec une rétention cible de 0,90. | La rétention dure des années. | La charge quotidienne est plafonnée à 60 révisions. |
| Série quotidienne | Elle compte les jours joués, avec 1 jour de grâce par semaine. | L'habitude s'installe. | Rompre la série ne retire aucun point. |
| Tuile à compteur | « 14 / 26 notions » sur chaque tuile. | La progression devient visible. | — |

- **R-08.1 🛑 Interdits :** l'achat, la publicité, la notification nocturne (de 22 h à 7 h), le compte à rebours anxiogène hors examen blanc, et la perte de progression.
- **R-08.2** L'AUDITEUR_PSY mesure 5 indicateurs : la durée médiane de session, le taux de retour à J1 et J7, le taux de reprise après erreur, la part de révisions FSRS effectuées, et la proportion de sessions qui dépassent le plafond (cible : moins de 10 %).

---

## § 9. FRONTEND
### 9.1 Infobulle « pourquoi j'existe » sur chaque icône
- **R-09.1 🛑** Chaque icône est déclarée dans `iconRegistry` avec 3 champs : `nom`, `raison` (1 phrase verbale qui dit pourquoi elle existe dans la plateforme) et `action`.
- **R-09.2** L'infobulle s'ouvre au survol, au tap long (500 ms) et au focus clavier. Le build échoue si une icône n'a pas de raison.
- **Exemple :** `{"nom":"Bouclier","raison":"Il mesure la sécurité de tes décisions pour le patient, car une erreur dangereuse pèse plus qu'une erreur mineure.","action":"Ouvrir l'historique de sécurité"}`.

### 9.2 Barre supérieure
- **R-09.3** La barre supérieure mesure **44 px au plus** : une rangée, des icônes et un libellé court.
- **R-09.4** Pendant un cas ou un duel, un clic dans une zone vide **escamote** la barre. Elle revient quand la souris s'approche à moins de 12 px du bord haut, ou par la poignée « barre de tâches » (8 px, visible), ou par la touche `Échap`.
- **R-09.5** Sur mobile, un balayage vers le bas fait revenir la barre.

### 9.3 Charte
- **R-09.6** Le fond est blanc. Le texte de contenu est en Atkinson Hyperlegible, de 15 à 16 px, dans une colonne de 880 px au plus. Chaque arène prend la couleur de sa spécialité (`sons_fx_45_spec.json`).
- **R-09.7** Le contraste est d'au moins 4,5:1. Le jeu respecte `prefers-reduced-motion` et reste entièrement jouable au clavier.

---

## § 10. SONS ET EFFETS PAR SPÉCIALITÉ
- **R-10.1** Chaque spécialité possède une signature sonore et une signature visuelle, définies dans `data/references/sons_fx_45_spec.json` (45 entrées).
- **R-10.2** Six événements sont sonorisés : bonne réponse, erreur mineure, **erreur dangereuse** (avec une dissonance grave), déblocage de tuile, maîtrise d'une notion et boss.
- **R-10.3** Le son est synthétisé par Tone.js : aucun fichier audio sous licence. Le volume par défaut est de 0,35, et la coupure générale reste accessible en 1 clic.
- **R-10.4** Si l'option de réduction des mouvements est active, chaque effet devient un simple fondu de couleur.

| Code | Spécialité | Son | Effet |
|---|---|---|---|
| ALL | Allergologie et immunologie clinique | Clochettes cristallines en mode lydien | Bulles d'histamine qui éclatent |
| ANE | Anesthésiologie | Bip de moniteur qui ralentit, souffle de ventilateur | Courbe de capnographie |
| ANG | Angiologie | Pulsation grave en glissando | Flux le long d'un vaisseau |
| CAR | Cardiologie | « Lub-dub » à 72/min | Trace ECG qui forme un QRS |
| CCT | Chirurgie cardiaque et vasculaire thoracique | Lub-dub et clic de valve | Valve qui claque |
| CHI | Chirurgie | Tintement d'instrument | Incision qui se referme en suture |
| CMA | Chirurgie de la main | Corde pincée | Doigts qui fléchissent |
| CMF | Chirurgie orale et maxillo-faciale | Grincement résonnant | Mâchoire qui s'articule |
| CPE | Chirurgie pédiatrique | Boîte à musique | Peluche qui lance des étoiles |
| CPL | Chirurgie plastique | Harpe ascendante | Lambeau qui se recolore |
| CTH | Chirurgie thoracique | Inspiration et expiration filtrées | Poumon qui se réexpand |
| CVA | Chirurgie vasculaire | Glissando de violoncelle | Stent qui se déploie |
| DER | Dermatologie et vénéréologie | Pizzicato léger | Lésion qui s'éclaircit |
| END | Endocrinologie-diabétologie | Marimba pentatonique | Papillon thyroïdien |
| GAS | Gastroentérologie | Gargouillis stylisé | Péristaltisme ondulant |
| GEN | Génétique médicale | Arpège sur 4 notes (A, C, G, T) | Double hélice qui s'apparie |
| GYN | Gynécologie et obstétrique | Battement fœtal à 140/min | Croissance fœtale |
| HEM | Hématologie | Gouttes en cascade | Globules en rouleaux |
| INF | Infectiologie | Crépitement organique | Anticorps qui neutralisent |
| INT | Médecine intensive | Alarme qui se résout en accord | Constantes du rouge au vert |
| LEG | Médecine légale | Marteau de juge | Balance qui s'équilibre |
| MIG | Médecine interne générale | Carillon suisse | Croix suisse qui réunit les organes |
| MPR | Médecine physique et réadaptation | Pas rythmés | Silhouette qui se relève |
| MTR | Médecine du travail | Sirène d'usine adoucie | Casque qui s'illumine |
| NCH | Neurochirurgie | Accord grave et précis | Zone cérébrale qui se décomprime |
| NEP | Néphrologie | Goutte d'eau | Néphron qui filtre |
| NEU | Neurologie | Arc électrique | Influx de nœud en nœud |
| NUC | Médecine nucléaire | Compteur Geiger harmonisé | Points chauds de scintigraphie |
| OPH | Ophtalmologie | Glissement de lentille | Pupille qui se contracte |
| ONC | Oncologie médicale | Accord solennel de piano | Cellules anormales qui s'éteignent |
| ORL | Oto-rhino-laryngologie | Diapason à 512 Hz | Ondes dans la cochlée |
| ORT | Chirurgie orthopédique et traumatologie | Claquement d'os puis accord | Fracture qui se consolide |
| PAT | Pathologie | Clic de lame | Coupe qui passe au grossissement |
| PEA | Psychiatrie de l'enfant et de l'adolescent | Carillon à vent | Cerf-volant qui s'élève |
| PED | Pédiatrie | Xylophone joyeux | Courbe de croissance |
| PHA | Médecine pharmaceutique | Cachet effervescent | Pilule qui se dissout |
| PNE | Pneumologie | Souffle régulier | Alvéoles qui se gonflent |
| PSP | Prévention et santé publique | Chœur bref | Population qui se colore de vert |
| PSY | Psychiatrie et psychothérapie | Nappe douce qui se résout | Puzzle mental qui s'emboîte |
| RAD | Radiologie | Balayage de scanner | Coupe qui défile |
| RHU | Rhumatologie | Craquement puis note souple | Articulation qui se dérouille |
| RON | Radio-oncologie | Bourdonnement focalisé | Faisceaux convergents |
| TOX | Pharmacologie et toxicologie cliniques | Bouillonnement d'éprouvette | Molécule qui rencontre son antidote |
| TRO | Médecine tropicale et de voyage | Kalimba | Globe et itinéraire |
| URO | Urologie | Cascade d'eau légère | Voies urinaires qui s'éclairent |

---

## § 11. DISCIPLINES TRANSVERSALES — LES 19 CASQUETTES
- **R-11.1** Chaque transversale a son agent `TRANSVERSAL_<lettre>`, ses leçons (`transversales_19_et_systemes.json`) et ses items.
- **R-11.2 🛑** Chaque cas long porte au moins 1 item transversal lié à sa situation.
- **R-11.3** Chaque transversale reçoit au moins 300 items, dont 30 % de K'.

| Lettre | Discipline | Références suisses à mobiliser |
|---|---|---|
| A | Assurances sociales & Expertise | LAMal, LAA, LAI, LCA, LPGA, expertise AI |
| B | Biostatistique & EBM | Sensibilité, spécificité, VPP/VPN, rapports de vraisemblance, NNT, Bayes |
| C | Communication clinique | Annonce, décision partagée, interprétariat |
| D | Digitalisation & Cybersanté | Dossier électronique du patient (DEP), LPD |
| E | Diversité, Équité & Inclusion | Migration, littératie, genre |
| F | Droit médical suisse | CC (protection de l'adulte, APEA), CP, LPMéd, secret médical |
| G | Épidémiologie | OFS, Obsan, déclarations obligatoires |
| H | Éthique biomédicale & Fin de vie | Directives de l'ASSM, directives anticipées, assistance au suicide |
| I | Génétique médicale & Conseil | LAGH, conseil génétique |
| J | Hygiène hospitalière | Swissnoso |
| K | Médecine du travail & Ergonomie | SUVA, OLT |
| L | Médecine légale & Forensique | Constat, levée de corps, signalement |
| M | Médecine palliative | palliative ch, contrôle des symptômes |
| N | Médecine sociale & Prévention | OFSP, plan de vaccination suisse |
| O | Pharmacologie, Toxicologie & Sécurité | Swissmedic (AIPS), Tox Info Suisse 145 |
| P | Qualité, Sécurité & Gestion de l'erreur | CIRS, Smarter Medicine |
| Q | Radioprotection & Smarter Medicine | ORaP, doses, listes « top 5 » |
| R | Santé planétaire | Empreinte écologique des soins |
| S | Urgences vitales & Triage | 144, REGA, Swiss Emergency Triage |

---

## § 12. AUDITS OBLIGATOIRES AVANT LIVRAISON
> **⚠️ MISE EN GARDE À TOUTE IA :** tu ne déclares JAMAIS le jeu livré sans les **trois audits** ci-dessous, chacun avec sa preuve sur disque (`audits/*.json` et capture). Une déclaration sans preuve vaut un échec.

### 12.1 Audit de fonctionnement
| Contrôle | Outil | Seuil |
|---|---|---|
| Parcours e2e des 13 zones | Playwright | 100 % vert |
| Tests unitaires du moteur (FSRS, facettes, barème K') | Vitest | Couverture d'au moins 85 % |
| Performance | Lighthouse CI | Score d'au moins 90 ; premier écran en moins de 2 s |
| Accessibilité | axe-core | 0 violation grave |
| Sons et effets | Playwright + journal audio | 45 profils chargés, coupure fonctionnelle |
| Persistance | Playwright | Export puis import sans perte |

### 12.2 Audit médical (script A + script B + REJECTOR_)
| Contrôle | Script A | Script B | Seuil |
|---|---|---|---|
| Couverture des notions pondérées | BM25 (`rank_bm25`) | Embeddings (`FlagEmbedding`, bge-m3) | Au moins 98 % confirmés par A **et** B |
| Ratio items / poids par entité | Comptage | Recomptage indépendant | Au moins 1 partout |
| Quota de zéro-D | Étiquettes | Classifieur par mots-clés | Au moins 30 % par entité |
| Gabarit | MinHash (`datasketch`) | n-grammes de début | 0 paire au-dessus de 0,5 |
| Phrases nominales | spaCy `fr_core_news_md` | Stanza (français) | 0 phrase nominale répétée |
| Posologies | Index AIPS | Cache Compendium | 100 % concordantes ou sourcées |
| Exactitude clinique | REJECTOR_ | Second auditeur IA, à l'aveugle | Rejets sous 2 % après correction |
| Échantillon humain | — | — | Vial relit 5 % par spécialité |

### 12.3 Audit psychologique (engagement sain)
| Contrôle | Méthode | Seuil |
|---|---|---|
| Boucle échec → apprentissage | Simulation de 100 sessions | Échelle affichée après 100 % des erreurs |
| Reprise après erreur | Télémétrie locale | Au moins 70 % des erreurs rejouées dans la session |
| Rétention | FSRS | Rétention prédite d'au moins 0,90 à J30 |
| Garde-fous | Revue du § 8 | 0 interdit violé |
| Dépassement du plafond | Télémétrie locale | Moins de 10 % des sessions |

---

## § 13. PLAN D'EXÉCUTION PAR PHASES
| Phase | Livrable | Porte de sortie |
|---|---|---|
| 0 | Identification, lecture de l'audit, plan des vagues | 🛑 Identification consignée |
| 1 | Code de § 2 (moteur, interface, sons, effets, règles locales), migration de la v1 | Audit de fonctionnement vert |
| 2 | **Prototype de contenu** : SSP G1 complet (22 entités, environ 699 items) + transversale S | 🛑 GO écrit de Vial |
| 3 | Strate 1 sur les 248 SSP | Audit médical vert par lot |
| 4 | Strates 2 à 4 | Audit médical vert par lot |
| 5 | 19 transversales, examen blanc | Les trois audits verts |
| 6 | Passation à l'agent d'affinage | `HANDOFF_AFFINAGE.md` complet |

---

## § 14. LISTE DES BLOCAGES 🛑 (ordre alphabétique)
- Audit déclaré sans preuve sur disque.
- Échelle de correction incomplète ou générique.
- Entité de `data/ssp` sans item.
- Gabarit détecté (similarité au-dessus de 0,5).
- Icône sans raison d'être.
- Identification absente ou incertaine.
- Image anatomique ou sémiologique dessinée par IA, ou image sans licence.
- Interdit psychologique violé (§ 8).
- Item sans `notionRefs`, ou dont le schéma est invalide.
- Item sans verdict `pass` de REJECTOR_.
- Phrase nominale dans un item.
- Posologie non sourcée par la cascade.
- Ratio items / poids inférieur à 1.
- Signature absente ou modifiée.
- Zone sans règle locale ni exemple.

---

## § 15. PASSATION À L'AGENT D'AFFINAGE
- **R-15.1** L'agent de production tient `HANDOFF_AFFINAGE.md` : une section par spécialité, une ligne par point non garanti (doute clinique, licence, posologie hors AIPS, performance).
- **R-15.2** L'agent d'affinage traite uniquement cette liste, relance les trois audits et signe ses modifications selon § 0.
- **R-15.3** Rien n'est supprimé : toute version remplacée part dans `_archive/`.
