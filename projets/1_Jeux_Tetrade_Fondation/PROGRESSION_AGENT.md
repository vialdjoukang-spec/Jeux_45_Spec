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

## 6. Suite

- Infectieux et immunitaire : non commencé dans ce passage (voir section 7 si ajoutée plus tard).
