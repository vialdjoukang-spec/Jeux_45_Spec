ID = "G25.8__G11-E04"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[Allen, Sleep Med, IRLSSG 2014]|Le diagnostic exige 5 critères : un besoin impérieux de bouger les jambes, souvent avec une sensation désagréable ; un début ou une aggravation au repos ; un soulagement par le mouvement ; une aggravation le soir ou la nuit ; l'absence d'autre affection qui l'explique mieux.",  # N01
"ana|symptôme|2||[avis d'expert]|Le patient décrit une gêne profonde des mollets, des fourmillements ou des tiraillements, qui l'obligent à se lever et à marcher le soir.",  # N02
"pos|diagnostic différentiel|2||[Allen, Sleep Med, IRLSSG 2014]|Les crampes, l'inconfort de position, les œdèmes, la neuropathie et l'akathisie imitent le trouble et doivent être écartés (5e critère).",  # N03
"bas|mécanisme|1||[avis d'expert]|Une carence cérébrale en fer et une dysfonction dopaminergique sous-tendent le trouble, ce qui explique l'effet du fer et l'aggravation par les antidopaminergiques.",  # N04
"epi|terrain particulier|2||[Winkelman, J Clin Sleep Med, AASM 2024 ; avis d'expert]|La carence martiale, la grossesse, l'insuffisance rénale terminale et la neuropathie favorisent le trouble.",  # N05
"gold|examen|3||[Winkelman, J Clin Sleep Med, AASM 2024]|Le bilan martial (ferritine et saturation de la transferrine) se fait chez tout patient gêné, idéalement le matin et sans supplément de fer depuis 24 heures.",  # N06
"acu|décision|2||[Winkelman, J Clin Sleep Med, AASM 2024]|La première étape corrige les facteurs aggravants : alcool, caféine, antihistaminiques, médicaments sérotoninergiques et antidopaminergiques, apnées du sommeil non traitées.",  # N07
"chr|seuil|2||[Winkelman, J Clin Sleep Med, AASM 2024]|Le fer se propose si la ferritine est ≤ 75 µg/l ou la saturation de la transferrine < 20 % ; entre 75 et 100 µg/l, seul le fer intraveineux se discute.",  # N08
"chr|molécule|2||[Winkelman, J Clin Sleep Med, AASM 2024]|La gabapentine, la prégabaline et le carboxymaltose ferrique intraveineux reçoivent une recommandation forte.",  # N09
"chr|piège|2||[Winkelman, J Clin Sleep Med, AASM 2024]|Les agonistes dopaminergiques (pramipexole, ropinirole, rotigotine) et la lévodopa ne sont plus recommandés en usage standard, à cause du risque d'augmentation à long terme.",  # N10
"hos|complication|2||[Winkelman, J Clin Sleep Med, AASM 2024]|L'augmentation est une aggravation induite par le traitement dopaminergique : les symptômes débutent plus tôt, s'étendent aux bras et deviennent plus intenses.",  # N11
"chr|molécule|1||[Winkelman, J Clin Sleep Med, AASM 2024]|Les opioïdes, comme l'oxycodone à libération prolongée, peuvent se discuter dans les formes réfractaires, avec prudence.",  # N12
"alt|examen|1||[avis d'expert]|La polysomnographie n'est pas nécessaire au diagnostic ; elle montre souvent des mouvements périodiques des jambes.",  # N13
"exa|signe|1||[avis d'expert]|L'examen neurologique est normal dans la forme primaire ; il cherche une neuropathie ou une radiculopathie associée.",  # N14
"red|piège|1||[avis d'expert]|L'akathisie sous neuroleptique donne une agitation intérieure de tout le corps, sans rythme vespéral ni lien avec le repos.",  # N15
"ana|symptôme|1||[avis d'expert]|Le trouble retarde l'endormissement, fragmente le sommeil et cause une fatigue diurne.",  # N16
"epi|chiffre|1||[avis d'expert]|La fréquence augmente avec l'âge et le trouble touche davantage les femmes.",  # N17
"pro|pronostic|1||[avis d'expert]|La forme liée à la grossesse disparaît le plus souvent après l'accouchement.",  # N18
"sur|examen|1||[Winkelman, J Clin Sleep Med, AASM 2024]|Le médecin recontrôle régulièrement le bilan martial chez les patients gênés.",  # N19
"fol|décision|1||[avis d'expert]|Une forme réfractaire ou une augmentation conduit vers un neurologue ou un centre du sommeil.",  # N20
"fol|contexte suisse|1|S|[avis d'expert]|En Suisse, l'indication et le remboursement du fer intraveineux dans ce trouble se vérifient dans l'AIPS et la Liste des spécialités.",  # N21
"acu|décision|1||[Winkelman, J Clin Sleep Med, AASM 2024 ; avis d'expert]|L'activité physique modérée, les étirements et des horaires de sommeil réguliers aident ; la stimulation bilatérale du nerf péronier reçoit une recommandation conditionnelle.",  # N22
"def|critère|1||[avis d'expert]|Le diagnostic est clinique : aucun examen ne le confirme.",  # N23
"chr|piège|1||[Winkelman, J Clin Sleep Med, AASM 2024]|Le clonazépam, le valproate, la carbamazépine et le bupropion ne sont pas recommandés.",  # N24
"chr|molécule|1||[Winkelman, J Clin Sleep Med, AASM 2024]|En insuffisance rénale terminale, la gabapentine, le fer saccharose intraveineux et la vitamine C peuvent se discuter.",  # N25
"pos|critère|1||[Allen, Sleep Med, IRLSSG 2014]|Une histoire familiale et des mouvements périodiques des jambes soutiennent le diagnostic.",  # N26
]
ANGLES = [
"Besoin de bouger, repos, soulagé en marchant, soir.",
"Ferritine et saturation le matin.",
"Ferritine ≤ 75 : fer.",
"Gabapentinoïdes et fer IV d'abord.",
"Agonistes dopaminergiques : augmentation.",
"Antihistaminique, ISRS, neuroleptique aggravent.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une comptable de 52 ans, à Delémont, se plaint depuis un an de ne pas pouvoir rester assise le soir devant la télévision : une gêne profonde des mollets l'oblige à se lever et à marcher, ce qui la soulage. Elle s'endort tard.", prompt="Quel diagnostic évoquez-vous en premier ?",
 items=["*Un syndrome de Willis-Ekbom || Le besoin de bouger au repos, soulagé par la marche, le soir, le caractérise.", "Des crampes nocturnes || Elles sont douloureuses, brèves, avec contraction palpable.", "Une artériopathie || Elle donne une douleur à la marche.", "Une insomnie psychophysiologique isolée || Elle ne donne pas de gêne des jambes.", "Une polyneuropathie || Elle ne s'améliore pas en marchant."],
 notions="N01 N02 N16", angle="application", diff=1, ladder=L("Gêne des jambes le soir.", "Willis-Ekbom.", "Soulagée par la marche.", "Critères.", "Willis-Ekbom.", "Crampes.", "Repos-soir-marche."), sources="[Allen, Sleep Med, IRLSSG 2014]"),
dict(format="A", serie=("S1", 2, 4), stem="Vous voulez compléter le bilan.", prompt="Quel examen demandez-vous en premier ?",
 items=["*Ferritine et saturation de la transferrine, le matin, sans supplément de fer depuis 24 heures || La carence martiale est la cause curable principale.", "Une polysomnographie || Elle n'est pas nécessaire au diagnostic.", "Une IRM lombaire || Rien ne l'indique.", "Un EEG || Il ne répond pas.", "Un dosage des CK || Il ne répond pas."],
 notions="N06 N13 N23", angle="direct", diff=1, ladder=L("Bilan.", "Bilan martial.", "Ferritine.", "Examen.", "Ferritine et saturation.", "Polysomnographie.", "Fer d'abord."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="A", serie=("S1", 3, 4), stem="La ferritine est à 42 µg/l et la saturation de la transferrine à 17 %.", prompt="Quelle conduite proposez-vous ?",
 items=["*Une supplémentation en fer, orale ou intraveineuse, et une recherche de la cause de la carence || Les seuils de traitement sont atteints.", "Aucun fer, car la ferritine est dans la norme du laboratoire || Le seuil pour ce trouble est plus élevé.", "Un agoniste dopaminergique d'emblée || Il expose à l'augmentation.", "Une benzodiazépine || Elle n'est pas recommandée.", "Une polysomnographie avant tout traitement || Elle n'est pas nécessaire."],
 notions="N08 N10 N05", angle="piège", diff=2, ladder=L("Ferritine 42.", "Fer.", "≤ 75.", "Seuil.", "Supplémenter.", "Norme du labo.", "≤ 75 = fer."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="A", serie=("S1", 4, 4), stem="Trois mois plus tard, la ferritine est à 120 µg/l, mais les symptômes la gênent encore 5 soirs par semaine.", prompt="Quel traitement proposez-vous ?",
 items=["*Un gabapentinoïde (gabapentine ou prégabaline) le soir || Il reçoit une recommandation forte.", "Le pramipexole au long cours || Il n'est plus recommandé en usage standard.", "Le clonazépam || Il n'est pas recommandé.", "Un antihistaminique sédatif || Il aggrave le trouble.", "Une nouvelle cure de fer || La ferritine dépasse les seuils."],
 notions="N09 N10 N24 N07", angle="application", diff=2, ladder=L("Fer corrigé.", "Gabapentinoïde.", "Ferritine 120.", "Choix.", "Gabapentinoïde.", "Pramipexole.", "Fer puis α2δ."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="A", stem="Un homme de 68 ans prend du ropinirole depuis 4 ans. Ses symptômes commencent maintenant en début d'après-midi, touchent aussi les bras et sont plus intenses malgré des doses croissantes.", prompt="Quel phénomène évoquez-vous ?",
 items=["*Une augmentation induite par le traitement dopaminergique || L'avance horaire, l'extension aux bras et l'intensité la définissent.", "Une simple tolérance qui impose d'augmenter la dose || Augmenter aggrave l'augmentation.", "Une maladie de Parkinson débutante || Le tableau est sensitif et circadien.", "Une polyneuropathie || Elle ne s'étend pas selon l'horaire.", "Un effet placebo inversé || Ce n'est pas un concept retenu."],
 notions="N11 N10", angle="direct", diff=2, ladder=L("Aggravation sous ropinirole.", "Augmentation.", "Plus tôt, bras.", "Définition.", "Augmentation.", "Tolérance.", "Plus tôt, plus loin, plus fort."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="A", stem="Chez ce patient, que faire du ropinirole ?", prompt="Quelle conduite est la plus juste ?",
 items=["*Vérifier le fer, puis passer progressivement à un gabapentinoïde avec l'avis d'un spécialiste || Il faut sortir du dopaminergique.", "Doubler la dose du ropinirole || Cela aggrave l'augmentation.", "Ajouter un second agoniste dopaminergique || Cela aggrave l'augmentation.", "Ajouter un neuroleptique sédatif || Il aggrave le trouble.", "Ne rien changer || L'augmentation progresse."],
 notions="N11 N20 N09", angle="application", diff=3, ladder=L("Augmentation.", "Conduite.", "Ropinirole.", "Changement.", "Fer, gabapentinoïde, spécialiste.", "Doubler.", "Sortir du dopaminergique."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="A", stem="Une femme de 45 ans voit ses symptômes de jambes le soir s'aggraver depuis le début d'un traitement pour une dépression. Elle prend aussi un antihistaminique le soir pour dormir.", prompt="Quelle mesure proposez-vous en premier ?",
 items=["*Revoir les médicaments aggravants, antidépresseur sérotoninergique et antihistaminique || La correction des facteurs aggravants est la première étape.", "Ajouter un agoniste dopaminergique || Il expose à l'augmentation.", "Augmenter l'antihistaminique || Il aggrave le trouble.", "Ajouter de la caféine le soir || Elle aggrave le trouble.", "Une IRM cérébrale || Rien ne l'indique."],
 notions="N07 N04", angle="piège", diff=2, ladder=L("Aggravation sous traitement.", "Médicaments.", "ISRS, antihistaminique.", "Première étape.", "Revoir les médicaments.", "Ajouter un dopaminergique.", "Aggravants d'abord."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="A", stem="Un homme de 39 ans traité par halopéridol décrit une impossibilité de rester en place, une agitation intérieure de tout le corps, à toute heure de la journée.", prompt="Quel diagnostic évoquez-vous ?",
 items=["*Une akathisie || L'agitation intérieure diffuse, non vespérale, sous neuroleptique la caractérise.", "Un syndrome de Willis-Ekbom || Il prédomine aux jambes, au repos, le soir.", "Un trouble anxieux généralisé isolé || Le lien avec le neuroleptique l'oriente ailleurs.", "Une crise épileptique || Rien ne l'évoque.", "Une hyperthyroïdie || Le contexte médicamenteux l'oriente ailleurs."],
 notions="N15 N03", angle="piège", diff=2, ladder=L("Agitation sous neuroleptique.", "Akathisie.", "Tout le corps, toute la journée.", "Discriminant.", "Akathisie.", "Willis-Ekbom.", "Diffus, diurne = akathisie."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 70 ans a des douleurs nocturnes brèves, très intenses, du mollet, qui durcit et se contracte ; l'étirement du pied le soulage.", prompt="Quel diagnostic évoquez-vous ?",
 items=["*Des crampes nocturnes || La contraction douloureuse et palpable, soulagée par l'étirement, les caractérise.", "Un syndrome de Willis-Ekbom || Il ne donne pas de contraction musculaire.", "Une thrombose veineuse profonde || Elle donne une douleur continue.", "Une sciatique || Elle suit un trajet radiculaire.", "Une akathisie || Elle est diffuse."],
 notions="N03 N01", angle="piège", diff=2, ladder=L("Douleur du mollet.", "Crampe.", "Contraction palpable.", "Discriminant.", "Crampe.", "Willis-Ekbom.", "Contraction = crampe."), sources="[Allen, Sleep Med, IRLSSG 2014]"),
dict(format="A", stem="Une femme enceinte de 32 semaines a depuis 1 mois un besoin de bouger les jambes le soir, qui la soulage quand elle marche.", prompt="Quelle conduite proposez-vous ?",
 items=["*Contrôler la ferritine, corriger une carence et la rassurer sur une régression habituelle après l'accouchement || La grossesse et la carence favorisent le trouble.", "Prescrire un agoniste dopaminergique || Il n'est pas le premier choix.", "Prescrire un antihistaminique sédatif || Il aggrave le trouble.", "Provoquer l'accouchement || Rien ne le justifie.", "Une polysomnographie urgente || Elle n'est pas nécessaire."],
 notions="N05 N18 N08", angle="application", diff=2, ladder=L("Grossesse.", "Carence, régression.", "32 semaines.", "Conduite.", "Ferritine, rassurer.", "Dopaminergique.", "Grossesse = fer et patience."), sources="[avis d'expert]"),
dict(format="A", stem="Un patient de 66 ans en hémodialyse décrit une gêne des mollets quand il est assis le soir, soulagée par la marche. Sa ferritine est à 150 µg/l et sa saturation de la transferrine à 15 %.", prompt="Quelle option peut se discuter ?",
 items=["*Le fer saccharose intraveineux, la gabapentine à dose adaptée ou la vitamine C || Ce sont les options suggérées en insuffisance rénale terminale.", "La rotigotine || Elle est déconseillée dans ce contexte.", "La lévodopa au long cours || Elle est déconseillée.", "Le valproate || Il n'est pas recommandé.", "Aucune option n'existe en dialyse || Plusieurs options existent."],
 notions="N25 N05", angle="application", diff=3, ladder=L("Dialyse.", "Options spécifiques.", "Saturation 15 %.", "Choix.", "Fer saccharose, gabapentine, vitamine C.", "Rotigotine.", "Dialyse : fer IV et gabapentine."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="A", stem="Un homme de 56 ans ronfle fort, se réveille fatigué et décrit en plus des impatiences des jambes le soir. Son épouse a remarqué des pauses respiratoires.", prompt="Quelle démarche est la plus juste ?",
 items=["*Chercher et traiter des apnées du sommeil, qui aggravent le trouble || Elles font partie des facteurs aggravants.", "Prescrire un agoniste dopaminergique d'emblée || Il expose à l'augmentation.", "Prescrire une benzodiazépine || Elle aggrave les apnées.", "Ignorer le ronflement || Les apnées aggravent le trouble.", "Prescrire un antihistaminique sédatif || Il aggrave le trouble."],
 notions="N07 N13", angle="application", diff=2, ladder=L("Ronflement.", "Apnées.", "Pauses respiratoires.", "Facteur aggravant.", "Chercher les apnées.", "Benzodiazépine.", "Apnées aggravent."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(masque=False, sit="monographique", format="A", stem="Un interne révise les critères IRLSSG du syndrome des jambes sans repos.", prompt="Quel élément fait partie des critères essentiels ?",
 items=["*Une aggravation le soir ou la nuit || C'est l'un des 5 critères.", "Une ferritine basse || Elle n'est pas un critère.", "Des mouvements périodiques à la polysomnographie || Ils soutiennent sans être exigés.", "Une histoire familiale || Elle soutient sans être exigée.", "Une réponse à la lévodopa || Elle n'est pas exigée."],
 notions="N01 N26 N23 N02", angle="direct", diff=2, ladder=L("Critères.", "Essentiels.", "Soir.", "Distinction.", "Rythme vespéral.", "Ferritine.", "5 critères cliniques."), sources="[Allen, Sleep Med, IRLSSG 2014]"),
dict(format="A", stem="Malgré un fer corrigé et une prégabaline bien conduite, un patient de 71 ans dort 3 heures par nuit à cause de ses jambes.", prompt="Quelle option peut se discuter avec un spécialiste ?",
 items=["*Un opioïde à faible dose, comme l'oxycodone à libération prolongée, avec prudence || Il est une option des formes réfractaires.", "Le clonazépam au long cours || Il n'est pas recommandé.", "Un neuroleptique sédatif || Il aggrave le trouble.", "Un antihistaminique || Il aggrave le trouble.", "Le valproate || Il n'est pas recommandé."],
 notions="N12 N20 N24", angle="application", diff=3, ladder=L("Réfractaire.", "Opioïde.", "Fer et prégabaline.", "Option.", "Oxycodone LP.", "Clonazépam.", "Réfractaire = opioïde prudent."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez la recommandation AASM 2024 sur le syndrome des jambes sans repos.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La gabapentine et la prégabaline reçoivent une recommandation forte. || Elles sont en tête.", "V: Le carboxymaltose ferrique intraveineux reçoit une recommandation forte. || Si le bilan martial le permet.", "F: Le pramipexole reste le traitement standard de première intention. || Il est déconseillé en usage standard.", "F: Le clonazépam est recommandé. || Il ne l'est pas."],
 notions="N09 N10 N24", angle="direct", diff=2, ladder=L("Révision.", "AASM 2024.", "Forts, contre.", "Pièges.", "α2δ et fer IV.", "Pramipexole.", "Gabapentinoïdes et fer."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="Kprim", stem="Une patiente de 60 ans demande comment interpréter sa prise de sang pour ses jambes impatientes.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une ferritine à 60 µg/l justifie un traitement martial. || Le seuil est 75 µg/l.", "V: La prise de sang se fait de préférence le matin. || Elle limite les variations.", "F: Une ferritine dans la norme du laboratoire exclut tout bénéfice du fer. || Le seuil est plus élevé.", "F: Elle peut prendre son comprimé de fer juste avant la prise de sang. || Il fausse le résultat."],
 notions="N08 N06 N19", angle="application", diff=2, ladder=L("Prise de sang.", "Interprétation.", "Ferritine 60.", "Pièges.", "≤ 75, matin.", "Norme du labo.", "75 et le matin."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="Kprim", stem="Un patient de 64 ans sous pramipexole depuis 5 ans revient en consultation.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une extension des symptômes aux bras évoque une augmentation. || C'est un signe cardinal.", "V: Un début plus précoce dans la journée évoque une augmentation. || C'est un signe cardinal.", "F: L'augmentation se traite en augmentant la dose. || Elle s'aggrave.", "F: L'augmentation apparaît dès les premiers jours. || Elle se développe en mois ou en années."],
 notions="N11 N10", angle="piège", diff=2, ladder=L("Pramipexole.", "Augmentation.", "Bras, plus tôt.", "Pièges.", "Reconnaître.", "Augmenter la dose.", "Plus tôt, plus loin."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="Kprim", stem="Des étudiants discutent des imitateurs du besoin de bouger les jambes.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Les crampes nocturnes en font partie. || Elles s'écartent par la contraction palpable.", "V: L'akathisie en fait partie. || Elle s'écarte par son caractère diffus.", "F: Un examen neurologique normal exclut le diagnostic. || Il est normal dans la forme primaire.", "F: Une polysomnographie est obligatoire. || Le diagnostic est clinique."],
 notions="N03 N15 N14 N23", angle="direct", diff=2, ladder=L("Imitateurs.", "Différentiel.", "Crampes, akathisie.", "Pièges.", "Exclure les imitateurs.", "Examen normal.", "Clinique."), sources="[Allen, Sleep Med, IRLSSG 2014]"),
dict(format="MenuLong", stem="Une patiente a des impatiences des jambes le soir.", prompt="Choisissez les TROIS médicaments ou substances qui peuvent les aggraver.",
 items=["*Antihistaminique sédatif || Il aggrave le trouble.", "*Métoclopramide || Antidopaminergique, il aggrave le trouble.", "*Inhibiteur sélectif de la recapture de la sérotonine || Il peut aggraver le trouble.", "Gabapentine || Elle traite le trouble.", "Prégabaline || Elle traite le trouble.", "Fer || Il traite la carence.", "Paracétamol || Il n'aggrave pas le trouble.", "Oméprazole || Il n'est pas un facteur aggravant reconnu.", "Amlodipine || Elle n'est pas un facteur aggravant reconnu.", "Lévothyroxine à dose substitutive || Elle n'est pas un facteur aggravant reconnu.", "Vitamine D || Elle n'est pas un facteur aggravant reconnu.", "Atorvastatine || Elle n'est pas un facteur aggravant reconnu."],
 notions="N07 N04", angle="direct", diff=2, ladder=L("Impatiences.", "Facteurs aggravants.", "Médicaments.", "Lesquels.", "Antihistaminique, métoclopramide, ISRS.", "Gabapentine.", "Antidopaminergique, antihistaminique, sérotoninergique."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
dict(format="MenuLong", stem="Un homme de 50 ans a des impatiences gênantes et une ferritine à 55 µg/l.", prompt="Choisissez les TROIS mesures de première intention.",
 items=["*Supplémentation en fer || La ferritine est sous le seuil.", "*Arrêt de l'alcool et de la caféine le soir || Ce sont des facteurs aggravants.", "*Activité physique modérée et étirements || Ils soulagent.", "Pramipexole au long cours || Il expose à l'augmentation.", "Clonazépam || Il n'est pas recommandé.", "Antihistaminique sédatif || Il aggrave.", "Neuroleptique sédatif || Il aggrave.", "Valproate || Il n'est pas recommandé.", "Opioïde fort d'emblée || Il se réserve aux formes réfractaires.", "Bupropion || Il n'est pas recommandé.", "Polysomnographie systématique || Elle n'est pas nécessaire.", "Repos strict au lit || Il aggrave les symptômes."],
 notions="N08 N07 N22", angle="application", diff=2, ladder=L("Impatiences et fer bas.", "Première intention.", "Ferritine 55.", "Mesures.", "Fer, sevrage, activité.", "Pramipexole.", "Fer et hygiène."), sources="[Winkelman, J Clin Sleep Med, AASM 2024]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Syndrome des jambes sans repos : poser les 5 critères cliniques, écarter les imitateurs, doser ferritine et saturation, corriger les aggravants, traiter par fer et gabapentinoïdes, et éviter l'augmentation des dopaminergiques",
 notions=[
  dict(titre="Diagnostic", rub=["def", "ana", "pos", "exa"], comment="Applique les 5 critères IRLSSG et écarte les imitateurs.",
   tableau=(["Critère", "Contenu", "Pourquoi"], [
     ["1", "Besoin de bouger les jambes", "Symptôme central"],
     ["2", "Début ou aggravation au repos", "Lien avec l'immobilité"],
     ["3", "Soulagement par le mouvement", "Discriminant majeur"],
     ["4", "Aggravation le soir ou la nuit", "Rythme circadien"],
     ["5", _T("Pas d'autre explication", "Crampes, inconfort de position, œdèmes, neuropathie, akathisie."), "[IRLSSG 2014]"]]),
   points=["Le diagnostic est clinique."], sources=["[Allen, Sleep Med, IRLSSG 2014]"]),
  dict(titre="Fer et facteurs aggravants", rub=["gold", "acu", "epi", "bas"], comment="Corrige d'abord ce qui entretient le trouble.",
   tableau=(["Élément", "Seuil ou mesure", "Source"], [
     ["Ferritine", "≤ 75 µg/l : fer oral ou IV", "[AASM 2024]"],
     ["Ferritine 75 à 100 µg/l", "Fer IV seulement", "[AASM 2024]"],
     ["Saturation", "< 20 % : fer", "[AASM 2024]"],
     ["Aggravants", "Alcool, caféine, antihistaminiques, sérotoninergiques, antidopaminergiques, apnées", "[AASM 2024]"]]),
   points=["Le prélèvement se fait le matin, sans fer depuis 24 heures."], sources=["[Winkelman, J Clin Sleep Med, AASM 2024]"]),
  dict(titre="Traitement de fond", rub=["chr", "hos"], comment="Préfère gabapentinoïdes et fer, évite les dopaminergiques au long cours.",
   arbre=[("t1", None, "Symptômes gênants", "Le traitement suit le bilan martial."),
          ("t2", "t1", "Ferritine ≤ 75 ou saturation < 20 %", "Fer oral ou IV.", "rls"),
          ("t3", "t1", "Fer corrigé, symptômes persistants", "Gabapentine ou prégabaline.", "rls"),
          ("t4", "t3", "Échec", "Opioïde prudent, spécialiste.", "rls"),
          ("t5", "t1", "Sous dopaminergique, symptômes plus tôt et aux bras", "Augmentation : relais vers un gabapentinoïde.", "rls")],
   points=["Clonazépam, valproate, carbamazépine et bupropion ne sont pas recommandés."], sources=["[Winkelman, J Clin Sleep Med, AASM 2024]"]),
  dict(titre="Suivi", rub=["pro", "sur", "fol", "red"], comment="Recontrôle le fer et dépiste l'augmentation.",
   tableau=(["Situation", "Conduite", "Pourquoi"], [
     ["Patient gêné", "Bilan martial régulier", "Le fer cérébral compte"],
     ["Grossesse", "Fer, réassurance", "Régression après l'accouchement"],
     ["Réfractaire ou augmentation", "Neurologue, centre du sommeil", "Options spécialisées"],
     ["Akathisie possible", "Revoir le neuroleptique", "Diagnostic différentiel"]]),
   points=["La polysomnographie n'est pas nécessaire au diagnostic."], sources=["[avis d'expert]"]),
 ],
 ssp=dict(code="G11", nom="Troubles du sommeil (insomnies, hypersomnies ou somnolence, parasomnies)", officiel=True, algorithme=[
  ("n1", None, "Gêne des jambes le soir avec troubles du sommeil", "Le médecin vérifie les 5 critères."),
  ("n2", "n1", "Contraction douloureuse palpable", "Crampes.", None, "c1"),
  ("n3", "n1", "Agitation diffuse sous neuroleptique", "Akathisie.", None, "c4"),
  ("n4", "n1", "5 critères remplis", "Willis-Ekbom : bilan martial.", "rls", "c2"),
  ("n5", "n4", "Ferritine ≤ 75 ou saturation < 20 %", "Fer.", "rls", "c2"),
  ("n6", "n4", "Fer corrigé, gêne persistante", "Gabapentinoïde.", "rls", "c3")]),
 pec=[
  dict(cle="rls", titre="Syndrome des jambes sans repos (Willis-Ekbom)",
   but=["Restaurer le sommeil.", "Corriger la carence martiale.", "Éviter l'augmentation."],
   moyens=dict(accueil=["Vérifier les 5 critères.", "Lister les médicaments aggravants.", "Demander ferritine et saturation."],
    pharma=[("Fer oral (sulfate ferreux)", "Posologie à vérifier dans l'AIPS.", "Il corrige une carence sous les seuils.", "[Winkelman, J Clin Sleep Med, AASM 2024]"),
            ("Carboxymaltose ferrique intraveineux", "Posologie et remboursement à vérifier dans l'AIPS.", "Recommandation forte si le bilan martial le permet.", "[Winkelman, J Clin Sleep Med, AASM 2024]"),
            ("Gabapentine ou prégabaline le soir", "Posologie à vérifier dans l'AIPS ; adapter à la fonction rénale.", "Recommandation forte.", "[Winkelman, J Clin Sleep Med, AASM 2024]"),
            ("Oxycodone à libération prolongée (formes réfractaires)", "Posologie à vérifier dans l'AIPS.", "Option prudente après échec.", "[Winkelman, J Clin Sleep Med, AASM 2024]")],
    nonpharma=[("hygiène de vie", "Arrêt de l'alcool et de la caféine le soir, horaires réguliers.", "Ils réduisent les aggravants."),
               ("rééducation", "Activité physique modérée et étirements.", "Ils soulagent les symptômes."),
               ("éducation thérapeutique", "Information sur les médicaments à éviter.", "Elle prévient les aggravations.")],
    transversal=[("Neurologie", "Elle prend en charge les formes réfractaires et l'augmentation."), ("Médecine du sommeil", "Elle cherche des apnées associées.")]),
   urgence=None,
   horsUrgence=(["Bilan martial.", "Correction des aggravants avant tout médicament."],
            [("d'abord", "médecin de famille", "Pose le diagnostic et corrige les facteurs aggravants."),
             ("ensuite", "médecin de famille", "Supplémente en fer si les seuils sont atteints."),
             ("puis", "médecin de famille", "Introduit un gabapentinoïde si la gêne persiste."),
             ("puis", "neurologue", "Gère l'augmentation et les formes réfractaires.")]),
   pronostic="Le trouble est souvent chronique mais se contrôle bien ; la forme de grossesse régresse après l'accouchement.",
   suivi=[("Ferritine et saturation", "Régulièrement", "Au-dessus des seuils"), ("Horaire et extension des symptômes", "À chaque visite", "Pas d'augmentation"), ("Sommeil", "À chaque visite", "Amélioré")],
   sortie="Le suivi s'espace quand les symptômes sont contrôlés.",
   prevention=["Elle évite les médicaments aggravants.", "Elle maintient des réserves en fer suffisantes.", "Elle évite les dopaminergiques au long cours."]),
 ])
AVERIFIER = ["Posologies suisses du fer oral, du carboxymaltose ferrique, de la gabapentine, de la prégabaline et de l'oxycodone à vérifier dans l'AIPS.", "Remboursement du fer intraveineux dans ce trouble en Suisse (Liste des spécialités) à vérifier.", "Seuils martiaux AASM 2024 consensuels, non testés empiriquement (mentionné par la recommandation)."]
