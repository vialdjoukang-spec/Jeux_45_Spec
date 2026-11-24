# Ouvrier automatique — 2026-11-24 12:35 UTC

Dernier passage : **T3_pec_fiches_existantes** → en_cours (0.08 USD).

Le mode pec existe déjà dans scripts/produire_fiches_claude.py, et 628 des 779 fiches portent priseEnCharge, avec audit.rejector remis à null pour la réaudit. Les 151 fiches restantes sont rejetées pour erreur de forme : le mode pec les exclut volontairement, car T4 les reprend en entier avec le schéma qui inclut la prise en charge. Je n'ai lancé aucun appel ce passage, car il n'y a rien de nouveau à soumettre ; T3 passera à « fait » quand T4 aura régénéré ces 151 fiches.

**Crédit** : 51.68 USD dépensés, 140.32 USD disponibles avant le 27.11.2026 ; aujourd'hui 1.06 / 141.38 USD.

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
| F5_cas_thorax | fait | 1 | 1.21 |
| T2_recup_lot600 | fait | 1 | 0.0 |
| END_C_pilote | fait | 1 | 0.276 |
| V1_fusions | fait | 1 | 0.223 |
| END_N_lot | fait | 1 | 0.0 |
| END_N_recup | fait | 5 | 0.0 |
| END_Q_lot | fait | 1 | 0.0 |
| END_Q_recup | fait | 1 | 0.0 |
| END_C_lot | fait | 1 | 0.0 |
| END_C_recup | fait | 1 | 0.0 |
| T3_pec_fiches_existantes | en_cours | 7 | 0.084 |
| T4_reprise_rejets | a_faire | 0 |  |
| T5_items_valides | sans_objet | 0 |  |
| T7_transversal_lecons | sans_objet | 0 |  |
| T6_vague_urgences | sans_objet | 0 |  |
| V2_N_lot | bloque | 0 |  |
| V2_N_recup | bloque | 0 |  |
| V2_Q_lot | bloque | 0 |  |
| V2_Q_recup | bloque | 0 |  |
| V2_C_lot | bloque | 0 |  |
| V2_C_recup | bloque | 0 |  |

Signature : AAI (Anthropic AI)
