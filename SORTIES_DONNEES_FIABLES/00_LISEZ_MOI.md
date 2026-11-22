# Sorties de données fiables

Ce dossier ne contient que les données qui ont passé l'audit de fond de Claude : un examen y entre si son cœur clinique est rempli (visees, signeRecherche, seuil, indication, discriminant, avantageSelectif, plutotQue, limite, precautions, irradiation_mSv, delai) et si aucun doute ne reste ouvert sur lui. La liste aCompleter de chaque fichier nomme les examens fiables auxquels il manque encore les champs de présentation (synonymes, aspectNormal, anomaliesElementaires, syndromesParacliniques, pathologiesAssociees) : ils partent en lot de complément. Le jeu peut les charger telles quelles. Les sources de travail restent dans `conception/donnees/` ; ce dossier est régénéré par `python projets/outils/audit_fond.py`.

Mise à jour : 2026-11-22 · 554 examens fiables sur 820 · 464 à compléter en présentation · 299 justifications acceptées · 25 doutes encore ouverts.

| Organe | Examens | Fiables | Doutes ouverts |
|---|---|---|---|
| Articulation temporo-mandibulaire et dents | 4 | 0 | 0 |
| Cavité buccale et glandes salivaires | 11 | 7 | 0 |
| Encéphale | 31 | 24 | 5 |
| Hypophyse et hypothalamus | 12 | 7 | 5 |
| Méninges et LCR | 7 | 4 | 3 |
| Nerfs crâniens | 8 | 0 | 0 |
| Nez, sinus et cavum | 12 | 6 | 2 |
| Œil et orbite | 22 | 17 | 1 |
| Oreille et équilibre | 14 | 11 | 0 |
| Os du crâne et de la face | 7 | 3 | 0 |
| Ganglions cervicaux | 9 | 3 | 1 |
| Larynx et pharynx | 10 | 8 | 0 |
| Masses cervicales et kystes | 5 | 0 | 0 |
| Parathyroïdes | 7 | 7 | 0 |
| Thyroïde | 10 | 8 | 0 |
| Vaisseaux du cou et de la tête | 8 | 8 | 0 |
| Moelle épinière | 7 | 7 | 0 |
| Queue de cheval et cône terminal | 3 | 0 | 0 |
| Rachis osseux | 13 | 6 | 0 |
| Racines et plexus | 9 | 3 | 0 |
| Aorte thoracique et artères pulmonaires | 10 | 6 | 0 |
| Cœur et péricarde | 29 | 29 | 0 |
| Diaphragme et muscles respiratoires | 6 | 0 | 0 |
| Médiastin | 11 | 7 | 0 |
| Œsophage | 8 | 8 | 0 |
| Paroi thoracique et côtes | 6 | 4 | 0 |
| Plèvre | 7 | 7 | 0 |
| Poumons et voies aériennes | 32 | 32 | 0 |
| Seins | 13 | 9 | 0 |
| Aorte abdominale et vaisseaux digestifs | 6 | 6 | 0 |
| Appendice | 7 | 0 | 0 |
| Côlon, rectum et anus | 19 | 16 | 0 |
| Estomac et duodénum | 14 | 11 | 0 |
| Foie | 18 | 16 | 2 |
| Intestin grêle | 10 | 10 | 0 |
| Pancréas | 13 | 13 | 0 |
| Paroi abdominale et hernies | 4 | 0 | 0 |
| Péritoine et ascite | 5 | 5 | 0 |
| Rate | 10 | 4 | 0 |
| Reins | 18 | 18 | 0 |
| Rétropéritoine | 5 | 0 | 0 |
| Surrénales | 13 | 13 | 0 |
| Uretères | 9 | 4 | 0 |
| Veines caves et système porte | 8 | 8 | 0 |
| Vésicule et voies biliaires | 10 | 10 | 0 |
| Grossesse, fœtus et placenta | 22 | 15 | 0 |
| Pénis et urètre masculin | 6 | 0 | 0 |
| Plancher pelvien | 7 | 5 | 0 |
| Post-partum et allaitement | 5 | 0 | 0 |
| Prostate et vésicules séminales | 6 | 3 | 3 |
| Testicules et scrotum | 9 | 7 | 0 |
| Utérus, col, ovaires et annexes | 15 | 15 | 0 |
| Vessie et urètre | 12 | 12 | 0 |
| Vulve, vagin et périnée | 4 | 0 | 0 |
| Artères des membres | 9 | 9 | 0 |
| Articulations et synoviale | 11 | 11 | 0 |
| Cheville et pied | 9 | 4 | 0 |
| Coude, poignet et main | 8 | 4 | 1 |
| Épaule | 8 | 4 | 0 |
| Genou | 8 | 5 | 0 |
| Hanche et bassin | 8 | 4 | 0 |
| Muscles | 8 | 8 | 0 |
| Nerfs périphériques | 9 | 8 | 1 |
| Os longs et squelette | 12 | 12 | 0 |
| Tendons et ligaments | 3 | 0 | 0 |
| Veines des membres | 8 | 5 | 0 |
| Ongles et cheveux | 6 | 6 | 0 |
| Peau | 13 | 13 | 0 |
| Plaies, ulcères et escarres | 7 | 7 | 0 |
| Corps entier (bilan d'extension et trauma) | 6 | 6 | 0 |
| Croissance et développement de l'enfant | 8 | 0 | 0 |
| Évaluation gériatrique globale | 8 | 0 | 0 |
| Génétique | 5 | 0 | 0 |
| Infection et immunité | 14 | 0 | 0 |
| Métabolisme et endocrinologie | 11 | 0 | 0 |
| Moelle osseuse et ganglions | 6 | 0 | 0 |
| Psyché | 7 | 0 | 0 |
| Sang et hémostase | 13 | 12 | 1 |
| Sommeil et vigilance | 7 | 7 | 0 |
| Système lymphatique | 7 | 7 | 0 |
| Toxicologie et médicaments | 6 | 0 | 0 |
| Urgences et point-of-care | 9 | 0 | 0 |

Signature : AAI (Anthropic AI)
