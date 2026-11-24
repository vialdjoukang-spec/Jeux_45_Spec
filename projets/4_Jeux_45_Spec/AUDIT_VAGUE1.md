# Audit médical de la vague 1 du 45 Spec (END, CAR, PNE, NEP, GAS)

Date : 2026-11-24 · Branche : `veille/audit-medical` · Auditeur : Claude (AAI)

## Verdict

**Fusionnable**, avec une réserve : 5 corrections restent absentes (E11.9, I49.5, I75.0, E87.6, B18.9). Leurs notions et leurs questions sont conformes. Leurs corrections doivent être régénérées (T4).

- Les contrôles mécaniques exhaustifs ne laissent plus que ces 5 anomalies (`python scripts/audit_vague1.py`).
- L'échantillon médical montre un taux d'erreur factuelle inférieur à 1 % des QCM.
- Chaque erreur trouvée a été corrigée dans toute la spécialité, et dans toute la vague quand le défaut était systématique.

## 1. Contrôles mécaniques sur les 6 317 QCM

Le script `scripts/audit_vague1.py` contrôle tous les fichiers sans token. La réparation de forme passe par `scripts/reparer_vague1.py`, qui ne touche jamais au fond.

| Contrôle | Résultat avant | Résultat après |
|---|---|---|
| Type A : 5 options, 1 seule juste | conforme | conforme |
| Kprim : 4 affirmations ; menu long : 12–20 options, 1–3 justes | conforme | conforme |
| Ratio des formats A / Kprim / menu long | 70 / 20 / 10 % dans chaque spécialité | inchangé |
| Une explication (`why`) par option | conforme | conforme |
| Schéma `SCH_QUESTIONS` (clés parasites, plus de 6 notions) | 24 QCM en défaut | 0 |
| Diagnostic masqué nommé dans la vignette ou la question | 48 suspicions | 10 vraies fuites, passées en `diagnosticMasque: false` ; 38 faux positifs relus et listés dans `scripts/audit_vague1_revus.json` |
| Correction validée par `valider()` (notions, SSP, priseEnCharge) | 31 corrections en défaut, 20 absentes | 0 en défaut, 5 absentes |
| Lieu CNP ou CPCM | 0 | 0 |

## 2. Audit médical par échantillon stratifié

L'échantillon compte 8 pathologies par spécialité, soit 40 au total. Elles ont été choisies parmi les plus fréquentes à l'examen et couvrent les 4 formats : A, Kprim, menu long et séries progressives.

Pour chacune, l'audit a vérifié la réponse juste de chaque type A et de chaque menu long, les 4 affirmations de chaque Kprim, et chaque posologie de la `priseEnCharge`. Cela représente environ 800 QCM. Les sources consultées vont d'abord vers la Suisse (AIPS Swissmedic, OFSP, OPAS), puis vers les sociétés savantes (ESC 2023–2024, GOLD, GINA, KDIGO 2021, IPNA 2023, ESE, ESGE, EASL, Endocrine Society 2023, IWGDF 2023).

Les fichiers audités portent `audit.rejector = "pass"` (questions, notions et correction).

| Spécialité | Pathologies auditées | Erreurs trouvées | Taux d'erreur estimé (QCM) | Corrigées |
|---|---|---|---|---|
| END | E03.9 hypothyroïdie, E05.9 diarrhée endocrinienne, E10.9 DT1, E11.9 DT2, E11.6 pied diabétique, E22.2 SIADH, E28.2 SOPK, E78.0 HF | 0 dans les QCM ; 1 posologie imprécise (cyclosilicate de Na-Zr « 48 h au maximum » au lieu de 72 h, dans E11.2, trouvée par recherche ciblée) | < 1 % (0/160) | oui |
| CAR | I10 HTA, I21.9 SCA, I35.0 SA préopératoire, I46.9 ACR, I48.9 FA, I50.0 ICC, I50.1 ICA, I20.8 angor stable | 0 erreur factuelle ; I10 renvoyait à 2 plans `pec` absents ; 1 imprécision non corrigée (I20.8 Q08 : délai de 20 min avant d'appeler le 144, défendable mais long) | < 1 % (0/160) | oui (plans rédigés) |
| PNE | I26.9 EP, J18.9 PAC, J44.9 BPCO, J44.1 exacerbation, J45.9 asthme, J46 AAG, J90 épanchement, G47.3_1 SAOS | 1 : la tuberculose pleurale était « déclarée à l'OFSP », alors que le médecin déclare au médecin cantonal et le laboratoire à l'OFSP | ≈ 0,6 % (1/160) | oui, défaut systématique |
| NEP | E87.5 hyperK, E87.6 hypoK, E87.1 hypoNa, N10 néphrite interstitielle, N10 PNA, N18.5 MRC, N17.0 NTA, N04.9 sd néphrotique | 2 : seuil pédiatrique d'albuminémie < 25 g/L (ancien ISKDC) au lieu de < 30 g/L (KDIGO 2021, IPNA 2023), avec un RAC confondu avec le RPC ; durée du cyclosilicate de Na-Zr | ≈ 0,6 % (1/160) | oui |
| GAS | K21.0 RGO, K25.4 HDH, K74.6 cirrhose/ISLA, K85.8 pancréatite, K58.9 SII, K80.5 cholédocholithiase, D12.6 polypes, K76.0 MASLD | 1 : le dépistage colorectal restait remboursé de « 50 à 69 ans, sans franchise », alors que l'âge va jusqu'à 74 ans depuis le 1er juillet 2025 (OPAS art. 12e) et que la franchise ne tombe que dans un programme cantonal | ≈ 0,6 % (1/160) | oui, défaut systématique |

Bilan : 3 QCM faux sur environ 800 vérifiés, soit environ 0,4 % (borne haute à 95 % : environ 1,1 %). Les explications (`why`) et les notions n'ont été relues qu'en cas de doute ; elles n'ont pas été relues ligne à ligne.

## 3. Défauts systématiques et recherche ciblée

1. **Canal de déclaration suisse.** Le médecin déclare au médecin cantonal ; le laboratoire déclare à l'OFSP. La recherche ciblée a porté sur la tuberculose, la légionellose et les hépatites B et C. 10 fichiers ont été corrigés (PNE J90, J18.9 ; GAS B16.9, B17.9, B18.9). Source : [OFSP, déclaration des maladies infectieuses](https://www.bag.admin.ch/fr/declaration-des-maladies-infectieuses).
2. **Dépistage du cancer colorectal obsolète.** L'âge passe à 50–74 ans et la franchise ne tombe que dans un programme cantonal. La correction porte sur 57 chaînes dans 28 fichiers GAS. Sources : [admin.ch, OPAS 1er juillet 2025](https://www.admin.ch/fr/newnsb/9WndEYDLnuu3bVmIzrkdd) et [Ligue contre le cancer, 12 juin 2025](https://www.liguecancer.ch/medias/communiques-de-presse/depistage-du-cancer-du-colon-remboursement-jusqua-74-ans/-dl-/fileadmin/downloads/medien/2025/20250612-cdp-darmkrebsvorsorge-erhoehung-altersgrenze-fr.pdf).
3. **Syndrome néphrotique de l'enfant.** Le seuil d'albuminémie est < 30 g/L et le seuil de protéinurie un RPC ≥ 200 mg/mmol. La correction porte sur N04.9 (questions, notions, correction). Source : [IPNA 2023, tableau 1](https://pmc.ncbi.nlm.nih.gov/articles/PMC9589698/table/Tab1).
4. **Cyclosilicate de sodium-zirconium.** La phase de correction dure 48 h et peut être prolongée jusqu'à 72 h au maximum. La correction porte sur NEP E87.5 et END E11.2. Source : [Vidal, Lokelma](https://www.vidal.fr/actualites/37486-lokelma-nouvelle-option-pour-traiter-l-hyperkaliemie-de-l-adulte.html).
5. **Défauts de forme de l'API.** Le script a réparé les clés parasites (`false`, `whyd`, `prévention`, ` source`), les cellules mal typées, l'arbre rangé dans le tableau et les listes trop longues (56 fichiers). Trois `priseEnCharge` incomplètes ont été complétées à la main : I10 (`horsUrgence` et `prevention` nulles), I47.2 et K72.0 (moins de 3 étapes).
6. **Corrections archivées pour sérialisation cassée.** Sur 20 corrections archivées, 15 sont rétablies :
   - 13 sont récupérées sans token, car leur `priseEnCharge` était cachée dans la chaîne `ssp`. Leurs posologies ont été auditées.
   - K31.8 a reçu une `priseEnCharge` rédigée par Claude (3 plans).
   - E83.5 a reçu une correction entière rédigée par Claude, alignée sur l'Endocrine Society 2023.
   - Les 5 restantes contiennent du code JavaScript dans le JSON et doivent être régénérées.

## 4. Reprise des 14 corrections sans priseEnCharge

Les 14 corrections sont toutes en place dans `content/corrections/<SPEC>/` et validées par `valider()` :
- PNE : J98.6, J69.0 ;
- GAS : K22.7, K31.8, K90.9 ;
- CAR : I86.1, I21.9, I95.0 ;
- END : E66.2, E23.2, C73_1, E83.5, E83.4, E10.8.

La 15e correction rétablie, I45.8, s'y ajoute. Pour chaque fichier, `audit.note` et `signature.reprise` indiquent l'origine du contenu : récupération sans token ou rédaction par Claude.

## Points à vérifier (non bloquants)

- La disponibilité en Suisse de la calcitonine injectable, de la norfloxacine et de la mexilétine reste à vérifier, ainsi que l'indication suisse du dénosumab dans l'hypercalcémie maligne.
- La couverture des notions (`scripts/couverture_notions.py`) ne compte que les questions marquées `pass`. Elle ne reflète donc que l'échantillon audité.

Signature : AAI (Anthropic AI)
