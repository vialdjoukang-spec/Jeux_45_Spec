ID = "G47.5_trouble_du_comportem__G11-E08"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[ICSD-3, AASM 2014]|Le trouble du comportement en sommeil paradoxal associe des vocalisations et des comportements moteurs complexes pendant le sommeil paradoxal à une perte de l'atonie musculaire documentée par polysomnographie.",  # N01
"bas|mécanisme|2||[avis d'expert]|Des noyaux du tronc cérébral maintiennent normalement l'atonie du sommeil paradoxal ; leur atteinte, souvent par une synucléinopathie débutante, laisse le dormeur « vivre » ses rêves.",  # N02
"epi|terrain particulier|2||[Postuma, Brain 2019]|La forme isolée touche surtout l'homme après 50 ans : dans une cohorte de 1280 patients, 82,5 % étaient des hommes, d'âge moyen 66 ans.",  # N03
"pro|chiffre|3||[Postuma, Brain 2019]|La forme isolée évolue vers une maladie de Parkinson, une démence à corps de Lewy ou une atrophie multisystématisée à un rythme de 6,3 % par an, et 73,5 % des patients ont converti après 12 ans.",  # N04
"gold|examen|3||[ICSD-3, AASM 2014]|La vidéo-polysomnographie confirme le diagnostic en montrant un sommeil paradoxal sans atonie et écarte les imitateurs.",  # N05
"ana|symptôme|2||[avis d'expert]|Le patient rêve qu'on l'attaque et se défend, plutôt dans la seconde moitié de la nuit ; réveillé, il s'oriente vite et raconte un rêve cohérent.",  # N06
"pos|diagnostic différentiel|2||[avis d'expert]|Le somnambulisme et les terreurs nocturnes surviennent dans le premier tiers de la nuit, en sommeil lent profond, chez le sujet jeune, avec confusion et amnésie.",  # N07
"pos|diagnostic différentiel|2||[avis d'expert]|Un syndrome d'apnées obstructives sévère peut imiter le trouble par des mouvements à la fin des apnées ; la polysomnographie les distingue.",  # N08
"red|piège|2||[Howell, J Clin Sleep Med 2023]|Les antidépresseurs sérotoninergiques peuvent induire ou démasquer le trouble ; leur arrêt se discute lorsque c'est possible.",  # N09
"acu|décision|2||[Howell, J Clin Sleep Med 2023]|La sécurité de la chambre prime : retirer les armes et objets dangereux, capitonner les meubles, poser un tapis et, en cas de forme sévère, dormir séparément.",  # N10
"chr|molécule|2||[Howell, J Clin Sleep Med 2023]|La mélatonine à libération immédiate et le clonazépam font l'objet d'une recommandation conditionnelle dans la forme isolée (posologies à vérifier dans l'AIPS).",  # N11
"hos|complication|1||[avis d'expert]|Chez le sujet âgé, le clonazépam expose aux chutes, à la sédation, aux troubles cognitifs et à l'aggravation des apnées.",  # N12
"chr|molécule|1||[Howell, J Clin Sleep Med 2023]|La rivastigmine transdermique se suggère en cas de trouble cognitif léger, et le pramipexole reste une option conditionnelle.",  # N13
"pro|critère|1||[Postuma, Brain 2019]|Des anomalies motrices quantitatives (HR 3,16), une hyposmie (HR 2,62), un trouble cognitif léger, une dysfonction érectile, un DAT-scan anormal et une constipation prédisent la conversion.",  # N14
"sur|décision|2||[Postuma, Brain 2019 ; avis d'expert]|Le neurologue revoit le patient régulièrement pour dépister parkinsonisme, déclin cognitif et dysautonomie.",  # N15
"fol|décision|1||[avis d'expert]|L'annonce du risque neurodégénératif se fait avec tact, en respectant le souhait du patient de savoir ou non, et peut ouvrir l'accès à la recherche.",  # N16
"pos|diagnostic différentiel|1||[avis d'expert]|Une épilepsie hypermotrice liée au sommeil donne des épisodes brefs, stéréotypés et répétés, surtout en sommeil lent léger.",  # N17
"epi|terrain particulier|1||[avis d'expert]|Chez le sujet jeune, le trouble accompagne souvent une narcolepsie de type 1.",  # N18
"def|critère|1||[Howell, J Clin Sleep Med 2023]|On distingue une forme isolée, une forme secondaire à une maladie (Parkinson, narcolepsie) et une forme médicamenteuse.",  # N19
"exa|signe|1||[Postuma, Brain 2019]|L'examen cherche des signes prodromiques discrets : hyposmie, constipation, hypotension orthostatique, signes moteurs fins.",  # N20
"alt|examen|1||[Postuma, Brain 2019]|Le test olfactif et le DAT-scan stratifient le risque de conversion sans poser le diagnostic du trouble.",  # N21
"fol|contexte suisse|1|S|[avis d'expert]|En Suisse, la polysomnographie se réalise dans un centre du sommeil reconnu par la Société suisse de recherche sur le sommeil, de médecine du sommeil et de chronobiologie.",  # N22
"hos|complication|1||[avis d'expert]|Les épisodes blessent le patient et son conjoint : contusions, fractures, rarement hématome sous-dural.",  # N23
"pro|pronostic|1||[avis d'expert]|Le trouble peut précéder de plus de 10 ans les signes moteurs ou cognitifs d'une synucléinopathie.",  # N24
"epi|chiffre|1||[avis d'expert]|Sa prévalence avoisine 1 % après 60 ans, mais beaucoup de patients ne consultent pas.",  # N25
"chr|décision|1||[avis d'expert]|Le traitement d'un syndrome d'apnées associé améliore le sommeil et lève parfois un faux diagnostic.",  # N26
]
ANGLES = [
"Rêves violents agis en fin de nuit, récit cohérent.",
"Vidéo-polysomnographie : sommeil paradoxal sans atonie.",
"Conversion 6,3 %/an, 73,5 % à 12 ans.",
"Chambre sécurisée, mélatonine ou clonazépam.",
"Antidépresseurs sérotoninergiques.",
"Imitateurs : parasomnies NREM, apnées, épilepsie.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un homme de 67 ans consulte à Sion avec son épouse. Depuis 2 ans, il crie et donne des coups de poing en fin de nuit ; il rêve qu'on l'attaque. Réveillé, il raconte aussitôt un rêve cohérent. Elle a reçu un coup au visage.", prompt="Quel diagnostic évoquez-vous ?",
 items=["*Un trouble du comportement en sommeil paradoxal || Rêves violents agis en fin de nuit chez un homme âgé.", "Un somnambulisme || Il survient en début de nuit avec amnésie.", "Des terreurs nocturnes || Elles touchent l'enfant en début de nuit.", "Un syndrome des jambes sans repos || Il donne un besoin de bouger à l'éveil.", "Un trouble psychotique || Le récit est onirique et nocturne."],
 notions="N06 N01 N03", angle="direct", diff=1, ladder=L("Comportements nocturnes.", "Perte de l'atonie.", "Fin de nuit, récit cohérent.", "Homme âgé.", "TCSP.", "Somnambulisme.", "Rêve agi en fin de nuit = sommeil paradoxal."), sources="[ICSD-3, AASM 2014]"),
dict(format="A", serie=("S1", 2, 4), stem="Vous voulez confirmer votre hypothèse.", prompt="Quel examen demandez-vous ?",
 items=["*Une vidéo-polysomnographie || Elle montre le sommeil paradoxal sans atonie.", "Un EEG de routine à l'éveil || Il ne montre pas le sommeil paradoxal.", "Une IRM cérébrale seule || Elle ne confirme pas le trouble.", "Une actimétrie seule || Elle ne voit pas l'atonie.", "Un DAT-scan || Il stratifie le risque sans poser le diagnostic."],
 notions="N05 N01 N08 N22", angle="application", diff=1, ladder=L("Confirmation.", "Atonie.", "Sommeil paradoxal.", "Enregistrement.", "Vidéo-polysomnographie.", "EEG d'éveil.", "Prouver l'absence d'atonie."), sources="[ICSD-3, AASM 2014]"),
dict(format="A", serie=("S1", 3, 4), stem="L'examen confirme un sommeil paradoxal sans atonie, sans apnées significatives.", prompt="Quelle prise en charge initiale proposez-vous ?",
 items=["*Sécuriser la chambre et proposer de la mélatonine à libération immédiate || La sécurité prime et la mélatonine est bien tolérée.", "Une stimulation cérébrale profonde || Elle n'est pas recommandée.", "Un antidépresseur sérotoninergique || Il peut aggraver le trouble.", "Aucune mesure, car le trouble est bénin || Il blesse.", "Une contention au lit || Elle est dangereuse."],
 notions="N10 N11 N12", angle="application", diff=1, ladder=L("Diagnostic posé.", "Prévenir les blessures.", "Pas d'apnées.", "Sécurité puis molécule.", "Chambre sûre et mélatonine.", "Stimulation profonde.", "Protéger d'abord."), sources="[Howell, J Clin Sleep Med 2023]"),
dict(format="A", serie=("S1", 4, 4), stem="L'épouse demande si ce trouble annonce une autre maladie.", prompt="Quelle information donnez-vous ?",
 items=["*Il évolue souvent vers une maladie à corps de Lewy (Parkinson, démence, atrophie multisystématisée), environ 6 % par an, d'où un suivi neurologique régulier || 73,5 % ont converti après 12 ans.", "Il ne s'associe à aucune maladie || Il annonce souvent une synucléinopathie.", "Il annonce surtout une maladie d'Alzheimer || Il annonce surtout une synucléinopathie.", "La conversion est certaine dans l'année || Elle prend souvent des années.", "Il annonce une SLA || Ce n'est pas le lien attendu."],
 notions="N04 N15 N24", angle="application", diff=2, ladder=L("Avenir.", "Synucléine.", "Forme isolée.", "Taux de conversion.", "Suivi neurologique.", "Aucun lien.", "Rêves agis = Lewy à surveiller."), sources="[Postuma, Brain 2019]"),
dict(format="A", stem="Une femme de 24 ans se lève dans l'heure qui suit son endormissement, déambule l'air confus et ne se souvient de rien le matin.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Une parasomnie du sommeil lent profond (somnambulisme) || Début de nuit, confusion et amnésie l'orientent.", "Un trouble du comportement en sommeil paradoxal || Il survient en fin de nuit avec récit du rêve.", "Une narcolepsie || Elle donne une somnolence diurne.", "Une épilepsie absence || Elle survient à l'éveil.", "Un syndrome des jambes sans repos || Il ne fait pas déambuler endormi."],
 notions="N07 N06", angle="piège", diff=2, ladder=L("Déambulation nocturne.", "Éveil dissocié.", "Début de nuit, amnésie.", "Stade de sommeil.", "Parasomnie NREM.", "Sommeil paradoxal.", "Début de nuit + amnésie = sommeil lent."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme obèse de 62 ans ronfle fort ; sa femme le voit s'agiter et parler la nuit. La polysomnographie montre 45 apnées par heure, les mouvements survenant à la fin des apnées, avec une atonie conservée en sommeil paradoxal.", prompt="Quelle conclusion retenez-vous ?",
 items=["*Un syndrome d'apnées obstructives qui imite le trouble, à traiter par pression positive continue || L'atonie est conservée.", "Un trouble du comportement en sommeil paradoxal confirmé || L'atonie conservée l'exclut.", "Un somnambulisme || Le lien avec les apnées l'explique.", "Une épilepsie nocturne || Les mouvements suivent les apnées.", "Un trouble psychiatrique || La cause est respiratoire."],
 notions="N08 N05 N26", angle="piège", diff=2, ladder=L("Agitation nocturne.", "Éveils respiratoires.", "Apnées, atonie conservée.", "Imitateur.", "PPC.", "TCSP.", "Atonie conservée = pas de TCSP."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 55 ans agit ses rêves depuis 2 mois ; elle a débuté de la venlafaxine il y a 3 mois pour une dépression.", prompt="Quelle démarche retenez-vous ?",
 items=["*Évoquer une forme médicamenteuse et discuter avec le psychiatre l'arrêt ou le changement d'antidépresseur || Les sérotoninergiques suppriment l'atonie.", "Ajouter un deuxième antidépresseur sérotoninergique || Il aggraverait.", "Conclure à une synucléinopathie certaine || Le médicament peut l'expliquer.", "Arrêter brutalement l'antidépresseur sans avis || Le sevrage brutal est risqué.", "Ignorer le symptôme || Il expose aux blessures."],
 notions="N09 N19 N02", angle="application", diff=2, ladder=L("Rêves agis récents.", "Atonie supprimée.", "Venlafaxine.", "Forme médicamenteuse.", "Discuter l'arrêt.", "Ajouter un ISRS.", "Antidépresseur récent = suspect."), sources="[Howell, J Clin Sleep Med 2023]"),
dict(masque=False, sit="monographique", format="A", stem="Vous expliquez pourquoi le patient atteint d'un trouble du comportement en sommeil paradoxal agit ses rêves.", prompt="Quel mécanisme est juste ?",
 items=["*L'atteinte des noyaux du tronc cérébral qui maintiennent l'atonie, souvent par une synucléinopathie débutante || Le dormeur bouge pendant ses rêves.", "Une hyperactivité du cortex frontal en sommeil lent || C'est le mécanisme des parasomnies NREM.", "Une carence en fer || Elle concerne les jambes sans repos.", "Un trouble psychiatrique dissociatif || Le mécanisme est organique.", "Une lésion de la moelle || L'atonie dépend du tronc cérébral."],
 notions="N02 N24", angle="direct", diff=2, ladder=L("Mécanisme.", "Tronc cérébral.", "Atonie perdue.", "Synucléine.", "Noyaux pontiques.", "Cortex frontal.", "Plus de frein moteur en sommeil paradoxal."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 79 ans, traité par clonazépam pour des rêves agis, chute deux fois la nuit en se levant. Il ronfle et fait des pauses respiratoires.", prompt="Quelle adaptation proposez-vous ?",
 items=["*Remplacer le clonazépam par de la mélatonine et rechercher des apnées || Le clonazépam expose aux chutes et aggrave les apnées.", "Augmenter le clonazépam || Il aggraverait chutes et apnées.", "Ajouter un hypnotique Z || Il aggraverait.", "Arrêter tout traitement et toute surveillance || La sécurité reste nécessaire.", "Ajouter un antidépresseur || Il peut aggraver le trouble."],
 notions="N12 N11 N08", angle="piège", diff=2, ladder=L("Chutes sous benzodiazépine.", "Sédation, apnées.", "79 ans.", "Rapport bénéfice-risque.", "Mélatonine.", "Augmenter.", "Âgé + clonazépam = chute."), sources="[Howell, J Clin Sleep Med 2023]"),
dict(format="A", stem="Un homme de 35 ans présente plusieurs fois par nuit des épisodes de 30 secondes, toujours identiques, avec mouvements de pédalage et cris, peu après l'endormissement.", prompt="Quel diagnostic devez-vous évoquer ?",
 items=["*Une épilepsie hypermotrice liée au sommeil || Les épisodes brefs, stéréotypés et répétés l'orientent.", "Un trouble du comportement en sommeil paradoxal || Il n'est pas stéréotypé.", "Un somnambulisme || Il ne se répète pas à l'identique.", "Un cauchemar || Il ne donne pas de pédalage stéréotypé.", "Un trouble panique nocturne || Il ne donne pas ces mouvements."],
 notions="N17 N07", angle="application", diff=3, ladder=L("Épisodes nocturnes.", "Décharge frontale.", "Brefs, identiques.", "Stéréotypie.", "Épilepsie hypermotrice.", "TCSP.", "Stéréotypé = épilepsie."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 25 ans s'endort au volant et ses genoux lâchent quand il rit ; sa compagne le voit aussi agir ses rêves.", prompt="Quelle cause sous-jacente évoquez-vous ?",
 items=["*Une narcolepsie de type 1 || Somnolence, cataplexie et rêves agis l'orientent.", "Une maladie de Parkinson débutante || L'âge et la cataplexie orientent ailleurs.", "Une épilepsie absence || Elle ne donne pas de cataplexie.", "Un syndrome des jambes sans repos || Il ne donne pas de cataplexie.", "Une hypoglycémie || Elle ne donne pas de cataplexie."],
 notions="N18 N19", angle="application", diff=2, ladder=L("Jeune avec rêves agis.", "Orexine.", "Cataplexie.", "Forme secondaire.", "Narcolepsie.", "Parkinson.", "Jeune + cataplexie = narcolepsie."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 70 ans a une forme isolée confirmée. Vous voulez estimer son risque de conversion à court terme.", prompt="Quel ensemble d'éléments prédit le mieux une conversion ?",
 items=["*Des anomalies motrices fines, une hyposmie et un DAT-scan anormal || Ils augmentent fortement le risque.", "Le sexe masculin seul || Il ne prédit pas la conversion.", "Une insomnie || Elle ne la prédit pas.", "Un syndrome des jambes sans repos || Il ne la prédit pas.", "Une dépression || Elle ne la prédit pas dans cette cohorte."],
 notions="N14 N21 N20", angle="application", diff=3, ladder=L("Risque individuel.", "Marqueurs prodromiques.", "Moteur, odorat, DAT.", "Prédicteurs.", "Motricité, odorat, DAT-scan.", "Sexe.", "Moteur et odorat prédisent."), sources="[Postuma, Brain 2019]"),
dict(masque=False, sit="monographique", format="A", stem="Un patient avec un trouble du comportement en sommeil paradoxal isolé demande ce que signifie son diagnostic pour l'avenir.", prompt="Quelle attitude est la plus juste ?",
 items=["*Informer avec tact du risque de maladie neurodégénérative selon son souhait de savoir, et organiser un suivi régulier || L'annonce respecte son autonomie.", "Lui cacher toute information || Il a droit à l'information.", "Lui annoncer une maladie de Parkinson certaine dans l'année || Ce n'est pas exact.", "Lui dire qu'il n'y a aucun risque || Le risque est élevé.", "Arrêter tout suivi || Le suivi dépiste tôt."],
 notions="N16 N15 N04", angle="direct", diff=1, ladder=L("Annonce.", "Autonomie.", "Forme isolée.", "Information juste.", "Tact et suivi.", "Cacher.", "Informer et suivre."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 72 ans avec un trouble du comportement en sommeil paradoxal présente un trouble cognitif léger.", prompt="Quelle option thérapeutique se suggère particulièrement ?",
 items=["*La rivastigmine transdermique || Elle se suggère en cas de trouble cognitif léger.", "Le clonazépam à forte dose || Il aggrave les troubles cognitifs.", "Un antidépresseur tricyclique || Il peut aggraver le trouble.", "Une stimulation cérébrale profonde || Elle n'est pas recommandée.", "L'halopéridol || Il est dangereux dans les maladies à corps de Lewy."],
 notions="N13 N11", angle="direct", diff=2, ladder=L("Trouble cognitif.", "Cholinergique.", "TCSP.", "Choix ciblé.", "Rivastigmine.", "Clonazépam.", "Cognition fragile = rivastigmine."), sources="[Howell, J Clin Sleep Med 2023]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez le diagnostic du trouble du comportement en sommeil paradoxal.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La polysomnographie montre une perte de l'atonie en sommeil paradoxal. || C'est le critère objectif.", "V: Les épisodes surviennent plutôt dans la seconde moitié de la nuit. || Le sommeil paradoxal y domine.", "F: Les épisodes surviennent en sommeil lent profond. || Ils surviennent en sommeil paradoxal.", "F: La polysomnographie n'est jamais nécessaire. || Elle confirme et écarte les imitateurs."],
 notions="N01 N05 N06", angle="direct", diff=1, ladder=L("Diagnostic.", "Atonie.", "Fin de nuit.", "Pièges.", "Polysomnographie.", "Sommeil lent.", "Sommeil paradoxal sans atonie."), sources="[ICSD-3, AASM 2014]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez le pronostic du trouble du comportement en sommeil paradoxal isolé.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La conversion atteint environ 6,3 % par an. || Cohorte de 1280 patients.", "V: Environ 73,5 % des patients ont converti après 12 ans. || Postuma 2019.", "F: Il évolue surtout vers une maladie d'Alzheimer. || Il évolue vers une synucléinopathie.", "F: Il touche surtout la femme jeune. || Il touche surtout l'homme après 50 ans."],
 notions="N04 N24 N03", angle="direct", diff=2, ladder=L("Pronostic.", "Synucléine.", "6,3 % par an.", "Pièges.", "Suivre.", "Alzheimer.", "Lewy, pas Alzheimer."), sources="[Postuma, Brain 2019]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez la prise en charge du trouble du comportement en sommeil paradoxal.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La sécurisation de la chambre est prioritaire. || Bonne pratique de l'AASM.", "V: La mélatonine à libération immédiate est une option recommandée de façon conditionnelle. || AASM 2023.", "F: La stimulation cérébrale profonde est recommandée dans les formes secondaires. || L'AASM suggère de ne pas l'utiliser.", "F: Il faut augmenter un antidépresseur sérotoninergique en cours. || Il peut induire le trouble."],
 notions="N10 N11 N09", angle="direct", diff=2, ladder=L("Prise en charge.", "Sécurité.", "Mélatonine.", "Pièges.", "Protéger, traiter.", "Stimulation profonde.", "Chambre sûre d'abord."), sources="[Howell, J Clin Sleep Med 2023]"),
dict(format="Kprim", stem="Un patient de 65 ans présente des comportements nocturnes agités.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une parasomnie du sommeil lent survient plutôt dans le premier tiers de la nuit. || En sommeil lent profond.", "V: Un syndrome d'apnées sévère peut imiter des rêves agis. || La polysomnographie tranche.", "F: Une épilepsie nocturne ne peut jamais imiter une parasomnie. || Elle peut l'imiter.", "F: Les rêves agis touchent surtout l'enfant. || Ils touchent surtout l'adulte âgé."],
 notions="N07 N08 N17", angle="direct", diff=2, ladder=L("Diagnostic différentiel.", "Stades du sommeil.", "Horaire, apnées.", "Pièges.", "Polysomnographie.", "Épilepsie impossible.", "Horaire, apnées, stéréotypie."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un patient présente des comportements violents pendant son sommeil.", prompt="Choisissez les TROIS éléments qui orientent vers des rêves agis en sommeil paradoxal plutôt que vers un somnambulisme.",
 items=["*Épisodes dans la seconde moitié de la nuit || Le sommeil paradoxal y domine.", "*Récit d'un rêve cohérent au réveil || L'éveil est rapide et orienté.", "*Homme de plus de 50 ans || Terrain typique.", "Épisodes dans la première heure de sommeil || Sommeil lent profond.", "Amnésie complète le matin || Parasomnie NREM.", "Déambulation hors de la chambre || Somnambulisme.", "Confusion prolongée au réveil || Parasomnie NREM.", "Début dans l'enfance || Parasomnie NREM.", "Antécédents familiaux de somnambulisme || Parasomnie NREM.", "Yeux ouverts, regard vide || Somnambulisme.", "Déclenchement par la privation de sommeil || Parasomnie NREM.", "Épisodes stéréotypés de 30 secondes || Épilepsie."],
 notions="N06 N07 N03", angle="application", diff=2, ladder=L("Comportements nocturnes.", "Stade de sommeil.", "Horaire, récit, terrain.", "Discriminants.", "Sommeil paradoxal.", "Début de nuit.", "Fin de nuit, récit, homme âgé."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un homme de 68 ans sous sertraline agit des rêves violents ; une polysomnographie confirme un sommeil paradoxal sans atonie.", prompt="Choisissez les TROIS mesures initiales.",
 items=["*Sécuriser la chambre (objets dangereux retirés, meubles capitonnés) || Prévenir les blessures.", "*Proposer de la mélatonine à libération immédiate || Option bien tolérée.", "*Réévaluer la sertraline avec le prescripteur || Elle peut induire le trouble.", "Stimulation cérébrale profonde || Non recommandée.", "Contention au lit || Dangereuse.", "Ajouter un deuxième ISRS || Aggraverait.", "Halopéridol || Dangereux dans les maladies à corps de Lewy.", "Lévodopa d'emblée || Non indiquée sans parkinsonisme.", "Somnifère Z à forte dose || Risque de chute.", "Aucune mesure || Le trouble blesse.", "Interdire tout sommeil nocturne || Absurde.", "Alcool le soir || Il fragmente le sommeil."],
 notions="N10 N11 N09", angle="application", diff=2, ladder=L("Diagnostic posé.", "Sécurité et cause.", "Sertraline.", "Mesures initiales.", "Chambre, mélatonine, sertraline.", "Stimulation profonde.", "Protéger, traiter, revoir l'ISRS."), sources="[Howell, J Clin Sleep Med 2023]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Trouble du comportement en sommeil paradoxal : reconnaître les rêves agis de fin de nuit, confirmer par vidéo-polysomnographie, écarter les imitateurs et les causes médicamenteuses, sécuriser et traiter, puis suivre le risque élevé de synucléinopathie",
 notions=[
  dict(titre="Reconnaître le trouble", rub=["def", "ana", "epi", "bas"], comment="Pense au sommeil paradoxal devant des rêves violents agis en fin de nuit chez un homme âgé.",
   tableau=(["Élément", "Contenu", "Pourquoi"], [
     ["Horaire", "Seconde moitié de la nuit", "Le sommeil paradoxal y domine"],
     ["Récit", "Rêve cohérent, réveil orienté", _T("Éveil rapide", "Contraire du somnambulisme.")],
     ["Terrain", "Homme après 50 ans", "82,5 % d'hommes dans la grande cohorte"],
     ["Mécanisme", "Atonie perdue par atteinte du tronc cérébral", "Souvent synucléinopathie débutante"]]),
   points=["La prévalence avoisine 1 % après 60 ans."], sources=["[Postuma, Brain 2019]", "[ICSD-3, AASM 2014]"]),
  dict(titre="Confirmer et écarter les imitateurs", rub=["gold", "pos", "red", "alt"], comment="Demande une vidéo-polysomnographie : elle prouve l'absence d'atonie et démasque les imitateurs.",
   tableau=(["Imitateur", "Indice", "Conduite"], [
     ["Parasomnie du sommeil lent", "Début de nuit, confusion, amnésie", "Rassurer, hygiène du sommeil"],
     ["Apnées obstructives sévères", _T("Mouvements en fin d'apnée", "Atonie conservée.")],
     ["Épilepsie hypermotrice", "Épisodes brefs, stéréotypés, répétés", "EEG-vidéo"],
     ["Antidépresseur sérotoninergique", "Début après l'introduction", "Discuter l'arrêt"]]),
   points=["Le test olfactif et le DAT-scan stratifient le risque sans poser le diagnostic."], sources=["[Howell, J Clin Sleep Med 2023]"]),
  dict(titre="Protéger et traiter", rub=["acu", "chr", "hos"], comment="Sécurise d'abord la chambre, puis choisis la molécule selon l'âge, la cognition et les apnées.",
   arbre=[("t1", None, "Diagnostic confirmé", "Chambre sécurisée ; dormir séparément si forme sévère.", "tcsp"),
          ("t2", "t1", "Patient âgé ou apnées", "Mélatonine à libération immédiate plutôt que clonazépam.", "tcsp"),
          ("t3", "t1", "Patient jeune sans apnées", "Clonazépam ou mélatonine.", "tcsp"),
          ("t4", "t1", "Trouble cognitif léger", "Rivastigmine transdermique.", "tcsp"),
          ("t5", None, "Antidépresseur en cause", "Arrêt ou changement discuté.", "tcsp")],
   points=["L'AASM suggère de ne pas utiliser la stimulation cérébrale profonde pour ce trouble."], sources=["[Howell, J Clin Sleep Med 2023]"]),
  dict(titre="Suivre le risque neurodégénératif", rub=["pro", "sur", "fol"], comment="Annonce le risque avec tact et organise un suivi qui dépiste tôt.",
   tableau=(["Donnée", "Valeur", "Source"], [
     ["Conversion annuelle", "6,3 %", "Postuma 2019"],
     ["Conversion à 12 ans", _T("73,5 %", "Parkinson, démence à corps de Lewy, atrophie multisystématisée.")],
     ["Prédicteur moteur quantitatif", "HR 3,16", "Postuma 2019"],
     ["Hyposmie", "HR 2,62", "Postuma 2019"]]),
   points=["Le trouble peut précéder de plus de 10 ans les signes moteurs ou cognitifs."], sources=["[Postuma, Brain 2019]"]),
 ],
 ssp=dict(code="G11", nom="Troubles du sommeil (insomnies, hypersomnies ou somnolence, parasomnies)", officiel=True, algorithme=[
  ("n1", None, "Comportements nocturnes anormaux", "Le médecin précise horaire, récit, stéréotypie, ronflement et médicaments."),
  ("n2", "n1", "Rêves violents agis en fin de nuit", "Vidéo-polysomnographie.", "tcsp", "c2"),
  ("n3", "n2", "Sommeil paradoxal sans atonie", "TCSP : sécurité, mélatonine, suivi neurologique.", "tcsp", "c3"),
  ("n4", "n1", "Début de nuit, amnésie, sujet jeune", "Parasomnie du sommeil lent.", None, "c2"),
  ("n5", "n1", "Ronflement, apnées", "Polysomnographie : apnées imitatrices.", None, "c2"),
  ("n6", "n1", "Épisodes brefs et stéréotypés", "EEG-vidéo : épilepsie hypermotrice.", None, "c2")]),
 pec=[
  dict(cle="tcsp", titre="Trouble du comportement en sommeil paradoxal",
   but=["Prévenir les blessures du patient et du conjoint.", "Réduire les épisodes.", "Dépister tôt une synucléinopathie."],
   moyens=dict(accueil=["Interroger le conjoint.", "Évaluer les blessures.", "Revoir les médicaments."],
    pharma=[("Mélatonine à libération immédiate", "Au coucher ; à vérifier dans l'AIPS.", "Elle réduit les épisodes avec peu d'effets indésirables.", "[Howell, J Clin Sleep Med 2023]"),
            ("Clonazépam", "Faible dose au coucher ; à vérifier dans l'AIPS.", "Il réduit les comportements, au prix de la sédation.", "[Howell, J Clin Sleep Med 2023]"),
            ("Rivastigmine transdermique", "Si trouble cognitif léger ; à vérifier dans l'AIPS.", "Elle agit sur la composante cholinergique.", "[Howell, J Clin Sleep Med 2023]")],
    nonpharma=[("éducation thérapeutique", "Sécurisation de la chambre.", "Elle prévient les blessures."),
               ("hygiène de vie", "Éviter l'alcool et la privation de sommeil.", "Ils favorisent les épisodes."),
               ("autre", "Dormir séparément en cas de forme sévère.", "Il protège le conjoint.")],
    transversal=[("Médecine du sommeil", "Elle confirme le diagnostic."), ("Neurologie", "Elle suit le risque de conversion.")]),
   urgence=None,
   horsUrgence=(["Sécurité de la chambre.", "Suivi neurologique régulier."],
            [("d'abord", "médecin de famille", "Repère les rêves agis et revoit les médicaments."),
             ("ensuite", "médecin du sommeil", "Réalise la vidéo-polysomnographie."),
             ("puis", "neurologue", "Traite et suit le risque neurodégénératif.")]),
   pronostic="La forme isolée évolue vers une synucléinopathie à un rythme de 6,3 % par an, et 73,5 % des patients ont converti après 12 ans.",
   suivi=[("Épisodes et blessures", "À chaque consultation", "Rares, sans blessure"), ("Signes moteurs et cognitifs", "Au moins annuel", "Dépistés tôt"), ("Dysautonomie et odorat", "Annuel", "Évolution notée")],
   sortie="Le suivi reste ambulatoire et au long cours.",
   prevention=["Elle repose sur la sécurisation de la chambre.", "Elle passe par l'éviction des médicaments inducteurs.", "Elle ouvre l'accès à la recherche sur la neuroprotection."]),
 ])
AVERIFIER = ["Posologies de la mélatonine, du clonazépam et de la rivastigmine à vérifier dans l'AIPS (la mélatonine n'a pas forcément cette indication en Suisse).", "Prévalence d'environ 1 % après 60 ans : chiffre classique non vérifié ici sur une source primaire.", "Les critères ICSD-3 sont rapportés d'après leur contenu connu, sans consultation directe du manuel."]
