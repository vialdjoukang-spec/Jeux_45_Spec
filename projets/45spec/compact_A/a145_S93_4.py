from constructeur_agent_45spec import pec
ID = "S93.4__O4_1-E02"
D = " résumé lu le 25.11.2026]"
VUU = "[Vuurberg et al., Diagnosis, treatment and prevention of ankle sprains: update of an evidence-based clinical guideline, Br J Sports Med 2018;52:956, PMID 29514819,"+D
STI = "[Stiell et al., Decision rules for the use of radiography in acute ankle injuries. Refinement and prospective validation, JAMA 1993;269:1127-32, PMID 8433468,"+D
BAC = "[Bachmann et al., Accuracy of Ottawa ankle rules to exclude fractures of the ankle and mid-foot: systematic review, BMJ 2003;326:417, PMID 12595378,"+D
ACI = "[Agency for Clinical Innovation NSW, ECAT appendix « Ottawa ankle rules (adult) », aci.health.nsw.gov.au, page lue le 25.11.2026]"
LAM = "[Lamb et al., Mechanical supports for acute, severe ankle sprain: a pragmatic, multicentre, randomised controlled trial (CAST), Lancet 2009;373:575-81, PMID 19217992,"+D
DIJ = "[van Dijk et al., Physical examination is sufficient for the diagnosis of sprained ankles, J Bone Joint Surg Br 1996;78:958-62, PMID 8951015,"+D
HUP = "[Hupperets et al., Effect of unsupervised home based proprioceptive training on recurrences of ankle sprain, BMJ 2009;339:b2684, PMID 19589822,"+D
CMP = "[Compendium.ch, résumé (Brevier) de Brufen (ibuprofène), lu le 25.11.2026 ; AIPS complète à vérifier (Swissmedic)]"
EXP = "Avis d'expert, orthopédie, médecine du sport et urgences (à vérifier)"
_N = [
("def","definition","critère",3,0,EXP,"L'entorse latérale de la cheville est une distension ou une rupture du ligament talo-fibulaire antérieur, parfois du calcanéo-fibulaire, lors d'un mouvement d'inversion du pied."),
("epi","epidemiology","chiffre",1,0,BAC,"Moins de 15 % des patients radiographiés pour un traumatisme de la cheville ont une fracture."),
("sport","epidemiology","terrain particulier",1,0,VUU,"La pratique de certains sports augmente le risque d'entorse latérale."),
("seq","basicSciences","mécanisme",2,0,EXP,"Les faisceaux se rompent dans l'ordre : talo-fibulaire antérieur, puis calcanéo-fibulaire, plus rarement talo-fibulaire postérieur."),
("hx","anamnesis","symptôme",1,0,EXP,"On précise le mécanisme (inversion), la capacité à marcher juste après l'accident, un craquement et les entorses antérieures."),
("ottAnk","clinicalExam","critère",3,0,STI+" ; "+ACI,"Règle d'Ottawa pour la cheville : on radiographie si le bord postérieur des 6 derniers centimètres ou la pointe d'une malléole est douloureux, ou si le patient ne peut faire 4 pas juste après l'accident et à la consultation."),
("ottFoot","clinicalExam","critère",2,0,STI+" ; "+ACI,"Règle d'Ottawa pour le médio-pied : on radiographie le pied si la base du 5e métatarsien ou l'os naviculaire est douloureux, ou si le patient ne peut faire 4 pas."),
("delayed","clinicalExam","examen",3,0,DIJ+" ; "+VUU,"L'examen différé, 4 à 5 jours après l'accident, évalue le mieux la gravité de l'atteinte ligamentaire."),
("delayNum","clinicalExam","chiffre",1,0,DIJ,"L'examen différé à 5 jours a une sensibilité de 96 % et une spécificité de 84 % pour une lésion ligamentaire, comme l'arthrographie."),
("maison","presumptionRedFlags","diagnostic différentiel",2,0,EXP,"Une douleur du péroné proximal ou de la face médiale fait chercher une lésion de la syndesmose ou une fracture de Maisonneuve, que la règle d'Ottawa ne couvre pas (à vérifier)."),
("red","presumptionRedFlags","complication",1,0,EXP,"Une déformation, un déficit neurovasculaire ou une plaie imposent une radiographie et un avis orthopédique immédiat."),
("sens","workupGoldStandard","chiffre",2,0,STI+" ; "+BAC,"La règle d'Ottawa a une sensibilité proche de 100 % pour les fractures ; elle réduit de 30 à 40 % les radiographies inutiles."),
("lr","workupGoldStandard","chiffre",1,0,BAC,"Son rapport de vraisemblance négatif vaut 0,08 ; avec 15 % de fractures, une règle négative laisse moins de 1,4 % de fractures."),
("kids","workupAlternatives","terrain particulier",2,0,BAC,"La règle d'Ottawa reste fiable chez l'enfant (rapport de vraisemblance négatif 0,07)."),
("mri","workupAlternatives","piège",1,0,EXP,"L'IRM n'est pas un examen de routine de l'entorse latérale ; on la réserve à une douleur persistante malgré la rééducation (à vérifier)."),
("ddx","positiveDiagnosis","diagnostic différentiel",1,0,EXP,"On distingue une fracture malléolaire, une fracture de la base du 5e métatarsien, une lésion de la syndesmose et une lésion ostéochondrale du dôme du talus."),
("func","acuteManagement","décision",3,0,VUU,"Après le diagnostic, le patient gagne le plus à un traitement fonctionnel : bandage adhésif ou orthèse, avec un programme d'exercices."),
("cast","acuteManagement","décision",2,0,LAM,"Dans une entorse sévère, 10 jours de botte plâtrée sous le genou ou une orthèse Aircast accélèrent la récupération par rapport à un simple bandage tubulaire ; à 9 mois, la différence disparaît."),
("shortImm","acuteManagement","décision",1,0,VUU,"Une courte immobilisation peut soulager la douleur et l'œdème, mais elle ne remplace pas la mise en charge et les exercices."),
("nsaid","acuteManagement","molécule",2,0,VUU+" ; "+CMP,"Les AINS réduisent la douleur et l'œdème, mais ils ont des complications et pourraient freiner la cicatrisation ; ibuprofène : dose maximale de 2400 mg par jour chez l'adulte selon le Compendium (à vérifier dans l'AIPS)."),
("nsaidCI","hospitalizationComplications","piège",1,0,CMP,"L'ibuprofène est contre-indiqué en cas d'ulcère actif, d'insuffisance rénale sévère (clairance < 30 ml/min), d'insuffisance cardiaque NYHA III–IV et au 3e trimestre de la grossesse."),
("thrombo","hospitalizationComplications","complication",1,0,LAM,"Dans l'essai CAST, des thromboses veineuses profondes (3) et des embolies pulmonaires (2) sont survenues, tous traitements confondus."),
("exer","chronicManagement","décision",2,0,VUU,"Un programme d'exercices supervisé est préféré aux moyens passifs, car il restaure la stabilité fonctionnelle."),
("surgery","chronicManagement","décision",1,0,VUU,"On réserve la chirurgie aux échecs d'un traitement par exercices bien conduit."),
("progn","prognosisDischarge","pronostic",1,0,LAM,"Les écarts entre supports s'effacent à 9 mois ; la plupart des patients récupèrent."),
("recur","surveillance","prévention",2,0,HUP,"Un programme proprioceptif à domicile de 8 semaines réduit les récidives de 33 % à 22 % (réduction du risque de 35 %, 9 patients à traiter)."),
("brace","surveillance","prévention",1,0,VUU,"L'orthèse de cheville prévient efficacement les récidives d'entorse latérale."),
("swiss","followUpNetwork","contexte suisse",1,1,EXP,"En Suisse, l'assurance-accidents (LAA) prend en charge l'entorse ; le médecin de famille prescrit la physiothérapie et adresse à l'orthopédiste en cas d'instabilité persistante (à vérifier)."),
]
K = {k: i+1 for i, (k, *_r) in enumerate(_N)}
N = [t[1:] for t in _N]
n = lambda *ks: [K[k] for k in ks]
AM = ["Ottawa : bord postérieur ou pointe des malléoles, 4 pas.","Base du 5e métatarsien, naviculaire : radiographie du pied.","Péroné proximal : Maisonneuve.","Examen différé à 4–5 jours.","Traitement fonctionnel et exercices.","Proprioception contre la récidive."]
A = lambda *o: list(o)
Q = [
{"f":"A","s":("S1",1,3),"st":"Une joueuse de volley de 24 ans s'est tordu la cheville en retombant sur le pied d'une adversaire, le pied en inversion. Elle a marché jusqu'au vestiaire. La région située en avant de la malléole externe est gonflée et douloureuse ; le bord postérieur et la pointe des deux malléoles, la base du 5e métatarsien et l'os naviculaire sont indolores.",
 "p":"Quelle est votre conduite ?","o":A((1,"Aucune radiographie ; traitement fonctionnel","Stiell 1993 : règle d'Ottawa négative."),(0,"Une radiographie de la cheville, car l'œdème est important","Piège : l'œdème n'est pas un critère."),(0,"Une IRM en urgence","Faux."),(0,"Une radiographie du pied","Faux."),(0,"Un scanner","Faux.")),
 "n":n("ottAnk","sens","func","hx"),"a":"piège","d":4,"l":("Inversion.","Faisceau antérieur.","Œdème prémalléolaire.","Ottawa négative.","Pas de radiographie.","Radiographier l'œdème.","Ottawa négative : pas de cliché.")},
{"f":"A","s":("S1",2,3),"st":"Le lendemain, la cheville est très gonflée ; vous ne pouvez pas juger la stabilité. Elle veut savoir si quelque chose est rompu.",
 "p":"Que proposez-vous ?","o":A((1,"Un nouvel examen clinique 4 à 5 jours après l'accident","van Dijk 1996 ; Vuurberg 2018."),(0,"Une IRM le jour même","Piège."),(0,"Une arthrographie","Faux."),(0,"Une échographie de contrôle chaque jour","Faux."),(0,"Une chirurgie exploratrice","Faux.")),
 "n":n("delayed","delayNum","mri"),"a":"piège","d":4,"l":("Gravité.","Œdème.","Examen gêné.","Délai.","Réexaminer.","IRM.","Examen différé à 4–5 jours.")},
{"f":"A","s":("S1",3,3),"st":"Au 5e jour, le tiroir antérieur est positif et un hématome est apparu. La patiente veut reprendre le volley.",
 "p":"Quelle prise en charge recommandez-vous ?","o":A((1,"Une orthèse ou un bandage adhésif, avec un programme d'exercices","Vuurberg 2018."),(0,"Une suture chirurgicale d'emblée","Faux : chirurgie après échec des exercices."),(0,"Six semaines de plâtre sans appui","Faux."),(0,"Le repos strict sans exercice","Faux."),(0,"Des ultrasons seuls","Faux.")),
 "n":n("func","surgery","exer","def","seq"),"a":"application","d":3,"l":("Rupture.","Instabilité.","Tiroir positif.","Hématome.","Traitement fonctionnel.","Opérer.","Orthèse et exercices.")},
{"f":"A","st":"Un homme de 35 ans s'est tordu le pied en inversion en descendant un trottoir. Il marche en boitant. La pointe des malléoles est indolore, mais la base du 5e métatarsien est douloureuse à la palpation.",
 "p":"Quel examen demandez-vous ?","o":A((1,"Une radiographie du pied","Stiell 1993 ; ACI NSW."),(0,"Une radiographie de la cheville seule","Piège : la zone douloureuse est au pied."),(0,"Aucun examen","Faux."),(0,"Une IRM","Faux."),(0,"Une scintigraphie","Faux.")),
 "n":n("ottFoot","ddx","sens"),"a":"piège","d":4,"l":("Inversion.","Avulsion.","Base du 5e.","Ottawa du pied.","Cliché du pied.","Cliché de cheville.","Base du 5e : pied.")},
{"f":"A","st":"Un footballeur de 28 ans a subi une torsion en rotation externe. La pointe des malléoles est indolore et il fait 4 pas. Il a mal à la face médiale de la cheville et sous le genou, à la tête du péroné.",
 "p":"Quelle est votre conduite ?","o":A((1,"Une radiographie de la jambe entière et de la cheville","Expert (à vérifier) : Maisonneuve."),(0,"Aucune radiographie, car la règle d'Ottawa est négative","Piège : la règle ne couvre pas le péroné proximal."),(0,"Un bandage et une reprise du sport","Faux."),(0,"Une radiographie du pied","Faux."),(0,"Une échographie du genou seule","Faux.")),
 "n":n("maison","ottAnk","red"),"a":"piège","d":5,"l":("Rotation externe.","Syndesmose.","Péroné proximal.","Hors Ottawa.","Jambe entière.","Ottawa négative.","Péroné proximal : Maisonneuve.")},
{"f":"A","st":"Un garçon de 10 ans s'est tordu la cheville en jouant. Il fait 4 pas sans aide ; la palpation des malléoles, de la base du 5e métatarsien et de l'os naviculaire est indolore. Les parents réclament une radiographie, car il est en croissance.",
 "p":"Que leur répondez-vous ?","o":A((1,"La règle d'Ottawa reste fiable chez l'enfant : pas de radiographie","Bachmann 2003."),(0,"La règle ne s'applique pas à l'enfant : radiographie","Piège."),(0,"Une IRM des cartilages","Faux."),(0,"Une radiographie comparative des deux chevilles","Faux."),(0,"Un plâtre préventif","Faux.")),
 "n":n("kids","lr","ottAnk"),"a":"piège","d":4,"l":("Enfant.","Cartilage.","Ottawa négative.","Fiable chez l'enfant.","Pas de cliché.","Âge.","Enfant : Ottawa vaut aussi.")},
{"f":"A","st":"Une femme de 40 ans s'est tordu la cheville en inversion hier. Elle ne peut pas faire 4 pas ; aucune fracture n'apparaît à la radiographie. L'œdème est majeur.",
 "p":"Quel support accélère le plus la récupération à 3 mois ?","o":A((1,"Une botte plâtrée sous le genou pendant 10 jours","Lamb 2009 (CAST)."),(0,"Un bandage tubulaire seul","Piège : le moins efficace."),(0,"Une botte articulée de type Bledsoe","Faux : sans bénéfice."),(0,"Six semaines sans appui","Faux."),(0,"Aucun support","Faux.")),
 "n":n("cast","func","thrombo"),"a":"piège","d":4,"l":("Sévère.","Rupture.","Pas d'appui.","Radiographie normale.","Plâtre 10 jours.","Bandage tubulaire.","Sévère : 10 jours de botte.")},
{"f":"A","st":"Un basketteur de 22 ans en est à sa troisième torsion de la même cheville en un an. Il veut éviter une nouvelle blessure.",
 "p":"Quelle mesure a fait ses preuves ?","o":A((1,"Un programme proprioceptif à domicile de 8 semaines","Hupperets 2009."),(0,"Des AINS au long cours","Faux."),(0,"Une IRM annuelle","Faux."),(0,"Un arrêt définitif du sport","Faux."),(0,"Des infiltrations","Faux.")),
 "n":n("recur","brace","exer"),"a":"application","d":4,"l":("Récidive.","Proprioception.","Trois torsions.","Instabilité.","Programme proprioceptif.","AINS.","Proprioception, orthèse.")},
{"f":"A","m":0,"st":"Vous expliquez le mécanisme d'une entorse latérale de la cheville.",
 "p":"Quel faisceau se rompt le plus souvent en premier ?","o":A((1,"Le ligament talo-fibulaire antérieur","Expert."),(0,"Le ligament deltoïde","Faux."),(0,"Le ligament talo-fibulaire postérieur","Faux."),(0,"Le tendon d'Achille","Faux."),(0,"La syndesmose","Faux.")),
 "n":n("seq","def"),"a":"direct","d":1,"l":("Anatomie.","Inversion.","Faisceau antérieur.","Ordre.","Nommer.","Deltoïde.","Talo-fibulaire antérieur.")},
{"f":"A","m":0,"st":"Vous appliquez la règle d'Ottawa à une entorse de la cheville.",
 "p":"Combien de pas le patient doit-il pouvoir faire ?","o":A((1,"4 pas, juste après l'accident et à la consultation","Stiell 1993 ; ACI NSW."),(0,"10 pas","Faux."),(0,"1 pas","Faux."),(0,"Aucun critère de marche","Faux."),(0,"20 mètres","Faux.")),
 "n":n("ottAnk","sens"),"a":"direct","d":2,"l":("Règle.","Appui.","4 pas.","Deux moments.","Appliquer.","10 pas.","4 pas.")},
{"f":"A","m":0,"st":"Vous lisez la méta-analyse de Bachmann sur la règle d'Ottawa.",
 "p":"Quelle est sa sensibilité pour les fractures ?","o":A((1,"Presque 100 %","Bachmann 2003."),(0,"Environ 50 %","Faux."),(0,"Environ 70 %","Faux."),(0,"Environ 30 %","Faux."),(0,"Elle n'a pas été mesurée","Faux.")),
 "n":n("sens","lr","epi","kids"),"a":"direct","d":2,"l":("Preuve.","Exclure.","100 %.","Spécificité modeste.","Lire.","50 %.","Sensibilité proche de 100 %.")},
{"f":"A","m":0,"st":"Un patient avec une entorse de la cheville prend de l'ibuprofène et a une insuffisance rénale (clairance 25 ml/min).",
 "p":"Quelle est votre conduite ?","o":A((1,"Arrêter l'ibuprofène, contre-indiqué, et choisir un autre antalgique","Compendium (à vérifier dans l'AIPS)."),(0,"Doubler la dose","Faux."),(0,"Ajouter du diclofénac","Faux."),(0,"Poursuivre sans changement","Faux."),(0,"Ajouter un IEC","Faux.")),
 "n":n("nsaidCI","nsaid"),"a":"application","d":3,"l":("Rein.","Prostaglandines.","Clairance 25.","Contre-indication.","Arrêter.","Doubler.","Clairance < 30 : pas d'AINS.")},
{"f":"A","m":0,"st":"Un patient avec une entorse de la cheville demande à quoi sert l'examen 5 jours après l'accident.",
 "p":"Que lui répondez-vous ?","o":A((1,"Il évalue la lésion ligamentaire aussi bien qu'une arthrographie","van Dijk 1996."),(0,"Il remplace la radiographie des fractures","Faux."),(0,"Il n'apporte rien","Faux."),(0,"Il sert à poser un plâtre","Faux."),(0,"Il dépiste une thrombose","Faux.")),
 "n":n("delayNum","delayed"),"a":"direct","d":3,"l":("Gravité.","Œdème réduit.","Sensibilité 96 %.","Spécificité 84 %.","Expliquer.","Remplacer le cliché.","Examen différé fiable.")},
{"f":"A","m":0,"st":"Une entorse latérale de la cheville reste instable malgré trois mois d'exercices bien conduits.",
 "p":"Quelle est l'étape suivante ?","o":A((1,"Un avis orthopédique en vue d'une chirurgie","Vuurberg 2018."),(0,"Un plâtre de 6 semaines","Faux."),(0,"Des AINS au long cours","Faux."),(0,"Un arrêt définitif du sport","Faux."),(0,"Aucune","Faux.")),
 "n":n("surgery","mri","swiss"),"a":"application","d":3,"l":("Échec.","Instabilité.","Trois mois.","Exercices faits.","Adresser.","Plâtre.","Échec des exercices : chirurgien.")},
{"f":"Kprim","m":0,"st":"Vous décidez d'une radiographie après une entorse de la cheville.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"Une douleur à la pointe de la malléole externe impose une radiographie de la cheville.","Stiell 1993."),(1,"Une douleur de l'os naviculaire impose une radiographie du pied.","Stiell 1993."),(1,"L'incapacité de faire 4 pas impose une radiographie.","Stiell 1993."),(0,"Un œdème important impose une radiographie.","Faux.")),
 "n":n("ottAnk","ottFoot","epi"),"a":"direct","d":2,"l":("Règle.","Fracture.","Malléole, naviculaire.","4 pas.","Radiographier.","Œdème.","Ottawa.")},
{"f":"Kprim","m":0,"st":"Vous traitez une entorse latérale de la cheville sans fracture.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"Le traitement fonctionnel avec exercices est recommandé.","Vuurberg 2018."),(1,"Les exercices supervisés sont préférés aux moyens passifs.","Vuurberg 2018."),(1,"Les AINS ont des effets indésirables et pourraient freiner la cicatrisation.","Vuurberg 2018."),(0,"La chirurgie est le traitement de première intention de la rupture.","Faux.")),
 "n":n("func","exer","nsaid","shortImm"),"a":"direct","d":3,"l":("Traitement.","Cicatrisation.","Fonctionnel.","Exercices.","Traiter.","Chirurgie.","Fonctionnel, exercices.")},
{"f":"Kprim","m":0,"st":"Vous lisez l'essai CAST sur les entorses sévères de la cheville.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"La botte plâtrée de 10 jours a accéléré la récupération.","Lamb 2009."),(1,"Le bandage tubulaire était le moins efficace.","Lamb 2009."),(1,"À 9 mois, les différences avaient disparu.","Lamb 2009."),(0,"La botte Bledsoe était la plus efficace.","Faux.")),
 "n":n("cast","progn","thrombo"),"a":"direct","d":3,"l":("Preuve.","Sévère.","Plâtre.","9 mois.","Lire.","Bledsoe.","Plâtre 10 jours.")},
{"f":"Kprim","m":0,"st":"Vous prévenez la récidive d'une entorse de la cheville.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"Un programme proprioceptif de 8 semaines réduit les récidives.","Hupperets 2009."),(1,"Il faut traiter environ 9 patients pour éviter une récidive.","Hupperets 2009."),(1,"L'orthèse de cheville prévient les récidives.","Vuurberg 2018."),(0,"Le programme doit toujours être supervisé pour agir.","Faux : à domicile.")),
 "n":n("recur","brace","sport"),"a":"direct","d":3,"l":("Prévention.","Proprioception.","8 semaines.","NNT 9.","Prévenir.","Supervision.","Proprioception, orthèse.")},
{"f":"MenuLong","st":"Après une torsion de la cheville en inversion, vous examinez une femme de 30 ans aux urgences.",
 "p":"Choisissez les TROIS constatations qui imposent une radiographie.","o":A((1,"Une douleur du bord postérieur de la malléole interne, 3 cm au-dessus de la pointe","Stiell 1993."),(1,"Une douleur à la base du 5e métatarsien","Stiell 1993."),(1,"L'incapacité de faire 4 pas à la consultation et juste après l'accident","Stiell 1993."),(0,"Un œdème prémalléolaire externe","Faux."),(0,"Un hématome","Faux."),(0,"Un craquement entendu","Faux."),(0,"Une douleur en avant de la malléole externe","Faux."),(0,"Un âge de 30 ans","Faux."),(0,"Une entorse antérieure","Faux."),(0,"Une douleur à la mobilisation passive","Faux."),(0,"Une boiterie en marchant","Faux : elle marche."),(0,"Une pratique sportive","Faux.")),
 "n":n("ottAnk","ottFoot","hx","sens"),"a":"piège","d":4,"l":("Torsion.","Fracture.","Bord postérieur.","4 pas.","Radiographier.","Œdème.","Ottawa.")},
{"f":"MenuLong","m":0,"st":"Vous prenez en charge une entorse latérale de la cheville sans fracture et sans instabilité grave.",
 "p":"Choisissez les TROIS mesures justes.","o":A((1,"Une orthèse ou un bandage adhésif","Vuurberg 2018."),(1,"Un programme d'exercices","Vuurberg 2018."),(1,"Un programme proprioceptif pour prévenir la récidive","Hupperets 2009."),(0,"Une chirurgie d'emblée","Faux."),(0,"Une IRM systématique","Faux."),(0,"Six semaines sans appui","Faux."),(0,"Des AINS pendant 3 mois","Faux."),(0,"Une infiltration de corticoïde","Faux."),(0,"Une anticoagulation systématique","Faux."),(0,"Un arrêt du sport d'un an","Faux."),(0,"Une scintigraphie","Faux."),(0,"Des ultrasons seuls","Faux.")),
 "n":n("func","exer","recur","swiss","ddx","maison"),"a":"application","d":3,"l":("Traitement.","Cicatrisation.","Orthèse.","Exercices.","Traiter.","Chirurgie.","Orthèse, exercices, proprioception.")},
]
for _q in Q: _q["src"] = EXP
for _i in (0, 3, 9, 14, 18): Q[_i]["src"] = [STI, ACI]
Q[1]["src"] = [DIJ, VUU]; Q[12]["src"] = DIJ
for _i in (2, 13, 15): Q[_i]["src"] = VUU
for _i in (5, 10): Q[_i]["src"] = BAC
for _i in (6, 16): Q[_i]["src"] = LAM
for _i in (7, 17): Q[_i]["src"] = [HUP, VUU]
Q[11]["src"] = CMP
Q[19]["src"] = [VUU, HUP]
C = {"theme":"Entorse latérale aiguë de la cheville : mécanisme en inversion, règle d'Ottawa (cheville et médio-pied, 4 pas, enfant), Maisonneuve hors règle, examen différé à 4–5 jours, traitement fonctionnel et exercices, botte de 10 jours dans les formes sévères, AINS prudents, chirurgie après échec, prévention proprioceptive des récidives",
 "notions":[
  {"titre":"Comprendre","rub":["definition","epidemiology","basicSciences","anamnesis"],"comment":"L'inversion rompt d'abord le faisceau talo-fibulaire antérieur ; peu de patients ont une fracture.",
   "points":["Moins de 15 % de fractures.","Ordre : LTFA, puis calcanéo-fibulaire."],"sources":[BAC,EXP]},
  {"titre":"Évaluer","rub":["clinicalExam","presumptionRedFlags","workupGoldStandard","workupAlternatives"],"comment":"La règle d'Ottawa décide de la radiographie ; l'examen différé juge la gravité.",
   "arbre":[("d1",None,"Torsion de cheville","On applique la règle d'Ottawa.",None,None),("d2","d1","Règle positive à la cheville","On radiographie la cheville.",None,None),("d3","d1","Base du 5e ou naviculaire douloureux","On radiographie le pied.",None,None),("d4","d1","Péroné proximal douloureux","On radiographie la jambe entière.",None,None),("d5","d1","Règle négative","On traite et l'on réexamine à 4–5 jours.",None,None)],
   "points":["Sensibilité proche de 100 %.","Fiable chez l'enfant."],"sources":[STI,BAC,ACI,DIJ]},
  {"titre":"Traiter","rub":["positiveDiagnosis","acuteManagement","hospitalizationComplications","chronicManagement"],"comment":"On traite de façon fonctionnelle, avec des exercices ; la forme sévère profite d'une courte immobilisation.",
   "tab":(["Situation","Conduite","Source"],[["Entorse sans fracture","Orthèse ou bandage adhésif et exercices",[("Vuurberg 2018","Traitement fonctionnel.")]],["Entorse sévère","Botte plâtrée 10 jours ou Aircast",[("Lamb 2009","Récupération plus rapide.")]],["Douleur","AINS prudents",[("Vuurberg 2018","Complications possibles.")]],["Instabilité malgré les exercices","Avis chirurgical",[("Vuurberg 2018","Chirurgie après échec.")]]]),
   "points":["Ibuprofène : pas si clairance < 30 ml/min."],"sources":[VUU,LAM,CMP]},
  {"titre":"Suivre","rub":["prognosisDischarge","surveillance","followUpNetwork"],"comment":"On prévient la récidive par la proprioception et l'orthèse.",
   "points":["Programme proprioceptif de 8 semaines : NNT 9."],"sources":[HUP,VUU,EXP]}],
 "ssp":("O4.1","Consultation avant une activité sportive ou après une blessure sportive",True,[
   ("n1",None,"Torsion de la cheville","On recherche une déformation, un déficit neurovasculaire et l'on applique la règle d'Ottawa.","cheville","c2"),
   ("n2","n1","Règle d'Ottawa positive","On radiographie la cheville ou le pied.","cheville","c2"),
   ("n3","n1","Péroné proximal douloureux","On radiographie la jambe entière.","cheville","c2"),
   ("n4","n1","Règle négative","On commence le traitement fonctionnel.","cheville","c3"),
   ("n5","n4","Examen à 4–5 jours","On juge la gravité et l'on adapte le support.","cheville","c3"),
   ("n6","n5","Instabilité malgré les exercices","On adresse à l'orthopédiste.","cheville","c4")]),
 "pec":[
  pec("cheville","Entorse latérale aiguë de la cheville",["On écarte une fracture sans radiographie inutile.","On restaure la stabilité et l'on prévient la récidive."],
      ["On applique la règle d'Ottawa.","On recherche une douleur du péroné proximal et un déficit neurovasculaire."],
      [("Ibuprofène","Adulte : au maximum 2400 mg par jour en plusieurs prises selon le Compendium ; dose à vérifier dans l'AIPS (Swissmedic).","Il réduit la douleur et l'œdème, avec des complications possibles.",CMP)],
      [("rééducation","On prescrit un programme d'exercices supervisé, puis proprioceptif.","Il restaure la stabilité fonctionnelle et réduit les récidives."),("geste ou chirurgie","On pose une orthèse ou un bandage adhésif, ou une botte de 10 jours si l'entorse est sévère.","Le support accélère la récupération.")],
      [("S Urgences vitales Triage 144 REGA","On trie les torsions selon la règle d'Ottawa."),("A Assurances sociales","On déclare l'accident à l'assurance-accidents.")],
      None,
      (["On applique la règle d'Ottawa.","On réexamine à 4–5 jours."],[("d'abord","médecin de famille","Il applique la règle d'Ottawa et radiographie si besoin."),("ensuite","physiothérapeute","Il conduit les exercices et la proprioception."),("puis","orthopédiste","Il évalue une instabilité persistante.")]),
      "La plupart des patients récupèrent ; les écarts entre supports s'effacent à 9 mois.",
      [("Stabilité au tiroir antérieur","4–5 jours après l'accident","Gravité évaluée"),("Récidive","Pendant l'année suivante","Absente")],"Le suivi s'arrête quand la marche et la reprise du sport se font sans instabilité.",
      ("On échauffe et l'on entraîne la proprioception chez le sportif.","On porte une orthèse après une entorse.","On adresse au chirurgien une instabilité qui persiste après les exercices.")),]}
