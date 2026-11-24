ID = "G97.1__S7_6-E09"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[ICHD-3, IHS, 2018]|La céphalée post-ponction durale survient dans les 5 jours après une ponction lombaire, par fuite de LCR, et disparaît spontanément en 2 semaines ou après un blood patch.",  # N01
"epi|chiffre|1||[Nath, Lancet, 2018]|Dans la méta-analyse de Nath, l'aiguille atraumatique a abaissé l'incidence de 11,0 % à 4,2 % par rapport à l'aiguille tranchante.",  # N02
"bas|mécanisme|1||[avis d'expert]|La fuite de LCR fait baisser la pression intracrânienne ; le cerveau s'affaisse, tire sur les structures sensibles et les veines se dilatent par compensation.",  # N03
"ana|symptôme|3||[ICHD-3, IHS, 2018 ; avis d'expert]|La douleur est orthostatique : elle apparaît ou s'aggrave en position debout et se soulage en position couchée.",  # N04
"ana|signe|1||[ICHD-3, IHS, 2018]|Elle s'accompagne souvent d'une raideur de nuque, d'acouphènes ou d'une hypoacousie, de nausées, et rarement d'une diplopie par atteinte du VI.",  # N05
"exa|signe|1||[avis d'expert]|L'examen est normal, sans fièvre ni déficit focal.",  # N06
"red|piège|2||[avis d'expert]|Une douleur devenue permanente et non posturale, une fièvre, un déficit, une crise ou une baisse de vigilance font chercher hématome sous-dural, thrombose veineuse ou méningite.",  # N07
"gold|examen|2||[Uppal, JAMA Netw Open, 2023]|Le diagnostic est clinique ; l'imagerie se réserve aux tableaux atypiques ou réfractaires.",  # N08
"alt|examen|1||[avis d'expert]|L'IRM avec gadolinium montre, en cas d'hypotension du LCR, une prise de contraste pachyméningée diffuse et un affaissement cérébral.",  # N09
"pos|diagnostic différentiel|2||[avis d'expert]|La méningite donne fièvre et syndrome méningé ; la migraine n'est pas posturale ; l'hypotension intracrânienne spontanée survient sans ponction.",  # N10
"acu|décision|2||[Uppal, JAMA Netw Open, 2023]|Le traitement initial est conservateur : antalgiques simples, hydratation et repos selon le confort, car beaucoup de céphalées guérissent seules.",  # N11
"acu|piège|2||[Arevalo-Rodriguez, Cochrane, 2016]|L'alitement prolongé après une ponction lombaire ne prévient pas la céphalée.",  # N12
"chr|décision|3||[Uppal, JAMA Netw Open, 2023]|Le blood patch épidural est le traitement de choix d'une céphalée sévère ou persistante malgré le traitement conservateur.",  # N13
"chr|posologie|1||[Uppal, JAMA Netw Open, 2023]|L'anesthésiste injecte du sang autologue stérile dans l'espace épidural au niveau de la ponction ; le volume exact est à vérifier dans la recommandation.",  # N14
"hos|complication|1||[avis d'expert]|L'hématome sous-dural et la thrombose veineuse cérébrale sont des complications rares mais graves.",  # N15
"hos|complication|1||[avis d'expert]|Le blood patch donne souvent une douleur lombaire transitoire et rarement une radiculalgie ou une infection.",  # N16
"pro|pronostic|1||[ICHD-3, IHS, 2018]|La plupart des céphalées disparaissent en quelques jours à 2 semaines.",  # N17
"sur|examen|1||[avis d'expert]|Le suivi vérifie la disparition de la douleur posturale et la reprise des activités.",  # N18
"fol|prévention|2||[Nath, Lancet, 2018]|L'aiguille atraumatique (pointe de crayon) et de petit calibre prévient la céphalée ; la femme jeune, l'IMC bas et un antécédent augmentent le risque.",  # N19
"bas|mécanisme|1||[avis d'expert]|L'aiguille tranchante coupe la dure-mère, alors que l'aiguille atraumatique écarte ses fibres et laisse une brèche plus petite.",  # N20
"fol|terrain particulier|1||[avis d'expert]|Une brèche accidentelle par aiguille de Tuohy lors d'une péridurale obstétricale donne souvent une céphalée sévère.",  # N21
"fol|décision|1||[avis d'expert]|Le médecin adresse à l'anesthésiste pour le blood patch et au neurologue en cas de tableau atypique.",  # N22
"sur|examen|1||[avis d'expert]|Après un blood patch, le patient consulte en cas de fièvre, de douleur lombaire croissante ou de déficit.",  # N23
"ana|symptôme|1||[avis d'expert]|La douleur commence le plus souvent dans les 48 heures après la ponction.",  # N24
"acu|molécule|1||[Uppal, JAMA Netw Open, 2023]|La caféine n'a qu'un bénéfice modeste et transitoire, et les fortes doses exposent à l'insomnie et aux crises.",  # N25
"hos|piège|1||[avis d'expert]|En cas d'échec ou de récidive, un second blood patch se discute, puis une recherche d'une autre fuite.",  # N26
]
ANGLES = [
"Debout = mal, couché = soulagé.",
"Pas d'imagerie si typique.",
"Antalgiques puis blood patch.",
"Aiguille atraumatique pour prévenir.",
"L'alitement ne prévient rien.",
"Non postural, fièvre, déficit = autre cause.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une juriste de 27 ans, à Lausanne, a eu il y a 2 jours une ponction lombaire diagnostique à l'aiguille tranchante de 20 G. Elle a mal à la tête dès qu'elle se lève ; couchée, la douleur disparaît en 15 minutes. Elle a la nuque raide et des acouphènes, sans fièvre.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une céphalée post-ponction durale || Douleur orthostatique dans les 5 jours après la ponction.", "Une méningite bactérienne || Elle donne fièvre et douleur non posturale.", "Une migraine || Elle ne cède pas en position couchée.", "Une hémorragie méningée || Elle débute brutalement et ne varie pas avec la position.", "Une hypertension intracrânienne || Elle s'aggrave couchée."],
 notions="N04 N01 N24 N05", angle="application", diff=1, ladder=L("Mal de tête après geste.", "Hypotension du LCR.", "Debout, couché.", "Profil postural.", "Post-ponction.", "Méningite.", "Debout mal, couchée bien."), sources="[ICHD-3, IHS, 2018]"),
dict(format="A", serie=("S1", 2, 4), stem="L'examen neurologique de cette patiente est normal, sans fièvre.", prompt="Quel examen demandez-vous ?",
 items=["*Aucun, le diagnostic est clinique || Le tableau est typique.", "Une IRM avec gadolinium en urgence || Elle se réserve aux formes atypiques.", "Un scanner cérébral || Il n'apporte rien ici.", "Une nouvelle ponction lombaire || Elle aggraverait la fuite.", "Des hémocultures || Il n'y a pas de fièvre."],
 notions="N08 N06", angle="direct", diff=1, ladder=L("Examen normal.", "Bilan.", "Tableau typique.", "Utilité.", "Aucun examen.", "IRM.", "Typique = clinique."), sources="[Uppal, JAMA Netw Open, 2023]"),
dict(format="A", serie=("S1", 3, 4), stem="Elle demande ce qu'elle peut faire pour aller mieux.", prompt="Que lui proposez-vous d'abord ?",
 items=["*Antalgiques simples, hydratation et repos selon le confort || Beaucoup de cas guérissent seuls.", "Un blood patch immédiat || Il suit l'échec du traitement conservateur sauf forme sévère.", "De la morphine en continu || Elle n'est pas indiquée.", "Des corticoïdes à haute dose || Ils ne sont pas recommandés.", "Une intervention chirurgicale || Elle n'est pas indiquée."],
 notions="N11 N17 N25", angle="application", diff=1, ladder=L("Traitement initial.", "Conservateur.", "Guérison spontanée.", "Premier pas.", "Antalgiques, hydratation.", "Blood patch d'emblée.", "D'abord conservateur."), sources="[Uppal, JAMA Netw Open, 2023]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Quatre jours plus tard, elle ne peut toujours pas rester debout plus de 10 minutes et ne peut pas travailler.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un blood patch épidural est le traitement de choix. || Le tableau est sévère et persistant.", "V: L'anesthésiste injecte du sang autologue dans l'espace épidural. || Le caillot obture la brèche.", "F: Il faut d'abord une semaine d'alitement strict. || L'alitement n'apporte pas de bénéfice.", "F: Une IRM est obligatoire avant tout blood patch. || Le tableau typique n'en exige pas."],
 notions="N13 N14 N12 N08", angle="application", diff=2, ladder=L("Échec du conservateur.", "Traitement invasif.", "Brèche.", "Geste.", "Blood patch.", "Alitement.", "Persistant = blood patch."), sources="[Uppal, JAMA Netw Open, 2023]"),
dict(format="A", stem="Un homme de 72 ans sous anticoagulant a eu une ponction lombaire il y a 12 jours. Ses maux de tête, d'abord posturaux, sont devenus permanents. Il vomit et sa femme le trouve confus.", prompt="Quelle conduite est prioritaire ?",
 items=["*Une imagerie cérébrale urgente pour chercher un hématome sous-dural || La perte du caractère postural et la confusion sont des signaux d'alerte.", "Un blood patch sans imagerie || Il retarderait le diagnostic.", "Un antalgique et du repos || Les drapeaux rouges imposent l'imagerie.", "De la caféine à forte dose || Elle ne répond pas au problème.", "Une nouvelle ponction lombaire || Elle serait dangereuse."],
 notions="N07 N15", angle="piège", diff=2, ladder=L("Aggravation.", "Complication.", "Confusion, anticoagulant.", "Drapeau rouge.", "Imagerie urgente.", "Blood patch.", "Plus postural = imager."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 35 ans a eu une ponction lombaire hier. Il a mal à la tête, 39,2 °C et une raideur de nuque marquée, même couché.", prompt="Quelle hypothèse imposez-vous d'éliminer ?",
 items=["*Une méningite iatrogène || La fièvre et la douleur non posturale l'évoquent.", "Une simple céphalée post-ponction || Elle ne donne pas de fièvre.", "Une migraine || Elle ne donne pas de fièvre.", "Une céphalée de tension || Elle ne donne pas de fièvre.", "Une sinusite || La chronologie désigne la ponction."],
 notions="N10 N07", angle="piège", diff=2, ladder=L("Fièvre après geste.", "Infection.", "Raideur, couché.", "Drapeau rouge.", "Méningite.", "Post-ponction.", "Fièvre = infection."), sources="[avis d'expert]"),
dict(format="A", stem="Vous préparez une ponction lombaire diagnostique chez une femme de 30 ans mince.", prompt="Quelle mesure réduit le plus le risque de maux de tête après le geste ?",
 items=["*Utiliser une aiguille atraumatique de petit calibre || Elle écarte les fibres durales.", "Imposer 24 heures d'alitement || Il ne prévient rien.", "Faire boire 3 litres || L'hydratation ne prévient pas.", "Utiliser une aiguille tranchante de gros calibre || Elle augmente le risque.", "Donner de la caféine avant le geste || Elle n'a pas d'effet préventif démontré."],
 notions="N19 N20 N02", angle="direct", diff=1, ladder=L("Prévention.", "Choix de l'aiguille.", "Femme jeune.", "Mesure efficace.", "Aiguille atraumatique.", "Alitement.", "Pointe de crayon."), sources="[Nath, Lancet, 2018]"),
dict(format="A", stem="Après une ponction lombaire, l'infirmier veut garder le patient à plat 4 heures pour éviter les maux de tête.", prompt="Que lui répondez-vous ?",
 items=["*L'alitement ne prévient pas les maux de tête ; le patient peut se lever || Les essais n'ont pas montré de bénéfice.", "Il faut 24 heures à plat || L'alitement ne prévient rien.", "Il faut le mettre tête en bas || Rien ne le justifie.", "Il faut lui donner un blood patch préventif systématique || Ce n'est pas recommandé.", "Il faut lui donner de la morphine || Elle n'est pas indiquée."],
 notions="N12 N19", angle="piège", diff=2, ladder=L("Consigne après geste.", "Prévention.", "Alitement.", "Preuve.", "Inutile.", "24 heures à plat.", "Le lit ne prévient pas."), sources="[Arevalo-Rodriguez, Cochrane, 2016]"),
dict(format="A", stem="Une femme de 29 ans a accouché sous péridurale ; l'anesthésiste a noté une brèche accidentelle de la dure-mère. Le lendemain, elle ne peut plus se lever ni allaiter assise à cause d'un mal de tête intense qui cède couchée.", prompt="Quelle conduite proposez-vous ?",
 items=["*Un traitement conservateur bref puis un blood patch si la douleur reste sévère || L'aiguille de Tuohy laisse une grosse brèche.", "Un scanner cérébral systématique || Le tableau est typique.", "Arrêter l'allaitement || Rien ne l'impose.", "Une ponction lombaire de contrôle || Elle aggraverait la fuite.", "Des triptans || Ce n'est pas une migraine."],
 notions="N21 N13 N04", angle="application", diff=2, ladder=L("Post-partum.", "Brèche obstétricale.", "Tuohy.", "Traitement.", "Blood patch si sévère.", "Scanner.", "Grosse brèche = patch."), sources="[Uppal, JAMA Netw Open, 2023]"),
dict(masque=False, sit="monographique", format="A", stem="Vous enseignez les critères ICHD-3 de la céphalée post-ponction durale.", prompt="Dans quel délai après la ponction la céphalée doit-elle apparaître ?",
 items=["*Dans les 5 jours || C'est le critère ICHD-3.", "Dans les 2 heures || Le délai est plus long.", "Dans les 24 heures exclusivement || Le délai est plus long.", "Dans le mois || Il est trop long.", "Le délai n'a aucune importance || Il fait partie des critères."],
 notions="N01 N17", angle="direct", diff=2, ladder=L("Critères.", "ICHD-3.", "Délai.", "Seuil.", "5 jours.", "24 heures.", "Dans les 5 jours."), sources="[ICHD-3, IHS, 2018]"),
dict(format="A", stem="Une femme de 40 ans a des maux de tête qui apparaissent debout et cèdent couchée depuis une quinte de toux il y a 3 semaines. Elle n'a eu ni ponction ni anesthésie.", prompt="Quel examen demandez-vous ?",
 items=["*Une IRM cérébrale avec gadolinium || Elle cherche une hypotension intracrânienne spontanée.", "Aucun examen || Le tableau sans ponction doit s'explorer.", "Une ponction lombaire diagnostique d'emblée || Elle aggraverait une fuite.", "Un EEG || Il est inutile.", "Un doppler des carotides || Il ne répond pas."],
 notions="N10 N09 N08", angle="application", diff=3, ladder=L("Douleur posturale.", "Hypotension du LCR.", "Sans ponction.", "Imagerie.", "IRM gadolinium.", "Aucun examen.", "Sans ponction = spontanée."), sources="[avis d'expert]"),
dict(format="A", stem="Un étudiant demande pourquoi la douleur apparaît en position debout après une fuite de LCR.", prompt="Quel mécanisme expliquez-vous ?",
 items=["*La pression du LCR baisse, le cerveau s'affaisse et tire sur les structures sensibles ; les veines se dilatent || C'est l'hypotension du LCR.", "La pression intracrânienne augmente debout || Elle baisse.", "Une inflammation méningée || Elle donne fièvre.", "Une vasoconstriction cérébrale || Ce n'est pas le mécanisme.", "Une contracture musculaire cervicale isolée || Elle n'explique pas le caractère postural."],
 notions="N03 N04", angle="direct", diff=2, ladder=L("Caractère postural.", "Hypotension du LCR.", "Debout.", "Mécanisme.", "Affaissement, traction.", "Hypertension.", "Moins de LCR = traction."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 33 ans a, depuis une ponction lombaire il y a 5 jours, des maux de tête posturaux et voit double en regardant à gauche.", prompt="Quelle atteinte explique la diplopie ?",
 items=["*Une atteinte du nerf abducens (VI) par traction || Son long trajet le rend vulnérable.", "Une atteinte du III || Elle donnerait ptosis et mydriase.", "Une myasthénie || La chronologie désigne la ponction.", "Un AVC du tronc || L'examen serait différent.", "Une atteinte du IV || Elle donne une diplopie verticale."],
 notions="N05 N03", angle="application", diff=3, ladder=L("Diplopie.", "Nerf crânien.", "Regard latéral.", "Mécanisme.", "VI par traction.", "III.", "Horizontale = VI."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 31 ans a des maux de tête posturaux depuis une ponction lombaire. Un ami lui conseille de boire 10 cafés par jour.", prompt="Que lui répondez-vous ?",
 items=["*La caféine aide peu et brièvement, et ces doses exposent à l'insomnie et aux crises || Le bénéfice est modeste.", "C'est le traitement le plus efficace || Le blood patch l'est davantage.", "Il faut aussi rester alité une semaine || L'alitement n'aide pas.", "Il faut y ajouter un triptan || Ce n'est pas une migraine.", "La caféine est contre-indiquée en toute dose || Une dose modérée est acceptable."],
 notions="N25 N11", angle="piège", diff=2, ladder=L("Conseil populaire.", "Caféine.", "10 cafés.", "Bénéfice et risque.", "Modeste, toxique à forte dose.", "Traitement majeur.", "Café ≠ solution."), sources="[Uppal, JAMA Netw Open, 2023]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez la céphalée post-ponction durale.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Elle s'aggrave en position debout. || Elle est orthostatique.", "V: Elle peut s'accompagner d'acouphènes. || L'hypotension du LCR touche l'oreille interne.", "F: Elle apparaît typiquement après 2 semaines. || Elle apparaît dans les 5 jours.", "F: La fièvre en fait partie. || Elle oriente vers une méningite."],
 notions="N01 N04 N05 N07", angle="direct", diff=1, ladder=L("Révision.", "Critères.", "Posture, oreille.", "Pièges.", "Debout, acouphènes.", "Fièvre.", "Posture sans fièvre."), sources="[ICHD-3, IHS, 2018]"),
dict(format="Kprim", stem="Un homme de 45 ans a reçu hier un blood patch pour des maux de tête posturaux après ponction lombaire.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une douleur lombaire transitoire est fréquente. || Elle suit l'injection.", "V: Il doit consulter en cas de fièvre ou de déficit. || Une infection ou un hématome sont possibles.", "F: Un second blood patch est toujours impossible. || Il se discute en cas d'échec.", "F: Aucun suivi n'est utile. || Le suivi vérifie la disparition de la douleur."],
 notions="N16 N23 N26 N18", angle="application", diff=2, ladder=L("Après blood patch.", "Suivi.", "Effets.", "Consignes.", "Lombalgie, alerte.", "Aucun suivi.", "Consulter si fièvre."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Une équipe révise ses pratiques de ponction lombaire pour limiter les maux de tête après le geste.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'aiguille atraumatique réduit le risque. || Elle écarte les fibres.", "V: La femme jeune a un risque plus élevé. || C'est un facteur connu.", "F: Une hydratation abondante prévient la céphalée. || Elle n'a pas montré d'effet préventif.", "F: L'alitement de 24 heures prévient la céphalée. || Il n'a pas montré d'effet."],
 notions="N19 N12 N11", angle="piège", diff=2, ladder=L("Pratiques.", "Prévention.", "Aiguille, terrain.", "Mythes.", "Atraumatique.", "Alitement.", "Aiguille, pas le lit."), sources="[Nath, Lancet, 2018 ; Arevalo-Rodriguez, Cochrane, 2016]"),
dict(format="MenuLong", stem="Un patient a mal à la tête depuis une ponction lombaire il y a 4 jours.", prompt="Quels éléments imposent une imagerie cérébrale ? (3 réponses)",
 items=["*Déficit moteur focal || Il évoque hématome ou thrombose.", "*Crise convulsive || Elle évoque une thrombose veineuse.", "*Douleur devenue permanente, non posturale || Elle évoque un hématome sous-dural.", "Douleur soulagée couchée || Elle est typique.", "Raideur de nuque sans fièvre || Elle est fréquente.", "Acouphènes || Ils sont fréquents.", "Nausées || Elles sont fréquentes.", "Début 24 heures après le geste || Il est typique.", "Photophobie modérée || Elle est fréquente.", "Douleur occipitale || Elle est fréquente.", "Soulagement partiel par le paracétamol || Il est attendu.", "Antécédent de migraine || Il ne change rien."],
 notions="N07 N10", angle="direct", diff=2, ladder=L("Après ponction.", "Drapeaux rouges.", "Imagerie.", "Lesquels.", "Déficit, crise, non postural.", "Acouphènes.", "Alerte = imager."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Vous informez des patients avant une ponction lombaire.", prompt="Quels éléments augmentent le risque de maux de tête après le geste ? (3 réponses)",
 items=["*Aiguille tranchante de gros calibre || Elle laisse une grosse brèche.", "*Sexe féminin et âge jeune || Ce sont des facteurs connus.", "*Antécédent de céphalée après ponction || Il augmente le risque.", "Âge supérieur à 70 ans || Le risque diminue avec l'âge.", "Obésité || Elle ne l'augmente pas.", "Aiguille atraumatique || Elle réduit le risque.", "Alitement court après le geste || Il ne change rien.", "Position couchée pendant le geste || Elle ne l'augmente pas.", "Hydratation normale || Elle ne change rien.", "Prise de paracétamol || Elle ne change rien.", "Petit calibre d'aiguille || Il réduit le risque.", "Ponction réussie au premier essai || Elle ne l'augmente pas."],
 notions="N19 N02", angle="application", diff=2, ladder=L("Information.", "Facteurs de risque.", "Aiguille, terrain.", "Lesquels.", "Tranchante, femme jeune, antécédent.", "Âge avancé.", "Gros calibre tranchant."), sources="[Nath, Lancet, 2018]"),
dict(format="A", stem="Une femme de 38 ans a été soulagée par un blood patch, mais ses maux de tête posturaux reviennent partiellement 3 jours plus tard. Elle n'a ni fièvre ni déficit.", prompt="Quelle conduite proposez-vous ?",
 items=["*Discuter avec l'anesthésiste un second blood patch, puis chercher une autre fuite en cas d'échec || La récidive partielle est possible.", "Conclure à une cause psychogène || La récidive posturale est organique.", "Opérer d'emblée la dure-mère || Ce n'est pas la première étape.", "Prescrire des opioïdes au long cours || Ils ne traitent pas la fuite.", "Imposer l'alitement prolongé || Il n'apporte rien."],
 notions="N26 N13 N22", angle="piège", diff=3, ladder=L("Récidive.", "Échec partiel.", "Après patch.", "Suite.", "Second patch.", "Psychogène.", "Échec = second patch."), sources="[Uppal, JAMA Netw Open, 2023]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Céphalée post-ponction durale : la reconnaître à son caractère orthostatique dans les 5 jours, écarter les drapeaux rouges, traiter d'abord simplement puis par blood patch, et la prévenir par l'aiguille atraumatique",
 notions=[
  dict(titre="Reconnaître", rub=["def", "ana", "exa", "bas"], comment="Relie la douleur posturale à la fuite de LCR.",
   tableau=(["Élément", "Caractère", "Pourquoi"], [
     ["Délai", "≤ 5 jours après la ponction", "Souvent dans les 48 heures"],
     ["Douleur", _T("Debout aggravée, couchée soulagée", "La traction varie avec la position."), "Hypotension du LCR"],
     ["Signes associés", "Nuque raide, acouphènes, nausées", "Diplopie par atteinte du VI rare"]]),
   points=["Examen normal, sans fièvre."], sources=["[ICHD-3, IHS, 2018]"]),
  dict(titre="Écarter le grave", rub=["red", "gold", "alt", "pos"], comment="N'image que les tableaux atypiques.",
   tableau=(["Signal", "Cause à évoquer", "Examen"], [
     ["Fièvre, raideur couché", "Méningite", "Ponction, hémocultures"],
     ["Douleur non posturale, confusion", "Hématome sous-dural", "Imagerie urgente"],
     ["Crise, déficit", "Thrombose veineuse", "IRM ou angio-CT veineux"],
     ["Sans ponction", _T("Hypotension spontanée", "IRM gadolinium : prise de contraste pachyméningée."), "IRM"]]),
   points=["Typique : aucun examen."], sources=["[Uppal, JAMA Netw Open, 2023]"]),
  dict(titre="Traiter", rub=["acu", "chr", "hos"], comment="Escalade du simple au blood patch.",
   arbre=[("t1", None, "Douleur posturale post-ponction", "Beaucoup guérissent seules."),
          ("t2", "t1", "Légère", "Antalgiques, hydratation, repos selon confort.", "cpp"),
          ("t3", "t1", "Sévère ou persistante", "Blood patch épidural.", "cpp"),
          ("t4", "t3", "Échec", "Second patch, puis recherche d'une autre fuite.", "cpp")],
   points=["Caféine : bénéfice modeste."], sources=["[Uppal, JAMA Netw Open, 2023]"]),
  dict(titre="Prévenir et suivre", rub=["pro", "sur", "fol"], comment="Choisit la bonne aiguille et suit l'évolution.",
   tableau=(["Mesure", "Effet", "Source"], [
     ["Aiguille atraumatique", _T("11,0 % → 4,2 %", "Méta-analyse de Nath, 2018."), "[Nath, Lancet, 2018]"],
     ["Alitement", "Aucun effet préventif", "[Arevalo-Rodriguez, Cochrane, 2016]"],
     ["Après patch", "Consulter si fièvre ou déficit", "[avis d'expert]"]]),
   points=["Femme jeune, IMC bas, antécédent : risque plus élevé."], sources=["[Nath, Lancet, 2018]"]),
 ],
 ssp=dict(code="S7.6", nom="Céphalées", officiel=True, algorithme=[
  ("n1", None, "Céphalée après ponction", "Les drapeaux rouges se cherchent d'abord."),
  ("n2", "n1", "Fièvre, déficit, non posturale", "Autre cause : imagerie ou ponction.", None, "c2"),
  ("n3", "n1", "Orthostatique, ≤ 5 jours", "Céphalée post-ponction durale.", "cpp", "c1"),
  ("n4", "n3", "Légère", "Traitement conservateur.", "cpp", "c3"),
  ("n5", "n3", "Sévère ou persistante", "Blood patch.", "cpp", "c3"),
  ("n6", "n5", "Échec", "Second patch, autre fuite.", "cpp", "c3"),
  ("n7", "n1", "Prochain geste", "Aiguille atraumatique.", "cpp", "c4")]),
 pec=[
  dict(cle="cpp", titre="Céphalée post-ponction durale",
   but=["Soulager rapidement et rendre l'autonomie.", "Ne pas manquer une complication grave."],
   moyens=dict(accueil=["Vérifier le caractère orthostatique et l'absence de fièvre.", "Expliquer l'évolution le plus souvent spontanément favorable.", "Donner des consignes de retour."],
    pharma=[("Paracétamol (antalgique)", "Dose usuelle ; à vérifier dans l'AIPS.", "Il soulage la douleur.", "[Uppal, JAMA Netw Open, 2023]"),
            ("Ibuprofène (AINS)", "Dose usuelle ; à vérifier dans l'AIPS.", "Il soulage la douleur.", "[Uppal, JAMA Netw Open, 2023]"),
            ("Caféine (méthylxanthine)", "Dose modérée ; à vérifier dans l'AIPS.", "Son bénéfice reste modeste et transitoire.", "[Uppal, JAMA Netw Open, 2023]")],
    nonpharma=[("geste ou chirurgie", "Blood patch épidural autologue.", "Il obture la brèche et soulage vite."),
               ("hygiène de vie", "Repos selon le confort et hydratation normale.", "Ils améliorent le confort sans prévenir."),
               ("éducation thérapeutique", "Consignes de retour après le geste.", "Elles font reconnaître une complication.")],
    transversal=[("Anesthésiologie", "Elle réalise le blood patch."), ("Obstétrique", "Elle signale les brèches accidentelles de péridurale.")]),
   urgence=None,
   horsUrgence=(["Recherche des drapeaux rouges.", "Escalade vers le blood patch si sévère."],
            [("d'abord", "médecin responsable", "Confirme le caractère orthostatique et écarte les drapeaux rouges."),
             ("ensuite", "médecin responsable", "Prescrit antalgiques et repos selon le confort."),
             ("puis", "anesthésiste", "Réalise le blood patch si la douleur persiste."),
             ("puis", "neurologue", "Explore un tableau atypique ou réfractaire.")]),
   pronostic="La guérison survient le plus souvent en quelques jours à 2 semaines, ou rapidement après blood patch.",
   suivi=[("Douleur debout", "Quotidien les premiers jours", "Disparition"), ("Fièvre, déficit", "Jusqu'à guérison", "Absents"), ("Reprise des activités", "À 1 semaine", "Complète")],
   sortie="Le patient rentre avec des consignes de retour.",
   prevention=["Elle utilise une aiguille atraumatique de petit calibre.", "Elle abandonne l'alitement systématique.", "Elle informe les patients à risque."]),
 ])
AVERIFIER = ["Volume recommandé du blood patch épidural à vérifier dans Uppal 2023.", "Doses de paracétamol, d'ibuprofène et de caféine à vérifier dans l'AIPS."]
