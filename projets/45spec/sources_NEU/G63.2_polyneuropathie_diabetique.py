ID = "G63.2__O3_2-E10"
PLAN = "monographique"
NOTIONS = [
"def|critère|1||[ADA, Standards of Care, 2026 ; avis d'expert]|La polyneuropathie diabétique distale symétrique atteint les fibres nerveuses de façon longueur-dépendante, d'abord aux pieds puis aux mains.",  # N01
"epi|chiffre|1||[ADA, Standards of Care, 2026]|Elle est fréquente et souvent asymptomatique, ce qui justifie un dépistage systématique.",  # N02
"bas|mécanisme|1||[avis d'expert]|L'hyperglycémie chronique, par stress oxydatif, glycation et microangiopathie des vasa nervorum, lèse d'abord les fibres les plus longues.",  # N03
"ana|symptôme|2||[avis d'expert]|Le patient décrit des paresthésies et des brûlures des pieds, souvent nocturnes, en chaussettes puis en gants.",  # N04
"exa|signe|2||[ADA, 2026 ; avis d'expert]|L'examen trouve une hypoesthésie distale en chaussettes, une baisse de la sensibilité vibratoire et une abolition des réflexes achilléens.",  # N05
"gold|examen|3||[ADA, Standards of Care, 2026]|Le dépistage débute au diagnostic d'un diabète de type 2 et 5 ans après celui d'un diabète de type 1, puis se répète au moins chaque année.",  # N06
"gold|examen|2||[ADA, Standards of Care, 2026]|Il associe la température ou la piqûre pour les petites fibres, le diapason de 128 Hz pour les grosses fibres et le monofilament de 10 g, qui ne s'utilise jamais seul.",  # N07
"alt|examen|1||[avis d'expert]|L'électroneuromyographie n'est utile que si le tableau est atypique.",  # N08
"red|piège|2||[avis d'expert]|Une atteinte asymétrique, motrice prédominante ou rapidement progressive fait chercher une autre cause, comme une polyradiculonévrite chronique ou une vascularite.",  # N09
"pos|diagnostic différentiel|2||[ADA, Standards of Care, 2026]|Une carence en vitamine B12 se recherche chez tout patient neuropathe, surtout sous metformine au long cours.",  # N10
"pos|diagnostic différentiel|1||[avis d'expert]|L'alcool, l'hypothyroïdie, l'insuffisance rénale, une gammapathie monoclonale ou un médicament neurotoxique sont d'autres causes à exclure.",  # N11
"acu|décision|2||[ADA, Standards of Care, 2026]|Un contrôle glycémique précoce prévient la neuropathie dans le type 1 et ralentit sa progression dans le type 2, avec le contrôle du poids, de la pression artérielle et des lipides.",  # N12
"acu|molécule|3||[ADA, Standards of Care, 2026]|La douleur neuropathique se traite d'abord par un gabapentinoïde, un inhibiteur de recapture de la sérotonine et de la noradrénaline, un tricyclique ou un bloqueur des canaux sodiques.",  # N13
"acu|posologie|1||[RCP Lyrica et Cymbalta ; AIPS Swissmedic]|La prégabaline débute à 150 mg par jour en 2 ou 3 prises, jusqu'à 600 mg au plus, avec adaptation rénale ; la duloxétine se donne à 60 mg une fois par jour ; à vérifier dans l'AIPS.",  # N14
"acu|piège|2||[ADA, Standards of Care, 2026]|Les opioïdes, y compris le tramadol et le tapentadol, ne s'utilisent pas pour la douleur neuropathique diabétique, sauf rare exception.",  # N15
"hos|complication|3||[ADA, Standards of Care, 2026]|La perte de la sensibilité protectrice expose à l'ulcère plantaire indolore et à l'amputation.",  # N16
"hos|complication|2||[ADA, Standards of Care, 2026]|Un pied chaud, rouge et gonflé sans plaie évoque une neuroarthropathie de Charcot : radiographie, décharge totale et avis spécialisé urgent.",  # N17
"sur|examen|1||[ADA, Standards of Care, 2026]|Un examen complet des pieds se fait au moins chaque année, et une inspection à chaque consultation en cas de perte de sensibilité, d'ulcère ou d'amputation.",  # N18
"sur|seuil|1||[ADA, Standards of Care, 2026]|La fréquence d'examen suit le risque : annuelle sans perte de sensibilité ni artériopathie, tous les 6 à 12 mois avec l'une d'elles, tous les 1 à 3 mois au risque élevé.",  # N19
"fol|décision|1||[ADA, Standards of Care, 2026]|Le patient à risque modéré ou élevé est adressé à une équipe spécialisée du pied, en urgence s'il a une plaie ouverte.",  # N20
"fol|contexte suisse|1|S|[OFSP, OPAS art. 11c, 2022]|Depuis 2022, l'assurance de base rembourse la podologie sur prescription médicale aux diabétiques présentant des facteurs de risque.",  # N21
"chr|prévention|1||[avis d'expert]|Le patient inspecte ses pieds chaque jour, porte des chaussures adaptées et ne marche pas pieds nus.",  # N22
"hos|complication|1||[ADA, Standards of Care, 2026]|La neuropathie autonome se dépiste chaque année : une baisse de 20 mmHg de systolique ou de 10 mmHg de diastolique au lever définit l'hypotension orthostatique.",  # N23
"pro|pronostic|1||[ADA, Standards of Care, 2026]|Le traitement ralentit la neuropathie mais ne récupère pas la perte neuronale.",  # N24
"hos|piège|1||[AIPS Swissmedic ; avis d'expert]|Les gabapentinoïdes donnent vertiges, somnolence et œdèmes, exposent aux chutes et s'adaptent à la fonction rénale.",  # N25
]
ANGLES = [
"Brûlures en chaussettes chez le diabétique = polyneuropathie.",
"Monofilament jamais seul : + diapason ou piqûre.",
"Gabapentinoïde, IRSN, tricyclique ; pas d'opioïde.",
"B12 sous metformine.",
"Pied chaud rouge sans plaie = Charcot.",
"Asymétrique ou motrice = autre cause.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un homme de 63 ans, diabétique de type 2 depuis 12 ans, consulte à Yverdon pour des brûlures et des fourmillements des deux pieds, pires la nuit. Il a l'impression de marcher sur du coton.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une polyneuropathie diabétique distale symétrique || Atteinte longueur-dépendante symétrique.", "Une artériopathie oblitérante || Elle donne une claudication à la marche.", "Un syndrome des jambes sans repos || Il donne un besoin de bouger, sans hypoesthésie.", "Une sciatique bilatérale || Elle suit un dermatome.", "Une goutte || Elle donne une arthrite aiguë."],
 notions="N04 N05 N01", angle="application", diff=1, ladder=L("Brûlures des pieds.", "Fibres longues lésées.", "Diabète ancien.", "Topographie.", "Polyneuropathie diabétique.", "Artériopathie.", "Chaussettes + diabète."), sources="[ADA, 2026]"),
dict(format="A", serie=("S1", 2, 4), stem="Vous voulez évaluer la sensibilité de ses pieds et le risque d'ulcère.", prompt="Quels tests choisissez-vous ?",
 items=["*Le monofilament de 10 g associé au diapason de 128 Hz || Le monofilament ne s'utilise jamais seul.", "Le monofilament seul || Il ne suffit pas au diagnostic.", "Une électroneuromyographie d'emblée || Elle se réserve aux formes atypiques.", "Une IRM médullaire || Rien ne l'indique.", "Une biopsie nerveuse || Elle n'est pas indiquée."],
 notions="N07 N05 N08", angle="direct", diff=2, ladder=L("Évaluer la sensibilité.", "Petites et grosses fibres.", "Pieds.", "Tests simples.", "Monofilament et diapason.", "ENMG.", "Monofilament + diapason."), sources="[ADA, 2026]"),
dict(format="A", serie=("S1", 3, 4), stem="Les tests confirment une atteinte. Les brûlures l'empêchent de dormir malgré le paracétamol.", prompt="Quel traitement proposez-vous ?",
 items=["*De la prégabaline ou de la duloxétine || Elles sont des traitements de premier choix.", "Du tramadol || Les opioïdes ne s'utilisent pas.", "De l'ibuprofène au long cours || Il est inefficace et néphrotoxique.", "De la prednisone || Elle n'est pas indiquée.", "Du diazépam || Il ne traite pas la douleur neuropathique."],
 notions="N13 N14", angle="application", diff=2, ladder=L("Douleur neuropathique.", "Modulation de la douleur.", "Insomnie.", "Premier choix.", "Prégabaline ou duloxétine.", "Opioïde.", "Gabapentinoïde ou IRSN."), sources="[ADA, 2026]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Vous organisez le suivi de cet homme traité par metformine.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une carence en vitamine B12 se recherche. || La metformine l'expose.", "V: Ses pieds s'inspectent à chaque consultation. || Il a perdu sa sensibilité.", "F: Le tramadol est une bonne alternative. || Les opioïdes ne s'utilisent pas.", "F: Normaliser l'HbA1c fera disparaître la neuropathie. || La perte neuronale ne récupère pas."],
 notions="N10 N18 N15 N24", angle="direct", diff=2, ladder=L("Suivi.", "Causes associées et pieds.", "Metformine.", "Surveillance.", "B12, pieds.", "Tramadol.", "B12 + pieds à chaque visite."), sources="[ADA, 2026]"),
dict(format="A", stem="Une femme de 58 ans, diabétique de type 2, a depuis 6 semaines une faiblesse croissante de la jambe droite et une douleur de la cuisse droite. La sensibilité est peu touchée.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Chercher une autre cause par ENMG et avis neurologique || L'atteinte asymétrique, motrice et rapide est atypique.", "Conclure à une polyneuropathie diabétique banale || Elle est symétrique et sensitive.", "Augmenter la prégabaline || Le diagnostic n'est pas posé.", "Rassurer et revoir dans un an || L'évolution rapide inquiète.", "Prescrire de la vitamine B1 seule || Elle ne règle pas le diagnostic."],
 notions="N09 N08", angle="piège", diff=3, ladder=L("Faiblesse asymétrique.", "Autre mécanisme.", "Évolution rapide.", "Tableau atypique.", "ENMG, neurologue.", "Polyneuropathie banale.", "Atypique = chercher."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 70 ans, diabétique de type 2 traité par metformine depuis 10 ans, a des paresthésies des pieds et une anémie macrocytaire.", prompt="Quel dosage demandez-vous en priorité ?",
 items=["*La vitamine B12 || La metformine favorise sa carence.", "La ferritine || L'anémie est macrocytaire.", "La vitamine D || Elle n'explique pas ce tableau.", "Le cuivre en premier || La B12 est bien plus probable.", "La CK || Rien n'évoque une myopathie."],
 notions="N10 N11", angle="application", diff=2, ladder=L("Paresthésies et macrocytose.", "Carence vitaminique.", "Metformine.", "Cause associée.", "B12.", "Fer.", "Metformine = B12."), sources="[ADA, 2026]"),
dict(format="A", stem="Une femme de 61 ans, diabétique avec perte de sensibilité des pieds, a depuis 5 jours un pied gauche chaud, rouge et gonflé, sans plaie ni fièvre. Elle se souvient d'une petite torsion.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Radiographie, décharge totale et avis spécialisé urgent pour une neuroarthropathie de Charcot || Le pied chaud sans plaie l'évoque.", "Antibiotique oral pour un érysipèle || Sans plaie ni fièvre, le Charcot prime.", "Anti-inflammatoire et reprise de la marche || L'appui détruit le pied.", "Rassurer, c'est une entorse || La neuropathie change l'interprétation.", "Échodoppler veineux seul || Il ne répond pas à la question."],
 notions="N17 N16", angle="piège", diff=3, ladder=L("Pied chaud rouge.", "Destruction ostéoarticulaire.", "Pas de plaie.", "Urgence.", "Charcot : décharge.", "Érysipèle.", "Chaud sans plaie = Charcot."), sources="[ADA, 2026]"),
dict(format="A", stem="Un homme de 67 ans, diabétique, découvre en se déchaussant une plaie indolore sous la tête du premier métatarsien droit.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*L'adresser en urgence à une équipe spécialisée du pied, avec décharge || La plaie ouverte l'impose.", "Lui conseiller une crème et un contrôle dans 3 mois || La plaie menace le membre.", "Attendre qu'elle devienne douloureuse || La neuropathie supprime la douleur.", "Lui faire marcher davantage pour la circulation || L'appui aggrave l'ulcère.", "Prescrire uniquement de la prégabaline || Elle ne traite pas la plaie."],
 notions="N16 N20 N07", angle="application", diff=2, ladder=L("Plaie indolore.", "Perte de sensibilité protectrice.", "Métatarsien.", "Urgence du pied.", "Équipe spécialisée.", "Attendre.", "Plaie = urgence."), sources="[ADA, 2026]"),
dict(format="A", stem="Un homme de 52 ans vient d'apprendre qu'il a un diabète de type 2. Il n'a aucun symptôme aux pieds.", prompt="Quand dépistez-vous une atteinte nerveuse ?",
 items=["*Dès maintenant, puis au moins chaque année || Le dépistage débute au diagnostic.", "Dans 5 ans || Ce délai concerne le type 1.", "Seulement s'il a des symptômes || L'atteinte est souvent asymptomatique.", "Seulement si l'HbA1c dépasse 10 % || Le dépistage est systématique.", "Jamais, le risque est faible || Il est réel."],
 notions="N06 N02", angle="direct", diff=2, ladder=L("Diabète nouveau.", "Atteinte silencieuse.", "Type 2.", "Calendrier.", "Au diagnostic, puis annuel.", "5 ans.", "Type 2 : tout de suite."), sources="[ADA, 2026]"),
dict(format="A", stem="Une femme de 66 ans, diabétique, souffre de brûlures plantaires. Elle demande du tapentadol, qui a soulagé une amie.", prompt="Que lui répondez-vous ?",
 items=["*Les opioïdes ne s'utilisent pas ; un gabapentinoïde, un IRSN ou un tricyclique sont préférables || Ils sont le premier choix.", "Le tapentadol est le premier choix || Les opioïdes sont déconseillés.", "Le tramadol est une alternative sûre || Il est aussi déconseillé.", "La morphine à faible dose est recommandée || Elle est déconseillée.", "Aucun traitement n'existe || Plusieurs classes sont efficaces."],
 notions="N15 N13", angle="piège", diff=2, ladder=L("Demande d'opioïde.", "Choix thérapeutique.", "Tapentadol.", "Erreur fréquente.", "Pas d'opioïde.", "Tapentadol.", "Neuropathie : pas d'opioïde."), sources="[ADA, 2026]"),
dict(format="A", stem="Un homme de 59 ans, diabétique de type 2 depuis 15 ans avec paresthésies des pieds, a des vertiges en se levant. Sa pression passe de 140/80 couché à 112/66 mmHg debout, sans accélération du pouls.", prompt="Quelle atteinte expliquent ces chiffres ?",
 items=["*Une neuropathie autonome cardiovasculaire avec hypotension orthostatique || La systolique baisse de plus de 20 mmHg.", "Une déshydratation simple || Le pouls s'accélérerait.", "Un vertige positionnel paroxystique bénin || Il ne baisse pas la pression.", "Une sténose aortique || Elle ne s'explique pas ainsi.", "Une hypoglycémie || Elle ne dépend pas de la position."],
 notions="N23 N06", angle="application", diff=3, ladder=L("Vertiges au lever.", "Dysautonomie.", "Baisse de 28 mmHg.", "Seuil.", "Hypotension orthostatique.", "Déshydratation.", "> 20/10 = orthostatique."), sources="[ADA, 2026]"),
dict(masque=False, sit="monographique", format="A", stem="Une étudiante demande pourquoi la polyneuropathie diabétique commence aux orteils.", prompt="Quelle explication est la plus juste ?",
 items=["*Les fibres les plus longues sont lésées les premières par l'hyperglycémie chronique || L'atteinte est longueur-dépendante.", "Les pieds reçoivent moins de glucose || C'est l'excès de glucose qui lèse.", "La moelle lombaire est comprimée || L'atteinte est périphérique.", "Les chaussures compriment les nerfs || La cause est métabolique.", "Un virus gagne les nerfs des pieds || Rien ne l'indique."],
 notions="N03 N04 N01", angle="direct", diff=2, ladder=L("Topographie.", "Longueur des axones.", "Orteils d'abord.", "Mécanisme.", "Fibres longues.", "Compression.", "Plus long = plus tôt."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 78 ans, avec une insuffisance rénale chronique, prend de la prégabaline pour des brûlures des pieds. Elle a chuté deux fois et se sent somnolente.", prompt="Quelle mesure est la plus adaptée ?",
 items=["*Réduire la prégabaline selon la fonction rénale || Elle s'accumule et donne vertiges et somnolence.", "Doubler la dose || Elle aggraverait les chutes.", "Ajouter du tramadol || Il est déconseillé et majore les chutes.", "Ajouter un somnifère || Il majorerait la somnolence.", "Ne rien changer || Les chutes l'imposent."],
 notions="N25 N14", angle="application", diff=2, ladder=L("Chutes sous prégabaline.", "Élimination rénale.", "Insuffisance rénale.", "Effet indésirable.", "Réduire la dose.", "Augmenter.", "Rein = adapter."), sources="[AIPS Swissmedic]"),
dict(format="A", stem="Un homme de 22 ans, diabétique de type 1 depuis 2 ans, pense que l'équilibre glycémique n'a plus d'importance pour ses nerfs.", prompt="Quelle réponse est la plus juste ?",
 items=["*Un contrôle glycémique précoce prévient ou retarde la neuropathie dans le type 1 || Le niveau de preuve est élevé.", "Le contrôle glycémique n'a aucun effet sur les nerfs || Il a un effet préventif.", "Seule la pression artérielle compte || La glycémie est centrale.", "La neuropathie est inévitable || Elle peut être retardée.", "Un contrôle glycémique strict guérit une neuropathie installée || La perte neuronale ne récupère pas."],
 notions="N12 N24", angle="piège", diff=2, ladder=L("Prévention.", "Glycémie et nerfs.", "Type 1 jeune.", "Niveau de preuve.", "Prévient dans le type 1.", "Inutile.", "Type 1 : la glycémie protège."), sources="[ADA, 2026]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous enseignez le dépistage de la polyneuropathie diabétique.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le diapason de 128 Hz teste les grosses fibres. || Il mesure la sensibilité vibratoire.", "V: Dans le type 2, le dépistage débute au diagnostic. || L'atteinte peut précéder le diagnostic.", "F: Le monofilament de 10 g suffit seul au diagnostic. || Il s'associe à un autre test.", "F: Dans le type 1, le dépistage débute au diagnostic. || Il débute 5 ans après."],
 notions="N07 N06", angle="piège", diff=2, ladder=L("Enseignement.", "Tests et calendrier.", "Type 1 et 2.", "Erreurs fréquentes.", "Diapason, type 2 au diagnostic.", "Monofilament seul.", "Deux tests, bon calendrier."), sources="[ADA, 2026]"),
dict(format="Kprim", stem="Une femme de 69 ans, diabétique, a perdu la sensibilité protectrice des pieds, sans artériopathie ni antécédent d'ulcère. Vous préparez avec elle un plan de soins à Martigny.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Ses pieds s'examinent tous les 6 à 12 mois au moins. || Elle a perdu la sensibilité.", "V: La podologie peut être remboursée par l'assurance de base sur prescription. || C'est le cas depuis 2022 en Suisse.", "V: Un pied chaud, rouge et gonflé sans plaie impose une décharge et un avis urgent. || Il évoque un Charcot.", "F: Marcher pieds nus à la maison est sans risque. || Une blessure passerait inaperçue."],
 notions="N19 N21 N17 N22", angle="application", diff=2, ladder=L("Plan de soins.", "Prévention des ulcères.", "Perte de sensibilité.", "Rythme et réseau.", "Examen, podologie, alerte.", "Pieds nus.", "Surveiller, podologue, alerte."), sources="[ADA, 2026 ; OFSP, 2022]"),
dict(format="Kprim", stem="Un homme de 64 ans souffre de brûlures plantaires diabétiques. Vous discutez des antalgiques.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La duloxétine est un traitement de premier choix. || Elle est un IRSN.", "V: Un tricyclique est possible, avec prudence chez le sujet âgé. || Ses effets anticholinergiques gênent.", "F: Les opioïdes sont recommandés en second choix. || Ils ne s'utilisent pas.", "F: La prégabaline ne demande aucune adaptation rénale. || Elle s'élimine par le rein."],
 notions="N13 N15 N25", angle="piège", diff=2, ladder=L("Antalgiques.", "Classes efficaces.", "Brûlures.", "Pièges.", "IRSN, tricyclique.", "Opioïdes.", "Pas d'opioïde, rein pour la prégabaline."), sources="[ADA, 2026]"),
dict(format="MenuLong", stem="Vous dépistez une atteinte nerveuse chez un patient diabétique.", prompt="Quels tests utilisez-vous ? (3 réponses)",
 items=["*Monofilament de 10 g || Il teste la sensibilité protectrice.", "*Diapason de 128 Hz || Il teste les grosses fibres.", "*Piqûre ou température || Elles testent les petites fibres.", "IRM lombaire || Elle ne dépiste pas.", "Biopsie nerveuse || Elle n'est pas un test de dépistage.", "Électroneuromyographie systématique || Elle se réserve aux formes atypiques.", "Dosage de la CK || Il n'est pas utile.", "Radiographie du pied || Elle cherche un Charcot.", "Index de pression systolique seul || Il cherche une artériopathie.", "Test de Romberg seul || Il ne suffit pas.", "Glycémie capillaire || Elle ne teste pas les nerfs.", "Scanner cérébral || Il n'est pas utile."],
 notions="N07 N06", angle="direct", diff=1, ladder=L("Dépistage.", "Fibres petites et grosses.", "Tests de cabinet.", "Lesquels.", "Monofilament, diapason, piqûre.", "ENMG.", "Trois tests simples."), sources="[ADA, 2026]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un patient diabétique présente une polyneuropathie sensitive distale.", prompt="Quelles autres causes devez-vous exclure ? (3 réponses)",
 items=["*Carence en vitamine B12 || Surtout sous metformine.", "*Consommation excessive d'alcool || Elle est neurotoxique.", "*Hypothyroïdie || Elle peut causer une neuropathie.", "Migraine || Elle ne cause pas de neuropathie.", "Asthme || Il n'en fait pas partie.", "Hypertension artérielle seule || Elle ne cause pas ce tableau.", "Myopie || Elle n'a aucun lien.", "Reflux gastro-œsophagien || Il n'a aucun lien.", "Psoriasis || Il n'en fait pas partie.", "Lithiase biliaire || Elle n'a aucun lien.", "Anémie ferriprive || Elle ne cause pas de neuropathie.", "Arthrose du genou || Elle n'en fait pas partie."],
 notions="N10 N11 N09", angle="application", diff=2, ladder=L("Neuropathie.", "Causes multiples.", "Diabétique.", "Diagnostic différentiel.", "B12, alcool, thyroïde.", "Arthrose.", "Ne pas tout attribuer au diabète."), sources="[ADA, 2026 ; avis d'expert]"),
dict(format="A", stem="Un homme de 57 ans, diabétique de type 2 avec paresthésies des pieds, est en surpoids et hypertendu ; son LDL est élevé.", prompt="Quelle stratégie ralentit le mieux la progression de son atteinte nerveuse ?",
 items=["*Optimiser à la fois glycémie, poids, pression artérielle et lipides || Ces facteurs réduisent le risque ou ralentissent l'évolution.", "Viser seulement la normoglycémie la plus rapide possible || Le contrôle multifactoriel compte.", "Prescrire de la prégabaline préventive || Elle traite la douleur, pas l'évolution.", "Supplémenter en vitamines sans bilan || Elle ne vise pas la cause.", "Ne rien faire, l'atteinte est installée || La progression peut être ralentie."],
 notions="N12 N24", angle="application", diff=2, ladder=L("Prévention secondaire.", "Facteurs métaboliques.", "Surpoids, HTA, LDL.", "Stratégie.", "Contrôle multifactoriel.", "Glycémie seule.", "Tout optimiser."), sources="[ADA, 2026]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Polyneuropathie diabétique : la dépister chaque année par plusieurs tests simples, exclure les autres causes, traiter la douleur sans opioïde et protéger le pied contre l'ulcère et le Charcot",
 notions=[
  dict(titre="Reconnaître et dépister", rub=["ana", "exa", "gold", "epi"], comment="Dépiste tôt, car l'atteinte reste souvent silencieuse.",
   tableau=(["Test", "Fibres", "Rôle"], [
     ["Piqûre ou température", "Petites fibres", "Douleur et brûlures"],
     ["Diapason 128 Hz", "Grosses fibres", "Sensibilité vibratoire"],
     ["Monofilament 10 g", _T("Sensibilité protectrice", "Sa perte prédit l'ulcère."), _T("Jamais seul", "Il s'associe à un autre test.")]]),
   points=["Type 2 : au diagnostic ; type 1 : après 5 ans ; puis chaque année."], sources=["[ADA, Standards of Care, 2026]"]),
  dict(titre="Ne pas tout attribuer au diabète", rub=["pos", "red", "alt"], comment="Cherche une autre cause si le tableau dévie.",
   tableau=(["Indice", "Cause à chercher", "Examen"], [
     ["Metformine au long cours", "Carence en B12", "Vitamine B12"],
     ["Asymétrie, atteinte motrice, évolution rapide", _T("Polyradiculonévrite, vascularite", "Le mécanisme n'est pas métabolique."), "ENMG, neurologue"],
     ["Consommation d'alcool", "Neuropathie alcoolique", "Anamnèse"],
     ["Fatigue, frilosité", "Hypothyroïdie", "TSH"]]),
   points=["ENMG seulement si atypique."], sources=["[ADA, 2026]", "[avis d'expert]"]),
  dict(titre="Traiter", rub=["acu", "chr"], comment="Ralentis l'atteinte et calme la douleur sans opioïde.",
   arbre=[("t1", None, "Polyneuropathie confirmée", "Le traitement est multifactoriel."),
          ("t2", "t1", "Contrôle métabolique", "Glycémie, poids, PA, lipides.", "pnd"),
          ("t3", "t1", "Douleur neuropathique", "Gabapentinoïde, IRSN, tricyclique ou bloqueur sodique.", "pnd"),
          ("t4", "t3", "Insuffisant", "Associer deux classes.", "pnd"),
          ("t5", "t3", "Demande d'opioïde", "Refuser, sauf rare exception.", "pnd")],
   points=["Prégabaline : adaptation rénale."], sources=["[ADA, Standards of Care, 2026]"]),
  dict(titre="Protéger le pied", rub=["hos", "sur", "fol"], comment="Adapte le rythme de surveillance au risque et agis vite devant une plaie.",
   tableau=(["Situation", "Conduite", "Pourquoi"], [
     ["Sans perte de sensibilité ni artériopathie", "Examen annuel", "Risque faible."],
     ["Perte de sensibilité ou artériopathie", "Examen tous les 6-12 mois", "Risque d'ulcère."],
     ["Plaie ouverte", _T("Avis spécialisé urgent", "Le membre est menacé."), "Ulcère indolore."],
     ["Pied chaud, rouge, gonflé sans plaie", _T("Décharge totale, radiographie", "Le Charcot détruit le pied à l'appui."), "Charcot."]]),
   points=["Podologie remboursée sur prescription en Suisse depuis 2022."], sources=["[ADA, 2026]", "[OFSP, 2022]"]),
 ],
 ssp=dict(code="S5.5", nom="Douleur, brûlure, crampe ou engourdissement des extrémités", officiel=True, algorithme=[
  ("n1", None, "Brûlures ou engourdissement des extrémités", "La topographie oriente."),
  ("n2", "n1", "Symétrique, distal, chez un diabétique", "Polyneuropathie diabétique.", "pnd", "c1"),
  ("n3", "n1", "Asymétrique ou moteur rapide", "Autre cause : ENMG.", None, "c1"),
  ("n4", "n1", "Claudication à la marche", "Artériopathie (même SSP).", None, "c1"),
  ("n5", "n2", "Sous metformine", "Doser la B12.", "pnd", "c2"),
  ("n6", "n2", "Douleur", "Gabapentinoïde ou IRSN.", "pnd", "c2"),
  ("n7", "n2", "Plaie ou pied chaud", "Équipe du pied en urgence.", "pnd", "c3")]),
 pec=[
  dict(cle="pnd", titre="Polyneuropathie diabétique distale symétrique",
   but=["Ralentir l'atteinte nerveuse.", "Soulager la douleur.", "Prévenir ulcère et amputation."],
   moyens=dict(accueil=["Examiner les pieds et tester la sensibilité.", "Rechercher une carence en B12 et d'autres causes.", "Évaluer la douleur et le sommeil."],
    pharma=[("Prégabaline (gabapentinoïde)", "150 mg/j en 2-3 prises, max 600 mg/j, adaptation rénale ; à vérifier dans l'AIPS.", "Elle réduit la douleur neuropathique.", "[ADA, 2026 ; AIPS Swissmedic]"),
            ("Duloxétine (IRSN)", "60 mg une fois par jour ; à vérifier dans l'AIPS.", "Elle réduit la douleur et aide si une dépression coexiste.", "[ADA, 2026 ; AIPS Swissmedic]"),
            ("Amitriptyline (tricyclique)", "Faible dose le soir ; à vérifier dans l'AIPS.", "Elle soulage la douleur, avec prudence chez le sujet âgé.", "[ADA, 2026]"),
            ("Vitamine B12", "Si carence ; à vérifier dans l'AIPS.", "Elle corrige une cause associée, fréquente sous metformine.", "[ADA, 2026]")],
    nonpharma=[("éducation thérapeutique", "Inspecter les pieds chaque jour, porter des chaussures adaptées, éviter de marcher pieds nus.", "Le patient repère tôt une plaie qu'il ne sent pas."),
               ("soins infirmiers", "Soins de podologie et décharge des zones d'appui.", "Ils préviennent l'ulcère."),
               ("hygiène de vie", "Perte de poids, activité physique, arrêt du tabac et de l'alcool.", "Ils ralentissent l'atteinte nerveuse et vasculaire.")],
    transversal=[("Endocrinologie-diabétologie", "Elle optimise le contrôle glycémique."), ("Podologie", "Elle prévient les lésions du pied à risque.")]),
   urgence=(["Décharger immédiatement le pied.", "Adresser en urgence à une équipe du pied."],
            [("d'abord", "médecin de famille", "Reconnaît la plaie ou le Charcot et met le pied en décharge."),
             ("ensuite", "équipe spécialisée du pied", "Évalue infection, ischémie et destruction osseuse."),
             ("puis", "podologue", "Assure les soins et la décharge au long cours.")]),
   horsUrgence=(["Dépistage annuel.", "Rythme d'examen du pied selon le risque."],
            [("d'abord", "médecin de famille", "Dépiste chaque année et classe le risque du pied."),
             ("ensuite", "diabétologue", "Optimise le contrôle métabolique."),
             ("puis", "podologue", "Soigne le pied à risque sur prescription."),
             ("en même temps", "patient·e", "Inspecte ses pieds chaque jour.")]),
   pronostic="Le traitement ralentit la neuropathie sans récupérer la perte neuronale ; la perte de sensibilité protectrice expose à l'ulcère et à l'amputation.",
   suivi=[("Examen des pieds", "Selon le risque, de 1 à 12 mois", "Pas de plaie"), ("Douleur et sommeil", "À chaque consultation", "Douleur contrôlée"), ("Vitamine B12", "Périodiquement sous metformine", "Valeur normale")],
   sortie="Le suivi reste ambulatoire, avec un recours rapide à l'équipe du pied en cas de plaie.",
   prevention=["Elle optimise glycémie, poids, PA et lipides.", "Elle éduque à l'inspection quotidienne des pieds.", "Elle organise la podologie pour le pied à risque."]),
 ])
AVERIFIER = ["Posologies suisses de la prégabaline, de la duloxétine et de l'amitriptyline dans la douleur neuropathique diabétique à vérifier dans l'AIPS.",
             "Prévalence chiffrée de la polyneuropathie diabétique en Suisse à vérifier."]
