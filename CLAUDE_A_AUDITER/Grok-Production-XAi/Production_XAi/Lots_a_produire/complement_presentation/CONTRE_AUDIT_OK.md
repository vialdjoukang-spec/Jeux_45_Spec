# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 22.11.2026 23:33 (heure de Zurich).
Lots contrôlés dans ce dossier, dans l'ordre : LOT_COMPLEMENT_7, LOT_COMPLEMENT_1, puis LOT_COMPLEMENT_5. Ce fichier ne couvre pas les autres lots du dossier ; les lots 3, 2, 4 et 6 ont leur propre fichier, CONTRE_AUDIT_OK.lots_3_2_4_6.md.

Verdict LOT_COMPLEMENT_7 : conforme, transmis sans correction.

Fichiers couverts :
- LOT_COMPLEMENT_7_membres_et_appareil_locomoteur_production_XAi.json
- LOT_COMPLEMENT_1_tete_et_encephale_production_XAi.json
- LOT_COMPLEMENT_5_abdomen_production_XAi.json

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

### LOT_COMPLEMENT_1 : réserves reprises le 23.11.2026 (heure de Zurich)

Corrections :
- Ponction lombaire, rapport glucose LCR/sang : l'attribution erronée à Swiss Memory Clinics est remplacée par McGill et al. (2016) : rapport < 0,36, sensibilité et spécificité de 93 %.
- LCR (aspect, pression d'ouverture, cellules) :
  - glucose normal ≈ 2/3 de la glycémie et pression normale 12-20 cmH2O (McGill et al., 2016) ;
  - « Pression d'ouverture > 25 cmH2O » devient « ≥ 25 cmH2O », d'après les critères révisés de Friedman et al. (Neurology 2013) ;
  - le lactate ≥ 2,1 mmol/l, présenté comme un signe de méningite bactérienne et attribué à Swiss Memory Clinics, est en réalité la limite normale. Il est remplacé par le seuil de 35 mg/dl de McGill et al. (2016) : sensibilité 93 %, spécificité 96 %.

Sources relues en ligne :
- McGill et al., recommandation britannique sur la méningite aiguë de l'adulte (J Infect 2016), texte intégral, tableau 4 et paragraphe sur la biochimie du LCR ;
- Friedman, Liu et Digre (Neurology 2013) : ≥ 250 mm de LCR chez l'adulte, ≥ 280 mm chez l'enfant.

Réserves encore ouvertes : Swiss Stroke Society 2021, EPOS 2020, ILAE-IFCN 2022, EANM 2022 et IFCN 2017. Elles sont inchangées et déclarées dans _lot.aVerifier.

## LOT_COMPLEMENT_5 (contre-audit terminé le 23.11.2026, heure de Zurich)

Verdict : conforme après correction. Les 136 examens ont été audités. Il reste des réserves, déclarées dans _lot.aVerifier, qui indiquent pour chacune ce qui a été cherché, où, et le résultat.

Contrôles :
- structure identique au squelette de main (clés, ordre, id, nom, modalite, _meta) ;
- JSON valide, aucun champ vide ;
- étiquettes ≤ 45 caractères ;
- aucune mention de production ni renvoi interne dans le contenu.

Le lot n'a pas de clé glossaire, ni de champ Smarter Medicine ou de dose : ces contrôles sont sans objet.

Corrections principales (journal machine : corrections.jsonl) :
- 82 examens du foie, de la vésicule, du pancréas, de la rate, de l'estomac, du grêle et du côlon. Leurs syndromes et pathologies avaient été rattachés mécaniquement à une anomalie erronée, par exemple « Hépatite C chronique » liée à « AgHBs positif » ou « Hyperplasie nodulaire focale » liée à un hyposignal. La version déjà contre-auditée de ces organes est restaurée : 163 champs.
- Scintigraphies DMSA et MAG3 : le contenu était fait de phrases de travail (« non relu dans cette session ») et citait Taïeb et al. 2019, qui porte sur le phéochromocytome. Il est réécrit sur les recommandations SNMMI/EANM.
- JAK2 V617F et bilan de thrombophilie : les renvois internes sont retirés et le texte est réécrit d'après Baveno VII, recommandations 8.1 à 8.5 et 8.32.
- Laparoscopie et biopsies péritonéales : réécrites d'après Sanai et Bzeizi (2005), sur la péritonite tuberculeuse.
- Calcium, phosphate et PTH : le renvoi interne est retiré et le texte est réécrit d'après KDIGO 2017.
- Coloscopie : l'attribution à l'article 12e de l'OPAS, un texte de remboursement, est remplacée par les indicateurs ESGE 2017 et par ESGE 2019, préparation insuffisante.
- Vidange gastrique : l'attribution à l'EANM est remplacée par le consensus ANMS-SNM (Abell et al., 2008), et « 3 ou 4 h » devient « 4 h ».
- AFP : la « sensibilité d'environ 60 % » ne figure pas dans l'EASL 2018. Elle est remplacée par le passage relu : bonne sensibilité mais faible spécificité à 20 µg/l, et AFP anormale dans 10 à 20 % seulement des CHC précoces.
- INR ≥ 1,5 devient INR > 1,5 (EASL 2017). La fausse attribution au score de Child-Pugh pour la vitamine K est retirée, et la phrase est déclarée.
- Corrections de forme et de cohérence :
  - « consensus consensus de Baveno » corrigé (11 champs) et « Baveno 7 » harmonisé en « Baveno VII » ;
  - 70 phrases reçoivent une majuscule initiale ;
  - 38 listes de synonymes sont nettoyées (doublons du nom, « échographie abdominal », « CT abdominale ») ;
  - la classification de Forrest retrouve ses chiffres romains ;
  - une étiquette > 45 caractères est raccourcie ;
  - la nuance du seuil d'élastase est ajoutée (UEG 2025).

Sources revérifiées en ligne, avec la valeur contrôlée. Pour les sources marquées (T), le texte intégral ou le PDF officiel a été ouvert ; pour les autres, le passage a été lu sur la page officielle ou dans l'extrait rendu par la recherche.
- Baveno VII, J Hepatol 2022 (T, section 8) : JAK2 V617F chez tout adulte ; CALR, exon 12 et NGS si négatif ; biopsie médullaire à discuter ; LSM ≥ 25 kPa ; gradient > 5 et ≥ 10 mmHg
- SNMMI/EANM DMSA de l'enfant, 2022 (T) : fonction différentielle 45-55 % ; cicatrice au moins 6 mois après l'infection
- Taylor et al., SNMMI/EANM scintigraphie diurétique, 2018 (T, PMC6020824) : T1/2 < 10 min exclut l'obstruction ; captation relative 42-58 %
- Sanai et Bzeizi 2005 (résumé), repris par Vaid et Kane 2017 (T) : laparoscopie, sensibilité 93 %, spécificité 98 %
- KDIGO 2017 troubles minéraux et osseux (résumé officiel) : surveillance dès G3a ; tendances ; Ca et P séparés
- ECCO-ESGAR-ESP-IBUS 2025 : calprotectine 50 µg/g, sensibilité 87 %, spécificité 92 %
- EASL-EASD-EASO 2024 : FIB-4 1,3 et 2,67 ; 8 et 12 kPa ; PDFF ≥ 5 %
- EASL 2022 hémochromatose : CST > 45 % + ferritine > 200 (femme) ; > 50 % + > 300 (homme)
- Swiss Cancer Screening, standards nationaux : FIT ≤ 20 µg Hb/g
- mediX 2023 : B12 < 150 ; 150-250 pmol/l ; acide méthylmalonique > 270 nmol/l
- Abell et al. 2008 : 90 % à 1 h, 60 % à 2 h, 10 % à 4 h
- ESMO 2025 rectum et ESGAR IRM rectale : marge ≤ 1 mm ; EMVI ; ganglions latéraux ≥ 7 mm
- ESMO 2020 côlon : ACE postopératoire > 5
- Guide européen 2022 des tests respiratoires : 20 ppm ; 10-12 ppm ; ≥ 10 % de non-producteurs
- EFSUMB 2017 : paroi du grêle < 2 mm ; EFSUMB 2018 : paroi > 3 mm, sensibilité 89 %
- ERS 2017 : < 11 µM
- ESPGHAN 2020 : ≥ 10 × N ; rapport villosités/cryptes < 2 ; Marsh 2-3
- ESGE 2019 lithiase de la VBP : bilirubine > 22 µmol/l, sensibilité 84 % ; PAL > 125 U/l, 91 % ; écho-endoscopie 97 %
- EASL 2022 cholangites sclérosantes : IgG4 > 4 × N, spécificité 100 % ; 25-30 % normales
- ENETS 2023 : gastrine > 10 × N et pH ≤ 2 ; chromogranine A faussée par les IPP
- Endocrine Society 2009 : glycémie < 3,0 mmol/l ; insuline ≥ 18 pmol/l ; peptide C ≥ 0,2 nmol/l
- ACG pancréatite aiguë : triglycérides > 11,3 mmol/l
- UEG 2025 : élastase 200 µg/g, seuil usuel non définitif
- ASGE 2023 : brossage, sensibilité 40 % ; ESGE 2025 sténoses biliaires : CA 19-9 > 37, exactitude 81 %
- Kirkineska et al. 2014 : ≥ 4 % d'hématies piquées ; EFSUMB (rate) : 11-12 cm et 3-4 cm ; aire > 65 cm²
- EASL 2018 CHC (T, PDF easl.eu) : AFP à 20 et à 200 ng/ml (sensibilité 22 %) ; 6 à 8 % de détection ajoutée
- ESGE 2017 indicateurs de qualité : ≥ 90 % ; ESGE 2019 préparation : examen à refaire dans l'année
- ACG 2017 tests hépatiques : R > 5 et < 2 ; ASAT/ALAT ≥ 2
- CFF 2017 : chlorure ≥ 60 mmol/l ; EASL 2017 insuffisance hépatique aiguë : INR > 1,5 + encéphalopathie
- EAU 2025 lithiase : échographie, sensibilité 45 %, spécificité 94 % ; ESVS 2025 : angio-CT ≤ 1 mm quelle que soit la fonction rénale ; lactate ou D-dimères isolés insuffisants

Au total, 36 sources sont revérifiées en ligne pour ce lot, et 2 de plus pour le lot 1.

Réserves principales pour la relecture :
- 187 phrases du bloc des 82 ont reçu de leur rédacteur une source citée ailleurs dans le même examen. Les chiffres en ont été revérifiés, mais pas le rattachement phrase par phrase de chaque phrase descriptive. La liste, par source, figure dans _lot.aVerifier.
- « Rigidité élevée sur hépatite aiguë », attribuée à Baveno VII : le passage n'a pas été trouvé dans le texte de Baveno VII.
- La correction de l'INR par la vitamine K est restée sans source relue.
- Les extraits locaux du rédacteur ne correspondaient pas tous à ce qui était cité (eau_2025.txt porte sur l'incontinence). Les chiffres en cause ont été revérifiés en ligne et confirmés.

Décisions retenues :
- Une étiquette de syndrome peut ne pas figurer dans la liste des anomalies : c'est l'usage déjà admis sur main. Les syndromes contre-audités sont donc gardés.
- Les citations Smarter Medicine sont sans objet : le lot n'a pas ce champ.
- Une source prêtée sans relecture est retirée ou déclarée ; elle n'est jamais gardée telle quelle.
