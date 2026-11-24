ID = "G12.2_sclerose_laterale_am__F1_11-E09"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[Shefner, Gold Coast, Clin Neurophysiol, 2020]|Les critères de Gold Coast exigent un déficit moteur progressif après une fonction normale, une atteinte des neurones moteurs central et périphérique dans au moins une région ou périphérique dans au moins deux, et l'exclusion des autres maladies.",  # N01
"epi|chiffre|1||[avis d'expert]|La maladie est sporadique dans environ 9 cas sur 10 et débute le plus souvent entre 50 et 70 ans.",  # N02
"bas|mécanisme|1||[avis d'expert]|Les neurones moteurs du cortex, des noyaux bulbaires et de la corne antérieure dégénèrent, avec des agrégats de TDP-43 chez la plupart des patients.",  # N03
"ana|signe|3||[avis d'expert]|L'atteinte périphérique (amyotrophie, fasciculations, faiblesse) coexiste avec l'atteinte centrale (réflexes vifs dans un muscle amyotrophié, signe de Babinski, spasticité), sans trouble sensitif.",  # N04
"ana|symptôme|2||[avis d'expert]|Le début est spinal (faiblesse distale asymétrique, main qui fond) ou bulbaire (dysarthrie, dysphagie) ; l'oculomotricité et les sphincters restent longtemps épargnés.",  # N05
"exa|signe|1||[avis d'expert]|Des réflexes vifs dans un membre amyotrophié et des fasciculations de la langue sont très évocateurs.",  # N06
"red|piège|2||[Andersen, EFNS, Eur J Neurol, 2012]|L'orthopnée, les céphalées matinales, le sommeil perturbé et la respiration paradoxale signalent une insuffisance respiratoire et imposent spirométrie et gaz du sang.",  # N07
"gold|examen|2||[Shefner, Gold Coast, Clin Neurophysiol, 2020]|L'EMG montre dénervation active et réinnervation chronique dans plusieurs régions, avec des conductions sensitives normales.",  # N08
"alt|examen|2||[avis d'expert]|L'IRM cervicale et cérébrale, la biologie et l'étude des conductions motrices excluent compression, neuropathie et autres causes.",  # N09
"pos|diagnostic différentiel|2||[avis d'expert]|La myélopathie cervicarthrosique donne troubles sensitifs et sphinctériens ; la neuropathie motrice multifocale donne des blocs de conduction et répond aux immunoglobulines ; la myasthénie est fluctuante et oculaire.",  # N10
"acu|décision|1||[Andersen, EFNS, Eur J Neurol, 2012]|L'annonce se fait dans une consultation dédiée, et une équipe pluridisciplinaire suit ensuite le patient.",  # N11
"chr|molécule|3||[Miller, Cochrane, 2012]|Le riluzole prolonge modestement la survie, de quelques mois, sans arrêter la maladie.",  # N12
"chr|posologie|1||[AIPS Swissmedic]|Le riluzole se prend en général 50 mg deux fois par jour et impose une surveillance des transaminases ; à vérifier dans l'AIPS.",  # N13
"chr|molécule|1||[Swissmedic, 2025]|Le tofersen intrathécal vise les formes liées à une mutation SOD1 et a reçu en Suisse une autorisation à durée limitée en décembre 2025.",  # N14
"chr|décision|2||[Bourke, Lancet Neurol, 2006]|La ventilation non invasive prolonge la survie et améliore la qualité de vie en cas d'insuffisance respiratoire.",  # N15
"chr|décision|2||[Andersen, EFNS, Eur J Neurol, 2012]|La gastrostomie se discute tôt devant une dysphagie ou une perte de poids, avant que la fonction respiratoire ne s'effondre.",  # N16
"chr|molécule|1||[Andersen, EFNS, Eur J Neurol, 2012]|La sialorrhée se traite par anticholinergique ou toxine botulique dans les glandes salivaires, et crampes et spasticité ont leurs traitements.",  # N17
"hos|complication|1||[avis d'expert]|La pneumonie d'aspiration, la dénutrition et l'insuffisance respiratoire causent la plupart des décès.",  # N18
"pro|pronostic|2||[avis d'expert]|La survie médiane est de quelques années après les premiers symptômes ; le début bulbaire, l'amaigrissement et l'atteinte respiratoire précoce l'assombrissent.",  # N19
"sur|examen|1||[avis d'expert]|Le suivi pluridisciplinaire, environ tous les 3 mois, mesure poids, capacité vitale, déglutition et score fonctionnel.",  # N20
"fol|contexte suisse|1|S|[LAI]|En Suisse, l'AI finance les moyens auxiliaires avant l'âge de la retraite, et l'allocation pour impotent aide les patients dépendants.",  # N21
"fol|contexte suisse|1|S|[CC art. 370]|En Suisse, les directives anticipées fixent à l'avance les choix sur la ventilation, la trachéotomie et la gastrostomie.",  # N22
"fol|terrain particulier|1||[avis d'expert]|Une démence frontotemporale accompagne une minorité de patients, et des troubles cognitifs ou comportementaux plus discrets sont fréquents.",  # N23
"bas|mécanisme|1||[avis d'expert]|L'expansion du gène C9orf72 est la cause génétique la plus fréquente en Europe, devant les mutations SOD1.",  # N24
"hos|piège|1||[avis d'expert]|L'oxygène seul, sans ventilation, peut aggraver l'hypercapnie d'un patient en insuffisance respiratoire neuromusculaire.",  # N25
]
ANGLES = [
"Central + périphérique sans trouble sensitif.",
"EMG + IRM pour exclure.",
"Riluzole : quelques mois.",
"Orthopnée = VNI.",
"Gastrostomie tôt.",
"Directives anticipées.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un menuisier de 58 ans, à Martigny, perd la force de la main droite depuis 8 mois. L'éminence thénar a fondu et les muscles fasciculent. Les réflexes du bras droit sont vifs et le signe de Babinski est présent à droite. La sensibilité est normale.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une sclérose latérale amyotrophique || Atteinte centrale et périphérique sans trouble sensitif.", "Un syndrome du tunnel carpien || Il donne des troubles sensitifs.", "Une myélopathie cervicarthrosique || Elle donne des troubles sensitifs.", "Une myasthénie || Elle est fluctuante, sans amyotrophie ni Babinski.", "Une neuropathie motrice multifocale || Elle ne donne pas de signes centraux."],
 notions="N04 N05 N06 N02 N01", angle="application", diff=1, ladder=L("Main qui fond.", "Neurone moteur.", "Fasciculations, Babinski.", "Profil.", "SLA.", "Myélopathie.", "Central + périphérique."), sources="[Shefner, Gold Coast, 2020]"),
dict(format="A", serie=("S1", 2, 4), stem="Vous voulez étayer le diagnostic chez cet homme.", prompt="Quels examens demandez-vous ?",
 items=["*Un EMG et une IRM cervicale || Ils montrent la dénervation et excluent une compression.", "Une biopsie musculaire d'emblée || Elle n'est pas nécessaire.", "Un EEG || Il n'aide pas.", "Une ponction lombaire seule || Elle ne suffit pas.", "Aucun examen || Le diagnostic exige d'exclure d'autres causes."],
 notions="N08 N09 N10", angle="direct", diff=1, ladder=L("Confirmation.", "Électrophysiologie, imagerie.", "Dénervation.", "Examens.", "EMG, IRM.", "Biopsie.", "EMG + exclure."), sources="[Shefner, Gold Coast, 2020]"),
dict(format="A", serie=("S1", 3, 4), stem="Le diagnostic est confirmé et annoncé dans une consultation dédiée.", prompt="Quel traitement de fond proposez-vous ?",
 items=["*Le riluzole || Il prolonge modestement la survie.", "Des corticoïdes || Ils sont inefficaces.", "Des immunoglobulines IV || Elles traitent la neuropathie motrice multifocale.", "La pyridostigmine || Elle traite la myasthénie.", "Aucun traitement n'existe || Le riluzole a un bénéfice."],
 notions="N12 N13 N11", angle="application", diff=1, ladder=L("Diagnostic posé.", "Traitement de fond.", "Survie.", "Molécule.", "Riluzole.", "Corticoïdes.", "Riluzole pour tous."), sources="[Miller, Cochrane, 2012]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Cet homme commence le riluzole et demande ce qu'il peut en attendre.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une équipe pluridisciplinaire le suivra. || Elle améliore la prise en charge.", "V: Ses transaminases seront surveillées. || Le riluzole peut léser le foie.", "F: Le riluzole arrêtera la progression. || Il ne fait que la ralentir un peu.", "F: Ses mouvements oculaires seront atteints en premier. || Ils sont longtemps épargnés."],
 notions="N12 N13 N11 N05", angle="piège", diff=2, ladder=L("Attentes.", "Traitement.", "Riluzole.", "Limites.", "Modeste, surveillance.", "Arrêt de la maladie.", "Ralentit, ne guérit pas."), sources="[Miller, Cochrane, 2012]"),
dict(format="A", stem="Un homme de 66 ans a les mains maladroites et fondantes depuis un an. Il a des paresthésies des doigts, des réflexes vifs aux jambes et des mictions impérieuses.", prompt="Quel examen demandez-vous d'abord ?",
 items=["*Une IRM cervicale || Les troubles sensitifs et sphinctériens évoquent une myélopathie.", "Un EMG seul et l'annonce d'une maladie du neurone moteur || Les signes sensitifs orientent ailleurs.", "Un dosage de l'acétylcholine || Il n'existe pas en pratique.", "Une biopsie nerveuse || Elle n'est pas indiquée.", "Un EEG || Il n'aide pas."],
 notions="N10 N09", angle="piège", diff=2, ladder=L("Mains fondantes.", "Diagnostic différentiel.", "Sensitif, vessie.", "Imagerie.", "IRM cervicale.", "Neurone moteur.", "Sensitif = pas SLA."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 42 ans a une faiblesse asymétrique des avant-bras depuis 2 ans, sans amyotrophie marquée, sans réflexes vifs ni Babinski. L'étude des conductions montre des blocs de conduction moteurs.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Une neuropathie motrice multifocale || Atteinte périphérique pure avec blocs de conduction.", "Une maladie du neurone moteur || Il manque l'atteinte centrale et les blocs l'excluent.", "Une myasthénie || Elle ne donne pas de blocs de conduction.", "Une myopathie || Elle est proximale et symétrique.", "Une syringomyélie || Elle donne des troubles sensitifs."],
 notions="N10 N08", angle="piège", diff=3, ladder=L("Faiblesse asymétrique.", "Neuropathie.", "Blocs de conduction.", "Diagnostic traitable.", "Neuropathie motrice multifocale.", "Neurone moteur.", "Blocs = immunoglobulines."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 63 ans, suivie pour une maladie du neurone moteur, ne peut plus dormir à plat et se réveille avec des maux de tête. Sa respiration devient paradoxale en position couchée.", prompt="Quelle conduite proposez-vous ?",
 items=["*Mesurer la capacité vitale et les gaz du sang, puis proposer une ventilation non invasive || L'insuffisance respiratoire est installée.", "Donner de l'oxygène seul la nuit || Il peut aggraver l'hypercapnie.", "Prescrire une benzodiazépine pour dormir || Elle déprime la respiration.", "Rassurer, ce sont des céphalées de tension || Les signes sont respiratoires.", "Attendre la prochaine consultation trimestrielle || Le risque est vital."],
 notions="N07 N15", angle="application", diff=2, ladder=L("Orthopnée.", "Insuffisance respiratoire.", "Céphalées matinales.", "Traitement.", "VNI.", "Oxygène seul.", "Orthopnée = VNI."), sources="[Bourke, Lancet Neurol, 2006]"),
dict(masque=False, sit="monographique", format="A", stem="Vous enseignez les critères de Gold Coast de la sclérose latérale amyotrophique (2020).", prompt="Quelle combinaison est exigée en plus du déficit moteur progressif ?",
 items=["*Atteinte centrale et périphérique dans une région, ou périphérique dans deux régions, et exclusion des autres causes || C'est la règle de Gold Coast.", "Atteinte centrale isolée dans une région || Elle ne suffit pas.", "Fasciculations isolées || Elles ne suffisent pas.", "Trouble sensitif dans deux régions || Il oriente ailleurs.", "Mutation génétique obligatoire || Elle n'est pas exigée."],
 notions="N01 N09", angle="direct", diff=2, ladder=L("Critères.", "Gold Coast.", "Régions.", "Combinaison.", "Central + périphérique ou périphérique ×2.", "Fasciculations.", "Une ou deux régions."), sources="[Shefner, Gold Coast, 2020]"),
dict(format="A", stem="Un homme de 61 ans à début bulbaire tousse en mangeant, a perdu 10 % de son poids en 4 mois et a fait une pneumonie.", prompt="Quelle mesure proposez-vous ?",
 items=["*Discuter une gastrostomie sans attendre || La dénutrition et l'aspiration menacent.", "Attendre que la capacité vitale s'effondre || Le geste deviendrait risqué.", "Prescrire un régime liquide strict || Les liquides augmentent l'aspiration.", "Arrêter de s'alimenter par la bouche sans alternative || Il se dénutrirait.", "Prescrire des corticoïdes || Ils n'ont pas de rôle."],
 notions="N16 N18", angle="application", diff=2, ladder=L("Dysphagie.", "Nutrition.", "Perte de poids.", "Moment.", "Gastrostomie tôt.", "Attendre.", "Gastrostomie avant le souffle."), sources="[Andersen, EFNS, 2012]"),
dict(format="A", stem="Une femme de 47 ans atteinte d'une maladie du neurone moteur a une mutation SOD1. Sa mère avait la même maladie.", prompt="Quel traitement spécifique se discute ?",
 items=["*Le tofersen par voie intrathécale || Il cible l'ARN SOD1.", "Le nusinersen || Il traite l'amyotrophie spinale.", "Les immunoglobulines IV || Elles traitent la neuropathie motrice multifocale.", "La lévodopa || Elle traite le parkinson.", "Une greffe de moelle osseuse || Elle n'est pas indiquée."],
 notions="N14 N24", angle="application", diff=3, ladder=L("Forme familiale.", "Thérapie génique.", "SOD1.", "Molécule.", "Tofersen.", "Nusinersen.", "SOD1 = tofersen."), sources="[Swissmedic, 2025]"),
dict(format="A", stem="Vous comparez deux patients atteints d'une maladie du neurone moteur, l'un à début bulbaire avec amaigrissement, l'autre à début distal d'un membre.", prompt="Quel élément assombrit le plus le pronostic ?",
 items=["*Le début bulbaire avec amaigrissement || Ils accélèrent dénutrition et atteinte respiratoire.", "Le début distal d'un membre || Il est plutôt moins sévère.", "Le sexe féminin seul || Il ne suffit pas.", "Des fasciculations nombreuses seules || Elles ne déterminent pas le pronostic.", "Un réflexe vif || Il ne pèse pas sur le pronostic."],
 notions="N19 N02", angle="direct", diff=2, ladder=L("Comparaison.", "Pronostic.", "Bulbaire.", "Facteurs.", "Bulbaire, amaigrissement.", "Distal.", "Bulbaire = plus grave."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 65 ans avec maladie du neurone moteur est essoufflé la nuit. Sa capacité vitale a chuté et sa PaCO2 est élevée. Un collègue propose seulement de l'oxygène nasal.", prompt="Que répondez-vous ?",
 items=["*L'oxygène seul peut aggraver l'hypercapnie ; une ventilation non invasive est indiquée || Elle traite l'hypoventilation.", "L'oxygène seul suffit || Il ne corrige pas l'hypoventilation.", "Une benzodiazépine est préférable || Elle déprime la respiration.", "Rien ne peut être fait || La VNI aide.", "Une trachéotomie s'impose d'emblée || La VNI vient d'abord."],
 notions="N25 N07 N15", angle="piège", diff=2, ladder=L("Hypercapnie.", "Ventilation.", "Oxygène seul.", "Danger.", "VNI.", "Oxygène.", "Hypoventilation = VNI."), sources="[Bourke, Lancet Neurol, 2006]"),
dict(format="A", stem="Un homme de 59 ans suivi pour une maladie du neurone moteur devient désinhibé, fait des achats impulsifs et néglige son hygiène. Sa femme ne le reconnaît plus.", prompt="Quelle complication évoquez-vous ?",
 items=["*Une démence frontotemporale associée || Elle partage la pathologie TDP-43.", "Une dépression réactionnelle simple || Elle n'explique pas la désinhibition.", "Un effet du riluzole || Ce n'est pas un effet connu.", "Une hypoglycémie || Elle est aiguë.", "Une maladie d'Alzheimer || Elle commence par la mémoire."],
 notions="N23 N03", angle="application", diff=2, ladder=L("Changement de comportement.", "Atteinte cognitive.", "Désinhibition.", "Lien.", "Démence frontotemporale.", "Dépression.", "Même maladie, autre face."), sources="[avis d'expert]"),
dict(format="A", stem="Un enseignant de 55 ans, à Neuchâtel, atteint d'une maladie du neurone moteur, a besoin d'un fauteuil roulant électrique et d'aménagements de son logement.", prompt="Quel organisme finance d'abord ces moyens auxiliaires ?",
 items=["*L'assurance-invalidité (AI) || Elle finance les moyens auxiliaires avant l'âge de la retraite.", "L'assurance-accidents || La maladie n'est pas un accident.", "L'assurance obligatoire des soins seule || Elle ne couvre pas tous ces moyens.", "Les prestations complémentaires d'abord || Elles viennent en complément.", "Personne, tout reste à sa charge || L'AI intervient."],
 notions="N21", angle="application", diff=2, ladder=L("Moyens auxiliaires.", "Assurances sociales.", "55 ans.", "Organisme.", "AI.", "Accident.", "Avant la retraite = AI."), sources="[LAI]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez la sémiologie de la sclérose latérale amyotrophique.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Des fasciculations peuvent coexister avec un signe de Babinski. || L'atteinte est centrale et périphérique.", "V: La sensibilité reste normale. || Seuls les neurones moteurs dégénèrent.", "F: Les paralysies oculomotrices sont précoces. || L'oculomotricité est longtemps épargnée.", "F: Les troubles sphinctériens sont précoces. || Ils sont tardifs ou absents."],
 notions="N04 N05 N06", angle="direct", diff=1, ladder=L("Révision.", "Sémiologie.", "Central, périphérique.", "Épargnes.", "Sensibilité, yeux épargnés.", "Sphincters.", "Moteur pur."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Vous organisez le suivi d'une femme de 60 ans atteinte d'une maladie du neurone moteur.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La capacité vitale se mesure régulièrement. || Elle guide la VNI.", "V: Le poids se surveille à chaque visite. || L'amaigrissement aggrave le pronostic.", "F: Le riluzole ne demande aucune surveillance biologique. || Les transaminases se surveillent.", "F: La gastrostomie se pose au mieux le plus tard possible. || Elle devient risquée quand le souffle s'effondre."],
 notions="N20 N16 N13 N19", angle="piège", diff=2, ladder=L("Suivi.", "Surveillance.", "Souffle, poids.", "Pièges.", "Spirométrie, poids.", "Gastrostomie tardive.", "Mesurer tôt, agir tôt."), sources="[Andersen, EFNS, 2012]"),
dict(format="Kprim", stem="Un homme de 64 ans atteint d'une maladie du neurone moteur évoluée veut fixer ses choix de fin de vie.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Ses directives anticipées peuvent refuser la trachéotomie. || Le Code civil les rend contraignantes.", "V: Les soins palliatifs s'intègrent tôt. || Ils améliorent la qualité de vie.", "F: L'oxygène seul traite efficacement son hypoventilation. || Il peut aggraver l'hypercapnie.", "F: Ses directives n'ont aucune valeur juridique en Suisse. || Elles s'imposent aux soignants."],
 notions="N22 N25 N15", angle="piège", diff=2, ladder=L("Fin de vie.", "Directives anticipées.", "Trachéotomie.", "Droit suisse.", "Directives contraignantes.", "Oxygène seul.", "Choix écrits respectés."), sources="[CC art. 370]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Vous examinez un patient suspect de sclérose latérale amyotrophique.", prompt="Choisissez les TROIS signes qui soutiennent ce diagnostic.",
 items=["*Fasciculations || Signe périphérique.", "*Amyotrophie || Signe périphérique.", "Troubles sensitifs objectifs étendus || Ils plaident contre une SLA.", "*Signe de Babinski || Signe central.", "Niveau sensitif || Il évoque une myélopathie.", "Ptosis fluctuant || Il évoque une myasthénie.", "Rétention urinaire précoce || Elle évoque une atteinte médullaire.", "Paresthésies distales || Elles évoquent une neuropathie.", "Ophtalmoplégie || Elle oriente ailleurs.", "Tremblement de repos || Il évoque un parkinson.", "Ataxie cérébelleuse || Elle oriente ailleurs.", "Aréflexie généralisée || Elle évoque une polyneuropathie."],
 notions="N04 N06", angle="direct", diff=1, ladder=L("Examen.", "Signes moteurs.", "Central, périphérique.", "Lesquels.", "Fasciculations, amyotrophie, réflexes vifs, Babinski.", "Niveau sensitif.", "Quatre signes moteurs."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Une femme de 62 ans suivie pour une maladie du neurone moteur décrit ses nuits.", prompt="Quels signes évoquent une insuffisance respiratoire ? (3 réponses)",
 items=["*Orthopnée || Le diaphragme faiblit.", "*Céphalées matinales || Elles traduisent l'hypercapnie.", "*Respiration paradoxale couchée || Elle signe la faiblesse diaphragmatique.", "Crampes des mollets || Elles sont fréquentes mais non respiratoires.", "Hypersalivation || Elle est bulbaire.", "Rire spasmodique || Il est pseudobulbaire.", "Constipation || Elle n'est pas respiratoire.", "Fasciculations || Elles sont périphériques.", "Œdèmes des chevilles || Ils ne l'évoquent pas.", "Dysarthrie || Elle est bulbaire.", "Amaigrissement || Il est nutritionnel.", "Spasticité || Elle est centrale."],
 notions="N07 N18", angle="application", diff=2, ladder=L("Nuits.", "Respiration.", "Diaphragme.", "Lesquels.", "Orthopnée, céphalées, paradoxale.", "Crampes.", "Orthopnée = alerte."), sources="[Andersen, EFNS, 2012]"),
dict(format="A", stem="Un homme de 67 ans à début bulbaire bave en permanence, ce qui le gêne pour parler et le fait s'étouffer.", prompt="Quel traitement proposez-vous ?",
 items=["*Un anticholinergique ou une toxine botulique dans les glandes salivaires || Ils réduisent la salive.", "Le riluzole à double dose || Il ne traite pas la sialorrhée.", "Un neuroleptique sédatif || Il n'est pas indiqué.", "Une ablation chirurgicale de la langue || Elle n'est pas indiquée.", "Une restriction hydrique || Elle déshydrate sans effet."],
 notions="N17 N05", angle="application", diff=2, ladder=L("Bave.", "Symptôme bulbaire.", "Sialorrhée.", "Traitement.", "Anticholinergique, toxine.", "Riluzole.", "Moins de salive."), sources="[Andersen, EFNS, 2012]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Sclérose latérale amyotrophique : la reconnaître par l'atteinte motrice centrale et périphérique sans trouble sensitif, exclure les diagnostics traitables, prescrire le riluzole, anticiper ventilation et gastrostomie et organiser le soutien suisse",
 notions=[
  dict(titre="Reconnaître", rub=["def", "ana", "exa", "bas"], comment="Associe signes centraux et périphériques.",
   tableau=(["Atteinte", "Signes", "Pourquoi"], [
     ["Périphérique", "Amyotrophie, fasciculations", "Corne antérieure et noyaux bulbaires"],
     ["Centrale", "Réflexes vifs, Babinski, spasticité", "Cortex moteur"],
     ["Épargnes", _T("Sensibilité, yeux, sphincters", "Elles orientent ailleurs si atteintes."), "Moteur pur"]]),
   points=["Gold Coast : une région centrale + périphérique ou deux régions périphériques."], sources=["[Shefner, Gold Coast, 2020]"]),
  dict(titre="Exclure", rub=["gold", "alt", "pos", "red"], comment="Élimine les maladies traitables.",
   tableau=(["Diagnostic", "Indice", "Examen"], [
     ["Myélopathie cervicale", "Troubles sensitifs, vessie", "IRM cervicale"],
     ["Neuropathie motrice multifocale", _T("Blocs de conduction", "Elle répond aux immunoglobulines."), "Conductions motrices"],
     ["Myasthénie", "Fluctuations, ptosis", "Anticorps, EMG"]]),
   points=["EMG : dénervation dans plusieurs régions."], sources=["[avis d'expert]"]),
  dict(titre="Traiter", rub=["acu", "chr", "hos"], comment="Ralentit la maladie et traite les défaillances.",
   arbre=[("t1", None, "SLA confirmée", "Annonce dédiée, équipe pluridisciplinaire."),
          ("t2", "t1", "Pour tous", "Riluzole, surveillance hépatique.", "sla"),
          ("t3", "t1", "Mutation SOD1", "Tofersen intrathécal.", "sla"),
          ("t4", "t1", "Orthopnée, hypercapnie", "VNI.", "sla"),
          ("t5", "t1", "Dysphagie, amaigrissement", "Gastrostomie tôt.", "sla")],
   points=["Oxygène seul : danger d'hypercapnie."], sources=["[Miller, Cochrane, 2012]", "[Bourke, Lancet Neurol, 2006]"]),
  dict(titre="Suivre et accompagner", rub=["pro", "sur", "fol"], comment="Anticipe les décisions et mobilise les aides.",
   tableau=(["Domaine", "Mesure", "Pourquoi"], [
     ["Suivi", "Poids, capacité vitale tous les 3 mois", "Ils guident VNI et gastrostomie"],
     ["Droit suisse", _T("Directives anticipées", "Elles fixent les choix sur la ventilation."), "CC art. 370"],
     ["Assurances", "AI, allocation pour impotent", "Moyens auxiliaires"]]),
   points=["Début bulbaire : pronostic plus sombre."], sources=["[LAI]", "[CC art. 370]"]),
 ],
 ssp=dict(code="S7.8", nom="Parésie, paralysie", officiel=True, algorithme=[
  ("n1", None, "Faiblesse progressive", "Le profil des signes oriente."),
  ("n2", "n1", "Troubles sensitifs, vessie", "Myélopathie : IRM.", None, "c2"),
  ("n3", "n1", "Périphérique pur, blocs", "Neuropathie motrice multifocale.", None, "c2"),
  ("n4", "n1", "Central + périphérique sans sensitif", "SLA probable.", "sla", "c1"),
  ("n5", "n4", "Confirmation", "EMG, IRM.", "sla", "c2"),
  ("n6", "n5", "Traitement", "Riluzole, VNI, gastrostomie.", "sla", "c3"),
  ("n7", "n6", "Accompagnement", "Directives anticipées, AI.", "sla", "c4")]),
 pec=[
  dict(cle="sla", titre="Sclérose latérale amyotrophique",
   but=["Prolonger la survie et préserver la qualité de vie.", "Respecter les choix du patient."],
   moyens=dict(accueil=["Annoncer le diagnostic dans une consultation dédiée.", "Présenter l'équipe pluridisciplinaire.", "Proposer des directives anticipées."],
    pharma=[("Riluzole (antiglutamatergique)", "En général 50 mg deux fois par jour ; à vérifier dans l'AIPS.", "Il prolonge modestement la survie.", "[Miller, Cochrane, 2012]"),
            ("Tofersen (oligonucléotide antisens)", "Intrathécal selon l'AIPS.", "Il cible les formes SOD1.", "[Swissmedic, 2025]"),
            ("Toxine botulique (neurotoxine)", "Injections salivaires ; à vérifier dans l'AIPS.", "Elle réduit la sialorrhée.", "[Andersen, EFNS, 2012]")],
    nonpharma=[("autre", "Ventilation non invasive.", "Elle prolonge la survie en insuffisance respiratoire."),
               ("nutrition", "Gastrostomie, textures adaptées.", "Elle prévient dénutrition et aspiration."),
               ("rééducation", "Physiothérapie, ergothérapie, logopédie.", "Elles maintiennent l'autonomie et la communication."),
               ("social et assurances", "AI, allocation pour impotent, moyens auxiliaires.", "Elles financent l'adaptation du quotidien.")],
    transversal=[("Pneumologie", "Elle installe et suit la VNI."), ("Soins palliatifs", "Ils soulagent dyspnée et angoisse.")]),
   urgence=None,
   horsUrgence=(["Suivi pluridisciplinaire tous les 3 mois.", "Décisions anticipées."],
            [("d'abord", "neurologue", "Confirme le diagnostic et prescrit le riluzole."),
             ("en même temps", "pneumologue", "Suit la capacité vitale et propose la VNI."),
             ("ensuite", "diététicien·ne", "Suit le poids et prépare la gastrostomie."),
             ("puis", "équipe de soins palliatifs", "Accompagne les choix de fin de vie.")]),
   pronostic="La survie médiane est de quelques années ; le début bulbaire et l'atteinte respiratoire précoce l'assombrissent.",
   suivi=[("Capacité vitale", "Tous les 3 mois", "Décision de VNI à temps"), ("Poids", "Tous les 3 mois", "Pas d'amaigrissement"), ("Transaminases", "Sous riluzole", "Normales")],
   sortie="Le suivi reste ambulatoire et à domicile autant que possible.",
   prevention=["Elle anticipe VNI et gastrostomie.", "Elle prévient les pneumonies d'aspiration.", "Elle soutient les proches."]),
 ])
AVERIFIER = ["Posologie et surveillance suisses du riluzole à vérifier dans l'AIPS.", "Statut et indication exacte du tofersen (autorisation à durée limitée Swissmedic du 19.12.2025) à relire dans l'AIPS.", "Survie médiane chiffrée volontairement non donnée (avis d'expert)."]
