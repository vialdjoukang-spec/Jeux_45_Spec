# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 02:12 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/PE04_Endoscopies_Thorax_8-fiches_production_XAi.json
- 2_Pratique/PE04-PR_Endoscopies_Thorax_8-fiches_PRATIQUE_production_XAi.json

Contrôles : structure identique au squelette de main (clés, ordre, chemins, _meta, nom/id), JSON valide, sens de chaque champ (fonction, traces avec description de ce qu'on voit, seuils, interprétation, diagnostics), défis pratiques (cohérence cas/réponse/justification, réponses courtes ≤ 45 caractères), sigles du glossaire, citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, aucune mention de production ; `controle` : PASS.

Valeurs revérifiées en ligne :
- Meyer et al., ATS 2012 (PDF intégral thoracic.org) : > 15 % lymphocytes, CD4/CD8 > 3,5, éosinophiles ≥ 25 % « virtually diagnostic », normale > 85 % macrophages, 10–15 % lymphocytes, < 3 % neutrophiles, < 1 % éosinophiles
- NAVIGATE (Folch et al., J Thorac Oncol 2019, résumé) : rendement 72,9 % à 12 mois, pneumothorax 4,3 %
- Mönig et al., Rev Med Suisse 2020;16:1292 (revmed.ch) : EUS T3-T4 sensibilité 81–92 %, spécificité 94–97 % ; OGD la plus sensible ; Barrett 4 quadrants + Prague
- Godat, Schoepfer, Moradpour, Rev Med Suisse 2011 (revmed.ch) : endoscopie normale dans ~30 % des œsophagites à éosinophiles ; ≥ 15 éosinophiles/champ (400 ×) ; 4 biopsies par localisation

Cherché, non trouvé (déclaré dans _lot.aVerifier) :
- Opitz et al. 2020 (thoracoscopie 92 %, 0,34 %, 1,8 %, 47 études) : concordant d'après une synthèse de recherche, texte OUP refusé (403)
- EBUS/EUS : ganglion > 1 cm (Vilmann 2015) non relu

Corrections faites :
- Navigation : trace « pneumothorax » (complication, pas un aspect) déplacée en limite, remplacée par l'inflammation granulomateuse
- BAL : normale chiffrée (ATS 2012) ; « soutiennent fortement » → « quasi diagnostiques » (texte ATS)
- OGD : seuil réel ajouté (≥ 15 éosinophiles/champ) ; clé de glossaire invalide remplacée par OGD et Prague ; Smarter Medicine (Barrett) rétabli mot pour mot dans la pratique
- EBUS et EUS : réponse tautologique corrigée ; cas clinique différencié de l'EBUS avec ponction
