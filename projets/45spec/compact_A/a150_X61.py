from constructeur_agent_45spec import pec
ID = "X61__G13-E04"
PLAN = "non_monographique"
OBS = "[Obsan, bulletin 8/2024 « Suicides et tentatives de suicide en Suisse », 23.09.2024, PDF obsan.admin.ch lu le 25.11.2026]"
VD = "[Direction générale de la santé du canton de Vaud, fiche INTER_TECH « Décès de cause non naturelle ou indéterminée », janvier 2022, PDF vd.ch lu le 25.11.2026]"
HUG = "[HUG, SMUR, protocole 1.5 « Décès », version 2.1 du 19.02.2013, PDF hug.ch lu le 25.11.2026]"
NICE = "[NICE NG225, Self-harm: assessment, management and preventing recurrence, 2022, chapitre « Rationale and impact », nice.org.uk lu le 25.11.2026]"
CAR = "[Carroll R, Metcalfe C, Gunnell D, Hospital presenting self-harm and risk of fatal and non-fatal repetition: systematic review and meta-analysis, PLoS One 2014;9:e89944, PMID 24587141, résumé lu le 25.11.2026]"
HAW = "[Hawton K et al., Long term effect of reduced pack sizes of paracetamol on poisoning deaths and liver transplant activity in England and Wales, BMJ 2013;346:f403, PMID 23393081, résumé lu le 25.11.2026]"
ASS = "[Gysin-Maillart A et al., A Novel Brief Therapy for Patients Who Attempt Suicide: ASSIP, PLoS Med 2016;13:e1001968, PMID 26930055, résumé lu le 25.11.2026]"
BE = "[APEA du canton de Berne (KESB), notice 066 « Mesures de protection de l'adulte » pour les professionnels de la santé, PDF kesb.dij.be.ch lu le 25.11.2026]"
EXP = "Avis d'expert, médecine légale et psychiatrie (à vérifier)"
_N = [
("def","definition","critère",2,0,VD,"Un décès est de cause non naturelle quand il résulte d'un accident, d'un suicide (assisté compris) ou de l'action d'un tiers."),
("indet","definition","critère",1,0,VD,"Un décès est d'origine indéterminée quand une cause non naturelle est incertaine mais ne peut pas être exclue."),
("epi","epidemiology","chiffre",3,0,OBS,"En 2022, 958 personnes se sont suicidées en Suisse (hors suicide assisté), soit 11,0 pour 100 000 habitants ; le taux des hommes est environ trois fois celui des femmes."),
("methods","epidemiology","chiffre",2,0,OBS,"En 2022, les femmes se sont suicidées surtout par pendaison (27,8 %) et par empoisonnement (20,2 %) ; les hommes par pendaison (29,1 %) et par arme à feu (27,2 %)."),
("attempts","epidemiology","chiffre",1,0,OBS,"En 2022, 14 137 hospitalisations ont suivi une tentative de suicide présumée ; le taux des jeunes femmes de 15 à 19 ans a atteint 9,5 pour 1000."),
("riskfactor","basicSciences","terrain particulier",1,0,CAR,"Un geste auto-agressif non mortel est le facteur de risque le plus fort d'un suicide ultérieur."),
("hx","anamnesis","décision",1,0,EXP,"Après un geste, on explore l'intention, la préparation, une lettre, les précautions contre la découverte et le regret d'avoir survécu (à vérifier)."),
("scene","clinicalExam","examen",1,0,HUG,"Sur les lieux, le médecin cherche des substances toxiques (alcool, drogues, médicaments), des signes de violence ou d'effraction et note si les portes étaient fermées."),
("cert","positiveDiagnosis","contexte suisse",3,1,VD,"Devant un décès non naturel ou indéterminé, le médecin demande l'avis du médecin légiste de garde, coche « mort non naturelle » ou « mort d'origine indéterminée » sur le certificat et fait venir la police."),
("ddx","positiveDiagnosis","diagnostic différentiel",1,0,VD,"Quand on ne peut pas exclure un accident ou l'intervention d'un tiers, on coche « mort d'origine indéterminée » plutôt que de trancher seul."),
("curml","workupGoldStandard","décision",2,0,VD,"En cas de désaccord, l'avis du médecin légiste prévaut ; la police informe le ministère public, qui décide de l'examen médico-légal."),
("tox","workupAlternatives","examen",1,0,EXP,"L'autopsie et les analyses toxicologiques post-mortem sont ordonnées par le ministère public (à vérifier)."),
("redflag","presumptionRedFlags","signe",2,0,EXP,"Une lettre d'adieu, un geste préparé, le refus de soins et l'annonce d'une récidive signalent un danger élevé (à vérifier)."),
("nice","presumptionRedFlags","piège",3,0,NICE,"Les outils et échelles de risque ne prédisent pas le suicide ni la récidive ; on ne classe pas le patient en risque faible, moyen ou élevé pour décider des soins ou de la sortie."),
("psa","acuteManagement","décision",2,0,NICE,"Toute personne qui s'est fait du mal reçoit une évaluation psychosociale ; le traitement somatique ne doit pas servir à la retarder ou à la refuser."),
("pafa","acuteManagement","contexte suisse",3,1,BE,"Un médecin habilité peut ordonner un placement à des fins d'assistance pour six semaines au plus (art. 429 CC) quand un trouble psychique exige une assistance impossible en ambulatoire ; le recours est possible dans les dix jours."),
("trust","acuteManagement","contexte suisse",1,1,BE,"La personne placée peut faire appel à une personne de confiance de son choix (art. 432 CC) ; elle est entendue avant la décision."),
("release","hospitalizationComplications","décision",1,0,VD,"Le corps n'est remis aux pompes funèbres qu'après l'autorisation écrite du ministère public."),
("bereave","hospitalizationComplications","prévention",1,0,OBS,"Le suivi des personnes qui ont perdu un proche par suicide fait partie des mesures encore nécessaires en Suisse."),
("assip","chronicManagement","décision",2,0,ASS,"L'ASSIP bernois ajoute trois séances et des lettres pendant 24 mois : 8,3 % de récidive contre 26,7 %, soit un risque réduit d'environ 80 %."),
("safety","chronicManagement","décision",1,0,NICE,"On élabore un plan de sécurité avec la personne, on lui en remet une copie et on le partage avec ses proches quand c'est approprié."),
("presc","chronicManagement","prévention",2,0,NICE,"On tient compte de la toxicité des médicaments prescrits et de l'accès aux autres médicaments pour limiter le risque d'ingestion massive."),
("carroll","prognosisDischarge","chiffre",2,0,CAR,"Après un geste auto-agressif, 16,3 % récidivent dans l'année ; 1,6 % meurent par suicide en un an et 3,9 % en cinq ans, soit un patient sur 25."),
("after48","surveillance","décision",2,0,NICE,"On assure un suivi dans les 48 heures si des inquiétudes persistent, car la récidive survient surtout dans les 2 à 3 jours."),
("surv2","surveillance","décision",1,0,NICE,"Quand la personne ne peut pas encore participer à l'évaluation, on la revoit régulièrement pour la faire dès que possible."),
("plan","followUpNetwork","contexte suisse",1,1,OBS,"La Suisse a lancé en 2016 un plan d'action national pour la prévention du suicide."),
("means","followUpNetwork","prévention",1,0,OBS,"Limiter l'accès aux moyens de suicide aide à réduire et à stabiliser le taux de suicide."),
("hawton","followUpNetwork","chiffre",1,0,HAW,"Au Royaume-Uni, la réduction des emballages de paracétamol a été suivie de 43 % de décès en moins par ce produit en 11 ans."),
]
K = {k: i+1 for i, (k, *_r) in enumerate(_N)}
N = [t[1:] for t in _N]
n = lambda *ks: [K[k] for k in ks]
AM = ["Ne jamais certifier « mort naturelle » sous la pression de la famille.","Échelle de risque basse ne permet pas la sortie.","Évaluation psychosociale pour tous.","Suivi dans les 48 heures.","PAFA possible même chez un patient lucide.","Limiter les quantités prescrites."]
A = lambda *o: list(o)
Q = [
{"f":"A","s":("S1",1,3),"st":"Médecin de garde, vous êtes appelé chez une femme de 54 ans trouvée morte dans son lit. Le corps est rigide ; plusieurs plaquettes vides et une lettre adressée à sa fille sont sur la table de nuit. Le mari vous demande de signer vite une « mort naturelle » pour éviter la police.",
 "p":"Que faites-vous ?","o":A((1,"Demander l'avis du médecin légiste de garde, cocher une mort non naturelle et faire venir la police","VD 2022."),(0,"Signer une mort naturelle, faute de signe de violence","Piège."),(0,"Signer une mort d'origine cardiaque probable","Faux."),(0,"Laisser le mari appeler les pompes funèbres","Faux."),(0,"Partir sans certificat","Faux.")),
 "n":n("cert","def","curml"),"a":"piège","d":4,"l":("Décès.","Cause externe.","Plaquettes, lettre.","Non naturel.","Légiste, police.","Mort naturelle.","Non naturel : police.")},
{"f":"A","s":("S1",2,3),"st":"En attendant la police, la fille veut jeter les plaquettes et la lettre « pour protéger sa mère ».",
 "p":"Que lui répondez-vous ?","o":A((1,"Laisser tout en place pour l'enquête, en expliquant la démarche avec tact","HUG 2013 ; Expert."),(0,"Accepter, par respect du deuil","Faux."),(0,"Emporter vous-même les plaquettes à l'hôpital","Faux."),(0,"Laver les verres et ranger la chambre","Faux."),(0,"Photographier puis jeter","Faux.")),
 "n":n("scene","tox"),"a":"application","d":3,"l":("Lieux.","Preuves.","Plaquettes.","Enquête.","Préserver.","Ranger.","Ne rien déplacer.")},
{"f":"A","s":("S1",3,3),"st":"Le ministère public autorise la remise du corps. Le mari est effondré et dit qu'il « aurait dû voir venir ».",
 "p":"Quelle mesure lui proposez-vous ?","o":A((1,"Un soutien et un suivi pour les proches endeuillés","Obsan 2024."),(0,"Aucune, le deuil est normal","Faux."),(0,"Un hypnotique pour un mois","Faux."),(0,"Une hospitalisation immédiate","Faux."),(0,"Un certificat d'aptitude","Faux.")),
 "n":n("bereave","release"),"a":"application","d":3,"l":("Deuil.","Culpabilité.","Effondré.","Proches.","Soutenir.","Rien.","Suivre les proches.")},
{"f":"A","st":"Une étudiante de 19 ans a pris tous ses comprimés après une rupture. Elle est somatiquement stable, dit que c'était « un appel à l'aide » et veut rentrer. L'interne a rempli une échelle de risque au score bas et propose la sortie.",
 "p":"Quelle est la bonne conduite ?","o":A((1,"Faire une évaluation psychosociale complète avant toute décision, sans se fier au score","NICE NG225."),(0,"Laisser partir, puisque le score est bas","Piège : les échelles ne prédisent pas."),(0,"Garder 24 heures sans évaluation","Faux."),(0,"Prescrire un somnifère et la laisser partir","Faux."),(0,"Ordonner un PAFA d'emblée","Faux.")),
 "n":n("nice","psa","riskfactor","hx","carroll"),"a":"piège","d":5,"l":("Geste.","Risque.","Score bas.","Échelles inutiles.","Évaluer.","Score.","Évaluation psychosociale.")},
{"f":"A","st":"Un homme de 35 ans quitte l'hôpital après avoir avalé ses comprimés lors d'une crise. Il accepte un suivi ambulatoire. Vous cherchez l'intervention brève dont l'efficacité sur la récidive a été montrée à Berne.",
 "p":"Laquelle proposez-vous ?","o":A((1,"Trois séances centrées sur le patient suivies de lettres régulières pendant deux ans","ASSIP 2016."),(0,"Une seule consultation sans suivi","Faux."),(0,"Un contrat de non-suicide signé","Piège."),(0,"Une échelle de risque mensuelle seule","Faux."),(0,"Un hypnotique au long cours","Faux.")),
 "n":n("assip","carroll","safety"),"a":"application","d":4,"l":("Après la crise.","Alliance.","Suivi.","Lettres.","Proposer.","Contrat.","Séances et lettres.")},
{"f":"A","st":"Un homme de 60 ans, déprimé, a été hospitalisé l'an dernier après avoir avalé ses comprimés. Son médecin de famille veut lui prescrire un antidépresseur tricyclique pour trois mois en une seule boîte, « pour simplifier ».",
 "p":"Que lui conseillez-vous ?","o":A((1,"Choisir un produit moins toxique et limiter les quantités remises","NICE NG225 (1.13)."),(0,"Garder la boîte de trois mois pour l'observance","Piège."),(0,"Ne rien prescrire du tout","Faux."),(0,"Doubler la dose","Faux."),(0,"Laisser sa femme gérer sans en parler","Faux.")),
 "n":n("presc","means","hawton","methods"),"a":"piège","d":4,"l":("Antécédent.","Toxicité.","Boîte de 3 mois.","Accès.","Limiter.","Observance.","Moins toxique, moins de boîtes.")},
{"f":"A","st":"Un homme de 45 ans a avalé ses médicaments hier ; il est maintenant éveillé, orienté et lucide. Atteint d'une dépression sévère, il refuse tout soin et annonce qu'il « recommencera dès ce soir ».",
 "p":"Quelle mesure est possible ?","o":A((1,"Un placement à des fins d'assistance ordonné par un médecin habilité, pour six semaines au plus","Art. 426 et 429 CC (Berne)."),(0,"Aucune, puisqu'il est lucide","Piège : le trouble psychique et le danger suffisent."),(0,"Attendre la décision de l'APEA dans un mois","Faux."),(0,"Une contention sans décision","Faux."),(0,"Une curatelle de portée générale","Faux.")),
 "n":n("pafa","redflag","trust"),"a":"piège","d":5,"l":("Refus.","Danger.","Récidive annoncée.","PAFA.","Placer.","Lucidité.","PAFA ≤ 6 semaines.")},
{"f":"A","m":0,"st":"Vous présentez les chiffres suisses du suicide.",
 "p":"Combien de suicides (hors suicide assisté) ont été enregistrés en Suisse en 2022 ?","o":A((1,"Environ 960 (958)","Obsan 2024."),(0,"Environ 96","Faux."),(0,"Environ 9600","Faux."),(0,"Environ 300","Faux."),(0,"Environ 30 000","Faux.")),
 "n":n("epi"),"a":"direct","d":1,"l":("Chiffre.","Mortalité.","2022.","958.","Retenir.","9600.","Près de 1000.")},
{"f":"A","m":0,"st":"Vous comparez les suicides des hommes et des femmes en Suisse en 2022.",
 "p":"Quelle affirmation est juste ?","o":A((1,"Le taux des hommes est environ trois fois celui des femmes","Obsan 2024 : 16,2 contre 5,8."),(0,"Les taux sont égaux","Faux."),(0,"Les femmes se suicident plus","Faux."),(0,"Les hommes utilisent d'abord l'empoisonnement","Faux."),(0,"Le taux augmente depuis 1998","Faux.")),
 "n":n("epi","methods"),"a":"direct","d":2,"l":("Sexe.","Taux.","Hommes.","Trois fois.","Comparer.","Égalité.","Hommes × 3.")},
{"f":"A","m":0,"st":"Vous défendez une limitation des emballages de médicaments pour prévenir les intoxications volontaires mortelles.",
 "p":"Quel résultat de l'étude britannique de Hawton citez-vous ?","o":A((1,"43 % de décès en moins par paracétamol en 11 ans","Hawton 2013."),(0,"Aucun effet","Faux."),(0,"Une hausse des décès","Faux."),(0,"Une baisse de 5 %","Faux."),(0,"Une baisse de 90 %","Faux.")),
 "n":n("hawton","means"),"a":"direct","d":3,"l":("Preuve.","Accès.","Emballages.","43 %.","Prévenir.","Aucun effet.","Limiter l'accès.")},
{"f":"A","m":0,"st":"Une mère demande quel est le risque de décès de sa fille, vue aux urgences pour une intoxication médicamenteuse volontaire.",
 "p":"Que retient la méta-analyse de Carroll ?","o":A((1,"Environ un patient sur 25 meurt par suicide dans les cinq ans","Carroll 2014 : 3,9 %."),(0,"Aucun risque après un appel à l'aide","Faux."),(0,"Un patient sur deux","Faux."),(0,"Un patient sur 1000","Faux."),(0,"Le risque disparaît après un mois","Faux.")),
 "n":n("carroll","riskfactor","epi"),"a":"application","d":3,"l":("Pronostic.","Récidive.","Cinq ans.","3,9 %.","Informer.","Aucun risque.","Un sur 25.")},
{"f":"A","m":0,"st":"Vous lisez le bulletin Obsan 2024 sur les tentatives de suicide.",
 "p":"Quelle tendance est juste ?","o":A((1,"Le taux d'hospitalisation des jeunes femmes de 15 à 19 ans a nettement augmenté entre 2017 et 2022","Obsan 2024 : 3,8 → 9,5 pour 1000."),(0,"Les tentatives ont disparu","Faux."),(0,"Les hommes sont plus hospitalisés","Faux."),(0,"Aucune donnée n'existe","Faux."),(0,"Les adolescentes sont épargnées","Faux.")),
 "n":n("attempts"),"a":"direct","d":2,"l":("Tendance.","Jeunes.","15–19 ans.","9,5 ‰.","Lire.","Hommes.","Jeunes femmes en hausse.")},
{"f":"A","m":0,"st":"Vous avez coché « mort non naturelle » après une intoxication médicamenteuse volontaire mortelle dans le canton de Vaud.",
 "p":"Qui décide de l'examen médico-légal ?","o":A((1,"Le ministère public, informé par la police","VD 2022."),(0,"La famille","Faux."),(0,"Le médecin de famille","Faux."),(0,"Les pompes funèbres","Faux."),(0,"L'assurance-maladie","Faux.")),
 "n":n("curml","release","tox"),"a":"direct","d":3,"l":("Procédure.","Justice.","Non naturel.","Ministère public.","Décider.","Famille.","Ministère public.")},
{"f":"A","m":0,"st":"Une patiente sort des urgences après une intoxication médicamenteuse volontaire ; des inquiétudes persistent.",
 "p":"Dans quel délai organisez-vous le suivi ?","o":A((1,"Dans les 48 heures","NICE NG225."),(0,"Dans trois mois","Faux."),(0,"Aucun suivi","Faux."),(0,"Dans un mois","Faux."),(0,"Seulement si elle rappelle","Faux.")),
 "n":n("after48","surv2"),"a":"direct","d":2,"l":("Suivi.","Récidive précoce.","Sortie.","48 heures.","Organiser.","Trois mois.","48 h.")},
{"f":"Kprim","m":0,"st":"Vous évaluez un patient après une intoxication médicamenteuse volontaire.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"Les échelles de risque ne prédisent pas le suicide.","NICE NG225."),(1,"On ne classe pas le risque en faible, moyen ou élevé pour décider de la sortie.","NICE NG225."),(1,"Le traitement somatique ne doit pas retarder l'évaluation psychosociale.","NICE NG225."),(0,"Un score bas permet la sortie sans évaluation.","Faux.")),
 "n":n("nice","psa","surv2"),"a":"direct","d":3,"l":("Évaluation.","Prédiction.","Échelles.","Stratification.","Évaluer.","Score bas.","Pas d'échelle.")},
{"f":"Kprim","m":0,"st":"Vous lisez les données suisses 2022 sur le suicide.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"Le taux standardisé était de 11,0 pour 100 000.","Obsan 2024."),(1,"Chez les hommes, pendaison et armes à feu dominent.","Obsan 2024."),(1,"Chez les femmes, l'empoisonnement représente 20,2 %.","Obsan 2024."),(0,"Chez les femmes, l'empoisonnement est la première méthode.","Faux : pendaison 27,8 %.")),
 "n":n("methods","epi","plan"),"a":"direct","d":2,"l":("Données.","Méthodes.","11,0.","20,2 %.","Lire.","Première méthode.","Pendaison d'abord.")},
{"f":"Kprim","m":0,"st":"Vous constatez le décès d'une personne après une intoxication médicamenteuse volontaire, dans le canton de Vaud.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"Un suicide est une mort non naturelle.","VD 2022."),(1,"Si une cause externe est incertaine, on coche « mort d'origine indéterminée ».","VD 2022."),(1,"En cas de désaccord, l'avis du médecin légiste prévaut.","VD 2022."),(0,"On peut cocher « mort naturelle » si la famille le demande.","Faux.")),
 "n":n("cert","ddx","indet","def"),"a":"application","d":3,"l":("Certificat.","Catégories.","Indéterminé.","Légiste.","Certifier.","Famille.","Non naturel.")},
{"f":"Kprim","m":0,"st":"Vous présentez l'essai bernois ASSIP après une tentative de suicide.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A((1,"Il comporte trois séances de thérapie.","ASSIP 2016."),(1,"Des lettres personnalisées suivent pendant 24 mois.","ASSIP 2016."),(1,"La récidive passe de 26,7 % à 8,3 %.","ASSIP 2016."),(0,"Il excluait les patients atteints d'un trouble de l'humeur.","Faux : 63 % en avaient un.")),
 "n":n("assip","safety"),"a":"direct","d":3,"l":("Essai.","Alliance.","Trois séances.","Lettres.","Proposer.","Exclusion.","ASSIP.")},
{"f":"MenuLong","st":"Appelé de nuit, vous constatez le décès d'un homme de 70 ans seul chez lui, entouré de boîtes de médicaments ouvertes et d'une bouteille d'alcool.",
 "p":"Choisissez les TROIS actions justes.","o":A((1,"Demander l'avis du médecin légiste de garde","VD 2022."),(1,"Faire venir la police","VD 2022."),(1,"Cocher « mort non naturelle » ou « mort d'origine indéterminée »","VD 2022."),(0,"Cocher « mort naturelle » vu l'âge","Faux."),(0,"Ranger les boîtes pour la famille","Faux."),(0,"Appeler d'abord les pompes funèbres","Faux."),(0,"Déplacer le corps sur le lit","Faux."),(0,"Partir avant l'arrivée de la police","Faux."),(0,"Jeter l'alcool","Faux."),(0,"Signer une cause cardiaque","Faux."),(0,"Remettre le corps sans autorisation","Faux."),(0,"Rédiger un certificat d'aptitude","Faux.")),
 "n":n("cert","curml","scene","release"),"a":"piège","d":4,"l":("Décès.","Cause externe.","Boîtes.","Légiste.","Police.","Âge.","Légiste, police, non naturel.")},
{"f":"MenuLong","m":0,"st":"Vous préparez la sortie d'une patiente après une intoxication médicamenteuse volontaire non mortelle.",
 "p":"Choisissez les TROIS éléments justes du plan de sortie.","o":A((1,"Un plan de sécurité élaboré avec elle, dont elle garde une copie","NICE NG225."),(1,"Un suivi dans les 48 heures","NICE NG225."),(1,"Une limitation des médicaments à domicile","NICE NG225 ; Obsan."),(0,"Un score de risque pour décider seul","Faux."),(0,"Un contrat de non-suicide seul","Faux."),(0,"Une ordonnance de trois mois d'un tricyclique","Faux."),(0,"Aucune information aux proches, même si elle le souhaite","Faux."),(0,"Un rendez-vous dans six mois","Faux."),(0,"Un somnifère en grande boîte","Faux."),(0,"Une sortie sans évaluation","Faux."),(0,"Un arrêt de tout suivi","Faux."),(0,"Un PAFA systématique après tout geste","Faux : il exige un trouble psychique et une assistance impossible en ambulatoire.")),
 "n":n("safety","after48","presc","means","redflag","pafa"),"a":"application","d":3,"l":("Sortie.","Récidive.","Plan.","48 h.","Protéger.","Score.","Plan, 48 h, moyens.")},
]
for _q in Q: _q["src"] = NICE
Q[0]["src"] = VD; Q[1]["src"] = [HUG, EXP]; Q[2]["src"] = OBS; Q[4]["src"] = ASS; Q[6]["src"] = BE; Q[7]["src"] = OBS; Q[8]["src"] = OBS
Q[9]["src"] = HAW; Q[10]["src"] = CAR; Q[11]["src"] = OBS; Q[12]["src"] = VD; Q[15]["src"] = OBS; Q[16]["src"] = VD; Q[17]["src"] = ASS; Q[18]["src"] = VD; Q[19]["src"] = [NICE, OBS]
C = {"theme":"Intoxication médicamenteuse volontaire mortelle et geste non mortel : mort non naturelle (légiste, police, ministère public), préservation des lieux, soutien des proches, 958 suicides en Suisse en 2022, évaluation psychosociale sans échelle de risque, PAFA, suivi dans les 48 heures, plan de sécurité, ASSIP et limitation des moyens",
 "notions":[
  {"titre":"Comprendre","rub":["definition","epidemiology","basicSciences","anamnesis"],"comment":"Le suicide est une mort non naturelle ; un geste non mortel est le principal facteur de risque d'un suicide ultérieur.",
   "points":["958 suicides en 2022.","Hommes × 3."],"sources":[VD,OBS,CAR]},
  {"titre":"Constater ou évaluer","rub":["clinicalExam","presumptionRedFlags","workupGoldStandard","workupAlternatives"],"comment":"Devant un décès, on appelle le légiste et la police ; devant un survivant, on évalue sans échelle de risque.",
   "arbre":[("d1",None,"Personne trouvée après une ingestion de médicaments","On distingue le décès du survivant.",None,None),("d2","d1","Décès","On demande l'avis du légiste, on coche une mort non naturelle et l'on fait venir la police.",None,None),("d3","d1","Survivant stabilisé","On fait une évaluation psychosociale.",None,None),("d4","d3","Danger grave et refus de soins","On envisage un PAFA médical.",None,None),("d5","d3","Sortie possible","On remet un plan de sécurité et l'on revoit dans les 48 heures.",None,None)],
   "points":["Les échelles ne prédisent pas."],"sources":[VD,HUG,NICE]},
  {"titre":"Agir","rub":["positiveDiagnosis","acuteManagement","hospitalizationComplications","chronicManagement"],"comment":"On respecte la procédure légale, on protège le survivant et l'on soutient les proches.",
   "tab":(["Situation","Conduite","Source"],[["Décès","Légiste, police, mort non naturelle",[("VD 2022","Ministère public.")]],["Survivant en danger","PAFA médical ≤ 6 semaines",[("Berne","Art. 429 CC.")]],["Survivant sortant","Plan de sécurité, suivi 48 h, ASSIP",[("NICE 2022","ASSIP 2016.")]]]),
   "points":["Limiter les quantités prescrites."],"sources":[VD,BE,NICE,ASS]},
  {"titre":"Suivre et prévenir","rub":["prognosisDischarge","surveillance","followUpNetwork"],"comment":"Le risque reste élevé des années ; la limitation des moyens réduit les décès.",
   "points":["Un sur 25 en cinq ans.","Emballages réduits : −43 %."],"sources":[CAR,NICE,OBS,HAW]}],
 "ssp":("G13","Décès non naturel",True,[
   ("n1",None,"Personne trouvée après une ingestion de médicaments","On distingue le décès du survivant.","geste","c2"),
   ("n2","n1","Décès","On demande l'avis du légiste, on coche une mort non naturelle et l'on fait venir la police.","geste","c3"),
   ("n3","n2","Proches endeuillés","On propose un soutien.","geste","c4"),
   ("n4","n1","Survivant stabilisé","On fait une évaluation psychosociale sans échelle de risque.","geste","c2"),
   ("n5","n4","Danger grave et refus","On envisage un PAFA médical.","geste","c3"),
   ("n6","n4","Sortie","On remet un plan de sécurité et l'on revoit dans les 48 heures.","geste","c4")]),
 "pec":[
  pec("geste","Intoxication médicamenteuse volontaire, mortelle ou non",["On respecte la procédure légale devant un décès non naturel.","On évalue et l'on protège le survivant pour éviter la récidive."],
      ["On constate le décès ou l'on stabilise le survivant.","On recueille les circonstances et l'on préserve les lieux."],
      [],
      [("psychothérapie","On propose une intervention brève de type ASSIP et un suivi psychiatrique.","On réduit la récidive."),("social et assurances","On soutient les proches endeuillés et la famille du survivant.","On limite les conséquences du deuil et l'isolement."),("soins infirmiers","On surveille le survivant et l'on sécurise l'environnement.","On évite un nouveau geste à l'hôpital.")],
      [("N Médecine sociale Prévention OFSP","On limite l'accès aux moyens et l'on soutient le plan d'action national."),("C Communication clinique","On annonce le décès et la procédure légale avec tact.")],
      (["On demande l'avis du légiste.","On fait venir la police.","On préserve les lieux."],[("d'abord","médecin de garde","Il constate le décès et appelle le légiste."),("ensuite","police","Elle informe le ministère public."),("puis","ministère public","Il décide de l'examen médico-légal et de la remise du corps.")]),
      (["On évalue le survivant.","On organise la sortie."],[("d'abord","psychiatre","Il mène l'évaluation psychosociale."),("ensuite","médecin de famille","Il revoit le patient dans les 48 heures et limite les quantités prescrites."),("puis","psychothérapeute","Il assure une intervention brève et le suivi.")]),
      "Après un geste non mortel, 16,3 % récidivent dans l'année et 3,9 % meurent par suicide en cinq ans ; un suivi structuré réduit la récidive.",
      [("Contact après la sortie","Dans les 48 heures","Rendez-vous honoré"),("Plan de sécurité","À chaque consultation","Plan connu et actualisé")],"Le suivi s'allège quand la crise est résolue et que le traitement de fond est en place.",
      ("On limite l'accès aux moyens.","On évalue et l'on suit chaque personne après un geste.","On soutient les proches endeuillés.")),]}
