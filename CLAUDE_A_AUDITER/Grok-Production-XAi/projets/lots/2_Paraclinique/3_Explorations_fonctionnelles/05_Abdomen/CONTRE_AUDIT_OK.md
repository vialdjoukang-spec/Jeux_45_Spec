# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 02:30 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/PF05_Explorations_fonctionnelles_Abdomen_10-fiches_production_XAi.json
- 2_Pratique/PF05-PR_Explorations_fonctionnelles_Abdomen_10-fiches_PRATIQUE_production_XAi.json

Contrôles : structure identique au squelette de main (clés, ordre, chemins, _meta, nom/id), JSON valide, sens de chaque champ (fonction, traces avec description de ce qu'on voit, seuils, interprétation, diagnostics), défis pratiques (cohérence cas/réponse/justification, réponses courtes ≤ 45 caractères), sigles du glossaire, citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, aucune mention de production ; `controle` : PASS.

Valeurs revérifiées en ligne :
- Endocrine Society 2025 (hyperaldostéronisme) : charge sodée < 217 pmol/l (immunodosage) / < 162 pmol/l (LC-MS/MS) ; indice de latéralisation ≥ 4 — concordant (sources secondaires pour l'indice)
- ESE/ENSAT 2023 : cortisol ≤ 50 nmol/l après 1 mg de dexaméthasone exclut une sécrétion autonome ; au-delà sans Cushing = MACS — concordant
- Endocrine Society 2016 : pic de cortisol < 500 nmol/l à 30 ou 60 min après 250 µg = insuffisance surrénale — concordant (seuil dépendant de la méthode)

Cherché, non trouvé (déclaré dans _lot.aVerifier) :
- Endocrine Society 2025 : texte de l'indice de latéralisation (< 3 bilatéral) non relu en source primaire
- Baveno VII (5 et 10 mmHg) et UEG 2025 (sécrétine) : non relus dans ce tour
- Lien RAIR absent → maladie de Hirschsprung : non relu dans l'IAPWG 2019

Corrections faites :
- Renvoi interne retiré (cortisol : « valeurs … dans les fiches d'analyse »)
- « Selon la même source » remplacé par la source nommée (cathétérisme surrénalien, charge sodée)
- 5 réponses tautologiques remplacées par un diagnostic avec description chiffrée (cathétérisme surrénalien, Synacthène, charge sodée, freinage à la dexaméthasone ; ex. « Cortisol de plus de 50 nmol/l » → « Sécrétion autonome légère de cortisol »)
- Aspects mal placés retirés (« aldostérone freinée », « réponse normale » à la sécrétine) ; traces de manométrie anorectale réécrites (ce qu'on voit)
- Indication : cas « Non » ajouté (Synacthène pendant une crise surrénalienne) ; avant : 9 Oui sur 10
