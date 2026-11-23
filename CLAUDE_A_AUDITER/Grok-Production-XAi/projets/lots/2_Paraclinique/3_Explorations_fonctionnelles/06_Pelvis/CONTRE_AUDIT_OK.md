# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 02:30 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/PF06_Explorations_fonctionnelles_Pelvis_9-fiches_production_XAi.json
- 2_Pratique/PF06-PR_Explorations_fonctionnelles_Pelvis_9-fiches_PRATIQUE_production_XAi.json

Contrôles : structure identique au squelette de main (clés, ordre, chemins, _meta, nom/id), JSON valide, sens de chaque champ (fonction, traces avec description de ce qu'on voit, seuils, interprétation, diagnostics), défis pratiques (cohérence cas/réponse/justification, réponses courtes ≤ 45 caractères), sigles du glossaire, citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, aucune mention de production ; `controle` : PASS.

Valeurs revérifiées en ligne :
- FIGO 2015 (CTG) : ligne de base 110–160, variabilité 5–25 ; pathologique < 100, variabilité réduite > 50 min, décélération > 5 min — concordant
- EAU (femme) : pad-test ≥ 1,4 g en 1 h, ≥ 4,4 g en 24 h — concordant
- EAU (homme) : Qmax < 10 ml/s spécificité 70 %, sensibilité 47 % ; volume uriné > 150 ml — concordant

Cherché, non trouvé (déclaré dans _lot.aVerifier) :
- EAU 2026 : « pas de bilan urodynamique de routine avant traitement conservateur » non relu mot pour mot
- EPDS : seuils 10/11 du programme des HUG non relus ; item 10 et NICE CG192 non relus

Corrections faites :
- Doublons vérifiés : les deux bilans urodynamiques (femme/incontinence SSGO vs homme/obstruction EAU) et les deux calendriers mictionnels (nocturie vs pad-test) sont déjà différenciés
- CTG : diagnostic fantôme « Diabète gestationnel | Surveillance par enregistrements » retiré
- EPDS : aspect qui répétait le normal et diagnostic « anxiété » retirés ; item 10 ajouté
- 3 réponses tautologiques remplacées (CTG, pad-test, érection pharmaco-induite)
- Indication : cas « Non » ajouté (urodynamique avant traitement conservateur) ; avant : 9 Oui sur 9
