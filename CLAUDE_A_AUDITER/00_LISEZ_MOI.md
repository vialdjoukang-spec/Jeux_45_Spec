# CLAUDE_A_AUDITER — boîte de dépôt des IA de production

Déposez ici les lots rendus (Grok, Gemini, Claude Cowork…), dans un sous-dossier par IA :
`CLAUDE_A_AUDITER/<ia>/<nom_du_lot>.json` (ex. `CLAUDE_A_AUDITER/grok/P04-01_poumons.json`).

À chaque dépôt, GitHub lance gratuitement `projets/outils/audit_auto.py` (0 token) et écrit
`CLAUDE_A_AUDITER/RAPPORT_AUTO.md` : JSON lisible, chemins exacts, éléments, schéma, remplissage.
- 🟩 intégrable · 🟧 à compléter · 🟥 refusé (illisible, chemin ou élément inventé).
Claude audite ensuite le fond médical, puis fusionne par champ (`fusionner_retours.py`).

Ne renommez ni les chemins ni les clés ; un lot produit sur un ancien schéma reste accepté (fusion par champ).

Signature : AAI (Anthropic AI)
