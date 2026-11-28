from constructeur_agent_45spec import pec
ID = "T74.9_1__O7_24-E05"
PLAN = "non_monographique"
CP = "[Code pénal suisse (RS 311.0), état au 1.11.2026, art. 123, 126, 180, 181, 181b et 321, fedlex, lu le 28.11.2026]"
CC = "[Code civil suisse (RS 210), état au 1.7.2026, art. 28b, 28c, 314c, 314d et 443, fedlex, lu le 28.11.2026]"
LAVI = "[Loi sur l'aide aux victimes (LAVI, RS 312.5), état au 1.1.2025, art. 1, 5, 14, 15 et 25, fedlex, lu le 28.11.2026]"
AVCH = "[Aide aux victimes en Suisse (aide-aux-victimes.ch), numéro national 142 depuis le 1er mai 2026, gratuit, confidentiel, anonyme, pas un numéro d'urgence, lu le 28.11.2026]"
LAAM = "[Loi sur l'armée (LAAM, RS 510.10), état au 1.6.2026, art. 113 al. 2 et 7, fedlex, lu le 28.11.2026]"
BFA4 = "[BFEG, feuille d'information A4 « Chiffres de la violence domestique en Suisse » (juillet 2024), statistique policière 2023, homicides 2009–2016, prévalence, lu le 28.11.2026]"
BFA2 = "[BFEG, feuille d'information A2 « Violence dans les relations de couple : causes, facteurs de risque et de protection » (janvier 2026), séparation, grossesse, isolement, lu le 28.11.2026]"
BFB6 = "[BFEG, feuille d'information B6 « Violence domestique et recours aux armes » (juin 2020), létalité des armes à feu, armes d'ordonnance, lu le 28.11.2026]"
VD26 = "[Dal Gobbo et Dorthe, « Cadre légal : secret de fonction, secret médical », Journée du réseau vaudois contre la violence domestique (4 juin 2026, vd.ch), adulte : consentement ou levée par le Conseil de santé, art. 17 CP, art. 314c CC, lu le 28.11.2026]"
FR = "[État de Fribourg, « Déliement du secret professionnel / obligation et droits d'annonce du médecin » (fr.ch), art. 90a LSan, lu le 28.11.2026]"
UMV = "[CURML, dépliant « Unité de médecine des violences : consultation médico-légale pour adultes victimes de violences » (2022), lu le 28.11.2026]"
HUG = "[HUG, communiqué « Une nouvelle consultation médico-légale pour adultes victimes de violences » (23.01.2025), lu le 28.11.2026]"
VQF = "[violencequefaire.ch, rubrique « Victime » (plan de sécurité, départ avec les enfants, constat médical, plainte en 3 mois, LAVI), lu le 28.11.2026]"
VQFV = "[violencequefaire.ch, pages « Violence et handicap », « LGBTIQ » et « Violences numériques », lues le 28.11.2026]"
USP = "[USPSTF, Intimate Partner Violence and Caregiver Abuse of Older or Vulnerable Adults: Screening, Final Recommendation Statement (24.06.2025), lu le 28.11.2026]"
NICE = "[NICE PH50, Domestic violence and abuse: multi-agency working (2014), recommandations 6, 9, 10 et 13, lues le 28.11.2026]"
GLASS = "[Glass N et al., Non-fatal strangulation is an important risk factor for homicide of women, J Emerg Med 2008, PMID 17961956, résumé lu le 28.11.2026]"
SHAR = "[Sharman LS et al., Medical evidence assisting non-fatal strangulation prosecution: a scoping review, BMJ Open 2023, PMID 36972965, texte intégral PMC10077461 lu le 28.11.2026]"
DOWN = "[Downing NR et al., Indicators for CT angiography following nonfatal strangulation: a scoping review, J Forensic Nurs 2026, PMID 42853890, résumé lu le 28.11.2026]"
MAG = "[Maguire S et al., Can you age bruises accurately in children? A systematic review, Arch Dis Child 2005, PMID 15665179, résumé lu le 28.11.2026]"
EXP = "Avis d'expert (à vérifier)"
_N = [
("def","definition","critère",1,1,BFA4,"La statistique policière suisse définit la violence domestique comme l'exercice ou la menace d'une violence entre partenaires actuels ou anciens, mariés ou non, entre parents et enfants ou entre autres proches."),
("formes","definition","signe",1,0,VQFV+" ; "+VQF,"Elle prend des formes physiques, psychologiques, sexuelles, économiques et numériques (surveillance du téléphone, géolocalisation, traceur), qui se poursuivent souvent après la séparation."),
("epi","epidemiology","chiffre",1,1,BFA4,"En 2023, la police a enregistré 19 918 infractions de violence domestique ; 70,1 % des victimes étaient des femmes ; environ une femme sur cinq (20,7 %, Gillioz 1997) subit une violence physique ou sexuelle dans son couple au cours de sa vie."),
("hom","epidemiology","chiffre",1,1,BFA4+" ; "+BFB6,"De 2009 à 2016, la Suisse a compté 75 homicides ou tentatives domestiques par an, mortels dans 34 % des cas ; une arme à feu a servi dans 34 % des homicides consommés, et 67 % des victimes visées par une arme à feu dans le couple sont mortes."),
("emprise","basicSciences","mécanisme",1,0,VQF+" ; "+EXP,"La peur, la honte, l'espoir d'un changement et la dépendance font que la personne minimise les faits, se sent prise au piège et revient parfois ; la séparation reste le moment le plus dangereux."),
("seule","anamnesis","décision",3,0,NICE+" ; "+USP,"On pose la question en privé, seul à seul, sans partenaire ni proche, de façon directe et bienveillante, avec un interprète professionnel et jamais un membre de la famille ; en téléconsultation, un tiers peut entendre les réponses."),
("repere","anamnesis","décision",2,0,USP+" ; "+NICE,"L'USPSTF (2025, grade B) recommande de dépister les femmes en âge de procréer, y compris enceintes et en post-partum ; NICE demande de poser la question en santé mentale, en addictologie et en suivi prénatal même sans indice."),
("indices","anamnesis","signe",1,0,NICE+" ; "+EXP,"Des consultations répétées ou annulées, une explication qui ne colle pas aux lésions et un partenaire qui répond à la place du patient doivent faire poser la question."),
("exam","clinicalExam","examen",2,0,SHAR+" ; "+MAG+" ; "+EXP,"On examine tout le corps avec l'accord du patient, y compris le cou, les yeux, les gencives et l'arrière des oreilles (pétéchies) ; on décrit chaque lésion sans dater une ecchymose d'après sa couleur, méthode sans base fiable (démontré chez l'enfant)."),
("strang","presumptionRedFlags","signe",3,0,GLASS+" ; "+SHAR,"Une compression du cou multiplie par environ 7,5 le risque d'homicide ultérieur ; 44 % des personnes n'ont aucune marque visible, et la perte de connaissance, la perte d'urines, la voix modifiée, la douleur à la déglutition et les pétéchies signent sa gravité."),
("danger","presumptionRedFlags","critère",2,0,BFA2+" ; "+VQF+" ; "+USP,"La séparation récente ou annoncée, la grossesse, l'accès à une arme, les menaces de mort, l'isolement et l'escalade augmentent le risque de violence grave."),
("constat","workupGoldStandard","examen",3,1,SHAR+" ; "+VQF+" ; "+HUG,"Le constat de coups et blessures, établi de préférence le jour même et indépendamment d'une plainte, décrit chaque lésion (siège, taille, forme, couleur), avec photographies avec et sans règle, photographies de suivi, schéma corporel et paroles du patient entre guillemets ; on conseille de le garder hors du domicile."),
("umv","workupAlternatives","contexte suisse",1,1,UMV+" ; "+HUG,"L'Unité de médecine des violences du CHUV (Lausanne, Nyon, Rennaz, Yverdon) et la consultation médico-légale des HUG (depuis janvier 2025) offrent aux adultes un constat avec photographies, gratuit, confidentiel et indépendant de la plainte ; aux HUG, les violences sexuelles restent prises en charge aux urgences."),
("imag","workupAlternatives","examen",1,0,SHAR+" ; "+DOWN,"Après une compression du cou, le scanner apporte peu au-delà de l'examen clinique, l'IRM révèle des lésions des tissus mous invisibles, et aucun indicateur clinique validé ne prédit une lésion vasculaire, rare mais grave."),
("vuln","positiveDiagnosis","terrain particulier",2,0,VQFV+" ; "+NICE+" ; "+BFA4,"Les hommes (environ 30 % des victimes enregistrées), les personnes handicapées dépendantes de leur partenaire pour les soins, les médicaments ou l'argent, et les personnes LGBTIQ (coming out forcé, amis communs) rencontrent des obstacles supplémentaires à demander de l'aide."),
("secret","acuteManagement","décision",3,1,CP+" ; "+CC+" ; "+VD26,"Face à un adulte capable de discernement, le médecin garde le secret (art. 321 CP) : il ne transmet qu'avec son consentement ou une levée écrite par l'autorité ; la poursuite d'office ne lève pas le secret, et l'art. 443 CC le réserve pour l'avis à l'APEA."),
("canton","acuteManagement","contexte suisse",2,1,CP+" ; "+FR+" ; "+VD26+" ; "+CC,"L'art. 321 ch. 3 CP réserve les droits d'aviser fédéraux et cantonaux : Fribourg permet d'annoncer au ministère public un constat de crime ou de délit contre l'intégrité corporelle (art. 90a LSan), Vaud exige pour l'adulte une levée par le Conseil de santé, et l'art. 314c CC permet d'aviser l'APEA pour un enfant sans levée."),
("urg","acuteManagement","décision",1,1,AVCH+" ; "+CC+" ; "+VD26,"En cas de danger imminent, on appelle la police (117) ; l'état de nécessité (art. 17 CP) peut justifier la révélation ; un service cantonal peut expulser immédiatement l'auteur du logement (art. 28b al. 4 CC)."),
("arme","acuteManagement","contexte suisse",1,1,LAAM+" ; "+BFB6,"Le médecin est délié du secret pour signaler au DDPS des indices qu'un militaire pourrait faire un usage dangereux de son arme personnelle, qui lui est alors retirée (art. 113 LAAM)."),
("plan","chronicManagement","prévention",2,0,VQF+" ; "+NICE,"On construit un plan de sécurité : numéros 117 et 144, code convenu avec un proche, sac caché avec papiers, argent et clés, accès aux armes rendu difficile, départ sans prévenir l'auteur, procuration bancaire annulée."),
("civil","chronicManagement","contexte suisse",1,1,CC+" ; "+VQF,"Le juge civil peut interdire d'approcher et de contacter, expulser l'auteur du logement (art. 28b CC) et ordonner une surveillance électronique (art. 28c CC) ; quitter le domicile est un droit qui ne fait perdre ni logement ni droits sur les enfants."),
("enfants","hospitalizationComplications","complication",2,1,NICE+" ; "+CC+" ; "+VQF,"Les enfants exposés aux scènes en souffrent ; partir avec eux est un acte de protection ; le médecin peut aviser l'APEA sans levée du secret quand leur intérêt le justifie (art. 314c CC), mais l'obligation de l'art. 314d CC ne vise pas les personnes soumises au secret."),
("psy","hospitalizationComplications","complication",1,0,USP+" ; "+NICE,"Les conséquences comprennent dépression, état de stress post-traumatique, abus de substances, comportement suicidaire, douleurs chroniques, grossesse non désirée et IST ; on traite le trouble (thérapie centrée sur le trauma) en réévaluant le danger."),
("suivi","surveillance","décision",1,0,SHAR+" ; "+NICE,"On revoit la personne, on réévalue le danger et le plan de sécurité à chaque contact et l'on photographie l'évolution des lésions ; après une compression du cou, on demande de reconsulter en urgence au moindre symptôme neurologique, respiratoire ou de déglutition."),
("prono","prognosisDischarge","pronostic",1,0,USP,"Le bénéfice vient d'interventions à plusieurs composantes avec un soutien continu ; une simple brochure ou un conseil bref isolé n'a pas montré de bénéfice."),
("office","followUpNetwork","contexte suisse",2,1,CP+" ; "+VQF,"Entre partenaires faisant ménage commun, et jusqu'à un an après la séparation, les lésions corporelles simples, les voies de fait réitérées et les menaces se poursuivent d'office ; une voie de fait unique reste sur plainte (délai de 3 mois)."),
("lavi","followUpNetwork","contexte suisse",2,1,LAVI+" ; "+AVCH,"La LAVI offre une aide gratuite (dont l'hébergement d'urgence) dans le centre choisi, quelle que soit la date de l'infraction et même sans plainte ; l'indemnisation se demande dans les 5 ans ; depuis le 1er mai 2026, le 142 joint l'aide aux victimes, sans être un numéro d'urgence."),
("stalk","followUpNetwork","contexte suisse",1,1,CP+" ; "+VQFV,"Depuis le 1er janvier 2026, le harcèlement obsessionnel (art. 181b CP) est punissable sur plainte, même sans contact physique ; la contrainte (art. 181 CP) se poursuit d'office."),
]
K = {k: i+1 for i, (k, *_r) in enumerate(_N)}
N = [t[1:] for t in _N]
n = lambda *ks: [K[k] for k in ks]
AM = ["Compression du cou sans marque : 44 % sans lésion visible, risque d'homicide × 7,5.","Poursuite d'office ≠ levée du secret médical.","Art. 443 CC : secret réservé pour l'adulte ; art. 314c CC : avis possible pour l'enfant sans levée.","Art. 113 LAAM : médecin délié du secret pour l'arme d'ordonnance.","Fribourg (art. 90a LSan) ≠ Vaud (levée par le Conseil de santé).","Pas de datation d'une ecchymose par sa couleur.","142 depuis le 1er mai 2026, pas un numéro d'urgence ; harcèlement obsessionnel sur plainte depuis 2026.","Téléconsultation : un tiers peut entendre ; voir seul au cabinet."]
A = lambda *o: list(o)
Q = [
{"f":"A","s":("S1",1,3),"st":"Une femme de 34 ans consulte un médecin de famille à Neuchâtel pour une voix rauque et une douleur en avalant depuis la veille. Son compagnon l'accompagne, répond à sa place et dit qu'elle « a avalé de travers ». À l'examen, vous voyez de fines taches rouges punctiformes sur les paupières et derrière les oreilles ; le cou ne porte aucune marque.",
 "p":"Quelle est votre prochaine étape ?","o":A(
  (1,"Vous trouvez un motif pour la voir seule, sans le compagnon, puis vous lui demandez directement et avec bienveillance si quelqu'un lui a serré le cou ou lui a fait du mal","NICE PH50 : question posée en privé, seul à seul ; pétéchies du visage, voix rauque et douleur à la déglutition évoquent une compression du cou (Sharman 2023)."),
  (0,"Vous prescrivez un anti-inflammatoire et la revoyez dans une semaine si la voix ne revient pas","Faux : des pétéchies du visage avec voix rauque et dysphagie ne relèvent pas d'une simple irritation ; on cherche d'abord une cause qui peut menacer la vie."),
  (0,"Vous demandez au compagnon de décrire précisément l'épisode, puisqu'il en a été témoin","Faux : la personne qui répond à la place de la patiente peut être l'auteur ; on interroge la patiente seule."),
  (0,"Vous lui posez la question devant son compagnon pour montrer que vous n'avez rien à cacher","Faux : poser la question devant un partenaire possiblement en cause expose la patiente et empêche une réponse libre (NICE PH50)."),
  (0,"Vous l'adressez en ORL pour une laryngoscopie programmée et la laissez repartir sans autre question","Faux : la laryngoscopie différée ne répond pas à la question de la cause, et le retour sans entretien seul manque une situation à haut risque.")),
 "n":n("seule","indices","strang","exam"),"a":"application","d":4,
 "l":("Voix rauque, dysphagie, pétéchies du visage.","Compression du cou : stase veineuse au-dessus.","Partenaire qui répond à sa place.","Pétéchies au-dessus d'un cou sans marque.","Voir seule, demander directement.","Croire l'explication du compagnon.","Pétéchies et voix rauque : demander seule.")},
{"f":"A","s":("S1",2,3),"st":"Seule avec vous, elle dit qu'hier soir son compagnon lui a serré le cou des deux mains, qu'elle a « vu noir » quelques secondes et qu'elle a perdu ses urines. Elle n'a aucune marque visible et pense que « ce n'était pas si grave ».",
 "p":"Comment interprétez-vous ces éléments ?","o":A(
  (1,"C'est un marqueur de danger très élevé, qui multiplie le risque d'homicide ultérieur ; la perte de connaissance et la perte d'urines signent une compression sévère, même sans marque, et imposent une évaluation médicale et médico-légale le jour même","Glass 2008 : rapport de cotes de 7,48 pour un homicide ultérieur ; Sharman 2023 : perte de connaissance et perte d'urines sont des indicateurs cliniques essentiels."),
  (0,"L'absence de marque cutanée exclut une compression importante","Faux : en moyenne 44 % des personnes n'ont aucune lésion externe visible (Sharman 2023)."),
  (0,"La perte d'urines oriente d'abord vers une crise d'épilepsie, à explorer par un EEG avant toute autre démarche","Faux : la perte d'urines fait partie des signes de compression grave du cou ; l'EEG ne répond pas au danger immédiat."),
  (0,"Un scanner cervical normal permettrait d'exclure toute lésion et de la rassurer définitivement","Faux : le scanner apporte peu au-delà de l'examen (Sharman 2023) et aucun indicateur ne prédit fiablement une lésion vasculaire (Downing 2026)."),
  (0,"Le danger reste faible, puisqu'il s'agit d'un premier épisode et qu'elle minimise les faits","Faux : la gravité tient au geste lui-même ; la minimisation est fréquente et ne rassure pas.")),
 "n":n("strang","danger","imag","emprise"),"a":"piège","d":5,
 "l":("Perte de connaissance, perte d'urines.","Anoxie cérébrale par compression du cou.","Souvent aucune marque.","Perte de connaissance et d'urines : compression sévère.","Évaluer le jour même.","Pas de marque, pas de gravité.","Cou serré : danger de mort.")},
{"f":"A","s":("S1",3,3),"st":"Elle refuse d'appeler la police, accepte d'être examinée et veut dormir chez sa sœur. Elle habite Lausanne et craint que son compagnon apprenne la consultation.",
 "p":"Que lui proposez-vous ?","o":A(
  (1,"Une consultation médico-légale du CHUV, gratuite, confidentielle et indépendante d'une plainte, pour un constat avec photographies, un plan de sécurité, et la consigne de reconsulter en urgence au moindre trouble neurologique, respiratoire ou de déglutition","Dépliant UMV 2022 ; violencequefaire.ch ; Sharman 2023 (lésions internes parfois retardées)."),
  (0,"Vous informez la police sans son accord, puisque l'infraction est poursuivie d'office","Faux : la poursuite d'office ne lève pas le secret médical (art. 321 CP) ; sans danger imminent, on ne transmet pas sans consentement ni levée."),
  (0,"Vous attendez l'apparition d'ecchymoses dans quelques jours pour faire le constat","Faux : le constat se fait de préférence le jour même ; on photographie ensuite l'évolution (violencequefaire.ch, Sharman 2023)."),
  (0,"Vous lui remettez le constat à garder dans l'appartement qu'elle partage avec lui","Faux : on conseille de garder le constat ailleurs qu'au domicile, chez un proche ou chez le médecin (violencequefaire.ch)."),
  (0,"Vous proposez une thérapie de couple pour apaiser la relation","Faux : une thérapie de couple ne s'envisage pas tant que des menaces ou des actes persistent (violencequefaire.ch).")),
 "n":n("umv","constat","secret","plan","suivi"),"a":"application","d":4,
 "l":("Refus de la police, examen accepté.","Preuves fragiles et danger persistant.","Lésions internes possibles plus tard.","Constat indépendant de la plainte.","Constat, plan, consignes.","Dénoncer malgré elle.","Documenter sans dénoncer.")},
{"f":"A","st":"Un homme de 42 ans, paraplégique, consulte pour une plaie sacrée profonde et négligée. Son épouse gère ses soins, ses médicaments et son argent, et elle insiste pour rester. Vous notez des ecchymoses en bandes aux deux poignets ; il dit qu'elle « oublie » parfois ses antalgiques et le laisse seul toute la journée. Il est capable de discernement.",
 "p":"Quelle est la démarche la plus appropriée ?","o":A(
  (1,"Vous le voyez seul, explorez sa dépendance pour les soins, les médicaments et l'argent ainsi que ses craintes, documentez les lésions et lui proposez une aide extérieure, sans rien transmettre sans son accord hors danger imminent","NICE PH50 (seul à seul, personnes handicapées) ; violencequefaire.ch « Violence et handicap » ; art. 443 CC (secret réservé)."),
  (0,"Vous attribuez les ecchymoses aux transferts du fauteuil et traitez seulement la plaie","Faux : des ecchymoses en bandes aux poignets, des antalgiques retenus et un isolement imposent d'explorer une dépendance abusive."),
  (0,"Vous avisez immédiatement l'APEA sans son accord, puisque l'art. 443 CC permet à toute personne de le faire","Faux : pour un adulte, l'art. 443 CC réserve le secret professionnel ; le médecin doit obtenir le consentement ou une levée."),
  (0,"Vous confiez à son épouse un plan de soins plus détaillé, puisqu'elle s'occupe de tout","Faux : on renforcerait l'emprise d'une personne possiblement en cause ; on parle d'abord au patient seul."),
  (0,"Vous écartez d'emblée l'hypothèse d'une épouse en cause, rare chez un homme","Faux : environ 30 % des victimes enregistrées par la police suisse sont des hommes (BFEG A4).")),
 "n":n("vuln","seule","secret"),"a":"piège","d":5,
 "l":("Paraplégie, plaie négligée, ecchymoses des poignets.","Dépendance pour soins, médicaments, argent.","Épouse qui reste, antalgiques retenus.","Adulte capable de discernement.","Voir seul, documenter, proposer.","Signaler sans accord ou ignorer.","Dépendance = vulnérabilité, mais secret.")},
{"f":"A","st":"Une femme de 26 ans, enceinte de 20 semaines, est vue en téléconsultation vidéo pour un contrôle. Une voix d'homme commente ses réponses hors champ ; elle répond par monosyllabes, a annulé deux rendez-vous et cache de la main une marque bleutée de la pommette.",
 "p":"Que faites-vous ?","o":A(
  (1,"Vous n'abordez pas le sujet à distance devant un tiers et fixez rapidement une consultation au cabinet, où vous la verrez seule, la grossesse étant un moment de repérage systématique","USPSTF 2025 : risque qu'un partenaire entende en téléconsultation ; dépistage chez la femme enceinte ; NICE PH50."),
  (0,"Vous lui demandez directement en vidéo si quelqu'un lui fait du mal","Faux : en téléconsultation, le partenaire peut entendre les réponses, ce qui expose la patiente (USPSTF 2025)."),
  (0,"Vous lui envoyez un questionnaire de repérage par courriel à domicile","Faux : un document reçu au domicile peut être lu par un tiers et l'exposer."),
  (0,"Vous attendez le contrôle prévu dans quatre semaines","Faux : la grossesse augmente le risque (BFEG A2) et la marque visible impose une réévaluation rapide."),
  (0,"Vous demandez à l'homme présent d'expliquer la marque de la pommette","Faux : on n'interroge pas un tiers possiblement en cause ; on voit la patiente seule.")),
 "n":n("repere","danger","indices"),"a":"application","d":4,
 "l":("Grossesse, marque cachée, rendez-vous annulés.","Contrôle par un tiers présent.","Voix d'homme hors champ.","Téléconsultation non sûre.","Revoir seule au cabinet.","Questionner en vidéo.","Grossesse = poser la question, mais seule.")},
{"f":"A","st":"Une femme de 39 ans, à Sion, vous dit qu'elle quittera son mari la semaine prochaine. Il est soldat de milice, garde son fusil d'assaut à la maison et a dit qu'il « finirait tout » si elle partait. Elle refuse que vous parliez à la police.",
 "p":"Quelle démarche la loi vous permet-elle sans son accord ?","o":A(
  (1,"Signaler aux services compétents du DDPS les indices qu'il pourrait faire un usage dangereux de son arme personnelle, la loi sur l'armée déliant le médecin du secret pour ce signalement","Art. 113 al. 2 et 7 LAAM : arme retirée en cas d'indices de danger ; médecins libérés du secret professionnel."),
  (0,"Aucune : le secret médical interdit toute communication sans levée par l'autorité","Faux : l'art. 321 ch. 3 CP réserve les droits d'aviser fédéraux et cantonaux, dont l'art. 113 al. 7 LAAM."),
  (0,"Aviser l'APEA, compétente pour retirer l'arme","Faux : le retrait de l'arme personnelle relève du DDPS (art. 113 LAAM), et l'avis à l'APEA pour un adulte réserve le secret (art. 443 CC)."),
  (0,"Attendre un passage à l'acte, la menace n'étant pas une infraction","Faux : la menace entre époux est poursuivie d'office (art. 180 al. 2 CP), et la séparation annoncée est la période la plus dangereuse."),
  (0,"Lui conseiller d'annoncer son départ à son mari pour l'apaiser","Faux : on conseille de ne pas révéler le projet de départ, moment de risque très élevé (violencequefaire.ch).")),
 "n":n("arme","canton","danger","hom"),"a":"piège","d":5,
 "l":("Départ annoncé, arme à domicile, menace.","Séparation et arme : létalité accrue.","Fusil d'assaut d'ordonnance.","Base légale fédérale spéciale.","Signaler au DDPS.","Se croire muet par le secret.","Arme d'ordonnance : LAAM délie le médecin.")},
{"f":"A","st":"Une patiente de 45 ans présente des ecchymoses jaunes, vertes et violacées sur les bras et le dos. Son avocate vous demande de préciser dans le constat l'âge de chaque ecchymose d'après sa couleur, pour faire coïncider les dates avec son récit.",
 "p":"Que répondez-vous ?","o":A(
  (1,"Vous décrivez chaque lésion (siège, taille mesurée, forme, couleur) avec des photographies avec et sans règle, sans dater les ecchymoses d'après leur couleur, méthode sans base fiable","Maguire 2005 (revue systématique chez l'enfant) ; Sharman 2023 (photographies) ; extrapolation à l'adulte : avis d'expert."),
  (0,"Vous datez chaque lésion, le jaune signant toujours une ecchymose de plus de 48 heures","Faux : du jaune a été décrit avant 48 heures et toute couleur peut se voir à tout âge (Maguire 2005)."),
  (0,"Vous concluez que les lésions sont compatibles avec le récit, sans les décrire","Faux : le constat est d'abord descriptif et précis ; une conclusion sans description n'a guère de valeur."),
  (0,"Vous refusez tout constat tant qu'aucune plainte n'est déposée","Faux : la documentation médico-légale est indépendante de la plainte (HUG 2025)."),
  (0,"Vous ne photographiez que les lésions du visage, seules utiles en justice","Faux : on documente toutes les lésions, y compris les zones cachées, avec vue d'ensemble et gros plans (Sharman 2023).")),
 "n":n("exam","constat"),"a":"piège","d":4,
 "l":("Ecchymoses de couleurs variées.","Évolution de l'hémoglobine dégradée.","Couleurs non spécifiques.","Décrire, ne pas dater.","Mesurer et photographier.","Dater par la couleur.","Couleur ≠ âge.")},
{"f":"A","st":"Une mère de deux enfants de 4 et 7 ans veut partir ce soir chez une amie, après des menaces répétées de son compagnon. Elle hésite à emmener les enfants, de peur qu'on lui reproche de les avoir enlevés à leur père. Les enfants assistent aux scènes, et le plus jeune mouille de nouveau son lit.",
 "p":"Que lui dites-vous ?","o":A(
  (1,"Partir est un droit et emmener les enfants est un acte de protection ; leur exposition aux scènes les met en danger, et vous pouvez aviser l'APEA sans levée du secret si leur intérêt le justifie","violencequefaire.ch ; art. 314c al. 2 CC ; NICE PH50."),
  (0,"Elle doit laisser les enfants au domicile jusqu'à une décision du juge","Faux : laisser les enfants pourrait être interprété en sa défaveur ; les emmener les protège (violencequefaire.ch)."),
  (0,"Vous êtes obligé par l'art. 314d CC d'aviser l'APEA","Faux : l'art. 314d CC ne vise pas les personnes soumises au secret professionnel selon le CP ; le médecin a un droit d'aviser (art. 314c)."),
  (0,"Vous devez d'abord obtenir une levée du secret pour aviser l'APEA","Faux : pour un enfant, l'art. 314c al. 2 CC permet d'aviser sans levée quand l'intérêt de l'enfant le justifie."),
  (0,"Les enfants ne sont pas concernés tant qu'ils ne sont pas touchés eux-mêmes","Faux : l'exposition aux scènes entre parents nuit aux enfants ; l'énurésie secondaire en est un signe possible.")),
 "n":n("enfants","plan","canton"),"a":"piège","d":5,
 "l":("Départ ce soir, enfants témoins.","Exposition = mise en danger de l'enfant.","Énurésie secondaire.","Droit de partir avec les enfants.","Rassurer, protéger, aviser si besoin.","Laisser les enfants.","Partir avec eux protège.")},
{"f":"A","m":0,"st":"Une patiente victime de violence dans son couple souhaite parler à un service spécialisé, de façon anonyme ; elle ne court aucun danger immédiat ce soir.",
 "p":"Quel numéro national lui indiquez-vous depuis le 1er mai 2026 ?","o":A(
  (1,"Le 142, numéro national de l'aide aux victimes, gratuit, confidentiel et anonyme","aide-aux-victimes.ch."),
  (0,"Le 117, pour un conseil anonyme sans danger immédiat","Faux : le 117 est la police, à appeler en cas de danger imminent."),
  (0,"Le 144, pour un conseil juridique","Faux : le 144 est le numéro des urgences sanitaires."),
  (0,"Le 142, à composer en priorité en cas de danger imminent","Faux : le 142 n'est pas un numéro d'urgence ; en cas de danger imminent, on appelle le 117 ou le 144."),
  (0,"Aucun : seuls des numéros cantonaux existent","Faux : depuis le 1er mai 2026, le 142 joint l'aide aux victimes dans toute la Suisse.")),
 "n":n("lavi","urg"),"a":"direct","d":2,
 "l":("Besoin de conseil anonyme.","Aide aux victimes.","Pas de danger immédiat.","142, pas une urgence.","Orienter.","Confondre avec le 117.","142 = aide aux victimes.")},
{"f":"A","m":0,"st":"Lors d'un colloque à Berne, on vous demande de situer la violence domestique en Suisse.",
 "p":"Quelle affirmation est exacte ?","o":A(
  (1,"En 2023, la police a enregistré près de 20 000 infractions de violence domestique ; environ 70 % des victimes étaient des femmes et 30 % des hommes","BFEG A4 : 19 918 infractions, 70,1 % de victimes femmes."),
  (0,"La violence domestique ne concerne que les couples mariés","Faux : la définition policière inclut les couples actuels ou passés, mariés ou non, et les relations familiales."),
  (0,"Seule la violence physique entre dans la définition","Faux : elle comprend aussi les violences psychologiques, sexuelles, économiques et numériques."),
  (0,"Les homicides domestiques sont exceptionnels et presque jamais mortels","Faux : de 2009 à 2016, 75 homicides ou tentatives par an, mortels dans 34 % des cas (BFEG A4)."),
  (0,"Moins de 5 % des femmes subissent une violence physique ou sexuelle dans leur couple au cours de leur vie","Faux : 20,7 % dans l'étude de Gillioz 1997, soit environ une femme sur cinq (BFEG A4).")),
 "n":n("epi","def","hom"),"a":"direct","d":2,
 "l":("Ampleur.","Statistique policière.","Femmes surtout, hommes aussi.","20 000 infractions, 70 % de femmes.","Situer.","Mariage seul, coups seuls.","Une femme sur cinq.")},
{"f":"A","m":0,"st":"Une femme de 31 ans, en concubinage depuis 3 ans, a reçu de son compagnon une gifle unique, sans lésion ; il y a un mois, il l'avait menacée de mort. Elle demande ce que la justice peut faire sans sa plainte.",
 "p":"Quelle réponse est exacte ?","o":A(
  (1,"La menace entre partenaires faisant ménage commun se poursuit d'office ; une voie de fait unique ne se poursuit que sur plainte, alors que des voies de fait réitérées se poursuivent d'office","Art. 180 al. 2 et 126 CP."),
  (0,"Tout se poursuit d'office dès qu'il s'agit de partenaires","Faux : une voie de fait unique reste poursuivie sur plainte (art. 126 al. 1 CP)."),
  (0,"Rien ne se poursuit d'office faute de mariage","Faux : les partenaires faisant ménage commun pour une durée indéterminée sont visés (art. 123, 126, 180 CP)."),
  (0,"La poursuite d'office cesse le jour de la séparation","Faux : elle s'étend à l'année qui suit la séparation."),
  (0,"Elle dispose d'un an pour porter plainte pour la gifle","Faux : le délai de plainte est de trois mois (violencequefaire.ch).")),
 "n":n("office"),"a":"piège","d":3,
 "l":("Gifle unique, menace de mort.","Régime d'office conditionnel.","Concubinage.","Unique ou réitérée.","Expliquer.","Tout d'office.","Voie de fait unique : sur plainte.")},
{"f":"A","m":0,"st":"Une femme de 50 ans révèle des coups subis de son ex-mari il y a 4 ans, jamais dénoncés. Elle fait des cauchemars, évite tout rappel des faits et demande si l'aide aux victimes peut encore l'aider.",
 "p":"Quelle réponse est exacte ?","o":A(
  (1,"Elle peut consulter gratuitement le centre LAVI de son choix quelle que soit la date de l'infraction, même sans plainte ; une indemnisation se demande en principe dans les 5 ans, et l'on oriente ses symptômes post-traumatiques vers une thérapie centrée sur le trauma","LAVI art. 1, 5, 15 et 25 ; NICE PH50 rec. 13."),
  (0,"La LAVI exige une plainte pénale préalable","Faux : le droit existe que l'auteur ait été découvert ou non (art. 1 al. 3 LAVI)."),
  (0,"Le délai pour consulter un centre LAVI est d'un an après l'infraction","Faux : on peut s'adresser au centre quelle que soit la date de l'infraction (art. 15 al. 2 LAVI)."),
  (0,"Elle doit s'adresser au seul centre LAVI de son canton de domicile","Faux : la victime choisit son centre (art. 15 al. 3 LAVI)."),
  (0,"Ses cauchemars sortent du champ de la LAVI, limitée aux lésions physiques","Faux : la LAVI couvre l'atteinte psychique et l'assistance psychologique (art. 1 et 14 LAVI).")),
 "n":n("lavi","psy"),"a":"application","d":3,
 "l":("Faits anciens, symptômes post-traumatiques.","Droits de la victime.","Pas de plainte.","Date sans importance pour l'aide.","Orienter.","Croire un délai d'un an.","LAVI : choix libre, gratuit, sans plainte.")},
{"f":"A","m":0,"st":"À Lausanne, une patiente de 38 ans, capable de discernement, révèle des coups répétés de son mari. Elle refuse toute démarche aujourd'hui ; il n'existe aucun danger imminent. Votre assistant veut dénoncer les faits, « poursuivis d'office ».",
 "p":"Quelle attitude est correcte ?","o":A(
  (1,"Vous gardez le secret : vous documentez, proposez un constat et des ressources, et ne transmettez qu'avec son consentement ou après une levée du secret par le Conseil de santé","Art. 321 CP ; Dal Gobbo et Dorthe 2026 (Vaud)."),
  (0,"Vous dénoncez les faits au ministère public, la poursuite d'office l'imposant","Faux : la poursuite d'office concerne l'autorité pénale, pas le secret du médecin."),
  (0,"Vous avisez l'APEA, puisque l'art. 443 CC permet à toute personne de le faire","Faux : l'art. 443 CC réserve le secret professionnel pour l'adulte."),
  (0,"Vous lui remettez une brochure, mesure dont l'efficacité est démontrée à elle seule","Faux : une information isolée sans soutien continu n'a pas montré de bénéfice (USPSTF 2025)."),
  (0,"Vous cessez le suivi tant qu'elle reste avec son mari","Faux : on maintient le lien et l'on réévalue le danger à chaque consultation.")),
 "n":n("secret","canton","office","prono"),"a":"application","d":3,
 "l":("Adulte capable, refus, pas de danger imminent.","Autonomie et secret.","Poursuite d'office invoquée.","Secret maintenu.","Documenter et accompagner.","Dénoncer.","D'office ≠ levée du secret.")},
{"f":"A","m":0,"st":"Une femme séparée depuis 18 mois de son compagnon reçoit chaque jour des dizaines de messages de lui ; il la suit, et elle a trouvé un traceur GPS sous sa voiture. Il ne l'a jamais touchée.",
 "p":"Que lui expliquez-vous ?","o":A(
  (1,"Depuis le 1er janvier 2026, le harcèlement obsessionnel est une infraction poursuivie sur plainte, à déposer dans les trois mois ; elle peut aussi demander au juge civil une interdiction d'approcher et de contacter, et doit conserver les preuves","Art. 181b CP ; art. 28b CC ; violencequefaire.ch."),
  (0,"Ces faits ne sont pas punissables en l'absence de coups","Faux : l'art. 181b CP réprime le fait de traquer ou d'importuner obstinément."),
  (0,"Ces faits sont poursuivis d'office parce qu'il s'agit d'un ex-partenaire","Faux : l'art. 181b CP est poursuivi sur plainte, et le régime d'office des art. 123, 126 et 180 CP ne vaut que dans l'année qui suit la séparation."),
  (0,"Le juge civil ne peut intervenir qu'en cas de coups","Faux : l'art. 28b CC vise aussi les menaces et le harcèlement."),
  (0,"Une surveillance électronique de l'auteur n'existe pas en Suisse","Faux : le juge peut ordonner le port d'un appareil électronique non amovible (art. 28c CC).")),
 "n":n("stalk","civil","formes"),"a":"piège","d":3,
 "l":("Messages, filature, traceur.","Contrôle numérique après séparation.","Pas de contact physique.","Infraction depuis 2026, sur plainte.","Plainte, mesures civiles, preuves.","Rien sans coups.","Traque obstinée : art. 181b CP.")},
{"f":"Kprim","m":0,"st":"Vous établissez un constat après des coups reçus d'un partenaire.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"On photographie chaque lésion avec et sans règle, puis on refait des photographies de suivi si de nouvelles lésions apparaissent.","Sharman 2023."),
  (1,"On note entre guillemets les paroles exactes de la personne sur les faits.","Sharman 2023."),
  (0,"On estime l'âge de chaque ecchymose d'après sa couleur.","Faux : méthode sans base fiable (Maguire 2005)."),
  (0,"Le constat ne sert que si une plainte est déjà déposée.","Faux : la documentation est indépendante de la plainte (HUG 2025) et peut servir plus tard ; l'UMV la propose gratuitement.")),
 "n":n("constat","exam","umv"),"a":"direct","d":3,
 "l":("Constat.","Preuve médicale.","Photographies, citations.","Description sans datation.","Documenter.","Dater par la couleur.","Règle, guillemets, suivi.")},
{"f":"Kprim","m":0,"st":"Vous évaluez le danger chez une personne exposée à la violence de son partenaire.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"Une séparation récente ou annoncée augmente le risque de violence grave.","BFEG A2 2026 ; violencequefaire.ch."),
  (1,"Une grossesse augmente le risque.","BFEG A2 2026 ; USPSTF 2025."),
  (1,"Une arme à feu à domicile, y compris une arme d'ordonnance, accroît le risque d'issue mortelle.","BFEG B6 : 67 % des victimes visées par une arme à feu dans le couple meurent."),
  (0,"Une compression du cou sans marque visible traduit un danger faible.","Faux : elle multiplie le risque d'homicide (Glass 2008) et ne laisse souvent aucune marque (Sharman 2023).")),
 "n":n("danger","strang","hom"),"a":"direct","d":3,
 "l":("Danger.","Létalité.","Séparation, grossesse, arme.","Cou serré même sans marque.","Évaluer.","Pas de marque, pas de danger.","Séparation, grossesse, arme, cou.")},
{"f":"Kprim","m":0,"st":"Vous révisez le secret médical face à la violence domestique.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"L'art. 321 CP réserve les droits d'aviser une autorité prévus par le droit fédéral ou cantonal.","Art. 321 ch. 3 CP."),
  (1,"À Fribourg, le médecin peut annoncer à l'autorité de poursuite pénale un constat qui fait conclure à un crime ou à un délit contre l'intégrité corporelle.","fr.ch, art. 90a LSan."),
  (0,"Pour un adulte capable de discernement, l'art. 443 CC permet au médecin d'aviser l'APEA sans levée du secret.","Faux : l'art. 443 CC réserve le secret professionnel."),
  (1,"Pour un enfant exposé, le médecin peut aviser l'APEA sans levée du secret quand l'intérêt de l'enfant le justifie.","Art. 314c al. 2 CC.")),
 "n":n("canton","secret","enfants"),"a":"direct","d":3,
 "l":("Secret.","Bases légales d'avis.","Adulte ou enfant.","Droits cantonaux réservés.","Vérifier la base légale.","Confondre adulte et enfant.","Enfant : 314c ; adulte : consentement.")},
{"f":"Kprim","m":0,"st":"Vous organisez le repérage de la violence domestique au cabinet.",
 "p":"Ces affirmations sont-elles vraies ou fausses ?","o":A(
  (1,"L'USPSTF recommande en 2025 de dépister les femmes en âge de procréer, y compris pendant la grossesse et le post-partum.","USPSTF 2025, grade B."),
  (1,"NICE demande de poser la question en santé mentale, en addictologie et en suivi prénatal, même sans indice.","NICE PH50 rec. 6."),
  (0,"Un membre de la famille peut traduire pour gagner du temps.","Faux : NICE demande un interprète professionnel, jamais un proche ou un ami."),
  (1,"Une personne qui dépend de son partenaire pour ses soins ou ses déplacements rencontre des obstacles supplémentaires à demander de l'aide.","violencequefaire.ch « Violence et handicap ».")),
 "n":n("repere","vuln","seule"),"a":"direct","d":3,
 "l":("Repérage.","Question systématique.","Groupes cibles.","Interprète professionnel.","Organiser.","Proche interprète.","Demander à tous, seul à seul.")},
{"f":"MenuLong","st":"Une femme de 30 ans a décidé de quitter son compagnon dans les prochains jours, avec ses deux enfants. Il ne doit pas l'apprendre. Elle vous demande comment se préparer.",
 "p":"Choisissez les TROIS conseils adaptés.","o":A(
  (1,"Préparer un sac caché avec papiers d'identité, argent, cartes, clés et affaires des enfants","violencequefaire.ch."),
  (1,"Convenir avec un proche d'un code, par exemple un SMS vide, pour qu'il alerte la police","violencequefaire.ch."),
  (1,"Garder accessibles les numéros 117 et 144 et l'adresse d'un centre d'accueil d'urgence","violencequefaire.ch ; LAVI art. 14 (hébergement d'urgence)."),
  (0,"Annoncer son départ au compagnon pour éviter une réaction","Faux : on conseille de ne pas révéler le projet ; la séparation est le moment le plus dangereux."),
  (0,"Se rendre d'abord au poste de police pour obtenir l'autorisation de partir","Faux : il n'est pas nécessaire de signaler son départ à la police ni de demander une autorisation."),
  (0,"Laisser les enfants au domicile pour ne pas être accusée de les enlever","Faux : emmener les enfants est un acte de protection."),
  (0,"Garder le constat médical dans le logement commun","Faux : on le garde hors du domicile, chez un proche ou chez le médecin."),
  (0,"Proposer une thérapie de couple avant le départ","Faux : elle ne s'envisage pas tant que des menaces ou des actes persistent."),
  (0,"Attendre une décision de garde du juge avant de partir","Faux : partir est un droit, et la garde se règle ensuite."),
  (0,"Annoncer aux enfants la date exacte du départ plusieurs semaines à l'avance","Faux : on évite d'en parler aux enfants si cela présente le moindre risque d'ébruiter le projet."),
  (0,"Laisser au compagnon la procuration sur son compte bancaire","Faux : on conseille d'annuler la procuration et d'ouvrir un compte personnel."),
  (0,"Effacer les messages menaçants reçus pour se protéger","Faux : on conserve les preuves (messages, photos)."),),
 "n":n("plan","danger","enfants"),"a":"application","d":4,
 "l":("Départ préparé en secret avec enfants.","Séparation : pic de danger.","Auteur non informé.","Sac, code, numéros.","Planifier.","Prévenir l'auteur.","Partir préparé et en silence.")},
{"f":"MenuLong","m":0,"st":"Vous expliquez la poursuite pénale à une patiente qui vit en ménage commun avec son compagnon depuis cinq ans.",
 "p":"Choisissez les TROIS actes poursuivis d'office dans cette situation.","o":A(
  (1,"Des lésions corporelles simples infligées par le compagnon","Art. 123 ch. 2 CP."),
  (1,"Une menace grave proférée par le compagnon","Art. 180 al. 2 CP."),
  (1,"Des voies de fait réitérées du compagnon","Art. 126 al. 2 let. c CP."),
  (0,"Une voie de fait unique, sans lésion, du compagnon","Faux : poursuite sur plainte (art. 126 al. 1 CP)."),
  (0,"Un harcèlement obsessionnel du compagnon (art. 181b CP)","Faux : poursuite sur plainte."),
  (0,"Des lésions corporelles simples sans arme ni objet dangereux infligées par un ancien compagnon trois ans après la séparation","Faux : au-delà d'un an après la séparation, poursuite sur plainte (art. 123 ch. 1 CP)."),
  (0,"Une menace grave proférée par un ancien compagnon deux ans après la séparation","Faux : au-delà d'un an après la séparation, poursuite sur plainte (art. 180 al. 1 CP)."),
  (0,"Une voie de fait unique d'un ancien compagnon","Faux : poursuite sur plainte (art. 126 al. 1 CP)."),
  (0,"Une menace grave proférée par un voisin","Faux : hors couple, poursuite sur plainte (art. 180 al. 1 CP)."),
  (0,"Des lésions corporelles simples sans arme infligées par un collègue de travail","Faux : hors cas qualifiés, poursuite sur plainte (art. 123 ch. 1 CP)."),
  (0,"La révélation par le médecin du secret confié par la patiente","Faux : la violation du secret professionnel se poursuit sur plainte (art. 321 CP)."),
  (0,"Une voie de fait unique d'un voisin","Faux : poursuite sur plainte (art. 126 al. 1 CP).")),
 "n":n("office","stalk"),"a":"direct","d":3,
 "l":("Régime d'office.","Protection du couple.","Ménage commun.","Lésions, menaces, voies de fait réitérées.","Expliquer.","Croire tout d'office.","Trois actes d'office dans le couple.")},
]
for _q in Q: _q["src"] = [EXP]
_S = [[NICE,SHAR],[GLASS,SHAR,DOWN,EXP],[UMV,VQF,CP,SHAR],[NICE,VQFV,CC,BFA4],[USP,NICE,BFA2],[LAAM,CP,CC,VQF],[MAG,SHAR,HUG],[VQF,CC,NICE],[AVCH],[BFA4],[CP,VQF],[LAVI,NICE],[CP,VD26,CC,USP],[CP,CC,VQF],[SHAR,MAG,HUG,UMV],[BFA2,VQF,BFB6,GLASS],[CP,FR,CC],[USP,NICE,VQFV],[VQF,LAVI],[CP]]
for _q, _s in zip(Q, _S): _q["src"] = _s
C = {"theme":"Patient adulte victime de violence domestique ou de maltraitance au cabinet (porte O7.24, patients vulnérables) : repérage seul à seul et en présentiel, compression du cou souvent sans marque (risque d'homicide × 7,5), constat descriptif sans datation par la couleur, consultations médico-légales UMV et HUG, secret médical et droits d'aviser selon le canton (Fribourg, Vaud, LAAM, art. 314c CC), régime d'office et harcèlement obsessionnel depuis 2026, LAVI et 142 depuis le 1er mai 2026, enfants exposés, plan de sécurité",
 "notions":[
  {"titre":"Comprendre","rub":["definition","epidemiology","basicSciences","prognosisDischarge"],"comment":"La violence domestique touche surtout les femmes, mais aussi environ 30 % d'hommes parmi les victimes enregistrées ; l'emprise explique la minimisation et les retours.",
   "points":["2023 : 19 918 infractions, 70,1 % de victimes femmes.","Homicides 2009–2016 : 75 par an, mortels dans 34 % des cas.","Bénéfice : soutien continu à plusieurs composantes, pas une brochure seule."],"sources":[BFA4,BFA2,VQF,USP]},
  {"titre":"Reconnaître","rub":["anamnesis","clinicalExam","presumptionRedFlags","positiveDiagnosis"],"comment":"On demande seul à seul, en présentiel, avec un interprète professionnel, et l'on cherche les signes d'une compression du cou.",
   "arbre":[("d1",None,"Indices ou groupe à repérer","On voit le patient seul et l'on demande directement.",None,None),("d2","d1","Cou serré, perte de connaissance ou d'urines","On évalue le jour même, même sans marque.",None,None),("d3","d1","Séparation, grossesse, arme, menaces de mort","On considère le danger comme élevé.",None,None),("d4","d1","Dépendance pour soins ou argent","On explore la vulnérabilité, sans tiers présent.",None,None)],
   "points":["44 % sans marque après compression du cou.","Téléconsultation : un tiers peut entendre."],"sources":[NICE,USP,GLASS,SHAR]},
  {"titre":"Décider","rub":["workupGoldStandard","workupAlternatives","acuteManagement","chronicManagement"],"comment":"On documente, on protège et l'on respecte le secret de l'adulte capable de discernement, sauf base légale ou danger imminent.",
   "tab":(["Situation","Conduite","Base"],[["Adulte capable, pas de danger imminent","Consentement ou levée du secret",[("CP","Art. 321 ch. 2.")]],["Danger imminent","Police 117, état de nécessité",[("CP","Art. 17.")]],["Fribourg, crime ou délit corporel","Droit d'annonce au ministère public",[("FR","Art. 90a LSan.")]],["Arme d'ordonnance et indices de danger","Signalement au DDPS",[("LAAM","Art. 113 al. 7.")]],["Enfant exposé","Avis à l'APEA sans levée",[("CC","Art. 314c al. 2.")]]]),
   "points":["Constat le jour même, indépendant de la plainte, photos avec et sans règle.","Plan de sécurité : sac, code, 117 et 144, départ sans prévenir."],"sources":[UMV,VD26,FR,LAAM]},
  {"titre":"Suivre","rub":["hospitalizationComplications","surveillance","followUpNetwork"],"comment":"On revoit, on réévalue le danger, on protège les enfants et l'on oriente vers la LAVI et le juge civil.",
   "points":["142 depuis le 1er mai 2026 ; centre LAVI au choix, gratuit, sans plainte.","Voie de fait unique et harcèlement obsessionnel : sur plainte (3 mois)."],"sources":[LAVI,AVCH,CP,CC]}],
 "ssp":("O7.24","Patients vulnérables",True,[
   ("n1",None,"Indices de violence domestique ou de maltraitance","On voit le patient seul et l'on pose une question directe.","vd","c2"),
   ("n2","n1","Compression du cou ou danger imminent","On évalue le jour même et l'on appelle le 117 si besoin.","vd","c2"),
   ("n3","n1","Révélation sans danger imminent","On documente par un constat et l'on propose la consultation médico-légale.","vd","c3"),
   ("n4","n3","Adulte capable qui refuse","On garde le secret, sauf base légale cantonale ou fédérale.","vd","c3"),
   ("n5","n3","Enfants exposés ou arme d'ordonnance","On avise l'APEA ou le DDPS selon la base légale.","vd","c3"),
   ("n6","n3","Projet de départ","On construit le plan de sécurité et l'on oriente vers la LAVI.","vd","c4")]),
 "pec":[
  pec("vd","Violence domestique ou maltraitance chez l'adulte au cabinet",["On protège la vie et l'intégrité du patient et de ses enfants.","On documente les faits et l'on oriente vers le réseau en respectant l'autonomie."],
      ["On reçoit le patient seul, au calme, avec un interprète professionnel si besoin.","On croit le récit, on ne juge pas et l'on explique le secret médical."],
      [],
      [("social et assurances","On oriente vers un centre LAVI (142), une maison d'accueil ou l'hébergement d'urgence.","On donne au patient des ressources gratuites et confidentielles."),("psychothérapie","On propose une thérapie centrée sur le trauma en cas de symptômes post-traumatiques.","On traite les conséquences psychiques en réévaluant le danger."),("autre","On établit le constat de coups et blessures ou l'on adresse à la consultation médico-légale.","On préserve des preuves utiles même si la plainte vient plus tard.")],
      [("F Droit médical suisse","On applique le secret médical et les droits d'aviser fédéraux et cantonaux."),("C Communication clinique","On pose une question directe et bienveillante, seul à seul."),("N Médecine sociale Prévention OFSP","On mobilise le réseau d'aide aux victimes et la protection des enfants.")],
      (["On évalue le danger immédiat.","On protège le patient et les enfants.","On documente les lésions."],[("d'abord","médecin","Il évalue le danger, cherche une compression du cou et appelle le 117 si le danger est imminent."),("en même temps","médecin","Il examine et documente les lésions par un constat ou adresse à la consultation médico-légale."),("ensuite","centre LAVI","Il organise l'hébergement d'urgence et le soutien si le retour au domicile est dangereux.")]),
      (["On respecte le rythme du patient.","On réévalue le danger à chaque contact."],[("d'abord","médecin de famille","Il construit le plan de sécurité et remet les ressources sans document compromettant."),("puis","centre LAVI","Il conseille sur les droits, la plainte, l'indemnisation et les mesures civiles."),("ensuite","psychothérapeute","Il traite les symptômes post-traumatiques avec une réévaluation continue du danger.")]),
      "L'issue dépend du danger et du soutien ; la séparation reste la période la plus dangereuse, et un soutien continu améliore la situation.",
      [("Danger et plan de sécurité","À chaque consultation","Plan à jour, aucune nouvelle violence"),("Lésions et symptômes après compression du cou","Dans les jours qui suivent","Photographies de suivi, aucun signe neurologique")],"Le patient repart avec un plan de sécurité, les numéros 117, 144 et 142, et un rendez-vous de suivi.",
      ("On repère activement la violence domestique, seul à seul, dans les groupes à risque.","On documente tôt et l'on oriente vers la LAVI et la consultation médico-légale.","On suit les conséquences psychiques et l'on protège les enfants exposés.")),]}
