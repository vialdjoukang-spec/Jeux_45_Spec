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

> Audit médical du 2026-11-24 : 15 des 22 points sont résolus et sourcés ; 7 restent ouverts avec leur raison (voir `AUDIT_TETRADE.md`). La liste ci-dessous garde l'état d'avant l'audit.

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

## 10. Système dermatologique : jouable (branche `agent/tetrade-loco`)

| Élément | Valeur |
|---|---|
| Organes rédigés | 6 (épiderme, derme et hypoderme, poils et cheveux, ongles, glandes sudorales et sébacées, muqueuses) |
| Volets propres | 7 |
| Mots-clés | 32 (anatomie → vue 3D ; physiologie → fenêtre nouvelle `de_brulure`, formule de Parkland) |
| Sémiologie | 5 temps d'examen, 12 temps par organe, 30 signes (27 typiques, 3 atypiques) |
| Pathologies | 32 : 7 TF, 14 F, 5 U, 6 R (les ongles n'ont pas de palier « urgence » propre) |
| Glossaire | 27 sigles nouveaux |
| Interprétations corrélées | 4 scénarios `de_brulure` |

Renvois sans doublon : érysipèle, fasciite nécrosante, nécrolyse épidermique toxique, urticaire aiguë et angio-œdème → Infectieux ; zona → Neurologique ; Raynaud primaire → Cardiovasculaire ; aphtose et Sjögren → Digestif ; lupus systémique, rhumatisme psoriasique et myosites → Locomoteur ; SOPK → Endocrinien. **L'érysipèle de l'infectieux renvoie désormais vers Dermatologique** (portes d'entrée : ulcère veineux, escarre, onychomycose). Les muqueuses génitales sont nommées sans aucune image.

Changements de moteur : une ligne `Dermatologique` dans `systemes_rediges.py` (préfixe `de_`, couleur `#b07a5a`) ; 1 modèle canvas `de_brulure` ; 6 renommages `org_dermat_*` → `de_*` déclarés. Vérifications : chaîne complète réussie (34/34, couverture, non-perte 0, interprétations 159/159) ; Playwright 0 erreur JS sur `de_brulure`.

### Points `aVerifier` (dermatologique)

- **Psoriasis en plaques** : L'année et la revue de la dernière mise à jour de la recommandation EuroGuiDerm sur le psoriasis restent à confirmer.
- **Mélanome** : La recommandation suisse sur le mélanome (Swiss Melanoma Guidelines) n'a pas été lue ; le rythme du suivi suisse reste à confirmer.
- **Eczéma herpeticum** : La dose et la durée du valaciclovir dans l'eczéma herpeticum de l'adulte restent à confirmer ; aucune recommandation dédiée n'a été lue.
- **Brûlure étendue** : Le volume initial de remplissage (2 ou 4 ml/kg par % de surface) varie selon les centres ; à confirmer avec le protocole des centres suisses des brûlés.
- **Sclérodermie systémique** : Une mise à jour EULAR plus récente (2023) sur la sclérodermie existerait ; à confirmer.
- **Alopécie androgénétique** : L'usage du minoxidil oral à faible dose, hors autorisation en Suisse, reste à vérifier.
- **Pelade** : L'autorisation et le remboursement du baricitinib dans la pelade sévère en Suisse restent à vérifier dans l'AIPS ; la référence Meah 2020 reste à confirmer.
- **Acné vulgaire** : La version la plus récente de la recommandation européenne sur l'acné et les conditions suisses de prescription de l'isotrétinoïne restent à vérifier.
- **Hyperhidrose primaire** : La référence Nawrocki et Cha 2019 et le remboursement suisse de la toxine botulique dans l'hyperhidrose restent à vérifier.
- **Coup de chaleur** : La référence de la Wilderness Medical Society (2019) et la cible d'arrêt du refroidissement restent à confirmer.
- **Lichen plan buccal** : Aucune recommandation européenne sur le lichen plan buccal n'a été lue ; le rythme de surveillance reste à confirmer.
- **Érythème polymorphe majeur** : La place des corticoïdes systémiques dans l'érythème polymorphe majeur reste discutée ; aucune recommandation n'a été lue.

## 8. Suite proposée

- Audit médical de Claude sur `hemato/pathologies.txt`, `infectio/pathologies.txt` et les 24 interprétations `he_*` et `ii_*`, puis fusion sur main.
- Locomoteur et dermatologique : audit médical de Claude fait le 2026-11-24 (AUDIT_TETRADE.md, lot 2 : 17 doutes résolus, 19 restants) ; fusion sur main à décider.
- Système suivant : ophtalmologique et ORL.
- Correctif conseillé à `generer_json.py` : écrire les leçons transversales avec la même indentation que leur source et ne plus dédoublonner l'IGRA, pour que la régénération ne produise plus de bruit.

## 9. Système ophtalmologique et ORL : jouable (branche `agent/tetrade-orl`, 2026-11-24)

Le plan (`conception/plans/tetrade.plan.json`) regroupe l'œil et l'ORL en un seul système « Ophtalmologique & ORL » de 9 organes : l'agent a suivi ce regroupement.

| Élément | Valeur |
|---|---|
| Organes rédigés | 5 (paupières et voies lacrymales, globe oculaire, voies optiques, oreille externe et moyenne, oreille interne) |
| Organes en renvoi (`LIENS`) | 4 : Nez et sinus → Respiratoire (Fosses nasales et sinus) ; Cavité buccale et pharynx → Digestif et Respiratoire ; Larynx → Respiratoire ; Glandes salivaires → Digestif |
| Volets propres | 9 (`V` dans `orl/contenu.txt`) |
| Mots-clés d'anatomie et de physiologie | 75 (anatomie → vue 3D ; physiologie → 12 ouvrent une fenêtre de courbe) |
| Sémiologie | 8 temps d'examen, 15 temps par organe, 46 signes (typiques, atypiques, 1 signe unique assumé : déficit pupillaire afférent) |
| Pathologies du système | 40 : 11 TF, 16 F, 8 U, 5 R après l'audit (sécheresse oculaire reclassée TF ; chaque organe a ses 4 paliers) |
| Pathologies ajoutées aux maisons | 5 : polypose nasosinusienne (F) et carcinome du nasopharynx (R) aux fosses nasales, carcinome de l'oropharynx (F) au pharynx, carcinome du larynx (F) au larynx, tumeur de la parotide (F) à la cavité buccale |
| Glossaire | 26 sigles nouveaux (`orl/glossaire.txt`) + 3 au glossaire respiratoire |
| Fenêtres nouvelles (canvas) | `or_refraction` (œil réduit, accommodation de Hofstetter), `or_pio` (équation de Goldmann), `or_audio` (audiogramme tonal, grades OMS 2021) |
| Interprétations corrélées | 18 scénarios nouveaux (`or_*`), statut AUDITÉ (2026-11-24) |

Répartition par organe : paupières 7, globe 12, voies optiques 6, oreille externe et moyenne 8, oreille interne 7.

Renvois sans doublon vers le système neurologique (par nom) : paralysie faciale de Bell, schwannome vestibulaire, paralysies oculomotrices, myasthénie oculaire, artérite à cellules géantes, migraine, AVC ; vers l'endocrinien : adénome hypophysaire et apoplexie.

### Changements de moteur

- `systemes_rediges.py` : une ligne `Ophtalmologique & ORL` (préfixe `or_`, couleur `#5b6574`).
- `construire_config_tetrade.py` : 4 entrées `LIENS` (Nez et sinus, Cavité buccale et pharynx, Larynx, Glandes salivaires).
- `fenetres.js` : 3 modèles canvas ; aucune fonction existante modifiée.
- `projets/retours/migrations_ids.json` : 5 renommages `org_ophtal_*` → `or_*`. Les 4 organes en renvoi gardent leur identifiant `org_ophtal_*` (dont `org_ophtal_larynx`, qui porte un modèle 3D produit).
- Non fait, à décider par un humain : purger un `aVerifier` levé dans la source lors de la régénération (défaut relevé dans `AUDIT_TETRADE.md`). La correction exige d'assouplir `non_perte.py` ; l'agent n'a pas touché à la garde.

### Vérifications passées avant le push

- `construire_config_tetrade.py` → 3109 nœuds, 36 organes encore à produire.
- `construire_plans.py`, `generer_json.py`, `rendre_plans.py` → plans écrits, PDF générés (non commités).
- `audit_fond.py` → 0 correction, 815 examens fiables.
- `auditer_conception.py` → **RÉUSSI 34/34** ; `auditer_couverture.py` → **RÉUSSI**.
- `non_perte.py` → **OK (0 perte)**, après restauration des deux `2_cou/ganglions_cervicaux.json` depuis main (défaut IGRA connu).
- `verifier_interpretations.py` → **160/160, 0 défaut**.
- Playwright sans écran (routage de fichiers) : `or_refraction`, `or_pio`, `or_audio`, tous les scénarios et tous les curseurs aux extrêmes, **0 erreur JS**, valeurs plausibles (emmétropie 0 D, myopie axiale −4,75 D, PIO normale 16 mmHg, crise de fermeture 62 mmHg, otosclérose avec encoche de Carhart, surdité brusque 65 dB HL).

### Sources vérifiées en ligne pendant la production

- SGRM 2024 (fiche vision, d'après l'OAC annexe 1) : groupe 1, acuité 0,5 au meilleur œil et 0,2 à l'autre (0,6 si un seul œil) ; champ binoculaire horizontal d'au moins 120 degrés, 50 de chaque côté, 20 en haut et en bas ; champ central normal jusqu'à 20 degrés.
- Mémento AVS 3.07 (état au 1er janvier 2023) : forfait de 630 francs pour une oreille, 1237,50 francs pour les deux, au plus tous les 5 ans.
- Plebani, Paediatrica 2023;34(1) (CHUV) : antibiotique d'emblée avant 2 ans, otite bilatérale ou perforée ; amoxicilline 25 mg/kg 2 fois par jour (au plus 1 g), 5 jours dès 2 ans, 10 jours avant 2 ans ou si perforation.
- PubMed : chaque référence datée a été confrontée à sa notice (Owen 2019, Mac Grory 2021, Bartalena 2021, Chandrasekhar 2019, Basura 2020, Rosenfeld 2014 et 2016, Schwartz 2017, Bhattacharyya 2017, Stachler 2018, Carelli 2017, Petzold 2022, Mollan 2018, Friedman 2013, Strupp 2004, Kattah 2009, Minor 1998, Yung 2017, Lopez-Escamez 2015, Adrion 2016, Dua 2001, Gazzard 2019, Yam 2019, Schmidt-Erfurth 2014, Jabs 2005, Chandler 1970, Bossi 2021, Machiels 2020, AAO Blepharitis 2024, Conjunctivitis 2024, PVD 2025).

### Points `aVerifier` (19 ; audités le 2026-11-24 : 7 résolus, 12 restants, voir `AUDIT_TETRADE.md`, lot 3)

Sécheresse oculaire (TFOS DEWS III) ; blépharite (dose de doxycycline) ; dacryocystite et cellulite orbitaire (schéma antibiotique) ; orbitopathie (téprotumumab en Suisse) ; myopie (atropine faible en Suisse) ; DMLA (mise à jour après EURETINA 2014) ; rétinopathie diabétique (intervalle suisse) ; occlusion de l'artère centrale (thrombolyse) ; kératite amibienne (polihexanide en Suisse) ; ischémie du nerf optique (15 % de l'œil adelphe) ; Leber (idébénone en Suisse) ; otite moyenne (dose adulte) ; otite externe (spécialité suisse) ; mastoïdite et otite nécrosante (antibiotiques) ; névrite vestibulaire (corticoïdes) ; traumatisme sonore (corticoïdes, seuil Suva) ; polypose (dupilumab, Liste des spécialités). Toutes les posologies gardent « à vérifier dans l'AIPS ».

### Suite proposée

- Audit médical de Claude sur `orl/pathologies.txt`, les 5 ajouts des maisons et les 18 interprétations `or_*`, puis fusion sur main (après la branche `agent/tetrade-loco`).
- Production des modèles 3D des 5 organes `or_*` (absents de `anatomie3d/index.json`, comme les organes `he_*`).

Signature : AAI (Anthropic AI)

## 11. Arène Tétrade : 108 questions jouables (branche `agent/tetrade-arene`, 2026-11-24)

| Élément | Valeur |
|---|---|
| Paquets | 11 `tetrade_<dossier>` (un par système rédigé sur main) |
| Questions | 108 : 92 type A (5 options, 1 juste), 16 Kprim (4 affirmations) |
| Répartition | cardio 12, neuro 12, respi 11, digestif 11, endocrino 11, hémato 10, rénal 10, ORL 9, loco 8, infectio 7, derma 7 |
| Interprétations de courbes | 30 questions liées à une courbe (`I` : ecg, spiro, gazometrie, fena, osmo, en_tsh_t4, he_fer, or_audio, lo_ck…) |
| Correction | explication par option + échelle mécanisme / discriminant / ancre |

Fonctionnement (0 token) : les sources sont du texte, `conception/donnees/tetrade/arene/<dossier>.txt` (format en tête de `cardio.txt`). `construire_arenes.py` les lit, rattache chaque question à une pathologie rédigée (`X nom exact`) dont la ligne `s` devient la source affichée, et **échoue bruyamment** si : type A sans 5 options ou sans réponse unique, Kprim sans 4 affirmations, explication vide, pathologie inconnue, ou **titre qui contient un mot du diagnostic**. Aucune référence nouvelle n'est donc créée : la source est celle de la pathologie déjà auditée.

Contrôles : chaîne complète réussie (conception 34/34, couverture, non-perte 0, interprétations 177/177, plans 31/31) ; `conception/outils/tests/test_arene_tetrade.py` (Playwright sans écran, routage de fichiers) joue les 108 questions avec la bonne réponse : **0 erreur JS**, chaque question reconnue « Juste » et sourcée.

Jauge mesurée sur la branche : Tétrade **51 → 81 %** (arène 0 → 108/100).

Points à auditer par Claude : relecture médicale des 108 vignettes (doses citées : adrénaline IM 0,5 mg, Parkland 4 ml/kg/%, seuils FENa, CRB-65, critères de Light, 4T). Remarque : `arene.html` charge `atk400/700.woff2` depuis son dossier, ignorés par `.gitignore` ; en local sans copie, la police Atkinson Hyperlegible retombe sur la police de secours.
## 12. Organes 3D réels : 46 → 76 / 124 (branche `agent/tetrade-3d`, 2026-11-24)

30 organes ajoutés à `conception/outils/anatomie3d/organes_fma.json`, construits par `construire_organes.py` depuis BodyParts3D 4.0 (CC BY-SA 2.1 JP) : circulation pulmonaire (cv), 7 organes de la Psyché (substrat neural : lobes, système limbique, striatum, thalamus, tronc ; champ `note` « avis d'expert »), organes lymphoïdes, thymus, rate, moelle osseuse (sternum, os coxal, sacrum), nez, cavité buccale (arcades dentaires, mandibule, maxillaires, 2 organes), plancher pelvien, globe oculaire, voies optiques, paupières, les 10 organes osseux et musculaires du locomoteur et l'épiderme.

Occultation : nouveau champ `rogner` (boîte pelvienne du skill 3d-images-upload-super) ; la peau perd ses faces génitales avant export, vérifié sur un rendu de face. Aucun maillage génital chargé.

Non produits faute de maillage dans BodyParts3D (pas de devis inventé) : péricarde, conduction, artères des membres, microcirculation, plèvre, pharynx, larynx, thyroïde, parathyroïdes, glandes salivaires, ganglions, nerfs et plexus, oreille, sein, utérus, ovaires, trompes, placenta, organes cellulaires (sang, immunité) et pédiatriques. Piste : Z-Anatomy ou TotalSegmentator (thyroïde, larynx, utérus) via GitHub Actions.

Les `.glb` restent hors Git (`.gitignore`) ; `index.json` est versionné et le script les régénère à l'identique (46 anciens inchangés). Chaîne complète réussie. Jauge Tétrade sur la branche : 51 → 55 %.
## 13. Système Psyché : jouable (branche `agent/tetrade-sys-psyche`, 2026-11-24)

| Élément | Valeur |
|---|---|
| Organes rédigés | 7 (fonctions cognitives, perception et pensée, affects et humeur, pulsions-motivation-comportement, conscience de soi et personnalité, sommeil et vigilance, récompense et addictions) |
| Volets propres | 15 ; mots-clés 60 (l'« anatomie » décrit les circuits qui portent la fonction, sans en faire la cause unique) |
| Sémiologie | 6 temps (ordre AMDP : interrogatoire → examen somatique et toxique), 14 temps par organe, 39 signes ; cataplexie = signe unique assumé |
| Pathologies | 33 : 9 TF, 10 F, 7 U, 7 R, code CIM-10 dans « retenir » |
| Glossaire | 31 sigles |
| Identifiants | les 7 `org_psyche_*` sont **conservés** par `ids` dans `systemes_rediges.py` (préfixe `ps_` pour le reste) : aucune migration, et les clés 3D de la branche `agent/tetrade-3d` restent valides |

Renvois sans doublon : Alzheimer, trouble cognitif léger, encéphalite limbique, syndromes malin et sérotoninergique → Neurologique ; apnées → Respiratoire ; retard de phase → Endocrinien ; renutrition inappropriée → Endocrinien ; dépression respiratoire aux opioïdes → Respiratoire. Contexte suisse : PAFA (Code civil, art. 426), directives ASSM sur la contrainte, La Main Tendue (143), Tox Info Suisse (145), SSAM, OFSP.

Contrôles : chaîne complète réussie (conception 34/34, couverture, non-perte 0, interprétations 177/177, plans 31/31). Aucune fenêtre de courbe nouvelle (la jauge des interprétations dépasse déjà sa cible).

### Points `aVerifier` (Psyché, 9)
TDAH (conditions suisses des psychostimulants) ; physostigmine (disponibilité, dose) ; mise à jour SSPP dépression après 2016 ; lisdexamfétamine dans l'hyperphagie (AIPS) ; trouble de symptôme somatique (recommandation dédiée) ; jambes sans repos (année AASM 2024 ou 2025) ; SSAM alcool (titre, année) ; tabac (recommandation suisse, disponibilité de la varénicline) ; OFSP/SSAM agonistes opioïdes (version). Sources sans recommandation dédiée signalées « avis d'expert » : pseudo-démence, Charles Bonnet, trouble factice, syndrome anticholinergique.
