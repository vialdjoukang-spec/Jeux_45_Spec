# Ouvrier automatique — 2026-11-23 15:57 UTC

Dernier passage : **SSP_etendus** → fait (1.93 USD).

J'ai créé data/ssp_etendus/ avec 1094 points de départ hors des 248 SSP officiels : G.json (45), 14 fichiers S_<système> (485), 15 fichiers F_<famille> (483, y compris gazométrie, ECG, imageries, anatomopathologie), O.json (81) et INDEX.json (comptes par fichier, type et catégorie). Chaque entrée porte code, intitulé FR/EN, catégorie, type de départ, parent officiel (ou null), justification et 5 à 12 diagnostics différentiels ; un script a vérifié l'unicité des codes et l'absence de doublon exact avec les 248. Le contenu vient des connaissances cliniques générales sans vérification contre les sources suisses : une relecture médicale ligne à ligne par l'audit horaire reste nécessaire, et le critère de sens (doublon proche d'un SSP officiel) n'a été contrôlé qu'à la main.

**Crédit** : 20.69 USD dépensés, 79.31 USD disponibles avant le 27.11.2026 ; aujourd'hui 20.69 / 25.00 USD.

| Tâche | État | Passages | Dernier coût (USD) |
|---|---|---|---|
| complement_3 | fait | 1 | 0.03 |
| complement_1 | fait | 1 | 0.133 |
| complement_2 | fait | 1 | 0.035 |
| complement_4 | fait | 1 | 0.111 |
| j45_pilote_fiches | fait | 3 | 0.0 |
| j45_lot_CAR | fait | 1 | 0.0 |
| j45_pilote_items | fait | 1 | 0.0 |
| j45_pilote_items_haiku | attente_decision | 1 | 0.0 |
| j45_recup_CAR | fait | 1 | 0.0 |
| complement_5 | fait | 1 | 0.196 |
| complement_6 | sans_objet | 0 |  |
| complement_7 | sans_objet | 0 |  |
| renal | fait | 1 | 1.206 |
| neuro | fait | 1 | 2.202 |
| endocrino | fait | 1 | 3.138 |
| interpretations_courbes | fait | 1 | 1.185 |
| T1_pilote_pec_et_lot600 | fait | 1 | 0.26 |
| END_pilote_notions_questions | fait | 2 | 0.272 |
| F2_examens_vides | fait | 1 | 0.684 |
| SSP_etendus | fait | 1 | 1.933 |
| F5_cas_thorax | a_faire | 0 |  |
| T2_recup_lot600 | a_faire | 0 |  |
| T3_pec_fiches_existantes | a_faire | 0 |  |
| T4_reprise_rejets | a_faire | 0 |  |
| T5_items_valides | a_faire | 0 |  |
| T7_transversal_lecons | a_faire | 0 |  |
| T6_vague_urgences | a_faire | 0 |  |

Signature : AAI (Anthropic AI)
