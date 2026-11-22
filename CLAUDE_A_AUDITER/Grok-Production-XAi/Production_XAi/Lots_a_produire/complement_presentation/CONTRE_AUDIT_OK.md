# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:33 (heure de Zurich).
Lots contrôlés dans ce dossier, dans l'ordre : LOT_COMPLEMENT_7 puis LOT_COMPLEMENT_1. Les autres lots du dossier ne sont pas couverts.

Verdict LOT_COMPLEMENT_7 : conforme, transmis sans correction.

Fichiers couverts :
- LOT_COMPLEMENT_7_membres_et_appareil_locomoteur_production_XAi.json
- LOT_COMPLEMENT_1_tete_et_encephale_production_XAi.json

Contrôles : structure identique à l'original de main (clés, ordre, id, nom, _meta), JSON valide, champs vides, étiquettes ≤ 45 caractères, glossaire des sigles, doses (OFSP 2018 tableaux 13 et 16, directive R-06-06), citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, sondage de sources chiffrées revérifiées en ligne.

Sources revérifiées en ligne :
- Buso et al., Rev Med Suisse 2019 : IPS normal 1,0-1,4, limite 0,90-0,99, pathologique < 0,90 ; index orteil-bras anormal < 0,70 ; baisse > 20 % ou > 30 mmHg après effort ; TcPO2 ≤ 10 et > 40 mmHg ; duplex 85-90 % / > 95 %
- Schwitzguebel et al., Rev Med Suisse 2018 : échographie si douleur ≥ 5 jours, examen de référence, ponction d'hématome des lésions de haut grade
- Rahimi et Barrelet, stratégie HUG TVP 2023 : phlébographie standard de référence

Corrections faites :
- aucune

## LOT_COMPLEMENT_1 (contre-audit terminé le 22.11.2026 23:57, heure de Zurich)

Verdict : conforme après correction ; 80 réserves déclarées dans _lot.aVerifier, chacune avec ce qui a été cherché et le résultat.

Contrôles : structure identique au squelette de main (clés, ordre, id, nom, modalite, _meta), JSON valide, aucun champ vide, aucune mention interdite, étiquettes ≤ 45 caractères. Ce lot n'a pas de clé glossaire ; les sigles restent à relire à la fusion.

Sources relues en ligne (passage réel) :
- Shiboski et al. 2017, critères ACR/EULAR 2016 du Sjögren : focus score ≥ 1 foyer/4 mm² = 3 points, classement à 4 points
- Oleszkiewicz et al. 2019 : normosmie dès un TDI de 30,75 ; anosmie fonctionnelle ≤ 16
- Abdulazim et al. 2023 : vasospasme léger à modéré 120–200 cm/s, sévère > 200 cm/s
- Fleseriu et al. 2016 : cortisol de 8–9 h < 3 µg/dl (83 nmol/l) et > 15 µg/dl (414 nmol/l) ; pic < 500 nmol/l
- Bhasin et al. 2018 : testostérone 264 ng/dl (9,2 nmol/l), dosage répété
- Giustina et al. 2023 (14e conférence) : IGF-1 > 1,3 fois la limite supérieure ; nadir de GH 0,4 µg/l (IMC < 25) et 0,2 µg/l (IMC ≥ 25)
- Petersenn et al. 2023 : prolactine > 200 µg/l
- Winzeler et al. 2019 : copeptine 3,8 pmol/l à 60 min ; Timper et al. 2015 : copeptine de base > 21,4 pmol/l
- AACE 2019 : glycémie < 2,2 mmol/l, pic de GH ≤ 5 µg/l
- Brain Trauma Foundation 2016 : PIC > 22 mmHg
- Kale 2019 : immunodosage présomptif jusqu'à confirmation
- Flitcroft et al. 2019 (IMI) : myopie ≤ −0,50 D, forte myopie ≤ −6,00 D
- Papile 1978 : grade III avec dilatation ventriculaire
- NICE NG98 2018 : asymétrie ≥ 15 dB sur deux fréquences voisines
- Swiss Memory Clinics 2024 : LCR ≤ 4 cellules/µl, protéines ≤ 0,45 g/l, lactate < 2,1 mmol/l
- Strupp et al. 2017 (Bárány Society) : gain du vHIT < 0,6 des deux côtés

Corrections faites :
- vHIT : seuil remplacé par la valeur du passage relu (0,6 des deux côtés, Strupp et al. 2017) au lieu de 0,7
- Copeptine de base > 21,4 pmol/l : source corrigée en Timper et al. (2015)
- Acromégalie : année ajoutée à la 14e conférence de consensus (Giustina et al., 2023)
- Lampe à fente : grade 0 du groupe SUN écrit « moins d'une cellule par champ »
- _lot.aVerifier réécrit : chaque réserve dit ce qui a été cherché et ce qui a été trouvé

Réserves principales pour la relecture :
- Rapport glucose LCR/sang et pression d'ouverture > 25 cmH2O : attribués à Swiss Memory Clinics, absents de cette source ; source à remplacer
- Swiss Stroke Society (Michel et al., 2021), EPOS 2020, ILAE-IFCN 2022, EANM 2022, IFCN 2017 : textes non retrouvés ; contenu gardé et déclaré

Décisions retenues :
- Les sigles ajoutés au glossaire sont gardés ; le rejet « clés ajoutées » du contrôle de forme est un faux positif.
- Les citations Smarter Medicine remplacées mot pour mot sont gardées après vérification (aucune dans ce lot).
- vHIT : la valeur du passage relu est gardée.
