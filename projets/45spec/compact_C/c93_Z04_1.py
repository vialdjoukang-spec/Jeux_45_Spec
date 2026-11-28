from constructeur_agent_45spec import pec
ID = "Z04.1__O7_17-E06"
PLAN = "non_monographique"
HUG23 = "[HUG, Service de médecine de premier recours, stratégie « Violences, tortures et guerres » (Escard, Abriel et Whitaker, 2023), annexes 1 et 2 « Guide du constat médical » et « Exemple de constat médical », lu le 28.11.2026]"
FRA = "[Fracasso T (CURML), « Le constat de coups et blessures », atelier de médecine de premier recours des HUG (29.01.2020), lu le 28.11.2026]"
HAS = "[Haute Autorité de santé, Certificat médical initial concernant une personne victime de violences, fiche de synthèse (octobre 2011), lu le 28.11.2026]"
UMV = "[Commission cantonale vaudoise de lutte contre la violence domestique et CURML, fiche « L'Unité de médecine des violences » (2018), lu le 28.11.2026]"
CMLV = "[HUG, page « Consultation médico-légale pour adultes victimes de violence (CMLV) », mise à jour du 15.07.2026, lu le 28.11.2026]"
ACEP = "[Rozzi HV, « Laceration or Incised Wound: Know the Difference », ACEP Now, août 2014, lu le 28.11.2026]"
MAG = "[Maguire S et al., Can you age bruises accurately in children? A systematic review, Arch Dis Child 2005, PMID 15665179, résumé lu le 28.11.2026]"
LPGA = "[Loi fédérale sur la partie générale du droit des assurances sociales (LPGA, RS 830.1), état au 1.1.2024, art. 4 et 28, fedlex, lu le 28.11.2026]"
LAA = "[Loi fédérale sur l'assurance-accidents (LAA, RS 832.20), état au 1.1.2026, art. 37, 45, 46 et 54a, fedlex, lu le 28.11.2026]"
OLAA = "[Ordonnance sur l'assurance-accidents (OLAA, RS 832.202), état au 1.1.2026, art. 49 et 53, fedlex, lu le 28.11.2026]"
SUVA = "[Suva Medical, Guckau J, « Transmission de rapports par des médecins traitants dans l'assurance-accidents » (30.09.2021), lu le 28.11.2026]"
CP = "[Code pénal suisse (RS 311.0), état au 1.11.2026, art. 17, 31, 123, 318 et 321, fedlex, lu le 28.11.2026]"
CPP = "[Code de procédure pénale suisse (RS 312.0), état au 1.4.2025, art. 171 et 195, fedlex, lu le 28.11.2026]"
CC = "[Code civil suisse (RS 210), état au 1.7.2026, art. 314c et 443, fedlex, lu le 28.11.2026]"
LSGE = "[Loi genevoise sur la santé (LS, K 1 03), modifications au 31.10.2026, art. 12, 55 et 86, silgeneve.ch, lu le 28.11.2026]"
LAVI = "[Loi fédérale sur l'aide aux victimes d'infractions (LAVI, RS 312.5), état au 1.1.2025, art. 1, 3, 4, 5, 14, 15 et 25, fedlex, lu le 28.11.2026]"
PV = "[OFSP et CFV, Plan de vaccination suisse 2026, prophylaxie antitétanique en cas de plaies et tableau 10, lu le 28.11.2026]"
BOO = "[Compendium.ch, résumé (Brevier) de Boostrix (dTpa), indication, dosage et contre-indications, lu le 28.11.2026 ; AIPS complète à vérifier]"
EXP = "Avis d'expert (à vérifier)"
_N = [
("def","definition","critère",3,0,HUG23+" ; "+FRA,"Le constat de coups et blessures est un « état des lieux » descriptif, non interprétatif, des atteintes physiques et psychiques, établi à la demande du patient ; l'interprétation (mécanisme, compatibilité, auteur) relève de l'expertise, demandée par un magistrat et précédée d'une levée du secret."),
("refus","definition","décision",1,0,HUG23+" ; "+HAS+" ; "+FRA,"C'est un acte médical qui ne peut pas être refusé au patient, même s'il ne veut pas porter plainte ; il se rédige de façon neutre, sans céder à la pression du patient, des proches, de la police ou des avocats."),
("epi","epidemiology","chiffre",1,1,UMV,"En 2017, l'Unité de médecine des violences du CURML a fait 1018 consultations, presque autant pour des hommes (49,7 %) que pour des femmes, avec un âge médian de 32 ans ; la violence communautaire (rue, travail) représente environ deux tiers des consultations, surtout chez des hommes (73 %), et la violence de couple ou familiale environ un tiers, surtout chez des femmes."),
("preuve","basicSciences","mécanisme",2,0,FRA+" ; "+HAS,"Les lésions évoluent et s'effacent : aucun délai légal n'empêche l'examen, mais on l'idéalise dans les 24 à 48 heures ; examiné à distance, on ne mentionne que ce que l'on observe à la date de l'examen et les allégations du patient."),
("ecchy","basicSciences","piège",1,0,HUG23+" ; "+MAG,"On note la couleur de chaque ecchymose (rouge vif, bleu-vert, jaunâtre) pour permettre une interprétation ultérieure, mais on ne la date pas soi-même : toute couleur peut se voir sur une ecchymose récente ou ancienne, et la datation clinique à 24 heures près est juste dans moins de 40 % des cas (revue chez l'enfant)."),
("dires","anamnesis","critère",3,0,HUG23+" ; "+FRA+" ; "+HAS,"On rapporte les faits sur le mode déclaratif, entre guillemets (« selon les dires de… », « le patient nous raconte que… »), en précisant qui (et le lien), où, quand et comment, avec le verbatim plutôt qu'une reformulation, et sans mot à connotation judiciaire."),
("plaintes","anamnesis","symptôme",1,0,HUG23+" ; "+FRA,"On énumère toutes les plaintes physiques et psychiques depuis les faits, au moment des faits et de la consultation, y compris les symptômes de stress post-traumatique (sommeil, anxiété, irritabilité), car des suites tardives peuvent fonder des demandes ultérieures aux assurances."),
("descr","clinicalExam","critère",3,0,HUG23+" ; "+HAS,"Chaque lésion se décrit par son type (ecchymose, abrasion, plaie contuse…), sa localisation anatomique précise, sa forme, son orientation, sa taille en centimètres, son aspect, sa couleur et ses abords, sans terme interprétatif (« brûlure de cigarette », « marque de coup de bâton »)."),
("corps","clinicalExam","examen",1,0,HUG23+" ; "+FRA,"On examine tout le corps, y compris le cou, les mains, la bouche, les gencives, les dents, le nez, les tympans et les organes génitaux, et l'on note l'identité, la date, l'heure, le lieu de l'examen et les personnes présentes (interprète compris)."),
("drap","presumptionRedFlags","signe",2,0,FRA+" ; "+HUG23,"Une tentative de strangulation, des menaces de mort et des épisodes antérieurs de violence se recherchent et se consignent ; on évalue les risques immédiats (récidive, homicide, suicide, danger pour les enfants) et l'on n'organise pas d'entretien de couple sans évaluation précise des risques."),
("psy","presumptionRedFlags","piège",1,0,HUG23,"On décrit l'état émotionnel (pleurs, anxiété) sans termes connotés (« gentille dame », « patient revendicateur ») ni flous (« collaborant ») ; en cas de risque suicidaire ou de décompensation, on demande l'avis d'un psychiatre."),
("enfant","presumptionRedFlags","contexte suisse",1,1,CC+" ; "+HUG23,"Pour un enfant dont l'intégrité semble menacée, le médecin peut aviser l'autorité de protection de l'enfant sans levée du secret quand son intérêt le justifie (art. 314c al. 2 CC) ; pour un adulte, l'avis à l'autorité de protection de l'adulte réserve le secret professionnel (art. 443 CC)."),
("photo","workupGoldStandard","examen",3,0,FRA+" ; "+HAS,"Les photographies, prises avec l'accord du patient, sont essentielles : un champ large puis un détail, l'appareil perpendiculaire à la lésion, une échelle métrique tenue au même plan, un fond uni, un contrôle à l'écran, en deux exemplaires (patient et dossier), avec un schéma corporel."),
("umv","workupAlternatives","contexte suisse",2,1,UMV+" ; "+CMLV,"L'Unité de médecine des violences du CURML (Vaud) et la consultation médico-légale des HUG (CMLV, rattachée au CURML) offrent aux adultes un examen avec photographies, gratuit et confidentiel, par des infirmières formées supervisées par des légistes, sans suivi au long cours ; à Genève, l'UIMPV assure évaluations, conseils et suivis, et les violences sexuelles vont aux urgences."),
("exams","workupAlternatives","examen",1,0,HUG23+" ; "+HAS,"On mentionne les examens complémentaires faits (radiographie, scanner, analyses) avec leurs résultats commentés et l'avis des spécialistes ; si un résultat arrive plus tard, on établit un document complémentaire."),
("vocab","positiveDiagnosis","critère",2,0,ACEP+" ; "+HUG23,"Une plaie contuse (déchirure par une force contondante) a des bords irréguliers, abrasés ou contus et des ponts tissulaires ; une plaie par instrument tranchant a des bords nets, sans pont, et est plus longue que profonde ; une plaie piquante est plus profonde que longue."),
("negatifs","positiveDiagnosis","signe",1,0,HAS+" ; "+HUG23,"On mentionne les signes négatifs utiles (zone douloureuse sans lésion visible), l'association de lésions d'aspects différents et la phrase « nous ne mettons pas en évidence d'autre lésion au moment de l'examen »."),
("diag","positiveDiagnosis","piège",2,0,FRA+" ; "+HAS,"On ne conclut ni sur la réalité des faits, ni sur l'auteur, ni sur le caractère volontaire : « contusion post-agression » ou « traces de strangulation » sont des interprétations qui relèvent de l'expertise, pas du constat."),
("soins","acuteManagement","décision",1,1,PV+" ; "+BOO,"On soigne d'abord ; devant une plaie profonde ou souillée chez un adulte de 26 à 64 ans complètement vacciné, on fait un rappel antitétanique (dTpa, par exemple Boostrix, 1 dose i.m.) si la dernière dose remonte à 10 ans ou plus (20 ans pour une plaie superficielle propre), sans immunoglobulines (posologies à vérifier dans l'AIPS (Swissmedic))."),
("secret","acuteManagement","décision",2,1,CP+" ; "+LSGE+" ; "+HUG23+" ; "+CPP,"Le document appartient au patient : on ne le transmet à la police ou au ministère public qu'avec son consentement ou une levée écrite (art. 321 ch. 2 CP ; à Genève, commission du secret professionnel, art. 12 et 86 LS) ; la poursuite d'office ne délie pas le médecin, qui peut refuser de témoigner sauf s'il est délié (art. 171 CPP)."),
("laa54a","acuteManagement","contexte suisse",2,1,LAA+" ; "+SUVA+" ; "+LPGA,"À l'assureur-accidents, le médecin transmet sans consentement supplémentaire les indications nécessaires pour statuer sur les prestations (art. 54a LAA), en se limitant aux données juridiquement pertinentes ; les autres parties du dossier exigent l'accord du patient."),
("decl","chronicManagement","contexte suisse",2,1,LAA+" ; "+OLAA,"Le salarié avise sans retard son employeur ou l'assureur de tout accident qui nécessite un traitement ou entraîne une incapacité de travail, l'employeur avise l'assureur, et le médecin remplit honnêtement et entièrement les formulaires ; un retard inexcusable de plus de 3 mois permet de réduire les prestations de moitié."),
("rixe","chronicManagement","piège",1,1,OLAA+" ; "+LPGA,"Lors d'un accident non professionnel survenu pendant une rixe ou une bagarre, les prestations en espèces sont réduites au moins de moitié, sauf si l'assuré n'y prenait aucune part ou venait en aide à une personne sans défense : on consigne les dires sans trancher la participation."),
("faux","hospitalizationComplications","complication",1,1,CP+" ; "+FRA,"Le document engage la responsabilité civile et pénale de son auteur : un certificat intentionnellement contraire à la vérité, destiné à une autorité ou à procurer un avantage illicite, est puni d'une peine privative de liberté de 3 ans au plus ou d'une peine pécuniaire (art. 318 CP)."),
("remise","surveillance","décision",1,1,FRA+" ; "+HUG23+" ; "+LSGE,"On remet le document en mains propres (ou à une adresse sûre) et l'on garde une copie au dossier ; à Genève, le patient peut consulter son dossier et s'en faire remettre les pièces, en principe gratuitement (art. 55 LS)."),
("prono","prognosisDischarge","pronostic",1,0,FRA+" ; "+CMLV,"Un document neutre et rigoureux aide la victime à faire valoir ses droits et contribue à sa reconnaissance ; par lui, le médecin signifie aussi sa volonté de rompre le silence."),
("lavi","followUpNetwork","contexte suisse",2,1,LAVI,"La LAVI aide toute victime d'une infraction contre son intégrité, que l'auteur soit identifié ou non, gratuitement pour les conseils et l'aide immédiate, dans le centre de son choix et quelle que soit la date de l'infraction ; ses prestations restent subsidiaires (auteur, assurances), et l'indemnisation se demande dans les 5 ans."),
("plainte","followUpNetwork","contexte suisse",1,1,CP+" ; "+CPP,"Les lésions corporelles simples se poursuivent sur plainte (3 mois dès que l'ayant droit connaît l'auteur), sauf cas qualifiés poursuivis d'office (arme ou objet dangereux, conjoint) ; les autorités pénales requièrent les certificats médicaux utiles à la procédure (art. 195 CPP)."),
]
K = {k: i+1 for i, (k, *_r) in enumerate(_N)}
N = [t[1:] for t in _N]
n = lambda *ks: [K[k] for k in ks]
AM = ["Constat = descriptif ; interprétation = expertise (magistrat).","Dires entre guillemets : qui, où, quand, comment ; pas d'auteur affirmé.","Pas de « brûlure de cigarette » ni de « traces de strangulation » : décrire.","Plaie contuse = ponts tissulaires ; tranchante = bords nets, sans pont ; ecchymose jamais datée par sa couleur.","Police : rien sans consentement ou levée écrite ; poursuite d'office ≠ levée.","Assureur LAA : indications nécessaires sans consentement supplémentaire (art. 54a LAA).","Rixe : prestations en espèces réduites au moins de moitié (art. 49 OLAA).","Pas de délai légal ; idéal 24–48 heures ; à distance, seulement ce que l'on voit."]
A = lambda *o: list(o)
Q = [
{"f":"A","s":("S1",1,4),"st":"Un étudiant de 23 ans consulte à 9 heures, le lendemain d'une altercation à la sortie d'un bar genevois ; il hésite à porter plainte. À la queue du sourcil gauche, vous voyez une plaie de 2 cm, horizontale, à bords irréguliers et ecchymotiques, avec au fond de fins filaments tendus d'une berge à l'autre.",
 "p":"Comment décrivez-vous cette plaie dans votre note ?","o":A(
  (1,"Plaie contuse de 2 cm, horizontale, à bords irréguliers et ecchymotiques, avec ponts tissulaires, à la queue du sourcil gauche","Juste : type, taille, orientation, bords et siège, sans interprétation (ACEP 2014 ; HUG 2023)."),
  (0,"Plaie par instrument tranchant de 2 cm à la queue du sourcil gauche","Faux : une plaie tranchante a des bords nets, sans pont tissulaire."),
  (0,"Coupure par tesson de bouteille à l'arcade gauche","Faux : désigner l'objet est une interprétation, et la plaie décrite n'est pas une coupure."),
  (0,"Plaie due au coup de poing de son agresseur","Faux : on ne nomme ni l'auteur ni le mécanisme supposé ; c'est une interprétation."),
  (0,"Plaie piquante de l'arcade sourcilière gauche","Faux : une plaie piquante est plus profonde que longue, sans ponts tissulaires.")),
 "n":n("vocab","descr"),"a":"application","d":4,"l":("Plaie du visage après altercation.","Force contondante sur une saillie osseuse.","Bords irréguliers, filaments entre les berges.","Ponts tissulaires = plaie contuse.","Décrire sans interpréter.","Écrire « coupure » ou nommer l'objet.","Ponts tissulaires : contondant.")},
{"f":"A","s":("S1",2,4),"st":"Il vous dit : « Le videur m'a frappé au visage avec sa lampe de poche, puis je suis tombé sur le trottoir. »",
 "p":"Comment consignez-vous ce récit ?","o":A(
  (1,"Entre guillemets, sur le mode déclaratif (« le patient nous dit que… »), en gardant qui, où, quand et comment, sans reformuler ni trancher","Juste : les dires se rapportent fidèlement, identité de la personne désignée comprise, sans les faire siens (Fracasso 2020 ; HAS 2011)."),
  (0,"« Le patient a été frappé au visage par le videur avec une lampe de poche. »","Faux : la phrase affirme les faits comme constatés par le médecin."),
  (0,"« Lésion compatible avec un coup de lampe de poche porté par le videur. »","Faux : la compatibilité et l'auteur relèvent de l'interprétation, donc de l'expertise."),
  (0,"Vous omettez la mention du videur pour ne désigner personne","Faux : les dires spontanés, y compris la personne désignée, se notent sur le mode déclaratif."),
  (0,"« Agression par un tiers à la sortie d'un bar. »","Faux : terme à connotation judiciaire et résumé qui perd le verbatim.")),
 "n":n("dires","diag"),"a":"piège","d":4,"l":("Récit d'un tiers désigné.","Le médecin n'a pas vu les faits.","Paroles du patient.","Guillemets, qui-où-quand-comment.","Rapporter sans affirmer.","Écrire les faits comme certains.","Il dit, entre guillemets.")},
{"f":"A","s":("S1",3,4),"st":"Il accepte que vous photographiiez ses lésions du visage et de l'avant-bras.",
 "p":"Comment procédez-vous ?","o":A(
  (1,"Une vue d'ensemble puis un détail de chaque lésion, appareil perpendiculaire, échelle métrique tenue au même plan que la lésion, fond uni et contrôle à l'écran, en deux exemplaires (patient et dossier)","Juste : règles de prise de vue du CURML (Fracasso 2020)."),
  (0,"Une seule photo rapprochée, sans repère de taille","Faux : il faut un champ large pour situer la lésion et une échelle pour la mesurer."),
  (0,"Des photos de biais pour mieux montrer le relief","Faux : l'appareil se place perpendiculairement pour respecter les proportions."),
  (0,"Une règle posée sur la table à côté du bras","Faux : l'échelle doit être au même plan que la lésion, sinon elle fausse la taille."),
  (0,"Des photos sur votre téléphone privé, sans copie au dossier","Faux : un exemplaire va au dossier et un au patient.")),
 "n":n("photo","remise"),"a":"application","d":4,"l":("Accord du patient.","Image = preuve durable.","Lésions visibles.","Ensemble, détail, échelle au même plan.","Photographier selon des règles.","Photo de biais sans repère.","Large, détail, échelle, perpendiculaire.")},
{"f":"A","s":("S1",4,4),"st":"Le lendemain, un policier vous téléphone : il veut la description de ses blessures et vos photographies, car « l'objet utilisé rend l'infraction poursuivable d'office ». Le patient ne vous a rien autorisé.",
 "p":"Que répondez-vous ?","o":A(
  (1,"Vous ne communiquez rien sans son consentement ou une levée écrite par la commission du secret professionnel ; le document lui appartient et c'est à lui de le remettre s'il le souhaite","Juste : art. 321 CP, art. 12 et 86 LS (Genève) ; la poursuite d'office ne délie pas le médecin (HUG 2023)."),
  (0,"Vous transmettez tout, puisque l'infraction se poursuit d'office","Faux : la poursuite d'office n'autorise pas le médecin à informer la police."),
  (0,"Vous donnez l'essentiel par téléphone, sans les photographies","Faux : une révélation partielle reste une violation du secret."),
  (0,"Vous refusez définitivement, même si une autorité vous délie un jour","Faux : délié par écrit, le médecin doit témoigner (art. 171 al. 2 CPP)."),
  (0,"Vous envoyez le document à l'assureur-accidents, qui le fera suivre à la police","Faux : l'art. 54a LAA vise les prestations d'assurance, pas l'enquête pénale.")),
 "n":n("secret","remise"),"a":"piège","d":5,"l":("Demande policière sans accord.","Secret professionnel.","Poursuite d'office invoquée.","Consentement ou levée écrite.","Refuser poliment, orienter.","Croire que l'office délie.","Office ≠ levée du secret.")},
{"f":"A","st":"Une femme de 26 ans consulte six jours après avoir été, dit-elle, poussée contre une table. Vous voyez au flanc droit une plage jaune-verdâtre de 6 × 4 cm et, au bras gauche, deux taches bleu-violacé ovalaires de 2 cm. Elle vous demande d'écrire que toutes ces marques datent du même soir.",
 "p":"Que faites-vous ?","o":A(
  (1,"Vous décrivez chaque lésion avec sa couleur, vous rapportez entre guillemets la date qu'elle indique et vous mentionnez des lésions d'aspects différents, sans les dater vous-même","Juste : la couleur ne date pas une ecchymose de façon fiable (Maguire 2005) ; on décrit, on rapporte (HAS 2011 ; HUG 2023)."),
  (0,"Vous écrivez que la plage jaune a plus de 48 heures et les taches violettes moins de 24 heures","Faux : toute couleur peut se voir à tout âge ; la datation clinique est peu fiable."),
  (0,"Vous écrivez qu'elles datent toutes du même soir, comme elle le demande","Faux : ce serait affirmer un fait non observé, voire un certificat contraire à la vérité (art. 318 CP)."),
  (0,"Vous ne décrivez que les taches bleu-violacé, plus récentes","Faux : on décrit toutes les lésions, et rien ne prouve laquelle est la plus récente."),
  (0,"Vous renoncez, car le délai de 48 heures est dépassé","Faux : aucun délai légal ; on décrit ce que l'on voit le jour de l'examen.")),
 "n":n("ecchy","descr","negatifs","preuve"),"a":"piège","d":5,"l":("Ecchymoses de couleurs différentes.","Résorption variable de l'hémoglobine.","Jaune et violet.","Pas de datation par la couleur.","Décrire, rapporter.","Dater pour faire plaisir.","Couleur décrite, jamais datée.")},
{"f":"A","st":"Un serveur de 29 ans, salarié à plein temps, consulte lundi pour une plaie du cuir chevelu et des douleurs costales après « une bagarre » devant une discothèque samedi soir, à laquelle il dit avoir pris part. Il craint pour son salaire.",
 "p":"Quelle affirmation est exacte ?","o":A(
  (1,"L'assureur-accidents réduit d'au moins moitié les prestations en espèces s'il a pris part à la bagarre ; vous consignez ses dires sans trancher sa participation, et il doit aviser sans retard son employeur","Juste : art. 49 al. 2 OLAA, art. 45 LAA ; le médecin rapporte, il ne juge pas."),
  (0,"Des lésions reçues dans une bagarre ne relèvent jamais de l'assurance-accidents","Faux : l'OLAA prévoit une réduction des prestations en espèces, pas une exclusion de l'accident."),
  (0,"L'aide aux victimes paie d'emblée son salaire à la place de l'assureur-accidents","Faux : les prestations LAVI sont subsidiaires (art. 4 LAVI)."),
  (0,"Vous écrivez qui a commencé la bagarre pour aider l'assureur","Faux : on ne se prononce pas sur les faits ni sur les responsabilités."),
  (0,"Il a trois mois pour aviser son employeur sans aucune conséquence","Faux : l'avis se fait sans retard ; un retard inexcusable peut réduire les prestations (art. 46 LAA).")),
 "n":n("rixe","decl","lavi","diag"),"a":"piège","d":5,"l":("Blessé dans une bagarre.","Accident non professionnel.","Participation déclarée.","Réduction des prestations en espèces.","Rapporter, aviser sans retard.","Croire à une exclusion totale.","Rixe : espèces réduites de moitié au moins.")},
{"f":"A","st":"Une menuisière de 38 ans s'est entaillé la main avec un ciseau à bois à l'atelier ; vous l'avez soignée. Trois semaines plus tard, l'assureur-accidents vous demande les informations médicales nécessaires pour statuer sur ses prestations ; elle n'a signé aucune autorisation.",
 "p":"Que faites-vous ?","o":A(
  (1,"Vous transmettez à l'assureur les indications médicales nécessaires, sans consentement supplémentaire, en vous limitant à ce qui est pertinent pour ses prestations","Juste : art. 54a LAA ; Suva 2021 : autorisés et tenus, dans le respect de la proportionnalité."),
  (0,"Vous exigez d'abord une levée du secret par l'autorité cantonale","Faux : l'art. 54a LAA fonde la transmission à l'assureur."),
  (0,"Vous refusez tant qu'elle n'a pas signé un consentement écrit","Faux : le médecin est tenu de renseigner l'assureur-accidents sur les données pertinentes."),
  (0,"Vous envoyez tout le dossier, y compris des antécédents psychiatriques sans lien","Faux : seules les données juridiquement pertinentes se transmettent sans accord."),
  (0,"Vous adressez aussi le diagnostic à son employeur","Faux : l'employeur n'a pas droit au diagnostic ; le secret s'applique.")),
 "n":n("laa54a","secret"),"a":"application","d":4,"l":("Demande de l'assureur-accidents.","Base légale de transmission.","Pas d'autorisation signée.","Art. 54a LAA, proportionnalité.","Transmettre le nécessaire.","Exiger une levée inutile.","LAA : nécessaire, sans plus.")},
{"f":"A","st":"Une caissière de 41 ans consulte pour une douleur du bras ; sous la manche, vous voyez des ecchymoses en bandes parallèles. Elle dit que son compagnon « a promis de me tuer si je parlais à quelqu'un » et qu'il possède une arme ; leur fille de 6 ans vit avec eux.",
 "p":"Quelle est votre priorité ?","o":A(
  (1,"Évaluer avec elle les risques immédiats pour elle et sa fille, organiser sa protection et l'orienter vers une consultation spécialisée (Unité de médecine des violences ou consultation des HUG pour adultes victimes de violence) et le réseau","Juste : menaces de mort et arme sont des signaux de danger (Fracasso 2020 ; HUG 2023)."),
  (0,"Proposer un entretien de couple avec le compagnon pour apaiser la situation","Faux : contre-indiqué sans évaluation précise des risques (HUG 2023)."),
  (0,"Exiger qu'elle porte plainte avant toute aide","Faux : l'aide ne dépend pas d'une plainte, et la décision lui appartient."),
  (0,"Prescrire un antalgique et la revoir dans un mois","Faux : le danger immédiat n'est pas évalué."),
  (0,"Téléphoner au compagnon pour l'avertir","Faux : cela met la patiente en danger et viole le secret.")),
 "n":n("drap","umv","enfant"),"a":"application","d":4,"l":("Menaces de mort, arme, enfant.","Risque d'escalade.","Ecchymoses en bandes.","Risques immédiats.","Protéger, orienter.","Entretien de couple.","Menace + arme = danger.")},
{"f":"A","st":"Un maçon de 50 ans consulte cinq jours après avoir été, dit-il, frappé par un voisin. Les marques pâlissent et il pense qu'il est trop tard pour que vous notiez quoi que ce soit ; il a encore mal à une côte.",
 "p":"Que lui répondez-vous ?","o":A(
  (1,"Vous l'examinez aujourd'hui, notez entre guillemets ses dires et toutes ses plaintes depuis les faits, décrivez ce que vous observez à la date de l'examen et mentionnez les examens faits avec leurs résultats","Juste : pas de délai légal, idéal 24–48 heures ; à distance, seulement l'observé du jour et les allégations (Fracasso 2020 ; HAS 2011 ; HUG 2023)."),
  (0,"Vous refusez, car au-delà de 48 heures rien n'est utilisable","Faux : la demande ne peut pas être refusée ; seul le contenu se limite à l'observé."),
  (0,"Vous décrivez les lésions telles qu'il dit les avoir eues le jour des faits","Faux : on ne décrit que ce que l'on observe soi-même."),
  (0,"Vous l'envoyez à la police, seule compétente","Faux : le médecin documente lui-même ce qu'il observe."),
  (0,"Vous attendez qu'il ait déposé plainte","Faux : l'examen ne dépend pas d'une plainte.")),
 "n":n("preuve","dires","refus","plaintes","exams"),"a":"application","d":4,"l":("Consultation tardive.","Lésions qui s'effacent.","Douleur persistante.","Observé du jour + dires.","Examiner quand même.","Refuser pour délai.","Tard, mais jamais trop tard.")},
{"f":"A","m":0,"st":"Une étudiante en médecine vous demande ce qui distingue le constat de coups et blessures d'une expertise médico-légale.",
 "p":"Que lui répondez-vous ?","o":A(
  (1,"Le constat décrit, à la demande du patient, ce que le médecin observe ; l'interprétation (mécanisme, compatibilité, auteur) relève de l'expertise ordonnée par un magistrat","Juste : constat descriptif, rapport d'expertise interprétatif (Fracasso 2020 ; HUG 2023)."),
  (0,"Le constat doit conclure sur l'auteur des lésions","Faux : on ne se prononce jamais sur l'auteur."),
  (0,"Seul un médecin légiste peut établir un constat","Faux : tout médecin consulté peut et doit l'établir."),
  (0,"L'expertise se fait à la demande du patient, sans levée du secret","Faux : l'expertise répond à un magistrat."),
  (0,"Le constat se limite aux lésions physiques","Faux : il décrit aussi l'état psychique et les plaintes.")),
 "n":n("def","diag"),"a":"direct","d":1,"l":("Définition.","Décrire ou interpréter.","Deux documents.","Patient ou magistrat.","Distinguer.","Interpréter dans le constat.","Constat décrit, expertise interprète.")},
{"f":"A","m":0,"st":"Une avocate lausannoise vous demande vers quelle structure adresser une cliente adulte frappée pour obtenir une documentation médico-légale.",
 "p":"Que retenez-vous de l'Unité de médecine des violences ?","o":A(
  (1,"Unité du CURML qui accueille toute personne adulte victime de violence, hommes compris, gratuitement et confidentiellement, avec un rendez-vous en principe dans les 24 à 48 heures","Juste : fiche UMV 2018 (49,7 % d'hommes, consultations gratuites financées par l'État de Vaud)."),
  (0,"Elle est réservée aux femmes victimes de violence conjugale","Faux : la violence communautaire forme environ deux tiers des consultations, surtout chez des hommes."),
  (0,"La consultation est payante pour la victime","Faux : elle est financée par l'État de Vaud et gratuite."),
  (0,"Elle assure le suivi psychothérapeutique au long cours","Faux : l'UMV n'effectue pas de suivi ; elle oriente vers le réseau."),
  (0,"Elle prend en charge les mineurs","Faux : elle s'adresse aux adultes.")),
 "n":n("umv","epi"),"a":"direct","d":2,"l":("Réseau vaudois.","Consultation spécialisée.","Adultes victimes.","UMV : gratuite, 24–48 h.","Adresser.","Croire qu'elle ne voit que des femmes.","UMV : adultes, hommes et femmes.")},
{"f":"A","m":0,"st":"À Genève, une femme de 35 ans, capable de discernement, présente des ecchymoses infligées, dit-elle, par son mari ; elle refuse que la police soit informée. Leurs deux enfants vivent au domicile.",
 "p":"Que retenez-vous sur le secret médical ?","o":A(
  (1,"Le secret s'applique malgré la poursuite d'office ; hors danger imminent, l'autorité pénale ne s'informe qu'avec son accord ou une levée par la commission du secret professionnel, mais vous pouvez aviser l'autorité de protection de l'enfant sans levée si l'intérêt des enfants le justifie","Juste : art. 321 CP, art. 12 et 86 LS, art. 17 CP, art. 314c al. 2 CC ; HUG 2023."),
  (0,"Vous devez dénoncer, car les lésions entre époux se poursuivent d'office","Faux : la poursuite d'office n'impose ni n'autorise la dénonciation par le médecin."),
  (0,"Vous pouvez informer la police dès que l'infraction se poursuit d'office","Faux : il faut un consentement, une levée ou un état de nécessité."),
  (0,"Pour aviser l'autorité de protection de l'enfant, une levée par la commission est toujours nécessaire","Faux : l'art. 314c al. 2 CC permet l'avis sans levée."),
  (0,"Le mari, qui partage le domicile, peut vous délier du secret","Faux : seul le maître du secret (la patiente) ou l'autorité peut délier.")),
 "n":n("secret","drap","enfant"),"a":"piège","d":3,"l":("Adulte capable, refus.","Secret professionnel.","Enfants au domicile.","Commission genevoise ; 314c.","Garder le secret, protéger les enfants.","Croire que l'office délie.","Adulte : secret ; enfant : avis possible.")},
{"f":"A","st":"Un paysagiste de 40 ans, complètement vacciné dans l'enfance, se fait au travail une plaie profonde de la paume souillée de terre ; sa dernière dose antitétanique remonte à 12 ans.",
 "p":"Quelle prophylaxie antitétanique proposez-vous ?","o":A(
  (1,"Une dose de rappel antitétanique (dTpa), sans immunoglobulines","Juste : de 26 à 64 ans, plaie à risque et dernière dose ≥ 10 ans (plan de vaccination 2026, tableau 10) ; posologies à vérifier dans l'AIPS (Swissmedic)."),
  (0,"Un rappel et des immunoglobulines antitétaniques","Faux : les immunoglobulines visent moins de 3 doses, un statut inconnu ou une immunosuppression."),
  (0,"Aucun rappel, car le seuil est de 20 ans","Faux : 20 ans vaut pour une plaie superficielle propre."),
  (0,"Une vaccination de base complète en trois doses","Faux : sa vaccination de base est complète."),
  (0,"Un rappel seulement si la plaie s'infecte","Faux : la prophylaxie se fait au moment de la blessure.")),
 "n":n("soins"),"a":"application","d":3,"l":("Plaie souillée, adulte.","Spores de Clostridium tetani.","Dernière dose à 12 ans.","Seuil 10 ans si risque élevé.","Rappel dTpa.","Ajouter des immunoglobulines.","26–64 ans : 10 ans si plaie à risque.")},
{"f":"A","m":0,"st":"L'avocat d'une patiente vous demande d'ajouter à votre constat : « lésions causées par M. X lors de l'agression du 3 mars ». La patiente est d'accord.",
 "p":"Que faites-vous ?","o":A(
  (1,"Vous refusez : le constat ne désigne pas l'auteur ni n'affirme les faits ; ses dires y figurent déjà entre guillemets, et l'interprétation relève de l'expertise","Juste : HAS 2011 ; Fracasso 2020 ; un document neutre garde sa valeur de reconnaissance."),
  (0,"Vous l'ajoutez, puisque la patiente consent","Faux : le consentement ne transforme pas une allégation en constatation."),
  (0,"Vous ajoutez « lésions compatibles avec les dires de la patiente »","Faux : la compatibilité est une interprétation."),
  (0,"Vous envoyez directement le constat modifié à l'avocat","Faux : on ne modifie pas le contenu, et le document se remet à la patiente."),
  (0,"Vous changez la date de l'examen pour la faire coïncider avec les faits","Faux : certificat contraire à la vérité (art. 318 CP).")),
 "n":n("faux","diag","def","prono"),"a":"piège","d":3,"l":("Pression d'un avocat.","Neutralité du document.","Auteur nommé.","Pas d'auteur, pas d'interprétation.","Refuser, expliquer.","Céder au consentement.","Le constat décrit, il n'accuse pas.")},
{"f":"Kprim","m":0,"st":"Vous rédigez la partie « examen » d'un constat de coups et blessures.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"On examine tout le corps, y compris la bouche, les gencives, les tympans, les mains et les organes génitaux.","Vrai : HUG 2023."),
  (1,"Chaque lésion se décrit par son type, sa localisation, sa forme, son orientation, sa taille, son aspect, sa couleur et ses abords.","Vrai : HUG 2023."),
  (1,"On décrit l'état émotionnel sans termes connotés comme « patient revendicateur » ou « gentille dame ».","Vrai : HUG 2023."),
  (0,"On écrit « brûlure de cigarette » quand la forme est typique.","Faux : c'est une interprétation ; on décrit la lésion.")),
 "n":n("corps","descr","psy"),"a":"direct","d":3,"l":("Examen.","Exhaustivité.","Tout le corps.","Huit critères.","Décrire.","Interpréter la forme.","Type, siège, forme, taille, couleur.")},
{"f":"Kprim","m":0,"st":"Vous photographiez les lésions pour un constat de coups et blessures.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"On prend un champ large puis un détail de chaque lésion.","Vrai : Fracasso 2020."),
  (1,"L'échelle métrique se place au même plan que la lésion.","Vrai : Fracasso 2020."),
  (1,"On garde un exemplaire au dossier et l'on en remet un au patient.","Vrai : Fracasso 2020."),
  (0,"On photographie sans l'accord du patient, car l'intérêt de la preuve prime.","Faux : les photographies se font et se joignent avec son accord (HAS 2011).")),
 "n":n("photo","remise"),"a":"direct","d":3,"l":("Photographies.","Preuve.","Règles.","Large, détail, échelle.","Photographier.","Sans accord.","Accord, échelle, deux exemplaires.")},
{"f":"Kprim","m":0,"st":"Un accidenté vous consulte et vous remplissez les documents de l'assurance-accidents (LAA).",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"Le salarié doit aviser sans retard son employeur ou l'assureur de tout accident qui nécessite un traitement médical.","Vrai : art. 45 al. 1 LAA."),
  (1,"Le médecin traitant remplit honnêtement et entièrement les formulaires et les renvoie sans délai.","Vrai : art. 53 al. 3 OLAA."),
  (1,"Le médecin transmet à l'assureur les indications nécessaires sans consentement supplémentaire du patient.","Vrai : art. 54a LAA."),
  (0,"Un avis tardif de plus de 3 mois fait perdre toute prestation, soins compris.","Faux : l'assureur peut réduire les prestations de moitié en cas de retard inexcusable (art. 46 LAA).")),
 "n":n("decl","laa54a","rixe"),"a":"direct","d":3,"l":("LAA.","Déclaration et renseignements.","Rôles.","Avis sans retard, formulaires.","Remplir.","Croire à une perte totale.","Sans retard, honnêtement.")},
{"f":"Kprim","m":0,"st":"Une victime de coups vous interroge sur ses droits après son constat.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"Des lésions corporelles simples, sans arme ni objet dangereux, se poursuivent en principe sur plainte.","Vrai : art. 123 ch. 1 CP."),
  (1,"Le délai de plainte est de 3 mois dès que la victime connaît l'auteur.","Vrai : art. 31 CP."),
  (1,"Elle peut s'adresser au centre LAVI de son choix, quelle que soit la date de l'infraction.","Vrai : art. 15 LAVI."),
  (0,"L'aide aux victimes exige que l'auteur soit identifié.","Faux : le droit existe que l'auteur ait été découvert ou non (art. 1 al. 3 LAVI).")),
 "n":n("plainte","lavi","umv"),"a":"direct","d":3,"l":("Droits.","Plainte et aide.","Délais.","3 mois ; LAVI au choix.","Informer.","Exiger un auteur connu.","Plainte 3 mois ; LAVI sans auteur connu.")},
{"f":"MenuLong","m":0,"st":"Vous rédigez le constat d'une femme de 37 ans qui dit avoir été frappée la veille.",
 "p":"Choisissez les TROIS formulations conformes.","o":A(
  (1,"« Plaie contuse de 1,5 cm à bords irréguliers avec ponts tissulaires, au cuir chevelu pariétal droit. »","Juste : type, taille, bords et siège."),
  (1,"« Mme X nous raconte que, le 2 mars vers 22 heures, à son domicile, son compagnon l'a saisie aux bras. »","Juste : dires déclaratifs, avec qui, où, quand et comment."),
  (1,"« Nous ne mettons pas en évidence d'autre lésion au moment de l'examen. »","Juste : signe négatif utile (HUG 2023)."),
  (0,"« Traces de strangulation. »","Faux : interprétation qui relève de l'expertise."),
  (0,"« Contusions du membre supérieur gauche post-agression. »","Faux : terme interprétatif et judiciaire."),
  (0,"« Brûlure de cigarette à l'avant-bras. »","Faux : interprétation de l'objet."),
  (0,"« Patiente gentille et collaborante. »","Faux : termes connotés et flous."),
  (0,"« Lésions compatibles avec les dires de la patiente. »","Faux : interprétation."),
  (0,"« Ecchymose datant de trois jours d'après sa couleur. »","Faux : datation non fiable."),
  (0,"« Mme X a été victime de violences de la part de son compagnon. »","Faux : affirme les faits et l'auteur."),
  (0,"« Plaie par instrument tranchant à bords irréguliers avec ponts tissulaires. »","Faux : contradictoire ; les ponts signent une plaie contuse."),
  (0,"« Incapacité totale de travail au sens du droit français : 5 jours. »","Faux : notion française ; en Suisse, on note l'incapacité de travail en pourcentage.")),
 "n":n("dires","vocab","negatifs","diag","descr"),"a":"direct","d":3,"l":("Rédaction.","Décrire, rapporter.","Formulations.","Descriptif, déclaratif, négatif.","Choisir.","Interpréter, dater, connoter.","Il dit ; je vois ; rien d'autre.")},
{"f":"MenuLong","m":0,"st":"Une employée de commerce de 30 ans a été frappée dans la rue par un inconnu ; vous avez établi son constat et elle vous interroge sur l'aide aux victimes (LAVI).",
 "p":"Choisissez les TROIS affirmations exactes.","o":A(
  (1,"Elle a droit à l'aide même si l'auteur n'est pas identifié","Juste : art. 1 al. 3 LAVI."),
  (1,"Les conseils et l'aide immédiate du centre de consultation sont gratuits","Juste : art. 5 LAVI."),
  (1,"Une éventuelle demande d'indemnisation LAVI s'introduit dans les 5 ans","Juste : art. 25 al. 1 LAVI."),
  (0,"La LAVI paie avant l'assureur-accidents","Faux : ses prestations sont subsidiaires (art. 4 LAVI)."),
  (0,"Elle doit d'abord porter plainte pour consulter un centre LAVI","Faux : aucune plainte n'est exigée pour consulter."),
  (0,"Elle ne peut consulter que le centre de son domicile","Faux : elle choisit son centre (art. 15 al. 3 LAVI)."),
  (0,"Une infraction commise à l'étranger donne droit à une indemnité LAVI","Faux : ni indemnité ni réparation morale (art. 3 al. 2 LAVI)."),
  (0,"Le délai de plainte pour des lésions simples est d'un an","Faux : 3 mois (art. 31 CP)."),
  (0,"Le médecin doit transmettre le constat au centre LAVI","Faux : le document lui appartient ; le secret s'applique."),
  (0,"La LAVI n'aide que les victimes de violence conjugale","Faux : toute atteinte à l'intégrité par une infraction."),
  (0,"Les proches n'ont droit à aucune aide","Faux : les proches y ont aussi droit (art. 1 al. 2 LAVI)."),
  (0,"L'aide cesse dès que la plainte est retirée","Faux : l'aide ne dépend pas de la plainte.")),
 "n":n("lavi","plainte"),"a":"application","d":4,"l":("Victime d'un inconnu.","Aide aux victimes.","Droits.","Auteur inconnu, gratuité, 5 ans.","Orienter.","Croire la LAVI prioritaire.","LAVI : sans auteur connu, subsidiaire.")},
]
_S = [[ACEP,HUG23],[FRA,HAS,HUG23],[FRA,HAS],[CP,LSGE,CPP,HUG23],[MAG,HAS,HUG23,CP],[OLAA,LAA,LAVI,HAS],[LAA,SUVA,LPGA],[FRA,HUG23,UMV,CMLV],[FRA,HAS,HUG23],[FRA,HUG23],[UMV],[CP,LSGE,CC,HUG23],[PV,BOO],[HAS,FRA,CP],[HUG23],[FRA,HAS],[LAA,OLAA],[CP,LAVI,UMV],[HUG23,HAS,ACEP,MAG],[LAVI,CP]]
for _q, _s in zip(Q, _S): _q["src"] = _s
C = {"theme":"Constat médical initial de lésions traumatiques par le médecin de premier recours (porte O7.17) : document descriptif et non interprétatif qui ne se refuse pas, dires entre guillemets (qui, où, quand, comment), description de chaque lésion selon huit critères, vocabulaire (plaie contuse à ponts tissulaires, plaie tranchante, plaie piquante), pas de datation par la couleur, photographies avec échelle en deux exemplaires, examen à distance sans délai légal ; UMV du CURML et CMLV des HUG, UIMPV ; secret (art. 321 CP, commission genevoise, art. 171 CPP), transmission à l'assureur-accidents (art. 54a LAA), déclaration et rixe (art. 45–46 LAA, art. 49 et 53 OLAA), art. 318 CP, LAVI, rappel antitétanique (dTpa)",
 "notions":[
  {"titre":"Comprendre","rub":["definition","epidemiology","basicSciences","prognosisDischarge"],"comment":"Le constat est un état des lieux descriptif que tout médecin consulté établit à la demande du patient ; l'expertise interprétative répond au magistrat.",
   "points":["UMV 2017 : 1018 consultations, 49,7 % d'hommes, âge médian 32 ans.","Pas de délai légal ; idéal 24–48 heures.","Pas de datation d'une ecchymose par sa couleur."],"sources":[HUG23,FRA,UMV,MAG]},
  {"titre":"Reconnaître","rub":["anamnesis","clinicalExam","presumptionRedFlags","positiveDiagnosis"],"comment":"On rapporte les dires entre guillemets, on examine tout le corps et l'on décrit chaque lésion sans l'interpréter.",
   "arbre":[("d1",None,"Patient qui dit avoir été blessé","On note ses dires entre guillemets et toutes ses plaintes.",None,None),("d2","d1","Examen de tout le corps","On décrit chaque lésion selon huit critères.",None,None),("d3","d1","Strangulation, menaces de mort, arme","On évalue les risques immédiats.",None,None),("d4","d2","Ponts tissulaires dans une plaie","On écrit plaie contuse, sans nommer d'objet.",None,None)],
   "points":["Qui, où, quand, comment, en verbatim.","Ni auteur, ni réalité des faits, ni caractère volontaire."],"sources":[HUG23,FRA,HAS,ACEP]},
  {"titre":"Décider","rub":["workupGoldStandard","workupAlternatives","acuteManagement","chronicManagement"],"comment":"On photographie avec méthode, on soigne, on respecte le secret et l'on remplit les documents de l'assurance-accidents.",
   "tab":(["Destinataire","Conduite","Base"],[["Patient","Remise en mains propres, copie au dossier",[("CURML","Document qui lui appartient.")]],["Police ou ministère public","Consentement ou levée écrite",[("CP","Art. 321 ch. 2 ; Genève : art. 12 et 86 LS.")]],["Assureur-accidents","Indications nécessaires sans consentement supplémentaire",[("LAA","Art. 54a.")]],["Employeur","Avis d'accident par le salarié",[("LAA","Art. 45.")]],["Autorité de protection de l'enfant","Avis possible sans levée",[("CC","Art. 314c al. 2.")]]]),
   "points":["Photographies : large, détail, échelle au même plan, deux exemplaires.","Rixe : prestations en espèces réduites au moins de moitié."],"sources":[FRA,CP,LAA,OLAA]},
  {"titre":"Suivre","rub":["hospitalizationComplications","surveillance","followUpNetwork"],"comment":"On garde une copie, on oriente vers la LAVI et les consultations spécialisées et l'on évite tout document contraire à la vérité.",
   "points":["Art. 318 CP : 3 ans au plus ou peine pécuniaire.","LAVI : sans auteur connu, gratuite, subsidiaire ; indemnisation dans les 5 ans.","Lésions simples : plainte dans les 3 mois."],"sources":[CP,LAVI,LSGE,CMLV]}],
 "ssp":("O7.17","Demande de certificat, d’attestation ou d’expertise par un patient ou un assureur",True,[
   ("n1",None,"Demande de documentation de blessures","On soigne d'abord, puis l'on accepte la demande, même sans plainte.","cl","c2"),
   ("n2","n1","Récit des faits","On note les dires entre guillemets et toutes les plaintes.","cl","c2"),
   ("n3","n1","Examen","On décrit chaque lésion, on photographie et l'on mentionne les examens.","cl","c3"),
   ("n4","n2","Strangulation, menaces, enfants","On évalue les risques immédiats et l'on oriente vers l'UMV ou la CMLV.","cl","c2"),
   ("n5","n3","Demande d'un tiers","On transmet à l'assureur-accidents le nécessaire, à la police seulement avec accord ou levée.","cl","c3"),
   ("n6","n3","Remise","On remet le document au patient, on garde une copie et l'on oriente vers la LAVI.","cl","c4")]),
 "pec":[
  pec("cl","Constat médical initial de lésions traumatiques",["On fournit au patient une preuve contemporaine, neutre et complète de ses lésions.","On soigne, on protège et l'on oriente sans juger les faits."],
      ["On reçoit le patient au calme, avec un interprète professionnel si besoin.","On explique le secret médical et à qui appartient le document."],
      [("Rappel antitétanique (dTpa), par exemple Boostrix","1 dose i.m. dans le deltoïde dès 4 ans (résumé suisse) ; de 26 à 64 ans, si la dernière dose remonte à 10 ans ou plus pour une plaie à risque, 20 ans pour une plaie superficielle propre ; posologies à vérifier dans l'AIPS (Swissmedic)","Il prévient le tétanos après une plaie souillée ou profonde.",PV+" ; "+BOO)],
      [("autre","On rédige le document descriptif avec photographies et schéma corporel.","On préserve une preuve fiable des lésions qui s'effacent."),("social et assurances","On oriente vers un centre LAVI et l'on remplit les formulaires de l'assurance-accidents.","On permet au patient de faire valoir ses droits."),("psychothérapie","On propose un soutien en cas de symptômes de stress post-traumatique.","On traite les suites psychiques de la violence.")],
      [("L Médecine légale Forensique","On décrit sans interpréter et l'on adresse si besoin à l'UMV ou à la CMLV."),("F Droit médical suisse","On respecte le secret et les bases légales de transmission."),("A Assurances sociales","On distingue la transmission à l'assureur-accidents de la remise au patient.")],
      None,
      (["On soigne d'abord.","On documente sans interpréter.","On remet le document au patient."],[("d'abord","médecin de premier recours","Il soigne les lésions, fait la prophylaxie antitétanique et évalue les risques immédiats."),("ensuite","médecin de premier recours","Il note les dires entre guillemets, décrit chaque lésion et prend les photographies."),("puis","consultation spécialisée ou centre LAVI","Elle complète la documentation si besoin et soutient la victime dans ses démarches.")]),
      "Un document neutre et complet aide la victime à faire valoir ses droits ; un document tardif, interprétatif ou complaisant perd sa valeur et engage la responsabilité du médecin.",
      [("Évolution des lésions","Dans les jours qui suivent si besoin","Photographies de suivi et document complémentaire"),("Symptômes psychiques et danger","À chaque consultation","Soutien en place, aucune nouvelle violence")],"Le patient repart avec son document remis en mains propres, une copie au dossier et les adresses de la LAVI.",
      ("On informe la population qu'un examen médical rapide préserve les preuves.","On documente tôt et l'on oriente vers les consultations spécialisées.","On suit les suites physiques et psychiques et l'on complète la documentation.")),]}
