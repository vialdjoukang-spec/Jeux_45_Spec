# Progression PED — MedSuisse Arena 45 (45 Spec)

Branche : `agent/45spec-PED`. Production par agent Claude **sans API** (même schéma, même `valider()` que `scripts/produire_notions_questions.py`), outil : `projets/45spec/agent_ecrire.py`.
Ordre : celui de `selection()` (fréquence puis identifiant). Contrôles : `valider()` sans erreur ; couverture des notions de poids ≥ 2 au moins deux fois sous deux angles ; formats ≈ 70/20/10.
Les données douteuses portent la mention « à vérifier » dans leur source (AIPS, version de recommandation).

**Avancement : 3 / 69 pathologies canoniques complètes (notions + questions + correction).**

| # | Identifiant | Pathologie | Fréq. | Complet | Notions | Questions |
|---|---|---|---|---|---|---|
| 1 | `K21.9__O2_6-E01` | Reflux gastro-œsophagien (RGO) physiologique du nourrisson | 1 | ✅ | 33 | 20 |
| 2 | `P05.1__O1_1-E02` | Retard de croissance intra-utérin (RCIU) / Petit poids pour  | 1 | ✅ | 34 | 22 |
| 3 | `P07.3_1__O2_11-E03` | Hypotonie physiologique du prématuré | 1 | ✅ | 31 | 21 |
| 4 | `P07.3__O1_1-E01` | Grande prématurité (28 0/7 – 31 6/7 SA) | 1 | ⬜ |  |  |
| 5 | `P08.1__O1_1-E03` | Macrosomie fœtale (LGA / poids > 4000 g ou > 90e percentile) | 1 | ⬜ |  |  |
| 6 | `P55.1__F2_17-E02` | Incompatibilité ABO mère-nouveau-né | 1 | ⬜ |  |  |
| 7 | `P59.9__S6_5-E01` | Ictère physiologique / au lait maternel du nouveau-né | 1 | ⬜ |  |  |
| 8 | `Q75.3__S1_13-E01` | Macrocéphalie familiale bénigne (mégalencéphalie familiale) | 1 | ⬜ |  |  |
| 9 | `R10.4__O2_9-E01` | Coliques du nourrisson (pleurs excessifs fonctionnels) | 1 | ⬜ |  |  |
| 10 | `R56.0__S7_10-E03` | Convulsions fébriles simples de l'enfant (6 mois – 5 ans) | 1 | ⬜ |  |  |
| 11 | `R63.3__O2_6-E02` | Néophobie alimentaire physiologique et sélectivité bénigne d | 1 | ⬜ |  |  |
| 12 | `R95__G14-E08` | Syndrome de mort subite du nourrisson (MSN / MIN) | 1 | ⬜ |  |  |
| 13 | `Z63.4__O6_7-E01` | Deuil normal (réaction aiguë et processus d'adaptation à la  | 1 | ⬜ |  |  |
| 14 | `Z63.5__O6_6-E02` | Détresse psychologique et somatisations de l'enfant face au  | 1 | ⬜ |  |  |
| 15 | `Z71.8__O2_2-E04` | Crises de colère / opposition physiologiques du jeune enfant | 1 | ⬜ |  |  |
| 16 | `A41.9__O2_8-E03` | Infection foudroyante méconnue du nourrisson (sepsis à ménin | 2 | ⬜ |  |  |
| 17 | `P08.2__O1_1-E06` | Grossesse prolongée / Post-maturité (>= 42 0/7 SA) | 2 | ⬜ |  |  |
| 18 | `Q39.3__S2_9-E05` | Anneau de Schatzki (anneau muqueux œsophagien inférieur) | 2 | ⬜ |  |  |
| 19 | `R68.1__O2_8-E08` | Malaise grave du nourrisson (BRUE à haut risque / ancien ALT | 2 | ⬜ |  |  |
| 20 | `Z63.4_1__O6_7-E05` | Deuil périnatal (fausse couche, IMG, mortinatalité, mort sub | 2 | ⬜ |  |  |
| 21 | `J21.0__S2_1-E12` | Bronchiolite aiguë du nourrisson | 3 | ⬜ |  |  |
| 22 | `J21.9__F1_10-E16` | Bronchiolite aiguë grave du nourrisson avec apnées et cyanos | 3 | ⬜ |  |  |
| 23 | `P22.0__O1_1-E11` | Syndrome de détresse respiratoire néonatale (maladie des mem | 3 | ⬜ |  |  |
| 24 | `P36.9__O1_1-E15` | Sepsis néonatal précoce (< 72 h) | 3 | ⬜ |  |  |
| 25 | `P39.1__O7_12-E17` | Conjonctivite néonatale (à gonocoque ou Chlamydia trachomati | 3 | ⬜ |  |  |
| 26 | `P52.2__O1_1-E14` | Hémorragie intraventriculaire (HIV) du prématuré | 3 | ⬜ |  |  |
| 27 | `P55.0_1__O1_3-E13` | Incompatibilité rhésus sévère avec anémie fœtale (allo-immun | 3 | ⬜ |  |  |
| 28 | `P56.0__F2_17-E15` | Anasarque fœto-placentaire (hydrops fetalis) sur allo-immuni | 3 | ⬜ |  |  |
| 29 | `P57.9__F2_17-E16` | Ictère nucléaire (encéphalopathie bilirubinique aiguë) | 3 | ⬜ |  |  |
| 30 | `P61.4__O2_7-E14` | Anémie fœtale sévère sur hémorragie fœto-maternelle massive  | 3 | ⬜ |  |  |
| 31 | `P70.4__O1_1-E12` | Hypoglycémie néonatale sévère ou symptomatique | 3 | ⬜ |  |  |
| 32 | `P74.1__O1_6-E13` | Déshydratation hypernatrémique sévère du nouveau-né allaité | 3 | ⬜ |  |  |
| 33 | `P77.9__O1_1-E13` | Entérocolite nécrosante (ECN) du nouveau-né | 3 | ⬜ |  |  |
| 34 | `P77__S3_9-E14` | Entérocolite nécrosante du nouveau-né prématuré (ECN) | 3 | ⬜ |  |  |
| 35 | `P80.8__O1_1-E16` | Hypothermie néonatale sévère (< 35,0 °C) | 3 | ⬜ |  |  |
| 36 | `P83.2__O1_3-E12` | Hygroma kystique cervical avec hydrops fœtal (anasarque T1/T | 3 | ⬜ |  |  |
| 37 | `P94.0__O2_11-E18` | Myasthénie néonatale transitoire ou syndrome myasthénique co | 3 | ⬜ |  |  |
| 38 | `Q30.0__S1_15-E11` | Atrésie choanale bilatérale du nouveau-né | 3 | ⬜ |  |  |
| 39 | `Q52.3__S4_1-E14` | Hématocolpos sur imperforation hyménéale | 3 | ⬜ |  |  |
| 40 | `Q85.0__S6_3-E14` | Syndrome de Peutz-Jeghers / neurofibromatose de type 1 (macu | 3 | ⬜ |  |  |
| 41 | `R06.8__S2_1-E11` | Malaise grave du nourrisson (BRUE à haut risque / apnée prol | 3 | ⬜ |  |  |
| 42 | `R45.8__O6_6-E11` | Crise suicidaire aiguë suite à une rupture ou perte de garde | 3 | ⬜ |  |  |
| 43 | `R56.0_1__O4_2-E15` | Convulsions fébriles post-vaccinales du nourrisson | 3 | ⬜ |  |  |
| 44 | `T67.0__O2_8-E14` | Hypothermie ou hyperthermie extrême (coup de chaleur) du nou | 3 | ⬜ |  |  |
| 45 | `Z62.8_1__O6_6-E14` | Enlèvement ou rétention illicite d'enfant redouté / crise de | 3 | ⬜ |  |  |
| 46 | `Z63.5_1__O6_6-E13` | Fugue ou mise en danger aiguë d'un enfant/adolescent lors d' | 3 | ⬜ |  |  |
| 47 | `P05.0__O1_1-E08` | Petit poids constitutionnel (SGA sans RCIU pathologique) | 4 | ⬜ |  |  |
| 48 | `P07.2__O1_1-E07` | Extrême prématurité (< 28 0/7 SA) | 4 | ⬜ |  |  |
| 49 | `P55.0__F2_17-E08` | Maladie hémolytique du nouveau-né par incompatibilité RhD | 4 | ⬜ |  |  |
| 50 | `P59.3__O1_6-E07` | Ictère au lait de mère (ictère tardif du nourrisson allaité) | 4 | ⬜ |  |  |
| 51 | `P80.9__G8-E07` | Hypothermie néonatale par perte thermique précoce | 4 | ⬜ |  |  |
| 52 | `Q05.9__O1_3-E07` | Anomalies de fermeture du tube neural (spina bifida, anencép | 4 | ⬜ |  |  |
| 53 | `Q53.9__O2_12-E08` | Cryptorchidie (testicule non descendu) | 4 | ⬜ |  |  |
| 54 | `Q67.3__S1_4-E08` | Plagiocéphalie positionnelle et torticolis musculaire congén | 4 | ⬜ |  |  |
| 55 | `Q75.0__S1_13-E05` | Craniosténose (synostose prématurée d'une ou plusieurs sutur | 4 | ⬜ |  |  |
| 56 | `Q86.0__O2_5-E07` | Syndrome d'alcoolisation fœtale (SAF / TCAF) | 4 | ⬜ |  |  |
| 57 | `Z62.8__O6_6-E07` | Aliénation parentale / instrumentalisation grave de l'enfant | 4 | ⬜ |  |  |
| 58 | `Z63.4_2__O6_7-E06` | Deuil chez l'enfant et l'adolescent | 4 | ⬜ |  |  |
| 59 | `P28.4__S2_1-E09` | Apnée du prématuré (immaturité des centres respiratoires néo | 5 | ⬜ |  |  |
| 60 | `P35.1__O1_1-E09` | RCIU d'origine infectieuse congénitale (CMV, toxoplasmose, r | 5 | ⬜ |  |  |
| 61 | `Q15.0__O2_9-E10` | Glaucome congénital (buphtalmie, larmoiement, photophobie) | 5 | ⬜ |  |  |
| 62 | `Q43.0_1__S4_7-E10` | Diverticule de Meckel compliqué (douleur pelvienne / FID) | 5 | ⬜ |  |  |
| 63 | `Q43.0__S3_9-E10` | Diverticule de Meckel hémorragique (hétérotopie muqueuse gas | 5 | ⬜ |  |  |
| 64 | `Q44.2__S6_5-E10` | Atrésie des voies biliaires (ictère cholestatique du nourris | 5 | ⬜ |  |  |
| 65 | `Q65.8__O2_12-E10` | Dysplasie développementale de la hanche (DDH) | 5 | ⬜ |  |  |
| 66 | `Q76.3__S5_1-E09` | Scoliose congénitale sur malformation vertébrale (hémivertèb | 5 | ⬜ |  |  |
| 67 | `Q77.4__S5_3-E10` | Achondroplasie / dysplasie squelettique génétique | 5 | ⬜ |  |  |
| 68 | `Q85.1__S6_3-E10` | Sclérose tubéreuse de Bourneville (macules hypomélaniques en | 5 | ⬜ |  |  |
| 69 | `Q89.2__S1_9-E10` | Kyste du tractus thyréoglosse ou kyste branchial cervical | 5 | ⬜ |  |  |

Signature : AAI (Anthropic AI)
