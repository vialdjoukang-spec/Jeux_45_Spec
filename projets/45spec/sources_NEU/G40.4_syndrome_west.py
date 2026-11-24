ID = "G40.4__O2_5-E12"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[Wilmshurst, Epilepsia, ILAE 2015 ; avis d'expert]|Le syndrome de West associe des spasmes épileptiques en salves, une hypsarythmie à l'EEG et un arrêt ou une régression du développement.",  # N01
"ana|symptôme|2||[avis d'expert]|Les spasmes sont des contractions brèves en flexion ou en extension de la tête, du tronc et des membres, répétées en salves, surtout au réveil.",  # N02
"epi|terrain particulier|2||[avis d'expert]|Le début se situe le plus souvent entre 3 et 12 mois de vie.",  # N03
"gold|examen|3||[Wilmshurst, Epilepsia, ILAE 2015]|L'EEG de veille et de sommeil se fait en urgence, dans les jours qui suivent la suspicion, pour chercher l'hypsarythmie.",  # N04
"red|piège|2||[avis d'expert]|Les salves de spasmes sont souvent prises pour des coliques, un reflux ou un réflexe de sursaut, ce qui retarde le diagnostic.",  # N05
"bas|mécanisme|1||[avis d'expert]|L'hypsarythmie est une activité EEG de fond désorganisée, de grande amplitude, avec des pointes multifocales.",  # N06
"pos|diagnostic différentiel|2||[avis d'expert]|Les myoclonies bénignes du nourrisson et le frisson (« shuddering ») ressemblent aux spasmes, mais l'EEG reste normal et le développement progresse.",  # N07
"alt|examen|2||[avis d'expert]|L'IRM cérébrale, l'examen de la peau à la lampe de Wood, puis les bilans métabolique et génétique cherchent la cause.",  # N08
"epi|terrain particulier|2||[avis d'expert]|Les causes comprennent l'encéphalopathie anoxo-ischémique, les malformations cérébrales, la sclérose tubéreuse de Bourneville, la trisomie 21 et des causes génétiques ; une part reste sans cause trouvée.",  # N09
"exa|signe|1||[avis d'expert]|Des macules hypomélaniques visibles à la lampe de Wood orientent vers une sclérose tubéreuse de Bourneville.",  # N10
"acu|décision|3||[Wilmshurst, Epilepsia, ILAE 2015]|Le traitement de première ligne repose sur l'hormonothérapie (ACTH ou prednisolone à forte dose) ou sur le vigabatrin.",  # N11
"acu|molécule|2||[Wilmshurst, Epilepsia, ILAE 2015]|Le vigabatrin est le premier choix en cas de sclérose tubéreuse de Bourneville.",  # N12
"acu|décision|2||[O'Callaghan, Lancet Neurol, 2017 (ICISS)]|L'association d'une hormonothérapie et du vigabatrin arrête plus souvent les spasmes que l'hormonothérapie seule.",  # N13
"hos|complication|2||[avis d'expert]|Le vigabatrin peut réduire le champ visuel de façon irréversible ; l'hormonothérapie expose à l'hypertension, à l'hyperglycémie, aux infections et à l'irritabilité.",  # N14
"pro|pronostic|1||[avis d'expert]|La plupart des enfants gardent un retard de développement, et certains évoluent vers d'autres épilepsies, comme le syndrome de Lennox-Gastaut.",  # N15
"pro|pronostic|1||[avis d'expert]|Un diagnostic et un traitement rapides améliorent les chances de développement, surtout quand aucune cause n'est trouvée.",  # N16
"sur|examen|1||[avis d'expert]|Le suivi contrôle l'arrêt des spasmes et la disparition de l'hypsarythmie à l'EEG, ainsi que la pression artérielle et la glycémie sous hormonothérapie.",  # N17
"fol|décision|1||[avis d'expert]|Le neuropédiatre coordonne la prise en charge avec la physiothérapie, l'ergothérapie, la logopédie et le soutien aux parents.",  # N18
"fol|contexte suisse|1|S|[avis d'expert]|En Suisse, l'assurance-invalidité peut prendre en charge certaines épilepsies au titre des infirmités congénitales ; la demande se fait tôt.",  # N19
"def|critère|1||[avis d'expert]|Le terme « spasmes épileptiques » désigne les crises, et le syndrome de West la triade complète.",  # N20
"ana|symptôme|1||[avis d'expert]|Les parents décrivent souvent une perte du sourire, du contact visuel ou de la tenue de tête avant ou avec les spasmes.",  # N21
"chr|décision|1||[avis d'expert]|En cas d'échec des premières lignes, le neuropédiatre discute d'autres antiépileptiques, le régime cétogène ou une chirurgie si une lésion focale est en cause.",  # N22
"red|signe|1||[avis d'expert]|Une régression du développement chez un nourrisson impose une évaluation neuropédiatrique rapide.",  # N23
"ana|examen|1||[avis d'expert]|La vidéo des épisodes filmée par les parents aide beaucoup au diagnostic.",  # N24
"hos|complication|1||[avis d'expert]|Sous hormonothérapie à forte dose, l'enfant reçoit une surveillance des infections et une protection gastrique selon le protocole.",  # N25
"sur|seuil|1||[avis d'expert]|La réponse se juge en quelques semaines ; la persistance des spasmes ou de l'hypsarythmie impose de changer de stratégie.",  # N26
]
ANGLES = [
"Salves de flexions au réveil chez un nourrisson.",
"Spasmes + hypsarythmie + régression.",
"EEG en urgence.",
"Pas des coliques.",
"Hormones ou vigabatrin ; vigabatrin si Bourneville.",
"Vigabatrin : champ visuel.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une fillette de 6 mois, à Lausanne, a depuis 2 semaines des épisodes où elle fléchit brusquement la tête et lève les bras, une dizaine de fois de suite, surtout au réveil. Sa mère pensait à des coliques. Elle ne sourit plus et tient moins bien sa tête.", prompt="Quel diagnostic devez-vous évoquer en premier ?",
 items=["*Des spasmes épileptiques dans le cadre d'un syndrome de West || Les salves en flexion au réveil avec régression l'évoquent.", "Des coliques du nourrisson || Elles ne donnent ni salves de flexions ni régression.", "Un reflux gastro-œsophagien || Il n'explique pas la régression.", "Des myoclonies bénignes du nourrisson || Elles ne s'accompagnent pas de régression.", "Un réflexe de Moro normal || Il disparaît vers 4 à 6 mois et ne donne pas de régression."],
 notions="N02 N03 N05 N21 N01", angle="application", diff=2, ladder=L("Salves au réveil.", "Spasmes épileptiques.", "Flexion, régression.", "Piège des coliques.", "West.", "Coliques.", "Salves + régression."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 2, 4), stem="Vous suspectez une épilepsie du nourrisson.", prompt="Quel examen demandez-vous et dans quel délai ?",
 items=["*Un EEG de veille et de sommeil dans les jours qui viennent || Il cherche l'hypsarythmie et ne doit pas attendre.", "Un EEG dans 3 mois || Le délai nuit au développement.", "Une échographie abdominale || Elle cherche un reflux, pas une épilepsie.", "Un scanner cérébral seul || Il ne remplace pas l'EEG.", "Aucun examen, la clinique suffit || L'EEG est nécessaire."],
 notions="N04 N06 N16", angle="direct", diff=1, ladder=L("Suspicion.", "EEG urgent.", "Nourrisson.", "Délai.", "EEG en jours.", "Dans 3 mois.", "EEG vite."), sources="[Wilmshurst, Epilepsia, ILAE 2015]"),
dict(format="A", serie=("S1", 3, 4), stem="L'EEG montre une hypsarythmie. L'examen à la lampe de Wood révèle 4 macules hypopigmentées.", prompt="Quelle cause évoquez-vous ?",
 items=["*Une sclérose tubéreuse de Bourneville || Les macules hypomélaniques et le syndrome de West l'évoquent.", "Une neurofibromatose de type 1 || Elle donne des taches café au lait.", "Un vitiligo isolé || Il n'explique pas l'épilepsie.", "Une trisomie 21 || Elle a un phénotype propre.", "Une méningite || Rien ne l'évoque."],
 notions="N10 N09 N08", angle="application", diff=2, ladder=L("Macules blanches.", "Bourneville.", "Lampe de Wood.", "Cause.", "Sclérose tubéreuse.", "NF1.", "Taches blanches = Bourneville."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 4, 4), stem="L'IRM confirme des tubers corticaux.", prompt="Quel traitement est le premier choix ?",
 items=["*Le vigabatrin || Il est le premier choix en cas de sclérose tubéreuse.", "Le paracétamol || Il ne traite pas l'épilepsie.", "La carbamazépine || Elle n'est pas un traitement de première ligne des spasmes.", "Une simple surveillance || Les spasmes nécessitent un traitement rapide.", "Un antireflux || Il ne répond pas."],
 notions="N12 N11", angle="application", diff=2, ladder=L("Bourneville.", "Vigabatrin.", "Tubers.", "Premier choix.", "Vigabatrin.", "Carbamazépine.", "Bourneville = vigabatrin."), sources="[Wilmshurst, Epilepsia, ILAE 2015]"),
dict(format="A", stem="Un garçon de 7 mois, né à terme après une asphyxie périnatale, a des salves de contractions en extension et ne suit plus du regard. L'EEG montre une hypsarythmie et l'IRM des lésions anoxiques anciennes.", prompt="Quelle stratégie est la plus efficace pour arrêter les spasmes ?",
 items=["*Une hormonothérapie associée au vigabatrin || L'association arrête plus souvent les spasmes que les hormones seules.", "Une simple surveillance || Le traitement doit être rapide.", "Une benzodiazépine orale seule au long cours || Elle n'est pas un traitement de première ligne.", "Une carbamazépine || Elle n'est pas indiquée.", "Une chirurgie d'emblée || Elle n'est pas la première ligne."],
 notions="N13 N11 N09", angle="application", diff=3, ladder=L("Hypsarythmie post-asphyxie.", "Traitement.", "Sans Bourneville.", "Stratégie.", "Hormones + vigabatrin.", "Surveillance.", "ICISS : association."), sources="[O'Callaghan, Lancet Neurol, 2017]"),
dict(format="A", stem="Une enfant traitée par vigabatrin depuis plusieurs mois va bien.", prompt="Quel effet indésirable surveillez-vous en particulier ?",
 items=["*Un rétrécissement irréversible du champ visuel || C'est l'effet propre du vigabatrin.", "Une hypothyroïdie || Elle n'est pas typique.", "Une ototoxicité || Elle n'est pas typique.", "Une hépatite fulminante || Elle évoque plutôt le valproate.", "Une alopécie définitive || Elle n'est pas typique."],
 notions="N14 N17", angle="direct", diff=2, ladder=L("Vigabatrin.", "Champ visuel.", "Traitement prolongé.", "Effet.", "Champ visuel.", "Hépatite.", "Vigabatrin = vision."), sources="[avis d'expert]"),
dict(format="A", stem="Un nourrisson de 5 mois reçoit de la prednisolone à forte dose pour des spasmes épileptiques.", prompt="Quelle surveillance s'impose ?",
 items=["*Pression artérielle, glycémie, signes d'infection et irritabilité || L'hormonothérapie les expose.", "Champ visuel uniquement || Il concerne le vigabatrin.", "Audiogramme mensuel || Il n'est pas utile.", "Aucune surveillance particulière || Les effets indésirables sont fréquents.", "Densitométrie osseuse hebdomadaire || Elle n'est pas utile."],
 notions="N14 N25 N17", angle="application", diff=2, ladder=L("Prednisolone.", "Effets.", "Forte dose.", "Surveillance.", "PA, glycémie, infections.", "Champ visuel.", "Corticoïde = PA, sucre, infection."), sources="[avis d'expert]"),
dict(format="A", stem="Un nourrisson de 4 mois a des secousses brèves des membres seulement pendant les repas, sans changement de son développement ; l'EEG pendant les épisodes est normal.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Des myoclonies bénignes non épileptiques du nourrisson || L'EEG normal et le développement normal les caractérisent.", "Un syndrome de West || L'EEG serait anormal.", "Un état de mal épileptique || L'EEG serait anormal.", "Une hypocalcémie grave || Le contexte ne l'évoque pas.", "Une méningite || Rien ne l'évoque."],
 notions="N07 N04", angle="piège", diff=3, ladder=L("Secousses au repas.", "Bénin.", "EEG normal.", "Discriminant.", "Myoclonies bénignes.", "West.", "EEG normal + développe = bénin."), sources="[avis d'expert]"),
dict(format="A", stem="Une mère consulte pour son fils de 8 mois qui « se plie en deux » plusieurs fois de suite au réveil depuis 10 jours. Le pédiatre précédent a conclu à des coliques.", prompt="Quelle démarche est la plus juste ?",
 items=["*Demander une vidéo des épisodes et un EEG rapide, sans retenir les coliques sur ce tableau || Les salves au réveil évoquent des spasmes.", "Confirmer les coliques et rassurer || L'âge et les salves ne cadrent pas.", "Changer de lait || Il ne répond pas.", "Prescrire un antireflux || Il ne répond pas.", "Revoir l'enfant dans 3 mois || Le délai nuit au développement."],
 notions="N05 N24 N04", angle="piège", diff=2, ladder=L("Plié en deux.", "Piège des coliques.", "Salves au réveil.", "Démarche.", "Vidéo et EEG.", "Coliques.", "Salves = EEG."), sources="[avis d'expert]"),
dict(format="A", stem="Chez un nourrisson avec hypsarythmie, l'IRM et l'examen cutané sont normaux.", prompt="Quelle étape suivante proposez-vous pour chercher une cause ?",
 items=["*Des bilans métabolique et génétique || Une part des causes est génétique ou métabolique.", "Aucune recherche supplémentaire || Une cause traitable peut exister.", "Une coloscopie || Elle ne répond pas.", "Une biopsie musculaire systématique || Elle n'est pas systématique.", "Un scanner thoracique || Il ne répond pas."],
 notions="N08 N09", angle="direct", diff=2, ladder=L("IRM normale.", "Cause.", "Peau normale.", "Étape.", "Métabolique, génétique.", "Rien.", "Chercher génétique."), sources="[avis d'expert]"),
dict(format="A", stem="Après 3 semaines de traitement de première ligne, un enfant a toujours des salves quotidiennes et l'EEG montre encore une hypsarythmie.", prompt="Quelle conduite proposez-vous ?",
 items=["*Changer de stratégie avec le neuropédiatre (autre première ligne, association, puis options de deuxième ligne) || La persistance impose d'agir vite.", "Poursuivre sans changement pendant 6 mois || Le délai nuit au développement.", "Arrêter tout traitement || Les spasmes persistent.", "Ajouter un antireflux || Il ne répond pas.", "Conclure à un échec définitif || D'autres options existent."],
 notions="N26 N22 N16", angle="application", diff=3, ladder=L("Échec.", "Changer.", "3 semaines.", "Conduite.", "Autre stratégie.", "Poursuivre.", "Échec = changer vite."), sources="[avis d'expert]"),
dict(format="A", stem="Les parents d'un enfant de 10 mois traité pour des spasmes épileptiques demandent ce qui l'attend.", prompt="Quelle information est la plus juste ?",
 items=["*Un retard de développement est fréquent et d'autres épilepsies peuvent apparaître, mais un traitement rapide améliore les chances || Le pronostic dépend de la cause et de la rapidité.", "La guérison complète est certaine || Elle ne l'est pas.", "Le pronostic est toujours désespéré || Certains enfants évoluent bien.", "Le développement ne sera jamais touché || Il l'est souvent.", "Le pronostic ne dépend pas de la cause || La cause compte beaucoup."],
 notions="N15 N16", angle="direct", diff=2, ladder=L("Avenir.", "Pronostic.", "Parents.", "Information.", "Retard fréquent, rapidité utile.", "Guérison certaine.", "Cause et vitesse."), sources="[avis d'expert]"),
dict(format="A", stem="Une famille vaudoise demande quelles aides existent pour leur enfant atteint d'une épilepsie du nourrisson avec retard de développement.", prompt="Quelle réponse est la plus juste ?",
 items=["*L'assurance-invalidité peut prendre en charge certaines épilepsies au titre des infirmités congénitales, et une demande précoce est utile || C'est une particularité suisse.", "Aucune aide n'existe en Suisse || C'est faux.", "Seule l'assurance complémentaire paie || L'AI peut intervenir.", "Il faut attendre la scolarité pour demander || La demande se fait tôt.", "L'employeur des parents paie les thérapies || Ce n'est pas son rôle."],
 notions="N19 N18", angle="application", diff=2, ladder=L("Aides.", "AI.", "Famille vaudoise.", "Cadre suisse.", "Infirmité congénitale.", "Aucune aide.", "AI tôt."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un étudiant révise le syndrome de West.", prompt="Quelle triade le définit ?",
 items=["*Spasmes épileptiques, hypsarythmie et arrêt ou régression du développement || C'est la triade.", "Absences, pointes-ondes à 3 Hz et développement normal || C'est l'épilepsie-absences.", "Crises toniques, pointes-ondes lentes et déficience intellectuelle || C'est le syndrome de Lennox-Gastaut.", "Convulsions fébriles, EEG normal et développement normal || Ce sont des convulsions fébriles.", "Myoclonies au réveil, polypointes et adolescence || C'est l'épilepsie myoclonique juvénile."],
 notions="N01 N20 N06", angle="direct", diff=1, ladder=L("Triade.", "West.", "Spasmes, EEG, développement.", "Définition.", "Spasmes + hypsarythmie + régression.", "Lennox-Gastaut.", "Trois éléments."), sources="[Wilmshurst, Epilepsia, ILAE 2015]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez le traitement du syndrome de West.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'ACTH ou la prednisolone à forte dose sont des traitements de première ligne. || C'est la recommandation.", "V: Le vigabatrin est le premier choix en cas de sclérose tubéreuse. || Il y est particulièrement efficace.", "F: La carbamazépine est le traitement de référence. || Elle n'est pas indiquée.", "F: L'association hormones et vigabatrin est moins efficace que les hormones seules. || Elle arrête plus souvent les spasmes."],
 notions="N11 N12 N13", angle="direct", diff=2, ladder=L("Révision.", "Traitement.", "Hormones, vigabatrin.", "Pièges.", "Première ligne.", "Carbamazépine.", "Hormones ou vigabatrin."), sources="[O'Callaghan, Lancet Neurol, 2017]"),
dict(format="Kprim", stem="Une pédiatre de garde reçoit un nourrisson de 6 mois avec des salves de flexions au réveil.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un EEG doit se faire dans les jours qui viennent. || Le délai compte.", "V: Une vidéo des épisodes aide au diagnostic. || Elle montre les salves.", "F: Des coliques expliquent le mieux ce tableau. || Les salves au réveil évoquent des spasmes.", "F: Un développement en régression est rassurant. || Il est inquiétant."],
 notions="N04 N24 N05 N23", angle="application", diff=2, ladder=L("Garde.", "Démarche.", "Salves au réveil.", "Pièges.", "EEG vite, vidéo.", "Coliques.", "Ne pas attendre."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Un enfant de 9 mois est traité pour des spasmes épileptiques.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le vigabatrin peut réduire le champ visuel. || C'est un effet connu.", "V: La prednisolone à forte dose peut élever la pression artérielle. || Elle l'expose.", "F: L'hypsarythmie persistante n'a pas d'importance si les salves diminuent. || Elle impose de réévaluer.", "F: Les effets indésirables des hormones sont rares. || Ils sont fréquents."],
 notions="N14 N26 N17", angle="piège", diff=2, ladder=L("Traitement.", "Effets, suivi.", "Vigabatrin, prednisolone.", "Pièges.", "Vision, PA, EEG.", "Hypsarythmie sans importance.", "EEG aussi."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Des internes discutent des causes du syndrome de West.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La sclérose tubéreuse de Bourneville en est une cause. || Elle est classique.", "V: L'encéphalopathie anoxo-ischémique en est une cause. || Elle est fréquente.", "F: Une cause est toujours trouvée. || Une part reste sans cause.", "F: L'IRM cérébrale est inutile. || Elle cherche une lésion."],
 notions="N09 N08 N10", angle="piège", diff=2, ladder=L("Causes.", "Étiologie.", "Bourneville, anoxie.", "Pièges.", "Structurelles, génétiques.", "Toujours trouvée.", "Chercher par IRM."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un nourrisson de 7 mois a des salves de contractions brèves au réveil.", prompt="Choisissez les TROIS éléments qui orientent vers un syndrome de West.",
 items=["*Hypsarythmie à l'EEG || Elle fait partie de la triade.", "*Perte du sourire et du contact visuel || Elle traduit la régression.", "*Salves répétées au réveil || Elles sont typiques des spasmes.", "Fièvre élevée || Elle évoque une autre cause.", "EEG normal pendant les épisodes || Il oriente vers un trouble bénin.", "Développement qui progresse normalement || Il ne cadre pas.", "Épisodes seulement pendant les repas || Ils évoquent un trouble bénin.", "Pleurs du soir soulagés par le portage || Ils évoquent des coliques.", "Régurgitations après le biberon || Elles évoquent un reflux.", "Diarrhée || Elle n'oriente pas.", "Toux || Elle n'oriente pas.", "Éruption cutanée fébrile || Elle n'oriente pas."],
 notions="N01 N02 N21 N03 N07", angle="direct", diff=2, ladder=L("Salves.", "Triade.", "EEG, régression.", "Lesquels.", "Hypsarythmie, régression, salves.", "Fièvre.", "Triade."), sources="[Wilmshurst, Epilepsia, ILAE 2015]"),
dict(format="MenuLong", stem="Un nourrisson a une hypsarythmie confirmée.", prompt="Choisissez les TROIS examens utiles pour chercher la cause.",
 items=["*IRM cérébrale || Elle cherche une lésion structurelle.", "*Examen cutané à la lampe de Wood || Il cherche des macules de Bourneville.", "*Bilan génétique || Une part des causes est génétique.", "Coloscopie || Elle ne répond pas.", "Spirométrie || Elle ne répond pas.", "Échographie du genou || Elle ne répond pas.", "Densitométrie osseuse || Elle ne répond pas.", "Test d'effort || Il ne répond pas.", "Audiogramme isolé || Il ne cherche pas la cause.", "Radiographie du thorax || Elle ne répond pas.", "Dosage du PSA || Il ne répond pas.", "Mammographie || Elle ne répond pas."],
 notions="N08 N10 N09", angle="application", diff=1, ladder=L("Hypsarythmie.", "Cause.", "IRM, peau, gènes.", "Lesquels.", "IRM, Wood, génétique.", "Coloscopie.", "Image, peau, gènes."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Syndrome de West : reconnaître les salves de spasmes au réveil derrière de fausses « coliques », faire l'EEG en urgence (hypsarythmie), chercher la cause (IRM, lampe de Wood, génétique) et traiter vite par hormones ou vigabatrin, au mieux associés",
 notions=[
  dict(titre="Reconnaître", rub=["def", "ana", "epi", "red"], comment="Pose la triade et déjoue le piège des coliques.",
   tableau=(["Élément", "Contenu", "Pourquoi"], [
     ["Spasmes", "Salves de flexions ou extensions au réveil", "Signe clinique clé"],
     ["Hypsarythmie", _T("EEG désorganisé", "Fond de grande amplitude avec pointes multifocales."), "Signe EEG clé"],
     ["Développement", "Arrêt ou régression", "Troisième élément"],
     ["Âge", "3 à 12 mois le plus souvent", "Terrain"]]),
   points=["Les coliques, le reflux et le sursaut retardent souvent le diagnostic."], sources=["[Wilmshurst, Epilepsia, ILAE 2015]"]),
  dict(titre="Explorer", rub=["gold", "alt", "exa", "pos"], comment="Confirme vite et cherche la cause.",
   arbre=[("e1", None, "Salves suspectes", "Vidéo et EEG en urgence."),
          ("e2", "e1", "EEG normal, développement normal", "Myoclonies bénignes ou frisson."),
          ("e3", "e1", "Hypsarythmie", "IRM, lampe de Wood, métabolique, génétique.", "west"),
          ("e4", "e3", "Macules hypomélaniques", "Sclérose tubéreuse de Bourneville.", "west")],
   points=["L'IRM et l'examen cutané viennent en premier."], sources=["[avis d'expert]"]),
  dict(titre="Traiter", rub=["acu", "chr", "hos"], comment="Traite vite et surveille les effets indésirables.",
   tableau=(["Situation", "Traitement", "Source"], [
     ["Cas général", "ACTH ou prednisolone forte dose, ou vigabatrin", "[Wilmshurst, ILAE 2015]"],
     ["Sclérose tubéreuse", "Vigabatrin", "[Wilmshurst, ILAE 2015]"],
     ["Arrêt plus fréquent", "Hormones + vigabatrin", "[O'Callaghan, ICISS 2017]"],
     ["Échec", "Autres antiépileptiques, régime cétogène, chirurgie si lésion", "[avis d'expert]"]]),
   points=["Vigabatrin : champ visuel ; hormones : PA, glycémie, infections."], sources=["[O'Callaghan, Lancet Neurol, 2017]"]),
  dict(titre="Suivi et réseau", rub=["pro", "sur", "fol", "bas"], comment="Mesure la réponse et accompagne la famille.",
   tableau=(["Élément", "Conduite", "Pourquoi"], [
     ["Spasmes et EEG", "Contrôle en quelques semaines", "Changer vite si échec"],
     ["Développement", "Thérapies précoces", "Retard fréquent"],
     ["Assurance-invalidité", "Demande précoce", "Particularité suisse"]]),
   points=["Un traitement rapide améliore les chances de développement."], sources=["[avis d'expert]"]),
 ],
 ssp=dict(code="O2.5", nom="Retard du développement", officiel=True, algorithme=[
  ("n1", None, "Nourrisson avec régression du développement", "Le médecin cherche des crises et des salves."),
  ("n2", "n1", "Salves de flexions au réveil", "EEG en urgence.", "west", "c2"),
  ("n3", "n2", "Hypsarythmie", "Syndrome de West : bilan de cause et traitement.", "west", "c3"),
  ("n4", "n2", "EEG normal, développement normal", "Trouble bénin.", None, "c2"),
  ("n5", "n3", "Macules hypomélaniques", "Bourneville : vigabatrin.", "west", "c3"),
  ("n6", "n1", "Pas de crise", "Bilan du retard selon la cause.", None, "c1")]),
 pec=[
  dict(cle="west", titre="Syndrome de West (spasmes épileptiques du nourrisson)",
   but=["Arrêter les spasmes et l'hypsarythmie au plus vite.", "Préserver le développement.", "Traiter la cause."],
   moyens=dict(accueil=["Demander une vidéo des épisodes.", "Organiser l'EEG en urgence.", "Informer et soutenir les parents."],
    pharma=[("Prednisolone à forte dose ou ACTH", "Schéma et posologie selon le neuropédiatre et l'AIPS.", "Hormonothérapie de première ligne.", "[Wilmshurst, Epilepsia, ILAE 2015]"),
            ("Vigabatrin", "Posologie à vérifier dans l'AIPS.", "Première ligne, premier choix si Bourneville.", "[Wilmshurst, Epilepsia, ILAE 2015]")],
    nonpharma=[("rééducation", "Physiothérapie, ergothérapie et logopédie précoces.", "Elles soutiennent le développement."),
               ("éducation thérapeutique", "Reconnaissance des salves et des effets indésirables.", "Elle permet d'agir vite."),
               ("social et assurances", "Demande précoce à l'assurance-invalidité.", "Elle finance les thérapies.")],
    transversal=[("Neuropédiatrie", "Elle conduit le traitement."), ("Ophtalmologie", "Elle surveille le champ visuel sous vigabatrin."), ("Génétique médicale", "Elle cherche la cause.")]),
   urgence=None,
   horsUrgence=(["EEG et traitement dans les jours qui suivent la suspicion.", "Bilan de cause en parallèle."],
            [("d'abord", "pédiatre", "Suspecte les spasmes et adresse sans délai."),
             ("ensuite", "neuropédiatre", "Confirme par EEG et débute le traitement."),
             ("en même temps", "neuropédiatre", "Organise IRM, lampe de Wood et bilans."),
             ("puis", "équipe de rééducation", "Soutient le développement.")]),
   pronostic="Le retard de développement est fréquent ; la rapidité du traitement et la cause déterminent l'évolution.",
   suivi=[("Spasmes", "Quotidiennement par les parents", "Disparus"), ("EEG", "Après quelques semaines", "Sans hypsarythmie"), ("PA et glycémie sous hormones", "Régulièrement", "Normales")],
   sortie="Le suivi neuropédiatrique se poursuit au long cours.",
   prevention=["Elle repose sur la reconnaissance rapide des salves.", "Elle évite les retards d'EEG.", "Elle dépiste les effets visuels du vigabatrin."]),
 ])
AVERIFIER = ["Schémas et posologies de la prednisolone, de l'ACTH et du vigabatrin à vérifier dans l'AIPS et les protocoles neuropédiatriques.", "Disponibilité de l'ACTH (tétracosactide dépôt) en Suisse à vérifier.", "Prise en charge AI au titre des infirmités congénitales (liste OIC) à vérifier pour chaque situation."]
