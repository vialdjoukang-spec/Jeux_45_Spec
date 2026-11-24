# Audit médical des branches agents du 45 Spec (PSY, NEU, INF, PED)

Date : 2026-11-24 · Branches : `agent/45spec-PSY`, `agent/45spec-NEU`, `agent/45spec-INF`, `agent/45spec-PED` · Auditeur : Claude (AAI)
Méthode : celle de `AUDIT_VAGUE1.md` (contrôle mécanique exhaustif par `scripts/audit_vague1.py`, puis audit médical par échantillon).

## Verdict

| Branche | Verdict | Raison |
|---|---|---|
| PSY | **Fusionnable** | 0 anomalie mécanique après correction ; 0 erreur factuelle dans l'échantillon. |
| NEU | **Non fusionnable en l'état** | 14 menus longs gardent 4 réponses justes ; le fond est juste. |
| INF | **Non fusionnable en l'état** | 30 menus longs gardent 4 à 7 réponses justes ; le fond est juste. |
| PED | **Non fusionnable en l'état** | 61 menus longs gardent 4 à 7 réponses justes ; le fond est juste. |

NEU, INF et PED deviennent fusionnables dès que leurs menus longs respectent la règle « 1 à 3 réponses justes ». Le jeu annonce en effet au joueur « Menu long : une à trois réponses » (`conception/prototypes/arene45/index.html`). Une question à 6 réponses justes devient donc impossible à réussir.

## 1. Contrôles mécaniques (tous les fichiers produits au 24.11.2026)

| Contrôle | PSY (33 fichiers, 632 QCM) | NEU (35, 708) | INF (30, 591) | PED (39, 799) |
|---|---|---|---|---|
| Ratio A / Kprim / menu long | 71 / 19 / 10 % | 70 / 20 / 10 % | 70 / 20 / 10 % | 71 / 20 / 10 % |
| Type A, Kprim, explications, sources, notions, CNP/CPCM | conforme | conforme | conforme | conforme |
| Correction validée par `valider()` | 8 en défaut → 0 | conforme | conforme | conforme |
| Diagnostic masqué nommé | 15 fuites → 0 | 5 → 2 faux positifs | 19 → 1 faux positif | 17 → 0 |
| Menu long à plus de 3 réponses justes | 0 | 14 → **14** | 36 → **30** | 73 → **61** |

- **Corrections PSY** : le renommage des 8 pathologies fusionnées (commit `3ab47d6a`) avait remplacé l'objet `ssp` (code, nom, algorithme) par un simple code. L'audit a restauré l'objet d'origine depuis l'historique git, sans toucher au contenu.
- **Fuites du diagnostic** : 53 questions de prise en charge nommaient l'entité dans la vignette. Elles passent en `diagnosticMasque: false`, comme dans la vague 1. Les 3 faux positifs relus (NEU G43.9 Q11, NEU G95.2 Q16, INF A69.2_1 Q18) posent bien la question du diagnostic sans le nommer. Ils restent à ajouter à `scripts/audit_vague1_revus.json` sur main, car l'audit n'a pas le droit de modifier `scripts/`.

## 2. Audit médical par échantillon

Chaque branche a fourni 6 pathologies, soit 24 au total, choisies parmi les plus fréquentes à l'examen. Chacune contient les 4 formats : A, Kprim, menu long et séries progressives. L'audit a vérifié la réponse juste de chaque type A et de chaque menu long, les 4 affirmations de chaque Kprim, puis chaque seuil et chaque posologie de la `priseEnCharge`. Il a donné la priorité aux sources suisses (AIPS, OFSP, LCR, CC), puis aux recommandations ESO, ESC, EAN, ESCMID, CANMAT/ISBD et ILAE.

| Branche | Pathologies auditées | QCM vérifiés | Erreurs factuelles | Taux estimé | Corrigées |
|---|---|---|---|---|---|
| PSY | F32.1 dépression, F41.0 panique, F10.3 sevrage alcoolique, F05.9 delirium, F31.3 bipolaire, F20.9 schizophrénie | 118 | 0 | < 1 % (0/118) | ras ; 8 `ssp` restaurés |
| NEU | I63.9 AVC, G41.0 état de mal, G00.9 méningite, G43.9 migraine, G40.9 première crise, G61.0 Guillain-Barré | 125 | 0 | < 1 % (0/125) | ras |
| INF | A15.0 tuberculose, A46 érysipèle, A04.7 C. difficile, B24 VIH, A09.0 gastro-entérite, A69.2 neuroborréliose | 120 | 0 (6 menus longs hors format) | < 1 % (0/120) | oui (format) |
| PED | J21.0 bronchiolite, R56.0 convulsion fébrile, P59.9 ictère, P36.9 sepsis précoce, P70.4 hypoglycémie, Q65.8 DDH | 125 | 0 (12 menus longs hors format) | < 1 % (0/125) | oui (format) |

Au total, l'échantillon ne contient aucune erreur factuelle sur 488 QCM. La borne haute à 95 % se situe à environ 0,6 %. Les points sensibles ont été vérifiés en ligne :
- la tuberculose compte 366 cas en 2022 (OFSP) ;
- l'isolement se lève après 5 à 15 jours de traitement efficace, et l'IGRA du contact se fait 2 mois après l'exposition (manuel OFSP) ;
- Latuda est autorisé en Suisse dans la dépression bipolaire I depuis le 01.11.2020 (OFSP).

Les 24 pathologies portent `audit.rejector = "pass"` dans leurs trois fichiers (questions, notions et correction). Dans ces 24 corrections, 48 posologies standard vérifiées perdent la mention « à vérifier dans l'AIPS ».

## 3. Défauts systématiques

1. **Menus longs à 4–7 réponses justes (NEU, INF, PED).** Le défaut est massif en INF et en PED : il touche les deux menus longs finaux de presque chaque fichier. Les réponses en trop sont médicalement vraies, et leur explication l'est aussi. Le défaut tient au format, pas au fond. Sa cause est simple : `agent_ecrire.py` et `valider()` ne contrôlent que 12 à 20 options, sans contrôler 1 à 3 justes.
   - **Correction modèle**, appliquée aux 18 menus longs de l'échantillon : l'audit garde les 3 réponses les plus importantes, réécrit chaque réponse en trop en distracteur faux avec son explication, et précise « Choisissez les TROIS… » dans l'énoncé. Le nombre d'options reste de 12.
   - **À faire par les producteurs** : appliquer la même correction aux 105 menus longs restants (liste : `python scripts/audit_vague1.py --specs NEU,INF,PED`), puis ajouter le contrôle 1–3 dans `projets/45spec/agent_ecrire.py` et dans le skill `45spec-production-sans-api`.
2. **Script de fusion/renommage (PSY)** : il écrasait `ssp`. Les 8 fichiers touchés sont réparés. Le script doit recopier l'objet `ssp` entier.
3. **Canal de déclaration** : la recherche a porté sur toutes les mentions de déclaration à l'OFSP dans les 4 branches. Elle n'a trouvé qu'une imprécision : PED P39.1 écrivait « Déclaration à l'OFSP » au lieu de « Déclaration par le laboratoire (OFSP et médecin cantonal) ». Le point est corrigé. Toutes les autres mentions sont justes.
4. **Recherche ciblée sans résultat** : l'audit n'a trouvé ni métronidazole en premier choix pour C. difficile, ni recommandation du BCG, ni vaccination rotavirus erronée, ni lieu CNP/CPCM.

## Points à vérifier (non bloquants)

- Les mentions « à vérifier » restent nombreuses (PSY 125, NEU 417, INF 997, PED 362). La plupart portent sur des posologies standard. Elles se résolvent par lot à partir de l'AIPS.
- L'autorisation suisse de la ténectéplase dans l'AVC reste à vérifier (NEU I63.9), ainsi que l'absence de vaccin contre la maladie de Lyme autorisé en Suisse à fin 2026 (INF A69.2, Q18).
- Le seuil de SpO2 de la bronchiolite suit SAPP 2003 (> 92 %). Il reste à confronter à une éventuelle mise à jour suisse.

Signature : AAI (Anthropic AI)
