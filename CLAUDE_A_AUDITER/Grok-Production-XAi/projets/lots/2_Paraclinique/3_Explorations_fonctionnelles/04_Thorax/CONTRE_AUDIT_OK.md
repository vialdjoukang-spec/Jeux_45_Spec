# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 02:24 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/PF04-1_Explorations_fonctionnelles_Thorax_12-fiches_production_XAi.json
- 1_Theorie/PF04-2_Explorations_fonctionnelles_Thorax_12-fiches_production_XAi.json
- 2_Pratique/PF04-1-PR_Explorations_fonctionnelles_Thorax_12-fiches_PRATIQUE_production_XAi.json
- 2_Pratique/PF04-2-PR_Explorations_fonctionnelles_Thorax_12-fiches_PRATIQUE_production_XAi.json

Contrôles : structure identique au squelette de main (clés, ordre, chemins, _meta, nom/id), JSON valide, sens de chaque champ (fonction, traces avec description de ce qu'on voit, seuils, interprétation, diagnostics), défis pratiques (cohérence cas/réponse/justification, réponses courtes ≤ 45 caractères), sigles du glossaire, citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, aucune mention de production ; `controle` : PASS.

Valeurs revérifiées en ligne :
- ESC/ERS 2022 hypertension pulmonaire : PAPm > 20 mmHg, PAPO ≤ 15 mmHg, RVP > 2 UW — concordant
- ATS 2011 (Dweik et al.) : FeNO < 25 ppb improbable, > 50 ppb probable — concordant
- ESC syncope 2018 : massage sinocarotidien > 3 s ou > 50 mmHg, > 40 ans — concordant
- Consensus de Lyon 2018 : temps d'exposition acide > 6 % pathologique, < 4 % normal — concordant ; ERREUR de rangement corrigée (< 4 % était un aspect pathologique)
- ERS 2017 (Coates et al.) : PD20 > 400 µg normale ; pas de test si VEMS < 60 % ou < 1,5 l — concordant
- ESC syncope 2018 : HV 70 ms dans le bloc bifasciculaire — seuil concordant, borne (≥ ou >) non relue

Cherché, non trouvé (déclaré dans _lot.aVerifier) :
- ESC syncope 2018 : borne exacte de l'intervalle HV (≥ ou > 70 ms)
- Laveneziana et al. 2019 (CV couchée > 25 %, PImax 80/70) : non relu
- GINA 2024 (variabilité du DEP > 10 %) : non relu

Corrections faites :
- 11 réponses tautologiques (la réponse recopiait l'aspect) remplacées par un diagnostic, avec une description chiffrée du tracé : ECG, ENMG phrénique, ergospirométrie, FeNO, Holter, massage sinocarotidien, pléthysmographie, spirométrie, spirométrie couchée, tilt-test, pH-métrie
- Seuils non chiffrés ou sans source réécrits (cathétérisme droit, contrôle de stimulateur, massage, tilt-test, épreuve d'effort, étude électrophysiologique)
- Moniteur implantable : aspect pathologique « rythme sinusal » qui répétait l'aspect normal retiré
- Indication : 3 cas « Non » argumentés ajoutés (ergospirométrie avec VEMS et DLCO > 80 %, Holter pour syncopes espacées, méthacholine avec VEMS < 60 %) ; avant : 22 Oui sur 24
