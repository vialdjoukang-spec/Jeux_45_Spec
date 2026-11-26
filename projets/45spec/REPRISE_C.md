# Point de reprise — producteur groupe C (AAI), 26.11.2026

- Fusionnés sur main, contrôles au vert (menus longs 0, classer_rendement, arène 45, test_arene.py « erreurs: 0 ») :
  - lot 1 : N81.6, N81.8, N92.2 ;
  - lot 2 : N92.4, N93.9_2, N95.2_1 ;
  - lot 3 : N97.1, N97.9_1, O02.1 (audit : couverture de O02.1 complétée, masquage corrigé dans O02.1 et N97.1, sources NICE NG257, NG126, CHUV et Brevier relues) ;
  - lot 4 : O20.0 (saignement du 1er trimestre sur grossesse évolutive), O10.0 (HTA chronique en grossesse), O04.9_1 (interruption médicale après 12 SA).
- Compte du groupe C selon `classer_rendement.py` : 107 / 800.
- Mention harmonisée dans toutes les formes compactes C : « posologies à vérifier dans l'AIPS (Swissmedic) ».
- Points restés « à vérifier » : statut suisse de la nifédipine en grossesse (non trouvée au Compendium) ; misoprostol et mifépristone (MisoOne, Mifegyne) utilisés hors autorisation suisse dans NICE NG126 et NG140 ; aspirine préventive hors indication suisse (Aspirin Cardio contre-indiqué au 3e trimestre) ; anti-D au 1er trimestre (NICE 2026 contre résumé suisse de Rhophylac) ; examen fœtopathologique et conseil génétique après IMG (avis d'expert).
- Pathologie suivante : reprendre l'ordre du rang (`content/pathologies/RANG_RENDEMENT.json`, groupe C), en sautant les pathologies déjà produites et celles qui n'ont que des notions de l'API (V3C_N).
- Formes compactes : `projets/45spec/compact_C/c01…c12`.

Signature : AAI (Anthropic AI)
