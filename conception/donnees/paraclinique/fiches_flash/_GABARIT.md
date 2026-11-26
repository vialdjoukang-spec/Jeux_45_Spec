# Fiches flash de Paraclinique (gabarit de Vial, 26.11.2026)

Un fichier `<organe>.json` par organe, clé = nom exact de la pathologie dans Paraclinique :
```json
{"Pneumonie communautaire": {
  "def": "Définition vraie et concise, en une phrase verbale.",
  "epi": "Épidémiologie en une ligne (fréquence, terrain), chiffrée et sourcée.",
  "meca": "Mécanisme en quelques mots.",
  "syndromesCliniques": [{"nom": "Syndrome de condensation", "composantes": "Matité, augmentation des vibrations vocales, crépitants, souffle tubaire."}],
  "butTraitement": "But du traitement en quelques mots.",
  "moyens": [{"general": "Antibiothérapie", "specifiques": "amoxicilline", "detail": "1 g 3×/j pendant 5 jours ; posologie à vérifier dans l'AIPS."}],
  "source": "Société, année, document ; une source par fait vérifiable."}}
```
Règles : rien de mémoire, tout vient d'une source citée ; sinon « à vérifier ». Les champs absents restent « à produire » dans la page. Signature : AAI (Anthropic AI).
