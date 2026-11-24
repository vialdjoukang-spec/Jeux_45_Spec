# Manques du catalogue PED — 45 Spec

Date : 24.11.2026. Méthode : recherche par expression régulière sur le nom des 2626 entités de `canoniques()` (`scripts/produire_notions_questions.py`) et dans `content/pathologies` ; une entité est dite « pédiatrique » si son nom mentionne enfant, nourrisson, nouveau-né, adolescent, bébé ou infantile.
Constat : aucune des 12 pathologies pédiatriques majeures ci-dessous ne figure dans les entités canoniques PED. Six existent sous une forme pédiatrique dans une autre spécialité ; six n'existent qu'en version adulte ou générale.

| Pathologie pédiatrique | Spécialité canonique qui la porte | Entité(s) trouvée(s) | Verdict |
|---|---|---|---|
| Méningite bactérienne de l'enfant | NEU (générale), INF, HEM | `G00.9__F1_15-E17` Méningite bactérienne aiguë ; `G03.9__S1_16-E11` Méningite aiguë et syndrome méningé fébrile ; `A39.2__F1_4-E12` Purpura fulminans (INF) ; PED ne traite que `A41.9_1__O2_8-E03` (sepsis foudroyant du nourrisson, méningocoque compris) | Absente sous forme pédiatrique ; seulement générale (NEU) |
| Asthme de l'enfant (et bronchite obstructive) | PNE (adulte/général) | `J45.9_asthme_bronchique__F1_3-E02` Asthme bronchique ; `J46_asthme_aigu_grave__F1_3-E16` Asthme aigu grave | Absente sous forme pédiatrique ; seulement générale (PNE) |
| Laryngite (faux croup) | ORL | `J05.0__S1_3-E12` Laryngite aiguë sous-glottique de l'enfant (faux croup) ; `J05.0_1__S1_18-E11` Stridor aigu / laryngite sous-glottique ou épiglottite | Présente en ORL |
| Otite moyenne aiguë | ORL | `H66.9__O2_9-E02` Otite moyenne aiguë du nourrisson ; `H70.0__S1_4-E14` Mastoïdite aiguë | Présente en ORL |
| Pneumonie communautaire de l'enfant | PNE, INF (adulte/général) | `J18.9_pneumonie_communauta__F1_10-E04` Pneumonie communautaire ; `J86.9_1__F2_18-E14` Empyème pleural (CTH) | Absente sous forme pédiatrique ; seulement générale (PNE) |
| Infection urinaire fébrile / pyélonéphrite de l'enfant | NEP, URO, INT (adulte/général) | `N10_pyelonephrite_aigue___F2_15-E04` Pyélonéphrite aiguë simple (NEP) ; `N30.0__F2_15-E01` Cystite (URO) ; aucun reflux vésico-urétéral de l'enfant | Absente sous forme pédiatrique ; seulement générale (NEP/URO) |
| Invagination intestinale aiguë | CPE (+ CHI) | `K56.1__O2_4-E12` Invagination intestinale aiguë du nourrisson | Présente en CPE |
| Sténose hypertrophique du pylore | CPE | `Q40.0__O2_6-E11` Sténose hypertrophique du pylore du nourrisson | Présente en CPE |
| Maltraitance de l'enfant / bébé secoué | LEG (+ NCH, PEA) | `T74.1_11__O6_3-E03` Syndrome de l'enfant battu ; `T74.1__G13-E20` Syndrome du bébé secoué ; `T74.1_7__O2_9-E15` Fracture occulte sur maltraitance du nourrisson ; `T74.1_8__O2_12-E13` ; `T74.8_3__O7_24-E12` ; `T74.1_1__S1_13-E08` (NCH) ; `Z62.8_5__O7_24-E07` (PEA) | Présente en LEG |
| Diabète de type 1 / acidocétose de l'enfant | END (adulte/général), PEA | `E10.9__F1_8-E08` Diabète de type 1 ; `E10.1_acidocetose_diabetiq__F1_13-E11` Acidocétose diabétique ; `E10.1__S4_14-E13` Acidocétose inaugurale révélée par une énurésie (PEA) | Présente en PEA sous l'angle énurésie seulement ; la forme pédiatrique (œdème cérébral, protocole pédiatrique) est absente |
| Épilepsie de l'enfant | NEU | `G40.4__O2_5-E12` Spasmes infantiles (syndrome de West) ; `G40.3_2__S9_2-E08` et `G40.7__O2_10-E08` Épilepsie-absences de l'enfant (doublon probable) ; `G40.3_1__F1_19-E04` Épilepsie généralisée idiopathique | Présente en NEU (doublon `G40.3_2` / `G40.7` à fusionner) |
| Gastro-entérite avec déshydratation du nourrisson | INF (générale), INT | `A08.4__G5-E02`, `A09.0__F2_8-E02`, `A09.9__S3_1-E01` Gastro-entérite (INF) ; `A00.9__S3_8-E15` Déshydratation aiguë sévère du nourrisson avec choc (INT) ; PED ne porte que `P74.1__O1_6-E13` (déshydratation hypernatrémique du nouveau-né allaité) | Présente en INT pour la forme sévère avec choc ; la forme courante (réhydratation orale, SRO) est absente |

## Ce qu'il faut corriger au catalogue

1. **Les entités absentes partout sous forme pédiatrique** sont la méningite de l'enfant, l'asthme de l'enfant, la pneumonie de l'enfant, l'infection urinaire fébrile de l'enfant, le diabète de type 1 de l'enfant avec son acidocétose, et la gastro-entérite courante avec déshydratation légère à modérée. Il faut les créer en PED, ou ajouter le code PED aux entités générales (`codes`), car l'examen fédéral les interroge avec des seuils et des posologies propres à l'enfant.
2. **Les entités pédiatriques rangées ailleurs** (ORL, CPE, LEG, NEU, INT) restent valables, mais elles devraient porter aussi le code PED. Ainsi, un joueur qui choisit la pédiatrie les rencontrerait.
3. **Un doublon est à fusionner** : `G40.3_2__S9_2-E08` et `G40.7__O2_10-E08` portent le même nom (Épilepsie-absences de l'enfant).

Signature : AAI (Anthropic AI)
