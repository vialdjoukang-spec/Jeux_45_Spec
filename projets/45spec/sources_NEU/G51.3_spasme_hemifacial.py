ID = "G51.3__S1_4-E07"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[Abbruzzese, Handb Clin Neurol 2011]|Le spasme hémifacial est un mouvement anormal d'origine périphérique : des contractions cloniques ou toniques involontaires, indolores, des muscles d'un hémiface innervés par le nerf facial.",  # N01
"ana|symptôme|2||[Abbruzzese, Handb Clin Neurol 2011 ; avis d'expert]|Les contractions débutent le plus souvent à l'orbiculaire de l'œil puis gagnent la joue et la commissure ; dans les formes secondaires, le haut et le bas du visage se prennent d'emblée.",  # N02
"bas|mécanisme|2||[Abbruzzese, Handb Clin Neurol 2011]|Une artère comprime le nerf facial à sa zone d'émergence du tronc cérébral ; la démyélinisation locale permet une transmission éphaptique qui génère les décharges.",  # N03
"epi|terrain particulier|1||[avis d'expert]|Le trouble touche surtout l'adulte d'âge moyen et un peu plus souvent la femme.",  # N04
"exa|signe|2||[Pawlowski, Mov Disord 2013]|Le signe de Babinski-2 associe fermeture de l'œil et élévation du sourcil homolatéral ; il était présent chez 86 % des patients d'une série et absent du blépharospasme.",  # N05
"pos|diagnostic différentiel|3||[Abbruzzese, Handb Clin Neurol 2011 ; avis d'expert]|Le blépharospasme, bilatéral et dystonique, et les myokymies faciales, ondulantes et continues, se distinguent du spasme hémifacial unilatéral.",  # N06
"pos|diagnostic différentiel|1||[avis d'expert]|Les tics, suppressibles et précédés d'une envie, et les crises focales motrices se distinguent par leur clinique.",  # N07
"pos|signe|1||[avis d'expert]|Les contractions persistent pendant le sommeil, à la différence du blépharospasme.",  # N08
"gold|examen|3||[Matmusaev, Asian J Neurosurg 2020 ; avis d'expert]|L'IRM cérébrale avec séquences fines de l'angle pontocérébelleux montre le conflit neurovasculaire et exclut une lésion.",  # N09
"red|piège|2||[Abbruzzese, Handb Clin Neurol 2011 ; avis d'expert]|Une forme secondaire se cherche (tumeur de l'angle, lésion du tronc, séquelle de paralysie faciale), surtout devant une surdité, une paralysie faciale ou l'atteinte d'autres nerfs crâniens.",  # N10
"alt|examen|1||[avis d'expert]|L'électromyogramme peut montrer des décharges synchrones et une réponse de diffusion latérale, utile dans les cas douteux.",  # N11
"chr|molécule|2||[Abbruzzese, Handb Clin Neurol 2011]|L'injection locale de toxine botulique est le traitement symptomatique préféré ; son efficacité et sa tolérance au long cours sont documentées.",  # N12
"chr|décision|2||[Abbruzzese, Handb Clin Neurol 2011 ; Li, Neurosurg Rev 2022]|La décompression vasculaire microchirurgicale traite la cause et améliore nettement la majorité des patients, mais récidives et complications ne sont pas rares.",  # N13
"hos|complication|2||[Bartindale, Otolaryngol Head Neck Surg 2018]|Une hypoacousie a été rapportée après 8,25 % des décompressions pour spasme hémifacial, et après 13,39 % quand l'audiogramme était systématique.",  # N14
"chr|piège|1||[Abbruzzese, Handb Clin Neurol 2011]|Les anticonvulsivants et les médicaments GABAergiques sont généralement inefficaces.",  # N15
"hos|complication|1||[Li, Neurosurg Rev 2022]|Une paralysie faciale peut suivre la décompression ; la plupart des complications sont transitoires.",  # N16
"acu|décision|1||[avis d'expert]|Le trouble n'est pas une urgence : la prise en charge est ambulatoire, sauf signe neurologique associé.",  # N17
"acu|piège|1||[avis d'expert]|Les injections de toxine peuvent causer une ptose ou une faiblesse faciale transitoires.",  # N18
"pro|pronostic|1||[avis d'expert]|Le trouble disparaît rarement de lui-même et tend à progresser lentement.",  # N19
"sur|décision|1||[avis d'expert]|Les injections se répètent selon la durée de l'effet, souvent tous les quelques mois.",  # N20
"fol|décision|1||[avis d'expert]|Le neurologue injecte la toxine ; le neurochirurgien discute la décompression chez le patient qui souhaite un traitement causal.",  # N21
"fol|contexte suisse|1|S|[avis d'expert]|En Suisse, l'indication et le remboursement de la toxine botulique dans le spasme hémifacial se vérifient dans l'AIPS et la Liste des spécialités.",  # N22
"epi|terrain particulier|1||[Li, Neurosurg Rev 2022]|Les compressions par l'artère vertébrale touchent des patients plus âgés, plus souvent du côté gauche, avec plus de complications opératoires.",  # N23
"def|critère|1||[Abbruzzese, Handb Clin Neurol 2011]|La forme primaire relève d'une compression vasculaire ; la forme secondaire, d'une lésion du nerf facial ou du tronc cérébral.",  # N24
"ana|symptôme|1||[avis d'expert]|Le stress et la fatigue aggravent les contractions, qui gênent la vision et la vie sociale.",  # N25
"alt|piège|1||[avis d'expert]|Le scanner ne montre pas le conflit neurovasculaire : l'IRM reste l'examen de choix.",  # N26
]
ANGLES = [
"Unilatéral, débute à l'œil, persiste en dormant.",
"Babinski-2 : œil fermé, sourcil levé.",
"IRM de l'angle pontocérébelleux.",
"Toxine botulique d'abord.",
"Décompression : hypoacousie possible.",
"Surdité ou paralysie : forme secondaire.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une secrétaire de 52 ans, à Sion, a depuis 8 mois des clignements involontaires de l'œil gauche, qui tirent maintenant aussi la commissure labiale gauche. Ils sont indolores et son mari les voit aussi pendant son sommeil.", prompt="Quel diagnostic évoquez-vous en premier ?",
 items=["*Un spasme hémifacial || Contractions unilatérales, débutant à l'œil, persistant en dormant.", "Un blépharospasme || Il est bilatéral et disparaît pendant le sommeil.", "Des myokymies faciales || Elles ondulent sous la peau sans fermer l'œil.", "Un tic moteur || Il est suppressible et précédé d'une envie.", "Une crise focale motrice || Elle est brève et ne dure pas des mois en continu."],
 notions="N01 N02 N08 N06", angle="direct", diff=1, ladder=L("Clignements d'un œil.", "Hyperactivité du VII.", "S'étend à la bouche.", "Unilatéral, en dormant.", "Spasme hémifacial.", "Blépharospasme.", "Un côté, œil puis bouche."), sources="[Abbruzzese, Handb Clin Neurol 2011]"),
dict(format="A", serie=("S1", 2, 4), stem="Pendant une contraction, l'œil gauche se ferme et, en même temps, le sourcil gauche s'élève.", prompt="Que vous apprend ce signe ?",
 items=["*Il s'agit du signe de Babinski-2, qui oriente vers un spasme hémifacial plutôt qu'un blépharospasme || Il est très spécifique.", "Il oriente vers un blépharospasme || Dans le blépharospasme, le sourcil s'abaisse.", "Il signe une paralysie faciale centrale || Il traduit une contraction, pas un déficit.", "Il signe une crise épileptique || Il n'a pas ce sens.", "Il n'a aucune valeur || Il est très spécifique."],
 notions="N05 N06", angle="application", diff=2, ladder=L("Œil fermé, sourcil levé.", "Co-contraction.", "Frontal et orbiculaire.", "Spécificité.", "Babinski-2.", "Blépharospasme.", "Sourcil levé = spasme hémifacial."), sources="[Pawlowski, Mov Disord 2013]"),
dict(format="A", serie=("S1", 3, 4), stem="Vous voulez confirmer la cause.", prompt="Quel examen demandez-vous ?",
 items=["*Une IRM cérébrale avec séquences fines de l'angle pontocérébelleux || Elle montre le conflit et exclut une lésion.", "Un scanner cérébral sans contraste || Il ne montre pas le conflit.", "Un EEG || Le tableau n'est pas épileptique.", "Une ponction lombaire || Rien ne l'indique.", "Aucun examen, car le diagnostic est clinique et la cause toujours bénigne || Une forme secondaire doit être exclue."],
 notions="N09 N10 N26", angle="application", diff=2, ladder=L("Cause.", "Conflit neurovasculaire.", "Angle pontocérébelleux.", "Exclure une lésion.", "IRM ciblée.", "Scanner.", "IRM de l'angle."), sources="[Matmusaev, Asian J Neurosurg 2020]"),
dict(format="A", serie=("S1", 4, 4), stem="L'IRM montre une boucle de l'artère cérébelleuse antéro-inférieure au contact du nerf facial gauche, sans tumeur. La patiente veut un traitement efficace sans opération.", prompt="Que lui proposez-vous ?",
 items=["*Des injections locales de toxine botulique, répétées selon l'effet || C'est le traitement symptomatique préféré.", "De la carbamazépine au long cours || Les anticonvulsivants sont généralement inefficaces.", "Du clonazépam au long cours || Les GABAergiques sont généralement inefficaces.", "Des corticoïdes || Rien ne les justifie.", "Une décompression d'emblée malgré son refus || Elle souhaite éviter la chirurgie."],
 notions="N12 N15 N13 N03", angle="application", diff=2, ladder=L("Conflit confirmé.", "Compression artérielle.", "AICA.", "Pas de chirurgie voulue.", "Toxine botulique.", "Carbamazépine.", "Toxine d'abord."), sources="[Abbruzzese, Handb Clin Neurol 2011]"),
dict(format="A", stem="Un homme de 45 ans a des contractions involontaires de l'hémiface gauche depuis 6 mois, avec une baisse progressive de l'audition gauche et un acouphène gauche.", prompt="Quelle conduite est la plus juste ?",
 items=["*Une IRM rapide de l'angle pontocérébelleux pour chercher une lésion compressive || La surdité associée évoque une forme secondaire.", "Des injections de toxine sans imagerie || Une lésion doit d'abord être exclue.", "Un audiogramme seul, sans imagerie || L'association impose l'IRM.", "Une réassurance sur une forme vasculaire bénigne || La surdité fait chercher une tumeur.", "Un EEG || Rien ne l'oriente."],
 notions="N10 N09", angle="piège", diff=2, ladder=L("Spasme et surdité.", "Lésion de l'angle.", "Acouphène.", "Signe associé.", "IRM rapide.", "Toxine d'emblée.", "Signe associé = imagerie."), sources="[Abbruzzese, Handb Clin Neurol 2011]"),
dict(format="A", stem="Une femme de 60 ans a des fermetures forcées des deux yeux, aggravées par la lumière vive et disparaissant pendant le sommeil. Le sourcil s'abaisse pendant les contractions.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Un blépharospasme || Il est bilatéral, dystonique et disparaît pendant le sommeil.", "Un spasme hémifacial bilatéral || Il est presque toujours unilatéral et persiste en dormant.", "Des myokymies faciales || Elles ne ferment pas les yeux.", "Une myasthénie || Elle donne une ptose, pas des fermetures forcées.", "Une paralysie faciale bilatérale || Elle empêche la fermeture."],
 notions="N06 N08 N05", angle="piège", diff=2, ladder=L("Fermetures des deux yeux.", "Dystonie focale.", "Bilatéral.", "Disparaît en dormant.", "Blépharospasme.", "Spasme hémifacial.", "Deux yeux = blépharospasme."), sources="[Pawlowski, Mov Disord 2013]"),
dict(format="A", stem="Un homme de 38 ans décrit de fines ondulations vermiculaires continues sous la peau de la joue droite, sans fermeture de l'œil.", prompt="Quel diagnostic évoquez-vous ?",
 items=["*Des myokymies faciales || Leurs ondulations continues, sans contraction en masse, les caractérisent.", "Un spasme hémifacial || Il ferme l'œil et tire la commissure.", "Un blépharospasme || Il est bilatéral et ferme les yeux.", "Un tic moteur || Il est bref et suppressible.", "Des fasciculations de sclérose latérale amyotrophique certaines || Le tableau est localisé à la face."],
 notions="N06 N07", angle="piège", diff=2, ladder=L("Ondulations de la joue.", "Décharges continues.", "Vermiculaires.", "Pas de fermeture de l'œil.", "Myokymies.", "Spasme hémifacial.", "Ondule = myokymie."), sources="[avis d'expert]"),
dict(format="A", stem="Une patiente avec des contractions involontaires de l'hémiface droit demande de la carbamazépine, efficace chez sa sœur pour une névralgie du trijumeau.", prompt="Que lui répondez-vous ?",
 items=["*La carbamazépine est généralement peu efficace ici ; la toxine botulique est le traitement symptomatique préféré || Le bénéfice des anticonvulsivants est faible.", "La carbamazépine est le traitement de référence || Elle est généralement inefficace.", "La carbamazépine guérit le conflit vasculaire || Elle ne traite pas la cause.", "Seul le clonazépam est efficace || Les GABAergiques sont aussi peu efficaces.", "Aucun traitement n'existe || La toxine et la décompression existent."],
 notions="N15 N12", angle="piège", diff=2, ladder=L("Demande de carbamazépine.", "Mouvement anormal, pas douleur.", "Névralgie chez la sœur.", "Efficacité.", "Toxine botulique.", "Carbamazépine.", "Spasme ≠ névralgie."), sources="[Abbruzzese, Handb Clin Neurol 2011]"),
dict(format="A", stem="Un homme de 48 ans en bonne santé reçoit des injections pour des contractions de l'hémiface gauche depuis 7 ans ; l'IRM montre un conflit vasculaire. Il souhaite un traitement définitif.", prompt="Quelle option lui proposez-vous ?",
 items=["*Un avis neurochirurgical pour une décompression vasculaire microchirurgicale, en l'informant du risque d'hypoacousie || C'est le seul traitement causal.", "Une augmentation indéfinie des doses de toxine || Elle ne traite pas la cause.", "La carbamazépine || Elle est généralement inefficace.", "Une section du nerf facial || Elle cause une paralysie faciale.", "Une radiothérapie || Elle n'est pas un traitement validé."],
 notions="N13 N14 N21", angle="application", diff=2, ladder=L("Souhait définitif.", "Décompression.", "Bonne santé.", "Rapport bénéfice-risque.", "Neurochirurgie.", "Toxine indéfinie.", "Causal = décompression."), sources="[Li, Neurosurg Rev 2022]"),
dict(masque=False, sit="monographique", format="A", stem="Avant une décompression vasculaire pour un spasme de l'hémiface, le patient demande quelle complication il doit surtout connaître.", prompt="Quelle complication lui expliquez-vous ?",
 items=["*Une hypoacousie homolatérale || Elle a été rapportée dans environ 8 à 13 % des cas selon la méthode de mesure.", "Une cécité || Elle n'est pas une complication attendue.", "Une hémiplégie systématique || Elle n'est pas attendue.", "Une épilepsie chronique fréquente || Elle n'est pas une complication attendue.", "Aucune complication possible || Hypoacousie et paralysie faciale sont possibles."],
 notions="N14 N16", angle="direct", diff=2, ladder=L("Information préopératoire.", "Proximité du VIII.", "Angle pontocérébelleux.", "Risque principal.", "Hypoacousie.", "Aucun risque.", "Décompression = audition."), sources="[Bartindale, Otolaryngol Head Neck Surg 2018]"),
dict(masque=False, sit="monographique", format="A", stem="Dix jours après une injection de toxine botulique pour un spasme de l'hémiface droit, la patiente a une paupière droite tombante.", prompt="Quelle explication est la plus probable ?",
 items=["*Une ptose transitoire liée à la diffusion de la toxine || C'est un effet indésirable connu et réversible.", "Un AVC du tronc cérébral || Le contexte l'explique mieux.", "Une myasthénie révélée certaine || Le lien temporel avec l'injection l'explique mieux.", "Une paralysie du III complète || La ptose isolée après injection l'explique mieux.", "Un échec définitif du traitement || L'effet est transitoire."],
 notions="N18 N20", angle="application", diff=2, ladder=L("Ptose après injection.", "Diffusion de la toxine.", "Dix jours.", "Lien temporel.", "Effet transitoire.", "AVC.", "Ptose post-toxine = transitoire."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 55 ans a eu une paralysie faciale gauche périphérique il y a 2 ans. Son œil gauche se ferme maintenant quand elle sourit, et le haut et le bas du visage se contractent ensemble.", prompt="Quelle interprétation est la plus juste ?",
 items=["*Une forme secondaire post-paralytique, avec syncinésies par régénération aberrante || Le haut et le bas du visage se prennent ensemble.", "Un spasme hémifacial primaire par conflit vasculaire certain || L'antécédent oriente vers une forme secondaire.", "Un blépharospasme || Il est bilatéral.", "Une récidive aiguë de paralysie faciale || Il s'agit de contractions, pas d'un déficit.", "Un tic || Il n'est pas lié à un mouvement volontaire."],
 notions="N24 N02 N10 N01", angle="piège", diff=3, ladder=L("Contractions après paralysie.", "Régénération aberrante.", "Œil fermé au sourire.", "Haut et bas ensemble.", "Forme secondaire.", "Forme primaire.", "Antécédent de paralysie = secondaire."), sources="[Abbruzzese, Handb Clin Neurol 2011]"),
dict(masque=False, sit="monographique", format="A", stem="Un étudiant révise la physiopathologie du spasme hémifacial primaire.", prompt="Quel mécanisme est retenu ?",
 items=["*Une transmission éphaptique liée à la démyélinisation du nerf facial comprimé à sa zone d'émergence || C'est l'hypothèse nerveuse principale.", "Une décharge du cortex moteur || Le trouble est périphérique.", "Une dystonie des noyaux gris centraux || C'est le mécanisme du blépharospasme.", "Une inflammation virale du nerf facial || Elle donne une paralysie.", "Une atteinte de la jonction neuromusculaire || Elle donne une faiblesse."],
 notions="N03 N01", angle="direct", diff=2, ladder=L("Physiopathologie.", "Éphapse.", "Zone d'émergence.", "Périphérique.", "Compression vasculaire.", "Cortex.", "Compression → démyélinisation → éphapse."), sources="[Abbruzzese, Handb Clin Neurol 2011]"),
dict(format="A", stem="Un patient avec des contractions unilatérales de la face a eu un scanner cérébral normal aux urgences.", prompt="Quelle est l'étape suivante ?",
 items=["*Une IRM avec séquences fines de l'angle pontocérébelleux || Le scanner ne montre pas le conflit neurovasculaire.", "Aucun examen, le scanner suffit || Il ne voit pas le conflit et voit mal l'angle.", "Une angiographie conventionnelle d'emblée || Elle est invasive et non nécessaire.", "Une ponction lombaire || Rien ne l'indique.", "Un EEG || Rien ne l'indique."],
 notions="N26 N09", angle="piège", diff=2, ladder=L("Scanner normal.", "Conflit invisible au scanner.", "Angle.", "Limite du scanner.", "IRM ciblée.", "Scanner suffisant.", "Conflit = IRM."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez le spasme hémifacial primaire.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une artère comprime le nerf facial à sa sortie du tronc cérébral. || C'est la cause habituelle.", "V: Les compressions par l'artère vertébrale touchent des patients plus âgés. || Elles prédominent aussi à gauche.", "F: Les contractions sont douloureuses. || Elles sont indolores.", "F: Les contractions disparaissent pendant le sommeil. || Elles persistent."],
 notions="N03 N23 N01 N08", angle="direct", diff=2, ladder=L("Révision.", "Compression.", "Indolore.", "Persiste en dormant.", "Connaître.", "Disparaît en dormant.", "Artère, nerf, éphapse."), sources="[Li, Neurosurg Rev 2022]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un patient discute de la toxine botulique pour son spasme hémifacial.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Elle est le traitement symptomatique préféré. || Son efficacité au long cours est documentée.", "V: Les injections se répètent selon la durée de l'effet. || L'effet est temporaire.", "F: Elle guérit définitivement le trouble. || Elle est symptomatique.", "F: Le trouble disparaît en général spontanément, ce qui rend les injections inutiles. || Il régresse rarement seul."],
 notions="N12 N20 N19 N22", angle="direct", diff=1, ladder=L("Toxine.", "Blocage de l'acétylcholine.", "Injections.", "Temporaire.", "Répéter.", "Guérison.", "Symptomatique et répétée."), sources="[Abbruzzese, Handb Clin Neurol 2011]"),
dict(format="Kprim", stem="Un neurochirurgien informe un patient candidat à une décompression vasculaire.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La décompression est le seul traitement qui agit sur la cause. || Elle libère le nerf.", "V: Une hypoacousie peut suivre l'intervention. || Elle est une complication reconnue.", "F: L'intervention est sans aucun risque. || Hypoacousie et paralysie faciale sont possibles.", "F: Elle peut se faire sans IRM préalable. || L'IRM montre le conflit et exclut une lésion."],
 notions="N13 N14 N16 N09", angle="piège", diff=2, ladder=L("Information.", "Décompression.", "Risques.", "Pièges.", "Informer.", "Sans risque.", "Causal mais risqué."), sources="[Bartindale, Otolaryngol Head Neck Surg 2018]"),
dict(format="Kprim", stem="Des internes discutent des mouvements anormaux de la face.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le blépharospasme est en général bilatéral. || C'est une dystonie focale.", "V: Un tic peut être retenu volontairement un moment. || Il est suppressible.", "F: Le signe de Babinski-2 est typique du blépharospasme. || Il oriente vers le spasme hémifacial.", "F: Les myokymies ferment l'œil et tirent la commissure. || Elles ondulent sans contraction en masse."],
 notions="N06 N07 N05", angle="direct", diff=2, ladder=L("Mouvements de la face.", "Dystonie, tic, éphapse.", "Bilatéral ou non.", "Signes distinctifs.", "Classer.", "Babinski-2.", "Un côté, deux côtés, ondulation."), sources="[Pawlowski, Mov Disord 2013]"),
dict(format="MenuLong", stem="Une femme de 50 ans a des contractions involontaires de l'hémiface droit.", prompt="Choisissez les TROIS éléments qui doivent faire chercher une forme secondaire.",
 items=["*Hypoacousie homolatérale || Elle évoque une lésion de l'angle.", "*Paralysie faciale associée || Elle évoque une lésion du nerf.", "*Hypoesthésie de l'hémiface || Elle évoque l'atteinte d'un autre nerf crânien.", "Début à l'orbiculaire de l'œil || C'est typique de la forme primaire.", "Contractions indolores || C'est typique.", "Persistance pendant le sommeil || C'est typique.", "Signe de Babinski-2 || Il est typique.", "Aggravation par le stress || Elle est banale.", "Âge de 50 ans || C'est l'âge typique.", "Atteinte unilatérale || Elle est typique.", "Évolution lente sur des années || Elle est typique.", "Sexe féminin || Il est fréquent."],
 notions="N10 N02 N25", angle="application", diff=2, ladder=L("Spasme hémifacial.", "Forme secondaire.", "Signes associés.", "Drapeaux.", "Surdité, paralysie, autre nerf.", "Début à l'œil.", "Signe associé = cause à chercher."), sources="[Abbruzzese, Handb Clin Neurol 2011]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Vous révisez les traitements du spasme hémifacial primaire.", prompt="Choisissez les DEUX traitements dont l'efficacité est la mieux établie.",
 items=["*Toxine botulique en injections locales || Elle est le traitement symptomatique préféré.", "*Décompression vasculaire microchirurgicale || Elle traite la cause.", "Carbamazépine || Elle est généralement inefficace.", "Clonazépam || Il est généralement inefficace.", "Baclofène || Il est généralement inefficace.", "Gabapentine || Elle n'a pas fait ses preuves.", "Corticoïdes || Ils ne sont pas indiqués.", "Aciclovir || Il n'est pas indiqué.", "Propranolol || Il n'est pas indiqué.", "Kinésithérapie seule || Elle ne suffit pas.", "Acupuncture || Elle n'a pas fait ses preuves.", "Halopéridol || Il n'est pas indiqué."],
 notions="N12 N13 N15", angle="direct", diff=1, ladder=L("Traitements.", "Symptôme ou cause.", "Toxine et chirurgie.", "Médicaments oraux.", "Toxine, décompression.", "Carbamazépine.", "Toxine ou chirurgie."), sources="[Abbruzzese, Handb Clin Neurol 2011]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Spasme hémifacial : reconnaître les contractions unilatérales indolores débutant à l'œil, les distinguer du blépharospasme, des myokymies et des tics, montrer le conflit et exclure une lésion par IRM, puis traiter par toxine botulique ou décompression",
 notions=[
  dict(titre="Reconnaître", rub=["def", "ana", "exa", "epi"], comment="Pense au spasme hémifacial devant des contractions d'un seul côté qui débutent à l'œil et persistent en dormant.",
   tableau=(["Élément", "Contenu", "Pourquoi"], [
     ["Topographie", "Un hémiface, débute à l'orbiculaire de l'œil", "Territoire du VII"],
     ["Caractère", "Clonique ou tonique, indolore", _T("Pas une névralgie", "La douleur oriente vers le trijumeau.")],
     ["Sommeil", "Persiste", _T("Discriminant", "Le blépharospasme disparaît en dormant.")],
     ["Signe", "Babinski-2 : œil fermé, sourcil levé", "Très spécifique"]]),
   points=["Le stress et la fatigue l'aggravent."], sources=["[Abbruzzese, Handb Clin Neurol 2011]", "[Pawlowski, Mov Disord 2013]"]),
  dict(titre="Différencier", rub=["pos", "red", "def"], comment="Distingue le spasme hémifacial de ses imitateurs et cherche les signes d'une forme secondaire.",
   tableau=(["Trouble", "Caractère", "Discriminant"], [
     ["Spasme hémifacial", "Unilatéral, œil puis bouche", "Persiste en dormant"],
     ["Blépharospasme", "Bilatéral, dystonique", _T("Disparaît en dormant", "Il relève des noyaux gris centraux.")],
     ["Myokymies", "Ondulations continues", "Pas de contraction en masse"],
     ["Tic", "Bref, suppressible", "Précédé d'une envie"],
     ["Forme secondaire", "Haut et bas d'emblée, signes associés", _T("Surdité, paralysie, autre nerf", "Ils font chercher une lésion.")]]),
   points=["Une séquelle de paralysie faciale donne des syncinésies."], sources=["[Abbruzzese, Handb Clin Neurol 2011]"]),
  dict(titre="Explorer", rub=["gold", "alt", "bas"], comment="Montre le conflit et exclut une lésion par une IRM ciblée.",
   tableau=(["Examen", "Apport", "Pourquoi"], [
     ["IRM de l'angle pontocérébelleux", "Conflit neurovasculaire, lésion", "Examen de choix"],
     ["Scanner", "Insuffisant", _T("Conflit invisible", "Il voit mal l'angle.")],
     ["Électromyogramme", "Décharges synchrones", "Cas douteux"]]),
   points=["La compression par l'artère vertébrale touche des patients plus âgés."], sources=["[Matmusaev, Asian J Neurosurg 2020]", "[Li, Neurosurg Rev 2022]"]),
  dict(titre="Traiter", rub=["chr", "hos", "sur", "fol"], comment="Propose la toxine botulique d'abord et la décompression à qui veut un traitement causal.",
   arbre=[("t1", None, "Spasme hémifacial primaire confirmé", "Le médecin explique les deux options."),
          ("t2", "t1", "Souhait d'un traitement symptomatique", "Toxine botulique répétée.", "hfs"),
          ("t3", "t1", "Souhait d'un traitement causal, bon état général", "Décompression vasculaire.", "hfs"),
          ("t4", "t3", "Information", "Hypoacousie et paralysie faciale possibles.", "hfs"),
          ("t5", "t2", "Ptose après injection", "Effet transitoire.", "hfs")],
   points=["Les anticonvulsivants et les GABAergiques sont généralement inefficaces."], sources=["[Abbruzzese, Handb Clin Neurol 2011]", "[Bartindale, Otolaryngol Head Neck Surg 2018]"]),
 ],
 ssp=dict(code="S1.4", nom="Asymétrie ou déformation du visage", officiel=True, algorithme=[
  ("n1", None, "Mouvements involontaires d'un hémiface", "Le médecin précise topographie, sommeil et signes associés."),
  ("n2", "n1", "Déficit moteur facial sans contractions", "Paralysie faciale : renvoi à la pathologie correspondante.", None, "c2"),
  ("n3", "n1", "Atteinte bilatérale, disparaît en dormant", "Blépharospasme : neurologue.", None, "c2"),
  ("n4", "n1", "Contractions unilatérales, persistant en dormant", "Spasme hémifacial : IRM de l'angle.", None, "c3"),
  ("n5", "n4", "Lésion à l'IRM ou signes associés", "Forme secondaire : traitement de la cause.", None, "c2"),
  ("n6", "n4", "Conflit vasculaire sans lésion", "Toxine botulique ou décompression.", "hfs", "c4")]),
 pec=[
  dict(cle="hfs", titre="Spasme hémifacial primaire",
   but=["Réduire les contractions.", "Préserver la vision et la vie sociale.", "Proposer un traitement causal si souhaité."],
   moyens=dict(accueil=["Décrire topographie et persistance pendant le sommeil.", "Chercher surdité, paralysie faciale et atteinte d'autres nerfs.", "Demander une IRM de l'angle pontocérébelleux."],
    pharma=[("Toxine botulique de type A en injections locales", "Doses et intervalles à vérifier dans l'AIPS.", "Traitement symptomatique préféré.", "[Abbruzzese, Handb Clin Neurol 2011]")],
    nonpharma=[("geste ou chirurgie", "Décompression vasculaire microchirurgicale.", "Elle traite la cause."),
               ("éducation thérapeutique", "Information sur la ptose transitoire et la répétition des injections.", "Elle améliore l'adhésion."),
               ("psychothérapie", "Soutien face à la gêne sociale.", "Le trouble est visible et stigmatisant.")],
    transversal=[("Neurologie", "Elle injecte la toxine et suit le patient."), ("Neurochirurgie", "Elle pose l'indication de décompression.")]),
   urgence=None,
   horsUrgence=(["IRM avant tout traitement.", "Choix partagé entre toxine et chirurgie."],
            [("d'abord", "médecin de famille", "Reconnaît le trouble et adresse au neurologue."),
             ("ensuite", "neurologue", "Confirme le diagnostic et demande l'IRM."),
             ("puis", "neurologue", "Injecte la toxine de façon répétée."),
             ("puis", "neurochirurgien·ne", "Discute la décompression chez le patient demandeur.")]),
   pronostic="Le trouble progresse lentement ; la toxine le contrôle et la décompression améliore la majorité des patients opérés.",
   suivi=[("Effet de la toxine", "À chaque injection", "Contractions réduites"), ("Effets indésirables", "Après chaque injection", "Pas de ptose durable"), ("Audition après décompression", "Postopératoire", "Conservée")],
   sortie="Le patient reste suivi par le neurologue pour les injections ou après la décompression.",
   prevention=["Elle n'a pas de prévention primaire connue.", "Elle repose sur l'exclusion précoce d'une forme secondaire par IRM.", "Elle limite les complications par l'information et une technique experte."]),
 ])
AVERIFIER = ["Doses et remboursement de la toxine botulique dans le spasme hémifacial en Suisse à vérifier dans l'AIPS et la Liste des spécialités.", "Le Babinski-2 (86 %, spécificité 100 %) vient d'une petite série de 35 patients (Pawlowski 2013).", "Les taux d'hypoacousie postopératoire dépendent fortement de la méthode de mesure (Bartindale 2018)."]
