# Registre des skills du dépôt (tenu par perfect-skill-user-organizer-collector)

| Skill | Rôle | Déclencheurs | Relais |
|---|---|---|---|
| perfect-skill-user-organizer-collector | Registre, dotation des agents, anti-doublon | lancement d'agent, création de skill | skill-network-master |
| ultra-competent-fast-doctor | Raisonnement et rédaction médicale experte et rapide | tout contenu médical | medical-accuracy-100 |
| autonomous-skill-creator | Transforme une procédure répétée en skill | procédure vue deux fois | skill-network-master |
| pipeline-autonomous-builder | Pipeline gratuit et relançable de bout en bout | centaines d'éléments | i-med-pipeline-builder |
| i-never-waste-token | Extrait exact avec source, sans bruit | toute lecture ou recherche | harness-for-work |
| text-of-all-kind-contractor-notion-preserved | Contraction de tout texte sans perte de notion (+ scripts/ancres.py) | raccourcir, condenser, trop long, réduire les tokens | med-text-contractor (variante médicale) |
| agent-producteur-45spec | Production 45 Spec sans API au format du script (constructeur + contrôle de couverture dans projets/45spec) | agent qui remplace l'API pour une spécialité | ultra-competent-fast-doctor |
| concept-corelator | Corrélations physiopathologie → thérapeutique | courbes, mécanismes | medical-accuracy-100 |
| 45spec-production-sans-api | Production à la main des notions, questions et corrections 45 Spec au format du script (outil projets/45spec/agent_ecrire.py) | agent qui remplace l'API pour une spécialité 45 Spec | pipeline-autonomous-builder |

Dotation minimale de chaque agent : les cinq premiers skills ci-dessus (décision de Vial, 24.11.2026).
Signature : AAI (Anthropic AI)

| production-45spec-sans-api | Production manuelle (sans API) des notions/questions/corrections 45 Spec via lib.py et contrôles | agent qui remplace l'API pour une spécialité 45 Spec | psych-ultra-ch, medical-accuracy-100 |
