ID = "G93.3_syndrome_de_fatigue___G4-E06"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[NICE NG206, 2021]|Le syndrome se suspecte quand fatigue invalidante aggravée par l'activité et non soulagée par le repos, malaise post-effort, sommeil non réparateur et difficultés cognitives persistent au moins 6 semaines chez l'adulte, avec une nette baisse des activités et sans autre explication.",  # N01
"def|critère|2||[NICE NG206, 2021]|Le diagnostic se confirme après 3 mois de symptômes persistants, une fois les autres causes exclues.",  # N02
"ana|symptôme|3||[NICE NG206, 2021]|Le malaise post-effort est l'aggravation des symptômes après une activité, souvent retardée de quelques heures à quelques jours, disproportionnée et suivie d'une récupération prolongée ; il est obligatoire au diagnostic.",  # N03
"epi|terrain particulier|2||[Healthcare (Basel) 2022, synthèse de NG206]|Le sexe féminin prédispose et une infection virale, y compris la COVID-19, est le déclencheur le plus fréquent.",  # N04
"epi|chiffre|1||[Healthcare (Basel) 2022, synthèse de NG206]|Un cabinet de 10 000 patients compterait environ 40 personnes atteintes, dont un quart sévèrement.",  # N05
"bas|mécanisme|1||[Healthcare (Basel) 2022, synthèse de NG206]|La cause reste inconnue ; des facteurs immunitaires, une hypoactivité de l'axe hypothalamo-hypophyso-surrénalien et une dysautonomie sont évoqués.",  # N06
"exa|signe|1||[NICE NG206, 2021 ; avis d'expert]|L'examen physique est habituellement normal ; il sert surtout à chercher une autre cause.",  # N07
"gold|examen|2||[NICE NG206, 2021]|Le bilan d'exclusion comprend bandelette urinaire, formule sanguine, urée et électrolytes, tests hépatiques, fonction thyroïdienne, VS ou CRP, calcium et phosphate, HbA1c, ferritine, sérologie cœliaque et CK.",  # N08
"alt|examen|1||[NICE NG206, 2021]|Selon le contexte s'ajoutent vitamine D, vitamine B12, folates, sérologies infectieuses et cortisol du matin.",  # N09
"red|piège|2||[NICE NG206, 2021 ; avis d'expert]|Une perte de poids, une fièvre, des sueurs nocturnes, des adénopathies ou un déficit neurologique focal orientent vers une autre maladie.",  # N10
"pos|diagnostic différentiel|2||[avis d'expert]|La dépression, les apnées du sommeil, l'hypothyroïdie, l'anémie et la maladie cœliaque imitent le syndrome ; l'absence de malaise post-effort oriente ailleurs.",  # N11
"pos|piège|1||[NICE NG206, 2021]|Aucun test ne confirme le diagnostic, qui reste clinique.",  # N12
"acu|décision|2||[NICE NG206, 2021]|Dès la suspicion, le médecin conseille de ne pas dépasser sa limite d'énergie, de se reposer au besoin et de garder une alimentation équilibrée avec une hydratation suffisante.",  # N13
"chr|piège|3||[NICE NG206, 2021]|Aucun programme à augmentation fixe de l'activité physique, comme la thérapie par exercice gradué, ne doit être proposé.",  # N14
"chr|décision|2||[NICE NG206, 2021]|La thérapie cognitivo-comportementale se propose comme soutien face à la maladie chronique, jamais comme traitement curatif.",  # N15
"chr|décision|1||[NICE NG206, 2021]|Un programme d'activité physique se réserve à certains patients, par un physiothérapeute d'une équipe spécialisée, en restant dans les limites d'énergie.",  # N16
"chr|molécule|1||[NICE NG206, 2021]|Aucun médicament ne guérit le syndrome ; les traitements visent les symptômes et aucun supplément vitaminique n'est recommandé, hormis la vitamine D selon les règles de la population générale.",  # N17
"hos|complication|1||[NICE NG206, 2021]|Les formes sévères, alitées et dépendantes, exposent à la dénutrition et justifient diététicien et visites à domicile.",  # N18
"pro|pronostic|1||[NICE NG206, 2021]|L'évolution fluctue avec poussées et rechutes ; une aggravation sévère ou durable impose une réévaluation clinique.",  # N19
"sur|décision|1||[NICE NG206, 2021]|Le suivi en soins primaires est régulier et se rapproche quand les symptômes changent ou s'aggravent.",  # N20
"fol|décision|1||[NICE NG206, 2021]|Une équipe spécialisée multidisciplinaire confirme le diagnostic et établit le plan de soins.",  # N21
"fol|contexte suisse|1|S|[avis d'expert]|En Suisse, le médecin documente l'incapacité de travail, oriente vers les assurances sociales (perte de gain, AI) et discute les adaptations du poste.",  # N22
"ana|symptôme|1||[NICE NG206, 2021]|Une intolérance orthostatique, des hypersensibilités sensorielles, des douleurs et des symptômes pseudo-grippaux accompagnent souvent le tableau.",  # N23
"red|terrain particulier|1||[Healthcare (Basel) 2022, synthèse de NG206]|Une partie des patients avec COVID long remplissent les critères du syndrome.",  # N24
"acu|piège|1||[NICE NG206, 2021]|Le patient ne doit pas « forcer » à travers les symptômes pour finir une tâche, car il déclenche un malaise post-effort.",  # N25
]
ANGLES = [
"Malaise post-effort retardé = cardinal.",
"Suspicion à 6 semaines, diagnostic à 3 mois.",
"Pas d'exercice gradué.",
"TCC = soutien, pas guérison.",
"Bilan d'exclusion de base.",
"Perte de poids, fièvre : autre cause.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une enseignante de 34 ans, à Yverdon, est épuisée depuis une infection virale il y a 7 semaines. Après une courte marche ou une journée de cours, elle est clouée au lit le surlendemain pendant plusieurs jours. Elle dort mal et cherche ses mots.", prompt="Quel symptôme est le plus caractéristique de son tableau ?",
 items=["*L'aggravation retardée et prolongée après l'effort || Le malaise post-effort est le symptôme cardinal.", "La fatigue matinale qui cède après le café || Elle n'est pas spécifique.", "La somnolence après les repas || Elle n'est pas spécifique.", "L'essoufflement immédiat à l'effort || Il oriente vers le cœur ou le poumon.", "La tristesse || Elle oriente vers une dépression."],
 notions="N03 N01 N04", angle="direct", diff=1, ladder=L("Épuisement post-viral.", "Dysrégulation énergétique.", "Effort puis effondrement retardé.", "Retard et disproportion.", "Malaise post-effort.", "Fatigue banale.", "Effort aujourd'hui, effondrement après-demain."), sources="[NICE NG206, 2021]"),
dict(format="A", serie=("S1", 2, 4), stem="Vous voulez exclure une autre cause.", prompt="Quel bilan initial demandez-vous ?",
 items=["*Formule sanguine, électrolytes, tests hépatiques et rénaux, TSH, CRP ou VS, ferritine, HbA1c, sérologie cœliaque, CK et bandelette urinaire || C'est le bilan d'exclusion recommandé.", "Une IRM cérébrale systématique || Elle n'est pas de première intention sans signe focal.", "Une biopsie musculaire || Elle n'est pas indiquée.", "Une ponction lombaire || Elle n'est pas indiquée.", "Aucun bilan, le diagnostic est évident || Les autres causes doivent être exclues."],
 notions="N08 N09 N12 N10", angle="application", diff=2, ladder=L("Exclusion.", "Imitateurs fréquents.", "Fatigue post-virale.", "Bilan de base.", "Biologie ciblée.", "IRM systématique.", "Exclure avant de conclure."), sources="[NICE NG206, 2021]"),
dict(format="A", serie=("S1", 3, 4), stem="Le bilan est normal. Les symptômes durent depuis 7 semaines et l'empêchent de travailler.", prompt="Quelle conduite adoptez-vous ?",
 items=["*Évoquer le syndrome, conseiller de rester dans sa limite d'énergie et expliquer que le diagnostic se confirme après 3 mois || La suspicion permet d'agir tôt.", "Conclure à une simulation || Les symptômes sont réels.", "Prescrire un programme d'exercice progressif obligatoire || Il expose au malaise post-effort.", "Conclure au diagnostic définitif dès maintenant || Il faut 3 mois.", "Lui conseiller de forcer pour retrouver la forme || Forcer déclenche le malaise post-effort."],
 notions="N02 N13 N25", angle="application", diff=2, ladder=L("Bilan normal à 7 semaines.", "Gestion de l'énergie.", "Incapacité.", "Suspicion, pas encore diagnostic.", "Conseils d'énergie.", "Forcer.", "Suspecter à 6 semaines, confirmer à 3 mois."), sources="[NICE NG206, 2021]"),
dict(format="A", serie=("S1", 4, 4), stem="Quatre mois plus tard, un physiothérapeute propose d'augmenter chaque semaine de 10 % le temps de marche, quel que soit son état.", prompt="Quelle est votre position ?",
 items=["*Refuser ce programme à augmentation fixe, qui n'est pas recommandé ; l'activité s'adapte à sa limite d'énergie || Il expose à des rechutes.", "L'accepter, c'est le traitement de référence || Il n'est plus recommandé.", "L'accepter en doublant l'augmentation || Le risque augmente.", "Interdire toute activité à vie || L'activité s'adapte, elle n'est pas interdite.", "Remplacer par un marathon progressif || Il est inadapté."],
 notions="N14 N16", angle="piège", diff=2, ladder=L("Programme à paliers fixes.", "Malaise post-effort.", "10 % par semaine.", "Augmentation imposée.", "Refuser, adapter.", "Exercice gradué.", "Pas de paliers fixes."), sources="[NICE NG206, 2021]"),
dict(format="A", stem="Un homme de 45 ans est fatigué depuis 4 mois. Il a perdu 8 kg, transpire la nuit et présente une adénopathie cervicale ferme de 2,5 cm.", prompt="Quelle conduite est la plus juste ?",
 items=["*Chercher activement une autre maladie, notamment un lymphome || Ces signes ne relèvent pas du syndrome de fatigue chronique.", "Conclure à un syndrome de fatigue chronique || Les signes d'alarme l'écartent.", "Proposer seulement une gestion de l'énergie || Une maladie grave doit être exclue.", "Proposer une thérapie cognitivo-comportementale || Elle ne répond pas au problème.", "Revoir dans un an || Le délai est dangereux."],
 notions="N10 N11", angle="piège", diff=2, ladder=L("Fatigue avec amaigrissement.", "Maladie organique.", "Sueurs, adénopathie.", "Signes d'alarme.", "Bilan d'une autre cause.", "Fatigue chronique.", "Perte de poids = chercher ailleurs."), sources="[NICE NG206, 2021]"),
dict(format="A", stem="Une femme de 29 ans est fatiguée depuis 5 mois. Elle ne prend plus plaisir à rien, se sent coupable et inutile ; une marche lui fait plutôt du bien et ne l'épuise pas les jours suivants.", prompt="Quel diagnostic évoquez-vous en premier ?",
 items=["*Un épisode dépressif || Anhédonie et culpabilité, sans malaise post-effort, l'orientent.", "Un syndrome de fatigue chronique || L'absence de malaise post-effort l'écarte.", "Une hypothyroïdie certaine sans dosage || Elle doit être dosée, mais le tableau oriente ailleurs.", "Une myasthénie || Elle donne une fatigabilité musculaire.", "Une sclérose en plaques || Rien ne l'évoque."],
 notions="N11 N03", angle="piège", diff=2, ladder=L("Fatigue et tristesse.", "Humeur.", "Anhédonie, culpabilité.", "Pas de malaise post-effort.", "Dépression.", "Fatigue chronique.", "L'effort aide = pas de malaise post-effort."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 52 ans, IMC 34, est fatigué depuis 6 mois. Sa femme signale des ronflements et des pauses respiratoires ; il s'endort au volant.", prompt="Quel examen demandez-vous en priorité ?",
 items=["*Une polygraphie ou polysomnographie pour chercher des apnées du sommeil || Elles expliquent fatigue et somnolence.", "Une IRM cérébrale || Rien ne l'indique.", "Une biopsie musculaire || Rien ne l'indique.", "Un EEG || Rien ne l'indique.", "Aucun, il s'agit d'un syndrome de fatigue chronique || Une cause fréquente doit être exclue."],
 notions="N11 N08", angle="application", diff=1, ladder=L("Fatigue et ronflements.", "Sommeil fragmenté.", "Pauses respiratoires.", "Somnolence au volant.", "Étude du sommeil.", "IRM.", "Ronfle et somnole = apnées."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Une patiente avec un syndrome de fatigue chronique confirmé rapporte qu'on lui a présenté la thérapie cognitivo-comportementale comme un traitement qui la guérira.", prompt="Que lui expliquez-vous ?",
 items=["*La thérapie cognitivo-comportementale peut la soutenir face à la maladie chronique, mais elle n'est pas un traitement curatif || C'est la position NICE 2021.", "Elle guérit la maladie dans la plupart des cas || Les preuves ne le montrent pas.", "Elle doit être associée à un exercice gradué obligatoire || L'exercice gradué n'est pas recommandé.", "Elle est contre-indiquée || Elle peut soutenir.", "Elle remplace tout suivi médical || Le suivi médical reste nécessaire."],
 notions="N15 N14", angle="piège", diff=2, ladder=L("Promesse de guérison.", "Soutien psychologique.", "TCC.", "Place réelle.", "Soutien, pas cure.", "TCC curative.", "TCC = soutien."), sources="[NICE NG206, 2021]"),
dict(format="A", stem="Une femme de 38 ans atteinte depuis 3 ans est alitée presque toute la journée, dépend de son mari et perd du poids.", prompt="Quelle mesure est prioritaire ?",
 items=["*Une évaluation diététique, des visites à domicile et un soutien adapté à la forme sévère || Elle est à risque de dénutrition.", "Un programme d'exercice gradué || Il n'est pas recommandé.", "Une hospitalisation psychiatrique sous contrainte || Rien ne la justifie.", "Des consultations exigeant des déplacements fréquents || Elles l'épuisent.", "Aucune mesure, l'évolution est fixée || Elle a besoin de soutien."],
 notions="N18 N13", angle="application", diff=2, ladder=L("Alitée, amaigrie.", "Forme sévère.", "Dépendance.", "Dénutrition.", "Diététicien, domicile.", "Exercice gradué.", "Sévère = venir à elle."), sources="[NICE NG206, 2021]"),
dict(format="A", stem="Un homme de 41 ans a eu la COVID-19 il y a 5 mois. Depuis, tout effort modeste l'épuise pendant plusieurs jours ; son sommeil n'est pas réparateur et il a du mal à se concentrer. Le bilan est normal.", prompt="Quel diagnostic devez-vous envisager ?",
 items=["*Un syndrome de fatigue chronique déclenché par l'infection || Il en remplit les critères.", "Une simulation || Les symptômes sont réels.", "Une insuffisance cardiaque certaine || Le bilan est normal.", "Une démence débutante || Le tableau ne l'évoque pas.", "Aucun trouble, il doit forcer || Forcer aggrave."],
 notions="N24 N04 N01", angle="application", diff=2, ladder=L("Après COVID.", "Déclencheur viral.", "Malaise post-effort.", "Critères remplis.", "Évoquer le syndrome.", "Simulation.", "Post-viral + malaise post-effort."), sources="[Healthcare (Basel) 2022, synthèse de NG206]"),
dict(masque=False, sit="monographique", format="A", stem="Une patiente suivie pour un syndrome de fatigue chronique a des vertiges, des palpitations et des nausées quand elle reste debout.", prompt="Comment interprétez-vous ces symptômes ?",
 items=["*Une intolérance orthostatique, fréquente dans ce syndrome, à évaluer et à traiter symptomatiquement || Elle fait partie des symptômes associés.", "Une crise d'angoisse certaine || Le lien avec la position l'oriente ailleurs.", "Un AVC || Rien ne l'évoque.", "Une preuve de simulation || Les symptômes sont réels.", "Une indication à un exercice gradué || Il n'est pas recommandé."],
 notions="N23 N17 N07", angle="application", diff=2, ladder=L("Symptômes debout.", "Dysautonomie.", "Palpitations, vertiges.", "Lien postural.", "Intolérance orthostatique.", "Angoisse.", "Debout = orthostatisme."), sources="[NICE NG206, 2021]"),
dict(masque=False, sit="monographique", format="A", stem="Une patiente avec un syndrome de fatigue chronique stable fait une rechute nette après un déménagement ; elle aggrave son état en essayant de finir les cartons.", prompt="Quel conseil donnez-vous ?",
 items=["*Réduire ses activités à sa limite d'énergie actuelle, prioriser l'essentiel, et consulter si l'aggravation est sévère ou durable || C'est la gestion d'une rechute.", "Forcer pour finir au plus vite || Forcer entretient la rechute.", "Commencer un exercice gradué || Il n'est pas recommandé.", "Arrêter tout suivi || Une aggravation durable impose une réévaluation.", "Prendre des stimulants || Ils ne sont pas recommandés."],
 notions="N19 N20 N25", angle="application", diff=2, ladder=L("Rechute.", "Dépassement de la limite.", "Déménagement.", "Gestion de la rechute.", "Réduire, prioriser.", "Forcer.", "Rechute = revenir sous sa limite."), sources="[NICE NG206, 2021]"),
dict(masque=False, sit="monographique", format="A", stem="Une patiente avec un syndrome de fatigue chronique veut prendre cinq suppléments vitaminiques vendus comme « anti-fatigue ».", prompt="Que lui répondez-vous ?",
 items=["*Les preuves manquent pour ces suppléments ; seule la vitamine D peut se discuter comme dans la population générale || Les doses élevées ont aussi des effets indésirables.", "Ils guérissent le syndrome || Aucune preuve ne le montre.", "Il faut en prendre à forte dose || Les doses élevées exposent à des effets indésirables.", "Ils remplacent la gestion de l'énergie || Elle reste centrale.", "Tout supplément est interdit, même la vitamine D || Elle peut se discuter."],
 notions="N17 N13", angle="piège", diff=2, ladder=L("Suppléments.", "Absence de preuve.", "Cinq produits.", "Vitamine D seule.", "Informer.", "Guérison.", "Pas de cure vitaminique."), sources="[NICE NG206, 2021]"),
dict(masque=False, sit="monographique", format="A", stem="Une employée de commerce de 36 ans avec un syndrome de fatigue chronique confirmé ne tient plus son poste à plein temps.", prompt="Quelle démarche est la plus adaptée en Suisse ?",
 items=["*Documenter l'incapacité de travail, discuter un temps partiel avec l'employeur et orienter vers les assurances sociales || Elle protège l'emploi et le revenu.", "Exiger la reprise à plein temps || Elle aggrave les symptômes.", "Refuser tout certificat || L'incapacité est réelle.", "Conseiller une démission immédiate || D'autres solutions existent.", "Prescrire un exercice gradué pour la reprise || Il n'est pas recommandé."],
 notions="N22 N21", angle="application", diff=2, ladder=L("Travail.", "Limite d'énergie.", "Plein temps impossible.", "Assurances.", "Certificat, adaptation, AI.", "Reprise forcée.", "Adapter le poste."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez les critères du syndrome de fatigue chronique (NICE 2021).", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le malaise post-effort est nécessaire au diagnostic. || Il est cardinal.", "V: Le syndrome se suspecte après 6 semaines chez l'adulte. || Le diagnostic se confirme à 3 mois.", "F: Un test sanguin spécifique confirme le diagnostic. || Le diagnostic est clinique.", "F: Le bilan d'exclusion est inutile si les symptômes sont typiques. || Il exclut les imitateurs."],
 notions="N01 N02 N12 N08", angle="direct", diff=2, ladder=L("Critères.", "Clinique.", "Malaise post-effort.", "Délais.", "Suspecter puis confirmer.", "Test spécifique.", "6 semaines, 3 mois, sans test."), sources="[NICE NG206, 2021]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Une équipe discute de la prise en charge du syndrome de fatigue chronique.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le patient doit rester dans sa limite d'énergie. || Il prévient le malaise post-effort.", "V: La thérapie cognitivo-comportementale peut servir de soutien. || Elle n'est pas curative.", "F: La thérapie par exercice gradué est recommandée. || Elle ne l'est plus.", "F: Forcer à travers les symptômes accélère la guérison. || Il déclenche des rechutes."],
 notions="N13 N15 N14 N25", angle="direct", diff=2, ladder=L("Prise en charge.", "Gestion de l'énergie.", "Limite.", "Pièges.", "Soutenir.", "Exercice gradué.", "Rester sous sa limite."), sources="[NICE NG206, 2021]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Des étudiants révisent l'épidémiologie et la physiopathologie du syndrome de fatigue chronique.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une infection virale est le déclencheur le plus fréquent. || Y compris la COVID-19.", "V: Les femmes sont plus souvent touchées. || Le sexe féminin prédispose.", "F: La cause est connue et unique. || Elle reste inconnue.", "F: Les formes sévères ne sont jamais alitées. || Certaines sont alitées et dépendantes."],
 notions="N04 N06 N05 N18", angle="direct", diff=1, ladder=L("Épidémiologie.", "Facteurs multiples.", "Infection, sexe féminin.", "Pièges.", "Connaître.", "Cause unique.", "Post-viral, féminin, cause inconnue."), sources="[Healthcare (Basel) 2022, synthèse de NG206]"),
dict(format="Kprim", stem="Un homme de 50 ans consulte pour une fatigue depuis 4 mois.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une perte de poids inexpliquée fait chercher une autre maladie. || C'est un signe d'alarme.", "V: Un déficit neurologique focal fait chercher une autre maladie. || Il n'appartient pas au syndrome.", "F: Un examen physique anormal est typique du syndrome de fatigue chronique. || L'examen est habituellement normal.", "F: Une fatigue nettement soulagée par le repos est typique du syndrome. || Elle ne l'est pas."],
 notions="N10 N07 N01", angle="piège", diff=2, ladder=L("Fatigue de 4 mois.", "Exclure.", "Alarmes.", "Ce qui n'en fait pas partie.", "Chercher ailleurs.", "Examen anormal typique.", "Alarme = autre cause."), sources="[NICE NG206, 2021]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Vous révisez les symptômes exigés pour suspecter un syndrome de fatigue chronique, en plus de la fatigue invalidante.", prompt="Choisissez les TROIS symptômes exigés.",
 items=["*Malaise post-effort || Il est obligatoire.", "*Sommeil non réparateur || Il est exigé.", "*Difficultés cognitives || Elles sont exigées.", "Intolérance orthostatique || Elle est fréquente mais non exigée.", "Hypersensibilité sensorielle || Elle est fréquente mais non exigée.", "Fièvre > 38,5 °C || Elle oriente vers une autre cause.", "Perte de poids || Elle oriente vers une autre cause.", "Adénopathies dures || Elles orientent vers une autre cause.", "Déficit moteur focal || Il oriente vers une autre cause.", "Arthrite || Elle oriente vers une autre cause.", "Ictère || Il oriente vers une autre cause.", "Hématurie || Elle oriente vers une autre cause."],
 notions="N01 N03 N23", angle="direct", diff=2, ladder=L("Critères.", "Symptômes clés.", "Fatigue plus trois.", "Exigés ou associés.", "Malaise, sommeil, cognition.", "Orthostatisme.", "Effort, sommeil, cerveau."), sources="[NICE NG206, 2021]"),
dict(format="MenuLong", stem="Une femme de 40 ans est épuisée depuis 2 mois avec un malaise post-effort ; l'examen est normal.", prompt="Choisissez les TROIS examens qui font partie du bilan initial recommandé.",
 items=["*TSH || Elle cherche une dysthyroïdie.", "*Ferritine || Elle cherche une carence martiale.", "*Sérologie cœliaque || Elle cherche une maladie cœliaque.", "IRM cérébrale systématique || Elle n'est pas de première intention.", "Ponction lombaire || Elle n'est pas indiquée.", "EEG || Il n'est pas indiqué.", "Biopsie musculaire || Elle n'est pas indiquée.", "PET-scanner || Il n'est pas indiqué.", "Polysomnographie systématique || Elle se réserve aux signes d'apnées.", "Test d'effort maximal || Il expose au malaise post-effort.", "Holter ECG systématique || Il n'est pas indiqué d'emblée.", "Électromyogramme || Il n'est pas indiqué."],
 notions="N08 N09", angle="application", diff=2, ladder=L("Fatigue et malaise post-effort.", "Exclusion.", "Examen normal.", "Biologie de base.", "TSH, ferritine, cœliaque.", "IRM systématique.", "Exclure simple et fréquent."), sources="[NICE NG206, 2021]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Syndrome de fatigue chronique (encéphalomyélite myalgique) : reconnaître le malaise post-effort, suspecter à 6 semaines et confirmer à 3 mois après un bilan d'exclusion, conseiller la gestion de l'énergie, éviter l'exercice gradué et réserver la TCC au soutien",
 notions=[
  dict(titre="Reconnaître", rub=["def", "ana", "epi", "exa"], comment="Cherche le malaise post-effort, qui distingue ce syndrome des autres fatigues.",
   tableau=(["Critère", "Contenu", "Pourquoi"], [
     ["Fatigue", "Invalidante, aggravée par l'activité, non soulagée par le repos", "Critère 1"],
     ["Malaise post-effort", _T("Retardé, disproportionné, récupération prolongée", "Il est obligatoire.")],
     ["Sommeil", "Non réparateur", "Critère 3"],
     ["Cognition", "Brouillard, mots, concentration", "Critère 4"],
     ["Durée", "Suspicion à 6 semaines, diagnostic à 3 mois", _T("NICE 2021", "Le délai permet d'agir tôt.")]]),
   points=["Une infection virale, dont la COVID-19, déclenche souvent le syndrome."], sources=["[NICE NG206, 2021]"]),
  dict(titre="Exclure", rub=["gold", "alt", "pos", "red"], comment="Exclut les causes fréquentes et les signes d'alarme avant de retenir le diagnostic.",
   tableau=(["Piste", "Indice", "Examen"], [
     ["Thyroïde, anémie, cœliaque, diabète", "Fatigue non spécifique", "TSH, formule, ferritine, sérologie, HbA1c"],
     ["Dépression", _T("Anhédonie, culpabilité, pas de malaise post-effort", "L'effort améliore plutôt l'humeur.")],
     ["Apnées du sommeil", "Ronflements, pauses, somnolence", "Étude du sommeil"],
     ["Maladie grave", _T("Perte de poids, fièvre, adénopathie, déficit focal", "Signes d'alarme.")]]),
   points=["Aucun test ne confirme le diagnostic."], sources=["[NICE NG206, 2021]"]),
  dict(titre="Prendre en charge", rub=["acu", "chr", "hos"], comment="Applique la gestion de l'énergie et évite tout programme d'activité à paliers fixes.",
   arbre=[("t1", None, "Suspicion", "Conseils d'énergie dès maintenant.", "emcfs"),
          ("t2", "t1", "Activité", "Rester sous sa limite, ne pas forcer.", "emcfs"),
          ("t3", "t1", "Exercice gradué proposé", "Le refuser : il n'est pas recommandé.", "emcfs"),
          ("t4", "t1", "Soutien psychologique", "TCC comme soutien, pas comme cure.", "emcfs"),
          ("t5", "t1", "Forme sévère", "Domicile, diététicien, dénutrition.", "emcfs")],
   points=["Aucun supplément n'est recommandé, hormis la vitamine D selon la population générale."], sources=["[NICE NG206, 2021]"]),
  dict(titre="Suivre", rub=["pro", "sur", "fol", "bas"], comment="Suit un trouble fluctuant et réévalue toute aggravation sévère ou durable.",
   tableau=(["Situation", "Conduite", "Pourquoi"], [
     ["Rechute", "Revenir sous la limite, prioriser", "Stabiliser"],
     ["Aggravation sévère ou durable", "Réévaluation clinique", "Autre cause possible"],
     ["Diagnostic", "Équipe spécialisée", "Plan de soins"],
     ["Travail en Suisse", "Certificat, adaptation, assurances", "Protéger emploi et revenu"]]),
   points=["La cause reste inconnue."], sources=["[NICE NG206, 2021]", "[avis d'expert]"]),
 ],
 ssp=dict(code="G4", nom="Fatigue, lassitude", officiel=True, algorithme=[
  ("n1", None, "Fatigue persistante", "Le médecin cherche signes d'alarme et malaise post-effort."),
  ("n2", "n1", "Perte de poids, fièvre, adénopathie, déficit focal", "Autre maladie à chercher.", None, "c2"),
  ("n3", "n1", "Anhédonie, culpabilité, sans malaise post-effort", "Dépression : renvoi à la pathologie correspondante.", None, "c2"),
  ("n4", "n1", "Ronflements, pauses, somnolence", "Apnées du sommeil.", None, "c2"),
  ("n5", "n1", "Malaise post-effort, sommeil non réparateur, cognition atteinte ≥ 6 semaines", "Bilan d'exclusion et conseils d'énergie.", "emcfs", "c1"),
  ("n6", "n5", "Persistance ≥ 3 mois, bilan normal", "Syndrome de fatigue chronique : équipe spécialisée.", "emcfs", "c3")]),
 pec=[
  dict(cle="emcfs", titre="Syndrome de fatigue chronique (encéphalomyélite myalgique)",
   but=["Prévenir le malaise post-effort.", "Soulager les symptômes.", "Préserver la vie sociale et professionnelle."],
   moyens=dict(accueil=["Croire et reconnaître les symptômes.", "Faire le bilan d'exclusion.", "Donner des conseils de gestion de l'énergie."],
    pharma=[("Traitements symptomatiques (douleur, sommeil, orthostatisme)", "Selon le symptôme ; posologies à vérifier dans l'AIPS.", "Aucun médicament ne guérit le syndrome.", "[NICE NG206, 2021]"),
            ("Vitamine D si carence", "Selon les règles de la population générale ; à vérifier dans l'AIPS.", "Seul supplément qui peut se discuter.", "[NICE NG206, 2021]")],
    nonpharma=[("éducation thérapeutique", "Gestion de l'énergie, repos réguliers, ne pas forcer.", "Elle prévient le malaise post-effort."),
               ("psychothérapie", "TCC de soutien si le patient le souhaite.", "Elle aide à vivre avec la maladie."),
               ("social et assurances", "Certificat, adaptation du poste, assurances sociales.", "Elle protège emploi et revenu.")],
    transversal=[("Médecine interne", "Elle exclut les autres causes."), ("Physiothérapie spécialisée", "Elle adapte l'activité sans paliers fixes.")]),
   urgence=None,
   horsUrgence=(["Pas d'exercice gradué.", "Suivi régulier."],
            [("d'abord", "médecin de famille", "Suspecte le syndrome et fait le bilan d'exclusion."),
             ("ensuite", "médecin de famille", "Conseille la gestion de l'énergie."),
             ("puis", "équipe spécialisée", "Confirme le diagnostic à 3 mois et établit le plan."),
             ("puis", "médecin de famille", "Suit les rechutes et l'aptitude au travail.")]),
   pronostic="L'évolution fluctue avec poussées et rechutes ; un quart des patients ont une forme sévère.",
   suivi=[("Niveau d'activité", "À chaque visite", "Sous la limite d'énergie"), ("Poids et nutrition", "Formes sévères", "Stables"), ("Symptômes nouveaux", "À chaque visite", "Réévalués")],
   sortie="Le suivi reste au long cours, rapproché lors des rechutes.",
   prevention=["Elle n'a pas de prévention primaire établie.", "Elle passe par une suspicion précoce et la gestion de l'énergie.", "Elle évite les programmes à paliers fixes."]),
 ])
AVERIFIER = ["Les recommandations citées viennent de NICE NG206 (2021), vérifiées ici à travers une synthèse publiée (Healthcare (Basel) 2022) ; la page NICE n'a pu être lue qu'en partie.", "Le chiffre de 40 patients pour 10 000 vient d'une estimation britannique et n'est pas transposé à la Suisse.", "Pratique suisse de l'AI et des assurances perte de gain dans ce syndrome à vérifier."]
