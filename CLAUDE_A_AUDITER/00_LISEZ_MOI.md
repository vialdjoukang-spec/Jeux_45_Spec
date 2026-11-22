# CLAUDE_A_AUDITER — boîte de dépôt des IA de production

Déposez ici les lots rendus (Grok, Gemini, Claude Cowork…), dans un sous-dossier par IA :
`CLAUDE_A_AUDITER/<ia>/<nom_du_lot>.json` (ex. `CLAUDE_A_AUDITER/Grok-Production-XAi/P04-01_poumons.json`). L'ancien dossier `grok/` reste lu.

À chaque dépôt, GitHub lance gratuitement `projets/outils/audit_auto.py` (0 token) et écrit
`CLAUDE_A_AUDITER/RAPPORT_AUTO.md` : JSON lisible, chemins exacts, éléments, schéma, remplissage.
- 🟩 intégrable · 🟧 à compléter · 🟥 refusé (illisible, chemin ou élément inventé).
Claude audite ensuite le fond médical, puis fusionne par champ (`fusionner_retours.py`).

Ne renommez ni les chemins ni les clés ; un lot produit sur un ancien schéma reste accepté (fusion par champ).

## Veille automatique (gratuite, 0 token)
`.github/workflows/veille.yml` se réveille toutes les 5 minutes ; un curseur (`projets/outils/cadence.py`) espace les passages de 5 à 60 minutes selon le nombre de lots reçus récemment, et tout dépôt sur main la déclenche aussitôt. Elle lit les lots de main et de toutes les branches `production-xai-*` ; sur une branche, un lot n'est pris qu'après le contre-audit de l'orchestrateur XAi, déclaré par un fichier `CONTRE_AUDIT_OK` dans son dossier (ou un dossier parent). Elle répare la forme (balises markdown, BOM, virgules finales, chemins Windows), fusionne par champ et relance les contrôles, mais seulement sur la branche `veille/audit-medical`. Claude audite ensuite médicalement chaque valeur (`projets/outils/AUDIT_MEDICAL_CLAUDE.md`), corrige, puis ouvre et fusionne la PR vers main. Rien n'arrive sur main sans cet audit. Un lot déjà traité n'est jamais refusionné (`projets/retours/veille_traites.json`).

Signature : AAI (Anthropic AI)
