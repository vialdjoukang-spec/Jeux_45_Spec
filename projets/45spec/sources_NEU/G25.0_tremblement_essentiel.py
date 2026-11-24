ID = "G25.0__S7_3-E01"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[Bhatia, MDS, Mov Disord, 2018]|Le tremblement essentiel est un tremblement d'action isolé et bilatéral des membres supérieurs, présent depuis au moins 3 ans, sans dystonie, ataxie ni parkinsonisme.",  # N01
"def|critère|1||[Bhatia, MDS, Mov Disord, 2018]|Le « tremblement essentiel plus » ajoute des signes discrets d'importance incertaine, comme une marche en tandem perturbée ou un tremblement de repos.",  # N02
"epi|chiffre|1||[avis d'expert]|Il compte parmi les troubles du mouvement les plus fréquents ; sa prévalence augmente avec l'âge et une histoire familiale se retrouve souvent.",  # N03
"bas|mécanisme|1||[avis d'expert]|Un dysfonctionnement du circuit cérébello-thalamo-cortical l'entretient ; le noyau ventral intermédiaire (VIM) du thalamus relaie ce circuit.",  # N04
"ana|signe|2||[avis d'expert]|L'alcool réduit souvent le tremblement de façon transitoire, tandis que le stress, la fatigue et la caféine l'aggravent.",  # N05
"ana|symptôme|2||[avis d'expert]|Le tremblement est postural et cinétique ; il gêne l'écriture, le verre porté à la bouche et la cuillère, et peut atteindre la tête ou la voix.",  # N06
"exa|signe|2||[avis d'expert]|L'examen cherche le tremblement bras tendus, au dessin de spirale et au verre d'eau, et vérifie l'absence de bradykinésie et de rigidité.",  # N07
"pos|diagnostic différentiel|3||[avis d'expert]|Le tremblement parkinsonien est de repos, asymétrique et s'accompagne de bradykinésie et de rigidité ; l'écriture devient micrographique.",  # N08
"pos|diagnostic différentiel|2||[avis d'expert]|Un tremblement physiologique exagéré se cherche avant tout : hyperthyroïdie, lithium, valproate, bêta-2-mimétiques, amiodarone, antidépresseurs, café, sevrage alcoolique.",  # N09
"red|piège|1||[avis d'expert]|Un tremblement unilatéral, brutal ou associé à d'autres signes neurologiques fait chercher une cause secondaire ; avant 40 ans, une maladie de Wilson se cherche.",  # N10
"gold|examen|2||[avis d'expert]|Le diagnostic est clinique ; une TSH et une revue des médicaments suffisent en général.",  # N11
"alt|examen|1||[avis d'expert]|La scintigraphie des transporteurs de la dopamine (DaTSCAN) est normale dans le tremblement essentiel et sert en cas de doute avec un syndrome parkinsonien.",  # N12
"acu|décision|1||[Zesiewicz, AAN, Neurology, 2011]|Le traitement se justifie seulement si le tremblement gêne la vie quotidienne ou sociale.",  # N13
"chr|molécule|3||[Zesiewicz, AAN, Neurology, 2011]|Le propranolol et la primidone sont les deux traitements de premier choix, au plus haut niveau de recommandation de l'AAN.",  # N14
"chr|posologie|1||[AIPS Swissmedic]|Le propranolol s'augmente progressivement ; la primidone commence à très faible dose le soir pour limiter nausées et ataxie ; doses à vérifier dans l'AIPS.",  # N15
"chr|molécule|1||[Zesiewicz, AAN, Neurology, 2011]|Le topiramate et la gabapentine sont probablement efficaces en second choix ; la toxine botulique peut traiter le tremblement de la tête ou de la voix.",  # N16
"chr|décision|2||[Zesiewicz, AAN, 2011 ; Elias, NEJM, 2016]|Un tremblement invalidant et réfractaire relève de la stimulation cérébrale profonde du VIM ou d'une thalamotomie, y compris par ultrasons focalisés guidés par IRM.",  # N17
"hos|complication|1||[AIPS Swissmedic]|Le propranolol ralentit le cœur, fatigue et peut masquer les signes d'une hypoglycémie.",  # N18
"hos|piège|2||[AIPS Swissmedic]|Le propranolol se contre-indique dans l'asthme et le bloc auriculo-ventriculaire ; la primidone endort et déséquilibre le sujet âgé.",  # N19
"pro|pronostic|1||[avis d'expert]|L'évolution est lentement progressive ; elle ne réduit pas l'espérance de vie mais peut devenir invalidante.",  # N20
"sur|examen|1||[avis d'expert]|Le suivi évalue l'écriture, la spirale et les gestes quotidiens, et contrôle la fréquence cardiaque sous propranolol.",  # N21
"fol|contexte suisse|1|S|[OPAS art. 6]|En Suisse, l'ergothérapie prescrite par le médecin est remboursée par l'assurance obligatoire ; elle adapte couverts lestés et gestes.",  # N22
"fol|prévention|1||[avis d'expert]|Le patient réduit la caféine et gère le stress pour limiter les aggravations.",  # N23
"hos|complication|1||[avis d'expert]|L'automédication par l'alcool expose à la dépendance et ne constitue jamais un traitement.",  # N24
"pos|diagnostic différentiel|1||[Bhatia, MDS, Mov Disord, 2018]|Le tremblement dystonique s'accompagne de postures dystoniques et peut céder à un geste antagoniste.",  # N25
]
ANGLES = [
"Bilatéral, d'action, ≥ 3 ans, alcool-sensible = essentiel.",
"Repos + bradykinésie = parkinson.",
"Propranolol ou primidone en premier.",
"Asthme = primidone, pas de propranolol.",
"Chercher médicaments et thyroïde.",
"Réfractaire = stimulation du VIM.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un enseignant retraité de 62 ans, à Yverdon, tremble des deux mains depuis 6 ans. Il renverse son café et son écriture devient illisible. Un verre de vin le calme une heure. Son père tremblait aussi.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Un tremblement essentiel || Tremblement d'action bilatéral, ancien, familial et sensible à l'alcool.", "Une maladie de Parkinson || Elle donne un tremblement de repos asymétrique.", "Un tremblement cérébelleux || Il s'accompagne d'ataxie.", "Un tremblement dystonique || Il s'accompagne de postures dystoniques.", "Une hyperthyroïdie || Elle se vérifie mais l'histoire est ancienne et familiale."],
 notions="N01 N06 N05 N03", angle="application", diff=1, ladder=L("Tremblement des mains.", "Tremblement d'action.", "Alcool, famille.", "Profil.", "Tremblement essentiel.", "Parkinson.", "Action + alcool = essentiel."), sources="[Bhatia, MDS, 2018]"),
dict(format="A", serie=("S1", 2, 4), stem="L'examen montre un tremblement bras tendus et au dessin de spirale, sans rigidité ni lenteur. Il ne prend aucun médicament.", prompt="Quel examen demandez-vous ?",
 items=["*Une TSH || Elle exclut une hyperthyroïdie ; le reste du diagnostic est clinique.", "Une IRM cérébrale || Elle n'apporte rien sans signe d'alerte.", "Un DaTSCAN || Il se réserve au doute avec un parkinsonisme.", "Un EEG || Il est inutile.", "Une ponction lombaire || Rien ne l'indique."],
 notions="N11 N09 N07", angle="direct", diff=1, ladder=L("Examen typique.", "Bilan minimal.", "Pas de parkinsonisme.", "Cause à exclure.", "TSH.", "IRM.", "Clinique + TSH."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 3, 4), stem="Le tremblement l'empêche d'écrire et de manger en public. Il n'a ni asthme ni trouble de la conduction cardiaque.", prompt="Quel traitement proposez-vous en premier ?",
 items=["*Le propranolol, augmenté progressivement || Il est un premier choix de niveau élevé.", "La lévodopa || Elle traite le parkinson.", "Le clonazépam || Il est de faible niveau de preuve et expose à la dépendance.", "La stimulation cérébrale profonde d'emblée || Elle se réserve aux formes réfractaires.", "Aucun traitement, car il ne guérit pas || La gêne justifie un traitement."],
 notions="N14 N13 N15", angle="application", diff=1, ladder=L("Gêne fonctionnelle.", "Traitement.", "Pas de contre-indication.", "Premier choix.", "Propranolol.", "Lévodopa.", "Propranolol ou primidone."), sources="[Zesiewicz, AAN, 2011]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Vous débutez le propranolol chez cet homme.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Il peut ralentir la fréquence cardiaque et fatiguer. || Ce sont des effets attendus.", "V: Il serait contre-indiqué en cas d'asthme. || Il provoque un bronchospasme.", "F: Un verre d'alcool par jour remplace utilement le traitement. || L'alcool expose à la dépendance.", "F: La primidone ne peut jamais remplacer le propranolol. || Elle est l'autre premier choix."],
 notions="N18 N19 N05 N14", angle="piège", diff=2, ladder=L("Bêtabloquant.", "Tolérance.", "Cœur, bronches.", "Alternatives.", "Primidone.", "Alcool.", "Bradycardie, asthme."), sources="[AIPS Swissmedic ; Zesiewicz, AAN, 2011]"),
dict(masque=False, sit="monographique", format="A", stem="Une femme de 58 ans atteinte de tremblement essentiel gênant souffre d'un asthme traité.", prompt="Quel traitement choisissez-vous ?",
 items=["*La primidone à faible dose le soir || Elle est l'autre premier choix, sans effet bronchique.", "Le propranolol || Il est contre-indiqué dans l'asthme.", "Le sotalol || C'est aussi un bêtabloquant.", "L'halopéridol || Il n'a pas d'indication.", "La lévodopa || Elle traite le parkinson."],
 notions="N19 N14 N15", angle="piège", diff=2, ladder=L("Asthme.", "Choix du traitement.", "Bêtabloquant.", "Contre-indication.", "Primidone.", "Propranolol.", "Asthme = primidone."), sources="[Zesiewicz, AAN, 2011]"),
dict(format="A", stem="Un homme de 70 ans tremble de la main droite au repos, bras posé sur la cuisse. Le tremblement disparaît quand il prend un objet. Il marche à petits pas et ses gestes alternatifs ralentissent progressivement.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Une maladie de Parkinson || Tremblement de repos asymétrique avec bradykinésie.", "Un tremblement essentiel || Il est d'action et bilatéral.", "Un tremblement physiologique exagéré || Il est d'action et symétrique.", "Un tremblement cérébelleux || Il est intentionnel.", "Un tremblement psychogène || Il varie et se distrait."],
 notions="N08 N07", angle="application", diff=2, ladder=L("Tremblement de repos.", "Syndrome parkinsonien.", "Bradykinésie.", "Distinguer.", "Parkinson.", "Essentiel.", "Repos + lenteur = parkinson."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 45 ans traitée par lithium pour un trouble bipolaire tremble des deux mains depuis 3 mois, surtout en tenant sa tasse.", prompt="Quelle démarche est prioritaire ?",
 items=["*Doser la lithémie et la TSH || Le lithium donne un tremblement et une hypothyroïdie.", "Débuter le propranolol sans bilan || La cause médicamenteuse doit se vérifier.", "Demander un DaTSCAN || Rien n'évoque un parkinsonisme.", "Arrêter brutalement le lithium || Il expose à la rechute.", "Conclure à un tremblement essentiel || L'histoire est récente et médicamenteuse."],
 notions="N09 N11", angle="piège", diff=2, ladder=L("Tremblement récent.", "Cause médicamenteuse.", "Lithium.", "Vérification.", "Lithémie, TSH.", "Essentiel.", "Médicament d'abord."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Vous hésitez chez un homme de 66 ans entre tremblement essentiel et début de maladie de Parkinson, car son tremblement prédomine à droite.", prompt="Quel examen aide le mieux ?",
 items=["*Un DaTSCAN || Il est normal dans le tremblement essentiel et anormal dans le parkinson.", "Une IRM cérébrale standard || Elle est normale dans les deux.", "Un EEG || Il n'aide pas.", "Un dosage de la céruloplasmine || Il cherche une maladie de Wilson chez le jeune.", "Un EMG des quatre membres || Il n'est pas discriminant ici."],
 notions="N12 N08", angle="direct", diff=2, ladder=L("Doute.", "Imagerie fonctionnelle.", "Voie dopaminergique.", "Discriminant.", "DaTSCAN.", "IRM.", "DaTSCAN normal = essentiel."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 68 ans souffre d'un tremblement essentiel qui l'empêche de boire et de s'habiller malgré le propranolol puis la primidone à doses efficaces.", prompt="Quelle option proposez-vous ?",
 items=["*Une stimulation cérébrale profonde du VIM ou une thalamotomie par ultrasons focalisés || Elles traitent le tremblement réfractaire.", "La lévodopa || Elle traite le parkinson.", "Une benzodiazépine à forte dose || Elle endort sans bénéfice durable.", "Un traitement par alcool encadré || Il expose à la dépendance.", "Aucune option n'existe || La chirurgie fonctionnelle existe."],
 notions="N17 N04", angle="application", diff=2, ladder=L("Échec médical.", "Neurochirurgie fonctionnelle.", "Invalidant.", "Cible.", "VIM.", "Lévodopa.", "Réfractaire = VIM."), sources="[Zesiewicz, AAN, 2011 ; Elias, NEJM, 2016]"),
dict(masque=False, sit="monographique", format="A", stem="Vous enseignez la classification des tremblements de la Movement Disorder Society (2018).", prompt="Quelle durée minimale exige le diagnostic de tremblement essentiel ?",
 items=["*3 ans || La durée évite de classer un tremblement débutant d'une autre cause.", "3 mois || Elle est trop courte.", "6 mois || Elle est trop courte.", "1 an || Elle est trop courte.", "10 ans || Elle est trop longue."],
 notions="N01 N02", angle="direct", diff=2, ladder=L("Classification.", "Critères MDS.", "Durée.", "Seuil.", "3 ans.", "1 an.", "Au moins 3 ans."), sources="[Bhatia, MDS, 2018]"),
dict(format="A", stem="Un étudiant de 24 ans tremble des deux mains depuis un an. Il a des transaminases élevées et son humeur a changé. L'examen trouve une dysarthrie.", prompt="Quel examen demandez-vous en priorité ?",
 items=["*Une céruloplasmine et une cuprurie de 24 heures || Une maladie de Wilson se cherche avant 40 ans.", "Aucun, c'est un tremblement essentiel du jeune || Les signes associés l'excluent.", "Un DaTSCAN || Il cherche un parkinsonisme dégénératif.", "Un EEG || Il n'aide pas.", "Une lithémie || Il ne prend pas de lithium."],
 notions="N10 N09", angle="piège", diff=3, ladder=L("Tremblement du jeune.", "Cause secondaire.", "Foie, humeur.", "Maladie métabolique.", "Wilson.", "Essentiel.", "Jeune + foie = cuivre."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 76 ans prend sa première dose de primidone, à dose pleine. Elle est prise de nausées, de vertiges et tombe dans la nuit.", prompt="Quelle erreur a été commise ?",
 items=["*La primidone aurait dû commencer à très faible dose le soir || La sensibilité initiale est fréquente.", "La primidone se donne le matin à jeun || La prise du soir est préférable.", "Elle aurait dû recevoir du propranolol à forte dose d'emblée || Il s'augmente aussi progressivement.", "Ces effets prouvent une allergie || Ce sont des effets dose-dépendants.", "La chute est sans lien || Elle est typique."],
 notions="N15 N19", angle="application", diff=2, ladder=L("Chute nocturne.", "Effet indésirable.", "Primidone.", "Titration.", "Très faible dose le soir.", "Allergie.", "Commencer bas."), sources="[AIPS Swissmedic]"),
dict(format="A", stem="Un homme de 64 ans tremble des deux mains depuis 10 ans. L'examen trouve aussi une marche en tandem imparfaite, sans ataxie franche ni autre signe.", prompt="Comment classez-vous ce tableau selon la MDS ?",
 items=["*Un « tremblement essentiel plus » || Des signes discrets s'ajoutent au tremblement.", "Un tremblement cérébelleux || L'ataxie franche manque.", "Une maladie de Parkinson || Ni repos, ni bradykinésie.", "Un tremblement psychogène || Il est ancien et stable.", "Un tremblement essentiel pur || La marche en tandem est perturbée."],
 notions="N02 N07", angle="direct", diff=3, ladder=L("Signe discret.", "Classification MDS.", "Tandem.", "Catégorie.", "Essentiel plus.", "Cérébelleux.", "Signe discret = plus."), sources="[Bhatia, MDS, 2018]"),
dict(format="A", stem="Un homme de 55 ans, tremblant des mains depuis des années, boit chaque soir 4 verres de vin parce que cela calme ses mains.", prompt="Quel conseil lui donnez-vous ?",
 items=["*Réduire l'alcool, qui expose à la dépendance, et discuter un traitement efficace || L'alcool n'est jamais un traitement.", "Poursuivre, car l'alcool est le meilleur traitement || Il expose à la dépendance.", "Augmenter la dose le matin || Elle aggrave le risque.", "Remplacer le vin par du café || La caféine aggrave le tremblement.", "Arrêter brutalement sans suivi || Le sevrage aggrave le tremblement."],
 notions="N24 N05 N23", angle="piège", diff=2, ladder=L("Alcool.", "Automédication.", "4 verres.", "Risque.", "Dépendance.", "Café.", "Alcool ≠ traitement."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous comparez le tremblement essentiel et la maladie de Parkinson.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le tremblement essentiel prédomine à l'action. || Il est postural et cinétique.", "V: Le parkinson s'accompagne de bradykinésie. || Elle définit le syndrome parkinsonien.", "F: L'écriture est micrographique dans le tremblement essentiel. || Elle est tremblée et ample.", "F: L'alcool aggrave typiquement le tremblement essentiel. || Il l'améliore souvent."],
 notions="N08 N06 N07 N05", angle="direct", diff=1, ladder=L("Comparaison.", "Deux tremblements.", "Action ou repos.", "Pièges.", "Action vs repos.", "Micrographie.", "Action ≠ repos."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Une femme de 67 ans, à Sion, tremble des deux mains depuis 15 ans. Elle n'arrive plus à manger proprement et sort moins. Elle prend déjà le propranolol.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'ergothérapie prescrite par le médecin est remboursée par l'assurance obligatoire. || Elle adapte couverts et gestes.", "V: Le topiramate est une option de second choix. || Il est probablement efficace.", "F: Un traitement est inutile tant qu'elle n'a pas de handicap social. || Le handicap social justifie le traitement.", "F: Cette maladie réduit nettement l'espérance de vie. || Elle ne la réduit pas."],
 notions="N22 N16 N13 N20", angle="application", diff=2, ladder=L("Gêne quotidienne.", "Mesures associées.", "Suisse.", "Remboursement.", "Ergothérapie, topiramate.", "Espérance de vie.", "Ergothérapie remboursée."), sources="[OPAS ; Zesiewicz, AAN, 2011]"),
dict(format="Kprim", stem="Vous suivez un homme de 72 ans tremblant depuis 12 ans, sous propranolol, qui a reçu une stimulation cérébrale profonde il y a un an.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le dessin de spirale objective l'évolution. || Il mesure le tremblement.", "V: La fréquence cardiaque se contrôle sous propranolol. || Il ralentit le cœur.", "F: Le tremblement disparaît en général spontanément avec l'âge. || Il progresse lentement.", "F: La stimulation cible le noyau sous-thalamique dans cette indication. || Elle cible le VIM du thalamus."],
 notions="N21 N20 N17 N18", angle="application", diff=2, ladder=L("Suivi.", "Évaluation.", "Spirale, pouls.", "Évolution.", "Lente progression.", "Disparition.", "VIM, spirale, pouls."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un patient consulte parce que ses mains tremblent.", prompt="Quels éléments orientent vers un tremblement essentiel ? (3 réponses)",
 items=["*Tremblement d'action bilatéral || Il est typique.", "*Amélioration après un peu d'alcool || Elle est fréquente.", "*Évolution depuis plusieurs années avec histoire familiale || Elle est typique.", "Tremblement de repos unilatéral || Il oriente vers un parkinson.", "Bradykinésie || Elle oriente vers un parkinson.", "Rigidité en roue dentée || Elle oriente vers un parkinson.", "Micrographie || Elle oriente vers un parkinson.", "Ataxie franche || Elle oriente vers un tremblement cérébelleux.", "Postures dystoniques || Elles orientent vers un tremblement dystonique.", "Début brutal || Il oriente vers une cause secondaire.", "Perte de poids et palpitations || Elles orientent vers une hyperthyroïdie.", "Début sous lithium || Il oriente vers une cause médicamenteuse."],
 notions="N06 N05 N01 N25", angle="direct", diff=1, ladder=L("Tremblement.", "Type.", "Action, alcool.", "Lesquels.", "Bilatéral, alcool, ancien.", "Repos.", "Action + alcool."), sources="[Bhatia, MDS, 2018]"),
dict(format="MenuLong", stem="Un homme de 60 ans tremble des mains en tenant un objet depuis 2 mois.", prompt="Quels médicaments peuvent l'expliquer ? (3 réponses)",
 items=["*Lithium || Il donne un tremblement d'action.", "*Valproate || Il donne un tremblement d'action.", "*Salbutamol || Les bêta-2-mimétiques donnent un tremblement.", "Propranolol || Il réduit le tremblement.", "Primidone || Elle réduit le tremblement.", "Paracétamol || Il ne fait pas trembler.", "Oméprazole || Il ne fait pas trembler.", "Atorvastatine || Elle ne fait pas trembler.", "Amlodipine || Elle ne fait pas trembler.", "Metformine || Elle ne fait pas trembler.", "Ramipril || Il ne fait pas trembler.", "Topiramate || Il réduit le tremblement."],
 notions="N09 N11", angle="application", diff=2, ladder=L("Tremblement récent.", "Cause médicamenteuse.", "Revue des traitements.", "Lesquels.", "Lithium, valproate, salbutamol.", "Propranolol.", "Revoir les médicaments."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Vous expliquez à un patient atteint de tremblement essentiel pourquoi la stimulation cérébrale profonde peut l'aider.", prompt="Quelle structure cible-t-elle ?",
 items=["*Le noyau ventral intermédiaire (VIM) du thalamus || Il relaie le circuit cérébello-thalamo-cortical.", "Le noyau sous-thalamique || Il est la cible du parkinson.", "Le globus pallidus interne || Il est la cible de la dystonie.", "L'hippocampe || Il n'intervient pas.", "Le noyau caudé || Il n'est pas la cible."],
 notions="N04 N17", angle="direct", diff=2, ladder=L("Neurostimulation.", "Circuit cérébelleux.", "Thalamus.", "Cible.", "VIM.", "Sous-thalamique.", "Tremblement = VIM."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Tremblement essentiel : le reconnaître sur un tremblement d'action bilatéral ancien, le distinguer du parkinson et des causes médicamenteuses, traiter par propranolol ou primidone selon le terrain et adresser les formes réfractaires à la stimulation du VIM",
 notions=[
  dict(titre="Reconnaître", rub=["def", "ana", "exa", "epi"], comment="Applique les critères MDS 2018.",
   tableau=(["Critère", "Contenu", "Pourquoi"], [
     ["Topographie", "Membres supérieurs, bilatéral", "Il peut gagner tête et voix"],
     ["Type", "Action (postural, cinétique)", _T("Pas de repos", "Le repos oriente vers le parkinson.")],
     ["Durée", "≥ 3 ans", "Elle écarte les tremblements récents secondaires"],
     ["Signes associés", "Aucun (sinon « plus »)", "Dystonie, ataxie, parkinsonisme l'excluent"]]),
   points=["L'alcool l'améliore souvent."], sources=["[Bhatia, MDS, 2018]"]),
  dict(titre="Distinguer", rub=["pos", "red", "gold", "alt"], comment="Élimine parkinson, médicaments, thyroïde et Wilson.",
   tableau=(["Diagnostic", "Indice", "Examen"], [
     ["Parkinson", "Repos, bradykinésie, rigidité", _T("DaTSCAN si doute", "Il est anormal dans le parkinson.")],
     ["Physiologique exagéré", "Médicament, café, thyroïde", "TSH, revue des médicaments"],
     ["Wilson", "Avant 40 ans, foie, psychiatrie", "Céruloplasmine"]]),
   points=["Diagnostic clinique, TSH."], sources=["[avis d'expert]"]),
  dict(titre="Traiter", rub=["acu", "chr", "hos"], comment="Traite la gêne selon le terrain.",
   arbre=[("t1", None, "Tremblement gênant", "Seule la gêne justifie un traitement."),
          ("t2", "t1", "Sans asthme ni BAV", "Propranolol progressif.", "te"),
          ("t3", "t1", "Asthme ou BAV", "Primidone, faible dose le soir.", "te"),
          ("t4", "t2", "Échec", "Topiramate, gabapentine, toxine botulique.", "te"),
          ("t5", "t4", "Réfractaire invalidant", "Stimulation du VIM ou ultrasons focalisés.", "te")],
   points=["Jamais l'alcool comme traitement."], sources=["[Zesiewicz, AAN, 2011]"]),
  dict(titre="Suivre", rub=["pro", "sur", "fol"], comment="Suit la gêne et accompagne au quotidien.",
   tableau=(["Domaine", "Mesure", "Pourquoi"], [
     ["Fonction", "Écriture, spirale, repas", "Elle guide le traitement"],
     ["Propranolol", "Fréquence cardiaque", "Il ralentit le cœur"],
     ["Quotidien (Suisse)", _T("Ergothérapie sur prescription", "Elle est remboursée par l'AOS."), "Couverts lestés, adaptations"]]),
   points=["Évolution lente, espérance de vie normale."], sources=["[OPAS art. 6]"]),
 ],
 ssp=dict(code="S7.3", nom="Mouvements involontaires anormaux, tremblements, tics, troubles de la coordination", officiel=True, algorithme=[
  ("n1", None, "Tremblement", "Le type (repos ou action) oriente d'abord."),
  ("n2", "n1", "Repos, asymétrique, lenteur", "Syndrome parkinsonien (autre SSP).", None, "c2"),
  ("n3", "n1", "Action, récent", "Médicament, thyroïde, café : corriger la cause.", None, "c2"),
  ("n4", "n1", "Action, bilatéral, ≥ 3 ans", "Tremblement essentiel.", "te", "c1"),
  ("n5", "n4", "Gêne", "Propranolol ou primidone.", "te", "c3"),
  ("n6", "n5", "Réfractaire", "Stimulation du VIM.", "te", "c3"),
  ("n7", "n4", "Quotidien", "Ergothérapie, suivi fonctionnel.", "te", "c4")]),
 pec=[
  dict(cle="te", titre="Tremblement essentiel",
   but=["Réduire la gêne fonctionnelle et sociale.", "Éviter les effets indésirables et l'automédication par l'alcool."],
   moyens=dict(accueil=["Expliquer le caractère bénin pour la vie.", "Revoir les médicaments et la caféine.", "Évaluer la gêne au quotidien."],
    pharma=[("Propranolol (bêtabloquant)", "Augmentation progressive ; à vérifier dans l'AIPS.", "Il est un premier choix de niveau élevé.", "[Zesiewicz, AAN, 2011]"),
            ("Primidone (barbiturique)", "Très faible dose le soir, titrée ; à vérifier dans l'AIPS.", "Elle est l'autre premier choix, utile en cas d'asthme.", "[Zesiewicz, AAN, 2011]"),
            ("Topiramate (antiépileptique)", "Titration lente ; à vérifier dans l'AIPS.", "Il est un second choix.", "[Zesiewicz, AAN, 2011]")],
    nonpharma=[("rééducation", "Ergothérapie, couverts lestés.", "Elle compense le tremblement au quotidien."),
               ("geste ou chirurgie", "Stimulation du VIM ou thalamotomie.", "Elle traite le tremblement réfractaire."),
               ("hygiène de vie", "Moins de caféine, gestion du stress, alcool limité.", "Ils réduisent les aggravations.")],
    transversal=[("Pneumologie", "Elle signale l'asthme qui contre-indique le propranolol.")]),
   urgence=None,
   horsUrgence=(["Revue des médicaments.", "Traitement seulement si gêne."],
            [("d'abord", "médecin de famille", "Pose le diagnostic clinique et dose la TSH."),
             ("ensuite", "médecin de famille", "Débute propranolol ou primidone."),
             ("puis", "neurologue", "Confirme en cas de doute et gère l'échec."),
             ("puis", "ergothérapeute", "Adapte les gestes et le matériel.")]),
   pronostic="L'évolution est lente ; l'espérance de vie reste normale mais la gêne peut devenir invalidante.",
   suivi=[("Gêne fonctionnelle", "À chaque consultation", "Gestes possibles"), ("Fréquence cardiaque", "Sous propranolol", "Pas de bradycardie gênante"), ("Consommation d'alcool", "À chaque consultation", "Pas d'automédication")],
   sortie="Le suivi reste ambulatoire.",
   prevention=["Elle limite la caféine.", "Elle prévient l'automédication alcoolique.", "Elle revoit les médicaments trémorigènes."]),
 ])
AVERIFIER = ["Doses de propranolol, de primidone et de topiramate à vérifier dans l'AIPS ; disponibilité suisse de la primidone à vérifier dans l'AIPS."]
