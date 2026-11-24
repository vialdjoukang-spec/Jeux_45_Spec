ID = "G31.8__F1_9-E06"
PLAN = "monographique"
NOTIONS = [
"def|critère|1||[McKeith, DLB Consortium, Neurology, 2017]|On parle de démence à corps de Lewy quand la démence précède le parkinsonisme ou survient dans l'année ; au-delà, on parle de démence de la maladie de Parkinson.",  # N01
"epi|chiffre|1||[avis d'expert]|Elle compte parmi les démences neurodégénératives les plus fréquentes après la maladie d'Alzheimer.",  # N02
"bas|mécanisme|1||[avis d'expert]|Des corps de Lewy faits d'alpha-synucléine envahissent cortex et tronc cérébral ; le déficit cholinergique profond explique la bonne réponse aux anticholinestérasiques.",  # N03
"ana|critère|3||[McKeith, DLB Consortium, Neurology, 2017]|Les quatre signes cardinaux sont les fluctuations de l'attention, les hallucinations visuelles récurrentes et détaillées, le trouble comportemental en sommeil paradoxal et le parkinsonisme.",  # N04
"ana|symptôme|2||[McKeith, DLB Consortium, Neurology, 2017]|Les troubles de l'attention, exécutifs et visuospatiaux dominent au début, alors que la mémoire est d'abord relativement préservée.",  # N05
"ana|signe|1||[McKeith, DLB Consortium, Neurology, 2017]|Les signes évocateurs comprennent dysautonomie, chutes, syncopes, hypersomnie, hyposmie, idées délirantes et dépression.",  # N06
"exa|signe|1||[avis d'expert]|Les tests échouent à la copie des pentagones et aux épreuves exécutives ; le parkinsonisme est souvent symétrique et axial, avec peu de tremblement.",  # N07
"red|piège|3||[McKeith, DLB Consortium, Neurology, 2017]|Une hypersensibilité sévère aux neuroleptiques peut provoquer rigidité aiguë, confusion et décès ; l'halopéridol s'évite.",  # N08
"gold|critère|2||[McKeith, DLB Consortium, Neurology, 2017]|Le diagnostic est probable avec au moins deux signes cardinaux, ou un signe cardinal et au moins un biomarqueur indicatif.",  # N09
"gold|examen|2||[McKeith, DLB Consortium, Neurology, 2017]|Les biomarqueurs indicatifs sont une captation réduite des transporteurs de la dopamine (DaTSCAN), une scintigraphie cardiaque au MIBG abaissée et un sommeil paradoxal sans atonie en polysomnographie.",  # N10
"alt|examen|1||[McKeith, DLB Consortium, Neurology, 2017]|L'IRM préserve relativement les lobes temporaux médians, et l'EEG montre des ondes lentes postérieures.",  # N11
"pos|diagnostic différentiel|2||[avis d'expert]|La maladie d'Alzheimer commence par la mémoire avec atrophie hippocampique ; la démence parkinsonienne suit un parkinsonisme de plus d'un an ; le delirium a une cause aiguë.",  # N12
"pos|diagnostic différentiel|1||[avis d'expert]|Devant une aggravation brutale, un delirium (infection, médicament, trouble métabolique) se cherche d'abord.",  # N13
"acu|décision|2||[McKeith, DLB Consortium, Neurology, 2017]|Devant des hallucinations, on cherche un déclencheur et on réduit les anticholinergiques ; si elles gênent, un anticholinestérasique précède la quétiapine ou la clozapine à faible dose.",  # N14
"chr|molécule|3||[McKeith, DLB Consortium, Neurology, 2017]|Les anticholinestérasiques (rivastigmine, donépézil) améliorent la cognition, les fluctuations et les hallucinations.",  # N15
"chr|posologie|1||[AIPS Swissmedic]|La rivastigmine se titre par paliers, orale ou en patch ; elle donne nausées et bradycardie ; indication et doses suisses à vérifier dans l'AIPS.",  # N16
"chr|molécule|2||[McKeith, DLB Consortium, Neurology, 2017]|La lévodopa à la plus faible dose utile traite un parkinsonisme gênant ; elle peut aggraver les hallucinations, et les agonistes dopaminergiques s'évitent.",  # N17
"chr|molécule|1||[avis d'expert]|Le trouble comportemental en sommeil paradoxal se traite par sécurisation de la chambre, mélatonine ou clonazépam prudent.",  # N18
"hos|complication|2||[avis d'expert]|Les chutes, l'hypotension orthostatique et les pneumonies d'aspiration compliquent l'évolution ; les anticholinergiques aggravent la confusion.",  # N19
"pro|pronostic|1||[avis d'expert]|L'évolution est souvent plus rapide et plus émaillée d'hospitalisations que celle de la maladie d'Alzheimer.",  # N20
"sur|examen|1||[avis d'expert]|Le suivi surveille cognition, chutes, tension couchée-debout, poids, déglutition et épuisement de l'aidant.",  # N21
"fol|contexte suisse|1|S|[CC art. 370 et 378]|En Suisse, les directives anticipées s'appliquent quand le patient perd sa capacité de discernement ; sinon, un représentant légal désigné par le Code civil décide des soins.",  # N22
"fol|contexte suisse|1|S|[LAVS art. 43bis]|En Suisse, l'allocation pour impotent de l'AVS soutient la personne âgée qui dépend d'autrui pour les actes ordinaires de la vie.",  # N23
"fol|terrain particulier|1||[avis d'expert]|L'aidant s'épuise souvent ; des relais, un accueil de jour et des séjours de répit le soulagent.",  # N24
"ana|signe|1||[McKeith, DLB Consortium, Neurology, 2017]|Le trouble comportemental en sommeil paradoxal peut précéder la démence de plusieurs années.",  # N25
]
ANGLES = [
"Fluctuations + hallucinations visuelles + TCSP = Lewy.",
"Jamais d'halopéridol.",
"Anticholinestérasique en premier.",
"Démence avant ou dans l'année du parkinsonisme.",
"DaTSCAN ou MIBG confirment.",
"Aggravation brutale = delirium d'abord.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un horloger retraité de 74 ans, à La Neuveville, décline depuis un an. Certains jours il est vif, d'autres il somnole et suit mal la conversation. Il voit des enfants assis au salon. Sa femme raconte qu'il donne des coups de pied en rêvant depuis des années. Il marche plus lentement et raide.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une démence à corps de Lewy || Fluctuations, hallucinations visuelles, TCSP et parkinsonisme.", "Une maladie d'Alzheimer || Elle commence par la mémoire, sans hallucinations précoces.", "Une démence de la maladie de Parkinson || Le parkinsonisme précède alors la démence de plus d'un an.", "Un delirium || Il est aigu et a une cause.", "Une schizophrénie tardive || Les signes neurologiques l'excluent."],
 notions="N04 N25 N05 N01", angle="application", diff=1, ladder=L("Déclin fluctuant.", "Synucléinopathie.", "Hallucinations, rêves agités.", "Signes cardinaux.", "Démence à corps de Lewy.", "Alzheimer.", "Fluctue + voit + rêve agité."), sources="[McKeith, DLB Consortium, 2017]"),
dict(format="A", serie=("S1", 2, 4), stem="Une nuit, cet homme s'agite à cause de ses visions. Le médecin de garde propose de l'halopéridol.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Éviter l'halopéridol, chercher un déclencheur et rassurer || L'hypersensibilité aux neuroleptiques peut être mortelle.", "Donner 5 mg d'halopéridol IM || Il expose à une réaction sévère.", "Donner de la rispéridone || Elle expose au même risque.", "Augmenter la lévodopa || Elle aggrave les hallucinations.", "Contentionner sans autre mesure || Elle aggrave l'agitation."],
 notions="N08 N14", angle="piège", diff=2, ladder=L("Agitation nocturne.", "Neuroleptiques.", "Halopéridol.", "Risque.", "Éviter.", "Rispéridone.", "Lewy = pas d'halopéridol."), sources="[McKeith, DLB Consortium, 2017]"),
dict(format="A", serie=("S1", 3, 4), stem="Le lendemain, vous discutez du traitement de fond de ses troubles cognitifs et de ses hallucinations.", prompt="Quel traitement proposez-vous en premier ?",
 items=["*Un anticholinestérasique, par exemple la rivastigmine || Le déficit cholinergique est profond.", "La quétiapine en première intention || Elle vient après l'anticholinestérasique.", "Un agoniste dopaminergique || Il aggrave les hallucinations.", "Une benzodiazépine le soir || Elle aggrave la confusion.", "L'amitriptyline || Ses effets anticholinergiques aggravent la confusion."],
 notions="N15 N16 N03 N14", angle="application", diff=2, ladder=L("Traitement de fond.", "Déficit cholinergique.", "Hallucinations.", "Premier choix.", "Rivastigmine.", "Quétiapine.", "Anticholinestérasique d'abord."), sources="[McKeith, DLB Consortium, 2017]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Vous cherchez à étayer le diagnostic par des examens.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un DaTSCAN réduit est un biomarqueur indicatif. || La voie dopaminergique est atteinte.", "V: Une scintigraphie cardiaque au MIBG abaissée est un biomarqueur indicatif. || L'innervation sympathique cardiaque est atteinte.", "F: Une atrophie hippocampique marquée est attendue. || Les lobes temporaux médians sont relativement préservés.", "F: Le diagnostic exige une biopsie. || Il est clinique, aidé des biomarqueurs."],
 notions="N10 N09 N11", angle="application", diff=2, ladder=L("Confirmation.", "Biomarqueurs.", "DaTSCAN, MIBG.", "Imagerie.", "Biomarqueurs indicatifs.", "Biopsie.", "DaTSCAN ou MIBG."), sources="[McKeith, DLB Consortium, 2017]"),
dict(masque=False, sit="monographique", format="A", stem="Vous enseignez les critères 2017 du consortium de la démence à corps de Lewy.", prompt="Quelle combinaison suffit à un diagnostic probable ?",
 items=["*Deux signes cardinaux, ou un signe cardinal et un biomarqueur indicatif || C'est la règle de 2017.", "Un seul signe évocateur || Il ne suffit pas.", "Une IRM normale || Elle ne prouve rien.", "Une hypotension orthostatique isolée || C'est un signe évocateur.", "Un biomarqueur indicatif sans démence || La démence est requise."],
 notions="N09 N04 N10", angle="direct", diff=2, ladder=L("Critères.", "Consortium.", "Signes cardinaux.", "Combinaison.", "2 cardinaux ou 1 + biomarqueur.", "Signe évocateur.", "Deux ou un plus un."), sources="[McKeith, DLB Consortium, 2017]"),
dict(format="A", stem="Une femme de 79 ans oublie depuis 3 ans ses rendez-vous et répète les mêmes questions. Elle n'a ni hallucinations, ni fluctuations, ni trouble moteur. L'IRM montre une atrophie hippocampique bilatérale.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Une maladie d'Alzheimer || Mémoire au premier plan et atrophie hippocampique.", "Une démence à corps de Lewy || Elle donne fluctuations et hallucinations précoces.", "Une démence frontotemporale || Elle commence par le comportement.", "Une démence vasculaire || Elle s'accompagne de lésions vasculaires.", "Une démence de la maladie de Parkinson || Il n'y a pas de parkinsonisme."],
 notions="N12 N05 N02", angle="application", diff=1, ladder=L("Oubli progressif.", "Démence.", "Hippocampe.", "Profil.", "Alzheimer.", "Lewy.", "Mémoire d'abord = Alzheimer."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 72 ans a une maladie de Parkinson depuis 8 ans. Depuis un an, il perd ses capacités d'organisation et voit parfois des chats inexistants.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Une démence de la maladie de Parkinson || Le parkinsonisme précède la démence de plus d'un an.", "Une démence à corps de Lewy || La démence aurait précédé ou suivi de moins d'un an.", "Une maladie d'Alzheimer || Le profil n'est pas mnésique.", "Une schizophrénie || Les hallucinations s'expliquent autrement.", "Une paralysie supranucléaire progressive || Elle donne une paralysie du regard vertical."],
 notions="N01 N12", angle="application", diff=2, ladder=L("Parkinson ancien.", "Règle de l'année.", "8 ans.", "Classement.", "Démence parkinsonienne.", "Lewy.", "Parkinson > 1 an d'abord."), sources="[McKeith, DLB Consortium, 2017]"),
dict(format="A", stem="Une femme de 81 ans, suivie pour des troubles cognitifs fluctuants avec hallucinations visuelles, devient très confuse en 2 jours. Elle a 38,4 °C et des brûlures mictionnelles.", prompt="Quelle conduite est prioritaire ?",
 items=["*Chercher et traiter un delirium d'origine infectieuse || L'aggravation brutale a une cause aiguë.", "Conclure à une simple fluctuation de la maladie || Elle ne donne pas de fièvre.", "Augmenter l'anticholinestérasique || La cause doit se traiter.", "Donner de l'halopéridol || Il est dangereux ici.", "Demander un DaTSCAN urgent || Il n'aide pas."],
 notions="N13 N04 N12", angle="piège", diff=2, ladder=L("Aggravation brutale.", "Delirium.", "Fièvre.", "Cause.", "Infection urinaire.", "Fluctuation.", "Brutal = delirium."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 77 ans avec troubles cognitifs fluctuants et hallucinations visuelles tombe à cause d'une rigidité et d'une lenteur qui l'empêchent de s'habiller.", prompt="Quel traitement de son parkinsonisme proposez-vous ?",
 items=["*La lévodopa à la plus faible dose utile || Elle aide sans trop aggraver les hallucinations.", "Le pramipexole || Les agonistes aggravent les hallucinations.", "Le bipéridène || Les anticholinergiques aggravent la confusion.", "L'halopéridol || Il aggrave le parkinsonisme.", "Aucun traitement possible || La lévodopa peut aider."],
 notions="N17 N19", angle="application", diff=2, ladder=L("Parkinsonisme gênant.", "Dopaminergiques.", "Hallucinations.", "Choix.", "Lévodopa faible dose.", "Agoniste.", "Lévodopa prudente."), sources="[McKeith, DLB Consortium, 2017]"),
dict(format="A", stem="Une femme de 80 ans avec troubles cognitifs fluctuants reçoit de l'oxybutynine pour une incontinence urinaire. Elle devient très confuse en une semaine.", prompt="Quelle explication est la plus probable ?",
 items=["*L'effet anticholinergique de l'oxybutynine || Le déficit cholinergique rend la patiente très sensible.", "Une progression naturelle de la maladie || La chronologie désigne le médicament.", "Une hypoglycémie || Rien ne l'indique.", "Un effet de la rivastigmine || Elle améliore la cognition.", "Un AVC || La chronologie désigne le médicament."],
 notions="N19 N14", angle="piège", diff=2, ladder=L("Confusion nouvelle.", "Iatrogénie.", "Oxybutynine.", "Mécanisme.", "Anticholinergique.", "Progression.", "Pas d'anticholinergique."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 70 ans bouge violemment en rêvant et a blessé sa femme. Il a des troubles cognitifs fluctuants débutants.", prompt="Quelle mesure proposez-vous ?",
 items=["*Sécuriser la chambre et proposer de la mélatonine || Elle limite les blessures avec peu d'effets.", "Prescrire de l'halopéridol le soir || Il est dangereux.", "Prescrire un hypnotique Z à forte dose || Il favorise chutes et confusion.", "Ne rien faire || Le risque de blessure est réel.", "Prescrire de l'amitriptyline || Elle peut aggraver le trouble."],
 notions="N18 N25", angle="application", diff=2, ladder=L("Rêves agités.", "Parasomnie.", "Blessures.", "Traitement.", "Sécuriser, mélatonine.", "Halopéridol.", "Sécurité d'abord."), sources="[avis d'expert]"),
dict(format="A", stem="Un étudiant vous demande pourquoi les anticholinestérasiques aident souvent davantage ces patients fluctuants et hallucinés que dans la maladie d'Alzheimer.", prompt="Quelle explication est la plus juste ?",
 items=["*Le déficit cholinergique cortical y est plus profond || Les noyaux cholinergiques sont tôt atteints.", "Les patients ont moins d'amyloïde || Ce n'est pas l'explication.", "La dopamine est en excès || Elle est au contraire déficitaire.", "Le médicament agit sur l'alpha-synucléine || Il n'agit pas sur elle.", "Les patients sont plus jeunes || L'âge n'explique pas l'effet."],
 notions="N03 N15", angle="direct", diff=3, ladder=L("Réponse au traitement.", "Neurotransmission.", "Acétylcholine.", "Mécanisme.", "Déficit cholinergique profond.", "Amyloïde.", "Moins d'ACh = plus d'effet."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 76 ans avec troubles cognitifs fluctuants et hallucinations visuelles tombe en se levant. Sa tension passe de 140/80 couchée à 105/70 debout. Elle prend de l'amlodipine et un diurétique.", prompt="Quelle première mesure proposez-vous ?",
 items=["*Réduire les antihypertenseurs et appliquer les mesures posturales || L'hypotension orthostatique est dysautonomique et iatrogène.", "Ajouter un bêtabloquant || Il aggraverait la chute tensionnelle.", "Prescrire de l'halopéridol || Il n'a aucun rôle.", "Restreindre les boissons || Elle aggrave l'hypotension.", "Augmenter le diurétique || Il aggrave l'hypotension."],
 notions="N19 N06 N21", angle="application", diff=2, ladder=L("Chutes.", "Dysautonomie.", "Tension debout.", "Mesure.", "Moins d'antihypertenseurs.", "Diurétique.", "Mesurer couché-debout."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 82 ans, à Delémont, n'a plus sa capacité de discernement. Il n'a pas rédigé de directives anticipées. Sa femme vit avec lui et l'assiste régulièrement.", prompt="Qui consent aux soins à sa place ?",
 items=["*Son épouse, représentante légale dans le domaine médical selon le Code civil || Le conjoint qui fait ménage commun et l'assiste est désigné.", "Le médecin seul || Il doit consulter le représentant.", "Le directeur de l'EMS || Il n'a pas ce rôle.", "Personne, aucun soin n'est possible || La loi désigne un représentant.", "Le juge de paix systématiquement || Il intervient seulement en l'absence de représentant."],
 notions="N22", angle="application", diff=2, ladder=L("Incapacité.", "Représentation.", "Pas de directives.", "Code civil.", "Conjoint.", "Médecin seul.", "Code civil art. 378."), sources="[CC art. 378]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez les signes cardinaux de la démence à corps de Lewy.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Les fluctuations de l'attention en font partie. || C'est un signe cardinal.", "V: Les hallucinations visuelles détaillées en font partie. || C'est un signe cardinal.", "F: Une perte de mémoire massive au début en fait partie. || La mémoire est d'abord préservée.", "F: Les neuroleptiques classiques sont bien tolérés. || L'hypersensibilité peut être grave."],
 notions="N04 N05 N08", angle="direct", diff=1, ladder=L("Révision.", "Signes cardinaux.", "Quatre signes.", "Pièges.", "Fluctuations, hallucinations.", "Mémoire.", "Attention, pas mémoire."), sources="[McKeith, DLB Consortium, 2017]"),
dict(format="Kprim", stem="Un homme de 78 ans avec troubles cognitifs fluctuants, hallucinations visuelles et parkinsonisme est hospitalisé. L'équipe discute des psychotropes.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'halopéridol peut déclencher une réaction sévère. || L'hypersensibilité aux neuroleptiques est un signe évocateur.", "V: La quétiapine à faible dose peut se discuter si les hallucinations restent graves. || Elle est moins dangereuse.", "F: La rispéridone est sans risque. || Elle expose au même risque.", "F: Un neuroleptique se donne d'emblée à toute hallucination. || On cherche d'abord un déclencheur."],
 notions="N08 N14", angle="piège", diff=2, ladder=L("Psychotropes.", "Neuroleptiques.", "Hypersensibilité.", "Choix.", "Quétiapine faible dose.", "Rispéridone.", "Éviter, sinon quétiapine."), sources="[McKeith, DLB Consortium, 2017]"),
dict(format="Kprim", stem="La femme d'un homme de 79 ans, fluctuant et halluciné depuis 2 ans, s'épuise à domicile à Fribourg.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'allocation pour impotent de l'AVS peut aider ce couple. || Il dépend d'autrui pour les actes de la vie.", "V: Un accueil de jour ou un séjour de répit soulage l'aidante. || L'épuisement est fréquent.", "F: L'évolution est en général plus lente que celle de la maladie d'Alzheimer. || Elle est souvent plus rapide.", "F: Le poids et la déglutition n'ont pas à être suivis. || Les pneumonies d'aspiration menacent."],
 notions="N23 N24 N20 N21", angle="application", diff=2, ladder=L("Aidante épuisée.", "Soutien.", "Suisse.", "Aides.", "Allocation, répit.", "Évolution lente.", "Soulager l'aidant."), sources="[LAVS art. 43bis]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Vous résumez les critères 2017 de la démence à corps de Lewy.", prompt="Choisissez les TROIS signes cardinaux présents dans cette liste.",
 items=["*Fluctuations de l'attention et de la vigilance || Signe cardinal.", "*Hallucinations visuelles récurrentes || Signe cardinal.", "*Trouble comportemental en sommeil paradoxal || Signe cardinal.", "Syndrome des jambes sans repos || Il n'est pas un signe cardinal.", "Hypotension orthostatique || Signe évocateur.", "Chutes répétées || Signe évocateur.", "Hyposmie || Signe évocateur.", "Dépression || Signe évocateur.", "Hypersomnie || Signe évocateur.", "Atrophie hippocampique || Elle n'est pas attendue.", "Aphasie précoce || Elle oriente ailleurs.", "Amnésie au premier plan || Elle oriente vers Alzheimer."],
 notions="N04 N06", angle="direct", diff=2, ladder=L("Critères.", "Signes cardinaux.", "Quatre.", "Lesquels.", "Fluctuations, hallucinations, TCSP, parkinsonisme.", "Signes évocateurs.", "Quatre cardinaux."), sources="[McKeith, DLB Consortium, 2017]"),
dict(format="MenuLong", stem="Un homme de 80 ans a des troubles cognitifs fluctuants, des hallucinations visuelles et un parkinsonisme.", prompt="Quels médicaments évitez-vous ? (3 réponses)",
 items=["*Halopéridol || Hypersensibilité aux neuroleptiques.", "*Oxybutynine || Anticholinergique confusiogène.", "*Bipéridène || Anticholinergique confusiogène.", "Rivastigmine || Elle est le traitement de fond.", "Donépézil || Il est utile.", "Lévodopa à faible dose || Elle peut traiter le parkinsonisme.", "Mélatonine || Elle traite le TCSP.", "Paracétamol || Il est sans risque particulier.", "Quétiapine à faible dose || Elle est une option si nécessaire.", "Vitamine D || Elle est sans risque.", "Macrogol || Il traite la constipation.", "Clozapine à faible dose sous surveillance || Elle est une option."],
 notions="N08 N19 N17", angle="piège", diff=2, ladder=L("Prescription.", "Iatrogénie.", "Neuroleptiques, anticholinergiques.", "Lesquels.", "Halopéridol, oxybutynine, bipéridène.", "Rivastigmine.", "Ni neuroleptique classique ni anticholinergique."), sources="[McKeith, DLB Consortium, 2017]"),
dict(format="A", stem="Une femme de 73 ans obtient 22/30 au MoCA. Elle échoue à la copie des pentagones et au tracé de piste, mais rappelle 4 mots sur 5 sans aide. Elle voit parfois des personnes dans sa chambre.", prompt="Quel profil cognitif cet examen montre-t-il ?",
 items=["*Un profil attentionnel, exécutif et visuospatial, à mémoire relativement préservée || Il oriente vers une synucléinopathie.", "Un profil amnésique hippocampique || Le rappel est bon.", "Un profil aphasique || Le langage n'est pas en cause.", "Un profil normal pour l'âge || 22/30 avec échecs ciblés est anormal.", "Un profil frontal comportemental || Le comportement n'est pas décrit."],
 notions="N07 N05", angle="application", diff=2, ladder=L("Test cognitif.", "Profil.", "Pentagones.", "Mémoire.", "Visuospatial, exécutif.", "Amnésique.", "Pentagones ratés, rappel bon."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Démence à corps de Lewy : la reconnaître par ses signes cardinaux, la confirmer par DaTSCAN ou MIBG, éviter les neuroleptiques et les anticholinergiques, traiter par anticholinestérasique et soutenir l'aidant",
 notions=[
  dict(titre="Reconnaître", rub=["def", "ana", "exa", "epi"], comment="Cherche les quatre signes cardinaux.",
   tableau=(["Signe cardinal", "Ce qu'on observe", "Pourquoi"], [
     ["Fluctuations", "Jours vifs et jours somnolents", "L'attention varie"],
     ["Hallucinations visuelles", "Personnes, animaux détaillés", _T("Déficit cholinergique", "Il explique aussi la réponse aux anticholinestérasiques.")],
     ["TCSP", "Coups en rêvant", "Il précède souvent de plusieurs années"],
     ["Parkinsonisme", "Lenteur, rigidité", "Démence avant ou dans l'année"]]),
   points=["Mémoire d'abord préservée ; pentagones échoués."], sources=["[McKeith, DLB Consortium, 2017]"]),
  dict(titre="Confirmer et distinguer", rub=["gold", "alt", "pos"], comment="Applique la règle des critères et élimine les diagnostics voisins.",
   tableau=(["Élément", "Résultat", "Sens"], [
     ["DaTSCAN", "Captation réduite", "Biomarqueur indicatif"],
     ["MIBG cardiaque", "Captation abaissée", "Biomarqueur indicatif"],
     ["IRM", _T("Hippocampes préservés", "L'atrophie marquée oriente vers Alzheimer."), "Signe d'appui"],
     ["Aggravation brutale", "Fièvre, médicament", "Delirium à traiter d'abord"]]),
   points=["Probable : 2 cardinaux ou 1 + biomarqueur."], sources=["[McKeith, DLB Consortium, 2017]"]),
  dict(titre="Traiter sans nuire", rub=["red", "acu", "chr", "hos"], comment="Évite les neuroleptiques et les anticholinergiques.",
   arbre=[("t1", None, "Démence à corps de Lewy", "La iatrogénie est le premier danger."),
          ("t2", "t1", "Cognition, hallucinations", "Anticholinestérasique.", "dcl"),
          ("t3", "t2", "Hallucinations graves persistantes", "Quétiapine ou clozapine faible dose ; jamais d'halopéridol.", "dcl"),
          ("t4", "t1", "Parkinsonisme gênant", "Lévodopa à faible dose.", "dcl"),
          ("t5", "t1", "TCSP", "Sécuriser, mélatonine.", "dcl")],
   points=["Retirer les anticholinergiques."], sources=["[McKeith, DLB Consortium, 2017]"]),
  dict(titre="Suivre et soutenir", rub=["pro", "sur", "fol"], comment="Prévient chutes et épuisement et prépare les décisions.",
   tableau=(["Domaine", "Mesure", "Pourquoi"], [
     ["Chutes", "Tension couchée-debout", "La dysautonomie fait tomber"],
     ["Déglutition, poids", "Surveillance régulière", "Les pneumonies d'aspiration menacent"],
     ["Droit suisse", _T("Directives anticipées, représentant", "Le Code civil désigne qui décide."), "Capacité de discernement perdue"],
     ["Aidant", "Répit, allocation pour impotent", "Il s'épuise"]]),
   points=["Évolution souvent plus rapide qu'Alzheimer."], sources=["[CC art. 370 et 378]", "[LAVS art. 43bis]"]),
 ],
 ssp=dict(code="S7.7", nom="Troubles cognitifs, notamment difficultés de concentration, troubles de la mémoire et de la compréhension", officiel=True, algorithme=[
  ("n1", None, "Troubles cognitifs", "Le delirium s'élimine d'abord."),
  ("n2", "n1", "Début aigu, cause", "Delirium : traiter la cause.", None, "c2"),
  ("n3", "n1", "Mémoire d'abord", "Maladie d'Alzheimer (même SSP).", None, "c2"),
  ("n4", "n1", "Fluctuations, hallucinations, TCSP", "Démence à corps de Lewy.", "dcl", "c1"),
  ("n5", "n4", "Doute", "DaTSCAN ou MIBG.", "dcl", "c2"),
  ("n6", "n4", "Traitement", "Anticholinestérasique, pas de neuroleptique classique.", "dcl", "c3"),
  ("n7", "n6", "Suivi", "Chutes, déglutition, aidant, représentation.", "dcl", "c4")]),
 pec=[
  dict(cle="dcl", titre="Démence à corps de Lewy",
   but=["Améliorer cognition et hallucinations sans iatrogénie.", "Prévenir chutes et épuisement de l'aidant."],
   moyens=dict(accueil=["Rassurer patient et proches sur les hallucinations.", "Revoir tous les médicaments anticholinergiques.", "Signaler l'hypersensibilité aux neuroleptiques dans le dossier."],
    pharma=[("Rivastigmine (anticholinestérasique)", "Titration par paliers, orale ou patch ; à vérifier dans l'AIPS.", "Elle améliore cognition, fluctuations et hallucinations.", "[McKeith, DLB Consortium, 2017]"),
            ("Lévodopa (dopaminergique)", "Plus faible dose utile ; à vérifier dans l'AIPS.", "Elle traite un parkinsonisme gênant.", "[McKeith, DLB Consortium, 2017]"),
            ("Quétiapine (antipsychotique atypique)", "Très faible dose si indispensable ; à vérifier dans l'AIPS.", "Elle est moins dangereuse que l'halopéridol.", "[McKeith, DLB Consortium, 2017]")],
    nonpharma=[("éducation thérapeutique", "Expliquer les hallucinations et les fluctuations aux proches.", "Elle réduit l'angoisse et les recours aux neuroleptiques."),
               ("rééducation", "Physiothérapie de l'équilibre et ergothérapie.", "Elles limitent les chutes."),
               ("social et assurances", "Allocation pour impotent, accueil de jour, directives anticipées.", "Elles soutiennent l'aidant et préparent les décisions.")],
    transversal=[("Gériatrie", "Elle évalue chutes et polymédication."), ("Psychiatrie de l'âge avancé", "Elle aide pour les hallucinations et la dépression.")]),
   urgence=None,
   horsUrgence=(["Revue des médicaments.", "Mention de l'hypersensibilité aux neuroleptiques."],
            [("d'abord", "médecin de famille", "Repère les signes et élimine un delirium."),
             ("ensuite", "neurologue", "Confirme et débute l'anticholinestérasique."),
             ("en même temps", "infirmier·ère de soins à domicile", "Surveille chutes, tension et observance."),
             ("puis", "assistant·e social·e", "Organise répit et allocation pour impotent.")]),
   pronostic="L'évolution est souvent plus rapide que celle de la maladie d'Alzheimer, avec chutes et pneumonies.",
   suivi=[("Cognition et hallucinations", "Tous les 3 à 6 mois", "Stabilité"), ("Tension couchée-debout", "À chaque consultation", "Pas d'hypotension orthostatique"), ("Charge de l'aidant", "À chaque consultation", "Aidant soutenu")],
   sortie="Le suivi reste ambulatoire tant que le maintien à domicile est sûr.",
   prevention=["Elle évite neuroleptiques classiques et anticholinergiques.", "Elle prévient les chutes.", "Elle anticipe les décisions par directives anticipées."]),
 ])
AVERIFIER = ["Indication suisse de la rivastigmine (démence parkinsonienne / corps de Lewy) et doses à vérifier dans l'AIPS.", "Doses de lévodopa et de quétiapine à vérifier dans l'AIPS."]
