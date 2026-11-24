ID = "G21.0__F1_15-E11"
PLAN = "monographique"
NOTIONS = [
"def|critère|2||[Gurrera, J Clin Psychiatry, 2011 ; DSM-5-TR]|Le syndrome malin des neuroleptiques associe, après exposition à un antagoniste dopaminergique, hyperthermie, rigidité généralisée, altération de la conscience et instabilité autonome, avec CK élevées.",  # N01
"epi|chiffre|1||[Strawn, Am J Psychiatry, 2007 ; à vérifier]|Le syndrome est rare, de l'ordre de quelques cas pour 10 000 patients exposés, mais il reste potentiellement mortel.",  # N02
"bas|mécanisme|1||[Strawn, Am J Psychiatry, 2007]|Le blocage brutal des récepteurs dopaminergiques D2 dans l'hypothalamus et le striatum dérègle la thermorégulation et le tonus musculaire.",  # N03
"bas|terrain particulier|2||[Strawn, 2007 ; avis d'expert]|Un antipsychotique de haute puissance, une voie intramusculaire, une augmentation rapide des doses, la déshydratation et l'agitation augmentent le risque.",  # N04
"ana|terrain particulier|2||[avis d'expert]|L'arrêt brutal d'un traitement dopaminergique chez un parkinsonien provoque un tableau identique, ce qui impose de le reprendre.",  # N05
"ana|symptôme|1||[Strawn, 2007]|Le syndrome s'installe en général en quelques jours, souvent dans les 2 premières semaines après le début ou l'augmentation du traitement.",  # N06
"exa|signe|3||[avis d'expert]|La rigidité en tuyau de plomb, la fièvre élevée, la confusion, la tachycardie, la labilité tensionnelle et la sudation constituent le tableau clinique.",  # N07
"red|piège|2||[avis d'expert]|Les antiémétiques antidopaminergiques comme le métoclopramide peuvent aussi provoquer le syndrome.",  # N08
"gold|résultat|2||[Gurrera, 2011]|Les CK nettement élevées, la leucocytose et la myoglobinurie soutiennent le diagnostic, qui reste clinique et d'exclusion.",  # N09
"alt|examen|1||[avis d'expert]|Une ponction lombaire et une imagerie cérébrale excluent une méningo-encéphalite lorsque fièvre et confusion le font craindre.",  # N10
"pos|diagnostic différentiel|3||[Boyer, NEJM, 2005]|Le syndrome sérotoninergique débute en quelques heures, avec clonies, hyperréflexie, mydriase et diarrhée, alors que le syndrome malin donne une rigidité et une bradykinésie.",  # N11
"pos|diagnostic différentiel|1||[avis d'expert]|L'hyperthermie maligne survient pendant une anesthésie aux halogénés ou à la succinylcholine.",  # N12
"pos|diagnostic différentiel|1||[avis d'expert]|Le syndrome anticholinergique donne une peau sèche et chaude, une mydriase et une rétention urinaire, sans rigidité marquée.",  # N13
"pos|diagnostic différentiel|1||[avis d'expert]|La catatonie maligne ressemble au syndrome malin et répond aussi aux benzodiazépines et à l'électroconvulsivothérapie.",  # N14
"acu|décision|3||[avis d'expert]|L'antipsychotique s'arrête immédiatement, et le patient reçoit hydratation intraveineuse, refroidissement et surveillance, souvent aux soins intensifs.",  # N15
"acu|molécule|2||[avis d'expert ; AIPS Swissmedic]|Le lorazépam soulage rigidité et agitation ; la bromocriptine ou le dantrolène se discutent dans les formes sévères, posologies à vérifier dans l'AIPS.",  # N16
"acu|piège|1||[avis d'expert]|Un antipsychotique supplémentaire pour calmer l'agitation aggrave le syndrome.",  # N17
"hos|complication|2||[avis d'expert]|La rhabdomyolyse expose à l'insuffisance rénale aiguë et à l'hyperkaliémie, d'où le suivi de la créatinine, du potassium et de la diurèse.",  # N18
"hos|complication|1||[avis d'expert]|La pneumonie d'inhalation, la CIVD et la thrombose veineuse compliquent les formes sévères.",  # N19
"pro|pronostic|1||[Strawn, 2007 ; à vérifier]|La mortalité a baissé avec la reconnaissance précoce, mais elle reste de l'ordre de 5 à 10 %.",  # N20
"sur|décision|1||[avis d'expert]|La température, les constantes, les CK, la fonction rénale et la vigilance se surveillent jusqu'à normalisation.",  # N21
"chr|décision|1||[avis d'expert]|La reprise d'un antipsychotique attend au moins 2 semaines après la guérison et privilégie une molécule de faible puissance augmentée lentement.",  # N22
"chr|molécule|1||[avis d'expert]|L'électroconvulsivothérapie reste une option dans les formes réfractaires ou avec catatonie.",  # N23
"fol|contexte suisse|1|S|[Swissmedic, pharmacovigilance ; Tox Info Suisse]|Le cas se déclare à Swissmedic comme effet indésirable grave, et Tox Info Suisse (145) conseille en cas de doute.",  # N24
"fol|prévention|1||[avis d'expert]|Le dossier mentionne l'antécédent et l'équipe évite les antipsychotiques de haute puissance par voie intramusculaire chez ce patient.",  # N25
]
ANGLES = [
"Rigidité en tuyau de plomb ≠ clonies sérotoninergiques.",
"Arrêt de la L-dopa : même tableau.",
"Métoclopramide aussi.",
"Pas d'antipsychotique de plus.",
"CK et rein à surveiller.",
"Reprise ≥ 2 semaines, faible puissance.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un homme de 32 ans hospitalisé à Genève pour un épisode psychotique a reçu de l'halopéridol intramusculaire à doses croissantes depuis 4 jours. Il présente 40,2 °C, une rigidité diffuse en tuyau de plomb, une confusion, une tachycardie à 130/min et une PA variable. Les CK sont à 12 000 U/L.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Un syndrome malin des neuroleptiques || Hyperthermie, rigidité, confusion, dysautonomie et CK élevées sous antipsychotique.", "Un syndrome sérotoninergique || Il donne des clonies et une hyperréflexie.", "Une méningite bactérienne || Elle ne donne pas de rigidité en tuyau de plomb ni de CK aussi élevées.", "Une dystonie aiguë || Elle ne donne pas de fièvre.", "Un sevrage alcoolique || Le contexte ne l'évoque pas."],
 notions="N01 N07 N04", angle="application", diff=2, ladder=L("Fièvre et rigidité sous antipsychotique.", "Blocage D2 hypothalamique.", "CK 12 000.", "Tétrade.", "Syndrome malin.", "Syndrome sérotoninergique.", "Fièvre + rigidité + CK."), sources="[Gurrera, 2011]"),
dict(format="A", serie=("S1", 2, 4), stem="Le diagnostic est retenu chez cet homme.", prompt="Quelle mesure est prioritaire ?",
 items=["*Arrêter l'halopéridol, hydrater par voie IV, refroidir et surveiller en soins intensifs || C'est le socle du traitement.", "Augmenter l'halopéridol pour calmer l'agitation || Il aggrave le syndrome.", "Ajouter de l'olanzapine || Tout antipsychotique aggrave.", "Donner seulement du paracétamol || La fièvre est centrale.", "Faire une électroconvulsivothérapie d'emblée || Elle se réserve aux formes réfractaires."],
 notions="N15 N17", angle="direct", diff=2, ladder=L("Syndrome malin confirmé.", "Lever le blocage.", "Instabilité.", "Mesures de base.", "Arrêt, hydratation, froid.", "Plus d'antipsychotique.", "Arrêter et réanimer."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 3, 4), stem="Le lendemain, la diurèse de cet homme chute, ses urines sont foncées et le potassium monte à 6,1 mmol/L.", prompt="Quelle complication explique ce tableau ?",
 items=["*Une rhabdomyolyse avec insuffisance rénale aiguë || La myoglobine lèse les tubules.", "Une glomérulonéphrite aiguë || Le contexte oriente vers la rhabdomyolyse.", "Une rétention urinaire anticholinergique || Elle ne donne pas d'hyperkaliémie isolée.", "Une hématurie de cystite || Rien ne l'évoque.", "Une déshydratation simple || Les urines foncées et la kaliémie évoquent la myolyse."],
 notions="N18 N09", angle="application", diff=2, ladder=L("Oligurie, urines foncées.", "Myoglobinurie.", "Hyperkaliémie.", "Complication.", "Rhabdomyolyse, IRA.", "Glomérulonéphrite.", "CK + oligurie = myolyse."), sources="[avis d'expert]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Cet homme guérit en 10 jours. Le psychiatre envisage la suite du traitement antipsychotique.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La reprise attend au moins 2 semaines après la guérison. || Le risque de récidive baisse.", "V: Une molécule de faible puissance augmentée lentement est préférée. || Le risque est moindre.", "V: L'événement se déclare à Swissmedic. || C'est un effet indésirable grave.", "F: L'halopéridol IM peut être repris à la même dose. || Le risque de récidive est élevé."],
 notions="N22 N24 N25", angle="application", diff=3, ladder=L("Reprise.", "Risque de récidive.", "Guérison.", "Précautions.", "Délai, faible puissance, déclaration.", "Même molécule.", "≥ 2 semaines, lent."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 74 ans atteint de maladie de Parkinson est hospitalisé à Bâle pour une pneumonie. Sa lévodopa a été arrêtée car il ne déglutit plus. Deux jours plus tard, il a 39,5 °C, une rigidité majeure, une confusion et des CK élevées.", prompt="Quelle mesure est indispensable ?",
 items=["*Reprendre le traitement dopaminergique, par sonde ou par voie alternative || L'arrêt brutal provoque ce syndrome.", "Ajouter de l'halopéridol pour la confusion || Il aggraverait.", "Maintenir l'arrêt de la lévodopa || Il entretient le syndrome.", "Augmenter seulement l'antibiotique || La fièvre n'est pas seulement infectieuse.", "Donner du métoclopramide pour la déglutition || Il est antidopaminergique."],
 notions="N05 N08", angle="piège", diff=3, ladder=L("Parkinsonien fébrile rigide.", "Sevrage dopaminergique.", "Lévodopa arrêtée.", "Cause iatrogène.", "Reprendre la dopa.", "Halopéridol.", "Ne jamais arrêter la dopa."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 28 ans traitée par sertraline a reçu du tramadol il y a 6 heures. Elle est agitée, a 38,8 °C, des pupilles dilatées, une diarrhée, une hyperréflexie et des clonies inductibles aux membres inférieurs.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Un syndrome sérotoninergique || Début rapide, clonies, hyperréflexie, mydriase, diarrhée.", "Un syndrome malin des neuroleptiques || Il donne rigidité et bradykinésie en quelques jours.", "Une hyperthermie maligne || Elle survient en anesthésie.", "Un syndrome anticholinergique || Il ne donne pas de diarrhée ni de clonies.", "Une méningite || Les clonies et le contexte orientent ailleurs."],
 notions="N11", angle="piège", diff=2, ladder=L("Agitation fébrile.", "Excès de sérotonine.", "ISRS + tramadol.", "Clonies.", "Syndrome sérotoninergique.", "Syndrome malin.", "Clonies = sérotonine."), sources="[Boyer, NEJM, 2005]"),
dict(format="A", stem="Une femme de 45 ans reçoit du métoclopramide IV depuis 3 jours pour des vomissements postopératoires à Fribourg. Elle développe une fièvre à 39,8 °C, une rigidité généralisée et une confusion. Elle ne prend aucun antipsychotique.", prompt="Quelle cause évoquez-vous ?",
 items=["*Un syndrome malin lié au métoclopramide antidopaminergique || Les antiémétiques antidopaminergiques peuvent le provoquer.", "Une infection de site opératoire seule || Elle n'explique pas la rigidité.", "Une hyperthermie maligne tardive || Elle survient pendant l'anesthésie.", "Une dystonie aiguë || Elle ne donne pas de fièvre.", "Une crise thyréotoxique || Elle ne donne pas de rigidité."],
 notions="N08 N01", angle="application", diff=3, ladder=L("Rigidité fébrile post-opératoire.", "Blocage D2.", "Métoclopramide.", "Cause cachée.", "Syndrome malin.", "Infection.", "Antiémétique = antidopaminergique."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 30 ans sous rispéridone depuis 1 semaine présente fièvre, confusion et rigidité. Il a une raideur de nuque discutable et a eu un syndrome grippal.", prompt="Quel examen est indiqué pour exclure le principal diagnostic différentiel ?",
 items=["*Une ponction lombaire après imagerie si nécessaire || Une méningo-encéphalite doit être exclue.", "Un EEG seul || Il n'exclut pas l'infection.", "Un dosage de prolactine || Il n'a pas de valeur ici.", "Une échographie abdominale || Rien ne l'indique.", "Un test au Synacthen || Rien ne l'indique."],
 notions="N10 N09", angle="application", diff=2, ladder=L("Fièvre, confusion.", "Infection du SNC possible.", "Raideur, syndrome grippal.", "Diagnostic d'exclusion.", "PL.", "EEG seul.", "Fièvre + confusion : PL."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 25 ans présente sous anesthésie générale avec sévoflurane une hypercapnie brutale, une rigidité des masséters, une tachycardie et une hyperthermie rapide.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une hyperthermie maligne || Elle survient sous halogénés ou succinylcholine.", "Un syndrome malin des neuroleptiques || Il suppose un antidopaminergique et s'installe en jours.", "Un syndrome sérotoninergique || Le contexte n'y correspond pas.", "Un sepsis || Il ne donne pas de rigidité des masséters.", "Une thyrotoxicose || Elle ne donne pas cette rigidité peropératoire."],
 notions="N12 N11", angle="piège", diff=2, ladder=L("Rigidité peropératoire.", "Canal RYR1.", "Halogéné.", "Contexte.", "Hyperthermie maligne.", "Syndrome malin.", "Anesthésie = hyperthermie maligne."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 40 ans en syndrome malin reste très rigide et agité malgré l'arrêt de l'antipsychotique, l'hydratation et le refroidissement depuis 24 heures.", prompt="Quel traitement ajoutez-vous en premier ?",
 items=["*Du lorazépam || Il réduit rigidité et agitation.", "De l'halopéridol || Il aggraverait.", "Du métoclopramide || Il est antidopaminergique.", "De la prednisone || Elle n'est pas indiquée.", "De la quétiapine || Tout antipsychotique aggrave."],
 notions="N16 N17", angle="direct", diff=2, ladder=L("Rigidité persistante.", "Modulation GABA.", "24 heures.", "Escalade.", "Lorazépam.", "Antipsychotique.", "Benzodiazépine d'abord."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 35 ans en syndrome malin sévère a 41 °C, des CK à 40 000 U/L et une rigidité extrême malgré les benzodiazépines.", prompt="Quelle option thérapeutique se discute ?",
 items=["*La bromocriptine ou le dantrolène || Ils se discutent dans les formes sévères.", "L'halopéridol IV || Il aggraverait.", "L'acide acétylsalicylique seul || Il ne traite pas la cause.", "La L-thyroxine || Rien ne l'indique.", "Une antibiothérapie seule || Elle ne traite pas le syndrome."],
 notions="N16 N15", angle="application", diff=3, ladder=L("Forme sévère.", "Agonisme D2 ou relaxation musculaire.", "41 °C, CK 40 000.", "Escalade.", "Bromocriptine, dantrolène.", "Antipsychotique.", "Sévère : bromocriptine/dantrolène."), sources="[avis d'expert]"),
dict(format="A", stem="Un patient de 50 ans stuporeux, mutique et rigide garde une posture imposée. Il a de la fièvre et une dysautonomie. Ses antipsychotiques ont été arrêtés et les benzodiazépines ont échoué.", prompt="Quel traitement est le plus adapté ?",
 items=["*L'électroconvulsivothérapie || Elle traite la catatonie maligne et le syndrome malin réfractaire.", "Un nouvel antipsychotique de haute puissance || Il aggraverait.", "Une psychothérapie seule || L'urgence est somatique.", "Un antibiotique seul || Il ne traite pas la catatonie.", "Une simple observation || Le pronostic vital est en jeu."],
 notions="N14 N23", angle="application", diff=4, ladder=L("Catatonie fébrile.", "Dysrégulation GABA-dopamine.", "Échec des benzodiazépines.", "Réfractaire.", "ECT.", "Antipsychotique.", "Réfractaire : ECT."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un interne vous demande quand survient le plus souvent un syndrome malin des neuroleptiques.", prompt="Quelle réponse est la plus juste ?",
 items=["*Dans les 2 premières semaines après le début ou l'augmentation du traitement, en quelques jours || Le changement de dose est le moment critique.", "Uniquement après des années de traitement || Il survient surtout tôt.", "En quelques minutes après la première dose || Le début est progressif.", "Seulement à l'arrêt du traitement chez le schizophrène || C'est le sevrage dopaminergique du parkinsonien qui compte.", "Seulement chez l'enfant || Il touche surtout l'adulte."],
 notions="N06 N04 N01 N05", angle="direct", diff=2, ladder=L("Chronologie.", "Changement de dose.", "Début.", "Fenêtre de risque.", "2 premières semaines.", "Années.", "Tôt après un changement."), sources="[Strawn, 2007]"),
dict(masque=False, sit="monographique", format="A", stem="Un patient guéri d'un syndrome malin des neuroleptiques demande si la maladie peut tuer.", prompt="Quelle réponse est la plus juste ?",
 items=["*Oui, la mortalité reste de l'ordre de 5 à 10 % malgré la reconnaissance précoce || Les complications en sont la cause.", "Non, elle est toujours bénigne || Elle peut tuer.", "Oui, elle tue plus de la moitié des patients || Ce chiffre est trop élevé.", "Non, sauf chez l'enfant || L'adulte est aussi exposé.", "On ne connaît aucun décès || Des décès sont décrits."],
 notions="N20 N19", angle="direct", diff=2, ladder=L("Pronostic.", "Complications systémiques.", "Guérison.", "Mortalité.", "5-10 %.", "Bénin.", "Rare mais grave."), sources="[Strawn, 2007]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous comparez syndrome malin des neuroleptiques et syndrome sérotoninergique pour des étudiants à Lausanne.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le syndrome sérotoninergique débute en quelques heures. || Il suit rapidement la prise.", "V: La rigidité en tuyau de plomb oriente vers le syndrome malin. || Le blocage D2 la provoque.", "F: Les clonies inductibles orientent vers le syndrome malin. || Elles orientent vers la sérotonine.", "F: La diarrhée est typique du syndrome malin. || Elle évoque la sérotonine."],
 notions="N11 N07", angle="direct", diff=2, ladder=L("Comparaison.", "Deux toxidromes.", "Signes.", "Discriminants.", "Rigidité vs clonies.", "Confondre.", "Rigidité = malin ; clonies = sérotonine."), sources="[Boyer, NEJM, 2005]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un patient en syndrome malin des neuroleptiques est admis aux soins intensifs.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Les CK, la créatinine et le potassium se surveillent. || La rhabdomyolyse menace le rein.", "V: La prévention de la thrombose veineuse se discute. || L'immobilité y expose.", "V: Le risque d'inhalation se prévient. || La rigidité et la confusion gênent la déglutition.", "F: La fièvre se traite seulement par paracétamol. || Le refroidissement physique est nécessaire."],
 notions="N18 N19 N21 N15", angle="application", diff=2, ladder=L("Soins intensifs.", "Complications.", "Rhabdomyolyse.", "Surveillance.", "CK, rein, inhalation, TVP.", "Paracétamol seul.", "Rein + inhalation + TVP."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Une femme de 22 ans reçoit de l'halopéridol IM pour une agitation aiguë. Elle est déshydratée et très agitée.", prompt="Évaluez chacune des affirmations suivantes sur son risque de syndrome malin.",
 items=["V: La voie intramusculaire augmente le risque. || Elle donne des taux élevés rapidement.", "V: La déshydratation augmente le risque. || Elle favorise l'hyperthermie.", "V: L'agitation augmente le risque. || L'effort musculaire élève la température.", "F: Les antipsychotiques de haute puissance exposent moins. || Ils exposent davantage."],
 notions="N04 N03", angle="piège", diff=2, ladder=L("Facteurs de risque.", "Blocage D2 intense.", "IM, déshydratation.", "Lesquels.", "IM, déshydratation, agitation.", "Haute puissance protectrice.", "Haute puissance IM = risque."), sources="[Strawn, 2007]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un syndrome malin des neuroleptiques est suspecté.", prompt="Quels résultats biologiques le soutiennent ? (3 réponses)",
 items=["*CK nettement élevées || Rhabdomyolyse.", "*Leucocytose || Fréquente.", "*Myoglobinurie || Rhabdomyolyse.", "Hyponatrémie isolée || Elle n'est pas typique.", "Éosinophilie || Elle n'est pas typique.", "Hypoglycémie || Elle n'est pas typique.", "Procalcitonine très élevée || Elle évoque une infection.", "Anticorps anti-NMDA || Ils évoquent une encéphalite.", "TSH effondrée || Elle évoque une thyrotoxicose.", "Lipase élevée || Elle évoque une pancréatite.", "Troponine isolée || Elle n'est pas typique.", "Hyperéosinophilie du LCR || Elle n'est pas typique."],
 notions="N09 N18", angle="direct", diff=2, ladder=L("Biologie.", "Myolyse et inflammation.", "Laboratoire.", "Soutien.", "CK, leucocytes, myoglobine.", "Marqueurs d'infection.", "CK + GB + myoglobine."), sources="[Gurrera, 2011]"),
dict(format="MenuLong", stem="Un homme de 35 ans traité par antipsychotique présente fièvre, rigidité et confusion.", prompt="Quels traitements sont appropriés ? (3 réponses)",
 items=["*Arrêt de l'antipsychotique || Il lève le blocage.", "*Hydratation intraveineuse || Elle protège le rein.", "*Lorazépam || Il réduit rigidité et agitation.", "Halopéridol || Il aggrave.", "Métoclopramide || Il est antidopaminergique.", "Olanzapine || Elle aggrave.", "Prednisone || Elle n'est pas indiquée.", "Restriction hydrique || Elle aggrave le rein.", "Succinylcholine || Elle expose à l'hyperkaliémie.", "Lithium || Il n'est pas indiqué.", "Tramadol || Il n'est pas indiqué.", "Contention prolongée sans sédation || Elle aggrave l'hyperthermie."],
 notions="N15 N16 N17", angle="application", diff=2, ladder=L("Traitement.", "Arrêt et soutien.", "Phase aiguë.", "Mesures.", "Arrêt, hydratation, lorazépam.", "Autre antipsychotique.", "Stop + IV + lorazépam."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 60 ans agité reçoit de l'atropine par erreur. Il a 38,9 °C, une peau sèche et rouge, des pupilles dilatées, un globe vésical et une confusion, sans rigidité.", prompt="Quel syndrome reconnaissez-vous ?",
 items=["*Un syndrome anticholinergique || Peau sèche, mydriase, rétention, confusion.", "Un syndrome malin des neuroleptiques || Il donne une rigidité et une sudation.", "Un syndrome sérotoninergique || Il donne sudation et clonies.", "Une hyperthermie maligne || Le contexte anesthésique manque.", "Un coup de chaleur d'effort || Le contexte manque."],
 notions="N13 N07", angle="piège", diff=2, ladder=L("Fièvre, peau sèche.", "Blocage muscarinique.", "Atropine.", "Toxidrome.", "Anticholinergique.", "Syndrome malin.", "Sec et rouge = anticholinergique."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Syndrome malin des neuroleptiques : reconnaître fièvre, rigidité, confusion et dysautonomie sous antidopaminergique, arrêter le produit, réanimer, prévenir la rhabdomyolyse et le distinguer des autres toxidromes",
 notions=[
  dict(titre="Toxidromes hyperthermiques", rub=["pos", "exa"], comment="Distingue par le délai, le tonus et la peau.",
   tableau=(["Syndrome", "Déclencheur", "Délai", "Discriminant"], [
     ["Syndrome malin", "Antipsychotique, métoclopramide, arrêt de dopa", "Jours", _T("Rigidité en tuyau de plomb", "Le blocage D2 du striatum la crée.")],
     ["Sérotoninergique", "ISRS + tramadol, IMAO", "Heures", _T("Clonies, hyperréflexie", "L'excès de 5-HT excite la moelle.")],
     ["Hyperthermie maligne", "Halogénés, succinylcholine", "Peropératoire", _T("Hypercapnie", "Le muscle s'emballe (RYR1).")],
     ["Anticholinergique", "Atropine, antihistaminiques", "Heures", _T("Peau sèche", "La sudation est bloquée.")]]),
   points=["La catatonie maligne ressemble et répond à l'ECT."], sources=["[Boyer, NEJM, 2005]", "[Gurrera, 2011]"]),
  dict(titre="Terrain et diagnostic", rub=["def", "bas", "gold", "alt"], comment="Cherche l'exposition puis exclus l'infection.",
   tableau=(["Élément", "Contenu", "Pourquoi"], [
     ["Facteurs de risque", "Haute puissance, IM, augmentation rapide, déshydratation", [("Blocage brutal", "Il dérègle thermorégulation et tonus.")]],
     ["Biologie", "CK élevées, leucocytose, myoglobinurie", [("Rhabdomyolyse", "La rigidité lyse le muscle.")]],
     ["Exclusion", "PL et imagerie si doute", [("Méningo-encéphalite", "Elle donne fièvre et confusion.")]]]),
   points=["Arrêt de la lévodopa : même tableau."], sources=["[Strawn, 2007]"]),
  dict(titre="Traitement", rub=["acu", "chr"], comment="Arrête, refroidis, hydrate, puis escalade.",
   arbre=[("t1", None, "Syndrome malin", "L'arrêt de l'agent est immédiat."),
          ("t2", "t1", "Mesures de base", "Hydratation IV, refroidissement, soins intensifs.", "smn"),
          ("t3", "t2", "Rigidité, agitation", "Lorazépam.", "smn"),
          ("t4", "t3", "Forme sévère", "Bromocriptine ou dantrolène.", "smn"),
          ("t5", "t4", "Réfractaire ou catatonie", "ECT.", "smn"),
          ("t6", "t1", "Parkinsonien sevré", "Reprendre la dopa.", "smn")],
   points=["Jamais d'antipsychotique supplémentaire."], sources=["[avis d'expert]"]),
  dict(titre="Complications et suite", rub=["hos", "pro", "fol"], comment="Protège le rein et prépare une reprise prudente.",
   tableau=(["Thème", "Conduite", "Pourquoi"], [
     ["Rhabdomyolyse", "Hydratation, créatinine, potassium", "Elle menace le rein."],
     ["Inhalation, TVP, CIVD", "Prévention et surveillance", "Elles compliquent les formes sévères."],
     ["Reprise", "≥ 2 semaines, faible puissance, lente", "Le risque de récidive baisse."],
     ["Déclaration", "Swissmedic ; Tox Info Suisse 145", "C'est un effet grave."]]),
   points=["Mortalité de l'ordre de 5 à 10 %."], sources=["[Strawn, 2007]"]),
 ],
 ssp=dict(code="F1.15", nom="Altération ou perte de conscience, coma", officiel=True, algorithme=[
  ("n1", None, "Confusion fébrile", "Le contexte médicamenteux oriente."),
  ("n2", "n1", "Antidopaminergique ou arrêt de dopa, rigidité", "Syndrome malin.", "smn", "c1"),
  ("n3", "n1", "Sérotoninergique, clonies", "Syndrome sérotoninergique : arrêt, benzodiazépine.", None, "c1"),
  ("n4", "n1", "Peau sèche, mydriase, rétention", "Syndrome anticholinergique.", None, "c1"),
  ("n5", "n1", "Raideur de nuque, contexte infectieux", "PL : méningo-encéphalite (même SSP).", None, "c2"),
  ("n6", "n2", "Mesures de base", "Arrêt, hydratation, refroidissement.", "smn", "c3"),
  ("n7", "n6", "Rhabdomyolyse", "Rein et potassium.", "smn", "c4"),
  ("n8", "n6", "Échec", "Lorazépam, bromocriptine, dantrolène, ECT.", "smn", "c3")]),
 pec=[
  dict(cle="smn", titre="Syndrome malin des neuroleptiques",
   but=["Lever le blocage dopaminergique.", "Prévenir rhabdomyolyse et décès."],
   moyens=dict(accueil=["Arrêt immédiat de l'antidopaminergique.", "CK, créatinine, potassium, NFS."],
    pharma=[("Lorazépam (benzodiazépine)", "IV ; à vérifier dans l'AIPS.", "Il réduit rigidité et agitation.", "[avis d'expert]"),
            ("Bromocriptine (agoniste dopaminergique)", "Forme sévère ; à vérifier dans l'AIPS.", "Elle restaure le tonus dopaminergique.", "[avis d'expert]"),
            ("Dantrolène (myorelaxant)", "Forme sévère ; à vérifier dans l'AIPS.", "Il réduit la production de chaleur musculaire.", "[avis d'expert]")],
    nonpharma=[("soins infirmiers", "Refroidissement, hydratation, prévention d'escarres et d'inhalation.", "Ils limitent les complications."),
               ("geste ou chirurgie", "Électroconvulsivothérapie si réfractaire.", "Elle agit sur la catatonie associée.")],
    transversal=[("Psychiatrie", "Elle planifie une reprise prudente de l'antipsychotique."), ("Néphrologie", "Elle traite l'insuffisance rénale aiguë.")]),
   urgence=(["Arrêt de l'agent et hydratation IV.", "Admission en soins intensifs si instable."],
            [("d'abord", "médecin responsable", "Arrête l'agent et demande CK et fonction rénale."),
             ("en même temps", "infirmier·ère", "Refroidit, perfuse et surveille constantes et diurèse."),
             ("ensuite", "intensiviste", "Traite les formes sévères.")]),
   horsUrgence=(["Reprise ≥ 2 semaines après guérison.", "Déclaration de pharmacovigilance."],
            [("d'abord", "psychiatre", "Choisit une molécule de faible puissance."),
             ("ensuite", "médecin de famille", "Inscrit l'antécédent au dossier."),
             ("puis", "patient·e", "Signale tout nouveau traitement antidopaminergique.")]),
   pronostic="La mortalité reste de l'ordre de 5 à 10 % ; la guérison survient souvent en 1 à 2 semaines.",
   suivi=[("Température et constantes", "Continue", "Normalisation"), ("CK et créatinine", "Quotidienne", "Décroissance"), ("Vigilance", "Pluriquotidienne", "Retour à l'état antérieur")],
   sortie="Le patient sort après normalisation clinique et biologique.",
   prevention=["Elle augmente les doses lentement.", "Elle évite l'IM chez le patient déshydraté.", "Elle ne stoppe jamais brutalement la dopa d'un parkinsonien."]),
 ])
AVERIFIER = ["Incidence et mortalité chiffrées du syndrome malin (Strawn, Am J Psychiatry, 2007) à vérifier.",
             "Posologies du lorazépam, de la bromocriptine et du dantrolène à vérifier dans l'AIPS.",
             "Disponibilité du dantrolène IV hors anesthésie en Suisse à vérifier."]
