ID = "G41.9_etat_de_mal_epilepti__F1_15-E16"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[Trinka, ILAE, Epilepsia, 2015]|L'ILAE fixe le seuil de traitement à 10 minutes pour l'état de mal focal avec altération de la conscience et à 10-15 minutes pour l'état de mal d'absences ; au-delà de 60 minutes, l'état de mal focal expose à des lésions durables.",  # N01
"epi|chiffre|1||[avis d'expert]|L'état de mal non convulsif explique une part méconnue des confusions et des comas inexpliqués, surtout chez le sujet âgé et en soins intensifs.",  # N02
"bas|mécanisme|1||[avis d'expert]|L'activité épileptique persiste sans convulsion ; après un état de mal convulsif, elle peut continuer à bas bruit.",  # N03
"ana|signe|2||[avis d'expert]|Le tableau associe confusion, mutisme, persévérations, automatismes et myoclonies discrètes des paupières ou de la face, parfois un nystagmus.",  # N04
"ana|terrain particulier|1||[avis d'expert]|Le sevrage brutal de benzodiazépines, l'arrêt d'un antiépileptique et certains médicaments déclenchent l'état de mal chez le sujet âgé.",  # N05
"exa|signe|1||[avis d'expert]|L'examen trouve une réactivité fluctuante et des secousses subtiles, sans convulsion franche.",  # N06
"red|piège|3||[avis d'expert]|Un patient qui ne se réveille pas après un état de mal convulsif traité doit avoir un EEG urgent pour chercher un état de mal non convulsif.",  # N07
"gold|examen|3||[Beniczky, Salzburg, Epilepsia, 2013]|L'EEG est indispensable ; les critères de Salzbourg retiennent des décharges à plus de 2,5 Hz, ou plus lentes si elles évoluent ou répondent au traitement.",  # N08
"alt|examen|1||[avis d'expert]|L'EEG continu en soins intensifs, l'IRM, l'ionogramme, la glycémie, les taux d'antiépileptiques et les toxiques cherchent la cause.",  # N09
"pos|diagnostic différentiel|2||[avis d'expert]|Le delirium, l'encéphalopathie métabolique ou toxique, la catatonie, l'ictus amnésique et l'état postcritique imitent l'état de mal non convulsif.",  # N10
"acu|décision|2||[Beniczky, Salzburg, Epilepsia, 2013]|Une benzodiazépine IV sous EEG qui améliore la clinique et le tracé soutient le diagnostic.",  # N11
"acu|molécule|2||[avis d'expert]|Le traitement commence par une benzodiazépine, puis un antiépileptique IV peu sédatif (lévétiracétam, valproate, lacosamide) ; l'anesthésie générale s'évite chez le patient non comateux.",  # N12
"acu|molécule|1||[avis d'expert]|L'état de mal d'absences répond à la benzodiazépine IV ou au valproate ; la carbamazépine et la phénytoïne aggravent les absences.",  # N13
"acu|posologie|1||[AIPS Swissmedic]|Les doses de charge de lévétiracétam, de valproate et de lacosamide IV se calculent au poids ; à vérifier dans l'AIPS.",  # N14
"hos|complication|1||[avis d'expert]|L'intubation et le coma thérapeutique exposent le sujet âgé non comateux à plus de risques que l'état de mal lui-même.",  # N15
"pro|pronostic|2||[avis d'expert]|Le pronostic dépend surtout de la cause et du niveau de conscience : sombre dans le coma, bon dans l'état de mal d'absences.",  # N16
"hos|piège|2||[avis d'expert]|La céfépime en insuffisance rénale, le sevrage de benzodiazépines, le lithium et l'arrêt des antiépileptiques sont des causes iatrogènes à chercher.",  # N17
"chr|décision|1||[avis d'expert]|Après le contrôle, on traite la cause et on ajuste le traitement de fond.",  # N18
"sur|examen|1||[avis d'expert]|L'EEG se répète jusqu'à la disparition des décharges, puis la cognition se réévalue.",  # N19
"fol|contexte suisse|1|S|[Tox Info Suisse]|En Suisse, Tox Info Suisse répond au 145 pour orienter une intoxication suspecte.",  # N20
"fol|terrain particulier|1||[avis d'expert]|Un état de mal d'absences peut apparaître de novo chez une personne âgée sans épilepsie connue.",  # N21
"def|critère|1||[Trinka, ILAE, Epilepsia, 2015]|L'ILAE distingue l'état de mal non convulsif avec coma et sans coma, ce dernier comprenant les formes focales et l'état de mal d'absences.",  # N22
"bas|mécanisme|1||[avis d'expert]|Les récepteurs GABA-A s'internalisent pendant l'état de mal, ce qui rend les benzodiazépines moins efficaces avec le temps.",  # N23
"sur|piège|1||[avis d'expert]|Les ondes triphasiques d'une encéphalopathie métabolique peuvent ressembler à un état de mal et compliquer l'interprétation.",  # N24
"fol|décision|1||[avis d'expert]|Un hôpital sans EEG transfère le patient vers un centre capable de l'enregistrer et de l'interpréter en urgence.",  # N25
]
ANGLES = [
"Confusion inexpliquée + myoclonies subtiles = EEG.",
"Pas de réveil après convulsions = EEG.",
"Benzodiazépine IV sous EEG.",
"Pas d'anesthésie chez le non-comateux.",
"Chercher la cause iatrogène.",
"Absences : pas de carbamazépine.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une femme de 78 ans, à Bulle, est confuse depuis 2 jours. Elle répète les mêmes mots, répond lentement et ses paupières battent de petites secousses. Elle a cessé brutalement son lorazépam il y a 3 jours. Elle n'a jamais fait de crise.", prompt="Quel diagnostic devez-vous évoquer en premier ?",
 items=["*Un état de mal non convulsif || Confusion, myoclonies palpébrales et sevrage de benzodiazépine.", "Une maladie d'Alzheimer || Elle ne débute pas en 2 jours.", "Un AVC ischémique || Les myoclonies et le sevrage orientent ailleurs.", "Une dépression sévère || Les myoclonies l'excluent.", "Un ictus amnésique || Il ne donne ni myoclonies ni persévérations prolongées."],
 notions="N04 N05 N21 N02 N01", angle="application", diff=2, ladder=L("Confusion aiguë.", "Activité épileptique.", "Myoclonies, sevrage.", "Hypothèse.", "État de mal non convulsif.", "Démence.", "Confuse + secousses = EEG."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 2, 4), stem="La glycémie et l'ionogramme de cette patiente sont normaux.", prompt="Quel examen confirme le diagnostic ?",
 items=["*Un EEG en urgence || Il est indispensable au diagnostic.", "Un scanner cérébral seul || Il ne voit pas l'activité épileptique.", "Une ponction lombaire || Elle cherche une infection.", "Un dosage de la TSH || Il n'est pas urgent.", "Une IRM seule || Elle ne voit pas les décharges."],
 notions="N08 N10", angle="direct", diff=1, ladder=L("Bilan normal.", "Électrophysiologie.", "Activité cérébrale.", "Examen clé.", "EEG.", "Scanner.", "Sans EEG, pas de diagnostic."), sources="[Beniczky, Salzburg, 2013]"),
dict(format="A", serie=("S1", 3, 4), stem="L'EEG montre des pointes-ondes généralisées continues à 3 Hz.", prompt="Quel traitement donnez-vous d'abord ?",
 items=["*Une benzodiazépine IV sous contrôle EEG || Elle traite et confirme le diagnostic.", "Une intubation et un coma au propofol || Elle n'est pas indiquée chez la patiente non comateuse.", "De la carbamazépine || Elle aggrave les absences.", "De la phénytoïne || Elle aggrave les absences.", "Un neuroleptique || Il n'est pas indiqué."],
 notions="N11 N12 N13 N08", angle="application", diff=2, ladder=L("Pointes-ondes continues.", "État de mal d'absences.", "3 Hz.", "Premier traitement.", "Benzodiazépine IV.", "Coma induit.", "Benzodiazépine sous EEG."), sources="[Beniczky, Salzburg, 2013]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Après la benzodiazépine, la patiente répond et le tracé se normalise.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'amélioration clinique et électrique soutient le diagnostic. || C'est un critère de Salzbourg.", "V: Le sevrage de benzodiazépine explique probablement l'épisode. || Il est un déclencheur connu.", "F: Une intubation avec coma thérapeutique reste nécessaire. || Elle exposerait à plus de risques.", "F: La phénytoïne serait le meilleur traitement de fond. || Elle aggrave les absences."],
 notions="N11 N15 N13 N17", angle="application", diff=2, ladder=L("Réponse.", "Confirmation.", "Sevrage.", "Suite.", "Diagnostic confirmé.", "Coma induit.", "Réponse = preuve."), sources="[Beniczky, Salzburg, 2013]"),
dict(format="A", stem="Un homme de 52 ans a convulsé 25 minutes avant de répondre au lorazépam puis au lévétiracétam IV. Les convulsions ont cessé il y a 45 minutes, mais il reste comateux, avec de petites secousses du coin de la bouche.", prompt="Quelle conduite est prioritaire ?",
 items=["*Un EEG urgent pour chercher un état de mal persistant || Le non-réveil doit faire chercher une activité infraclinique.", "Attendre le réveil spontané jusqu'au lendemain || Il retarderait le traitement.", "Conclure à un coma postcritique simple || Il se réveille d'habitude plus vite.", "Arrêter tous les antiépileptiques || Il risquerait une récidive.", "Faire une ponction lombaire d'abord || L'EEG est prioritaire."],
 notions="N07 N03", angle="piège", diff=2, ladder=L("Pas de réveil.", "Activité infraclinique.", "Secousses subtiles.", "Danger.", "EEG urgent.", "Postcritique.", "Pas réveillé = EEG."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 70 ans en insuffisance rénale reçoit de la céfépime pour une pneumonie. Au 4e jour, elle devient confuse, avec des myoclonies multifocales.", prompt="Quelle hypothèse évoquez-vous d'abord ?",
 items=["*Une neurotoxicité de la céfépime, possiblement avec état de mal non convulsif || La céfépime s'accumule en insuffisance rénale.", "Une démence débutante || Le début est aigu.", "Une méningite à pneumocoque || Elle donne fièvre et syndrome méningé.", "Un AVC || Les myoclonies multifocales orientent ailleurs.", "Une dépression || Elle ne donne pas de myoclonies."],
 notions="N17 N10", angle="piège", diff=3, ladder=L("Confusion sous antibiotique.", "Iatrogénie.", "Céfépime, rein.", "Hypothèse.", "Neurotoxicité.", "Démence.", "Céfépime + rein = EEG."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Vous enseignez la définition ILAE 2015 de l'état de mal épileptique.", prompt="À partir de quelle durée traite-t-on un état de mal focal avec altération de la conscience ?",
 items=["*10 minutes || C'est le seuil t1 de l'ILAE.", "5 minutes || Il concerne l'état de mal tonico-clonique.", "30 minutes || C'est le seuil t2 du tonico-clonique.", "60 minutes || C'est le seuil t2 du focal.", "24 heures || Il est bien trop long."],
 notions="N01 N22", angle="direct", diff=2, ladder=L("Définition.", "ILAE 2015.", "Focal.", "Seuil.", "10 minutes.", "5 minutes.", "Focal : 10 et 60 minutes."), sources="[Trinka, ILAE, 2015]"),
dict(format="A", stem="Un homme de 61 ans cirrhotique est confus et somnolent. L'EEG montre des ondes triphasiques diffuses. Son ammoniémie est élevée.", prompt="Quelle interprétation est la plus prudente ?",
 items=["*Une encéphalopathie hépatique est probable, mais un état de mal reste à discuter avec le neurologue || Les ondes triphasiques peuvent imiter un état de mal.", "Un état de mal certain || Les ondes triphasiques ne le prouvent pas.", "Une démence vasculaire || Le début est aigu.", "Un EEG normal pour l'âge || Il est anormal.", "Une catatonie || L'EEG serait normal."],
 notions="N10 N24", angle="application", diff=3, ladder=L("Confusion du cirrhotique.", "Encéphalopathie.", "Ondes triphasiques.", "Interprétation.", "Hépatique probable.", "État de mal certain.", "Triphasique ≠ preuve."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 74 ans non comateuse reste confuse avec des décharges continues à l'EEG malgré deux doses de benzodiazépine IV.", prompt="Quelle étape suivante choisissez-vous ?",
 items=["*Un antiépileptique IV peu sédatif comme le lévétiracétam || Il traite sans exposer au coma induit.", "Une intubation et un coma au thiopental || Le risque dépasse le bénéfice ici.", "Une troisième et quatrième dose de benzodiazépine || Elles exposent à la dépression respiratoire.", "De la carbamazépine orale || Elle agit trop lentement.", "Une simple surveillance || Les décharges persistent."],
 notions="N12 N15 N14", angle="application", diff=2, ladder=L("Échec des benzodiazépines.", "Deuxième ligne.", "Non comateuse.", "Choix.", "Lévétiracétam IV.", "Coma induit.", "Pas d'anesthésie si éveillée."), sources="[avis d'expert]"),
dict(format="A", stem="Vous lisez avec un collègue l'EEG d'un patient confus.", prompt="Selon les critères de Salzbourg, quel aspect suffit au diagnostic chez un patient sans encéphalopathie épileptique connue ?",
 items=["*Des décharges épileptiformes à plus de 2,5 Hz || C'est le critère principal.", "Un ralentissement diffus thêta || Il est non spécifique.", "Des ondes triphasiques isolées || Elles ne suffisent pas.", "Un rythme alpha postérieur normal || Il est normal.", "Des pointes isolées toutes les minutes || Elles ne suffisent pas."],
 notions="N08 N22", angle="direct", diff=3, ladder=L("Lecture d'EEG.", "Critères.", "Salzbourg.", "Fréquence.", "> 2,5 Hz.", "Ralentissement.", "Plus de 2,5 Hz."), sources="[Beniczky, Salzburg, 2013]"),
dict(format="A", stem="Une jeune femme de 19 ans avec épilepsie-absences de l'adolescent a reçu de la carbamazépine par erreur. Elle est depuis 2 jours lente, distraite, avec des clignements continus.", prompt="Quelle explication retenez-vous ?",
 items=["*La carbamazépine a aggravé les absences jusqu'à un état de mal || Elle aggrave les épilepsies généralisées.", "Une intoxication alcoolique || Rien ne l'indique.", "Un trouble anxieux || Les clignements continus sont épileptiques.", "Une encéphalite || La chronologie désigne le médicament.", "Une hypoglycémie || Elle ne dure pas 2 jours."],
 notions="N13 N17", angle="piège", diff=2, ladder=L("Erreur de traitement.", "Aggravation iatrogène.", "Carbamazépine.", "Mécanisme.", "Absences aggravées.", "Anxiété.", "Pas de carbamazépine."), sources="[avis d'expert]"),
dict(format="A", stem="Vous comparez trois patients en état de mal sans convulsion : une jeune femme en état d'absences, un homme âgé confus sur sevrage, un patient comateux après anoxie cérébrale.", prompt="Quel facteur pèse le plus sur leur pronostic ?",
 items=["*La cause et le niveau de conscience || Le coma anoxique a le pronostic le plus sombre.", "La fréquence des décharges seule || Elle pèse moins que la cause.", "L'âge seul || Il ne suffit pas.", "La couleur des myoclonies || Elle n'existe pas.", "Le jour de la semaine || Il est sans rapport."],
 notions="N16 N02", angle="direct", diff=2, ladder=L("Comparaison.", "Pronostic.", "Cause, conscience.", "Facteur clé.", "Cause et coma.", "Âge.", "La cause décide."), sources="[avis d'expert]"),
dict(format="A", stem="Un interne demande pourquoi il faut traiter vite un état de mal, même sans convulsion.", prompt="Quel mécanisme justifie l'urgence ?",
 items=["*L'internalisation des récepteurs GABA-A réduit l'effet des benzodiazépines avec le temps || L'efficacité baisse.", "Les benzodiazépines deviennent toxiques après 1 heure || Ce n'est pas le mécanisme.", "Le foie élimine plus vite les médicaments || Ce n'est pas le mécanisme.", "La barrière hémato-encéphalique se ferme || Ce n'est pas le mécanisme.", "Le cerveau cesse de consommer du glucose || C'est faux."],
 notions="N23 N11", angle="direct", diff=3, ladder=L("Urgence.", "Pharmacodynamie.", "GABA-A.", "Mécanisme.", "Internalisation.", "Toxicité.", "Plus tard = moins efficace."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 67 ans sous lithium est confuse, tremble et présente des myoclonies. Sa famille craint une prise excessive de comprimés.", prompt="Quelle démarche est la plus adaptée ?",
 items=["*Doser la lithémie, faire un EEG et contacter Tox Info Suisse au 145 || La cause toxique se cherche avec l'EEG.", "Donner de l'halopéridol || Il aggraverait la situation.", "Attendre 48 heures || Le risque est grave.", "Augmenter le lithium || Il est peut-être en excès.", "Faire uniquement une IRM || Elle ne répond pas seule."],
 notions="N20 N09 N17", angle="application", diff=2, ladder=L("Confusion sous lithium.", "Intoxication.", "Myoclonies.", "Démarche.", "Lithémie, EEG, 145.", "Halopéridol.", "Toxique + EEG."), sources="[Tox Info Suisse]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez l'état de mal épileptique non convulsif.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Son diagnostic exige un EEG. || La clinique ne suffit pas.", "V: Des myoclonies palpébrales subtiles peuvent l'accompagner. || Elles sont évocatrices.", "F: Il s'accompagne toujours de convulsions visibles. || Il est par définition non convulsif.", "F: Un EEG normal pendant les symptômes le confirme. || Il l'exclut."],
 notions="N08 N04 N01 N06", angle="direct", diff=1, ladder=L("Révision.", "Définition.", "EEG.", "Pièges.", "EEG, myoclonies.", "Convulsions.", "EEG indispensable."), sources="[Beniczky, Salzburg, 2013]"),
dict(format="Kprim", stem="Un homme de 69 ans a récupéré d'une confusion de 3 jours avec décharges continues à l'EEG, après traitement IV.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une IRM et un bilan biologique cherchent la cause. || La cause guide le pronostic.", "V: Son traitement de fond doit s'ajuster. || Il prévient la récidive.", "F: Aucun EEG de contrôle n'est utile. || Il vérifie la disparition des décharges.", "F: Le pronostic est toujours excellent quelle que soit la cause. || Il dépend de la cause."],
 notions="N18 N09 N19 N16", angle="application", diff=2, ladder=L("Après contrôle.", "Suite.", "Cause, fond.", "Suivi.", "IRM, ajustement, EEG.", "Pronostic toujours bon.", "Cause + suivi EEG."), sources="[avis d'expert]"),
dict(format="Kprim", stem="L'équipe de garde discute du traitement d'une femme de 82 ans confuse, non comateuse, avec décharges continues à l'EEG.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un essai de benzodiazépine IV sous EEG se justifie. || Il traite et confirme.", "V: Un antiépileptique IV peu sédatif suit en cas d'échec. || Il évite le coma induit.", "F: Le coma barbiturique s'impose d'emblée. || Il expose à plus de risques.", "F: La carbamazépine est le meilleur choix dans un état de mal d'absences. || Elle aggrave les absences."],
 notions="N12 N15 N13 N11", angle="piège", diff=2, ladder=L("Garde.", "Stratégie.", "Sujet âgé.", "Pièges.", "Benzodiazépine puis IV.", "Coma barbiturique.", "Doux chez le non-comateux."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un patient de 75 ans est confus sans cause évidente.", prompt="Quels signes doivent faire demander un EEG en urgence ? (3 réponses)",
 items=["*Myoclonies palpébrales ou faciales subtiles || Elles évoquent une activité épileptique.", "*Réactivité fluctuante avec persévérations || Elle est évocatrice.", "*Nystagmus ou déviation du regard intermittents || Ils sont évocateurs.", "Fièvre isolée || Elle oriente vers une infection.", "Constipation || Elle n'oriente pas.", "Hypertension artérielle stable || Elle n'oriente pas.", "Oubli progressif depuis 2 ans || Il évoque une démence.", "Douleur abdominale || Elle n'oriente pas.", "Rétention urinaire || Elle n'oriente pas.", "Tremblement de repos ancien || Il évoque un parkinson.", "Toux productive || Elle évoque une infection.", "Œdèmes des chevilles || Ils n'orientent pas."],
 notions="N04 N06", angle="direct", diff=2, ladder=L("Confusion.", "Signes subtils.", "EEG.", "Lesquels.", "Myoclonies, fluctuations, nystagmus.", "Fièvre.", "Subtil = EEG."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un neurologue cherche la cause d'un état de mal sans convulsion chez une patiente âgée.", prompt="Quels déclencheurs iatrogènes cherchez-vous ? (3 réponses)",
 items=["*Sevrage brutal de benzodiazépines || Il abaisse le seuil épileptogène.", "*Céfépime en insuffisance rénale || Elle s'accumule.", "*Arrêt d'un antiépileptique || Il expose à la récidive.", "Paracétamol à dose usuelle || Il n'est pas épileptogène.", "Vitamine D || Elle n'est pas épileptogène.", "Amlodipine || Elle n'est pas épileptogène.", "Oméprazole || Il n'est pas épileptogène.", "Insuline bien dosée || Elle n'est pas en cause.", "Statine || Elle n'est pas épileptogène.", "Lévothyroxine à dose stable || Elle n'est pas en cause.", "Macrogol || Il n'est pas épileptogène.", "Collyre lubrifiant || Il n'est pas en cause."],
 notions="N17 N05", angle="application", diff=2, ladder=L("Cause.", "Iatrogénie.", "Médicaments.", "Lesquels.", "Sevrage, céfépime, arrêt.", "Paracétamol.", "Revoir les médicaments."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 58 ans reste comateux après des convulsions dans un petit hôpital régional qui ne dispose pas d'EEG.", prompt="Quelle décision prenez-vous ?",
 items=["*Le transférer vers un centre capable d'enregistrer un EEG en urgence || Le diagnostic d'état de mal persistant en dépend.", "Attendre son réveil sur place 48 heures || Le retard aggrave le pronostic.", "Lui donner de l'halopéridol || Il n'est pas indiqué.", "Conclure à une mort cérébrale || Rien ne le permet.", "Faire seulement un scanner et rentrer || Il ne cherche pas l'activité épileptique."],
 notions="N25 N07", angle="application", diff=2, ladder=L("Pas d'EEG sur place.", "Organisation.", "Coma.", "Décision.", "Transfert.", "Attendre.", "Pas d'EEG = transférer."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="État de mal non convulsif : l'évoquer devant une confusion ou un coma inexpliqués, le prouver par EEG, le traiter par benzodiazépine puis antiépileptique IV peu sédatif, chercher la cause iatrogène et ne pas anesthésier le patient non comateux",
 notions=[
  dict(titre="Évoquer", rub=["def", "ana", "exa", "epi"], comment="Pense à l'état de mal devant toute confusion inexpliquée.",
   tableau=(["Situation", "Indice", "Seuil ILAE"], [
     ["Confusion du sujet âgé", "Persévérations, myoclonies palpébrales", "Focal : 10 min (t1), 60 min (t2)"],
     ["Absences", "Clignements, lenteur", "10-15 min"],
     ["Après convulsions", _T("Pas de réveil", "L'activité peut persister à bas bruit."), "EEG urgent"]]),
   points=["Avec ou sans coma."], sources=["[Trinka, ILAE, 2015]"]),
  dict(titre="Prouver", rub=["red", "gold", "alt", "pos"], comment="Fait l'EEG et élimine les imitateurs.",
   tableau=(["Élément", "Critère", "Piège"], [
     ["EEG", "> 2,5 Hz", "Indispensable"],
     ["Test benzodiazépine", "Amélioration clinique et EEG", _T("Sédation", "Elle peut masquer la réponse.")],
     ["Ondes triphasiques", "Encéphalopathie métabolique", "Elles imitent l'état de mal"]]),
   points=["Sans EEG : transférer."], sources=["[Beniczky, Salzburg, 2013]"]),
  dict(titre="Traiter", rub=["acu", "chr", "hos"], comment="Traite sans nuire au patient non comateux.",
   arbre=[("t1", None, "État de mal non convulsif", "L'efficacité des benzodiazépines baisse avec le temps."),
          ("t2", "t1", "Première ligne", "Benzodiazépine IV sous EEG.", "emnc"),
          ("t3", "t2", "Échec", "Lévétiracétam, valproate ou lacosamide IV.", "emnc"),
          ("t4", "t3", "Non comateux", "Pas d'anesthésie générale.", "emnc"),
          ("t5", "t1", "Absences", "Pas de carbamazépine ni de phénytoïne.", "emnc")],
   points=["Traiter la cause."], sources=["[avis d'expert]"]),
  dict(titre="Cause et pronostic", rub=["pro", "sur", "fol"], comment="Cherche la cause, qui fait le pronostic.",
   tableau=(["Cause", "Exemple", "Action"], [
     ["Iatrogène", "Céfépime, sevrage, lithium", _T("Arrêter, doser", "Tox Info Suisse au 145 si intoxication.")],
     ["Structurelle", "AVC, tumeur", "IRM"],
     ["Anoxie", "Coma post-arrêt", "Pronostic sombre"]]),
   points=["EEG de contrôle jusqu'à normalisation."], sources=["[avis d'expert]"]),
 ],
 ssp=dict(code="S7.10", nom="Secousses musculaires, fasciculations, convulsions, crise épileptique et état de mal épileptique", officiel=True, algorithme=[
  ("n1", None, "Confusion ou coma inexpliqués", "L'EEG se demande tôt."),
  ("n2", "n1", "EEG sans décharge", "Delirium ou encéphalopathie : chercher la cause.", None, "c2"),
  ("n3", "n1", "Décharges > 2,5 Hz", "État de mal non convulsif.", "emnc", "c2"),
  ("n4", "n3", "Première ligne", "Benzodiazépine IV sous EEG.", "emnc", "c3"),
  ("n5", "n4", "Échec", "Antiépileptique IV peu sédatif.", "emnc", "c3"),
  ("n6", "n3", "Cause", "Iatrogène, structurelle, métabolique.", "emnc", "c4"),
  ("n7", "n1", "Pas de réveil après convulsions", "EEG urgent.", "emnc", "c1")]),
 pec=[
  dict(cle="emnc", titre="État de mal non convulsif",
   but=["Arrêter l'activité épileptique sans iatrogénie.", "Trouver et traiter la cause."],
   moyens=dict(accueil=["Assurer voies aériennes, glycémie et surveillance.", "Revoir les médicaments récents et arrêtés.", "Informer les proches."],
    pharma=[("Lorazépam IV (benzodiazépine)", "Dose selon poids ; à vérifier dans l'AIPS.", "Il traite et confirme le diagnostic.", "[avis d'expert]"),
            ("Lévétiracétam IV (antiépileptique)", "Dose de charge selon poids ; à vérifier dans l'AIPS.", "Il traite sans trop endormir le patient.", "[avis d'expert]"),
            ("Valproate IV (antiépileptique)", "Dose de charge selon poids ; à vérifier dans l'AIPS.", "Il traite aussi l'état de mal d'absences.", "[avis d'expert]")],
    nonpharma=[("soins infirmiers", "Surveillance de la vigilance, de la respiration et des chutes.", "Elle détecte la dépression respiratoire."),
               ("autre", "EEG continu en soins intensifs si coma.", "Il guide le traitement."),
               ("éducation thérapeutique", "Prévenir le sevrage brutal de benzodiazépines.", "Elle évite la récidive.")],
    transversal=[("Néphrologie", "Elle adapte les antibiotiques à la fonction rénale."), ("Pharmacologie clinique", "Elle aide à repérer les causes iatrogènes.")]),
   urgence=(["EEG dès que possible.", "Pas de coma induit chez le non-comateux."],
            [("d'abord", "médecin responsable", "Stabilise, dose la glycémie et revoit les médicaments."),
             ("en même temps", "neurologue", "Demande et lit l'EEG en urgence."),
             ("ensuite", "médecin responsable", "Donne la benzodiazépine IV sous EEG."),
             ("puis", "neurologue", "Ajoute un antiépileptique IV peu sédatif si échec."),
             ("puis", "intensiviste", "Prend en charge le patient comateux sous EEG continu.")]),
   horsUrgence=(["Ajustement du traitement de fond.", "EEG de contrôle."],
            [("d'abord", "neurologue", "Ajuste le traitement de fond."),
             ("ensuite", "médecin de famille", "Évite les déclencheurs iatrogènes."),
             ("puis", "neurologue", "Contrôle l'EEG et la cognition.")]),
   pronostic="Le pronostic dépend de la cause : bon dans l'état de mal d'absences, sombre dans le coma anoxique.",
   suivi=[("EEG", "Jusqu'à disparition des décharges", "Tracé sans décharge"), ("Vigilance", "Toutes les heures en aigu", "Éveil"), ("Cognition", "Après résolution", "Retour à l'état antérieur")],
   sortie="Le patient sort après résolution clinique et électrique et traitement de la cause.",
   prevention=["Elle évite le sevrage brutal de benzodiazépines.", "Elle adapte la céfépime à la fonction rénale.", "Elle maintient le traitement antiépileptique."]),
 ])
AVERIFIER = ["Doses de charge IV de lorazépam, de lévétiracétam, de valproate et de lacosamide à vérifier dans l'AIPS.", "Formulation exacte des critères de Salzbourg (Beniczky 2013) à relire avant publication."]
