from constructeur_agent_45spec import pec
ID = "R76.1__O7_13-E05"
PLAN = "non_monographique"
MAN = "[Ligue pulmonaire suisse et OFSP, Tuberculose en Suisse – Guide à l'usage des professionnels de la santé, V1.2024 (chapitres 3, 4, 5, 7 à 11), lu le 28.11.2026]"
OFSP = "[OFSP, page « Tuberculose » (transmission, 5 à 10 % de malades, BCG non disponible, Centre de compétence tuberculose), lue le 28.11.2026]"
BUL = "[OFSP, Bulletin « La tuberculose en Suisse et dans la Principauté de Liechtenstein en 2025 » (2026), nombre de cas, taux et origine, lu le 28.11.2026]"
SEM = "[OFSP, Information aux médecins traitant la tuberculose dans le domaine de l'asile (13.11.2018), accord OFSP–SEM et rapport médical, lue le 28.11.2026]"
OMS = "[OMS, WHO consolidated guidelines on tuberculosis, Module 1: Prevention – Tuberculosis preventive treatment, 2e édition (2024), recommandations 1 à 21, lues le 28.11.2026]"
CDC = "[Sterling TR et al., Guidelines for the Treatment of Latent Tuberculosis Infection: NTCA and CDC, 2020, MMWR Recomm Rep (2020), PMID 32053584, résumé lu le 28.11.2026]"
INT = "[OFSP, page « Interprétariat communautaire » (rôle et financement cantonal), lue le 28.11.2026]"
RIM = "[Compendium.ch, résumé (Brevier) de Rimactan 150 mg (rifampicine), indication, posologie et contre-indications, lu le 28.11.2026 ; AIPS complète à vérifier]"
RIF = "[Compendium.ch, résumé (Brevier) de Rifinah 150/100 mg (rifampicine et isoniazide), posologie et contre-indications, lu le 28.11.2026 ; AIPS complète à vérifier]"
INH = "[Compendium.ch, résumé (Brevier) d'Isoniaz-TB 100 mg (isoniazide), prophylaxie, pyridoxine et contre-indications, lu le 28.11.2026 ; AIPS complète à vérifier]"
HUM = "[Compendium.ch, résumé (Brevier) de Humira (adalimumab), contre-indications, lu le 28.11.2026 ; AIPS complète à vérifier]"
EXP = "Avis d'expert (à vérifier)"
_N = [
("def","definition","critère",1,0,OMS+" ; "+MAN,"L'infection tuberculeuse est une réponse immunitaire persistante aux antigènes de M. tuberculosis sans maladie clinique ; un test positif mesure une empreinte immunologique, sans prouver la présence de bacilles vivants, et ni le test cutané ni l'IGRA ne distinguent l'infection de la maladie."),
("risk","epidemiology","chiffre",2,0,OFSP+" ; "+MAN,"Cinq à dix pour cent des personnes infectées tombent malades au cours de leur vie, surtout dans les deux ans qui suivent l'infection ; chez les migrants, les cas qui surviennent après l'arrivée sont jusqu'à dix fois plus nombreux que ceux trouvés à l'arrivée, surtout chez les jeunes enfants et les 15–24 ans."),
("epich","epidemiology","contexte suisse",1,1,BUL,"En 2025, la Suisse a déclaré 544 cas de tuberculose (6,0 pour 100 000 habitants) ; la hausse concerne presque exclusivement les personnes nées à l'étranger, surtout d'Érythrée, de Somalie et d'Afghanistan."),
("immuno","basicSciences","mécanisme",1,0,MAN,"Le test cutané mesure l'accumulation in vivo de lymphocytes T mémoire autour de la tuberculine ; l'IGRA mesure la libération in vitro d'interféron gamma au contact de peptides du complexe M. tuberculosis, absents de M. bovis BCG."),
("progr","basicSciences","terrain particulier",1,0,MAN,"Le risque de progression rapide est élevé chez l'enfant de moins de 2 ans et chez l'immunodéprimé (VIH, anti-TNF) ; il est modérément accru en cas de diabète, d'insuffisance rénale ou de silicose."),
("qui","anamnesis","décision",3,1,MAN+" ; "+OMS,"On ne teste que si l'on prévoit de traiter un résultat positif : contacts récents d'un cas contagieux, personnes immunodéprimées (bilan initial du VIH, avant un anti-TNF ou une greffe) et professionnels exposés (test de référence) ; un dépistage non ciblé n'est pas recommandé, en raison de sa faible valeur prédictive."),
("migr","anamnesis","contexte suisse",2,1,MAN,"Chez les migrants, le dépistage de l'infection reste controversé : on ne l'envisage que chez de jeunes migrants venus de régions à très forte incidence (par exemple plus de 100 pour 100 000 par an), dans un cadre stable où l'observance est probable, en tenant compte du parcours migratoire (logements surpeuplés, détention), des contacts et des comorbidités."),
("interp","anamnesis","piège",1,1,MAN+" ; "+INT,"Un migrant peut ne pas distinguer toux et crachats ou taire une toux jugée impolie : on interroge avec un interprète communautaire professionnel, qui traduit complètement et fidèlement, tenu au secret et à la neutralité."),
("exam","clinicalExam","signe",1,0,MAN,"Aucun signe n'est pathognomonique : l'examen clinique après l'entretien recherche un amaigrissement ou des adénopathies que le seul questionnaire aurait manqués."),
("sympt","presumptionRedFlags","signe",3,0,OMS+" ; "+MAN,"Avant tout traitement préventif, on exclut une tuberculose active : toux, fièvre, perte de poids ou sueurs nocturnes imposent un bilan de maladie ; l'absence de tout symptôme et une radiographie thoracique sans anomalie permettent de l'exclure chez un adulte non infecté par le VIH."),
("xray","workupGoldStandard","examen",3,0,MAN,"Après un test positif, on fait l'anamnèse des symptômes, l'examen clinique et une radiographie thoracique ; une anomalie compatible impose des échantillons respiratoires (PCR, microscopie, culture), car la radiographie ne distingue pas une lésion active d'une cicatrice."),
("igra","workupAlternatives","examen",2,0,MAN+" ; "+OMS,"L'IGRA a une sensibilité comparable au test cutané mais une spécificité plus grande, car il n'est pas influencé par le BCG ; le test cutané reste préférable chez le jeune enfant non vacciné, et les deux tests ensemble ne se font que chez le jeune enfant."),
("tct","workupAlternatives","seuil",1,0,MAN,"Le test cutané injecte par voie intradermique 0,1 ml de tuberculine PPD RT23 (2 unités) ; on mesure à 48–72 heures le diamètre transverse de l'induration, sans tenir compte de l'érythème ; chez un contact, 5 mm et plus sont positifs ; la tuberculine manque souvent en Suisse."),
("immsup","positiveDiagnosis","piège",2,0,MAN,"L'immunosuppression rend les tests faussement négatifs et l'IGRA indéterminé : un contact immunodéprimé à forte probabilité d'infection dont le résultat est indéterminé se traite comme infecté."),
("bcg","positiveDiagnosis","piège",1,1,MAN+" ; "+OFSP,"Le BCG n'est plus recommandé aux résidents permanents de Suisse ni disponible en Suisse ; il ne se discute que pour un nourrisson de moins de 12 mois qui vivra durablement dans un pays à plus de 50 cas pour 100 000 ; un test cutané positif chez une personne vaccinée peut refléter le BCG, d'où l'intérêt de l'IGRA."),
("regimes","acuteManagement","décision",3,1,MAN,"Le guide suisse propose trois schémas d'efficacité égale : isoniazide chaque jour pendant 6 (ou 9) mois, rifampicine chaque jour pendant 4 mois, ou isoniazide et rifampicine chaque jour pendant 3 mois ; la rifapentine n'est ni homologuée ni disponible en Suisse."),
("doses","acuteManagement","posologie",2,1,MAN+" ; "+RIM+" ; "+INH+" ; "+RIF,"Rimactan : 10 (8–12) mg/kg une fois par jour, au plus 600 mg, à jeun au moins 30 minutes avant le repas ; Isoniaz-TB : 5 mg/kg une fois par jour, au plus 300 mg, avec 10 à 20 mg de pyridoxine par jour contre la neuropathie ; Rifinah 150/100 mg : 4 comprimés par jour au-delà de 50 kg ; le Brevier d'Isoniaz-TB indique 9 mois de prophylaxie, le guide 6 (ou 9) mois (posologies à vérifier dans l'AIPS (Swissmedic))."),
("hiv","acuteManagement","terrain particulier",1,0,OMS+" ; "+MAN+" ; "+RIM,"Une personne vivant avec le VIH reçoit un traitement préventif même sous traitement antirétroviral et quel que soit son degré d'immunosuppression ; la rifampicine est contre-indiquée avec les inhibiteurs de protéase et les inhibiteurs non nucléosidiques de la transcriptase inverse : on choisit le schéma avec un spécialiste."),
("who","chronicManagement","décision",1,0,OMS+" ; "+CDC,"L'OMS 2024 recommande l'isoniazide 6 ou 9 mois, la rifapentine et l'isoniazide hebdomadaires 3 mois ou l'isoniazide et la rifampicine 3 mois, et place la rifampicine 4 mois parmi les alternatives ; le CDC 2020 préfère les schémas courts à base de rifamycine, l'isoniazide seul étant plus toxique et moins souvent mené à terme ; discordance avec le guide suisse, qui juge les trois schémas d'efficacité égale."),
("inter","chronicManagement","molécule",2,0,MAN+" ; "+RIM,"La rifampicine, inductrice enzymatique, réduit l'effet des contraceptifs oraux, des opiacés, des antiépileptiques et des glucocorticoïdes : la contraception hormonale est inefficace pendant le traitement et jusqu'à un mois après ; l'isoniazide élève le taux de la plupart des antiépileptiques et interagit avec l'acénocoumarol ; on vérifie chaque médicament par un logiciel d'interactions."),
("preg","chronicManagement","terrain particulier",1,0,MAN+" ; "+RIF,"La grossesse n'est pas une contre-indication au traitement préventif selon le guide suisse (aucun effet tératogène de l'isoniazide ni de la rifampicine, risque un peu plus élevé en péri-partum) et l'allaitement est compatible, avec de la vitamine B6 pour la mère et le nouveau-né sous isoniazide ; le Brevier de Rifinah range grossesse et allaitement parmi les contre-indications : discordance à vérifier dans l'AIPS."),
("hepat","hospitalizationComplications","complication",1,0,MAN,"Une hépatite médicamenteuse se suspecte devant des symptômes avec une ALAT d'au moins 3 fois la normale, ou d'au moins 5 fois sans symptôme : on arrête les médicaments hépatotoxiques jusqu'à normalisation et l'on demande l'avis d'un spécialiste (seuils donnés pour le traitement de la tuberculose, à vérifier pour le traitement préventif)."),
("antitnf","hospitalizationComplications","complication",1,0,MAN+" ; "+OMS+" ; "+HUM,"Un anti-TNF expose à une progression rapide vers la tuberculose : on recherche et traite l'infection avant de le commencer, et l'adalimumab est contre-indiqué en cas de tuberculose active."),
("liver","surveillance","décision",2,0,MAN,"On revoit régulièrement la tolérance et l'observance ; des tests hépatiques initiaux se discutent, surtout avant l'association isoniazide et rifampicine ; s'ils sont normaux, on ne les répète chaque mois qu'en cas d'hépatopathie, de consommation régulière d'alcool ou d'autre médicament hépatotoxique ; le risque hépatique est plus faible avec la rifampicine."),
("prono","prognosisDischarge","pronostic",1,0,MAN,"Un traitement préventif bien suivi réduit jusqu'à 90 % le risque de tuberculose ; la très grande majorité des personnes positives n'évolueront pourtant jamais vers la maladie."),
("decl","followUpNetwork","contexte suisse",2,1,MAN,"Le médecin déclare au médecin cantonal, dans la semaine, toute tuberculose traitée par au moins trois médicaments ou à culture positive (le laboratoire déclare en 24 heures) ; les traitements de l'infection par M. tuberculosis ne se déclarent pas."),
("asile","followUpNetwork","contexte suisse",2,1,MAN+" ; "+SEM,"Dans les centres fédéraux, le dépistage se fait par entretien dans les 72 heures (radiographie systématique abandonnée en 2006), sans IGRA systématique ; l'accord OFSP–SEM (rapport médical au SEM) fait mener à terme en Suisse le traitement d'une tuberculose, mais pas celui d'une infection latente, qui ne peut jamais empêcher un renvoi."),
("couts","followUpNetwork","contexte suisse",1,1,MAN+" ; "+INT,"L'assurance-maladie ne paie pas le dépistage de l'infection chez les migrants (accord préalable avec le canton) ; après un test positif, elle couvre le bilan et le traitement avec franchise et quote-part, sans dispense ; le canton paie les enquêtes d'entourage qu'il ordonne, la personne qui demande un test de son propre chef le paie, et le financement de l'interprétariat varie selon les cantons."),
]
K = {k: i+1 for i, (k, *_r) in enumerate(_N)}
N = [t[1:] for t in _N]
n = lambda *ks: [K[k] for k in ks]
AM = ["Tester seulement si l'on prévoit de traiter : dépistage ciblé, jamais général.","Exclure une tuberculose active (symptômes, radiographie, expectorations si anomalie) avant tout traitement préventif.","IGRA non influencé par le BCG ; immunodéprimé indéterminé = traiter comme infecté.","Rifampicine 4 mois (max. 600 mg/j, à jeun) : contraception hormonale inefficace jusqu'à 1 mois après ; contre-indiquée avec les inhibiteurs de protéase du VIH.","Pas de tests hépatiques mensuels si bilan normal, sauf foie malade, alcool ou autre hépatotoxique.","L'infection latente ne se déclare pas et ne suspend pas un renvoi ; le dépistage des migrants n'est pas payé par la LAMal."]
A = lambda *o: list(o)
Q = [
{"f":"A","s":("S1",1,3),"st":"Un homme de 24 ans, arrivé d'Érythrée il y a 8 mois, vit dans un appartement attribué par le canton à Lausanne et suit un cours de français. Dans le cadre d'un programme cantonal ciblé, son test sanguin de libération d'interféron gamma revient positif ; il se dit en bonne santé.",
 "p":"Que faites-vous d'abord ?","o":A(
 (1,"Vous recherchez les symptômes avec un interprète professionnel, l'examinez et demandez une radiographie thoracique avant de décider d'un traitement","Guide suisse 2024 et OMS 2024 : la maladie active s'exclut avant tout traitement préventif."),
 (0,"Vous débutez d'emblée 4 mois de rifampicine","Faux : aucun traitement préventif avant d'avoir exclu une maladie active par l'anamnèse, l'examen et la radiographie."),
 (0,"Vous répétez le test sanguin dans 2 mois pour le confirmer","Faux : un second test n'apporte rien ; c'est le bilan de maladie active qui décide de la suite."),
 (0,"Vous demandez un test cutané de confirmation","Faux : le test cutané, moins spécifique que l'IGRA, ne confirme pas un IGRA positif ; c'est le bilan de maladie active qui décide de la suite."),
 (0,"Vous déclarez le cas au médecin cantonal","Faux : un résultat positif sans maladie ne se déclare pas.")),
 "n":n("sympt","xray","exam","migr","interp"),"a":"application","d":4,"l":("Jeune migrant récent, test positif.","Infection possible, maladie à exclure.","Aucune plainte spontanée.","Symptômes, examen, radiographie.","Exclure avant de traiter.","Traiter d'emblée.","Test positif = d'abord exclure la maladie.")},
{"f":"A","s":("S1",2,3),"st":"Avec l'interprète, il précise qu'il crache un peu chaque matin depuis un mois, sans se considérer comme quelqu'un qui tousse. Il n'a pas de fièvre. La radiographie montre une petite opacité nodulaire apicale droite, sans caverne.",
 "p":"Quelle est la suite ?","o":A(
 (1,"Vous faites analyser des échantillons respiratoires par PCR, microscopie et culture avant tout traitement","Guide suisse 2024 : une anomalie radiologique compatible impose un examen microbiologique, car la radiographie ne distingue pas lésion active et cicatrice."),
 (0,"Vous concluez à une cicatrice ancienne et débutez 4 mois de rifampicine","Piège : une opacité ne passe pour une cicatrice qu'après des échantillons négatifs par PCR, microscopie et culture."),
 (0,"Vous débutez 9 mois d'isoniazide","Faux : une monothérapie se donne seulement après exclusion d'une maladie active."),
 (0,"Vous refaites une radiographie dans 6 mois","Faux : des crachats avec une opacité apicale demandent un bilan rapide, pas une attente."),
 (0,"Vous demandez seulement une tomodensitométrie thoracique","Faux : l'imagerie seule ne dit pas si la lésion est active ; la microbiologie tranche.")),
 "n":n("xray","sympt","interp"),"a":"piège","d":5,"l":("Crachats matinaux et opacité apicale.","Lésion peut-être active.","Symptôme sous-déclaré.","Microbiologie avant traitement.","Prélever.","Cicatrice supposée.","Opacité + crachats = prélever.")},
{"f":"A","m":0,"s":("S1",3,3),"st":"Les échantillons respiratoires sont négatifs par PCR, microscopie et culture ; vous retenez une infection tuberculeuse latente. Il pèse 62 kg, ne boit pas d'alcool, ne prend aucun médicament et ses tests hépatiques initiaux sont normaux.",
 "p":"Que proposez-vous ?","o":A(
 (1,"De la rifampicine (Rimactan) 600 mg une fois par jour, à jeun au moins 30 minutes avant le repas, pendant 4 mois, avec des contrôles cliniques réguliers et sans tests hépatiques mensuels systématiques","Guide suisse 2024 ; Brevier Rimactan : 10 mg/kg, au plus 600 mg (posologies à vérifier dans l'AIPS (Swissmedic))."),
 (0,"De la rifampicine 600 mg chaque matin avec un petit-déjeuner riche en graisses pour mieux la tolérer","Faux : les repas gras réduisent fortement l'absorption de la rifampicine."),
 (0,"De la rifapentine et de l'isoniazide une fois par semaine pendant 12 semaines","Faux : la rifapentine n'est ni homologuée ni disponible en Suisse."),
 (0,"De la rifampicine 900 mg par jour pendant 2 mois","Faux : la dose maximale est de 600 mg par jour et la durée du schéma est de 4 mois."),
 (0,"Une association de quatre antituberculeux pendant 2 mois","Faux : une quadrithérapie traite la maladie active, exclue ici.")),
 "n":n("regimes","doses","liver"),"a":"application","d":3,"l":("Infection sans maladie.","Bacilles quiescents.","Bilan négatif.","Schéma court.","Rifampicine 4 mois.","Repas gras, rifapentine.","10 mg/kg, max. 600 mg, à jeun.")},
{"f":"A","st":"Une femme de 29 ans, arrivée de Somalie il y a 3 ans, doit commencer de l'adalimumab pour une maladie de Crohn. Son test sanguin de libération d'interféron gamma est positif, sa radiographie thoracique est normale et elle n'a aucun symptôme. Vous lui proposez 4 mois de rifampicine. Elle prend une pilule œstroprogestative et ne souhaite pas de grossesse.",
 "p":"Que lui conseillez-vous ?","o":A(
 (1,"Une contraception non hormonale pendant tout le traitement et jusqu'à un mois après, car la rifampicine rend la contraception hormonale inefficace","Guide suisse 2024, interactions de la rifampicine."),
 (0,"Garder sa pilule seule, sans autre précaution","Faux : l'induction enzymatique par la rifampicine rend la pilule inefficace."),
 (0,"Prendre deux comprimés de pilule par jour","Faux : le guide suisse tient la contraception hormonale pour inefficace sous rifampicine ; on passe à une méthode non hormonale."),
 (0,"Reprendre sa pilule seule dès la fin du traitement","Faux : l'effet inducteur persiste ; la contraception hormonale reste inefficace jusqu'à un mois après."),
 (0,"Commencer l'adalimumab sans traitement préventif","Faux : on traite l'infection avant un anti-TNF, qui expose à une progression rapide vers la maladie.")),
 "n":n("inter","antitnf"),"a":"application","d":4,"l":("Anti-TNF prévu, test positif.","Induction enzymatique.","Pilule en cours.","Contraception non hormonale.","Protéger la contraception.","Pilule seule.","Rifampicine = pilule inefficace jusqu'à 1 mois après.")},
{"f":"A","st":"Un homme de 34 ans, arrivé d'Afghanistan il y a un an, vit avec le VIH ; il prend du darunavir boosté par le ritonavir avec deux analogues nucléosidiques et sa charge virale est indétectable. Son test sanguin de libération d'interféron gamma est positif ; il n'a ni toux, ni fièvre, ni perte de poids, ni sueurs nocturnes, et sa radiographie thoracique est normale.",
 "p":"Quelle prise en charge proposez-vous ?","o":A(
 (1,"De l'isoniazide 5 mg/kg par jour (300 mg au plus) avec de la pyridoxine pendant 6 à 9 mois, en vérifiant les interactions avec son infectiologue","Brevier Rimactan : rifampicine contre-indiquée avec les inhibiteurs de protéase du VIH ; Brevier Isoniaz-TB ; guide suisse 2024 (posologies à vérifier dans l'AIPS (Swissmedic))."),
 (0,"De la rifampicine pendant 4 mois sans changer son traitement antirétroviral","Piège : la rifampicine est contre-indiquée avec les inhibiteurs de protéase du VIH."),
 (0,"Rifinah (isoniazide et rifampicine) pendant 3 mois","Faux : Rifinah contient de la rifampicine, qui pose le même problème d'interaction."),
 (0,"Aucun traitement préventif, car il reçoit déjà un traitement antirétroviral efficace","Faux : l'OMS recommande le traitement préventif aussi sous traitement antirétroviral."),
 (0,"De la rifapentine et de l'isoniazide hebdomadaires pendant 12 semaines","Faux : la rifapentine n'est pas disponible en Suisse.")),
 "n":n("hiv","inter","doses","regimes"),"a":"piège","d":5,"l":("VIH sous inhibiteur de protéase, test positif.","Induction du CYP3A.","Maladie exclue.","Schéma sans rifampicine.","Isoniazide avec B6.","Rifampicine par défaut.","Inhibiteur de protéase = pas de rifampicine.")},
{"f":"A","m":0,"st":"Une femme de 27 ans, originaire d'Érythrée et enceinte de 22 semaines, a un IGRA positif lors de l'enquête d'entourage autour de son mari, atteint de tuberculose pulmonaire contagieuse. Elle n'a aucun symptôme et sa radiographie thoracique est normale.",
 "p":"Que lui proposez-vous ?","o":A(
 (1,"Un traitement préventif dès maintenant, car la grossesse n'est pas une contre-indication et le risque augmente en péri-partum, avec de la vitamine B6 si l'on choisit l'isoniazide","Guide suisse 2024 ; discordance : le Brevier de Rifinah range la grossesse parmi les contre-indications (à vérifier dans l'AIPS)."),
 (0,"Une interruption de grossesse avant tout traitement","Faux : l'isoniazide et la rifampicine n'ont aucun effet tératogène connu."),
 (0,"Un report du traitement après la fin de l'allaitement","Faux : l'allaitement est compatible avec l'isoniazide et la rifampicine, et le risque augmente en péri-partum."),
 (0,"Une association de quatre antituberculeux pendant 2 mois","Faux : la maladie active est exclue ; une quadrithérapie n'est pas indiquée."),
 (0,"Aucun traitement, car les antituberculeux sont tératogènes","Faux : le guide suisse ne décrit aucun effet tératogène de l'isoniazide ni de la rifampicine.")),
 "n":n("preg","doses"),"a":"application","d":3,"l":("Grossesse, contact récent.","Infection récente.","Maladie exclue.","Traiter pendant la grossesse.","B6 si isoniazide.","Attendre.","Grossesse ≠ contre-indication.")},
{"f":"A","st":"Un homme de 46 ans prend depuis 7 semaines un antibiotique quotidien prescrit après un test sanguin positif, avec de la vitamine B6 ; il boit 4 à 5 bières par jour. Il consulte pour des nausées, une fatigue et des urines foncées ; l'ALAT vaut 4 fois la limite supérieure de la normale.",
 "p":"Que faites-vous ?","o":A(
 (1,"Vous arrêtez ce traitement, suivez les tests hépatiques jusqu'à normalisation et demandez l'avis d'un spécialiste avant toute reprise","Guide suisse 2024 : arrêt dès 3 fois la normale avec symptômes (seuils donnés pour les antituberculeux, à vérifier pour le traitement préventif)."),
 (0,"Vous poursuivez, car l'ALAT reste sous 5 fois la normale","Piège : le seuil de 5 fois ne vaut qu'en l'absence de symptômes ; avec symptômes, 3 fois suffisent."),
 (0,"Vous réduisez la dose de moitié et contrôlez dans un mois","Faux : une hépatite médicamenteuse symptomatique impose l'arrêt, pas une demi-dose."),
 (0,"Vous ajoutez un second antibiotique pour raccourcir le traitement","Faux : on n'ajoute aucun médicament potentiellement hépatotoxique pendant une hépatite."),
 (0,"Vous attendez la fin prévue du traitement pour refaire un bilan","Faux : des symptômes d'hépatite sous traitement exigent une évaluation et un arrêt immédiats.")),
 "n":n("hepat","liver"),"a":"piège","d":5,"l":("Nausées, urines foncées, alcool.","Hépatite médicamenteuse.","ALAT × 4 avec symptômes.","Seuil 3× si symptômes.","Arrêter.","Attendre 5×.","Symptômes + ALAT ≥ 3× = arrêt.")},
{"f":"A","m":0,"st":"Une femme de 52 ans, sous méthotrexate et prednisone 20 mg par jour pour une polyarthrite rhumatoïde, partage la chambre de son mari, chez qui une tuberculose pulmonaire contagieuse vient d'être diagnostiquée. Son IGRA est indéterminé avec une réponse faible au mitogène ; elle n'a aucun symptôme et sa radiographie thoracique est normale.",
 "p":"Que proposez-vous ?","o":A(
 (1,"Vous la traitez comme infectée et lui proposez un traitement préventif, car l'immunosuppression rend les tests faussement négatifs ou indéterminés et son risque de progression est élevé","Guide suisse 2024, sélection du type de test et terrains à risque."),
 (0,"Vous considérez le résultat comme négatif et la rassurez","Faux : un IGRA indéterminé n'exclut pas l'infection chez une personne immunodéprimée."),
 (0,"Vous répétez l'IGRA dans un an","Faux : une personne contact immunodéprimée se traite sans attendre, car son risque de progression rapide est élevé."),
 (0,"Vous faites un test cutané qui, s'il est négatif, exclut l'infection","Faux : le test cutané est lui aussi faussement négatif sous immunosuppression."),
 (0,"Vous débutez une association de quatre antituberculeux","Faux : la maladie active est exclue ; une quadrithérapie n'est pas indiquée.")),
 "n":n("immsup","progr"),"a":"application","d":3,"l":("Contact sous immunosuppresseurs.","Réponse lymphocytaire affaiblie.","IGRA indéterminé.","Traiter comme infectée.","Traitement préventif.","Croire le résultat.","Immunodéprimé indéterminé = traiter.")},
{"f":"A","m":0,"st":"Un étudiant vous demande ce que signifie un IGRA positif chez un adulte asymptomatique.",
 "p":"Quelle réponse est juste ?","o":A(
 (1,"Il traduit une mémoire immunitaire des lymphocytes T contre des antigènes du complexe M. tuberculosis, sans prouver la présence de bacilles vivants ni distinguer infection et maladie ; la plupart des personnes positives ne tomberont jamais malades","Guide suisse 2024, infection par M. tuberculosis et tests."),
 (0,"Il prouve que la personne est contagieuse","Faux : un IGRA positif ne dit rien de la contagiosité, qui dépend d'une maladie pulmonaire active."),
 (0,"Il reflète le plus souvent une vaccination par le BCG","Faux : les peptides de l'IGRA sont absents de M. bovis BCG."),
 (0,"Il mesure des anticorps dirigés contre le bacille","Faux : il mesure l'interféron gamma libéré in vitro par les lymphocytes T."),
 (0,"Il impose une association de quatre antituberculeux","Faux : la quadrithérapie traite une maladie active démontrée, non un test positif isolé.")),
 "n":n("def","immuno","prono","igra"),"a":"direct","d":2,"l":("IGRA positif.","Mémoire lymphocytaire T.","Asymptomatique.","Empreinte, pas preuve.","Expliquer.","Contagieux.","Positif ≠ malade.")},
{"f":"A","m":0,"st":"Vous commencez chez un requérant d'asile de 20 ans un traitement de 4 mois de rifampicine pour une infection tuberculeuse latente.",
 "p":"Que devez-vous déclarer ?","o":A(
 (1,"Rien : les traitements de l'infection ne se déclarent pas ; seule une tuberculose traitée par au moins trois médicaments ou à culture positive se déclare au médecin cantonal dans la semaine","Guide suisse 2024, système de déclaration."),
 (0,"Une déclaration clinique au médecin cantonal dans la semaine","Piège : cette déclaration vaut pour la tuberculose maladie, pas pour le traitement de l'infection."),
 (0,"Une déclaration à l'OFSP dans les 24 heures","Faux : le délai de 24 heures concerne la déclaration du laboratoire en cas de mycobactérie identifiée."),
 (0,"Un rapport médical au SEM pour suspendre son renvoi","Faux : l'accord OFSP–SEM ne s'applique pas à l'infection latente."),
 (0,"Une annonce à la Suva","Faux : l'assurance-accidents ne concerne que l'infection d'origine professionnelle.")),
 "n":n("decl"),"a":"piège","d":2,"l":("Traitement préventif.","Pas de maladie.","Asile.","Pas de déclaration.","Ne rien déclarer.","Déclarer quand même.","Infection = pas de déclaration.")},
{"f":"A","m":0,"st":"Un requérant d'asile débouté de 23 ans prend depuis 6 semaines de la rifampicine pour une infection tuberculeuse latente ; son transfert Dublin vers l'Italie est fixé dans 3 semaines. Le foyer vous demande d'annoncer le traitement au SEM pour suspendre le renvoi.",
 "p":"Que répondez-vous ?","o":A(
 (1,"Que l'accord OFSP–SEM ne vaut que pour la tuberculose maladie et que l'infection latente ne peut pas empêcher un renvoi ; vous l'expliquez au patient avec un interprète et lui remettez un résumé médical pour poursuivre le traitement","Information OFSP–SEM 2018 ; guide suisse 2024 ; relais à l'étranger : avis d'expert (à vérifier)."),
 (0,"Que vous remplissez le rapport médical du SEM, qui suspend le renvoi jusqu'à la fin du traitement","Piège : ce report ne concerne que le traitement d'une tuberculose maladie."),
 (0,"Que vous déclarez le traitement au médecin cantonal","Faux : les traitements de l'infection ne se déclarent pas."),
 (0,"Que vous arrêtez le traitement sans en parler au patient","Faux : on informe le patient et l'on favorise la poursuite du traitement plutôt qu'un arrêt silencieux."),
 (0,"Que vous passez à une quadrithérapie pour obtenir la suspension","Faux : une quadrithérapie sans maladie active est injustifiée et dangereuse.")),
 "n":n("asile","interp"),"a":"application","d":3,"l":("Renvoi Dublin, traitement préventif.","Accord limité à la maladie.","Requérant débouté.","Pas de suspension.","Informer et transmettre.","Rapport SEM.","Infection latente ≠ suspension du renvoi.")},
{"f":"A","st":"Un médecin de famille de Bienne veut proposer un test sanguin de libération d'interféron gamma à tous ses patients nés à l'étranger, car il a lu que les cas augmentent en Suisse. Parmi eux, un retraité de 67 ans, arrivé d'Italie il y a 45 ans, n'a ni symptôme ni traitement immunosuppresseur.",
 "p":"Que lui conseillez-vous ?","o":A(
 (1,"De ne tester que des personnes qu'il est prêt à traiter si le test est positif, dans les groupes ciblés (contacts récents, immunodéprimés, avant un anti-TNF ou une greffe, éventuellement jeunes migrants récents de pays à très forte incidence), donc pas ce retraité","Guide suisse 2024 ; Bulletin OFSP 2026 : la hausse de 2025 concerne surtout des personnes nées à l'étranger, sans justifier un dépistage général."),
 (0,"De tester toutes les personnes nées à l'étranger, quel que soit leur âge","Faux : un dépistage non ciblé a une faible valeur prédictive positive et n'est pas recommandé."),
 (0,"De tester ce retraité et de traiter tout résultat positif","Faux : sans facteur de risque ni projet de traitement, le test n'est pas indiqué."),
 (0,"De faire une radiographie thoracique à tous ses patients nés à l'étranger","Faux : la radiographie de routine a été abandonnée en Suisse pour son mauvais rapport coût-efficacité, et un dépistage non ciblé n'est pas recommandé."),
 (0,"De répéter le test chaque année chez les migrants","Faux : aucun test répété de routine n'est recommandé hors exposition.")),
 "n":n("qui","migr","risk","epich"),"a":"application","d":4,"l":("Dépistage général proposé.","Faible valeur prédictive.","Retraité sans risque.","Tester seulement pour traiter.","Cibler.","Tout le monde.","Pas de test sans projet de traitement.")},
{"f":"A","st":"Une étudiante en soins infirmiers de 22 ans, née en Inde et vaccinée à la naissance (cicatrice au bras), fait le test de référence demandé par l'hôpital avant un stage aux urgences : le test cutané intradermique montre une induration de 11 mm à 72 heures. Elle n'a aucun symptôme.",
 "p":"Que faites-vous ?","o":A(
 (1,"Vous demandez un test sanguin de libération d'interféron gamma, plus spécifique après le BCG, puis, s'il est positif, le bilan clinique et radiologique avant toute décision","Guide suisse 2024 : IGRA non influencé par le BCG, à spécificité plus grande."),
 (0,"Vous concluez que la vaccination explique toujours la réaction et ne faites rien","Piège : le BCG peut expliquer la réaction, mais pas toujours ; une infection reste possible chez une personne née en zone d'endémie."),
 (0,"Vous débutez d'emblée 4 mois de rifampicine","Faux : on n'instaure aucun traitement préventif avant d'avoir exclu une maladie active."),
 (0,"Vous refaites le test cutané chaque année pendant son stage","Faux : les tests répétés de routine ne sont pas recommandés chez les professionnels de la santé."),
 (0,"Vous lui proposez un rappel de vaccination par le BCG","Faux : le BCG n'est plus recommandé aux résidents permanents de Suisse et n'y est pas disponible.")),
 "n":n("igra","bcg","tct"),"a":"application","d":4,"l":("Vaccinée, induration 11 mm.","Réaction croisée possible.","Test de référence.","IGRA plus spécifique.","Confirmer par IGRA.","Tout attribuer au BCG.","Vaccinée = IGRA.")},
{"f":"A","m":0,"st":"Un centre d'hébergement cantonal veut proposer un dépistage de l'infection tuberculeuse par IGRA à ses jeunes résidents venus de pays à très forte incidence.",
 "p":"Que faut-il organiser en premier ?","o":A(
 (1,"Un accord préalable avec les autorités cantonales sur la prise en charge du dépistage, non payé par l'assurance-maladie, et un cadre qui permet de mener le traitement à terme, interprètes compris","Guide suisse 2024, dépistage hors des centres fédéraux ; OFSP : financement de l'interprétariat réglé par chaque canton."),
 (0,"La facturation du dépistage à l'assurance-maladie, sans franchise ni quote-part","Faux : l'assurance-maladie ne paie pas ce dépistage et n'accorde aucune dispense de participation pour la tuberculose."),
 (0,"La facturation à l'assurance-accidents","Faux : l'assurance-accidents ne couvre que l'infection d'origine professionnelle reconnue."),
 (0,"Un dépistage par IGRA dès l'arrivée dans le centre fédéral","Faux : le dépistage systématique de l'infection n'est pas recommandé dans les centres fédéraux."),
 (0,"Un dépistage sans plan de traitement des résultats positifs","Faux : on ne teste que si le traitement peut être mené à terme.")),
 "n":n("couts","migr","interp"),"a":"piège","d":3,"l":("Programme de dépistage.","Coûts et observance.","Jeunes migrants.","Accord cantonal préalable.","Organiser avant de tester.","Facturer à la LAMal.","Pas de LAMal pour le dépistage.")},
{"f":"Kprim","m":0,"st":"Vous comparez les tests de l'infection tuberculeuse.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
 (1,"L'IGRA n'est pas influencé par une vaccination antérieure par le BCG.","Guide suisse 2024 : peptides absents de M. bovis BCG."),
 (1,"Le test cutané se lit à 48–72 heures en mesurant l'induration, sans tenir compte de l'érythème.","Guide suisse 2024."),
 (0,"Un IGRA positif prouve la présence de bacilles vivants.","Faux : il mesure une mémoire immunitaire, sans prouver la persistance de bacilles."),
 (0,"Chez une personne immunodéprimée, un IGRA négatif exclut l'infection.","Faux : l'immunosuppression rend les tests faussement négatifs.")),
 "n":n("igra","tct","def","immuno","immsup"),"a":"direct","d":3,"l":("Tests.","Lymphocytes T mémoire.","Lecture.","Spécificité, limites.","Choisir le test.","Positif = bacilles.","IGRA spécifique, jamais une preuve.")},
{"f":"Kprim","m":0,"st":"Vous choisissez un traitement de l'infection tuberculeuse latente en Suisse.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
 (1,"La rifampicine chaque jour pendant 4 mois est un schéma proposé par le guide suisse.","Guide suisse 2024 ; l'OMS 2024 la classe parmi les alternatives."),
 (1,"L'association isoniazide et rifampicine chaque jour pendant 3 mois est un schéma proposé.","Guide suisse 2024 ; OMS 2024."),
 (1,"L'isoniazide chaque jour pendant 6 (ou 9) mois est un schéma proposé.","Guide suisse 2024 ; le Brevier d'Isoniaz-TB indique 9 mois."),
 (0,"La rifapentine hebdomadaire pendant 12 semaines est disponible et remboursée en Suisse.","Faux : la rifapentine n'est ni homologuée ni remboursée en Suisse.")),
 "n":n("regimes","who"),"a":"direct","d":3,"l":("Schémas.","Rifamycines et isoniazide.","Suisse.","Trois schémas.","Choisir.","Rifapentine.","4R, 3HR, 6–9H ; pas de rifapentine.")},
{"f":"Kprim","m":0,"st":"Vous traitez une infection tuberculeuse latente dans des situations particulières.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
 (1,"La contraception hormonale reste inefficace jusqu'à un mois après la fin de la rifampicine.","Guide suisse 2024."),
 (1,"Un contact immunodéprimé à forte probabilité d'infection dont l'IGRA est indéterminé se traite comme infecté.","Guide suisse 2024."),
 (1,"L'allaitement est compatible avec l'isoniazide et la rifampicine, avec de la vitamine B6 pour le nouveau-né sous isoniazide.","Guide suisse 2024 ; discordance : le Brevier de Rifinah cite l'allaitement parmi les contre-indications."),
 (0,"Rimactan peut être associé sans restriction à un inhibiteur non nucléosidique de la transcriptase inverse.","Faux : le Brevier de Rimactan contre-indique cette association.")),
 "n":n("inter","immsup","preg","hiv"),"a":"direct","d":3,"l":("Terrains particuliers.","Induction enzymatique.","Contraception, VIH, allaitement.","Interactions.","Adapter.","Associer sans vérifier.","Rifampicine = vérifier chaque médicament.")},
{"f":"Kprim","m":0,"st":"Vous présentez le cadre suisse de l'infection tuberculeuse latente.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
 (1,"Les traitements de l'infection ne se déclarent pas au médecin cantonal.","Guide suisse 2024."),
 (0,"Tous les requérants d'asile passent une radiographie thoracique à leur arrivée.","Faux : la radiographie de routine a été remplacée en 2006 par un dépistage par entretien."),
 (0,"L'accord OFSP–SEM sur le traitement mené à terme en Suisse s'applique aussi à l'infection latente.","Faux : il ne concerne que la tuberculose maladie."),
 (1,"Cinq à dix pour cent des personnes infectées tombent malades au cours de leur vie, surtout dans les deux ans.","OFSP ; guide suisse 2024.")),
 "n":n("decl","asile","risk"),"a":"direct","d":2,"l":("Cadre suisse.","Risque de progression.","Asile.","Déclaration, accord SEM.","Connaître le cadre.","Radiographie systématique.","Infection : ni déclaration ni suspension.")},
{"f":"MenuLong","st":"Vous voyez ce matin, au cabinet à Fribourg, les personnes suivantes.",
 "p":"Choisissez les TROIS personnes chez qui un test sanguin de libération d'interféron gamma est indiqué.","o":A(
 (1,"Un homme de 41 ans qui doit commencer de l'adalimumab pour une spondylarthrite","Guide suisse 2024 et OMS 2024 : test avant un anti-TNF."),
 (1,"Une femme de 36 ans chez qui une infection par le VIH vient d'être découverte","Guide suisse 2024 : contrôle initial lors d'une infection par le VIH."),
 (1,"Un homme de 55 ans inscrit sur la liste d'attente d'une greffe rénale","Guide suisse 2024 : test avant une transplantation."),
 (0,"Un retraité de 67 ans arrivé d'Italie il y a 45 ans, sans facteur de risque","Faux : aucun facteur de risque ni projet de traitement ; un test non ciblé n'est pas indiqué."),
 (0,"Un requérant d'asile arrivé hier dans un centre fédéral, sans symptôme","Faux : le centre fédéral fait un dépistage par entretien dans les 72 heures, sans IGRA systématique."),
 (0,"Une infirmière au test de référence négatif, sans exposition, qui demande son contrôle annuel","Faux : les tests répétés de routine ne sont pas recommandés hors exposition."),
 (0,"Un lycéen qui souhaite un test pour un séjour linguistique","Faux : aucune indication médicale ; un test demandé de son propre chef est à sa charge."),
 (0,"Une femme de 30 ans qui tousse depuis 6 semaines avec des sueurs nocturnes","Piège : ces symptômes imposent la recherche d'une maladie active (radiographie, échantillons respiratoires), pas un test d'infection."),
 (0,"Un touriste qui rentre de deux semaines de vacances au Vietnam","Faux : un court séjour touristique ne justifie pas de test (avis d'expert, à vérifier)."),
 (0,"Une femme de 45 ans née en Suisse qui demande un bilan de santé complet","Faux : sans facteur de risque, le test a une faible valeur prédictive."),
 (0,"Un homme de 50 ans hypertendu et bien traité","Faux : l'hypertension n'augmente pas le risque de progression."),
 (0,"Un enfant de 9 ans né en Suisse, en bonne santé, pour son entrée à l'école","Faux : aucune exposition ni facteur de risque ; pas d'indication.")),
 "n":n("qui","asile","sympt","migr"),"a":"piège","d":4,"l":("Demandes variées.","Risque de progression.","Immunodépression prévue ou présente.","Tester pour traiter.","Cibler.","Symptomatique, requérant en centre fédéral.","Anti-TNF, VIH, greffe.")},
{"f":"MenuLong","m":0,"st":"Un homme de 30 ans, non infecté par le VIH, contact familial d'une personne atteinte de tuberculose pulmonaire confirmée, a un IGRA positif.",
 "p":"Choisissez les DEUX constatations qui permettent, selon l'OMS 2024, d'exclure une tuberculose active avant le traitement préventif.","o":A(
 (1,"L'absence de tout symptôme de tuberculose","OMS 2024, recommandation 14."),
 (1,"Une radiographie thoracique sans anomalie","OMS 2024, recommandation 14."),
 (0,"Une valeur d'IGRA faiblement positive","Faux : l'intensité de l'IGRA ne distingue pas infection et maladie."),
 (0,"Une CRP inférieure à 5 mg/l","Faux : l'OMS ne propose la CRP que pour le dépistage chez les personnes vivant avec le VIH."),
 (0,"Un test cutané inférieur à 5 mm","Faux : un test cutané ne renseigne pas sur l'activité de la maladie."),
 (0,"Une auscultation pulmonaire normale","Faux : aucun signe clinique n'est pathognomonique ; un examen normal n'exclut pas la maladie."),
 (0,"Une vitesse de sédimentation normale","Faux : ce marqueur ne figure pas parmi les critères d'exclusion de l'OMS."),
 (0,"Une formule sanguine normale","Faux : elle n'exclut pas une tuberculose active."),
 (0,"Une saturation en oxygène normale","Faux : elle est souvent normale au début de la maladie."),
 (0,"Une spirométrie normale","Faux : elle n'explore pas l'activité infectieuse."),
 (0,"L'absence de cicatrice de BCG","Faux : le statut vaccinal ne renseigne pas sur une maladie active."),
 (0,"Un examen ORL normal","Faux : il n'a aucune valeur pour exclure une atteinte pulmonaire.")),
 "n":n("sympt","xray","exam"),"a":"direct","d":3,"l":("Contact, IGRA positif.","Maladie à exclure.","Asymptomatique ?","Symptômes et radiographie.","Exclure puis traiter.","Marqueurs inutiles.","Pas de symptôme + radiographie normale.")},
]
for _q in Q: _q["src"] = [MAN]
_SRC = {0:[MAN,OMS,INT],1:[MAN],2:[MAN,RIM],3:[MAN,HUM],4:[MAN,RIM,INH,OMS],5:[MAN,RIF],6:[MAN],7:[MAN],8:[MAN],9:[MAN],
        10:[SEM,MAN,EXP],11:[MAN,BUL,OMS],12:[MAN],13:[MAN,INT],14:[MAN],15:[MAN,OMS,INH],16:[MAN,RIM,RIF],17:[MAN,OFSP],18:[MAN,OMS,EXP],19:[OMS]}
for i, s in _SRC.items(): Q[i]["src"] = s
C = {"theme":"Infection tuberculeuse latente du migrant (porte O7.13) selon le guide suisse 2024 de la Ligue pulmonaire et de l'OFSP : dépistage ciblé (tester seulement pour traiter), IGRA contre test cutané et BCG, exclusion d'une tuberculose active (symptômes, radiographie, échantillons respiratoires) avant tout traitement préventif, schémas suisses (rifampicine 4 mois, isoniazide 6–9 mois, isoniazide et rifampicine 3 mois), interactions de la rifampicine, grossesse, VIH, anti-TNF, surveillance hépatique, absence de déclaration, asile, interprétariat et coûts",
 "notions":[
  {"titre":"Comprendre","rub":["definition","epidemiology","basicSciences","prognosisDischarge"],"comment":"Un test positif est une empreinte immunitaire ; le risque de maladie se concentre sur les deux premières années et sur les terrains fragiles.",
   "points":["5–10 % de malades au cours de la vie, surtout dans les 2 ans.","2025 : 544 cas en Suisse, hausse chez les personnes nées à l'étranger.","Traitement bien suivi : jusqu'à 90 % de cas évités."],"sources":[MAN,OFSP,BUL,OMS]},
  {"titre":"Qui tester et comment","rub":["anamnesis","clinicalExam","workupAlternatives","positiveDiagnosis"],"comment":"On teste seulement les groupes ciblés, avec le bon test et un interprète si besoin.",
   "tab":(["Situation","Test","Remarque"],[["Contact récent, immunodéprimé, avant anti-TNF ou greffe","IGRA ou test cutané",[("Guide suisse","Tester seulement si l'on prévoit de traiter.")]],["Jeune migrant de pays > 100/100 000, cadre stable","IGRA à discuter",[("Guide suisse","Accord préalable avec le canton sur les coûts.")]],["Personne vaccinée par le BCG","IGRA",[("Guide suisse","Plus spécifique que le test cutané.")]],["Jeune enfant non vacciné","Test cutané",[("Guide suisse","IGRA moins fiable chez le jeune enfant.")]]]),
   "points":["Immunodéprimé indéterminé : traiter comme infecté.","Toux et crachats : demander avec un interprète professionnel."],"sources":[MAN,OMS,INT]},
  {"titre":"Exclure puis traiter","rub":["presumptionRedFlags","workupGoldStandard","acuteManagement","chronicManagement"],"comment":"On exclut d'abord une maladie active, puis l'on choisit un schéma adapté aux interactions et au terrain.",
   "arbre":[("d1",None,"Test positif","On recherche symptômes et signes et l'on fait une radiographie thoracique.",None,None),("d2","d1","Symptôme ou radiographie anormale","On analyse des échantillons respiratoires avant tout traitement.",None,None),("d3","d1","Asymptomatique, radiographie normale","On propose un traitement préventif.",None,None),("d4","d3","Inhibiteur de protéase du VIH","On évite la rifampicine et l'on choisit avec un spécialiste.",None,None)],
   "points":["Rimactan 10 mg/kg, max. 600 mg/j, à jeun, 4 mois.","Contraception hormonale inefficace jusqu'à 1 mois après la rifampicine.","Grossesse non contre-indiquée selon le guide ; discordance avec le Brevier de Rifinah."],"sources":[MAN,OMS,RIM,RIF]},
  {"titre":"Suivre et orienter","rub":["hospitalizationComplications","surveillance","followUpNetwork"],"comment":"On surveille la tolérance, on connaît les règles de déclaration et d'asile, et l'on règle les coûts à l'avance.",
   "points":["Hépatite : arrêt dès 3× la normale avec symptômes, 5× sans symptôme.","Infection latente : pas de déclaration, pas de suspension de renvoi.","Dépistage des migrants non payé par l'assurance-maladie."],"sources":[MAN,SEM,INT]}],
 "ssp":("O7.13","Patient d’un autre milieu culturel, migration",True,[
   ("n1",None,"Migrant asymptomatique","On décide de tester seulement si un traitement est prévu.","itl","c2"),
   ("n2","n1","Test positif","On recherche symptômes et signes et l'on fait une radiographie.","itl","c3"),
   ("n3","n2","Anomalie ou symptôme","On analyse des échantillons respiratoires avant tout traitement.","itl","c3"),
   ("n4","n2","Maladie exclue","On choisit un schéma préventif selon les interactions.","itl","c3"),
   ("n5","n4","Sous traitement","On surveille tolérance, observance et foie.","itl","c4"),
   ("n6","n5","Asile, coûts, déclaration","On applique le cadre suisse sans déclarer l'infection.","itl","c4")]),
 "pec":[
  pec("itl","Infection tuberculeuse latente du migrant",["On prévient la progression vers une tuberculose chez les personnes à risque.","On évite tout traitement préventif chez une personne atteinte de maladie active."],
      ["On explique avec un interprète professionnel le sens du test et l'intérêt du traitement.","On recherche les symptômes et l'on vérifie la liste complète des médicaments."],
      [("Rifampicine (Rimactan)","10 (8–12) mg/kg une fois par jour, au plus 600 mg, à jeun au moins 30 minutes avant le repas, pendant 4 mois (guide suisse) ; posologies à vérifier dans l'AIPS (Swissmedic)","Elle détruit les bacilles quiescents avec un schéma court et un risque hépatique plus faible.",RIM),
       ("Isoniazide (Isoniaz-TB) avec pyridoxine","5 mg/kg une fois par jour, au plus 300 mg, pendant 6 (ou 9) mois (guide) ou 9 mois (Brevier), avec 10 à 20 mg de pyridoxine par jour ; posologies à vérifier dans l'AIPS (Swissmedic)","Il remplace la rifampicine quand les interactions l'interdisent, et la pyridoxine prévient la neuropathie.",INH),
       ("Rifampicine et isoniazide (Rifinah 150/100 mg)","4 comprimés par jour au-delà de 50 kg, 3 en dessous, pendant 3 mois (guide suisse) ; posologies à vérifier dans l'AIPS (Swissmedic)","Elle associe deux antituberculeux pour raccourcir le traitement à trois mois.",RIF)],
      [("éducation thérapeutique","On explique la prise à jeun, les interactions et les signes d'hépatite.","On améliore l'observance et la sécurité du traitement."),("social et assurances","On règle à l'avance la prise en charge des coûts avec le canton et l'assurance-maladie.","On évite qu'un obstacle financier interrompe le traitement."),("soins infirmiers","On organise les contrôles réguliers avec la Ligue pulmonaire cantonale.","On suit la tolérance et l'observance jusqu'à la fin du traitement.")],
      [("C Communication clinique","On recourt à un interprète communautaire professionnel pour l'anamnèse et le consentement."),("N Médecine sociale Prévention OFSP","On applique les règles de déclaration, d'asile et de financement du guide suisse.")],
      None,
      (["On cible le dépistage.","On exclut une maladie active.","On traite et l'on surveille."],[("d'abord","médecin de famille","Il vérifie l'indication du test et le projet de traitement avec le patient."),("ensuite","médecin de famille","Il recherche les symptômes, examine et fait faire une radiographie thoracique."),("puis","Ligue pulmonaire cantonale","Elle accompagne le traitement préventif, l'observance et les questions d'asile et de coûts.")]),
      "Un traitement préventif bien suivi réduit jusqu'à 90 % le risque de tuberculose ; la plupart des personnes positives ne tombent jamais malades.",
      [("Symptômes de tuberculose","À chaque contrôle","Absents"),("Tolérance et observance","Régulièrement pendant le traitement","Traitement mené à terme"),("Tests hépatiques","Au début, puis chaque mois si hépatopathie, alcool ou autre hépatotoxique","Pas d'hépatite médicamenteuse")],"La personne termine son traitement préventif, connaît les symptômes qui doivent la faire consulter et garde son dossier.",
      ("On dépiste et traite rapidement les cas contagieux et l'on organise l'enquête d'entourage.","On teste les groupes ciblés et l'on traite l'infection après exclusion d'une maladie active.","On surveille l'hépatotoxicité et les interactions et l'on mène le traitement à son terme.")),]}
