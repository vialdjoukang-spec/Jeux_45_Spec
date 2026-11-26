# Point de reprise — producteur groupe C (AAI), 26.11.2026 (mise à jour après le lot 9)

- Fusionnés sur main, contrôles au vert (menus longs 0, classer_rendement, arène 45, test_arene.py « erreurs: 0 ») :
  - lot 1 : N81.6, N81.8, N92.2 ;
  - lot 2 : N92.4, N93.9_2, N95.2_1 ;
  - lot 3 : N97.1, N97.9_1, O02.1 (audit : couverture de O02.1 complétée, masquage corrigé dans O02.1 et N97.1, sources NICE NG257, NG126, CHUV et Brevier relues) ;
  - lot 4 : O20.0 (saignement du 1er trimestre sur grossesse évolutive), O10.0 (HTA chronique en grossesse), O04.9_1 (interruption médicale après 12 SA) ;
  - lot 5 : O26.8_2 (douleurs lombaires et de la ceinture pelvienne de la grossesse), O32.1 (siège à terme), O36.6 (macrosomie fœtale suspectée) ; sources NICE NG201, NG192, NG121, NG207, NG3, Vleeming 2008, Cochrane 2015, Term Breech Trial, FAQ DGGG 2023, protocole HUG 2022, Boulvain 2015, SECO, Brevier Brufen, Panadol S, Rhophylac et Gynipral.
  - lot 6 : O40 (hydramnios), O41.0 (oligoamnios), O81.4 (extraction instrumentale) ; sources SMFM #46, MSD 2024, Cochrane 2008 et 2010, NICE NG25, NG133, NG235, ANODE, HUG 2022 et 2025, Brevier Zestril, directive SBU 2026 ;
  - lot 7 : O92.7_1 (canal lactophore bouché), O99.2 (hypothyroïdie et grossesse), Q02 (microcéphalie congénitale infectieuse) ; sources ABM #36 2022, ETA 2014, ECCI 2024, SSGO n° 73, OMS Zika 2025, OFSP toxoplasmose, Brevier Brufen, Algifor et Eltroxin (limitation LS) ;
  - lot 8 : R00.1 (bradycardie sinusale), R01.0 (souffle innocent), R09.1 (douleur pleurétique) ; sources Drezner 2017, RCUK 2025, AFP 2017 et 2022, MSD 2023, NICE NG158, HUG 2024 (PAC), Brevier Beloc Zok et Procoralan ;
  - lot 9 : R11 (nausées et vomissements en soins palliatifs), R13 (dysphagie oropharyngée), R15 (incontinence fécale) ; sources aide-mémoire HUG 2025, NICE NG128, NG236, CG49, ESPEN 2022, Brevier Paspertin, Sandostatin et Imodium.
- Compte du groupe C selon `classer_rendement.py` : 122 / 800.
- Mention harmonisée dans toutes les formes compactes C : « posologies à vérifier dans l'AIPS (Swissmedic) ».
- Points restés « à vérifier » (lots 6–9) : RCOG Green-top 26 non lisible (remplacé par NICE NG235 et une directive galloise) ; seuil de microcéphalie à −2 DS (usuel, non lu) ; sonde dans la démence avancée (ESPEN 2015 non lue) ; remboursement OPAS de la logopédie et des conseils en allaitement ; montants LiMA des protections ; discordances signalées : ibuprofène et allaitement (Brevier contre ABM), métoclopramide 30 mg/5 jours (Brevier) contre 120 mg/24 h (HUG palliatif), octréotide hors indication, PCR amniotique dès 17 semaines (ECCI) contre 18–20 (SSGO), atropine 0,5 mg (RCUK/ERC) contre 1 mg (AHA), CT (HUG) contre radiographie (AFP) à 6 semaines.
- Points restés « à vérifier » (lot 5) : nombre de séances de physiothérapie remboursées (OPAS) ; paracétamol en grossesse renvoyé à l'AIPS ; statut de la metformine en grossesse ; RCOG Green-top 20a et 20b et texte de la S3 Sectio non lisibles (Wiley et Thieme bloqués), remplacés par NICE et la FAQ DGGG ; seuils ACOG 4500/5000 g non lus (résumé seul).
- Points restés « à vérifier » (lots 1–4) : statut suisse de la nifédipine en grossesse (non trouvée au Compendium) ; misoprostol et mifépristone (MisoOne, Mifegyne) utilisés hors autorisation suisse dans NICE NG126 et NG140 ; aspirine préventive hors indication suisse (Aspirin Cardio contre-indiqué au 3e trimestre) ; anti-D au 1er trimestre (NICE 2026 contre résumé suisse de Rhophylac) ; examen fœtopathologique et conseil génétique après IMG (avis d'expert).
- Pathologie suivante : R16.2__F1_6-E07 (hépatosplénomégalie à la percussion), puis R18__S3_2-E03 (ascite sur cirrhose), R23.2__G7-E05 ; reprendre l'ordre du rang (`content/pathologies/RANG_RENDEMENT.json`, groupe C), en sautant les pathologies déjà produites.
- Formes compactes : `projets/45spec/compact_C/c01…c27`.

Signature : AAI (Anthropic AI)
