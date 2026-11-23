# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 02:36 (heure de Zurich).
Verdict : conforme après correction (transposition faible, voir avertissement)

Fichiers couverts :
- 1_Theorie/PF09-1_Explorations_fonctionnelles_Systemes_transversaux_corps_en_15-fiches_production_XAi.json
- 1_Theorie/PF09-2_Explorations_fonctionnelles_Systemes_transversaux_corps_en_14-fiches_production_XAi.json
- 2_Pratique/PF09-1-PR_Explorations_fonctionnelles_Systemes_transversaux_corps_en_15-fiches_PRATIQUE_production_XAi.json
- 2_Pratique/PF09-2-PR_Explorations_fonctionnelles_Systemes_transversaux_corps_en_14-fiches_PRATIQUE_production_XAi.json

Contrôles : structure identique au squelette de main (clés, ordre, chemins, _meta, nom/id), JSON valide, sens de chaque champ (fonction, traces avec description de ce qu'on voit, seuils, interprétation, diagnostics), défis pratiques (cohérence cas/réponse/justification, réponses courtes ≤ 45 caractères), sigles du glossaire, citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, aucune mention de production ; `controle` : PASS.

Valeurs revérifiées en ligne :
- Candreia et al., pédiatrie suisse, 16.12.2019 (texte relu) : OEA détectables = perte < 30 dB HL, dépistage la première semaine, contrôle avant la fin du premier mois, détection au cours des 3 premiers mois, 1 à 2 ‰ — concordant
- ESC 2023, syndromes coronariens aigus : ECG en moins de 10 minutes, seuils de sus-décalage 2,5/2/1,5/1 mm, ECG répété si doute — concordant
- AASM 2017 (Kapur et al.) : polygraphie chez l'adulte sans comorbidité ; polysomnographie si maladie cardiorespiratoire, neuromusculaire, hypoventilation, opioïdes, AVC, insomnie sévère, ou polygraphie négative/douteuse — concordant
- Recommandation suisse « Aptitude à la conduite en cas de somnolence diurne » 2017 : TME 4 × 40 min, < 20 min / 20–33 min / ≥ 34 min, 34 min pour la conduite professionnelle, Epworth ≥ 15 — concordant
- Barbaud et al., EAACI/ENDA 2024 : test de provocation contre-indiqué après SJS, NET, DRESS, PEAG — concordant
- Cryer et al. 2009 : glycémie < 55 mg/dl (3,0 mmol/l), insuline ≥ 3 µU/ml, peptide C ≥ 0,2 nmol/l, proinsuline ≥ 5 pmol/l, bêta-hydroxybutyrate ≤ 2,7 mmol/l, remontée ≥ 25 mg/dl (1,4 mmol/l) après glucagon — concordant

Cherché, non trouvé (déclaré dans _lot.aVerifier) :
- AASM 2017 : « index rapporté au temps d'enregistrement, qui sous-estime la sévérité » non relu mot pour mot

Corrections faites :
- Doublon polygraphie/polysomnographie (contenu identique) : différenciés d'après Kapur et al. 2017 (domicile sans EEG vs laboratoire avec EEG, indications respectives)
- Doublon ECG en moins de 10 minutes / ECG 12 dérivations (PF04-1) : fiche recentrée sur le tri du syndrome coronarien aigu (ESC 2023)
- Doublon dépistage auditif néonatal / otoémissions (PF01-2) : réécrit comme programme de dépistage suisse en deux temps (Candreia et al. 2019)
- Diagnostics fantômes retirés : choc septique sur qSOFA, Parkinson sur vitesse de marche, warfarine → fibrillation auriculaire, sulfonylurée → diabète, contextes (post-partum, chirurgie cardiaque) donnés comme diagnostics, trouble de la personnalité sur un seul score
- Traces mal placées retirées : « apports > 70 % » (consigne), « moins de 70 % de données » (validité)
- 20 réponses tautologiques de « lire le tracé » réécrites en cas chiffrés (ex. « Glasgow de 8 ou moins → TC sévère » devient Y2 V2 M4 → « Traumatisme crânien sévère (Glasgow 8) »)
- 4 cas d'indication « Non » ajoutés (polygraphie sous opioïdes, HGPO chez une diabétique connue, provocation après nécrolyse épidermique, jeûne de 72 h sous sulfonylurée)
- Citations Smarter Medicine (gériatrie 2017 n° 4, pharmacie 2025 n° 1) remises mot pour mot ; sigles développés ou ajoutés au glossaire
