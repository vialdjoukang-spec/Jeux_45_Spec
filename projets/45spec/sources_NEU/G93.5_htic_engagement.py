ID = "G93.5_hypertension_intracr__F1_12-E11"
PLAN = "monographique"
NOTIONS = [
"def|critère|1||[BTF, Carney, Neurosurgery, 2017]|L'hypertension intracrânienne désigne une pression intracrânienne durablement élevée, au-delà d'environ 20 à 22 mmHg chez l'adulte.",  # N01
"bas|mécanisme|3||[avis d'expert]|Selon la doctrine de Monro-Kellie, le volume intracrânien est fixe : une masse ou un œdème élève la pression dès que la compensation par le LCR et le sang veineux est épuisée.",  # N02
"bas|mécanisme|2||[avis d'expert]|La pression de perfusion cérébrale égale la pression artérielle moyenne moins la pression intracrânienne, ce qui explique l'ischémie quand la pression intracrânienne monte.",  # N03
"epi|terrain particulier|1||[avis d'expert]|Les tumeurs, hématomes, abcès, hydrocéphalies, œdèmes post-traumatiques et thromboses veineuses cérébrales sont les causes principales.",  # N04
"ana|symptôme|2||[avis d'expert]|La céphalée matinale ou aggravée en décubitus et à l'effort, les vomissements et les éclipses visuelles orientent vers une hypertension intracrânienne.",  # N05
"exa|signe|1||[avis d'expert]|L'œdème papillaire au fond d'œil signe une hypertension intracrânienne installée, mais son absence ne l'exclut pas en phase aiguë.",  # N06
"exa|signe|2||[avis d'expert]|Une paralysie du VI, uni- ou bilatérale, avec strabisme convergent, est un faux signe de localisation de l'hypertension intracrânienne.",  # N07
"red|signe|3||[avis d'expert]|L'engagement temporal donne une mydriase aréactive homolatérale par compression du III, puis coma et hémiparésie, et impose un geste en minutes.",  # N08
"red|signe|1||[avis d'expert]|La triade de Cushing, avec hypertension artérielle, bradycardie et respiration irrégulière, annonce un engagement imminent.",  # N09
"red|signe|1||[avis d'expert]|L'engagement des amygdales cérébelleuses donne raideur ou torticolis, troubles respiratoires et arrêt respiratoire brutal.",  # N10
"gold|examen|2||[avis d'expert]|Le scanner cérébral en urgence identifie la masse, l'hydrocéphalie ou l'effacement des citernes, et précède toute ponction lombaire.",  # N11
"alt|examen|1||[avis d'expert]|L'IRM précise la cause, et la mesure invasive de la pression intracrânienne guide le traitement en réanimation.",  # N12
"pos|piège|2||[avis d'expert]|Une ponction lombaire en présence d'une masse ou de signes d'engagement peut précipiter l'engagement.",  # N13
"pos|diagnostic différentiel|1||[avis d'expert]|L'hypertension intracrânienne idiopathique touche surtout la jeune femme obèse, avec imagerie normale et pression d'ouverture élevée.",  # N14
"acu|décision|3||[BTF, 2017 ; avis d'expert]|Les mesures de base associent tête surélevée à 30°, cou dans l'axe, normothermie, normocapnie, normoglycémie et natrémie normale ou haute.",  # N15
"acu|molécule|2||[BTF, 2017 ; AIPS Swissmedic]|Le mannitol ou le sérum salé hypertonique réduisent la pression intracrânienne en urgence, posologies à vérifier dans l'AIPS.",  # N16
"acu|piège|2||[BTF, 2017]|L'hyperventilation ne sert que de pont bref avant un geste, car l'hypocapnie prolongée provoque une ischémie cérébrale.",  # N17
"acu|molécule|2||[CRASH, Lancet, 2004 ; avis d'expert]|La dexaméthasone réduit l'œdème vasogénique des tumeurs, mais elle est délétère dans le traumatisme crânien.",  # N18
"acu|décision|1||[avis d'expert]|La dérivation ventriculaire externe, l'évacuation d'une masse ou la craniectomie décompressive traitent la cause mécanique.",  # N19
"hos|complication|1||[avis d'expert]|L'hypertension intracrânienne non contrôlée aboutit à l'ischémie globale puis à la mort encéphalique.",  # N20
"pro|pronostic|1||[avis d'expert]|Le pronostic dépend de la cause et de la rapidité de la décompression.",  # N21
"sur|décision|1||[avis d'expert]|La surveillance répète le Glasgow, la taille et la réactivité des pupilles, et la pression intracrânienne si elle est mesurée.",  # N22
"chr|décision|1||[avis d'expert]|En situation palliative tumorale, la dexaméthasone, les antalgiques et les antiémétiques soulagent les céphalées de l'hypertension intracrânienne chronique.",  # N23
"fol|décision|1||[avis d'expert]|Chez l'enfant, un strabisme convergent récent avec céphalées et vomissements matinaux impose une imagerie cérébrale rapide.",  # N24
"fol|contexte suisse|1|S|[ASSM, directives anticipées]|En situation palliative, les directives anticipées et le représentant thérapeutique guident l'intensité des soins.",  # N25
]
ANGLES = [
"Mydriase aréactive = engagement temporal.",
"VI : faux signe de localisation.",
"Scanner avant ponction lombaire.",
"Hyperventilation : pont bref seulement.",
"Corticoïdes : tumeur oui, trauma non.",
"Tête à 30°, normocapnie.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une femme de 56 ans consulte à Lausanne pour des céphalées depuis 3 semaines, plus fortes au réveil, avec des vomissements matinaux et des voiles visuels brefs en se penchant.", prompt="Quel examen du fond d'œil attendez-vous ?",
 items=["*Un œdème papillaire bilatéral || Il signe une hypertension intracrânienne installée.", "Une rétinopathie diabétique || Rien ne l'oriente.", "Une excavation papillaire glaucomateuse || Elle ne donne pas ce tableau.", "Une occlusion de l'artère centrale || Elle est brutale et unilatérale.", "Un fond d'œil toujours normal || L'œdème est attendu après 3 semaines."],
 notions="N06 N05", angle="application", diff=2, ladder=L("Céphalée matinale.", "Pression transmise à la gaine optique.", "Éclipses visuelles.", "Fond d'œil.", "Œdème papillaire.", "Normal.", "Matin + vomissements + papille."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 2, 4), stem="Le fond d'œil de cette femme montre un œdème papillaire bilatéral.", prompt="Quel examen demandez-vous en premier ?",
 items=["*Un scanner ou une IRM cérébrale en urgence || L'imagerie cherche la cause et précède toute PL.", "Une ponction lombaire immédiate || Elle peut précipiter un engagement.", "Un EEG || Il ne cherche pas la cause.", "Un champ visuel seul || Il ne cherche pas la cause.", "Une échographie des carotides || Elle n'explique pas le tableau."],
 notions="N11 N13", angle="direct", diff=2, ladder=L("Œdème papillaire.", "Masse possible.", "Urgence.", "Ordre des examens.", "Imagerie d'abord.", "PL d'abord.", "Image avant PL."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 3, 4), stem="L'IRM montre une tumeur frontale de 5 cm entourée d'un œdème vasogénique important avec effet de masse.", prompt="Quel traitement réduit l'œdème en attendant la neurochirurgie ?",
 items=["*La dexaméthasone || Elle réduit l'œdème vasogénique tumoral.", "Le furosémide seul || Il est peu efficace sur l'œdème tumoral.", "L'hyperventilation prolongée || Elle provoque une ischémie.", "L'acétazolamide || Il sert l'HTIC idiopathique.", "Le paracétamol seul || Il ne réduit pas l'œdème."],
 notions="N18 N04", angle="application", diff=2, ladder=L("Œdème tumoral.", "Rupture de la barrière.", "Effet de masse.", "Traitement d'attente.", "Dexaméthasone.", "Hyperventilation.", "Tumeur : corticoïde."), sources="[avis d'expert]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="La neurochirurgie de cette femme est programmée dans 48 heures.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La tête du lit se surélève à 30°. || Le retour veineux s'améliore.", "V: Une mydriase aréactive impose une réévaluation immédiate. || Elle signe un engagement.", "F: Une hypotonie salée par perfusion de glucosé 5 % est sans risque. || L'hyponatrémie aggrave l'œdème.", "F: La surveillance des pupilles est inutile sous dexaméthasone. || L'engagement reste possible."],
 notions="N15 N22 N08", angle="direct", diff=2, ladder=L("Attente chirurgicale.", "Prévenir l'engagement.", "48 heures.", "Surveillance.", "30°, pupilles.", "Glucosé, relâchement.", "Pupilles + 30°."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 68 ans sous anticoagulant est surveillé pour un hématome sous-dural. Il devient somnolent, sa pupille droite se dilate et ne réagit plus, et il présente une hémiparésie gauche.", prompt="Que se passe-t-il ?",
 items=["*Un engagement temporal droit || Mydriase aréactive homolatérale, coma, hémiparésie controlatérale.", "Une crise épileptique simple || Elle n'explique pas la mydriase aréactive.", "Une intoxication aux opiacés || Elle donne un myosis.", "Un AVC du tronc isolé || L'hématome connu explique l'engagement.", "Une hypoglycémie || Elle ne donne pas de mydriase unilatérale."],
 notions="N08 N02", angle="application", diff=2, ladder=L("Mydriase et somnolence.", "Uncus sur le III.", "Hématome connu.", "Engagement.", "Temporal droit.", "Crise.", "Mydriase aréactive = engagement."), sources="[avis d'expert]"),
dict(format="A", stem="Chez cet homme en engagement temporal, la neurochirurgie arrive dans 20 minutes.", prompt="Quelle mesure temporaire est adaptée ?",
 items=["*Une osmothérapie par mannitol ou sérum salé hypertonique, tête à 30° || Elle baisse la pression en minutes.", "Une ponction lombaire évacuatrice || Elle aggraverait l'engagement.", "Une hyperventilation prolongée pendant 24 heures || Elle provoque une ischémie.", "Un remplissage par glucosé 5 % || Il aggrave l'œdème.", "Une attente sans traitement || Le délai est vital."],
 notions="N16 N15 N17", angle="application", diff=3, ladder=L("Engagement.", "Réduire le volume.", "20 minutes.", "Pont.", "Osmothérapie.", "PL.", "Mannitol/NaCl hypertonique."), sources="[BTF, 2017]"),
dict(format="A", stem="Un garçon de 7 ans présente depuis 3 semaines des céphalées et des vomissements au réveil. Ses parents remarquent qu'il louche vers l'intérieur depuis quelques jours et qu'il est maladroit.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Une imagerie cérébrale rapide || Le VI et les signes d'HTIC évoquent une tumeur de la fosse postérieure.", "Une correction optique seule || Le strabisme est neurologique.", "Une rééducation orthoptique || Elle retarde le diagnostic.", "Un antiémétique et une réévaluation dans 1 mois || Le délai est dangereux.", "Un test d'allergie alimentaire || Rien ne l'oriente."],
 notions="N24 N07", angle="application", diff=2, ladder=L("Strabisme et vomissements.", "Masse de la fosse postérieure.", "Ataxie.", "Faux signe du VI.", "Imagerie.", "Lunettes.", "Enfant + VI + matin = image."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 46 ans a une paralysie bilatérale du VI avec céphalée et vomissements. L'IRM montre une hydrocéphalie sans lésion du tronc.", prompt="Comment interprétez-vous l'atteinte du VI ?",
 items=["*Comme un faux signe de localisation lié à l'hypertension intracrânienne || Le long trajet du VI le rend vulnérable.", "Comme une lésion du noyau du VI || L'IRM ne la montre pas.", "Comme une myasthénie oculaire || Le contexte oriente vers l'HTIC.", "Comme un diabète || Rien ne l'oriente.", "Comme un strabisme congénital || Il est récent."],
 notions="N07 N02 N05", angle="direct", diff=3, ladder=L("VI bilatéral.", "Étirement du nerf.", "Hydrocéphalie.", "Interprétation.", "Faux signe de localisation.", "Lésion nucléaire.", "VI = faux signe."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 30 ans victime d'un traumatisme crânien grave est en réanimation à Berne. La PA est à 190/100 mmHg, la fréquence cardiaque à 45/min et la respiration irrégulière.", prompt="Que signifie cette association ?",
 items=["*Une triade de Cushing annonçant un engagement imminent || La pression intracrânienne menace le tronc.", "Une douleur mal contrôlée || La bradycardie l'exclut.", "Un sepsis || Il donne une tachycardie.", "Une hypovolémie || Elle donne une tachycardie et une hypotension.", "Un sevrage alcoolique || Il donne une tachycardie."],
 notions="N09 N03", angle="direct", diff=2, ladder=L("HTA, bradycardie.", "Réflexe de perfusion.", "Trauma.", "Signe tardif.", "Cushing.", "Douleur.", "HTA + bradycardie = engagement."), sources="[avis d'expert]"),
dict(format="A", stem="Le même homme est intubé. Un collègue propose de baisser la PaCO2 à 25 mmHg pendant 48 heures pour contrôler la pression intracrânienne.", prompt="Quelle remarque est la plus juste ?",
 items=["*L'hyperventilation ne sert que de pont bref, car l'hypocapnie prolongée provoque une ischémie || La vasoconstriction réduit la perfusion.", "C'est le traitement de référence au long cours || Elle est délétère prolongée.", "Il faut viser une PaCO2 de 15 mmHg || L'ischémie serait majeure.", "La PaCO2 n'influence pas la pression intracrânienne || Elle module le volume sanguin.", "Il faut associer une ponction lombaire || Elle est contre-indiquée."],
 notions="N17 N03", angle="piège", diff=3, ladder=L("Hyperventilation.", "Vasoconstriction.", "48 heures.", "Effet délétère.", "Pont bref.", "Prolonger.", "Hypocapnie brève."), sources="[BTF, 2017]"),
dict(format="A", stem="Un homme de 45 ans victime d'un traumatisme crânien a un œdème cérébral diffus. Un interne propose de la méthylprednisolone à forte dose.", prompt="Quelle réponse donnez-vous ?",
 items=["*Les corticoïdes sont délétères dans le traumatisme crânien et ne s'utilisent pas || L'essai CRASH a montré une surmortalité.", "Ils sont indiqués comme dans les tumeurs || L'œdème traumatique diffère.", "Ils réduisent la mortalité de moitié || L'essai CRASH montre l'inverse.", "Ils remplacent l'osmothérapie || Ils ne sont pas indiqués.", "Ils sont indiqués seulement chez le sujet jeune || Ils ne sont pas indiqués."],
 notions="N18", angle="piège", diff=3, ladder=L("Corticoïdes et trauma.", "Œdème cytotoxique.", "Trauma.", "Preuve.", "Non.", "Comme les tumeurs.", "CRASH : pas de corticoïdes."), sources="[CRASH, Lancet, 2004]"),
dict(format="A", stem="Une femme de 25 ans, obèse, se plaint de céphalées et d'éclipses visuelles. Elle a un œdème papillaire bilatéral. L'IRM et la veinographie sont normales et la pression d'ouverture à la ponction lombaire est élevée.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Une hypertension intracrânienne idiopathique || Imagerie normale et pression élevée chez une jeune femme obèse.", "Une tumeur cérébrale || L'IRM est normale.", "Une thrombose veineuse cérébrale || La veinographie est normale.", "Une migraine chronique || Elle ne donne pas d'œdème papillaire.", "Une méningite || Rien ne l'oriente."],
 notions="N14 N06", angle="piège", diff=2, ladder=L("HTIC à imagerie normale.", "Mécanisme idiopathique.", "Jeune femme obèse.", "Exclusion.", "HTIC idiopathique.", "Tumeur.", "IRM normale + PL haute."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 62 ans atteint d'un glioblastome en soins palliatifs à domicile souffre de céphalées et de vomissements matinaux. Il a rédigé des directives anticipées refusant toute réanimation.", prompt="Quelle prise en charge est la plus adaptée ?",
 items=["*Dexaméthasone, antalgiques et antiémétiques selon ses directives anticipées || Ils soulagent l'hypertension intracrânienne chronique.", "Hospitalisation en réanimation pour mesure invasive || Elle contredit ses directives.", "Ponction lombaire évacuatrice || Elle expose à l'engagement.", "Arrêt de tout traitement symptomatique || Les symptômes se soulagent.", "Hyperventilation à domicile || Elle n'a pas de sens."],
 notions="N23 N25", angle="application", diff=2, ladder=L("HTIC palliative.", "Œdème tumoral.", "Directives anticipées.", "Confort.", "Corticoïde, symptomatiques.", "Réanimation.", "Palliatif : soulager."), sources="[ASSM ; avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Une PAM de 80 mmHg et une pression intracrânienne de 30 mmHg sont mesurées chez un patient en réanimation.", prompt="Quelle est la pression de perfusion cérébrale ?",
 items=["*50 mmHg || PPC = PAM − PIC.", "110 mmHg || Les valeurs ne s'additionnent pas.", "80 mmHg || La PIC doit être soustraite.", "30 mmHg || C'est la PIC.", "2,7 mmHg || Les valeurs ne se divisent pas."],
 notions="N03 N01", angle="direct", diff=2, ladder=L("Calcul.", "PPC = PAM − PIC.", "80 et 30.", "Formule.", "50 mmHg.", "Addition.", "PAM − PIC."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous enseignez la physiopathologie de l'hypertension intracrânienne.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le volume intracrânien total est fixe chez l'adulte. || C'est la doctrine de Monro-Kellie.", "V: Le LCR et le sang veineux compensent d'abord une masse. || Puis la compensation s'épuise.", "F: La pression monte de façon linéaire avec le volume. || La courbe devient brutalement exponentielle.", "F: Une pression intracrânienne élevée augmente la perfusion cérébrale. || Elle la réduit."],
 notions="N02 N03", angle="direct", diff=2, ladder=L("Physiopathologie.", "Monro-Kellie.", "Compensation.", "Courbe.", "Volume fixe, compensation.", "Linéarité.", "Compensation puis décompensation."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un patient présente des signes d'hypertension intracrânienne aiguë aux urgences de Genève.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le cou se garde dans l'axe. || Le retour veineux jugulaire reste libre.", "V: La fièvre se traite. || Elle augmente le métabolisme cérébral.", "V: Une dérivation ventriculaire traite une hydrocéphalie aiguë. || Elle draine le LCR.", "F: Une hyponatrémie est sans conséquence. || Elle aggrave l'œdème."],
 notions="N15 N19", angle="application", diff=2, ladder=L("HTIC aiguë.", "Mesures de base.", "Urgences.", "Physiologie.", "Axe, normothermie, DVE.", "Hyponatrémie.", "Axe + 37 °C + Na."), sources="[BTF, 2017]"),
dict(format="Kprim", stem="Une femme de 70 ans a une hémorragie cérébelleuse. Elle se plaint de torticolis puis présente des pauses respiratoires.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un engagement des amygdales cérébelleuses est à craindre. || Le torticolis et les pauses l'annoncent.", "V: Un arrêt respiratoire brutal peut survenir. || Le bulbe est comprimé.", "F: Une ponction lombaire est indiquée pour décomprimer. || Elle précipiterait l'engagement.", "F: Le torticolis est sans valeur. || Il peut signer l'engagement."],
 notions="N10 N13", angle="piège", diff=3, ladder=L("Fosse postérieure.", "Engagement amygdalien.", "Torticolis, apnées.", "Risque.", "Arrêt respiratoire.", "PL.", "Torticolis + apnée = amygdales."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un patient présente une hypertension intracrânienne aiguë.", prompt="Quelles mesures sont recommandées ? (3 réponses)",
 items=["*Tête surélevée à 30° || Elle favorise le retour veineux.", "*Normocapnie || Elle évite l'ischémie et la vasodilatation.", "*Osmothérapie si signes d'engagement || Elle baisse la pression.", "Glucosé 5 % en perfusion libre || Il aggrave l'œdème.", "Hyperventilation prolongée || Elle provoque une ischémie.", "Ponction lombaire évacuatrice || Elle peut engager.", "Corticoïdes dans le traumatisme || Ils sont délétères.", "Hyperthermie tolérée || Elle aggrave.", "Collier cervical serré || Il gêne le retour veineux.", "Décubitus strict à plat || Il gêne le retour veineux.", "Hypotension permissive || Elle réduit la perfusion.", "Hyponatrémie tolérée || Elle aggrave l'œdème."],
 notions="N15 N16 N17", angle="direct", diff=2, ladder=L("HTIC.", "Mesures.", "Aiguë.", "Lesquelles.", "30°, CO2, osmose.", "PL.", "30° + normocapnie + osmothérapie."), sources="[BTF, 2017]"),
dict(format="MenuLong", stem="Un homme de 50 ans a un hématome intracrânien et devient somnolent.", prompt="Quels signes annoncent un engagement ? (3 réponses)",
 items=["*Mydriase aréactive unilatérale || Compression du III.", "*Bradycardie avec hypertension || Triade de Cushing.", "*Respiration irrégulière || Atteinte du tronc.", "Myosis bilatéral réactif || Il n'est pas spécifique.", "Tachycardie isolée || Elle n'est pas spécifique.", "Fièvre || Elle n'est pas spécifique.", "Diarrhée || Elle n'a aucun lien.", "Éruption || Elle n'a aucun lien.", "Toux || Elle n'a aucun lien.", "Paresthésies des pieds || Elles n'ont aucun lien.", "Prurit || Il n'a aucun lien.", "Douleur abdominale || Elle n'a aucun lien."],
 notions="N08 N09", angle="application", diff=2, ladder=L("Somnolence.", "Engagement.", "Hématome.", "Signes.", "Mydriase, Cushing.", "Signes non spécifiques.", "Pupille + Cushing."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 38 ans présente des céphalées progressives depuis 1 semaine, des vomissements et une crise convulsive. Elle prend une contraception œstroprogestative. Le scanner sans injection montre un infarctus hémorragique pariétal.", prompt="Quelle cause d'hypertension intracrânienne cherchez-vous ?",
 items=["*Une thrombose veineuse cérébrale par angio-CT ou IRM veineuse || Le contexte et l'infarctus hémorragique l'évoquent.", "Une hypertension intracrânienne idiopathique || L'imagerie n'est pas normale.", "Une migraine || La crise et l'infarctus orientent ailleurs.", "Une méningite || Rien ne l'oriente.", "Une tumeur hypophysaire || Rien ne l'oriente."],
 notions="N04 N12 N11", angle="application", diff=3, ladder=L("HTIC et infarctus hémorragique.", "Gêne au drainage veineux.", "Contraception.", "Cause veineuse.", "TVC.", "HTIC idiopathique.", "Œstrogène + hémorragie : veines."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Hypertension intracrânienne secondaire : reconnaître céphalée matinale, papille et VI, guetter l'engagement, imager avant toute ponction lombaire et décomprimer par mesures de base, osmothérapie et geste",
 notions=[
  dict(titre="Physiopathologie", rub=["bas", "def"], comment="Raisonne en volumes et en perfusion.",
   tableau=(["Notion", "Contenu", "Conséquence"], [
     ["Monro-Kellie", "Volume fixe : cerveau, sang, LCR", _T("Décompensation brutale", "La courbe pression-volume devient exponentielle.")],
     ["PPC", "PAM − PIC", _T("Ischémie", "Une PIC haute réduit la perfusion.")],
     ["Seuil", "PIC > 20-22 mmHg", _T("Traitement", "Il se déclenche au-delà.")]]),
   points=["Tumeur, hématome, abcès, hydrocéphalie, TVC."], sources=["[BTF, 2017]"]),
  dict(titre="Signes et engagements", rub=["ana", "exa", "red"], comment="Reconnais l'engagement avant le coma.",
   tableau=(["Tableau", "Signes", "Pourquoi"], [
     ["HTIC installée", "Céphalée matinale, vomissements, papille", [("Décubitus", "La pression monte la nuit.")]],
     ["Faux signe", "VI uni- ou bilatéral", [("Long trajet", "Le nerf s'étire sur la pointe du rocher.")]],
     ["Engagement temporal", "Mydriase aréactive homolatérale, coma, hémiparésie", [("III", "L'uncus le comprime.")]],
     ["Engagement amygdalien", "Torticolis, apnées", [("Bulbe", "Il est comprimé dans le foramen magnum.")]],
     ["Cushing", "HTA, bradycardie, respiration irrégulière", [("Tardif", "Il annonce l'engagement.")]]]),
   points=["L'absence de papille n'exclut pas l'HTIC aiguë."], sources=["[avis d'expert]"]),
  dict(titre="Traitement", rub=["acu", "gold"], comment="Image d'abord, puis applique l'escalade.",
   arbre=[("t1", None, "HTIC suspectée", "Le scanner précède toute PL."),
          ("t2", "t1", "Mesures de base", "Tête 30°, cou dans l'axe, normothermie, normocapnie, Na normal.", "htic"),
          ("t3", "t2", "Signes d'engagement", "Mannitol ou NaCl hypertonique.", "htic"),
          ("t4", "t3", "Pont bref", "Hyperventilation courte jusqu'au geste.", "htic"),
          ("t5", "t3", "Geste", "DVE, évacuation, craniectomie.", "htic"),
          ("t6", "t2", "Œdème tumoral", "Dexaméthasone ; jamais dans le trauma.", "htic")],
   points=["Posologies à vérifier dans l'AIPS."], sources=["[BTF, 2017]", "[CRASH, Lancet, 2004]"]),
  dict(titre="Situations particulières", rub=["pos", "chr", "fol"], comment="Adapte la démarche au terrain.",
   tableau=(["Situation", "Conduite", "Pourquoi"], [
     ["Enfant avec VI et vomissements", "Imagerie rapide", "Une tumeur de fosse postérieure est possible."],
     ["Jeune femme obèse, imagerie normale", "PL : HTIC idiopathique", "L'imagerie a exclu une masse."],
     ["Œstrogènes, infarctus hémorragique", "Imagerie veineuse", "Une TVC est possible."],
     ["Palliatif tumoral", [("Dexaméthasone, symptomatiques", "Les directives anticipées guident.")], "Le confort prime."]]),
   points=["Surveillance pupilles et Glasgow."], sources=["[ASSM]"]),
 ],
 ssp=dict(code="S7.6", nom="Céphalées", officiel=True, algorithme=[
  ("n1", None, "Céphalée", "Le profil temporel oriente."),
  ("n2", "n1", "Matinale, progressive, vomissements", "HTIC : fond d'œil et imagerie.", None, "c2"),
  ("n3", "n2", "Masse, hématome, hydrocéphalie", "HTIC secondaire.", "htic", "c3"),
  ("n4", "n2", "Imagerie normale, jeune femme obèse", "HTIC idiopathique (même SSP).", None, "c4"),
  ("n5", "n2", "Infarctus hémorragique, œstrogènes", "TVC : imagerie veineuse.", None, "c4"),
  ("n6", "n3", "Mydriase aréactive ou Cushing", "Engagement : osmothérapie et geste.", "htic", "c2"),
  ("n7", "n1", "Brutale", "Hémorragie méningée (même SSP).", None, "c2"),
  ("n8", "n1", "Épisodique sans drapeau rouge", "Céphalée primaire (même SSP).", None, "c2")]),
 pec=[
  dict(cle="htic", titre="Hypertension intracrânienne secondaire",
   but=["Préserver la perfusion cérébrale.", "Traiter la cause mécanique."],
   moyens=dict(accueil=["Glasgow et pupilles.", "Scanner cérébral avant toute PL."],
    pharma=[("Mannitol (osmotique)", "En bolus ; à vérifier dans l'AIPS.", "Il retire l'eau du cerveau.", "[BTF, 2017]"),
            ("NaCl hypertonique", "En bolus ; à vérifier dans l'AIPS.", "Il crée un gradient osmotique.", "[BTF, 2017]"),
            ("Dexaméthasone (corticoïde)", "Œdème tumoral seulement ; à vérifier dans l'AIPS.", "Elle réduit l'œdème vasogénique.", "[avis d'expert]")],
    nonpharma=[("soins infirmiers", "Tête 30°, cou dans l'axe, normothermie.", "Ils facilitent le retour veineux."),
               ("geste ou chirurgie", "DVE, évacuation, craniectomie.", "Ils lèvent la cause mécanique.")],
    transversal=[("Neurochirurgie", "Elle décide du geste."), ("Soins palliatifs", "Ils soulagent l'HTIC tumorale terminale.")]),
   urgence=(["Scanner immédiat.", "Osmothérapie si signes d'engagement."],
            [("d'abord", "médecin urgentiste", "Reconnaît l'engagement et sécurise les voies aériennes."),
             ("en même temps", "infirmier·ère", "Surélève la tête et surveille pupilles et Glasgow."),
             ("ensuite", "neurochirurgien·ne", "Draine ou décomprime."),
             ("puis", "intensiviste", "Contrôle PIC, PPC, CO2 et natrémie.")]),
   horsUrgence=(["Traitement de la cause.", "Surveillance neurologique."],
            [("d'abord", "neurologue ou neurochirurgien·ne", "Traite la cause."),
             ("ensuite", "médecin de famille", "Repère toute récidive des symptômes."),
             ("puis", "patient·e", "Consulte en urgence si céphalée, vomissements ou somnolence réapparaissent.")]),
   pronostic="Le pronostic dépend de la cause et de la rapidité de la décompression.",
   suivi=[("Glasgow et pupilles", "Horaire", "Stables"), ("PIC si mesurée", "Continue", "< 22 mmHg"), ("Natrémie", "Pluriquotidienne", "Normale ou haute")],
   sortie="La sortie suit le traitement de la cause et la stabilité neurologique.",
   prevention=["Elle impose l'imagerie avant toute PL.", "Elle évite les solutés hypotoniques.", "Elle traite tôt les causes connues."]),
 ])
AVERIFIER = ["Seuil de traitement de la PIC (22 mmHg selon BTF 2016/2017) à vérifier.",
             "Doses de mannitol, de NaCl hypertonique et de dexaméthasone à vérifier dans l'AIPS."]
