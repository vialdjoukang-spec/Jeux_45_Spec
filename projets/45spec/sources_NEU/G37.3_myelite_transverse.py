ID = "G37.3_myelite_transverse_a__S4_15-E12"
PLAN = "monographique"
NOTIONS = [
"def|critère|3||[TMCWG, Neurology 2002]|La myélite transverse aiguë associe un déficit moteur, sensitif et autonome bilatéral d'origine médullaire, avec un niveau sensitif, qui atteint son maximum entre 4 heures et 21 jours.",  # N01
"red|piège|3||[TMCWG, Neurology 2002]|Le médecin exclut d'abord une compression médullaire par une IRM urgente, car elle relève de la chirurgie ou de la radiothérapie.",  # N02
"gold|examen|3||[TMCWG, Neurology 2002]|L'IRM médullaire et cérébrale avec gadolinium et la ponction lombaire prouvent l'inflammation par une prise de contraste, une pléiocytose ou un index IgG élevé.",  # N03
"pos|critère|2||[Wingerchuk, Neurology 2015]|Une lésion qui s'étend sur au moins 3 segments vertébraux contigus oriente vers une neuromyélite optique ou une maladie liée aux anticorps anti-MOG.",  # N04
"pos|diagnostic différentiel|2||[avis d'expert]|Une lésion courte et partielle, des lésions cérébrales périventriculaires et des bandes oligoclonales orientent vers une sclérose en plaques.",  # N05
"gold|examen|2||[Wingerchuk, Neurology 2015 ; avis d'expert]|Le bilan cherche les anticorps sériques anti-aquaporine 4 et anti-MOG par un test cellulaire.",  # N06
"acu|molécule|2||[avis d'expert]|Une méthylprednisolone intraveineuse à forte dose pendant 3 à 5 jours constitue le traitement de première ligne (posologie à vérifier dans l'AIPS).",  # N07
"acu|décision|2||[Weinshenker, Ann Neurol 1999]|Sans amélioration sous corticoïdes, les échanges plasmatiques s'imposent : dans un essai contrôlé, 42,1 % des cures actives ont amélioré le déficit contre 5,9 % des cures simulées.",  # N08
"ana|symptôme|1||[avis d'expert]|Le patient décrit une douleur dorsale en ceinture, des paresthésies ascendantes, une faiblesse des jambes et une rétention urinaire.",  # N09
"exa|signe|2||[avis d'expert]|En phase aiguë, un choc spinal rend les membres flasques et aréflexiques ; la spasticité et le signe de Babinski apparaissent ensuite.",  # N10
"hos|complication|2||[avis d'expert]|La rétention urinaire impose un sondage, l'immobilité une prophylaxie de la thrombose et des escarres, et une lésion haute une surveillance de la dysautonomie.",  # N11
"epi|terrain particulier|1||[avis d'expert]|Le VZV, l'HSV, les entérovirus, la syphilis, le VIH et la neuroborréliose, fréquente en Suisse, peuvent causer une myélite.",  # N12
"alt|examen|1||[avis d'expert]|Le LCR se teste par PCR (VZV, HSV, entérovirus) et par un index d'anticorps anti-Borrelia ; le sang par une sérologie de la syphilis et du VIH.",  # N13
"pos|diagnostic différentiel|1||[avis d'expert]|Un lupus, un syndrome de Sjögren, une sarcoïdose ou un syndrome des antiphospholipides peuvent causer une myélite secondaire.",  # N14
"pos|diagnostic différentiel|1||[avis d'expert]|Un infarctus médullaire s'installe en quelques minutes, épargne souvent la proprioception et montre une restriction de diffusion.",  # N15
"pos|diagnostic différentiel|1||[avis d'expert]|Une carence en vitamine B12 ou en cuivre, parfois révélée par le protoxyde d'azote, donne une myélopathie subaiguë des cordons postérieurs.",  # N16
"pos|diagnostic différentiel|1||[avis d'expert]|Une fistule durale artérioveineuse donne une paraparésie progressive aggravée par l'effort chez l'homme âgé, avec des vides de flux à l'IRM.",  # N17
"acu|décision|1||[avis d'expert]|Devant une suspicion de myélite à VZV ou HSV, l'aciclovir intraveineux se débute en attendant les PCR (posologie à vérifier dans l'AIPS).",  # N18
"pro|pronostic|1||[avis d'expert]|Classiquement, environ un tiers des patients récupère bien, un tiers garde un handicap modéré et un tiers un handicap sévère.",  # N19
"pro|critère|1||[avis d'expert]|Une installation très rapide, un choc spinal, une douleur dorsale intense et un déficit complet annoncent une récupération moins bonne.",  # N20
"chr|décision|1||[avis d'expert]|Une neuromyélite optique ou une sclérose en plaques confirmée justifie un traitement de fond pour prévenir les récidives.",  # N21
"chr|décision|1||[avis d'expert]|La rééducation, l'autosondage et le traitement de la spasticité, par exemple par baclofène, organisent la phase chronique.",  # N22
"fol|contexte suisse|1|S|[avis d'expert]|En Suisse, les centres de paraplégie spécialisés, comme ceux de Nottwil ou du Balgrist, assurent la réadaptation des atteintes médullaires sévères.",  # N23
"sur|examen|1||[avis d'expert]|Le suivi répète l'IRM et réévalue les anticorps, car une myélite peut inaugurer une sclérose en plaques ou une neuromyélite optique.",  # N24
"def|critère|1||[avis d'expert]|Une myélite partielle et asymétrique expose davantage à une sclérose en plaques qu'une myélite complète et symétrique.",  # N25
"red|signe|1||[avis d'expert]|Une myélite cervicale haute peut paralyser les muscles respiratoires et justifie une surveillance aux soins intensifs.",  # N26
"bas|mécanisme|1||[avis d'expert]|L'inflammation d'un segment médullaire interrompt à la fois les voies motrices descendantes, les voies sensitives ascendantes et les voies autonomes, d'où un déficit sous le niveau de la lésion.",  # N27
]
ANGLES = [
"IRM urgente pour exclure une compression.",
"Niveau sensitif, rétention, nadir 4 h - 21 jours.",
"Lésion ≥ 3 segments = AQP4 ou MOG.",
"Méthylprednisolone puis échanges plasmatiques.",
"Choc spinal flasque ≠ atteinte périphérique.",
"Infarctus médullaire : en minutes.",
]
L = lambda *a: list(a)
QUESTIONS = [
dict(format="A", serie=("S1", 1, 4), stem="Une femme de 34 ans consulte à Martigny pour une douleur dorsale en ceinture depuis 3 jours, des fourmillements qui montent des pieds, une faiblesse des jambes et une rétention urinaire. Vous trouvez un niveau sensitif en T8.", prompt="Quel examen demandez-vous en urgence ?",
 items=["*Une IRM médullaire, pour exclure d'abord une compression || Une compression relève d'un geste urgent.", "Un ENMG || Le niveau sensitif désigne la moelle.", "Une ponction lombaire avant toute imagerie || L'imagerie passe d'abord.", "Une radiographie du rachis seule || Elle ne voit pas la moelle.", "Un scanner cérébral || Le niveau est médullaire."],
 notions="N02 N01 N09", angle="application", diff=1, ladder=L("Paraparésie aiguë.", "Moelle.", "Niveau T8, rétention.", "Compression d'abord.", "IRM médullaire.", "ENMG.", "Niveau sensitif = IRM de la moelle."), sources="[TMCWG, Neurology 2002]"),
dict(format="A", serie=("S1", 2, 4), stem="L'IRM ne montre aucune compression, mais un hypersignal T2 central de T6 à T11, rehaussé par le gadolinium.", prompt="Quel bilan sanguin oriente le mieux la cause ?",
 items=["*Les anticorps anti-aquaporine 4 et anti-MOG || Une lésion de plus de 3 segments les évoque.", "Les CK || Elles cherchent une myopathie.", "Les anticorps anti-récepteur de l'acétylcholine || Ils cherchent une myasthénie.", "La TSH seule || Elle n'oriente pas ici.", "Les anticorps anti-GM1 || Ils cherchent une neuropathie."],
 notions="N04 N06 N03", angle="application", diff=2, ladder=L("Lésion étendue.", "Auto-immunité ciblée.", "Six segments.", "Plus de 3 segments.", "AQP4, MOG.", "CK.", "Longue = AQP4 ou MOG."), sources="[Wingerchuk, Neurology 2015]"),
dict(format="A", serie=("S1", 3, 4), stem="Le LCR montre une pléiocytose lymphocytaire modérée ; les PCR virales sont en cours.", prompt="Quel traitement débutez-vous ?",
 items=["*Une méthylprednisolone intraveineuse à forte dose || Elle constitue la première ligne.", "Une abstention jusqu'aux résultats des anticorps || Le délai aggrave le pronostic.", "Un interféron bêta || Il n'est pas un traitement de poussée.", "Une chirurgie de décompression || Il n'y a pas de compression.", "Des AINS seuls || Ils ne traitent pas l'inflammation médullaire."],
 notions="N07 N03 N18", angle="direct", diff=1, ladder=L("Inflammation médullaire.", "Œdème inflammatoire.", "Pléiocytose.", "Première ligne.", "Corticoïdes IV.", "Attendre.", "Myélite = corticoïdes IV."), sources="[avis d'expert]"),
dict(format="A", serie=("S1", 4, 4), stem="Au 5e jour, elle reste paraplégique malgré les corticoïdes.", prompt="Quelle étape suit ?",
 items=["*Des échanges plasmatiques || Ils améliorent une part des patients résistants aux corticoïdes.", "Doubler la durée des corticoïdes oraux seuls || L'escalade se fait autrement.", "Arrêter tout traitement || Une option efficace existe.", "Une radiothérapie médullaire || Rien ne l'indique.", "Une laminectomie || Il n'y a pas de compression."],
 notions="N08 N07 N04", angle="application", diff=2, ladder=L("Échec des corticoïdes.", "Anticorps circulants.", "Paraplégie persistante.", "Escalade.", "Échanges plasmatiques.", "Arrêter.", "Pas de réponse = plasma."), sources="[Weinshenker, Ann Neurol 1999]"),
dict(format="A", stem="Un homme de 28 ans présente depuis 4 jours des paresthésies de la main droite et du tronc. L'IRM montre une lésion médullaire latérale de C4 sur un seul segment et plusieurs lésions cérébrales périventriculaires ; le LCR contient des bandes oligoclonales.", prompt="Quelle maladie cette atteinte inaugure-t-elle probablement ?",
 items=["*Une sclérose en plaques || Lésion courte, partielle, lésions cérébrales et bandes oligoclonales l'orientent.", "Une neuromyélite optique || Elle donne des lésions longues.", "Un infarctus médullaire || L'installation n'est pas brutale.", "Une compression discale || Le profil est inflammatoire.", "Une carence en B12 || Elle touche les cordons postérieurs de façon symétrique."],
 notions="N05 N25 N24", angle="application", diff=2, ladder=L("Myélite partielle.", "Démyélinisation multifocale.", "Lésion courte, cerveau atteint.", "Bandes oligoclonales.", "SEP.", "Neuromyélite.", "Courte + cerveau = SEP."), sources="[avis d'expert]"),
dict(format="A", stem="Une femme de 66 ans, traitée pour un cancer du sein, développe en 2 jours une paraparésie avec un niveau sensitif en T10. Un interne veut lui donner tout de suite des corticoïdes pour une « myélite ».", prompt="Que corrigez-vous ?",
 items=["*Il faut d'abord une IRM médullaire urgente pour exclure une compression métastatique || La compression change toute la prise en charge.", "Rien, les corticoïdes suffisent || Le diagnostic n'est pas posé.", "Il faut une ponction lombaire immédiate || Elle passe après l'imagerie.", "Il faut attendre une semaine || Le délai menace la marche.", "Il faut un ENMG || La lésion est médullaire."],
 notions="N02 N01", angle="piège", diff=2, ladder=L("Paraparésie.", "Moelle.", "Cancer connu.", "Compression d'abord.", "IRM urgente.", "Corticoïdes à l'aveugle.", "Niveau + cancer = compression jusqu'à preuve du contraire."), sources="[TMCWG, Neurology 2002]"),
dict(format="A", stem="Un homme de 72 ans devient paraplégique en quelques minutes au réveil d'une chirurgie de l'aorte. Il sent la vibration et la position de ses orteils, mais pas la douleur.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Un infarctus médullaire dans le territoire spinal antérieur || L'installation en minutes et la proprioception épargnée l'orientent.", "Une myélite inflammatoire || Elle s'installe en heures ou en jours.", "Un syndrome de Guillain-Barré || Il ne donne pas de dissociation de ce type.", "Une compression discale || Le contexte est vasculaire.", "Une sclérose en plaques || Le début n'est pas aussi brutal."],
 notions="N15 N01", angle="piège", diff=2, ladder=L("Paraplégie brutale.", "Ischémie.", "Chirurgie aortique.", "Proprioception épargnée.", "Infarctus spinal antérieur.", "Myélite.", "Minutes = vasculaire."), sources="[avis d'expert]"),
dict(format="A", stem="Au 2e jour d'une atteinte médullaire inflammatoire, un patient a des jambes flasques et aréflexiques, un niveau sensitif en T6 et une rétention urinaire. Un interne évoque un syndrome de Guillain-Barré.", prompt="Que lui répondez-vous ?",
 items=["*L'aréflexie traduit un choc spinal ; le niveau sensitif et la rétention désignent la moelle || La spasticité viendra plus tard.", "Il a raison, l'aréflexie exclut la moelle || Le choc spinal l'explique.", "Il faut un ENMG avant toute IRM || L'IRM est prioritaire.", "Le diagnostic est une myopathie || Le niveau sensitif l'exclut.", "Il faut attendre la spasticité pour conclure || Le niveau suffit."],
 notions="N10 N09 N01", angle="piège", diff=2, ladder=L("Aréflexie.", "Choc spinal.", "Niveau T6.", "Topographie.", "Moelle.", "Guillain-Barré.", "Niveau sensitif = moelle, même aréflexique."), sources="[avis d'expert]"),
dict(format="A", stem="Une patiente hospitalisée pour une inflammation médullaire thoracique n'a pas uriné depuis 10 heures ; l'échographie montre 900 ml dans la vessie.", prompt="Quelles mesures prenez-vous ?",
 items=["*Un sondage vésical, une prophylaxie de la thrombose et une prévention des escarres || L'atteinte autonome et l'immobilité les imposent.", "Un diurétique || Il aggraverait la rétention.", "Une attente de 24 heures || La vessie se distend.", "Un AINS seul || Il ne traite pas la rétention.", "Une restriction hydrique || Elle n'est pas utile."],
 notions="N11 N26", angle="application", diff=1, ladder=L("Rétention.", "Atteinte autonome.", "900 ml.", "Complications.", "Sonde, thromboprophylaxie, escarres.", "Diurétique.", "Moelle = vessie, veines, peau."), sources="[avis d'expert]"),
dict(format="A", stem="Un forestier de 45 ans de l'Emmental développe une myélite thoracique ; il se souvient d'une tache rouge qui s'élargissait sur sa cuisse il y a 6 semaines.", prompt="Quel examen oriente le plus la cause ?",
 items=["*Un index d'anticorps anti-Borrelia dans le LCR || La neuroborréliose est fréquente en Suisse.", "Un test de Coombs || Il ne cherche pas cette cause.", "Une électrophorèse de l'hémoglobine || Elle n'est pas utile.", "Des anticorps anti-gangliosides || Ils cherchent une neuropathie.", "Un dosage de la ferritine || Il n'est pas utile."],
 notions="N12 N13", angle="application", diff=2, ladder=L("Myélite.", "Infection.", "Érythème migrant.", "Neuroborréliose.", "Index anti-Borrelia.", "Coombs.", "Tique + myélite = Borrelia."), sources="[avis d'expert]"),
dict(format="A", stem="Une étudiante de 22 ans développe en 3 semaines des paresthésies des pieds et une ataxie. Elle consomme régulièrement du protoxyde d'azote en soirée. L'IRM montre un hypersignal des cordons postérieurs cervicaux.", prompt="Quelle cause évoquez-vous ?",
 items=["*Une myélopathie par carence fonctionnelle en vitamine B12 || Le protoxyde d'azote inactive la B12.", "Une myélite transverse aiguë idiopathique || Le profil postérieur et le contexte orientent ailleurs.", "Une neuromyélite optique || Le contexte toxique l'explique.", "Une compression discale || L'IRM ne le montre pas.", "Un trouble fonctionnel || L'IRM est anormale."],
 notions="N16 N03", angle="piège", diff=2, ladder=L("Ataxie subaiguë.", "B12 inactivée.", "Protoxyde d'azote.", "Cordons postérieurs.", "Carence en B12.", "Myélite idiopathique.", "Gaz hilarant = B12."), sources="[avis d'expert]"),
dict(format="A", stem="Un homme de 68 ans voit sa paraparésie s'aggraver depuis 8 mois, surtout à la marche. L'IRM montre un œdème médullaire étendu et des vides de flux à la surface de la moelle.", prompt="Quel diagnostic retenez-vous ?",
 items=["*Une fistule durale artérioveineuse, à confirmer par angiographie médullaire || Les vides de flux et l'aggravation à l'effort l'orientent.", "Une myélite transverse aiguë || L'évolution sur 8 mois ne concorde pas.", "Un infarctus médullaire || Il est brutal.", "Une SLA || Elle ne donne pas d'œdème médullaire.", "Une carence en B12 || Elle ne donne pas de vides de flux."],
 notions="N17 N15", angle="application", diff=3, ladder=L("Paraparésie progressive.", "Hypertension veineuse.", "Effort, vides de flux.", "Œdème étendu.", "Fistule durale.", "Myélite.", "Vides de flux = fistule."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="Une myélite transverse longitudinalement étendue a révélé une neuromyélite optique à anticorps anti-aquaporine 4.", prompt="Quelle décision prenez-vous à distance ?",
 items=["*Débuter un traitement de fond pour prévenir les récidives || Chaque poussée laisse des séquelles.", "Ne rien faire, car la maladie est monophasique || Elle récidive.", "Prescrire un interféron bêta || Il est inadapté à cette maladie.", "Arrêter le suivi IRM || Le suivi reste nécessaire.", "Se contenter des corticoïdes à chaque poussée || La prévention compte."],
 notions="N21 N04 N24", angle="direct", diff=2, ladder=L("Neuromyélite.", "Récidives.", "AQP4 positif.", "Prévention.", "Traitement de fond.", "Monophasique.", "AQP4 = traiter au long cours."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="A", stem="La famille d'une patiente paraplégique après une myélite transverse sévère demande ce qui l'attend.", prompt="Quelle réponse est la plus juste ?",
 items=["*Environ un tiers récupère bien, un tiers modérément et un tiers peu ; une réadaptation en centre de paraplégie améliore l'autonomie || Une installation rapide et un choc spinal annoncent une récupération moins bonne.", "La récupération est toujours complète || Elle ne l'est pas.", "Aucune récupération n'est possible || Elle est fréquente.", "La réadaptation est inutile || Elle améliore l'autonomie.", "Le pronostic se juge à 48 heures || Il se juge sur des mois."],
 notions="N19 N20 N23 N22", angle="direct", diff=1, ladder=L("Pronostic.", "Remyélinisation.", "Paraplégie.", "Règle des tiers.", "Réadaptation.", "Récupération totale.", "Un tiers, un tiers, un tiers."), sources="[avis d'expert]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez les critères de la myélite transverse aiguë.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Le déficit est bilatéral avec un niveau sensitif. || Il désigne la moelle.", "V: Le maximum est atteint entre 4 heures et 21 jours. || Ce délai écarte l'infarctus et les formes chroniques.", "F: L'exclusion d'une compression n'est pas nécessaire. || Elle est obligatoire.", "F: Le LCR doit être normal. || Une pléiocytose soutient l'inflammation."],
 notions="N01 N02 N03 N27", angle="direct", diff=1, ladder=L("Critères.", "Inflammation médullaire.", "Niveau, délai.", "Pièges.", "Exclure, prouver.", "Compression ignorée.", "Bilatéral, niveau, 4 h à 21 jours."), sources="[TMCWG, Neurology 2002]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez l'orientation étiologique d'une myélite transverse.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une lésion d'au moins 3 segments contigus oriente vers une neuromyélite optique ou une maladie anti-MOG. || Elle est longitudinalement étendue.", "V: Les anticorps anti-AQP4 et anti-MOG se cherchent par un test cellulaire. || C'est la méthode de référence.", "F: Une lésion longue est typique de la sclérose en plaques. || La SEP donne des lésions courtes.", "F: Des anticorps anti-AQP4 négatifs excluent une neuromyélite optique. || Des formes séronégatives existent."],
 notions="N04 N06 N05", angle="direct", diff=2, ladder=L("Étiologie.", "Longueur de la lésion.", "AQP4, MOG.", "Pièges.", "Classer.", "Longue = SEP.", "Longue = AQP4 ou MOG, courte = SEP."), sources="[Wingerchuk, Neurology 2015]"),
dict(masque=False, sit="monographique", format="Kprim", stem="Vous révisez le traitement aigu de la myélite transverse.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: La méthylprednisolone IV à forte dose est la première ligne. || Pendant 3 à 5 jours.", "V: Les échanges plasmatiques se proposent en cas de réponse insuffisante. || 42,1 % contre 5,9 % dans un essai contrôlé.", "F: Les corticoïdes sont contre-indiqués dans la myélite. || Ils sont la première ligne.", "F: Les échanges plasmatiques ne se discutent qu'après 6 mois. || Ils se font rapidement."],
 notions="N07 N08 N18", angle="direct", diff=2, ladder=L("Traitement aigu.", "Immunomodulation.", "Corticoïdes, plasma.", "Pièges.", "Escalader vite.", "Contre-indication.", "Corticoïdes puis plasma."), sources="[Weinshenker, Ann Neurol 1999]"),
dict(format="Kprim", stem="Un patient a une atteinte médullaire inflammatoire aiguë cervicale.", prompt="Évaluez chacune des affirmations suivantes.",
 items=["V: Une rétention urinaire impose un sondage. || L'atteinte est autonome.", "V: Une lésion cervicale haute expose à une insuffisance respiratoire. || Elle justifie une surveillance intensive.", "F: Une aréflexie initiale prouve une atteinte périphérique. || Elle traduit un choc spinal.", "F: La prophylaxie de la thrombose est inutile. || L'immobilité l'impose."],
 notions="N11 N26 N10", angle="direct", diff=2, ladder=L("Complications.", "Moelle cervicale.", "Vessie, respiration.", "Pièges.", "Surveiller.", "Aréflexie périphérique.", "Vessie, souffle, veines."), sources="[avis d'expert]"),
dict(format="MenuLong", stem="Une IRM confirme une myélite sans compression.", prompt="Choisissez les TROIS examens qui orientent le plus la cause.",
 items=["*Anticorps anti-aquaporine 4 || Neuromyélite optique.", "*Anticorps anti-MOG || Maladie anti-MOG.", "*Ponction lombaire avec cellules, PCR et bandes oligoclonales || Inflammation et infection.", "Dosage des CK || Myopathie.", "ENMG || Neuropathie.", "Anticorps anti-récepteur de l'acétylcholine || Myasthénie.", "Biopsie musculaire || Myopathie.", "Échocardiographie || Pas utile en première intention.", "Dosage de la TSH seul || Peu utile.", "Spirométrie seule || Pas étiologique.", "Anticorps anti-GQ1b || Miller Fisher.", "Électroencéphalogramme || Pas utile."],
 notions="N06 N03 N13", angle="application", diff=2, ladder=L("Bilan étiologique.", "Auto-immunité, infection.", "AQP4, MOG, LCR.", "Tri.", "Trois examens.", "CK.", "Anticorps et LCR."), sources="[Wingerchuk, Neurology 2015]"),
dict(format="MenuLong", stem="Un patient de 30 ans présente une myélite aiguë.", prompt="Choisissez les TROIS éléments qui orientent vers une sclérose en plaques plutôt que vers une neuromyélite optique.",
 items=["*Lésion médullaire de moins de 3 segments || La SEP donne des lésions courtes.", "*Lésions cérébrales périventriculaires || Elles sont typiques de la SEP.", "*Bandes oligoclonales dans le LCR || Elles sont fréquentes dans la SEP.", "Lésion de 6 segments || Elle oriente vers une neuromyélite.", "Anticorps anti-AQP4 positifs || Neuromyélite.", "Névrite optique bilatérale sévère || Elle oriente plutôt vers une neuromyélite.", "Hoquet incoercible || Area postrema.", "Pléiocytose à neutrophiles marquée || Neuromyélite.", "Lésion centromédullaire étendue || Neuromyélite.", "Anticorps anti-MOG positifs || Maladie anti-MOG.", "Myélite complète symétrique || Moins typique de la SEP.", "Vomissements incoercibles || Area postrema."],
 notions="N05 N04 N25", angle="application", diff=3, ladder=L("SEP ou neuromyélite.", "Profil de démyélinisation.", "Lésion courte, cerveau, bandes.", "Discriminants.", "SEP.", "Lésion longue.", "Courte, cerveau, bandes = SEP."), sources="[Wingerchuk, Neurology 2015]"),
]
_T = lambda t, i: [(t, i)]
CORRECTION = dict(
 theme="Myélite transverse aiguë : exclure d'abord une compression, prouver l'inflammation, classer selon la longueur de la lésion et les anticorps AQP4 et MOG, traiter par corticoïdes puis échanges plasmatiques et prévenir les complications médullaires",
 notions=[
  dict(titre="Reconnaître et exclure la compression", rub=["def", "red", "ana", "exa"], comment="Pense moelle devant un niveau sensitif et une rétention ; image en urgence avant tout traitement.",
   tableau=(["Élément", "Contenu", "Pourquoi"], [
     ["Déficit", "Moteur, sensitif et autonome bilatéral", "Atteinte transverse de la moelle"],
     ["Niveau sensitif", "Horizontal", "Il localise la lésion"],
     ["Délai du maximum", _T("4 heures à 21 jours", "Plus court : infarctus ; plus long : cause chronique.")],
     ["Aréflexie initiale", "Choc spinal", "La spasticité vient ensuite"]]),
   points=["Une IRM urgente exclut d'abord une compression."], sources=["[TMCWG, Neurology 2002]"]),
  dict(titre="Prouver et classer", rub=["gold", "alt", "pos"], comment="Prouve l'inflammation, puis laisse la longueur de la lésion et les anticorps orienter la cause.",
   tableau=(["Profil", "Orientation", "Examen clé"], [
     ["Lésion ≥ 3 segments, centrale", "Neuromyélite optique ou anti-MOG", _T("AQP4, MOG", "Test cellulaire.")],
     ["Lésion courte, partielle, lésions cérébrales", "Sclérose en plaques", "Bandes oligoclonales"],
     ["Érythème migrant, tique", "Neuroborréliose", "Index anti-Borrelia"],
     ["Installation en minutes", "Infarctus médullaire", "Diffusion"]]),
   points=["Carence en B12 ou en cuivre et fistule durale imitent une myélite."], sources=["[Wingerchuk, Neurology 2015]", "[TMCWG, Neurology 2002]"]),
  dict(titre="Traiter la phase aiguë", rub=["acu", "hos"], comment="Débute vite les corticoïdes et escalade sans tarder ; protège vessie, veines, peau et respiration.",
   arbre=[("t1", None, "Myélite confirmée, compression exclue", "Méthylprednisolone IV forte dose 3 à 5 jours.", "mt"),
          ("t2", "t1", "Réponse insuffisante", "Échanges plasmatiques : 42,1 % contre 5,9 %.", "mt"),
          ("t3", None, "Suspicion de VZV ou HSV", "Aciclovir IV en attendant les PCR.", "mt"),
          ("t4", None, "Rétention, immobilité", "Sondage, thromboprophylaxie, prévention des escarres.", "mt"),
          ("t5", None, "Lésion cervicale haute", "Surveillance respiratoire intensive.", "mt")],
   points=["Les échanges plasmatiques reposent sur un essai contrôlé dans les poussées démyélinisantes résistantes aux corticoïdes."], sources=["[Weinshenker, Ann Neurol 1999]"]),
  dict(titre="Pronostic et suite", rub=["pro", "chr", "sur", "fol"], comment="Annonce la règle des tiers et prépare le traitement de fond si une maladie récidivante se confirme.",
   tableau=(["Situation", "Conduite", "Pourquoi"], [
     ["Neuromyélite ou SEP confirmée", "Traitement de fond", "Prévenir les récidives"],
     ["Déficit sévère", "Centre de paraplégie", _T("Réadaptation", "Nottwil, Balgrist.")],
     ["Vessie neurologique", "Autosondage", "Prévenir infections et reflux"],
     ["Myélite idiopathique", "IRM et anticorps de suivi", "Une SEP peut se révéler"]]),
   points=["Une installation rapide, un choc spinal et un déficit complet annoncent une récupération moins bonne."], sources=["[avis d'expert]"]),
 ],
 ssp=dict(code="S7.9", nom="Troubles de la sensibilité (hyperesthésie, hypoesthésie, paresthésies, hyperalgésie ou hypoalgésie)", officiel=True, algorithme=[
  ("n1", None, "Paresthésies ascendantes avec niveau sensitif", "Le médecin cherche faiblesse, rétention et douleur dorsale."),
  ("n2", "n1", "Niveau sensitif et rétention", "IRM médullaire urgente.", "mt", "c1"),
  ("n3", "n2", "Compression", "Neurochirurgie ou radiothérapie : renvoi au SSP compression médullaire.", None, "c1"),
  ("n4", "n2", "Hypersignal inflammatoire sans compression", "Myélite : LCR, AQP4, MOG, corticoïdes IV.", "mt", "c2"),
  ("n5", "n4", "Lésion ≥ 3 segments", "Neuromyélite ou anti-MOG.", "mt", "c2"),
  ("n6", "n1", "Installation en minutes", "Infarctus médullaire : IRM de diffusion.", None, "c2")]),
 pec=[
  dict(cle="mt", titre="Myélite transverse aiguë",
   but=["Exclure une compression et traiter l'inflammation vite.", "Prévenir les complications médullaires.", "Identifier une maladie récidivante."],
   moyens=dict(accueil=["Chercher un niveau sensitif et une rétention.", "Demander une IRM médullaire urgente.", "Surveiller la respiration si la lésion est cervicale."],
    pharma=[("Méthylprednisolone IV", "Forte dose pendant 3 à 5 jours ; à vérifier dans l'AIPS.", "Elle réduit l'inflammation médullaire.", "[avis d'expert]"),
            ("Échanges plasmatiques", "Cinq à sept séances selon le protocole local ; à vérifier.", "Ils retirent les anticorps pathogènes.", "[Weinshenker, Ann Neurol 1999]"),
            ("Aciclovir IV", "Si suspicion de VZV ou HSV ; à vérifier dans l'AIPS.", "Il traite une myélite virale.", "[avis d'expert]")],
    nonpharma=[("soins infirmiers", "Sondage, prévention des escarres, thromboprophylaxie.", "Ils préviennent les complications."),
               ("rééducation", "Physiothérapie et ergothérapie précoces.", "Elles soutiennent la récupération."),
               ("social et assurances", "Orientation vers un centre de paraplégie et démarches d'assurance.", "Elles organisent la suite.")],
    transversal=[("Neurologie", "Elle pose le diagnostic et dirige l'immunothérapie."), ("Neuroradiologie", "Elle exclut la compression et classe la lésion.")]),
   urgence=(["IRM médullaire urgente.", "Corticoïdes IV dès la compression exclue."],
            [("d'abord", "médecin urgentiste", "Repère le niveau sensitif et demande l'IRM."),
             ("en même temps", "infirmier·ère", "Mesure le résidu vésical et pose une sonde."),
             ("ensuite", "neurologue", "Fait la ponction lombaire et débute les corticoïdes."),
             ("puis", "médecin des soins intensifs", "Surveille la respiration si la lésion est haute.")]),
   horsUrgence=(["Traitement de fond si maladie récidivante.", "Réadaptation spécialisée."],
            [("d'abord", "neurologue", "Classe la cause et décide du traitement de fond."),
             ("ensuite", "centre de paraplégie", "Organise la réadaptation."),
             ("puis", "urologue", "Prend en charge la vessie neurologique.")]),
   pronostic="Classiquement, un tiers récupère bien, un tiers modérément et un tiers garde un handicap sévère.",
   suivi=[("Motricité et sensibilité", "Régulier", "Progression"), ("IRM et anticorps", "Selon la cause", "Pas de nouvelle lésion"), ("Vessie", "Régulier", "Pas d'infection ni de rétention")],
   sortie="Le patient sort vers la réadaptation quand il est stable et que la cause est classée.",
   prevention=["Elle repose sur le traitement de fond d'une maladie récidivante.", "Elle passe par la prévention des complications vésicales et cutanées.", "Elle impose de traiter une neuroborréliose identifiée."]),
 ])
AVERIFIER = ["Posologies de la méthylprednisolone et de l'aciclovir, et nombre de séances d'échanges plasmatiques, à vérifier dans l'AIPS et les protocoles locaux.", "La « règle des tiers » du pronostic est un repère classique, non vérifié ici sur une source primaire.", "Les critères du TMCWG (2002) sont rapportés d'après leur contenu connu ; seul le résumé a été consulté."]
