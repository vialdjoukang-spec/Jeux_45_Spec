ID = "G51.0__F1_4-E17"
PLAN = "monographique"
NOTIONS = [
"def|critère|2||[Baugh, Otolaryngol Head Neck Surg, 2013, AAO-HNS]|La paralysie faciale périphérique idiopathique (paralysie de Bell) est une atteinte aiguë unilatérale du nerf facial, installée en moins de 72 heures, sans autre cause retrouvée.",  # N01
"epi|chiffre|1||[Baugh, Otolaryngol Head Neck Surg, 2013]|La paralysie de Bell représente la majorité des paralysies faciales périphériques et survient plus souvent pendant la grossesse et chez le diabétique.",  # N02
"bas|mécanisme|3||[avis d'expert]|Le front est épargné dans la paralysie faciale centrale, car la partie supérieure du noyau facial reçoit une innervation corticale des deux hémisphères.",  # N03
"bas|mécanisme|1||[avis d'expert]|Une inflammation probablement virale fait gonfler le nerf dans son canal osseux étroit, ce qui le comprime.",  # N04
"ana|symptôme|1||[avis d'expert]|L'hyperacousie, la perte du goût des deux tiers antérieurs de la langue et la sécheresse oculaire traduisent l'atteinte des branches intrapétreuses du nerf facial.",  # N05
"exa|signe|2||[avis d'expert]|La paralysie périphérique touche tout l'hémivisage, avec impossibilité de plisser le front et de fermer l'œil (signe de Charles Bell).",  # N06
"exa|signe|1||[avis d'expert]|L'examen otoscopique et cutané cherche des vésicules du conduit auditif externe, qui évoquent un zona.",  # N07
"red|signe|3||[avis d'expert]|Une asymétrie faciale qui épargne le front, surtout associée à une faiblesse du membre ou à une aphasie, évoque un AVC et impose la filière AVC.",  # N08
"red|piège|2||[Baugh, Otolaryngol Head Neck Surg, 2013]|Une évolution progressive au-delà de 3 semaines, une atteinte d'autres nerfs crâniens ou une absence de récupération à 3 mois imposent une imagerie.",  # N09
"gold|décision|2||[Baugh, Otolaryngol Head Neck Surg, 2013]|Le diagnostic de paralysie de Bell est clinique, et ni imagerie ni bilan biologique ne sont systématiques dans une forme typique.",  # N10
"alt|examen|1|S|[avis d'expert ; OFSP]|En zone d'endémie de Lyme comme la Suisse, une sérologie de Borrelia et parfois une ponction lombaire se discutent, surtout chez l'enfant ou en cas d'atteinte bilatérale.",  # N11
"alt|examen|1||[avis d'expert]|L'électroneuromyographie évalue le pronostic d'une paralysie complète après quelques jours.",  # N12
"pos|diagnostic différentiel|2||[avis d'expert]|Le syndrome de Ramsay Hunt associe paralysie faciale, otalgie, vésicules auriculaires et parfois surdité ou vertige, et se traite par antiviral et corticoïde.",  # N13
"pos|diagnostic différentiel|1||[avis d'expert]|Une paralysie faciale bilatérale évoque une neuroborréliose, un Guillain-Barré ou une sarcoïdose plutôt qu'une paralysie de Bell.",  # N14
"pos|diagnostic différentiel|1||[avis d'expert]|Une paralysie lentement progressive ou partielle avec masse parotidienne évoque une tumeur.",  # N15
"pos|diagnostic différentiel|1||[avis d'expert]|Une otite moyenne aiguë ou un cholestéatome peuvent comprimer le nerf facial et relèvent de l'ORL.",  # N16
"acu|posologie|3|S|[Sullivan, NEJM, 2007 ; AIPS Swissmedic]|La prednisolone débutée dans les 72 heures, par exemple 50 mg/j pendant 10 jours, augmente la récupération complète, posologie à vérifier dans l'AIPS.",  # N17
"acu|piège|2||[Sullivan, NEJM, 2007 ; Baugh, 2013]|Un antiviral seul n'est pas efficace dans la paralysie de Bell, et son ajout aux corticoïdes n'est qu'une option dans les formes sévères.",  # N18
"acu|décision|2||[Baugh, Otolaryngol Head Neck Surg, 2013]|L'œil qui ne se ferme pas se protège par larmes artificielles le jour, pommade et occlusion la nuit, pour prévenir une kératite.",  # N19
"acu|molécule|1||[avis d'expert]|La neuroborréliose faciale se traite par doxycycline per os ou ceftriaxone IV selon l'atteinte, posologies à vérifier dans l'AIPS.",  # N20
"chr|complication|1||[avis d'expert]|Une récupération incomplète laisse des syncinésies, que la rééducation et la toxine botulique peuvent améliorer.",  # N21
"hos|complication|2||[avis d'expert]|La kératite d'exposition est la complication aiguë à prévenir, car elle peut menacer la vision.",  # N22
"pro|pronostic|2||[Sullivan, NEJM, 2007]|La plupart des paralysies de Bell récupèrent complètement en quelques semaines à quelques mois, surtout sous corticoïdes.",  # N23
"pro|pronostic|1||[avis d'expert]|Une paralysie complète initiale, un âge avancé et l'absence de début de récupération à 3 semaines annoncent un pronostic moins bon.",  # N24
"sur|décision|1||[avis d'expert]|Le patient est revu pour vérifier la récupération et la protection oculaire, et adressé si la récupération manque à 3 mois.",  # N25
"fol|contexte suisse|1|S|[avis d'expert]|Une paralysie persistante peut justifier une prise en charge en ORL ou chirurgie plastique faciale, ainsi qu'une physiothérapie spécialisée.",  # N26
]
ANGLES = [
"Le front épargné signe une atteinte centrale.",
"La prednisolone se donne dans les 72 heures ; l'antiviral seul est inefficace.",
"Les vésicules auriculaires changent le diagnostic et le traitement.",
"La Suisse est une zone d'endémie de Lyme.",
"L'œil qui ne se ferme pas doit être protégé.",
"L'absence de récupération à 3 mois impose une imagerie.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un homme de 41 ans consulte à Neuchâtel car, ce matin, sa bouche tombe à droite et il bave en buvant. Il ne peut ni plisser le front ni fermer l'œil droit. Il ne présente aucun autre déficit.", prompt="Où se situe la lésion ?",
 items=["*Sur le nerf facial droit en périphérie || Le front est atteint.", "Dans le cortex moteur gauche || Une lésion centrale épargne le front.", "Dans le nerf trijumeau || Il est sensitif et masticateur.", "Dans la jonction neuromusculaire || Le tableau est brutal et unilatéral.", "Dans le muscle orbiculaire seul || Tout l'hémivisage est atteint."],
 notions="N06 N03", angle="application", diff=1, ladder=L("Asymétrie faciale.", "Innervation corticale bilatérale du front.", "Front atteint.", "Central versus périphérique.", "Périphérique.", "Penser AVC.", "Front atteint : périphérique."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 2, 4), stem="Cet homme n'a ni vésicule, ni otalgie, ni fièvre, ni piqûre de tique connue. L'otoscopie est normale. Les symptômes datent de 18 heures.", prompt="Quel traitement est indiqué ?",
 items=["*Prednisolone dans les 72 heures, par exemple 50 mg/j pendant 10 jours || Elle augmente la récupération complète.", "Valaciclovir seul || Un antiviral seul est inefficace.", "Aucun traitement, la récupération est toujours complète || Les corticoïdes améliorent le pronostic.", "Antibiothérapie par amoxicilline || Rien n'évoque une infection bactérienne.", "Chirurgie de décompression d'emblée || Elle n'est pas indiquée."],
 notions="N17 N18 N01 N10", angle="application", diff=2, ladder=L("Paralysie typique récente.", "Œdème du nerf.", "Moins de 72 h.", "Fenêtre thérapeutique.", "Prednisolone.", "Antiviral seul.", "< 72 h : corticoïde."), sources="[Sullivan, NEJM, 2007]"),
dict(format="A", serie=("S1", 3, 4), stem="Cet homme ne parvient pas à fermer complètement l'œil droit et le trouve sec et irrité.", prompt="Quelle mesure est indispensable ?",
 items=["*Larmes artificielles le jour, pommade et occlusion la nuit || Elles préviennent une kératite d'exposition.", "Aucune mesure, l'œil se protège seul || Il reste ouvert.", "Collyre corticoïde au long cours || Il expose à des complications.", "Patch sans pommade jour et nuit pendant des mois || L'hydratation est indispensable.", "Lunettes de soleil seules || Elles ne suffisent pas la nuit."],
 notions="N19 N22", angle="application", diff=1, ladder=L("Œil ouvert.", "Exposition cornéenne.", "Sécheresse.", "Kératite.", "Protection oculaire.", "Négliger l'œil.", "Œil qui ne ferme pas : protéger."), sources="[Baugh, Otolaryngol Head Neck Surg, 2013]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Trois mois plus tard, la paralysie de cet homme n'a pas du tout récupéré.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une imagerie est indiquée. || L'absence de récupération à 3 mois fait chercher une autre cause.", "V: Une tumeur du nerf facial ou de la parotide doit être recherchée. || Elle peut mimer une paralysie de Bell.", "F: L'absence de récupération est banale et ne demande rien. || Elle est un drapeau rouge.", "F: Une deuxième cure d'antiviral seul est le traitement. || L'antiviral seul est inefficace."],
 notions="N09 N15 N25 N18", angle="piège", diff=3, ladder=L("Pas de récupération.", "Cause tumorale possible.", "Trois mois.", "Drapeau rouge.", "Imagerie, ORL.", "Banaliser.", "Pas de récupération : imager."), sources="[Baugh, Otolaryngol Head Neck Surg, 2013]"),
dict(format="A", stem="Une femme de 71 ans est amenée aux urgences de Berne pour une bouche déviée à gauche depuis 40 minutes. Elle plisse normalement le front et ferme les deux yeux. Son bras droit est maladroit.", prompt="Quelle est la conduite la plus adaptée ?",
 items=["*Activer la filière AVC aiguë || Une atteinte faciale épargnant le front avec déficit du membre évoque un AVC.", "Prescrire de la prednisolone || Le tableau n'est pas une paralysie de Bell.", "Prescrire un antiviral || Le tableau est central.", "Revoir dans 72 heures || Le délai fait perdre la fenêtre de reperfusion.", "Demander une sérologie de Lyme || Le tableau évoque un AVC."],
 notions="N08 N03", angle="piège", diff=2, ladder=L("Asymétrie faciale aiguë.", "Lésion corticale.", "Front épargné, bras maladroit.", "Central versus périphérique.", "Code AVC.", "Prednisolone.", "Front épargné : AVC."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 66 ans présente une paralysie faciale droite complète depuis hier, une douleur intense de l'oreille droite et des vésicules dans le conduit auditif. Il signale un vertige et une baisse de l'audition.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Un syndrome de Ramsay Hunt || Paralysie faciale, otalgie, vésicules, atteinte cochléovestibulaire.", "Une paralysie de Bell || Les vésicules et l'atteinte cochléovestibulaire orientent ailleurs.", "Une otite externe simple || Elle n'explique pas la paralysie.", "Une neuroborréliose || Elle ne donne pas de vésicules.", "Un AVC || Le tableau est périphérique."],
 notions="N13 N07", angle="application", diff=2, ladder=L("Paralysie et otalgie.", "Réactivation du VZV.", "Vésicules du conduit.", "Ramsay Hunt versus Bell.", "Antiviral et corticoïde.", "Traiter comme Bell.", "Vésicules : zona."), sources="[avis d'expert]"),
dict(format="A", stem="Un garçon de 9 ans du canton de Berne présente une paralysie faciale gauche depuis 2 jours. Il a joué en forêt cet été et sa mère a retiré une tique il y a 6 semaines.", prompt="Quelle démarche est la plus adaptée ?",
 items=["*Rechercher une neuroborréliose par sérologie et discuter la ponction lombaire || La Suisse est une zone d'endémie et l'enfant est exposé.", "Prescrire de la prednisolone sans autre examen || Une neuroborréliose doit être exclue.", "Prescrire un antiviral seul || Il est inefficace.", "Demander une IRM cérébrale en urgence || Le contexte oriente vers Lyme.", "Rassurer sans examen || Une cause traitable doit être exclue."],
 notions="N11 N20 N14", angle="application", diff=3, ladder=L("Paralysie faciale chez un enfant.", "Borrelia neurotrope.", "Tique en forêt.", "Lyme versus Bell.", "Sérologie, PL, antibiotique.", "Corticoïde seul.", "Enfant + tique : Lyme."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 30 ans présente en 5 jours une paralysie faciale bilatérale. Elle a des paresthésies des pieds et les réflexes rotuliens sont diminués.", prompt="Quelle hypothèse évoquez-vous ?",
 items=["*Un syndrome de Guillain-Barré || Diplégie faciale, paresthésies et hyporéflexie.", "Une double paralysie de Bell || Elle est exceptionnelle et n'explique pas l'hyporéflexie.", "Un AVC bilatéral || Il n'explique pas l'aréflexie.", "Une migraine || Rien ne l'évoque.", "Une parotidite || Elle n'explique pas les signes périphériques."],
 notions="N14 N09", angle="piège", diff=3, ladder=L("Diplégie faciale.", "Atteinte des nerfs périphériques.", "Paresthésies, hyporéflexie.", "Bilatéral : pas Bell.", "LCR, ENMG.", "Conclure à Bell.", "Bilatéral : chercher une cause."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 32 ans enceinte de 34 semaines présente une paralysie faciale périphérique droite apparue il y a 24 heures, sans autre signe.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Proposer une corticothérapie courte dans les 72 heures après évaluation, avec protection oculaire et contrôle tensionnel || La grossesse favorise la paralysie de Bell et une prééclampsie doit être exclue.", "Interdire tout traitement pendant la grossesse || La corticothérapie courte reste possible.", "Prescrire un antiviral seul || Il est inefficace.", "Programmer une césarienne || Rien ne l'indique.", "Faire une IRM cérébrale avec gadolinium en urgence || Elle n'est pas indiquée."],
 notions="N02 N17 N19", angle="application", diff=3, ladder=L("Paralysie en grossesse.", "Terrain favorisant.", "Troisième trimestre.", "Balance bénéfice-risque.", "Corticoïde, œil, tension.", "Ne rien faire.", "Grossesse : terrain à risque."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 55 ans présente depuis 4 mois une faiblesse lentement progressive de l'hémivisage gauche et une tuméfaction sous l'oreille gauche.", prompt="Quelle hypothèse évoquez-vous ?",
 items=["*Une tumeur de la parotide envahissant le nerf facial || L'évolution progressive et la masse l'évoquent.", "Une paralysie de Bell || Elle s'installe en moins de 72 heures.", "Un syndrome de Ramsay Hunt || Il est aigu avec vésicules.", "Un AVC || Il est brutal et central.", "Une myasthénie || Elle ne donne pas de masse."],
 notions="N15 N09", angle="direct", diff=2, ladder=L("Paralysie progressive.", "Envahissement tumoral.", "Masse parotidienne.", "Progressif versus aigu.", "Imagerie, ORL.", "Conclure à Bell.", "Progressif : tumeur."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un patient de 47 ans présente une paralysie faciale de Bell. Il remarque qu'il entend les sons trop forts du côté atteint et que la nourriture a moins de goût.", prompt="Comment expliquez-vous ces symptômes ?",
 items=["*Par l'atteinte du nerf du muscle stapédien et de la corde du tympan || Ces branches naissent dans le trajet intrapétreux.", "Par une atteinte du nerf cochléaire || L'hyperacousie traduit la perte du réflexe stapédien.", "Par une atteinte du trijumeau || Il ne porte pas le goût antérieur.", "Par une anxiété || Les symptômes sont neurologiques.", "Par une otite associée || L'otoscopie est normale dans la forme typique."],
 notions="N05 N04", angle="direct", diff=2, ladder=L("Hyperacousie et goût.", "Branches intrapétreuses.", "Stapédien et corde du tympan.", "Topographie.", "Expliquer.", "Penser au nerf cochléaire.", "Branches du VII."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 38 ans présente une paralysie faciale périphérique typique depuis 24 heures. Il demande un scanner et une prise de sang « pour être sûr ».", prompt="Quelle réponse est la plus adaptée ?",
 items=["*Expliquer que le diagnostic est clinique et que ces examens ne sont pas utiles dans une forme typique || Ils n'améliorent pas la prise en charge.", "Prescrire un CT cérébral systématique || Il expose aux rayons sans bénéfice.", "Prescrire un bilan sanguin complet systématique || Il n'est pas utile dans la forme typique.", "Prescrire une IRM en urgence || Elle n'est pas indiquée sans drapeau rouge.", "Refuser toute explication || L'information fait partie des soins."],
 notions="N10 N01", angle="piège", diff=2, ladder=L("Demande d'examens.", "Diagnostic clinique.", "Forme typique.", "Smarter Medicine.", "Expliquer.", "Examens inutiles.", "Typique : pas d'imagerie."), sources="[Baugh, Otolaryngol Head Neck Surg, 2013]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous expliquez à un groupe d'étudiants à Genève la différence entre paralysie faciale centrale et périphérique.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La paralysie centrale épargne le front. || Le front reçoit une innervation corticale bilatérale.", "V: La paralysie périphérique empêche la fermeture de l'œil. || L'orbiculaire de l'œil est paralysé.", "F: Une paralysie centrale s'accompagne d'hyperacousie. || L'hyperacousie traduit une atteinte périphérique.", "F: Un front épargné permet de prescrire un corticoïde sans autre bilan. || Il évoque un AVC."],
 notions="N03 N06 N05 N08", angle="direct", diff=2, ladder=L("Central versus périphérique.", "Innervation du front.", "Front, œil.", "Topographie.", "Distinguer.", "Corticoïde sur un AVC.", "Front épargné : central."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un patient de 60 ans demande à Lucerne quel est son pronostic après une paralysie de Bell complète.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La plupart des paralysies de Bell récupèrent complètement. || Le pronostic global est favorable.", "V: Une paralysie complète initiale annonce un pronostic moins bon. || L'atteinte axonale est plus probable.", "V: Des syncinésies peuvent persister en cas de récupération incomplète. || La repousse axonale est aberrante.", "F: L'électroneuromyographie n'a aucune valeur pronostique. || Elle évalue la dégénérescence axonale."],
 notions="N23 N24 N21 N12", angle="direct", diff=3, ladder=L("Pronostic.", "Dégénérescence axonale.", "Paralysie complète.", "Facteurs pronostiques.", "Informer.", "Pessimisme ou optimisme excessif.", "Majorité de récupération."), sources="[Sullivan, NEJM, 2007]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Une femme de 44 ans a présenté une paralysie de Bell il y a 8 mois. Elle garde une asymétrie et son œil se ferme quand elle sourit.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Elle présente des syncinésies. || La repousse axonale est aberrante.", "V: La toxine botulique peut améliorer ces syncinésies. || Elle affaiblit les contractions indésirables.", "V: Une physiothérapie faciale spécialisée peut l'aider. || Elle rééduque le contrôle moteur.", "F: Une corticothérapie maintenant améliorera la récupération. || La fenêtre est dépassée."],
 notions="N21 N26 N17", angle="piège", diff=2, ladder=L("Séquelles.", "Repousse aberrante.", "Œil qui se ferme au sourire.", "Syncinésies.", "Toxine, physiothérapie.", "Corticoïde tardif.", "Syncinésies : toxine."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 69 ans a une paralysie faciale de Bell sévère depuis 12 heures et un œil droit qui reste ouvert. Il demande s'il doit prendre aussi un antiviral.", prompt="Quelle réponse est la plus juste ?",
 items=["*La prednisolone est le traitement de base ; l'ajout d'un antiviral n'est qu'une option discutée dans les formes sévères || Le bénéfice de l'antiviral est incertain.", "L'antiviral seul suffit || Il est inefficace seul.", "L'antiviral est obligatoire dans tous les cas || Son bénéfice n'est pas démontré.", "Aucun traitement n'est utile || La prednisolone améliore la récupération.", "Un antibiotique est préférable || Rien ne l'indique."],
 notions="N18 N17 N19 N22", angle="direct", diff=3, ladder=L("Forme sévère.", "Hypothèse virale.", "Demande d'antiviral.", "Preuves.", "Corticoïde, option antivirale.", "Antiviral seul.", "Corticoïde d'abord."), sources="[Baugh, Otolaryngol Head Neck Surg, 2013]"),
dict(format="A", stem="Un enfant de 6 ans présente une paralysie faciale avec une otalgie, une fièvre et un tympan bombé et rouge.", prompt="Quelle cause est la plus probable ?",
 items=["*Une otite moyenne aiguë compliquée, qui relève de l'ORL || L'inflammation de l'oreille moyenne comprime le nerf facial.", "Une paralysie de Bell || La fièvre et le tympan pathologique orientent ailleurs.", "Un AVC || Rien ne l'évoque.", "Une tumeur parotidienne || Le tableau est aigu et infectieux.", "Une myasthénie || Rien ne l'évoque."],
 notions="N16 N07", angle="application", diff=2, ladder=L("Paralysie et otite.", "Nerf dans l'oreille moyenne.", "Tympan bombé.", "Cause otogène.", "ORL, antibiotique.", "Conclure à Bell.", "Otoscopie systématique."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un adulte présente une paralysie faciale périphérique aiguë.", prompt="Choisissez les TROIS éléments qui doivent faire rechercher une autre cause qu'une paralysie de Bell.",
 items=["*Atteinte bilatérale || Elle évoque Lyme, Guillain-Barré ou sarcoïdose.", "Hypoesthésie subjective de la joue || Elle est fréquente dans la paralysie de Bell.", "*Évolution progressive sur plus de 3 semaines || Elle évoque une tumeur.", "*Atteinte d'autres nerfs crâniens || Elle évoque une lésion de la base du crâne.", "Installation en moins de 72 heures || Elle est typique.", "Douleur rétro-auriculaire modérée || Elle est fréquente.", "Hyperacousie || Elle est fréquente.", "Perte du goût || Elle est fréquente.", "Sécheresse oculaire || Elle est fréquente.", "Atteinte du front || Elle est typique.", "Larmoiement || Il est possible.", "Diabète associé || Il est un facteur de risque."],
 notions="N09 N14 N13 N15", angle="direct", diff=3, ladder=L("Paralysie périphérique.", "Causes secondaires.", "Signes atypiques.", "Bell versus autre.", "Chercher une cause.", "Tout appeler Bell.", "Atypique : explorer."), sources="[Baugh, Otolaryngol Head Neck Surg, 2013]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un patient de 52 ans atteint d'une paralysie de Bell depuis 24 heures demande ce que vous lui prescrivez.", prompt="Quelles mesures sont recommandées ? (3 réponses)",
 items=["*Prednisolone pendant 10 jours || Elle améliore la récupération.", "*Larmes artificielles le jour || Elles protègent la cornée.", "*Pommade et occlusion oculaire la nuit || Elles évitent la kératite.", "Antiviral seul || Inefficace seul.", "Antibiotique || Aucune indication.", "Décompression chirurgicale immédiate || Pas d'indication de routine.", "CT cérébral systématique || Pas d'indication.", "Électrostimulation précoce || Non recommandée.", "Benzodiazépine || Aucune indication.", "Collyre corticoïde || Non indiqué.", "Arrêt de travail de 6 mois || Excessif.", "Repos strict au lit || Non nécessaire."],
 notions="N17 N19 N22", angle="application", diff=2, ladder=L("Traitement initial.", "Œdème et exposition.", "Bell récente.", "Mesures prouvées.", "Corticoïde et œil.", "Mesures inutiles.", "Corticoïde + œil."), sources="[Baugh, Otolaryngol Head Neck Surg, 2013]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 50 ans a une paralysie faciale de Bell depuis 3 semaines. Aucun début de récupération n'est visible.", prompt="Quelle attitude est la plus adaptée ?",
 items=["*Le revoir régulièrement, l'informer d'un pronostic plus réservé et l'adresser si rien ne récupère à 3 mois || L'absence de récupération précoce assombrit le pronostic.", "Reprendre une corticothérapie maintenant || La fenêtre est dépassée.", "Décompression chirurgicale immédiate || Elle n'est pas recommandée de routine.", "Conclure à une guérison certaine || Le pronostic est moins bon.", "Arrêter toute protection oculaire || L'œil reste exposé."],
 notions="N24 N25 N23", angle="application", diff=3, ladder=L("Pas de récupération à 3 semaines.", "Dégénérescence axonale probable.", "Paralysie persistante.", "Pronostic.", "Suivi et seuil de 3 mois.", "Corticoïde tardif.", "3 mois : explorer."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Asymétrie faciale aiguë : distinguer central et périphérique, traiter la paralysie de Bell dans les 72 heures et protéger l'œil",
 notions=[
  dict(titre="Central ou périphérique", rub=["bas", "exa", "red"], comment="Regarde le front d'abord : il localise la lésion.",
   tableau=(["Atteinte", "Front", "Œil", "Discriminant"], [
     ["Centrale (AVC)", "Épargné", "Se ferme", _T("Déficit associé", "La lésion corticale touche aussi le membre ou le langage.")],
     ["Périphérique", "Atteint", "Ne se ferme pas", _T("Signe de Charles Bell", "L'orbiculaire est paralysé et l'œil monte.")],
     ["Branches intrapétreuses", "—", "Sécheresse", _T("Hyperacousie, goût", "Le stapédien et la corde du tympan naissent dans le rocher.")]]),
   points=["Front épargné + bras : Code AVC."], sources=["[avis d'expert]"]),
  dict(titre="Causes de paralysie périphérique", rub=["pos", "alt"], comment="Cherche les indices d'une cause avant de retenir la paralysie de Bell.",
   tableau=(["Cause", "Indice", "Conduite"], [
     ["Bell", "Aigu < 72 h, isolé", _T("Diagnostic d'exclusion", "Il ne se retient qu'en l'absence d'autre cause.")],
     ["Ramsay Hunt", "Vésicules, otalgie, surdité", _T("Antiviral + corticoïde", "Le VZV se réactive dans le ganglion géniculé.")],
     ["Neuroborréliose", "Tique, enfant, bilatéral", _T("Sérologie, PL, antibiotique", "La Suisse est une zone d'endémie.")],
     ["Guillain-Barré", "Bilatéral, aréflexie", _T("LCR, ENMG", "L'atteinte est radiculaire diffuse.")],
     ["Tumeur parotidienne", "Progressif, masse", _T("Imagerie, ORL", "La croissance tumorale est lente.")],
     ["Otite, cholestéatome", "Tympan anormal", _T("ORL", "Le nerf traverse l'oreille moyenne.")]]),
   points=["Bilatéral : jamais Bell d'emblée."], sources=["[Baugh, Otolaryngol Head Neck Surg, 2013]"]),
  dict(titre="Traitement de la paralysie de Bell", rub=["acu", "gold"], comment="Traite dans les 72 heures et protège l'œil.",
   arbre=[("t1", None, "Paralysie faciale périphérique typique", "Le diagnostic est clinique, sans imagerie."),
          ("t2", "t1", "Moins de 72 heures", "Prednisolone pendant 10 jours.", "bell"),
          ("t3", "t1", "Fermeture palpébrale incomplète", "Larmes, pommade et occlusion nocturne.", "bell"),
          ("t4", "t2", "Forme sévère", "L'ajout d'un antiviral reste une option.", "bell"),
          ("t5", "t1", "Pas de récupération à 3 mois", "Imagerie et avis ORL."),
          ("t6", "t1", "Vésicules ou tique", "Autre cause : traitement spécifique.")],
   points=["Antiviral seul : inefficace."], sources=["[Sullivan, NEJM, 2007]"]),
  dict(titre="Pronostic et séquelles", rub=["pro", "chr", "sur", "hos"], comment="Informe sur une récupération fréquente et repère les séquelles.",
   tableau=(["Élément", "Contenu", "Pourquoi"], [
     ["Récupération", "Complète chez la plupart", "La compression est souvent réversible."],
     ["Mauvais pronostic", "Paralysie complète, âge, pas de récupération à 3 semaines", "La dégénérescence axonale ralentit la repousse."],
     ["Kératite", "Prévention oculaire", "La cornée exposée s'ulcère."],
     ["Syncinésies", "Toxine botulique, physiothérapie", "La repousse axonale est aberrante."]]),
   points=["Revoir à 3 mois en l'absence de récupération."], sources=["[Sullivan, NEJM, 2007]"]),
 ],
 ssp=dict(code="S1.4", nom="Asymétrie ou déformation du visage", officiel=True, algorithme=[
  ("n1", None, "Asymétrie faciale aiguë", "Le premier tri porte sur le front."),
  ("n2", "n1", "Front épargné", "Atteinte centrale : chercher un AVC (Code AVC).", None, "c1"),
  ("n3", "n1", "Front atteint", "Atteinte périphérique : chercher une cause.", None, "c2"),
  ("n4", "n3", "Vésicules, otalgie", "Ramsay Hunt : antiviral et corticoïde.", None, "c2"),
  ("n5", "n3", "Tique, enfant, bilatéral", "Neuroborréliose : sérologie, PL, antibiotique.", None, "c2"),
  ("n6", "n3", "Tympan anormal", "Cause otogène : ORL.", None, "c2"),
  ("n7", "n3", "Isolée, aiguë, < 72 h", "Paralysie de Bell : prednisolone et protection oculaire.", "bell", "c3"),
  ("n8", "n7", "Pas de récupération à 3 mois", "Imagerie et ORL.", None, "c4"),
  ("n9", "n1", "Asymétrie progressive avec masse", "Tumeur parotidienne : imagerie (SSP masse cervicale).")]),
 pec=[
  dict(cle="bell", titre="Paralysie de Bell",
   but=["Augmenter la récupération complète.", "Prévenir la kératite d'exposition."],
   moyens=dict(accueil=["Vérifier l'atteinte du front et l'absence d'autre déficit.", "Examiner oreille, peau et autres nerfs crâniens."],
    pharma=[("Prednisolone (corticoïde)", "Par exemple 50 mg/j pendant 10 jours, débutée dans les 72 heures ; à vérifier dans l'AIPS.", "Elle réduit l'œdème du nerf dans son canal.", "[Sullivan, NEJM, 2007]"),
            ("Valaciclovir (antiviral)", "Option dans les formes sévères, associé au corticoïde ; à vérifier dans l'AIPS.", "Son bénéfice ajouté reste incertain.", "[Baugh, 2013]"),
            ("Larmes artificielles et pommade ophtalmique", "Plusieurs fois par jour et le soir ; à vérifier dans l'AIPS.", "Elles protègent la cornée.", "[Baugh, 2013]")],
    nonpharma=[("soins infirmiers", "Occlusion oculaire nocturne.", "Elle prévient la kératite."),
               ("rééducation", "Physiothérapie faciale si récupération incomplète.", "Elle améliore le contrôle moteur.")],
    transversal=[("ORL", "Elle explore les formes atypiques et non récupérées."), ("Ophtalmologie", "Elle traite une kératite.")]),
   urgence=None,
   horsUrgence=(["Revoir à 2-3 semaines puis à 3 mois si besoin.", "Adresser si signes atypiques."],
            [("d'abord", "médecin de famille", "Pose le diagnostic et prescrit le traitement."),
             ("ensuite", "ORL", "Explore une forme atypique."),
             ("puis", "patient·e", "Protège son œil et signale toute aggravation.")]),
   pronostic="La plupart des patients récupèrent complètement, surtout sous corticoïdes [Sullivan, NEJM, 2007].",
   suivi=[("Fonction faciale", "À 3 semaines et 3 mois", "Récupération"), ("Cornée", "En cas de douleur ou rougeur", "Absence de kératite")],
   sortie="La prise en charge est ambulatoire.",
   prevention=["Elle n'existe pas de façon spécifique.", "Elle passe par la protection oculaire.", "Elle traite les syncinésies par rééducation et toxine botulique."]),
 ])
AVERIFIER = ["Posologie suisse de la prednisolone dans la paralysie de Bell à vérifier dans l'AIPS.",
             "Indication de la sérologie de Lyme chez l'adulte en Suisse à vérifier dans les recommandations suisses.",
             "Proportion de récupération complète sous corticoïdes à confirmer."]
