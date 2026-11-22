# CONTRE_AUDIT_OK — lots de complément 3, 2, 4 et 6

Contre-audit croisé interne terminé le 23.11.2026 00:21 (heure de Zurich), dans cet ordre : LOT_COMPLEMENT_3, LOT_COMPLEMENT_2, LOT_COMPLEMENT_4, LOT_COMPLEMENT_6.
Ce fichier ne couvre que ces quatre lots ; le CONTRE_AUDIT_OK.md voisin couvre les lots 7 et 1.

Fichiers contrôlés :
- LOT_COMPLEMENT_3_rachis_moelle_et_racines_production_XAi.json (16 examens)
- LOT_COMPLEMENT_2_cou_production_XAi.json (35 examens)
- LOT_COMPLEMENT_4_thorax_production_XAi.json (70 examens)
- LOT_COMPLEMENT_6_pelvis_production_XAi.json (60 examens)

Contrôles faits : structure identique à l'original de main (clés, ordre, chemins, _meta, id, nom, modalite) ; seuls les cinq champs demandés sont remplis (synonymes, aspectNormal, anomaliesElementaires, syndromesParacliniques, pathologiesAssociees) ; JSON valide ; aucun champ vide ; étiquettes de 45 caractères au plus ; chaque anomalie citée dans un syndrome ou une pathologie figure dans anomaliesElementaires ; aucun synonyme identique au nom ; une source nommée dans chaque phrase ; aucune mention de fabrication du contenu ; entrées à vérifier relues une à une. Ces lots n'ont pas de clé glossaire : les sigles restent à relire à la fusion.

Verdicts :
- LOT_COMPLEMENT_3 : conforme après correction
- LOT_COMPLEMENT_2 : conforme après correction
- LOT_COMPLEMENT_4 : conforme après correction ; 1 réserve maintenue dans _lot.aVerifier (déficit fixe de la scintigraphie, directive OFSP)
- LOT_COMPLEMENT_6 : conforme après correction ; 2 réserves maintenues dans _lot.aVerifier (agénésie du corps calleux, ISUOG ; AMH et FSH, ESHRE 2023)

Sources revérifiées en ligne :
- Lindenholz et al., Eur Radiol 2014 : vides de signal périmédullaires chez les 53 patients
- Raymaekers et al., World Neurosurg 2025 : sensibilité poolée de détection 98,2 % ; bon côté 91 %, bon niveau 76 %
- Montalban et al. 2025 (critères de McDonald 2024) : index kappa ≥ 6,1 ; LCR positif à la place de la dissémination dans le temps
- Banwell et al. 2023 (MOGAD) : anti-MOG franchement positif ≥ 1:100, faiblement positif 1:10 à < 1:100
- mediX, carence en vitamine B12 : zone grise 150-250 pmol/l, dosage de l'acide méthylmalonique
- Royal College of Radiologists 2014 : ganglion cervical anormal au-delà de 8 mm d'axe court, 10 mm en jugulo-digastrique, nécrose centrale anormale même sous 10 mm
- ESVS 2023 (Naylor et al.) : réserve vasculaire altérée (sténose 70-99 %), signal microembolique sur 1 h (50-99 %)
- ETA 2023 (Durante et al.) : calcitonine basale > 30 pg/ml (femme), > 34 pg/ml (homme)
- ESC 2018 syncope : HV > 70 ms = étude positive ; syncope enregistrée en rythme sinusal = cause arythmique exclue
- ESC 2019 syndromes coronariens chroniques : FFR ≤ 0,80
- EAU 2026 cancer de la prostate : PI-RADS ≥ 3, sensibilité 96 % pour ISUP ≥ 2
- EAU 2025 infertilité masculine : caryotype si azoospermie ou < 5 millions/ml
- EAU 2026 LUTS masculins : résidu ≥ 350 ml associé à la progression (MTOPS, ALTESS)
- SSGO avis d'experts n° 94 (2026) : génotypage RHD fœtal, anti-D 300 µg à 28 semaines si fœtus RHD positif
- Smarter Medicine, liste Top 5 de gynécologie et obstétrique : pas de bilan hormonal systématique devant une ménopause clinique (texte relu)

Corrections faites :
LOT_COMPLEMENT_3
- « L'examen les localise avec une sensibilité poolée de 98 %, selon Raymaekers et al. (2025, World Neurosurgery). » → « L'examen détecte la fistule avec une sensibilité poolée de 98 % et trouve le bon côté dans 91 % des cas, le bon niveau dans 76 %, selon Raymaekers et al. (2025, World Neurosurgery). » (fond : 98 % = sensibilité de détection, pas de localisation (méta-analyse relue))
- « Le temps de conduction motrice centrale et le rapport d'amplitude restent dans moins de 2,5 à 3 écarts-types de la moyenne normale, » → « Le temps de conduction motrice centrale et le rapport d'amplitude ne s'écartent pas de plus de 2,5 à 3 écarts-types de la moyenne normale, » (formulation)
- « La culture reste stérile ce qui ne prouve pas une infection, » → « La culture reste stérile, ce qui n'apporte pas la preuve d'une infection, » (ponctuation et formulation)
- « Pangonogramme rachidien » → « Rachis entier en charge » (synonyme inexact (le pangonogramme concerne les membres inférieurs))
LOT_COMPLEMENT_2
- « synonymes : Signe du halo » → « synonymes : Écho-Doppler des artères temporales » (synonyme : « Signe du halo » est un signe, pas un nom d'examen (l'anomalie « Signe du halo » est gardée))
LOT_COMPLEMENT_4
- « Épanchement pleural visible : Il rend l'examen positif, selon Alrajhi et al. (2012). » → « Il rend l'examen positif, selon la BTS (Roberts et al., 2023). » (source inadaptée : Alrajhi et al. (2012) porte sur le pneumothorax)
- « conception/donnees/paraclinique/topographie/4_thorax/coeur_et_pericarde.json › coeur_et_pericarde__etude_electrophysiologique_endocavitaire › anomaliesElementaires : la conduction infrahisienne allong » → entrée retirée (ESC 2018 relu (HV > 70 ms ou bloc de 2e-3e degré = étude positive, stimulation de classe I))
- « conception/donnees/paraclinique/topographie/4_thorax/coeur_et_pericarde.json › coeur_et_pericarde__holter_ecg_24_h_a_7_jours › aspectNormal : la corrélation symptôme-rythme est attribuée aux recommand » → entrée retirée (ESC 2018 relu (une syncope enregistrée en rythme sinusal exclut une cause arythmique))
- « conception/donnees/paraclinique/topographie/4_thorax/coeur_et_pericarde.json › coeur_et_pericarde__coronarographie › aspectNormal : le seuil de FFR de 0,80 est attribué à l'ESC 2019 (syndromes coronar » → entrée retirée (ESC 2019 relu (FFR ≤ 0,80 ou iFR ≤ 0,89 = sténose significative))
LOT_COMPLEMENT_6
- « synonymes : β-hCG » → « synonymes : hCG quantitative » (synonyme identique au nom de l'examen)
- « synonymes : Urétrographie rétrograde » → « synonymes : Urétrographie ascendante » (synonyme identique au nom de l'examen)

Remarques pour la relecture :
- LOT_COMPLEMENT_4 : l'échocardiographie transœsophagienne cite la recommandation EANM/SNMMI v2.0 (2025) pour les végétations et abcès ; les recommandations ESC 2023 sur l'endocardite seraient une source plus directe.
- Les rapports de vraisemblance de Fournier, Moix et Hugli (Rev Med Suisse 2008) n'ont pas été relus.
