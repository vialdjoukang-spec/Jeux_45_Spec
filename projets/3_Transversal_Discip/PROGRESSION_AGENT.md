# Progression de l'agent de production — Transversal

Signature : AAI (Anthropic AI). Statut des leçons rédigées : « RÉDIGÉ — à auditer par Claude ».

## Leçons rédigées par lettre

| Lettre | Rédigées | Total |
|---|---|---|
| A | 12 | 12 |
| B | 12 | 12 |
| C | 12 | 12 |
| D | 12 | 12 |
| E | 12 | 12 |
| F | 12 | 12 |
| G | 12 | 12 |
| H | 12 | 12 |
| I | 12 | 12 |
| J | 12 | 12 |
| K | 12 | 12 |
| L | 12 | 12 |
| M | 12 | 12 |
| N | 12 | 12 |
| O | 12 | 12 |
| P | 9 | 12 |
| Q | 12 | 12 |
| R | 0 | 12 |
| S | 12 | 12 |
| **Total** | **213** | **228** |

## Points à vérifier (_meta.aVerifier)

- **TRANS_A-S4-01** : Contenu des ATF cités comme distracteurs ou repères (130 V 352 de 2004, 137 V 210 de 2011, 143 V 409/418 de 2017) : cohérent avec la doctrine connue mais non relu sur bger.ch (base inaccessible pendant l'audit). Vérifiés : ATF 125 V 351 (critères de valeur probante, guide FMH) et le changement de pratique de 2015 (arrêt 9C_492/2014 publié ATF 141 V 281, circulaire OFAS du 7.7.2015).
- **TRANS_P-S1-01** : Résultats de l'étude de Haynes (NEJM 2009) : mortalité de 1,5 % à 0,8 % et complications de 11 % à 7 % après introduction de la checklist ; à confirmer avant citation chiffrée.
- **TRANS_P-S1-01** : Programme pilote progress! « La sécurité en chirurgie » de Sécurité des patients Suisse (2012-2015) et taux d'utilisation actuel de la checklist dans les hôpitaux suisses.
- **TRANS_P-S1-02** : Références originales du modèle de Reason (Human Error, 1990 ; BMJ 2000;320:768-770) et distinction entre erreurs actives et conditions latentes.
- **TRANS_P-S1-02** : Modèle de la « culture juste » (just culture) et algorithme de décision sur la responsabilité individuelle (par exemple l'arbre de culpabilité de Reason).
- **TRANS_P-S1-03** : Recommandations de Sécurité des patients Suisse sur le KCl concentré (programme progress! « La sécurité de la médication », retrait des ampoules concentrées des unités) et sur l'identification des patients (deux identifiants).
- **TRANS_P-S1-03** : Liste suisse des médicaments à haut risque (high-alert) et doubles contrôles recommandés.
- **TRANS_P-S2-01** : Protection juridique des déclarations CIRS en Suisse (absence de protection légale explicite jusqu'à la révision de la LAMal ? art. 58g LAMal ou projet de loi sur la protection des données de qualité) : statut 2026 à confirmer.
- **TRANS_P-S2-01** : Fonctionnement actuel du réseau CIRRNET de Sécurité des patients Suisse et nombre d'établissements participants.
- **TRANS_P-S2-02** : Titre et date de la brochure de Sécurité des patients Suisse « Quand un incident survient » (2006) et éventuelle mise à jour.
- **TRANS_P-S2-02** : Clauses des assurances RC professionnelles suisses sur la reconnaissance de responsabilité et articulation avec l'excuse (lois « apology » inexistantes en Suisse).
- **TRANS_P-S2-03** : Proportion de patients présentant au moins une divergence médicamenteuse non intentionnelle à l'admission (souvent citée entre 30 et 70 %) : non écrite faute de chiffre suisse vérifié.
- **TRANS_P-S2-03** : Format et diffusion en 2026 de l'eMediplan suisse et du dossier électronique du patient (DEP) pour la transmission des traitements.
- **TRANS_P-S3-01** : Données sur l'effet des interruptions de tâche sur les erreurs d'administration médicamenteuse (Westbrook et al., Arch Intern Med 2010 : risque augmenté d'environ 12 % par interruption) : chiffre non écrit dans le texte.
- **TRANS_P-S3-01** : Limites de durée du travail des médecins assistants en Suisse (50 heures par semaine selon la LTr depuis 2005) et projet de semaine de 42 + 4 heures.
- **TRANS_P-S3-02** : Liste actuelle des mesures nationales de l'ANQ en soins aigus (réadmissions potentiellement évitables, infections du site opératoire Swissnoso, chutes et escarres, satisfaction des patients) et publication transparente des résultats par hôpital.
- **TRANS_P-S3-02** : Rôle de la Commission fédérale pour la qualité (CFQ) instituée par l'art. 58b LAMal révisé (en vigueur depuis le 1.4.2021).
- **TRANS_P-S3-03** : Ressources suisses de soutien aux secondes victimes en 2026 (programmes hospitaliers de soutien par les pairs, ReMed de la FMH, recommandations de Sécurité des patients Suisse).
- **TRANS_P-S3-03** : Données sur la prévalence des symptômes chez les secondes victimes (environ la moitié des soignants impliqués selon les études) : chiffre non écrit.
- **TRANS_S-S4-01** : Le titre (catalogue) annonce une « méthode suisse » de tri que l'audit n'a pas pu identifier dans les sources officielles : le SSC élabore un concept national d'afflux massif ; le corps de la leçon reste juste. Décider s'il faut renommer le titre au catalogue.

## Conventions de format utilisées (pour l'audit et le moteur de jeu)

- `parties` : 9 chaînes de texte (une par clé « 1. Cadre » … « 9. Exercices et répétition »).
- `items[].type` : « A » (5 options), « Kprim » (4 affirmations), « menu long » (12 à 20 options). Répartition par leçon : 4 A + 1 Kprim, ou 3 A + 1 Kprim + 1 menu long (≈ 70 / 20 / 10 %).
- `bonneReponse` : lettre (« A » à « E », ou « A » à « T » pour le menu long) ; liste de 4 booléens pour Kprim.
- `explicationParOption` : clés « A »… pour A et menu long, « 1 »… « 4 » pour Kprim (chaque explication Kprim commence par « Vrai » ou « Faux », contrôlé par script).
- `bulle` : {def, pourquoi, confusion, retenir}. `liensSSP` : codes du catalogue PROFILES (ex. « F1.18 »).
- `_meta` ajoutés : `signature`, `aVerifier`, `sources`.

## Arrêt et reprise

Premier agent : S, F, Q, A, B. Second agent (reprise) : C, D, E, G, H, puis I à P, R dans cet ordre. Lettres restantes : P (9/12), R (0/12).
