# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:54 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P07-11_Examens_Veines_des_membres_8-examens_production_XAi.json
- 2_Pratique/P07-11-PR_Examens_Veines_des_membres_8-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Kalva et al., Radiology 2008 (PubMed 18227548) : bassin 5,2 mSv, jambes 0,6 mSv — confirmé
- Kline et al., J Thromb Haemost 2004 (PubMed 15304025) : 8 critères PERC (âge < 50, pouls < 100, SaO2 > 94 %, pas d'œdème unilatéral, d'hémoptysie, de trauma ou chirurgie récents, d'antécédent d'EP/TVP, d'hormones) — confirmé
- Score 4T (Lo et al. 2006) : tableau relu dans la recommandation BSH 2012 et Cuker et al., Blood 2012 (PMC3501714) : nadir ≥ 20 × 10⁹/l = 2 points, début jour 5 à 10 — confirmé
- ESVS 2021 (Kakkos et al., texte intégral ejves.com) : D-dimères sensibilité ≈ 95 %, VPN 99–100 %, spécificité 35–55 %, seuils ajustés à l'âge spécificité 51,1 % ; Wells bas : TVP jusqu'à 5 % ; 4T bas VPN 99,8 %, VPP 14 % et 64 % — confirmé
- Schouten et al., BMJ 2013 (PubMed 23645857) : âge × 10 µg/l, sensibilité > 97 % dans toutes les classes d'âge — confirmé
- Hart et al., HPA-CRCE-012 (2010, annexe A, gov.uk) : « venography of a limb » 0,56 mSv — confirmé
- Smarter Medicine : Angiologie 2024 n° 4, Radiologie 2020 n° 1 — texte exact retrouvé dans le corpus

Corrections faites :
- 16 anomalieTypique de plus de 45 caractères raccourcis ; sources gardées dans les champs rédigés
- 2 citations Smarter Medicine au format commun : Société Suisse d'Angiologie (2024), recommandation 4 ; Société Suisse de Radiologie (2020), recommandation 1 ; texte inchangé, vérifié mot pour mot
- Phlébo-CT : irradiation_mSv 5,8 (Kalva 2008, hors OFSP) → 7,1 (R-06-06 protocole 8, 470 mGy·cm × 0,015, valeur déjà acceptée sur main) ; Kalva gardé en comparaison
- Phlébographie : irradiation_mSv 8,0 (ligne générique OFSP 2018 tableau 17) → 0,56 (HPA-CRCE-012, phlébographie d'un membre, valeur déjà acceptée sur main) ; precautions complétées ; défi : « très irradiante » → « irradiante »
- Anti-PF4 : « nadir supérieur à 20 G/l » (ESVS « >20 000/mL », coquille) → « nadir d'au moins 20 G/l » selon le score 4T de Lo et al. (2006) repris par la British Society for Haematology (2012) ; début du 5e au 10e jour ajouté avec sa source
- D-dimères : seuil ajusté à l'âge hors embolie pulmonaire ajouté (Schouten et al., BMJ 2013 ; ESVS 2021, spécificité 51,1 %) ; seuil affiché 500 µg/l (HUG 2023) gardé
- Règle PERC : les 8 critères ajoutés d'après Kline et al. (J Thromb Haemost 2004, résumé PubMed)
- referencePour de l'échodoppler veineux rétabli depuis main : « Thrombose veineuse profonde »
- Option + bonneReponse « Bilan de thrombophilie discuté avec un spécialiste » (50) → « Bilan de thrombophilie avec un spécialiste »
- Glossaire : BMJ, CIPR, HPA-CRCE, OFSP ajoutés ; aVerifier réécrit (5 réserves tranchées ou mises à jour)
- Note pour la relecture : 5 « reponse » de défis de plus de 45 caractères laissées telles quelles (réponses rédigées)
