ID = "G80.9__O2_11-E05"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[avis d'expert]|La paralysie cérébrale regroupe des troubles permanents du mouvement et de la posture dus à une lésion non progressive du cerveau fœtal ou du nourrisson.",  # N01
"epi|chiffre|2||[Novak, JAMA Pediatr 2017]|Elle touche environ 1 naissance vivante sur 500 et constitue le handicap physique le plus fréquent de l'enfance.",  # N02
"epi|terrain particulier|2||[avis d'expert]|La prématurité, l'encéphalopathie hypoxique-ischémique, l'AVC néonatal et les infections congénitales en sont les principaux terrains.",  # N03
"bas|mécanisme|1||[avis d'expert]|Chez le prématuré, la leucomalacie périventriculaire lèse les fibres corticospinales des membres inférieurs, ce qui explique la diplégie spastique.",  # N04
"ana|symptôme|2||[avis d'expert]|Une hypotonie axiale et un retard des acquisitions motrices précèdent souvent l'apparition d'une spasticité ou d'une dyskinésie vers 6 à 12 mois.",  # N05
"exa|signe|2||[Novak, JAMA Pediatr 2017]|L'examen neurologique standardisé de Hammersmith (HINE) détecte le risque avec une sensibilité de 90 %.",  # N06
"red|piège|2||[avis d'expert]|Une régression des acquisitions ou une aggravation progressive écarte la paralysie cérébrale et fait chercher une maladie neurodégénérative ou métabolique.",  # N07
"gold|examen|3||[Novak, JAMA Pediatr 2017]|Avant 5 mois d'âge corrigé, l'IRM à terme (sensibilité 86 à 89 %), l'évaluation des mouvements généraux de Prechtl (98 %) et le HINE (90 %) prédisent le mieux le risque.",  # N08
"gold|résultat|2||[Novak, JAMA Pediatr 2017 ; avis d'expert]|L'absence des mouvements « fidgety » vers 3 mois d'âge corrigé à l'évaluation de Prechtl signale un risque élevé de paralysie cérébrale.",  # N09
"alt|examen|1||[Novak, JAMA Pediatr 2017]|Après 5 mois d'âge corrigé, l'IRM, le HINE et une échelle de développement standardisée prennent le relais.",  # N10
"pos|diagnostic différentiel|2||[avis d'expert]|Devant un nourrisson hypotone, une aréflexie, des fasciculations de la langue et un éveil préservé orientent vers une cause périphérique, comme l'amyotrophie spinale.",  # N11
"pos|critère|1||[Novak, JAMA Pediatr 2017]|L'association d'une anamnèse à risque, d'une IRM et d'examens standardisés concordants permet de poser le diagnostic ou un « haut risque » avant 6 mois d'âge corrigé.",  # N12
"acu|décision|3||[Novak, JAMA Pediatr 2017]|Dès la suspicion, l'enfant s'oriente vers une intervention précoce spécifique, sans attendre la certitude, pour profiter de la plasticité cérébrale.",  # N13
"chr|décision|1||[avis d'expert]|La prise en charge est interdisciplinaire : physiothérapie, ergothérapie, logopédie, orthopédie et neuropédiatrie.",  # N14
"chr|molécule|1||[avis d'expert]|La toxine botulique traite une spasticité focale ; le baclofène, oral ou intrathécal, une spasticité étendue (posologies à vérifier dans l'AIPS).",  # N15
"hos|complication|2||[avis d'expert]|Épilepsie, déficience intellectuelle, troubles visuels ou auditifs, troubles de la déglutition, douleur et luxation de hanche accompagnent souvent la maladie.",  # N16
"hos|complication|1||[avis d'expert]|La hanche se surveille par radiographie régulière, car le risque de luxation augmente avec la sévérité motrice.",  # N17
"pro|pronostic|2||[Novak, JAMA Pediatr 2017]|Dans les pays à revenu élevé, 2 enfants sur 3 marcheront, 3 sur 4 parleront et 1 sur 2 aura une intelligence normale.",  # N18
"pro|critère|1||[avis d'expert]|La classification GMFCS décrit la motricité globale en 5 niveaux et aide au pronostic de marche.",  # N19
"sur|examen|1||[avis d'expert]|Les nourrissons à risque (grands prématurés, encéphalopathie néonatale) suivent un dépistage structuré du développement.",  # N20
"fol|contexte suisse|1|S|[avis d'expert]|En Suisse, l'assurance-invalidité prend en charge les mesures médicales des paralysies cérébrales congénitales au titre des infirmités congénitales.",  # N21
"fol|décision|1||[Novak, JAMA Pediatr 2017]|Le soutien aux parents et à leur bien-être fait partie de l'intervention précoce.",  # N22
"red|prévention|1||[Shepherd, Cochrane 2024]|Le sulfate de magnésium donné à la mère avant 34 semaines réduit la paralysie cérébrale à 2 ans (RR 0,71 ; 60 femmes à traiter pour un bénéfice).",  # N23
"acu|molécule|1||[avis d'expert]|L'hypothermie thérapeutique débutée dans les 6 heures chez le nouveau-né d'au moins 36 semaines avec encéphalopathie hypoxique-ischémique modérée ou sévère réduit décès et handicap.",  # N24
"def|piège|1||[avis d'expert]|La lésion ne progresse pas, mais les manifestations cliniques changent avec la croissance.",  # N25
"exa|signe|1||[avis d'expert]|Une préférence manuelle avant 12 mois fait suspecter une atteinte unilatérale.",  # N26
]
ANGLES = [
"Hypotonie axiale du prématuré : Prechtl, HINE, IRM.",
"Absence de fidgety à 3 mois.",
"Intervention précoce sans attendre 2 ans.",
"Régression = pas une paralysie cérébrale.",
"Aréflexie + fasciculations linguales = périphérique.",
"Sulfate de magnésium avant 34 semaines.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un garçon né à 29 semaines a 3 mois d'âge corrigé. Ses parents, à Lucerne, le trouvent « mou » ; il tient mal sa tête et bouge peu. Le reste de l'examen est sans particularité.", prompt="Quel outil standardisé est le plus sensible à cet âge pour détecter un risque de trouble moteur permanent ?",
 items=["*L'évaluation des mouvements généraux de Prechtl || Sa sensibilité atteint 98 % avant 5 mois.", "Un EEG de sommeil || Il ne prédit pas ce trouble moteur.", "Un dosage des CK || Il cherche une myopathie, rarement en cause ici.", "Une échographie des hanches || Elle ne prédit pas ce trouble.", "Le score d'Apgar de naissance seul || Il est peu prédictif."],
 notions="N05 N03 N08", angle="application", diff=2, ladder=L("Nourrisson mou.", "Lésion cérébrale précoce.", "Grand prématuré.", "Outil sensible.", "Prechtl.", "EEG.", "Prématuré mou = Prechtl, HINE, IRM."), sources="[Novak, JAMA Pediatr 2017]"),
dict(format="A", serie=("S1", 2, 4), stem="La vidéo montre l'absence des mouvements « fidgety » attendus à cet âge.", prompt="Comment interprétez-vous ce résultat ?",
 items=["*Un risque élevé de paralysie cérébrale || L'absence de fidgety à 3 mois est très prédictive.", "Un résultat normal pour un prématuré || Les fidgety sont attendus à cet âge corrigé.", "Une épilepsie || Ce n'est pas un signe épileptique.", "Une amyotrophie spinale certaine || Le test ne la diagnostique pas.", "Un résultat sans valeur avant 2 ans || Il est très prédictif tôt."],
 notions="N09 N08 N12", angle="direct", diff=2, ladder=L("Fidgety absents.", "Réseaux moteurs lésés.", "3 mois corrigés.", "Prédictif.", "Haut risque.", "Normal chez le prématuré.", "Pas de fidgety = risque élevé."), sources="[Novak, JAMA Pediatr 2017]"),
dict(format="A", serie=("S1", 3, 4), stem="L'IRM montre une leucomalacie périventriculaire bilatérale.", prompt="Quelle décision prenez-vous ?",
 items=["*Annoncer un haut risque et orienter sans attendre vers une intervention précoce spécifique || La plasticité cérébrale est maximale tôt.", "Attendre 2 ans avant toute prise en charge || Le retard perd la fenêtre de plasticité.", "Refaire une IRM dans un an avant de décider || Le diagnostic peut se poser maintenant.", "Prescrire du baclofène d'emblée || Il n'y a pas de spasticité gênante.", "Rassurer, car l'IRM du prématuré n'a pas de valeur || L'IRM est très prédictive."],
 notions="N13 N04 N12 N09", angle="application", diff=2, ladder=L("Leucomalacie.", "Fibres corticospinales.", "Bilatérale.", "Concordance des examens.", "Intervention précoce.", "Attendre 2 ans.", "Risque élevé = agir tout de suite."), sources="[Novak, JAMA Pediatr 2017]"),
dict(format="A", serie=("S1", 4, 4), stem="À 2 ans, l'enfant a une diplégie spastique et marche avec un déambulateur.", prompt="Quelle complication orthopédique devez-vous surveiller systématiquement ?",
 items=["*La luxation de hanche, par radiographie régulière || Son risque augmente avec la sévérité motrice.", "La scoliose idiopathique de l'adolescente || Elle n'est pas liée à la spasticité.", "L'arthrite juvénile || Elle n'est pas une complication.", "La fracture du scaphoïde || Elle n'est pas une complication attendue.", "Aucune surveillance n'est utile || La hanche est à risque."],
 notions="N17 N16 N19", angle="application", diff=2, ladder=L("Diplégie spastique.", "Déséquilibre musculaire.", "Marche aidée.", "Hanche à risque.", "Radiographie des hanches.", "Aucune surveillance.", "Spasticité = hanche à surveiller."), sources="[avis d'expert]"),
dict(format="A", stem="Un nourrisson de 4 mois, né à terme sans incident, est hypotone. Il est aréflexique, sa langue présente des fasciculations, mais son regard est vif et il suit des yeux.", prompt="Quel diagnostic évoquez-vous en premier ?",
 items=["*Une amyotrophie spinale || Aréflexie, fasciculations et éveil préservé orientent vers une cause périphérique.", "Une paralysie cérébrale hypotonique || Elle ne donne ni aréflexie ni fasciculations.", "Une hypothyroïdie congénitale || Elle ne donne pas de fasciculations.", "Une encéphalopathie hypoxique-ischémique || La naissance était sans incident.", "Un retard simple de maturation || L'aréflexie est pathologique."],
 notions="N11 N05", angle="piège", diff=2, ladder=L("Nourrisson hypotone.", "Motoneurone.", "Fasciculations linguales.", "Aréflexie, éveil vif.", "Cause périphérique.", "Paralysie cérébrale.", "Aréflexique et éveillé = périphérique."), sources="[avis d'expert]"),
dict(format="A", stem="Un garçon de 18 mois, dont le développement était normal, cesse de marcher et perd les mots qu'il disait.", prompt="Quelle conclusion est la plus juste ?",
 items=["*La régression écarte une lésion non progressive et fait chercher une maladie neurodégénérative ou métabolique || Le tableau progresse.", "Il s'agit d'une paralysie cérébrale tardive || La lésion n'est pas progressive.", "Il s'agit d'un retard simple || Une perte d'acquis est pathologique.", "Il faut attendre 6 mois avant tout bilan || La régression impose un bilan rapide.", "Il s'agit d'une dyspraxie isolée || Elle ne fait pas perdre la marche."],
 notions="N07 N25 N01", angle="piège", diff=2, ladder=L("Perte d'acquis.", "Processus évolutif.", "Marche et langage perdus.", "Régression.", "Bilan neurométabolique.", "Paralysie cérébrale.", "Régression ≠ paralysie cérébrale."), sources="[avis d'expert]"),
dict(format="A", stem="Une fillette de 8 mois utilise exclusivement sa main droite depuis 4 mois ; sa main gauche reste fermée.", prompt="Quelle hypothèse et quelle démarche retenez-vous ?",
 items=["*Une atteinte unilatérale, par exemple un AVC néonatal, à explorer par IRM || Une préférence manuelle avant 12 mois est anormale.", "Une latéralité droite normale || Elle ne s'établit pas si tôt.", "Une paralysie du plexus brachial certaine || Le tableau oriente vers une cause centrale.", "Une simple paresse de la main gauche || Elle n'existe pas à cet âge.", "Une observation sans examen jusqu'à 3 ans || L'IRM s'impose."],
 notions="N26 N03 N05", angle="application", diff=2, ladder=L("Préférence manuelle précoce.", "Lésion unilatérale.", "Main gauche fermée.", "Avant 12 mois.", "IRM.", "Latéralité normale.", "Main préférée avant 1 an = suspect."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Des parents apprennent que leur fils de 10 mois a une atteinte motrice cérébrale permanente. Ils demandent ce qu'il pourra faire plus tard.", prompt="Quelle information est la plus juste ?",
 items=["*Dans les pays à revenu élevé, 2 enfants sur 3 marchent, 3 sur 4 parlent et 1 sur 2 a une intelligence normale || Le pronostic est souvent meilleur que redouté.", "Aucun enfant ne marche || La majorité marche.", "Tous ont une déficience intellectuelle || La moitié a une intelligence normale.", "Le pronostic est impossible à préciser avant 10 ans || La GMFCS aide dès l'enfance.", "Tous marcheront normalement || Le pronostic varie selon la sévérité."],
 notions="N18 N19", angle="direct", diff=1, ladder=L("Annonce.", "Lésion fixée.", "Avenir.", "Chiffres.", "Informer avec nuance.", "Aucun ne marche.", "2 sur 3 marchent."), sources="[Novak, JAMA Pediatr 2017]"),
dict(format="A", stem="Un pédiatre dit aux parents d'un ancien prématuré de 4 mois, au HINE et à l'IRM anormaux, qu'il faut attendre 2 ans avant de parler de diagnostic et de débuter une thérapie.", prompt="Que corrigez-vous ?",
 items=["*Le diagnostic ou un haut risque peut se poser avant 6 mois d'âge corrigé et l'intervention précoce ne doit pas attendre || Ce trouble est fréquent et la plasticité est maximale tôt.", "Rien, il faut attendre 2 ans || Cette pratique est dépassée.", "Il faut attendre 5 ans || Rien ne le justifie.", "Seule une biopsie confirmerait le diagnostic || Elle n'a pas de place.", "L'IRM n'a aucune valeur à cet âge || Elle est très prédictive."],
 notions="N13 N12 N06 N02", angle="piège", diff=2, ladder=L("Attente de 2 ans.", "Plasticité.", "HINE et IRM anormaux.", "Diagnostic précoce.", "Agir maintenant.", "Attendre.", "Haut risque = intervention."), sources="[Novak, JAMA Pediatr 2017]"),
dict(format="A", stem="Une femme enceinte de 28 semaines est admise en travail prématuré imminent.", prompt="Quelle mesure réduit le risque de trouble moteur cérébral permanent chez l'enfant ?",
 items=["*Le sulfate de magnésium intraveineux à la mère || Il réduit ce risque à 2 ans.", "Une césarienne systématique || Elle n'est pas une neuroprotection.", "Le paracétamol || Il n'est pas neuroprotecteur.", "Une hypothermie maternelle || Elle n'est pas indiquée.", "Aucune mesure n'existe || Le sulfate de magnésium est efficace."],
 notions="N23 N03", angle="application", diff=2, ladder=L("Travail prématuré.", "Neuroprotection fœtale.", "28 semaines.", "Avant 34 semaines.", "Sulfate de magnésium.", "Césarienne.", "Prématurité imminente = magnésium."), sources="[Shepherd, Cochrane 2024]"),
dict(format="A", stem="Un nouveau-né de 39 semaines a une encéphalopathie hypoxique-ischémique modérée après une asphyxie à la naissance ; il a 2 heures de vie.", prompt="Quelle mesure réduit décès et handicap ?",
 items=["*Une hypothermie thérapeutique débutée dans les 6 heures || Elle protège le cerveau dans cette indication.", "Un réchauffement actif à 38 °C || L'hyperthermie aggrave la lésion.", "Des corticoïdes à forte dose || Ils ne sont pas indiqués.", "Une attente de 24 heures avant toute mesure || La fenêtre est de 6 heures.", "Du sulfate de magnésium au nouveau-né en routine || Il n'est pas la mesure de référence."],
 notions="N24 N03", angle="application", diff=2, ladder=L("Encéphalopathie néonatale.", "Lésion secondaire.", "Terme, 2 heures.", "Fenêtre de 6 heures.", "Hypothermie.", "Réchauffer.", "Asphyxie à terme = refroidir."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un enfant de 6 ans avec une atteinte motrice cérébrale congénitale marche sur la pointe du pied droit à cause d'une spasticité du triceps sural.", prompt="Quel traitement proposez-vous en premier ?",
 items=["*Une injection de toxine botulique avec physiothérapie || Elle traite une spasticité focale.", "Du baclofène intrathécal d'emblée || Il se réserve aux spasticités étendues et sévères.", "Une ténotomie d'Achille immédiate sans essai conservateur || Le traitement conservateur se tente d'abord.", "Un plâtre définitif || Il n'est pas un traitement de fond.", "Aucun traitement || La spasticité gêne la marche."],
 notions="N15 N14", angle="application", diff=2, ladder=L("Marche sur la pointe.", "Spasticité focale.", "Triceps sural.", "Focale ou étendue.", "Toxine et physiothérapie.", "Baclofène intrathécal.", "Focal = toxine."), sources="[avis d'expert]"),
dict(format="A", stem="Un enfant de 5 ans avec une diplégie spastique présente depuis 2 semaines des épisodes brefs de fixité du regard avec des secousses du bras.", prompt="Quelle conduite proposez-vous ?",
 items=["*Chercher une épilepsie associée par EEG et avis neuropédiatrique || L'épilepsie est une comorbidité fréquente.", "Attribuer les épisodes à la spasticité || Les secousses et la fixité évoquent des crises.", "Augmenter la physiothérapie || Elle ne traite pas des crises.", "Considérer une aggravation de la lésion cérébrale || Elle ne progresse pas.", "Ignorer les épisodes || Les crises se traitent."],
 notions="N16 N07", angle="application", diff=2, ladder=L("Épisodes paroxystiques.", "Cortex lésé.", "Fixité, secousses.", "Comorbidité.", "EEG.", "Spasticité.", "Paroxysme = penser épilepsie."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Les parents d'un enfant suisse avec une paralysie cérébrale congénitale demandent qui finance les thérapies.", prompt="Quelle réponse est la plus juste ?",
 items=["*L'assurance-invalidité prend en charge les mesures médicales au titre des infirmités congénitales || C'est une particularité suisse.", "Les parents paient tout || L'AI intervient.", "Seule l'assurance-accidents paie || Il ne s'agit pas d'un accident.", "Aucune assurance ne couvre la physiothérapie || L'AI la prend en charge.", "La commune paie tout || Ce n'est pas le système."],
 notions="N21 N22", angle="direct", diff=1, ladder=L("Financement.", "Infirmité congénitale.", "Suisse.", "Assureur.", "AI.", "Assurance-accidents.", "Congénital = AI."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez la définition et le diagnostic de la paralysie cérébrale.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La lésion cérébrale ne progresse pas. || C'est un critère.", "V: Les manifestations changent avec la croissance. || La spasticité apparaît souvent après l'hypotonie.", "F: Le diagnostic est impossible avant 2 ans. || Il peut se poser avant 6 mois d'âge corrigé.", "F: Une IRM est le seul outil utile avant 5 mois. || Prechtl et HINE sont aussi très sensibles."],
 notions="N01 N25 N12 N08", angle="direct", diff=2, ladder=L("Définition.", "Lésion fixée.", "Évolution clinique.", "Diagnostic précoce.", "Combiner les outils.", "Attendre 2 ans.", "Fixée mais changeante."), sources="[Novak, JAMA Pediatr 2017]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Une équipe de néonatologie organise le dépistage précoce de la paralysie cérébrale.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'évaluation de Prechtl a une sensibilité de 98 % avant 5 mois. || C'est l'outil le plus sensible.", "V: Le HINE a une sensibilité de 90 %. || Il sert avant et après 5 mois.", "F: L'EEG est l'outil le plus prédictif. || Il ne prédit pas le trouble moteur.", "F: Une échelle de développement standardisée n'a aucune utilité après 5 mois. || Elle prend le relais."],
 notions="N08 N06 N10 N20", angle="direct", diff=2, ladder=L("Dépistage.", "Prédiction.", "Prechtl, HINE.", "Pièges.", "Organiser.", "EEG.", "Prechtl, HINE, IRM."), sources="[Novak, JAMA Pediatr 2017]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Les parents d'un enfant de 3 ans avec une atteinte motrice cérébrale congénitale posent des questions sur les problèmes associés.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une épilepsie peut s'associer. || C'est une comorbidité fréquente.", "V: La hanche peut se luxer. || La surveillance radiologique le dépiste.", "F: Une déficience intellectuelle est constante. || La moitié a une intelligence normale.", "F: La douleur est exceptionnelle. || Elle est fréquente."],
 notions="N16 N18 N17", angle="piège", diff=2, ladder=L("Comorbidités.", "Lésion étendue.", "Épilepsie, hanche.", "Pièges.", "Dépister.", "Déficience constante.", "Chercher, ne pas présumer."), sources="[Novak, JAMA Pediatr 2017]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez la prévention de la paralysie cérébrale.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le sulfate de magnésium maternel avant 34 semaines réduit la paralysie cérébrale à 2 ans. || RR 0,71.", "V: L'hypothermie thérapeutique protège le nouveau-né à terme avec encéphalopathie modérée ou sévère. || Elle réduit décès et handicap.", "F: Le bénéfice du sulfate de magnésium sur la paralysie cérébrale est démontré à l'âge scolaire. || Les données y sont incertaines.", "F: La paralysie cérébrale est rare, moins de 1 naissance sur 10 000. || Elle touche environ 1 naissance sur 500."],
 notions="N23 N24 N03 N02", angle="direct", diff=2, ladder=L("Prévention.", "Neuroprotection.", "Magnésium, hypothermie.", "Limites.", "Appliquer.", "Maladie rare.", "Magnésium et froid."), sources="[Shepherd, Cochrane 2024]"),
dict(format="MenuLong", stem="Un ancien prématuré de 3 mois d'âge corrigé est hypotone.", prompt="Choisissez les TROIS outils les plus prédictifs du risque de trouble moteur permanent à cet âge.",
 items=["*IRM cérébrale à terme || Sensibilité 86 à 89 %.", "*Évaluation des mouvements généraux de Prechtl || Sensibilité 98 %.", "*Examen neurologique de Hammersmith (HINE) || Sensibilité 90 %.", "EEG || Il ne prédit pas le trouble moteur.", "Potentiels évoqués visuels || Ils ne prédisent pas le trouble moteur.", "Dosage des CK || Il cherche une myopathie.", "Échographie des hanches || Elle ne prédit pas le trouble.", "Ponction lombaire || Elle n'est pas indiquée.", "Caryotype || Il ne prédit pas ce trouble.", "TSH || Elle cherche une autre cause.", "Ammoniémie || Elle cherche une autre cause.", "Score d'Apgar seul || Il est peu prédictif."],
 notions="N08 N06 N10", angle="application", diff=2, ladder=L("Nourrisson à risque.", "Prédiction.", "3 mois corrigés.", "Outils validés.", "IRM, Prechtl, HINE.", "EEG.", "Image, vidéo, examen."), sources="[Novak, JAMA Pediatr 2017]"),
dict(format="MenuLong", stem="Un nourrisson de 3 mois est hypotone.", prompt="Choisissez les TROIS signes qui orientent vers une cause périphérique plutôt que cérébrale.",
 items=["*Aréflexie ostéotendineuse || Elle signe une atteinte du nerf, du motoneurone ou du muscle.", "*Fasciculations de la langue || Elles signent une atteinte du motoneurone.", "*Éveil et regard vif préservés || Le cerveau fonctionne normalement.", "Réflexes vifs || Ils orientent vers une cause centrale.", "Crises épileptiques || Elles orientent vers une cause centrale.", "Microcéphalie || Elle oriente vers une cause centrale.", "Retard des interactions sociales || Il oriente vers une cause centrale.", "Clonus de cheville || Il oriente vers une cause centrale.", "Préférence manuelle précoce || Elle oriente vers une cause centrale.", "Persistance des réflexes archaïques || Elle oriente vers une cause centrale.", "Strabisme || Il oriente plutôt vers une cause centrale.", "Irritabilité excessive || Elle oriente vers une cause centrale."],
 notions="N11 N05", angle="application", diff=2, ladder=L("Nourrisson hypotone.", "Central ou périphérique.", "Réflexes, langue, éveil.", "Discriminants.", "Aréflexie, fasciculations, éveil.", "Réflexes vifs.", "Mou et éveillé = périphérique."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Paralysie cérébrale à la phase hypotonique précoce : reconnaître le nourrisson à risque, prédire le trouble avant 5 mois par Prechtl, HINE et IRM, écarter une cause périphérique ou évolutive, orienter sans attendre vers l'intervention précoce et prévenir par magnésium et hypothermie",
 notions=[
  dict(titre="Reconnaître le nourrisson à risque", rub=["def", "epi", "ana", "exa"], comment="Pense à une atteinte motrice cérébrale devant un nourrisson hypotone né prématuré ou après une encéphalopathie néonatale.",
   tableau=(["Élément", "Contenu", "Pourquoi"], [
     ["Définition", "Troubles permanents du mouvement et de la posture", _T("Lésion non progressive", "Les signes changent pourtant avec l'âge.")],
     ["Terrain", "Prématurité, encéphalopathie, AVC néonatal, infection congénitale", "Causes principales"],
     ["Phase précoce", "Hypotonie axiale, retard moteur", "La spasticité vient vers 6 à 12 mois"],
     ["Préférence manuelle avant 12 mois", "Atteinte unilatérale", "Anormale à cet âge"]]),
   points=["Elle touche environ 1 naissance vivante sur 500."], sources=["[Novak, JAMA Pediatr 2017]"]),
  dict(titre="Prédire tôt", rub=["gold", "alt", "pos"], comment="Combine anamnèse, IRM et examens standardisés pour poser un haut risque avant 6 mois d'âge corrigé.",
   tableau=(["Âge corrigé", "Outil", "Sensibilité"], [
     ["Avant 5 mois", "Mouvements généraux de Prechtl", _T("98 %", "L'absence de fidgety vers 3 mois est le signal.")],
     ["Avant 5 mois", "IRM à terme", "86 à 89 %"],
     ["Avant et après 5 mois", "HINE", "90 %"],
     ["Après 5 mois", "Échelle de développement standardisée", "Relais"]]),
   points=["Un résultat anormal suffit à orienter vers l'intervention précoce."], sources=["[Novak, JAMA Pediatr 2017]"]),
  dict(titre="Écarter les imitateurs", rub=["pos", "red", "bas"], comment="Cherche une cause périphérique ou évolutive avant de conclure.",
   tableau=(["Indice", "Orientation", "Pourquoi"], [
     ["Aréflexie, fasciculations linguales, éveil vif", "Cause périphérique (amyotrophie spinale)", _T("Motoneurone", "Le cerveau fonctionne normalement.")],
     ["Régression des acquis", "Maladie neurodégénérative ou métabolique", "La lésion n'est pas fixée"],
     ["Réflexes vifs, crises, microcéphalie", "Cause centrale", "Compatible"],
     ["Leucomalacie périventriculaire", "Diplégie spastique", "Fibres des membres inférieurs"]]),
   points=["Une régression n'est jamais une paralysie cérébrale."], sources=["[avis d'expert]"]),
  dict(titre="Agir et prévenir", rub=["acu", "chr", "hos", "fol"], comment="Oriente vers l'intervention précoce dès la suspicion et dépiste les comorbidités.",
   arbre=[("t1", None, "Haut risque ou diagnostic posé", "L'enfant entre dans une intervention précoce spécifique.", "pc"),
          ("t2", "t1", "Spasticité focale gênante", "Toxine botulique et physiothérapie.", "pc"),
          ("t3", "t1", "Spasticité étendue sévère", "Baclofène, éventuellement intrathécal.", "pc"),
          ("t4", "t1", "Comorbidités", "Épilepsie, vision, audition, déglutition, douleur, hanches.", "pc"),
          ("t5", None, "Prévention", "Magnésium maternel avant 34 semaines ; hypothermie néonatale.", None)],
   points=["En Suisse, l'AI prend en charge les mesures médicales au titre des infirmités congénitales."], sources=["[Novak, JAMA Pediatr 2017]", "[Shepherd, Cochrane 2024]"]),
 ],
 ssp=dict(code="O2.11", nom="Faible tonus musculaire et hypotonie", officiel=True, algorithme=[
  ("n1", None, "Nourrisson hypotone", "Le médecin cherche réflexes, fasciculations, éveil et terrain."),
  ("n2", "n1", "Aréflexie, fasciculations, éveil préservé", "Cause périphérique : génétique de l'amyotrophie spinale.", None, "c3"),
  ("n3", "n1", "Régression des acquis", "Bilan neurométabolique : renvoi au SSP retard du développement.", None, "c3"),
  ("n4", "n1", "Prématurité ou encéphalopathie, réflexes présents", "Prechtl, HINE et IRM.", None, "c2"),
  ("n5", "n4", "Examens anormaux concordants", "Haut risque de paralysie cérébrale : intervention précoce.", "pc", "c4"),
  ("n6", "n4", "Examens normaux", "Suivi structuré du développement.", None, "c2")]),
 pec=[
  dict(cle="pc", titre="Paralysie cérébrale ou haut risque chez le nourrisson",
   but=["Optimiser la motricité et la cognition par la plasticité.", "Prévenir les complications secondaires.", "Soutenir les parents."],
   moyens=dict(accueil=["Annoncer le haut risque avec tact.", "Organiser l'intervention précoce.", "Dépister vision, audition et déglutition."],
    pharma=[("Toxine botulique (spasticité focale)", "Doses selon le poids ; à vérifier dans l'AIPS.", "Elle réduit la spasticité ciblée.", "[avis d'expert]"),
            ("Baclofène (spasticité étendue)", "Posologie pédiatrique à vérifier dans l'AIPS.", "Il réduit la spasticité généralisée.", "[avis d'expert]")],
    nonpharma=[("rééducation", "Physiothérapie et ergothérapie précoces et spécifiques.", "Elles exploitent la plasticité."),
               ("rééducation", "Logopédie pour alimentation et communication.", "Elle prévient les troubles de déglutition."),
               ("social et assurances", "Demande AI au titre des infirmités congénitales.", "Elle finance les mesures médicales.")],
    transversal=[("Neuropédiatrie", "Elle coordonne et traite l'épilepsie."), ("Orthopédie pédiatrique", "Elle surveille les hanches et les déformations.")]),
   urgence=None,
   horsUrgence=(["Intervention précoce sans attendre la certitude.", "Surveillance des hanches."],
            [("d'abord", "pédiatre", "Repère le nourrisson à risque et organise Prechtl, HINE et IRM."),
             ("ensuite", "neuropédiatre", "Pose le haut risque ou le diagnostic."),
             ("puis", "physiothérapeute", "Débute l'intervention précoce."),
             ("puis", "orthopédiste pédiatrique", "Surveille hanches et spasticité.")]),
   pronostic="Dans les pays à revenu élevé, 2 enfants sur 3 marchent, 3 sur 4 parlent et 1 sur 2 a une intelligence normale.",
   suivi=[("Motricité (GMFCS)", "Régulier", "Niveau stable ou meilleur"), ("Hanches", "Radiographie régulière", "Pas de luxation"), ("Comorbidités", "À chaque visite", "Dépistées et traitées")],
   sortie="Le suivi reste interdisciplinaire et au long cours.",
   prevention=["Elle repose sur le sulfate de magnésium maternel avant 34 semaines et l'hypothermie néonatale.", "Elle passe par l'intervention précoce.", "Elle prévient luxation de hanche et complications."]),
 ])
AVERIFIER = ["Prise en charge par l'AI au titre des infirmités congénitales (OIC) : numéro et conditions à vérifier dans l'annexe de l'ordonnance.", "Posologies pédiatriques de la toxine botulique et du baclofène à vérifier dans l'AIPS.", "La définition de la paralysie cérébrale et les critères de l'hypothermie néonatale reposent sur des références classiques non citées ici en détail (Rosenbaum 2007, essais d'hypothermie)."]
