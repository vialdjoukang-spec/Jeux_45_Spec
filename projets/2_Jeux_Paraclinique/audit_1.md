# Audit 1 — fond et fonctionnement — Jeux_Paraclinique — examens complémentaires

| Constat | Correction appliquée |
|---|---|
| Le catalogue listait les examens sans dire ce qu'on y cherche. | Chaque examen porte « signe recherché » et sa visée. |
| La fenêtre de clichés ne montrait pas l'anatomie normale. | La radio-anatomie normale annotée s'affiche à droite. |
| Le JSON d'examen n'avait pas les champs « signe recherché » et « seuil », malgré la règle. | Champs ajoutés aux 616 examens, avec un glossaire par organe. |
| La biologie existait en deux endroits (organe et prélèvement), avec un risque de valeurs divergentes. | Le prélèvement devient la source unique des valeurs ; l'organe y renvoie par « prelevementRef ». |
| Les précautions manquaient : grossesse, enfant, insuffisance rénale, produit de contraste, implant en IRM. | Champs « precautions », « irradiation_mSv » et « delai » ajoutés : ils nourrissent la lentille et le choix économe. |
| Les séquences IRM n'étaient pas discriminées. | 27 techniques décrites : ce qu'elles voient le mieux, quand, plutôt que quoi, limite. |
