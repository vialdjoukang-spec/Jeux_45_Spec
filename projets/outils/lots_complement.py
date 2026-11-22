"""Prépare les lots de complément pour l'IA de production (0 token) : un lot par région, qui ne demande
que les champs de présentation manquants des examens déjà fiables (synonymes, aspectNormal,
anomaliesElementaires, syndromesParacliniques, pathologiesAssociees). Le retour se fusionne par champ
avec projets/outils/fusionner_retours.py, sans toucher au cœur clinique audité.
Usage : python projets/outils/lots_complement.py
Signature : AAI (Anthropic AI)"""
import json, glob, os

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SORTIE = os.path.join(RAC, "Production_XAi", "Lots_a_produire", "complement_presentation")
CHAMPS = ["synonymes", "aspectNormal", "anomaliesElementaires", "syndromesParacliniques", "pathologiesAssociees"]
VIDES = (None, "", [], {})
EXEMPLE = "conception/donnees/paraclinique/topographie/8_peau_et_phaneres/peau.json › peau__dermatoscopie"

os.makedirs(SORTIE, exist_ok=True)
total = 0
for dreg in sorted(glob.glob(os.path.join(RAC, "SORTIES_DONNEES_FIABLES", "paraclinique", "*"))):
    fichiers = {}
    for f in sorted(glob.glob(os.path.join(dreg, "*.json"))):
        fiable = json.load(open(f, encoding="utf-8"))
        a_completer = set(fiable["_meta"].get("aCompleter", []))
        if not a_completer:
            continue
        src = fiable["_meta"]["source"]
        exams = [{"id": e["id"], "nom": e["nom"], "modalite": e["modalite"], **{k: ([] if k != "aspectNormal" else None) for k in CHAMPS if e.get(k) in VIDES}}
                 for e in fiable["examens"] if e["id"] in a_completer]
        if exams:
            fichiers[src] = {"_meta": {"organe": fiable["_meta"]["organe"], "regles": [
                "Remplis seulement les champs vides présents ; le reste de l'examen est déjà audité et ne doit pas changer.",
                "Prends le format exact de l'exemple : " + EXEMPLE + "."]}, "examens": exams}
            total += len(exams)
    if fichiers:
        reg = os.path.basename(dreg)
        lot = {"_lot": {"tache": "COMPLEMENT-" + reg[:2], "titre": f"Compléter la présentation des examens fiables ({reg[2:].replace('_', ' ')})",
                        "projet": "2_Jeux_Paraclinique", "nombreFichiers": len(fichiers),
                        "consigne": "Remplis uniquement les cinq champs de présentation demandés, avec des phrases verbales et une source nommée ; garde les chemins, les id et les clés ; rends le même objet.",
                        "aVerifier": []}, "fichiers": fichiers}
        json.dump(lot, open(os.path.join(SORTIE, f"LOT_COMPLEMENT_{reg}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"{total} examens à compléter, lots dans {os.path.relpath(SORTIE, RAC)}")
