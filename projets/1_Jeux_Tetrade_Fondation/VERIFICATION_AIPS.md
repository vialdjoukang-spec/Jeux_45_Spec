# Levée des « à vérifier » de la Tétrade (branche `tetrade-finition`, 28.11.2026)

## Méthode
- Source des posologies : texte AIPS publié par Swissmedic, lu dans la base AmiKo FR (ywesee, `pillbox.oddb.org/amiko_db_full_idx_fr.zip`, version du 27.11.2026, 4651 informations professionnelles). La base n'est pas versionnée (154 Mo).
- `outils/verifier_aips.py <système>` relie chaque ligne `t` à sa spécialité suisse (marque, sinon DCI), relève son n° d'autorisation et la date de mise à jour, puis cherche chaque dose dans la rubrique « Posologie/Mode d'emploi ».
- Les doses retrouvées valent contrôle ; chaque dose absente est relue à la main dans l'AIPS (requêtes ciblées) puis classée : conforme (faux négatif), hors AIPS (dose de la recommandation, dite dans la ligne `s`), ou erreur corrigée.
- Une molécule sans AIPS est signalée comme absente du marché suisse.
- `outils/appliquer_aips.py` remplace « posologies à vérifier dans l'AIPS (Swissmedic) » par « posologies contrôlées dans l'AIPS (Swissmedic), lue le 28.11.2026 », suivi des écarts.
- Les références « à vérifier » sont identifiées sur PubMed (titre, revue, année, pages) ; ce qui exige le texte intégral garde la mention avec le lieu de vérification.
- Trace : `verification_aips/<système>.json` (correspondances et doses) et `<système>_decisions.json` (textes appliqués).

## Bilan par système
| Système | « à vérifier » avant | après | Écarts AIPS signalés | Absents du marché suisse |
|---|---|---|---|---|
| cardio | 40 | 4 | spironolactone 12,5 mg ; amiodarone IV en 10–20 min ; MgSO₄ 2 g en bolus ; HNF en UI/kg ; demi-dose de ténectéplase ≥ 75 ans ; altéplase 0,6 mg/kg ; hydrocortisone 200 mg/j (choc septique) ; corticoïdes 1 mg/kg (PTT) ; AAS 75 mg | ampicilline, nadolol |
| respi | 36 | 0 | mométasone (schéma inverse de l'AIPS dans la polypose) ; prednisone en mg/kg ; dexaméthasone orale et adrénaline nébulisée (croup) ; salbutamol nébulisé 5 mg ; MgSO₄ IV dans l'asthme ; itraconazole 200 mg 2×/j ; altéplase et dornase intrapleurales ; naloxone dès 0,04 mg | — |
| digestif | 57 | 0 | FLOT, FOLFOX, mFOLFIRINOX (5-FU en perfusion longue, irinotécan 150 mg/m²), capécitabine 825 mg/m² ; pantoprazole 8 mg/h ; érythromycine prokinétique ; thiamine 500 mg IV ; baclofène hors spasticité ; trientine 2700 mg ; UDCA en prévention ; rifampicine (prurit) ; prednisone en mg/kg ; octréotide 500 µg ; albumine 1,5 g/kg ; ciprofloxacine en prophylaxie ; seladelpar autorisé (Lyvdelzi), bézafibrate hors CBP | D-pénicillamine, céfotaxime, anakinra, élafibranor, psyllium seul |
| renal | 37 | 1 | prednisone en mg/kg ; salbutamol nébulisé 10–20 mg ; ceftriaxone 500 mg (CDC) ; bléomycine BEP ; Kinpeygo autorisé | pivmécillinam, citrate de potassium ; gluconate/chlorure de calcium IV sans AIPS ni Refdata (reste « à vérifier » auprès de la pharmacie hospitalière) |
| neuro | 71 | 0 | pramipexole corrigé en sel (0,125 mg) ; lamotrigine 500 mg ; lorazépam, lévétiracétam, valproate IV (état de mal) ; primidone 25 mg ; thiamine 500 mg ; desmopressine /8 h ; sumatriptan 100 mg ; prednisone en mg/kg ; ténectéplase (Metalyse 5000 U) et amifampridine (Firdapse) autorisés | ampicilline, D-pénicillamine, antitoxine botulique, captopril, nitroglycérine pommade 2 %, cyproheptadine |
| endocrino | 84 | 1 | lévothyroxine en µg/kg ; hydrocortisone IV en relais ; propylthiouracile > 600 mg/j ; calcitonine 4 UI/kg SC ; glimépiride 0,5 mg ; méthylprednisolone en mg/kg ; fénofibrate (200 mg en Suisse) ; sélpercatinib, vandétanib, métyrapone disponibles | thiamazole (carbimazole à sa place), lévothyroxine IV, alfacalcidol, phentolamine, phénoxybenzamine, métréleptine, urée orale ; gluconate de calcium IV (reste « à vérifier » auprès de la pharmacie hospitalière) |
| hemato | 47 | 0 | prednisone en mg/kg ; hydroxyurée hors AIPS dans la drépanocytose ; CCP contre anti-Xa ; 3 doutes aVerifier levés (B12 IM, luspatercept absent de la LS, filgrastim non remboursé dans l'agranulocytose) | Siklos |
| infectio | 18 | 0 | artéméther-luméfantrine corrigé (24 comprimés en 3 jours, AIPS Riamet ; la ligne disait 5 jours) ; prednisone en mg/kg ; doute anakinra levé ; ssi.guidelines.ch exige une authentification (aVerifier érysipèle conservé) | artésunate IV, anakinra |
| orl | 40 | 0 | doxycycline 50 mg introuvable ; sélénium hors indication ; dimenhydrinate (seule forme 20 mg) ; 5 doutes aVerifier levés (téprotumumab et idébénone hors LS, atropine 0,01 % et polihexanide 0,08 % sans AIPS, amoxicilline adulte conforme) | atropine 0,01 %, polihexanide 0,08 % |
| loco | 58 | 0 | colchicine en prophylaxie hors AIPS ; prednisone en mg/kg ; 2 doutes levés (néridronate absent ; duloxétine et prégabaline sans indication fibromyalgie) | néridronate |
| derma | 33 | 0 | clobétasol 20–40 g/j ; nifédipine (Raynaud) et doxycycline (acné, hidradénite) hors indication ; isotrétinoïne 0,3 mg/kg ; nystatine 4–6 ml ; prednisone en mg/kg ; 3 doutes levés (minoxidil oral absent ; baricitinib et Botox sans limitation LS pour pelade et hyperhidrose ; ritlécitinib hors LS) | minoxidil oral |
| psyche | 36 | 1 | 3 doutes levés (méthylphénidate adulte : Concerta remboursé, Ritaline seulement narcolepsie ; lisdexamfétamine sans indication boulimie ; varénicline Dalita autorisée hors LS) ; recommandation suisse de sevrage tabagique non lue (reste « à vérifier ») | physostigmine (Anticholium), oxybate de sodium |
| gyneco | 33 | 1 | méthotrexate dans la GEU hors indication ; flucloxacilline orale sans produit suisse (aussi signalée en derma ×2 et loco ×1) ; avis SSGO et prise en charge du test HPV primaire : lieu de vérification précisé | flucloxacilline orale |
| pediatrie | 23 | 1 | gel de dextrose 40 % sans AIPS ; SwissPedDose exige un compte (contrôle pédiatrique « à vérifier » dans l'en-tête) | gel de dextrose 40 % |
| **Total** | **613** | **9** | | |

## Sources lues (28.11.2026)
- AIPS Swissmedic : base AmiKo FR du 27.11.2026 (`pillbox.oddb.org/amiko_db_full_idx_fr.zip`), 4651 informations professionnelles.
- Index Refdata des articles (`files.refdata.ch/simis-public-prod/Articles/1.0/Refdata.Articles.zip`, généré le 28.11.2026, 18 523 articles) : présence sur le marché suisse. Il peut manquer des solutions hospitalières : le gluconate de calcium injectable garde donc sa mention « à vérifier ».
- Liste des spécialités de l'OFSP : publication du 03.11.2026 (`epl.bag.admin.ch/static/sl/archive/per-year/2026/2026-11-03/BAG_xls_2026.zip`, fichier `foph-sl-publication-20261103-fr.ndjson`) : remboursement et limitations.
- PubMed : FMD 2019 (doi 10.1177/1358863X18821816), ISL 2023 (Lymphology 56:133-151), BTS 2023 (doi 10.1136/thorax-2022-219784), EAU 2025 (doi 10.1016/j.eururo.2025.02.020).

## Les 9 « à vérifier » restants
| Système | Objet | Raison | Où vérifier |
|---|---|---|---|
| cardio | Myxome : référentiel chirurgical suisse | Aucun référentiel publié trouvé | Société suisse de chirurgie cardiaque et vasculaire thoracique |
| cardio | Syndrome cave supérieur : recommandation ESMO | Référence imprécise | esmo.org (Clinical Practice Guidelines) |
| cardio | Thrombus cave : chapitre EAU 2025 | Seul le résumé a été lu | uroweb.org (texte intégral) |
| cardio | Chylothorax : chapitre BTS 2023 | Notice sans résumé | thorax.bmj.com (texte intégral) |
| renal | Gluconate/chlorure de calcium IV (hyperkaliémie) | Ni AIPS ni article Refdata (index possiblement incomplet pour l'hôpital) | Pharmacie hospitalière |
| endocrino | Gluconate de calcium IV (hypocalcémie) | Idem | Pharmacie hospitalière |
| gyneco | Avis SSGO récent ; prise en charge du test HPV primaire | Non lus | sggg.ch ; Liste des analyses (OFSP) |
| psyche | Recommandation suisse récente de sevrage tabagique | Non lue | Ligue pulmonaire suisse |
| pediatrie | Doses pédiatriques dans SwissPedDose | Base sous compte | db.swisspeddose.ch |

## Sites bloqués (notés, non contournés)
- `ssi.guidelines.ch` : application avec authentification (recommandations SSI non lues).
- `db.swisspeddose.ch` : connexion exigée.
- `www.spezialitaetenliste.ch/File.axd` : renvoie désormais l'application web ; la LS a été lue par l'archive officielle `epl.bag.admin.ch`.

## Limites d'outillage relevées
- `non_perte.py` (référence origin/main) compte comme perte la suppression d'un champ `aVerifier`, même résolu : les doutes levés gardent donc leur champ, réécrit « Doute levé le 28.11.2026 : … ».
- Après un rebase sur main, la branche poussée divergeait : elle a été fusionnée (sans push forcé), puis main a été intégrée par fusion.
- Les 4 fichiers paracliniques en perte sur main (`ganglions_cervicaux.json` ×2, `coude_poignet_et_main.json`, `recherche/index.json`) relèvent d'autres couloirs : restaurés à chaque contrôle, jamais commités.
