# Ouvrier automatique — 2026-11-24 13:36 UTC

Dernier passage : **T3_pec_fiches_existantes** → fait (0.13 USD).

Le mode pec de scripts/produire_fiches_claude.py existe déjà, a été testé en direct puis exécuté en trois lots (154, 61 et 9 fiches), tous récupérés ; 628 des 779 fiches portent maintenant priseEnCharge, dont 383 avec audit.rejector à null pour réaudit. Les 151 fiches restantes sont rejetées pour erreur de forme ou troncature : le mode pec les exclut volontairement, et T4 les archive puis les resoumet en entier avec le nouveau schéma, donc le critère « toutes les fiches » se complète par T4. Ce passage n'a lancé aucun appel API (module anthropic absent de l'environnement, 0 USD dépensé).

**Crédit** : 51.81 USD dépensés, 140.19 USD disponibles avant le 27.11.2026 ; aujourd'hui 1.19 / 141.38 USD.

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
| T3_pec_fiches_existantes | fait | 8 | 0.133 |
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
