# File de travail de Claude (chat) — jeu le moins coûteux à faire progresser : Paraclinique

Source : feuille de route « Feuilles de route des 4 jeux » (23.11.2026). L'agent API suit sa propre file T1 → T7 (projets/ouvrier/MISSION_45SPEC.md).

## Phase 1 — Paraclinique jouable
- **F1** ✅ Réseau complet sur le corps 3D : 9 régions, 82 organes, 820 examens, infobulle signe / seuil / pourquoi lui (`paraclinique_complet.json`).
- **F2** Compléter les 41 examens vides (signe, seuil, indication, discriminant, avantage, limite), sourcés selon medical-accuracy-100.
- **F3** Pipeline de clichés à 0 token (Open-i, Wikimedia) pour les 352 entités sans candidat, dans GitHub Actions.
- **F4** Moteur d'arène commun (vignette, options A/K', chronomètre, correction en 7 marches, répétition espacée), premier client « le bon examen ».
- **F5** 20 cas thoraciques « le bon examen », pénalité Smarter Medicine pour chaque examen inutile.
- **F6** Audit, catalogue, jauge mise à jour.

## Phase 2 — Socle commun aux 4 jeux
- **F7** Référentiel pathologies (clé CIM-10) : Tétrade ↔ 45 Spec, avec la prise en charge holistique commune.
- **F8** Bilans → identifiant d'examen paraclinique ; **F9** traitements → molécule ; **F10** glossaire fusionné.
- **F11** Audit médical du digestif (Tétrade) ; audit horaire continu des fiches et leçons de l'agent.
- **F12** Arène Cardiologie (45 Spec) et puzzles de la Tétrade sur le moteur F4.

Signature : AAI (Anthropic AI)
