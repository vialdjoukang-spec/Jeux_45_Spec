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
