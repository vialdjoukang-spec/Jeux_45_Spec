# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:54 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P07-12_Examens_Nerfs_peripheriques_9-examens_production_XAi.json
- 2_Pratique/P07-12-PR_Examens_Nerfs_peripheriques_9-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Van den Bergh et al., EAN/PNS PIDC 2021 (PDF AAN et JPNS) : section du médian > 10 mm² à l'avant-bras, > 13 mm² au bras, > 9 mm² troncs interscaléniques, > 12 mm² racines ; racine IRM > 5 mm — confirmé
- van Doorn et al., EAN/PNS SGB 2023 (Eur J Neurol, JPNS, PDF UEMS) : LCR < 5 cellules/µl, > 50 → autre diagnostic, protéines élevées 50 % avant 3 jours et 84 % après 7 jours, anti-GQ1b sensibilité 88–100 %, spécificité 100 % — confirmé
- Lauria et al., J Peripher Nerv Syst 2010 (PubMed 21040142, 550 sujets, 5e percentile) et tableau 1 de Kool et al. 2025 (Maastricht) : 8,4 → 1,6 et 6,1 → 1,7 fibres/mm — confirmé
- Cartwright et al., J Neuroimaging 2009 (PubMed 18482371) : section du médian 7,5 à 9,8 mm² chez 50 volontaires — confirmé
- Fabry et al., Front Neurol 2020 (PMC7214721) : biopsie cutanée sensibilité 58 %, spécificité 91 % ; conductance sensibilité 60 %, spécificité 89 % ; tests cardiovasculaires sensibilité 15 % ; normes du fabricant 70 µS aux pieds et 60 µS aux mains — confirmé

Corrections faites :
- 23 anomalieTypique de plus de 45 caractères raccourcis ; le chiffre 42 à 77 % (sensibilité de la protéinorachie dans la PIDC) déplacé de l'étiquette vers la limite du LCR avec sa source
- Biopsie cutanée : valeurs normatives ajoutées (5e percentile de 8,4 à 1,6 fibre/mm chez la femme, de 6,1 à 1,7 chez l'homme, Lauria et al. 2010, tableau repris par Kool et al. 2025)
- Échographie nerveuse : section normale moyenne du médian ajoutée (7,5 à 9,8 mm², Cartwright et al. 2009) à côté des seuils d'élargissement EAN/PNS 2021
- referencePour rétablis depuis main : LCR « Syndrome de Guillain-Barré », biopsie cutanée « Neuropathie des petites fibres »
- Glossaire : C3 (théorie), C6 et C7 (pratique) ajoutés ; aVerifier mis à jour (biopsie cutanée, échographie)
- Équivalent 10⁶/l vérifié : 1 cellule/µl = 10⁶/l, conforme aussi au texte EAN/PNS 2023 (« <5 × 10⁶/L »)
- Note pour la relecture : 6 « reponse » de défis de plus de 45 caractères laissées telles quelles (réponses rédigées)
- Réserves gardées : seuils de conductance cutanée du fabricant, TSH sans anomalie décrite, Theaudin 2022 en résumé
