ID = "E51.2__F1_15-E07"
PLAN = "monographique"
NOTIONS = [
"def|critère|2||[Galvin, Eur J Neurol, 2010, EFNS]|L'encéphalopathie de Gayet-Wernicke est une urgence neurologique due à une carence aiguë en thiamine (vitamine B1), réversible si elle est traitée tôt.",  # N01
"epi|terrain particulier|3||[Galvin, Eur J Neurol, 2010]|Elle survient surtout chez l'alcoolique, mais aussi après chirurgie bariatrique, en cas de vomissements prolongés, d'hyperemesis gravidarum, de dénutrition ou de cancer.",  # N02
"bas|mécanisme|2||[avis d'expert]|La thiamine est un cofacteur du métabolisme du glucose, si bien qu'un apport de glucose sans thiamine peut déclencher ou aggraver l'encéphalopathie.",  # N03
"bas|mécanisme|1||[avis d'expert]|Les lésions touchent les corps mamillaires, les thalamus médians et la substance grise périaqueducale.",  # N04
"ana|symptôme|2||[Harper, J Neurol Neurosurg Psychiatry, 1986]|La triade confusion, troubles oculomoteurs et ataxie n'est complète que chez une minorité de patients.",  # N05
"exa|signe|2||[avis d'expert]|Les troubles oculomoteurs comprennent nystagmus, paralysie du VI et ophtalmoplégie, et l'ataxie touche surtout la marche.",  # N06
"red|critère|2||[Caine, J Neurol Neurosurg Psychiatry, 1997]|Chez l'alcoolique, deux critères parmi carence alimentaire, signes oculomoteurs, atteinte cérébelleuse et trouble mental suffisent à retenir le diagnostic.",  # N07
"red|piège|2||[avis d'expert]|L'état confusionnel de l'alcoolique est souvent attribué à tort à l'ivresse ou au sevrage, ce qui retarde la thiamine.",  # N08
"red|signe|1||[avis d'expert]|Une hypothermie, une hypotension ou un coma inexpliqués chez un patient dénutri peuvent révéler l'encéphalopathie.",  # N09
"gold|décision|3||[Galvin, Eur J Neurol, 2010]|Le diagnostic est clinique, et le traitement ne doit jamais attendre un dosage ou une imagerie.",  # N10
"alt|examen|1||[avis d'expert]|L'IRM peut montrer un hypersignal des thalamus médians, des corps mamillaires et de la région périaqueducale, mais une IRM normale n'exclut rien.",  # N11
"alt|examen|1||[avis d'expert]|Un dosage de thiamine prélevé avant le traitement peut confirmer a posteriori, sans retarder la perfusion.",  # N12
"pos|diagnostic différentiel|1||[avis d'expert]|Le diagnostic différentiel comprend l'hypoglycémie, l'intoxication, l'encéphalopathie hépatique, l'hématome sous-dural et l'état de mal non convulsif.",  # N13
"acu|posologie|2|S|[Galvin, Eur J Neurol, 2010 ; AIPS Swissmedic]|La thiamine se donne par voie IV à haute dose, par exemple 200 à 500 mg trois fois par jour pendant plusieurs jours, posologie à vérifier dans l'AIPS.",  # N14
"acu|piège|3||[avis d'expert]|Chez le patient à risque, la thiamine se donne avant ou avec le glucose, jamais après.",  # N15
"acu|piège|1||[avis d'expert]|La voie orale est insuffisante en phase aiguë, car l'absorption intestinale de la thiamine est réduite chez l'alcoolique.",  # N16
"acu|molécule|1||[avis d'expert]|Une hypomagnésémie se corrige aussi, car le magnésium est nécessaire à l'action de la thiamine.",  # N17
"chr|prévention|2||[avis d'expert]|Tout patient à risque hospitalisé, notamment pour sevrage alcoolique ou renutrition, reçoit une thiamine prophylactique.",  # N18
"chr|décision|1||[avis d'expert]|Une prise en charge addictologique et nutritionnelle prévient la récidive après la phase aiguë.",  # N19
"hos|complication|1||[avis d'expert]|Sans traitement, l'encéphalopathie évolue vers un syndrome de Korsakoff avec amnésie antérograde et confabulations, souvent irréversible.",  # N20
"hos|complication|1||[avis d'expert]|Le syndrome de renutrition inappropriée associe hypophosphatémie, hypokaliémie et carence en thiamine chez le dénutri qu'on réalimente.",  # N21
"pro|pronostic|1||[avis d'expert]|Les troubles oculomoteurs régressent en heures à jours sous thiamine, alors que les troubles mnésiques récupèrent lentement et souvent incomplètement.",  # N22
"sur|décision|1||[avis d'expert]|Le suivi surveille vigilance, oculomotricité, marche, mémoire et électrolytes.",  # N23
"fol|contexte suisse|1|S|[avis d'expert]|Après la sortie, le réseau addictologique et le médecin de famille organisent le sevrage, la supplémentation et, si besoin, une mesure de protection.",  # N24
"fol|terrain particulier|1||[avis d'expert]|Après chirurgie bariatrique, une supplémentation vitaminique au long cours et un suivi nutritionnel préviennent la carence.",  # N25
]
ANGLES = [
"La triade complète manque le plus souvent.",
"La thiamine passe avant le glucose.",
"Le traitement n'attend ni dosage ni IRM.",
"La voie orale ne suffit pas en aigu.",
"La confusion de l'alcoolique n'est pas toujours l'ivresse.",
"La chirurgie bariatrique et les vomissements exposent aussi.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un homme de 54 ans, connu pour une consommation d'alcool importante, est amené aux urgences de Neuchâtel par la police. Il est désorienté, marche en élargissant le polygone et présente un nystagmus horizontal. L'alcoolémie est à 0,3 ‰. Glycémie 3,4 mmol/L.", prompt="Quelle est la première mesure ?",
 items=["*Thiamine IV à haute dose, puis glucose || La thiamine passe avant le glucose chez le patient à risque.", "Glucose 40 % IV seul || Le glucose sans thiamine aggrave l'encéphalopathie.", "Attendre la fin de l'ivresse || L'alcoolémie basse n'explique pas le tableau.", "Halopéridol IV pour l'agitation || Il ne traite pas la cause.", "IRM cérébrale avant tout traitement || Le traitement ne doit pas attendre."],
 notions="N15 N01 N08 N10", angle="application", diff=2, ladder=L("Confusion chez un alcoolique.", "Carence en thiamine.", "Nystagmus, ataxie.", "Wernicke versus ivresse.", "Thiamine puis glucose.", "Glucose d'abord.", "B1 avant glucose."), sources="[Galvin, Eur J Neurol, 2010]"),
dict(masque=False, sit="monographique", format="A", serie=("S1", 2, 4), stem="Chez cet homme, l'interne propose 100 mg de thiamine per os par jour.", prompt="Quelle est votre réponse ?",
 items=["*Prescrire la thiamine IV à haute dose plusieurs fois par jour || La voie orale est insuffisante en phase aiguë.", "Accepter la voie orale || L'absorption est réduite chez l'alcoolique.", "Donner une dose unique IV puis rien || Plusieurs jours sont nécessaires.", "Remplacer par de la vitamine B12 || La carence en cause est la B1.", "Attendre le dosage de thiamine || Le traitement ne doit pas attendre."],
 notions="N14 N16 N12", angle="piège", diff=3, ladder=L("Prescription orale.", "Malabsorption.", "Phase aiguë.", "Voie et dose.", "IV haute dose.", "Per os.", "Aigu : IV."), sources="[Galvin, Eur J Neurol, 2010]"),
dict(format="Kprim", serie=("S1", 3, 4), stem="Le bilan de cet homme montre un magnésium bas. Une IRM est réalisée le lendemain.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'hypomagnésémie doit être corrigée. || Le magnésium est un cofacteur de la thiamine.", "V: L'IRM peut montrer un hypersignal des thalamus médians et des corps mamillaires. || Ce sont les zones vulnérables.", "F: Une IRM normale permet d'arrêter la thiamine. || Elle n'exclut pas le diagnostic.", "F: Le diagnostic exige la triade complète. || Elle manque souvent."],
 notions="N17 N11 N04 N05", angle="direct", diff=3, ladder=L("Bilan.", "Cofacteurs, topographie.", "Magnésium bas.", "Valeur de l'IRM.", "Corriger, poursuivre.", "Arrêter sur IRM normale.", "IRM normale n'exclut rien."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 4, 4), stem="Deux semaines plus tard, le nystagmus de cet homme a disparu, mais il ne retient rien de nouveau et invente des récits sur ses journées.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Un syndrome de Korsakoff || Amnésie antérograde et confabulations après une encéphalopathie de Wernicke.", "Une maladie d'Alzheimer || Le contexte aigu et carentiel l'oriente ailleurs.", "Un état confusionnel persistant simple || L'attention est restaurée.", "Une psychose alcoolique || Il s'agit de confabulations mnésiques.", "Un trouble factice || Les confabulations ne sont pas intentionnelles."],
 notions="N20 N22", angle="application", diff=2, ladder=L("Amnésie après Wernicke.", "Lésions mamillo-thalamiques.", "Confabulations.", "Korsakoff.", "Réadaptation, protection.", "Alzheimer.", "Confabule : Korsakoff."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 36 ans opérée d'un bypass gastrique il y a 4 mois vomit plusieurs fois par jour depuis 3 semaines. Elle est confuse, voit double et ne tient pas debout.", prompt="Quel diagnostic évoquez-vous en premier ?",
 items=["*Une encéphalopathie par carence en thiamine || Vomissements prolongés après chirurgie bariatrique.", "Un syndrome de dumping || Il ne donne pas de diplopie ni d'ataxie.", "Une hypoglycémie isolée || Elle n'explique pas la diplopie et l'ataxie persistantes.", "Une sclérose en plaques || Le contexte carentiel l'oriente ailleurs.", "Une migraine basilaire || Le contexte et la durée l'excluent."],
 notions="N02 N05 N06", angle="application", diff=2, ladder=L("Vomissements après bypass.", "Carence en B1.", "Diplopie, ataxie, confusion.", "Terrain non alcoolique.", "Thiamine IV.", "Penser uniquement à l'alcool.", "Bypass + vomissements : B1."), sources="[Galvin, Eur J Neurol, 2010]"),
dict(format="A", stem="Une femme de 24 ans enceinte de 12 semaines est hospitalisée à Lausanne pour des vomissements incoercibles depuis 4 semaines. Elle va recevoir une perfusion glucosée.", prompt="Quelle mesure ajoutez-vous ?",
 items=["*De la thiamine avant ou avec la perfusion glucosée || L'hyperemesis expose à la carence en B1.", "Aucune, la grossesse protège || Elle n'en protège pas.", "De la vitamine A à haute dose || Elle est tératogène à forte dose.", "Un régime sans glucides || Il n'a pas de sens.", "Une IRM cérébrale avant toute perfusion || Elle n'est pas nécessaire."],
 notions="N18 N15 N02", angle="application", diff=2, ladder=L("Hyperemesis.", "Épuisement des réserves de B1.", "Perfusion glucosée.", "Prévention.", "Thiamine.", "Glucose seul.", "Vomissements : B1."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 61 ans, sans domicile fixe et dénutri, est trouvé à Bienne avec une température à 34,5 °C, une TA à 85/50 mmHg et une somnolence. La glycémie est normale.", prompt="Quelle hypothèse ne faut-il pas manquer ?",
 items=["*Une encéphalopathie de Wernicke, qui peut se présenter par hypothermie, hypotension et trouble de vigilance || La thiamine se donne sans attendre.", "Une simple exposition au froid sans autre cause || La dénutrition oriente vers une carence.", "Une hypoglycémie || La glycémie est normale.", "Une hyperthyroïdie || Elle donnerait une hyperthermie.", "Une crise de panique || Le tableau est organique."],
 notions="N09 N02 N10", angle="piège", diff=3, ladder=L("Hypothermie et somnolence.", "Atteinte hypothalamique.", "Dénutrition.", "Présentation atypique.", "Thiamine IV.", "Réchauffer seulement.", "Dénutri + coma : B1."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 48 ans est hospitalisé à Fribourg pour un sevrage alcoolique programmé. Il est orienté et marche normalement.", prompt="Quelle mesure préventive est indiquée ?",
 items=["*Une thiamine prophylactique || Le patient alcoolique est à risque.", "Aucune mesure en l'absence de symptôme || La prévention est recommandée.", "Une perfusion glucosée seule || Elle peut déclencher la carence.", "Un antipsychotique prophylactique || Il n'est pas indiqué.", "Une IRM cérébrale systématique || Elle n'est pas indiquée."],
 notions="N18 N03 N15", angle="direct", diff=1, ladder=L("Sevrage programmé.", "Réserves faibles.", "Asymptomatique.", "Prévention.", "Thiamine.", "Attendre les signes.", "Sevrage : B1."), sources="[avis d'expert]"),
dict(format="A", stem="Un patient de 70 ans dénutri, réalimenté par sonde depuis 2 jours, devient confus avec une faiblesse généralisée. Phosphate 0,3 mmol/L, potassium 2,9 mmol/L.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Un syndrome de renutrition inappropriée, avec risque de carence en thiamine || Hypophosphatémie et hypokaliémie lors de la réalimentation.", "Une gastroentérite || Rien ne l'évoque.", "Une hyperthyroïdie || Rien ne l'évoque.", "Une insuffisance surrénalienne isolée || Le tableau électrolytique oriente ailleurs.", "Un AVC || Le tableau est métabolique."],
 notions="N21 N03", angle="application", diff=3, ladder=L("Confusion à la réalimentation.", "Entrée intracellulaire des électrolytes.", "Phosphate bas.", "Renutrition.", "Ralentir, corriger, thiamine.", "Augmenter l'apport.", "Réalimentation : phosphate et B1."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 57 ans, alcoolique, est confus depuis 2 jours. Il a chuté il y a une semaine. La glycémie et l'oculomotricité sont normales.", prompt="Quel examen ne faut-il pas omettre ?",
 items=["*Un CT cérébral à la recherche d'un hématome sous-dural || La chute chez l'alcoolique expose à cette complication.", "Une électromyographie || Elle n'est pas indiquée.", "Une coloscopie || Elle n'est pas indiquée.", "Une échographie thyroïdienne || Elle n'est pas indiquée.", "Une biopsie hépatique || Elle n'est pas indiquée."],
 notions="N13 N08", angle="piège", diff=2, ladder=L("Confusion après chute.", "Saignement sous-dural.", "Alcoolique.", "Diagnostic différentiel.", "CT cérébral.", "Tout attribuer à l'alcool.", "Chute + confusion : CT."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous expliquez la carence en thiamine à des étudiants à Genève.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La thiamine est un cofacteur du métabolisme du glucose. || Les neurones en dépendent.", "V: Les corps mamillaires et les thalamus médians sont particulièrement vulnérables. || Leur métabolisme est intense.", "F: La triade est complète chez la plupart des patients. || Elle manque souvent.", "F: La carence ne survient que chez l'alcoolique. || D'autres terrains exposent."],
 notions="N03 N04 N05 N02 N01", angle="direct", diff=2, ladder=L("Physiopathologie.", "Cofacteur métabolique.", "Topographie.", "Terrain.", "Comprendre.", "Alcool uniquement.", "Triade souvent incomplète."), sources="[Harper, 1986]"),
dict(format="Kprim", stem="Un homme alcoolique de 50 ans est confus. Vous appliquez les critères de Caine.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Deux critères parmi les quatre suffisent. || Ils augmentent la sensibilité.", "V: La carence alimentaire est l'un des critères. || Elle témoigne du terrain.", "F: Un trouble mental isolé suffit. || Deux critères sont nécessaires.", "F: Le dosage de thiamine fait partie des critères. || Ils sont cliniques."],
 notions="N07 N10", angle="direct", diff=3, ladder=L("Critères.", "Sensibilité clinique.", "Alcoolique confus.", "Caine.", "Appliquer.", "Exiger la triade.", "Deux critères sur quatre."), sources="[Caine, 1997]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un patient de 59 ans est traité depuis 3 jours par thiamine IV pour une encéphalopathie carentielle.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Les troubles oculomoteurs régressent souvent en quelques heures à jours. || Ils répondent vite.", "V: Les troubles de mémoire récupèrent plus lentement. || Les lésions mamillo-thalamiques sont plus durables.", "V: Une prise en charge addictologique doit être organisée. || Elle prévient la récidive.", "F: La thiamine peut être arrêtée dès la régression du nystagmus. || Le traitement se poursuit."],
 notions="N22 N19 N14", angle="application", diff=2, ladder=L("Évolution sous traitement.", "Récupération différenciée.", "J3.", "Pronostic.", "Poursuivre, addictologie.", "Arrêt précoce.", "Yeux vite, mémoire lentement."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 45 ans, opérée d'un bypass il y a 3 ans, a arrêté ses vitamines. Elle demande si c'est grave.", prompt="Quelle réponse est la plus adaptée ?",
 items=["*Reprendre la supplémentation au long cours et le suivi nutritionnel, car la carence peut survenir à tout moment || La malabsorption persiste.", "Les vitamines sont inutiles après la première année || La malabsorption persiste.", "Seule la vitamine C compte || Plusieurs carences menacent.", "Il suffit de manger davantage de pain blanc || Il ne compense pas la malabsorption.", "Seule une prise de sang annuelle est nécessaire sans supplément || La prévention repose sur la supplémentation."],
 notions="N25 N02", angle="application", diff=2, ladder=L("Arrêt des vitamines.", "Malabsorption durable.", "Bypass ancien.", "Prévention.", "Reprendre et suivre.", "Arrêter.", "Bypass : vitamines à vie."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme alcoolique de 52 ans hospitalisé à Lucerne est confus et ataxique. L'interne attribue tout au sevrage et prescrit seulement une benzodiazépine.", prompt="Quelle erreur commet-il ?",
 items=["*Il omet la thiamine IV, car une encéphalopathie carentielle peut coexister avec le sevrage || L'ataxie et la confusion doivent la faire évoquer.", "Il prescrit une benzodiazépine, contre-indiquée dans le sevrage || Elle est indiquée dans le sevrage.", "Il n'a pas demandé d'EEG || Il n'est pas prioritaire.", "Il n'a pas prescrit d'antibiotique || Rien ne l'indique.", "Il n'a pas demandé de ponction lombaire || Elle n'est pas prioritaire."],
 notions="N08 N14 N07", angle="piège", diff=3, ladder=L("Confusion attribuée au sevrage.", "Coexistence possible.", "Ataxie.", "Biais d'ancrage.", "Thiamine IV.", "Tout attribuer au sevrage.", "Sevrage : penser B1."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 66 ans atteint d'un syndrome de Korsakoff ne peut plus gérer ses affaires ni ses médicaments. Il vit seul à Sion.", prompt="Quelle démarche est la plus adaptée ?",
 items=["*Organiser un réseau de soutien et discuter une mesure de protection de l'adulte auprès de l'APEA || Il a perdu la capacité de gérer ses affaires.", "Le laisser seul sans aide || Il est en danger.", "Le placer d'office en prison || Ce n'est pas une mesure de soins.", "Le renvoyer sans suivi || Le risque de récidive et d'accident est élevé.", "Lui prescrire un anticholinestérasique || Il n'est pas indiqué."],
 notions="N24 N20 N23", angle="application", diff=2, ladder=L("Séquelles amnésiques.", "Incapacité de gestion.", "Vit seul.", "Protection de l'adulte.", "Réseau et APEA.", "Abandon.", "Protéger."), sources="[Code civil suisse]"),
dict(masque=False, sit="monographique", format="A", stem="Une femme de 40 ans, végétarienne équilibrée, sans alcool, consulte pour des fourmillements des pieds. Elle demande si elle risque une encéphalopathie carentielle aiguë.", prompt="Quelle réponse est la plus juste ?",
 items=["*Son risque est faible en l'absence d'alcool, de vomissements, de chirurgie bariatrique ou de dénutrition || Ces terrains exposent à la carence aiguë.", "Tout végétarien développe cette encéphalopathie || L'alimentation équilibrée apporte de la thiamine.", "Elle doit recevoir de la thiamine IV d'urgence || Rien ne l'indique.", "Ses fourmillements prouvent la carence en B1 || D'autres causes sont plus probables.", "Elle doit arrêter tout végétal || Cela n'a pas de sens."],
 notions="N02 N13", angle="piège", diff=2, ladder=L("Inquiétude.", "Terrain à risque.", "Pas de facteur de risque.", "Risque faible.", "Rassurer, chercher d'autres causes.", "Traiter à tort.", "Terrain = risque."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Vous identifiez les patients hospitalisés à risque de carence aiguë en thiamine.", prompt="Quelles situations justifient une thiamine prophylactique ? (4 réponses)",
 items=["*Sevrage alcoolique || Réserves faibles.", "*Hyperemesis gravidarum || Pertes prolongées.", "*Dénutrition sévère avant réalimentation || Risque de renutrition.", "*Vomissements prolongés après chirurgie bariatrique || Malabsorption et pertes.", "Fracture du poignet chez un sportif || Pas de risque.", "Appendicite simple chez un adulte sain || Pas de risque.", "Hypertension isolée || Pas de risque.", "Asthme stable || Pas de risque.", "Migraine || Pas de risque.", "Entorse de cheville || Pas de risque.", "Grossesse normale sans vomissement || Pas de risque particulier.", "Hypothyroïdie substituée || Pas de risque."],
 notions="N18 N02 N21", angle="application", diff=2, ladder=L("Prévention.", "Réserves épuisées.", "Terrains à risque.", "Cibler.", "Thiamine prophylactique.", "Oublier les terrains non alcooliques.", "Alcool, vomissements, dénutrition."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un patient confus est admis aux urgences.", prompt="Quels éléments orientent vers une encéphalopathie carentielle en thiamine ? (3 réponses)",
 items=["*Nystagmus || Trouble oculomoteur typique.", "*Ataxie de la marche || Atteinte cérébelleuse.", "*Dénutrition ou alcoolisme chronique || Terrain typique.", "Raideur de nuque fébrile || Elle évoque une méningite.", "Hémiparésie brutale || Elle évoque un AVC.", "Mydriase unilatérale avec coma || Elle évoque un engagement.", "Ictère et astérixis || Ils évoquent une encéphalopathie hépatique.", "Myosis serré et bradypnée || Ils évoquent un opioïde.", "Hypersalivation et myosis || Ils évoquent un organophosphoré.", "Rash pétéchial fébrile || Il évoque un méningocoque.", "Tremblement de repos || Il évoque un parkinsonisme.", "Hyperthermie et rigidité sous neuroleptique || Elles évoquent un syndrome malin."],
 notions="N06 N07 N13", angle="direct", diff=2, ladder=L("Confusion.", "Carence en B1.", "Signes et terrain.", "Diagnostic différentiel.", "Thiamine.", "Confondre avec d'autres toxidromes.", "Yeux, marche, terrain."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme alcoolique de 58 ans confus et ataxique a reçu de la thiamine IV. Le laboratoire peut doser la thiamine sur un prélèvement fait avant la perfusion.", prompt="Quel est l'intérêt de ce dosage ?",
 items=["*Confirmer a posteriori sans retarder le traitement || Le dosage ne guide pas la décision initiale.", "Décider de débuter ou non la thiamine || Le traitement ne l'attend pas.", "Remplacer l'examen clinique || Le diagnostic est clinique.", "Fixer la durée exacte du traitement || Elle se fixe sur la clinique.", "Exclure le diagnostic s'il est normal || Il peut être faussement rassurant."],
 notions="N12 N10", angle="direct", diff=2, ladder=L("Dosage de B1.", "Confirmation.", "Prélèvement avant traitement.", "Place du dosage.", "Ne pas attendre.", "Attendre le résultat.", "Traiter d'abord."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Encéphalopathie de Gayet-Wernicke : penser au terrain, donner la thiamine IV avant le glucose et sans attendre",
 notions=[
  dict(titre="Terrain et présentation", rub=["epi", "ana", "red"], comment="Cherche le terrain carentiel, car la triade manque souvent.",
   tableau=(["Terrain", "Mécanisme", "Indice"], [
     ["Alcoolisme", [("Apport et absorption réduits", "L'alcool freine l'absorption et le stockage de la thiamine.")], "Confusion attribuée à l'ivresse"],
     ["Chirurgie bariatrique", [("Malabsorption et vomissements", "Le court-circuit réduit l'absorption.")], "Vomissements prolongés"],
     ["Hyperemesis gravidarum", [("Pertes prolongées", "Les réserves s'épuisent en quelques semaines.")], "Grossesse avec vomissements"],
     ["Dénutrition, cancer, réalimentation", [("Consommation accrue", "Le glucose apporté consomme la thiamine restante.")], "Hypothermie, coma"]]),
   points=["Critères de Caine : deux sur quatre."], sources=["[Galvin, Eur J Neurol, 2010]", "[Caine, 1997]"]),
  dict(titre="Conduite d'urgence", rub=["gold", "acu"], comment="Traite d'abord, confirme ensuite.",
   arbre=[("w1", None, "Patient à risque confus, ataxique ou avec trouble oculomoteur", "Le diagnostic est clinique."),
          ("w2", "w1", "Glycémie", "Une hypoglycémie se corrige, mais après ou avec la thiamine.", "wer_aigu"),
          ("w3", "w1", "Thiamine IV à haute dose", "Elle restaure le métabolisme neuronal.", "wer_aigu"),
          ("w4", "w3", "Magnésium bas", "Le magnésium se corrige, car il active la thiamine.", "wer_aigu"),
          ("w5", "w1", "Chute, déficit focal", "Un CT cherche un hématome sous-dural."),
          ("w6", "w3", "Après la phase aiguë", "Addictologie, nutrition et suivi cognitif.", "wer_aigu")],
   points=["Jamais de glucose avant la thiamine."], sources=["[Galvin, Eur J Neurol, 2010]"]),
  dict(titre="Examens et différentiels", rub=["alt", "pos"], comment="N'attends aucun examen pour traiter.",
   tableau=(["Examen ou diagnostic", "Apport", "Pourquoi"], [
     ["IRM", "Hypersignal thalamique et mamillaire", "Une IRM normale n'exclut rien."],
     ["Dosage de thiamine", "Confirmation a posteriori", "Il ne doit pas retarder."],
     ["Hématome sous-dural", "CT", "Les chutes de l'alcoolique y exposent."],
     ["Encéphalopathie hépatique", "Astérixis, ammoniémie", "Elle coexiste souvent."]]),
   points=["La confusion de l'alcoolique n'est pas toujours l'ivresse."], sources=["[avis d'expert]"]),
  dict(titre="Évolution et suites", rub=["hos", "pro", "fol"], comment="Prévois la récupération inégale et le risque de Korsakoff.",
   tableau=(["Élément", "Contenu", "Pourquoi"], [
     ["Oculomotricité", "Récupère en heures à jours", "La dysfonction est d'abord métabolique."],
     ["Mémoire", "Récupère lentement, souvent incomplètement", "Les lésions mamillo-thalamiques persistent."],
     ["Korsakoff", "Amnésie antérograde, confabulations", "Il complique un traitement tardif."],
     ["Suites", "Addictologie, supplémentation, protection de l'adulte", "Elles préviennent la récidive et protègent le patient."]]),
   points=["Bypass : vitamines à vie."], sources=["[avis d'expert]"]),
 ],
 ssp=dict(code="F1.15", nom="Altération ou perte de conscience, coma", officiel=True, algorithme=[
  ("n1", None, "Trouble de conscience", "Le premier tri mesure la glycémie et cherche le terrain."),
  ("n2", "n1", "Terrain carentiel (alcool, dénutrition, vomissements)", "Thiamine IV avant tout glucose.", "wer_aigu", "c1"),
  ("n3", "n2", "Nystagmus, ataxie", "L'encéphalopathie de Wernicke est probable.", "wer_aigu", "c2"),
  ("n4", "n1", "Hypoglycémie", "Correction, avec thiamine si terrain à risque.", None, "c2"),
  ("n5", "n1", "Signes focaux ou chute", "CT cérébral pour un hématome ou un AVC.", None, "c3"),
  ("n6", "n1", "Fièvre, raideur", "Une méningite se cherche (même SSP).", None),
  ("n7", "n1", "Myosis, bradypnée", "Une intoxication aux opioïdes se traite par naloxone."),
  ("n8", "n3", "Amnésie persistante", "Un syndrome de Korsakoff impose un suivi et une protection.", "wer_aigu", "c4")]),
 pec=[
  dict(cle="wer_aigu", titre="Encéphalopathie de Gayet-Wernicke",
   but=["Restaurer la thiamine avant des lésions irréversibles.", "Prévenir le Korsakoff et la récidive."],
   moyens=dict(accueil=["Mesurer la glycémie et la température.", "Identifier le terrain carentiel."],
    pharma=[("Thiamine (vitamine B1)", "Par exemple 200 à 500 mg IV trois fois par jour pendant plusieurs jours ; à vérifier dans l'AIPS.", "Elle restaure le métabolisme neuronal du glucose.", "[Galvin, Eur J Neurol, 2010]"),
            ("Glucose", "Après ou avec la thiamine en cas d'hypoglycémie ; à vérifier dans l'AIPS.", "Il corrige l'hypoglycémie sans aggraver la carence.", "[avis d'expert]"),
            ("Magnésium", "Selon le déficit ; à vérifier dans l'AIPS.", "Il est cofacteur de la thiamine.", "[avis d'expert]")],
    nonpharma=[("nutrition", "Réalimentation progressive avec surveillance du phosphate.", "Elle prévient la renutrition inappropriée."),
               ("social et assurances", "Réseau addictologique, mesure de protection si besoin.", "Il prévient la récidive et protège.")],
    transversal=[("Addictologie", "Elle prend en charge la dépendance."), ("Nutrition clinique", "Elle conduit la renutrition.")]),
   urgence=(["Thiamine IV avant le glucose.", "Ne pas attendre d'examen."],
            [("d'abord", "médecin responsable", "Reconnaît le terrain et prescrit la thiamine IV."),
             ("en même temps", "infirmier·ère", "Administre la thiamine et surveille glycémie et température."),
             ("ensuite", "neurologue", "Évalue l'évolution et les séquelles.")]),
   horsUrgence=(["Poursuivre la supplémentation orale après la phase IV.", "Organiser le suivi addictologique."],
            [("d'abord", "médecin de famille", "Suit la supplémentation et l'abstinence."),
             ("ensuite", "addictologue", "Accompagne le sevrage."),
             ("puis", "assistant·e social·e", "Organise le soutien et la protection.")]),
   pronostic="Les troubles oculomoteurs régressent vite ; la mémoire récupère lentement et parfois incomplètement.",
   suivi=[("Vigilance, oculomotricité, marche", "Quotidienne", "Amélioration"), ("Phosphate, potassium, magnésium", "Quotidienne à la réalimentation", "Normaux"), ("Mémoire", "À la sortie puis à 3 mois", "Récupération")],
   sortie="Le patient sort quand la vigilance est normale, la marche sûre et le suivi addictologique organisé.",
   prevention=["Elle repose sur la réduction de la consommation d'alcool.", "Elle passe par la thiamine prophylactique chez tout patient à risque.", "Elle prévient la récidive par la supplémentation et l'abstinence."]),
 ])
AVERIFIER = ["Schéma posologique de la thiamine IV (dose, rythme, durée) selon l'AIPS et les recommandations suisses à vérifier.",
             "Proportion de patients présentant la triade complète (Harper 1986) à confirmer.",
             "Dose de thiamine prophylactique chez le patient alcoolique hospitalisé à vérifier."]
