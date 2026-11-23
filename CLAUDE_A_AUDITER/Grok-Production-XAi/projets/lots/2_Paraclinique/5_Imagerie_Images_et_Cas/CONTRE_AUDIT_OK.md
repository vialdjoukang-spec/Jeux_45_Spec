# CONTRE_AUDIT_OK — 5_Imagerie_Images_et_Cas

Contre-audit croisé interne terminé le 23.11.2026 03:33 (heure de Zurich).
Verdict : conforme après correction (P25) ; conforme (P23).

Fichiers couverts :
- P23_Images_reelles_Thorax_URL_et_licences_production_XAi.json (9 fichiers, 122 examens)
- P25_Cas_cliniques_Thorax_le_bon_examen_production_XAi.json (20 cas)

## P23
- Identité réelle vérifiée par script : les 122 examens sont identiques, champ par champ, à ceux des 21 fichiers de théorie du thorax du commit 2def72c (production-xai-a03-thorax, déjà contre-audités). Les 9 glossaires sont identiques eux aussi.
- Aucune image n'a été cherchée. Le squelette de main n'a pas de champ d'image.
- Avertissements hérités du thorax (source répétée, « à confirmer » au diaphragme) : non bloquants, laissés à l'audit externe.
- Aucune correction.

## P25
- Chaque conduite a été confrontée aux phrases sourcées des fiches thorax contre-auditées et aux critères P21 relus. Tous les nombres sont retrouvés : seuil de D-dimères ajusté à l'âge, RV 14/0,02 et 14/0,04, CURB-65 0,7 → 57 %, 91 % contre 50 %, critères de Light, pH ≤ 7,2, NT-proBNP < 125 ng/l, 0 h/1 h et 60 min, HEART 2,5 %, VEMS/CVF < 0,70 et z < −1,645, < 20 % d'épaississement, ACR 40 et 30 ans, BI-RADS 2.
- Le diagnostic de chaque cas est cohérent avec l'examen proposé (embolie ×4, aorte ×2, pneumonie, pneumothorax, plèvre, insuffisance cardiaque, SCA, dépistage, BPCO, PID, stadification, diaphragme, œsophage ×2, sein ×2).

Corrections faites (journal corrections.jsonl, tour t10) :
- Cas 3 (grossesse) : « On préfère la scintigraphie… irradie peu les seins » → « On peut privilégier la scintigraphie… elle irradie moins que l'angio-CT, épargne l'iode et peut être favorisée chez la femme jeune ou enceinte ». La fiche source ne dit pas « on préfère » et ne parle pas des seins.
- Cas 4 (instabilité) : « selon ce qui est disponible le plus vite » → « selon la disponibilité », comme dans la fiche source.
- Cas 5 (dissection) : la phrase « Selon les mêmes auteurs, les D-dimères ne permettent pas… » est retirée. La fiche thorax ne l'attribue pas à Fournier et al.

## Réserves
- clicheBrut, clicheAnnote, lesions et sourceLocaleUniquement restent vides, comme sur main, puisque les images sont interdites. C'est déclaré dans aVerifier.
- Le dossier P23 duplique le thorax : toute correction future doit être faite des deux côtés.
