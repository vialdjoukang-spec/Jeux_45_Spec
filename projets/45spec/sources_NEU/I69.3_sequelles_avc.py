ID = "I69.3_sequelles_d_avc_apha__F1_11-E04"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[avis d'expert]|L'aphasie est un trouble acquis du langage ; l'aphasie de Broca est non fluente avec compréhension relativement préservée, l'aphasie de Wernicke est fluente avec compréhension altérée et paraphasies.",  # N01
"ana|signe|2||[avis d'expert]|L'aphasie de conduction touche surtout la répétition, et l'aphasie globale altère à la fois l'expression et la compréhension.",  # N02
"pos|diagnostic différentiel|2||[avis d'expert]|La dysarthrie altère l'articulation sans toucher le langage : le patient comprend, lit et écrit normalement.",  # N03
"bas|mécanisme|1||[avis d'expert]|L'aphasie de Broca traduit une lésion frontale inférieure gauche, l'aphasie de Wernicke une lésion temporale supérieure gauche, dans le territoire de l'artère cérébrale moyenne.",  # N04
"chr|décision|3||[Breitenstein, Lancet, 2017]|Une logopédie intensive d'au moins 10 heures par semaine pendant 3 semaines améliore la communication verbale même plus de 6 mois après l'AVC.",  # N05
"chr|décision|2||[Winstein, Stroke, AHA/ASA 2016]|La rééducation motrice répétitive et orientée vers des tâches, dont la thérapie par contrainte induite du membre supérieur, améliore la fonction du côté parétique.",  # N06
"chr|molécule|2||[Winstein, Stroke, AHA/ASA 2016]|La toxine botulique A réduit la spasticité focale et améliore l'hygiène et le confort, en complément de la physiothérapie.",  # N07
"chr|piège|2||[FOCUS Trial Collaboration, Lancet, 2019]|La fluoxétine donnée pour améliorer la récupération motrice n'améliore pas le pronostic fonctionnel et augmente les fractures.",  # N08
"epi|chiffre|2||[Hackett, Int J Stroke, 2014]|La dépression touche environ un tiers des patients après un AVC.",  # N09
"hos|complication|2||[avis d'expert]|Les séquelles exposent aux chutes, à l'épaule douloureuse de l'hémiplégique, aux escarres, aux pneumonies d'aspiration en cas de dysphagie et à l'épilepsie post-AVC.",  # N10
"sur|seuil|3||[Kleindorfer, Stroke, AHA/ASA 2021]|En prévention secondaire, la pression artérielle vise moins de 130/80 mmHg chez la plupart des patients et le LDL moins de 1,8 mmol/l (70 mg/dl) en cas d'origine athéroscléreuse.",  # N11
"chr|molécule|1||[Kleindorfer, Stroke, AHA/ASA 2021]|Un antiplaquettaire au long cours s'impose après un AVC ischémique non cardio-embolique, et une anticoagulation en cas de fibrillation auriculaire.",  # N12
"exa|signe|1||[avis d'expert]|L'hémiparésie séquellaire montre une spasticité, des réflexes vifs et un signe de Babinski du côté atteint.",  # N13
"ana|symptôme|1||[avis d'expert]|L'aphasie de Wernicke s'accompagne souvent d'une anosognosie : le patient ne perçoit pas ses erreurs.",  # N14
"gold|examen|2||[avis d'expert]|Le bilan du langage par le logopédiste mesure expression, compréhension, répétition, dénomination, lecture et écriture et guide la rééducation.",  # N15
"alt|examen|1||[avis d'expert]|Un dépistage de la dysphagie précède toute alimentation orale, car l'aspiration peut être silencieuse.",  # N16
"red|signe|2||[avis d'expert]|Une aggravation nouvelle d'un déficit ancien fait chercher une récidive d'AVC, une crise épileptique ou une cause métabolique ou infectieuse.",  # N17
"acu|décision|1||[avis d'expert]|À la phase de séquelles, une aggravation aiguë se traite comme un nouvel AVC jusqu'à preuve du contraire.",  # N18
"pro|pronostic|1||[avis d'expert]|La récupération est la plus rapide dans les 3 premiers mois, mais le langage et la fonction peuvent encore progresser au-delà.",  # N19
"fol|contexte suisse|1|S|[LCR art. 15d ; avis d'expert]|Le médecin évalue l'aptitude à conduire ; la loi sur la circulation routière l'autorise à signaler un doute sur cette aptitude à l'autorité cantonale.",  # N20
"fol|contexte suisse|1|S|[LAI ; avis d'expert]|L'assurance-invalidité finance des mesures de réadaptation professionnelle, et une annonce précoce favorise le maintien en emploi.",  # N21
"fol|décision|1||[avis d'expert]|L'équipe associe physiothérapie, ergothérapie, logopédie, neuropsychologie et service social, et elle forme les proches à la communication avec la personne aphasique.",  # N22
"red|piège|1||[avis d'expert]|L'aphasique n'est pas confus ni dément pour autant : il faut adapter la communication et ne pas conclure à une incapacité de discernement sans évaluation spécifique.",  # N23
"epi|terrain particulier|1||[avis d'expert]|L'aphasie touche surtout les AVC de l'hémisphère gauche, dominant pour le langage chez la grande majorité des droitiers.",  # N24
"acu|décision|1||[avis d'expert]|La mobilisation de l'épaule parétique se fait sans traction sur le bras, avec un bon positionnement, pour prévenir la subluxation et la douleur.",  # N25
"sur|examen|1||[avis d'expert]|Le suivi dépiste à chaque visite la dépression, les troubles cognitifs, la spasticité, les chutes et l'observance de la prévention secondaire.",  # N26
"def|critère|1||[avis d'expert]|Les séquelles d'AVC désignent les déficits qui persistent après la phase aiguë, moteurs, langagiers, cognitifs ou thymiques.",  # N27
]
ANGLES = [
"Broca non fluente, comprend ; Wernicke fluente, ne comprend pas.",
"Dysarthrie ≠ aphasie.",
"Logopédie intensive même en chronique.",
"Fluoxétine : pas pour la motricité.",
"Dépression : un tiers.",
"Prévention secondaire : < 130/80, LDL < 1,8.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un mécanicien de 61 ans, à Yverdon, a fait un AVC sylvien gauche il y a 8 mois. Il parle peu, avec effort, en mots isolés ; il comprend bien les consignes simples et s'énerve de ne pas trouver ses mots. Il a une hémiparésie droite à prédominance brachiale.", prompt="Quel trouble du langage présente-t-il ?",
 items=["*Une aphasie de Broca || Le discours non fluent avec compréhension préservée la caractérise.", "Une aphasie de Wernicke || Elle est fluente avec compréhension altérée.", "Une dysarthrie isolée || Elle n'empêche pas de trouver les mots.", "Une aphasie de conduction || Elle touche surtout la répétition.", "Une démence frontale || Le début brutal après AVC l'écarte."],
 notions="N01 N04", angle="application", diff=1, ladder=L("Langage pauvre.", "Broca.", "Non fluent, comprend.", "Type d'aphasie.", "Broca.", "Wernicke.", "Non fluent + comprend = Broca."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 2, 4), stem="Sa logopédie, d'une séance par semaine, s'est arrêtée au 6e mois, car « la récupération est terminée ».", prompt="Que proposez-vous ?",
 items=["*Une logopédie intensive, d'au moins 10 heures par semaine pendant 3 semaines || Elle améliore la communication même en phase chronique.", "Aucune rééducation, le plateau est atteint || Des progrès restent possibles.", "Un neuroleptique pour l'irritabilité || Rien ne l'indique.", "Une IRM de contrôle mensuelle || Elle ne change rien.", "Un apprentissage exclusif de la langue des signes || Il ne remplace pas la rééducation."],
 notions="N05 N19", angle="piège", diff=2, ladder=L("Rééducation arrêtée.", "Logopédie intensive.", "8 mois.", "Phase chronique.", "≥ 10 h/semaine.", "Plateau.", "Intensif même tard."), sources="[Breitenstein, Lancet, 2017]"),
dict(format="A", serie=("S1", 3, 4), stem="Sa femme rapporte qu'il dort mal, a perdu tout intérêt pour son jardin et pleure souvent depuis 2 mois.", prompt="Quelle conduite proposez-vous ?",
 items=["*Dépister une dépression post-AVC et la traiter, car elle touche environ un tiers des patients || Elle freine la rééducation.", "Conclure à une réaction normale sans suivi || Elle mérite d'être dépistée.", "Prescrire une benzodiazépine au long cours || Elle aggrave chutes et cognition.", "Attribuer les pleurs à l'aphasie || L'aphasie n'explique pas l'anhédonie.", "Suspendre la rééducation || Elle doit continuer."],
 notions="N09 N26", angle="application", diff=2, ladder=L("Tristesse.", "Dépression post-AVC.", "Anhédonie, sommeil.", "Fréquence.", "Dépister, traiter.", "Réaction normale.", "Un tiers."), sources="[Hackett, Int J Stroke, 2014]"),
dict(format="A", serie=("S1", 4, 4), stem="Il veut reprendre sa voiture et son travail de mécanicien.", prompt="Quelle démarche est la plus juste ?",
 items=["*Évaluer l'aptitude à conduire et organiser une annonce précoce à l'assurance-invalidité pour la réadaptation professionnelle || Ces deux volets relèvent du droit suisse.", "Autoriser la conduite sans évaluation || La sécurité routière l'interdit.", "Lui interdire définitivement tout travail || La réadaptation peut aider.", "Attendre 5 ans avant d'en parler || Le délai nuit au maintien en emploi.", "Renvoyer la question à son garagiste || Elle relève du médecin."],
 notions="N20 N21", angle="application", diff=2, ladder=L("Conduite et travail.", "Aptitude et AI.", "Mécanicien.", "Démarche.", "Évaluer, AI précoce.", "Autoriser sans évaluer.", "LCR et LAI."), sources="[LCR art. 15d]"),
dict(format="A", stem="Une femme de 74 ans a, depuis un AVC temporal gauche, un discours abondant et fluide, mais rempli de mots déformés et incompréhensibles. Elle n'exécute pas les consignes et semble ignorer ses erreurs.", prompt="Quel trouble présente-t-elle ?",
 items=["*Une aphasie de Wernicke || Le discours fluent, la compréhension altérée et l'anosognosie la caractérisent.", "Une aphasie de Broca || Elle est non fluente.", "Une confusion aiguë || Le déficit est stable et linguistique.", "Une dysarthrie || Elle n'altère pas la compréhension.", "Une psychose tardive || Le contexte d'AVC l'écarte."],
 notions="N01 N14 N04", angle="application", diff=2, ladder=L("Discours fluide incompréhensible.", "Wernicke.", "Paraphasies, anosognosie.", "Type.", "Wernicke.", "Psychose.", "Fluent + ne comprend pas = Wernicke."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 66 ans, après un AVC du tronc cérébral, parle de façon pâteuse et lente. Il comprend tout, lit le journal et écrit sans erreur.", prompt="Quel trouble présente-t-il ?",
 items=["*Une dysarthrie || L'articulation est atteinte, le langage est intact.", "Une aphasie de Broca || L'écriture serait atteinte.", "Une aphasie de Wernicke || La compréhension serait atteinte.", "Une aphasie globale || Tout serait atteint.", "Une aphasie de conduction || La répétition serait atteinte."],
 notions="N03 N02", angle="piège", diff=2, ladder=L("Parole pâteuse.", "Dysarthrie.", "Lit et écrit.", "Discriminant.", "Dysarthrie.", "Broca.", "Écrit bien = pas d'aphasie."), sources="[avis d'expert]"),
dict(format="A", stem="Un patient de 59 ans répète mal les phrases, alors qu'il parle de façon fluide et comprend bien.", prompt="Quel trouble évoquez-vous ?",
 items=["*Une aphasie de conduction || Le trouble prédominant de la répétition la caractérise.", "Une aphasie de Broca || Elle est non fluente.", "Une aphasie de Wernicke || La compréhension serait altérée.", "Une dysarthrie || Elle ne touche pas la répétition seule.", "Une surdité || Il comprend bien."],
 notions="N02 N15", angle="direct", diff=2, ladder=L("Répétition.", "Conduction.", "Fluide, comprend.", "Discriminant.", "Conduction.", "Broca.", "Répète mal = conduction."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 70 ans a une hémiparésie gauche depuis un AVC il y a 5 mois. Le coude et le poignet restent fléchis et raides ; l'hygiène de la main devient difficile.", prompt="Quel traitement proposez-vous en complément de la physiothérapie ?",
 items=["*Des injections de toxine botulique A dans les muscles spastiques || Elles réduisent la spasticité focale.", "Une immobilisation stricte du membre || Elle aggrave la raideur.", "Une benzodiazépine à forte dose || Elle sédate sans cibler la spasticité focale.", "Une chirurgie d'emblée || Elle n'est pas le premier recours.", "Aucun traitement, la spasticité est définitive || Elle se traite."],
 notions="N07 N13", angle="application", diff=2, ladder=L("Main fléchie.", "Spasticité focale.", "Coude, poignet.", "Traitement.", "Toxine botulique.", "Immobilisation.", "Focal = toxine."), sources="[Winstein, Stroke, AHA/ASA 2016]"),
dict(format="A", stem="Un homme de 68 ans a une hémiparésie droite stable depuis un AVC il y a 1 an. Depuis ce matin, sa main droite est plus faible et il parle moins bien.", prompt="Quelle conduite s'impose ?",
 items=["*Le traiter comme une suspicion de nouvel AVC et l'adresser en urgence || Une aggravation aiguë impose d'exclure une récidive.", "Attribuer l'aggravation à la fatigue || Elle ne doit pas être présumée.", "Augmenter la physiothérapie || L'urgence est neurologique.", "Reprendre rendez-vous dans un mois || Le délai ferait perdre la fenêtre de traitement.", "Prescrire un myorelaxant || Il ne répond pas."],
 notions="N17 N18", angle="piège", diff=2, ladder=L("Aggravation.", "Récidive.", "Ce matin.", "Urgence.", "Filière AVC.", "Fatigue.", "Nouveau = urgence."), sources="[avis d'expert]"),
dict(format="A", stem="Un patient de 64 ans aux antécédents d'AVC ischémique athéromateux a une pression de 148/88 mmHg et un LDL de 2,9 mmol/l sous statine faible dose.", prompt="Quelles cibles visez-vous ?",
 items=["*Pression < 130/80 mmHg et LDL < 1,8 mmol/l || Ce sont les cibles de prévention secondaire.", "Pression < 160/100 mmHg et LDL < 4 mmol/l || Elles sont trop laxistes.", "Pression < 110/60 mmHg et LDL < 0,5 mmol/l || Elles ne sont pas recommandées.", "Aucune cible, le dommage est fait || La prévention réduit les récidives.", "Pression < 140/90 mmHg seulement || La cible est plus basse."],
 notions="N11 N12", angle="direct", diff=2, ladder=L("Prévention secondaire.", "Cibles.", "PA, LDL.", "Seuils.", "< 130/80, LDL < 1,8.", "< 140/90.", "130/80 et 1,8."), sources="[Kleindorfer, Stroke, AHA/ASA 2021]"),
dict(format="A", stem="Une neurologue propose de la fluoxétine à un patient non déprimé, 2 semaines après un AVC, pour améliorer sa récupération motrice.", prompt="Quelle remarque est la plus juste ?",
 items=["*Les grands essais n'ont pas montré de bénéfice fonctionnel et ont relevé plus de fractures || La fluoxétine n'est pas indiquée pour cela.", "Elle double la récupération motrice || Les essais l'ont démenti.", "Elle est obligatoire après tout AVC || Elle ne l'est pas.", "Elle remplace la physiothérapie || Rien ne la remplace.", "Elle prévient la récidive d'AVC || Elle ne la prévient pas."],
 notions="N08 N06", angle="piège", diff=3, ladder=L("Fluoxétine.", "Récupération motrice.", "Non déprimé.", "Preuves.", "Pas de bénéfice, fractures.", "Récupération doublée.", "FOCUS négatif."), sources="[FOCUS Trial Collaboration, Lancet, 2019]"),
dict(format="A", stem="Un homme de 72 ans, hémiplégique gauche depuis 3 mois, se plaint d'une douleur de l'épaule gauche lors des transferts.", prompt="Quelle mesure de prévention est la plus juste ?",
 items=["*Positionner l'épaule et éviter de tirer sur le bras lors des transferts || Cela prévient la subluxation et la douleur.", "Tirer sur le bras pour le relever || Cela aggrave la subluxation.", "Immobiliser l'épaule en permanence || Cela favorise la capsulite.", "Prescrire un opioïde au long cours || Il ne prévient rien.", "Ignorer la plainte || La douleur freine la rééducation."],
 notions="N25 N10", angle="application", diff=1, ladder=L("Épaule douloureuse.", "Prévention.", "Transferts.", "Mesure.", "Positionner, ne pas tirer.", "Tirer.", "Ne pas tirer le bras."), sources="[avis d'expert]"),
dict(format="A", stem="Un patient de 77 ans, hémiparétique depuis un AVC, tousse à chaque repas et a fait deux pneumonies en 3 mois.", prompt="Quelle démarche proposez-vous ?",
 items=["*Une évaluation de la déglutition par le logopédiste et une adaptation des textures || Une dysphagie avec aspirations est probable.", "Une antibiothérapie préventive au long cours || Elle ne traite pas la cause.", "Une IRM cérébrale urgente || Elle ne répond pas à la question.", "Un sirop antitussif || Il masque le signe d'alerte.", "Aucune mesure || Le risque de pneumonie persiste."],
 notions="N16 N10", angle="application", diff=2, ladder=L("Toux aux repas.", "Dysphagie.", "Pneumonies.", "Démarche.", "Bilan de déglutition.", "Antibiotique.", "Toux au repas = aspirer."), sources="[avis d'expert]"),
dict(format="A", stem="Un notaire demande si un patient très aphasique depuis son AVC peut signer un testament.", prompt="Quelle réponse est la plus juste ?",
 items=["*L'aphasie ne prouve pas une incapacité de discernement : une évaluation spécifique, avec une communication adaptée, est nécessaire || Le langage et le jugement sont distincts.", "Il est incapable de discernement par définition || L'aphasie n'abolit pas le jugement.", "Il est capable sans évaluation || Le doute justifie une évaluation.", "Seul un scanner peut trancher || Il ne mesure pas le discernement.", "Un proche peut signer à sa place sans démarche || Ce n'est pas prévu."],
 notions="N23 N15", angle="piège", diff=3, ladder=L("Testament.", "Discernement.", "Aphasie.", "Distinction.", "Évaluer spécifiquement.", "Incapable d'office.", "Aphasie ≠ incapacité."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez les types d'aphasie séquellaire après un AVC.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'aphasie de Broca est non fluente. || Le discours est réduit et laborieux.", "V: L'aphasie de Wernicke altère la compréhension. || Elle s'accompagne de paraphasies.", "F: La dysarthrie est une forme d'aphasie. || Elle touche l'articulation, pas le langage.", "F: L'aphasie de conduction altère surtout la compréhension. || Elle altère surtout la répétition."],
 notions="N01 N02 N03", angle="direct", diff=2, ladder=L("Révision.", "Types.", "Fluence, compréhension.", "Pièges.", "Broca, Wernicke.", "Dysarthrie.", "Fluence et compréhension."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Une équipe de réadaptation discute du programme d'un patient avec hémiparésie et aphasie séquellaires.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La toxine botulique A complète la physiothérapie dans la spasticité focale. || Elle est recommandée.", "V: La logopédie intensive garde un effet après 6 mois. || L'essai FCET2EC l'a montré.", "F: La fluoxétine améliore la récupération motrice. || Les essais sont négatifs.", "F: Toute progression cesse après 3 mois. || Des progrès restent possibles."],
 notions="N07 N05 N08 N19", angle="direct", diff=2, ladder=L("Programme.", "Rééducation.", "Tâches, logopédie.", "Pièges.", "Tâches et intensif.", "Fluoxétine.", "Intensif et orienté tâche."), sources="[Breitenstein, Lancet, 2017]"),
dict(format="Kprim", stem="Un médecin de famille revoit un patient 9 mois après un AVC ischémique.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Il dépiste la dépression, fréquente après un AVC. || Elle touche environ un tiers des patients.", "V: Il vérifie la pression artérielle et le LDL. || Ils guident la prévention secondaire.", "F: L'aptitude à conduire ne le concerne pas. || Il doit l'évaluer.", "F: Un antiplaquettaire peut s'arrêter après 6 mois. || Il se poursuit au long cours."],
 notions="N09 N11 N20 N12", angle="application", diff=2, ladder=L("Suivi à 9 mois.", "Dépistage.", "Dépression, PA, LDL.", "Pièges.", "Dépister, cibler.", "Conduite.", "Suivi global."), sources="[Kleindorfer, Stroke, AHA/ASA 2021]"),
dict(format="Kprim", stem="Des internes discutent d'un patient hémiplégique qui chute souvent depuis son AVC.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Les chutes font partie des complications fréquentes des séquelles. || Le déficit et la spasticité les favorisent.", "V: Une épilepsie post-AVC peut expliquer des chutes. || Elle est une complication connue.", "F: Une benzodiazépine le soir réduit les chutes. || Elle les augmente.", "F: Une aggravation brutale du déficit n'a pas à être explorée. || Elle impose d'exclure une récidive."],
 notions="N10 N17 N26", angle="direct", diff=2, ladder=L("Chutes.", "Complications.", "Épilepsie, déficit.", "Pièges.", "Chercher les causes.", "Benzodiazépine.", "Chute = chercher."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un patient garde une hémiparésie et une aphasie depuis un AVC.", prompt="Choisissez les TROIS complications les plus fréquentes à dépister.",
 items=["*Dépression || Elle touche environ un tiers des patients.", "*Chutes || Le déficit les favorise.", "*Pneumonie d'aspiration en cas de dysphagie || Elle est fréquente et grave.", "Hypothyroïdie || Elle n'est pas une complication de l'AVC.", "Cataracte || Elle n'est pas une complication de l'AVC.", "Goutte || Elle n'est pas une complication de l'AVC.", "Psoriasis || Il n'est pas une complication de l'AVC.", "Anémie ferriprive || Elle n'est pas une complication de l'AVC.", "Lithiase rénale || Elle n'est pas une complication de l'AVC.", "Myopie || Elle n'est pas une complication de l'AVC.", "Asthme || Il n'est pas une complication de l'AVC.", "Hernie inguinale || Elle n'est pas une complication de l'AVC."],
 notions="N09 N10 N16", angle="direct", diff=1, ladder=L("Séquelles.", "Complications.", "Dépistage.", "Lesquelles.", "Dépression, chutes, aspiration.", "Hypothyroïdie.", "Humeur, chute, déglutition."), sources="[Hackett, Int J Stroke, 2014]"),
dict(format="MenuLong", stem="Une famille demande qui intervient dans la réadaptation de leur père aphasique et hémiparétique.", prompt="Choisissez les TROIS professionnels les plus directement concernés par ses déficits.",
 items=["*Logopédiste || Il rééduque le langage et la déglutition.", "*Physiothérapeute || Il rééduque la marche et la motricité.", "*Ergothérapeute || Il travaille l'autonomie au quotidien.", "Dermatologue || Il n'intervient pas d'emblée.", "Orthodontiste || Il n'intervient pas.", "Chirurgien cardiaque || Il n'intervient pas.", "Gynécologue || Il n'intervient pas.", "Allergologue || Il n'intervient pas.", "Néphrologue || Il n'intervient pas d'emblée.", "Orthopédiste pédiatrique || Il n'intervient pas.", "Ophtalmologue pédiatrique || Il n'intervient pas.", "Chirurgien plasticien || Il n'intervient pas."],
 notions="N22 N05 N06", angle="application", diff=1, ladder=L("Réadaptation.", "Équipe.", "Langage, motricité.", "Qui.", "Logo, physio, ergo.", "Dermatologue.", "Trois rééducateurs."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Séquelles d'AVC : nommer l'aphasie (Broca, Wernicke, conduction) et la distinguer de la dysarthrie, rééduquer intensivement même tard, traiter spasticité et dépression, tenir les cibles de prévention secondaire et régler conduite et travail selon le droit suisse",
 notions=[
  dict(titre="Types d'aphasie", rub=["def", "ana", "pos", "bas"], comment="Classe l'aphasie par fluence, compréhension et répétition.",
   tableau=(["Type", "Fluence", "Compréhension", "Répétition"], [
     ["Broca", "Non fluente", "Relativement préservée", "Altérée"],
     ["Wernicke", "Fluente, paraphasies", "Altérée, anosognosie", "Altérée"],
     ["Conduction", "Fluente", "Préservée", "Très altérée"],
     ["Globale", "Non fluente", "Altérée", "Altérée"],
     ["Dysarthrie", _T("Articulation seule", "Le patient lit, écrit et comprend normalement."), "Normale", "Normale"]]),
   points=["L'aphasie ne prouve pas une incapacité de discernement."], sources=["[avis d'expert]"]),
  dict(titre="Rééduquer", rub=["chr", "gold"], comment="Mise sur l'intensité et la répétition des tâches.",
   tableau=(["Déficit", "Mesure", "Source"], [
     ["Aphasie", "Logopédie ≥ 10 h/semaine pendant 3 semaines", "[Breitenstein, Lancet, 2017]"],
     ["Membre supérieur", "Rééducation orientée tâche, contrainte induite", "[Winstein, AHA/ASA 2016]"],
     ["Spasticité focale", "Toxine botulique A", "[Winstein, AHA/ASA 2016]"],
     ["Récupération motrice", "Pas de fluoxétine", "[FOCUS, Lancet, 2019]"]]),
   points=["Des progrès restent possibles au-delà de 6 mois."], sources=["[Breitenstein, Lancet, 2017]"]),
  dict(titre="Complications", rub=["hos", "red", "acu", "alt"], comment="Dépiste ce qui aggrave le pronostic.",
   arbre=[("k1", None, "Séquelles d'AVC", "Le médecin dépiste les complications."),
          ("k2", "k1", "Aggravation aiguë", "Nouvel AVC jusqu'à preuve du contraire.", "seq"),
          ("k3", "k1", "Toux aux repas", "Bilan de déglutition.", "seq"),
          ("k4", "k1", "Tristesse, anhédonie", "Dépression post-AVC (environ un tiers).", "seq"),
          ("k5", "k1", "Épaule douloureuse", "Positionner, ne pas tirer le bras.", "seq")],
   points=["L'épilepsie post-AVC peut expliquer chutes et aggravations transitoires."], sources=["[Hackett, Int J Stroke, 2014]"]),
  dict(titre="Prévention secondaire et réseau suisse", rub=["sur", "fol", "pro", "epi"], comment="Tient les cibles et règle conduite et travail.",
   tableau=(["Domaine", "Cible ou démarche", "Source"], [
     ["Pression artérielle", "< 130/80 mmHg", "[Kleindorfer, AHA/ASA 2021]"],
     ["LDL", "< 1,8 mmol/l si athérome", "[Kleindorfer, AHA/ASA 2021]"],
     ["Antithrombotique", "Antiplaquettaire ou anticoagulant", "[Kleindorfer, AHA/ASA 2021]"],
     ["Conduite", "Évaluer ; signalement possible", "[LCR art. 15d]"],
     ["Travail", "Annonce précoce AI", "[LAI]"]]),
   points=["La récupération est la plus rapide dans les 3 premiers mois."], sources=["[Kleindorfer, Stroke, AHA/ASA 2021]"]),
 ],
 ssp=dict(code="F1.11", nom="Parole ou élocution anormale", officiel=True, algorithme=[
  ("n1", None, "Parole anormale après un AVC", "Le médecin distingue langage et articulation."),
  ("n2", "n1", "Lit, écrit et comprend normalement", "Dysarthrie.", None, "c1"),
  ("n3", "n1", "Non fluent, comprend", "Aphasie de Broca.", "seq", "c1"),
  ("n4", "n1", "Fluent, ne comprend pas", "Aphasie de Wernicke.", "seq", "c1"),
  ("n5", "n1", "Répétition seule altérée", "Aphasie de conduction.", "seq", "c1"),
  ("n6", "n1", "Aggravation brutale", "Récidive d'AVC : urgence.", None, "c3")]),
 pec=[
  dict(cle="seq", titre="Séquelles d'AVC (aphasie, hémiparésie)",
   but=["Restaurer la communication et l'autonomie.", "Prévenir les complications et la récidive.", "Réintégrer le patient socialement et professionnellement."],
   moyens=dict(accueil=["Adapter la communication : phrases courtes, temps de réponse, supports visuels.", "Évaluer langage, motricité, humeur et déglutition.", "Associer les proches."],
    pharma=[("Toxine botulique A", "Selon l'AIPS et le spécialiste.", "Elle réduit la spasticité focale.", "[Winstein, Stroke, AHA/ASA 2016]"),
            ("Antiplaquettaire (aspirine ou clopidogrel)", "Posologie à vérifier dans l'AIPS.", "Il prévient la récidive ischémique non cardio-embolique.", "[Kleindorfer, Stroke, AHA/ASA 2021]"),
            ("Statine", "Posologie à vérifier dans l'AIPS ; cible LDL < 1,8 mmol/l.", "Elle réduit la récidive athéroscléreuse.", "[Kleindorfer, Stroke, AHA/ASA 2021]"),
            ("Antidépresseur si dépression avérée", "Posologie à vérifier dans l'AIPS.", "Il traite la dépression post-AVC, pas la motricité.", "[FOCUS Trial Collaboration, Lancet, 2019]")],
    nonpharma=[("rééducation", "Logopédie intensive, physiothérapie orientée tâche, ergothérapie.", "L'intensité et la répétition entraînent la plasticité."),
               ("social et assurances", "Annonce précoce à l'assurance-invalidité et évaluation de la conduite.", "Elles protègent l'emploi et la sécurité."),
               ("éducation thérapeutique", "Formation des proches à la communication avec la personne aphasique.", "Elle réduit l'isolement.")],
    transversal=[("Neuropsychologie", "Elle évalue la cognition et le discernement."), ("Psychiatrie", "Elle traite une dépression sévère."), ("Neurologie", "Elle ajuste la prévention secondaire.")]),
   urgence=None,
   horsUrgence=(["Programme de réadaptation intensif.", "Prévention secondaire aux cibles."],
            [("d'abord", "médecin de famille", "Évalue les déficits, l'humeur et les facteurs de risque."),
             ("en même temps", "logopédiste", "Mène la rééducation intensive du langage."),
             ("ensuite", "physiothérapeute", "Rééduque la motricité orientée tâche."),
             ("puis", "neurologue", "Traite la spasticité et ajuste la prévention."),
             ("puis", "office AI", "Organise la réadaptation professionnelle.")]),
   pronostic="La récupération est la plus rapide dans les 3 premiers mois et se poursuit plus lentement ensuite.",
   suivi=[("Pression artérielle et LDL", "Tous les 3 à 6 mois", "< 130/80 mmHg, LDL < 1,8 mmol/l"), ("Humeur", "À chaque visite", "Pas de dépression"), ("Fonction et chutes", "À chaque visite", "Stable ou meilleure")],
   sortie="Le suivi reste au long cours pour la prévention secondaire.",
   prevention=["Elle traite les facteurs de risque vasculaire.", "Elle prévient la récidive par antithrombotique et statine.", "Elle prévient chutes, dépression et aspirations."]),
 ])
AVERIFIER = ["Posologies suisses des antiplaquettaires, statines et antidépresseurs à vérifier dans l'AIPS.", "Cibles de prévention secondaire : vérifier la recommandation ESO ou suisse la plus récente par rapport à l'AHA/ASA 2021.", "Modalités cantonales d'évaluation de l'aptitude à conduire après AVC à vérifier (directives de la Société suisse de neurologie)."]
