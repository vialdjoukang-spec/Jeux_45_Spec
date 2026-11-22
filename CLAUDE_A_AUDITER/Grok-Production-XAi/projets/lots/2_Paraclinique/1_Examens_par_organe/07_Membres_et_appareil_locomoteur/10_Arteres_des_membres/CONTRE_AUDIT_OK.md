# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:54 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P07-10_Examens_Arteres_des_membres_9-examens_production_XAi.json
- 2_Pratique/P07-10-PR_Examens_Arteres_des_membres_9-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Willmann et al., Radiology 2005 (PubMed 16055691) : sensibilité 96 %, spécificité 97 % ; dose angio-CT 1,6 à 3,9 mSv contre 6,4 à 16,0 mSv en artériographie — confirmé
- Buso et al., Rev Med Suisse 2021 (dépôt UNIL) : IPS normal 1 à 1,3 ; limite 0,91 à 0,99 ; ≤ 0,9 = AOMI ; > 1,4 = non compressible — confirmé
- ESC 2024 (via la revue de Vrsalović et al., Cardiologia Croatica 2024) : IPS ≤ 0,90, > 1,40, index orteil-bras ≤ 0,70, échodoppler sensibilité 88 % et spécificité 95 % pour > 50 %, TcPO2 > 30 et < 10 mmHg, chute d'IPS > 20 % ou de cheville > 30 mmHg à l'effort — confirmé
- Hart et al., HPA-CRCE-012 (2010, annexe A, gov.uk) : « femoral angiogram lower limbs » 2,3 mSv (E-103) — confirmé
- Smith et al., Autoimmunity Reviews 2020 (manuscrit UCL) : densité normale ≥ 7 capillaires/mm, mégacapillaire ≥ 50 µm, largeur < 20 µm — confirmé
- Smarter Medicine, Société Suisse d'Angiologie (2024), recommandation 2 et son commentaire (échographie duplex couleur de premier choix) — texte exact retrouvé
- Directive OFSP R-06-06 rév. 2 (2018), protocole 11 : valeur cible 450 mGy·cm — relue (copie téléchargée)

Corrections faites :
- 17 anomalieTypique de plus de 45 caractères (source dans l'étiquette) raccourcis ; sources gardées dans les champs rédigés ; 3 consignes (« … est une option ») remplacées par l'anomalie « Occlusion artérielle aiguë »
- 2 citations Smarter Medicine mises au format commun (« … », selon Smarter Medicine, liste Top 5 de la Société Suisse d'Angiologie (2024), recommandation 2) ; texte inchangé, vérifié mot pour mot
- Angio-CT : irradiation_mSv 3,9 (Willmann 2005, hors OFSP) → 6,8 (R-06-06 protocole 11, 450 mGy·cm × 0,015, valeur déjà acceptée sur main) ; precautions réécrites, Willmann gardé en comparaison
- Artériographie : irradiation_mSv 8,0 (ligne générique OFSP 2018 tableau 17 « autres ») → 2,3 (HPA-CRCE-012, artériographie fémorale, valeur déjà acceptée sur main) ; precautions réécrites
- referencePour de l'échodoppler artériel rétabli depuis main : « Artériopathie oblitérante des membres » (vidé dans le lot)
- Angio-IRM, seuil : renvoi interne « dans les textes relus » retiré du contenu
- Glossaire : OFSP, CIPR, HPA-CRCE ajoutés
- Décisions : OFSP 2018 tableaux 13, 14 et 16 relus, aucune ligne d'angio-CT ni d'artériographie ; convention du projet (R-06-06 × AAPM) et HPA-CRCE-012 retenues, comme sur main. Équivalents kPa recalculés : tous exacts (30 mmHg = 4,0 ; 10 = 1,3 ; 22 = 2,9 ; 70 = 9,3 ; 140 = 18,7 ; 98 = 13,1 ; 132 = 17,6 ; 90 = 12,0 ; 24 = 3,2 ; 8 = 1,1 kPa)
- Réserves gardées dans aVerifier : capillaroscopie (Della Vedova 2026 en résumé seul), complications de la ponction artérielle (supplément ESC non relu), équivalents kPa calculés
- Note pour la relecture : 9 « reponse » de défis de plus de 45 caractères sont des réponses rédigées, laissées telles quelles (règle du journal)
