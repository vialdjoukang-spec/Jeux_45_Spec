ID = "I63.9_avc_de_la_circulatio__F1_15-E14"
PLAN = "monographique"
NOTIONS = [
"def|critère|1||[avis d'expert]|L'AVC de la circulation postérieure touche le territoire vertébro-basilaire : tronc cérébral, cervelet, thalamus et lobes occipitaux.",  # N01
"epi|chiffre|1||[Merwick, BMJ, 2014 ; à vérifier]|Environ un AVC ischémique sur cinq touche la circulation postérieure, et son diagnostic est plus souvent retardé que celui du territoire carotidien.",  # N02
"bas|mécanisme|1||[avis d'expert]|L'athérome vertébro-basilaire, l'embolie cardiaque et la dissection vertébrale sont les mécanismes principaux.",  # N03
"ana|symptôme|2||[avis d'expert]|Vertige, diplopie, dysarthrie, dysphagie, ataxie et déficit croisé ou bilatéral orientent vers le tronc cérébral ou le cervelet.",  # N04
"exa|signe|3||[Kattah, Stroke, 2009]|Devant un syndrome vestibulaire aigu, un test d'impulsion céphalique normal, un nystagmus changeant de direction ou un skew deviation indiquent une cause centrale (HINTS).",  # N05
"exa|signe|2||[Kattah, Stroke, 2009]|Une ataxie axiale qui empêche de tenir assis ou debout sans aide oriente vers une lésion cérébelleuse, même sans autre signe.",  # N06
"exa|signe|2||[avis d'expert]|Le syndrome de Wallenberg associe, du côté de la lésion, Horner, hypoesthésie thermo-algique faciale, ataxie et troubles de déglutition, et du côté opposé une hypoesthésie thermo-algique du corps.",  # N07
"exa|signe|1||[Lee, Stroke, 2002 ; avis d'expert]|Une surdité brusque unilatérale associée à un vertige aigu peut révéler un infarctus du territoire de l'AICA.",  # N08
"red|piège|3||[avis d'expert]|L'occlusion du tronc basilaire donne des troubles fluctuants de vigilance, une tétraparésie et des troubles oculomoteurs, et menace la vie si elle n'est pas recanalisée.",  # N09
"red|piège|2||[avis d'expert]|Le score NIHSS sous-estime la gravité des AVC postérieurs, car il pèse peu le vertige, l'ataxie axiale et la dysphagie.",  # N10
"gold|examen|2||[ESO, 2021 ; avis d'expert]|L'IRM de diffusion est l'examen de référence, mais elle peut être faussement normale dans les 24 à 48 premières heures pour les petits infarctus du tronc.",  # N11
"alt|examen|1||[avis d'expert]|Le scanner sans injection, peu sensible en fosse postérieure, s'associe à l'angio-CT qui montre l'occlusion basilaire ou vertébrale.",  # N12
"pos|diagnostic différentiel|2||[avis d'expert]|La névrite vestibulaire donne un test d'impulsion céphalique pathologique, un nystagmus unidirectionnel et une marche possible.",  # N13
"pos|diagnostic différentiel|1||[avis d'expert]|Le locked-in syndrome laisse une conscience intacte et des mouvements oculaires verticaux, qu'il faut chercher avant de conclure à un coma.",  # N14
"acu|décision|3||[ESO, 2021 ; AIPS Swissmedic]|La thrombolyse intraveineuse se discute dans les 4,5 heures selon les critères habituels, posologies à vérifier dans l'AIPS.",  # N15
"acu|décision|2||[ATTENTION, NEJM, 2022 ; BAOCHE, NEJM, 2022]|La thrombectomie mécanique améliore le pronostic fonctionnel de l'occlusion du tronc basilaire, selon les essais ATTENTION et BAOCHE.",  # N16
"acu|décision|1||[avis d'expert]|Un patient en filière AVC se transfère sans délai vers un stroke center capable de thrombectomie lorsque l'angio-CT montre une occlusion basilaire.",  # N17
"hos|complication|2||[ESO, 2021 ; avis d'expert]|Un infarctus cérébelleux étendu gonfle vers le 2e au 4e jour et menace par hydrocéphalie et compression du tronc, ce qui justifie une surveillance en unité spécialisée.",  # N18
"hos|décision|1||[ESO, 2021]|La craniectomie décompressive sous-occipitale ou la dérivation ventriculaire traitent l'œdème cérébelleux compressif.",  # N19
"hos|complication|1||[avis d'expert]|L'atteinte bulbaire expose à la fausse route et à l'insuffisance respiratoire, d'où le test de déglutition avant toute alimentation.",  # N20
"pro|pronostic|1||[avis d'expert]|L'occlusion basilaire non recanalisée a une mortalité très élevée, alors que de nombreux infarctus du tronc limités récupèrent bien.",  # N21
"sur|décision|1||[avis d'expert]|La surveillance neurologique rapprochée cherche une baisse de vigilance, qui signe l'œdème cérébelleux ou l'extension de la thrombose.",  # N22
"chr|décision|1||[ESO ; avis d'expert]|La prévention secondaire suit la cause : antiagrégation et statine pour l'athérome, anticoagulation pour la fibrillation auriculaire.",  # N23
"fol|contexte suisse|1|S|[SFCNS]|La filière suisse oriente les AVC aigus vers des stroke units et stroke centers certifiés par la SFCNS.",  # N24
"fol|décision|1||[avis d'expert]|La réadaptation traite l'ataxie, la dysphagie et les troubles oculomoteurs avec physiothérapie, logopédie et orthoptie.",  # N25
]
ANGLES = [
"HINTS central bat l'IRM précoce.",
"Ataxie axiale isolée : cervelet.",
"NIHSS bas mais AVC grave.",
"Basilaire : thrombectomie.",
"Œdème cérébelleux J2-J4.",
"Surdité + vertige : AICA.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un homme de 67 ans, hypertendu et fumeur, arrive aux urgences de Berne avec un vertige rotatoire continu depuis 3 heures, des vomissements et une incapacité à se tenir debout sans aide. Le test d'impulsion céphalique est normal des deux côtés et le nystagmus change de direction selon le regard.", prompt="Quelle interprétation est la plus juste ?",
 items=["*Le tableau est central et impose la filière AVC || Impulsion normale et nystagmus changeant signent une cause centrale.", "Il s'agit d'une névrite vestibulaire || Elle donne un test d'impulsion pathologique.", "Il s'agit d'un vertige positionnel paroxystique bénin || Le vertige est continu.", "Il s'agit d'une maladie de Ménière || Les crises durent des heures avec surdité fluctuante.", "Il s'agit d'une hypotension orthostatique || Le vertige est rotatoire continu."],
 notions="N05 N06 N04", angle="application", diff=3, ladder=L("Syndrome vestibulaire aigu.", "Central ou périphérique.", "Impulsion normale, nystagmus changeant.", "HINTS.", "Central : filière AVC.", "Névrite.", "HINTS central = AVC."), sources="[Kattah, Stroke, 2009]"),
dict(format="A", serie=("S1", 2, 4), stem="Chez cet homme, le scanner cérébral sans injection est normal à 3 h 30 du début.", prompt="Quelle conduite proposez-vous ?",
 items=["*Compléter par un angio-CT et discuter la thrombolyse dans le délai de 4,5 heures || Le scanner est peu sensible en fosse postérieure.", "Conclure à une cause périphérique || Le scanner normal n'exclut pas l'infarctus.", "Prescrire un antivertigineux et un retour à domicile || Le tableau est central.", "Attendre une IRM dans 1 semaine || Le délai thérapeutique serait perdu.", "Faire une manœuvre de libération || Elle traite le VPPB."],
 notions="N12 N15 N11", angle="application", diff=3, ladder=L("CT normal.", "Faible sensibilité en fosse postérieure.", "3 h 30.", "Délai thérapeutique.", "Angio-CT, thrombolyse.", "Rassurer.", "CT normal ≠ pas d'AVC."), sources="[ESO, 2021]"),
dict(format="A", serie=("S1", 3, 4), stem="L'IRM réalisée le lendemain montre un infarctus cérébelleux droit étendu. Au 3e jour, l'homme devient somnolent et vomit à nouveau.", prompt="Quelle complication suspectez-vous ?",
 items=["*Un œdème cérébelleux avec hydrocéphalie ou compression du tronc || Il survient vers le 2e au 4e jour.", "Une simple aggravation du vertige || La somnolence signe une compression.", "Une gastro-entérite || La somnolence oriente vers le cerveau.", "Une crise d'angoisse || La vigilance baisse.", "Une hypotension orthostatique || Elle n'explique pas la somnolence."],
 notions="N18 N22", angle="direct", diff=2, ladder=L("Somnolence J3.", "Effet de masse en fosse postérieure.", "Infarctus étendu.", "Complication.", "Œdème, hydrocéphalie.", "Vertige.", "J2-J4 : œdème."), sources="[ESO, 2021]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Le scanner confirme une hydrocéphalie aiguë avec compression du quatrième ventricule chez cet homme.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une craniectomie sous-occipitale décompressive peut sauver sa vie. || Elle lève la compression du tronc.", "V: Une dérivation ventriculaire traite l'hydrocéphalie. || Elle draine le LCR.", "F: Des corticoïdes suffisent à traiter l'œdème. || Ils n'ont pas montré de bénéfice.", "F: Une ponction lombaire soulage sans risque. || Elle expose à l'engagement."],
 notions="N19 N18", angle="application", diff=3, ladder=L("Hydrocéphalie.", "Compression.", "IVe ventricule.", "Traitement.", "Chirurgie, dérivation.", "Corticoïdes.", "Décompression."), sources="[ESO, 2021]"),
dict(format="A", stem="Un homme de 58 ans présente brusquement un vertige, une dysphagie, une voix rauque et un hoquet. Il a un ptosis et un myosis gauches, une hypoesthésie thermo-algique de l'hémiface gauche et de l'hémicorps droit, et une ataxie gauche.", prompt="Quelle localisation retenez-vous ?",
 items=["*Une lésion latérale gauche du bulbe || C'est le syndrome de Wallenberg.", "Une lésion capsulaire droite || Elle donne un déficit moteur facio-brachio-crural.", "Une lésion du lobe occipital gauche || Elle donne une hémianopsie.", "Une lésion médullaire cervicale || Elle ne donne pas d'atteinte faciale.", "Une lésion du nerf facial gauche || Elle ne donne pas de syndrome croisé."],
 notions="N07 N04", angle="direct", diff=3, ladder=L("Syndrome croisé.", "Noyaux bulbaires latéraux.", "Horner, IX-X, thermo-algie croisée.", "Localisation.", "Bulbe latéral gauche.", "Capsule.", "Croisé + dysphagie : Wallenberg."), sources="[avis d'expert]"),
dict(format="A", stem="Chez ce patient atteint d'un syndrome bulbaire latéral, l'équipe veut lui donner son repas.", prompt="Quelle mesure est prioritaire ?",
 items=["*Un test de déglutition avant toute alimentation orale || L'atteinte bulbaire expose à la fausse route.", "Une alimentation normale assise || Le risque de fausse route est élevé.", "Des liquides seulement || Ils sont les plus dangereux.", "Une sonde gastrique d'emblée pour tous || Le test guide la décision.", "Aucune mesure, la dysphagie disparaît en 1 heure || Elle peut durer."],
 notions="N20 N07", angle="application", diff=2, ladder=L("Dysphagie bulbaire.", "Noyau ambigu.", "Repas.", "Prévention.", "Test de déglutition.", "Liquides.", "Tester avant de nourrir."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 72 ans en fibrillation auriculaire non anticoagulée présente depuis 2 heures une dysarthrie et une diplopie fluctuantes, puis une somnolence croissante et une faiblesse des quatre membres.", prompt="Quel diagnostic devez-vous exclure en priorité ?",
 items=["*Une occlusion du tronc basilaire || Fluctuations, tétraparésie et vigilance menacée l'évoquent.", "Une hypoglycémie isolée || La glycémie se contrôle mais le tableau est vasculaire.", "Une myasthénie || Elle ne donne pas de somnolence brutale.", "Une migraine basilaire || Le terrain et la tétraparésie orientent ailleurs.", "Une crise d'angoisse || La vigilance baisse."],
 notions="N09 N03", angle="application", diff=3, ladder=L("Signes fluctuants.", "Ischémie du tronc.", "FA, somnolence, tétraparésie.", "Urgence absolue.", "Occlusion basilaire.", "Migraine.", "Fluctuant + vigilance : basilaire."), sources="[avis d'expert]"),
dict(format="A", stem="L'angio-CT de cette femme montre une occlusion du tronc basilaire, 3 heures après le début.", prompt="Quel traitement est indiqué ?",
 items=["*Une thrombectomie mécanique, associée à la thrombolyse si elle est possible || Les essais ATTENTION et BAOCHE montrent un bénéfice.", "De l'aspirine seule || Elle ne recanalise pas.", "Une héparine thérapeutique seule || Elle ne recanalise pas.", "Une surveillance clinique || La mortalité spontanée est très élevée.", "Une craniectomie || Elle ne traite pas l'occlusion."],
 notions="N16 N15 N21", angle="direct", diff=2, ladder=L("Occlusion basilaire.", "Recanalisation.", "3 heures.", "Thérapie de reperfusion.", "Thrombectomie ± thrombolyse.", "Aspirine.", "Basilaire : thrombectomie."), sources="[ATTENTION, NEJM, 2022]"),
dict(format="A", stem="Un homme de 54 ans présente brutalement un vertige rotatoire, une surdité gauche, des acouphènes et une paralysie faciale périphérique gauche.", prompt="Quel diagnostic évoquez-vous ?",
 items=["*Un infarctus du territoire de l'AICA gauche || Surdité et vertige brutaux avec atteinte du VII.", "Une névrite vestibulaire || Elle n'entraîne pas de surdité.", "Une maladie de Ménière || Elle n'entraîne pas de paralysie faciale.", "Un VPPB || Il est positionnel et bref.", "Un bouchon de cérumen || Il ne donne pas de vertige aigu."],
 notions="N08 N04", angle="piège", diff=3, ladder=L("Vertige + surdité.", "Artère labyrinthique.", "VII gauche.", "Territoire.", "AICA.", "Ménière.", "Surdité + vertige + VII : AICA."), sources="[Lee, Stroke, 2002]"),
dict(format="A", stem="Un homme de 61 ans a un vertige aigu et une ataxie axiale qui l'empêchent de s'asseoir. Son NIHSS est à 1. Un interne propose un retour à domicile.", prompt="Quelle remarque est la plus juste ?",
 items=["*Le NIHSS sous-estime les AVC postérieurs et l'ataxie axiale impose la filière AVC || Ce score pèse peu l'ataxie axiale.", "Un NIHSS à 1 exclut un AVC grave || Il sous-estime le territoire postérieur.", "Le retour est possible avec un antivertigineux || Le tableau est central.", "Une IRM différée de 1 mois suffit || L'œdème menace dans les jours suivants.", "Il faut seulement une physiothérapie vestibulaire || Le tableau est central."],
 notions="N10 N06", angle="piège", diff=2, ladder=L("NIHSS bas.", "Score centré sur le carotidien.", "Ataxie axiale.", "Biais du score.", "Filière AVC.", "Score rassurant.", "NIHSS bas ≠ bénin."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 48 ans a un vertige aigu depuis 24 heures. Le test d'impulsion céphalique est pathologique à droite, le nystagmus bat toujours vers la gauche, sans skew deviation. Elle marche avec aide.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Une névrite vestibulaire droite || Impulsion pathologique et nystagmus unidirectionnel l'évoquent.", "Un infarctus cérébelleux || Le HINTS est périphérique.", "Une occlusion basilaire || Rien ne l'évoque.", "Un syndrome de Wallenberg || Il manque les signes croisés.", "Un VPPB || Le vertige est continu."],
 notions="N13 N05", angle="application", diff=2, ladder=L("Vertige continu.", "Atteinte du nerf vestibulaire.", "Impulsion pathologique.", "HINTS périphérique.", "Névrite vestibulaire.", "AVC.", "Impulsion anormale : périphérique."), sources="[Kattah, Stroke, 2009]"),
dict(format="A", stem="Un homme de 65 ans paraît comateux, tétraplégique et anarthrique après une occlusion basilaire. Il ouvre les yeux et les élève sur ordre.", prompt="Quel état décrivez-vous ?",
 items=["*Un locked-in syndrome avec conscience préservée || Les mouvements verticaux des yeux persistent.", "Un coma profond || Il répond sur ordre.", "Un état végétatif || Il obéit aux ordres.", "Une mort cérébrale || Il répond.", "Un mutisme psychogène || La lésion est pontique."],
 notions="N14 N09", angle="piège", diff=3, ladder=L("Tétraplégie, anarthrie.", "Lésion ventrale du pont.", "Ordres oculaires.", "Conscience.", "Locked-in.", "Coma.", "Yeux verticaux : conscient."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Une IRM de diffusion faite 6 heures après un vertige aigu avec HINTS central est normale.", prompt="Quelle conclusion est la plus juste ?",
 items=["*Elle n'exclut pas un petit infarctus du tronc, et le HINTS central garde sa valeur || La diffusion peut être faussement normale tôt.", "Elle exclut définitivement un AVC || Elle peut être faussement normale.", "Elle impose une ponction lombaire || Rien ne l'indique.", "Elle prouve une névrite vestibulaire || Le HINTS est central.", "Elle rend la surveillance inutile || Le risque persiste."],
 notions="N11 N05", angle="piège", diff=3, ladder=L("IRM précoce normale.", "Sensibilité limitée.", "HINTS central.", "Interprétation.", "Ne pas exclure.", "Exclure l'AVC.", "IRM précoce peut mentir."), sources="[Kattah, Stroke, 2009]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 70 ans sort d'hospitalisation après un infarctus du tronc cérébral d'origine athéromateuse vertébrale.", prompt="Quelle prévention secondaire est adaptée ?",
 items=["*Antiagrégation plaquettaire, statine et contrôle tensionnel || L'athérome en est la cause.", "Anticoagulation au long cours sans indication cardiaque || Elle n'est pas indiquée pour l'athérome.", "Aucun traitement || La récidive est fréquente.", "Statine seule || L'antiagrégation est aussi nécessaire.", "Corticoïdes || Ils ne préviennent pas l'athérome."],
 notions="N23 N03", angle="application", diff=2, ladder=L("Prévention secondaire.", "Athérome.", "Vertébral.", "Selon la cause.", "Antiagrégant, statine, PA.", "Anticoaguler.", "Athérome : antiagrégant + statine."), sources="[ESO ; avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous enseignez la sémiologie des AVC vertébro-basilaires à Lausanne.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un déficit croisé oriente vers le tronc cérébral. || Les voies longues et les nerfs crâniens s'y croisent.", "V: Une diplopie aiguë avec dysarthrie oriente vers le tronc. || Elle signe une atteinte des noyaux.", "F: Un vertige isolé est toujours périphérique. || Un infarctus cérébelleux peut le donner.", "F: Le NIHSS mesure bien l'ataxie axiale. || Il la sous-estime."],
 notions="N04 N10 N06", angle="direct", diff=2, ladder=L("Enseignement.", "Territoire postérieur.", "Signes.", "Pièges.", "Croisé, diplopie.", "Vertige toujours bénin.", "Croisé = tronc."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Un AVC du tronc cérébral est suspecté chez une femme de 63 ans vue à Genève 2 heures après le début.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un angio-CT cherche une occlusion basilaire. || Elle change la stratégie.", "V: La thrombolyse se discute dans les 4,5 heures. || Les critères sont les mêmes qu'en carotidien.", "V: Une occlusion basilaire justifie un transfert vers un stroke center. || La thrombectomie y est possible.", "F: Un scanner normal exclut l'infarctus. || Il est peu sensible en fosse postérieure."],
 notions="N12 N15 N17 N24 N16", angle="application", diff=2, ladder=L("Suspicion d'AVC postérieur.", "Reperfusion.", "2 heures.", "Filière.", "Angio-CT, thrombolyse, transfert.", "CT rassurant.", "Angio-CT + transfert."), sources="[ESO, 2021]"),
dict(format="A", stem="Une femme de 76 ans présente une dysarthrie, une dysphagie et une respiration irrégulière avec des pauses depuis 1 heure. La saturation baisse.", prompt="Quelle mesure est prioritaire ?",
 items=["*Protéger les voies aériennes et préparer une ventilation si nécessaire || L'atteinte bulbaire menace la respiration.", "Lui faire boire de l'eau pour tester la déglutition || Le risque d'inhalation est majeur.", "Donner un sédatif || Il aggraverait l'hypoventilation.", "Attendre l'IRM sans surveillance || La respiration est menacée.", "Prescrire un antiémétique seul || Il ne protège pas les voies aériennes."],
 notions="N20 N09", angle="application", diff=2, ladder=L("Atteinte bulbaire.", "Centres respiratoires.", "Pauses, désaturation.", "ABC.", "Voies aériennes.", "Test à l'eau.", "Bulbe : airway d'abord."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Un homme de 66 ans hospitalisé pour un infarctus cérébelleux du territoire de la PICA est surveillé en stroke unit.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une baisse de vigilance doit faire chercher un œdème compressif. || L'œdème culmine vers J2-J4.", "V: La physiothérapie et la logopédie aident la récupération. || Elles traitent ataxie et dysphagie.", "F: Le risque d'œdème est maximal dans la première heure. || Il culmine vers J2-J4.", "F: Le pronostic de tous les infarctus postérieurs est sombre. || Les infarctus limités récupèrent souvent bien."],
 notions="N22 N25 N18 N21", angle="piège", diff=2, ladder=L("Surveillance.", "Œdème et récupération.", "PICA.", "Calendrier.", "Vigilance, rééducation.", "Pronostic sombre.", "J2-J4 + rééducation."), sources="[ESO, 2021]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un patient présente un syndrome vestibulaire aigu.", prompt="Quels signes orientent vers une cause centrale ? (3 réponses)",
 items=["*Test d'impulsion céphalique normal || Le réflexe vestibulo-oculaire est préservé.", "*Nystagmus changeant de direction || Il signe une atteinte centrale.", "*Skew deviation || Il signe une atteinte du tronc.", "Test d'impulsion pathologique || Il oriente vers le périphérique.", "Nystagmus unidirectionnel horizonto-rotatoire || Il oriente vers le périphérique.", "Nausées || Elles ne discriminent pas.", "Acouphènes isolés || Ils ne discriminent pas seuls.", "Vertige positionnel bref || Il évoque un VPPB.", "Inhibition du nystagmus par la fixation || Elle oriente vers le périphérique.", "Âge jeune || Il n'exclut rien.", "Absence de céphalée || Elle n'exclut rien.", "Antécédent de migraine || Il ne discrimine pas."],
 notions="N05 N13", angle="direct", diff=3, ladder=L("Vertige aigu.", "HINTS.", "Trois signes.", "Central.", "Impulsion normale, nystagmus changeant, skew.", "Impulsion pathologique.", "INFARCT."), sources="[Kattah, Stroke, 2009]"),
dict(masque=False, sit="monographique", format="MenuLong", stem="Un syndrome de Wallenberg gauche est diagnostiqué.", prompt="Quels signes trouvez-vous du côté gauche ? (3 réponses)",
 items=["*Syndrome de Claude Bernard-Horner || Le sympathique descendant est atteint.", "*Hypoesthésie thermo-algique de l'hémiface || Le noyau spinal du V est atteint.", "*Ataxie des membres || Le pédoncule cérébelleux inférieur est atteint.", "Hypoesthésie thermo-algique de l'hémicorps || Elle est controlatérale.", "Hémiparésie || La voie pyramidale est épargnée.", "Paralysie faciale centrale || Elle n'en fait pas partie.", "Hémianopsie || Elle relève de l'occipital.", "Aphasie || Elle relève du cortex.", "Paralysie du III || Elle relève du mésencéphale.", "Surdité || Elle relève de l'AICA.", "Atteinte de la sensibilité profonde de l'hémicorps || Le lemnisque médian est épargné.", "Paralysie du XII || Elle relève du bulbe médian."],
 notions="N07", angle="application", diff=4, ladder=L("Wallenberg.", "Bulbe latéral.", "Côté de la lésion.", "Signes homolatéraux.", "Horner, face, ataxie.", "Hémicorps homolatéral.", "Face homo, corps contro."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="AVC de la circulation postérieure : reconnaître le vertige central par le HINTS, ne pas se fier au NIHSS ni au scanner, recanaliser le tronc basilaire et surveiller l'œdème cérébelleux",
 notions=[
  dict(titre="Vertige aigu : central ou périphérique", rub=["exa", "pos", "red"], comment="Examine les yeux avant d'imager, car le HINTS bat l'IRM précoce.",
   tableau=(["Signe", "Périphérique (névrite)", "Central (AVC)", "Pourquoi"], [
     ["Impulsion céphalique", "Pathologique", "Normale", _T("Réflexe préservé", "Le nerf vestibulaire est intact dans l'AVC.")],
     ["Nystagmus", "Unidirectionnel", "Change de direction", _T("Intégrateur central", "Le cervelet ne maintient plus le regard.")],
     ["Skew deviation", "Absent", "Présent", _T("Voies otolithiques", "Le tronc est atteint.")],
     ["Marche", "Possible avec aide", "Impossible, ataxie axiale", _T("Vermis", "Il contrôle l'équilibre du tronc.")],
     ["Surdité brusque", "Rare", "Possible (AICA)", _T("Artère labyrinthique", "Elle naît de l'AICA.")]]),
   points=["Le NIHSS sous-estime ces AVC."], sources=["[Kattah, Stroke, 2009]"]),
  dict(titre="Syndromes topographiques", rub=["exa", "ana"], comment="Localise par les signes croisés et les nerfs crâniens.",
   tableau=(["Syndrome", "Artère", "Signes", "Piège"], [
     ["Wallenberg", "PICA ou vertébrale", "Horner, face thermo-algique, ataxie homolatéraux ; corps controlatéral", _T("Dysphagie", "Le noyau ambigu expose à la fausse route.")],
     ["AICA", "Cérébelleuse antéro-inférieure", "Vertige, surdité, VII, ataxie", _T("Surdité", "Elle fait croire à une cause ORL.")],
     ["Occlusion basilaire", "Tronc basilaire", "Vigilance fluctuante, tétraparésie, oculomotricité", _T("Locked-in", "Les yeux verticaux révèlent la conscience.")],
     ["Cérébelleux", "PICA, SCA", "Ataxie, vertige, vomissements", _T("Œdème", "Il comprime vers J2-J4.")]]),
   points=["Un déficit croisé signe le tronc."], sources=["[avis d'expert]"]),
  dict(titre="Phase aiguë", rub=["gold", "alt", "acu"], comment="Image les artères et recanalise vite.",
   arbre=[("a1", None, "Suspicion d'AVC postérieur", "Le scanner seul ne suffit pas."),
          ("a2", "a1", "Angio-CT", "Il cherche l'occlusion basilaire ou vertébrale.", "post"),
          ("a3", "a2", "Occlusion basilaire", "Thrombectomie ± thrombolyse, stroke center.", "post"),
          ("a4", "a2", "Pas d'occlusion, < 4,5 h", "Thrombolyse selon critères.", "post"),
          ("a5", "a1", "Atteinte bulbaire", "Voies aériennes et test de déglutition.", "post")],
   points=["IRM de diffusion faussement normale possible avant 48 h."], sources=["[ESO, 2021]", "[ATTENTION, NEJM, 2022]"]),
  dict(titre="Complications et suite", rub=["hos", "pro", "chr", "fol"], comment="Surveille la vigilance et adapte la prévention à la cause.",
   tableau=(["Thème", "Conduite", "Pourquoi"], [
     ["Œdème cérébelleux", "Surveillance J2-J4, craniectomie ou dérivation", "Il comprime le tronc et le IVe ventricule."],
     ["Dysphagie", "Test de déglutition", "La fausse route menace."],
     ["Athérome", "Antiagrégant, statine, PA", "Il cause la récidive."],
     ["FA", "Anticoagulation", "Elle prévient l'embolie."],
     ["Réadaptation", "Physiothérapie, logopédie, orthoptie", "Elles traitent ataxie, dysphagie, diplopie."]]),
   points=["La basilaire non recanalisée est souvent fatale."], sources=["[ESO, 2021]"]),
 ],
 ssp=dict(code="S7.5", nom="Étourdissements, vertiges", officiel=True, algorithme=[
  ("n1", None, "Vertige", "La durée et le déclenchement orientent."),
  ("n2", "n1", "Bref et positionnel", "VPPB : Dix-Hallpike (même SSP).", None, "c1"),
  ("n3", "n1", "Continu (syndrome vestibulaire aigu)", "Le HINTS tranche.", None, "c1"),
  ("n4", "n3", "HINTS périphérique, marche possible", "Névrite vestibulaire.", None, "c1"),
  ("n5", "n3", "HINTS central ou ataxie axiale", "Filière AVC.", "post", "c1"),
  ("n6", "n3", "Surdité brusque associée", "Infarctus AICA à exclure.", "post", "c2"),
  ("n7", "n5", "Angio-CT", "Occlusion basilaire : thrombectomie.", "post", "c3"),
  ("n8", "n5", "Infarctus cérébelleux", "Surveiller l'œdème J2-J4.", "post", "c4"),
  ("n9", "n1", "Vertige avec vigilance fluctuante", "Occlusion basilaire : urgence absolue.", "post", "c2")]),
 pec=[
  dict(cle="post", titre="AVC de la circulation postérieure",
   but=["Recanaliser vite.", "Prévenir l'œdème compressif et la fausse route."],
   moyens=dict(accueil=["HINTS et recherche d'ataxie axiale.", "Scanner et angio-CT immédiats."],
    pharma=[("Alteplase ou ténectéplase (thrombolytique)", "Dans les 4,5 heures selon critères ; à vérifier dans l'AIPS.", "Elle recanalise l'artère.", "[ESO, 2021 ; AIPS Swissmedic]"),
            ("Acide acétylsalicylique (antiagrégant)", "Après exclusion d'une hémorragie ; à vérifier dans l'AIPS.", "Il réduit la récidive précoce.", "[ESO]"),
            ("Atorvastatine (statine)", "Haute intensité ; à vérifier dans l'AIPS.", "Elle stabilise l'athérome.", "[ESO]")],
    nonpharma=[("geste ou chirurgie", "Thrombectomie basilaire ; craniectomie sous-occipitale si œdème.", "Elles recanalisent et décompriment."),
               ("rééducation", "Physiothérapie, logopédie, orthoptie.", "Elles traitent ataxie, dysphagie, diplopie.")],
    transversal=[("ORL", "Elle aide à distinguer cause périphérique et centrale."), ("Neurochirurgie", "Elle traite l'œdème cérébelleux.")]),
   urgence=(["Angio-CT immédiat.", "Protection des voies aériennes si atteinte bulbaire."],
            [("d'abord", "médecin urgentiste", "Fait le HINTS et active la filière AVC."),
             ("en même temps", "infirmier·ère", "Surveille vigilance et saturation, ne donne rien per os."),
             ("ensuite", "neurologue", "Décide thrombolyse et thrombectomie."),
             ("puis", "neuroradiologue", "Réalise la thrombectomie.")]),
   horsUrgence=(["Prévention secondaire selon la cause.", "Réadaptation."],
            [("d'abord", "neurologue", "Établit la cause."),
             ("ensuite", "équipe de réadaptation", "Rééduque."),
             ("puis", "médecin de famille", "Contrôle facteurs de risque.")]),
   pronostic="L'occlusion basilaire non recanalisée tue souvent ; les infarctus limités récupèrent fréquemment.",
   suivi=[("Vigilance", "Horaire J1-J4", "Stable"), ("Déglutition", "Avant tout repas", "Sûre"), ("Facteurs de risque", "À chaque consultation", "Cibles atteintes")],
   sortie="La sortie suit la stabilisation, la sécurité de la déglutition et l'organisation de la réadaptation.",
   prevention=["Elle traite l'athérome par antiagrégant et statine.", "Elle anticoagule la fibrillation auriculaire.", "Elle contrôle PA et tabac."]),
 ])
AVERIFIER = ["Proportion des AVC ischémiques de la circulation postérieure et référence Merwick BMJ 2014 à vérifier.",
             "Doses d'alteplase et de ténectéplase à vérifier dans l'AIPS.",
             "Référence exacte de Lee, Stroke, 2002 sur l'infarctus AICA et la surdité à vérifier."]
