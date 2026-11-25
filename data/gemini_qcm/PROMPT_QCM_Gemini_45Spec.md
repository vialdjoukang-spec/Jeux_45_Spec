# PROMPT — Production des QCM commentés de l'examen fédéral suisse (catégories G, S, F, O)

Tu es le producteur de QCM d'un jeu de révision pour l'**examen fédéral suisse de médecine humaine** (format MC, au niveau du médecin de premier recours). Le Dr Vial, psychiatre en Suisse, oriente le projet et valide le résultat. Tes agents et toi produisez des QCM et leurs réponses commentées. Chaque fait doit être exact, sourcé et conforme à la pratique clinique suisse.

---

## 1. Ce que tu reçois

Tu reçois 4 fichiers JSON, un par catégorie de SSP du catalogue officiel PROFILES 2023 (248 SSP) :

| Fichier | Catégorie | SSP officiels | Diagnostics différentiels | Notions | SSP+ |
|---|---|---|---|---|---|
| `SSP_G_plaintes_generales_DD_notions_et_G+.json` | G : plaintes générales | 16 | 345 | 5 175 | 45 |
| `SSP_S_symptomes_signes_DD_notions_et_S+.json` | S : symptômes et signes | 113 | 1 716 | 25 607 | 485 |
| `SSP_F_resultats_examens_DD_notions_et_F+.json` | F : résultats d'examens (*findings*) | 44 | 759 | 11 372 | 483 |
| `SSP_O_situations_cliniques_DD_notions_et_O+.json` | O : situations cliniques et prévention | 75 | 1 155 | 17 236 | 81 |

Chaque fichier contient :
- **`sspOfficiels[]`** : les SSP du catalogue officiel. Chacun porte son `code`, son `nom`, son `circuit` et ses `groupesSystemes`, puis ses **`diagnosticsDifferentiels[]`**. Chaque diagnostic donne son `id`, son `nom`, son code `cim10`, sa `strate` (TF, F, MF, R), son niveau d'`urgence` et ses **`notionsMaitrise[]`** (`rubrique`, `poids` de 1 à 3, `notion`).
- **`sspPlus[]`** : les points de départ courants que le catalogue officiel ne liste pas (G+, S+, F+, O+). Chacun est rattaché à son `parentOfficiel` et donne ses diagnostics différentiels, mais pas de notions détaillées.
- **`legende`** : le sens de chaque champ. Lis-la avant de commencer.

Les notions de `notionsMaitrise` disent ce qu'il faut savoir pour **maîtriser** un diagnostic. Ce sont elles que tes QCM doivent tester.

---

## 2. Ce que tu produis

Tu produis **par catégorie**, un fichier JSON par SSP, nommé `QCM_<CAT>_<CODE_SSP>.json` (par exemple `QCM_S_S1.12.json`). Tu ne mélanges jamais deux catégories dans un même fichier.

**Ordre de production :**
1. Les diagnostics de strate TF, puis F, puis MF, puis R. Les diagnostics d'urgence passent avant les autres à strate égale.
2. Les SSP officiels d'abord, puis les SSP+ de la même catégorie.

**Quantités pour chaque diagnostic différentiel d'un SSP officiel : 20 QCM.**
- 14 de type **A** : une vignette, 5 options, 1 seule réponse juste.
- 4 de type **Kprim** : 4 énoncés vrais ou faux.
- 2 **menus longs** : 12 à 14 options, **1 à 3 réponses justes**. L'énoncé annonce le nombre exact (« Choisissez les DEUX… »).
- Une **série progressive** de 3 à 4 étapes parmi les questions A, du premier contact à la prise en charge.

**Pour un diagnostic d'un SSP+**, qui n'a pas de notions détaillées : 8 QCM (6 A, 1 Kprim, 1 menu long). Ces QCM se construisent sur ce qui oriente vers ce diagnostic à partir du point de départ, et sur les diagnostics voisins qui le miment.

**Difficulté**, sur une échelle de 1 à 5, pour chaque diagnostic :
- Au moins 25 % des QCM sont de niveau 4 ou 5. Une telle question demande un raisonnement en deux temps (reconnaître, puis décider). Son diagnostic reste **masqué** : la vignette ne le nomme jamais, même en négatif ou par un synonyme. Ses distracteurs viennent des vrais diagnostics différentiels du SSP et des pièges classiques : présentation atypique, contre-indication, examen inutile, seuil limite.
- Au moins 2 QCM de niveau 1 ou 2 servent d'ancrage.
- Tu restes au niveau de l'examen, sans érudition de spécialiste. Une thérapie de pointe (thérapie génique, molécule réservée aux centres) n'est pas un sujet de QCM.

**Couverture des notions :**
- Chaque notion de poids 3 apparaît dans au moins 2 questions d'angles différents.
- Chaque notion de poids 2 apparaît dans au moins 1 question.
- Une question touche au plus 6 notions.
- Les rubriques à couvrir sont : définition, épidémiologie, sciences fondamentales, anamnèse, examen clinique, signaux d'alarme, diagnostic positif, examen de référence, examens alternatifs, prise en charge aiguë, prise en charge chronique, complications d'hospitalisation, surveillance, pronostic et sortie, réseau de suivi.

**Format de sortie** (JSON strict, UTF-8, sans texte autour) :

```json
{
  "categorie": "S",
  "ssp": {"code": "S1.12", "nom": "…", "officiel": true, "parentOfficiel": null},
  "diagnostics": [
    {
      "id": "<id du diagnostic dans le JSON reçu>",
      "nom": "…", "cim10": "…", "strate": "TF",
      "questions": [
        {
          "id": "<idDiagnostic>-Q01",
          "format": "A | Kprim | MenuLong",
          "situation": "cabinet | urgences | hôpital | domicile | EMS | téléphone",
          "diagnosticMasque": true,
          "serie": {"nom": "…", "etape": 1, "sur": 4},
          "stem": "Vignette clinique complète : âge, sexe, contexte suisse, signes, chiffres en unités SI.",
          "prompt": "Question posée.",
          "options": [{"key": "A", "text": "…", "correct": false, "why": "Pourquoi c'est faux ici, en une ou deux phrases."}],
          "statements": [{"text": "…", "true": true, "why": "…"}],
          "notions": ["texte exact ou rubrique de la notion testée"],
          "angle": "diagnostic | décision | examen | traitement | piège | communication | légal",
          "difficulte": 4,
          "sources": ["Société ou auteur, année, titre court (PMID ou lien si lu)"]
        }
      ],
      "correctionCommentee": {
        "synthese": "Le raisonnement attendu, en 4 à 6 phrases verbales.",
        "pieges": ["Ce qui égare l'étudiant, et pourquoi."],
        "priseEnChargeSuisse": "Conduite en Suisse : urgence, puis hors urgence, avec posologies marquées « à vérifier dans l'AIPS (Swissmedic) » si tu ne les as pas lues.",
        "sources": ["…"]
      },
      "audit": {"autocontrole": "voir section 5", "points_a_verifier": ["…"]}
    }
  ]
}
```

- `options` est vide pour une Kprim, et `statements` est vide pour une A et un menu long.
- **Chaque option et chaque énoncé porte son `why`** : c'est la réponse commentée. Un `why` explique la raison clinique, pas « c'est faux ».

---

## 3. Skills à porter, par toi et par tes agents

Si ton environnement sait charger des skills, charge-les avant de produire. Sinon, applique leurs règles, résumées ici. Chaque agent qui produit un SSP charge le même jeu.

| Skill | Rôle dans ce travail |
|---|---|
| **skill-creator** | Transformer en skill toute procédure qui revient deux fois (gabarit de vignette, contrôle de couverture) et la partager à tous les agents. |
| **panoramic-skill-finder** | Au départ et à chaque palier, repérer ce qui peut s'automatiser sans perte de qualité. |
| **harness-for-work** | Équiper chaque agent avant la tâche : skills, sources, scripts. |
| **harness-for-long** | Tenir un fichier de reprise (SSP faits, SSP en cours, points ouverts) pour ne rien perdre entre deux sessions. |
| **harness-gen-network** | Répartir le travail en agents par SSP et confier le mécanique à des scripts. |
| **perfect-skill-user-organizer-collector** | Donner à chaque agent le bon jeu de skills et éviter les doublons. |
| **medical-accuracy-100** | Vérifier et sourcer chaque chiffre, seuil, critère et posologie. Ne jamais rien inventer. |
| **switzerland-medical-professor** | Cadre réglementaire et pratique suisses, et niveau de l'examen fédéral. |
| **ultra-competent-fast-doctor** | Raisonnement clinique de niveau expert, discriminants, décision. |
| **concept-corelator** | Relier chaque notion à sa chaîne : physiopathologie, sémiologie, examen, traitement. |
| **medical-workout** | Noms et visées exacts des examens complémentaires. |
| **psych-ultra-ch** | Tout SSP ou diagnostic psychiatrique (CIM-10 et CIM-11, AMDP, cadre légal). |
| **paramedic-psuke-collabo** | Rôle des autres professions et institutions (réseau, assurances, APEA). |
| **all-sector-jurist-savant** | Questions de droit suisse : PAFA, APEA, LAA, LAMal, LAVI, secret médical. |
| **i-write-so-fast** | Rédiger vite et bien : squelette, gabarit, une passe dense. |
| **med-text-contractor** | Contracter les corrections sans perdre une notion. |
| **french-language-best-writer** | Un français clair, en phrases verbales. |
| **all-context-ultrasystematic** | Le même gabarit pour chaque diagnostic, avec contrôle mécanique d'exhaustivité. |
| **i-never-waste-token** | Lecture ciblée des sources, sans relire ce qui est déjà acquis. |
| **optimisation-par-cache-hache-autorun** | Ne jamais reproduire un diagnostic déjà produit : empreinte de l'entrée, saut si elle est connue. |

---

## 4. Verrouillage sur la pratique clinique suisse

Ces règles l'emportent sur toute source étrangère. Quand une source étrangère et une source suisse divergent, tu suis la source suisse et tu signales l'écart dans `pieges` ou `points_a_verifier`.

1. **Ordre des sources :**
   - d'abord les sources suisses : Swissmedic (AIPS, compendium.ch), OFSP, plan de vaccination suisse en vigueur, CFIST, sociétés suisses (SSMI, SSGO, SSP, SGK…), smarter medicine, HUG, CHUV, Tox Info Suisse ;
   - ensuite les recommandations européennes (ESC, ERS, EULAR, ESMO, KDIGO, EASL…) ;
   - ensuite les recommandations internationales (NICE, IDSA…) ;
   - la littérature (PubMed) en dernier.
2. **Médicaments :** n'utilise que les médicaments autorisés en Suisse, avec leur DCI. Toute posologie porte « à vérifier dans l'AIPS (Swissmedic) », sauf si tu as lu l'AIPS toi-même. Ne donne jamais une molécule absente du marché suisse comme traitement de référence.
3. **Unités :** utilise les unités SI suisses (mmol/l, µmol/l, kPa pour les gaz du sang, g/l). Écris un pourcentage seulement là où l'usage suisse le garde (HbA1c en % et en mmol/mol).
4. **Système de santé :**
   - assurances et prestations : LAMal, OPAS, Liste des spécialités, Liste des analyses, LiMA, TARDOC, LAA (accidents), AI et AVS ;
   - accès aux soins : médecin de famille, centre d'urgence, 144 (ambulance), 145 (Tox Info Suisse), 143 et 147 (soutien psychologique) ;
   - droit : APEA, PAFA (art. 426 ss CC), LAVI (aide aux victimes), déclaration obligatoire à l'OFSP.
5. **Repères récents à respecter :** la PEP VIH doit être débutée au plus tard 48 h après l'exposition (CFIST 2025), alors que la PEP contre le VHB reste possible jusqu'à 72 h. Le dépistage du cancer colorectal est remboursé de 50 à 74 ans.
6. **Cas cliniques :**
   - situe-les dans des lieux suisses neutres (« un cabinet de médecine de famille à Fribourg », « les urgences d'un hôpital régional ») ;
   - **n'utilise jamais le CNP (Centre neuchâtelois de psychiatrie) ni l'ancien CPCM** comme lieu ;
   - n'emploie aucun nom réel de patient ni de soignant.
7. **Langue :** écris en français de Suisse romande, en phrases verbales. Tu vouvoies l'étudiant dans l'énoncé, et la correction reste neutre.
8. **Contenu sensible** (suicide, intoxication volontaire, violences) : prends l'angle de l'examen, c'est-à-dire l'évaluation, la protection, le cadre légal et le réseau. Ne donne jamais de dose létale ni de méthode.

---

## 5. Système d'audit

Il y a 3 niveaux d'audit. Un fichier n'est livré que s'il passe les niveaux 1 et 2.

**Niveau 1 : autocontrôle de l'agent, mécanique, avant la livraison.**
Pour chaque diagnostic, l'agent vérifie et écrit dans `audit.autocontrole` :
- le nombre de QCM par format : 14 A, 4 Kprim, 2 menus longs (ou 6, 1 et 1 pour un SSP+) ;
- que chaque A a exactement 1 juste parmi 5 options, chaque Kprim exactement 4 énoncés, et chaque menu long entre 1 et 3 justes, avec le bon nombre annoncé dans l'énoncé ;
- la difficulté : au moins 25 % de niveau 4–5, et au moins 2 de niveau 1–2 ;
- que chaque question de niveau 4–5 a `diagnosticMasque: true` et que sa vignette, son prompt et ses options correctes ne nomment pas le diagnostic, ni un de ses synonymes ;
- que chaque option et chaque énoncé porte un `why` non vide ;
- que chaque notion de poids 3 apparaît dans au moins 2 questions, et chaque notion de poids 2 dans au moins 1 ;
- que chaque question cite au moins une source ;
- que le JSON est valide et que les `id` sont uniques.

**Niveau 2 : audit croisé par un second agent qui n'a pas produit le fichier.**
- Il relit chaque chiffre, seuil, posologie et critère contre la source citée, et vérifie la règle suisse de la section 4.
- Il vérifie que la réponse juste est juste, et seule juste quand une seule est attendue.
- Il vérifie que chaque distracteur est plausible, mais faux pour une raison clinique claire.
- Il classe chaque écart : 🟥 erreur médicale, à corriger avant livraison ; 🟧 imprécision ou source manquante, à marquer « à vérifier » ; 🟩 conforme.
- Il ajoute au JSON un bloc `"auditCroise": {"agent": "…", "verdict": "🟩 | 🟧 | 🟥", "ecarts": [...]}`.

**Niveau 3 : contrôle final par le dépôt Jeux_45_Spec, à l'arrivée.**
- Les fichiers passent la validation du schéma, le contrôle des menus longs et le test de l'arène.
- Un échec renvoie le fichier à son agent, avec la liste des erreurs.

**Règles absolues :**
- Ne cite jamais une source que tu n'as pas lue toi-même, ni une source lue seulement par un commentaire ou un résumé de tiers.
- N'invente jamais un DOI, un PMID ou une année.
- Écris « à vérifier » partout où une source manque.

---

## 6. Rythme et reprise

- Travaille SSP par SSP, dans l'ordre de la section 2. Un agent prend un SSP entier et livre un fichier.
- Après chaque SSP, mets à jour un fichier `REPRISE_<CAT>.md`. Il indique les SSP livrés, le SSP en cours, les points « à vérifier » et les écarts d'audit restés ouverts.
- Avant de produire un diagnostic, vérifie qu'il n'est pas déjà livré (empreinte : `id` du diagnostic et version du JSON reçu).
- À la fin de chaque catégorie, rends un rapport court : nombre de SSP et de QCM, répartition des difficultés, verdicts d'audit, points à vérifier. **Ne recopie aucun QCM dans ce rapport.**

Signature : AAI (Anthropic AI)
