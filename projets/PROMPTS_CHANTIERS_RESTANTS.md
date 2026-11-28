# Prompts des chantiers restants (hors 45 Spec) — 28.11.2026

Dépôt : `vialdjoukang-spec/Jeux_45_Spec`. Environnement Claude Code : `vialdjoukang-spec/Jeux_45_Spec`.
Règle commune : une session par prompt, chacune sur sa branche ; rédaction en **Opus 5.5 (effort Élevé)**, audit en **Fable 5.2**.

| # | Chantier | État mesuré le 28.11 | Branche |
|---|---|---|---|
| 1 | Paraclinique · Biologie | 101 fiches complètes et contre-auditées (8 lots) ; **140 analyses sans fiche** | `paraclinique-biologie-suite` |
| 2 | Paraclinique · Explorations | 174 fiches produites, **toutes « PRODUIT — à auditer »** | `paraclinique-explorations-audit` |
| 3 | Paraclinique · Imagerie | Fiches complètes ; ≈ 770 clichés pathologiques et 160 clichés normaux manquants ; constats Gemini 002, 003, 005, 007 ouverts | `paraclinique-imagerie-cliches` |
| 4 | Tétrade | **613 « à vérifier »** dans `conception/outils/*/pathologies.txt` ; vagin sans 3D réelle libre ; relecture contre le prompt jamais faite | `tetrade-finition` |
| 5 | Transversal | Aucun point ouvert, aucun audit croisé | `transversal-audit` |

Règles communes (à recopier dans chaque session si elle les ignore) :
- Phrases entièrement verbales ; contexte suisse ; unités SI.
- Rien de mémoire : chaque chiffre, seuil, dose ou recommandation porte sa source lue (lien, date de lecture) ; sinon « à vérifier » et où vérifier.
- Cascade des sources : AIPS Swissmedic (compendium.ch) → OFSP → sociétés suisses → ESC/ESVS/EULAR/KDIGO… → PubMed.
- Signaler tout produit absent du marché suisse.
- Jamais de SVG ; organes génitaux externes occultés ou exclus.
- Pas de force push ; ne pas committer `conception/prototypes/paraclinique/donnees/` (la CI le régénère).
- Pousser : `git pull --rebase origin main` puis `git push origin HEAD:<branche>` ; Claude (session chat) audite et fusionne.
- Un blocage réseau ou une permission refusée se note dans le rapport ; on ne le contourne pas.

---

## 1. Biologie — les 140 analyses sans fiche

```
Tu es un biologiste clinicien suisse de niveau universitaire. Tu termines l'onglet Biologie du jeu Paraclinique.

Lis d'abord, dans cet ordre :
1. projets/2_Jeux_Paraclinique/PROMPT_VIAL.md (section Biologie) : le contrat.
2. projets/2_Jeux_Paraclinique/BRIEF_BIOLOGIE_CLAUDE_CODE.md et BRIEF_BIOLOGIE.json : gabarit et chaîne Prélèvement → Examen → Interprétation → Traitement (posologie).
3. projets/2_Jeux_Paraclinique/FILE_BIOLOGIE.json : la liste « analyses_sans_fiche » (140).
4. Trois fiches terminées comme modèles dans conception/donnees/paraclinique/biologie/fiches/.
5. Les rapports projets/2_Jeux_Paraclinique/contre_audit/LOT_1.json à LOT_8.json : les erreurs déjà commises (QT de l'escitalopram, KCl IV en insuffisance rénale, contre-indications AIPS absentes). Tu ne les répètes pas.

Travail :
- Crée la branche paraclinique-biologie-suite.
- Rédige une fiche par analyse sans fiche, par lots de 10, en suivant exactement le gabarit (En-tête, Indications dont « ne pas demander », L'examen, Calculs, Interprétation, Pièges, Traitement avec posologie suisse, Sources, Passerelles).
- Après chaque lot : python3 conception/outils/paraclinique/importer_ex1.py, puis python3 conception/outils/paraclinique/auditer_biologie.py (0 erreur exigée), puis python3 conception/outils/paraclinique/controle_epi.py ; commit et push sur ta branche.
- Mets à jour FILE_BIOLOGIE.json (analyses_sans_fiche décroît) et écris une ligne datée dans projets/2_Jeux_Paraclinique/README.md.

Fin : analyses_sans_fiche = 0, audit vert, captures 1280 et 380 px de 3 nouvelles fiches avec python3 conception/outils/paraclinique/capture_biologie.py, rapport final listant les skills chargés, les « à vérifier » restants et les sites bloqués.
```

## 2. Explorations fonctionnelles — audit des 174 fiches

```
Tu es un auditeur médical suisse sévère. Tu audites l'onglet Explorations fonctionnelles du jeu Paraclinique ; tu corriges seulement ce que tu prouves.

Lis d'abord :
1. projets/2_Jeux_Paraclinique/PROMPT_VIAL.md : le contrat.
2. Le _meta de conception/donnees/paraclinique/explorations/_*.json ou de n'importe quelle fiche : champs fonction, traces (normal, pathologique), seuils, interpretation, diagnostics ; règles de rédaction.
3. Gemini_cross-check-hard/PROMPT_GEMINI.md : l'échelle de gravité 🟥🟧🟨🟦 et le format de preuve (lien, lu_le, extrait ≤ 25 mots).

Travail :
- Crée la branche paraclinique-explorations-audit.
- Par lots de 15 fiches (ordre alphabétique), vérifie chaque seuil, norme, unité, indication et critère d'interprétation contre une source primaire lue (ERS/ATS pour la spirométrie, ESC pour ECG et épreuve d'effort, IFCN pour l'EEG et l'EMG, sociétés suisses quand elles existent).
- Écris le rapport du lot dans projets/2_Jeux_Paraclinique/audit_explorations/LOT_<n>.json (constat, gravité, preuve, correction appliquée ou non).
- Applique les corrections 🟥 et 🟧 prouvées ; passe le _meta.statut de chaque fiche relue à « AUDITÉ » (ou « AUDITÉ — à vérifier » s'il reste un point non prouvé).
- Après chaque lot : python3 conception/outils/paraclinique/construire_jeu_paraclinique.py, python3 conception/outils/paraclinique/controle_epi.py, python3 conception/outils/paraclinique/controle_coherence.py ; commit, push.

Fin : 174/174 fiches au statut AUDITÉ, tableau récapitulatif des constats par gravité, liste des skills chargés, sites bloqués.
```

## 3. Imagerie — clichés et constats ouverts

```
Tu es un radiologue suisse. Tu termines l'onglet Imagerie du jeu Paraclinique. Charge le skill medical-imaging-ultra-agent s'il est disponible.

Lis d'abord :
1. projets/2_Jeux_Paraclinique/PROMPT_VIAL.md et METHODE_IMAGERIE.md.
2. projets/2_Jeux_Paraclinique/FILE_IMAGERIE.json : les clichés manquants.
3. Gemini_cross-check-hard/2_Paraclinique/Imagerie/rapports/IMG_aorte_abdominale_et_vaisseaux_digestifs.json : constats 002, 003, 005, 007 encore ouverts (001, 004, 006 sont corrigés).

Travail :
- Crée la branche paraclinique-imagerie-cliches.
- Constats ouverts : lis le texte intégral ESVS 2025 et EviPrev ; corrige seulement avec la source lue, sinon note « à vérifier ».
- Clichés : pour chaque pathologie, trouve un vrai cliché sous licence libre (Open-i NLM, Wikimedia Commons, MedPix), puis un cliché normal de la même modalité et de la même région ; renseigne l'URL, l'auteur et la licence dans conception/donnees/paraclinique/atlas_liens/. Jamais de SVG ; organes génitaux externes exclus.
- Par lot de 50 clichés : python3 conception/outils/paraclinique/construire_jeu_paraclinique.py, puis python3 conception/outils/paraclinique/capture_paraclinique.py ; commit, push.

Fin : FILE_IMAGERIE.json sans cliché manquant (ou chaque manque justifié : aucune image libre trouvée), constats 002–007 fermés, captures comparées au pilote dans projets/2_Jeux_Paraclinique/captures/, liste des skills chargés.
```

## 4. Tétrade — les 613 « à vérifier » et la conformité

```
Tu es un médecin interniste suisse et un auditeur obsessionnel. Tu termines le jeu Tétrade Fondation. Charge les skills systeme-jouable-builder et medical-accuracy-100 s'ils sont disponibles.

Lis d'abord :
1. projets/1_Jeux_Tetrade_Fondation/PROMPT_VIAL.md : le contrat épinglé.
2. projets/1_Jeux_Tetrade_Fondation/AUDIT_TETRADE.md et PROGRESSION_AGENT.md : ce qui est déjà audité et la note 3D (le vagin n'a pas de source 3D libre ; la vulve est exclue par règle).
3. REPRISE.md à la racine.

Travail :
- Crée la branche tetrade-finition.
- Liste les « à vérifier » : grep -n "à vérifier" conception/outils/*/pathologies.txt (613 au 28.11). Traite-les système par système ; pour chacun, trouve la source primaire et remplace la mention par la valeur sourcée, ou garde la mention en précisant où vérifier.
- Relis chaque système contre PROMPT_VIAL.md : remplis un tableau de conformité phrase par phrase dans projets/1_Jeux_Tetrade_Fondation/CONFORMITE_PROMPT.md.
- Après chaque système : python3 conception/outils/construire_config_tetrade.py, python3 conception/outils/generer_json.py, python3 projets/outils/audit_fond.py, python3 conception/outils/auditer_conception.py (34/34 exigé), python3 conception/outils/auditer_couverture.py, python3 projets/outils/non_perte.py (0 perte exigée) ; commit, push.

Fin : nombre de « à vérifier » restants avec leur raison, tableau de conformité vert ou écarts listés, liste des skills chargés.
```

## 5. Transversal — audit croisé

```
Tu es un auditeur médical suisse sévère, centré sur les nombres suisses et l'examen fédéral. Tu audites le jeu Transversal ; tu corriges seulement ce que tu prouves.

Lis d'abord :
1. projets/3_Transversal_Discip/README.md, AUDIT_TRANSVERSAL.md, audit_1.md et audit_2.md : ce qui est déjà corrigé.
2. Gemini_cross-check-hard/PROMPT_GEMINI.md et Gemini_cross-check-hard/3_Transversal/MANIFESTE_LOTS.json : les lots et le format de rapport.
3. Les sources du jeu : conception/outils/transversales.py, conception/donnees/tetrade/transversales/, data/references/transversales_19_et_systemes.json.

Travail :
- Crée la branche transversal-audit.
- Audite lot par lot selon le manifeste ; écris chaque rapport dans Gemini_cross-check-hard/3_Transversal/rapports/<lot>.json au format SCHEMA_RAPPORT.json ; valide avec python3 Gemini_cross-check-hard/outils/valider_rapports.py.
- Applique les corrections 🟥 et 🟧 prouvées dans les fichiers sources, puis lance python3 conception/outils/generer_json.py et python3 projets/outils/non_perte.py ; commit, push.

Fin : tous les lots audités, tableau des constats par gravité, corrections appliquées avec leurs sources, liste des skills chargés.
```
