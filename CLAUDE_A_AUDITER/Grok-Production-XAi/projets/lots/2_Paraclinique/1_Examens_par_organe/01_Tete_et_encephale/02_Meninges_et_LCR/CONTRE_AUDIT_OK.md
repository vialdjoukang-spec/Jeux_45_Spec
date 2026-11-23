# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 01:07 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P01-02_Examens_Meninges_et_LCR_7-examens_production_XAi.json
- 2_Pratique/P01-02-PR_Examens_Meninges_et_LCR_7-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Swiss Memory Clinics 2024 (brochure OFSP, tableau 2) : ≤ 4 cellules/µl ; protéines 0,15 à 0,45 g/l ; glucose 60 % du taux sanguin ; lactate < 2,1 mmol/l ; comptage des cellules dans les 1 à 2 h ; bandes oligoclonales si suspicion d’affection inflammatoire chronique du SNC ✔
- ESCMID 2016 (van de Beek), via Spanos et al., JAMA 1989 et le protocole Amsterdam UMC qui la cite : glucose < 1,9 mmol/l, protéines > 2,2 g/l, leucocytes > 2000/mm³ ✔ (texte ESCMID intégral inaccessible, confirmé par sources secondaires)
- Cruickshank et al., UK NEQAS 2008 : ponction > 12 h ; NBA ≤ 0,007 UA non augmentée ; NOA ≥ 0,1 UA empêche d’exclure une HSA ✔
- EANO-ESMO 2023 (Le Rhun) : LCR idéalement > 10 ml, au moins 5 ml ; traitement dans les 30 min ; nodule mesurable ≥ 5 × 5 mm ; seconde ponction si première cytologie négative ✔
- Kapadia et al., CMAJ 2020 : PCR HSV faussement négative possible dans les 72 premières heures ✔
- Tibbling et al. 1977 (valeurs de référence) : index IgG normal jusqu’à 0,70 ✔ (confirmé par sources secondaires ; texte de 1977 non accessible)
- Friedman et al. 2013 : pression d’ouverture ≥ 250 mm de LCR chez l’adulte (≥ 280 mm chez l’enfant) ✔
- RCP indium-111 DTPA (Curium, 2024) : 9 à 20 MBq ; 0,14 mSv/MBq ; 2,8 mSv à 20 MBq ✔

Corrections faites :
- LCR (seuil) : « pression d’ouverture > 25 cmH2O (≈ 2,5 kPa). » (sans source) → « pression d’ouverture ≥ 25 cmH2O (≈ 2,5 kPa) chez l’adulte, selon les critères révisés de Friedman et al. (2013). »
- Cisternographie (precautions) : « On respecte les règles de radioprotection et l’asepsie de l’injection intrathécale. » → phrase ajoutée : RCP de l’indium-111 DTPA (Curium, 2024), 9 à 20 MBq chez l’adulte, 0,14 mSv/MBq, environ 2,8 mSv à l’activité maximale ; glossaire + DTPA
- Dose de la cisternographie : 2,0 mSv (valeur acceptée sur main) gardée, compatible avec la fourchette du RCP (1,3 à 2,8 mSv) ; aVerifier réécrit avec ce qui a été cherché
- Constat : Swiss Memory Clinics 2024 (tableau 2) donne bien ≤ 4 cellules/µl, protéines 0,15 à 0,45 g/l, glucose 60 % du taux sanguin, lactate < 2,1 mmol/l et comptage des cellules dans les 1 à 2 h ; ces attributions sont exactes et gardées
- Réponses de défis signalées (non raccourcies) : 71 caractères (« Rehaussement pachyméningé lisse évoquant une hypotension intracrânienne ») et 46 caractères
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main ; le _lot.aVerifier est ajouté comme dans les autres dépôts ; les « reponse » de défis de plus de 45 caractères sont des réponses rédigées, signalées et non raccourcies.
