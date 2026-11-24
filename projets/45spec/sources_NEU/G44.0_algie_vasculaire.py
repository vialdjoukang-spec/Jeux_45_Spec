ID = "G44.0__S1_11-E07"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[ICHD-3, IHS, 2018]|L'algie vasculaire de la face donne des crises de douleur orbitaire ou temporale unilatérale très intense de 15 à 180 minutes, avec signes dysautonomiques homolatéraux ou agitation.",  # N01
"def|critère|1||[ICHD-3, IHS, 2018]|La forme épisodique alterne des périodes de crises de quelques semaines et des rémissions d'au moins 3 mois, alors que la forme chronique a des rémissions plus courtes.",  # N02
"epi|terrain particulier|1||[May, Nat Rev Dis Primers, 2018]|L'algie vasculaire touche surtout l'homme jeune, souvent fumeur, et débute en général entre 20 et 40 ans.",  # N03
"bas|mécanisme|1||[May, Nat Rev Dis Primers, 2018]|L'hypothalamus, le système trigéminovasculaire et le réflexe trigémino-autonomique expliquent la périodicité et les signes dysautonomiques.",  # N04
"ana|symptôme|1||[ICHD-3, IHS, 2018]|Les crises surviennent souvent à heure fixe, la nuit, une à plusieurs fois par jour, et l'alcool les déclenche pendant les périodes actives.",  # N05
"exa|signe|2||[ICHD-3, IHS, 2018]|Pendant la crise, le patient présente larmoiement, rougeur conjonctivale, rhinorrhée, ptosis ou myosis du côté douloureux.",  # N06
"exa|signe|2||[ICHD-3, IHS, 2018]|Le patient s'agite et fait les cent pas pendant la crise, à l'inverse du migraineux qui reste immobile.",  # N07
"alt|décision|2||[EHF, 2023 ; avis d'expert]|Une IRM cérébrale avec étude de la région hypophysaire se fait au moins une fois, car des lésions peuvent mimer une algie vasculaire.",  # N08
"red|piège|1||[avis d'expert]|Un syndrome de Horner permanent avec douleur cervicale doit faire chercher une dissection carotidienne.",  # N09
"gold|décision|2||[ICHD-3, IHS, 2018]|Le diagnostic est clinique, fondé sur la durée, la topographie, les signes dysautonomiques et l'agitation.",  # N10
"pos|diagnostic différentiel|2||[ICHD-3, IHS, 2018]|La névralgie du trijumeau donne des décharges de quelques secondes déclenchées par le contact, sans signes dysautonomiques marqués.",  # N11
"pos|diagnostic différentiel|1||[ICHD-3, IHS, 2018]|L'hémicrânie paroxystique donne des crises plus brèves et plus nombreuses, qui répondent de façon absolue à l'indométacine.",  # N12
"pos|diagnostic différentiel|1||[avis d'expert]|Le glaucome aigu par fermeture de l'angle donne un œil rouge douloureux avec mydriase et baisse visuelle, qui impose une prise en charge ophtalmologique urgente.",  # N13
"acu|molécule|3|S|[EHF, 2023 ; May, 2018]|L'oxygène pur à haut débit (12 à 15 L/min) au masque à haute concentration pendant environ 15 minutes interrompt efficacement la crise.",  # N14
"acu|posologie|3|S|[AIPS Swissmedic ; EHF, 2023]|Le sumatriptan 6 mg sous-cutané interrompt la crise en quelques minutes, posologie à vérifier dans l'AIPS.",  # N15
"acu|piège|2||[avis d'expert]|Les triptans oraux et les antalgiques usuels agissent trop lentement pour des crises de moins de 3 heures.",  # N16
"chr|molécule|2||[EHF, 2023]|Le vérapamil est le traitement de fond de première ligne et exige un ECG avant et pendant l'augmentation des doses.",  # N17
"chr|décision|1||[EHF, 2023]|Une corticothérapie courte ou un bloc du nerf grand occipital servent de traitement de transition au début d'une période active.",  # N18
"chr|molécule|1||[EHF, 2023]|Le lithium et le topiramate sont des alternatives de fond, surtout dans la forme chronique.",  # N19
"chr|piège|1||[avis d'expert]|L'abus de triptans et de sumatriptan injectable peut survenir, ce qui justifie un traitement de fond efficace.",  # N20
"hos|complication|1||[avis d'expert]|L'intensité extrême des crises expose à la dépression et aux idées suicidaires, qui se recherchent.",  # N21
"pro|pronostic|1||[May, Nat Rev Dis Primers, 2018]|La forme épisodique peut devenir chronique, et inversement, et l'activité tend à diminuer avec l'âge.",  # N22
"sur|décision|1||[avis d'expert]|Le suivi compte les crises par agenda et surveille l'ECG sous vérapamil.",  # N23
"fol|contexte suisse|1|S|[avis d'expert]|L'oxygénothérapie à domicile se prescrit avec un équipement adapté, et son remboursement suit les conditions des assureurs suisses.",  # N24
"fol|prévention|1||[avis d'expert]|L'arrêt du tabac et l'abstention d'alcool pendant les périodes actives font partie des conseils.",  # N25
]
ANGLES = [
"Le patient s'agite, le migraineux s'immobilise.",
"L'oxygène pur à haut débit coupe la crise.",
"Les triptans oraux sont trop lents.",
"Le vérapamil exige un ECG.",
"Une IRM se fait au moins une fois.",
"L'hémicrânie paroxystique répond à l'indométacine.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un homme de 33 ans, fumeur, consulte à Lausanne pour des crises de douleur atroce derrière l'œil droit, de 45 minutes, chaque nuit vers 2 heures depuis 3 semaines. Pendant la crise, l'œil droit larmoie et rougit, le nez coule et il marche de long en large.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une algie vasculaire de la face || Crises orbitaires de 45 minutes, nocturnes, dysautonomiques, avec agitation.", "Une migraine sans aura || Le migraineux s'immobilise et les crises durent plus de 4 heures.", "Une névralgie du trijumeau || Elle donne des décharges de quelques secondes.", "Une sinusite aiguë || Elle ne donne pas de crises stéréotypées nocturnes.", "Un glaucome aigu || Il donne une baisse visuelle et une mydriase durable."],
 notions="N01 N06 N07 N05 N11", angle="application", diff=2, ladder=L("Douleur orbitaire nocturne.", "Réflexe trigémino-autonomique.", "Larmoiement, agitation.", "Durée et comportement.", "Algie vasculaire.", "Migraine.", "Agitation + 45 min."), sources="[ICHD-3, IHS, 2018]"),
dict(format="A", serie=("S1", 2, 4), stem="Cet homme demande un traitement pour couper ses crises.", prompt="Quel traitement de crise est le plus adapté ?",
 items=["*Oxygène pur à 12-15 L/min au masque à haute concentration ou sumatriptan 6 mg sous-cutané || Ils agissent en quelques minutes.", "Sumatriptan 50 mg per os || Il agit trop lentement.", "Paracétamol 1 g || Il est inefficace.", "Ibuprofène 400 mg || Il est inefficace.", "Tramadol || Il est inefficace et expose à l'abus."],
 notions="N14 N15 N16", angle="application", diff=2, ladder=L("Crises brèves.", "Vasoconstriction, inhibition trigéminale.", "Moins de 3 heures.", "Rapidité d'action.", "Oxygène ou sumatriptan SC.", "Triptan oral.", "Rapide : O2 ou SC."), sources="[EHF, 2023]"),
dict(format="A", serie=("S1", 3, 4), stem="Les crises de cet homme surviennent 2 fois par jour et la période active dure en général 2 mois.", prompt="Quel traitement de fond proposez-vous ?",
 items=["*Vérapamil avec ECG avant et pendant l'augmentation des doses || Il est la première ligne.", "Propranolol || Il est peu efficace dans cette indication.", "Amitriptyline || Elle est peu efficace dans cette indication.", "Sumatriptan oral quotidien || Il n'est pas un traitement de fond.", "Aucun traitement de fond || Deux crises par jour le justifient."],
 notions="N17 N18 N23", angle="application", diff=3, ladder=L("Période active.", "Modulation hypothalamique.", "Crises quotidiennes.", "Traitement de fond.", "Vérapamil sous ECG.", "Propranolol.", "Vérapamil + ECG."), sources="[EHF, 2023]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Vous complétez la prise en charge de cet homme.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une IRM cérébrale doit être faite au moins une fois. || Des lésions peuvent mimer le tableau.", "V: L'alcool déclenche des crises pendant la période active. || Il est un déclencheur classique.", "F: Le vérapamil ne nécessite aucun contrôle. || Il expose aux troubles de conduction.", "F: Les idées suicidaires sont exceptionnelles et ne se recherchent pas. || L'intensité des crises y expose."],
 notions="N08 N25 N17 N21", angle="direct", diff=2, ladder=L("Suivi.", "Causes secondaires, déclencheurs.", "Période active.", "Sécurité.", "IRM, ECG, humeur.", "Oublier l'humeur.", "IRM une fois."), sources="[EHF, 2023]"),
dict(format="A", stem="Une femme de 58 ans consulte à Genève pour des douleurs fulgurantes de la joue droite durant 2 à 3 secondes, déclenchées par le brossage des dents ou le vent, plusieurs fois par jour.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Une névralgie du trijumeau || Décharges brèves déclenchées par le contact.", "Une algie vasculaire de la face || Les crises durent 15 à 180 minutes.", "Une migraine || Les crises durent des heures.", "Une sinusite maxillaire || La douleur est continue.", "Une dissection carotidienne || Elle donne une douleur continue avec Horner."],
 notions="N11 N01", angle="piège", diff=2, ladder=L("Décharges faciales.", "Compression vasculaire du V.", "Secondes, gâchette.", "Durée des crises.", "Névralgie du trijumeau.", "Algie vasculaire.", "Secondes : trijumeau."), sources="[ICHD-3, IHS, 2018]"),
dict(format="A", stem="Une femme de 40 ans décrit des crises orbitaires gauches de 10 minutes, 15 fois par jour, avec larmoiement et rhinorrhée gauches.", prompt="Quel test thérapeutique oriente le diagnostic ?",
 items=["*L'indométacine, à laquelle l'hémicrânie paroxystique répond de façon absolue || La réponse complète confirme ce diagnostic.", "Le vérapamil || Il ne sert pas de test diagnostique.", "L'oxygène || La réponse n'est pas discriminante.", "La carbamazépine || Elle sert la névralgie du trijumeau.", "Le paracétamol || Il n'a pas de valeur diagnostique."],
 notions="N12 N01", angle="application", diff=4, ladder=L("Crises brèves et nombreuses.", "Céphalée trigémino-autonomique.", "10 minutes, 15 par jour.", "Hémicrânie paroxystique.", "Indométacine.", "Traiter comme une algie.", "Brève et fréquente : indométacine."), sources="[ICHD-3, IHS, 2018]"),
dict(format="A", stem="Un homme de 46 ans présente depuis 4 jours une douleur cervicale gauche et une céphalée continues, avec un ptosis et un myosis gauches permanents.", prompt="Quel examen demandez-vous en urgence ?",
 items=["*Une imagerie des artères cervicales à la recherche d'une dissection carotidienne || Le Horner permanent avec douleur cervicale l'évoque.", "Aucun examen, il s'agit d'une algie vasculaire || La douleur est continue et le Horner permanent.", "Un dosage de la TSH || Rien ne l'évoque.", "Un EEG || Rien ne l'indique.", "Un test à l'indométacine || Le tableau n'est pas paroxystique."],
 notions="N09 N08", angle="piège", diff=3, ladder=L("Horner permanent et douleur.", "Dissection de la paroi carotidienne.", "Douleur cervicale continue.", "Secondaire versus primaire.", "Angio-CT ou angio-IRM.", "Conclure à une algie.", "Horner + cou : dissection."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un patient de 38 ans connu pour une algie vasculaire, en période active, vous demande s'il peut boire du vin au repas.", prompt="Quel conseil donnez-vous ?",
 items=["*Éviter l'alcool pendant la période active, car il déclenche les crises || C'est un déclencheur classique.", "Boire librement, l'alcool n'a aucun effet || Il déclenche les crises.", "Boire avant le coucher pour mieux dormir || Il déclencherait une crise nocturne.", "Remplacer le vin par de la bière || L'alcool reste en cause.", "Arrêter le vérapamil pour pouvoir boire || Le traitement doit continuer."],
 notions="N25 N05", angle="application", diff=1, ladder=L("Alcool en période active.", "Vasodilatation.", "Déclencheur.", "Hygiène de vie.", "Éviter l'alcool.", "Boire librement.", "Période active : pas d'alcool."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 35 ans sous vérapamil à dose croissante pour des crises orbitaires nocturnes se sent fatigué. L'ECG montre un PR à 260 ms.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Ne plus augmenter le vérapamil et réévaluer la dose avec un ECG de contrôle || Le bloc auriculo-ventriculaire est un effet indésirable.", "Augmenter encore la dose || Le bloc risque de progresser.", "Ignorer l'ECG || Le PR allongé signe un bloc.", "Ajouter un bêtabloquant || Il aggraverait le bloc.", "Arrêter tout traitement définitivement || D'autres options existent."],
 notions="N17 N23", angle="piège", diff=3, ladder=L("PR allongé sous vérapamil.", "Inhibition calcique nodale.", "Fatigue.", "Effet indésirable.", "Réduire, contrôler.", "Augmenter.", "Vérapamil : ECG."), sources="[EHF, 2023]"),
dict(format="A", stem="Au début d'une période active, un homme de 42 ans a 4 crises par jour. Le vérapamil vient d'être débuté et mettra plusieurs semaines à agir.", prompt="Quelle mesure de transition proposez-vous ?",
 items=["*Une corticothérapie courte ou un bloc du nerf grand occipital || Ils réduisent les crises en attendant le traitement de fond.", "Un opioïde au long cours || Il est inefficace et expose à la dépendance.", "Un triptan oral quotidien || Il est inefficace en fond.", "Une benzodiazépine || Elle est inefficace.", "Aucune mesure, il faut attendre || La transition soulage."],
 notions="N18 N17", angle="direct", diff=3, ladder=L("Période active intense.", "Délai d'action du fond.", "4 crises par jour.", "Traitement de transition.", "Corticoïdes ou bloc.", "Opioïdes.", "Transition : corticoïde."), sources="[EHF, 2023]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 44 ans, souffrant d'une algie vasculaire chronique depuis 3 ans, vous dit qu'il ne supporte plus les crises et qu'il a pensé à en finir.", prompt="Quelle est la priorité ?",
 items=["*Évaluer le risque suicidaire et renforcer la prise en charge de la douleur et de l'humeur || L'intensité des crises expose au suicide.", "Le rassurer et le revoir dans 6 mois || Le risque doit être évalué.", "Augmenter seulement l'oxygène || La détresse doit être évaluée.", "Lui prescrire un opioïde fort || Il n'est pas efficace.", "Ignorer ses propos || Les idées suicidaires se prennent au sérieux."],
 notions="N21 N19", angle="application", diff=2, ladder=L("Idées suicidaires.", "Douleur extrême.", "Forme chronique.", "Risque suicidaire.", "Évaluer, protéger, traiter.", "Minimiser.", "Évaluer le risque."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous enseignez à Fribourg les caractéristiques de l'algie vasculaire de la face.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Elle touche plus souvent l'homme que la femme. || La prédominance masculine est nette.", "V: Les crises durent 15 à 180 minutes. || C'est le critère de durée.", "F: Le patient reste immobile dans le noir. || Il s'agite.", "F: Les signes dysautonomiques sont controlatéraux à la douleur. || Ils sont homolatéraux."],
 notions="N03 N01 N07 N06", angle="direct", diff=2, ladder=L("Enseignement.", "Céphalée trigémino-autonomique.", "Durée, comportement.", "Critères.", "Reconnaître.", "Confondre avec la migraine.", "Homme, 15-180 min, agitation."), sources="[ICHD-3, IHS, 2018]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un homme de 39 ans souffrant d'une algie vasculaire veut un traitement de crise à domicile.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'oxygène à domicile se prescrit avec un masque à haute concentration et un débit élevé. || Le débit est déterminant.", "V: Le sumatriptan sous-cutané est une alternative rapide. || Il agit en quelques minutes.", "F: L'oxygène à 2 L/min par lunettes suffit. || Le débit est trop faible.", "F: Le remboursement de l'oxygène à domicile est automatique sans condition. || Il suit les conditions des assureurs."],
 notions="N14 N15 N24", angle="piège", diff=3, ladder=L("Traitement à domicile.", "Hyperoxie.", "Matériel.", "Débit.", "O2 haut débit, sumatriptan SC.", "Bas débit.", "12-15 L/min."), sources="[EHF, 2023]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un patient de 50 ans souffrant d'une algie vasculaire épisodique depuis 15 ans s'interroge sur son évolution.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La forme épisodique peut devenir chronique. || Les rémissions peuvent raccourcir.", "V: L'activité tend souvent à diminuer avec l'âge. || Les périodes s'espacent.", "V: Le lithium et le topiramate sont des alternatives de fond. || Surtout dans la forme chronique.", "F: L'abus de triptans est impossible dans cette maladie. || Il peut survenir."],
 notions="N22 N19 N20 N02", angle="application", diff=2, ladder=L("Évolution.", "Variabilité.", "Épisodique ancienne.", "Pronostic.", "Informer.", "Croire à une évolution figée.", "Épisodique ↔ chronique."), sources="[May, Nat Rev Dis Primers, 2018]"),
dict(format="A", stem="Une femme de 62 ans arrive aux urgences de Bâle avec une douleur intense de l'œil gauche depuis 3 heures, un œil rouge, une baisse de vision, une pupille moyenne aréactive et des vomissements.", prompt="Quel diagnostic évoquez-vous en premier ?",
 items=["*Un glaucome aigu par fermeture de l'angle || Œil rouge, baisse visuelle, pupille aréactive.", "Une algie vasculaire de la face || Elle ne donne pas de baisse visuelle ni de pupille aréactive.", "Une migraine ophtalmique || Elle ne donne pas d'œil rouge avec pupille fixe.", "Une conjonctivite || Elle ne donne pas de baisse visuelle ni de pupille fixe.", "Une névrite optique || L'œil n'est pas rouge."],
 notions="N13 N06", angle="piège", diff=2, ladder=L("Œil rouge douloureux.", "Hypertension oculaire.", "Pupille aréactive.", "Urgence ophtalmologique.", "Ophtalmologue urgent.", "Algie vasculaire.", "Œil rouge + vision : glaucome."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 31 ans présente des crises typiques d'algie vasculaire. L'examen neurologique est normal. Il n'a jamais eu d'imagerie.", prompt="Quelle attitude est recommandée ?",
 items=["*Réaliser une IRM cérébrale au moins une fois || Une lésion, notamment hypophysaire, peut mimer le tableau.", "Ne jamais faire d'imagerie || Une IRM est recommandée une fois.", "Faire un CT tous les 6 mois || Il n'est pas utile.", "Faire une ponction lombaire || Elle n'est pas indiquée.", "Faire un EEG || Il n'est pas indiqué."],
 notions="N08 N10", angle="direct", diff=2, ladder=L("Algie typique.", "Causes secondaires rares.", "Pas d'imagerie.", "IRM une fois.", "IRM.", "Jamais d'imagerie.", "IRM au moins une fois."), sources="[EHF, 2023]"),
dict(format="A", stem="Un patient prend son sumatriptan en comprimé au début de chacune de ses crises orbitaires de 45 minutes, sans soulagement avant la fin de celle-ci.", prompt="Comment expliquez-vous l'échec ?",
 items=["*La voie orale agit trop lentement pour des crises de moins de 3 heures || La voie sous-cutanée agit en minutes.", "Le sumatriptan est inefficace dans cette maladie || La voie sous-cutanée est efficace.", "La dose de 50 mg est trop forte || La voie est le problème.", "Il faut le prendre à jeun || L'absorption reste trop lente.", "Il faut le prendre après la crise || Il doit couper la crise."],
 notions="N16 N15", angle="application", diff=2, ladder=L("Échec du triptan oral.", "Délai d'absorption.", "Crises courtes.", "Voie d'administration.", "Sumatriptan SC ou O2.", "Conclure à l'inefficacité.", "Courte crise : voie rapide."), sources="[EHF, 2023]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un homme de 36 ans présente des crises douloureuses orbitaires droites.", prompt="Quels signes homolatéraux orientent vers une algie vasculaire ? (4 réponses)",
 items=["*Larmoiement || Signe dysautonomique.", "*Rougeur conjonctivale || Signe dysautonomique.", "*Rhinorrhée || Signe dysautonomique.", "*Ptosis ou myosis || Signe sympathique.", "Mydriase aréactive || Elle évoque un glaucome ou un III.", "Baisse visuelle durable || Elle évoque une urgence ophtalmologique.", "Fièvre || Elle évoque une infection.", "Raideur de nuque || Elle évoque une méningite.", "Hémiparésie || Elle évoque un AVC.", "Aura visuelle de 20 minutes || Elle évoque une migraine.", "Photophobie bilatérale isolée || Elle n'est pas spécifique.", "Nausées isolées || Elles ne sont pas spécifiques."],
 notions="N06 N04", angle="direct", diff=2, ladder=L("Signes associés.", "Réflexe trigémino-autonomique.", "Homolatéraux.", "Signes spécifiques.", "Reconnaître.", "Confondre.", "Larmoiement, rhinorrhée, Horner."), sources="[ICHD-3, IHS, 2018]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un homme de 41 ans en période active d'algie vasculaire a besoin d'un traitement.", prompt="Quels traitements sont recommandés en crise ou en fond ? (3 réponses)",
 items=["*Oxygène pur à haut débit || Traitement de crise.", "*Sumatriptan sous-cutané || Traitement de crise.", "*Vérapamil || Traitement de fond.", "Propranolol || Inefficace ici.", "Paracétamol || Inefficace.", "Ibuprofène || Inefficace.", "Tramadol || Inefficace.", "Amitriptyline || Peu efficace ici.", "Sumatriptan oral || Trop lent.", "Benzodiazépine || Inefficace.", "Codéine || Inefficace.", "Flunarizine || Peu efficace ici."],
 notions="N14 N15 N17 N16", angle="piège", diff=2, ladder=L("Traitement.", "Crise et fond.", "Période active.", "Options validées.", "O2, SC, vérapamil.", "Antalgiques usuels.", "O2 + SC + vérapamil."), sources="[EHF, 2023]"),
dict(masque=False, sit="monographique", format="A", stem="Un patient de 37 ans demande s'il existe un examen qui confirme son algie vasculaire.", prompt="Quelle réponse est la plus juste ?",
 items=["*Le diagnostic est clinique, et l'IRM sert à exclure une cause secondaire || Aucun examen ne confirme la maladie.", "Un dosage sanguin confirme le diagnostic || Il n'en existe pas.", "L'EEG confirme le diagnostic || Il n'est pas utile.", "La ponction lombaire confirme le diagnostic || Elle n'est pas utile.", "Le scanner des sinus confirme le diagnostic || Il ne l'est pas."],
 notions="N10 N08", angle="application", diff=1, ladder=L("Demande d'examen.", "Diagnostic clinique.", "Algie.", "Rôle de l'IRM.", "Expliquer.", "Examen confirmatoire.", "Clinique + IRM d'exclusion."), sources="[ICHD-3, IHS, 2018]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Algie vasculaire de la face : reconnaître la crise orbitaire dysautonomique avec agitation, la couper par oxygène ou sumatriptan sous-cutané et prévenir par le vérapamil",
 notions=[
  dict(titre="Céphalées faciales brèves", rub=["def", "pos"], comment="Classe par la durée des crises et la réponse thérapeutique.",
   tableau=(["Céphalée", "Durée", "Fréquence", "Discriminant"], [
     ["Algie vasculaire", "15-180 min", "1 un jour sur deux à 8/j", _T("Agitation", "L'hypothalamus active la crise et le patient ne tient pas en place.")],
     ["Hémicrânie paroxystique", "2-30 min", "Très fréquente", _T("Indométacine", "La réponse absolue fait partie des critères.")],
     ["Névralgie du trijumeau", "Secondes", "Multiples", _T("Zone gâchette", "Le contact déclenche la décharge.")],
     ["Migraine", "4-72 h", "Variable", _T("Immobilité", "L'effort aggrave la douleur.")]]),
   points=["Signes dysautonomiques homolatéraux."], sources=["[ICHD-3, IHS, 2018]"]),
  dict(titre="Traitement de crise", rub=["acu"], comment="Choisis un traitement qui agit en minutes.",
   tableau=(["Traitement", "Modalité", "Pourquoi"], [
     ["Oxygène pur", "12-15 L/min, masque à haute concentration, 15 min", [("Hyperoxie", "Elle inhibe l'activation trigéminovasculaire.")]],
     ["Sumatriptan SC", "6 mg", [("Rapide", "La voie sous-cutanée agit en minutes.")]],
     ["Triptan oral, antalgiques", "À éviter", [("Trop lents", "La crise se termine avant leur effet.")]]]),
   points=["Posologies à vérifier dans l'AIPS."], sources=["[EHF, 2023]"]),
  dict(titre="Traitement de fond et transition", rub=["chr", "sur"], comment="Débute un fond dès la période active et couvre le délai d'action.",
   arbre=[("f1", None, "Période active", "Un traitement de fond réduit les crises."),
          ("f2", "f1", "Vérapamil", "Première ligne, ECG avant et pendant la titration.", "avf"),
          ("f3", "f1", "Transition", "Corticothérapie courte ou bloc du grand occipital.", "avf"),
          ("f4", "f2", "PR allongé", "Ne plus augmenter et réévaluer.", "avf"),
          ("f5", "f2", "Échec ou forme chronique", "Lithium, topiramate, centre spécialisé.", "avf")],
   points=["ECG sous vérapamil."], sources=["[EHF, 2023]"]),
  dict(titre="Drapeaux rouges et suivi", rub=["red", "hos", "fol"], comment="Écarte les mimes et protège l'humeur.",
   tableau=(["Situation", "Conduite", "Pourquoi"], [
     ["Première évaluation", "IRM au moins une fois", "Une lésion hypophysaire peut mimer l'algie."],
     ["Horner permanent et douleur cervicale", "Imagerie artérielle urgente", "Une dissection peut mimer."],
     ["Œil rouge, baisse visuelle", "Ophtalmologie urgente", "Un glaucome aigu menace la vue."],
     ["Idées suicidaires", "Évaluation et soutien", "La douleur extrême y expose."],
     ["Oxygène à domicile", [("Conditions des assureurs", "Le remboursement suit des conditions.")], "Prescription adaptée"]]),
   points=["Pas d'alcool en période active."], sources=["[avis d'expert]"]),
 ],
 ssp=dict(code="S7.6", nom="Céphalées", officiel=True, algorithme=[
  ("n1", None, "Céphalée", "Le premier tri cherche les drapeaux rouges."),
  ("n2", "n1", "Crises orbitaires unilatérales", "La durée oriente le diagnostic.", None, "c1"),
  ("n3", "n2", "15-180 min, dysautonomie, agitation", "Algie vasculaire.", "avf", "c1"),
  ("n4", "n2", "2-30 min, très fréquentes", "Hémicrânie paroxystique : indométacine.", None, "c1"),
  ("n5", "n2", "Secondes, zone gâchette", "Névralgie du trijumeau (même SSP).", None, "c1"),
  ("n6", "n2", "Œil rouge, baisse visuelle, mydriase", "Glaucome aigu : ophtalmologie urgente.", None, "c4"),
  ("n7", "n3", "Crise", "Oxygène ou sumatriptan sous-cutané.", "avf", "c2"),
  ("n8", "n3", "Période active", "Vérapamil sous ECG et transition.", "avf", "c3"),
  ("n9", "n1", "Horner permanent, douleur cervicale", "Dissection carotidienne à chercher.", None, "c4")]),
 pec=[
  dict(cle="avf", titre="Algie vasculaire de la face",
   but=["Couper les crises en minutes.", "Réduire le nombre de crises pendant la période active."],
   moyens=dict(accueil=["Confirmer les critères cliniques.", "Prévoir une IRM au moins une fois."],
    pharma=[("Oxygène pur", "12-15 L/min au masque à haute concentration pendant 15 min.", "Il coupe la crise sans effet systémique.", "[EHF, 2023]"),
            ("Sumatriptan (triptan)", "6 mg sous-cutané ; à vérifier dans l'AIPS.", "Il agit en quelques minutes.", "[AIPS Swissmedic]"),
            ("Vérapamil (inhibiteur calcique)", "Titration progressive sous ECG ; à vérifier dans l'AIPS.", "Il est le traitement de fond de première ligne.", "[EHF, 2023]"),
            ("Prednisone (corticoïde)", "Cure courte de transition ; à vérifier dans l'AIPS.", "Elle couvre le délai d'action du vérapamil.", "[EHF, 2023]")],
    nonpharma=[("hygiène de vie", "Éviter l'alcool en période active, arrêter le tabac.", "L'alcool déclenche les crises."),
               ("geste ou chirurgie", "Bloc du nerf grand occipital.", "Il réduit les crises en transition.")],
    transversal=[("Psychiatrie", "Elle évalue et traite la détresse et le risque suicidaire.")]),
   urgence=None,
   horsUrgence=(["ECG avant et pendant la titration du vérapamil.", "Agenda des crises."],
            [("d'abord", "médecin de famille", "Prescrit oxygène et sumatriptan SC."),
             ("ensuite", "neurologue", "Débute et ajuste le traitement de fond."),
             ("puis", "patient·e", "Tient l'agenda et évite l'alcool.")]),
   pronostic="La forme épisodique peut devenir chronique ; l'activité diminue souvent avec l'âge.",
   suivi=[("Crises", "À chaque consultation", "Réduction"), ("ECG sous vérapamil", "À chaque palier", "PR normal"), ("Humeur", "À chaque consultation", "Absence d'idées suicidaires")],
   sortie="Le suivi est ambulatoire.",
   prevention=["Elle n'existe pas de façon spécifique.", "Elle repose sur le traitement de fond en période active et l'éviction de l'alcool.", "Elle prévient la détresse par le suivi de l'humeur."]),
 ])
AVERIFIER = ["Conditions de remboursement de l'oxygène à domicile dans l'algie vasculaire en Suisse à vérifier.",
             "Référence exacte et année de la recommandation de l'European Headache Federation à vérifier.",
             "Doses maximales de vérapamil et rythme des ECG à vérifier dans l'AIPS."]
