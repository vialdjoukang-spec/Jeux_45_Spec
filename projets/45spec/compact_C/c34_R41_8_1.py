from constructeur_agent_45spec import pec
ID = "R41.8_1__O7_15-E06"
PLAN = "non_monographique"
EGS = "[HUG, Service de médecine de premier recours, Évaluation gériatrique standardisée (L. Di Pollina, A.-S. Steiner, G. Gold, 2010), § 2.3 AIVQ, § 2.5.1 troubles cognitifs, § 2.6.3 polymédication, points à retenir et annexes (test de l'horloge, semainier), lu le 27.11.2026]"
SMI = "[Smith C, Rubli E, Senn N, Major K, Nguyen S, Humbert M, Büla C, Patients âgés vulnérables au cabinet : comment les identifier et quelles ressources mobiliser ?, Rev Med Suisse (2014) 10:2077-80 (PDF chuv.ch), drapeaux rouges, tableau 3 et ressources, lu le 27.11.2026]"
C66 = "[HUG, CAPP-INFO n° 66, État confusionnel aigu chez le patient âgé ou en situation de vulnérabilité (2016), causes, tableau 2 et conduite médicamenteuse, lu le 27.11.2026]"
C67 = "[HUG, CAPP-INFO n° 67, Médicaments, chutes & fractures (2022), préambule et psychotropes, lu le 27.11.2026]"
PCV = "[HUG, Recommandations post-COVID pour médecins traitants (2025), évaluation cognitive : MoCA anormale sous 26/30, lu le 27.11.2026]"
JIM = "[HUG, Jimenez Thomet J., Améliorer la gestion de la polymédication auprès des personnes âgées dépendantes, mémoire du diplôme d'éducation thérapeutique (volée 2006-2009), chapitre « La compliance », lu le 27.11.2026]"
BEE = "[American Geriatrics Society, 2023 updated AGS Beers Criteria, J Am Geriatr Soc (2023), PMID 37139824, texte intégral PMC12478568 (tableaux 2, 3, 5 et 7), lu le 27.11.2026]"
STO = "[O'Mahony D et al., STOPP/START criteria for potentially inappropriate prescribing in older people: version 3, Eur Geriatr Med (2023), PMID 37256475, texte intégral PMC10447584 (résultats et discussion ; annexe des critères non lue), lu le 27.11.2026]"
MOC = "[Nasreddine ZS et al., The Montreal Cognitive Assessment, MoCA, J Am Geriatr Soc (2005), PMID 15817019, résumé lu le 27.11.2026]"
MCG = "[Borson S et al., The Mini-Cog: a cognitive 'vital signs' measure, Int J Geriatr Psychiatry (2000), PMID 11113982, résumé lu le 27.11.2026]"
GIL = "[Gill SS et al., A prescribing cascade involving cholinesterase inhibitors and anticholinergic drugs, Arch Intern Med (2005), PMID 15824303, résumé lu le 27.11.2026]"
COU = "[Coupland CAC et al., Anticholinergic drug exposure and the risk of dementia, JAMA Intern Med (2019), PMID 31233095, résumé lu le 27.11.2026]"
CAM = "[Campbell NL et al., Medication adherence in older adults with cognitive impairment: a systematic evidence-based review, Am J Geriatr Pharmacother (2012), PMID 22657941, résumé lu le 27.11.2026]"
ELS = "[El-Saifi N et al., Medication adherence in older patients with dementia: a systematic literature review, J Pharm Pract (2018), PMID 28539102, résumé lu le 27.11.2026]"
ARI = "[Compendium.ch, résumé (Brevier) d'Aricept Evess (donépézil) 5 mg, posologie et limitation LS, lu le 27.11.2026 ; AIPS complète à vérifier]"
ELI = "[Compendium.ch, résumé (Brevier) d'Eliquis (apixaban) 2,5 mg, posologie de la fibrillation auriculaire et critères de réduction, lu le 27.11.2026 ; AIPS complète à vérifier]"
DIA = "[Compendium.ch, résumé (Brevier) de Diamicron MR (gliclazide) 60 mg, posologie, contre-indications et limitation, lu le 27.11.2026 ; AIPS complète à vérifier]"
VES = "[Compendium.ch, résumé (Brevier) de Vesicare (solifénacine) 5 mg, posologie, contre-indications et quote-part, lu le 27.11.2026 ; AIPS complète à vérifier]"
LOA = "[pharmaSuisse, structure tarifaire LOA V / RBP V (en vigueur le 1.1.2026), prestation « semainier » par paliers de 3–5, 6–8 et 9 médicaments ou plus : extrait de recherche web seulement, PDF non ouvert (à vérifier)]"
MEL = "[Compendium.ch, résumé (Brevier) de Melix (glibenclamide) 5 mg, posologie et contre-indications, lu le 27.11.2026 ; AIPS complète à vérifier]"
ATA = "[Compendium.ch, résumé (Brevier) d'Atarax (hydroxyzine) 25 mg, indication prurit et contre-indications, lu le 27.11.2026 ; AIPS complète à vérifier]"
MAR = "[Compendium.ch, recherche de produit : Marcoumar (phenprocoumone) 3 mg commercialisé en Suisse, lu le 27.11.2026]"
EXP = "Avis d'expert (à vérifier)"
_N = [
("def","definition","critère",2,0,SMI+" ; "+CAM,"Les oublis du sujet âgé sont des prises incorrectes non voulues, liées à la charge thérapeutique (polymédication, définie le plus souvent par 5 médicaments ou plus) et à des déficits cognitifs, visuels ou manuels, et non à un refus du traitement."),
("epi","epidemiology","chiffre",2,0,ELS,"Chez la personne âgée avec une démence, la prise conforme du traitement varie de 17 à 42 % selon les études, l'arrêt avant terme de 37 à 80 %, et la mauvaise prise s'associe à plus d'hospitalisations et de décès."),
("barr","epidemiology","terrain particulier",1,0,CAM,"Chez la personne avec des troubles cognitifs, vivre seule, devoir comprendre de nouvelles consignes, intégrer les prises dans sa routine et recevoir des médicaments potentiellement inappropriés font obstacle à une prise correcte."),
("mech","basicSciences","mécanisme",2,0,EGS+" ; "+EXP,"Les risques d'interaction, de surdosage et de mauvaise prise augmentent fortement au-delà de 3 médicaments ; le déclin de la mémoire et des fonctions exécutives empêche de planifier les prises, et une baisse de la vue ou de la dextérité gêne la lecture des boîtes et l'ouverture des blisters."),
("achb","basicSciences","chiffre",1,0,COU+" ; "+BEE,"L'exposition cumulée aux anticholinergiques forts s'associe à un risque accru de démence (OR ajusté 1,49 au-delà de 1095 doses quotidiennes standard), notamment pour les antidépresseurs anticholinergiques, les antimuscariniques vésicaux et les antipsychotiques ; Beers 2023 demande d'évaluer la charge anticholinergique totale lors des revues régulières de médication."),
("bag","anamnesis","examen",2,0,EGS+" ; "+C66+" ; "+EXP,"On répertorie tout ce que la personne prend, prescrit ou non, phytothérapie comprise, en lui faisant apporter toutes ses boîtes et en interrogeant aussi ses proches, son pharmacien et son médecin traitant."),
("aivq","anamnesis","critère",1,0,EGS+" ; "+SMI,"« Prendre ses médicaments » fait partie des activités instrumentales de la vie quotidienne : on demande ce que la personne fait seule et qui prépare le semainier (elle-même, un proche ou une infirmière)."),
("cog","clinicalExam","examen",2,0,MCG+" ; "+MOC+" ; "+PCV,"Le Mini-Cog associe le rappel de 3 mots et le dessin d'une horloge en 3 minutes environ, peu influencé par la langue et la scolarité ; la MoCA détecte mieux un trouble cognitif léger que le MMSE (90 % contre 18 % au seuil de 26 points) et se juge anormale sous 26/30."),
("clock","clinicalExam","examen",1,0,EGS,"Le test de l'horloge des HUG demande de dessiner un cadran avec tous les chiffres et des aiguilles qui indiquent 11 h 10 ; il se cote sur 10 points (cadran 2, chiffres 4, aiguilles 4), et des aiguilles placées sur le 11 et le 10 signent un défaut d'inhibition."),
("sens","clinicalExam","signe",1,0,SMI+" ; "+EXP,"On dépiste la baisse de la vue en faisant lire le journal et l'on observe la personne sortir un comprimé de son emballage et lire une étiquette, car la vue et la dextérité conditionnent la prise autonome."),
("dbl","presumptionRedFlags","complication",3,0,EGS+" ; "+BEE+" ; "+EXP,"Une prise en double ou désordonnée d'un médicament à marge étroite (anticoagulant oral, hypoglycémiant, digoxine, diurétique) constitue le danger principal : hypoglycémie parfois prolongée sous sulfonylurée à longue action, hémorragie, bradycardie ou insuffisance rénale."),
("pos","positiveDiagnosis","critère",2,0,EGS+" ; "+EXP,"On retient des oublis liés à la charge ou aux troubles cognitifs quand des indices concordants (boîtes pleines ou finies trop tôt, retraits espacés à la pharmacie, déséquilibre inexpliqué) coexistent avec un test cognitif anormal ou une perte d'autonomie pour la prise des médicaments."),
("desq","positiveDiagnosis","diagnostic différentiel",1,0,C66+" ; "+EGS+" ; "+EXP,"Une confusion d'apparition aiguë et fluctuante n'est pas une démence : elle impose de chercher une cause (toxicité médicamenteuse dans environ 30 % des cas, hypoglycémie, infection, rétention urinaire, constipation) et de différer le test cognitif ; une dépression peut aussi mimer un déclin cognitif."),
("revue","workupGoldStandard","décision",3,0,EGS+" ; "+STO,"Le bilan de référence associe une revue structurée de tous les médicaments (indication, effet, doublons, marge étroite, anticholinergiques), aidée par exemple des critères STOPP/START, à une évaluation cognitive et fonctionnelle de la capacité à gérer seul son traitement."),
("stopp","workupGoldStandard","chiffre",1,0,STO,"La version 3 de STOPP/START (2023) compte 190 critères, 133 STOPP pour les médicaments potentiellement inappropriés et 57 START pour les omissions ; un logiciel ne suffit pas, car plus de la moitié des alertes de l'essai OPERAM n'étaient pas pertinentes pour le cas."),
("beers","workupAlternatives","critère",1,0,BEE,"Les critères de Beers 2023 visent les personnes de 65 ans et plus, sont conçus pour les États-Unis, et déconseillent en cas de démence les anticholinergiques, les benzodiazépines, les hypnotiques en Z et les antipsychotiques au long cours."),
("pharm","workupAlternatives","examen",2,0,C66+" ; "+EXP,"On confronte la liste au dossier de la pharmacie (dates des délivrances), au récit d'un proche et aux constats des soins à domicile, car le récit seul d'une personne dont la mémoire faiblit ne suffit pas."),
("acute","acuteManagement","décision",2,0,BEE+" ; "+EXP,"Devant une prise en double d'un hypoglycémiant ou d'un anticoagulant, on évalue d'emblée la glycémie ou les signes de saignement, on surveille assez longtemps une sulfonylurée à longue action, et l'on confie sans délai la préparation des doses à un tiers."),
("simp","chronicManagement","décision",3,0,EGS+" ; "+JIM+" ; "+EXP,"On simplifie le traitement : on arrête ce qui n'a plus d'indication, on supprime les doublons, on réduit le nombre de prises quand une forme à une prise existe, on note le but de chaque médicament sur une carte de traitement et l'on fait préparer un semainier par la pharmacie, un proche ou les soins à domicile."),
("depr","chronicManagement","décision",1,0,BEE+" ; "+C66,"On déprescrit en priorité les anticholinergiques, les benzodiazépines et les hypnotiques en Z, on évite d'associer plusieurs anticholinergiques ou 3 médicaments actifs sur le système nerveux central ou plus (benzodiazépines, hypnotiques en Z, opioïdes, antidépresseurs, antipsychotiques, antiépileptiques), et l'on arrête une benzodiazépine progressivement pour éviter le sevrage."),
("casc","chronicManagement","piège",1,0,GIL+" ; "+VES,"Une incontinence urinaire nouvelle sous inhibiteur de la cholinestérase peut en être l'effet indésirable : la traiter par un antimuscarinique crée une cascade médicamenteuse (risque ajusté 1,55) qui aggrave la confusion."),
("human","chronicManagement","décision",1,0,CAM,"Chez la personne avec des troubles cognitifs, des rappels humains fréquents (proche, infirmière, appel) semblent plus efficaces que des rappels techniques seuls."),
("hosp","hospitalizationComplications","complication",3,0,ELS+" ; "+C67+" ; "+C66,"Les erreurs de prise et les médicaments inappropriés mènent à des hospitalisations : chutes et fractures (surtout sous psychotropes), hémorragies, hypoglycémies et états confusionnels."),
("surv","surveillance","décision",2,0,EGS+" ; "+EXP,"On revoit la liste des médicaments si possible à chaque consultation et au moins tous les 6 mois, ainsi qu'à chaque sortie d'hôpital, et l'on vérifie avec le proche ou les soins à domicile que le semainier se vide comme prévu."),
("lsari","surveillance","contexte suisse",1,1,ARI,"En Suisse, la limitation LS du donépézil (Aricept) exige une évaluation cognitive (MMSE, ou MoCA convertie) au début puis tous les 6 mois, l'arrêt au stade sévère ou sous un MMSE de 10, et ne rembourse pas d'association ; on commence par 5 mg le soir pendant au moins 1 mois, au plus 10 mg par jour (posologies à vérifier dans l'AIPS (Swissmedic))."),
("prog","prognosisDischarge","pronostic",1,0,EGS+" ; "+JIM,"L'évaluation gériatrique systématique réduit le déclin fonctionnel, les hospitalisations et l'entrée en institution, et diminue de 35 % les effets indésirables médicamenteux sévères ; un semainier préparé et contrôlé soutient le maintien à domicile."),
("net","followUpNetwork","contexte suisse",1,1,SMI+" ; "+EGS,"Le médecin de famille coordonne le centre médico-social ou les soins à domicile, une consultation mémoire si le diagnostic reste incertain et une consultation pour proches aidants ; il recherche l'épuisement de l'aidant et discute une mesure de protection si nécessaire."),
("loa","followUpNetwork","contexte suisse",1,1,LOA,"En Suisse, la pharmacie facture la préparation d'un semainier selon la structure LOA V en vigueur depuis le 1er janvier 2026, par paliers selon le nombre de médicaments (3–5, 6–8, 9 ou plus) ; conditions de prescription et de remboursement à vérifier."),
]
K = {k: i+1 for i, (k, *_r) in enumerate(_N)}
N = [t[1:] for t in _N]
n = lambda *ks: [K[k] for k in ks]
AM = ["Boîtes pleines, retraits espacés, déséquilibre inexpliqué : vérifier la prise avant d'intensifier.",
      "Boîte finie trop tôt d'un médicament à marge étroite : prise en double possible (hypoglycémie, hémorragie).",
      "Mini-Cog, MoCA (< 26/30) et horloge : dépister la cause cognitive, jamais pendant une confusion aiguë.",
      "Simplifier et déprescrire (anticholinergiques, benzodiazépines, hypnotiques en Z) avant d'ajouter une aide.",
      "Cascade : incontinence sous donépézil traitée par antimuscarinique.",
      "Semainier LOA V en pharmacie, soins à domicile, proche aidant ; revue au moins tous les 6 mois."]
A = lambda *o: list(o)
PV = " (posologies à vérifier dans l'AIPS (Swissmedic))"
Q = [
{"f":"A","s":("S1",1,3),"st":"Une femme de 83 ans, veuve, vit seule. Son HbA1c est passée de 7,0 à 9,4 % en 6 mois sans changement de traitement. Sa fille a trouvé dans la cuisine trois boîtes de metformine encore pleines et une boîte de gliclazide vide, alors que la pharmacie l'avait délivrée pour un mois trois semaines plus tôt. Pendant la consultation, la patiente pose deux fois la même question.",
 "p":"Que faites-vous d'abord ?","o":A(
  (1,"Vous faites une revue de tous ses médicaments avec ses boîtes, le dossier de la pharmacie et sa fille, et un test cognitif rapide, avant de modifier le traitement","HUG EGS 2010 ; CAPP-INFO 66."),
  (0,"Vous ajoutez une insuline basale pour corriger l'HbA1c","Faux : le déséquilibre vient de la prise réelle ; ajouter un traitement complexe expose à l'hypoglycémie quand les prises reprennent."),
  (0,"Vous augmentez la dose de gliclazide","Faux : la boîte finie trop tôt évoque déjà des prises en trop, avec un risque d'hypoglycémie prolongée."),
  (0,"Vous demandez d'emblée une IRM cérébrale","Faux : on documente d'abord la prise et le déficit par un test de dépistage ; l'imagerie vient après un dépistage positif."),
  (0,"Vous lui remettez une liste écrite et la revoyez dans 3 mois","Faux : cette mesure ne corrige ni le risque immédiat d'hypoglycémie ni l'absence d'aide pour préparer les doses.")),
 "n":n("revue","dbl","pos","pharm","epi","bag"),"a":"application","d":4,"l":("Âgée, seule, déséquilibre sans cause.","Prises désordonnées.","Boîtes pleines et boîte vide trop tôt.","Revue et dépistage cognitif.","Vérifier avant d'intensifier.","Intensifier.","Boîtes discordantes = vérifier la prise.")},
{"f":"A","s":("S1",2,3),"st":"Le Mini-Cog est anormal : elle rappelle un mot sur trois et son horloge est désorganisée. La glycémie capillaire de 11 h est à 3,4 mmol/l ; elle reçoit du gliclazide 120 mg le matin et de la metformine 1000 mg deux fois par jour.",
 "p":"Quelle décision prenez-vous pour son diabète ?","o":A(
  (1,"Vous arrêtez le gliclazide, gardez un schéma simple et confiez la préparation et le contrôle des prises à un tiers","Beers 2023 (sulfonylurées à éviter, hypoglycémie) ; HUG EGS 2010."),
  (0,"Vous gardez le gliclazide et lui conseillez de manger davantage","Faux : la sulfonylurée expose à des hypoglycémies répétées et parfois prolongées chez une personne qui ne gère plus ses doses."),
  (0,"Vous ajoutez une insuline rapide selon la glycémie avant chaque repas","Faux : Beers 2023 déconseille l'insuline rapide seule selon la glycémie, qui augmente l'hypoglycémie sans mieux contrôler le diabète."),
  (0,"Vous passez à un schéma basal-bolus à quatre injections qu'elle fera seule","Faux : un schéma complexe est inadapté à une personne qui ne planifie plus ses prises."),
  (0,"Vous remplacez le gliclazide par du glibenclamide","Faux : le glibenclamide est une sulfonylurée à longue action, avec un risque encore plus élevé d'hypoglycémie prolongée.")),
 "n":n("dbl","simp","acute","cog"),"a":"piège","d":5,"l":("Hypoglycémie, test cognitif anormal.","Sulfonylurée et prises incontrôlées.","Glycémie basse.","Arrêter la sulfonylurée.","Simplifier, déléguer.","Ajouter ou garder.","Cognition faible + sulfonylurée = arrêter.")},
{"f":"A","s":("S1",3,3),"st":"La patiente veut rester chez elle. Ses médicaments tiennent désormais en une prise le matin. Sa fille travaille à plein temps et passe le week-end.",
 "p":"Comment organisez-vous la suite ?","o":A(
  (1,"Vous prescrivez un semainier préparé par la pharmacie, organisez un passage des soins à domicile pour la prise, informez la fille comme proche aidante et revoyez la liste au moins tous les 6 mois","Structure LOA V (à vérifier) ; Smith, Rev Med Suisse 2014 ; HUG EGS 2010."),
  (0,"Vous demandez à la patiente de remplir seule son semainier chaque dimanche","Faux : elle ne planifie plus ses prises ; la préparation doit revenir à un tiers."),
  (0,"Vous proposez une entrée immédiate en EMS contre son avis","Faux : les ressources à domicile permettent souvent le maintien, et la décision se prend avec elle."),
  (0,"Vous lui remettez seulement un pilulier électronique à alarme","Faux : les rappels humains semblent plus efficaces que les rappels techniques seuls chez la personne avec des troubles cognitifs."),
  (0,"Vous arrêtez tout suivi médical puisque le schéma est simplifié","Faux : on revoit la liste au moins tous les 6 mois et à chaque transition.")),
 "n":n("loa","net","surv","simp","prog"),"a":"application","d":3,"l":("Maintien à domicile.","Préparation par un tiers.","Fille absente en semaine.","Semainier, soins à domicile.","Organiser le réseau.","Autogestion.","Préparer, contrôler, revoir.")},
{"f":"A","m":0,"st":"Un homme de 79 ans prend du donépézil depuis 4 mois pour une maladie d'Alzheimer légère. Il perd ses urines depuis 2 mois, et l'on vient de lui prescrire de la solifénacine 5 mg par jour. Depuis, il est plus confus et constipé.",
 "p":"Que proposez-vous ?","o":A(
  (1,"Vous arrêtez la solifénacine, qui crée une cascade médicamenteuse, et vous rediscutez l'incontinence et la place du donépézil","Gill 2005 ; Beers 2023."),
  (0,"Vous doublez la solifénacine à 10 mg par jour","Faux : l'antimuscarinique aggrave la confusion et la constipation ; l'augmenter accroît la charge anticholinergique."+PV),
  (0,"Vous ajoutez de l'oxybutynine à la solifénacine","Faux : Beers 2023 déconseille d'associer plusieurs anticholinergiques (déclin cognitif, confusion, chutes)."),
  (0,"Vous concluez à une progression de la maladie et augmentez le donépézil","Faux : une aggravation rapide après un nouveau médicament évoque d'abord un effet indésirable."),
  (0,"Vous ajoutez un antipsychotique pour la confusion","Faux : Beers 2023 déconseille les antipsychotiques pour les troubles du comportement liés à la démence.")),
 "n":n("casc","depr","achb"),"a":"piège","d":3,"l":("Incontinence sous donépézil.","Effet cholinergique, puis anticholinergique.","Confusion, constipation.","Cascade.","Arrêter le second médicament.","Traiter l'effet indésirable.","Nouveau symptôme = nouveau médicament ?")},
{"f":"A","st":"Une femme de 86 ans, qui gère seule ses comprimés, est amenée par son fils. Depuis 2 jours, elle est somnolente, ne suit pas la conversation, tient des propos décousus le soir et va mieux le matin. On lui a prescrit il y a 5 jours de l'hydroxyzine pour des démangeaisons.",
 "p":"Quelle est votre conduite ?","o":A(
  (1,"Vous traitez la situation comme une urgence : vous arrêtez l'hydroxyzine, cherchez une hypoglycémie, une infection, une rétention ou une constipation, et différez tout test cognitif","CAPP-INFO 66 ; Beers 2023."),
  (0,"Vous faites une MoCA aujourd'hui et retenez une démence si le score est bas","Faux : un test fait pendant une confusion aiguë et fluctuante ne permet pas de conclure à une démence."),
  (0,"Vous ajoutez de l'halopéridol le soir","Faux : Beers 2023 déconseille les antipsychotiques dans la confusion sauf échec des mesures non médicamenteuses et danger important."),
  (0,"Vous ajoutez du lorazépam pour la nuit","Faux : les benzodiazépines favorisent la confusion et les chutes chez la personne âgée."),
  (0,"Vous organisez un semainier et la revoyez dans 3 mois","Faux : une confusion aiguë impose une recherche de cause immédiate.")),
 "n":n("desq","achb","beers","hosp","pos"),"a":"piège","d":5,"l":("Somnolence, inattention, fluctuation.","Cause aiguë, médicament anticholinergique.","Début récent, aggravation le soir.","Confusion aiguë ≠ démence.","Arrêter, chercher la cause.","Tester la cognition.","Aigu et fluctuant = chercher la cause.")},
{"f":"A","st":"Un homme de 81 ans, qui pèse 58 kg et dont la créatinine est à 140 µmol/l, prend de l'apixaban 5 mg deux fois par jour pour une fibrillation auriculaire. Il présente des ecchymoses multiples. La pharmacie signale qu'il est venu chercher une nouvelle boîte 12 jours avant la date attendue ; il range des boîtes entamées dans plusieurs pièces.",
 "p":"Que retenez-vous ?","o":A(
  (1,"La dose est trop forte pour lui, qui remplit deux critères de réduction à 2,5 mg deux fois par jour, et la boîte finie trop tôt évoque des prises en double : vous adaptez la dose, recherchez un saignement et confiez la préparation des prises à un tiers","Brevier Eliquis ; HUG EGS 2010 ; avis d'expert."+PV),
  (0,"La dose est adaptée et les ecchymoses sont banales à cet âge","Faux : âge de plus de 80 ans, poids de 60 kg ou moins et créatinine de 133 µmol/l ou plus font deux critères ou plus, qui imposent 2,5 mg deux fois par jour."+PV),
  (0,"Vous arrêtez définitivement l'anticoagulation","Faux : le risque d'AVC persiste ; on adapte la dose et l'on sécurise la prise plutôt que d'arrêter d'emblée."),
  (0,"Vous passez à la phenprocoumone pour mieux surveiller la prise","Faux : un antivitamine K donne un INR instable si les prises varient et ne règle pas la préparation des doses."),
  (0,"Vous lui demandez de noter ses prises sur un carnet sans autre mesure","Faux : un carnet tenu seul ne protège pas une personne qui ne se souvient plus de ses prises.")),
 "n":n("dbl","pharm","pos","acute"),"a":"application","d":4,"l":("Anticoagulé, ecchymoses, boîte finie trop tôt.","Surdosage et prises en double.","Âge, poids, créatinine.","Réduire, sécuriser.","Déléguer la préparation.","Arrêter ou changer de molécule.","Retrait trop précoce = prise en double ?")},
{"f":"A","st":"Une femme de 88 ans, avec des mains très déformées par l'arthrose et une cataracte des deux yeux, a une fibrillation auriculaire à 110/min, bien tolérée, sans signe de gravité. Dans sa boîte de bêtabloquant, les blisters sont presque intacts, alors que ses flacons à bouchon à vis sont presque vides.",
 "p":"Quelle explication cherchez-vous d'abord ?","o":A(
  (1,"Elle ne parvient probablement pas à sortir les comprimés des blisters : vous l'observez manipuler l'emballage, vérifiez sa vue et faites préparer ses prises dans un semainier facile à ouvrir","Smith, Rev Med Suisse 2014 ; HUG EGS 2010 ; avis d'expert."),
  (0,"Une résistance au bêtabloquant, qui justifie d'ajouter de la digoxine","Faux : le bêtabloquant n'est pas pris ; ajouter un médicament à marge étroite expose au surdosage quand les prises reprennent."),
  (0,"Une hyperthyroïdie à rechercher en premier","Faux : la discordance entre blisters intacts et flacons vides oriente d'abord vers un obstacle à la prise."),
  (0,"Un refus réfléchi du traitement","Faux : les flacons vides montrent qu'elle prend ce qu'elle peut ouvrir ; l'obstacle est manuel."),
  (0,"Une cardioversion électrique urgente","Faux : la fréquence reste tolérée, et l'on corrige d'abord le traitement non pris.")),
 "n":n("sens","mech","simp"),"a":"application","d":4,"l":("Mains déformées, cataracte.","Obstacle manuel et visuel.","Blisters intacts, flacons vides.","Observer la manipulation.","Adapter l'emballage.","Intensifier.","Blister intact = obstacle à l'ouverture ?")},
{"f":"A","m":0,"st":"Vous enseignez les oublis de médicaments liés à la polymédication chez la personne âgée.",
 "p":"Que retenez-vous ?","o":A(
  (1,"La polymédication se définit le plus souvent par 5 médicaments ou plus, et seule une minorité des personnes avec une démence prend son traitement comme prescrit (17 à 42 %)","Smith, Rev Med Suisse 2014 ; El-Saifi 2018."),
  (0,"La polymédication commence dès 2 médicaments","Faux : on retient le plus souvent 5 médicaments ou plus."),
  (0,"Le risque d'erreur de prise ne dépend pas du nombre de médicaments","Faux : il augmente fortement au-delà de 3 médicaments."),
  (0,"La plupart des personnes avec une démence prennent leur traitement sans erreur","Faux : la prise conforme varie de 17 à 42 %."),
  (0,"Les oublis traduisent presque toujours un refus délibéré","Faux : ils sont surtout non voulus, liés à la charge et aux déficits.")),
 "n":n("def","mech","epi"),"a":"direct","d":1,"l":("Définition.","Charge thérapeutique.","Seuil de 5.","Minorité de prises conformes.","Enseigner.","Refus délibéré.","5 médicaments, prises souvent incorrectes.")},
{"f":"A","m":0,"st":"Vous faites passer le test de l'horloge des HUG à un patient de 80 ans pour dépister un trouble cognitif.",
 "p":"Que retenez-vous de ce test ?","o":A(
  (1,"On demande un cadran avec tous les chiffres et des aiguilles qui indiquent 11 h 10, coté sur 10 points (cadran 2, chiffres 4, aiguilles 4)","HUG EGS 2010."),
  (0,"On demande de recopier une horloge dessinée par l'examinateur","Faux : la version spontanée demande de dessiner seul le cadran."),
  (0,"On aide le patient s'il bloque, pour ne pas le décourager","Faux : on ne l'aide pas ; on peut seulement répéter la consigne depuis le début."),
  (0,"Des aiguilles posées sur le 11 et le 10 sont une réponse correcte","Faux : elles signent une réponse forcée par le stimulus, un défaut d'inhibition."),
  (0,"Le test se cote sur 30 points comme le MMSE","Faux : il se cote sur 10 points.")),
 "n":n("clock","cog"),"a":"direct","d":2,"l":("Test de l'horloge.","Fonctions exécutives et visuospatiales.","Consigne 11 h 10.","Cotation sur 10.","Dépister.","Aider le patient.","Cadran 2, chiffres 4, aiguilles 4.")},
{"f":"A","m":0,"st":"Une patiente de 74 ans a un MMSE à 28/30, mais son mari décrit depuis un an des erreurs croissantes dans la prise de ses comprimés et dans ses paiements.",
 "p":"Quel test proposez-vous pour rechercher un trouble cognitif léger ?","o":A(
  (1,"Une MoCA, plus sensible que le MMSE pour un trouble cognitif léger et anormale sous 26/30","Nasreddine 2005 ; HUG post-COVID 2025."),
  (0,"Aucun, car un MMSE à 28/30 exclut tout trouble cognitif","Faux : au seuil de 26, le MMSE ne détecte que 18 % des troubles cognitifs légers."),
  (0,"Un nouveau MMSE dans 2 ans","Faux : la plainte de l'entourage et la perte d'autonomie justifient un test plus sensible maintenant."),
  (0,"Une ponction lombaire d'emblée","Faux : on dépiste d'abord par un test cognitif et l'on oriente ensuite."),
  (0,"Un questionnaire de satisfaction du traitement","Faux : il ne mesure pas la cognition.")),
 "n":n("cog","pos","def"),"a":"application","d":3,"l":("MMSE normal, plainte du conjoint.","Trouble léger.","Erreurs de comprimés et de paiements.","MoCA.","Tester mieux.","Se rassurer.","MMSE normal ≠ cognition normale.")},
{"f":"A","m":0,"st":"Vous faites la revue de médication d'un patient polymédiqué de 82 ans avec des troubles cognitifs.",
 "p":"Que retenez-vous des outils explicites ?","o":A(
  (1,"STOPP/START version 3 (2023) compte 190 critères, pour les médicaments inappropriés et les omissions ; Beers 2023 est conçu pour les États-Unis ; les alertes d'un logiciel demandent une interprétation clinique","STOPP/START v3 2023 ; Beers 2023."),
  (0,"Un logiciel qui applique STOPP/START remplace le jugement clinique","Faux : plus de la moitié des alertes de l'essai OPERAM n'étaient pas pertinentes pour le cas."),
  (0,"STOPP/START ne repère que les médicaments en trop, jamais les omissions","Faux : les critères START repèrent les omissions de traitement utiles."),
  (0,"Les critères de Beers s'appliquent sans réserve au marché suisse","Faux : ils sont conçus pour les États-Unis, avec des considérations propres à chaque pays."),
  (0,"La revue se limite aux médicaments prescrits","Faux : on répertorie aussi l'automédication et la phytothérapie.")),
 "n":n("stopp","beers","revue"),"a":"direct","d":3,"l":("Outils de revue.","Inapproprié et omis.","190 critères.","Interpréter les alertes.","Revoir.","Logiciel seul.","Outil explicite + jugement.")},
{"f":"A","m":0,"st":"Vous prescrivez en Suisse du donépézil (Aricept) à une patiente atteinte d'une maladie d'Alzheimer légère.",
 "p":"Que retenez-vous de la limitation et de la posologie ?","o":A(
  (1,"On fait une évaluation cognitive au début puis tous les 6 mois, on arrête sous un MMSE de 10, on ne rembourse pas d'association, et l'on commence par 5 mg le soir pendant au moins 1 mois avant d'aller au plus à 10 mg","Brevier Aricept."+PV),
  (0,"On commence d'emblée à 20 mg par jour","Faux : la dose maximale est de 10 mg par jour."+PV),
  (0,"Le remboursement ne demande aucune évaluation cognitive","Faux : la limitation exige une évaluation cognitive au début puis tous les 6 mois."),
  (0,"On poursuit le traitement quel que soit le stade","Faux : on l'arrête au stade sévère ou sous un MMSE de 10."),
  (0,"On rembourse l'association de deux traitements de la maladie","Faux : la limitation exclut le remboursement d'une association.")),
 "n":n("lsari","surv"),"a":"direct","d":3,"l":("Donépézil en Suisse.","Inhibiteur de la cholinestérase.","Limitation LS.","Évaluation tous les 6 mois.","Prescrire selon la LS.","Dose forte d'emblée.","LS : évaluer, arrêter sous 10.")},
{"f":"A","st":"Un homme de 84 ans vit avec son épouse de 82 ans, qui prépare chaque semaine ses 11 médicaments dans un semainier. Elle vient seule, épuisée ; elle dit qu'elle ne dort plus et qu'elle s'est trompée de case deux fois ce mois-ci. Lui ne sait plus nommer ses comprimés.",
 "p":"Que proposez-vous ?","o":A(
  (1,"Vous revoyez et simplifiez la liste, confiez la préparation du semainier à la pharmacie ou aux soins à domicile et orientez l'épouse vers une consultation pour proches aidants","Smith, Rev Med Suisse 2014 ; HUG EGS 2010 ; Campbell 2012."),
  (0,"Vous demandez à l'épouse de continuer en étant plus attentive","Faux : l'aidante est épuisée et les erreurs de case montrent que la préparation n'est plus sûre."),
  (0,"Vous remplacez le semainier par un pilulier électronique sans autre aide","Faux : les rappels humains semblent plus efficaces que les rappels techniques seuls."),
  (0,"Vous prescrivez un hypnotique en Z à l'épouse","Faux : Beers 2023 déconseille les hypnotiques en Z chez la personne âgée, et le problème tient à la charge d'aide."),
  (0,"Vous organisez une entrée immédiate en EMS du couple","Faux : on mobilise d'abord le réseau à domicile avec l'accord du couple.")),
 "n":n("net","human","simp","aivq"),"a":"application","d":4,"l":("Aidante épuisée, erreurs de case.","Charge d'aide trop lourde.","Onze médicaments.","Simplifier, déléguer, soutenir.","Mobiliser le réseau.","Laisser faire l'aidante.","Aidante épuisée = soins à domicile.")},
{"f":"A","st":"Une femme de 80 ans est hospitalisée pour une fracture du col du fémur après une chute nocturne. Elle prend du lorazépam, du zolpidem, de l'amitriptyline et de l'oxybutynine depuis plusieurs années.",
 "p":"Quelle décision médicamenteuse prenez-vous en priorité ?","o":A(
  (1,"Vous prévoyez une déprescription progressive des sédatifs et remplacez les anticholinergiques, car cette association augmente les chutes, la confusion et le déclin cognitif","Beers 2023 ; CAPP-INFO 67 ; CAPP-INFO 66."),
  (0,"Vous gardez tout, puisque ces médicaments sont bien tolérés depuis des années","Faux : un médicament toléré au long cours peut devenir dangereux quand l'état change ; la chute en témoigne."),
  (0,"Vous arrêtez brutalement les quatre médicaments le jour de l'admission","Faux : l'arrêt brutal d'une benzodiazépine expose au sevrage ; on diminue progressivement."),
  (0,"Vous ajoutez de la mélatonine et un deuxième hypnotique","Faux : ajouter un sédatif augmente encore le risque de chute."),
  (0,"Vous ajoutez du donépézil pour protéger la cognition","Faux : il ne corrige pas la charge anticholinergique et ajoute un médicament.")),
 "n":n("depr","hosp","achb","beers"),"a":"piège","d":5,"l":("Chute nocturne, fracture.","Sédatifs et anticholinergiques.","Quatre psychotropes.","Déprescrire progressivement.","Réduire la charge.","Arrêt brutal ou ajout.","Chute + sédatifs = déprescrire.")},
{"f":"Kprim","m":0,"st":"Vous évaluez si une personne âgée peut gérer seule ses médicaments.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"« Prendre ses médicaments » fait partie des activités instrumentales de la vie quotidienne.","HUG EGS 2010."),
  (1,"On demande qui prépare le semainier : la personne, un proche ou une infirmière.","HUG EGS 2010."),
  (1,"Le Mini-Cog associe le rappel de 3 mots et le dessin d'une horloge.","Borson 2000."),
  (0,"Une personne dont la mémoire faiblit qui affirme ne jamais rien oublier est un témoin fiable de ses prises.","Faux : on confronte son récit à la pharmacie et à un proche.")),
 "n":n("aivq","cog","pharm","bag"),"a":"direct","d":3,"l":("Capacité de gestion.","Autonomie instrumentale.","AIVQ, semainier.","Mini-Cog.","Évaluer.","Se fier au récit.","Récit + pharmacie + proche.")},
{"f":"Kprim","m":0,"st":"Vous faites la revue de médication d'une personne âgée polymédiquée selon la stratégie des HUG.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"On répertorie aussi l'automédication et la phytothérapie.","HUG EGS 2010."),
  (1,"On refait la revue si possible à chaque consultation et au moins tous les 6 mois.","HUG EGS 2010."),
  (1,"On évite deux médicaments qui ont le même but, comme deux benzodiazépines.","HUG EGS 2010."),
  (0,"On peut garder plusieurs anticholinergiques sans risque cognitif chez la personne âgée.","Faux : on minimise ou évite les anticholinergiques (HUG, Beers 2023).")),
 "n":n("bag","surv","revue","depr"),"a":"direct","d":3,"l":("Revue de médication.","Doublons et anticholinergiques.","Tout répertorier.","Tous les 6 mois.","Revoir.","Anticholinergiques sans risque.","Tout lister, au moins tous les 6 mois.")},
{"f":"Kprim","m":0,"st":"Vous évaluez les risques d'une personne âgée qui prend mal ses médicaments à marge étroite.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"Une sulfonylurée à longue action expose davantage à une hypoglycémie prolongée qu'une sulfonylurée à courte action.","Beers 2023."),
  (1,"L'association de 3 médicaments actifs sur le système nerveux central ou plus (benzodiazépines, opioïdes, antidépresseurs…) augmente le risque de chute et de fracture.","Beers 2023."),
  (1,"La toxicité médicamenteuse intervient dans environ 30 % des états confusionnels aigus.","CAPP-INFO 66."),
  (0,"Une hypoglycémie due à une sulfonylurée se règle toujours définitivement par un seul resucrage.","Faux : elle peut être prolongée et récidiver, ce qui impose une surveillance.")),
 "n":n("dbl","hosp","acute","desq"),"a":"piège","d":3,"l":("Risques.","Marge étroite.","Hypoglycémie, chute, confusion.","Surveiller.","Prévenir.","Resucrage unique.","Sulfonylurée = hypoglycémie prolongée.")},
{"f":"Kprim","st":"Un homme de 85 ans vit seul. Son INR oscille entre 1,3 et 5,8 depuis 3 mois sans changement de dose de phenprocoumone. La pharmacie signale qu'il n'est pas venu chercher ses comprimés pendant deux mois, puis qu'il en a pris deux boîtes d'un coup. Il ne sait plus le nom de ses comprimés.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"Un test cognitif rapide fait partie du bilan.","Borson 2000."),
  (1,"On compare son récit avec les délivrances de la pharmacie et l'avis d'un proche.","CAPP-INFO 66."),
  (1,"On confie la préparation et le contrôle de ses prises à un tiers.","Avis d'expert."),
  (0,"On augmente la dose de phenprocoumone, puisque l'INR est souvent bas.","Faux : l'INR varie avec la prise réelle ; augmenter la dose expose à l'hémorragie quand il prend tout.")),
 "n":n("pos","pharm","cog","simp","barr"),"a":"application","d":4,"l":("Vit seul, INR instable.","Prises désordonnées.","Retraits discordants.","Tester, objectiver, déléguer.","Sécuriser.","Augmenter la dose.","INR instable sans changement = vérifier la prise.")},
{"f":"MenuLong","st":"Une femme de 82 ans, qui vit seule, sort de l'hôpital après une hypoglycémie sévère. Elle prend 9 médicaments en quatre prises par jour, dont du glibenclamide (Melix). Elle ne se souvient plus de la dernière visite de son médecin.",
 "p":"Choisissez les TROIS mesures les plus utiles avant son retour à domicile.","o":A(
  (1,"Évaluer sa cognition et sa capacité à gérer seule ses médicaments","HUG EGS 2010."),
  (1,"Arrêter le glibenclamide et réduire le nombre de prises","Beers 2023 ; HUG EGS 2010."),
  (1,"Organiser un semainier préparé par la pharmacie et des passages des soins à domicile","Structure LOA V (à vérifier) ; Smith, Rev Med Suisse 2014."),
  (0,"Ajouter une insuline rapide selon la glycémie","Faux : Beers 2023 la déconseille seule, à cause du risque d'hypoglycémie."),
  (0,"Lui remettre une liste plus détaillée de ses 9 médicaments","Faux : une liste ne corrige ni la complexité ni la préparation des doses."),
  (0,"Remplacer le glibenclamide par du glimépiride","Faux : le glimépiride est aussi une sulfonylurée à longue action."),
  (0,"Faire une IRM cérébrale avant tout","Faux : on dépiste d'abord par un test cognitif."),
  (0,"Ajouter un hypnotique pour qu'elle dorme mieux à domicile","Faux : un sédatif augmente le risque de chute et de confusion."),
  (0,"Lui interdire de vivre seule","Faux : les ressources à domicile permettent souvent le maintien, et la décision se prend avec elle."),
  (0,"Doubler la metformine pour compenser l'arrêt","Faux : on fixe une cible prudente et un schéma simple, sans intensifier d'emblée."),
  (0,"Lui demander de tenir seule un carnet de ses prises","Faux : un carnet tenu seul ne protège pas une personne qui ne se souvient plus de ses prises."),
  (0,"Lui conseiller de doubler la dose suivante quand elle a manqué une prise","Faux : doubler une sulfonylurée expose à une nouvelle hypoglycémie.")),
 "n":n("simp","revue","net","dbl","hosp","epi"),"a":"application","d":4,"l":("Hypoglycémie, vit seule, 4 prises.","Sulfonylurée et schéma complexe.","Ne se souvient pas.","Évaluer, simplifier, déléguer.","Sécuriser la sortie.","Ajouter, lister.","Sortie = évaluer, simplifier, préparer.")},
{"f":"MenuLong","m":0,"st":"Une femme de 83 ans avec une démence modérée prend 12 médicaments.",
 "p":"Choisissez les TROIS médicaments que les critères de Beers 2023 demandent d'éviter chez elle.","o":A(
  (1,"Lorazépam","Beers 2023 : benzodiazépine à éviter en cas de démence."),
  (1,"Zolpidem","Beers 2023 : hypnotique en Z à éviter en cas de démence."),
  (1,"Amitriptyline","Beers 2023 : antidépresseur fortement anticholinergique à éviter en cas de démence."),
  (0,"Paracétamol","Faux : il ne figure pas parmi les médicaments à éviter en cas de démence."),
  (0,"Colécalciférol","Faux : il ne figure pas parmi les médicaments à éviter."),
  (0,"Lévothyroxine","Faux : Beers vise la thyroïde desséchée, pas la lévothyroxine."),
  (0,"Amlodipine","Faux : elle ne figure pas parmi les médicaments à éviter en cas de démence."),
  (0,"Metformine","Faux : Beers vise les sulfonylurées, pas la metformine."),
  (0,"Apixaban à dose adaptée","Faux : Beers 2023 ne l'exclut pas ; il signale même plus d'hémorragies sous rivaroxaban que sous les autres anticoagulants oraux directs, en particulier l'apixaban."),
  (0,"Ramipril","Faux : il ne figure pas parmi les médicaments à éviter en cas de démence."),
  (0,"Latanoprost en collyre","Faux : il ne figure pas parmi les médicaments à éviter."),
  (0,"Macrogol","Faux : il ne figure pas parmi les médicaments à éviter.")),
 "n":n("beers","depr","achb"),"a":"direct","d":3,"l":("Démence, 12 médicaments.","Effets sur le système nerveux.","Benzodiazépine, Z, anticholinergique.","Beers tableau 3.","Déprescrire.","Médicaments neutres.","Démence : pas de sédatif ni d'anticholinergique.")},
]
for _q in Q: _q["src"] = EGS
for i, s in ((0,[EGS,C66,ELS]),(1,[BEE,DIA,EGS]),(2,[LOA,SMI,EGS,CAM]),(3,[GIL,BEE,VES,ARI]),(4,[C66,BEE,ATA]),(5,[ELI,EGS,EXP]),(6,[SMI,EGS,EXP]),(7,[SMI,ELS,EGS]),(9,[MOC,PCV]),(10,[STO,BEE]),(11,[ARI]),(12,[SMI,EGS,CAM,BEE]),(13,[BEE,C67,C66]),(14,[EGS,MCG,C66]),(15,[EGS,BEE]),(16,[BEE,C66]),(17,[MCG,C66,MAR,EXP]),(18,[EGS,BEE,LOA,MEL]),(19,[BEE])): Q[i]["src"] = s
C = {"theme":"Oublis de médicaments du sujet âgé liés à la polymédication ou aux troubles cognitifs (porte O7.15) : indices concordants (boîtes pleines ou finies trop tôt, retraits espacés, déséquilibre inexpliqué), dépistage cognitif (Mini-Cog, MoCA sous 26/30, test de l'horloge), capacité à gérer seul son traitement, confusion aiguë à distinguer, revue structurée (STOPP/START v3, Beers 2023, charge anticholinergique, cascade), risques des médicaments à marge étroite (sulfonylurées, anticoagulants), simplification, semainier LOA V, soins à domicile et proches aidants",
 "notions":[
  {"titre":"Comprendre","rub":["definition","epidemiology","basicSciences","prognosisDischarge"],"comment":"Les oublis du sujet âgé sont surtout non voulus et naissent de la charge thérapeutique et des déficits cognitifs, visuels ou manuels.",
   "points":["Polymédication : 5 médicaments ou plus ; risques en forte hausse au-delà de 3.","Démence : prise conforme de 17 à 42 % seulement.","Exposition cumulée aux anticholinergiques : risque accru de démence."],"sources":[SMI,EGS,ELS,COU]},
  {"titre":"Reconnaître","rub":["anamnesis","clinicalExam","presumptionRedFlags","positiveDiagnosis"],"comment":"On objective la prise réelle et l'on dépiste la cause cognitive, en écartant une confusion aiguë.",
   "arbre":[("d1",None,"Déséquilibre inexpliqué ou boîtes discordantes","On fait apporter les boîtes et l'on interroge la pharmacie et un proche.",None,None),("d2","d1","Début aigu et fluctuant","On cherche la cause de la confusion avant tout test cognitif.",None,None),("d3","d1","Tableau stable","On fait un Mini-Cog, une MoCA ou un test de l'horloge et l'on évalue les AIVQ.",None,None),("d4","d1","Boîte finie trop tôt d'un médicament à marge étroite","On recherche une hypoglycémie ou un saignement.",None,None)],
   "points":["MoCA anormale sous 26/30.","Horloge sur 10 points : cadran 2, chiffres 4, aiguilles 4."],"sources":[EGS,C66,MCG,MOC]},
  {"titre":"Décider","rub":["workupGoldStandard","workupAlternatives","acuteManagement","chronicManagement"],"comment":"On revoit tout le traitement, on sécurise les médicaments dangereux, puis l'on simplifie et l'on délègue la préparation.",
   "tab":(["Situation","Conduite","Remarque"],[["Sulfonylurée et prises incontrôlées","Arrêt ou réduction",[("Beers 2023","Éviter les sulfonylurées ; longue action plus dangereuse.")]],["Apixaban dans la FA","5 mg 2×/j ; 2,5 mg 2×/j si 2 critères",[("Brevier","> 80 ans, ≤ 60 kg, créatinine ≥ 133 µmol/l ; posologies à vérifier dans l'AIPS (Swissmedic).")]],["Anticholinergiques, benzodiazépines, Z","Déprescription progressive",[("Beers 2023","À éviter en cas de démence.")]],["Incontinence sous donépézil","Ne pas ajouter d'antimuscarinique",[("Gill 2005","Cascade médicamenteuse.")]]]),
   "points":["STOPP/START v3 : 190 critères, alertes à interpréter.","Semainier préparé par un tiers, rappels humains."],"sources":[BEE,STO,ELI,GIL]},
  {"titre":"Suivre","rub":["hospitalizationComplications","surveillance","followUpNetwork"],"comment":"On prévient les hospitalisations iatrogènes et l'on organise le réseau autour de la personne et de son proche aidant.",
   "points":["Revue au moins tous les 6 mois et à chaque sortie d'hôpital.","Donépézil : évaluation tous les 6 mois, arrêt sous un MMSE de 10 (LS).","Semainier LOA V, centre médico-social, consultation pour proches aidants (à vérifier)."],"sources":[EGS,ARI,SMI,LOA]}],
 "ssp":("O7.15","Mauvaise adhésion au traitement",True,[
   ("n1",None,"Déséquilibre inexpliqué ou boîtes discordantes chez la personne âgée","On fait apporter toutes les boîtes et l'on interroge la pharmacie et un proche.","securiser","c2"),
   ("n2","n1","Confusion aiguë et fluctuante","On cherche la cause et l'on arrête le médicament suspect.","securiser","c2"),
   ("n3","n1","Boîte finie trop tôt d'un médicament à marge étroite","On recherche une hypoglycémie ou un saignement et l'on adapte la dose.","securiser","c3"),
   ("n4","n1","Tableau stable avec plainte de l'entourage","On dépiste par Mini-Cog, MoCA ou test de l'horloge et l'on évalue les AIVQ.","securiser","c2"),
   ("n5","n4","Capacité de gestion insuffisante","On simplifie, on déprescrit et l'on fait préparer un semainier par un tiers.","securiser","c3"),
   ("n6","n5","Maintien à domicile","On coordonne soins à domicile, pharmacie et proche aidant et l'on revoit tous les 6 mois.","securiser","c4")]),
 "pec":[
  pec("securiser","Oublis de médicaments du sujet âgé",["On rend la prise des médicaments sûre et conforme au plan convenu.","On réduit la charge thérapeutique et les médicaments inappropriés."],
      ["On reçoit la personne avec son proche et toutes ses boîtes.","On parle sans jugement des difficultés de prise."],
      [("Gliclazide (Diamicron MR)","Chez la personne âgée qui ne gère plus ses doses, on réduit ou l'on arrête ; si on le garde : 30 mg au petit déjeuner, augmentation au plus toutes les 2 semaines, maximum 120 mg par jour, contre-indiqué en cas d'insuffisance rénale sévère (Brevier) ; posologies à vérifier dans l'AIPS (Swissmedic)","Une sulfonylurée expose la personne âgée à des hypoglycémies parfois prolongées.",DIA),
       ("Apixaban (Eliquis)","Fibrillation auriculaire : 5 mg deux fois par jour ; 2,5 mg deux fois par jour si deux critères parmi âge de plus de 80 ans, poids de 60 kg ou moins, créatinine de 133 µmol/l ou plus (Brevier) ; posologies à vérifier dans l'AIPS (Swissmedic)","On ajuste la dose pour limiter le risque hémorragique quand la prise est sécurisée.",ELI),
       ("Donépézil (Aricept)","5 mg le soir pendant au moins 1 mois, puis au plus 10 mg par jour ; LS : évaluation cognitive au début et tous les 6 mois, arrêt sous un MMSE de 10 (Brevier) ; posologies à vérifier dans l'AIPS (Swissmedic)","Il traite les symptômes d'une maladie d'Alzheimer légère à modérée, sans dispenser d'organiser la prise.",ARI)],
      [("soins infirmiers","On fait préparer le semainier et contrôler les prises par la pharmacie ou les soins à domicile.","On évite les prises en double et les oublis chez la personne qui ne planifie plus."),("éducation thérapeutique","On note sur une carte de traitement le but de chaque médicament.","On aide la personne et son proche à reconnaître chaque comprimé."),("social et assurances","On oriente le proche aidant vers une consultation de soutien et l'on évalue les aides financières.","On prévient l'épuisement de l'aidant et l'on soutient le maintien à domicile.")],
      [("O Pharmacologie Toxicologie Sécurité","On revoit les médicaments à marge étroite, les doublons et la charge anticholinergique."),("C Communication clinique","On associe la personne et son proche aux décisions sans les juger.")],
      (["On évalue la gravité.","On sécurise le médicament en cause.","On organise la prise par un tiers."],[("d'abord","médecin de famille","Il mesure la glycémie ou recherche un saignement après une prise en double probable."),("en même temps","pharmacien","Il retrace les délivrances et signale les retraits discordants."),("puis","soins à domicile","Ils reprennent la préparation et le contrôle des prises dès le retour à domicile.")]),
      (["On objective la prise.","On simplifie.","On délègue et l'on revoit."],[("d'abord","médecin de famille","Il fait la revue de tous les médicaments et un test cognitif rapide."),("ensuite","pharmacien","Il prépare le semainier sur prescription et signale les écarts."),("puis","soins à domicile","Ils contrôlent les prises et informent le médecin et le proche aidant.")]),
      "Une prise sécurisée et un traitement allégé réduisent les effets indésirables graves et soutiennent le maintien à domicile ; un déclin cognitif impose d'adapter l'aide au fil du temps.",
      [("Liste des médicaments","Au moins tous les 6 mois et à chaque sortie d'hôpital","Liste à jour, sans doublon ni anticholinergique évitable"),("Semainier","Chaque semaine","Cases vidées comme prévu")],"La personne repart avec un traitement simplifié, un semainier préparé par un tiers et un réseau informé.",
      ("On évite de prescrire des anticholinergiques et des sédatifs chez la personne âgée.","On dépiste un trouble cognitif devant tout déséquilibre inexpliqué.","On revoit régulièrement le traitement pour prévenir chutes, hémorragies et hypoglycémies.")),]}
