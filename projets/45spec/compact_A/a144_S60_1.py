from constructeur_agent_45spec import pec
ID = "S60.1__S6_8-E05"
SEA = "[Seaberg et al., Treatment of subungual hematomas with nail trephination: a prospective study, Am J Emerg Med 1991;9:209-10, PMID 2018587, résumé lu le 25.11.2026]"
ROS = "[Roser et Gellman, Comparison of nail bed repair versus nail trephination for subungual hematomas in children, J Hand Surg Am 1999;24:1166-70, PMID 10584937, résumé lu le 25.11.2026]"
AFP = "[Hilgefort, Becker et Chu, Fingertip Injuries, Am Fam Physician 2025;112:47-54, texte lu sur aafp.org le 25.11.2026 (cotes SORT)]"
LEV = "[Levit et al., The ABC rule for clinical detection of subungual melanoma, J Am Acad Dermatol 2000;42:269-74, PMID 10642684, résumé lu le 25.11.2026]"
OZT = "[Oztas, Clinical and dermoscopic progression of subungual hematomas, Int Surg 2010;95:239-41, PMID 21067003, résumé lu le 25.11.2026]"
MET = "[Metcalfe et al., Prophylactic antibiotics in open distal phalanx fractures: systematic review and meta-analysis, J Hand Surg Eur 2016;41:423-30, PMID 26329883, résumé lu le 25.11.2026]"
STE = "[Stevenson et al., Prophylactic flucloxacillin in open fractures of the distal phalanx: double-blind randomized placebo-controlled trial, J Hand Surg Br 2003;28:388-94, PMID 12954243, résumé lu le 25.11.2026]"
PV26 = "[OFSP et CFV, Plan de vaccination suisse 2026, tableau 10 « Prophylaxie antitétanique en cas de plaies », PDF bag.admin.ch lu le 25.11.2026]"
LAA = "[OFSP, « Assurance-accidents : qui est assuré à titre obligatoire ? », bag.admin.ch, page lue le 25.11.2026]"
EXP = "Avis d'expert, chirurgie de la main, dermatologie et urgences (à vérifier)"
_N = [
("def","definition","critère",3,0,AFP+" ; "+SEA,"L'hématome sous-unguéal est une collection de sang sous la tablette de l'ongle après un écrasement ; son diagnostic est clinique, et il donne une coloration rouge-violacée à noire."),
("epi","epidemiology","chiffre",1,0,SEA,"C'est un motif fréquent de consultation aux urgences."),
("anticoag","epidemiology","terrain particulier",1,0,EXP,"Un traitement anticoagulant favorise l'hématome sans changer la conduite."),
("mech","basicSciences","mécanisme",1,0,EXP,"Le sang s'accumule sous une tablette rigide : la pression monte et provoque la douleur."),
("regrow","basicSciences","chiffre",1,0,SEA,"L'ongle met en moyenne environ 4 mois à repousser (4,0 ± 2,6 mois)."),
("hx","anamnesis","symptôme",2,0,EXP,"On précise le mécanisme d'écrasement (porte, marteau), l'heure de l'accident et un traitement anticoagulant."),
("timing","anamnesis","décision",1,0,EXP,"La trépanation soulage surtout dans les premières heures, tant que le sang reste liquide (à vérifier)."),
("exam","clinicalExam","examen",2,0,EXP,"On estime la surface de l'hématome, on vérifie l'intégrité de l'ongle et de ses bords, on cherche une plaie et une mobilité anormale de la phalange."),
("painless","clinicalExam","piège",1,0,AFP,"La plupart des hématomes relèvent de l'observation et de la réassurance ; on ne décomprime que l'hématome douloureux, et un hématome ancien indolore ne justifie pas de trépanation."),
("noTrauma","presumptionRedFlags","diagnostic différentiel",3,0,LEV,"Une bande brun-noir de 3 mm ou plus aux bords irréguliers, qui change, ou un pigment qui déborde sur le repli proximal ou latéral (signe de Hutchinson) font craindre un mélanome unguéal ; seule la biopsie confirme le diagnostic."),
("open","presumptionRedFlags","complication",1,0,MET+" ; "+STE,"Une plaie du lit avec fracture de la phalange distale réalise une fracture ouverte : on lave et l'on débride rapidement ; l'antibiotique prophylactique n'a pas réduit les infections superficielles (environ 4 %, aucune ostéite)."),
("nailbed","presumptionRedFlags","décision",1,0,AFP,"Une plaie du lit se traite par observation dans la plupart des cas ou par réparation au fil résorbable 6-0 ou 7-0, ou à la colle si l'ongle est déjà avulsé ; l'aspect final de l'ongle ne diffère pas entre observation et réparation."),
("xray","workupGoldStandard","examen",2,0,SEA,"On radiographie le doigt pour chercher une fracture de la phalange distale."),
("dermo","workupAlternatives","examen",1,0,OZT,"La dermoscopie de l'hématome montre une zone homogène et des globules rouge-violacés qui diminuent en 6 semaines ; elle aide à le distinguer d'un mélanome."),
("ddx","positiveDiagnosis","diagnostic différentiel",2,0,OZT+" ; "+LEV,"Un pigment sous l'ongle vient du sang, de la mélanine (nævus, mélanome) ou d'un champignon ; l'hématome est souvent pris à tort pour un mélanome."),
("trephine","acuteManagement","décision",3,0,SEA,"La trépanation de l'ongle soulage la douleur ; on n'a observé ni infection, ni ostéomyélite, ni déformation majeure, quelle que soit la taille de l'hématome ou la présence d'une fracture."),
("noremoval","acuteManagement","piège",3,0,SEA+" ; "+ROS,"Quand l'ongle et ses bords sont intacts, l'ablation de l'ongle et la suture du lit sont inutiles, quelle que soit la taille de l'hématome."),
("technique","acuteManagement","décision",1,0,AFP+" ; "+SEA,"On perce l'ongle de façon aseptique avec un trépan dédié, un électrocautère ou un trombone chauffé."),
("analg","acuteManagement","molécule",1,0,EXP,"Un antalgique simple complète la trépanation ; dose à vérifier dans l'AIPS (Swissmedic)."),
("tetanus","acuteManagement","prévention",1,0,PV26,"Un écrasement est une plaie à risque élevé de tétanos : entre 26 et 64 ans, on fait un rappel dT si la dernière dose date de 10 ans ou plus (5 ans ou plus avant 26 ans et dès 65 ans)."),
("complication","hospitalizationComplications","complication",1,0,ROS,"Des déformations transitoires de l'ongle (dépression, hypertrophie) peuvent survenir et disparaissent en environ 4 mois."),
("infection","hospitalizationComplications","complication",1,0,EXP,"Après trépanation, on garde le doigt propre et l'on reconsulte en cas de rougeur, de pus ou de fièvre."),
("children","chronicManagement","décision",2,0,ROS,"Chez l'enfant à ongle intact, la réparation chirurgicale ne fait pas mieux que la trépanation ou l'observation, quels que soient la taille (même plus de 25 %), la fracture, le mécanisme ou l'âge."),
("cost","chronicManagement","chiffre",1,0,ROS,"La réparation chirurgicale coûtait environ 4 fois plus cher que la trépanation (1263 contre 283 dollars)."),
("progn","prognosisDischarge","pronostic",1,0,SEA,"Après trépanation, on n'a observé aucune déformation majeure à 10 mois de suivi en moyenne."),
("surv","surveillance","décision",1,0,OZT+" ; "+LEV,"La tache doit migrer vers le bord libre et rétrécir ; une tache qui ne migre pas ou qui s'élargit impose une biopsie."),
("net","followUpNetwork","décision",1,0,AFP,"Le médecin de famille ou l'urgentiste traite l'hématome sans adresser, sauf fracture complexe ou ouverte ; le dermatologue évalue une pigmentation suspecte."),
("swiss","followUpNetwork","contexte suisse",1,1,LAA+" ; "+PV26,"En Suisse, l'assurance-accidents (LAA) couvre le salarié, aussi pour les accidents non professionnels s'il travaille au moins 8 heures par semaine chez le même employeur ; le rappel antitétanique suit le tableau 10 du plan de vaccination."),
]
K = {k: i+1 for i, (k, *_r) in enumerate(_N)}
N = [t[1:] for t in _N]
n = lambda *ks: [K[k] for k in ks]
AM = ["Trépaner, ne pas arracher l'ongle intact.","Taille ou fracture fermée : même conduite.","Sans traumatisme : penser mélanome.","Tache qui ne migre pas : biopsie.","Ongle arraché, plaie du lit : fracture ouverte.","Tétanos."]
A = lambda *o: list(o)
Q = [
{"f":"A","s":("S1",1,3),"st":"Un homme de 30 ans s'est écrasé l'index dans une porte il y a trois heures. Il a une douleur pulsatile intense ; une coloration bleu-noir occupe 60 % de l'ongle, dont la tablette et les bords sont intacts.",
 "p":"Quelle est votre prise en charge ?","o":A((1,"Une radiographie du doigt, puis une trépanation de l'ongle sans l'enlever","Seaberg 1991."),(0,"L'ablation de l'ongle et la suture du lit, car l'atteinte dépasse 50 %","Piège."),(0,"Une simple attente","Faux."),(0,"Un antibiotique seul","Faux."),(0,"Une incision de la pulpe","Faux.")),
 "n":n("trephine","noremoval","xray","exam","def"),"a":"piège","d":4,"l":("Écrasement.","Pression sous l'ongle.","60 %.","Ongle intact.","Trépaner.","Arracher.","Ongle intact : trépaner.")},
{"f":"A","s":("S1",2,3),"st":"La radiographie montre une fracture non déplacée de la houppe de la phalange distale ; la peau et l'ongle sont intacts.",
 "p":"Modifiez-vous votre conduite ?","o":A((1,"Non : vous trépanez sans enlever l'ongle","Seaberg 1991."),(0,"Oui : l'ablation de l'ongle devient obligatoire","Piège."),(0,"Oui : une ostéosynthèse","Faux."),(0,"Oui : un plâtre de l'avant-bras","Faux."),(0,"Oui : une hospitalisation","Faux.")),
 "n":n("noremoval","trephine","hx"),"a":"piège","d":4,"l":("Fracture.","Fermée.","Houppe.","Ongle intact.","Même conduite.","Ablation.","Fracture fermée : trépanation.")},
{"f":"A","s":("S1",3,3),"st":"Vous avez trépané l'ongle ; la douleur a disparu.",
 "p":"Que lui annoncez-vous ?","o":A((1,"L'ongle repoussera en quelques mois, en général sans déformation majeure","Seaberg 1991."),(0,"Il perdra définitivement l'ongle","Faux."),(0,"Il aura une ostéomyélite","Faux."),(0,"L'ongle repoussera en une semaine","Faux."),(0,"Il devra être opéré","Faux.")),
 "n":n("regrow","progn","technique","hx"),"a":"application","d":3,"l":("Évolution.","Pousse.","4 mois.","Sans déformation.","Informer.","Perte définitive.","Repousse en environ 4 mois.")},
{"f":"A","st":"Une femme de 52 ans a depuis six mois une tache brun-noir de l'ongle du gros orteil, sans souvenir de traumatisme. La bande s'élargit et le pigment déborde sur le repli proximal.",
 "p":"Quelle est votre conduite ?","o":A((1,"Une biopsie de la matrice auprès d'un dermatologue","Levit 2000 : signe de Hutchinson."),(0,"Une trépanation","Piège."),(0,"Une surveillance d'un an","Faux."),(0,"Un antifongique","Faux."),(0,"Une réassurance","Faux.")),
 "n":n("noTrauma","ddx","dermo"),"a":"piège","d":5,"l":("Sans traumatisme.","Mélanocytes.","Bande élargie.","Repli atteint.","Biopsie.","Trépaner.","Hutchinson : mélanome.")},
{"f":"A","st":"Un garçon de 6 ans s'est coincé le doigt dans une porte. Une coloration violacée occupe 70 % de l'ongle, qui est intact. Les parents demandent une opération.",
 "p":"Que leur répondez-vous ?","o":A((1,"Une trépanation ou une simple observation suffit ; la réparation chirurgicale n'apporte rien","Roser 1999."),(0,"Une ablation de l'ongle sous anesthésie générale, car l'atteinte dépasse 25 %","Piège."),(0,"Une radiographie annuelle","Faux."),(0,"Une antibiothérapie","Faux."),(0,"Une attelle du bras","Faux.")),
 "n":n("children","cost","noremoval"),"a":"piège","d":4,"l":("Enfant.","Lit intact.","70 %.","Ongle intact.","Trépaner ou observer.","Opérer.","Enfant, ongle intact : pas d'opération.")},
{"f":"A","st":"Un homme de 40 ans s'est frappé le doigt avec un marteau. L'ongle est à moitié arraché, le bord est rompu et le lit saigne ; la radiographie montre une fracture de la phalange distale.",
 "p":"Quelle est votre conduite ?","o":A((1,"Un lavage et un débridement soigneux, le traitement du lit et la vérification du tétanos, sans antibiotique systématique","Metcalfe 2016 ; plan de vaccination 2026."),(0,"Une trépanation simple","Piège."),(0,"Un pansement sec seul","Faux."),(0,"Une attente","Faux."),(0,"Une radiographie de contrôle seule","Faux.")),
 "n":n("open","nailbed","tetanus"),"a":"piège","d":4,"l":("Ongle arraché.","Communication.","Plaie du lit.","Fracture.","Réparer.","Trépaner.","Plaie et fracture : ouverte.")},
{"f":"A","st":"Un homme de 60 ans, qui prend du rivaroxaban, a un ongle noir depuis un choc il y a dix jours. Il n'a plus mal.",
 "p":"Quelle est votre conduite ?","o":A((1,"Pas de trépanation ; vous vérifiez que la tache migre avec la pousse","AFP 2025 ; Oztas 2010."),(0,"Une trépanation","Piège : trop tard, indolore."),(0,"L'arrêt du rivaroxaban","Faux."),(0,"Une biopsie immédiate","Faux."),(0,"Une ablation de l'ongle","Faux.")),
 "n":n("painless","timing","anticoag","surv"),"a":"piège","d":4,"l":("Ancien.","Sang coagulé.","Dix jours.","Indolore.","Surveiller.","Trépaner.","Indolore et ancien : surveiller.")},
{"f":"A","m":0,"st":"Vous définissez l'hématome sous-unguéal.",
 "p":"Quelle définition retenez-vous ?","o":A((1,"Une collection de sang sous l'ongle après un écrasement","Expert."),(0,"Une infection du repli","Faux."),(0,"Une tumeur de la matrice","Faux."),(0,"Une mycose","Faux."),(0,"Une fracture","Faux.")),
 "n":n("def","mech"),"a":"direct","d":1,"l":("Définition.","Sang.","Sous l'ongle.","Écrasement.","Définir.","Infection.","Sang sous l'ongle.")},
{"f":"A","m":0,"st":"Un patient demande combien de temps son ongle mettra à repousser après un hématome sous-unguéal.",
 "p":"Que lui répondez-vous ?","o":A((1,"Environ 4 mois","Seaberg 1991."),(0,"Une semaine","Faux."),(0,"Deux ans","Faux."),(0,"Jamais","Faux."),(0,"Un jour","Faux.")),
 "n":n("regrow"),"a":"direct","d":2,"l":("Pousse.","Matrice.","4 mois.","Moyenne.","Informer.","Une semaine.","Environ 4 mois.")},
{"f":"A","m":0,"st":"Vous lisez l'étude prospective de Seaberg sur l'hématome sous-unguéal.",
 "p":"Qu'a-t-elle montré après trépanation ?","o":A((1,"Aucune infection, ostéomyélite ou déformation majeure, quelle que soit la taille","Seaberg 1991."),(0,"Beaucoup d'ostéomyélites","Faux."),(0,"La nécessité d'enlever l'ongle au-delà de 50 %","Faux."),(0,"Une perte définitive de l'ongle","Faux."),(0,"Un échec antalgique","Faux.")),
 "n":n("trephine","progn","epi"),"a":"direct","d":3,"l":("Preuve.","Étude.","Trépanation.","Sans complication.","Lire.","Ostéomyélite.","Trépanation sûre.")},
{"f":"A","m":0,"st":"Un patient consulte pour un hématome sous-unguéal après un accident de bricolage.",
 "p":"Quelle vérification préventive faites-vous ?","o":A((1,"Le statut vaccinal contre le tétanos","Plan de vaccination suisse 2026."),(0,"Une sérologie VIH","Faux."),(0,"Une glycémie","Faux."),(0,"Un ECG","Faux."),(0,"Une ferritine","Faux.")),
 "n":n("tetanus","swiss"),"a":"application","d":3,"l":("Prévention.","Plaie.","Tétanos.","Plan suisse.","Vérifier.","VIH.","Tétanos.")},
{"f":"A","m":0,"st":"Un enfant a été traité pour un hématome sous-unguéal.",
 "p":"Quelle évolution de l'ongle peut-on observer ?","o":A((1,"Une dépression ou une hypertrophie transitoire, résolue en environ 4 mois","Roser 1999."),(0,"Une perte définitive","Faux."),(0,"Une ostéomyélite fréquente","Faux."),(0,"Un mélanome","Faux."),(0,"Une amputation","Faux.")),
 "n":n("complication","children"),"a":"direct","d":3,"l":("Évolution.","Pousse.","Dépression.","Transitoire.","Informer.","Définitive.","Transitoire, 4 mois.")},
{"f":"A","m":0,"st":"Vous venez de trépaner un hématome sous-unguéal.",
 "p":"Quel conseil donnez-vous ?","o":A((1,"Garder le doigt propre, prendre un antalgique et reconsulter en cas de rougeur ou de pus","Expert."),(0,"Prendre un antibiotique pendant 10 jours","Faux."),(0,"Plonger le doigt dans l'eau sale","Faux."),(0,"Arracher l'ongle à la maison","Faux."),(0,"Immobiliser le bras","Faux.")),
 "n":n("infection","analg"),"a":"application","d":3,"l":("Conseils.","Infection.","Propreté.","Rougeur.","Conseiller.","Antibiotique.","Propre, antalgique, reconsulter.")},
{"f":"A","m":0,"st":"Vous comparez une tache unguéale à un hématome sous-unguéal.",
 "p":"Quel examen non invasif aide à les distinguer ?","o":A((1,"La dermoscopie","Oztas 2010."),(0,"Une IRM","Faux."),(0,"Un scanner","Faux."),(0,"Une prise de sang","Faux."),(0,"Une échographie cardiaque","Faux.")),
 "n":n("dermo","ddx"),"a":"application","d":3,"l":("Pigment.","Sang ou mélanine.","Dermoscopie.","Globules.","Distinguer.","IRM.","Dermoscopie.")},
{"f":"Kprim","m":0,"st":"Vous traitez un hématome sous-unguéal récent et douloureux, ongle intact.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"La trépanation soulage la douleur.","Seaberg 1991."),(1,"On n'enlève pas l'ongle intact.","Seaberg 1991."),(1,"On cherche une fracture par radiographie.","Seaberg 1991."),(0,"Au-delà de 50 % de surface, l'ablation est obligatoire.","Faux.")),
 "n":n("trephine","noremoval","xray"),"a":"direct","d":2,"l":("Traitement.","Pression.","Trépaner.","Ongle intact.","Traiter.","50 %.","Trépaner, ne pas arracher.")},
{"f":"Kprim","m":0,"st":"Vous évaluez une pigmentation unguéale.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"L'absence de traumatisme doit alerter.","Expert."),(1,"Un pigment sur le repli proximal doit alerter.","Levit 2000."),(1,"Une tache qui ne migre pas avec la pousse doit alerter.","Oztas 2010."),(0,"Une douleur pulsatile après écrasement doit alerter.","Faux : hématome.")),
 "n":n("noTrauma","surv","ddx"),"a":"direct","d":3,"l":("Pigment.","Mélanome.","Sans traumatisme.","Repli.","Alerter.","Douleur.","Sans trauma, repli, pas de migration.")},
{"f":"Kprim","m":0,"st":"Vous prenez en charge un hématome sous-unguéal chez un enfant, ongle intact.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"La réparation chirurgicale ne fait pas mieux que la trépanation.","Roser 1999."),(1,"La chirurgie coûte environ 4 fois plus cher.","Roser 1999."),(1,"Une atteinte de plus de 25 % n'impose pas de réparation.","Roser 1999."),(0,"Une anesthésie générale est requise.","Faux.")),
 "n":n("children","cost","net"),"a":"direct","d":3,"l":("Enfant.","Preuve.","Pas mieux.","Coût.","Choisir.","Anesthésie.","Trépaner ou observer.")},
{"f":"Kprim","m":0,"st":"Un hématome sous-unguéal accompagne un ongle arraché et une plaie du lit.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"On traite le lit lésé par observation ou réparation.","AFP 2025."),(1,"On vérifie le tétanos.","Plan de vaccination 2026 : écrasement à risque élevé."),(1,"On lave et l'on débride la plaie.","Metcalfe 2016."),(0,"Un antibiotique prophylactique est indispensable.","Faux : sans bénéfice démontré.")),
 "n":n("open","nailbed","tetanus","infection"),"a":"application","d":3,"l":("Ongle arraché.","Plaie.","Explorer.","Tétanos.","Réparer.","Trépaner.","Ongle arraché : réparer.")},
{"f":"MenuLong","st":"Une femme de 45 ans consulte pour une tache noire sous l'ongle du pouce.",
 "p":"Choisissez les TROIS éléments qui font craindre une tumeur plutôt qu'un dépôt de sang.","o":A((1,"L'absence de traumatisme","Expert."),(1,"Un pigment qui déborde sur le repli proximal","Levit 2000."),(1,"Une tache qui ne migre pas avec la pousse","Oztas 2010."),(0,"Une douleur pulsatile","Faux."),(0,"Un écrasement récent","Faux."),(0,"Une couleur violacée homogène","Faux."),(0,"Un début brutal","Faux."),(0,"Un traitement anticoagulant","Faux."),(0,"Une tache qui avance vers le bord libre","Faux."),(0,"Une petite taille","Faux."),(0,"Un âge de 45 ans","Faux."),(0,"Un ongle lisse","Faux.")),
 "n":n("noTrauma","surv","dermo","hx"),"a":"piège","d":4,"l":("Tache.","Mélanocytes.","Sans traumatisme.","Repli, migration.","Biopsie.","Écrasement.","Hutchinson, pas de migration.")},
{"f":"MenuLong","m":0,"st":"Vous traitez un hématome sous-unguéal récent et douloureux ; l'ongle et ses bords sont intacts.",
 "p":"Choisissez les TROIS conduites justes.","o":A((1,"Une trépanation","Seaberg 1991."),(1,"Une radiographie si une fracture est suspectée","Seaberg 1991."),(1,"Un antalgique simple","Expert."),(0,"Une ablation de l'ongle","Faux."),(0,"Une suture du lit","Faux."),(0,"Un antibiotique systématique","Faux."),(0,"Une attelle du bras","Faux."),(0,"Une IRM","Faux."),(0,"Une anesthésie générale","Faux."),(0,"Une biopsie","Faux."),(0,"Une incision de la pulpe","Faux."),(0,"Un bain chaud prolongé","Faux.")),
 "n":n("trephine","xray","analg","noremoval","exam"),"a":"application","d":3,"l":("Traitement.","Pression.","Trépaner.","Radiographie.","Traiter.","Arracher.","Trépaner, radiographier, antalgique.")},
]
for _q in Q: _q["src"] = EXP
for _i in (0, 1, 2, 8, 9, 14): Q[_i]["src"] = SEA
for _i in (4, 11, 16): Q[_i]["src"] = ROS
Q[19]["src"] = [SEA, AFP]
Q[3]["src"] = LEV; Q[5]["src"] = [MET, STE, PV26]; Q[6]["src"] = [AFP, OZT]; Q[7]["src"] = AFP; Q[10]["src"] = PV26
Q[13]["src"] = OZT; Q[15]["src"] = [LEV, OZT]; Q[17]["src"] = [AFP, MET, PV26]; Q[18]["src"] = [LEV, OZT]
C = {"theme":"Hématome sous-unguéal traumatique : douleur pulsatile après écrasement, radiographie de la phalange distale, trépanation sans ablation de l'ongle intact quelle que soit la taille ou une fracture fermée, enfant, ongle arraché et fracture ouverte, tétanos, repousse en 4 mois, mélanome unguéal en diagnostic différentiel",
 "notions":[
  {"titre":"Comprendre","rub":["definition","epidemiology","basicSciences","anamnesis"],"comment":"Le sang piégé sous l'ongle fait mal par la pression ; l'ongle repousse en quelques mois.",
   "points":["Douleur pulsatile.","Repousse en environ 4 mois."],"sources":[SEA,EXP]},
  {"titre":"Évaluer","rub":["clinicalExam","presumptionRedFlags","workupGoldStandard","workupAlternatives"],"comment":"On vérifie l'intégrité de l'ongle, on radiographie et l'on écarte un mélanome.",
   "arbre":[("d1",None,"Ongle noir","On demande s'il y a eu un écrasement.",None,None),("d2","d1","Écrasement récent, ongle intact","On radiographie et l'on trépane.",None,None),("d3","d1","Ongle arraché, plaie du lit","On lave, on débride et l'on traite le lit.",None,None),("d4","d1","Aucun traumatisme","On fait une dermoscopie et une biopsie.",None,None),("d5","d2","Hématome ancien indolore","On surveille la migration.",None,None)],
   "points":["Hutchinson : mélanome."],"sources":[SEA,LEV,OZT]},
  {"titre":"Traiter","rub":["positiveDiagnosis","acuteManagement","hospitalizationComplications","chronicManagement"],"comment":"On trépane l'ongle intact sans l'enlever.",
   "tab":(["Situation","Conduite","Source"],[["Ongle intact, toute taille","Trépanation",[("Seaberg 1991","Aucune complication.")]],["Fracture fermée de P3","Trépanation",[("Seaberg 1991","Même conduite.")]],["Enfant, ongle intact","Trépanation ou observation",[("Roser 1999","Réparation inutile.")]],["Ongle arraché, plaie du lit","Lavage, débridement, traitement du lit, tétanos",[("Metcalfe 2016","Lavage, pas d'antibiotique systématique.")]]]),
   "points":["Pas d'antibiotique systématique, même si la fracture est ouverte."],"sources":[SEA,ROS,MET,AFP]},
  {"titre":"Suivre","rub":["prognosisDischarge","surveillance","followUpNetwork"],"comment":"La tache migre avec la pousse ; sinon, on biopsie.",
   "points":["Tétanos selon le plan suisse."],"sources":[SEA,OZT,PV26]}],
 "ssp":("S6.8","Plaintes concernant les ongles",True,[
   ("n1",None,"Ongle noir","On demande le mécanisme et l'on examine l'ongle.","ongle","c2"),
   ("n2","n1","Écrasement récent, douleur, ongle intact","On radiographie et l'on trépane.","ongle","c3"),
   ("n3","n1","Ongle arraché ou bords rompus","On explore et l'on répare le lit.","ongle","c2"),
   ("n4","n1","Aucun traumatisme, bande pigmentée","On adresse au dermatologue pour biopsie.","ongle","c2"),
   ("n5","n2","Repousse","On vérifie la migration de la tache.","ongle","c4"),
   ("n6","n2","Enfant","On trépane ou l'on observe sans chirurgie.","ongle","c3")]),
 "pec":[
  pec("ongle","Hématome sous-unguéal traumatique",["On soulage la douleur.","On ne méconnaît ni une fracture ouverte ni un mélanome."],
      ["On examine l'ongle et ses bords.","On demande le mécanisme et l'heure de l'accident."],
      [("Antalgique simple","Paracétamol ou AINS ; dose à vérifier dans l'AIPS (Swissmedic).","Il complète la trépanation.",EXP)],
      [("geste ou chirurgie","On trépane l'ongle de façon aseptique.","On évacue le sang et l'on supprime la douleur."),("éducation thérapeutique","On explique la repousse et les signes d'infection.","On évite une consultation inutile ou tardive.")],
      [("N Médecine sociale Prévention OFSP","On met à jour la vaccination antitétanique."),("A Assurances sociales","On déclare l'accident à l'assurance-accidents.")],
      (["On examine l'ongle.","On radiographie.","On trépane."],[("d'abord","urgentiste","Il examine l'ongle et radiographie le doigt."),("ensuite","urgentiste","Il trépane l'ongle intact."),("puis","chirurgien de la main","Il répare un lit lésé.")]),
      (["On surveille la pousse.","On adresse une pigmentation suspecte."],[("d'abord","médecin de famille","Il vérifie la migration de la tache."),("ensuite","dermatologue","Il biopsie une bande pigmentée sans traumatisme."),("puis","médecin de famille","Il contrôle la repousse.")]),
      "L'ongle repousse en environ 4 mois, en général sans déformation majeure.",
      [("Migration de la tache","Après quelques semaines","Vers le bord libre"),("Signes d'infection","Premiers jours","Absents")],"Le suivi s'arrête quand la tache a migré et que la douleur a disparu.",
      ("On protège les mains au travail.","On trépane tôt l'hématome douloureux.","On biopsie toute pigmentation qui ne migre pas.")),]}
