# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:19 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/P02-05_Examens_Ganglions_cervicaux_9-examens_production_XAi.json
- 2_Pratique/P02-05-PR_Examens_Ganglions_cervicaux_9-examens_PRATIQUE_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Ségot, Stalder, Goodyer, Lovey, Caduceus Express (Hôpital du Valais), mai 2026 : lymphocytose persistante > 5 × 10⁹/l, LDH élevée, adénopathie > 4 semaines, biopsie exérèse de référence, trocart en alternative
- OFSP 2018 tableau 16 : CT du cou 2,1 mSv

Corrections faites :
- PET-CT, precautions : la dose de 8,8 mSv était attribuée à Lewis-Jones et al. (2016), qui ne la donne pas ; attribution retirée, valeur typique du projet gardée (déclarée dans aVerifier)
- Glossaire + VCA
- Décision : les sigles ajoutés au glossaire sont gardés
- Note pour la relecture : le _meta de chaque fragment est celui du squelette de lot de main ; la fusion ne reprend pas le _meta du lot
- Réserves gardées dans aVerifier : blastes, LDH sans valeur chiffrée, prelevementRef de la cytoponction, AAO-HNS en résumé
