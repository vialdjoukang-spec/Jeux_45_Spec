from constructeur_agent_45spec import pec
ID = "T88.7__G5-E08"
C65 = "[HUG, CAPP-INFO n° 65, Hyponatrémie et médicaments (2015), SIADH, diurétiques, ISRS, prise en charge et « Que retenir ? », lu le 28.11.2026]"
C67 = "[HUG, CAPP-INFO n° 67, Médicaments, chutes & fractures (De Giorgi Salamun et al., 2022), FRIDs, lithium, cardiovasculaires et tableau d'optimisation, lu le 28.11.2026]"
RMS = "[Roukain A, Pechère-Bertschi A, Hypotension artérielle : l'envers du décor, Rev Med Suisse (2018) 14:1581-7, définition de l'hypotension orthostatique, causes et tableau 3, lu le 28.11.2026]"
BEE = "[Beeler PE, Stammschulte T, Dressel H, Hospitalisations related to adverse drug reactions in Switzerland 2012-2019, Drug Saf (2023), PMID 37335465, résumé lu le 28.11.2026]"
OPE = "[Blum MR et al., OPERAM cluster randomised controlled trial, BMJ (2021) 374:n1585, PMID 34257088, résumé lu le 28.11.2026]"
ZER = "[Zerah L et al., Trigger tool for drug-related hospital admissions in older people (OPERAM), Age Ageing (2022), PMID 34794171, résumé lu le 28.11.2026]"
LAP = "[Lapi F et al., Diuretics, ACE inhibitors or ARBs with NSAIDs and acute kidney injury, BMJ (2013) 346:e8525, PMID 23299844, résumé lu le 28.11.2026]"
GAN = "[Gandhi S et al., Calcium-channel blocker-clarithromycin drug interactions and acute kidney injury, JAMA (2013), PMID 24346990, résumé lu le 28.11.2026]"
MAN = "[Mangoni AA, Jackson SHD, Age-related changes in pharmacokinetics and pharmacodynamics, Br J Clin Pharmacol (2004), PMID 14678335, résumé lu le 28.11.2026]"
CAU = "[Lettre, Adverse drug reaction and causality assessment scales, Lung India (2011), PMID 21712934, texte intégral PMC3109846 (tableaux Naranjo et OMS-UMC), lu le 28.11.2026]"
CG185 = "[NICE CG185, Bipolar disorder (2014, mise à jour du 02.09.2025), recommandations 1.10.15 à 1.10.24 sur le lithium, lues le 28.11.2026]"
NG148 = "[NICE NG148, Acute kidney injury (mise à jour du 16.10.2024), recommandations 1.1.1, 1.2.14, 1.3.1, 1.4.3, 1.4.4, 1.5.3 et 1.6.4, lues le 28.11.2026]"
SMC = "[Swissmedic, page Pharmacovigilance : que déclarer, délais de 15 et 60 jours, obligation des professionnels, centres régionaux, lue le 28.11.2026]"
QUI = "[Compendium.ch, résumé (Brevier) de Quilonorm retard 12,2 mmol (lithium), posologie selon la lithémie et contre-indications, lu le 28.11.2026 ; AIPS complète à vérifier]"
SER = "[Compendium.ch, résumé (Brevier) de Seropram 20 mg (citalopram), posologie après 65 ans, réduction de dose et contre-indications, lu le 28.11.2026 ; AIPS complète à vérifier]"
KLA = "[Compendium.ch, résumé (Brevier) de Klacid 250 mg (clarithromycine), posologie et contre-indications, lu le 28.11.2026 ; AIPS complète à vérifier]"
BEL = "[Compendium.ch, résumé (Brevier) de Beloc Zok 25 mg (métoprolol), contre-indications, lu le 28.11.2026 ; AIPS complète à vérifier]"
BRU = "[Compendium.ch, résumé (Brevier) de Brufen granulé effervescent 600 mg (ibuprofène), contre-indications, lu le 28.11.2026 ; AIPS complète à vérifier]"
ARI = "[Compendium.ch, résumé (Brevier) d'Aricept Evess 5 mg (donépézil), posologie, lu le 28.11.2026 ; AIPS complète à vérifier]"
EXP = "Avis d'expert (à vérifier)"
_N = [
("def","definition","critère",1,1,SMC+" ; "+C67,"On parle d'effet indésirable au sens de l'OMS, repris par Swissmedic, quand la réaction survient lors de l'utilisation habituelle du médicament aux doses normales ; chez la personne âgée, il se présente souvent comme une sensation de maladie peu spécifique : fatigue, vertiges, somnolence, confusion ou chute."),
("epi","epidemiology","chiffre",2,1,BEE+" ; "+ZER,"En Suisse, de 2012 à 2019, 2,3 % des hospitalisations (environ 32 000 par an) étaient dues à un effet indésirable, dont 46,9 % chez des personnes de 65 ans ou plus, avec une mortalité hospitalière de 2,2 % ; chez les patients âgés multimorbides de l'essai OPERAM, 42 % des hospitalisations examinées étaient liées à un médicament."),
("pk","basicSciences","mécanisme",2,0,MAN,"Avec l'âge, les clairances rénale et hépatique diminuent et le volume de distribution des médicaments liposolubles augmente, ce qui allonge leur demi-vie ; la sensibilité aux anticoagulants, aux médicaments cardiovasculaires et aux psychotropes augmente le plus souvent."),
("cyp","basicSciences","mécanisme",2,0,GAN+" ; "+KLA,"La clarithromycine inhibe le CYP3A4, l'azithromycine non : associée à un anticalcique, la clarithromycine double le risque d'hospitalisation pour insuffisance rénale aiguë (0,44 % contre 0,22 %, OR 1,98 ; OR 5,33 avec la nifédipine) et augmente celui d'hospitalisation pour hypotension (OR 1,60)."),
("chrono","anamnesis","critère",3,0,C67+" ; "+CAU+" ; "+NG148,"On reconstitue la chronologie de tout ce que la personne prend, y compris les anti-inflammatoires achetés sans ordonnance : un médicament introduit, une dose modifiée ou un ajout récent (moins de 2 mois, surtout pour le système nerveux central et cardiovasculaire) précède le trouble avec un délai plausible, premier critère d'imputabilité."),
("ortho","clinicalExam","examen",2,0,RMS,"On mesure la TA couchée puis debout : une baisse systolique d'au moins 20 mmHg et/ou diastolique d'au moins 10 mmHg dans les 3 minutes définit l'hypotension orthostatique (test de Schellong) ; on la cherche systématiquement après 65 ans, sous antihypertenseur et devant des vertiges, une chute ou une fatigue, car elle est souvent peu symptomatique."),
("brady","clinicalExam","signe",1,1,C67+" ; "+BEL,"Un pouls lent sous bêtabloquant ou sous inhibiteur de la cholinestérase fait évoquer une cause médicamenteuse (syncope possible par bradyarythmie sous inhibiteur de la cholinestérase) ; la notice suisse de Beloc Zok contre-indique le métoprolol en cas de bradycardie sous 50/min, d'hypotension ou de bloc AV du 2e ou du 3e degré."),
("rf","presumptionRedFlags","signe",3,0,C65+" ; "+C67+" ; "+NG148+" ; "+EXP,"Une confusion ou des troubles de l'attention récents, une chute ou une syncope, une bradycardie, une hypotension, une hyponatrémie ou une hausse de la créatinine chez une personne âgée traitée imposent une évaluation rapide, souvent hospitalière, et la recherche d'un médicament en cause."),
("litox","presumptionRedFlags","complication",1,1,CG185+" ; "+QUI+" ; "+C67,"Sous lithium, un tremblement accru, une ataxie, des paresthésies, une confusion ou des troubles cognitifs font évoquer une atteinte neurologique, possible même à une lithémie dans la cible (NICE) ; la notice suisse de Quilonorm contre-indique le lithium en cas de maladie rénale, de déshydratation avec trouble du sodium et de régime pauvre en sel."),
("bilan","workupGoldStandard","décision",2,0,NG148+" ; "+RMS+" ; "+C65+" ; "+EXP,"Le bilan de base associe la revue de toute la liste, la TA couchée et debout, la natrémie, la kaliémie et la créatinine comparée à la valeur antérieure, et un ECG en cas de pouls lent ; une hausse de créatinine d'au moins 26 µmol/l en 48 heures ou d'au moins 50 % en 7 jours définit une insuffisance rénale aiguë."),
("lilev","workupAlternatives","seuil",2,1,CG185+" ; "+QUI,"On dose les médicaments à marge étroite comme le lithium, 1 semaine après le début et après chaque changement de dose : NICE vise 0,6 à 0,8 mmol/l en première prescription, alors que le résumé suisse de Quilonorm retard indique 0,5 à 1,0 mmol/l au long cours et 0,8 à 1,2 mmol/l dans la manie aiguë, discordance à signaler (posologies à vérifier dans l'AIPS (Swissmedic))."),
("naranjo","workupAlternatives","critère",1,0,CAU,"L'échelle de Naranjo additionne des points (délai, amélioration à l'arrêt, récidive à la réexposition, absence d'autre cause, taux toxique, effet-dose) : 5 à 8 points signent un effet probable, 1 à 4 un effet possible, 0 un effet douteux, au-delà un effet certain."),
("imput","positiveDiagnosis","critère",3,0,CAU,"Selon l'OMS-UMC, le lien est probable quand le délai est raisonnable, qu'une maladie ou un autre médicament l'explique mal et que l'évolution à l'arrêt est cohérente, sans réexposition nécessaire ; il reste possible si une autre cause peut aussi l'expliquer ou si l'évolution à l'arrêt manque."),
("na","positiveDiagnosis","résultat",2,0,C65,"Une hyponatrémie (moins de 136 mmol/l) sous traitement oriente d'abord vers un thiazidique ou un analogue (hyponatrémie chez environ 11 % des patients sous diurétique), un ISRS (0,5 à 32 %, quelques semaines après le début, régressive environ 2 semaines après l'arrêt), la carbamazépine, un antipsychotique ou un opiacé ; l'âge avancé et les diurétiques en sont les principaux facteurs de risque."),
("nadx","positiveDiagnosis","diagnostic différentiel",1,0,C65,"On écarte une fausse hyponatrémie (hyperglycémie, hyperlipidémie, paraprotéine) ; un SIADH, diagnostic d'exclusion, ne se retient ni sous diurétique ni sans fonctions cardiaque, rénale, surrénalienne, hépatique et thyroïdienne normales, et il se documente par natrémie, osmolalité plasmatique et natriurèse simultanées."),
("stop","acuteManagement","décision",3,0,NG148+" ; "+C65+" ; "+CAU+" ; "+EXP,"On suspend ou réduit le médicament suspect après avoir pesé bénéfice et risque, on corrige la volémie et les électrolytes et l'on suspend temporairement IEC et sartans en cas de diarrhée, de vomissements ou de sepsis ; l'arrêt sert à la fois de traitement et d'argument diagnostique."),
("nacorr","acuteManagement","seuil",1,0,C65,"Une hyponatrémie hypovolémique se corrige par du sérum salé isotonique, une hyponatrémie euvolémique par une restriction hydrique ; la natrémie ne doit idéalement pas remonter de plus de 9 mmol/l par 24 heures, au maximum de 10 à 12 mmol/l, pour éviter une myélinolyse centropontine."),
("klacid","acuteManagement","piège",1,1,KLA+" ; "+GAN,"La notice suisse de Klacid (250 à 500 mg toutes les 12 heures) contre-indique la clarithromycine avec la simvastatine, la lovastatine, la colchicine, la quétiapine, le ticagrélor ou l'ivabradine, en cas de QT long ou d'hypokaliémie ; l'azithromycine, qui n'inhibe pas le CYP3A4, est une alternative (posologies à vérifier dans l'AIPS (Swissmedic))."),
("sick","chronicManagement","prévention",2,0,NG148+" ; "+CG185,"On prévient la personne à risque : en cas de diarrhée, de vomissements ou de maladie aiguë, elle consulte, maintient ses boissons et l'on envisage de suspendre temporairement IEC et sartans ; elle évite les anti-inflammatoires achetés sans ordonnance, surtout sous lithium."),
("operam","chronicManagement","piège",1,1,OPE,"Dans l'essai OPERAM (Suisse, Pays-Bas, Belgique, Irlande ; médiane de 9 médicaments), une optimisation structurée a réduit les prescriptions inappropriées (présentes chez 86,1 % des patients) sans réduire les hospitalisations liées aux médicaments à 12 mois (HR 0,95) : la revue ne dispense pas du suivi clinique."),
("cit","chronicManagement","posologie",1,1,SER,"Le résumé suisse de Seropram limite le citalopram à la moitié de la dose après 65 ans, au maximum 20 mg par jour et le contre-indique avec les médicaments qui allongent le QT (posologies à vérifier dans l'AIPS (Swissmedic))."),
("start","chronicManagement","décision",1,0,C67,"Chez la personne âgée, on tient compte du poids et des fonctions rénale et hépatique, on commence à la plus petite dose et l'on augmente lentement, on évite de cumuler les médicaments qui font chuter et l'on réévalue toute benzodiazépine après 4 semaines."),
("nocasc","chronicManagement","piège",1,0,C67+" ; "+EXP,"On ne traite pas un symptôme nouveau (vertiges, troubles de l'attention, tremblement, chute) par un médicament supplémentaire avant d'avoir cherché sa cause dans la liste existante : l'ajout crée une cascade de prescriptions et de nouveaux risques."),
("aki","hospitalizationComplications","complication",2,1,LAP+" ; "+NG148+" ; "+BRU,"L'association d'un diurétique, d'un IEC ou d'un sartan et d'un anti-inflammatoire augmente le risque d'insuffisance rénale aiguë (rapport de taux 1,31 ; 1,82 dans les 30 premiers jours), alors que la double association ne l'augmente pas ; la notice suisse de Brufen contre-indique l'ibuprofène sous une clairance de 30 ml/min et en cas d'insuffisance cardiaque sévère."),
("fall","hospitalizationComplications","complication",1,0,C67,"Les médicaments qui font chuter agissent par sédation, confusion, vertiges, hypotension orthostatique ou bradycardie : psychotropes surtout, diurétiques de l'anse, bêtabloquants non cardiosélectifs, digoxine ; ISRS, inhibiteurs de la pompe à protons, glucocorticoïdes et certains antiépileptiques fragilisent l'os."),
("surv","surveillance","décision",1,0,C67+" ; "+CG185,"Après une introduction ou un changement de dose, on informe et l'on surveille de plus près pendant les 2 premiers mois ; sous lithium, on contrôle la lithémie 1 semaine après chaque changement, puis tous les 3 mois chez la personne âgée, et la fonction rénale et thyroïdienne tous les 6 mois."),
("prog","prognosisDischarge","pronostic",1,1,C65+" ; "+CAU+" ; "+BEE,"Après l'arrêt du médicament en cause, le trouble régresse en général (hyponatrémie sous ISRS en 2 semaines environ), ce qui renforce l'imputabilité ; la mortalité hospitalière des hospitalisations dues à un effet indésirable atteint pourtant 2,2 % en Suisse."),
("pv","followUpNetwork","contexte suisse",1,1,SMC+" ; "+BEE+" ; "+C65,"En Suisse, tout professionnel qui prescrit ou remet des médicaments déclare à Swissmedic un effet grave (hospitalisation comprise) dans les 15 jours et un effet inconnu ou mal décrit non grave dans les 60 jours, sur simple suspicion ; seules 5 % des hospitalisations dues à un effet indésirable sont déclarées ; les centres régionaux de pharmacologie clinique et le CAPP des HUG conseillent le médecin."),
]
K = {k: i+1 for i, (k, *_r) in enumerate(_N)}
N = [t[1:] for t in _N]
n = lambda *ks: [K[k] for k in ks]
AM = ["Malaise, vertiges, chute ou confusion du sujet âgé : chercher d'abord dans la liste des médicaments.",
      "Chronologie : ajout ou changement de dose dans les 2 derniers mois, anti-inflammatoires achetés sans ordonnance.",
      "TA couchée et debout pendant 3 minutes, natrémie, kaliémie, créatinine comparée à la base, ECG si pouls lent.",
      "Hyponatrémie sous thiazidique : pas de SIADH sous diurétique, correction au plus 10 à 12 mmol/l par 24 heures.",
      "Lithium : signes neurologiques possibles même dans la cible ; diarrhée et anti-inflammatoires y exposent.",
      "Pas de médicament de plus pour un symptôme nouveau ; déclaration Swissmedic en 15 jours si hospitalisation."]
A = lambda *o: list(o)
Q = [
# 1 série S1, étape 1 (masquée)
{"f":"A","s":("S1",1,3),"st":"Une femme de 82 ans, qui vit seule à Neuchâtel, consulte son médecin de famille parce qu'elle « se sent mal » depuis 10 jours : fatigue, étourdissements en se levant, deux chutes sans perte de connaissance, et sa fille la trouve plus distraite. Il y a 3 semaines, un remplaçant a ajouté de l'hydrochlorothiazide 25 mg à son amlodipine ; elle prend aussi du citalopram 20 mg depuis 6 mois et de l'ibuprofène acheté en pharmacie pour ses genoux. Elle n'a ni fièvre ni signe neurologique focal.",
 "p":"Que faites-vous d'abord ?","o":A(
  (1,"Vous reprenez la chronologie de tout ce qu'elle prend, achats sans ordonnance compris, mesurez la TA couchée puis debout pendant 3 minutes et dosez natrémie, kaliémie et créatinine","Juste : l'ajout récent précède les symptômes ; orthostatisme et électrolytes se vérifient d'emblée (CAPP-INFO 65 et 67, Rev Med Suisse 2018)."),
  (0,"Vous demandez un CT cérébral en urgence","Faux : sans signe focal ni traumatisme crânien grave, l'imagerie ne précède pas la recherche des causes fréquentes et réversibles."),
  (0,"Vous faites un test de mémoire et introduisez du donépézil","Faux : une distraction récente avec chutes n'est pas une démence ; ajouter un médicament aggraverait le risque de chute et de bradycardie."),
  (0,"Vous prescrivez de la bétahistine pour les étourdissements","Faux : traiter le symptôme par un médicament de plus, sans chercher la cause dans la liste, crée une cascade de prescriptions."),
  (0,"Vous organisez d'abord un Holter de 24 heures","Faux : sans pouls lent ni palpitations, c'est un examen de second temps ; l'orthostatisme et la natrémie se vérifient au cabinet.")),
 "n":n("chrono","ortho","bilan","rf","nocasc"),"a":"application","d":4,"l":("Âgée, chutes, distraite depuis un ajout récent.","Diurétique et ISRS abaissent le sodium ; vasodilatation.","Étourdissement au lever, troubles de l'attention.","Délai plausible après l'ajout.","Chronologie, TA couchée-debout, ionogramme.","Imagerie ou médicament de plus.","Nouveau symptôme = relire la liste.")},
# 2 série S1, étape 2 (masquée)
{"f":"A","s":("S1",2,3),"st":"La TA est de 142/78 mmHg couchée et de 116/70 mmHg debout à 3 minutes ; la natrémie est à 124 mmol/l, la kaliémie à 3,3 mmol/l et la créatinine stable. Les muqueuses sont sèches, sans œdème. La glycémie est normale.",
 "p":"Quelle conduite retenez-vous ?","o":A(
  (1,"Vous l'hospitalisez, arrêtez l'hydrochlorothiazide, corrigez la volémie par du sérum salé isotonique et limitez la remontée de la natrémie à environ 9 mmol/l par 24 heures (au plus 10 à 12)","Juste : hyponatrémie hypovolémique sous thiazidique ; correction lente pour éviter la myélinolyse (CAPP-INFO 65)."),
  (0,"Vous donnez du NaCl 3 % en bolus répétés pour normaliser la natrémie en 24 heures","Faux : normaliser en un jour impose une remontée de 12 à 15 mmol/l, au-delà de la limite de 10 à 12 mmol/l, avec un risque de myélinolyse centropontine ; le NaCl 3 % se réserve à l'hyponatrémie aiguë."),
  (0,"Vous prescrivez une restriction hydrique à 800 ml par jour","Faux : la restriction vise l'hyponatrémie euvolémique ; ici les muqueuses sèches et l'orthostatisme signent une hypovolémie."),
  (0,"Vous retenez un SIADH et poursuivez le diurétique","Faux : un SIADH ne peut pas être retenu chez une patiente sous diurétique."),
  (0,"Vous remplacez l'hydrochlorothiazide par de l'indapamide","Faux : l'indapamide est un analogue thiazidique, qui figure parmi les causes les plus fréquentes d'hyponatrémie.")),
 "n":n("na","nacorr","stop","nadx"),"a":"piège","d":5,"l":("Sodium bas, déshydratation, orthostatisme.","Perte rénale de sodium sous thiazidique.","Muqueuses sèches, chute tensionnelle.","Hypovolémie, pas de SIADH sous diurétique.","Arrêter, isotonique, correction lente.","Correction rapide ou restriction hydrique.","Thiazidique + vieillesse = sodium à surveiller.")},
# 3 série S1, étape 3 (nomme le lien)
{"f":"A","m":0,"s":("S1",3,3),"st":"Une semaine après l'arrêt du diurétique, la natrémie est à 134 mmol/l, la patiente ne chute plus et se sent mieux. Elle est restée 4 jours à l'hôpital et aucune autre cause n'a été trouvée.",
 "p":"Que retenez-vous ?","o":A(
  (1,"Le lien est probable selon l'OMS-UMC (délai plausible, autre cause peu probable, évolution favorable à l'arrêt, sans réexposition nécessaire) et vous le déclarez à Swissmedic dans les 15 jours, car il a nécessité une hospitalisation","Juste : critères OMS-UMC ; une hospitalisation rend l'effet grave (Swissmedic)."),
  (0,"Seule une réexposition au diurétique permettrait de parler de lien probable","Faux : la catégorie « probable » de l'OMS-UMC n'exige pas de réexposition."),
  (0,"Vous ne déclarez rien, car l'effet est décrit dans la notice","Faux : un effet grave se déclare même s'il est connu ; seuls les effets non graves connus échappent à l'obligation."),
  (0,"Vous le déclarez dans les 60 jours","Faux : le délai de 60 jours vaut pour un effet non grave ; une hospitalisation impose 15 jours."),
  (0,"Vous attendez la certitude du lien avant de déclarer","Faux : la simple suspicion suffit pour déclarer à Swissmedic.")),
 "n":n("imput","pv","prog"),"a":"application","d":3,"l":("Amélioration à l'arrêt.","Effet réversible du médicament.","Sodium normalisé, plus de chute.","Délai, pas d'autre cause, arrêt favorable.","Classer et déclarer.","Attendre une réexposition ou la certitude.","Hospitalisation = grave = 15 jours.")},
# 4 lithium (masquée)
{"f":"A","st":"Un homme de 76 ans, suivi depuis 15 ans pour un trouble bipolaire stable sous lithium (Quilonorm retard), est amené par son épouse : depuis 3 jours, il tremble davantage, marche de façon instable et paraît confus. La semaine passée, il a eu des diarrhées pendant 4 jours et a pris de l'ibuprofène acheté en pharmacie pour un genou douloureux. La lithémie de ce matin est à 1,0 mmol/l.",
 "p":"Quelle est la conduite la plus juste ?","o":A(
  (1,"Vous suspendez le lithium et l'ibuprofène et l'adressez aux urgences pour évaluer l'hydratation, la fonction rénale et l'ionogramme, car ces signes neurologiques peuvent survenir même avec une lithémie dans la cible","Juste : NICE CG185 1.10.24 et 1.10.17–18 ; déshydratation et anti-inflammatoires exposent au lithium (CAPP-INFO 67, notice Quilonorm)."),
  (0,"Vous le rassurez, car la lithémie se situe dans la zone thérapeutique","Faux : piège du seuil ; tremblement, ataxie et confusion peuvent apparaître dans la cible, et 1,0 mmol/l dépasse la cible NICE de première intention (0,6–0,8)."),
  (0,"Vous ajoutez de l'halopéridol pour la confusion","Faux : on masque le tableau sans traiter la cause, et l'antipsychotique augmente le risque de chute."),
  (0,"Vous remplacez l'ibuprofène par du diclofénac","Faux : tout anti-inflammatoire est à éviter sous lithium (NICE CG185 1.10.18)."),
  (0,"Vous augmentez le lithium, car le tremblement annonce une rechute","Faux : tremblement accru, ataxie et confusion orientent vers un excès de lithium, pas vers une rechute thymique.")),
 "n":n("litox","lilev","rf","sick","stop"),"a":"piège","d":5,"l":("Tremblement, ataxie, confusion sous thymorégulateur.","Déshydratation et anti-inflammatoire réduisent l'élimination rénale.","Signes neurologiques récents.","Taux « normal » mais tableau clinique typique.","Suspendre et évaluer aux urgences.","Se fier à la lithémie.","La clinique prime sur le taux.")},
# 5 clarithromycine + anticalcique (masquée)
{"f":"A","st":"Une femme de 81 ans, traitée par amlodipine 10 mg pour une hypertension, reçoit depuis 4 jours de la clarithromycine 500 mg deux fois par jour pour une bronchite. Elle se sent faible et a des vertiges dès qu'elle se lève ; la TA est de 94/56 mmHg, le pouls de 92/min. La créatinine est passée de 80 à 135 µmol/l et la bandelette urinaire est normale.",
 "p":"Quelle est la meilleure conduite ?","o":A(
  (1,"Vous arrêtez la clarithromycine (azithromycine si un antibiotique reste nécessaire), suspendez temporairement l'amlodipine, réhydratez et contrôlez la créatinine","Juste : la clarithromycine inhibe le CYP3A4 et majore l'effet de l'anticalcique (Gandhi 2013) ; hausse de créatinine de plus de 50 % (NICE NG148)."),
  (0,"Vous ajoutez du furosémide pour relancer la diurèse","Faux : NICE NG148 1.5.3 déconseille le diurétique de l'anse pour traiter une insuffisance rénale aiguë, et il aggraverait l'hypotension."),
  (0,"Vous demandez une échographie rénale en urgence","Faux : NICE NG148 1.4.4 ne la propose pas d'office quand la cause est identifiée."),
  (0,"Vous poursuivez les deux traitements et ajoutez de la midodrine","Faux : on ajoute un médicament au lieu de lever une cause réversible."),
  (0,"Vous remplacez l'amlodipine par de la nifédipine","Faux : avec la clarithromycine, le risque est le plus élevé pour la nifédipine (OR 5,33).")),
 "n":n("cyp","aki","stop","bilan"),"a":"application","d":4,"l":("Vertiges, hypotension, créatinine en hausse sous antibiotique.","Inhibition du CYP3A4, anticalcique majoré.","Hypotension, insuffisance rénale aiguë.","Début récent du macrolide.","Arrêter, suspendre, réhydrater.","Diurétique ou échographie.","Macrolide + anticalcique = azithromycine.")},
# 6 triple association (masquée)
{"f":"A","st":"Un homme de 73 ans prend du lisinopril et de l'hydrochlorothiazide pour une hypertension. Depuis 10 jours, il prend 3 × 400 mg d'ibuprofène par jour, achetés en pharmacie pour une gonarthrose. Il consulte pour une grande fatigue et des nausées ; la créatinine est à 190 µmol/l (95 µmol/l il y a 4 mois), la kaliémie à 5,6 mmol/l, la bandelette urinaire est normale.",
 "p":"Que faites-vous ?","o":A(
  (1,"Vous arrêtez l'ibuprofène, suspendez temporairement le lisinopril et l'hydrochlorothiazide, corrigez l'hydratation et contrôlez de près créatinine et kaliémie","Juste : l'association diurétique, IEC et anti-inflammatoire augmente le risque d'insuffisance rénale aiguë, surtout au début (Lapi 2013 ; NICE NG148)."),
  (0,"Vous remplacez l'ibuprofène par du diclofénac","Faux : le diclofénac est aussi un anti-inflammatoire et garde le même effet rénal."),
  (0,"Vous ajoutez du furosémide","Faux : NICE NG148 ne recommande pas le diurétique de l'anse pour traiter l'insuffisance rénale aiguë."),
  (0,"Vous demandez une biopsie rénale","Faux : la cause est identifiée et la bandelette ne montre ni sang ni protéines (NICE NG148 1.4.3)."),
  (0,"Vous poursuivez tout et recontrôlez dans 3 mois","Faux : une créatinine doublée est une insuffisance rénale aiguë qui impose d'agir maintenant.")),
 "n":n("aki","sick","chrono","stop"),"a":"piège","d":4,"l":("Fatigue, créatinine doublée, kaliémie haute.","Prostaglandines et angiotensine maintiennent la filtration.","Nausées, insuffisance rénale aiguë.","Ajout récent d'un achat sans ordonnance.","Arrêter et suspendre.","Changer d'anti-inflammatoire.","Diurétique + IEC + anti-inflammatoire = rein en danger.")},
# 7 bradycardie (masquée)
{"f":"A","st":"Une femme de 84 ans, en EMS à Fribourg, reçoit du donépézil 10 mg pour une maladie d'Alzheimer et du métoprolol (Beloc Zok) 50 mg pour une hypertension. Depuis 2 semaines, elle a des vertiges, une grande fatigue, et elle a chuté hier avec une brève perte de connaissance. Le pouls est régulier à 44/min, la TA à 105/60 mmHg ; l'ECG montre une bradycardie sinusale sans bloc auriculoventriculaire de haut degré, l'ionogramme est normal.",
 "p":"Quelle conduite est la plus juste ?","o":A(
  (1,"Vous suspendez le métoprolol, réévaluez le donépézil avec le gériatre et surveillez rythme et TA avant de discuter un stimulateur","Juste : la notice suisse contre-indique le métoprolol sous 50/min ; l'inhibiteur de la cholinestérase peut causer une syncope par bradyarythmie (CAPP-INFO 67)."),
  (0,"Vous faites poser d'emblée un stimulateur cardiaque","Faux : on lève d'abord les causes réversibles de la bradycardie avant un geste définitif (avis d'expert)."),
  (0,"Vous augmentez le donépézil, car les chutes traduisent l'aggravation de la démence","Faux : 10 mg est la dose maximale, et le donépézil peut lui-même ralentir le cœur."),
  (0,"Vous remplacez le métoprolol par du propranolol","Faux : le propranolol ralentit aussi le cœur et appartient aux bêtabloquants non cardiosélectifs, associés à plus de chutes."),
  (0,"Vous ajoutez de la midodrine pour remonter la TA","Faux : on ajoute un médicament sans traiter la cause de la bradycardie.")),
 "n":n("brady","rf","chrono","fall","nocasc"),"a":"piège","d":5,"l":("Syncope, pouls à 44 sous deux freinateurs.","Bêtabloquant et cholinomimétique ralentissent le nœud sinusal.","Vertiges, chute, perte de connaissance.","Pas de bloc de haut degré, ionogramme normal.","Suspendre et réévaluer.","Stimulateur d'emblée.","Pouls lent = relire la liste avant le stimulateur.")},
# 8 orthostatisme (masquée)
{"f":"A","st":"Un homme de 81 ans consulte pour des étourdissements au lever depuis 3 semaines, avec une impression de « tête vide » et une grande fatigue le matin. Son urologue a ajouté de la tamsulosine il y a 1 mois ; il prend aussi de l'amlodipine. Après 5 minutes couché, la TA est de 152/86 mmHg ; debout, elle est de 134/82 mmHg à 1 minute et de 128/80 mmHg à 3 minutes, sans accélération notable du pouls.",
 "p":"Que retenez-vous ?","o":A(
  (1,"La baisse systolique de 24 mmHg à 3 minutes répond à la définition de l'hypotension orthostatique ; vous revoyez l'alpha-bloquant et l'antihypertenseur","Juste : baisse systolique d'au moins 20 mmHg en 3 minutes ; alpha-bloquants et dihydropyridines favorisent l'orthostatisme (Rev Med Suisse 2018)."),
  (0,"La mesure est normale, car la TA debout reste au-dessus de 120 mmHg","Faux : la définition repose sur la baisse, pas sur la valeur debout."),
  (0,"Seule une baisse diastolique compte pour retenir le diagnostic","Faux : une baisse systolique d'au moins 20 mmHg ou diastolique d'au moins 10 mmHg suffit."),
  (0,"Il faut un tilt-test avant toute conclusion","Faux : le test couché-debout suffit ici ; le tilt-test ne sert qu'à étayer un diagnostic incertain."),
  (0,"Vous ajoutez d'emblée de la fludrocortisone","Faux : on retire d'abord les médicaments en cause ; la fludrocortisone expose à l'hypokaliémie, aux œdèmes et à l'hypertension couchée.")),
 "n":n("ortho","chrono","start","nocasc"),"a":"piège","d":4,"l":("Étourdissement au lever après un ajout récent.","Vasodilatation alpha et calcique, baroréflexe émoussé.","Tête vide, fatigue matinale.","Baisse systolique de 24 mmHg à 3 minutes.","Revoir les vasodilatateurs.","Se fier à la valeur debout.","La baisse compte, pas la valeur.")},
# 9 épidémiologie
{"f":"A","m":0,"st":"Vous préparez un exposé sur les effets indésirables des médicaments dans les hôpitaux suisses.",
 "p":"Que montrent les données nationales de 2012 à 2019 ?","o":A(
  (1,"Environ 2,3 % des hospitalisations, soit près de 32 000 par an, étaient dues à un effet indésirable, dont près de la moitié chez des personnes de 65 ans ou plus","Juste : Beeler 2023, données de l'Office fédéral de la statistique."),
  (0,"Moins de 0,1 % des hospitalisations","Faux : la proportion mesurée est de 2,3 %."),
  (0,"Environ 25 % des hospitalisations","Faux : ce chiffre surestime largement la proportion nationale."),
  (0,"Environ 2,3 %, presque toutes déclarées à Swissmedic","Faux : seules 5 % environ de ces hospitalisations ont été déclarées, malgré l'obligation légale."),
  (0,"Environ 2,3 %, surtout chez les enfants","Faux : les enfants et adolescents représentaient 6,5 % des cas, les 65 ans ou plus 46,9 %.")),
 "n":n("epi","def","pv"),"a":"direct","d":2,"l":("Fréquence.","Réactions aux doses habituelles.","Hospitalisations.","2,3 % ; 5 % déclarés.","Connaître l'ampleur.","Croire tout déclaré.","Un séjour sur 40.")},
# 10 pharmacocinétique
{"f":"A","m":0,"st":"Une étudiante vous demande pourquoi les personnes âgées font plus souvent des effets indésirables.",
 "p":"Que lui expliquez-vous ?","o":A(
  (1,"Les clairances rénale et hépatique diminuent et le volume de distribution des médicaments liposolubles augmente, ce qui allonge leur demi-vie ; la sensibilité aux psychotropes, aux médicaments cardiovasculaires et aux anticoagulants augmente","Juste : Mangoni et Jackson 2004."),
  (0,"Le volume de distribution des liposolubles diminue, ce qui raccourcit leur demi-vie","Faux : il augmente avec l'âge et la demi-vie s'allonge."),
  (0,"La clairance rénale augmente avec l'âge","Faux : elle diminue."),
  (0,"La sensibilité aux psychotropes diminue avec l'âge","Faux : elle augmente le plus souvent."),
  (0,"Seule l'absorption digestive change ; le reste est stable","Faux : l'élimination rénale et hépatique et la distribution changent aussi.")),
 "n":n("pk","start"),"a":"direct","d":2,"l":("Vieillissement.","Clairance basse, distribution large.","Effets prolongés.","Demi-vie allongée.","Doses prudentes.","Croire la clairance plus élevée.","Lent à éliminer, sensible.")},
# 11 citalopram
{"f":"A","m":0,"st":"Une femme de 79 ans prend depuis des années du citalopram (Seropram) 40 mg par jour pour une dépression ; on lui a récemment prescrit un autre médicament qui allonge l'intervalle QT.",
 "p":"Que retenez-vous selon le résumé suisse ?","o":A(
  (1,"Après 65 ans, la dose se réduit de moitié, au maximum 20 mg par jour et l'association à un médicament qui allonge le QT est contre-indiquée (posologies à vérifier dans l'AIPS (Swissmedic))","Juste : Brevier de Seropram."),
  (0,"40 mg reste la dose maximale à tout âge","Faux : après 65 ans, le maximum est de 20 mg par jour."),
  (0,"La dose maximale après 65 ans est de 60 mg par jour","Faux : elle est de 20 mg par jour."),
  (0,"L'association à un médicament qui allonge le QT ne pose pas de problème","Faux : elle est contre-indiquée dans la notice suisse."),
  (0,"Vous arrêtez le citalopram brutalement le jour même","Faux : l'arrêt brutal d'un ISRS expose à des symptômes de sevrage ; on ramène la dose à 20 mg au plus.")),
 "n":n("cit","pk","start"),"a":"application","d":3,"l":("Dose d'ISRS chez la personne âgée.","Élimination ralentie, QT.","Risque de trouble du rythme.","Plus de 65 ans : 20 mg maximum.","Réduire progressivement.","Arrêt brutal.","Après 65 ans, moitié de dose.")},
# 12 clarithromycine et statine
{"f":"A","m":0,"st":"Un homme de 77 ans, sous simvastatine 40 mg et colchicine pour une goutte, doit recevoir un macrolide pour une infection respiratoire.",
 "p":"Que choisissez-vous ?","o":A(
  (1,"L'azithromycine plutôt que la clarithromycine, car la clarithromycine inhibe le CYP3A4 et la notice suisse de Klacid la contre-indique avec la simvastatine et la colchicine","Juste : Brevier de Klacid ; l'azithromycine n'inhibe pas le CYP3A4 (Gandhi 2013)."),
  (0,"La clarithromycine sans aucun changement","Faux : l'association avec la simvastatine et avec la colchicine est contre-indiquée."),
  (0,"La clarithromycine en arrêtant seulement la colchicine","Faux : la simvastatine est aussi contre-indiquée avec la clarithromycine."),
  (0,"La clarithromycine, car seuls les anticoagulants posent problème avec les macrolides","Faux : statines, colchicine, quétiapine, ticagrélor et anticalciques sont aussi concernés."),
  (0,"La clarithromycine à double dose pour raccourcir le traitement","Faux : doubler la dose augmente encore l'inhibition du CYP3A4 et dépasse la posologie de la notice.")),
 "n":n("klacid","cyp"),"a":"piège","d":3,"l":("Macrolide chez un patient sous statine.","Inhibition du CYP3A4.","Myopathie, toxicité de la colchicine.","Clarithromycine contre-indiquée.","Choisir l'azithromycine.","Ne regarder que les anticoagulants.","Clarithromycine + statine = non.")},
# 13 surveillance du lithium
{"f":"A","m":0,"st":"Un homme de 70 ans commence un traitement de lithium pour un trouble bipolaire.",
 "p":"Que retenez-vous de la surveillance ?","o":A(
  (1,"Lithémie 1 semaine après le début et après chaque changement de dose, cible NICE de 0,6 à 0,8 mmol/l en première prescription (0,5 à 1,0 mmol/l au long cours selon le résumé suisse de Quilonorm), puis contrôle tous les 3 mois chez la personne âgée","Juste : NICE CG185 1.10.15 et 1.10.20 ; Brevier de Quilonorm (discordance des cibles à signaler)."),
  (0,"Une lithémie par an suffit chez la personne âgée","Faux : NICE prévoit un contrôle tous les 3 mois chez la personne âgée."),
  (0,"La cible est de 1,5 à 2 mmol/l","Faux : ces valeurs dépassent toutes les cibles thérapeutiques citées."),
  (0,"Aucun contrôle n'est nécessaire après un changement de dose","Faux : NICE demande une lithémie 1 semaine après chaque changement de dose."),
  (0,"La fonction rénale ne se surveille pas sous lithium","Faux : NICE demande créatinine, DFGe et fonction thyroïdienne tous les 6 mois.")),
 "n":n("lilev","surv"),"a":"direct","d":3,"l":("Surveillance du lithium.","Élimination rénale, marge étroite.","Taux sanguin.","1 semaine, puis tous les 3 mois.","Doser régulièrement.","Un contrôle annuel.","Changement de dose = lithémie à 1 semaine.")},
# 14 OPERAM
{"f":"A","m":0,"st":"Un collègue affirme qu'une revue structurée des médicaments à l'hôpital suffit à éviter les réhospitalisations liées aux médicaments chez les patients âgés multimorbides.",
 "p":"Que montre l'essai OPERAM ?","o":A(
  (1,"L'intervention a réduit les prescriptions inappropriées, mais pas les hospitalisations liées aux médicaments à 12 mois (HR 0,95)","Juste : OPERAM, BMJ 2021."),
  (0,"Elle a réduit de moitié les hospitalisations liées aux médicaments","Faux : le hazard ratio était de 0,95, sans différence significative."),
  (0,"Elle a augmenté la mortalité","Faux : la mortalité ne différait pas significativement (HR 0,90)."),
  (0,"Les prescriptions inappropriées étaient rares, sous 10 %","Faux : 86,1 % des patients du groupe d'intervention en avaient."),
  (0,"Les patients prenaient en médiane 2 médicaments","Faux : la médiane était de 9 médicaments.")),
 "n":n("operam","epi"),"a":"piège","d":3,"l":("Essai européen à direction bernoise.","Optimiser ne suffit pas toujours.","Hospitalisations liées aux médicaments.","Prescriptions inappropriées réduites, hospitalisations non.","Garder le suivi clinique.","Croire la revue suffisante.","Moins d'erreurs ≠ moins d'hospitalisations.")},
# 15 Kprim hyponatrémie
{"f":"Kprim","m":0,"st":"Vous enseignez l'hyponatrémie liée aux médicaments chez la personne âgée.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"Sous ISRS, elle survient en général quelques semaines après le début et régresse environ 2 semaines après l'arrêt.","Vrai : CAPP-INFO 65."),
  (0,"Un SIADH peut être retenu chez une patiente qui prend un diurétique thiazidique.","Faux : le SIADH ne se retient qu'en l'absence de traitement diurétique."),
  (1,"Une hyperglycémie peut donner une fausse hyponatrémie.","Vrai : pseudo-hyponatrémie hyperosmolaire (CAPP-INFO 65)."),
  (1,"Même entre 120 et 130 mmol/l, elle s'accompagne souvent de troubles de l'attention, de l'équilibre et de chutes.","Vrai : CAPP-INFO 65.")),
 "n":n("na","nadx","nacorr"),"a":"direct","d":3,"l":("Sodium bas.","ADH et pertes rénales.","Chutes, attention.","ISRS, thiazidiques ; pas de SIADH sous diurétique.","Arrêter, corriger lentement.","SIADH sous diurétique.","Diurétique : pas de SIADH.")},
# 16 Kprim maladie aiguë et rein
{"f":"Kprim","m":0,"st":"Vous conseillez une femme de 72 ans avec une insuffisance rénale chronique (DFGe 45 ml/min/1,73 m²), traitée par un IEC et un diurétique.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"En cas de diarrhée ou de vomissements, on envisage de suspendre temporairement l'IEC jusqu'à stabilisation.","Vrai : NICE NG148 1.2.14."),
  (1,"On l'informe du risque des anti-inflammatoires achetés sans ordonnance.","Vrai : NICE NG148 1.6.4."),
  (0,"Une hausse de créatinine de 15 µmol/l en 48 heures suffit à définir une insuffisance rénale aiguë.","Faux : le seuil est d'au moins 26 µmol/l en 48 heures ou de 50 % en 7 jours."),
  (1,"Devant une maladie aiguë, on dose la créatinine et on la compare à la valeur de base.","Vrai : NICE NG148 1.1.1.")),
 "n":n("sick","aki","bilan"),"a":"direct","d":3,"l":("Jours de maladie.","Déshydratation et filtration.","Créatinine qui monte.","26 µmol/l en 48 heures.","Suspendre, informer.","Seuil trop bas.","Diarrhée = suspendre l'IEC.")},
# 17 Kprim imputabilité
{"f":"Kprim","m":0,"st":"Vous évaluez le lien entre un médicament et un trouble apparu sous traitement.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"Selon l'OMS-UMC, un lien probable n'exige pas de réexposition.","Vrai : critère « rechallenge not required »."),
  (1,"Selon l'OMS-UMC, le lien reste possible si une maladie ou un autre médicament peut aussi expliquer l'événement.","Vrai : catégorie « possible »."),
  (1,"Dans l'échelle de Naranjo, un score de 5 à 8 correspond à un effet probable.","Vrai : 5–8 = probable."),
  (0,"Dans l'échelle de Naranjo, l'amélioration après l'arrêt du médicament n'apporte aucun point.","Faux : elle rapporte 1 point.")),
 "n":n("imput","naranjo","prog"),"a":"direct","d":3,"l":("Imputabilité.","Délai, arrêt, réexposition.","Trouble sous traitement.","Probable sans réexposition.","Classer le lien.","Exiger la réexposition.","Délai + arrêt favorable = probable.")},
# 18 Kprim chutes
{"f":"Kprim","m":0,"st":"Vous revoyez les médicaments d'une personne âgée qui chute.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"Les psychotropes sont les médicaments les plus à risque de chute.","Vrai : CAPP-INFO 67."),
  (1,"La plupart des études associent davantage les diurétiques de l'anse que les thiazidiques au risque de chute.","Vrai : CAPP-INFO 67."),
  (0,"Les bêtabloquants cardiosélectifs forment le sous-groupe de bêtabloquants qui augmente le plus les chutes.","Faux : c'est le sous-groupe non cardiosélectif qui augmente le risque."),
  (1,"Un changement de traitement de moins de 2 mois justifie une information et une surveillance accrues.","Vrai : tableau d'optimisation du CAPP-INFO 67.")),
 "n":n("fall","surv","start"),"a":"direct","d":3,"l":("Chutes et médicaments.","Sédation, orthostatisme, bradycardie.","Chute.","Psychotropes, anse, non cardiosélectifs.","Réduire, surveiller.","Cardiosélectif.","Psychotropes d'abord.")},
# 19 menu long examens (masquée)
{"f":"MenuLong","st":"Un homme de 83 ans, autonome, consulte à Sion parce qu'il « n'est pas bien » depuis 2 semaines : asthénie, étourdissements, ralentissement. La dose de son comprimé pour le cœur a été augmentée il y a 10 jours ; il prend aussi un diurétique. Le pouls est à 48/min ; l'examen neurologique est normal.",
 "p":"Choisissez les TROIS examens à faire d'emblée.","o":A(
  (1,"Mesurer la TA couchée puis debout à 1 et 3 minutes","Juste : recherche d'une hypotension orthostatique (Rev Med Suisse 2018)."),
  (1,"Doser natrémie, kaliémie et créatinine en les comparant aux valeurs antérieures","Juste : diurétique et hausse de dose ; comparaison à la base (NICE NG148)."),
  (1,"Faire un ECG de repos","Juste : pouls à 48/min (avis d'expert)."),
  (0,"Demander un CT cérébral","Faux : l'examen neurologique est normal ; l'imagerie ne précède pas le bilan simple."),
  (0,"Demander une IRM cérébrale","Faux : aucun signe focal ne la justifie à ce stade."),
  (0,"Faire un EEG","Faux : rien n'évoque une crise d'épilepsie."),
  (0,"Faire une ponction lombaire","Faux : ni fièvre ni méningisme."),
  (0,"Doser la vitamine D","Faux : ce dosage n'explique pas le tableau aigu et n'est pas utile en routine (CAPP-INFO 67)."),
  (0,"Demander une coloscopie","Faux : aucun signe digestif ni anémie connue."),
  (0,"Demander une scintigraphie myocardique","Faux : aucun angor ; la bradycardie se documente d'abord par l'ECG."),
  (0,"Demander un PET-CT","Faux : aucun argument pour un cancer occulte à ce stade."),
  (0,"Doser les anticorps antinucléaires","Faux : aucun signe de maladie systémique.")),
 "n":n("bilan","ortho","rf","brady"),"a":"application","d":4,"l":("Âgé, pouls lent, hausse de dose récente.","Freinateur cardiaque et diurétique.","Asthénie, étourdissements.","Pouls à 48, orthostatisme possible.","TA couchée-debout, ionogramme, ECG.","Imagerie d'emblée.","Simple et ciblé d'abord.")},
# 20 menu long médicaments hyponatrémiants
{"f":"MenuLong","m":0,"st":"Une femme de 80 ans a une natrémie à 126 mmol/l. Sa liste comprend douze médicaments.",
 "p":"Choisissez les TROIS médicaments de sa liste les plus susceptibles d'expliquer l'hyponatrémie.","o":A(
  (1,"Hydrochlorothiazide","Juste : les thiazidiques figurent parmi les causes les plus fréquentes (CAPP-INFO 65)."),
  (1,"Citalopram","Juste : les ISRS provoquent un SIADH (CAPP-INFO 65)."),
  (1,"Carbamazépine","Juste : hyponatrémie chez 4,8 à 41,5 % des patients traités (CAPP-INFO 65)."),
  (0,"Atorvastatine","Faux : elle ne figure pas parmi les classes hyponatrémiantes du CAPP-INFO 65."),
  (0,"Apixaban","Faux : aucun lien connu avec l'hyponatrémie dans cette source."),
  (0,"Latanoprost en collyre","Faux : collyre sans lien connu avec l'hyponatrémie."),
  (0,"Alendronate","Faux : aucun lien connu avec l'hyponatrémie dans cette source."),
  (0,"Metformine","Faux : elle ne figure pas parmi les médicaments hyponatrémiants cités."),
  (0,"Allopurinol","Faux : aucun lien connu avec l'hyponatrémie dans cette source."),
  (0,"Carbonate de calcium","Faux : sans lien connu avec l'hyponatrémie."),
  (0,"Macrogol","Faux : le laxatif osmotique n'est pas cité parmi les causes."),
  (0,"Cholécalciférol","Faux : sans lien connu avec l'hyponatrémie.")),
 "n":n("na"),"a":"direct","d":3,"l":("Sodium bas.","Diurétique, SIADH.","Liste longue.","Thiazidique, ISRS, antiépileptique.","Cibler les suspects.","Accuser un médicament neutre.","Diurétique, ISRS, carbamazépine.")},
]
for _q in Q: _q["src"] = EXP
_SRC = {0:[C65,C67,RMS],1:[C65],2:[CAU,SMC],3:[CG185,QUI,C67],4:[GAN,NG148,KLA],5:[LAP,NG148,BRU,EXP],6:[BEL,C67,ARI,EXP],7:[RMS],8:[BEE],9:[MAN],10:[SER],11:[KLA,GAN],12:[CG185,QUI],13:[OPE],14:[C65],15:[NG148],16:[CAU],17:[C67],18:[RMS,NG148,C67,EXP],19:[C65]}
for i, s in _SRC.items(): Q[i]["src"] = s
C = {"theme":"Effet indésirable chez le sujet âgé polymédiqué vu par la sensation de maladie (porte G5) : présentation aspécifique (fatigue, vertiges, chute, confusion), chronologie et critères d'imputabilité OMS-UMC et Naranjo, TA couchée-debout et hypotension orthostatique, hyponatrémie sous thiazidique ou ISRS et sa correction, bradycardie sous bêtabloquant ou inhibiteur de la cholinestérase, lithium et signes neurologiques dans la cible, insuffisance rénale aiguë de la triple association et règles des jours de maladie, clarithromycine et CYP3A4, pharmacocinétique du grand âge, pas de cascade, données suisses (2,3 % des hospitalisations, OPERAM) et déclaration à Swissmedic",
 "notions":[
  {"titre":"Comprendre","rub":["definition","epidemiology","basicSciences","prognosisDischarge"],"comment":"L'effet indésirable du sujet âgé se cache derrière un malaise banal ; l'âge allonge la demi-vie et augmente la sensibilité.",
   "points":["2,3 % des hospitalisations en Suisse, dont près de la moitié après 65 ans.","Clarithromycine : inhibiteur du CYP3A4 ; azithromycine : non.","Régression à l'arrêt : argument d'imputabilité."],"sources":[BEE,MAN,GAN,SMC]},
  {"titre":"Reconnaître","rub":["anamnesis","clinicalExam","presumptionRedFlags","positiveDiagnosis"],"comment":"On relie le trouble à un ajout ou à un changement de dose récent, on mesure la TA couchée et debout et l'on classe le lien.",
   "arbre":[("d1",None,"Malaise, vertiges, chute ou confusion sous traitement","On reconstitue la chronologie de toute la liste.",None,None),("d2","d1","Baisse de TA au lever ou pouls lent","On revoit vasodilatateurs et freinateurs.",None,None),("d3","d1","Sodium bas ou créatinine en hausse","On cherche thiazidique, ISRS, anti-inflammatoire.",None,None),("d4","d1","Signes neurologiques sous lithium","On suspend et l'on évalue aux urgences.",None,None)],
   "points":["Hypotension orthostatique : baisse de 20/10 mmHg en 3 minutes.","OMS-UMC : probable sans réexposition.","Pas de SIADH sous diurétique."],"sources":[C67,RMS,CAU,C65]},
  {"titre":"Décider","rub":["workupGoldStandard","workupAlternatives","acuteManagement","chronicManagement"],"comment":"On fait un bilan simple, on suspend le suspect et l'on corrige prudemment, puis l'on prévient la récidive.",
   "tab":(["Situation","Conduite","Remarque"],[["Hyponatrémie sous thiazidique","Arrêt, isotonique si hypovolémie",[("HUG","Au plus 10 à 12 mmol/l par 24 heures.")]],["Lithium et signes neurologiques","Suspension, urgences",[("NICE","Possible dans la cible.")]],["Anticalcique et clarithromycine","Arrêt du macrolide",[("Suisse","Azithromycine en alternative.")]],["Diurétique, IEC et anti-inflammatoire","Arrêt de l'anti-inflammatoire, suspension temporaire",[("NICE","Créatinine comparée à la base.")]]]),
   "points":["Lithémie : NICE 0,6–0,8 ; Quilonorm 0,5–1,0 mmol/l.","Seropram après 65 ans : 20 mg au plus.","Pas de médicament de plus pour un symptôme nouveau."],"sources":[C65,CG185,NG148,QUI]},
  {"titre":"Suivre","rub":["hospitalizationComplications","surveillance","followUpNetwork"],"comment":"On surveille de près les deux premiers mois après un changement et l'on déclare les effets graves.",
   "points":["Triple association : risque rénal surtout le premier mois.","Déclaration Swissmedic : 15 jours si grave, 60 jours sinon.","Seules 5 % des hospitalisations dues à un effet indésirable sont déclarées."],"sources":[LAP,C67,SMC,BEE]}],
 "ssp":("G5","Sensation de maladie",True,[
   ("n1",None,"Malaise, vertiges, chute ou confusion chez une personne âgée traitée","On reconstitue la chronologie et l'on cherche les signes d'alerte.","eim","c2"),
   ("n2","n1","Signes d'alerte (syncope, pouls lent, confusion, insuffisance rénale aiguë)","On évalue en urgence et l'on suspend le médicament suspect.","eim","c3"),
   ("n3","n1","Baisse tensionnelle au lever","On revoit vasodilatateurs, alpha-bloquants et diurétiques.","eim","c3"),
   ("n4","n1","Hyponatrémie","On arrête le thiazidique ou l'ISRS et l'on corrige lentement.","eim","c3"),
   ("n5","n1","Créatinine en hausse","On arrête l'anti-inflammatoire et l'on suspend IEC et diurétique.","eim","c3"),
   ("n6","n2","Amélioration à l'arrêt","On classe le lien, on déclare à Swissmedic et l'on surveille.","eim","c4")]),
 "pec":[
  pec("eim","Effet indésirable chez le sujet âgé polymédiqué",["On identifie et l'on retire le médicament en cause en préservant les traitements utiles.","On prévient la récidive, les chutes et les hospitalisations évitables."],
      ["On fait apporter toutes les boîtes, y compris les achats sans ordonnance.","On mesure la TA couchée et debout et le pouls."],
      [("Chlorure de sodium 0,9 % (sérum salé isotonique)","Hyponatrémie hypovolémique : perfusion adaptée à la volémie, natrémie remontée d'au plus 9 mmol/l par 24 heures (maximum 10 à 12) ; posologies à vérifier dans l'AIPS (Swissmedic)","Il restaure la volémie et corrige le sodium sans risque de correction trop rapide.",C65),
       ("Lithium (Quilonorm retard 12,2 mmol)","Reprise éventuelle selon la lithémie : 0,5 à 1,0 mmol/l au long cours selon le résumé suisse, 0,6 à 0,8 mmol/l selon NICE en première prescription ; posologies à vérifier dans l'AIPS (Swissmedic)","Il garde la stabilisation de l'humeur si la cause de l'excès est corrigée et la surveillance assurée.",QUI+" ; "+CG185),
       ("Citalopram (Seropram)","Après 65 ans : moitié de la dose au maximum 20 mg par jour ; posologies à vérifier dans l'AIPS (Swissmedic)","Il reste utile pour la dépression à une dose adaptée qui limite le risque de QT long et d'hyponatrémie.",SER)],
      [("éducation thérapeutique","On explique les règles en cas de diarrhée, de vomissements ou de fièvre et le danger des anti-inflammatoires achetés sans ordonnance.","On prévient l'insuffisance rénale aiguë et l'excès de lithium."),("soins infirmiers","On surveille TA couchée-debout, pouls, chutes et vigilance après chaque changement.","On repère tôt la récidive.")],
      [("O Pharmacologie Toxicologie Sécurité","On classe le lien selon l'OMS-UMC et l'on demande un avis de pharmacologie clinique si le cas est complexe."),("F Droit médical suisse","On déclare à Swissmedic tout effet grave dans les 15 jours, selon la loi sur les produits thérapeutiques."),("P Qualité Sécurité Gestion de l'erreur","On revoit la liste à chaque transition de soins pour éviter les doublons et les associations à risque.")],
      (["On évalue les signes vitaux.","On suspend le médicament suspect.","On corrige volémie et électrolytes."],[("d'abord","médecin d'urgence","Il évalue TA, pouls, vigilance, ionogramme, créatinine et ECG."),("ensuite","médecin hospitalier","Il suspend le médicament suspect et corrige volémie et natrémie lentement."),("puis","pharmacien clinicien","Il revoit toute la liste et propose les adaptations à la fonction rénale.")]),
      (["On reprend la chronologie.","On simplifie.","On revoit."],[("d'abord","médecin de famille","Il relie le trouble à l'ajout récent et suspend ou réduit le médicament."),("ensuite","pharmacien d'officine","Il vérifie achats sans ordonnance, doublons et associations à risque."),("puis","médecin de famille","Il revoit la personne après le changement et déclare l'effet grave à Swissmedic.")]),
      "Le trouble régresse en général après l'arrêt du médicament en cause, mais les hospitalisations dues à un effet indésirable gardent une mortalité de 2,2 % en Suisse.",
      [("TA couchée-debout et pouls","À chaque consultation après un changement","Pas de baisse orthostatique, pouls de 50/min ou plus"),("Natrémie et créatinine","Quelques jours après l'arrêt ou le changement","Retour aux valeurs de base"),("Lithémie","1 semaine après chaque changement, puis tous les 3 mois après 65 ans","Dans la cible prescrite")],"La personne repart avec une liste à jour, les règles des jours de maladie et un contrôle planifié.",
      ("On commence chaque médicament à la plus petite dose et l'on adapte à la fonction rénale.","On cherche un effet indésirable devant tout malaise, chute ou confusion d'une personne âgée traitée.","On évite la réexposition, on documente l'effet et on le déclare à Swissmedic.")),]}
