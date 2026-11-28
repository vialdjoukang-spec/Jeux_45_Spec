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
