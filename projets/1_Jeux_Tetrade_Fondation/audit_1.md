# Audit 1 — fond et fonctionnement — Jeux_Tetrade_Fondation — anatomie, physiologie, sémiologie, physiopathologie

| Constat | Correction appliquée |
|---|---|
| Les termes techniques n'étaient pas définis (« atypique »). | Glossaire obligatoire ; l'audit bloque tout sigle non défini (45 termes au pilote). |
| Le bilan surchargeait l'infobulle de détails. | Le bilan n'affiche que des noms groupés par visée ; chaque nom est un support d'infobulle (signe recherché, seuil). |
| Les présentations atypiques manquaient. | Catégorie atypique en rouge à chaque temps et à l'anamnèse ; 4 cases atypiques au pilote. |
| Le système cardiovasculaire se réduisait au cœur. | Source unique systemes.py : 14 systèmes, 124 organes ; l'audit bloque tout système incomplet. |
| Les cases pouvaient porter de longs textes. | Audit de concision (≤ 45 caractères) ; détail en infobulle, courbe en fenêtre. |
| Des sigles de physiologie n'étaient pas définis (VEMS, DLCO, PaCO₂…). | 21 termes ajoutés au glossaire ; l'audit les exige. |
| La pharmacologie n'avait plus de projet propre dans la liste des 4. | Elle est rattachée à la Tétrade comme cinquième pilier (à valider). |
