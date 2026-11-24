ID = "I67.0_dissection_des_arter__F1_12-E12"
PLAN = "monographique"
NOTIONS = [
"def|critère|1||[Debette, ESO, Eur Stroke J, 2021]|La dissection d'une artère cervicale crée un hématome dans la paroi de la carotide interne ou de la vertébrale, qui sténose la lumière ou forme un pseudo-anévrisme.",  # N01
"epi|terrain particulier|2||[Debette, ESO, 2021]|La dissection est une cause majeure d'AVC ischémique chez l'adulte de moins de 50 ans.",  # N02
"bas|mécanisme|1||[Debette, ESO, 2021]|L'AVC résulte surtout d'une embolie à partir du thrombus formé sur la déchirure, plus rarement d'une hypoperfusion.",  # N03
"bas|terrain particulier|1||[avis d'expert]|Un traumatisme mineur, une manipulation cervicale, un effort, une dysplasie fibromusculaire ou une maladie du tissu conjonctif favorisent la dissection.",  # N04
"ana|symptôme|2||[Debette, ESO, 2021]|Une douleur cervicale ou une céphalée unilatérale inhabituelle précède souvent de quelques heures à quelques jours les signes ischémiques.",  # N05
"exa|signe|3||[avis d'expert]|Un syndrome de Claude Bernard-Horner partiel (ptosis et myosis) avec douleur cervicale du même côté évoque une dissection carotidienne.",  # N06
"exa|signe|1||[avis d'expert]|Un acouphène pulsatile ou une paralysie des nerfs crâniens bas, notamment du XII, peuvent révéler une dissection carotidienne.",  # N07
"exa|signe|2||[avis d'expert]|Une dissection vertébrale associe douleur cervicale postérieure ou occipitale et signes de la circulation postérieure, comme vertige et ataxie.",  # N08
"red|piège|2||[avis d'expert]|Une cervicalgie après manipulation ou traumatisme mineur, suivie d'un vertige ou d'un déficit, ne doit pas être prise pour une banale entorse.",  # N09
"gold|examen|3||[Debette, ESO, 2021]|L'angio-CT ou l'IRM cervicale avec séquence T1 à saturation de graisse et angio-IRM confirment la dissection en montrant l'hématome pariétal en croissant.",  # N10
"alt|examen|1||[avis d'expert]|L'échodoppler cervical peut orienter mais ne suffit pas à exclure une dissection, notamment vertébrale ou haute.",  # N11
"pos|diagnostic différentiel|1||[avis d'expert]|Une algie vasculaire de la face donne un Horner transitoire pendant les crises, alors que la dissection donne une douleur continue.",  # N12
"pos|diagnostic différentiel|1||[avis d'expert]|L'hémorragie méningée se cherche si la céphalée est brutale, car une dissection vertébrale intracrânienne peut saigner.",  # N13
"acu|décision|2||[ESO, 2021 ; Debette, 2021]|La présence d'une dissection ne contre-indique pas la thrombolyse intraveineuse d'un AVC dans les délais, ni la thrombectomie d'une occlusion proximale.",  # N14
"acu|molécule|3||[TREAT-CAD, Engelter, Lancet Neurol, 2021 ; CADISS, Lancet Neurol, 2015]|Un antiagrégant ou un anticoagulant se prescrivent pour prévenir l'AVC ; les essais CADISS et TREAT-CAD n'ont pas établi la supériorité claire de l'un sur l'autre.",  # N15
"acu|contexte suisse|1|S|[TREAT-CAD, Engelter, Lancet Neurol, 2021]|L'essai TREAT-CAD, conduit principalement en Suisse, n'a pas montré la non-infériorité de l'aspirine face aux antivitamines K.",  # N16
"acu|piège|2||[Debette, ESO, 2021]|Une dissection intracrânienne avec hémorragie sous-arachnoïdienne contre-indique les antithrombotiques.",  # N17
"hos|complication|1||[avis d'expert]|Le risque de récidive ischémique se concentre dans les premières semaines.",  # N18
"pro|pronostic|1||[Debette, ESO, 2021]|La plupart des dissections recanalisent ou s'améliorent dans les 3 à 6 mois, et la récidive de dissection est rare.",  # N19
"sur|examen|1||[Debette, ESO, 2021]|Une imagerie artérielle de contrôle à 3 à 6 mois guide la durée du traitement antithrombotique.",  # N20
"chr|décision|1||[Debette, ESO, 2021]|Le traitement antithrombotique se poursuit en général 3 à 6 mois, puis un antiagrégant se discute selon l'évolution artérielle.",  # N21
"fol|prévention|1||[avis d'expert]|Le patient évite les manipulations cervicales et les sports à risque de traumatisme cervical pendant la phase de cicatrisation.",  # N22
"fol|décision|1||[avis d'expert]|Des dissections multiples ou récidivantes font chercher une dysplasie fibromusculaire ou une maladie du tissu conjonctif.",  # N23
"hos|complication|1||[Debette, ESO, 2021]|Un pseudo-anévrisme disséquant persiste parfois, mais il se complique rarement et se surveille sans chirurgie systématique.",  # N24
"alt|résultat|1||[avis d'expert]|La dysplasie fibromusculaire donne un aspect en collier de perles des artères cervicales ou rénales à l'imagerie.",  # N25
]
ANGLES = [
"Douleur cervicale + Horner partiel = dissection.",
"La dissection ne contre-indique pas la thrombolyse.",
"Antiagrégant ou anticoagulant : pas de vainqueur clair.",
"Dissection intracrânienne avec HSA : pas d'antithrombotique.",
"IRM T1 fat-sat montre l'hématome en croissant.",
"Contrôle d'imagerie à 3-6 mois.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une femme de 41 ans consulte à Lausanne pour une douleur du côté gauche du cou et de la tempe depuis 4 jours, apparue après une séance de manipulation cervicale. Elle a un ptosis et un myosis gauches, sans autre déficit.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une dissection de la carotide interne gauche || Douleur cervicale et Horner partiel homolatéraux.", "Une algie vasculaire de la face || Elle donne des crises de 15 à 180 minutes.", "Une migraine sans aura || Elle ne donne pas de Horner.", "Une cervicalgie musculaire banale || Elle ne donne pas de Horner.", "Une tumeur de l'apex pulmonaire || Le contexte aigu oriente ailleurs."],
 notions="N06 N05 N04", angle="application", diff=2, ladder=L("Douleur cervicale et Horner.", "Fibres sympathiques péricarotidiennes.", "Manipulation récente.", "Association évocatrice.", "Dissection carotidienne.", "Cervicalgie banale.", "Horner + cou = dissection."), sources="[Debette, ESO, 2021]"),
dict(format="A", serie=("S1", 2, 4), stem="Vous voulez confirmer le diagnostic chez cette femme.", prompt="Quel examen choisissez-vous ?",
 items=["*Un angio-CT ou une IRM cervicale avec T1 à saturation de graisse et angio-IRM || Ils montrent l'hématome pariétal.", "Une radiographie cervicale || Elle ne montre pas l'artère.", "Un EEG || Il n'est pas utile.", "Une ponction lombaire || Elle n'est pas indiquée sans suspicion d'hémorragie.", "Un échodoppler seul pour exclure || Il ne suffit pas à exclure."],
 notions="N10 N11", angle="direct", diff=2, ladder=L("Suspicion de dissection.", "Hématome de paroi.", "Horner.", "Imagerie artérielle.", "Angio-CT ou IRM fat-sat.", "Doppler seul.", "Croissant en T1 fat-sat."), sources="[Debette, ESO, 2021]"),
dict(format="A", serie=("S1", 3, 4), stem="L'IRM confirme une dissection carotidienne interne gauche extracrânienne, sans infarctus ni hémorragie.", prompt="Quel traitement proposez-vous ?",
 items=["*Un antiagrégant ou un anticoagulant, choisi au cas par cas || Les essais n'ont pas établi de supériorité claire.", "Aucun traitement || Le risque d'AVC précoce justifie un antithrombotique.", "Une thrombolyse IV || Elle traite un AVC aigu, absent ici.", "Un stent carotidien d'emblée || Il se réserve aux échecs.", "Des corticoïdes || Ils ne sont pas indiqués."],
 notions="N15 N18", angle="application", diff=3, ladder=L("Dissection non compliquée.", "Embolie à partir du thrombus.", "Pas d'AVC.", "Prévention.", "Antithrombotique.", "Abstention.", "Antiagrégant ou anticoagulant."), sources="[CADISS, 2015 ; TREAT-CAD, 2021]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Vous organisez le suivi de cette femme.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une imagerie de contrôle se fait à 3 à 6 mois. || Elle guide la durée du traitement.", "V: Elle doit éviter les manipulations cervicales. || Elles peuvent aggraver la paroi.", "F: Le risque de récidive de dissection est élevé. || Il est faible.", "F: Le traitement antithrombotique doit être poursuivi à vie à pleine dose. || Il dure en général 3 à 6 mois."],
 notions="N20 N22 N19 N21", angle="direct", diff=2, ladder=L("Suivi.", "Cicatrisation artérielle.", "3-6 mois.", "Calendrier.", "Imagerie, prudence.", "Traitement à vie.", "Contrôle à 3-6 mois."), sources="[Debette, ESO, 2021]"),
dict(format="A", stem="Un homme de 36 ans a fait une chute à vélo il y a 2 jours. Il se plaint d'une douleur occipitale droite et présente depuis 1 heure un vertige, une dysarthrie et une ataxie droite.", prompt="Quelle cause évoquez-vous ?",
 items=["*Une dissection de l'artère vertébrale droite || Douleur occipitale et signes postérieurs après traumatisme.", "Une entorse cervicale simple || Elle ne donne pas de déficit.", "Un VPPB post-traumatique || Il ne donne pas de dysarthrie ni d'ataxie.", "Une commotion cérébrale || Elle ne donne pas de syndrome cérébelleux focal.", "Une migraine vestibulaire || Le contexte et les signes focaux orientent ailleurs."],
 notions="N08 N09 N04", angle="application", diff=2, ladder=L("Douleur occipitale + signes postérieurs.", "Dissection vertébrale.", "Chute récente.", "Piège traumatique.", "Dissection vertébrale.", "Entorse.", "Trauma + vertige + ataxie."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 44 ans présente depuis 90 minutes une aphasie et une hémiparésie droite. L'angio-CT montre une dissection de la carotide interne gauche sans hémorragie.", prompt="Quelle conduite est la plus juste ?",
 items=["*Proposer la thrombolyse IV si les critères sont remplis, car la dissection ne la contre-indique pas || Les recommandations la permettent.", "Contre-indiquer la thrombolyse à cause de la dissection || La dissection n'est pas une contre-indication.", "Attendre 24 heures puis débuter l'aspirine || Le délai de reperfusion serait perdu.", "Faire une ponction lombaire || Elle n'est pas indiquée.", "Donner des corticoïdes || Ils ne sont pas indiqués."],
 notions="N14 N03", angle="piège", diff=3, ladder=L("AVC sur dissection.", "Occlusion embolique.", "90 minutes.", "Reperfusion.", "Thrombolyse permise.", "Contre-indication supposée.", "Dissection ≠ contre-indication."), sources="[ESO, 2021]"),
dict(format="A", stem="Un homme de 48 ans présente une céphalée occipitale brutale. Le scanner montre une hémorragie sous-arachnoïdienne et l'angiographie une dissection de la vertébrale intracrânienne.", prompt="Quelle attitude concernant les antithrombotiques est correcte ?",
 items=["*Ne pas en prescrire, car l'hémorragie les contre-indique || Le risque de resaignement prime.", "Débuter une héparine thérapeutique || Elle aggraverait le saignement.", "Débuter l'aspirine immédiatement || Elle est contre-indiquée ici.", "Associer aspirine et clopidogrel || Le risque hémorragique est majeur.", "Donner une thrombolyse || Elle est contre-indiquée."],
 notions="N17 N13", angle="piège", diff=3, ladder=L("HSA sur dissection.", "Paroi fragile intracrânienne.", "Saignement.", "Contre-indication.", "Pas d'antithrombotique.", "Anticoaguler.", "HSA : pas d'antithrombotique."), sources="[Debette, ESO, 2021]"),
dict(format="A", stem="Un homme de 39 ans se plaint d'un bruit pulsatile dans l'oreille droite et d'une douleur cervicale droite depuis 3 jours. Sa langue dévie à droite en protraction.", prompt="Quel diagnostic devez-vous évoquer ?",
 items=["*Une dissection de la carotide interne droite || Acouphène pulsatile et atteinte du XII homolatéral.", "Un bouchon de cérumen || Il ne donne pas d'atteinte du XII.", "Une otite moyenne || Elle ne donne pas d'atteinte du XII.", "Une SLA bulbaire || Elle évolue lentement sans douleur.", "Une paralysie faciale a frigore || Elle touche le VII."],
 notions="N07 N05", angle="piège", diff=3, ladder=L("Acouphène pulsatile et XII.", "Compression nerveuse par l'hématome.", "Douleur cervicale.", "Signe rare.", "Dissection carotidienne.", "Cause ORL.", "XII + acouphène = dissection."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 35 ans a une troisième dissection artérielle cervicale en 2 ans. Elle a des hématomes faciles et une peau fine.", prompt="Quelle démarche complémentaire est indiquée ?",
 items=["*Chercher une maladie du tissu conjonctif, comme un Ehlers-Danlos vasculaire, ou une dysplasie fibromusculaire || Les dissections multiples l'imposent.", "Aucune démarche, le hasard explique tout || La récidive est rare sans terrain.", "Une biopsie musculaire || Elle n'est pas indiquée.", "Un dosage de la TSH seul || Il n'explique pas les dissections.", "Un EEG || Il n'est pas utile."],
 notions="N23 N04 N25", angle="application", diff=3, ladder=L("Dissections récidivantes.", "Paroi fragile.", "Peau fine, hématomes.", "Terrain.", "Bilan génétique et vasculaire.", "Hasard.", "Récidive = chercher un terrain."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 42 ans a des crises de douleur orbitaire droite de 60 minutes chaque nuit, avec ptosis, larmoiement et rhinorrhée droits, qui disparaissent entre les crises.", prompt="Quel élément le distingue d'une dissection carotidienne ?",
 items=["*Le Horner est transitoire et lié aux crises, avec retour à la normale entre elles || La dissection donne un Horner permanent et une douleur continue.", "Le côté de la douleur || Il est homolatéral dans les deux cas.", "L'âge || Il ne discrimine pas.", "La présence d'un ptosis || Elle existe dans les deux.", "Le sexe masculin || Il ne discrimine pas."],
 notions="N12 N06", angle="piège", diff=2, ladder=L("Horner et douleur orbitaire.", "Céphalée trigémino-autonomique.", "Crises nocturnes.", "Transitoire ou permanent.", "Algie vasculaire.", "Dissection.", "Horner permanent = dissection."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 46 ans traitée par aspirine pour une dissection carotidienne extracrânienne revient à 4 mois. L'angio-IRM montre une recanalisation complète.", prompt="Quelle décision prenez-vous ?",
 items=["*Discuter l'arrêt ou le maintien d'un antiagrégant au long cours selon l'évolution artérielle || Le traitement dure en général 3 à 6 mois.", "Passer à une anticoagulation à vie || Rien ne la justifie.", "Poser un stent || L'artère est recanalisée.", "Répéter l'IRM chaque mois à vie || Elle n'est pas utile.", "Ajouter du clopidogrel || Rien ne le justifie."],
 notions="N21 N20 N19 N24", angle="application", diff=2, ladder=L("Recanalisation.", "Cicatrisation.", "4 mois.", "Durée du traitement.", "Réévaluer l'antiagrégant.", "Anticoagulation à vie.", "Recanalisée : désescalade."), sources="[Debette, ESO, 2021]"),
dict(masque=False, sit="monographique", format="A", stem="Un patient de 38 ans demande pourquoi sa dissection carotidienne a causé un AVC.", prompt="Quelle explication est la plus juste ?",
 items=["*Un thrombus formé sur la déchirure de la paroi a embolisé vers le cerveau || L'embolie est le mécanisme principal.", "La carotide s'est rompue dans le cerveau || La dissection est cervicale.", "La pression artérielle a chuté || L'hypoperfusion est plus rare.", "Le cœur a envoyé un caillot || La cause est artérielle.", "Une infection a gagné le cerveau || Rien ne l'évoque."],
 notions="N03 N01", angle="direct", diff=2, ladder=L("Mécanisme.", "Thrombose sur déchirure.", "Dissection.", "Embolie artério-artérielle.", "Embolie.", "Hypoperfusion.", "Thrombus pariétal embolise."), sources="[Debette, ESO, 2021]"),
dict(masque=False, sit="monographique", format="A", stem="Un médecin de Bâle discute de l'essai TREAT-CAD sur les dissections artérielles cervicales.", prompt="Quel résultat de cet essai est exact ?",
 items=["*L'aspirine n'a pas montré sa non-infériorité face aux antivitamines K || Le critère composite était plus fréquent sous aspirine.", "L'aspirine s'est montrée nettement supérieure || Elle ne l'a pas été.", "Les anticoagulants ont doublé les hémorragies majeures significativement || Ce n'était pas le message principal.", "L'essai a comparé chirurgie et médicament || Il a comparé deux antithrombotiques.", "L'essai a montré qu'aucun traitement n'est utile || Il n'avait pas de bras sans traitement."],
 notions="N16 N15", angle="direct", diff=4, ladder=L("Essai suisse.", "Aspirine contre AVK.", "Non-infériorité.", "Résultat.", "Non-infériorité non montrée.", "Aspirine supérieure.", "TREAT-CAD : pas de non-infériorité."), sources="[Engelter, Lancet Neurol, 2021]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous enseignez à des assistants la dissection des artères cervicales.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Elle est une cause majeure d'AVC chez l'adulte jeune. || Elle domine avant 50 ans.", "V: La douleur précède souvent les signes ischémiques. || Elle alerte précocement.", "F: Un échodoppler normal exclut la dissection. || Il manque les formes hautes et vertébrales.", "F: La thrombolyse est contre-indiquée en cas de dissection. || Elle est permise."],
 notions="N02 N05 N11 N14", angle="piège", diff=2, ladder=L("Enseignement.", "Épidémiologie et pièges.", "Jeune.", "Erreurs fréquentes.", "Reconnaître et traiter.", "Doppler rassurant.", "Jeune + douleur = dissection."), sources="[Debette, ESO, 2021]"),
dict(format="Kprim", stem="Un homme de 33 ans se présente aux urgences de Sion 1 jour après un accident de ski avec une douleur cervicale gauche et un ptosis gauche.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une imagerie artérielle cervicale est indiquée. || Le Horner douloureux évoque une dissection.", "V: Une IRM avec T1 à saturation de graisse montre l'hématome pariétal. || Elle visualise le croissant.", "F: Une radiographie cervicale normale suffit à rassurer. || Elle ne voit pas l'artère.", "F: Il faut attendre l'apparition d'un déficit avant d'imager. || La prévention précède l'AVC."],
 notions="N10 N09 N06", angle="application", diff=2, ladder=L("Trauma, Horner.", "Dissection traumatique.", "Ski.", "Bilan.", "Imagerie artérielle.", "Radiographie.", "Horner douloureux : imager."), sources="[Debette, ESO, 2021]"),
dict(format="Kprim", stem="Une femme de 47 ans traitée pour une dissection vertébrale extracrânienne vous interroge sur son avenir.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La plupart des dissections s'améliorent en 3 à 6 mois. || La paroi cicatrise.", "V: Le risque ischémique est maximal dans les premières semaines. || Le thrombus est récent.", "F: Une seconde dissection est très probable. || Elle est rare.", "F: Les manipulations cervicales sont recommandées pour la douleur. || Elles sont à éviter."],
 notions="N19 N18 N22", angle="direct", diff=2, ladder=L("Pronostic.", "Cicatrisation.", "Vertébrale.", "Information.", "Bon pronostic.", "Récidive fréquente.", "Bon pronostic, pas de manipulation."), sources="[Debette, ESO, 2021]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Une dissection de la carotide interne extracrânienne est suspectée.", prompt="Quels signes cliniques la soutiennent ? (3 réponses)",
 items=["*Ptosis et myosis homolatéraux || Horner partiel.", "*Douleur cervicale ou céphalée unilatérale || Signe d'alerte précoce.", "*Acouphène pulsatile || Flux turbulent.", "Mydriase aréactive || Elle évoque un III.", "Fièvre || Elle évoque une infection.", "Raideur méningée || Elle évoque une méningite.", "Larmoiement en crises de 30 min || Il évoque une algie vasculaire.", "Hémianopsie isolée || Elle relève de l'occipital.", "Diarrhée || Elle n'a aucun lien.", "Éruption cutanée || Elle n'a aucun lien.", "Paresthésies des pieds || Elles évoquent une polyneuropathie.", "Toux || Elle n'a aucun lien."],
 notions="N06 N05 N07", angle="direct", diff=2, ladder=L("Signes.", "Dissection carotidienne.", "Locaux.", "Lesquels.", "Horner, douleur, acouphène.", "III.", "Horner + douleur + acouphène."), sources="[Debette, ESO, 2021]"),
dict(format="MenuLong", stem="Un homme de 34 ans présente un AVC ischémique sans facteur de risque vasculaire.", prompt="Quels facteurs favorisent une dissection cervicale ? (3 réponses)",
 items=["*Manipulation cervicale récente || Elle étire l'artère.", "*Dysplasie fibromusculaire || Elle fragilise la paroi.", "*Syndrome d'Ehlers-Danlos vasculaire || Il fragilise le collagène.", "Hypothyroïdie || Elle n'en fait pas partie.", "Asthme || Il n'en fait pas partie.", "Goutte || Elle n'en fait pas partie.", "Psoriasis || Il n'en fait pas partie.", "Anémie ferriprive || Elle n'en fait pas partie.", "Myopie || Elle n'en fait pas partie.", "Lithiase rénale || Elle n'en fait pas partie.", "Reflux gastro-œsophagien || Il n'en fait pas partie.", "Hypercholestérolémie familiale || Elle favorise l'athérome."],
 notions="N04 N23 N02", angle="application", diff=2, ladder=L("AVC du jeune.", "Paroi fragile.", "Sans facteur de risque.", "Facteurs.", "Manipulation, DFM, EDS.", "Athérome.", "Manipulation + DFM + EDS."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 50 ans a reçu une manipulation cervicale par rotation brusque il y a 3 jours. Il a depuis une douleur cervicale postérieure gauche et, depuis ce matin, un vertige, un hoquet et une hypoesthésie thermo-algique de l'hémiface gauche.", prompt="Quelle artère est le plus probablement lésée ?",
 items=["*L'artère vertébrale gauche || Douleur postérieure et syndrome bulbaire latéral homolatéral.", "La carotide interne gauche || Elle donne des signes hémisphériques.", "La carotide externe gauche || Elle ne vascularise pas le tronc.", "L'artère cérébrale moyenne droite || Le tableau est bulbaire.", "L'artère spinale antérieure || Elle ne donne pas ce tableau facial."],
 notions="N08 N09", angle="direct", diff=2, ladder=L("Douleur postérieure et bulbe.", "Vertébrale disséquée.", "Manipulation.", "Territoire.", "Vertébrale gauche.", "Carotide.", "Occipital + bulbe = vertébrale."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 43 ans arrive 2 heures après une hémiparésie gauche. L'angio-CT montre une dissection carotidienne droite extracrânienne. Le neurologue envisage une thrombolyse.", prompt="Quel élément contre-indiquerait les antithrombotiques ?",
 items=["*Une hémorragie sous-arachnoïdienne sur dissection intracrânienne || Le risque de resaignement prime.", "La dissection extracrânienne elle-même || Elle ne contre-indique pas la reperfusion.", "L'âge de 43 ans || Il n'est pas une contre-indication.", "Une douleur cervicale || Elle est attendue.", "Un ptosis droit || Il est attendu."],
 notions="N17 N14", angle="direct", diff=3, ladder=L("Reperfusion et dissection.", "Contre-indications.", "Extracrânienne.", "Saignement.", "HSA intracrânienne.", "Dissection seule.", "Seule l'HSA contre-indique."), sources="[Debette, ESO, 2021]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Dissection des artères cervicales : reconnaître la douleur unilatérale avec Horner ou signes postérieurs, confirmer par imagerie artérielle, traiter par antithrombotique sauf hémorragie et ne pas priver de thrombolyse",
 notions=[
  dict(titre="Carotide ou vertébrale", rub=["ana", "exa", "red"], comment="Associe la douleur et le territoire des signes.",
   tableau=(["Artère", "Douleur", "Signes locaux", "Signes ischémiques"], [
     ["Carotide interne", "Cervicale antérieure, temporale, orbitaire", _T("Horner partiel, acouphène, XII", "L'hématome comprime le sympathique et les nerfs bas."), "Hémisphériques, amaurose"],
     ["Vertébrale", "Cervicale postérieure, occipitale", _T("Rares", "Les nerfs voisins sont moins exposés."), "Vertige, ataxie, Wallenberg"]]),
   points=["La douleur précède souvent l'ischémie de quelques heures à jours."], sources=["[Debette, ESO, 2021]"]),
  dict(titre="Diagnostic", rub=["gold", "alt", "pos"], comment="Image l'artère et sa paroi, pas seulement le flux.",
   tableau=(["Examen", "Apport", "Limite"], [
     ["Angio-CT", "Sténose effilée, pseudo-anévrisme", [("Rapide", "Il s'intègre à la filière AVC.")]],
     ["IRM T1 fat-sat + angio-IRM", "Hématome pariétal en croissant", [("Paroi", "Elle visualise l'hématome lui-même.")]],
     ["Échodoppler", "Orientation", [("Insuffisant", "Il manque les segments hauts et vertébraux.")]]]),
   points=["Horner transitoire en crises : algie vasculaire."], sources=["[Debette, ESO, 2021]"]),
  dict(titre="Traitement", rub=["acu", "chr"], comment="Préviens l'embolie sauf saignement.",
   arbre=[("t1", None, "Dissection confirmée", "Le risque embolique domine."),
          ("t2", "t1", "AVC aigu dans les délais", "Thrombolyse et thrombectomie permises.", "dis"),
          ("t3", "t1", "Hémorragie sous-arachnoïdienne", "Pas d'antithrombotique.", "dis"),
          ("t4", "t1", "Sans saignement", "Antiagrégant ou anticoagulant 3 à 6 mois.", "dis"),
          ("t5", "t4", "Contrôle à 3-6 mois", "Décide de la suite.", "dis")],
   points=["CADISS et TREAT-CAD n'ont pas désigné de vainqueur clair."], sources=["[CADISS, Lancet Neurol, 2015]", "[Engelter, Lancet Neurol, 2021]"]),
  dict(titre="Pronostic et terrain", rub=["pro", "fol", "bas"], comment="Rassure sur l'évolution et cherche un terrain si les dissections récidivent.",
   tableau=(["Thème", "Message", "Pourquoi"], [
     ["Évolution", "Amélioration en 3-6 mois", "La paroi cicatrise."],
     ["Récidive", "Rare", "Sauf terrain fragile."],
     ["Dissections multiples", "Chercher DFM, Ehlers-Danlos vasculaire", "La paroi est fragile."],
     ["Prévention", "Éviter les manipulations cervicales", "Elles étirent l'artère."]]),
   points=["Risque ischémique maximal les premières semaines."], sources=["[Debette, ESO, 2021]"]),
 ],
 ssp=dict(code="S7.6", nom="Céphalées", officiel=True, algorithme=[
  ("n1", None, "Céphalée ou cervicalgie inhabituelle", "Les signes associés orientent."),
  ("n2", "n1", "Unilatérale avec Horner permanent", "Dissection carotidienne : imagerie artérielle.", "dis", "c1"),
  ("n3", "n1", "Occipitale avec vertige ou ataxie", "Dissection vertébrale : imagerie artérielle.", "dis", "c1"),
  ("n4", "n1", "Brutale en coup de tonnerre", "Hémorragie méningée à exclure (même SSP).", None, "c2"),
  ("n5", "n1", "Crises orbitaires avec Horner transitoire", "Algie vasculaire (même SSP).", None, "c2"),
  ("n6", "n2", "Déficit aigu", "Filière AVC : thrombolyse permise.", "dis", "c3"),
  ("n7", "n2", "Sans déficit", "Antithrombotique 3 à 6 mois.", "dis", "c3"),
  ("n8", "n4", "HSA sur dissection intracrânienne", "Pas d'antithrombotique.", "dis", "c3")]),
 pec=[
  dict(cle="dis", titre="Dissection d'une artère cervicale",
   but=["Prévenir l'AVC embolique.", "Ne pas aggraver un saignement."],
   moyens=dict(accueil=["Examen neurologique et recherche de Horner.", "Angio-CT ou IRM cervicale rapides."],
    pharma=[("Acide acétylsalicylique (antiagrégant)", "Au long cours de la phase aiguë ; à vérifier dans l'AIPS.", "Il prévient l'embolie.", "[Debette, ESO, 2021]"),
            ("Anticoagulant (AVK ou héparine)", "Alternative selon le cas ; à vérifier dans l'AIPS.", "Il prévient l'embolie.", "[CADISS, 2015 ; TREAT-CAD, 2021]"),
            ("Thrombolytique", "Si AVC dans les délais ; à vérifier dans l'AIPS.", "La dissection ne le contre-indique pas.", "[ESO, 2021]")],
    nonpharma=[("éducation thérapeutique", "Éviter manipulations cervicales et sports de contact.", "Elle protège la paroi en cicatrisation."),
               ("geste ou chirurgie", "Thrombectomie si occlusion proximale ; stent en cas d'échec.", "Elle recanalise.")],
    transversal=[("Génétique médicale", "Elle cherche une maladie du tissu conjonctif si récidive.")]),
   urgence=(["Imagerie artérielle.", "Filière AVC si déficit."],
            [("d'abord", "médecin urgentiste", "Évoque la dissection devant douleur et Horner."),
             ("ensuite", "neurologue", "Choisit l'antithrombotique ou la reperfusion."),
             ("puis", "neuroradiologue", "Réalise la thrombectomie si nécessaire.")]),
   horsUrgence=(["Contrôle à 3-6 mois.", "Réévaluation du traitement."],
            [("d'abord", "neurologue", "Ajuste la durée du traitement."),
             ("ensuite", "médecin de famille", "Surveille la tolérance."),
             ("puis", "patient·e", "Évite les manipulations cervicales.")]),
   pronostic="La plupart des dissections cicatrisent en 3 à 6 mois et la récidive est rare.",
   suivi=[("Imagerie artérielle", "3 à 6 mois", "Recanalisation"), ("Signes neurologiques", "À chaque consultation", "Absence"), ("Saignements", "Sous traitement", "Absence")],
   sortie="Le suivi est ambulatoire après exclusion d'un AVC évolutif.",
   prevention=["Elle évite les manipulations cervicales.", "Elle cherche un terrain en cas de récidive.", "Elle informe des signes d'alerte."]),
 ])
AVERIFIER = ["Résultats chiffrés exacts de TREAT-CAD (Engelter, Lancet Neurol, 2021) et de CADISS (Lancet Neurol, 2015) à vérifier.",
             "Durée recommandée du traitement antithrombotique selon ESO 2021 (Debette, Eur Stroke J) à vérifier.",
             "Posologies d'aspirine et d'anticoagulants à vérifier dans l'AIPS."]
