# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 02:12 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/PE05_Endoscopies_Abdomen_15-fiches_production_XAi.json
- 2_Pratique/PE05-PR_Endoscopies_Abdomen_15-fiches_PRATIQUE_production_XAi.json

Contrôles : structure identique au squelette de main (clés, ordre, chemins, _meta, nom/id), JSON valide, sens de chaque champ (fonction, traces avec description de ce qu'on voit, seuils, interprétation, diagnostics), défis pratiques (cohérence cas/réponse/justification, réponses courtes ≤ 45 caractères), sigles du glossaire, citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, aucune mention de production ; `controle` : PASS.

Valeurs revérifiées en ligne :
- ESGE 2022 intestin grêle (Pennazio et al., Endoscopy 2023, PDF esge.com) : capsule 55–62 %, rétention 1,2–2,1 %, entéroscopie 56 → 75 % après capsule positive, capsule idéalement < 48 h, entéroscopie 48–72 h
- ESGE 2022 lésions sous-épithéliales (Deprez et al., PDF esge.com) : exactitude 45,5–48 % ; erreurs sur les lésions hypoéchogènes de la 4e couche (GIST)
- ESGE 2019 calculs de la VBP (Manes et al., PDF esge.com) : EUS sensibilité 97 %, spécificité 87 %
- ESGE 2025 sténoses biliaires (Facciorusso et al., Endoscopy 2025;57:166, PDF esge.com) : cholangioscopie 74 % vs 50 %, gain 27 % ; brossage 40 %, biopsies 52 %, association 66 % (méta-analyse de 21 études)
- Maastricht VI (Malfertheiner et al., Gut 2022, texte intégral) : IPP 14 jours, antibiotiques/bismuth 4 semaines, endoscopie après 50 ans, ≥ 2 biopsies antre + fundus en pots séparés, incisure pour OLGA/OLGIM
- Baveno VII (2022) : 20 kPa, 150 × 10⁹/l, endoscopie < 12 h (synthèse de recherche concordante, texte intégral non relu)
- EAU, ESCP, ESGE 2020, OPAS : non revérifiés (voir ci-dessous)

Cherché, non trouvé (déclaré dans _lot.aVerifier) :
- ESGE 2019 cholangite avec choc < 12 h ; ESGE 2021 Forrest 24/12 h ; ESGE 2018 complications 1 % / pancréatite 0,3 % ; ECCO-ESGAR 2025 44–80 % ; AASLD 2021 SAAG 11 g/l ; EAU 2026 grade > 90 % ; ESMO 2022 (91/77/82/41/49) ; ESGAR 2026 accord 88 % ; OPAS art. 12e let. d (50–74 ans, 10 ans) ; ESGE 2020 (50–75 ans)

Corrections faites :
- Gastroscopie : copie exacte de l'OGD œsophagienne remplacée par une fiche distincte (varices, hypertension portale) tirée de la fiche contre-auditée du système porte, théorie et pratique
- Anuscopie : trace « Autre lésion … écarter une autre pathologie » et seuil-recommandation réécrits (aucun seuil chiffré, critère de qualité ESCP)
- Traces abstraites (angiectasie « à traiter », « lésion à biopsier », sténose « se voit comme un rétrécissement », 4e couche…) réécrites avec ce qu'on voit
- 11 réponses de lecture de tracé qui répétaient l'aspect décrit remplacées par le diagnostic
- Gastrite atrophique : attribution OLGA/OLGIM ramenée à Maastricht VI (texte relu)
- Sigles ACE et MICI ajoutés ; interprétation : casse restaurée (FIT, ACE, Helicobacter)
