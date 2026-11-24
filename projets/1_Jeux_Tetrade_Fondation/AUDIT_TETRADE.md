# Audit médical Tétrade : systèmes hématologique et infectieux (2026-11-24)

Claude a relu chaque chiffre, seuil, dose, voie, rythme et chaque palier (TF/F/U/R) de 45 pathologies hématologiques, de 17 pathologies infectieuses et immunitaires, de leurs organes, signes et glossaires, et des 24 scénarios des interprétations `he_anemie`, `he_fer`, `he_coag` et `ii_anticorps`. Les 22 champs `aVerifier` ont été confrontés aux sources primaires. Les paliers restent tous justes : aucun reclassement.

## 1. Bilan par système

| Système | Vérifiées | Corrigées | Doutes résolus | Doutes restants |
|---|---|---|---|---|
| Hématologique et oncologique (45 pathologies, 6 organes, glossaire) | 45 | 15 pathologies + contenu (réserve médullaire) + glossaire (SLiM ; PCV, PCV20, PCV21 ajoutés) | 11 sur 14 | 3 |
| Infectieux et immunitaire (17 pathologies, 4 organes, glossaire) | 17 | 8 pathologies + contenu (voie des lectines, CH50) + sémiologie (qSOFA) + glossaire (AP50, MASP ajoutés) | 4 sur 8 | 4 |
| Interprétations `he_` et `ii_` (4 fenêtres, 24 scénarios) | 24 | 3 | sans objet | 0 ; `_meta.statut` : **AUDITÉ** |

## 2. Erreurs de fond corrigées

| Pathologie ou élément | Erreur | Correction | Source |
|---|---|---|---|
| Syndrome myélodysplasique | Époétine limitée à 40 000 U/semaine ; darbépoétine « toutes les 2 semaines » | Époétine 30 000 à 80 000 U/semaine ou darbépoétine 150 à 300 µg/semaine ; ajout du luspatercept après échec des ASE (MDS-RS) | ESMO 2021 (Fenaux) ; Swissmedic Reblozyl n° 69592 |
| Carence en vitamine B12 | Entretien IM « chaque mois » sans préciser la molécule | Hydroxocobalamine 1 mg 3×/semaine 2 semaines, puis tous les 3 mois (tous les 2 mois si atteinte neurologique) | BSH 2014 (Devalia, Br J Haematol 166:496) |
| Nécrolyse épidermique toxique | Ciclosporine « 3 à 5 mg/kg pendant 7 jours » | 3 mg/kg/j per os 10 jours, puis décroissance sur 1 mois | Valeyrie-Allanore, Br J Dermatol 2010;163:847 |
| Purpura fulminans méningococcique | Fenêtre « dans les 24 heures » présentée comme limite ; déclaration sans délai | Dose de ciprofloxacine 20 mg/kg (max 500 mg) ; rifampicine en alternative ; idéalement 24 h, au plus 10 jours ; déclaration de la suspicion en 24 h au médecin cantonal et à l'OFSP | OFSP Bulletin 4/2025 (20.01.2025) |
| Asplénie | Vaccin pneumococcique sans valence ; intervalles méningocoques imprécis | PCV21 (18–64 ans à risque ; PCV21 ou PCV20 dès 65 ans) ; ACWY 2 doses à 1–2 mois ; B 2 doses à 2 mois ; rappels tous les 5 ans ; B hors indication et non remboursé après 24 ans | OFSP/CFV PCV (état 01.07.2026) ; OFSP Bulletin 7/2024 |
| Réaction transfusionnelle hémolytique | Recommandation BSH 2012 citée comme en vigueur | BSH 2023 (Soutar) remplace Tinegate 2012 | Br J Haematol 2023;201:832 |
| Hémoglobinurie paroxystique nocturne | Inhibiteurs proximaux absents | Pegcetacoplan (autorisé 23.03.2023) et iptacopan (29.08.2024) après réponse insuffisante au C5 | Swissmedic SwissPAR Aspaveli, Fabhalta |
| Neutropénie isolée « modérée » | Plage 0,5–1,5 G/l contraire aux seuils du contenu (modérée = 0,5–1,0) | Plage nommée « légère à modérée » ; chiffres Duffy ajoutés | Merz, Blood Adv 2023;7:317 |
| Lymphome B diffus | Pola-R-CHP « IPI élevé » | IPI de 2 à 5 (critère de POLARIX) | Tilly, N Engl J Med 2022 |
| Complément (contenu) | Voie des lectines « active directement C3 » | La voie des lectines active C4 et C2 par les MASP ; seule la voie alterne active directement C3 ; AP50 ajouté au raisonnement CH50 | Physiologie du complément (fait établi) |
| Moelle (contenu) | Réserve de « 10 jours » de neutrophiles, production « triplée » | Réserve de quelques jours, production multipliée plusieurs fois | Fait établi ; chiffre précis non retenu faute de source lue |
| Glossaire SLiM | « lésion focale à l'IRM » | « plus d'une lésion focale » | IMWG 2014 |
| qSOFA (sémiologie) | « dépasse 22 » | « atteint 22 ou plus » | Sepsis-3 2016 |
| Références erronées | Gibson « Hematology ASH Educ 2014 » ; Merz « Blood » ; Andrès « Expert Opin Drug Saf » ; Becker « Clin J Sport Med » ; ISA-EHA « 2022 » | Blood 2014;124:1251 ; Blood Adv 2023 ; J Clin Med 2019;8:1351 ; Sports Health 2014;6:232 ; Amyloid 2023;30:3 (en ligne 2022) | PubMed |
| Interprétations | `he_fer` « le fer oral n'est pas absorbé » ; seuils IC attribués à « ESC 2023 » ; `he_anemie` anémie rénale « sous 30 ml/min » | « mal absorbé (hepcidine) » ; ESC 2021 reprise en 2023 ; anémie fréquente dès 60 et surtout sous 30 ml/min | ESC 2021/2023 ; KDIGO |

Corrections de forme : un double espace et un « : » mal placé (neutropénie), une précision de déclaration OFSP dans « retenir ».

## 3. Les 22 doutes `aVerifier`

| # | Pathologie | Résultat | Source |
|---|---|---|---|
| 1 | Syndrome myélodysplasique | Doses résolues ; luspatercept autorisé ; **reste** : remboursement (LS) non trouvé | ESMO 2021 ; Swissmedic |
| 2 | Amylose AL | Résolu : Wechalekar, Amyloid 2023;30:3-17 | PubMed 35838162 |
| 3 | Anémie ferriprive | Résolu : phosphate contrôlé si doses élevées répétées ou facteur de risque, sans rythme fixé | Swissmedic Vigilance-News 2019 |
| 4 | Carence en B12 | Hydroxocobalamine résolue ; **reste** : rythme suisse de la cyanocobalamine (AIPS inaccessible) | BSH 2014 |
| 5 | Crise drépanocytaire | Résolu : antalgie en 30 min après le tri (60 min après l'enregistrement), réévaluation 15–30 min, O₂ si SpO₂ < 95 % | NHLBI 2014 (texte intégral) |
| 6 | Réaction transfusionnelle | Résolu : BSH 2023 (Soutar) | PubMed 37211954 |
| 7 | HPN | Résolu : Aspaveli 2023, Fabhalta 2024 | Swissmedic |
| 8 | Neutropénie isolée | Résolu : Merz, Blood Adv 2023 | PubMed 35994632 |
| 9 | Agranulocytose | Référence corrigée ; **reste** : prise en charge du G-CSF (AIPS et LS illisibles) ; aucun essai randomisé sur la mortalité | Andrès, J Clin Med 2019 |
| 10 | PTI | Résolu : ASH 2026 lue (Cuker, Blood Adv 2026;10:7076) | PubMed 42617047 |
| 11 | Hémophilie A acquise | Résolu : émicizumab hors indication en Suisse (AIPS : hémophilie congénitale) | Swissmedic Hemlibra 2018 |
| 12 | Asplénie | Résolu : PCV21, intervalles méningocoques | OFSP/CFV 2026 ; OFSP 2024 |
| 13 | Infarctus splénique | Résolu : Brett, JAMA Intern Med 2020;180:1125 | PubMed 32658244 |
| 14 | Kikuchi-Fujimoto | Résolu : Dumas, Medicine 2014;93:372 | PubMed 25500707 |
| 15 | Érysipèle | **Reste** : ssi.guidelines.ch inaccessible depuis la session | — |
| 16 | Choc toxique | Bénéfice chiffré ajouté (méta-analyse) ; **reste** : dose d'IgIV absente des résumés | Parks, CID 2018 ; Darenberg, CID 2003 |
| 17 | Urticaire aiguë | Résolu : la recommandation fixe 10 jours au plus, sans dose | EAACI 2021 |
| 18 | Maladie de Still | **Reste** : indication et remboursement de l'anakinra (AIPS inaccessible) | — |
| 19 | Mononucléose | Résolu : Dunmire 2015 confirmé ; Becker publié dans Sports Health 2014 | PubMed 26424648, 24790693 |
| 20 | Nécrolyse épidermique | Dose corrigée ; **reste** (formulé) : aucun essai randomisé ne prouve l'efficacité | Valeyrie-Allanore 2010 |
| 21 | Angio-œdème héréditaire | Résolu : Takhzyro (2019) et Orladeyo (2022) autorisés et admis sur la LS | Swissmedic ; OFSP |
| 22 | Purpura fulminans | Résolu : 24 h, schéma de chimioprophylaxie OFSP | OFSP Bulletin 4/2025 |

Bilan : 15 doutes résolus, 7 restent avec leur raison précise (1, 4, 9, 15, 16, 18, 20).

## 4. Sources inaccessibles depuis la session (à lire par un humain)

- compendium.ch et swissmedicinfo.ch (AIPS) : le proxy de la session a refusé l'accès ; aucune posologie n'a donc été confirmée dans l'AIPS, et toutes gardent la mention « à vérifier dans l'AIPS ».
- ssi.guidelines.ch (recommandation suisse sur l'érysipèle) et ch.oddb.org : accès refusé.

## 5. Chaîne relancée après correction

Fusion de `origin/main` (lot transversal 2), puis `construire_config_tetrade.py`, `construire_plans.py`, `generer_json.py`, `rendre_plans.py` (31/31), `auditer_conception.py` **34/34**, `auditer_couverture.py` **RÉUSSI**, `non_perte.py` **OK**, `verifier_interpretations.py` **142/142, 0 défaut**. `2_cou/ganglions_cervicaux.json` a été restauré depuis main (défaut IGRA connu) ; le bruit de `trans_s_s4_01.json` et des PDF n'a pas été commité.

Défaut d'outillage découvert : `construire_config_tetrade.py` et `generer_json.py` gardent un champ `aVerifier` retiré de la source (fusion conservatrice). Claude a retiré à la main les 15 champs résolus des JSON d'organes et du graphe ; un correctif de l'outil reste conseillé.

Signature : AAI (Anthropic AI)
