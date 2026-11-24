ID = "G04.9_1__S7_7-E13"
PLAN = "monographique"
NOTIONS = [
"def|critère|2||[Venkatesan, Clin Infect Dis, 2013, IEC]|L'encéphalite associe une altération de la conscience ou du comportement à des signes d'inflammation cérébrale, comme fièvre, crises, signes focaux, pléiocytose ou anomalies à l'IRM ou à l'EEG.",  # N01
"epi|chiffre|1||[Tunkel, Clin Infect Dis, 2008, IDSA]|Le virus herpès simplex de type 1 est la cause la plus fréquente d'encéphalite virale sporadique grave.",  # N02
"epi|contexte suisse|2|S|[OFSP, plan de vaccination suisse]|L'encéphalite à tiques (FSME) est endémique en Suisse, et la vaccination est recommandée aux personnes exposées vivant ou séjournant dans les zones à risque.",  # N03
"bas|mécanisme|1||[avis d'expert]|Le virus herpès simplex atteint préférentiellement les lobes temporaux internes et le cortex insulaire, d'où les troubles mnésiques, comportementaux et du langage.",  # N04
"ana|symptôme|2||[avis d'expert]|Une fièvre avec confusion, troubles du comportement, aphasie ou crises évoque une encéphalite plutôt qu'une méningite simple.",  # N05
"ana|symptôme|2||[Dalmau, Lancet Neurol, 2019]|L'encéphalite à anticorps anti-NMDAR débute souvent par des troubles psychiatriques chez une femme jeune, puis s'aggrave par crises, dyskinésies, dysautonomie et baisse de vigilance.",  # N06
"exa|signe|1||[avis d'expert]|Des signes focaux, une aphasie ou une hémianopsie orientent vers une atteinte temporale ou corticale.",  # N07
"red|décision|3||[Tunkel, Clin Infect Dis, 2008 ; Solomon, J Infect, 2012]|L'aciclovir IV débute dès la suspicion d'encéphalite, sans attendre l'imagerie ni la PCR.",  # N08
"gold|résultat|2||[avis d'expert]|Le LCR montre en général une pléiocytose lymphocytaire, des protéines modérément élevées et un glucose normal.",  # N09
"gold|examen|3||[Tunkel, Clin Infect Dis, 2008]|La PCR HSV du LCR confirme l'encéphalite herpétique, mais elle peut être négative dans les 72 premières heures et doit alors être répétée.",  # N10
"alt|examen|1||[avis d'expert]|L'IRM montre un hypersignal temporal interne et insulaire, et l'EEG peut montrer des anomalies temporales périodiques.",  # N11
"alt|examen|1||[Graus, Lancet Neurol, 2016]|Les anticorps neuronaux se recherchent dans le LCR et le sérum, le LCR étant plus sensible pour les anti-NMDAR.",  # N12
"pos|diagnostic différentiel|1||[avis d'expert]|Un premier épisode psychiatrique aigu avec crises, dyskinésies ou instabilité végétative doit faire chercher une encéphalite auto-immune.",  # N13
"pos|diagnostic différentiel|1||[avis d'expert]|La méningite bactérienne, l'état de mal non convulsif, l'encéphalopathie métabolique et l'encéphalopathie de Wernicke font partie du diagnostic différentiel.",  # N14
"acu|posologie|3|S|[Tunkel, Clin Infect Dis, 2008 ; AIPS Swissmedic]|L'aciclovir se donne à 10 mg/kg IV toutes les 8 heures pendant 14 à 21 jours, adapté à la fonction rénale, posologie à vérifier dans l'AIPS.",  # N15
"acu|piège|2||[AIPS Swissmedic]|L'aciclovir peut précipiter dans les tubules rénaux, ce qui impose hydratation et surveillance de la créatinine.",  # N16
"acu|décision|2||[Graus, Lancet Neurol, 2016]|L'encéphalite auto-immune se traite par corticoïdes, immunoglobulines IV ou échanges plasmatiques, puis par rituximab ou cyclophosphamide en deuxième ligne.",  # N17
"acu|décision|2||[Dalmau, Lancet Neurol, 2019]|Chez la femme atteinte d'encéphalite anti-NMDAR, on cherche un tératome ovarien, dont l'ablation améliore le pronostic.",  # N18
"acu|décision|1||[avis d'expert]|Les crises se traitent par antiépileptique, et un EEG cherche un état de mal non convulsif chez le patient peu réactif.",  # N19
"chr|piège|1||[Armangue, Lancet Neurol, 2018]|Une aggravation neurologique quelques semaines après une encéphalite herpétique peut révéler une encéphalite auto-immune anti-NMDAR secondaire.",  # N20
"hos|complication|1||[avis d'expert]|L'œdème cérébral, l'état de mal et l'hypertension intracrânienne peuvent compliquer l'encéphalite herpétique.",  # N21
"pro|pronostic|1||[avis d'expert]|Malgré l'aciclovir, des séquelles mnésiques, comportementales et épileptiques persistent chez une partie importante des patients, d'autant plus que le traitement a été tardif.",  # N22
"sur|décision|1||[avis d'expert]|Le suivi évalue mémoire, comportement, crises et fonction rénale pendant et après le traitement.",  # N23
"fol|contexte suisse|1|S|[avis d'expert]|Une réadaptation neuropsychologique et un accompagnement social et assurantiel préparent le retour à domicile et au travail.",  # N24
"fol|prévention|1|S|[OFSP, plan de vaccination suisse]|La vaccination contre l'encéphalite à tiques comporte une primovaccination en trois doses et des rappels.",  # N25
]
ANGLES = [
"L'aciclovir ne doit jamais attendre la PCR.",
"Une PCR HSV précoce peut être faussement négative.",
"Un premier épisode psychiatrique avec crises évoque une encéphalite auto-immune.",
"Le tératome ovarien se cherche chez la femme avec anti-NMDAR.",
"L'aciclovir est néphrotoxique.",
"La Suisse est une zone d'endémie de l'encéphalite à tiques.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un homme de 58 ans est amené aux urgences de Fribourg par sa femme. Depuis 2 jours, il a de la fièvre à 38,8 °C, il tient des propos incohérents, cherche ses mots et a présenté une crise convulsive ce matin. Il n'a pas de raideur de nuque.", prompt="Quelle mesure prenez-vous sans délai ?",
 items=["*Débuter l'aciclovir IV après les prélèvements, sans attendre l'imagerie ni la PCR || Chaque heure de retard aggrave le pronostic.", "Attendre le résultat de la PCR HSV || Le retard aggrave les séquelles.", "Prescrire un antipsychotique et observer || Le tableau est organique.", "Débuter des corticoïdes seuls || Ils ne traitent pas le virus.", "Renvoyer à domicile avec antipyrétique || Le tableau est grave."],
 notions="N08 N05 N01", angle="application", diff=2, ladder=L("Fièvre et confusion avec crise.", "Inflammation du parenchyme.", "Aphasie, crise.", "Encéphalite versus méningite.", "Aciclovir immédiat.", "Attendre la PCR.", "Fièvre + confusion : aciclovir."), sources="[Tunkel, Clin Infect Dis, 2008]"),
dict(format="A", serie=("S1", 2, 4), stem="Le LCR de cet homme, prélevé au 2e jour, montre 95 leucocytes/µL lymphocytaires, des protéines à 0,8 g/L et un glucose normal. La PCR HSV est négative.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Poursuivre l'aciclovir et répéter la PCR quelques jours plus tard || Une PCR précoce peut être faussement négative.", "Arrêter l'aciclovir || La PCR précoce ne l'exclut pas.", "Remplacer par une céphalosporine seule || Le profil est viral.", "Conclure à une méningite bactérienne || Le profil est lymphocytaire.", "Arrêter tout traitement et observer || Le tableau reste grave."],
 notions="N10 N09 N15", angle="piège", diff=3, ladder=L("PCR négative précoce.", "Charge virale faible au début.", "LCR lymphocytaire.", "Faux négatif.", "Poursuivre et répéter.", "Arrêter l'aciclovir.", "PCR précoce négative : répéter."), sources="[Tunkel, Clin Infect Dis, 2008]"),
dict(format="Kprim", serie=("S1", 3, 4), stem="L'IRM de cet homme montre un hypersignal temporal interne et insulaire gauche. La deuxième PCR revient positive pour HSV-1.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'aciclovir se poursuit 14 à 21 jours. || La durée prévient la rechute.", "V: L'hydratation et la créatinine se surveillent. || L'aciclovir peut précipiter dans les tubules.", "V: La topographie temporale explique ses troubles du langage. || Le lobe temporal gauche porte le langage.", "F: L'aciclovir se donne à dose fixe quelle que soit la fonction rénale. || Il s'adapte à la clairance."],
 notions="N15 N16 N04 N11", angle="direct", diff=3, ladder=L("Encéphalite herpétique confirmée.", "Tropisme temporal.", "Hypersignal temporal.", "Durée et toxicité.", "Aciclovir 14-21 j, rein.", "Dose fixe.", "Rein sous aciclovir."), sources="[Tunkel, Clin Infect Dis, 2008]"),
dict(format="A", serie=("S1", 4, 4), stem="Cinq semaines après sa sortie, cet homme, qui s'améliorait, présente de nouveaux troubles du comportement, des mouvements anormaux et des crises. La PCR HSV du LCR est désormais négative.", prompt="Quelle hypothèse évoquez-vous ?",
 items=["*Une encéphalite auto-immune anti-NMDAR secondaire à l'encéphalite herpétique || Elle survient quelques semaines après.", "Une rechute virale certaine || La PCR négative et les mouvements anormaux orientent ailleurs.", "Une démence d'Alzheimer || L'évolution est trop rapide.", "Un trouble psychiatrique primaire || Les crises et les mouvements anormaux l'excluent.", "Un effet tardif de l'aciclovir || Il n'explique pas le tableau."],
 notions="N20 N12 N17", angle="piège", diff=4, ladder=L("Rechute après encéphalite herpétique.", "Auto-immunité post-infectieuse.", "Mouvements anormaux, crises.", "Auto-immune versus virale.", "Anticorps, immunothérapie.", "Reprendre seulement l'aciclovir.", "Rechute : chercher anti-NMDAR."), sources="[Armangue, Lancet Neurol, 2018]"),
dict(format="A", stem="Une femme de 23 ans est hospitalisée en psychiatrie à Genève pour une agitation et des idées délirantes apparues en 10 jours. Elle présente ensuite une crise convulsive, des mouvements de mâchonnement et une tachycardie fluctuante.", prompt="Quel examen est prioritaire ?",
 items=["*La recherche d'anticorps anti-NMDAR dans le LCR et le sérum || Le tableau évoque une encéphalite auto-immune.", "Une augmentation de l'antipsychotique sans autre examen || Le tableau est organique.", "Un dosage de la prolactine seul || Il ne trouve pas la cause.", "Un test de grossesse seul || Il ne suffit pas.", "Aucun examen, il s'agit d'une schizophrénie || Les crises et dyskinésies l'excluent."],
 notions="N06 N13 N12", angle="application", diff=3, ladder=L("Psychose aiguë avec crises.", "Anticorps anti-récepteur NMDA.", "Dyskinésies, dysautonomie.", "Organique versus psychiatrique.", "Anticorps LCR.", "Antipsychotique seul.", "Psychose + crise : anti-NMDAR."), sources="[Dalmau, Lancet Neurol, 2019]"),
dict(format="A", stem="Chez une femme de 23 ans, les anticorps anti-NMDAR sont positifs dans le LCR.", prompt="Quel examen complémentaire est indispensable ?",
 items=["*Une imagerie pelvienne à la recherche d'un tératome ovarien || Son ablation améliore le pronostic.", "Une coronarographie || Rien ne l'indique.", "Une scintigraphie thyroïdienne || Rien ne l'indique.", "Une biopsie cérébrale || Elle n'est pas nécessaire.", "Une endoscopie digestive || Rien ne l'indique."],
 notions="N18 N06", angle="direct", diff=3, ladder=L("Anti-NMDAR positifs.", "Tératome qui exprime le récepteur.", "Femme jeune.", "Cause tumorale.", "Imagerie pelvienne.", "Oublier le tératome.", "Anti-NMDAR : tératome."), sources="[Dalmau, Lancet Neurol, 2019]"),
dict(format="A", stem="Chez cette jeune femme, un tératome ovarien est retiré.", prompt="Quel traitement immunologique de première ligne associez-vous ?",
 items=["*Corticoïdes, immunoglobulines IV ou échanges plasmatiques || Ils constituent la première ligne.", "Aciclovir seul || Il ne traite pas l'auto-immunité.", "Antibiotique seul || Rien ne l'indique.", "Aucun traitement après la chirurgie || L'immunothérapie reste nécessaire.", "Lithium || Il n'a pas sa place."],
 notions="N17 N18", angle="application", diff=3, ladder=L("Tumeur retirée.", "Anticorps persistants.", "Encéphalite active.", "Immunothérapie.", "Corticoïdes, IgIV, échanges.", "S'arrêter à la chirurgie.", "Chirurgie + immunothérapie."), sources="[Graus, Lancet Neurol, 2016]"),
dict(format="A", stem="Un homme de 45 ans traité par aciclovir IV depuis 4 jours a une créatinine qui passe de 80 à 210 µmol/L.", prompt="Quelle est la conduite la plus adaptée ?",
 items=["*Hydrater, adapter la dose d'aciclovir à la clairance et surveiller la fonction rénale || L'aciclovir précipite dans les tubules.", "Arrêter définitivement l'aciclovir || Il reste nécessaire à dose adaptée.", "Augmenter la dose || Elle aggraverait la néphrotoxicité.", "Ajouter un AINS || Il aggraverait l'insuffisance rénale.", "Ne rien changer || La créatinine monte."],
 notions="N16 N15", angle="application", diff=3, ladder=L("Insuffisance rénale sous aciclovir.", "Cristallurie.", "Créatinine en hausse.", "Toxicité rénale.", "Hydrater, adapter.", "Arrêter ou ignorer.", "Aciclovir : hydrater."), sources="[AIPS Swissmedic]"),
dict(format="A", stem="Un homme de 52 ans traité par aciclovir pour une confusion fébrile reste peu réactif depuis 2 jours, sans convulsions visibles, avec de discrètes clonies palpébrales.", prompt="Quel examen demandez-vous ?",
 items=["*Un EEG à la recherche d'un état de mal non convulsif || Il peut expliquer la non-réactivité.", "Une IRM médullaire || Elle n'explique pas le tableau.", "Un électromyogramme || Il n'est pas indiqué.", "Une scintigraphie osseuse || Elle n'est pas indiquée.", "Aucun examen, la sédation suffit à expliquer || Un état de mal doit être exclu."],
 notions="N19 N21", angle="application", diff=3, ladder=L("Patient peu réactif.", "Activité épileptique continue.", "Clonies discrètes.", "État de mal non convulsif.", "EEG.", "Attribuer à l'encéphalite.", "Peu réactif : EEG."), sources="[avis d'expert]"),
dict(format="A", stem="Un forestier de 50 ans du canton de Berne, non vacciné, présente une fièvre il y a 3 semaines, puis, après une amélioration de quelques jours, une nouvelle fièvre avec céphalées, confusion et tremblements.", prompt="Quel diagnostic évoquez-vous ?",
 items=["*Une encéphalite à tiques (FSME) || Évolution biphasique chez un sujet exposé non vacciné.", "Une borréliose de Lyme cutanée || Elle ne donne pas cette évolution encéphalitique.", "Une grippe saisonnière || Elle n'explique pas l'encéphalite biphasique.", "Une encéphalopathie hépatique || Le contexte ne l'évoque pas.", "Une maladie de Parkinson || Le tableau est aigu et fébrile."],
 notions="N03 N05", angle="application", diff=3, ladder=L("Fièvre biphasique.", "Flavivirus transmis par tique.", "Forestier non vacciné.", "Exposition en Suisse.", "Sérologie FSME.", "Penser Lyme seulement.", "Biphasique + tique : FSME."), sources="[OFSP]"),
dict(masque=False, sit="monographique", format="A", stem="Une randonneuse de 35 ans habitant Zurich vous demande si elle doit se faire vacciner contre l'encéphalite à tiques.", prompt="Quelle réponse est la plus adaptée ?",
 items=["*La vaccination est recommandée aux personnes exposées dans les zones à risque, avec une primovaccination en trois doses || La FSME est endémique en Suisse.", "La vaccination est inutile en Suisse || La maladie y est endémique.", "Une dose unique suffit à vie || La primovaccination comporte trois doses et des rappels.", "La vaccination protège aussi de la borréliose || Elle ne protège pas de Lyme.", "Elle doit se faire vacciner seulement après une piqûre || La vaccination est préventive."],
 notions="N25 N03", angle="direct", diff=2, ladder=L("Conseil vaccinal.", "Prévention de la FSME.", "Randonneuse.", "Zones à risque.", "Vacciner.", "Confondre avec Lyme.", "FSME : 3 doses + rappels."), sources="[OFSP, plan de vaccination suisse]"),
dict(format="A", stem="Un homme de 61 ans, alcoolique, est confus et fébrile. Il présente un nystagmus et une ataxie. La glycémie est normale.", prompt="Quelle mesure ajoutez-vous à l'aciclovir et aux antibiotiques empiriques ?",
 items=["*De la thiamine IV || Une encéphalopathie de Wernicke est au diagnostic différentiel.", "Du glucose seul || Il pourrait aggraver une carence en thiamine.", "Un antipsychotique || Il n'est pas prioritaire.", "Un bêtabloquant || Il n'est pas indiqué.", "Aucune mesure supplémentaire || La carence en thiamine doit être couverte."],
 notions="N14 N08", angle="piège", diff=3, ladder=L("Confusion chez un alcoolique.", "Carence en thiamine possible.", "Nystagmus, ataxie.", "Diagnostic différentiel.", "Thiamine IV.", "Ne penser qu'à l'infection.", "Alcool : B1."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous expliquez l'encéphalite herpétique à des internes à Lausanne.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: HSV-1 est la cause la plus fréquente d'encéphalite virale sporadique grave. || Il réactive ou infecte le lobe temporal.", "V: Le LCR montre en général une pléiocytose lymphocytaire. || Le glucose reste normal.", "F: Le traitement attend la confirmation par PCR. || L'aciclovir débute dès la suspicion.", "F: Le glucose du LCR est effondré. || Il est en général normal."],
 notions="N02 N09 N08 N10", angle="direct", diff=2, ladder=L("Enseignement.", "Virus neurotrope.", "LCR lymphocytaire.", "Traitement empirique.", "Aciclovir d'emblée.", "Attendre la PCR.", "HSV-1, LCR lymphocytaire."), sources="[Tunkel, Clin Infect Dis, 2008]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un homme de 60 ans sort de l'hôpital après une encéphalite herpétique traitée.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Des troubles mnésiques peuvent persister. || Le lobe temporal interne a été lésé.", "V: Une réadaptation neuropsychologique est utile. || Elle aide la récupération.", "V: Une épilepsie séquellaire est possible. || Le cortex temporal lésé devient épileptogène.", "F: Un traitement précoce n'influence pas le pronostic. || Le délai d'aciclovir pèse sur les séquelles."],
 notions="N22 N24 N23", angle="application", diff=2, ladder=L("Sortie.", "Lésions temporales.", "Séquelles.", "Pronostic.", "Réadaptation, suivi.", "Négliger le délai.", "Traiter tôt limite les séquelles."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Une femme de 28 ans est suspecte d'encéphalite auto-immune à Berne.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Les anticorps anti-NMDAR sont plus souvent détectés dans le LCR que dans le sérum. || Le LCR est plus sensible.", "V: Les corticoïdes, les immunoglobulines ou les échanges plasmatiques constituent la première ligne. || Ils réduisent l'inflammation.", "F: L'attente du résultat des anticorps est obligatoire avant tout traitement. || L'immunothérapie peut débuter sur des critères cliniques.", "F: Un tératome ovarien est sans rapport avec la maladie. || Il peut l'induire."],
 notions="N12 N17 N18", angle="piège", diff=3, ladder=L("Suspicion auto-immune.", "Anticorps intrathécaux.", "Femme jeune.", "Délai thérapeutique.", "Traiter sans attendre.", "Attendre les anticorps.", "LCR plus sensible."), sources="[Graus, Lancet Neurol, 2016]"),
dict(masque=False, sit="monographique", format="A", stem="Un patient de 49 ans traité pour une encéphalite herpétique devient somnolent au 3e jour avec une pupille droite plus large. Le CT montre un œdème temporal droit avec effet de masse.", prompt="Quelle conduite est prioritaire ?",
 items=["*Traiter l'hypertension intracrânienne et demander un avis neurochirurgical urgent || L'œdème menace d'engagement.", "Arrêter l'aciclovir || Il reste indispensable.", "Faire une ponction lombaire immédiate || Elle est dangereuse avec effet de masse.", "Attendre l'évolution || L'engagement menace.", "Donner un antipsychotique || Il ne traite pas l'œdème."],
 notions="N21 N07", angle="application", diff=4, ladder=L("Somnolence et anisocorie.", "Œdème temporal.", "Effet de masse.", "Engagement imminent.", "Traiter l'HTIC, neurochirurgie.", "Ponctionner.", "Anisocorie : engagement."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Une femme de 30 ans présente depuis 2 jours une céphalée fébrile, sans confusion ni signe focal. Le LCR est lymphocytaire avec glucose normal.", prompt="Quel élément distinguerait une encéphalite d'une méningite virale simple ?",
 items=["*L'apparition d'une confusion, de crises ou de signes focaux || Ils signent l'atteinte du parenchyme.", "La fièvre || Elle est commune aux deux.", "La céphalée || Elle est commune aux deux.", "La pléiocytose lymphocytaire || Elle est commune aux deux.", "La raideur de nuque || Elle oriente vers une atteinte méningée."],
 notions="N01 N05", angle="direct", diff=2, ladder=L("Céphalée fébrile.", "Méninges versus parenchyme.", "LCR lymphocytaire.", "Signes encéphalitiques.", "Surveiller la conscience.", "Se fier au LCR seul.", "Confusion = parenchyme."), sources="[Venkatesan, 2013]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un homme de 55 ans est hospitalisé pour fièvre et confusion.", prompt="Choisissez les TROIS diagnostics qui font partie du différentiel d'une encéphalite.",
 items=["*Méningite bactérienne || Elle donne fièvre et confusion.", "*État de mal non convulsif || Il donne une confusion prolongée.", "*Encéphalopathie de Wernicke || Elle donne confusion et ataxie.", "Céphalée de tension || Elle ne donne ni fièvre ni confusion.", "Tremblement essentiel || Il ne donne pas de confusion.", "Névralgie du trijumeau || Elle ne donne pas de confusion.", "Canal carpien || Hors sujet.", "Migraine sans aura typique || Elle ne donne pas de fièvre ni de confusion.", "Hernie discale || Hors sujet.", "Paralysie de Bell || Elle ne donne pas de confusion.", "Myasthénie oculaire || Elle ne donne pas de confusion.", "Syndrome des jambes sans repos || Hors sujet."],
 notions="N14 N01", angle="direct", diff=2, ladder=L("Fièvre et confusion.", "Causes multiples.", "Différentiel.", "Causes graves traitables.", "Tout chercher.", "Fermer le diagnostic trop tôt.", "Méningite, état de mal, Wernicke."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Une femme de 24 ans présente un tableau neuropsychiatrique aigu.", prompt="Quels éléments évoquent une encéphalite anti-NMDAR ? (3 réponses)",
 items=["*Dyskinésies orofaciales || Elles sont typiques.", "*Instabilité végétative || Elle est fréquente.", "*Crises épileptiques || Elles sont fréquentes.", "Évolution sur 10 ans || Elle est trop lente.", "Tremblement de repos isolé || Il évoque un parkinsonisme.", "Hémiparésie brutale isolée || Elle évoque un AVC.", "Aréflexie ascendante || Elle évoque un Guillain-Barré.", "Ptosis fluctuant || Il évoque une myasthénie.", "Céphalée en coup de tonnerre || Elle évoque une HSA.", "Douleur faciale de quelques secondes || Elle évoque un trijumeau.", "Fourmillements des pieds lents || Hors sujet.", "Myopie || Hors sujet."],
 notions="N06 N13", angle="application", diff=3, ladder=L("Tableau neuropsychiatrique.", "Anti-NMDAR.", "Dyskinésies, dysautonomie, crises.", "Organique versus psychiatrique.", "Anticorps.", "Étiqueter psychiatrique.", "Dyskinésies + crises."), sources="[Dalmau, Lancet Neurol, 2019]"),
dict(masque=False, sit="monographique", format="A", stem="Un patient de 64 ans a été traité pour une encéphalite herpétique il y a 4 mois. Il a repris sa vie à domicile mais oublie ses rendez-vous et perd son emploi.", prompt="Quelle démarche est la plus utile ?",
 items=["*Organiser une évaluation neuropsychologique, une réadaptation et un accompagnement social et assurantiel || Les séquelles mnésiques limitent le retour au travail.", "Reprendre l'aciclovir || Il n'y a pas de rechute virale.", "Attendre une récupération spontanée sans suivi || L'accompagnement améliore l'insertion.", "Prescrire une benzodiazépine || Elle aggrave la mémoire.", "Lui interdire tout travail à vie || La réadaptation peut aider."],
 notions="N24 N22", angle="application", diff=2, ladder=L("Séquelles mnésiques.", "Lésion temporale.", "Perte d'emploi.", "Réadaptation.", "Neuropsychologie, AI.", "Abandonner.", "Réadapter."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Encéphalite aiguë : traiter par aciclovir dès la suspicion, confirmer par PCR et IRM, et penser à l'auto-immunité",
 notions=[
  dict(titre="Reconnaître l'encéphalite", rub=["def", "ana", "pos"], comment="Cherche une atteinte du parenchyme : conscience, comportement, crises, signes focaux.",
   tableau=(["Entité", "Indice", "Discriminant"], [
     ["Encéphalite herpétique", "Fièvre, confusion, aphasie, crises", _T("Tropisme temporal", "Le virus atteint le lobe temporal interne.")],
     ["Encéphalite anti-NMDAR", "Psychose, dyskinésies, dysautonomie", _T("Femme jeune, tératome", "La tumeur exprime le récepteur NMDA.")],
     ["Encéphalite à tiques", "Fièvre biphasique, exposition", _T("Non-vacciné", "La FSME est endémique en Suisse.")],
     ["Méningite virale", "Céphalée fébrile sans confusion", _T("Pas de signe parenchymateux", "Seules les méninges sont touchées.")]]),
   points=["Confusion fébrile : penser encéphalite."], sources=["[Venkatesan, 2013]", "[Dalmau, Lancet Neurol, 2019]"]),
  dict(titre="Conduite initiale", rub=["red", "gold", "alt", "acu"], comment="Traite d'abord, confirme ensuite.",
   arbre=[("e1", None, "Fièvre et confusion, crises ou signes focaux", "Une encéphalite est suspectée."),
          ("e2", "e1", "Aciclovir IV immédiat", "Il ne doit attendre ni imagerie ni PCR.", "enc_aigu"),
          ("e3", "e2", "Imagerie puis ponction lombaire", "L'imagerie précède la ponction si signes focaux.", "enc_aigu"),
          ("e4", "e3", "PCR HSV négative précoce", "La PCR se répète, l'aciclovir se poursuit."),
          ("e5", "e3", "Anticorps neuronaux positifs", "Immunothérapie et recherche tumorale.", "enc_aigu"),
          ("e6", "e1", "Peu réactif", "EEG pour un état de mal non convulsif.", "enc_aigu")],
   points=["Thiamine si terrain alcoolique."], sources=["[Tunkel, Clin Infect Dis, 2008]"]),
  dict(titre="Traitements", rub=["acu", "chr"], comment="Adapte le traitement à la cause et surveille la toxicité.",
   tableau=(["Cause", "Traitement", "Piège"], [
     ["HSV", "Aciclovir 10 mg/kg/8 h, 14-21 j", _T("Néphrotoxicité", "Il précipite dans les tubules.")],
     ["Anti-NMDAR", "Corticoïdes, IgIV, échanges, puis rituximab", _T("Tératome", "Son ablation améliore le pronostic.")],
     ["Post-HSV", "Immunothérapie", _T("Rechute à quelques semaines", "L'infection déclenche une auto-immunité.")],
     ["FSME", "Symptomatique", _T("Prévention vaccinale", "Aucun antiviral spécifique.")]]),
   points=["Aciclovir adapté à la clairance."], sources=["[Graus, Lancet Neurol, 2016]", "[Armangue, Lancet Neurol, 2018]"]),
  dict(titre="Complications, séquelles et prévention", rub=["hos", "pro", "fol", "sur"], comment="Anticipe l'œdème, les crises et les séquelles.",
   tableau=(["Problème", "Conduite", "Pourquoi"], [
     ["Œdème, engagement", "Traitement de l'HTIC, neurochirurgie", "La nécrose temporale gonfle."],
     ["État de mal", "EEG, antiépileptique", "Le cortex inflammé décharge."],
     ["Séquelles mnésiques", "Réadaptation neuropsychologique, AI", "L'hippocampe est lésé."],
     ["FSME", [("Vaccin : 3 doses et rappels", "La vaccination est recommandée aux personnes exposées.")], "OFSP"]]),
   points=["Le délai d'aciclovir pèse sur le pronostic."], sources=["[avis d'expert]"]),
 ],
 ssp=dict(code="S7.7", nom="Troubles cognitifs, notamment difficultés de concentration, troubles de la mémoire et de la compréhension", officiel=True, algorithme=[
  ("n1", None, "Trouble cognitif ou comportemental aigu", "Le premier tri cherche fièvre, crises et signes focaux."),
  ("n2", "n1", "Fièvre, crises ou signes focaux", "Une encéphalite impose l'aciclovir immédiat.", "enc_aigu", "c2"),
  ("n3", "n2", "LCR lymphocytaire, PCR HSV positive", "Encéphalite herpétique : aciclovir 14-21 jours.", "enc_aigu", "c3"),
  ("n4", "n2", "Psychose, dyskinésies, femme jeune", "Anticorps anti-NMDAR et tératome.", "enc_aigu", "c3"),
  ("n5", "n2", "Exposition aux tiques, non-vacciné", "Sérologie FSME.", None, "c1"),
  ("n6", "n1", "Sans fièvre, fluctuant, inattention", "État confusionnel : chercher une cause métabolique ou toxique."),
  ("n7", "n1", "Progressif sur des mois", "Trouble neurocognitif (même SSP)."),
  ("n8", "n3", "Après traitement", "Réadaptation et suivi des séquelles.", "enc_aigu", "c4")]),
 pec=[
  dict(cle="enc_aigu", titre="Encéphalite aiguë",
   but=["Traiter la cause le plus tôt possible.", "Prévenir complications et séquelles."],
   moyens=dict(accueil=["Évaluer conscience, crises et signes focaux.", "Prélever hémocultures et préparer imagerie et ponction."],
    pharma=[("Aciclovir (antiviral)", "10 mg/kg IV toutes les 8 heures, 14 à 21 jours, adaptation rénale ; à vérifier dans l'AIPS.", "Il inhibe la réplication de HSV.", "[Tunkel, Clin Infect Dis, 2008]"),
            ("Méthylprednisolone (corticoïde)", "Bolus en cas d'encéphalite auto-immune ; à vérifier dans l'AIPS.", "Il réduit l'inflammation auto-immune.", "[Graus, Lancet Neurol, 2016]"),
            ("Immunoglobulines IV", "2 g/kg sur 5 jours en cas d'encéphalite auto-immune ; à vérifier dans l'AIPS.", "Elles neutralisent les anticorps.", "[Graus, Lancet Neurol, 2016]"),
            ("Lévétiracétam (antiépileptique)", "En cas de crises, adaptation rénale ; à vérifier dans l'AIPS.", "Il contrôle les crises.", "[avis d'expert]")],
    nonpharma=[("soins infirmiers", "Hydratation, surveillance neurologique et rénale.", "Elles préviennent la néphrotoxicité et dépistent l'aggravation."),
               ("geste ou chirurgie", "Ablation d'un tératome ovarien.", "Elle supprime la source antigénique."),
               ("rééducation", "Réadaptation neuropsychologique.", "Elle limite le retentissement des séquelles.")],
    transversal=[("Infectiologie", "Elle guide l'antiviral."), ("Gynécologie", "Elle retire un tératome.")]),
   urgence=(["Aciclovir dès la suspicion.", "EEG si non-réactivité."],
            [("d'abord", "médecin responsable", "Prescrit l'aciclovir et les prélèvements."),
             ("en même temps", "infirmier·ère", "Hydrate et surveille la conscience."),
             ("ensuite", "neurologue", "Interprète IRM, LCR et EEG."),
             ("puis", "intensiviste", "Prend en charge œdème et état de mal.")]),
   horsUrgence=(["Suivi des séquelles et de l'épilepsie.", "Vaccination FSME des personnes exposées."],
            [("d'abord", "neurologue", "Suit crises et cognition."),
             ("ensuite", "neuropsychologue", "Évalue et rééduque."),
             ("puis", "médecin de famille", "Coordonne le retour à domicile et au travail.")]),
   pronostic="Des séquelles mnésiques et comportementales persistent chez une partie importante des patients, surtout si l'aciclovir a été tardif.",
   suivi=[("Conscience et crises", "Plusieurs fois par jour", "Amélioration"), ("Créatinine", "Tous les 1 à 2 jours sous aciclovir", "Stable"), ("Cognition", "À 3 et 6 mois", "Récupération")],
   sortie="Le patient sort quand l'antiviral est terminé, les crises contrôlées et la réadaptation organisée.",
   prevention=["Elle repose sur la vaccination FSME des personnes exposées.", "Elle repose sur l'aciclovir précoce.", "Elle limite les séquelles par la réadaptation."]),
 ])
AVERIFIER = ["Zones de recommandation de la vaccination FSME en Suisse et schéma de rappels à vérifier dans le plan de vaccination de l'OFSP.",
             "Mortalité et fréquence des séquelles de l'encéphalite herpétique traitée à confirmer.",
             "Durée exacte de l'aciclovir (14 ou 21 jours) selon les recommandations récentes à vérifier."]
