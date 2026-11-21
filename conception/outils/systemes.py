"""Source unique : SYSTÈME → ORGANES (de haut en bas) → tétrade.
Chaque organe se déplie selon l'espace actif :
  Anatomie        : macroscopie, microscopie, vascularisation, innervation (+ rapports et projections, embryologie et variantes)
  Physiologie     : paramètres du plus simple au plus complexe ; chaque mot-clé ouvre une fenêtre (courbe, tracé, calculateur)
  Sémiologie      : temps d'examen et anamnèse → signes typiques et atypiques → syndromes
  Physiopathologie: fonction perturbée → mécanisme → signe
« topo » relie l'organe au catalogue des examens (catalogue_paraclinique.TOPO)."""

VOLETS_ANATOMIE = ["Macroscopie", "Microscopie", "Vascularisation", "Innervation", "Rapports et projections", "Embryologie et variantes"]
VOLETS_PHYSIOLOGIE = ["Paramètres simples", "Régulation", "Lois physiques et biochimie", "Intégration avec les autres organes", "Valeurs normales (unités SI)"]

# organe : (nom, ancre 3D BodyParts3D, clés topo)
SYSTEMES = {
 "Cardiovasculaire": [
  # validé par Vial le 2026-11-21 : ordre haut → bas, péricarde avant le cœur, cœur scindé en 4, circulation pulmonaire fusionnée,
  # système porte rattaché au digestif (« Vascularisation digestive et système porte »). Contenu : cardio/contenu.txt et cardio/pathologies.txt.
  ("Troncs supra-aortiques (carotides, vertébrales, sous-clavières)", "aorte", ["Vaisseaux du cou et de la tête"]), ("Aorte thoracique et crosse", "aorte", ["Aorte thoracique et artères pulmonaires"]),
  ("Péricarde", "coeur", ["Cœur et péricarde"]), ("Cœur : myocarde et cavités", "coeur", ["Cœur et péricarde"]), ("Cœur : valves", "coeur", ["Cœur et péricarde"]),
  ("Cœur : tissu de conduction", "coeur", ["Cœur et péricarde"]), ("Cœur : circulation coronaire", "coeur", ["Cœur et péricarde"]),
  ("Circulation pulmonaire (artères et veines)", "coeur", ["Aorte thoracique et artères pulmonaires"]), ("Veines caves", "coeur", ["Veines caves et système porte"]),
  ("Aorte abdominale et artères viscérales", "aorte", ["Aorte abdominale et vaisseaux digestifs"]), ("Artères des membres", "femur", ["Artères des membres"]), ("Veines des membres", "femur", ["Veines des membres"]),
  ("Microcirculation (artérioles, capillaires, veinules, endothélium)", None, ["Artères des membres"]), ("Système lymphatique", None, ["Système lymphatique"])],
 "Respiratoire": [
  ("Fosses nasales et sinus", "crane", ["Nez, sinus et cavum"]), ("Pharynx", "crane", ["Larynx et pharynx"]), ("Larynx", "trachee", ["Larynx et pharynx"]),
  ("Trachée", "trachee", ["Poumons et voies aériennes"]), ("Bronches et bronchioles", "poumon_d", ["Poumons et voies aériennes"]),
  ("Poumons (lobes, segments, acinus)", "poumon_d", ["Poumons et voies aériennes"]), ("Circulation pulmonaire", "poumon_d", ["Aorte thoracique et artères pulmonaires"]),
  ("Plèvre", "poumon_d", ["Plèvre"]), ("Diaphragme et muscles respiratoires", "diaphragme", ["Poumons et voies aériennes", "Diaphragme et muscles respiratoires"]),
  ("Paroi thoracique", "cage", ["Paroi thoracique et côtes"]), ("Centres respiratoires et chémorécepteurs", "cerveau", ["Encéphale"])],
 "Neurologique": [
  ("Méninges et LCR", "cerveau", ["Méninges et LCR"]), ("Hémisphères cérébraux (lobes, cortex)", "cerveau", ["Encéphale"]), ("Noyaux gris centraux et thalamus", "cerveau", ["Encéphale"]),
  ("Système limbique et hypothalamus", "cerveau", ["Encéphale", "Hypophyse et hypothalamus"]), ("Tronc cérébral", "cerveau", ["Encéphale"]), ("Cervelet", "cerveau", ["Encéphale"]),
  ("Nerfs crâniens (I à XII)", "cerveau", ["Encéphale", "Nerfs crâniens"]), ("Vascularisation cérébrale (polygone de Willis, sinus veineux)", "cerveau", ["Vaisseaux du cou et de la tête", "Encéphale"]),
  ("Moelle épinière", "rachis", ["Moelle épinière"]), ("Racines et plexus", "rachis", ["Racines et plexus", "Queue de cheval et cône terminal"]), ("Nerfs périphériques", "femur", ["Nerfs périphériques"]),
  ("Jonction neuromusculaire", None, ["Muscles"]), ("Système nerveux autonome", "rachis", ["Nerfs périphériques"])],
 "Psyché (psychiatrie)": [
  ("Fonctions cognitives (attention, mémoire, fonctions exécutives)", "cerveau", ["Psyché"]), ("Perception et pensée", "cerveau", ["Psyché"]),
  ("Affects et humeur", "cerveau", ["Psyché"]), ("Pulsions, motivation et comportement", "cerveau", ["Psyché"]), ("Conscience de soi et personnalité", "cerveau", ["Psyché"]),
  ("Sommeil et vigilance", "cerveau", ["Sommeil et vigilance"]), ("Circuits de la récompense et addictions", "cerveau", ["Toxicologie et médicaments"])],
 "Endocrinien & métabolique": [
  ("Hypothalamus et hypophyse", "cerveau", ["Hypophyse et hypothalamus"]), ("Épiphyse", "cerveau", ["Encéphale"]), ("Thyroïde", "trachee", ["Thyroïde"]),
  ("Parathyroïdes", "trachee", ["Parathyroïdes"]), ("Thymus", "coeur", ["Médiastin"]), ("Pancréas endocrine", "pancreas", ["Pancréas"]),
  ("Surrénales", "reins", ["Surrénales"]), ("Gonades (ovaires, testicules)", "bassin", ["Utérus, col, ovaires et annexes", "Testicules et scrotum"]),
  ("Tissu adipeux et métabolisme énergétique", None, ["Métabolisme et endocrinologie"]), ("Métabolisme phosphocalcique et osseux", "femur", ["Os longs et squelette"])],
 "Digestif & hépatobiliaire": [
  ("Cavité buccale et glandes salivaires", "crane", ["Cavité buccale et glandes salivaires", "Articulation temporo-mandibulaire et dents"]), ("Pharynx", "crane", ["Larynx et pharynx"]), ("Œsophage", "oesophage", ["Œsophage"]),
  ("Estomac", "estomac", ["Estomac et duodénum"]), ("Duodénum", "estomac", ["Estomac et duodénum"]), ("Foie", "foie", ["Foie"]), ("Vésicule et voies biliaires", "foie", ["Vésicule et voies biliaires"]),
  ("Pancréas exocrine", "pancreas", ["Pancréas"]), ("Jéjunum et iléon", "grele", ["Intestin grêle"]), ("Côlon", "colon", ["Côlon, rectum et anus", "Appendice"]),
  ("Rectum et canal anal", "colon", ["Côlon, rectum et anus"]), ("Péritoine", "grele", ["Péritoine et ascite", "Paroi abdominale et hernies"]), ("Vascularisation digestive et système porte", "foie", ["Aorte abdominale et vaisseaux digestifs", "Veines caves et système porte"])],
 "Rénal & uro-génital": [
  ("Reins (néphron, glomérule, tubule)", "reins", ["Reins"]), ("Uretères", "reins", ["Uretères", "Rétropéritoine"]), ("Vessie", "vessie", ["Vessie et urètre"]), ("Urètre", "vessie", ["Vessie et urètre", "Pénis et urètre masculin"]),
  ("Prostate et vésicules séminales", "vessie", ["Prostate et vésicules séminales"]), ("Testicules, épididymes et voies spermatiques", "bassin", ["Testicules et scrotum", "Pénis et urètre masculin"])],
 "Hématologique & oncologique": [
  ("Moelle osseuse (hématopoïèse)", "bassin", ["Moelle osseuse et ganglions"]), ("Sang : globules rouges", None, ["Sang et hémostase"]), ("Sang : globules blancs", None, ["Sang et hémostase"]),
  ("Plaquettes et hémostase", None, ["Sang et hémostase"]), ("Rate", "rate", ["Rate"]), ("Ganglions lymphatiques", None, ["Moelle osseuse et ganglions", "Ganglions cervicaux", "Corps entier (bilan d'extension et trauma)", "Masses cervicales et kystes"]), ("Thymus", "coeur", ["Médiastin"])],
 "Infectieux & immunitaire": [
  ("Barrières (peau, muqueuses, microbiote)", None, ["Peau", "Infection et immunité"]), ("Immunité innée", None, ["Infection et immunité"]), ("Immunité adaptative (lymphocytes B et T)", None, ["Infection et immunité"]),
  ("Complément", None, ["Infection et immunité"]), ("Organes lymphoïdes (moelle, thymus, rate, ganglions, MALT)", "rate", ["Moelle osseuse et ganglions", "Rate"])],
 "Locomoteur & rhumatologique": [
  ("Crâne et face", "crane", ["Os du crâne et de la face", "Articulation temporo-mandibulaire et dents"]), ("Rachis", "rachis", ["Rachis osseux"]), ("Ceinture scapulaire et épaule", "humerus", ["Épaule"]), ("Coude, poignet et main", "humerus", ["Coude, poignet et main"]),
  ("Bassin et hanche", "bassin", ["Hanche et bassin"]), ("Genou", "femur", ["Genou"]), ("Cheville et pied", "femur", ["Cheville et pied"]), ("Os (tissu osseux)", "femur", ["Os longs et squelette"]),
  ("Articulations et synoviale", "femur", ["Articulations et synoviale"]), ("Muscles striés squelettiques", "femur", ["Muscles"]), ("Tendons, ligaments et bourses", "femur", ["Articulations et synoviale", "Tendons et ligaments"])],
 "Dermatologique": [("Épiderme", None, ["Peau"]), ("Derme et hypoderme", None, ["Peau", "Plaies, ulcères et escarres"]), ("Annexes : poils et cheveux", None, ["Ongles et cheveux"]), ("Annexes : ongles", None, ["Ongles et cheveux"]), ("Glandes sudorales et sébacées", None, ["Peau"]), ("Muqueuses", None, ["Peau"])],
 "Ophtalmologique & ORL": [
  ("Paupières et voies lacrymales", "crane", ["Œil et orbite"]), ("Globe oculaire (cornée, cristallin, rétine)", "crane", ["Œil et orbite"]), ("Voies optiques", "cerveau", ["Œil et orbite", "Encéphale"]),
  ("Oreille externe et moyenne", "crane", ["Oreille et équilibre"]), ("Oreille interne (cochlée, vestibule)", "crane", ["Oreille et équilibre"]), ("Nez et sinus", "crane", ["Nez, sinus et cavum"]),
  ("Cavité buccale et pharynx", "crane", ["Cavité buccale et glandes salivaires", "Larynx et pharynx", "Masses cervicales et kystes"]), ("Larynx", "trachee", ["Larynx et pharynx"]), ("Glandes salivaires", "crane", ["Cavité buccale et glandes salivaires"])],
 "Gynéco-obstétrical": [
  ("Seins", "coeur", ["Seins", "Post-partum et allaitement"]), ("Ovaires", "bassin", ["Utérus, col, ovaires et annexes"]), ("Trompes", "bassin", ["Utérus, col, ovaires et annexes"]), ("Utérus et col", "bassin", ["Utérus, col, ovaires et annexes"]),
  ("Vagin et vulve", "bassin", ["Utérus, col, ovaires et annexes", "Vulve, vagin et périnée"]), ("Plancher pelvien", "bassin", ["Plancher pelvien"]), ("Placenta et unité fœto-placentaire", "bassin", ["Grossesse, fœtus et placenta", "Post-partum et allaitement"])],
 "Pédiatrique (croissance et développement)": [
  ("Croissance staturo-pondérale", None, ["Os longs et squelette", "Croissance et développement de l'enfant"]), ("Développement psychomoteur", "cerveau", ["Encéphale", "Croissance et développement de l'enfant"]), ("Puberté", "bassin", ["Métabolisme et endocrinologie", "Croissance et développement de l'enfant"]),
  ("Adaptation néonatale (vie extra-utérine)", "coeur", ["Grossesse, fœtus et placenta", "Cœur et péricarde"]), ("Génétique et dysmorphies", None, ["Génétique"])],
}

# L'anatomie, la physiologie et les pathologies du cardiovasculaire vivent dans cardio/ (lues par cardio.py).

# ---------- pilote 2 : physiologie du poumon (mots-clés → courbes et calculateurs) ----------
PHYSIOLOGIE_POUMON = {
 "Paramètres simples": [["Fréquence respiratoire", "12 à 20 cycles par minute chez l'adulte au repos.", None], ["Volume courant", "Environ 500 ml (6–8 ml/kg de poids idéal).", None],
                        ["Volumes et capacités", "CPT, CV, VR, CRF : la spirométrie et la pléthysmographie les mesurent.", "spiro"]],
 "Régulation": [["Chémorécepteurs centraux", "Ils répondent surtout à la PaCO₂ via le pH du LCR.", None], ["Chémorécepteurs périphériques", "Les corps carotidiens répondent à une PaO₂ < 8 kPa.", None]],
 "Lois physiques et biochimie": [["Équation des gaz alvéolaires", "PAO₂ = FiO₂ × (Patm − PH₂O) − PaCO₂ / QR : elle donne l'O₂ alvéolaire et le gradient A-a.", "alveolaire"],
                                 ["Courbe de dissociation de l'hémoglobine", "La saturation suit une sigmoïde ; la P50 normale vaut environ 3,5 kPa.", "odc"],
                                 ["Effet Bohr et effet Haldane", "L'acidose, la PaCO₂, la chaleur et le 2,3-DPG déplacent la courbe à droite ; l'oxygénation libère le CO₂.", "odc"],
                                 ["Henderson-Hasselbalch", "pH = 6,1 + log(HCO₃⁻ / (0,23 × PaCO₂ en kPa)).", "hh"],
                                 ["Loi de Fick (diffusion)", "Le débit de gaz augmente avec la surface et le gradient, et baisse avec l'épaisseur de la membrane.", None],
                                 ["Rapport ventilation / perfusion", "V/Q ≈ 0,8 en moyenne ; l'effet shunt et l'espace mort l'écartent.", None]],
 "Intégration avec les autres organes": [["Poumon et rein : équilibre acide-base", "Le poumon règle la PaCO₂ en minutes, le rein règle les bicarbonates en jours.", "hh"],
                                         ["Lecture des gaz du sang", "Tu relies pH, PaCO₂, HCO₃⁻, gradient A-a et compensation attendue (Winter).", "gazometrie"]],
 "Valeurs normales (unités SI)": [["Gaz du sang artériel", "pH 7,35–7,45 ; PaCO₂ 4,7–6,0 kPa ; PaO₂ 10–13 kPa ; HCO₃⁻ 22–26 mmol/l.", "gazometrie"]],
}


# Glossaire des sigles employés par les volets (l'apprenant ne quitte jamais l'application)
GLOSSAIRE = {
 "AV": "Atrioventriculaire : qui relie oreillette et ventricule (nœud AV, valves AV).",
 "CO₂": "Dioxyde de carbone : il est produit par les cellules et éliminé par la ventilation ; il règle le pH via l'acide carbonique.",
 "CPT": "Capacité pulmonaire totale : volume d'air contenu dans les poumons après une inspiration maximale (≈ 6 l chez l'adulte).",
 "CRF": "Capacité résiduelle fonctionnelle : volume qui reste dans les poumons en fin d'expiration calme (≈ 2,5 l).",
 "CV": "Capacité vitale : volume maximal expiré après une inspiration maximale.",
 "CVF": "Capacité vitale forcée : capacité vitale mesurée lors d'une expiration forcée ; elle baisse dans le syndrome restrictif.",
 "DLCO": "Capacité de diffusion du monoxyde de carbone : elle mesure le passage alvéolo-capillaire ; elle baisse dans la fibrose et l'emphysème.",
 "EIC": "Espace intercostal : intervalle entre deux côtes, repère de l'auscultation et de la ponction.",
 "FiO₂": "Fraction inspirée en oxygène : 0,21 à l'air ambiant ; elle monte sous oxygénothérapie.",
 "IVA": "Artère interventriculaire antérieure : branche de la coronaire gauche qui irrigue la paroi antérieure et le septum.",
 "LCR": "Liquide cérébrospinal : il baigne l'encéphale et la moelle ; on le prélève par ponction lombaire.",
 "MALT": "Tissu lymphoïde associé aux muqueuses : défense immunitaire locale des voies aériennes et digestives.",
 "ORL": "Oto-rhino-laryngologie : spécialité de l'oreille, du nez et de la gorge.",
 "PAO₂": "Pression alvéolaire en oxygène : PAO₂ = FiO₂ × (Patm − PH₂O) − PaCO₂ / 0,8 ; elle vaut ≈ 13,3 kPa au niveau de la mer.",
 "PH₂O": "Pression de vapeur d'eau à 37 °C : 6,3 kPa (47 mmHg), à soustraire de la pression atmosphérique.",
 "PaCO₂": "Pression artérielle en CO₂ : norme 4,7–6,0 kPa ; elle reflète directement la ventilation alvéolaire.",
 "PaO₂": "Pression artérielle en oxygène : norme 10,7–13,3 kPa chez l'adulte jeune ; elle baisse avec l'âge et l'altitude.",
 "QR": "Quotient respiratoire : rapport CO₂ produit / O₂ consommé, ≈ 0,8 avec une alimentation mixte.",
 "SI": "Système international d'unités : en Suisse, les gaz du sang s'expriment en kPa (1 kPa = 7,5 mmHg).",
 "VEMS": "Volume expiré maximal en une seconde : il baisse dans l'obstruction ; le rapport VEMS/CVF < 0,7 signe un trouble obstructif.",
 "VR": "Volume résiduel : air qui reste dans les poumons après une expiration maximale ; il augmente dans la distension.",
}
