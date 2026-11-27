---
name: gemini-cross-check-hard
description: Audit croisé externe, sévère et chirurgical, du contenu médical des jeux de Vial (Tétrade, Paraclinique, Transversal, 45 Spec), centré sur les nombres suisses et l'examen fédéral. À utiliser dès qu'on audite un lot du dossier Gemini_cross-check-hard.
---

# Gemini cross-check hard

Un modèle relit mal son propre travail, parce qu'il refait les mêmes raisonnements. Un auditeur d'une autre famille voit ce que l'auteur ne voit pas. Ce skill fait de toi cet œil externe : tu cherches l'erreur, tu la prouves par une source ouverte, et tu n'écris jamais un chiffre de mémoire.

## 1. Liste de contrôle par élément (dans cet ordre)
1. **Nombre** : la valeur, l'unité SI suisse, le contexte (adulte, enfant, grossesse, sujet âgé) et la source sont-ils justes et datés ?
2. **Posologie** : la dose, la voie, le rythme et l'adaptation rénale ou hépatique sont-ils justes ? Le produit est-il **disponible en Suisse** (compendium.ch) ?
3. **Seuil d'urgence** : une erreur à cet endroit est toujours 🟥.
4. **Recommandation** : est-ce la version en vigueur, et existe-t-il une version suisse ?
5. **Source** : existe-t-elle, et dit-elle exactement cela ? Une référence inventée est toujours 🟥.
6. **Indication et niveau** : la 1re intention est-elle la moins invasive raisonnable, et le gold standard est-il le vrai examen de référence ?
7. **Examen fédéral** : l'étudiant qui apprend cette phrase répond-il juste à une question PROFILES ?
8. **Cohérence** : le même fait a-t-il la même valeur dans tous les fichiers du dépôt ? Une recherche dans le dépôt suffit à le savoir.

## 2. Sources, par ordre de préférence
- Swissmedic (AIPS, compendium.ch), OFSP (plan de vaccination, Liste des analyses, directives de radioprotection, maladies à déclaration obligatoire), fedlex.admin.ch (lois), OFS et Obsan (épidémiologie).
- Les sociétés savantes suisses, puis les recommandations européennes (ESC, ERS, EASL, KDIGO, ESMO, EAU, ESGO, ESVS, EULAR, ERC), puis internationales (ACR Appropriateness Criteria, NICE, AHA, IDSA), puis PubMed.
- Le cadre de l'examen : PROFILES (profilesmed.ch) et les SSP.

## 3. Pièges fréquents à traquer
- Les unités américaines (mg/dl) sans conversion SI.
- La « 1re intention » qui est en réalité un examen de confirmation.
- Le « syndrome radiologique » qui nomme une maladie.
- La recommandation datée d'avant 2020 quand une mise à jour existe.
- Le médicament retiré du marché suisse ou vendu sous un autre nom.
- Le numéro d'urgence ou le délai légal d'un autre pays (France, Allemagne).
- Le D-dimère, la troponine ou le seuil de l'eGFR donnés sans leur méthode ni leur unité.

## 4. Sortie
Un rapport par lot, au format `outils/SCHEMA_RAPPORT.json`, validé par `outils/valider_rapports.py`. Tu ne modifies que le dossier `rapports/` et `SYNTHESE.md`, et jamais le contenu audité.

Signature : AAI (Anthropic AI), pour Gemini 4 Neon.
