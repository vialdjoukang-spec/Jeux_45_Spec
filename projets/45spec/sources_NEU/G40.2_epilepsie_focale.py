ID = "G40.2_epilepsie_focale_tem__G11-E17"
PLAN = "monographique"
NOTIONS = [
"def|critère|1||[Beniczky, ILAE, Epilepsia, 2025]|Une crise focale naît dans un réseau limité à un hémisphère ; l'ILAE 2025 la classe selon que la conscience reste préservée ou devient altérée.",  # N01
"epi|chiffre|1||[avis d'expert]|L'épilepsie temporale mésiale est l'épilepsie focale la plus fréquente de l'adulte et s'associe souvent à une sclérose hippocampique.",  # N02
"bas|mécanisme|1||[avis d'expert]|La sclérose hippocampique perd des neurones et se gliose ; elle suit souvent des convulsions fébriles prolongées de l'enfance.",  # N03
"ana|signe|3||[avis d'expert]|La crise temporale mésiale commence par une aura épigastrique ascendante ou un déjà-vu, puis le patient fixe, mâchonne, manipule d'une main et reste confus après la crise.",  # N04
"ana|signe|2||[avis d'expert]|La crise frontale est brève, souvent nocturne et en salves, hypermotrice, et la récupération est rapide.",  # N05
"ana|signe|1||[avis d'expert]|La crise jacksonienne propage des clonies selon la somatotopie, et une parésie de Todd peut la suivre quelques heures.",  # N06
"exa|signe|1||[avis d'expert]|L'examen intercritique est souvent normal ; une aphasie postcritique latéralise la crise dans l'hémisphère dominant.",  # N07
"red|piège|2||[avis d'expert]|Une première crise focale chez l'adulte impose de chercher une lésion structurelle (tumeur, AVC, cavernome) par IRM.",  # N08
"gold|examen|3||[Bernasconi, ILAE, Epilepsia, 2019]|L'IRM au protocole épilepsie (coupes coronales T2 et FLAIR fines) et l'EEG fondent le bilan ; la sclérose hippocampique montre une atrophie et un hypersignal T2/FLAIR.",  # N09
"alt|examen|1||[avis d'expert]|Un EEG standard normal n'exclut rien ; l'EEG après privation de sommeil et la vidéo-EEG précisent le diagnostic.",  # N10
"pos|diagnostic différentiel|2||[avis d'expert]|La syncope convulsivante, l'AIT, l'aura migraineuse et les crises non épileptiques psychogènes se distinguent par le contexte, la durée et la récupération.",  # N11
"acu|décision|2||[Fisher, ILAE, Epilepsia, 2014]|Une seule crise non provoquée suffit à diagnostiquer une épilepsie si le risque de récidive atteint au moins 60 %, par exemple avec une lésion et un EEG épileptiforme.",  # N12
"chr|molécule|3||[SANAD II, Lancet, 2021]|La lamotrigine reste le traitement de premier choix de l'épilepsie focale ; le lévétiracétam et le zonisamide ont été moins efficaces dans SANAD II.",  # N13
"chr|posologie|1||[AIPS Swissmedic]|La lamotrigine se titre lentement pour limiter le risque d'éruption grave, et plus lentement encore avec le valproate, qui double son taux ; à vérifier dans l'AIPS.",  # N14
"chr|piège|2||[Swissmedic ; EMA PRAC, 2018]|Le valproate s'évite chez la femme en âge de procréer, car il est tératogène et nuit au neurodéveloppement de l'enfant.",  # N15
"chr|piège|2||[AIPS Swissmedic]|La carbamazépine, inducteur enzymatique, réduit l'efficacité de la contraception hormonale, et les œstrogènes abaissent le taux de lamotrigine.",  # N16
"hos|complication|1||[avis d'expert]|La mort subite inattendue en épilepsie (SUDEP) menace surtout les patients aux crises tonico-cloniques nocturnes non contrôlées.",  # N17
"chr|seuil|2||[Kwan, ILAE, Epilepsia, 2010]|L'épilepsie devient pharmacorésistante après l'échec de deux médicaments bien choisis, bien tolérés et bien pris ; le patient doit alors aller en centre d'épilepsie.",  # N18
"chr|chiffre|2||[Wiebe, NEJM, 2001]|Après lobectomie temporale, 58 % des patients étaient libres de crises altérant la conscience à 1 an, contre 8 % sous médicaments.",  # N19
"pro|pronostic|1||[Kwan, NEJM, 2000]|Les chances de rémission baissent nettement après l'échec de chaque médicament bien choisi.",  # N20
"sur|examen|1||[avis d'expert]|Le suivi compte les crises dans un agenda, cherche les effets indésirables et dépiste l'humeur.",  # N21
"fol|contexte suisse|1|S|[Ligue suisse contre l'épilepsie, 2019]|En Suisse, le permis privé exige en général un an sans crise ; le permis professionnel exige cinq ans sans crise et sans traitement.",  # N22
"fol|terrain particulier|1||[avis d'expert]|La grossesse se planifie : acide folique, lamotrigine ou lévétiracétam, et dosage de la lamotrigine qui baisse pendant la grossesse.",  # N23
"fol|terrain particulier|1||[avis d'expert]|La dépression et l'anxiété accompagnent souvent l'épilepsie temporale, et le lévétiracétam peut rendre irritable.",  # N24
"hos|complication|1||[avis d'expert]|La lobectomie temporale peut laisser une quadranopsie supérieure controlatérale et un trouble de la mémoire verbale à gauche.",  # N25
]
ANGLES = [
"Aura épigastrique + mâchonnement = temporale.",
"IRM protocole épilepsie + EEG.",
"Lamotrigine d'abord (SANAD II).",
"Deux échecs = centre d'épilepsie.",
"Pas de valproate chez la jeune femme.",
"Un an sans crise pour conduire.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Un informaticien de 34 ans, à Fribourg, décrit des épisodes mensuels : une sensation qui monte de l'estomac et une impression de déjà-vu, puis il fixe le vide, mâchonne et tripote ses vêtements de la main droite pendant 2 minutes. Il reste confus 10 minutes et ne s'en souvient pas. Il a fait une longue convulsion fébrile à 2 ans.", prompt="Quel diagnostic est le plus probable ?",
 items=["*Des crises focales à conscience altérée d'origine temporale mésiale || Aura épigastrique, automatismes et confusion postcritique.", "Des absences typiques || Elles durent quelques secondes, sans aura ni confusion.", "Des crises non épileptiques psychogènes || La sémiologie est stéréotypée et typique.", "Des AIT || Ils donnent des symptômes négatifs.", "Des crises frontales || Elles sont brèves, hypermotrices, sans confusion."],
 notions="N04 N01 N02 N03", angle="application", diff=1, ladder=L("Épisodes stéréotypés.", "Crise focale.", "Aura épigastrique.", "Origine.", "Temporale mésiale.", "Absence.", "Aura + automatismes = temporale."), sources="[Beniczky, ILAE, 2025]"),
dict(format="A", serie=("S1", 2, 4), stem="L'examen neurologique de cet homme est normal entre les crises.", prompt="Quel bilan est le plus utile ?",
 items=["*Une IRM au protocole épilepsie et un EEG || Ils cherchent la lésion et l'activité épileptiforme.", "Un scanner cérébral seul || Il manque la sclérose hippocampique.", "Une ponction lombaire || Rien ne l'indique.", "Un Holter ECG seul || Il ne répond pas à la question.", "Aucun examen || Une épilepsie focale doit s'explorer."],
 notions="N09 N10", angle="direct", diff=1, ladder=L("Bilan.", "Imagerie et électrophysiologie.", "Examen normal.", "Choix.", "IRM protocole + EEG.", "Scanner.", "IRM dédiée."), sources="[Bernasconi, ILAE, 2019]"),
dict(format="A", serie=("S1", 3, 4), stem="L'IRM montre un hippocampe gauche atrophique en hypersignal FLAIR. L'EEG montre des pointes temporales gauches.", prompt="Quel traitement de fond proposez-vous en premier ?",
 items=["*La lamotrigine, titrée lentement || Elle est le premier choix des épilepsies focales.", "Le valproate || Il est moins efficace dans les crises focales.", "L'éthosuximide || Il ne traite que les absences.", "Une lobectomie temporale d'emblée || La chirurgie suit l'échec de deux médicaments.", "Le clonazépam au long cours || Il expose à la tolérance."],
 notions="N13 N14 N09", angle="application", diff=2, ladder=L("Sclérose hippocampique.", "Traitement de fond.", "Épilepsie focale.", "Premier choix.", "Lamotrigine.", "Chirurgie d'emblée.", "Lamotrigine d'abord."), sources="[SANAD II, Lancet, 2021]"),
dict(format="Kprim", serie=("S1", 4, 4), stem="Cet homme conduit tous les jours pour son travail de bureau et demande quand il pourra reprendre le volant.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Il doit en général rester un an sans crise avant de conduire une voiture. || C'est la règle suisse du permis privé.", "V: Ses crises altèrent la conscience, ce qui rend la conduite dangereuse. || La perte de contrôle est probable.", "F: Il pourra conduire un camion après un an sans crise. || Le permis professionnel exige 5 ans sans crise et sans traitement.", "F: Une seule crise ne permet jamais de parler d'épilepsie. || Un risque de récidive ≥ 60 % suffit."],
 notions="N22 N12 N04", angle="application", diff=2, ladder=L("Conduite.", "Aptitude.", "Suisse.", "Délais.", "1 an privé, 5 ans pro.", "Camion.", "Un an sans crise."), sources="[Ligue suisse contre l'épilepsie, 2019]"),
dict(format="A", stem="Une enseignante de 26 ans souhaite une grossesse dans deux ans. Elle a une épilepsie focale nouvellement diagnostiquée.", prompt="Quel médicament évitez-vous ?",
 items=["*Le valproate || Il est tératogène et nuit au neurodéveloppement.", "La lamotrigine || Elle est un bon choix chez la femme jeune.", "Le lévétiracétam || Il est une alternative acceptable.", "L'acide folique || Il se recommande.", "Aucun, tous se valent || Le valproate s'évite."],
 notions="N15 N23", angle="application", diff=1, ladder=L("Jeune femme.", "Choix du médicament.", "Projet de grossesse.", "Tératogénicité.", "Valproate.", "Lamotrigine.", "Jamais de valproate."), sources="[Swissmedic ; EMA PRAC, 2018]"),
dict(format="A", stem="Une femme de 31 ans prend de la carbamazépine pour une épilepsie focale et une pilule œstroprogestative. Elle découvre une grossesse non désirée.", prompt="Quelle explication est la plus probable ?",
 items=["*L'induction enzymatique de la carbamazépine a réduit l'efficacité de la pilule || La carbamazépine accélère le métabolisme des hormones.", "La pilule a abaissé le taux de carbamazépine || C'est l'inverse qui compte ici.", "La carbamazépine provoque l'ovulation || Ce n'est pas le mécanisme.", "Les crises ont empêché l'absorption || Rien ne l'indique.", "La grossesse est sans lien || L'interaction est classique."],
 notions="N16 N15", angle="piège", diff=2, ladder=L("Échec contraceptif.", "Interaction.", "Carbamazépine.", "Mécanisme.", "Induction enzymatique.", "Hasard.", "Inducteur = pilule inefficace."), sources="[AIPS Swissmedic]"),
dict(format="A", stem="Un homme de 38 ans a encore 3 crises focales par mois après la lamotrigine puis le lévétiracétam, pris correctement à dose efficace et bien tolérés. L'IRM montre une sclérose hippocampique droite.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*L'adresser à un centre d'épilepsie pour un bilan préchirurgical || L'épilepsie est pharmacorésistante.", "Essayer successivement tous les autres antiépileptiques || Les chances baissent à chaque échec.", "Augmenter les doses au-delà de la tolérance || Elle exposerait à la toxicité.", "Accepter les crises et ne rien changer || La chirurgie peut le guérir.", "Arrêter tous les médicaments || Il récidiverait."],
 notions="N18 N19 N20", angle="application", diff=2, ladder=L("Échecs répétés.", "Pharmacorésistance.", "Deux médicaments.", "Orientation.", "Centre d'épilepsie.", "Troisième molécule.", "Deux échecs = chirurgie."), sources="[Kwan, ILAE, 2010]"),
dict(masque=False, sit="monographique", format="A", stem="Vous expliquez à un patient pharmacorésistant les résultats de l'essai randomisé de Wiebe sur l'épilepsie temporale.", prompt="Quel résultat est exact ?",
 items=["*58 % des opérés contre 8 % des patients sous médicaments étaient libres de crises altérant la conscience à 1 an || C'est le critère principal de l'essai.", "La chirurgie n'a pas fait mieux que les médicaments || Elle a été nettement supérieure.", "Tous les opérés ont arrêté leurs médicaments || Ce n'est pas le résultat.", "La chirurgie a doublé la mortalité || Ce n'est pas observé.", "Le bénéfice ne concernait que les enfants || L'essai portait sur des adultes et adolescents."],
 notions="N19 N25", angle="direct", diff=3, ladder=L("Chirurgie.", "Essai randomisé.", "Lobectomie temporale.", "Résultat.", "58 % contre 8 %.", "Équivalence.", "Chirurgie supérieure."), sources="[Wiebe, NEJM, 2001]"),
dict(format="A", stem="Un homme de 58 ans a présenté des secousses de la main droite qui ont gagné l'avant-bras puis la face en une minute. Sa main reste faible deux heures plus tard.", prompt="Quelle conduite est prioritaire ?",
 items=["*Une IRM cérébrale pour chercher une lésion structurelle || Une première crise focale de l'adulte peut révéler une tumeur ou un AVC.", "Rassurer, car la faiblesse est une simple parésie de Todd || Elle n'exclut pas une lésion.", "Prescrire du valproate et revoir dans 6 mois || La cause prime.", "Un EEG seul || Il ne cherche pas la lésion.", "Un bilan psychiatrique || La marche jacksonienne est organique."],
 notions="N08 N06", angle="piège", diff=2, ladder=L("Marche jacksonienne.", "Crise focale motrice.", "58 ans.", "Cause.", "IRM.", "Todd rassurant.", "Focale adulte = lésion ?"), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 24 ans est réveillée plusieurs fois par nuit par des épisodes de 30 secondes : elle pédale, crie et se tord, puis se rendort aussitôt. Les épisodes sont identiques d'une fois à l'autre.", prompt="Quel diagnostic évoquez-vous d'abord ?",
 items=["*Des crises focales frontales hypermotrices || Brèves, nocturnes, en salves, stéréotypées.", "Des terreurs nocturnes || Elles sont rares chez l'adulte et non stéréotypées.", "Des crises temporales mésiales || Elles s'accompagnent de confusion prolongée.", "Des crises non épileptiques psychogènes || Elles surviennent rarement pendant le sommeil réel.", "Un trouble panique || Il ne donne pas d'épisodes stéréotypés."],
 notions="N05 N11", angle="application", diff=2, ladder=L("Épisodes nocturnes.", "Crise focale.", "Brève, hypermotrice.", "Localisation.", "Frontale.", "Parasomnie.", "Nocturne stéréotypée = frontale."), sources="[avis d'expert]"),
dict(format="A", stem="Un étudiant de 22 ans s'est effondré après une longue station debout dans un bus surchauffé. Il était pâle et nauséeux avant. Il a eu 10 secondes de secousses et a repris conscience aussitôt, bien orienté.", prompt="Quelle conduite est la plus adaptée ?",
 items=["*Retenir une syncope convulsivante, sans antiépileptique || Prodromes, brièveté et récupération rapide l'indiquent.", "Débuter la lamotrigine || Ce n'est pas une crise épileptique.", "Interdire la conduite pendant 5 ans || La règle ne s'applique pas.", "Demander une IRM au protocole épilepsie en urgence || Le contexte est syncopal.", "Retenir des crises non épileptiques psychogènes || La syncope l'explique."],
 notions="N11 N12", angle="piège", diff=2, ladder=L("Malaise.", "Syncope ou crise.", "Prodromes.", "Récupération.", "Syncope convulsivante.", "Épilepsie.", "Secousses ≠ épilepsie."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Vous préparez une présentation sur l'épilepsie focale pharmacorésistante.", prompt="Quelle définition de l'ILAE retenez-vous ?",
 items=["*L'échec de deux médicaments bien choisis, bien tolérés et bien pris || C'est la définition de 2010.", "L'échec d'un seul médicament || Un second médicament garde des chances.", "L'échec de cinq médicaments || Ce seuil retarderait la chirurgie.", "Plus d'une crise par mois || La fréquence ne définit pas la résistance.", "Un EEG anormal sous traitement || Il ne définit pas la résistance."],
 notions="N18 N20", angle="direct", diff=2, ladder=L("Définition.", "Pharmacorésistance.", "ILAE.", "Seuil.", "Deux échecs.", "Un échec.", "Deux médicaments bien pris."), sources="[Kwan, ILAE, 2010]"),
dict(format="A", stem="Une femme de 40 ans sous valproate pour une épilepsie ancienne reçoit en plus la lamotrigine, débutée à 100 mg par jour. Dix jours plus tard, elle a de la fièvre, une éruption étendue et des érosions buccales.", prompt="Quelle erreur explique cette situation ?",
 items=["*Une titration trop rapide de la lamotrigine en présence de valproate || Le valproate double le taux de lamotrigine.", "Une allergie au valproate pris depuis des années || La chronologie désigne la lamotrigine.", "Une infection virale sans lien || L'éruption grave est un effet connu.", "Une dose trop faible de lamotrigine || C'est l'inverse.", "Une interaction avec la pilule || Elle n'en prend pas."],
 notions="N14 N13", angle="piège", diff=3, ladder=L("Éruption grave.", "Toxidermie.", "Lamotrigine + valproate.", "Titration.", "Trop rapide.", "Virus.", "Titrer lentement."), sources="[AIPS Swissmedic]"),
dict(format="A", stem="Un homme de 45 ans a fait une première crise focale à conscience altérée. L'IRM montre une cicatrice d'AVC ancien et l'EEG des pointes dans la même région.", prompt="Quelle décision prenez-vous ?",
 items=["*Retenir une épilepsie et discuter un traitement de fond || Le risque de récidive dépasse 60 %.", "Attendre une deuxième crise avant de parler d'épilepsie || Une crise suffit ici.", "Ne rien faire, la crise était provoquée || Elle n'est pas aiguë symptomatique.", "Hospitaliser en soins intensifs || La crise est terminée.", "Prescrire une benzodiazépine quotidienne || Elle n'est pas un traitement de fond."],
 notions="N12 N08", angle="application", diff=2, ladder=L("Première crise.", "Définition pratique.", "Lésion + EEG.", "Risque de récidive.", "Épilepsie.", "Attendre.", "Risque ≥ 60 % = épilepsie."), sources="[Fisher, ILAE, 2014]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous enseignez la sémiologie des crises focales.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: L'aura épigastrique ascendante oriente vers une crise temporale mésiale. || C'est l'aura la plus typique.", "V: Une aphasie postcritique latéralise la crise dans l'hémisphère dominant. || Le langage y est atteint.", "F: La crise frontale donne une confusion prolongée. || La récupération est rapide.", "F: L'examen intercritique est le plus souvent anormal. || Il est souvent normal."],
 notions="N04 N05 N07", angle="direct", diff=2, ladder=L("Sémiologie.", "Localisation.", "Aura, aphasie.", "Pièges.", "Temporale vs frontale.", "Confusion frontale.", "Aura épigastrique = temporale."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Une femme de 36 ans est suivie pour des crises focales sous lévétiracétam. Elle a encore 2 crises nocturnes généralisées par an.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Un agenda des crises guide les ajustements. || Il objective la fréquence.", "V: Son humeur doit se dépister à chaque visite. || Le lévétiracétam peut rendre irritable ou déprimé.", "F: Le risque de SUDEP ne dépend pas du contrôle des crises. || Il augmente avec les crises tonico-cloniques nocturnes.", "F: Le taux sanguin de tout antiépileptique se dose à chaque visite. || Le dosage est ciblé."],
 notions="N21 N24 N17", angle="application", diff=2, ladder=L("Suivi.", "Surveillance.", "Crises nocturnes.", "Risques.", "Agenda, humeur, SUDEP.", "Dosage systématique.", "Contrôler les crises nocturnes."), sources="[avis d'expert]"),
dict(format="Kprim", stem="Une femme de 30 ans sous lamotrigine pour une épilepsie focale est enceinte de 8 semaines.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Elle doit poursuivre son traitement. || Les crises exposent la mère et le fœtus.", "V: Le taux de lamotrigine baisse souvent pendant la grossesse. || Les œstrogènes accélèrent son élimination.", "F: Il faut passer au valproate, plus sûr. || Il est le plus tératogène.", "F: L'acide folique est contre-indiqué. || Il se recommande."],
 notions="N23 N16 N15", angle="application", diff=2, ladder=L("Grossesse.", "Épilepsie et grossesse.", "Lamotrigine.", "Taux.", "Poursuivre, doser.", "Valproate.", "Doser la lamotrigine."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un patient décrit ses crises.", prompt="Quels éléments orientent vers une crise temporale mésiale ? (3 réponses)",
 items=["*Aura épigastrique ascendante || Elle est typique.", "*Impression de déjà-vu || Elle traduit l'atteinte hippocampique.", "*Mâchonnement et automatismes manuels || Ils sont typiques.", "Crises de 20 secondes en salves nocturnes || Elles évoquent le lobe frontal.", "Récupération immédiate || Elle évoque le lobe frontal.", "Pédalage violent || Il évoque le lobe frontal.", "Phosphènes colorés || Ils évoquent le lobe occipital.", "Marche jacksonienne || Elle évoque le cortex moteur.", "Paresthésies d'un hémicorps progressives || Elles évoquent le cortex sensitif.", "Pâleur et nausées debout avant la chute || Elles évoquent une syncope.", "Myoclonies au réveil || Elles évoquent une épilepsie généralisée.", "Rupture de contact de 5 secondes sans aura || Elle évoque une absence."],
 notions="N04 N05", angle="direct", diff=1, ladder=L("Sémiologie.", "Lobe temporal.", "Aura.", "Lesquels.", "Épigastre, déjà-vu, mâchonnement.", "Salves nocturnes.", "Aura + automatismes."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Un homme de 50 ans a perdu connaissance au travail. Un collègue a assisté à l'épisode.", prompt="Quels éléments orientent vers une crise épileptique plutôt qu'une syncope ? (3 réponses)",
 items=["*Morsure latérale de la langue || Elle est spécifique d'une crise.", "*Confusion postcritique de plusieurs minutes || Elle suit la crise.", "*Déjà-vu juste avant la perte de connaissance || C'est une aura.", "Prodromes de chaleur et de nausée || Ils évoquent une syncope.", "Survenue en station debout prolongée || Elle évoque une syncope.", "Récupération en quelques secondes || Elle évoque une syncope.", "Pâleur intense || Elle évoque une syncope.", "Secousses de 10 secondes || Elles s'observent aussi dans la syncope.", "Survenue à la vue du sang || Elle évoque une syncope vasovagale.", "Sueurs avant la chute || Elles évoquent une syncope.", "Bradycardie mesurée || Elle évoque une syncope.", "Vision qui se voile progressivement || Elle évoque une syncope."],
 notions="N11 N04", angle="application", diff=2, ladder=L("Perte de connaissance.", "Crise ou syncope.", "Témoin.", "Discriminants.", "Langue, confusion, aura.", "Secousses.", "Confusion = crise."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Un homme de 33 ans a subi une lobectomie temporale antérieure droite pour une épilepsie pharmacorésistante.", prompt="Quel déficit séquellaire est le plus attendu ?",
 items=["*Une quadranopsie supérieure gauche || Les radiations optiques temporales (anse de Meyer) sont lésées.", "Une hémiplégie gauche || Le cortex moteur n'est pas touché.", "Une aphasie de Broca || L'hémisphère est non dominant et frontal.", "Une hémianopsie inférieure droite || Elle est du mauvais côté et pariétale.", "Une paralysie faciale périphérique || Le nerf facial n'est pas en cause."],
 notions="N25 N19", angle="direct", diff=3, ladder=L("Après chirurgie.", "Voies visuelles.", "Lobe temporal droit.", "Anse de Meyer.", "Quadranopsie supérieure gauche.", "Hémianopsie.", "Temporal = quadrant supérieur."), sources="[avis d'expert]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Épilepsie focale : reconnaître la sémiologie temporale, frontale et jacksonienne, chercher la lésion par IRM et EEG, traiter d'abord par lamotrigine, éviter le valproate chez la jeune femme et adresser au centre d'épilepsie après deux échecs",
 notions=[
  dict(titre="Reconnaître la crise focale", rub=["def", "ana", "exa"], comment="Localise la crise par sa sémiologie.",
   tableau=(["Lobe", "Signes", "Après la crise"], [
     ["Temporal mésial", _T("Aura épigastrique, déjà-vu, mâchonnement", "L'hippocampe et l'amygdale sont en cause."), "Confusion de plusieurs minutes"],
     ["Frontal", "Bref, nocturne, hypermoteur, en salves", "Récupération rapide"],
     ["Central (jacksonien)", "Clonies à marche somatotopique", _T("Parésie de Todd", "Elle régresse en quelques heures.")]]),
   points=["ILAE 2025 : conscience préservée ou altérée."], sources=["[Beniczky, ILAE, 2025]"]),
  dict(titre="Explorer", rub=["red", "gold", "alt", "pos"], comment="Cherche la lésion et élimine les imitateurs.",
   tableau=(["Examen ou piège", "Apport", "Limite"], [
     ["IRM protocole épilepsie", "Sclérose hippocampique, tumeur, cavernome", "Coupes dédiées nécessaires"],
     ["EEG", "Pointes temporales", _T("Souvent normal", "Il se répète après privation de sommeil.")],
     ["Syncope convulsivante", "Prodromes, récupération rapide", "Pas d'antiépileptique"]]),
   points=["Première crise focale de l'adulte : IRM."], sources=["[Bernasconi, ILAE, 2019]"]),
  dict(titre="Traiter", rub=["acu", "chr"], comment="Choisit le médicament selon l'efficacité et le terrain.",
   arbre=[("t1", None, "Épilepsie focale", "Une crise suffit si le risque de récidive ≥ 60 %."),
          ("t2", "t1", "Premier choix", "Lamotrigine titrée lentement.", "ef"),
          ("t3", "t1", "Jeune femme", "Pas de valproate ; attention aux inducteurs.", "ef"),
          ("t4", "t2", "Deux échecs", "Centre d'épilepsie, bilan préchirurgical.", "ef"),
          ("t5", "t4", "Sclérose hippocampique", "Lobectomie temporale : 58 % contre 8 %.", "ef")],
   points=["SANAD II : lamotrigine supérieure au lévétiracétam."], sources=["[SANAD II, Lancet, 2021]", "[Wiebe, NEJM, 2001]"]),
  dict(titre="Suivre et vivre avec", rub=["hos", "pro", "sur", "fol"], comment="Suit les crises, l'humeur, la grossesse et la conduite.",
   tableau=(["Domaine", "Règle", "Pourquoi"], [
     ["Conduite (Suisse)", "1 an sans crise (privé)", _T("5 ans sans traitement (pro)", "Le risque professionnel est plus élevé.")],
     ["Grossesse", "Acide folique, dosage de lamotrigine", "Le taux baisse"],
     ["SUDEP", "Contrôler les crises nocturnes", "Le risque suit les crises tonico-cloniques"]]),
   points=["Dépister dépression et anxiété."], sources=["[Ligue suisse contre l'épilepsie, 2019]"]),
 ],
 ssp=dict(code="S7.10", nom="Secousses musculaires, fasciculations, convulsions, crise épileptique et état de mal épileptique", officiel=True, algorithme=[
  ("n1", None, "Épisode paroxystique", "Le témoignage décide d'abord : crise ou syncope."),
  ("n2", "n1", "Prodromes, récupération rapide", "Syncope : pas d'antiépileptique.", None, "c2"),
  ("n3", "n1", "Aura, automatismes, confusion", "Crise focale.", "ef", "c1"),
  ("n4", "n3", "IRM et EEG", "Lésion ou EEG épileptiforme : épilepsie.", "ef", "c2"),
  ("n5", "n4", "Traitement", "Lamotrigine en premier choix.", "ef", "c3"),
  ("n6", "n5", "Deux échecs", "Centre d'épilepsie, chirurgie.", "ef", "c3"),
  ("n7", "n5", "Vie quotidienne", "Conduite, grossesse, humeur.", "ef", "c4")]),
 pec=[
  dict(cle="ef", titre="Épilepsie focale",
   but=["Supprimer les crises avec le moins d'effets indésirables possible.", "Adresser tôt la pharmacorésistance à la chirurgie."],
   moyens=dict(accueil=["Recueillir le témoignage d'un tiers.", "Expliquer le diagnostic et les règles de sécurité.", "Remettre un agenda des crises."],
    pharma=[("Lamotrigine (antiépileptique)", "Titration lente sur plusieurs semaines ; à vérifier dans l'AIPS.", "Elle est le premier choix des crises focales.", "[SANAD II, Lancet, 2021]"),
            ("Lévétiracétam (antiépileptique)", "Dose titrée ; à vérifier dans l'AIPS.", "Il est une alternative, surveillée pour l'humeur.", "[SANAD II, Lancet, 2021]"),
            ("Midazolam buccal (benzodiazépine)", "Dose de secours selon l'AIPS.", "Il interrompt une crise prolongée à domicile.", "[avis d'expert]")],
    nonpharma=[("éducation thérapeutique", "Observance, sommeil régulier, alcool limité.", "Ils réduisent les crises."),
               ("geste ou chirurgie", "Lobectomie temporale après bilan préchirurgical.", "Elle guérit une majorité de patients pharmacorésistants."),
               ("social et assurances", "Information sur la conduite et l'activité professionnelle.", "Elle protège le patient et autrui.")],
    transversal=[("Gynécologie", "Elle planifie contraception et grossesse."), ("Psychiatrie", "Elle traite la dépression et l'anxiété associées.")]),
   urgence=None,
   horsUrgence=(["Agenda des crises.", "Évaluation précoce de la pharmacorésistance."],
            [("d'abord", "médecin de famille", "Recueille le témoignage et demande l'avis neurologique."),
             ("ensuite", "neurologue", "Demande IRM et EEG et débute la lamotrigine."),
             ("puis", "centre d'épilepsie", "Évalue la chirurgie après deux échecs."),
             ("en même temps", "patient·e", "Tient l'agenda et respecte l'interdiction de conduire.")]),
   pronostic="La majorité des patients deviennent libres de crises sous médicament ; la sclérose hippocampique résiste souvent mais répond bien à la chirurgie.",
   suivi=[("Nombre de crises", "À chaque consultation", "Zéro crise"), ("Humeur", "À chaque consultation", "Pas de dépression"), ("Taux de lamotrigine", "Pendant la grossesse", "Taux stable")],
   sortie="Le suivi reste ambulatoire neurologique.",
   prevention=["Elle maintient l'observance et le sommeil.", "Elle évite le valproate chez la jeune femme.", "Elle adresse tôt au centre d'épilepsie."]),
 ])
AVERIFIER = ["Titration et doses de lamotrigine, de lévétiracétam et de midazolam buccal à vérifier dans l'AIPS.", "Restrictions suisses exactes du valproate chez la femme en âge de procréer à vérifier dans l'AIPS."]
