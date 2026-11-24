ID = "I67.1__F1_12-E15"
PLAN = "monographique"
NOTIONS = [
"def|critère|1||[avis d'expert]|L'anévrisme de l'artère communicante postérieure peut comprimer le nerf oculomoteur (III) avant de se rompre, ce qui en fait un signe d'alarme.",  # N01
"epi|terrain particulier|2||[Etminan et Rinkel, Nat Rev Neurol, 2016]|Le tabac, l'hypertension, les antécédents familiaux, la polykystose rénale autosomique dominante et certaines maladies du tissu conjonctif augmentent le risque d'anévrisme.",  # N02
"bas|mécanisme|3||[avis d'expert]|Les fibres pupillomotrices parasympathiques cheminent en surface du III, si bien qu'une compression externe donne d'abord une mydriase.",  # N03
"bas|mécanisme|1||[avis d'expert]|L'ischémie microvasculaire du diabétique touche le centre du nerf et épargne habituellement la pupille.",  # N04
"ana|symptôme|1||[avis d'expert]|La paralysie du III anévrismale s'accompagne souvent d'une douleur rétro-orbitaire ou d'une céphalée homolatérale.",  # N05
"exa|signe|3||[avis d'expert]|La paralysie complète du III donne un ptosis, un œil en bas et en dehors, une diplopie et une mydriase aréactive.",  # N06
"red|décision|3||[avis d'expert ; AHA/ASA, 2015]|Une paralysie du III avec atteinte pupillaire impose une angiographie CT ou IRM en urgence pour chercher un anévrisme.",  # N07
"red|piège|1||[avis d'expert]|Une paralysie du III partielle, même pupille épargnée, ou chez un patient jeune non vasculaire, impose aussi une imagerie vasculaire.",  # N08
"red|symptôme|3||[Perry, JAMA, 2013]|Une céphalée brutale, maximale en moins d'une minute (en coup de tonnerre), évoque une hémorragie sous-arachnoïdienne par rupture d'anévrisme.",  # N09
"gold|examen|2||[Perry, BMJ, 2011]|Un CT cérébral natif réalisé dans les 6 heures suivant une céphalée en coup de tonnerre est très sensible pour l'hémorragie sous-arachnoïdienne.",  # N10
"gold|examen|1||[avis d'expert]|Au-delà de 6 heures avec CT normal, la ponction lombaire cherche une xanthochromie, idéalement au moins 12 heures après le début.",  # N11
"alt|examen|1||[avis d'expert]|L'angiographie numérisée reste l'examen de référence si l'angio-CT est négatif et la suspicion forte.",  # N12
"pos|diagnostic différentiel|2||[avis d'expert]|La paralysie du III microvasculaire du diabétique épargne la pupille et régresse en général en 3 mois.",  # N13
"pos|diagnostic différentiel|1||[avis d'expert]|Le syndrome de Claude Bernard-Horner donne un ptosis discret avec myosis, et non une mydriase.",  # N14
"pos|diagnostic différentiel|1||[avis d'expert]|La myasthénie donne un ptosis et une diplopie fluctuants sans atteinte pupillaire.",  # N15
"pos|diagnostic différentiel|1||[avis d'expert]|Une mydriase unilatérale avec coma traduit un engagement temporal, qui est une urgence neurochirurgicale.",  # N16
"acu|décision|2||[Molyneux, Lancet, 2002, ISAT ; AHA/ASA, 2023]|Un anévrisme rompu ou symptomatique se traite rapidement par voie endovasculaire (coil) ou par clip chirurgical selon l'anatomie.",  # N17
"acu|posologie|2|S|[Pickard, BMJ, 1989 ; AIPS Swissmedic]|La nimodipine per os, 60 mg toutes les 4 heures pendant 21 jours, réduit l'ischémie retardée après hémorragie sous-arachnoïdienne, posologie à vérifier dans l'AIPS.",  # N18
"acu|piège|2||[AHA/ASA, 2023]|Le resaignement survient surtout dans les premières heures, ce qui justifie de sécuriser l'anévrisme tôt et de contrôler la tension.",  # N19
"chr|décision|1||[Greving, Lancet Neurol, 2014, PHASES]|Le risque de rupture d'un anévrisme non rompu asymptomatique s'estime par le score PHASES, qui guide traitement ou surveillance.",  # N20
"chr|prévention|1||[avis d'expert]|L'arrêt du tabac et le contrôle de la tension réduisent le risque de croissance et de rupture.",  # N21
"hos|complication|2||[AHA/ASA, 2023]|Après rupture, l'hydrocéphalie aiguë, le vasospasme avec ischémie retardée entre le 3e et le 14e jour et l'hyponatrémie sont les complications majeures.",  # N22
"hos|complication|1||[avis d'expert]|Une baisse de vigilance ou un déficit nouveau entre le 3e et le 14e jour évoque une ischémie retardée.",  # N23
"pro|pronostic|1||[avis d'expert]|Le pronostic de l'hémorragie sous-arachnoïdienne dépend surtout de l'état neurologique initial, mesuré par les échelles WFNS ou Hunt et Hess.",  # N24
"pro|pronostic|1||[avis d'expert]|Après traitement précoce, la paralysie du III récupère souvent, au moins partiellement.",  # N25
"sur|examen|1||[avis d'expert]|Un anévrisme traité par coil se contrôle par imagerie, car une reperméabilisation est possible.",  # N26
"fol|prévention|2||[avis d'expert]|Un dépistage par angio-IRM se discute chez les personnes ayant au moins deux parents du premier degré atteints ou une polykystose rénale.",  # N27
"fol|contexte suisse|1|S|[avis d'expert]|Le patient suspect d'hémorragie sous-arachnoïdienne est transféré par le 144 ou la Rega vers un centre neurovasculaire disposant de neuroradiologie interventionnelle et de neurochirurgie.",  # N28
]
ANGLES = [
"La pupille dilatée signe la compression du III.",
"Un CT normal à plus de 6 heures ne suffit pas.",
"La paralysie du III partielle s'image aussi.",
"La nimodipine se donne per os pendant 21 jours.",
"L'ischémie retardée survient entre le 3e et le 14e jour.",
"Deux parents du premier degré atteints justifient un dépistage.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une femme de 52 ans, fumeuse, consulte aux urgences de Lausanne pour une vision double apparue ce matin et une douleur derrière l'œil gauche. La paupière gauche tombe, l'œil gauche est dévié en bas et en dehors et sa pupille est dilatée et peu réactive.", prompt="Quel examen demandez-vous en urgence ?",
 items=["*Une angiographie CT ou IRM des artères cérébrales || La mydriase oriente vers une compression par anévrisme.", "Un dosage des anticorps anti-récepteur de l'acétylcholine || La myasthénie épargne la pupille.", "Une glycémie seule et un contrôle dans 3 mois || La pupille atteinte impose une imagerie.", "Un champ visuel || Il n'explore pas la cause.", "Une IRM des orbites dans un mois || Le délai est dangereux."],
 notions="N06 N07 N03 N05", angle="application", diff=2, ladder=L("Diplopie et ptosis douloureux.", "Compression externe du III.", "Mydriase.", "Pupille atteinte.", "Angio-CT urgent.", "Attendre.", "Pupille dilatée : anévrisme."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", serie=("S1", 2, 4), stem="L'angio-CT de cette femme montre un anévrisme de 7 mm de l'artère communicante postérieure gauche, non rompu.", prompt="Quelle est la conduite la plus adaptée ?",
 items=["*Traiter rapidement l'anévrisme par voie endovasculaire ou chirurgicale || Un anévrisme symptomatique risque de se rompre.", "Surveiller par IRM annuelle || L'anévrisme symptomatique ne se surveille pas.", "Prescrire de l'aspirine et revoir dans 6 mois || Elle ne traite pas l'anévrisme.", "Débuter la nimodipine seule || Elle sert après rupture.", "Faire une ponction lombaire || Rien ne l'indique."],
 notions="N17 N01 N20", angle="application", diff=3, ladder=L("Anévrisme symptomatique.", "Expansion de la paroi.", "Compression du III.", "Symptomatique versus asymptomatique.", "Traitement rapide.", "Surveiller.", "Symptomatique : traiter."), sources="[AHA/ASA, 2023]"),
dict(format="A", serie=("S1", 3, 4), stem="Avant le traitement prévu, cette femme présente brutalement une céphalée explosive, des vomissements et une raideur de nuque. Glasgow 14.", prompt="Quel examen faites-vous en premier ?",
 items=["*Un CT cérébral natif || Il détecte l'hémorragie sous-arachnoïdienne dans les premières heures.", "Une ponction lombaire immédiate || Le CT vient d'abord.", "Une IRM de diffusion || Le CT est plus rapide et sensible au sang aigu.", "Un EEG || Il n'est pas indiqué.", "Un fond d'œil seul || Il ne suffit pas."],
 notions="N09 N10 N19", angle="application", diff=2, ladder=L("Céphalée explosive.", "Rupture anévrismale.", "Raideur, vomissements.", "Hémorragie méningée.", "CT natif.", "Ponctionner d'abord.", "Coup de tonnerre : CT."), sources="[Perry, BMJ, 2011]"),
dict(masque=False, sit="monographique", format="Kprim", serie=("S1", 4, 4), stem="Le CT de cette femme confirme une hémorragie sous-arachnoïdienne. L'anévrisme est traité par coil le jour même.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La nimodipine per os se donne pendant 21 jours. || Elle réduit l'ischémie retardée.", "V: Une baisse de vigilance au 7e jour doit faire chercher une ischémie retardée. || Le vasospasme culmine entre le 3e et le 14e jour.", "V: La natrémie se surveille. || L'hyponatrémie est fréquente.", "F: Après coil, aucune imagerie de contrôle n'est nécessaire. || Une reperméabilisation est possible."],
 notions="N18 N22 N23 N26", angle="direct", diff=3, ladder=L("HSA traitée.", "Vasospasme.", "Surveillance.", "Complications.", "Nimodipine, surveillance.", "Pas de contrôle.", "J3-J14 : vasospasme."), sources="[AHA/ASA, 2023]"),
dict(format="A", stem="Un homme diabétique de 68 ans consulte à Sion pour une diplopie apparue hier avec une douleur légère. L'œil droit présente un ptosis complet et une déviation en bas et en dehors, mais la pupille est normale et réactive.", prompt="Quelle cause est la plus probable ?",
 items=["*Une paralysie du III microvasculaire || Le diabète et la pupille épargnée l'orientent.", "Un anévrisme de la communicante postérieure certain || La pupille épargnée le rend moins probable.", "Un syndrome de Horner || Il donne un myosis.", "Une myasthénie || Le début brutal et complet l'oriente ailleurs.", "Un engagement temporal || Le patient est conscient."],
 notions="N13 N04 N03", angle="application", diff=3, ladder=L("III pupille épargnée.", "Ischémie centrale du nerf.", "Diabète.", "Microvasculaire versus compressif.", "Contrôle vasculaire, suivi.", "Conclure à l'anévrisme.", "Pupille épargnée : microvasculaire."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 34 ans, sans facteur de risque vasculaire, présente une paralysie partielle du III gauche avec ptosis incomplet ; la pupille est encore normale.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Demander une imagerie vasculaire en urgence || Une atteinte partielle chez un sujet jeune non vasculaire peut être compressive.", "Rassurer et revoir dans 3 mois || L'atteinte peut évoluer vers la rupture.", "Prescrire un patch oculaire seul || Il traite la diplopie, pas la cause.", "Doser l'HbA1c seule || Le patient n'a pas de terrain vasculaire.", "Faire un EEG || Il n'est pas indiqué."],
 notions="N08 N07", angle="piège", diff=3, ladder=L("III partiel.", "Compression débutante possible.", "Sujet jeune.", "Pupille encore normale.", "Imagerie vasculaire.", "Se rassurer.", "Partiel ou jeune : imager."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 45 ans consulte à Genève 9 heures après une céphalée brutale maximale en quelques secondes, survenue pendant un effort. L'examen est normal et le CT cérébral aussi.", prompt="Quelle est la prochaine étape ?",
 items=["*Une ponction lombaire à la recherche de xanthochromie, au moins 12 heures après le début || Le CT perd de sa sensibilité après 6 heures.", "Le retour à domicile avec antalgique || Une hémorragie n'est pas exclue.", "Un EEG || Il n'est pas indiqué.", "Une IRM lombaire || Elle n'est pas indiquée.", "Un triptan || Une céphalée en coup de tonnerre n'est pas une migraine."],
 notions="N11 N10 N09", angle="piège", diff=3, ladder=L("Coup de tonnerre.", "Sang dans le LCR.", "CT normal après 6 h.", "Sensibilité du CT.", "PL avec xanthochromie.", "Renvoyer à domicile.", "> 6 h : ponction."), sources="[Perry, BMJ, 2011]"),
dict(format="A", stem="Un homme de 50 ans est retrouvé comateux à Fribourg après une céphalée brutale. Sa pupille droite est dilatée et aréactive, avec une hémiparésie gauche.", prompt="Que traduit cette mydriase dans ce contexte ?",
 items=["*Un engagement temporal par hypertension intracrânienne || La compression du III par l'uncus signe une urgence vitale.", "Une paralysie du III microvasculaire || Le coma l'exclut.", "Un effet d'un collyre || Le contexte l'exclut.", "Une myasthénie || Elle épargne la pupille.", "Un syndrome de Horner || Il donne un myosis."],
 notions="N16 N03", angle="application", diff=3, ladder=L("Coma et mydriase.", "Engagement de l'uncus.", "Pupille fixe, hémiparésie.", "Engagement versus III isolé.", "Neurochirurgie urgente.", "Penser microvasculaire.", "Coma + mydriase : engagement."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 61 ans a un ptosis gauche discret avec une pupille gauche plus petite que la droite, surtout dans l'obscurité, sans diplopie.", prompt="Quel diagnostic évoquez-vous ?",
 items=["*Un syndrome de Claude Bernard-Horner || Ptosis discret et myosis.", "Une paralysie du III anévrismale || Elle donne une mydriase et une diplopie.", "Une myasthénie || Elle épargne la pupille.", "Une paralysie du VI || Elle donne une diplopie horizontale sans ptosis.", "Un glaucome aigu || Il donne un œil rouge et douloureux."],
 notions="N14 N06", angle="direct", diff=2, ladder=L("Ptosis et myosis.", "Voie sympathique.", "Anisocorie à l'obscurité.", "Horner versus III.", "Chercher une dissection ou une tumeur apicale.", "Penser III.", "Myosis : Horner."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 38 ans présente un ptosis et une diplopie qui varient au cours de la journée et s'aggravent le soir. Les pupilles sont normales.", prompt="Quelle hypothèse est la plus probable ?",
 items=["*Une myasthénie oculaire || Fluctuation et pupilles épargnées.", "Une paralysie du III anévrismale || La pupille serait atteinte et la paralysie fixe.", "Un syndrome de Horner || Il donne un myosis.", "Une sclérose en plaques || Elle ne fluctue pas ainsi.", "Une thrombose du sinus caverneux || Elle donne fièvre et chémosis."],
 notions="N15 N06", angle="application", diff=2, ladder=L("Ptosis fluctuant.", "Jonction neuromusculaire.", "Pupilles normales.", "Fluctuation versus fixité.", "Anticorps.", "Penser anévrisme.", "Fluctuant : myasthénie."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un patient de 56 ans hospitalisé à Berne pour une hémorragie sous-arachnoïdienne anévrismale non encore sécurisée a une tension à 190/100 mmHg et s'agite.", prompt="Quelle complication précoce faut-il surtout prévenir ?",
 items=["*Le resaignement, en contrôlant la tension et en sécurisant l'anévrisme rapidement || Il survient surtout dans les premières heures.", "Le vasospasme du jour même || Il survient entre le 3e et le 14e jour.", "Une surdité || Elle n'est pas une complication typique.", "Une rhabdomyolyse || Elle n'est pas typique.", "Une pancréatite || Elle n'est pas liée."],
 notions="N19 N17", angle="piège", diff=3, ladder=L("HSA non sécurisée.", "Fragilité du sac rompu.", "Hypertension, agitation.", "Chronologie des complications.", "Contrôle tensionnel, sécurisation.", "Penser vasospasme d'abord.", "Premières heures : resaignement."), sources="[AHA/ASA, 2023]"),
dict(format="A", stem="Un homme de 60 ans, 2 jours après une hémorragie sous-arachnoïdienne, devient somnolent. Le CT montre une dilatation des ventricules.", prompt="Quelle mesure est indiquée ?",
 items=["*Une dérivation ventriculaire externe par le neurochirurgien || L'hydrocéphalie aiguë menace la vie.", "Un diurétique seul || Il ne traite pas l'hydrocéphalie.", "Une ponction lombaire répétée en première intention || Elle est risquée en cas d'hydrocéphalie obstructive.", "Une surveillance simple || La somnolence signe une urgence.", "Une anticoagulation || Elle est contre-indiquée."],
 notions="N22 N24", angle="application", diff=3, ladder=L("Somnolence et ventricules dilatés.", "Blocage de la résorption du LCR.", "J2 d'une HSA.", "Hydrocéphalie aiguë.", "Dérivation ventriculaire.", "Surveiller.", "Hydrocéphalie : DVE."), sources="[AHA/ASA, 2023]"),
dict(format="Kprim", stem="Vous expliquez la paralysie du III compressive à des étudiants à Zurich.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Les fibres pupillomotrices sont superficielles dans le nerf. || La compression externe les atteint d'abord.", "V: L'œil atteint se place en bas et en dehors. || Seuls le droit latéral et l'oblique supérieur restent actifs.", "F: L'ischémie diabétique atteint toujours la pupille. || Elle l'épargne habituellement.", "F: Un myosis accompagne la paralysie du III. || Elle donne une mydriase."],
 notions="N03 N06 N04 N13", angle="direct", diff=2, ladder=L("Anatomie du III.", "Disposition des fibres.", "Ptosis, œil en bas et dehors.", "Compression versus ischémie.", "Comprendre.", "Confondre myosis et mydriase.", "Fibres pupillaires superficielles."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Une femme de 42 ans dont la mère et la sœur ont présenté une hémorragie sous-arachnoïdienne vous consulte à Bâle.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un dépistage par angio-IRM se discute. || Deux parents du premier degré atteints augmentent le risque.", "V: L'arrêt du tabac réduit son risque. || Le tabac favorise la croissance des anévrismes.", "V: La polykystose rénale est un autre motif de dépistage. || Elle s'associe aux anévrismes.", "F: Un anévrisme découvert doit toujours être opéré. || Le score PHASES guide traitement ou surveillance."],
 notions="N27 N21 N02 N20", angle="application", diff=3, ladder=L("Antécédents familiaux.", "Prédisposition.", "Mère et sœur atteintes.", "Dépistage ciblé.", "Angio-IRM, tabac.", "Opérer tout anévrisme.", "Deux parents : dépister."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un homme de 55 ans est pris en charge à Lugano pour une hémorragie sous-arachnoïdienne anévrismale.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Son état neurologique initial est le principal déterminant du pronostic. || Les échelles WFNS ou Hunt et Hess le mesurent.", "V: Le traitement endovasculaire est souvent privilégié quand l'anatomie le permet. || L'essai ISAT l'a montré favorable.", "F: Il peut être traité dans tout hôpital régional sans neuroradiologie. || Il relève d'un centre neurovasculaire.", "F: La nimodipine se donne par voie IV rapide en bolus. || Elle se donne en général per os."],
 notions="N24 N17 N28 N18", angle="piège", diff=3, ladder=L("HSA.", "Gravité initiale.", "Centre spécialisé.", "Organisation.", "Transfert, coil.", "Rester en hôpital régional.", "Centre neurovasculaire."), sources="[Molyneux, Lancet, 2002]"),
dict(format="A", stem="Au 6e jour d'une hémorragie sous-arachnoïdienne traitée, une patiente de 49 ans présente une aphasie nouvelle et une faiblesse du bras droit. Le CT ne montre pas de nouveau saignement.", prompt="Quelle complication évoquez-vous ?",
 items=["*Une ischémie cérébrale retardée par vasospasme || Elle survient entre le 3e et le 14e jour.", "Un resaignement || Le CT ne le montre pas.", "Une crise migraineuse || Le contexte est vasculaire.", "Une hypoglycémie certaine || Elle doit être exclue, mais le contexte oriente vers le vasospasme.", "Une méningite || Rien ne l'évoque."],
 notions="N23 N22 N18", angle="application", diff=3, ladder=L("Déficit à J6.", "Vasospasme artériel.", "Aphasie, CT sans sang.", "Ischémie retardée.", "Imagerie vasculaire, maintien de la perfusion.", "Penser resaignement.", "J3-J14 : vasospasme."), sources="[AHA/ASA, 2023]"),
dict(masque=False, sit="monographique", format="A", stem="Une femme de 64 ans traitée par coil il y a 3 mois pour un anévrisme de la communicante postérieure revoit son neurologue. La paralysie du III s'améliore.", prompt="Quelle information est correcte ?",
 items=["*La paralysie du III récupère souvent après traitement précoce et un contrôle d'imagerie de l'anévrisme est prévu || Une reperméabilisation est possible.", "La paralysie ne récupère jamais || Elle récupère souvent au moins partiellement.", "Aucun suivi n'est nécessaire || Le coil se contrôle.", "Elle doit éviter définitivement toute activité physique || Rien ne l'impose.", "Elle doit prendre de la nimodipine à vie || Elle sert 21 jours après rupture."],
 notions="N25 N26", angle="direct", diff=2, ladder=L("Suivi après coil.", "Décompression du nerf.", "Amélioration.", "Pronostic et suivi.", "Contrôle d'imagerie.", "Pas de suivi.", "Contrôler le coil."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un patient présente une mydriase unilatérale.", prompt="Quelles situations exigent une imagerie cérébrale ou vasculaire en urgence ? (3 réponses)",
 items=["*Mydriase avec ptosis et diplopie douloureux || Elle évoque un anévrisme.", "*Mydriase avec coma || Elle évoque un engagement.", "*Mydriase après céphalée en coup de tonnerre || Elle évoque une rupture.", "Mydriase après instillation d'un collyre mydriatique || Elle est pharmacologique.", "Anisocorie stable depuis l'enfance || Elle est physiologique.", "Pupille d'Adie connue || Elle est bénigne.", "Mydriase bilatérale sous atropine || Elle est médicamenteuse.", "Myosis avec ptosis discret || Il évoque un Horner.", "Anisocorie de 0,3 mm sans autre signe || Elle est physiologique.", "Mydriase après traumatisme oculaire direct isolé || Elle est souvent locale.", "Pupilles égales réactives || Elles sont normales.", "Mydriase lors d'une émotion bilatérale || Elle est physiologique."],
 notions="N07 N16 N09", angle="direct", diff=3, ladder=L("Mydriase.", "Compression du III ou engagement.", "Contexte.", "Urgent versus bénin.", "Imagerie urgente.", "Banaliser.", "Mydriase + signes : imager."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Une femme de 47 ans vous demande quels facteurs augmentent le risque d'anévrisme intracrânien.", prompt="Choisissez les TROIS facteurs reconnus.",
 items=["*Tabagisme || Il fragilise la paroi artérielle.", "*Hypertension artérielle || Elle augmente la contrainte pariétale.", "*Polykystose rénale autosomique dominante || Elle s'associe aux anévrismes.", "Hypercholestérolémie isolée || Elle n'est pas un facteur reconnu.", "Hypothyroïdie || Pas de lien établi.", "Asthme || Pas de lien.", "Migraine sans aura || Pas de lien établi.", "Myopie || Pas de lien.", "Diabète de type 1 || Pas de lien établi.", "Psoriasis || Pas de lien.", "Lithiase biliaire || Pas de lien.", "Gaucherie || Pas de lien."],
 notions="N02 N21 N27", angle="direct", diff=2, ladder=L("Facteurs de risque.", "Fragilité pariétale.", "Prévention.", "Modifiables ou non.", "Tabac, HTA.", "Facteurs fantaisistes.", "Tabac, HTA, famille, polykystose."), sources="[Etminan et Rinkel, Nat Rev Neurol, 2016]"),
dict(format="A", stem="Un homme de 58 ans fait une céphalée brutale en coup de tonnerre à Delémont. Vous le recevez au cabinet.", prompt="Quelle organisation est la plus adaptée ?",
 items=["*Appeler le 144 pour un transfert vers un centre neurovasculaire || La suspicion de rupture exige un CT et une équipe spécialisée.", "Lui conseiller de rentrer en voiture et de revenir si cela empire || Le risque de resaignement est majeur.", "Lui prescrire un triptan || La céphalée en coup de tonnerre n'est pas une migraine.", "Programmer un CT ambulatoire dans la semaine || Le délai est dangereux.", "Faire une ponction lombaire au cabinet || Elle n'a pas sa place au cabinet."],
 notions="N28 N09", angle="application", diff=2, ladder=L("Coup de tonnerre au cabinet.", "Rupture possible.", "Urgence.", "Filière.", "144 et centre neurovasculaire.", "Renvoyer à domicile.", "Coup de tonnerre : 144."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Paralysie du III et anévrisme de la communicante postérieure : lire la pupille, imager les vaisseaux et prévenir la rupture",
 notions=[
  dict(titre="Lire la pupille", rub=["bas", "exa", "pos"], comment="Laisse la pupille trier compression et ischémie.",
   tableau=(["Tableau", "Pupille", "Cause", "Pourquoi"], [
     ["III complet douloureux", "Mydriase", "Anévrisme de la communicante postérieure", _T("Fibres superficielles", "La compression externe touche d'abord les fibres pupillaires.")],
     ["III complet, diabétique", "Épargnée", "Ischémie microvasculaire", _T("Atteinte centrale", "L'ischémie touche le centre du nerf.")],
     ["Coma et mydriase", "Mydriase fixe", "Engagement temporal", _T("Uncus", "Le lobe temporal écrase le III contre la tente.")],
     ["Ptosis et myosis", "Myosis", "Horner", _T("Voie sympathique", "Le dilatateur est paralysé.")],
     ["Ptosis fluctuant", "Normale", "Myasthénie", _T("Jonction", "La pupille n'est pas striée.")]]),
   points=["Partiel ou jeune : imager quand même."], sources=["[avis d'expert]"]),
  dict(titre="Imagerie", rub=["red", "gold", "alt"], comment="Choisis l'examen selon la question : anévrisme ou sang.",
   arbre=[("i1", None, "Paralysie du III ou céphalée en coup de tonnerre", "Les deux posent la question d'un anévrisme."),
          ("i2", "i1", "III avec mydriase ou partiel", "Angio-CT ou angio-IRM en urgence.", "an_aigu"),
          ("i3", "i1", "Coup de tonnerre", "CT natif d'abord.", "an_aigu"),
          ("i4", "i3", "CT normal < 6 h", "Il exclut pratiquement l'hémorragie."),
          ("i5", "i3", "CT normal > 6 h", "Ponction lombaire à la recherche de xanthochromie."),
          ("i6", "i2", "Angio-CT négatif, suspicion forte", "Angiographie numérisée.")],
   points=["Le CT perd de sa sensibilité après 6 heures."], sources=["[Perry, BMJ, 2011]"]),
  dict(titre="Traitement et complications de la rupture", rub=["acu", "hos", "pro"], comment="Sécurise tôt, puis surveille selon le calendrier des complications.",
   tableau=(["Période", "Complication", "Mesure", "Pourquoi"], [
     ["Premières heures", "Resaignement", "Contrôle tensionnel, coil ou clip", _T("Sac fragile", "Le caillot est instable.")],
     ["Jours 1-3", "Hydrocéphalie aiguë", "Dérivation ventriculaire", _T("Résorption bloquée", "Le sang obstrue les granulations.")],
     ["Jours 3-14", "Ischémie retardée", "Nimodipine 21 jours", _T("Vasospasme", "Les produits de dégradation du sang contractent les artères.")],
     ["Tout le séjour", "Hyponatrémie", "Natrémie", _T("Perte de sel", "Le cerveau lésé dérègle le sodium.")]]),
   points=["Pronostic : état neurologique initial (WFNS, Hunt et Hess)."], sources=["[AHA/ASA, 2023]", "[Molyneux, Lancet, 2002]"]),
  dict(titre="Prévention et dépistage", rub=["chr", "fol", "sur", "epi"], comment="Agis sur les facteurs modifiables et dépiste les familles à risque.",
   tableau=(["Situation", "Mesure", "Pourquoi"], [
     ["Tabac, HTA", "Arrêt, contrôle", "Ils favorisent croissance et rupture."],
     ["Deux parents du premier degré, polykystose", "Angio-IRM de dépistage", "Le risque d'anévrisme est accru."],
     ["Anévrisme non rompu asymptomatique", "Score PHASES", "Il pèse traitement et surveillance."],
     ["Anévrisme traité par coil", "Imagerie de contrôle", "Une reperméabilisation est possible."]]),
   points=["Anévrisme symptomatique : traiter vite."], sources=["[Greving, Lancet Neurol, 2014]"]),
 ],
 ssp=dict(code="S1.1", nom="Diplopie, ptosis, mouvements oculaires anormaux", officiel=True, algorithme=[
  ("n1", None, "Diplopie ou ptosis", "Le premier tri distingue fluctuation et déficit fixe."),
  ("n2", "n1", "Fluctuant, pupilles normales", "Une myasthénie se cherche (même SSP).", None, "c1"),
  ("n3", "n1", "Ptosis discret avec myosis", "Un syndrome de Horner fait chercher une dissection.", None, "c1"),
  ("n4", "n1", "Paralysie du III", "La pupille et le terrain trient la cause.", None, "c1"),
  ("n5", "n4", "Mydriase, douleur, partiel ou sujet jeune", "Angio-CT ou angio-IRM en urgence.", "an_aigu", "c2"),
  ("n6", "n4", "Pupille épargnée, complet, diabétique", "Paralysie microvasculaire probable ; contrôle et réévaluation.", None, "c1"),
  ("n7", "n5", "Anévrisme symptomatique", "Traitement rapide par coil ou clip.", "an_aigu", "c3"),
  ("n8", "n4", "Coma associé", "Engagement temporal : urgence neurochirurgicale.", None, "c1"),
  ("n9", "n7", "Après traitement", "Suivi d'imagerie et prévention.", "an_aigu", "c4")]),
 pec=[
  dict(cle="an_aigu", titre="Anévrisme symptomatique ou rompu",
   but=["Prévenir la rupture ou le resaignement.", "Prévenir l'ischémie retardée et l'hydrocéphalie."],
   moyens=dict(accueil=["Évaluer Glasgow, pupilles et déficit.", "Contrôler la douleur et la tension."],
    pharma=[("Nimodipine (inhibiteur calcique)", "60 mg per os toutes les 4 heures pendant 21 jours après rupture ; à vérifier dans l'AIPS.", "Elle réduit l'ischémie retardée.", "[Pickard, BMJ, 1989]"),
            ("Antihypertenseur IV titrable", "Selon la cible fixée par l'équipe ; à vérifier dans l'AIPS.", "Il réduit le risque de resaignement avant sécurisation.", "[AHA/ASA, 2023]"),
            ("Antalgiques", "Paracétamol, opioïde si besoin ; à vérifier dans l'AIPS.", "La douleur élève la tension.", "[avis d'expert]")],
    nonpharma=[("geste ou chirurgie", "Coil endovasculaire ou clip chirurgical précoce.", "Ils excluent l'anévrisme de la circulation."),
               ("geste ou chirurgie", "Dérivation ventriculaire externe si hydrocéphalie.", "Elle draine le LCR.")],
    transversal=[("Neuroradiologie interventionnelle", "Elle pose le coil."), ("Médecine intensive", "Elle surveille vasospasme et natrémie.")]),
   urgence=(["Transfert par le 144 vers un centre neurovasculaire.", "Sécurisation précoce de l'anévrisme."],
            [("d'abord", "médecin responsable", "Reconnaît le tableau et demande l'imagerie."),
             ("ensuite", "neuroradiologue", "Confirme et traite l'anévrisme."),
             ("puis", "intensiviste", "Surveille les complications jusqu'au 14e jour.")]),
   horsUrgence=(["Contrôle d'imagerie après coil.", "Arrêt du tabac, contrôle tensionnel."],
            [("d'abord", "neurochirurgien·ne", "Planifie le suivi de l'anévrisme."),
             ("ensuite", "médecin de famille", "Contrôle tension et tabac."),
             ("puis", "patient·e", "Informe sa famille du dépistage possible.")]),
   pronostic="Le pronostic dépend de l'état neurologique initial ; la paralysie du III récupère souvent après traitement précoce.",
   suivi=[("Vigilance et déficit", "Plusieurs fois par jour jusqu'au 14e jour", "Absence d'ischémie retardée"), ("Natrémie", "Quotidienne", "Normale"), ("Imagerie de l'anévrisme", "Selon le protocole", "Occlusion stable")],
   sortie="Le patient sort quand l'anévrisme est sécurisé, la période de vasospasme passée et la réadaptation organisée.",
   prevention=["Elle repose sur l'arrêt du tabac et le contrôle de la tension.", "Elle passe par le traitement des anévrismes à risque et le dépistage familial ciblé.", "Elle passe par la réadaptation et la surveillance de l'anévrisme traité."]),
 ])
AVERIFIER = ["Cible tensionnelle avant sécurisation de l'anévrisme selon les recommandations AHA/ASA 2023 et suisses à vérifier.",
             "Critères exacts du dépistage familial des anévrismes à vérifier.",
             "Délai optimal de la ponction lombaire (≥ 12 heures) à confirmer."]
