"""PARTIE PRATIQUE des jeux : ce que le joueur FAIT avec chaque entité théorique.
La théorie remplit l'arbre (réseau Obsidian) ; la pratique remplit le jeu (arène, aventure, stations, cas).
Chaque fichier théorique a un jumeau pratique : conception/donnees/pratique/<même chemin>.json, une entrée par entité.
Source unique des gabarits de défis ; generer_json.py et taches.py la lisent (0 token)."""

# Modes de jeu par projet : où le défi est joué
MODES = {
    "1_Jeux_Tetrade_Fondation": ["Arène (défis chronométrés)", "Aventure par poste (puzzle clinique)", "Station OSCE (geste, communication)"],
    "2_Jeux_Paraclinique": ["Arène « le bon examen »", "Aventure par type d'examen", "Lecture d'image et de tracé"],
    "3_Transversal_Discip": ["Cas-décision", "QCM A et K'", "Simulation (annonce, consentement, triage)"],
    "4_Jeux_45_Spec": ["Items de la couche 3 (scripts/schema_item.json), déjà prévus"],
}

# Champs communs à tout défi
COMMUN = {"id": None, "type": None, "mode": None, "niveau": None, "points": None, "tempsSec": None,
          "correction": {"pourquoiJuste": None, "pourquoiFaux": None}, "sources": []}

# Gabarits de défis par genre d'entité : {genre: [(type, {champs propres}, quand)]}
# « quand » limite le défi à certaines modalités (None = toujours)
DEFIS = {
    "examen": [
        ("bon_examen", {"casClinique": None, "options": [], "bonneReponse": None, "visee": None}, None),
        ("seuil_decision", {"resultat": None, "decision": None}, ["Biologie", "Exploration fonctionnelle"]),
        ("lecture", {"consigne": None, "aspectRecherche": None, "reponse": None, "imageOuTraceAttendu": None}, ["Imagerie", "Exploration fonctionnelle", "Endoscopie", "Anatomopathologie / biopsie"]),
        ("piege", {"erreurFrequente": None, "consequence": None, "bonneConduite": None}, None),
    ],
    "analyse": [
        ("interpreter", {"contexte": None, "valeurAvecUnite": None, "question": None, "reponse": None}, None),
        ("preanalytique", {"situation": None, "piege": None, "bonneConduite": None}, None),
    ],
    "prelevement": [
        ("ordonner_le_geste", {"etapesMelangees": [], "ordreCorrect": []}, None),
        ("erreur_de_prelevement", {"situation": None, "consequence": None, "bonneConduite": None}, None),
    ],
    "exploration": [
        ("lire_le_trace", {"descriptionDuTrace": None, "question": None, "reponse": None}, None),
        ("indication", {"casClinique": None, "faireOuNon": None, "justification": None}, None),
    ],
    "organe": [
        ("reperage_3d", {"structure": None, "consigne": None, "vue": None}, None),
        ("relier", {"gauche": [], "droite": [], "paires": []}, None),
        ("calcul_ou_courbe", {"enonce": None, "donnees": None, "reponse": None, "fenetre": None}, None),
    ],
    "signe": [
        ("station_osce", {"consignePatient": None, "geste": None, "resultatNormal": None, "resultatPathologique": None}, None),
        ("ecoute_ou_observation", {"media": None, "question": None, "reponse": None}, None),
    ],
    "syndrome": [
        ("composer_le_syndrome", {"signesProposes": [], "minimumSuffisant": [], "intrus": []}, None),
        ("orienter", {"casClinique": None, "diagnosticsAEvoquer": [], "examenPrioritaire": None}, None),
    ],
    "mecanisme": [
        ("chaine_causale", {"etapesMelangees": [], "ordreCorrect": []}, None),
    ],
    "structure_pharmaco": [
        ("prescrire", {"casClinique": None, "options": [], "bonneReponse": None, "contreIndication": None, "posologieEtSource": None}, None),
        ("interaction_ou_effet", {"situation": None, "question": None, "reponse": None}, None),
    ],
    "classe": [
        ("chef_de_file", {"profil": None, "options": [], "bonneReponse": None}, None),
    ],
    "lecon": [
        ("cas_decision", {"casSuisse": None, "options": [], "bonneReponse": None}, None),
        ("simulation", {"situation": None, "repliqueAttendue": None, "erreursAEviter": []}, None),
    ],
}

# Genre d'entité selon le chemin du fichier théorique
def genre(chemin):
    c = chemin.replace("\\", "/")
    for motif, g in [("/topographie/", "examen"), ("/biologie/analyses/", "analyse"), ("/biologie/prelevements/", "prelevement"),
                     ("/explorations/", "exploration"), ("/organes/", "organe"), ("semiologie.json", "signe"), ("syndromes.json", "syndrome"),
                     ("criteres_cim10.json", "syndrome"), ("physiopathologie.json", "mecanisme"), ("structures.json", "structure_pharmaco"),
                     ("classes.json", "classe"), ("/transversales/lecons/", "lecon")]:
        if motif in c:
            return g
    return None


def defis_pour(g, modalite=None):
    out = []
    for i, (t, champs, quand) in enumerate(DEFIS.get(g, [])):
        if quand and modalite not in quand:
            continue
        out.append({**COMMUN, "id": None, "type": t, **champs})
    return out


REGLES = [
    "Un défi se joue en moins de 90 secondes et se corrige en deux phrases : pourquoi la bonne réponse est juste, pourquoi chaque distracteur est faux.",
    "Le défi s'appuie sur le fichier théorique jumeau rempli : il n'invente rien qui le contredise.",
    "Les cas cliniques sont suisses (âge, contexte, système de soins) ; les valeurs sont en unités SI.",
    "niveau : 1 = reconnaître, 2 = décider, 3 = piège d'expert ; points : 10, 20 ou 30 selon le niveau ; tempsSec : 30 à 90.",
    "mode : un des modes du projet (voir _meta.modes).",
    "Les options d'un QCM sont plausibles, de longueur comparable, et une seule est juste.",
]
