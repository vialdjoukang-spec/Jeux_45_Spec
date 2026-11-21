"""Onglet « Disciplines transversales » de la Tétrade (source unique).
Deux familles :
  1. OUTILS de la médecine (19 disciplines A → S, liste de la Cartographie Renouveau) : sous-onglets par lettre.
  2. LENTILLES (terrains et approches) : appliquées aux zones communes, elles n'affichent que ce qui est propre à la discipline."""
import json, os

ICI = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = json.load(open(os.path.join(ICI, "data", "references", "transversales_19_et_systemes.json"), encoding="utf-8"))

OUTILS = [{"lettre": t["letter"], "id": t["id"], "nom": t["name"], "icone": t["icon"], "couleur": t["color"],
           "sousOnglets": [s["name"] for s in t["subIcons"]], "lecons": len(t["lessons"])} for t in REF["transversales"]]
AXES = REF["axesLecons"]

# Lentilles cliniques : chacune filtre les zones communes (signes, examens, traitements) et révèle les particularités.
LENTILLES = [
 {"id": "PED", "nom": "Pédiatrie", "specialites": ["PED", "CPE", "PEA"], "filtre": "âge (nouveau-né, nourrisson, enfant, adolescent)",
  "revele": ["valeurs normales selon l'âge", "signes propres à l'enfant", "examens adaptés (échographie avant CT, sédation)", "posologies en mg/kg"]},
 {"id": "GER", "nom": "Gériatrie", "specialites": ["MIG"], "filtre": "âge avancé, fragilité, polymédication",
  "revele": ["présentations atypiques (confusion, chute)", "seuils et normes modifiés", "adaptation à la fonction rénale", "critères de Beers / PRISCUS", "objectifs de soins"]},
 {"id": "GYN", "nom": "Femme, grossesse et allaitement", "specialites": ["GYN"], "filtre": "sexe féminin, grossesse par trimestre, post-partum, allaitement",
  "revele": ["modifications physiologiques de la grossesse", "imagerie sans irradiation", "médicaments autorisés ou contre-indiqués", "urgences obstétricales"]},
 {"id": "CHI", "nom": "Chirurgie et périopératoire", "specialites": ["CHI", "ORT", "NCH", "CVA", "CTH", "CCT", "URO", "CPL", "CMA", "CMF", "ANE"], "filtre": "indication opératoire, risque anesthésique, suites",
  "revele": ["indications et contre-indications chirurgicales", "bilan préopératoire raisonné", "complications postopératoires", "relais des anticoagulants"]},
 {"id": "PSY", "nom": "Psychiatrie et psyché", "specialites": ["PSY", "PEA"], "filtre": "comorbidité psychique, capacité de discernement",
  "revele": ["manifestations psychiques d'une maladie somatique", "effets psychiques des traitements", "interactions des psychotropes", "communication adaptée"]},
 {"id": "URG", "nom": "Urgences et soins intensifs", "specialites": ["INT", "ANE"], "filtre": "instabilité vitale (ABCDE)",
  "revele": ["drapeaux rouges", "premiers gestes dans l'ordre", "examens au lit (POCUS, gazométrie)", "critères d'admission aux soins intensifs"]},
 {"id": "ONC", "nom": "Oncologie et radio-oncologie", "specialites": ["ONC", "RON", "HEM"], "filtre": "maladie tumorale, traitement oncologique",
  "revele": ["syndromes paranéoplasiques", "toxicités des traitements", "urgences oncologiques", "bilan d'extension"]},
 {"id": "IMG", "nom": "Imagerie et médecine nucléaire", "specialites": ["RAD", "NUC"], "filtre": "choix de la technique",
  "revele": ["examen de référence et facteur discriminant", "radio-anatomie normale", "irradiation et contre-indications", "recommandations smarter medicine"]},
 {"id": "PAT", "nom": "Pathologie et biologie", "specialites": ["PAT", "GEN"], "filtre": "preuve tissulaire ou moléculaire",
  "revele": ["preuve histologique attendue", "marqueurs immunohistochimiques et moléculaires", "conditions de prélèvement"]},
 {"id": "REA", "nom": "Réadaptation et handicap", "specialites": ["MPR"], "filtre": "fonction, autonomie, retour au travail",
  "revele": ["échelles fonctionnelles", "objectifs de rééducation", "aides et réseau suisse (Spitex, AI)"]},
 {"id": "VOY", "nom": "Voyage et médecine tropicale", "specialites": ["TRO", "INF"], "filtre": "séjour à l'étranger, migration",
  "revele": ["pathologies d'importation", "examens spécifiques (paludisme, sérologies)", "vaccinations et prophylaxies"]},
 {"id": "PHA", "nom": "Pharmacologie et toxicologie", "specialites": ["TOX", "PHA"], "filtre": "médicaments et toxiques",
  "revele": ["interactions (CYP450, QT)", "adaptation rénale et hépatique", "surdosages et antidotes"]},
]

# Modèle d'arborescence d'un cours de discipline transversale (de la coque vers le centre).
ARBORESCENCE = [
 ["1. Cadre", "Tu définis la discipline, son utilité pour le médecin et son cadre légal suisse."],
 ["2. Notions fondamentales", "Tu poses les concepts et les chiffres clés qui structurent la discipline."],
 ["3. Outils et méthodes", "Tu présentes les scores, échelles, tests et formulaires de la discipline."],
 ["4. Décisions et seuils", "Tu donnes les critères, les drapeaux rouges et les seuils qui font agir."],
 ["5. Applications par système", "Tu relies chaque outil aux systèmes de la Tétrade et aux SSP concernés."],
 ["6. Particularités par terrain", "Tu précises ce qui change chez l'enfant, la personne âgée, la femme enceinte."],
 ["7. Pièges et confusions", "Tu nommes les erreurs fréquentes et la manière de les éviter."],
 ["8. Pratique suisse", "Tu indiques le réseau, les numéros, les formulaires et les institutions suisses."],
 ["9. Exercices et répétition", "Tu proposes QCM A, K' et menus longs, et tu renvoies aux autres onglets où la notion revient."],
]
