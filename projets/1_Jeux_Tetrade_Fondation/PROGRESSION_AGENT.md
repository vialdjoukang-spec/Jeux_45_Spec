# Progression de l'agent Tétrade — rapport à Claude (garant médical)

Signature : AAI (Anthropic AI) · branche `agent/tetrade` · 2026-11-24

## 1. Système hématologique et oncologique : jouable

| Élément | Valeur |
|---|---|
| Organes rédigés | 6 (moelle osseuse, globules rouges, globules blancs, plaquettes et hémostase, rate, ganglions lymphatiques) |
| Organe en renvoi | Thymus → Endocrinien (maison unique, `LIENS`) |
| Volets propres | 10 (`V` dans `hemato/contenu.txt`) |
| Mots-clés d'anatomie et de physiologie | 63 (anatomie → vue 3D ; physiologie → 7 fenêtres de courbe) |
| Sémiologie | 5 temps d'examen, 13 temps par organe, 39 signes (typiques et atypiques) |
| Pathologies | 45 : 8 TF, 18 F, 13 U, 6 R (chaque organe a ses 4 paliers) |
| Glossaire | 83 sigles nouveaux |
| Fenêtres nouvelles | `he_anemie`, `he_fer`, `he_coag` (+ réutilisées : `odc`, `do2`) |
| Interprétations corrélées | 20 scénarios nouveaux (`he_*`) |

Répartition des pathologies par organe : moelle 9, globules rouges 8, globules blancs 6, plaquettes et hémostase 9, rate 6, ganglions 7.

## 2. Changements de moteur

- `systeme_source.py` lit un champ facultatif `aVerifier:` par pathologie ; il entre dans la bulle et porte le doute au lieu d'une affirmation.
- `construire_config_tetrade.py` : entrée `Thymus` dans `LIENS`.
- `systemes_rediges.py` : une ligne `Hématologique & oncologique` (préfixe `he_`, couleur `#a33`).
- `projets/retours/migrations_ids.json` : 6 renommages `org_hemato_*` → `he_*`.

## 3. Vérifications passées (avant chaque push)

- `python3 conception/outils/construire_config_tetrade.py` → 2756 nœuds, 50 organes encore à produire.
- `python3 conception/outils/construire_plans.py` puis `generer_json.py` puis `rendre_plans.py` → plans 31/31.
- `python3 projets/outils/audit_fond.py` → 0 correction, 815 examens fiables.
- `python3 conception/outils/auditer_conception.py` → **RÉUSSI 34/34**.
- `python3 conception/outils/auditer_couverture.py` → **RÉUSSI**.
- `python3 projets/outils/non_perte.py` → **OK (0 perte)**, après restauration de `2_cou/ganglions_cervicaux.json` (anomalie préexistante sur main : dédoublonnage IGRA par `generer_json.py`).
- `python3 projets/outils/verifier_interpretations.py` → 138/138, **0 défaut**.
- Playwright sans écran (routage de fichiers) sur `he_anemie`, `he_fer`, `he_coag` : tous les scénarios et les curseurs aux extrêmes, **0 erreur JS**, valeurs plausibles ; rendu canvas contrôlé visuellement.

## 4. Sources vérifiées en ligne pendant la production

- Consensus suisse sur la carence martiale (Nowak, Swiss Med Wkly 2019) : seuils de ferritine 30 et 100 µg/l, saturation 20 %, fer IV au plus 1000 mg ou 20 mg/kg par semaine.
- Mise à jour ASH 2026 du PTI (résumé des changements) : seuil 30 G/l inchangé ; prednisone au plus 6 semaines ou dexaméthasone 40 mg × 4 jours ; association d'emblée possible au rituximab ou à un agoniste de la thrombopoïétine.
- CHUV 2026 (asplénie, d'après OFSP/CFV 2015, complément méningocoques 2024 et plan suisse 2026) : vaccins, antibiotique de réserve amoxicilline-clavulanate 2 g puis 1 g × 2, moxifloxacine 400 mg.
- Swissmedic SwissPAR 2021 : andexanet alfa (Ondexxya) autorisé en Suisse.

## 5. Points `aVerifier` (à trancher par Claude ou dans l'AIPS)

- **Syndrome myélodysplasique** : Les doses d'époétine et de darbépoétine varient selon les centres ; le luspatercept et son remboursement en Suisse restent à vérifier.
- **Amylose AL** : L'année et la revue de la recommandation ISA-EHA (Wechalekar) restent à confirmer.
- **Anémie ferriprive** : Le carboxymaltose ferrique peut causer une hypophosphatémie ; la fréquence du contrôle du phosphate reste à préciser selon l'AIPS.
- **Carence en vitamine B12** : Le rythme d'entretien de la vitamine B12 intramusculaire diffère selon la molécule (cyanocobalamine ou hydroxocobalamine) ; à confirmer dans l'AIPS.
- **Crise drépanocytaire et syndrome thoracique** : Le seuil de saturation pour l'oxygène et le protocole d'antalgie varient selon les centres suisses.
- **Réaction transfusionnelle hémolytique aiguë** : Une mise à jour de la recommandation BSH de 2012 sur les réactions transfusionnelles aiguës reste à rechercher.
- **Hémoglobinurie paroxystique nocturne** : Le statut suisse des inhibiteurs proximaux du complément (iptacopan, pegcetacoplan) reste à vérifier dans l'AIPS.
- **Neutropénie isolée modérée** : La référence de Merz 2023 sur le nombre de neutrophiles du phénotype Duffy négatif reste à confirmer.
- **Agranulocytose médicamenteuse** : L'effet du G-CSF sur la durée de l'agranulocytose reste discuté ; sa prise en charge par l'assurance pour cette indication reste à vérifier.
- **Purpura thrombopénique immunologique** : La mise à jour ASH 2026 a été lue dans son résumé des changements seulement ; le texte complet et sa reprise par les hématologues suisses restent à vérifier.
- **Hémophilie A acquise** : L'indication de l'émicizumab dans l'hémophilie acquise et son statut suisse restent à vérifier dans l'AIPS.
- **Asplénie et hyposplénie** : Le vaccin conjugué contre le pneumocoque recommandé (valence) et l'intervalle du vaccin contre le méningocoque B changent avec le plan de vaccination suisse ; à vérifier sur le plan en vigueur.
- **Infarctus splénique** : La référence de Brett (2020) reste à confirmer ; la conduite repose surtout sur des séries de cas.
- **Maladie de Kikuchi-Fujimoto** : La référence de la série de Dumas (2014) reste à confirmer ; la conduite repose sur des séries de cas et l'avis d'expert.
Autres points ouverts : les posologies portent toutes « à vérifier dans l'AIPS » ; les chimiothérapies (myélome, leucémies, lymphomes, amylose) restent décidées et dosées par l'hématologue ou l'oncologue, sans dose chiffrée.

## 6. Système infectieux et immunitaire : jouable

| Élément | Valeur |
|---|---|
| Organes rédigés | 4 (barrières, immunité innée, immunité adaptative, complément) |
| Organe en renvoi | « Organes lymphoïdes » → Hématologique (moelle, rate, ganglions) et Endocrinien (thymus) ; MALT décrit aux barrières |
| Volets propres | 8 |
| Mots-clés | 32 |
| Sémiologie | 4 temps d'examen, 11 temps par organe, 28 signes |
| Pathologies | 17 : 3 TF, 5 F, 5 U, 4 R (barrières 4, innée 5, adaptative 5, complément 3 sans palier TF) |
| Glossaire | 31 sigles nouveaux |
| Fenêtre nouvelle | `ii_anticorps` (IgM et IgG, réponse primaire et secondaire, déficit humoral) + 4 interprétations |

Pathologies laissées à leur maison pour éviter les doublons : choc septique (cardiovasculaire), méningites (neurologique), fièvre méditerranéenne familiale et angio-œdème bradykinique (déjà rédigés).

Source vérifiée en ligne : Swiss TPH, recommandations de traitement du paludisme (31.01.2023) — forme grave dès 2 % de parasitémie chez le non-immun ; artésunate 2,4 mg/kg à 0, 12 et 24 h ; artéméther-luméfantrine sur 5 jours.

### Points `aVerifier` (infectieux et immunitaire)

- **Érysipèle** : La recommandation suisse de la SSI (ssi.guidelines.ch) sur l'érysipèle n'a pas été lue ; dose et durée de l'amoxicilline à confirmer avec elle.
- **Syndrome de choc toxique** : La dose d'immunoglobulines intraveineuses dans le choc toxique streptococcique varie selon les séries ; elle reste à confirmer avec l'infectiologue.
- **Urticaire aiguë** : La dose de prednisone de la cure courte n'est pas fixée par la recommandation ; elle reste à confirmer.
- **Maladie de Still de l'adulte** : Le remboursement de l'anakinra dans la maladie de Still de l'adulte en Suisse reste à vérifier.
- **Mononucléose infectieuse** : Les deux références (Dunmire 2015, Becker 2014) restent à confirmer ; la durée d'arrêt du sport repose sur l'avis d'expert.
- **Nécrolyse épidermique toxique** : L'efficacité de la ciclosporine et des immunoglobulines reste débattue ; la conduite suit le centre spécialisé.
- **Angio-œdème héréditaire** : Le statut suisse et le remboursement du bérotralstat et de la prophylaxie par lanadélumab restent à vérifier dans l'AIPS.
- **Purpura fulminans méningococcique** : Le délai exact de déclaration et le schéma de chimioprophylaxie de l'OFSP restent à confirmer sur le site de l'OFSP.

## 7. Vérifications après fusion de origin/main (transversal fusionné entre-temps)

- Conflit unique dans `REPRISE.md`, résolu en gardant les deux sections.
- Chaîne complète relancée : conception **34/34**, couverture **RÉUSSI**, non-perte **OK**, interprétations **142/142, 0 défaut**, Playwright 0 erreur sur `ii_anticorps`.
- Bruit de régénération non commité : `trans_s_s4_01.json` (simple réindentation par `generer_json.py`), `ganglions_cervicaux.json` (dédoublonnage IGRA), PDF.

## 9. Système locomoteur et rhumatologique : jouable (branche `agent/tetrade-loco`)

| Élément | Valeur |
|---|---|
| Organes rédigés | 11 (crâne et face, rachis, épaule, coude-poignet-main, bassin et hanche, genou, cheville et pied, os, articulations et synoviale, muscles, tendons-ligaments-bourses) |
| Volets propres | 9 (`V` dans `loco/contenu.txt`) |
| Mots-clés | 71 (anatomie → vue 3D ; physiologie → 3 fenêtres : `lo_synovie`, `lo_ck`, `en_calcium` réutilisée) |
| Sémiologie | 6 temps d'examen, 30 temps par organe, 70 signes (61 typiques, 9 atypiques) |
| Pathologies | 57 : 13 TF, 21 F, 12 U, 11 R (chaque organe a ses 4 paliers) |
| Glossaire | 26 sigles nouveaux |
| Interprétations corrélées | 13 scénarios nouveaux (`lo_synovie` 7, `lo_ck` 6) |

Répartition : articulations 7, muscles 7, rachis 6, coude-poignet-main 6, genou 5, cheville et pied 5, os 5, crâne et face 4, épaule 4, bassin et hanche 4, tendons 4.

Renvois sans doublon (maison unique) : ostéoporose, ostéomalacie et Paget → Endocrinien ; radiculopathie, canal lombaire étroit, queue de cheval, spondylodiscite, canal carpien, nerf ulnaire, myasthénie → Neurologique ; artérite à cellules géantes → Cardiovasculaire ; Still et fasciite nécrosante → Infectieux ; Sjögren → Digestif ; myélome → Hématologique. Les bulles d'organe et les « confusion » nomment la maison.

Changements de moteur : une ligne `Locomoteur & rhumatologique` dans `systemes_rediges.py` (préfixe `lo_`, couleur `#6b7280`) ; 2 modèles canvas dans `fenetres.js` ; 11 renommages `org_locomo_*` → `lo_*` dans `projets/retours/migrations_ids.json`. Aucun changement de `systeme_source.py` ni de `construire_config_tetrade.py` (aucun organe partagé).

Vérifications : chaîne complète **RÉUSSIE** (conception 34/34, couverture, non-perte 0, audit du fond, plans 31/31, interprétations 155/155) ; Playwright sans écran sur `lo_synovie` et `lo_ck` : tous les scénarios et curseurs aux extrêmes, **0 erreur JS**.

Sources vérifiées en ligne : Wüthrich, Alromaih et So, Swiss Med Wkly 2016;146:w14341 (goutte, perspective suisse) ; Gjika et al., Ann Rheum Dis 2019 (arthrite septique : 2 contre 4 semaines après drainage, Genève).

### Points `aVerifier` (locomoteur et rhumatologique)

- **Fracture du plancher de l'orbite** : L'antibioprophylaxie dans les fractures de l'orbite reste débattue et aucune recommandation suisse n'a été lue ; la durée et l'indication restent à confirmer avec le chirurgien maxillo-facial.
- **Lombalgie commune** : Une recommandation suisse dédiée (Société suisse de rhumatologie ou de médecine interne) sur la lombalgie commune n'a pas été lue ; la place du paracétamol, jugé peu efficace par NICE, reste à confirmer.
- **Cervicalgie commune** : La référence Côté 2016 (consensus de l'Ontario) reste à confirmer.
- **Tassement vertébral ostéoporotique** : L'année exacte de la dernière version des recommandations de l'Association suisse contre l'ostéoporose reste à confirmer sur le site de l'association.
- **Traumatisme du rachis cervical** : La cible de pression artérielle moyenne et sa durée après une lésion médullaire aiguë restent à confirmer dans la recommandation AO Spine.
- **Tendinopathie de la coiffe des rotateurs** : La référence AAOS 2019 et la place exacte des ondes de choc dans les calcifications restent à confirmer.
- **Capsulite rétractile** : La recommandation britannique sur la capsulite (année, revue) reste à confirmer.
- **Luxation antérieure gléno-humérale** : Aucune recommandation suisse sur la luxation d'épaule n'a été lue ; la durée d'immobilisation varie selon l'âge et les équipes.
- **Luxation postérieure méconnue de l'épaule** : La référence Robinson et Aderinto 2005 reste à confirmer.
- **Phlegmon des gaines des fléchisseurs** : Le schéma antibiotique empirique et sa durée totale restent à confirmer avec l'infectiologue et selon les recommandations SSI.
- **Syndrome douloureux régional complexe** : Le bisphosphonate validé dans cette indication (néridronate) n'est pas autorisé en Suisse à notre connaissance ; la molécule et la dose restent à vérifier dans l'AIPS.
- **Ostéonécrose de la tête fémorale** : La référence de la classification ARCO 2019 reste à confirmer.
- **Rupture du tendon d'Achille** : L'indication de la thromboprophylaxie lors de l'immobilisation d'un membre inférieur varie selon le score de risque ; à confirmer selon la pratique suisse.
- **Ostéite du pied diabétique** : Le choix de l'antibiotique empirique et ses doses doivent suivre l'infectiologue et la recommandation SSI ; aucune dose n'est fixée ici.
- **Fracture ouverte** : L'ajout d'un aminoside pour les fractures de type III varie selon les recommandations ; à confirmer avec l'infectiologue.
- **Crise de goutte** : La spécialité de colchicine disponible en Suisse et sa dose maximale journalière restent à vérifier dans l'AIPS ; le dépistage HLA-B*58:01 avant l'allopurinol se discute chez les patients d'origine asiatique.
- **Arthrite septique** : Le choix empirique entre flucloxacilline et céfazoline suit l'épidémiologie locale ; à confirmer avec la recommandation SSI et l'infectiologue.
- **Arthrite de Lyme** : Une recommandation suisse récente sur la borréliose (SSI) n'a pas été lue ; le schéma reste à confirmer avec elle.
- **Fibromyalgie** : L'autorisation de la duloxétine et de la prégabaline dans la fibromyalgie en Suisse reste à vérifier dans l'AIPS.
- **Rhabdomyolyse** : Le débit de diurèse visé et la place des bicarbonates reposent sur des données faibles ; à confirmer avec le néphrologue.
- **Myosite inflammatoire** : Aucune recommandation thérapeutique européenne complète n'a été lue ; les doses des immunosuppresseurs restent du ressort du spécialiste.
- **Bursite mécanique** : La référence Baumbach 2014 reste à confirmer.
- **Bursite septique** : Les deux références genevoises (Perez 2010, Uçkay 2017) et la durée exacte retenue restent à confirmer.
- **Tendinopathie aux fluoroquinolones** : La date et le contenu exacts de la communication de Swissmedic sur les fluoroquinolones restent à confirmer.

Autres points ouverts : toutes les posologies portent « à vérifier dans l'AIPS » ; les biothérapies, inhibiteurs de JAK, immunosuppresseurs et chimiothérapies des sarcomes restent décidés par le spécialiste, sans dose chiffrée.

## 8. Suite proposée

- Audit médical de Claude sur `hemato/pathologies.txt`, `infectio/pathologies.txt` et les 24 interprétations `he_*` et `ii_*`, puis fusion sur main.
- Locomoteur fait (section 9) : audit médical de Claude sur `loco/pathologies.txt` et les 13 interprétations `lo_*`, puis fusion.
- Système suivant : dermatologique (les infections cutanées de l'érysipèle y renverront).
- Correctif conseillé à `generer_json.py` : écrire les leçons transversales avec la même indentation que leur source et ne plus dédoublonner l'IGRA, pour que la régénération ne produise plus de bruit.
