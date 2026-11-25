from constructeur_agent_45spec import pec
ID = "T74.3_1__O2_3-E03"
PLAN = "non_monographique"
WHO = "[OMS, aide-mémoire « Abuse of older people », 15.06.2024, who.int lu le 25.11.2026]"
YON = "[Yon Y et al., Elder abuse prevalence in community settings: a systematic review and meta-analysis, Lancet Glob Health 2017;5:e147-e156, PMID 28104184, résumé lu le 25.11.2026]"
EASI = "[Yaffe MJ et al., Development and validation of a tool to improve physician identification of elder abuse: the Elder Abuse Suspicion Index (EASI), J Elder Abuse Negl 2008;20:276-300, PMID 18928055, résumé lu le 25.11.2026]"
KIT = "[Kitzmann KM et al., Child witnesses to domestic violence: a meta-analytic review, J Consult Clin Psychol 2003;71:339-52, PMID 12699028, résumé lu le 25.11.2026]"
BEJ = "[Office des mineurs du canton de Berne, notice « Droit et obligation d'aviser » (art. 314c et 314d CC, en vigueur depuis le 1.1.2019), PDF kja.dij.be.ch lu le 25.11.2026]"
GE = "[République et canton de Genève, page « Le signalement » (protection de l'adulte, art. 443 CC), ge.ch lue le 25.11.2026]"
OFJ = "[Office fédéral de la justice, page « Aide aux victimes d'infractions », bj.admin.ch lue le 25.11.2026]"
VSV = "[Vieillesse sans violence, Centre national de compétence, dépliant suisse (0848 00 13 13), PDF lu le 25.11.2026]"
EXP = "Avis d'expert, psychiatrie de la personne âgée et pédopsychiatrie (à vérifier)"
_N = [
("def","definition","critère",2,0,WHO,"L'OMS définit la maltraitance de la personne âgée comme un acte unique ou répété, ou l'absence d'action appropriée, dans une relation de confiance, qui cause un tort ou une détresse ; la forme psychologique et émotionnelle en fait partie."),
("forms","definition","signe",2,0,EXP,"La maltraitance psychologique passe par l'humiliation, les menaces d'abandon ou de placement, l'infantilisation et l'isolement imposé (à vérifier)."),
("prev","epidemiology","chiffre",3,0,YON,"Dans la communauté, 15,7 % des personnes de 60 ans et plus subissent une maltraitance en un an ; la forme psychologique est la plus fréquente (11,6 %), devant la financière (6,8 %)."),
("inst","epidemiology","chiffre",1,0,WHO,"En institution, deux soignants sur trois déclarent avoir commis une maltraitance dans l'année."),
("risk","basicSciences","terrain particulier",1,0,WHO,"La dépendance fonctionnelle, les troubles cognitifs et la mauvaise santé mentale exposent la victime ; la maladie mentale, l'abus de substances et la dépendance de l'auteur envers la victime exposent l'auteur."),
("bpsd","basicSciences","mécanisme",2,0,EXP,"Un proche aidant épuisé peut réagir par des cris et des menaces aux troubles du comportement d'une démence (à vérifier)."),
("alone","anamnesis","décision",3,0,EXP,"On reçoit la personne seule, sans le proche, et l'on pose des questions ouvertes sur la peur, les menaces et les restrictions (à vérifier)."),
("clues","clinicalExam","signe",2,0,EXP,"La peur en présence du proche, le regard vers lui avant de répondre, le retrait, la perte de poids et un téléphone confisqué doivent éveiller le soupçon (à vérifier)."),
("conseq","presumptionRedFlags","complication",1,0,WHO,"La maltraitance de la personne âgée entraîne dépression, déclin cognitif et mortalité prématurée."),
("easi","workupGoldStandard","examen",2,0,EASI,"L'EASI pose six questions en moins de deux minutes ; sa sensibilité de 0,47 et sa spécificité de 0,75 en font un outil de soupçon, pas de diagnostic : un résultat négatif n'exclut rien."),
("doc","workupAlternatives","décision",1,0,GE,"On note des informations complètes, exactes et factuelles, avec pièces à l'appui si possible."),
("kit","positiveDiagnosis","chiffre",2,0,KIT,"L'enfant témoin de violences entre ses parents a plus de difficultés que l'enfant non exposé (d = −0,40) et autant que l'enfant battu."),
("childsign","positiveDiagnosis","diagnostic différentiel",2,0,EXP,"Une énurésie secondaire, des cauchemars, de l'agressivité ou un retrait chez l'enfant font évoquer une exposition aux violences conjugales avant un TDAH ou un trouble anxieux isolé (à vérifier)."),
("ddx","positiveDiagnosis","diagnostic différentiel",1,0,EXP,"Chez la personne âgée, on distingue la maltraitance d'une dépression, d'une démence débutante ou d'un délire de préjudice, sans écarter la possibilité qu'elles coexistent (à vérifier)."),
("will","acuteManagement","décision",2,0,EXP,"Chez la personne âgée capable de discernement, on respecte sa volonté, on lui propose de l'aide et un plan de sécurité, et l'on maintient le suivi (à vérifier)."),
("adult","acuteManagement","contexte suisse",3,1,GE,"Toute personne peut aviser l'autorité de protection de l'adulte (art. 443 CC) ; le médecin soumis au secret professionnel ne le fait qu'après la levée du secret."),
("child314c","acuteManagement","contexte suisse",3,1,BEJ,"Depuis 2019, toute personne peut aviser l'APEA quand l'intégrité physique, psychique ou sexuelle d'un enfant semble menacée (art. 314c CC) ; le médecin le peut sans levée du secret quand l'intérêt de l'enfant le justifie."),
("child314d","acuteManagement","piège",2,1,BEJ,"L'obligation d'aviser (art. 314d CC) vise les professionnels en contact régulier avec des enfants qui ont des indices concrets ; les personnes soumises au secret pénal, dont les médecins, en sont exclues."),
("caregiver","hospitalizationComplications","prévention",1,0,WHO,"Les interventions qui allègent la charge du proche aidant préviennent la maltraitance."),
("chem","hospitalizationComplications","piège",1,0,EXP,"Calmer la personne âgée agitée par un neuroleptique pour soulager l'aidant ne traite pas la situation et expose à des effets graves (à vérifier)."),
("childcare","chronicManagement","décision",1,0,EXP,"On protège l'enfant exposé, on l'oriente vers la pédopsychiatrie et l'on soutient le parent victime (à vérifier)."),
("follow","chronicManagement","décision",1,0,EXP,"On revoit la personne âgée régulièrement, seule, et l'on réévalue le risque à chaque visite (à vérifier)."),
("prono","prognosisDischarge","pronostic",1,0,WHO,"Sans intervention, la maltraitance augmente la mortalité prématurée de la personne âgée."),
("surv","surveillance","décision",1,0,EXP,"On surveille le poids, l'humeur, la cognition et l'isolement, et l'on note chaque fait daté (à vérifier)."),
("vsv","followUpNetwork","contexte suisse",1,1,VSV,"Le Centre national de compétence Vieillesse sans violence répond au 0848 00 13 13, gratuitement et confidentiellement ; l'anonymat est possible."),
("lavi","followUpNetwork","contexte suisse",1,1,OFJ,"L'aide aux victimes (LAVI) s'adresse à toute personne atteinte directement dans son intégrité physique, psychique ou sexuelle par une infraction commise en Suisse, ainsi qu'à ses proches ; la victime choisit son centre de consultation."),
("142","followUpNetwork","contexte suisse",1,1,OFJ,"Depuis le 1er mai 2026, le numéro 142 offre un conseil gratuit et confidentiel aux victimes de violence, 24 heures sur 24."),
("net","followUpNetwork","décision",1,0,EXP,"On travaille avec le service social, les soins à domicile, l'assistant social de l'hôpital et, au besoin, l'APEA (à vérifier)."),
]
K = {k: i+1 for i, (k, *_r) in enumerate(_N)}
N = [t[1:] for t in _N]
n = lambda *ks: [K[k] for k in ks]
AM = ["Recevoir la personne âgée seule.","Adulte : levée du secret avant d'aviser l'APEA.","Enfant : le médecin peut aviser sans levée du secret.","Le médecin n'a pas d'obligation d'aviser (art. 314d).","EASI négatif n'exclut rien.","Forme psychologique la plus fréquente."]
A = lambda *o: list(o)
Q = [
{"f":"A","s":("S1",1,3),"st":"Une femme de 82 ans, atteinte de troubles cognitifs légers, consulte avec son fils, qui vit chez elle. Elle a perdu 4 kg, regarde son fils avant chaque réponse et dit à voix basse : « Il dit que je finirai au home si je me plains. »",
 "p":"Quelle est votre première démarche ?","o":A((1,"La recevoir seule, sans son fils, et lui poser des questions ouvertes","Expert (à vérifier)."),(0,"Faire un test cognitif détaillé en présence du fils","Piège : la peur fausse l'entretien."),(0,"Conclure à l'absence de problème si un court questionnaire de dépistage est négatif","Faux : sensibilité de l'EASI de 0,47 (Yaffe 2008)."),(0,"Prescrire un anxiolytique","Faux."),(0,"Rédiger d'emblée un avis à l'APEA sans l'avoir entendue","Faux.")),
 "n":n("alone","clues","forms","def","easi","ddx"),"a":"application","d":4,"l":("Peur.","Emprise.","Regard vers le fils.","Menace.","La voir seule.","Test cognitif.","Seule d'abord.")},
{"f":"A","s":("S1",2,3),"st":"Seule, elle raconte que son fils l'insulte, a confisqué son téléphone et menace de la placer. Elle est capable de discernement et refuse que vous en parliez à quiconque.",
 "p":"Que faites-vous ?","o":A((1,"Respecter sa volonté, lui proposer de l'aide (Vieillesse sans violence, service social) et un plan de sécurité, et la revoir rapidement","Expert ; GE art. 443 CC : levée du secret nécessaire."),(0,"Aviser l'APEA sans attendre, puisque toute personne en a le droit","Piège : le médecin doit d'abord être délié du secret."),(0,"Appeler le fils pour le confronter","Faux."),(0,"Lui faire signer une curatelle","Faux."),(0,"Ne rien faire, puisqu'elle refuse","Faux.")),
 "n":n("will","adult","vsv","follow"),"a":"piège","d":5,"l":("Discernement.","Autonomie.","Refus.","Secret.","Aider sans trahir.","Avis immédiat.","Volonté et suivi.")},
{"f":"A","s":("S1",3,3),"st":"Trois mois plus tard, elle accepte que vous parliez à son fils. Il dit être épuisé et ne plus supporter ses oublis.",
 "p":"Quelle mesure diminue le risque ?","o":A((1,"Alléger la charge de l'aidant (aide à domicile, accueil de jour)","OMS 2024."),(0,"Lui dire de se débrouiller","Faux."),(0,"Prescrire un neuroleptique à sa mère","Piège."),(0,"Rompre le suivi","Faux."),(0,"Le menacer d'une plainte","Faux.")),
 "n":n("caregiver","chem","net","bpsd"),"a":"application","d":3,"l":("Épuisement.","Charge.","Oublis.","Aidant.","Soulager.","Sédater.","Soulager l'aidant.")},
{"f":"A","st":"Un garçon de 6 ans, propre depuis l'âge de 3 ans, mouille de nouveau son lit, fait des cauchemars et frappe ses camarades. Sa mère, qui porte un hématome au bras, dit que son compagnon « crie beaucoup » et que l'enfant se cache sous son lit pendant les disputes.",
 "p":"Quelle est votre hypothèse principale ?","o":A((1,"Une exposition aux violences dans le couple, forme de maltraitance psychologique","Kitzmann 2003."),(0,"Un TDAH","Piège : l'agressivité a un contexte."),(0,"Une énurésie primaire","Faux : secondaire."),(0,"Un trouble du spectre de l'autisme","Faux."),(0,"Une infection urinaire isolée","Faux.")),
 "n":n("childsign","kit"),"a":"piège","d":4,"l":("Énurésie secondaire.","Stress.","Cache-toi.","Disputes.","Nommer l'exposition.","TDAH.","Témoin de violence.")},
{"f":"A","st":"Après cette consultation, vous, médecin installé, jugez que le développement psychique de ce garçon est menacé ; la mère refuse toute démarche.",
 "p":"Quelle est votre situation juridique en Suisse ?","o":A((1,"Vous pouvez aviser l'APEA sans demander la levée du secret, si l'intérêt de l'enfant le justifie","Art. 314c al. 2 CC (Berne 2019)."),(0,"Vous devez d'abord être délié du secret professionnel","Piège : c'est la règle pour l'adulte."),(0,"Vous êtes obligé d'aviser l'APEA (art. 314d)","Faux : les médecins en sont exclus."),(0,"Vous ne pouvez rien faire sans l'accord de la mère","Faux."),(0,"Vous devez porter plainte pénale","Faux.")),
 "n":n("child314c","child314d","adult"),"a":"piège","d":5,"l":("Enfant.","Secret.","Mère opposée.","Art. 314c.","Aviser.","Levée du secret.","Droit, pas obligation.")},
{"f":"A","st":"Un homme de 80 ans s'occupe seul de sa femme atteinte d'une démence, qui crie la nuit et le frappe. Il avoue lui hurler dessus et la menacer de « la laisser seule ». Il demande « un calmant fort » pour elle.",
 "p":"Quelle réponse est la plus adaptée ?","o":A((1,"Reconnaître son épuisement, organiser un relais (soins à domicile, accueil de jour) et traiter d'abord les troubles du comportement sans médicament","OMS 2024 ; Expert."),(0,"Prescrire un neuroleptique à haute dose","Piège : contention chimique."),(0,"Aviser la police","Faux."),(0,"Ne rien changer","Faux."),(0,"Hospitaliser le mari","Faux.")),
 "n":n("bpsd","caregiver","chem"),"a":"piège","d":4,"l":("Démence.","Épuisement.","Cris.","Aidant.","Soulager.","Neuroleptique.","Relais pour l'aidant.")},
{"f":"A","st":"Une femme de 38 ans consulte pour une insomnie. Son compagnon contrôle son argent, l'insulte devant les enfants et menace de les lui retirer. Elle n'a aucune lésion et pense que « ce n'est pas assez grave pour une aide ».",
 "p":"Que lui proposez-vous ?","o":A((1,"Un centre de consultation LAVI, car l'aide couvre aussi l'atteinte psychique","OFJ."),(0,"Rien, faute de lésion physique","Piège : la LAVI couvre l'intégrité psychique."),(0,"Un somnifère seul","Faux."),(0,"Une thérapie de couple d'emblée","Faux."),(0,"Un avis obligatoire à l'APEA","Faux.")),
 "n":n("lavi","142","kit"),"a":"piège","d":4,"l":("Contrôle.","Emprise.","Insultes.","Atteinte psychique.","LAVI.","Pas de lésion.","Psychique aussi.")},
{"f":"A","m":0,"st":"Vous présentez les chiffres de la maltraitance des personnes âgées.",
 "p":"Quelle proportion de personnes de 60 ans et plus subissent une maltraitance en un an dans la communauté ?","o":A((1,"Environ une sur six (15,7 %)","Yon 2017."),(0,"Une sur cent","Faux."),(0,"Une sur deux","Faux."),(0,"Une sur mille","Faux."),(0,"Aucune donnée","Faux.")),
 "n":n("prev"),"a":"direct","d":1,"l":("Fréquence.","Prévalence.","60 ans.","15,7 %.","Retenir.","1 %.","Une sur six.")},
{"f":"A","m":0,"st":"Vous enseignez les formes de maltraitance de la personne âgée.",
 "p":"Quelle forme est la plus fréquente ?","o":A((1,"La maltraitance psychologique","Yon 2017 : 11,6 %."),(0,"La maltraitance physique","Faux : 2,6 %."),(0,"La maltraitance sexuelle","Faux."),(0,"La négligence","Faux : 4,2 %."),(0,"La maltraitance financière","Faux : 6,8 %.")),
 "n":n("prev","def"),"a":"direct","d":2,"l":("Formes.","Fréquence.","Psychologique.","11,6 %.","Classer.","Physique.","Psychologique en tête.")},
{"f":"A","m":0,"st":"Vous résumez la méta-analyse de Kitzmann sur les enfants témoins de violences conjugales.",
 "p":"Quelle affirmation est juste ?","o":A((1,"Leurs difficultés ne diffèrent pas significativement de celles des enfants battus","Kitzmann 2003."),(0,"Ils n'ont aucune difficulté","Faux."),(0,"Seuls les adolescents sont touchés","Faux."),(0,"L'exposition verbale seule est plus grave","Faux."),(0,"Les effets disparaissent avant 3 ans","Faux.")),
 "n":n("kit","childcare"),"a":"direct","d":3,"l":("Preuve.","Exposition.","Témoins.","Comme battus.","Lire.","Aucun effet.","Témoin = victime.")},
{"f":"A","m":0,"st":"Votre médecin assistant fait passer l'EASI à une patiente de 78 ans ; le résultat est négatif.",
 "p":"Comment l'interprétez-vous ?","o":A((1,"Il n'exclut pas une maltraitance, car la sensibilité n'est que de 0,47","Yaffe 2008."),(0,"Il exclut la maltraitance","Piège."),(0,"Il pose le diagnostic","Faux."),(0,"Il impose un avis à l'APEA","Faux."),(0,"Il remplace l'entretien","Faux.")),
 "n":n("easi","alone","prev"),"a":"piège","d":3,"l":("Dépistage.","Sensibilité.","Négatif.","0,47.","Interpréter.","Exclure.","Négatif ≠ absence.")},
{"f":"A","m":0,"st":"Vous préparez, avec l'accord de la patiente, un avis à l'autorité de protection de l'adulte pour une maltraitance psychologique.",
 "p":"Comment le rédigez-vous ?","o":A((1,"Avec des faits complets, exacts et datés, si possible avec des pièces","GE."),(0,"Avec vos impressions sans faits","Faux."),(0,"Anonymement","Faux : l'auteur doit être connu."),(0,"Oralement seulement","Faux."),(0,"Avec le diagnostic du fils","Faux.")),
 "n":n("doc","adult","surv"),"a":"application","d":3,"l":("Avis.","Preuve.","Faits.","Exactitude.","Rédiger.","Impressions.","Faits datés.")},
{"f":"A","m":0,"st":"Une personne âgée victime de maltraitance psychologique souhaite parler à un service spécialisé.",
 "p":"Quel numéro national lui donnez-vous ?","o":A((1,"Vieillesse sans violence, 0848 00 13 13","Dépliant VSV."),(0,"Le 117 uniquement","Faux."),(0,"Le 145","Faux : Tox Info."),(0,"Le 1414","Faux."),(0,"Aucun","Faux.")),
 "n":n("vsv","net"),"a":"direct","d":2,"l":("Ressource.","Écoute.","Âgée.","0848 00 13 13.","Orienter.","145.","Vieillesse sans violence.")},
{"f":"A","m":0,"st":"Une victime de violence psychologique dans son couple veut un conseil la nuit, sans se déplacer.",
 "p":"Quel service lui indiquez-vous ?","o":A((1,"Le 142, gratuit et confidentiel, 24 heures sur 24, depuis le 1er mai 2026","OFJ."),(0,"Le 144","Faux."),(0,"Le 145","Faux."),(0,"Le service des automobiles","Faux."),(0,"L'APEA de garde","Faux.")),
 "n":n("142","lavi"),"a":"direct","d":2,"l":("Conseil.","Nuit.","Violence.","142.","Orienter.","144.","142.")},
{"f":"Kprim","m":0,"st":"Vous soupçonnez une maltraitance psychologique d'une personne âgée capable de discernement.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"Toute personne peut aviser l'autorité de protection de l'adulte.","GE, art. 443 CC."),(1,"Le médecin soumis au secret doit être délié du secret avant d'aviser.","GE."),(1,"L'autorité doit connaître l'identité de l'auteur de l'avis.","GE."),(0,"L'avis doit contenir des impressions plutôt que des faits.","Faux.")),
 "n":n("adult","doc","will"),"a":"direct","d":3,"l":("Avis.","Secret.","Identité.","Faits.","Aviser.","Impressions.","Levée du secret.")},
{"f":"Kprim","m":0,"st":"Un enfant est exposé aux violences conjugales.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"Toute personne peut aviser l'APEA si l'intégrité psychique de l'enfant semble menacée.","Art. 314c CC."),(1,"Le médecin peut aviser sans levée du secret si l'intérêt de l'enfant le justifie.","Art. 314c al. 2."),(1,"Les médecins ne sont pas soumis à l'obligation d'aviser de l'art. 314d.","Berne 2019."),(0,"Il faut la certitude d'une maltraitance avant d'aviser.","Faux.")),
 "n":n("child314c","child314d","childcare"),"a":"direct","d":3,"l":("Enfant.","Protection.","Psychique.","Droit.","Aviser.","Certitude.","Droit, pas obligation.")},
{"f":"Kprim","m":0,"st":"Vous lisez la méta-analyse de Yon sur la maltraitance des personnes âgées.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"La prévalence globale est de 15,7 %.","Yon 2017."),(1,"La maltraitance psychologique atteint 11,6 %.","Yon 2017."),(1,"La maltraitance financière atteint 6,8 %.","Yon 2017."),(0,"La maltraitance physique est la plus fréquente.","Faux : 2,6 %.")),
 "n":n("prev","inst","conseq","prono"),"a":"direct","d":2,"l":("Chiffres.","Prévalence.","15,7 %.","11,6 %.","Retenir.","Physique.","Psychologique d'abord.")},
{"f":"Kprim","m":0,"st":"Vous orientez une victime de violence psychologique dans son couple.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"L'aide aux victimes couvre l'atteinte à l'intégrité psychique.","OFJ."),(1,"Les proches de la victime y ont aussi accès.","OFJ."),(1,"La victime choisit son centre de consultation.","OFJ."),(0,"L'aide n'existe que pour une infraction commise à l'étranger.","Faux.")),
 "n":n("lavi","142","risk"),"a":"application","d":3,"l":("LAVI.","Psychique.","Proches.","Choix.","Orienter.","Étranger.","Psychique couverte.")},
{"f":"MenuLong","st":"Vous voyez seule une femme de 84 ans qui vit avec sa belle-fille. Vous cherchez des éléments qui suggèrent qu'un proche exerce sur elle une emprise.",
 "p":"Choisissez les TROIS éléments les plus évocateurs.","o":A((1,"Elle se tait et regarde la porte quand on entend la belle-fille","Expert (à vérifier)."),(1,"On lui a retiré son téléphone et ses clés","Expert (à vérifier)."),(1,"Elle rapporte des menaces de placement si elle se plaint","Expert (à vérifier)."),(0,"Une presbyacousie connue","Faux."),(0,"Une cataracte opérée","Faux."),(0,"Une arthrose des genoux","Faux."),(0,"Une hypertension traitée","Faux."),(0,"Un déambulateur","Faux."),(0,"Une visite quotidienne de son petit-fils qu'elle apprécie","Faux."),(0,"Une demande d'aide pour les courses","Faux."),(0,"Une constipation ancienne","Faux."),(0,"Une vaccination à jour","Faux.")),
 "n":n("clues","forms","alone","risk"),"a":"piège","d":4,"l":("Peur.","Contrôle.","Silence.","Isolement.","Repérer.","Âge.","Peur, isolement, menace.")},
{"f":"MenuLong","m":0,"st":"Vous prenez en charge un enfant de 7 ans exposé aux violences psychologiques entre ses parents.",
 "p":"Choisissez les TROIS mesures justes.","o":A((1,"L'orienter vers une consultation de pédopsychiatrie","Expert (à vérifier)."),(1,"Soutenir le parent victime et l'orienter vers l'aide aux victimes","OFJ."),(1,"Envisager un avis à l'APEA si son intégrité psychique semble menacée","Art. 314c CC."),(0,"Lui prescrire un somnifère","Faux."),(0,"Confronter l'enfant aux deux parents ensemble","Faux."),(0,"Attendre une lésion physique","Faux."),(0,"Exiger la levée du secret avant tout avis","Faux."),(0,"Porter plainte à sa place","Faux."),(0,"Ne pas en parler à l'enfant","Faux."),(0,"Prescrire du méthylphénidate","Faux."),(0,"Interrompre la scolarité","Faux."),(0,"Clore le suivi","Faux.")),
 "n":n("childcare","lavi","child314c","childsign"),"a":"application","d":3,"l":("Enfant.","Exposition.","Pédopsychiatrie.","APEA.","Protéger.","Somnifère.","Soins, soutien, avis.")},
]
for _q in Q: _q["src"] = EXP
Q[2]["src"] = [WHO, EXP]; Q[3]["src"] = [KIT, EXP]; Q[4]["src"] = BEJ; Q[5]["src"] = [WHO, EXP]; Q[6]["src"] = OFJ
Q[7]["src"] = YON; Q[8]["src"] = YON; Q[9]["src"] = KIT; Q[10]["src"] = EASI; Q[11]["src"] = GE; Q[12]["src"] = VSV; Q[13]["src"] = OFJ
Q[14]["src"] = GE; Q[15]["src"] = BEJ; Q[16]["src"] = YON; Q[17]["src"] = OFJ; Q[1]["src"] = [GE, VSV, EXP]; Q[0]["src"] = [EXP, EASI]; Q[19]["src"] = [BEJ, OFJ, EXP]
C = {"theme":"Maltraitance psychologique de la personne âgée et de l'enfant exposé aux violences conjugales : forme la plus fréquente (11,6 %), entretien seul, signes de peur et d'isolement, EASI comme outil de soupçon, soutien de l'aidant, avis à l'APEA (adulte : levée du secret ; enfant : droit sans levée, art. 314c CC), LAVI, 142 et Vieillesse sans violence",
 "notions":[
  {"titre":"Comprendre","rub":["definition","epidemiology","basicSciences","anamnesis"],"comment":"La maltraitance psychologique est la plus fréquente ; on la révèle par un entretien seul.",
   "points":["Une personne âgée sur six.","Aidant épuisé."],"sources":[WHO,YON,EXP]},
  {"titre":"Repérer","rub":["clinicalExam","presumptionRedFlags","workupGoldStandard","workupAlternatives"],"comment":"On cherche la peur, l'isolement et les menaces, et l'on documente des faits.",
   "arbre":[("d1",None,"Personne âgée craintive ou enfant perturbé","On reçoit la victime seule.",None,None),("d2","d1","Adulte capable de discernement","On respecte sa volonté et l'on propose de l'aide.",None,None),("d3","d1","Adulte incapable ou en danger, secret levé","On avise l'APEA.",None,None),("d4","d1","Enfant dont l'intégrité psychique semble menacée","On peut aviser l'APEA sans levée du secret.",None,None)],
   "points":["EASI négatif n'exclut rien."],"sources":[EASI,GE,WHO]},
  {"titre":"Agir","rub":["positiveDiagnosis","acuteManagement","hospitalizationComplications","chronicManagement"],"comment":"On protège sans trahir le secret de façon illégale et l'on soulage l'aidant.",
   "tab":(["Victime","Avis à l'APEA","Source"],[["Adulte","Droit de toute personne ; médecin délié du secret",[("GE","Art. 443 CC.")]],["Enfant","Droit du médecin sans levée du secret",[("Berne 2019","Art. 314c al. 2 CC.")]],["Enfant","Obligation pour les professionnels non soumis au secret",[("Berne 2019","Art. 314d CC.")]]]),
   "points":["Pas de contention chimique pour soulager l'aidant."],"sources":[GE,BEJ,KIT,EXP]},
  {"titre":"Suivre","rub":["prognosisDischarge","surveillance","followUpNetwork"],"comment":"On revoit la victime seule et l'on active le réseau.",
   "points":["Vieillesse sans violence 0848 00 13 13.","142 depuis le 1er mai 2026."],"sources":[WHO,VSV,OFJ]}],
 "ssp":("O3.1","Maltraitance et négligence envers la personne âgée",True,[
   ("n1",None,"Personne âgée craintive devant un proche","On la reçoit seule et l'on recherche menaces et isolement.","proteger","c2"),
   ("n2","n1","Capable de discernement, refuse l'avis","On respecte sa volonté, on propose de l'aide et l'on revoit vite.","proteger","c3"),
   ("n3","n1","Incapable de discernement ou danger grave","On demande la levée du secret et l'on avise l'APEA.","proteger","c3"),
   ("n4","n1","Proche aidant épuisé","On allège sa charge.","proteger","c3"),
   ("n5",None,"Enfant exposé aux violences conjugales","On peut aviser l'APEA sans levée du secret.","proteger","c3"),
   ("n6","n2","Suivi","On réévalue le risque à chaque visite.","proteger","c4")]),
 "pec":[
  pec("proteger","Maltraitance psychologique ou verbale",["On protège la victime en respectant son autonomie.","On active le réseau et l'APEA dans le cadre légal."],
      ["On reçoit la victime seule.","On note des faits datés et exacts."],
      [],
      [("psychothérapie","On soutient la victime et l'on oriente l'enfant vers la pédopsychiatrie.","On réduit les séquelles psychiques."),("social et assurances","On organise l'aide à domicile, l'accueil de jour et l'aide aux victimes.","On allège la charge de l'aidant et l'on protège la victime."),("soins infirmiers","Les soins à domicile observent la situation à chaque passage.","On repère tôt une aggravation.")],
      [("C Communication clinique","On mène un entretien seul, ouvert et sans jugement."),("N Médecine sociale Prévention OFSP","On prévient la maltraitance en soutenant les proches aidants.")],
      None,
      (["On évalue le danger.","On respecte la volonté de la personne capable.","On active le réseau."],[("d'abord","médecin de famille","Il reçoit la victime seule et documente les faits."),("ensuite","assistant social","Il organise l'aide à domicile ou l'aide aux victimes."),("puis","APEA","Elle examine la situation après un avis légal.")]),
      "Sans intervention, la maltraitance entraîne dépression, déclin cognitif et mortalité prématurée ; le soutien de l'aidant et le suivi améliorent la situation.",
      [("Humeur, poids, isolement","À chaque visite","Stables ou améliorés"),("Charge de l'aidant","Tous les 3 mois","Relais en place")],"Le suivi se poursuit tant que le risque persiste.",
      ("On soutient les proches aidants.","On reçoit la personne seule et l'on repère les signes.","On protège la victime et l'on évite la récidive.")),]}
