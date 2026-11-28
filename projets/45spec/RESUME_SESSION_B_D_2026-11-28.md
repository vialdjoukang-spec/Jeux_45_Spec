# Résumé de session — 45 Spec, groupes B et D (27–28.11.2026)

## Le point de départ a changé d'emblée

La consigne demandait de reprendre le groupe B à la première fiche non produite. Le fichier `PROGRESSION_B.md` annonçait 42 fiches sur 439, mais il était périmé : `main` en portait déjà 435. Il ne restait que trois fiches, celles que l'audit avait rejetées (don d'organes, mobbing, médecines complémentaires). La quatrième, G93.2, existait déjà sous NEU.

## Ce qui a été produit

**12 fiches, toutes fusionnées sur `main`, contrôles verts à chaque lot** (0 menu long fautif, 0 erreur de validation, arène « erreurs: 0 »).

| Lot | Fiches |
|---|---|
| B (clôture) | Z52.9 don d'organes et consentement · Z56.6 mobbing · Z71.8_20 remboursement des médecines complémentaires |
| D1 | Z32.1_1 grossesse sous contraception · Z34.9 travail et grossesse · Z50.4 réhabilitation psychiatrique et emploi |
| D2 | Z50.8_1 réadaptation gériatrique et chutes · Z51.5_2 arrêt d'une suppléance vitale · Z53.1 refus de transfusion |
| D3 | Z54.0 incapacité de travail après accident · Z56.6_1 harcèlement sexuel au travail · Z60.2_1 isolement et précarité |

## Jauge en fin de session

| Groupe | Jauge | Fait / Total |
|---|---|---|
| A | `████████████████████` | 500 / 500 (100 %) |
| B | `████████████████████` | 500 / 500 (100 %) |
| C (autre session) | `███░░░░░░░░░░░░░░░░░` | 125 / 800 (16 %) |
| D | `███░░░░░░░░░░░░░░░░░` | 118 / 725 (16 %) |
| Total | `██████████░░░░░░░░░░` | 1 243 / 2 525 (49 %) |

Le groupe C n'a pas été touché : une autre session le produisait en même temps.

## Obstacles rencontrés

- **Réseau.** Les sites officiels étaient bloqués au départ. Huit hôtes ont été ouverts avec l'accord de Vial (OFSP, admin.ch, SECO, portail PME, ASSM, FMH, Swisstransplant, Cloudinary). Une seconde demande (NICE, SSGO, Swiss Medical Weekly, Revue médicale suisse, AAFP, DermNet, EAU, FSRH, OFAS, AVS-AI) a été refusée ; le travail s'est fait sans.
- **Test de l'arène.** `test_arene.py` ne tourne pas dans cet environnement (module Python Playwright absent). Le même test a été rejoué avec le Playwright Node préinstallé, sans modifier le dépôt.
- **Permission refusée.** Au lot D2, le push vers `main` a été bloqué par le classificateur de permissions. Arrêt et signalement ; la fusion est passée après le « Termine » de Vial.
- **Conflits de fusion.** Uniquement sur des fichiers générés (decks de l'arène, classement), résolus en les régénérant.

## Points fragiles à vérifier

Chaque source citée a été ouverte, sauf quand la fiche porte « à vérifier ».

### Les plus sensibles

- **Deux questions difficiles reposent sur des sources non lues** :
  - Z56.6 : arrêts du Tribunal fédéral 4A_391/2016 et 1C_595/2023 sur l'incapacité limitée au poste (connus par des résumés de recherche seulement) ;
  - Z32.1_1 : interactions des contraceptifs avec les inducteurs enzymatiques (rifampicine, antiépileptiques, millepertuis), renvoyées à l'AIPS.
- **Z53.1, adulte inconscient** : la fiche suit l'avis des HUG de 2004 (la carte de refus n'est qu'un élément de la décision), alors que le droit de la protection de l'adulte de 2013 rend les directives anticipées contraignantes. La discordance est signalée, pas tranchée ; le Code civil n'a pas été relu.
- **Posologie** : une seule dans la session, la vitamine D à 800 UI/j (Z50.8_1), tirée d'un article suisse de 2013 qui cite l'OFSP 2012 ; non vérifiée sur compendium.ch.

### Par fiche

- **Z52.9** : calendrier du consentement présumé (registre au second semestre 2027, entrée en vigueur au premier semestre 2028 selon les pages OFSP ; un communiqué du 22.01.2026 dit encore « automne 2026 ») ; arrêt du registre Swisstransplant en 2022 non relu ; révision ASSM 2025 des directives sur le diagnostic de la mort non vérifiée.
- **Z56.6** : la brochure SECO date le chiffre de 6,8 % tantôt de 2012, tantôt de 2015 ; rôle du médecin et dépistage du risque suicidaire sur avis d'expert.
- **Z71.8_20** : participation aux coûts mentionnée sans chiffre ; conseil de ne pas abandonner un traitement efficace sur avis d'expert.
- **Z32.1_1** : conduite précise après oubli de pilule non citée (figures des recommandations CDC 2024 illisibles en texte) ; source américaine faute d'accès à la SSGO ; délai d'oubli de la pilule au désogestrel renvoyé à l'AIPS.
- **Z34.9** : signes d'alarme obstétricaux sur avis d'expert.
- **Z50.4** : quatre des huit principes du soutien à l'emploi lus dans l'article vaudois ; rôle de l'assurance-invalidité à vérifier.
- **Z50.8_1** : sources de 2010 et 2013 ; déconditionnement hospitalier sur avis d'expert.
- **Z51.5_2** : l'équivalence stricte entre « ne pas commencer » et « interrompre » n'est pas écrite telle quelle dans les directives ASSM ; statut de ces directives dans le code FMH non relu.
- **Z53.1** : capacité de discernement jugée acte par acte, tirée d'un résumé de recherche.
- **Z54.0** : indemnité de 80 % dès le 3e jour tirée d'un rapport fédéral de 2009 (règle stable, gain maximal non cité) ; liste des lésions assimilées non relue.
- **Z56.6_1** : chiffres d'une étude de 2008 ; guide SECO du 22.12.2025 non téléchargé ; conduite après une violence sur avis d'expert.
- **Z60.2_1** : définition de l'isolement, aides sociales et conduite pratique sur avis d'expert ; chiffres arrêtés à 2019.

### Hors mandat, à traiter ailleurs

- **Catalogue** : il range la thérapie neurale parmi les cinq médecines remboursées, ce que l'OFSP contredit. La fiche Z71.8_20 suit l'OFSP ; l'amorce du catalogue reste à corriger.
- **13 fiches du groupe B** n'ont pas exactement 20 questions (18, 21 ou 22), dont plusieurs en PED, NEU et PSY.

## Ce qui reste

607 fiches en D et 675 en C. Au rythme d'une fiche vérifiée à la fois, D seul demande environ 200 lots.

Deux façons d'avancer :
- continuer lot par lot (le plus sûr pour la qualité, très long) ;
- paralléliser avec plusieurs agents producteurs, relus par la session principale (plus rapide, plus coûteux, à demander explicitement).

Rouvrir NICE, la SSGO et Swiss Medical Weekly améliorerait les sources des fiches cliniques qui arrivent.

Prochaines fiches au rang : Z60.2 et suivantes du groupe D. Branche de travail : `agent/45spec-D`. Formes compactes : `projets/45spec/compact_B/b04…b06`, `projets/45spec/compact_D/d01…d09`.

Signature : AAI (Anthropic AI)
