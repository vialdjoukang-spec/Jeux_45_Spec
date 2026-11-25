from constructeur_agent_45spec import pec
ID = "T16__S1_8-E09"
D = " résumé lu le 25.11.2026]"
AFP = "[Heim et Maughan, Foreign bodies in the ear, nose, and throat, Am Fam Physician 2007;76:1185-9, texte lu sur aafp.org le 25.11.2026 (cotes SORT C)]"
SCH = "[Schulze et al., Pediatric external auditory canal foreign bodies: a review of 698 cases, Otolaryngol Head Neck Surg 2002;127:73-8, PMID 12161734,"+D
DIM = "[DiMuzio et Deschler, Emergency department management of foreign bodies of the external ear canal in children, Otol Neurotol 2002;23:473-5, PMID 12170148,"+D
MAR = "[Marin et Trainor, Foreign body removal from the external auditory canal in a pediatric emergency department, Pediatr Emerg Care 2006;22:630-4, PMID 16983246,"+D
ANS = "[Ansley et Cunningham, Treatment of aural foreign bodies in children, Pediatrics 1998;101:638-41, PMID 9521948,"+D
MSD = "[Kesser, External Ear Obstructions, MSD Manual Professional Edition, revue mai 2026, page lue le 25.11.2026]"
CUR = "[Curry et Maxwell, Management of Foreign Bodies in the Ear Canal, Otolaryngol Clin North Am 2023;56:881-9, PMID 37516654,"+D
AKG = "[Akgül et al., Mechanism of ear canal button battery injury and strategies for mitigation of damage, Acta Otorhinolaryngol Ital 2023;43:149-54, PMID 37099439,"+D
EXP = "Avis d'expert, ORL et urgences pédiatriques (à vérifier)"
_N = [
("def","definition","critère",3,0,AFP,"Le corps étranger du conduit auditif externe est un objet inerte, végétal ou un insecte bloqué dans le conduit ; il touche surtout l'enfant."),
("age","epidemiology","chiffre",2,0,AFP+" ; "+ANS,"Environ 75 % des corps étrangers de l'oreille surviennent avant 8 ans ; les insectes deviennent plus fréquents après 10 ans."),
("objects","epidemiology","terrain particulier",1,0,AFP,"Les objets fréquents sont les perles, les jouets en plastique, les cailloux et les grains de maïs ; l'adulte avec un handicap intellectuel ou une maladie psychique est aussi à risque."),
("hygro","basicSciences","mécanisme",2,0,MSD,"Un corps étranger végétal (haricot, graine) gonfle au contact de l'eau, ce qui complique son extraction."),
("battery","basicSciences","mécanisme",3,0,AFP+" ; "+AKG,"Une pile bouton provoque une nécrose de liquéfaction par le courant électrique et son contenu alcalin, en quelques heures."),
("hx","anamnesis","symptôme",1,0,AFP,"Beaucoup d'enfants n'ont aucun symptôme ; d'autres ont une otalgie, une hypoacousie, une sensation d'oreille pleine ou une otite."),
("buzz","anamnesis","symptôme",1,0,MSD,"Un insecte vivant donne un bourdonnement et une douleur très pénibles."),
("otoscopy","clinicalExam","examen",2,0,AFP,"On examine le conduit à l'otoscope pour préciser la nature de l'objet, sa forme saisissable ou non, sa position et l'état du tympan."),
("orifices","clinicalExam","examen",2,0,AFP,"Les corps étrangers multiples ne sont pas rares chez le petit enfant : après l'extraction, on inspecte tous les orifices de la tête."),
("discharge","presumptionRedFlags","signe",2,0,AFP,"Un écoulement ou une otite externe peuvent révéler un corps étranger méconnu ; on regarde le conduit avant de traiter."),
("urgBatt","presumptionRedFlags","décision",3,0,CUR+" ; "+AFP,"La plupart des corps étrangers de l'oreille se traitent sans urgence, mais une pile ou une substance caustique impose une extraction rapide."),
("visual","workupGoldStandard","examen",1,0,SCH,"L'extraction sous otomicroscopie par l'ORL réussit dans 86 % des cas, contre 77 % sous vision directe aux urgences."),
("audio","workupAlternatives","examen",1,0,AFP,"On envisage une audiométrie si l'on suspecte une lésion du tympan ou une perte auditive."),
("ddx","positiveDiagnosis","diagnostic différentiel",1,0,MSD,"On distingue un bouchon de cérumen, une otite externe, une exostose et un cholestéatome du conduit."),
("grasp","acuteManagement","décision",3,0,AFP+" ; "+DIM,"Un objet saisissable visible (mousse, papier, végétal) se retire à la pince sous vision directe ; un objet lisse et sphérique (perle, caillou) échoue plus souvent et blesse davantage le conduit."),
("graspNum","acuteManagement","chiffre",1,0,DIM,"Aux urgences, les objets non saisissables ont été retirés dans 45 % des cas avec 70 % de complications, contre 64 % et 14 % pour les objets saisissables."),
("first","acuteManagement","décision",2,0,AFP+" ; "+MAR,"La première tentative est décisive : plusieurs tentatives ou plusieurs instruments augmentent l'échec et les complications ; on adresse à l'ORL si plus d'une tentative est nécessaire."),
("insect","acuteManagement","décision",2,0,AFP+" ; "+MSD,"On tue un insecte vivant avant de l'extraire en remplissant le conduit de lidocaïne à 2 %, d'alcool ou d'huile minérale, sauf si le tympan est perforé."),
("noIrrig","acuteManagement","piège",2,0,AFP+" ; "+MSD,"On n'irrigue pas une pile bouton ni un objet végétal ; on n'irrigue pas non plus un tympan perforé."),
("glue","acuteManagement","décision",1,0,AFP,"L'acétone dissout le polystyrène et décolle la colle cyanoacrylate."),
("lac","hospitalizationComplications","complication",1,0,DIM+" ; "+AFP,"Les tentatives répétées provoquent des lacérations du conduit, un saignement qui gêne la vue et enfoncent l'objet."),
("otitisExt","hospitalizationComplications","molécule",1,0,AFP,"On prescrit des gouttes auriculaires antibiotiques en cas d'otite externe associée et on les envisage après une lacération du conduit ; produit et dose à vérifier dans l'AIPS (Swissmedic)."),
("ga","chronicManagement","chiffre",2,0,ANS,"Dans une série de 191 enfants, 30 % ont eu besoin d'une anesthésie générale, surtout les plus jeunes."),
("ent","chronicManagement","décision",1,0,AFP,"On adresse à l'ORL un enfant qui doit être sédaté, un objet coincé dans les deux tiers internes ou contre le tympan, un objet tranchant, une lésion du conduit ou du tympan, ou un échec."),
("delay","prognosisDischarge","pronostic",1,0,MAR,"Un objet présent depuis plus de 24 heures ou un âge de moins de 4 ans n'augmentaient pas l'échec ni les complications dans la série de Marin."),
("checkTM","surveillance","examen",1,0,AFP,"Après l'extraction, on contrôle le conduit et le tympan."),
("swab","followUpNetwork","prévention",1,0,EXP,"On déconseille les cotons-tiges et l'on range les piles bouton hors de portée des enfants (à vérifier)."),
("swiss","followUpNetwork","contexte suisse",1,1,EXP,"En Suisse, le pédiatre ou l'urgentiste tente l'extraction ; l'ORL extrait sous microscope ou sous anesthésie générale, et Tox Info Suisse (145) conseille pour une pile ingérée (à vérifier)."),
]
K = {k: i+1 for i, (k, *_r) in enumerate(_N)}
N = [t[1:] for t in _N]
n = lambda *ks: [K[k] for k in ks]
AM = ["Pile bouton : urgence, pas d'irrigation.","Végétal : pas d'eau.","Insecte : le tuer d'abord.","Perle contre le tympan : ORL.","Une seule tentative.","Inspecter les autres orifices."]
A = lambda *o: list(o)
Q = [
{"f":"A","s":("S1",1,3),"st":"Une fillette de 4 ans est amenée par sa mère, qui l'a vue jouer avec des perles. L'otoscopie montre une perle lisse et ronde au fond de l'oreille droite, au contact du tympan. L'enfant pleure et se débat.",
 "p":"Quelle est votre conduite ?","o":A((1,"L'adresser à l'ORL pour une extraction sous microscope","AFP 2007 ; Schulze 2002."),(0,"Tenter l'extraction à la pince crocodile","Piège : objet lisse, contre le tympan."),(0,"Irriguer le conduit à l'eau chaude","Faux."),(0,"Attendre l'expulsion spontanée","Faux."),(0,"Prescrire des gouttes antibiotiques seules","Faux.")),
 "n":n("grasp","ent","visual","otoscopy"),"a":"piège","d":4,"l":("Objet lisse.","Non saisissable.","Contre le tympan.","Enfant agité.","ORL.","Pince.","Sphérique et profond : ORL.")},
{"f":"A","s":("S1",2,3),"st":"L'ORL retire la perle sous microscope. La mère demande s'il faut regarder ailleurs.",
 "p":"Que faites-vous ensuite ?","o":A((1,"Inspecter l'autre oreille et les narines","AFP 2007."),(0,"Faire une radiographie du thorax systématique","Faux."),(0,"Rien de plus","Piège."),(0,"Une IRM des rochers","Faux."),(0,"Un scanner cérébral","Faux.")),
 "n":n("orifices","checkTM"),"a":"piège","d":3,"l":("Après extraction.","Objets multiples.","Autres orifices.","Petit enfant.","Inspecter.","S'arrêter.","Inspecter tous les orifices.")},
{"f":"A","s":("S1",3,3),"st":"Le conduit présente une petite éraflure qui saigne un peu ; le tympan est intact.",
 "p":"Que prescrivez-vous ?","o":A((1,"Envisager des gouttes auriculaires antibiotiques","AFP 2007."),(0,"Un antibiotique par voie orale de 10 jours","Faux."),(0,"Une irrigation quotidienne","Faux."),(0,"Une hospitalisation","Faux."),(0,"Une suture","Faux.")),
 "n":n("otitisExt","lac"),"a":"application","d":3,"l":("Lésion.","Conduit.","Éraflure.","Tympan intact.","Gouttes.","Antibiotique oral.","Lacération : gouttes à envisager.")},
{"f":"A","st":"Un garçon de 5 ans a mis un haricot sec dans son oreille hier. L'objet est visible au tiers externe du conduit.",
 "p":"Quelle technique évitez-vous ?","o":A((1,"L'irrigation à l'eau","MSD 2026 : l'objet gonfle."),(0,"La pince sous vision directe","Faux : objet saisissable."),(0,"L'aspiration douce","Faux."),(0,"La curette auriculaire","Faux."),(0,"L'examen à l'otoscope","Faux.")),
 "n":n("hygro","noIrrig","grasp"),"a":"piège","d":4,"l":("Végétal.","Gonflement.","Haricot.","Saisissable.","Pas d'eau.","Irriguer.","Végétal : pas d'irrigation.")},
{"f":"A","st":"Un homme de 32 ans se réveille avec un bourdonnement intense et une douleur de l'oreille gauche ; il a campé la nuit. L'otoscopie montre un petit insecte qui bouge ; le tympan paraît intact.",
 "p":"Quelle est la première mesure ?","o":A((1,"Tuer l'insecte en remplissant le conduit de lidocaïne ou d'huile minérale, puis l'extraire","AFP 2007 ; MSD 2026."),(0,"L'extraire vivant à la pince","Piège."),(0,"Prescrire des gouttes antibiotiques et revoir dans une semaine","Faux."),(0,"Faire un scanner","Faux."),(0,"Attendre qu'il sorte seul","Faux.")),
 "n":n("insect","buzz","age"),"a":"piège","d":4,"l":("Insecte.","Vivant.","Bourdonnement.","Tympan intact.","Tuer d'abord.","Pince.","Insecte : le tuer d'abord.")},
{"f":"A","st":"Un garçon de 3 ans a joué avec la télécommande ; il se plaint de l'oreille. L'otoscopie montre un petit disque métallique brillant dans le conduit.",
 "p":"Quelle est votre conduite ?","o":A((1,"Une extraction rapide, sans irrigation, par l'ORL si besoin","AFP 2007 ; Curry 2023."),(0,"Une irrigation pour le décoller","Piège : nécrose."),(0,"Un rendez-vous ORL dans une semaine","Faux."),(0,"Des gouttes d'huile et une attente","Faux."),(0,"Une radiographie et une surveillance","Faux.")),
 "n":n("battery","urgBatt","noIrrig"),"a":"piège","d":5,"l":("Télécommande.","Pile.","Disque métallique.","Nécrose rapide.","Extraire vite.","Irriguer.","Pile : urgence sans eau.")},
{"f":"A","st":"Aux urgences, un interne a fait deux tentatives infructueuses à la pince puis à la curette sur un caillou dans l'oreille d'un enfant de 6 ans. Le conduit saigne.",
 "p":"Quelle est la conduite ?","o":A((1,"Arrêter et adresser à l'ORL","Marin 2006 ; AFP 2007."),(0,"Essayer un troisième instrument","Piège : échec et complications."),(0,"Irriguer pour nettoyer le sang","Faux."),(0,"Laisser en place sans suivi","Faux."),(0,"Faire une sédation aux urgences et réessayer seul","Faux.")),
 "n":n("first","lac","ga"),"a":"piège","d":4,"l":("Échecs.","Saignement.","Deux tentatives.","Objet dur.","ORL.","Troisième essai.","Une tentative, puis ORL.")},
{"f":"A","st":"Une fillette de 3 ans est traitée depuis 10 jours par des gouttes pour un écoulement malodorant de l'oreille droite, sans amélioration. Elle n'a pas de fièvre. L'oreille gauche est normale.",
 "p":"Quel est votre prochain geste ?","o":A((1,"Nettoyer le conduit et l'examiner à l'otoscope, au besoin au microscope","AFP 2007."),(0,"Changer de gouttes sans regarder","Piège."),(0,"Prescrire de l'amoxicilline orale","Faux."),(0,"Faire un scanner d'emblée","Faux."),(0,"Rassurer et attendre","Faux.")),
 "n":n("discharge","otoscopy","ddx","hx"),"a":"piège","d":4,"l":("Écoulement.","Unilatéral.","Échec des gouttes.","Petite enfant.","Regarder.","Changer de gouttes.","Écoulement rebelle : chercher l'objet.")},
{"f":"A","m":0,"st":"Vous évoquez un corps étranger du conduit auditif externe.",
 "p":"Quelle tranche d'âge est la plus touchée ?","o":A((1,"Les enfants de moins de 8 ans","AFP 2007 ; Ansley 1998."),(0,"Les adolescents","Faux."),(0,"Les adultes de 40 ans","Faux."),(0,"Les personnes âgées","Faux."),(0,"Les nourrissons de moins de 6 mois","Faux.")),
 "n":n("age","def"),"a":"direct","d":1,"l":("Épidémiologie.","Jeu.","Moins de 8 ans.","75 %.","Nommer.","Adolescents.","Petit enfant.")},
{"f":"A","m":0,"st":"Vous retirez un corps étranger du conduit auditif externe.",
 "p":"Quel objet se retire le plus facilement aux urgences ?","o":A((1,"Un morceau de mousse ou de papier","AFP 2007 ; DiMuzio 2002."),(0,"Une perle lisse","Faux."),(0,"Un caillou rond","Faux."),(0,"Un grain de maïs","Faux."),(0,"Une bille","Faux.")),
 "n":n("grasp","graspNum"),"a":"direct","d":2,"l":("Saisissable.","Forme.","Mousse.","Prise.","Choisir.","Perle.","Saisissable : pince.")},
{"f":"A","m":0,"st":"Un enfant de 2 ans a un corps étranger dans le conduit auditif externe et ne coopère pas.",
 "p":"Quelle proportion d'enfants a eu besoin d'une anesthésie générale dans la série d'Ansley ?","o":A((1,"Environ 30 %","Ansley 1998."),(0,"Environ 1 %","Faux."),(0,"Environ 90 %","Faux."),(0,"Aucun","Faux."),(0,"Environ 60 %","Faux.")),
 "n":n("ga","ent"),"a":"direct","d":3,"l":("Anesthésie.","Coopération.","30 %.","Jeune âge.","Chiffrer.","1 %.","30 %.")},
{"f":"A","m":0,"st":"Un patient a de la colle cyanoacrylate dans le conduit auditif externe.",
 "p":"Quel produit aide à la décoller ?","o":A((1,"L'acétone","AFP 2007."),(0,"L'eau oxygénée","Faux."),(0,"L'huile de paraffine","Faux."),(0,"Le sérum physiologique","Faux."),(0,"L'alcool à 70 %","Faux.")),
 "n":n("glue","objects"),"a":"application","d":3,"l":("Colle.","Polymère.","Cyanoacrylate.","Solvant.","Décoller.","Eau oxygénée.","Acétone.")},
{"f":"A","m":0,"st":"Après l'extraction d'un corps étranger, un enfant semble mal entendre de cette oreille et le tympan est lésé.",
 "p":"Quel examen envisagez-vous ?","o":A((1,"Une audiométrie","AFP 2007."),(0,"Un EEG","Faux."),(0,"Une IRM cérébrale","Faux."),(0,"Une radiographie du crâne","Faux."),(0,"Aucun","Faux.")),
 "n":n("audio","checkTM"),"a":"application","d":3,"l":("Audition.","Tympan.","Hypoacousie.","Lésion.","Mesurer.","EEG.","Audiométrie.")},
{"f":"A","m":0,"st":"Des parents demandent comment éviter un nouveau corps étranger de l'oreille chez leur enfant.",
 "p":"Quel conseil donnez-vous ?","o":A((1,"Ranger les piles bouton et les petits objets hors de portée et éviter les cotons-tiges","Expert (à vérifier)."),(0,"Mettre des gouttes d'huile chaque jour","Faux."),(0,"Faire laver les oreilles à l'eau chaque semaine","Faux."),(0,"Faire porter des bouchons en permanence","Faux."),(0,"Aucun conseil n'est utile","Faux.")),
 "n":n("swab","swiss"),"a":"application","d":2,"l":("Prévention.","Accès.","Piles.","Cotons-tiges.","Conseiller.","Huile.","Hors de portée.")},
{"f":"Kprim","m":0,"st":"Vous retirez un corps étranger du conduit auditif externe.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"La première tentative est la plus importante.","AFP 2007."),(1,"Plusieurs instruments augmentent l'échec et les complications.","Marin 2006."),(1,"Un écoulement unilatéral rebelle chez le petit enfant fait chercher un objet dans le conduit.","AFP 2007."),(0,"On irrigue toujours en premier.","Faux.")),
 "n":n("first","grasp","discharge"),"a":"direct","d":2,"l":("Technique.","Échec.","Première tentative.","Instruments.","Décider.","Irrigation.","Une tentative.")},
{"f":"Kprim","m":0,"st":"Vous décidez d'irriguer un conduit auditif externe contenant un corps étranger.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"On n'irrigue pas une pile bouton.","AFP 2007."),(1,"On n'irrigue pas un objet végétal.","MSD 2026."),(1,"On n'irrigue pas un tympan perforé.","MSD 2026."),(0,"On irrigue une perle en plastique en toute circonstance.","Faux.")),
 "n":n("noIrrig","hygro","battery","urgBatt"),"a":"direct","d":3,"l":("Irrigation.","Contre-indications.","Pile.","Végétal.","Choisir.","Toujours.","Pile, végétal, perforation.")},
{"f":"Kprim","m":0,"st":"Vous lisez les séries pédiatriques de corps étrangers du conduit auditif externe.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"L'otomicroscopie de l'ORL réussit plus souvent que la vision directe.","Schulze 2002."),(1,"Les objets non saisissables causent plus de complications.","DiMuzio 2002."),(1,"Dans la série de Marin, un objet présent depuis plus de 24 h n'augmentait pas l'échec.","Marin 2006."),(0,"Les objets saisissables ont plus de complications que les objets lisses.","Faux.")),
 "n":n("visual","graspNum","delay"),"a":"direct","d":3,"l":("Preuve.","Séries.","Microscope.","Saisissable.","Lire.","Inversion.","Microscope, objets lisses.")},
{"f":"Kprim","m":0,"st":"Un insecte vivant se trouve dans le conduit auditif externe.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"On le tue avant l'extraction.","AFP 2007."),(1,"La lidocaïne à 2 % convient si le tympan est intact.","AFP 2007."),(1,"On n'instille pas ces produits si le tympan est perforé.","AFP 2007."),(0,"On l'extrait vivant pour éviter une réaction.","Faux.")),
 "n":n("insect","buzz","objects"),"a":"application","d":3,"l":("Insecte.","Vivant.","Lidocaïne.","Tympan.","Tuer.","Vivant.","Tuer d'abord.")},
{"f":"MenuLong","st":"Un garçon de 5 ans a quelque chose dans l'oreille gauche depuis ce matin. Vous hésitez à tenter l'extraction aux urgences.",
 "p":"Choisissez les TROIS situations qui justifient d'adresser d'emblée à l'ORL.","o":A((1,"Un objet lisse et sphérique contre le tympan","AFP 2007."),(1,"Un objet à bords tranchants comme un éclat de verre","AFP 2007."),(1,"Un enfant qui ne coopère pas et doit être sédaté","AFP 2007."),(0,"Un morceau de papier au tiers externe","Faux."),(0,"Un âge de 5 ans","Faux."),(0,"Un objet présent depuis 8 heures","Faux."),(0,"Un conduit sans lésion","Faux."),(0,"Un tympan intact","Faux."),(0,"Une mousse visible","Faux."),(0,"Une absence de douleur","Faux."),(0,"Un objet saisissable","Faux."),(0,"Une première consultation","Faux.")),
 "n":n("ent","grasp","delay","otoscopy","def"),"a":"piège","d":4,"l":("Objet.","Forme.","Contre le tympan.","Tranchant.","Adresser.","Papier.","Lisse, tranchant, sédation.")},
{"f":"MenuLong","m":0,"st":"Vous venez de retirer un corps étranger du conduit auditif externe d'un enfant de 3 ans.",
 "p":"Choisissez les TROIS gestes justes.","o":A((1,"Inspecter l'autre oreille et les narines","AFP 2007."),(1,"Contrôler le conduit et le tympan","AFP 2007."),(1,"Envisager des gouttes antibiotiques en cas de lacération","AFP 2007."),(0,"Faire une radiographie du thorax","Faux."),(0,"Prescrire un antibiotique oral","Faux."),(0,"Irriguer chaque jour","Faux."),(0,"Faire un scanner","Faux."),(0,"Hospitaliser","Faux."),(0,"Interdire la piscine un an","Faux."),(0,"Faire une IRM","Faux."),(0,"Mettre des gouttes d'huile","Faux."),(0,"Ne rien vérifier","Faux.")),
 "n":n("orifices","checkTM","otitisExt","swiss","otoscopy"),"a":"application","d":3,"l":("Après.","Contrôle.","Orifices.","Tympan.","Vérifier.","Radiographie.","Orifices, tympan, gouttes.")},
]
for _q in Q: _q["src"] = AFP
Q[0]["src"] = [AFP, SCH]; Q[3]["src"] = MSD; Q[4]["src"] = [AFP, MSD]; Q[5]["src"] = [AFP, CUR, AKG]
Q[6]["src"] = [MAR, AFP]; Q[8]["src"] = [AFP, ANS]; Q[9]["src"] = [AFP, DIM]; Q[10]["src"] = ANS
Q[13]["src"] = EXP; Q[14]["src"] = [AFP, MAR]; Q[15]["src"] = [AFP, MSD]; Q[16]["src"] = [SCH, DIM, MAR]
C = {"theme":"Corps étranger du conduit auditif externe : enfant de moins de 8 ans, objet saisissable ou lisse, pile bouton en urgence, végétal et perforation sans irrigation, insecte tué avant l'extraction, une seule tentative puis ORL, otomicroscopie, inspection des autres orifices, écoulement rebelle révélateur",
 "notions":[
  {"titre":"Comprendre","rub":["definition","epidemiology","basicSciences","anamnesis"],"comment":"Le petit enfant introduit des objets ; certains gonflent ou brûlent.",
   "points":["75 % avant 8 ans.","Pile : nécrose."],"sources":[AFP,ANS,MSD,AKG]},
  {"titre":"Évaluer","rub":["clinicalExam","presumptionRedFlags","workupGoldStandard","workupAlternatives"],"comment":"L'otoscope précise l'objet, sa forme et le tympan.",
   "arbre":[("d1",None,"Objet dans l'oreille","On examine à l'otoscope.",None,None),("d2","d1","Pile bouton","On extrait rapidement sans eau.",None,None),("d3","d1","Insecte vivant","On le tue, puis on l'extrait.",None,None),("d4","d1","Objet saisissable externe","On l'extrait à la pince.",None,None),("d5","d1","Objet lisse profond ou enfant agité","On adresse à l'ORL.",None,None)],
   "points":["Écoulement rebelle : regarder."],"sources":[AFP,CUR,SCH]},
  {"titre":"Traiter","rub":["positiveDiagnosis","acuteManagement","hospitalizationComplications","chronicManagement"],"comment":"La première tentative compte ; on n'insiste pas.",
   "tab":(["Objet","Conduite","Source"],[["Saisissable visible","Pince sous vision directe",[("AFP 2007","Cote C.")]],["Lisse ou contre le tympan","ORL, microscope",[("Schulze 2002","86 % contre 77 %.")]],["Pile bouton","Extraction rapide, sans eau",[("Curry 2023","Prompt removal.")]],["Végétal","Pas d'irrigation",[("MSD 2026","Gonfle.")]],["Insecte vivant","Lidocaïne, alcool ou huile, puis extraction",[("AFP 2007","Si tympan intact.")]]]),
   "points":["Plus d'une tentative : ORL."],"sources":[AFP,MAR,DIM,MSD]},
  {"titre":"Suivre","rub":["prognosisDischarge","surveillance","followUpNetwork"],"comment":"On contrôle le tympan et l'on prévient la récidive.",
   "points":["Inspecter les autres orifices."],"sources":[AFP,MAR,EXP]}],
 "ssp":("S8.6","Lésion par corps étranger",True,[
   ("n1",None,"Objet dans l'oreille","On examine à l'otoscope.","oreille","c2"),
   ("n2","n1","Pile bouton","On extrait sans délai et sans eau.","oreille","c3"),
   ("n3","n1","Insecte vivant","On le tue avant l'extraction.","oreille","c3"),
   ("n4","n1","Objet lisse profond ou échec","On adresse à l'ORL.","oreille","c3"),
   ("n5","n1","Écoulement rebelle","On nettoie et l'on regarde le conduit.","oreille","c2"),
   ("n6","n4","Après l'extraction","On contrôle le tympan et les autres orifices.","oreille","c4")]),
 "pec":[
  pec("oreille","Corps étranger du conduit auditif externe",["On retire l'objet sans blesser le conduit ni le tympan.","On traite en urgence une pile bouton."],
      ["On examine le conduit à l'otoscope.","On précise la nature de l'objet et l'heure de l'introduction."],
      [("Lidocaïne 2 % (instillation auriculaire)","Instillation dans le conduit pour tuer un insecte si le tympan est intact ; usage à vérifier dans l'AIPS (Swissmedic).","Elle tue l'insecte et soulage avant l'extraction.",AFP),("Gouttes auriculaires antibiotiques","Produit et dose à vérifier dans l'AIPS (Swissmedic).","Elles traitent une otite externe ou une lacération du conduit.",AFP)],
      [("geste ou chirurgie","On extrait l'objet à la pince, à la curette ou par aspiration, ou sous microscope.","On libère le conduit en une seule tentative."),("éducation thérapeutique","On explique aux parents le rangement des piles et des petits objets.","On prévient la récidive.")],
      [("S Urgences vitales Triage 144 REGA","On trie la pile bouton comme une urgence."),("N Médecine sociale Prévention OFSP","On prévient les accidents domestiques de l'enfant.")],
      (["On repère une pile bouton.","On n'irrigue pas.","On adresse vite à l'ORL."],[("d'abord","urgentiste","Il identifie la pile à l'otoscope."),("ensuite","ORL","Il l'extrait sans délai."),("puis","ORL","Il contrôle le conduit et le tympan.")]),
      (["On tente une extraction.","On adresse après un échec."],[("d'abord","pédiatre","Il tente une extraction d'un objet saisissable."),("ensuite","ORL","Il extrait sous microscope ou sous anesthésie générale."),("puis","pédiatre","Il inspecte les autres orifices.")]),
      "La plupart des objets s'extraient sans séquelle quand on évite les tentatives répétées.",
      [("Conduit et tympan","Après l'extraction","Intacts"),("Écoulement","Quelques jours","Absent")],"Le suivi s'arrête quand le conduit est propre et le tympan intact.",
      ("On range les piles bouton hors de portée.","On extrait en une seule tentative.","On contrôle l'audition après une lésion du tympan.")),]}
