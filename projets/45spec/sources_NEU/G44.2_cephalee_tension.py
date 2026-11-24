ID = "G44.2__G10-E02"
PLAN = "monographique"
NOTIONS = [
"def|critère|1||[ICHD-3, IHS, 2018]|La céphalée de tension est une céphalée primaire, habituellement bilatérale, en pression ou en étau, d'intensité légère à modérée.",  # N01
"epi|chiffre|1||[Bendtsen, EFNS, Eur J Neurol, 2010]|Elle est le type de céphalée le plus fréquent dans la population et cause un handicap notable dans ses formes fréquentes.",  # N02
"bas|mécanisme|1||[avis d'expert]|Une sensibilisation des voies nociceptives, d'abord périphérique puis centrale, entretient la forme chronique.",  # N03
"ana|critère|3||[ICHD-3, IHS, 2018]|Les épisodes durent de 30 minutes à 7 jours et présentent au moins deux de quatre caractères : bilatérale, en pression non pulsatile, légère à modérée, non aggravée par l'activité courante.",  # N04
"ana|critère|2||[ICHD-3, IHS, 2018]|La céphalée de tension ne donne ni nausée ni vomissement et au plus une seule photophobie ou phonophobie.",  # N05
"ana|seuil|2||[ICHD-3, IHS, 2018]|La forme est peu fréquente sous 1 jour par mois, fréquente de 1 à 14 jours par mois, et chronique à 15 jours par mois ou plus depuis plus de 3 mois.",  # N06
"exa|signe|1||[ICHD-3, IHS, 2018]|L'examen neurologique est normal, et la palpation manuelle trouve souvent une sensibilité des muscles péricrâniens.",  # N07
"red|piège|3||[avis d'expert]|Un début brutal, une fièvre, un déficit focal, un œdème papillaire ou une céphalée nouvelle après 50 ans imposent de chercher une cause secondaire.",  # N08
"gold|examen|2||[avis d'expert ; Bendtsen, EFNS, 2010]|Le diagnostic est clinique : sans drapeau rouge, aucune imagerie n'est utile.",  # N09
"pos|diagnostic différentiel|2||[ICHD-3, IHS, 2018]|La migraine se distingue par une douleur souvent unilatérale et pulsatile, aggravée par l'effort et accompagnée de nausées.",  # N10
"alt|examen|1||[avis d'expert]|Après 50 ans, une céphalée temporale récente avec claudication de la mâchoire fait doser VS et CRP pour une artérite à cellules géantes.",  # N11
"acu|molécule|2||[Bendtsen, EFNS, Eur J Neurol, 2010]|Les antalgiques simples et les AINS traitent l'épisode ; les associations avec caféine sont un second choix.",  # N12
"acu|posologie|1||[Bendtsen, EFNS, 2010 ; AIPS Swissmedic]|Les doses usuelles sont ibuprofène 200 à 800 mg, acide acétylsalicylique 500 à 1000 mg ou paracétamol 1000 mg par prise, à vérifier dans l'AIPS.",  # N13
"acu|piège|2||[Bendtsen, EFNS, Eur J Neurol, 2010]|Les triptans, les myorelaxants et les opioïdes ne s'utilisent pas dans la céphalée de tension.",  # N14
"hos|complication|3||[ICHD-3, IHS, 2018]|La céphalée par abus médicamenteux survient si les antalgiques simples se prennent 15 jours par mois ou plus, ou les triptans, associations et opioïdes 10 jours par mois ou plus, depuis plus de 3 mois.",  # N15
"chr|décision|2||[Diener, EAN, Eur J Neurol, 2020]|L'abus médicamenteux se traite d'abord par l'information ; l'arrêt peut être brutal pour les antalgiques simples, mais il est progressif pour les opioïdes et les tranquillisants.",  # N16
"chr|molécule|2||[Bendtsen, EFNS, Eur J Neurol, 2010]|L'amitriptyline est le traitement préventif de premier choix de la forme chronique ; la mirtazapine et la venlafaxine sont des seconds choix.",  # N17
"chr|décision|1||[Bendtsen, EFNS, 2010]|L'information, la réassurance et l'identification des facteurs déclenchants se proposent toujours.",  # N18
"chr|prévention|1||[Bendtsen, EFNS, 2010]|Le biofeedback électromyographique a une efficacité documentée, et la thérapie cognitivo-comportementale et la relaxation sont probablement efficaces.",  # N19
"chr|décision|1||[Bendtsen, EFNS, 2010]|La physiothérapie et l'acupuncture peuvent aider dans la forme fréquente, sans preuve robuste.",  # N20
"fol|contexte suisse|1|S|[OPAS art. 5 al. 2]|En Suisse, le médecin prescrit la physiothérapie par séries de 9 séances au plus par prescription.",  # N21
"fol|contexte suisse|1|S|[OPAS art. 11b ; OFSP, 2022]|Depuis le 1er juillet 2022, la psychothérapie pratiquée par un psychologue psychothérapeute est remboursée sur prescription médicale, par séries de 15 séances au plus.",  # N22
"sur|examen|1||[Diener, EAN, 2020 ; avis d'expert]|Un agenda des céphalées et des prises d'antalgiques objective la fréquence et dépiste l'abus médicamenteux.",  # N23
"pro|pronostic|1||[Bendtsen, EFNS, 2010]|L'efficacité des traitements préventifs est souvent limitée et leurs effets indésirables peuvent les freiner.",  # N24
"fol|terrain particulier|1||[avis d'expert]|L'anxiété, la dépression et les troubles du sommeil favorisent la chronicisation et se recherchent.",  # N25
"hos|piège|1||[AIPS Swissmedic ; avis d'expert]|L'amitriptyline donne somnolence, sécheresse buccale et prise de poids, et se prescrit avec prudence chez le sujet âgé ou cardiaque.",  # N26
]
ANGLES = [
"Bilatérale, en étau, sans nausée = tension.",
"Sans drapeau rouge, aucune imagerie.",
"Antalgique simple ou AINS ; jamais d'opioïde ni de triptan.",
"Antalgiques ≥ 15 j/mois = abus médicamenteux.",
"Amitriptyline pour la forme chronique.",
"Drapeau rouge = céphalée secondaire.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une comptable de 36 ans consulte à Neuchâtel pour des maux de tête qui reviennent 3 jours par mois depuis un an. La douleur serre les deux tempes comme un bandeau, dure 4 à 6 heures en fin de journée et ne l'empêche pas de travailler. Elle n'a ni nausée ni gêne à la lumière.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une céphalée de tension épisodique fréquente || Bilatérale, en étau, légère, sans nausée.", "Une migraine sans aura || Elle est pulsatile avec nausée ou photophobie.", "Une algie vasculaire de la face || Elle est orbitaire unilatérale et atroce.", "Une hypertension intracrânienne || Elle s'aggrave et donne des vomissements.", "Une céphalée par abus médicamenteux || Elle suppose une prise excessive d'antalgiques."],
 notions="N04 N05 N01", angle="application", diff=1, ladder=L("Céphalée en bandeau.", "Céphalée primaire.", "3 jours par mois.", "Profil clinique.", "Céphalée de tension.", "Migraine.", "Étau + bilatéral + sans nausée."), sources="[ICHD-3, IHS, 2018]"),
dict(format="A", serie=("S1", 2, 4), stem="L'examen neurologique de cette patiente est normal. La palpation des muscles temporaux et trapèzes est sensible.", prompt="Quel examen complémentaire demandez-vous ?",
 items=["*Aucun, le diagnostic est clinique || Aucun drapeau rouge n'est présent.", "Une IRM cérébrale || Elle n'apporte rien sans drapeau rouge.", "Un scanner cérébral || Il irradie sans bénéfice.", "Un EEG || Il n'est pas utile.", "Une ponction lombaire || Rien ne l'indique."],
 notions="N09 N07", angle="direct", diff=1, ladder=L("Examen normal.", "Céphalée primaire.", "Sensibilité péricrânienne.", "Utilité des examens.", "Aucun examen.", "IRM rassurante.", "Clinique sans alerte = rien."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 3, 4), stem="Elle demande quoi prendre lors d'un épisode.", prompt="Que lui conseillez-vous ?",
 items=["*De l'ibuprofène ou du paracétamol || Antalgiques simples et AINS sont le premier choix.", "Du sumatriptan || Les triptans ne s'utilisent pas ici.", "Du tramadol || Les opioïdes ne s'utilisent pas.", "Du tétrazépam ou un autre myorelaxant || Les myorelaxants ne s'utilisent pas.", "De la prednisone || Elle n'est pas indiquée."],
 notions="N12 N13", angle="application", diff=1, ladder=L("Traitement de crise.", "Antalgie simple.", "Épisode léger.", "Premier choix.", "AINS ou paracétamol.", "Triptan.", "Simple avant tout."), sources="[Bendtsen, EFNS, 2010]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Vous fixez avec cette patiente les règles d'utilisation de ses antalgiques.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Des antalgiques simples pris 15 jours par mois ou plus exposent à une céphalée par abus médicamenteux. || C'est le seuil ICHD-3.", "V: Un agenda des céphalées et des prises aide le suivi. || Il objective la fréquence.", "F: Un triptan soulagera mieux ses épisodes. || Les triptans ne s'utilisent pas ici.", "F: Un opioïde est un bon second choix. || Les opioïdes ne s'utilisent pas."],
 notions="N15 N23 N14 N12", angle="direct", diff=2, ladder=L("Règles d'usage.", "Abus médicamenteux.", "Fréquence des prises.", "Seuils.", "< 15 j/mois, agenda.", "Opioïde.", "Compter les jours."), sources="[ICHD-3, IHS, 2018 ; Bendtsen, EFNS, 2010]"),
dict(format="A", stem="Une femme de 71 ans a depuis 3 semaines une céphalée bilatérale en pression, plus marquée aux tempes. Elle a mal à la mâchoire en mastiquant et se sent fatiguée.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Doser VS et CRP en urgence pour une artérite à cellules géantes || La céphalée nouvelle après 50 ans est un drapeau rouge.", "Conclure à une céphalée de tension et prescrire du paracétamol || L'âge et la claudication imposent un bilan.", "Prescrire de l'amitriptyline || Le diagnostic n'est pas posé.", "Adresser au dentiste || La claudication évoque une artérite.", "Faire de la physiothérapie cervicale || Elle retarderait le diagnostic."],
 notions="N08 N11", angle="piège", diff=2, ladder=L("Céphalée nouvelle à 71 ans.", "Vascularite des artères temporales.", "Claudication de la mâchoire.", "Drapeau rouge.", "VS et CRP.", "Tension.", "Nouvelle après 50 = bilan."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 44 ans décrit une céphalée diffuse en pression, apparue il y a 6 semaines, qui s'aggrave et le réveille avec des vomissements. Le fond d'œil montre un œdème papillaire bilatéral.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Une imagerie cérébrale en urgence || L'œdème papillaire signe une hypertension intracrânienne.", "Un antalgique simple et un contrôle dans un mois || Le drapeau rouge impose une imagerie.", "De l'amitriptyline || Le diagnostic n'est pas posé.", "Une physiothérapie || Elle retarderait le diagnostic.", "Un agenda des céphalées seul || L'urgence est diagnostique."],
 notions="N09 N08", angle="piège", diff=2, ladder=L("Céphalée croissante.", "Hypertension intracrânienne.", "Œdème papillaire.", "Drapeau rouge.", "Imagerie urgente.", "Antalgique.", "Papille = imager."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 42 ans a mal à la tête 20 jours par mois depuis 8 mois. Elle prend du paracétamol presque tous les jours, environ 25 jours par mois. Ses maux de tête étaient autrefois bilatéraux, en étau et occasionnels.", prompt="Quel diagnostic s'ajoute au diagnostic initial ?",
 items=["*Une céphalée par abus médicamenteux || Antalgiques simples 15 jours par mois ou plus depuis plus de 3 mois.", "Une tumeur cérébrale || Rien ne l'évoque.", "Une migraine chronique || La douleur n'a pas de caractère migraineux.", "Une intoxication hépatique aiguë || Rien ne l'indique ici.", "Une sinusite chronique || Rien ne l'évoque."],
 notions="N15 N06", angle="application", diff=2, ladder=L("Céphalée quasi quotidienne.", "Abus médicamenteux.", "25 jours de paracétamol.", "Seuil.", "Abus médicamenteux.", "Tumeur.", "≥ 15 j/mois = abus."), sources="[ICHD-3, IHS, 2018]"),
dict(format="A", stem="Vous confirmez chez cette femme un abus de paracétamol sans autre médicament.", prompt="Quelle première étape proposez-vous ?",
 items=["*L'informer, puis arrêter le paracétamol, éventuellement de façon brutale, avec un traitement préventif || L'information est la première étape.", "Remplacer le paracétamol par du tramadol || Il aggraverait l'abus.", "Augmenter la dose de paracétamol || Elle entretient la céphalée.", "Ajouter un triptan quotidien || Il aggraverait l'abus.", "Hospitaliser d'emblée pour un sevrage lent de plusieurs mois || L'arrêt peut être brutal pour un antalgique simple."],
 notions="N16 N15", angle="application", diff=2, ladder=L("Abus d'antalgique simple.", "Sevrage.", "Paracétamol.", "Mode d'arrêt.", "Information et arrêt.", "Opioïde.", "Informer puis arrêter."), sources="[Diener, EAN, 2020]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 50 ans souffre d'une céphalée de tension chronique, 20 jours par mois depuis 1 an, sans abus d'antalgiques.", prompt="Quel traitement préventif proposez-vous en premier ?",
 items=["*De l'amitriptyline à faible dose le soir || Elle est le premier choix.", "Du sumatriptan quotidien || Il n'est pas préventif ici.", "Un anticorps anti-CGRP || Il est réservé à la migraine.", "Du diazépam au long cours || Il expose à la dépendance.", "Du tramadol || Les opioïdes ne s'utilisent pas."],
 notions="N17 N06", angle="application", diff=2, ladder=L("Forme chronique.", "Prophylaxie.", "20 jours par mois.", "Premier choix.", "Amitriptyline.", "Anti-CGRP.", "Chronique = amitriptyline."), sources="[Bendtsen, EFNS, 2010]"),
dict(format="A", stem="Une femme de 27 ans a 2 fois par mois une céphalée gauche pulsatile de 12 heures, avec nausées. Monter les escaliers l'aggrave et elle doit s'allonger.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Une migraine sans aura || Unilatérale, pulsatile, aggravée par l'effort, avec nausées.", "Une céphalée de tension épisodique || Elle n'est ni pulsatile ni nauséeuse.", "Une algie vasculaire || Ses crises sont orbitaires et courtes.", "Une névralgie du trijumeau || Elle donne des décharges de secondes.", "Une céphalée par abus médicamenteux || Les crises sont rares."],
 notions="N10 N05", angle="piège", diff=2, ladder=L("Céphalée pulsatile.", "Céphalée primaire.", "Nausées, effort.", "Distinguer.", "Migraine.", "Tension.", "Pulsatile + nausée = migraine."), sources="[ICHD-3, IHS, 2018]"),
dict(format="A", stem="Un homme de 39 ans souffre de céphalées bilatérales en étau 6 jours par mois. Il demande un « relaxant musculaire » ou de la codéine, conseillés par un collègue.", prompt="Que lui répondez-vous ?",
 items=["*Ces médicaments ne s'utilisent pas ; un AINS ou du paracétamol suffisent || Les myorelaxants et opioïdes n'ont pas leur place.", "La codéine est le meilleur choix || Les opioïdes ne s'utilisent pas.", "Un myorelaxant quotidien est recommandé || Il n'est pas recommandé.", "Un triptan est préférable || Il ne s'utilise pas ici.", "Un corticoïde est indiqué || Il n'est pas indiqué."],
 notions="N14 N12", angle="piège", diff=2, ladder=L("Demande du patient.", "Choix du traitement.", "Codéine, myorelaxant.", "Erreur fréquente.", "AINS ou paracétamol.", "Codéine.", "Pas d'opioïde ni de myorelaxant."), sources="[Bendtsen, EFNS, 2010]"),
dict(format="A", stem="Une femme de 45 ans souffre de céphalées bilatérales en étau devenues presque quotidiennes. Elle dort mal et se sent anxieuse depuis une surcharge professionnelle.", prompt="Quel mécanisme explique le mieux le passage à une forme quotidienne ?",
 items=["*Une sensibilisation centrale des voies de la douleur, favorisée par l'anxiété et le mauvais sommeil || Elle entretient la chronicisation.", "Une compression vasculaire du nerf || Elle explique la névralgie du trijumeau.", "Une inflammation méningée || Elle donne fièvre et raideur.", "Une hyperpression du liquide cérébrospinal || Elle donne un œdème papillaire.", "Une vasodilatation trigémino-vasculaire || Elle explique plutôt la migraine."],
 notions="N03 N25", angle="direct", diff=3, ladder=L("Chronicisation.", "Sensibilisation centrale.", "Anxiété, sommeil.", "Mécanisme.", "Sensibilisation.", "Vasculaire.", "Stress + sommeil = chronicisation."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un enseignant de 41 ans atteint d'une céphalée de tension chronique préfère éviter les médicaments.", prompt="Quelle approche non médicamenteuse a le meilleur appui scientifique ?",
 items=["*Le biofeedback électromyographique, avec TCC ou relaxation || Son efficacité est documentée.", "Le repos strict au lit || Il n'est pas recommandé.", "Les manipulations cervicales répétées || Leur preuve est faible.", "Le jeûne || Il peut déclencher des céphalées.", "Les lunettes teintées || Elles n'ont aucun effet démontré."],
 notions="N19 N18 N22", angle="application", diff=2, ladder=L("Sans médicament.", "Approche comportementale.", "Forme chronique.", "Niveau de preuve.", "Biofeedback, TCC.", "Repos.", "Biofeedback documenté."), sources="[Bendtsen, EFNS, 2010]"),
dict(format="A", stem="Un homme de 33 ans a, depuis 18 mois, 6 jours par mois des céphalées bilatérales en pression de quelques heures, sans nausée.", prompt="Comment classez-vous cette céphalée ?",
 items=["*Épisodique fréquente || Elle survient 1 à 14 jours par mois.", "Épisodique peu fréquente || Elle survient moins d'un jour par mois.", "Chronique || Elle exige 15 jours par mois ou plus.", "Migraine chronique || Les caractères ne sont pas migraineux.", "Céphalée quotidienne nouvelle persistante || Le début n'est pas brutal et quotidien."],
 notions="N06 N04", angle="direct", diff=2, ladder=L("Fréquence.", "Classification ICHD-3.", "6 jours par mois.", "Seuils.", "Épisodique fréquente.", "Chronique.", "1-14 j/mois = fréquente."), sources="[ICHD-3, IHS, 2018]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous enseignez la céphalée de tension à des étudiants.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Elle est en pression non pulsatile. || C'est un des quatre caractères.", "V: Elle ne donne pas de nausée. || La nausée oriente vers la migraine.", "F: L'activité physique courante l'aggrave. || Elle ne l'aggrave pas.", "F: Une IRM se fait systématiquement. || Le diagnostic est clinique."],
 notions="N04 N05 N09 N10", angle="direct", diff=1, ladder=L("Enseignement.", "Critères ICHD-3.", "Caractères.", "Erreurs fréquentes.", "Pression, sans nausée.", "IRM systématique.", "Étau, calme, clinique."), sources="[ICHD-3, IHS, 2018]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Une femme de 68 ans commence de l'amitriptyline pour une céphalée de tension chronique.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'amitriptyline est le préventif de premier choix. || Selon l'EFNS 2010.", "V: Elle se prend le soir, car elle peut endormir. || La somnolence est fréquente.", "F: Son effet est complet en 2 jours. || L'effet est lent et souvent partiel.", "F: Elle ne demande aucune prudence chez le sujet âgé. || Les effets anticholinergiques et cardiaques imposent la prudence."],
 notions="N17 N26 N24", angle="piège", diff=2, ladder=L("Prophylaxie.", "Antidépresseur tricyclique.", "68 ans.", "Tolérance.", "Premier choix, prudence.", "Effet rapide.", "Lent, partiel, prudent."), sources="[Bendtsen, EFNS, 2010 ; AIPS Swissmedic]"),
dict(format="Kprim", stem="Un homme de 47 ans, à Bienne, souffre de céphalées bilatérales en étau 10 jours par mois avec des cervicalgies. Vous discutez des mesures non médicamenteuses.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le médecin prescrit la physiothérapie par séries de 9 séances au plus. || C'est la règle de l'OPAS.", "V: L'acupuncture peut être une option, sans preuve robuste. || L'EFNS la mentionne.", "F: La physiothérapie a une efficacité solidement démontrée. || Les preuves restent limitées.", "F: La psychothérapie d'un psychologue n'est jamais remboursée. || Elle l'est sur prescription médicale depuis 2022."],
 notions="N21 N20 N22 N19", angle="application", diff=2, ladder=L("Mesures non médicamenteuses.", "Physiothérapie et psychothérapie.", "Suisse.", "Remboursement.", "9 séances, prescription.", "Preuve robuste.", "Physio, psy, sur prescription."), sources="[OPAS ; Bendtsen, EFNS, 2010]"),
dict(format="MenuLong", stem="Un patient consulte pour une céphalée.", prompt="Quels éléments imposent de chercher une cause secondaire ? (3 réponses)",
 items=["*Début brutal en coup de tonnerre || Il évoque une hémorragie méningée.", "*Fièvre avec raideur de nuque || Elle évoque une méningite.", "*Œdème papillaire || Il évoque une hypertension intracrânienne.", "Douleur bilatérale en étau || Elle est typique d'une céphalée primaire.", "Sensibilité des muscles péricrâniens || Elle est fréquente dans la tension.", "Céphalée liée au stress || Elle est banale.", "Durée de 4 heures || Elle est compatible.", "Absence de nausée || Elle est typique.", "Antécédent familial de céphalée || Il est fréquent.", "Céphalée en fin de journée || Elle est banale.", "Soulagement par le paracétamol || Il n'exclut ni ne prouve rien.", "Intensité légère || Elle est rassurante."],
 notions="N08 N09", angle="direct", diff=1, ladder=L("Céphalée.", "Cause secondaire.", "Alerte.", "Lesquels.", "Brutal, fièvre, papille.", "Étau.", "Drapeaux rouges."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Une femme de 30 ans décrit des céphalées récurrentes. Vous hésitez entre migraine et céphalée de tension.", prompt="Quels caractères orientent vers une céphalée de tension ? (3 réponses)",
 items=["*Localisation bilatérale || Elle est typique.", "*Douleur en pression ou en étau || Elle est non pulsatile.", "*Absence d'aggravation par l'activité courante || Elle distingue de la migraine.", "Douleur pulsatile || Elle oriente vers la migraine.", "Nausées || Elles orientent vers la migraine.", "Vomissements || Ils orientent vers la migraine.", "Aura visuelle || Elle oriente vers la migraine.", "Photophobie et phonophobie ensemble || Elles orientent vers la migraine.", "Aggravation en montant les escaliers || Elle oriente vers la migraine.", "Besoin de s'allonger dans le noir || Il oriente vers la migraine.", "Larmoiement homolatéral || Il oriente vers une algie vasculaire.", "Décharges de quelques secondes || Elles orientent vers une névralgie."],
 notions="N04 N10 N05", angle="application", diff=2, ladder=L("Deux céphalées.", "Critères ICHD-3.", "Caractères.", "Distinction.", "Bilatérale, étau, calme.", "Pulsatile.", "Étau sans effort."), sources="[ICHD-3, IHS, 2018]"),
dict(format="A", stem="Un homme de 52 ans souffre depuis des années de céphalées bilatérales en étau. Il prend depuis 1 an du tramadol 20 jours par mois et a mal presque tous les jours.", prompt="Comment conduisez-vous le sevrage ?",
 items=["*Par une diminution progressive du tramadol, avec information et traitement préventif || L'opioïde se sevre lentement.", "Par un arrêt brutal à domicile sans suivi || Il expose au syndrome de sevrage.", "Par un passage à la morphine || Il aggraverait l'abus.", "Par l'ajout d'un triptan || Il ajouterait un abus.", "Par la poursuite du tramadol, la céphalée étant primaire || Il entretient la céphalée."],
 notions="N16 N14", angle="piège", diff=3, ladder=L("Abus d'opioïde.", "Sevrage.", "Tramadol.", "Mode d'arrêt.", "Diminution progressive.", "Arrêt brutal.", "Opioïde = sevrage lent."), sources="[Diener, EAN, 2020]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Céphalée de tension : la reconnaître cliniquement, exclure les drapeaux rouges, traiter l'épisode par antalgique simple, prévenir l'abus médicamenteux et proposer l'amitriptyline et les mesures non médicamenteuses dans la forme chronique",
 notions=[
  dict(titre="Reconnaître", rub=["ana", "def", "pos"], comment="Applique les critères ICHD-3 et distingue de la migraine.",
   tableau=(["Caractère", "Tension", "Migraine"], [
     ["Siège", "Bilatéral", "Souvent unilatéral"],
     ["Qualité", _T("Pression, étau", "Non pulsatile."), "Pulsatile"],
     ["Effort", "Pas d'aggravation", _T("Aggravation", "Monter les escaliers aggrave.")],
     ["Signes associés", "Aucune nausée", "Nausée, photophobie et phonophobie"]]),
   points=["Peu fréquente < 1 j/mois ; fréquente 1-14 ; chronique ≥ 15 j/mois > 3 mois."], sources=["[ICHD-3, IHS, 2018]"]),
  dict(titre="Exclure une cause secondaire", rub=["red", "gold", "exa"], comment="Cherche les drapeaux rouges ; sans eux, n'image pas.",
   tableau=(["Drapeau rouge", "Cause à évoquer", "Examen"], [
     ["Début brutal", "Hémorragie méningée", "Scanner cérébral urgent"],
     ["Fièvre, raideur", "Méningite", "Ponction lombaire"],
     ["Œdème papillaire", "Hypertension intracrânienne", "Imagerie cérébrale"],
     ["Nouvelle après 50 ans", _T("Artérite à cellules géantes", "Claudication de la mâchoire."), "VS, CRP"]]),
   points=["Examen normal et sensibilité péricrânienne : céphalée primaire."], sources=["[avis d'expert]"]),
  dict(titre="Traiter", rub=["acu", "chr"], comment="Traite l'épisode simplement et prévient la forme chronique.",
   arbre=[("t1", None, "Céphalée de tension", "La fréquence guide le traitement."),
          ("t2", "t1", "Épisode", "Antalgique simple ou AINS ; ni triptan, ni opioïde, ni myorelaxant.", "ct"),
          ("t3", "t1", "Forme chronique", "Amitriptyline, puis mirtazapine ou venlafaxine.", "ct"),
          ("t4", "t1", "Toutes formes", "Information, biofeedback, TCC, relaxation.", "ct"),
          ("t5", "t3", "Abus médicamenteux", "Information puis sevrage.", "ct")],
   points=["Associations caféinées : second choix."], sources=["[Bendtsen, EFNS, 2010]"]),
  dict(titre="Abus médicamenteux", rub=["hos", "sur", "fol"], comment="Compte les jours de prise pour prévenir la céphalée par abus.",
   tableau=(["Médicament", "Seuil d'abus", "Sevrage"], [
     ["Antalgiques simples", "≥ 15 j/mois > 3 mois", _T("Arrêt brutal possible", "Le sevrage est bien toléré.")],
     ["Triptans, associations", "≥ 10 j/mois > 3 mois", "Arrêt brutal possible"],
     ["Opioïdes, tranquillisants", "≥ 10 j/mois > 3 mois", _T("Diminution progressive", "L'arrêt brutal expose au sevrage.")]]),
   points=["Agenda des céphalées et des prises."], sources=["[ICHD-3, IHS, 2018]", "[Diener, EAN, 2020]"]),
 ],
 ssp=dict(code="S7.6", nom="Céphalées", officiel=True, algorithme=[
  ("n1", None, "Céphalée", "Les drapeaux rouges se cherchent d'abord."),
  ("n2", "n1", "Drapeau rouge", "Cause secondaire : explorations ciblées.", None, "c1"),
  ("n3", "n1", "Bilatérale, en étau, sans nausée", "Céphalée de tension.", "ct", "c1"),
  ("n4", "n1", "Unilatérale, pulsatile, nauséeuse", "Migraine (même SSP).", None, "c1"),
  ("n5", "n3", "Épisodique", "Antalgique simple ou AINS.", "ct", "c2"),
  ("n6", "n3", "Chronique", "Amitriptyline et mesures non médicamenteuses.", "ct", "c2"),
  ("n7", "n6", "Antalgiques au-delà du seuil", "Abus médicamenteux : sevrage.", "ct", "c3")]),
 pec=[
  dict(cle="ct", titre="Céphalée de tension",
   but=["Soulager les épisodes sans créer d'abus médicamenteux.", "Réduire la fréquence de la forme chronique."],
   moyens=dict(accueil=["Exclure les drapeaux rouges.", "Expliquer le caractère bénin.", "Proposer un agenda des céphalées."],
    pharma=[("Ibuprofène (AINS)", "200 à 800 mg par prise ; à vérifier dans l'AIPS.", "Il soulage l'épisode avec un bon niveau de preuve.", "[Bendtsen, EFNS, 2010]"),
            ("Paracétamol (antalgique)", "1000 mg par prise ; à vérifier dans l'AIPS.", "Il soulage l'épisode, avec moins d'effets digestifs.", "[Bendtsen, EFNS, 2010]"),
            ("Amitriptyline (antidépresseur tricyclique)", "Faible dose le soir, titrée ; à vérifier dans l'AIPS.", "Elle est le préventif de premier choix de la forme chronique.", "[Bendtsen, EFNS, 2010]")],
    nonpharma=[("éducation thérapeutique", "Expliquer les seuils d'abus et tenir un agenda des prises.", "Le patient informé évite la céphalée par abus médicamenteux."),
               ("psychothérapie", "Biofeedback EMG, TCC ou relaxation.", "Elles réduisent la fréquence des céphalées."),
               ("rééducation", "Physiothérapie si composante cervicale.", "Elle peut aider malgré des preuves limitées."),
               ("hygiène de vie", "Sommeil régulier, activité physique, gestion du stress.", "Ils limitent les facteurs de chronicisation.")],
    transversal=[("Psychiatrie et psychologie", "Elles traitent anxiété, dépression et insomnie associées.")]),
   urgence=None,
   horsUrgence=(["Agenda des céphalées.", "Limitation des jours d'antalgiques."],
            [("d'abord", "médecin de famille", "Pose le diagnostic et exclut les drapeaux rouges."),
             ("ensuite", "patient·e", "Tient l'agenda et limite les prises."),
             ("puis", "psychologue psychothérapeute", "Propose TCC ou relaxation sur prescription."),
             ("puis", "neurologue", "Prend en charge la forme chronique réfractaire ou l'abus.")]),
   pronostic="La forme épisodique reste en général bénigne ; la forme chronique répond souvent partiellement aux préventifs.",
   suivi=[("Jours de céphalée", "À chaque consultation", "Baisse de la fréquence"), ("Jours d'antalgiques", "À chaque consultation", "Sous les seuils d'abus"), ("Tolérance de l'amitriptyline", "Après chaque palier", "Pas de somnolence gênante")],
   sortie="Le suivi reste ambulatoire chez le médecin de famille.",
   prevention=["Elle limite les jours d'antalgiques.", "Elle traite anxiété et troubles du sommeil.", "Elle encourage l'activité physique régulière."]),
 ])
AVERIFIER = ["Doses d'ibuprofène, de paracétamol et d'amitriptyline à vérifier dans l'AIPS (doses EFNS 2010)."]
