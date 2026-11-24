ID = "G95.2__O5_3-E12"
PLAN = "monographique"
NOTIONS = [
"def|critère|1||[NICE NG234, 2023]|La compression médullaire aiguë est une urgence neurologique dans laquelle une lésion du canal rachidien écrase la moelle et menace la marche et les sphincters.",  # N01
"epi|terrain particulier|2||[NICE NG234, 2023]|Chez le patient cancéreux, les métastases vertébrales des cancers du sein, du poumon, de la prostate, du rein et le myélome sont les causes principales de compression.",  # N02
"epi|terrain particulier|2||[Darouiche, NEJM, 2006]|L'abcès épidural, surtout à Staphylococcus aureus, survient chez le diabétique, l'usager de drogues IV ou après un geste rachidien.",  # N03
"epi|terrain particulier|1||[avis d'expert]|L'hématome épidural survient surtout sous anticoagulant ou après une ponction ou une péridurale.",  # N04
"bas|mécanisme|1||[avis d'expert]|La compression provoque ischémie et œdème médullaires, et le déficit devient irréversible si la décompression tarde.",  # N05
"ana|symptôme|3||[NICE NG234, 2023]|Une douleur rachidienne nouvelle, nocturne, aggravée en décubitus ou à la toux, chez un patient cancéreux, précède souvent le déficit de plusieurs semaines.",  # N06
"ana|symptôme|1||[avis d'expert]|Une douleur radiculaire en ceinture thoracique peut révéler une compression thoracique.",  # N07
"exa|signe|2||[avis d'expert]|L'examen trouve une faiblesse des membres inférieurs, un niveau sensitif sur le tronc et, à distance du choc spinal, des réflexes vifs avec signe de Babinski.",  # N08
"exa|piège|1||[avis d'expert]|À la phase aiguë, le choc spinal donne une paraplégie flasque aréflexique qui peut faire croire à une atteinte périphérique.",  # N09
"red|signe|2||[NICE NG234, 2023]|Les troubles sphinctériens (rétention, incontinence) sont tardifs et signent une compression avancée.",  # N10
"red|signe|1||[avis d'expert]|Une fièvre avec douleur rachidienne intense et déficit évoque un abcès épidural.",  # N11
"gold|examen|3||[NICE NG234, 2023]|L'IRM de tout le rachis se fait en urgence, car plusieurs niveaux peuvent être atteints.",  # N12
"alt|examen|1||[NICE NG234, 2023]|En cas de contre-indication à l'IRM, un CT ou un myéloscanner explore le canal rachidien.",  # N13
"alt|examen|1||[avis d'expert]|Les hémocultures et la CRP guident le diagnostic d'abcès, et la biopsie identifie un cancer inconnu.",  # N14
"pos|diagnostic différentiel|2||[avis d'expert]|Le syndrome de la queue de cheval associe anesthésie en selle, rétention urinaire et déficit périphérique des membres inférieurs, sans niveau sensitif thoracique.",  # N15
"pos|diagnostic différentiel|1||[avis d'expert]|Une polyradiculonévrite aiguë donne une faiblesse ascendante aréflexique sans niveau sensitif ni troubles sphinctériens précoces.",  # N16
"pos|diagnostic différentiel|1||[avis d'expert]|Une myélite transverse donne un tableau médullaire sans compression à l'IRM.",  # N17
"acu|posologie|3|S|[NICE NG234, 2023 ; AIPS Swissmedic]|La compression médullaire métastatique reçoit sans délai de la dexaméthasone, par exemple 16 mg/j, avec un inhibiteur de la pompe à protons, posologie à vérifier dans l'AIPS.",  # N18
"acu|décision|2||[Patchell, Lancet, 2005]|Chez un patient sélectionné, la chirurgie de décompression suivie de radiothérapie préserve mieux la marche que la radiothérapie seule.",  # N19
"acu|décision|1||[avis d'expert]|Les tumeurs radiosensibles comme le lymphome et le myélome se traitent souvent par radiothérapie sans chirurgie.",  # N20
"acu|décision|2||[Darouiche, NEJM, 2006]|L'abcès épidural se traite par antibiothérapie couvrant le staphylocoque doré et, en cas de déficit, par drainage chirurgical urgent.",  # N21
"acu|décision|1||[avis d'expert]|L'hématome épidural impose la neutralisation de l'anticoagulation et une évacuation chirurgicale urgente.",  # N22
"chr|décision|1||[avis d'expert]|La radiothérapie de la lésion métastatique se planifie avec l'oncologue selon le pronostic et la stabilité du rachis.",  # N23
"hos|complication|1||[avis d'expert]|La rétention urinaire impose un sondage, et l'immobilisation impose thromboprophylaxie et prévention des escarres.",  # N24
"hos|complication|1||[avis d'expert]|La constipation neurogène et la douleur nécessitent un traitement systématique.",  # N25
"pro|pronostic|3||[NICE NG234, 2023]|La capacité de marcher au moment du diagnostic est le meilleur facteur prédictif de la marche après traitement.",  # N26
"sur|décision|1||[avis d'expert]|Le suivi surveille la force, la sensibilité, les sphincters et la stabilité du rachis.",  # N27
"fol|contexte suisse|1|S|[avis d'expert]|La réadaptation se fait dans un centre spécialisé, par exemple le Centre suisse des paraplégiques, et le réseau palliatif s'implique selon le pronostic.",  # N28
"fol|décision|1||[NICE NG234, 2023]|Le patient cancéreux à risque reçoit une information écrite sur les symptômes d'alerte à signaler en urgence.",  # N29
]
ANGLES = [
"La douleur précède le déficit de plusieurs semaines.",
"L'IRM explore tout le rachis.",
"Les troubles sphinctériens sont tardifs.",
"Le choc spinal mime une atteinte périphérique.",
"La marche au diagnostic prédit la marche après traitement.",
"La dexaméthasone débute avant l'IRM si le doute est fort.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une femme de 63 ans, traitée il y a 4 ans pour un cancer du sein, consulte son médecin de famille à Sion pour une douleur dorsale apparue il y a 3 semaines. La douleur la réveille la nuit et augmente quand elle est couchée. L'examen neurologique est normal.", prompt="Quelle est la conduite la plus adaptée ?",
 items=["*Demander une IRM rachidienne en urgence || Une douleur nocturne nouvelle chez une patiente cancéreuse évoque des métastases rachidiennes.", "Prescrire des AINS et revoir dans 6 semaines || Le délai expose au déficit.", "Prescrire de la physiothérapie || Elle méconnaît une cause grave.", "Demander une radiographie standard seule || Elle est peu sensible.", "Rassurer, l'examen étant normal || Le déficit apparaît plus tard."],
 notions="N06 N02 N12", angle="application", diff=2, ladder=L("Douleur dorsale nouvelle.", "Métastase vertébrale.", "Douleur nocturne, cancer.", "Drapeaux rouges.", "IRM urgente.", "Lombalgie banale.", "Cancer + douleur : IRM."), sources="[NICE NG234, 2023]"),
dict(format="A", serie=("S1", 2, 4), stem="Avant l'IRM, cette femme se plaint de jambes lourdes depuis le matin. Vous trouvez une force à M4 aux membres inférieurs et une hypoesthésie remontant jusqu'à l'ombilic.", prompt="Quelle mesure prenez-vous immédiatement ?",
 items=["*Débuter la dexaméthasone avec un IPP et obtenir l'IRM de tout le rachis dans l'immédiat || La compression médullaire s'installe.", "Attendre l'IRM programmée la semaine prochaine || Le déficit progresse vite.", "Faire une ponction lombaire || Elle peut aggraver une compression.", "Prescrire un antalgique et revoir le lendemain || Le délai menace la marche.", "Demander une IRM lombaire seule || Le niveau est thoracique et d'autres niveaux sont possibles."],
 notions="N18 N12 N08 N05", angle="application", diff=3, ladder=L("Déficit débutant.", "Ischémie médullaire.", "Niveau sensitif ombilical.", "Urgence.", "Dexaméthasone et IRM.", "Attendre.", "Déficit : corticoïdes et IRM."), sources="[NICE NG234, 2023]"),
dict(format="A", serie=("S1", 3, 4), stem="L'IRM de cette femme montre une métastase de T10 qui comprime la moelle, et deux autres métastases sans compression. Elle marche encore avec aide. Son état général est bon et le cancer est contrôlé ailleurs.", prompt="Quelle stratégie est la plus adaptée ?",
 items=["*Une décompression chirurgicale suivie de radiothérapie, discutée en urgence avec neurochirurgien et oncologue || Chez le patient sélectionné, elle préserve mieux la marche.", "La radiothérapie seule dans un mois || Le délai menace la marche.", "La chimiothérapie seule || Elle n'agit pas assez vite.", "Les soins palliatifs exclusifs || Son état et son pronostic justifient un traitement actif.", "La surveillance sous corticoïdes seuls || Ils ne suffisent pas."],
 notions="N19 N23 N26", angle="application", diff=3, ladder=L("Compression confirmée.", "Décompression urgente.", "Bon état, maladie contrôlée.", "Sélection chirurgicale.", "Chirurgie puis radiothérapie.", "Radiothérapie seule tardive.", "Patchell."), sources="[Patchell, Lancet, 2005]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="En postopératoire, cette femme a une rétention urinaire et reste alitée quelques jours.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un sondage urinaire est nécessaire. || La vessie neurogène retient l'urine.", "V: Une thromboprophylaxie est indiquée. || L'immobilité et le cancer favorisent la thrombose.", "V: Sa capacité à marcher avant le traitement prédit sa marche après. || C'est le meilleur facteur pronostique.", "F: La prévention des escarres est inutile en quelques jours. || Elles se constituent en quelques heures."],
 notions="N24 N26 N25", angle="direct", diff=2, ladder=L("Postopératoire.", "Vessie neurogène, immobilité.", "Rétention, alitement.", "Complications.", "Sonde, HBPM, escarres.", "Négliger la peau.", "Prévenir les complications."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 54 ans, diabétique, se présente à Lausanne avec une fièvre à 39 °C, une douleur dorsale intense depuis 5 jours et une faiblesse des jambes depuis la veille. Il a reçu une infiltration rachidienne il y a 3 semaines.", prompt="Quel diagnostic évoquez-vous en premier ?",
 items=["*Un abcès épidural || Fièvre, douleur rachidienne et déficit après un geste rachidien chez un diabétique.", "Une lombalgie commune avec grippe || Le déficit est un drapeau rouge.", "Une polyradiculonévrite aiguë || La fièvre et la douleur rachidienne focale orientent ailleurs.", "Une hernie discale simple || La fièvre ne l'évoque pas.", "Une sclérose en plaques || Le contexte infectieux ne l'évoque pas."],
 notions="N03 N11 N21", angle="application", diff=2, ladder=L("Fièvre et douleur dorsale.", "Infection épidurale.", "Déficit, geste récent.", "Abcès versus lombalgie.", "IRM, hémocultures, chirurgie.", "Banaliser.", "Fièvre + dos + déficit : abcès."), sources="[Darouiche, NEJM, 2006]"),
dict(masque=False, sit="monographique", format="A", stem="Chez un homme de 54 ans, l'IRM confirme un abcès épidural thoracique avec compression médullaire et paraparésie.", prompt="Quel traitement est le plus adapté ?",
 items=["*Hémocultures, antibiothérapie couvrant le staphylocoque doré et drainage chirurgical urgent || Le déficit impose la décompression.", "Antibiothérapie orale seule || Elle est insuffisante.", "Corticoïdes à haute dose seuls || Ils ne traitent pas l'infection.", "Radiothérapie || Elle n'a pas sa place.", "Surveillance sans antibiotique jusqu'aux résultats || Le retard aggrave le pronostic."],
 notions="N21 N14 N05 N03", angle="direct", diff=2, ladder=L("Abcès compressif.", "Pus et ischémie.", "Paraparésie.", "Décompression.", "Drainage et antibiotiques.", "Antibiotique seul.", "Déficit : opérer."), sources="[Darouiche, NEJM, 2006]"),
dict(format="A", stem="Un homme de 78 ans sous apixaban a reçu une rachianesthésie pour une prothèse de genou à Bâle. Six heures plus tard, il ne sent plus ses jambes et ne peut les bouger, alors que l'effet de l'anesthésie devrait être levé.", prompt="Quelle cause évoquez-vous en premier ?",
 items=["*Un hématome épidural compressif || Anticoagulant et geste rachidien récent.", "Une prolongation banale de la rachianesthésie || Le délai dépasse l'effet attendu.", "Un AVC hémisphérique || L'atteinte est bilatérale aux membres inférieurs.", "Un syndrome de Guillain-Barré || Le délai et le contexte ne l'évoquent pas.", "Une hypokaliémie || Le contexte oriente vers une compression."],
 notions="N04 N22 N12", angle="piège", diff=3, ladder=L("Paraplégie après rachianesthésie.", "Saignement épidural.", "Sous anticoagulant.", "Hématome versus effet anesthésique.", "IRM, antagonisation, chirurgie.", "Attendre.", "Anticoagulant + geste : hématome."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 45 ans tombe d'une échelle à Fribourg. Une heure plus tard, il a une paraplégie flasque avec réflexes abolis et un niveau sensitif en T8.", prompt="Comment interprétez-vous l'aréflexie ?",
 items=["*Un choc spinal, qui donne une aréflexie transitoire malgré une lésion médullaire || La lésion reste centrale.", "Une atteinte des nerfs périphériques || Le niveau sensitif localise la moelle.", "Une polyradiculonévrite || Le contexte traumatique et le niveau sensitif l'excluent.", "Une simulation || Le tableau est neurologique.", "Une hypoglycémie || Elle n'explique pas un niveau sensitif."],
 notions="N09 N08", angle="piège", diff=3, ladder=L("Paraplégie flasque.", "Sidération médullaire.", "Niveau T8, aréflexie.", "Choc spinal versus nerf.", "Imagerie, stabilisation.", "Conclure au périphérique.", "Niveau sensitif = moelle."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 42 ans consulte aux urgences de Genève pour une lombosciatique bilatérale, une anesthésie du périnée et une rétention urinaire depuis 12 heures. Les réflexes achilléens sont abolis.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Un syndrome de la queue de cheval || Anesthésie en selle, rétention et déficit périphérique.", "Une compression médullaire thoracique || Elle donnerait un niveau thoracique et des réflexes vifs.", "Une lombalgie commune || Les signes neurologiques l'excluent.", "Une cystite || Elle n'explique pas l'anesthésie en selle.", "Une sclérose en plaques || Le tableau est radiculaire."],
 notions="N15 N10", angle="application", diff=2, ladder=L("Sciatique bilatérale.", "Compression des racines sacrées.", "Anesthésie en selle, rétention.", "Queue de cheval versus moelle.", "IRM et chirurgie urgentes.", "Banaliser.", "Selle + rétention : urgence."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 72 ans connu pour un cancer de la prostate métastatique présente depuis 10 jours une faiblesse des jambes. Il signale une incontinence urinaire depuis 2 jours.", prompt="Que vous apprend l'incontinence ?",
 items=["*Elle signe une compression avancée, de moins bon pronostic, qui impose une prise en charge immédiate || Les troubles sphinctériens sont tardifs.", "Elle est due à la prostate et sans rapport || Le contexte oriente vers la compression.", "Elle annonce une récupération spontanée || Elle signe au contraire une gravité.", "Elle exclut une compression médullaire || Elle en est un signe tardif.", "Elle ne change rien à l'urgence || Elle aggrave le pronostic."],
 notions="N10 N02 N26", angle="piège", diff=2, ladder=L("Incontinence tardive.", "Compression avancée.", "Faiblesse depuis 10 jours.", "Signe tardif.", "Urgence.", "Accuser la prostate.", "Sphincters = tardif."), sources="[NICE NG234, 2023]"),
dict(masque=False, sit="monographique", format="A", stem="Une femme de 68 ans atteinte d'un myélome présente une compression médullaire thoracique débutante. Elle marche encore.", prompt="Quel traitement est souvent privilégié pour cette tumeur ?",
 items=["*La radiothérapie, car le myélome est radiosensible, avec dexaméthasone || Elle décomprime souvent sans chirurgie.", "La chirurgie systématique sans radiothérapie || La radiothérapie est souvent suffisante.", "L'abstention || Le déficit progresserait.", "La chimiothérapie seule à 3 mois || Le délai est dangereux.", "La ponction lombaire évacuatrice || Elle n'a pas sa place."],
 notions="N20 N18", angle="application", diff=3, ladder=L("Myélome compressif.", "Radiosensibilité.", "Marche conservée.", "Choix du traitement.", "Radiothérapie et corticoïdes.", "Chirurgie systématique.", "Radiosensible : radiothérapie."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 60 ans porteur d'un pacemaker non compatible IRM présente une suspicion de compression médullaire.", prompt="Quel examen choisissez-vous ?",
 items=["*Un CT ou un myéloscanner du rachis || Il remplace l'IRM contre-indiquée.", "Aucune imagerie || Le diagnostic doit être confirmé.", "Une radiographie standard seule || Elle est insuffisante.", "Une scintigraphie osseuse seule || Elle ne montre pas la compression.", "Une échographie rachidienne || Elle n'est pas adaptée chez l'adulte."],
 notions="N13 N12", angle="application", diff=2, ladder=L("IRM impossible.", "Visualiser le canal.", "Pacemaker.", "Alternative.", "Myéloscanner.", "Renoncer.", "Sans IRM : CT."), sources="[NICE NG234, 2023]"),
dict(format="Kprim", stem="Vous rédigez à Neuchâtel une information pour des patients atteints d'un cancer à risque de métastases osseuses.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une douleur dorsale nouvelle et persistante doit être signalée rapidement. || Elle précède souvent le déficit.", "V: Une faiblesse ou un engourdissement des jambes est une urgence. || Il signe une compression.", "F: Les troubles urinaires sont le premier signe à attendre. || Ils sont tardifs.", "F: Une douleur qui augmente en position couchée est rassurante. || Elle est un drapeau rouge."],
 notions="N29 N06 N10", angle="direct", diff=2, ladder=L("Information.", "Signes d'alerte.", "Patients à risque.", "Douleur et déficit.", "Consulter vite.", "Attendre les urines.", "La douleur alerte."), sources="[NICE NG234, 2023]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un homme de 66 ans atteint d'un cancer pulmonaire présente une compression médullaire métastatique.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La dexaméthasone se donne avec un inhibiteur de la pompe à protons. || Elle expose à l'ulcère.", "V: L'IRM doit couvrir tout le rachis. || Plusieurs niveaux peuvent être atteints.", "F: La chirurgie est toujours indiquée. || Elle dépend de l'état et du pronostic.", "F: Le pronostic de marche ne dépend pas de l'état initial. || La marche au diagnostic le prédit."],
 notions="N18 N12 N19 N26", angle="piège", diff=3, ladder=L("Compression métastatique.", "Œdème et compression.", "Cancer pulmonaire.", "Décisions.", "Corticoïdes, IRM complète.", "Chirurgie systématique.", "Tout le rachis."), sources="[NICE NG234, 2023]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Une femme de 58 ans paraplégique depuis 3 semaines après une compression médullaire opérée prépare sa réadaptation.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un centre de réadaptation spécialisé est adapté. || Il couvre vessie, intestin, peau et mobilité.", "V: La constipation neurogène nécessite un programme intestinal. || L'atteinte médullaire ralentit le transit.", "V: La stabilité du rachis se surveille. || La lésion métastatique peut évoluer.", "F: La douleur ne nécessite pas de traitement systématique. || Elle est fréquente et se traite."],
 notions="N28 N25 N27", angle="application", diff=2, ladder=L("Paraplégie.", "Dénervation viscérale.", "Réadaptation.", "Besoins.", "Centre spécialisé.", "Négliger la douleur.", "Réadaptation globale."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 35 ans présente en 3 jours une paraparésie avec un niveau sensitif en T6 et une rétention urinaire. L'IRM ne montre aucune compression mais un hypersignal intramédullaire.", prompt="Quel diagnostic évoquez-vous ?",
 items=["*Une myélite transverse || Tableau médullaire sans compression.", "Une compression métastatique || L'IRM n'en montre pas.", "Un syndrome de la queue de cheval || Le niveau est thoracique.", "Une polyradiculonévrite || Le niveau sensitif l'exclut.", "Un abcès épidural || L'IRM l'aurait montré."],
 notions="N17 N08", angle="application", diff=3, ladder=L("Syndrome médullaire.", "Inflammation de la moelle.", "IRM sans compression.", "Myélite versus compression.", "Bilan inflammatoire.", "Conclure à une compression.", "Pas de compression : myélite."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 50 ans présente une faiblesse des jambes progressive depuis 5 jours, des paresthésies des mains et des pieds et une aréflexie, sans niveau sensitif ni trouble urinaire.", prompt="Quel diagnostic évoquez-vous en premier ?",
 items=["*Une polyradiculonévrite aiguë || Faiblesse ascendante aréflexique sans niveau.", "Une compression médullaire thoracique || Elle donne un niveau sensitif.", "Un syndrome de la queue de cheval || Il donne une anesthésie en selle.", "Une myélite transverse || Elle donne un niveau sensitif.", "Un AVC || L'atteinte est bilatérale et progressive."],
 notions="N16 N08 N15", angle="piège", diff=2, ladder=L("Faiblesse ascendante.", "Atteinte radiculaire.", "Pas de niveau.", "Moelle versus racines.", "LCR, ENMG.", "Penser moelle.", "Pas de niveau : racines."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un homme de 62 ans présente une compression médullaire. Vous cherchez la cause.", prompt="Quels cancers donnent le plus souvent des métastases vertébrales compressives ? (4 réponses)",
 items=["*Sein || Il métastase souvent à l'os.", "*Prostate || Il métastase souvent à l'os.", "*Poumon || Il métastase souvent à l'os.", "*Myélome || Il touche les vertèbres.", "Glioblastome || Il reste cérébral.", "Carcinome basocellulaire || Il métastase exceptionnellement.", "Cancer du col débutant || Il n'en est pas une cause principale.", "Thymome || Il n'en est pas une cause principale.", "Cancer de la vésicule || Il n'en est pas une cause principale.", "Leucémie lymphoïde chronique || Elle n'en est pas une cause principale.", "Mésothéliome || Il n'en est pas une cause principale.", "Cancer de l'œsophage || Il n'en est pas une cause principale."],
 notions="N02", angle="direct", diff=2, ladder=L("Cause tumorale.", "Tropisme osseux.", "Métastases.", "Primitifs fréquents.", "Chercher le primitif.", "Cancers rares.", "Sein, prostate, poumon, rein, myélome."), sources="[NICE NG234, 2023]"),
dict(format="MenuLong", stem="Un patient présente une paraparésie aiguë avec niveau sensitif. Vous dressez la liste des causes compressives à évoquer.", prompt="Quelles causes compressives sont à évoquer selon le contexte ? (3 réponses)",
 items=["*Abcès épidural || Fièvre, diabète, geste rachidien.", "*Hématome épidural || Anticoagulant, geste rachidien.", "*Hernie discale thoracique || Cause discale rare mais possible.", "Myélite transverse || Elle n'est pas compressive.", "Sclérose en plaques || Elle n'est pas compressive.", "Polyradiculonévrite || Elle n'est pas médullaire.", "Carence en vitamine B12 || Elle n'est pas compressive.", "Myasthénie || Elle n'est pas médullaire.", "Hypokaliémie || Elle n'est pas compressive.", "AVC cérébral || Il n'est pas médullaire.", "Neurosyphilis || Elle n'est pas compressive.", "Infarctus médullaire || Il n'est pas compressif."],
 notions="N03 N04 N22 N11", angle="application", diff=3, ladder=L("Paraparésie.", "Masse dans le canal.", "Contexte.", "Compressif versus non compressif.", "IRM.", "Oublier l'abcès.", "Contexte oriente la cause."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 77 ans, en fin de vie d'un cancer pulmonaire et alité depuis 2 mois, développe une paraplégie complète depuis 3 jours. Il souhaite rester à domicile.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Privilégier le confort avec antalgie, éventuelle dexaméthasone et radiothérapie palliative courte selon ses souhaits, avec le réseau palliatif || Le pronostic et ses souhaits guident.", "Une chirurgie de décompression urgente || Le bénéfice est nul dans cette situation.", "Une IRM et une chirurgie quelle que soit sa volonté || Ses souhaits priment.", "Aucune antalgie pour ne pas masquer les signes || La douleur doit être traitée.", "Un transfert en réadaptation intensive || Elle ne correspond pas à son état."],
 notions="N28 N23 N26", angle="application", diff=3, ladder=L("Fin de vie.", "Pronostic limité.", "Paraplégie complète ancienne.", "Proportionnalité.", "Soins palliatifs.", "Chirurgie à tout prix.", "Respecter le projet."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Compression médullaire aiguë : reconnaître la douleur d'alerte, imager tout le rachis en urgence et décomprimer avant la perte de la marche",
 notions=[
  dict(titre="Causes selon le contexte", rub=["epi", "red"], comment="Laisse le contexte désigner la cause, car elle dicte le traitement.",
   tableau=(["Cause", "Contexte", "Indice", "Traitement"], [
     ["Métastase", "Cancer connu ou non", _T("Douleur nocturne nouvelle", "La métastase étire le périoste et augmente en décubitus."), "Dexaméthasone, chirurgie et/ou radiothérapie"],
     ["Abcès épidural", "Diabète, drogue IV, geste", _T("Fièvre", "Le staphylocoque doré colonise l'espace épidural."), "Antibiotiques, drainage"],
     ["Hématome épidural", "Anticoagulant, péridurale", _T("Déficit après geste", "Le saignement comprime vite."), "Antagonisation, évacuation"],
     ["Traumatisme, fracture", "Chute, ostéoporose", _T("Choc spinal", "L'aréflexie initiale est transitoire."), "Stabilisation, chirurgie"]]),
   points=["Sein, prostate, poumon, rein, myélome."], sources=["[NICE NG234, 2023]", "[Darouiche, NEJM, 2006]"]),
  dict(titre="Sémiologie et différentiels", rub=["ana", "exa", "pos"], comment="Cherche un niveau sensitif : il localise la moelle.",
   tableau=(["Tableau", "Niveau sensitif", "Réflexes", "Discriminant"], [
     ["Compression médullaire", "Oui", "Vifs (aréflexie en choc spinal)", _T("Douleur rachidienne", "La lésion siège dans le canal.")],
     ["Queue de cheval", "Anesthésie en selle", "Abolis", _T("Racines sacrées", "La moelle se termine en L1-L2.")],
     ["Polyradiculonévrite", "Non", "Abolis", _T("Ascendante", "Les racines s'enflamment diffusément.")],
     ["Myélite transverse", "Oui", "Vifs", _T("IRM sans compression", "L'inflammation est intramédullaire.")]]),
   points=["Les sphincters sont tardifs."], sources=["[avis d'expert]"]),
  dict(titre="Conduite d'urgence", rub=["gold", "alt", "acu"], comment="Agis avant la perte de la marche.",
   arbre=[("u1", None, "Suspicion de compression médullaire", "La marche au diagnostic prédit la marche après."),
          ("u2", "u1", "Déficit neurologique", "Dexaméthasone et IRM de tout le rachis immédiates.", "cm_urgence"),
          ("u3", "u1", "Douleur seule chez un cancéreux", "IRM de tout le rachis rapide.", "cm_urgence"),
          ("u4", "u2", "Métastase, patient sélectionné", "Chirurgie puis radiothérapie.", "cm_urgence"),
          ("u5", "u2", "Tumeur radiosensible ou chirurgie impossible", "Radiothérapie.", "cm_urgence"),
          ("u6", "u2", "Abcès ou hématome", "Antibiotiques et drainage, ou antagonisation et évacuation.", "cm_urgence"),
          ("u7", "u1", "IRM contre-indiquée", "CT ou myéloscanner.")],
   points=["IRM de tout le rachis."], sources=["[NICE NG234, 2023]", "[Patchell, Lancet, 2005]"]),
  dict(titre="Complications, réadaptation et palliatif", rub=["hos", "pro", "sur", "fol"], comment="Prévois vessie, peau, thrombose et projet de vie.",
   tableau=(["Problème", "Mesure", "Pourquoi"], [
     ["Rétention", "Sondage", "La vessie neurogène se distend."],
     ["Thrombose", "Thromboprophylaxie", "Cancer et immobilité s'additionnent."],
     ["Escarres", "Retournements, matelas", "Elles se constituent en heures."],
     ["Réadaptation", [("Centre spécialisé", "Il couvre vessie, intestin, peau et mobilité.")], "Centre suisse des paraplégiques"],
     ["Fin de vie", [("Proportionnalité", "Le pronostic et les souhaits guident le traitement.")], "Réseau palliatif"]]),
   points=["Information écrite des patients à risque."], sources=["[NICE NG234, 2023]"]),
 ],
 ssp=dict(code="S7.2", nom="Troubles de la marche", officiel=True, algorithme=[
  ("n1", None, "Trouble de la marche aigu ou subaigu", "Le premier tri cherche un niveau sensitif et des troubles sphinctériens."),
  ("n2", "n1", "Niveau sensitif, douleur rachidienne", "Une compression médullaire impose une IRM de tout le rachis.", "cm_urgence", "c2"),
  ("n3", "n2", "Fièvre", "Un abcès épidural se cherche.", "cm_urgence", "c1"),
  ("n4", "n2", "Cancer connu", "Une métastase est probable ; dexaméthasone.", "cm_urgence", "c1"),
  ("n5", "n2", "Anticoagulant, geste rachidien", "Un hématome épidural se cherche.", "cm_urgence", "c1"),
  ("n6", "n1", "Anesthésie en selle, rétention", "Un syndrome de la queue de cheval est une urgence chirurgicale.", None, "c2"),
  ("n7", "n1", "Faiblesse ascendante aréflexique", "Une polyradiculonévrite se cherche (SSP parésie).", None, "c2"),
  ("n8", "n2", "IRM sans compression", "Une myélite transverse se discute.", None, "c2"),
  ("n9", "n4", "Après traitement", "Réadaptation ou soins palliatifs selon le pronostic.", "cm_suite", "c4")]),
 pec=[
  dict(cle="cm_urgence", titre="Compression médullaire : décomprimer en urgence",
   but=["Préserver ou récupérer la marche et les sphincters.", "Traiter la cause."],
   moyens=dict(accueil=["Examiner force, niveau sensitif et sphincters.", "Immobiliser le rachis si instabilité suspectée."],
    pharma=[("Dexaméthasone (corticoïde)", "Par exemple 16 mg/j avec IPP dans la compression métastatique ; à vérifier dans l'AIPS.", "Elle réduit l'œdème médullaire.", "[NICE NG234, 2023]"),
            ("Antibiotique antistaphylococcique", "Selon le germe et le protocole local ; à vérifier dans l'AIPS.", "Il traite l'abcès épidural.", "[Darouiche, NEJM, 2006]"),
            ("Antagoniste de l'anticoagulant", "Selon la molécule ; à vérifier dans l'AIPS.", "Il arrête le saignement épidural.", "[avis d'expert]")],
    nonpharma=[("geste ou chirurgie", "Décompression chirurgicale ou drainage.", "La décompression rapide sauve la moelle."),
               ("autre", "Radiothérapie urgente des tumeurs radiosensibles.", "Elle réduit la masse tumorale."),
               ("soins infirmiers", "Sondage, retournements, thromboprophylaxie.", "Ils préviennent les complications.")],
    transversal=[("Oncologie et radio-oncologie", "Elles décident radiothérapie et traitement du cancer."), ("Neurochirurgie", "Elle décomprime et stabilise.")]),
   urgence=(["IRM de tout le rachis immédiate.", "Décision chirurgicale en urgence."],
            [("d'abord", "médecin responsable", "Reconnaît le tableau et prescrit dexaméthasone et IRM."),
             ("en même temps", "infirmier·ère", "Sonde, prévient escarres, surveille la force."),
             ("ensuite", "neurochirurgien·ne", "Décide la décompression."),
             ("puis", "radio-oncologue", "Planifie la radiothérapie.")]),
   horsUrgence=None,
   pronostic="La marche au moment du diagnostic prédit la marche après traitement [NICE NG234, 2023].",
   suivi=[("Force, sensibilité, sphincters", "Plusieurs fois par jour", "Stabilité ou amélioration"), ("Glycémie sous corticoïdes", "Quotidienne", "Normoglycémie")],
   sortie="Le patient sort vers la réadaptation ou le domicile quand le rachis est stable et les complications prévenues.",
   prevention=["Elle n'existe pas de façon spécifique.", "Elle repose sur l'information des patients cancéreux à risque.", "Elle passe par la réadaptation et la prévention des complications."]),
  dict(cle="cm_suite", titre="Après la décompression : réadaptation ou palliatif",
   but=["Maximiser l'autonomie.", "Respecter le projet de vie."],
   moyens=dict(accueil=["Évaluer le pronostic avec l'oncologue.", "Discuter les souhaits du patient."],
    pharma=[("Antalgiques", "Selon l'intensité de la douleur ; à vérifier dans l'AIPS.", "La douleur osseuse et neuropathique est fréquente.", "[avis d'expert]")],
    nonpharma=[("rééducation", "Centre spécialisé de réadaptation.", "Il traite vessie, intestin, peau et mobilité."),
               ("social et assurances", "Adapter le domicile, mobiliser les assurances.", "Le retour à domicile se prépare.")],
    transversal=[("Soins palliatifs", "Ils accompagnent la fin de vie.")]),
   urgence=None,
   horsUrgence=(["Revoir la stabilité du rachis.", "Adapter le projet au pronostic."],
            [("d'abord", "médecin de réadaptation", "Fixe le programme."),
             ("ensuite", "oncologue", "Traite le cancer."),
             ("puis", "médecin de famille", "Coordonne le retour à domicile.")]),
   pronostic="Il dépend du déficit initial et du cancer sous-jacent.",
   suivi=[("Mobilité", "Hebdomadaire en réadaptation", "Progrès"), ("Peau et vessie", "Quotidien", "Absence de complication")],
   sortie="La sortie se fait quand le domicile est adapté.",
   prevention=["Elle n'existe pas de façon spécifique.", "Elle repose sur la surveillance du cancer.", "Elle prévient escarres et infections urinaires."]),
 ])
AVERIFIER = ["Dose de dexaméthasone recommandée (16 mg/j) et version suisse à vérifier dans l'AIPS et les recommandations oncologiques suisses.",
             "Référence NICE NG234 (2023) sur la compression médullaire métastatique à vérifier.",
             "Délai cible de l'IRM selon le déficit à vérifier."]
