ID = "G40.9_1__F1_15-E02"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[Gallmetzer, Neurology, 2004 ; avis d'expert]|La paralysie de Todd est un déficit moteur focal transitoire qui suit une crise épileptique, siège du côté opposé au foyer et régresse complètement.",  # N01
"epi|chiffre|1||[Gallmetzer, Neurology, 2004]|En vidéo-EEG, 13,4 % des patients avec épilepsie focale ont présenté une parésie post-critique, d'une durée médiane de 173,5 secondes (11 secondes à 22 minutes).",  # N02
"bas|mécanisme|1||[Gallmetzer, Neurology, 2004]|Les auteurs évoquent un processus inhibiteur actif du cortex après la décharge plutôt qu'un simple épuisement neuronal.",  # N03
"ana|symptôme|2||[avis d'expert]|Le témoin décrit souvent une crise motrice, en particulier des clonies unilatérales, juste avant le déficit ; son récit oriente le diagnostic.",  # N04
"exa|signe|1||[avis d'expert]|Une morsure latérale de langue, une perte d'urine, des myalgies et une confusion post-critique soutiennent l'origine épileptique.",  # N05
"red|piège|3||[Powers, Stroke, AHA/ASA, 2019 ; avis d'expert]|Un déficit focal aigu se traite comme un AVC jusqu'à preuve du contraire, même si une crise l'a précédé, car un AVC peut débuter par une crise.",  # N06
"gold|examen|2||[Powers, Stroke, AHA/ASA, 2019]|L'imagerie cérébrale urgente (scanner avec angio-CT, éventuellement perfusion, ou IRM) écarte une hémorragie, une occlusion artérielle ou une lésion causale.",  # N07
"alt|examen|1||[avis d'expert]|L'EEG cherche une activité épileptique persistante quand le déficit ou la confusion se prolongent.",  # N08
"pos|diagnostic différentiel|2||[avis d'expert]|L'AVC ou l'AIT, l'hypoglycémie, la migraine hémiplégique et l'état de mal non convulsif imitent un déficit post-critique.",  # N09
"exa|examen|2||[avis d'expert]|La glycémie capillaire se mesure immédiatement, car une hypoglycémie donne à la fois crise et déficit focal et se corrige en minutes.",  # N10
"acu|décision|2||[Powers, Stroke, AHA/ASA, 2019]|Une crise au début des symptômes n'exclut pas la thrombolyse si l'imagerie montre que le déficit relève d'une ischémie et non d'un phénomène post-critique.",  # N11
"acu|décision|1||[avis d'expert]|En phase post-critique, l'équipe place le patient en position latérale de sécurité, surveille la vigilance et la respiration et ne met rien dans sa bouche.",  # N12
"hos|complication|1||[avis d'expert]|La crise expose à la pneumonie d'aspiration, aux traumatismes et à la luxation postérieure de l'épaule.",  # N13
"pro|pronostic|2||[avis d'expert]|Le déficit régresse complètement, en général en quelques minutes à quelques heures ; un déficit qui persiste fait chercher un AVC, une lésion structurelle ou un état de mal.",  # N14
"bas|mécanisme|1||[Gallmetzer, Neurology, 2004]|La parésie a une forte valeur de latéralisation : elle siège toujours du côté opposé au foyer.",  # N15
"epi|terrain particulier|1||[Gallmetzer, Neurology, 2004]|La parésie dure plus longtemps après des clonies critiques et après une crise tonico-clonique.",  # N16
"red|piège|2||[avis d'expert]|Une paralysie post-critique signe une origine focale de la crise ; elle impose de chercher une lésion structurelle (tumeur, séquelle d'AVC, malformation).",  # N17
"gold|examen|1||[avis d'expert]|L'IRM cérébrale selon un protocole épilepsie se fait à distance pour chercher la lésion épileptogène.",  # N18
"chr|décision|2||[Fisher, Epilepsia, ILAE, 2014]|Le traitement antiépileptique se décide selon le risque de récidive : une seule crise non provoquée suffit à poser une épilepsie si ce risque atteint au moins 60 % sur 10 ans, par exemple en présence d'une lésion.",  # N19
"fol|contexte suisse|3|S|[Ligue suisse contre l'épilepsie, 2019]|Après une première crise non provoquée, le délai sans conduite est en général de 6 mois pour les permis privés et de 2 ans pour les permis C et D1 ; il est de 3 mois après une crise clairement provoquée.",  # N20
"fol|contexte suisse|1|S|[avis d'expert]|Le médecin informe le patient par écrit de l'interdiction de conduire et peut annoncer l'inaptitude à l'autorité selon la loi sur la circulation routière ; l'article exact est à vérifier.",  # N21
"ana|symptôme|1||[avis d'expert]|Après une crise généralisée, l'état post-critique associe confusion, somnolence, céphalée et myalgies pendant quelques minutes à quelques heures.",  # N22
"red|seuil|1||[Trinka, Epilepsia, ILAE, 2015]|Une crise tonico-clonique qui dure 5 minutes ou des crises sans retour à l'état de base définissent l'état de mal et imposent une benzodiazépine.",  # N23
"alt|examen|1||[avis d'expert]|Le bilan sanguin comprend glycémie, sodium, calcium, magnésium, CK, alcoolémie et toxiques selon le contexte.",  # N24
"sur|examen|1||[avis d'expert]|L'équipe répète l'examen neurologique, par exemple avec le score NIHSS, jusqu'à la récupération complète.",  # N25
"fol|décision|1||[avis d'expert]|Le médecin adresse le patient au neurologue pour l'EEG, l'IRM et la décision de traitement.",  # N26
"hos|piège|1||[avis d'expert]|Un déficit post-critique répété du même côté chez une personne âgée fait d'abord penser à une lésion vasculaire ancienne épileptogène.",  # N27
]
ANGLES = [
"Déficit aigu = filière AVC d'abord.",
"Une crise n'exclut pas la thrombolyse.",
"Glycémie capillaire avant tout.",
"Todd signe une crise focale : chercher une lésion.",
"Déficit persistant = pas un Todd.",
"Conduite en Suisse : 6 mois, 3 mois, 2 ans.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un homme de 66 ans, hypertendu, est amené à Sion par son épouse. Elle l'a vu présenter des secousses du bras droit puis une perte de connaissance de 2 minutes. Trente minutes plus tard, il garde une faiblesse du bras et de la jambe droits. Il s'est mordu le bord de la langue.", prompt="Quelle est la conduite immédiate la plus juste ?",
 items=["*Activer la filière AVC avec glycémie capillaire et imagerie urgente || Un AVC peut débuter par une crise.", "Conclure à un déficit post-critique et observer 24 heures || Ce serait ignorer un AVC possible.", "Donner un antiépileptique et renvoyer à domicile || Le déficit doit être exploré.", "Faire un EEG avant toute imagerie || L'imagerie est prioritaire.", "Programmer une IRM ambulatoire || Le délai est trop long."],
 notions="N06 N07 N10 N04", angle="application", diff=2, ladder=L("Déficit après crise.", "Imitation d'AVC.", "Clonies, morsure.", "Filière AVC.", "Imagerie urgente.", "Observer.", "Déficit aigu = AVC d'abord."), sources="[Powers, Stroke, AHA/ASA, 2019]"),
dict(format="A", serie=("S1", 2, 4), stem="La glycémie capillaire est à 6,1 mmol/l. Le scanner et l'angio-CT ne montrent ni hémorragie ni occlusion. Le déficit régresse nettement en 1 heure.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Un déficit moteur post-critique transitoire || Il suit une crise focale et régresse.", "Un AVC ischémique constitué || L'évolution régressive et l'imagerie ne le soutiennent pas.", "Une migraine hémiplégique || Il n'y a ni aura ni céphalée.", "Une hypoglycémie || La glycémie est normale.", "Un trouble fonctionnel || La crise est objectivée."],
 notions="N01 N09 N14", angle="direct", diff=1, ladder=L("Régression.", "Post-critique.", "Imagerie normale.", "Diagnostic.", "Parésie post-critique.", "AVC.", "Après crise, régresse."), sources="[Gallmetzer, Neurology, 2004]"),
dict(format="A", serie=("S1", 3, 4), stem="Le patient a récupéré complètement. Il n'avait jamais fait de crise.", prompt="Quelle conclusion tirez-vous de ce déficit post-critique ?",
 items=["*La crise a une origine focale et une lésion doit être cherchée par IRM || La parésie latéralise le foyer.", "La crise était généralisée d'emblée || Le déficit unilatéral désigne un foyer.", "Aucun bilan n'est nécessaire || Une lésion est possible.", "Le patient doit recevoir un anticoagulant || Rien ne l'indique.", "Le diagnostic est psychogène || La crise est organique."],
 notions="N17 N18 N15 N01", angle="application", diff=2, ladder=L("Récupération.", "Origine focale.", "Unilatéral.", "Bilan.", "IRM protocole épilepsie.", "Aucun bilan.", "Todd = focal."), sources="[Gallmetzer, Neurology, 2004]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Le patient, chauffeur de camion (permis C), demande quand il pourra reprendre la route.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Pour son permis privé, un délai de 6 mois s'applique en général après une première crise non provoquée. || C'est la recommandation de la Ligue.", "V: Pour le permis C, le délai est en général de 2 ans. || Il est plus long pour les permis professionnels.", "F: Il peut conduire dès la récupération du déficit. || Le risque de récidive impose un délai.", "F: Le médecin n'a aucun rôle d'information. || Il doit informer le patient."],
 notions="N20 N21", angle="application", diff=2, ladder=L("Reprise de la conduite.", "Aptitude.", "Permis C.", "Délais.", "6 mois, 2 ans.", "Tout de suite.", "Professionnel = plus long."), sources="[Ligue suisse contre l'épilepsie, 2019]"),
dict(format="A", stem="Une femme de 72 ans en fibrillation auriculaire non anticoagulée est trouvée à 9 h, aphasique et hémiplégique droite, après des secousses du bras droit décrites par sa fille. Les symptômes ont commencé il y a 50 minutes. L'angio-CT montre une occlusion de l'artère cérébrale moyenne gauche.", prompt="Quelle conduite proposez-vous ?",
 items=["*Une recanalisation (thrombolyse et thrombectomie) selon l'avis neurovasculaire || L'imagerie relie le déficit à l'ischémie.", "Aucune recanalisation, car une crise l'a précédé || La crise n'exclut pas le traitement ici.", "Un antiépileptique seul et une observation || L'occlusion doit être traitée.", "Un EEG avant toute décision || Il retarderait la reperfusion.", "Une IRM de contrôle à 48 heures || Le délai serait perdu."],
 notions="N11 N06 N07", angle="piège", diff=3, ladder=L("Crise et déficit.", "AVC inaugural.", "Occlusion visible.", "Thrombolyse.", "Recanaliser.", "Crise = contre-indication.", "L'imagerie tranche."), sources="[Powers, Stroke, AHA/ASA, 2019]"),
dict(format="A", stem="Un homme de 58 ans diabétique sous insuline fait une crise généralisée chez lui, puis garde une faiblesse du bras gauche. L'ambulancier arrive.", prompt="Quel geste fait-il en premier ?",
 items=["*Mesurer la glycémie capillaire || Une hypoglycémie donne crise et déficit focal.", "Administrer de l'aspirine || Une hémorragie n'est pas exclue.", "Donner du midazolam || La crise est terminée.", "Mesurer la température || Ce n'est pas prioritaire.", "Faire un ECG 12 dérivations || Ce n'est pas le premier geste."],
 notions="N10 N09", angle="direct", diff=1, ladder=L("Diabétique.", "Cause métabolique.", "Insuline.", "Premier geste.", "Glycémie.", "Aspirine.", "Glucose d'abord."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 45 ans a fait une crise focale motrice gauche il y a 30 heures. Elle garde une hémiparésie gauche qui ne s'améliore pas et reste ralentie. Le scanner initial était normal.", prompt="Quel examen demandez-vous en priorité ?",
 items=["*Un EEG pour chercher un état de mal non convulsif, et une IRM || Un déficit prolongé n'est pas un simple post-critique.", "Aucun, il faut attendre 72 heures || L'attente retarderait un diagnostic grave.", "Une ponction lombaire d'emblée || Elle n'est pas le premier examen sans fièvre.", "Un doppler veineux des jambes || Il ne répond pas.", "Un bilan thyroïdien || Il ne répond pas."],
 notions="N14 N08 N23", angle="piège", diff=3, ladder=L("Déficit prolongé.", "Diagnostic alternatif.", "30 heures.", "Examen.", "EEG et IRM.", "Attendre.", "Persiste = autre cause."), sources="[avis d'expert]"),
dict(format="A", stem="Une étudiante demande pourquoi un déficit qui suit une crise intéresse le neurologue.", prompt="Que lui expliquez-vous ?",
 items=["*Il latéralise le foyer, qui siège dans l'hémisphère opposé au côté parétique || Il a une forte valeur de latéralisation.", "Il prouve une crise généralisée primaire || Il désigne un foyer.", "Il prouve un AVC associé || Il est réversible.", "Il siège du même côté que le foyer || Il est controlatéral.", "Il n'a aucune valeur diagnostique || Il oriente le bilan."],
 notions="N15 N17 N01", angle="direct", diff=2, ladder=L("Intérêt du signe.", "Latéralisation.", "Côté.", "Foyer.", "Hémisphère opposé.", "Même côté.", "Controlatéral."), sources="[Gallmetzer, Neurology, 2004]"),
dict(format="A", stem="Un homme de 30 ans fait une crise tonico-clonique au travail. À l'arrivée des secours, il ne convulse plus, respire bruyamment et ne répond pas.", prompt="Quel geste réalisez-vous ?",
 items=["*Le placer en position latérale de sécurité et surveiller la respiration || Il protège les voies aériennes.", "Lui mettre un objet entre les dents || Il blesse sans protéger.", "Le maintenir assis || Il favorise l'inhalation.", "Lui donner à boire || Il risque l'aspiration.", "Le laisser seul se réveiller || La surveillance est nécessaire."],
 notions="N12 N13 N22", angle="application", diff=1, ladder=L("Après la crise.", "Post-critique.", "Inconscient.", "Geste.", "PLS.", "Objet en bouche.", "Côté, surveiller."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 40 ans convulse depuis 6 minutes devant l'ambulancier, sans reprendre conscience.", prompt="Quelle conduite s'impose ?",
 items=["*Administrer une benzodiazépine sans attendre || La durée définit un état de mal.", "Attendre 15 minutes la fin spontanée || Le délai aggrave le pronostic.", "Faire d'abord un scanner || Le traitement prime.", "Mettre un objet dans la bouche || Il est dangereux.", "Donner du paracétamol || Il ne traite pas la crise."],
 notions="N23 N12", angle="piège", diff=2, ladder=L("Crise longue.", "État de mal.", "6 minutes.", "Seuil.", "Benzodiazépine.", "Attendre.", "5 minutes = traiter."), sources="[Trinka, Epilepsia, ILAE, 2015]"),
dict(format="A", stem="Une femme de 34 ans fait une première crise focale avec déficit post-critique du bras droit. L'IRM montre un cavernome frontal gauche et l'EEG des pointes à gauche.", prompt="Quelle décision thérapeutique est la plus juste ?",
 items=["*Discuter un antiépileptique dès cette crise, car le risque de récidive est élevé || Une lésion et un EEG anormal suffisent à parler d'épilepsie.", "Attendre une deuxième crise avant tout traitement || La définition ILAE permet de traiter.", "Prescrire une benzodiazépine au long cours || Elle n'est pas un traitement de fond.", "Aucune surveillance, le déficit a régressé || Le risque reste élevé.", "Prescrire un anticoagulant || Rien ne l'indique."],
 notions="N19 N17", angle="application", diff=3, ladder=L("Première crise lésionnelle.", "Risque de récidive.", "Cavernome.", "Définition.", "Traiter.", "Attendre.", "Lésion = épilepsie."), sources="[Fisher, Epilepsia, ILAE, 2014]"),
dict(format="A", stem="Un homme de 25 ans fait une crise généralisée à jeun après une nuit blanche et beaucoup d'alcool. Il récupère complètement. Le bilan est normal.", prompt="Quel délai sans conduite lui recommandez-vous en général pour son permis B ?",
 items=["*3 mois après évaluation spécialisée, si la crise est clairement provoquée || Le délai est plus court qu'après une crise non provoquée.", "Aucun délai || Un délai s'applique.", "2 ans || Il concerne les permis professionnels.", "5 ans || Il concerne le permis D.", "Un retrait définitif || Rien ne le justifie."],
 notions="N20 N21", angle="piège", diff=2, ladder=L("Crise provoquée.", "Conduite.", "Permis B.", "Délai.", "3 mois.", "Aucun délai.", "Provoquée = 3 mois."), sources="[Ligue suisse contre l'épilepsie, 2019]"),
dict(format="A", stem="Une femme de 28 ans a des épisodes d'hémiparésie droite précédés de fourmillements qui migrent lentement sur 20 minutes, puis une céphalée pulsatile. Sa mère a les mêmes épisodes.", prompt="Quel diagnostic évoquez-vous ?",
 items=["*Une migraine hémiplégique || L'aura motrice progressive et l'histoire familiale l'évoquent.", "Un déficit post-critique || Aucune crise ne précède.", "Un AIT || La marche progressive et la récurrence familiale l'excluent probablement.", "Une sclérose en plaques || Les épisodes durent trop peu.", "Une hypoglycémie || Le contexte ne la suggère pas."],
 notions="N09 N14", angle="piège", diff=3, ladder=L("Déficit répété.", "Imitation.", "Marche lente, céphalée.", "Discriminant.", "Migraine hémiplégique.", "Post-critique.", "Marche lente = aura."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 61 ans est vu 20 minutes après une crise focale motrice du bras gauche suivie d'une faiblesse de ce bras.", prompt="Quel élément anamnestique soutient le plus l'origine épileptique du déficit ?",
 items=["*Le témoin a vu des secousses rythmiques du bras gauche avant la faiblesse || La crise motrice précède le déficit.", "Le patient a eu une céphalée la veille || Elle n'oriente pas.", "Le patient fume || C'est un facteur vasculaire.", "Le déficit a commencé brutalement au repos sans prodrome || Il évoque un AVC.", "Le patient est hypertendu || C'est un facteur vasculaire."],
 notions="N04 N05", angle="direct", diff=1, ladder=L("Témoin.", "Anamnèse.", "Secousses.", "Séquence.", "Crise avant déficit.", "Début brutal.", "Le témoin décide."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez la paralysie de Todd.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Elle siège du côté opposé au foyer. || Elle latéralise.", "V: Elle dure plus longtemps après des clonies ou une crise tonico-clonique. || C'est l'observation de Gallmetzer.", "F: Elle laisse en général un déficit séquellaire. || Elle régresse complètement.", "F: Elle exclut la thrombolyse. || L'imagerie décide."],
 notions="N01 N15 N16 N11", angle="direct", diff=2, ladder=L("Révision.", "Caractéristiques.", "Côté, durée.", "Pièges.", "Controlatérale, réversible.", "Séquelle.", "Réversible, latéralisante."), sources="[Gallmetzer, Neurology, 2004]"),
dict(format="Kprim", stem="Un homme de 50 ans arrive 40 minutes après une crise généralisée, encore confus et parétique à droite.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le bilan sanguin comprend glycémie, sodium et calcium. || Ils cherchent une cause provoquée.", "V: L'équipe répète l'examen neurologique jusqu'à récupération. || Elle détecte une aggravation.", "F: Une CK élevée exclut une crise. || Elle la soutient.", "F: L'imagerie est inutile si une crise a été vue. || Le déficit impose l'imagerie."],
 notions="N24 N25 N05 N07", angle="application", diff=2, ladder=L("Après crise.", "Bilan.", "Confus, parétique.", "Examens.", "Biologie, imagerie.", "Pas d'imagerie.", "Bilan + imagerie."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Une équipe d'urgence discute d'un patient de 70 ans avec un déficit après une crise.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un AVC peut débuter par une crise. || La crise est parfois inaugurale.", "V: L'hypoglycémie peut donner crise et déficit focal. || Elle se corrige en minutes.", "F: Un déficit répété du même côté exclut toute lésion. || Il fait chercher une lésion.", "F: Un traitement de fond n'est jamais possible après une seule crise. || Une lésion à haut risque de récidive permet de traiter dès la première crise."],
 notions="N06 N10 N27 N19", angle="piège", diff=2, ladder=L("Discussion d'équipe.", "Pièges.", "Âgé.", "Affirmations.", "AVC inaugural, glucose.", "Pas de lésion.", "Âgé = lésion."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un patient garde une hémiparésie 20 minutes après une crise.", prompt="Quelles affections peuvent imiter ou expliquer ce déficit ? (4 réponses)",
 items=["*AVC ischémique || Il peut débuter par une crise.", "*Hypoglycémie || Elle donne crise et déficit.", "*Migraine hémiplégique || Elle donne un déficit transitoire.", "*État de mal non convulsif || Il prolonge le déficit.", "Céphalée de tension || Elle ne donne pas de déficit.", "Syncope vasovagale || Elle ne donne pas de déficit.", "Névralgie du trijumeau || Elle ne donne pas de déficit.", "Hypothyroïdie fruste || Elle ne donne pas de déficit aigu.", "Lombalgie commune || Elle ne donne pas d'hémiparésie.", "Anémie ferriprive || Elle ne donne pas de déficit.", "Reflux gastro-œsophagien || Il ne donne pas de déficit.", "Tremblement essentiel || Il ne donne pas de déficit."],
 notions="N09 N06 N08", angle="direct", diff=2, ladder=L("Déficit après crise.", "Diagnostics différentiels.", "Hémiparésie.", "Lesquels.", "AVC, glucose, migraine, état de mal.", "Syncope.", "Penser AVC et glucose."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un homme de 52 ans a fait une première crise focale avec déficit post-critique, puis a récupéré.", prompt="Quelles démarches organisez-vous ? (4 réponses)",
 items=["*IRM cérébrale avec protocole épilepsie || Elle cherche une lésion.", "*EEG || Il cherche une activité épileptique.", "*Information écrite sur l'interdiction temporaire de conduire || Elle protège le patient et autrui.", "*Consultation de neurologie || Elle décide du traitement.", "Coronarographie || Rien ne l'indique.", "Anticoagulation empirique || Rien ne l'indique.", "Ponction lombaire systématique || Elle n'est pas systématique sans fièvre.", "Arrêt de travail définitif || Rien ne le justifie.", "Benzodiazépine au long cours || Elle n'est pas un traitement de fond.", "Scintigraphie osseuse || Elle ne répond pas.", "Holter tensionnel || Il ne répond pas.", "Test d'effort || Il ne répond pas."],
 notions="N18 N26 N21 N17", angle="application", diff=2, ladder=L("Après récupération.", "Suivi.", "Première crise focale.", "Démarches.", "IRM, EEG, conduite, neurologue.", "Coronarographie.", "Chercher la cause."), sources="[Ligue suisse contre l'épilepsie, 2019]"),
dict(masque=False, sit="monographique", format="A", stem="Vous enseignez la parésie post-critique à partir d'une étude en vidéo-EEG.", prompt="Quelle proportion de patients avec épilepsie focale présentait une parésie post-critique dans l'étude de Gallmetzer ?",
 items=["*Environ 13 % || L'étude rapporte 13,4 %.", "Environ 1 % || Elle est plus fréquente.", "Environ 50 % || Elle est moins fréquente.", "Environ 90 % || Elle est moins fréquente.", "Aucun patient || Elle était fréquente."],
 notions="N02 N16", angle="direct", diff=3, ladder=L("Chiffre.", "Fréquence.", "Vidéo-EEG.", "Proportion.", "13 %.", "50 %.", "Un patient sur huit."), sources="[Gallmetzer, Neurology, 2004]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Déficit après une crise : traiter d'abord comme un AVC, corriger le glucose, puis reconnaître la parésie post-critique réversible et chercher la lésion qu'elle désigne",
 notions=[
  dict(titre="Reconnaître", rub=["def", "ana", "exa", "bas"], comment="Relie le déficit transitoire à la crise focale qui le précède.",
   tableau=(["Élément", "Caractère", "Pourquoi"], [
     ["Séquence", "Crise motrice puis déficit", "Le témoin la décrit."],
     ["Côté", _T("Opposé au foyer", "La parésie a une forte valeur de latéralisation."), "[Gallmetzer, Neurology, 2004]"],
     ["Durée", _T("Minutes à heures", "Médiane de 173,5 secondes en vidéo-EEG."), "Régression complète"],
     ["Signes associés", "Morsure latérale, confusion", "Ils soutiennent la crise."]]),
   points=["Plus longue après clonies ou crise tonico-clonique."], sources=["[Gallmetzer, Neurology, 2004]"]),
  dict(titre="Écarter le grave", rub=["red", "gold", "pos"], comment="Ne pose le diagnostic qu'après avoir exclu l'AVC et l'hypoglycémie.",
   tableau=(["Diagnostic", "Discriminant", "Examen"], [
     ["AVC inaugural", "Occlusion ou hémorragie", "Scanner et angio-CT"],
     ["Hypoglycémie", "Glycémie basse", "Glycémie capillaire"],
     ["Migraine hémiplégique", "Aura progressive, céphalée", "Anamnèse"],
     ["État de mal non convulsif", "Déficit et confusion qui durent", "EEG"]]),
   points=["Une crise n'exclut pas la thrombolyse si l'imagerie montre une ischémie."], sources=["[Powers, Stroke, AHA/ASA, 2019]"]),
  dict(titre="Agir en urgence", rub=["acu", "hos"], comment="Protège le patient et ne retarde pas la reperfusion.",
   arbre=[("t1", None, "Déficit après crise", "La filière AVC s'active."),
          ("t2", "t1", "Glycémie basse", "Glucose intraveineux.", "todd"),
          ("t3", "t1", "Occlusion à l'imagerie", "Recanalisation selon l'avis neurovasculaire.", "todd"),
          ("t4", "t1", "Imagerie sans lésion aiguë", "Surveillance jusqu'à récupération.", "todd"),
          ("t5", "t1", "Crise ≥ 5 minutes", "Benzodiazépine.", "todd")],
   points=["Position latérale de sécurité, rien dans la bouche."], sources=["[Trinka, Epilepsia, ILAE, 2015]"]),
  dict(titre="Après la récupération", rub=["chr", "pro", "fol"], comment="Cherche la cause et règle la conduite.",
   tableau=(["Étape", "Contenu", "Source"], [
     ["Bilan", "IRM protocole épilepsie, EEG", "[avis d'expert]"],
     ["Traitement", _T("Selon le risque de récidive", "Une crise et un risque ≥ 60 % suffisent à poser l'épilepsie."), "[Fisher, Epilepsia, ILAE, 2014]"],
     ["Conduite privée", "6 mois (3 si provoquée)", "[Ligue suisse contre l'épilepsie, 2019]"],
     ["Conduite C, D1", "2 ans après crise non provoquée", "[Ligue suisse contre l'épilepsie, 2019]"]]),
   points=["Un déficit qui persiste n'est pas un simple post-critique."], sources=["[Ligue suisse contre l'épilepsie, 2019]"]),
 ],
 ssp=dict(code="S7.8", nom="Parésie, paralysie", officiel=True, algorithme=[
  ("n1", None, "Déficit focal aigu", "Il se traite comme un AVC jusqu'à preuve du contraire."),
  ("n2", "n1", "Glycémie capillaire basse", "Hypoglycémie : glucose.", "todd", "c2"),
  ("n3", "n1", "Imagerie : occlusion ou hémorragie", "AVC : filière neurovasculaire.", None, "c2"),
  ("n4", "n1", "Crise vue, imagerie sans lésion aiguë", "Parésie post-critique probable.", "todd", "c1"),
  ("n5", "n4", "Régression complète", "Bilan IRM, EEG, conduite.", "todd", "c4"),
  ("n6", "n4", "Déficit ou confusion prolongés", "EEG : état de mal non convulsif ?", "todd", "c2"),
  ("n7", "n1", "Aura progressive, céphalée", "Migraine hémiplégique.", None, "c2")]),
 pec=[
  dict(cle="todd", titre="Déficit post-critique",
   but=["Ne pas manquer un AVC ni une hypoglycémie.", "Trouver la cause de la crise et prévenir la récidive."],
   moyens=dict(accueil=["Recueillir le récit du témoin.", "Mesurer la glycémie capillaire.", "Placer en position latérale de sécurité si la vigilance baisse."],
    pharma=[("Glucose (soluté hypertonique)", "Dose selon la glycémie ; à vérifier dans l'AIPS.", "Il corrige une hypoglycémie.", "[avis d'expert]"),
            ("Midazolam (benzodiazépine)", "Dose selon le poids et la voie ; à vérifier dans l'AIPS.", "Il arrête une crise qui dure 5 minutes.", "[Trinka, Epilepsia, ILAE, 2015]"),
            ("Antiépileptique de fond (par exemple lévétiracétam)", "Posologie à vérifier dans l'AIPS.", "Il prévient la récidive si le risque est élevé.", "[Fisher, Epilepsia, ILAE, 2014]")],
    nonpharma=[("éducation thérapeutique", "Information sur les facteurs déclenchants.", "Elle limite les crises provoquées."),
               ("social et assurances", "Information écrite sur la conduite.", "Elle protège le patient et autrui.")],
    transversal=[("Neurologie vasculaire", "Elle décide de la reperfusion."), ("Neurologie de l'épilepsie", "Elle pose le diagnostic et le traitement.")]),
   urgence=(["Glycémie capillaire immédiate.", "Imagerie urgente selon la filière AVC."],
            [("d'abord", "ambulancier", "Mesure la glycémie et protège les voies aériennes."),
             ("ensuite", "urgentiste", "Active la filière AVC et demande l'imagerie."),
             ("puis", "neurologue", "Décide de la reperfusion ou de la surveillance.")]),
   horsUrgence=(["Bilan étiologique.", "Conseil de conduite."],
            [("d'abord", "neurologue", "Demande l'IRM protocole épilepsie et l'EEG."),
             ("ensuite", "neurologue", "Estime le risque de récidive et décide du traitement."),
             ("puis", "médecin de famille", "Informe par écrit sur le délai de conduite."),
             ("puis", "médecin de famille", "Suit l'observance et les facteurs déclenchants.")]),
   pronostic="Le déficit régresse complètement ; le pronostic dépend de la cause de la crise.",
   suivi=[("Examen neurologique", "Répété jusqu'à récupération", "Normal"), ("Crises", "À chaque consultation", "Aucune"), ("Conduite", "À la fin du délai", "Reprise autorisée")],
   sortie="Le patient sort après récupération complète, imagerie rassurante et consignes écrites.",
   prevention=["Elle évite privation de sommeil et alcool.", "Elle traite la lésion et prévient la récidive.", "Elle protège contre les accidents de conduite."]),
 ])
AVERIFIER = ["Article de la loi sur la circulation routière qui permet au médecin d'annoncer l'inaptitude (art. 15d LCR probable) à vérifier.", "Durée maximale classique de la parésie post-critique en dehors du vidéo-EEG (souvent citée jusqu'à 36-48 heures) à vérifier.", "Posologies de glucose, midazolam et lévétiracétam à vérifier dans l'AIPS."]
