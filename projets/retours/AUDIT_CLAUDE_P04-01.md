# Contre-audit Claude — pilote P04-01 Poumons et voies aériennes (Athéna / XAi)

**Verdict : validé, modèle à reproduire pour les autres organes du thorax.** Fusionné dans `conception/donnees` (théorie 32 examens, pratique 105 défis) ; audit de conception 34/34.

## Contrôle automatique
- 10/10 fichiers lisibles, chemins exacts, aucun élément ni champ inventé ; théorie remplie à 84–90 % (les vides restants sont les champs autorisés à `null`), pratique 100 %.
- 105 défis : 32 bon_examen, 32 piege, 23 lecture, 18 seuil_decision ; tous portent une source.

## Points à corriger ou vérifier avant la suite
1. **Attribution de source** : « selon la SSI, une PaO2 < 8 kPa traduit une hypoxémie » ; ce seuil vient des définitions BTS/ERS, pas de la Société suisse d'infectiologie. Corriger l'attribution.
2. **Smarter Medicine** : vérifier que la recommandation SSMI 2017 (gazométrie) et la recommandation SSOM 2024 (PET) figurent mot pour mot dans les listes Top 5 publiées ; sinon, mettre le champ à `null`.
3. **Doses de radiographie (décision)** : la valeur OFSP 2018 (tableau 13, 0,045 mSv pour le thorax) devient la référence du projet ; toutes les radiographies s'alignent sur ce tableau.
4. **Noms de plus de 45 caractères** : le défaut vient de l'ossature de Claude (238 noms). Ne modifiez jamais `nom` ; Claude ajoutera un libellé court pour les cases du réseau.
5. **Images** : les défis « lecture » décrivent l'image attendue (`imageOuTraceAttendu`), comme le demandent les instructions. Les vrais clichés seront ajoutés plus tard par un circuit séparé (images réelles sous licence libre) ; vous ne devez pas en chercher.
6. **Vitesse** : le contre-audit a porté sur un échantillon ; les sources des défis de pratique restent à vérifier par sondage à chaque livraison.

## Pour la suite
Déposez chaque organe dans `CLAUDE_A_AUDITER/grok/` (ou `POUR CLAUDE A AUDITER/`) : l'audit automatique gratuit se lance à chaque dépôt.

Signature : AAI (Anthropic AI)
