# Audit V2 groupe A — journal (80 pathologies produites par l'API)

Légende : 🟩 juste (réserves éventuelles notées) · 🟧 corrigé ou à vérifier · 🟥 rejeté.
Méthode : relecture complète des notions chiffrées, des posologies et des questions (réponses justes, menus longs 1 à 3 justes, diagnostic masqué des niveaux 4–5), puis contrôle mécanique `controle_menus_longs.py`.
Limite assumée : la lecture en ligne des sources primaires a échoué (PubMed renvoie une page de cookies) ; les seuils et doses ont été confrontés aux recommandations connues (ESC/ESVS, IDSA, ECIL-5, EASL, ARIA/EAACI, ASCRS, HerniaSurge, AIPS), et chaque doute est noté « à vérifier » dans le champ `audit.claude.aVerifier` des fichiers.
Contrôles transversaux sur les 80 : aucun CNP ni CPCM ; aucune mention de PEP VIH (règle des 48 h sans objet dans ces fichiers) ; 17 questions de niveau 4–5 non masquées recensées, à traiter pathologie par pathologie.

## Passage 1 — pathologies 1 à 10 sur 80

| # | Pathologie | Verdict | Corrections et points à vérifier |
|---|---|---|---|
| 1 | D84.8 Immunodépression iatrogène | 🟧 | Corrigé : durée de la prophylaxie anti-VHB précisée « après l'arrêt de l'immunosuppression » (EASL 2017) ; aciclovir i.v. ophtalmique limité à l'immunodéprimé (notion, correction, « why » de Q08). À vérifier : N04 (première cause d'immunodépression acquise, source absente). |
| 2 | J30.4 Rhinite allergique | 🟩 | Q11 (niveau 4) : diagnostic non nommé, `diagnosticMasque` passé à vrai. |
| 3 | J34.3 Hypertrophie des cornets | 🟩 | À vérifier : disponibilité suisse de l'association azélastine-fluticasone (AIPS). |
| 4 | I70.2_2 Ischémie critique chronique | 🟩 | À vérifier : pronostic à 1 an (amputation ≈ 25 %, mortalité ≈ 20 %) variable selon TASC II et ESC. |
| 5 | I73.8_2 Raynaud primaire, acrocyanose | 🟩 | Forme : clé `mesuresGénérales` hors schéma retirée. Hors AMM déjà signalé. |
| 6 | I83.0 Ulcère veineux | 🟩 | À vérifier : taux de cicatrisation à 6 mois (≈ 70 %). |
| 7 | I83.9_1 Varices, insuffisance veineuse | 🟩 | Forme : 31 cellules de tableau enveloppées pour respecter le schéma. À vérifier : polidocanol en grossesse (contre-indication relative). |
| 8 | K42.9 Hernie pariétale réductible | 🟩 | À vérifier : prophylaxie antibiotique (Swissnoso 2018) et énoxaparine, à ne pas rendre systématiques. |
| 9 | K56.4 Fécalome | 🟩 | Forme : deux notions de nature « surveillance » reclassées. À vérifier : définition du signe de Gersuny. |
| 10 | K60.0 Fissure anale | 🟩 | Source ASCRS harmonisée sur 2017 ; nature « suisse » corrigée en « contexte suisse ». À vérifier : référence ESGE 2020. |

Contrôles : `controle_menus_longs.py` ALL, ANG, CHI → 0 menu fautif ; reste 1 erreur de schéma sur K60.2 (correction sans `priseEnCharge`, pathologie 11 du prochain passage). Les spécialités CMF, HEM, MIG, OPH, ORL, PEA, TOX affichent encore des erreurs de schéma sur des pathologies non auditées (traitées aux passages suivants).

Reste à auditer : pathologies 11 à 80 (K60.2 → K52.1).
