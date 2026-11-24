ID = "G40.9_premiere_crise_epile__O3_7-E15"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[Fisher, ILAE, Epilepsia, 2014]|L'épilepsie se définit par deux crises non provoquées à plus de 24 heures d'intervalle, ou par une crise non provoquée avec un risque de récidive d'au moins 60 % sur 10 ans, ou par un syndrome épileptique.",  # N01
"def|critère|2||[Beghi, ILAE, Epilepsia, 2010]|Une crise symptomatique aiguë, dite provoquée, survient dans les 7 jours d'une agression cérébrale ou lors d'un trouble métabolique ou toxique, et ne définit pas une épilepsie.",  # N02
"epi|chiffre|1||[Krumholz, AAN/AES, Neurology, 2015]|Après une première crise non provoquée, le risque de récidive est le plus élevé dans les 2 premières années, de l'ordre de 21 à 45 %.",  # N03
"bas|mécanisme|1||[avis d'expert]|La privation de sommeil, l'alcool et certains médicaments abaissent le seuil épileptogène et favorisent une crise.",  # N04
"ana|symptôme|2||[Brigo, Seizure, 2012 ; avis d'expert]|Le témoignage d'un tiers est décisif : yeux ouverts, mouvements tonico-cloniques prolongés, cyanose et confusion post-critique prolongée orientent vers une crise plutôt qu'une syncope.",  # N05
"exa|signe|2||[Brigo, Seizure, 2012]|La morsure latérale de langue est très spécifique d'une crise généralisée tonico-clonique, alors que la perte d'urine ne distingue pas crise et syncope.",  # N06
"red|diagnostic différentiel|3||[ESC, Syncope, 2018]|La syncope convulsivante donne quelques secousses myocloniques brèves avec retour rapide à la conscience, et une cause cardiaque se cherche par l'ECG.",  # N07
"red|piège|2||[avis d'expert]|Une crise inaugurale avec déficit focal, céphalée brutale, fièvre, traumatisme ou anticoagulant impose un scanner cérébral en urgence.",  # N08
"gold|examen|2||[Krumholz, AAN/AES, 2015 ; ILAE]|L'EEG fait au mieux dans les 24 à 48 heures et l'IRM cérébrale avec protocole épilepsie estiment le risque de récidive et orientent le syndrome.",  # N09
"alt|examen|1||[avis d'expert]|La glycémie, le sodium, le calcium, l'alcoolémie, un dépistage toxique selon le contexte et un ECG cherchent une cause provoquée ou un mime cardiaque.",  # N10
"alt|résultat|1||[avis d'expert]|Un lactate élevé juste après l'épisode puis des CK élevées à distance soutiennent une crise généralisée, sans la prouver.",  # N11
"pos|diagnostic différentiel|1||[avis d'expert]|La crise psychogène non épileptique donne des mouvements asynchrones, des yeux fermés et une durée prolongée, et se confirme par vidéo-EEG.",  # N12
"pos|diagnostic différentiel|1||[avis d'expert]|L'hypoglycémie et le sevrage alcoolique, de 6 à 48 heures après l'arrêt, sont des causes provoquées fréquentes à corriger.",  # N13
"acu|décision|1||[avis d'expert]|Une crise de plus de 5 minutes se traite comme un état de mal par une benzodiazépine.",  # N14
"acu|décision|1||[avis d'expert]|Les premiers secours placent la personne en position latérale de sécurité, protègent la tête et ne mettent rien dans la bouche.",  # N15
"chr|décision|3||[Krumholz, AAN/AES, 2015]|Après une première crise non provoquée, un traitement antiépileptique immédiat réduit la récidive à 2 ans mais n'améliore pas la rémission à long terme, d'où une décision partagée.",  # N16
"chr|critère|2||[Fisher, ILAE, 2014]|Une anomalie épileptiforme à l'EEG ou une lésion structurelle à l'IRM font passer le risque au-dessus de 60 % et permettent de poser le diagnostic d'épilepsie dès la première crise.",  # N17
"chr|molécule|1|S|[Swissmedic, valproate, 2018 ; AIPS]|Le valproate s'évite chez la femme en âge de procréer en raison de sa tératogénicité, selon les restrictions de Swissmedic.",  # N18
"chr|molécule|1||[avis d'expert ; AIPS Swissmedic]|Le lévétiracétam et la lamotrigine sont des choix fréquents en première intention, posologies à vérifier dans l'AIPS.",  # N19
"hos|complication|1||[avis d'expert]|Une crise expose aux traumatismes, aux brûlures, à la luxation postérieure de l'épaule et à la noyade.",  # N20
"pro|pronostic|1||[Krumholz, AAN/AES, 2015]|Une crise provoquée récidive peu si sa cause est corrigée, alors qu'une crise non provoquée récidive surtout en cas d'EEG anormal, de lésion ou de crise nocturne.",  # N21
"sur|décision|1||[avis d'expert]|Le patient tient un journal des crises et revoit le neurologue avec les résultats de l'EEG et de l'IRM.",  # N22
"fol|contexte suisse|2|S|[Ligue suisse contre l'épilepsie, aptitude à la conduite ; LCR art. 15d]|L'aptitude à conduire est suspendue après une première crise selon les directives suisses, et le médecin peut signaler une inaptitude à l'autorité sans violer le secret.",  # N23
"fol|prévention|1||[avis d'expert]|Le patient évite de se baigner seul, préfère la douche au bain et ne nage que sous surveillance, car une crise dans l'eau peut noyer.",  # N24
"fol|prévention|1||[avis d'expert]|Un sommeil régulier, la modération de l'alcool et l'information des proches sur les premiers secours réduisent le risque et les conséquences d'une récidive.",  # N25
]
ANGLES = [
"La perte d'urine ne distingue pas crise et syncope.",
"La morsure latérale de langue est spécifique.",
"Crise provoquée n'égale pas épilepsie.",
"EEG anormal ou lésion : épilepsie dès la première crise.",
"Traiter ne change pas le pronostic à long terme.",
"Conduite suspendue, baignade surveillée.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une femme de 27 ans consulte à Fribourg parce qu'elle s'est réveillée ce matin avec les draps mouillés d'urine, une douleur du bord latéral droit de la langue et des courbatures. Elle avait peu dormi après une fête. C'est la première fois.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une crise tonico-clonique généralisée nocturne || La morsure latérale de langue est spécifique.", "Une infection urinaire || Elle n'explique pas la morsure ni les courbatures.", "Une énurésie isolée || Elle n'explique pas la morsure.", "Une syncope vasovagale || Elle ne survient pas en dormant et mord rarement la langue.", "Une crise de panique || Elle ne donne pas de morsure ni de perte de connaissance."],
 notions="N06 N05 N04", angle="application", diff=2, ladder=L("Perte d'urine nocturne.", "Décharge corticale généralisée.", "Morsure latérale, courbatures.", "Signe spécifique.", "Crise tonico-clonique.", "Énurésie.", "Langue latérale : crise."), sources="[Brigo, Seizure, 2012]"),
dict(format="A", serie=("S1", 2, 4), stem="L'examen neurologique de cette femme est normal. La glycémie et les électrolytes sont normaux.", prompt="Quels examens complémentaires demandez-vous ?",
 items=["*Un EEG rapide et une IRM cérébrale avec protocole épilepsie || Ils estiment le risque de récidive.", "Une ponction lombaire || Rien ne l'indique.", "Aucun examen, il s'agit d'une crise unique || Le bilan oriente la suite.", "Un scanner thoracique || Rien ne l'indique.", "Un dosage de la prolactine seul || Il ne suffit pas."],
 notions="N09 N17", angle="direct", diff=2, ladder=L("Première crise.", "Risque de récidive.", "Examen normal.", "Bilan.", "EEG + IRM.", "Rien.", "EEG + IRM."), sources="[Krumholz, AAN/AES, 2015]"),
dict(format="A", serie=("S1", 3, 4), stem="L'EEG montre des pointes-ondes généralisées et l'IRM est normale. La patiente vous demande si elle a une épilepsie.", prompt="Quelle réponse est la plus juste ?",
 items=["*Oui, car l'EEG anormal fait dépasser 60 % le risque de récidive || La définition de l'ILAE le permet dès une crise.", "Non, il faut obligatoirement deux crises || La définition de 2014 admet une seule crise.", "Non, la privation de sommeil rend la crise provoquée || Elle abaisse le seuil sans rendre la crise provoquée.", "Oui, car toute crise est une épilepsie || Une crise provoquée ne l'est pas.", "On ne peut rien dire avant 10 ans de suivi || Le risque s'estime d'emblée."],
 notions="N01 N17 N02", angle="application", diff=3, ladder=L("Première crise, EEG anormal.", "Probabilité de récidive.", "Pointes-ondes.", "Définition ILAE.", "Épilepsie.", "Deux crises obligatoires.", "Une crise + EEG anormal."), sources="[Fisher, ILAE, 2014]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Vous discutez de la suite avec cette patiente de 27 ans, qui conduit et souhaite une grossesse dans 2 ans.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Elle ne doit pas conduire pendant la période fixée par les directives suisses. || L'aptitude est suspendue après une crise.", "V: Le valproate s'évite chez elle. || Il est tératogène.", "F: Le traitement immédiat améliore la rémission à long terme. || Il réduit seulement la récidive à 2 ans.", "F: Le médecin ne peut jamais signaler l'inaptitude sans son accord. || La LCR l'y autorise."],
 notions="N23 N18 N16", angle="piège", diff=3, ladder=L("Conseils.", "Sécurité et grossesse.", "Conductrice, projet.", "Règles.", "Conduite, valproate.", "Traiter améliore tout.", "Pas de valproate."), sources="[Ligue suisse contre l'épilepsie ; Swissmedic]"),
dict(format="A", stem="Un homme de 64 ans a perdu connaissance debout dans une file d'attente à Bienne. Un témoin décrit une pâleur, quelques secousses des bras pendant 10 secondes et un réveil immédiat, bien orienté. Il s'est uriné dessus.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une syncope convulsivante || Secousses brèves et réveil immédiat orienté.", "Une crise tonico-clonique généralisée || Elle donne une confusion post-critique.", "Un état de mal épileptique || Il dure plus de 5 minutes.", "Un AIT || Il ne donne pas de perte de connaissance brève isolée.", "Une crise psychogène || Le contexte orthostatique et la pâleur orientent ailleurs."],
 notions="N07 N06 N05", angle="piège", diff=2, ladder=L("Perte de connaissance.", "Hypoperfusion cérébrale.", "Pâleur, debout, réveil immédiat.", "Syncope ou crise.", "Syncope convulsivante.", "Crise à cause de l'urine.", "Réveil immédiat : syncope."), sources="[ESC, Syncope, 2018]"),
dict(format="A", stem="Chez cet homme de 64 ans, vous retenez une perte de connaissance brève avec secousses, survenue debout.", prompt="Quel examen est indispensable dès la consultation ?",
 items=["*Un ECG à 12 dérivations || Une cause cardiaque doit être cherchée.", "Un EEG de sommeil || Il ne cherche pas une syncope.", "Une IRM cérébrale en urgence || Le tableau évoque une syncope.", "Une ponction lombaire || Rien ne l'indique.", "Un dosage de CK || Il ne distingue pas la cause cardiaque."],
 notions="N07 N10", angle="application", diff=2, ladder=L("Syncope convulsivante.", "Arythmie possible.", "Âge, debout.", "Examen clé.", "ECG.", "EEG.", "Syncope : ECG."), sources="[ESC, Syncope, 2018]"),
dict(format="A", stem="Un homme de 48 ans, gros buveur, présente une crise tonico-clonique 36 heures après son admission en chirurgie à Sion. Il tremble et transpire. La glycémie est normale.", prompt="Quelle cause retenez-vous ?",
 items=["*Un sevrage alcoolique || Il donne des crises entre 6 et 48 heures après l'arrêt.", "Une épilepsie temporale débutante || Le contexte oriente vers une crise provoquée.", "Une hypoglycémie || La glycémie est normale.", "Une hémorragie méningée || Rien ne l'oriente.", "Une syncope vasovagale || Le tableau est une crise tonico-clonique."],
 notions="N13 N02", angle="application", diff=2, ladder=L("Crise post-opératoire.", "Hyperexcitabilité de sevrage.", "36 heures, tremblement.", "Crise provoquée.", "Sevrage alcoolique.", "Épilepsie.", "6-48 h : sevrage."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 72 ans sous apixaban a fait une crise tonico-clonique après une chute dans l'escalier. Elle reste confuse 2 heures plus tard et se plaint de céphalée.", prompt="Quelle est la priorité ?",
 items=["*Un scanner cérébral en urgence || Le traumatisme, l'anticoagulant et la confusion prolongée l'imposent.", "Un EEG ambulatoire dans 3 semaines || Une hémorragie doit d'abord être exclue.", "Un lévétiracétam et un retour à domicile || La cause n'est pas connue.", "Un holter ECG || L'urgence est intracrânienne.", "Une IRM dans 2 mois || Le délai est dangereux."],
 notions="N08 N02", angle="application", diff=2, ladder=L("Crise après chute.", "Lésion intracrânienne possible.", "Anticoagulant, confusion.", "Drapeau rouge.", "Scanner urgent.", "EEG différé.", "Anticoagulant + trauma : CT."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 30 ans a fait une crise tonico-clonique unique. L'EEG et l'IRM sont normaux, l'examen aussi. Il hésite à prendre un traitement.", prompt="Quelle information est exacte ?",
 items=["*Le traitement immédiat réduit la récidive à 2 ans sans améliorer la rémission à long terme || La décision se partage.", "Le traitement est obligatoire après toute crise || Il ne l'est pas.", "Sans traitement, la récidive est certaine || Le risque est de 21 à 45 % à 2 ans.", "Le traitement guérit l'épilepsie || Il contrôle les crises.", "Le traitement permet de conduire dès le lendemain || Les règles d'aptitude s'appliquent."],
 notions="N16 N03", angle="direct", diff=3, ladder=L("Crise unique, bilan normal.", "Balance bénéfice-risque.", "Hésitation.", "Information.", "Décision partagée.", "Traitement obligatoire.", "Moins de récidive, même pronostic."), sources="[Krumholz, AAN/AES, 2015]"),
dict(format="A", stem="Une femme de 35 ans est amenée aux urgences de Genève parce qu'elle convulse depuis 7 minutes. Elle ne s'est pas réveillée entre les secousses.", prompt="Quelle mesure est prioritaire ?",
 items=["*Administrer une benzodiazépine || Une crise de plus de 5 minutes se traite comme un état de mal.", "Attendre la fin spontanée de la crise || Le risque de lésion augmente.", "Faire un EEG avant tout traitement || Il retarde le traitement.", "Mettre un objet dans la bouche || Cela blesse sans protéger.", "Donner du paracétamol || Il n'arrête pas la crise."],
 notions="N14 N15", angle="direct", diff=1, ladder=L("Convulsions prolongées.", "Auto-entretien de la crise.", "7 minutes.", "Seuil de 5 minutes.", "Benzodiazépine.", "Attendre.", "> 5 min : benzodiazépine."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 22 ans fait une première crise tonico-clonique en nageant dans le lac de Neuchâtel ; il est sorti de l'eau par un ami. Il va bien et veut reprendre la natation.", prompt="Quel conseil donnez-vous ?",
 items=["*Ne nager que sous surveillance d'une personne informée et ne pas se baigner seul || Une crise dans l'eau peut noyer.", "Reprendre librement dès demain || Le risque de noyade persiste.", "Interdire toute douche || La douche reste préférable au bain.", "Nager seul au large pour se rassurer || Le risque est maximal.", "Plonger en apnée || Le risque est majeur."],
 notions="N24 N20", angle="application", diff=1, ladder=L("Crise dans l'eau.", "Perte de contrôle.", "Natation.", "Prévention de la noyade.", "Surveillance.", "Liberté totale.", "Jamais seul dans l'eau."), sources="[avis d'expert]"),
dict(format="A", stem="Après une crise tonico-clonique, un homme de 40 ans se plaint d'une épaule droite douloureuse, bloquée en rotation interne.", prompt="Quelle lésion évoquez-vous ?",
 items=["*Une luxation postérieure de l'épaule || Elle complique classiquement une crise tonico-clonique.", "Une luxation antérieure isolée || Le blocage en rotation interne oriente vers la postérieure.", "Une tendinite simple || Le blocage oriente vers une luxation.", "Une capsulite rétractile || Elle s'installe lentement.", "Une fracture de la clavicule || Le blocage en rotation interne ne l'évoque pas."],
 notions="N20 N05", angle="piège", diff=3, ladder=L("Douleur d'épaule post-critique.", "Contraction tonique violente.", "Rotation interne bloquée.", "Complication.", "Luxation postérieure.", "Luxation antérieure.", "Crise + épaule : postérieure."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 25 ans présente des épisodes de 10 minutes de mouvements asynchrones du bassin, les yeux fermés, avec des pleurs, sans perte d'urine. L'EEG intercritique est normal.", prompt="Quel examen confirme le diagnostic le plus probable ?",
 items=["*Un enregistrement vidéo-EEG d'un épisode || Il montre l'absence de décharge pendant l'épisode.", "Un scanner cérébral || Il ne confirme pas ce diagnostic.", "Un dosage de prolactine isolé || Il manque de fiabilité.", "Une IRM médullaire || Rien ne l'indique.", "Un holter ECG || Il ne cherche pas ce diagnostic."],
 notions="N12 N09", angle="application", diff=3, ladder=L("Épisodes atypiques.", "Absence de décharge corticale.", "Yeux fermés, asynchronisme.", "Confirmation.", "Vidéo-EEG.", "Prolactine.", "Yeux fermés : vidéo-EEG."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous enseignez à des assistants la sémiologie qui distingue une crise épileptique d'une syncope.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La morsure latérale de langue oriente vers une crise. || Elle est très spécifique.", "V: Une confusion prolongée après l'épisode oriente vers une crise. || La syncope se termine vite.", "F: La perte d'urine prouve une crise. || Elle survient aussi dans la syncope.", "F: Des secousses excluent une syncope. || La syncope peut être convulsivante."],
 notions="N06 N05 N07", angle="piège", diff=2, ladder=L("Enseignement.", "Sémiologie discriminante.", "Témoignage.", "Signes fiables.", "Langue, confusion.", "Urine, secousses.", "Langue latérale."), sources="[Brigo, Seizure, 2012]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un homme de 52 ans a fait une crise tonico-clonique 3 jours après un traumatisme crânien avec contusion frontale.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Il s'agit d'une crise symptomatique aiguë. || Elle survient dans les 7 jours d'une agression cérébrale.", "V: Elle ne suffit pas à poser le diagnostic d'épilepsie. || Une crise provoquée ne la définit pas.", "F: Elle définit une épilepsie post-traumatique. || Celle-ci suppose des crises tardives non provoquées.", "F: Son risque de récidive est identique à celui d'une crise non provoquée. || Il est plus faible si la cause se corrige."],
 notions="N02 N01 N21 N08", angle="direct", diff=3, ladder=L("Crise post-traumatique précoce.", "Crise provoquée.", "J3.", "Définition.", "Symptomatique aiguë.", "Épilepsie.", "< 7 jours : provoquée."), sources="[Beghi, ILAE, 2010]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Une première crise tonico-clonique vient de survenir chez un homme de 45 ans, sans antécédent.", prompt="Évaluez chacune des affirmations suivantes au service des urgences.",
 items=["V: La glycémie se mesure immédiatement. || L'hypoglycémie se corrige.", "V: Un ECG fait partie du bilan. || Il cherche un mime cardiaque.", "V: Le sodium et le calcium se dosent. || Leurs troubles provoquent des crises.", "F: Un lactate élevé prouve à lui seul la crise. || Il soutient sans prouver."],
 notions="N10 N11 N13", angle="application", diff=2, ladder=L("Urgences.", "Cause provoquée ?", "Bilan initial.", "Examens utiles.", "Glycémie, ions, ECG.", "Lactate preuve.", "Glycémie + ions + ECG."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un chauffeur-livreur de 38 ans a fait une première crise non provoquée il y a 2 semaines. Il affirme qu'il continuera à conduire.", prompt="Quelle attitude est la plus juste ?",
 items=["*L'informer de l'inaptitude selon les directives suisses et, s'il persiste, envisager un signalement à l'autorité || La LCR l'autorise.", "Le laisser conduire s'il prend un traitement || Le traitement ne lève pas l'inaptitude.", "Signaler sans l'informer || L'information précède.", "Ne rien dire, par secret médical || La sécurité publique prime.", "L'autoriser à conduire de jour seulement || La règle ne prévoit pas cela."],
 notions="N23 N16", angle="application", diff=3, ladder=L("Conduite après crise.", "Risque routier.", "Conducteur professionnel.", "Droit suisse.", "Informer, signaler.", "Secret absolu.", "Informer puis LCR 15d."), sources="[LCR art. 15d ; Ligue suisse contre l'épilepsie]"),
dict(format="A", stem="Un étudiant de 19 ans a fait une crise tonico-clonique matinale après une nuit blanche de révisions. Il a des secousses des bras au réveil depuis 1 an, qui lui font lâcher sa tasse.", prompt="Quel élément oriente la suite ?",
 items=["*Les myoclonies matinales évoquent un syndrome épileptique, ce qui pose le diagnostic d'épilepsie || Un syndrome suffit selon l'ILAE.", "La nuit blanche rend la crise provoquée et sans suite || Elle abaisse le seuil seulement.", "Les secousses matinales sont physiologiques || Elles font lâcher les objets.", "Une syncope explique tout || Les myoclonies ne l'évoquent pas.", "Une hypoglycémie explique tout || Rien ne l'oriente."],
 notions="N01 N04 N17", angle="piège", diff=3, ladder=L("Crise et myoclonies.", "Épilepsie généralisée.", "Matin, privation de sommeil.", "Syndrome.", "Épilepsie myoclonique juvénile.", "Crise provoquée.", "Myoclonies matinales : syndrome."), sources="[Fisher, ILAE, 2014]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un homme de 33 ans a fait une première crise non provoquée.", prompt="Quels éléments augmentent le risque de récidive ? (3 réponses)",
 items=["*Anomalies épileptiformes à l'EEG || Elles élèvent nettement le risque.", "*Lésion cérébrale à l'IRM || Elle élève le risque.", "*Crise survenue pendant le sommeil || Elle élève le risque.", "Perte d'urine || Elle n'a pas de valeur pronostique.", "Lactate élevé || Il n'a pas de valeur pronostique.", "Sexe masculin || Il n'a pas de valeur pronostique.", "Fièvre récente || Elle oriente vers une cause aiguë.", "Hypoglycémie documentée || Elle rend la crise provoquée.", "Sevrage alcoolique || Il rend la crise provoquée.", "CK élevées || Elles n'ont pas de valeur pronostique.", "Morsure de langue || Elle n'a pas de valeur pronostique.", "Courbatures || Elles n'ont pas de valeur pronostique."],
 notions="N21 N17 N03", angle="direct", diff=3, ladder=L("Pronostic.", "Facteurs de récidive.", "Première crise.", "Lesquels.", "EEG, lésion, sommeil.", "Signes de la crise.", "EEG + lésion + nuit."), sources="[Krumholz, AAN/AES, 2015]"),
dict(format="MenuLong", stem="Une femme de 41 ans a fait une perte de connaissance avec secousses. Vous voulez éliminer un mime ou une cause provoquée.", prompt="Quels examens sont utiles en urgence ? (3 réponses)",
 items=["*Glycémie || Elle cherche une hypoglycémie.", "*Natrémie || Elle cherche une hyponatrémie.", "*ECG || Il cherche une arythmie.", "Prolactine isolée || Elle manque de fiabilité.", "Ponction lombaire systématique || Elle se réserve à la suspicion d'infection.", "Sérologie de Lyme || Rien ne l'indique.", "TSH en urgence || Elle n'est pas urgente.", "Ferritine || Rien ne l'indique.", "Vitamine B12 || Rien ne l'indique.", "Échographie abdominale || Rien ne l'indique.", "Radiographie du thorax || Elle n'oriente pas.", "Scanner des sinus || Rien ne l'indique."],
 notions="N10 N13 N07", angle="application", diff=2, ladder=L("Perte de connaissance.", "Causes provoquées, mimes.", "Urgences.", "Bilan ciblé.", "Glycémie, sodium, ECG.", "Examens non ciblés.", "Glucose + Na + ECG."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Première crise épileptique : distinguer crise, syncope et crise psychogène, chercher une cause provoquée, estimer la récidive par EEG et IRM, décider avec le patient et sécuriser conduite et baignade",
 notions=[
  dict(titre="Crise, syncope ou crise psychogène", rub=["ana", "exa", "red", "pos"], comment="Interroge le témoin et pèse chaque signe selon sa spécificité.",
   tableau=(["Élément", "Crise", "Syncope", "Pourquoi"], [
     ["Morsure de langue", "Latérale", "Rare, pointe", _T("Spécifique", "La contraction tonique mord le bord latéral.")],
     ["Perte d'urine", "Possible", "Possible", _T("Non discriminante", "Elle survient dans les deux.")],
     ["Secousses", "Prolongées", "Brèves (< 15 s)", _T("Durée", "L'hypoperfusion brève donne quelques myoclonies.")],
     ["Récupération", "Confusion prolongée", "Rapide et orientée", _T("Post-critique", "Le cortex épuisé récupère lentement.")],
     ["Yeux fermés, asynchronisme", "Rare", "Rare", _T("Crise psychogène", "La vidéo-EEG la confirme.")]]),
   points=["L'ECG cherche une syncope cardiaque."], sources=["[Brigo, Seizure, 2012]", "[ESC, Syncope, 2018]"]),
  dict(titre="Provoquée ou non provoquée", rub=["def", "alt"], comment="Cherche la cause aiguë avant de parler d'épilepsie.",
   tableau=(["Type", "Exemples", "Conséquence"], [
     ["Symptomatique aiguë", "Hypoglycémie, hyponatrémie, sevrage alcoolique, agression cérébrale < 7 jours", [("Corriger la cause", "Le risque de récidive baisse si la cause disparaît.")]],
     ["Non provoquée", "Aucune cause aiguë", [("Bilan EEG + IRM", "Il estime le risque de récidive.")]],
     ["Drapeau rouge", "Déficit, céphalée, fièvre, trauma, anticoagulant", [("Scanner urgent", "Une lésion aiguë doit être exclue.")]]]),
   points=["Glycémie, ions, ECG d'emblée."], sources=["[Beghi, ILAE, 2010]"]),
  dict(titre="Diagnostic d'épilepsie et traitement", rub=["def", "chr", "pro"], comment="Applique la définition ILAE puis décide avec le patient.",
   arbre=[("e1", None, "Crise non provoquée", "L'EEG et l'IRM estiment le risque."),
          ("e2", "e1", "EEG épileptiforme ou lésion", "Risque ≥ 60 % : épilepsie.", "crise1"),
          ("e3", "e1", "Bilan normal", "Récidive 21-45 % à 2 ans : décision partagée.", "crise1"),
          ("e4", "e2", "Traitement", "Lévétiracétam ou lamotrigine, pas de valproate chez la femme en âge de procréer.", "crise1"),
          ("e5", "e3", "Information", "Le traitement réduit la récidive à 2 ans sans changer la rémission à long terme.", "crise1")],
   points=["Un syndrome épileptique suffit aussi au diagnostic."], sources=["[Fisher, ILAE, 2014]", "[Krumholz, AAN/AES, 2015]"]),
  dict(titre="Sécurité et cadre suisse", rub=["fol", "hos", "acu"], comment="Protège le patient et autrui dès la consultation.",
   tableau=(["Thème", "Conduite", "Pourquoi"], [
     ["Crise > 5 min", "Benzodiazépine", "Elle se traite comme un état de mal."],
     ["Conduite", [("Suspension selon directives", "Les délais se vérifient auprès de la Ligue suisse contre l'épilepsie.")], "Le risque routier est majeur."],
     ["Signalement", "LCR art. 15d", "Le médecin peut signaler sans violer le secret."],
     ["Eau", "Pas de bain seul, natation surveillée", "Une crise dans l'eau peut noyer."],
     ["Épaule bloquée", "Chercher une luxation postérieure", "La contraction tonique la provoque."]]),
   points=["Sommeil régulier, alcool modéré."], sources=["[Ligue suisse contre l'épilepsie]", "[LCR art. 15d]"]),
 ],
 ssp=dict(code="S7.10", nom="Secousses musculaires, fasciculations, convulsions, crise épileptique et état de mal épileptique", officiel=True, algorithme=[
  ("n1", None, "Perte de connaissance avec secousses", "Le témoin et l'examen orientent."),
  ("n2", "n1", "Crise en cours > 5 min", "État de mal : benzodiazépine (même SSP).", None, "c4"),
  ("n3", "n1", "Réveil rapide, pâleur, debout", "Syncope : ECG et filière syncope (F1.15).", None, "c1"),
  ("n4", "n1", "Yeux fermés, asynchronisme", "Crise psychogène : vidéo-EEG.", None, "c1"),
  ("n5", "n1", "Crise probable", "La cause aiguë se cherche.", None, "c2"),
  ("n6", "n5", "Drapeau rouge", "Scanner cérébral urgent.", None, "c2"),
  ("n7", "n5", "Cause provoquée", "Corriger la cause sans antiépileptique au long cours.", "crise1", "c2"),
  ("n8", "n5", "Non provoquée", "EEG et IRM, décision partagée.", "crise1", "c3"),
  ("n9", "n8", "Conseils", "Conduite suspendue, baignade surveillée.", "crise1", "c4")]),
 pec=[
  dict(cle="crise1", titre="Première crise épileptique",
   but=["Exclure un mime et une cause aiguë.", "Estimer la récidive et protéger le patient."],
   moyens=dict(accueil=["Recueillir le témoignage.", "Glycémie, ions, ECG ; scanner si drapeau rouge."],
    pharma=[("Lévétiracétam (antiépileptique)", "Si traitement décidé ; posologie à vérifier dans l'AIPS.", "Il a peu d'interactions.", "[AIPS Swissmedic]"),
            ("Lamotrigine (antiépileptique)", "Titration lente ; à vérifier dans l'AIPS.", "Elle convient à la femme en âge de procréer.", "[AIPS Swissmedic]"),
            ("Benzodiazépine", "Si crise > 5 minutes ; à vérifier dans l'AIPS.", "Elle interrompt la crise.", "[avis d'expert]")],
    nonpharma=[("éducation thérapeutique", "Premiers secours aux proches, journal des crises.", "Ils réduisent les conséquences d'une récidive."),
               ("hygiène de vie", "Sommeil régulier, alcool modéré, pas de bain seul.", "Ils réduisent le risque et la noyade.")],
    transversal=[("Médecine du trafic", "Elle évalue l'aptitude à conduire selon les directives suisses.")]),
   urgence=(["Glycémie immédiate.", "Benzodiazépine si crise > 5 minutes."],
            [("d'abord", "médecin urgentiste", "Recueille le témoignage et cherche un drapeau rouge."),
             ("en même temps", "infirmier·ère", "Mesure glycémie, constantes et surveille la vigilance."),
             ("ensuite", "neurologue", "Organise EEG et IRM.")]),
   horsUrgence=(["EEG et IRM rapidement.", "Décision partagée sur le traitement."],
            [("d'abord", "neurologue", "Pose ou non le diagnostic d'épilepsie."),
             ("ensuite", "médecin de famille", "Suit l'observance et les effets indésirables."),
             ("puis", "patient·e", "Tient le journal et respecte les règles de conduite.")]),
   pronostic="Le risque de récidive se concentre sur les 2 premières années et dépend de l'EEG, de l'IRM et du caractère nocturne.",
   suivi=[("Crises", "À chaque consultation", "Absence de récidive"), ("Conduite", "Selon le délai fixé", "Aptitude réévaluée"), ("Tolérance", "Si traitement", "Absence d'effets indésirables")],
   sortie="Le patient sort après récupération complète et exclusion d'une cause aiguë grave.",
   prevention=["Elle évite la privation de sommeil et l'excès d'alcool.", "Elle forme les proches aux premiers secours.", "Elle sécurise conduite et baignade."]),
 ])
AVERIFIER = ["Délais d'inaptitude à la conduite après une première crise selon la Ligue suisse contre l'épilepsie à vérifier (groupe 1 et groupe 2).",
             "Date et contenu exacts des restrictions Swissmedic sur le valproate à vérifier.",
             "Posologies du lévétiracétam, de la lamotrigine et des benzodiazépines à vérifier dans l'AIPS."]
