#!/usr/bin/env python3
"""Génère, sans aucun appel de modèle, le manifeste des lots d'audit de chaque jeu.
Un lot = un petit ensemble de fichiers sources que Gemini relit en une passe.
Relance : python Gemini_cross-check-hard/outils/preparer_lots.py  (depuis la racine du dépôt).
Le manifeste porte l'empreinte sha256 de chaque fichier : un lot dont l'empreinte n'a pas changé depuis son rapport n'est pas réaudité."""
import glob, hashlib, json, os, datetime

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(R)
G = "Gemini_cross-check-hard"


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]


def lot(ident, titre, fichiers, focus):
    fichiers = [f for f in fichiers if os.path.isfile(f)]
    return {"lot": ident, "titre": titre, "fichiers": [{"chemin": f, "sha256": sha(f), "octets": os.path.getsize(f)} for f in fichiers],
            "focus": focus, "rapport": None} if fichiers else None


def ecrire(jeu, lots):
    lots = [l for l in lots if l]
    d = f"{G}/{jeu}"
    os.makedirs(f"{d}/rapports", exist_ok=True)
    m = {"jeu": jeu, "genere_le": datetime.date.today().isoformat(), "nb_lots": len(lots), "lots": lots}
    for l in lots:
        l["rapport"] = f"{d}/rapports/{l['lot']}.json"
    json.dump(m, open(f"{d}/MANIFESTE_LOTS.json", "w"), ensure_ascii=False, indent=1)
    print(f"{jeu}: {len(lots)} lots")


# 1. Tétrade : un lot par système (texte source rédigé à la main)
T = []
for s in sorted({p.split("/")[2] for p in glob.glob("conception/outils/*/pathologies.txt")}):
    b = f"conception/outils/{s}"
    T.append(lot(f"T_{s}", f"Tétrade — système {s}", [f"{b}/pathologies.txt", f"{b}/semiologie.txt", f"{b}/contenu.txt", f"{b}/glossaire.txt"],
                 "posologies (AIPS), seuils, critères, classes de recommandation, sources datées, épidémiologie suisse"))
ecrire("1_Tetrade", T)

# 2. Paraclinique
P = "conception/donnees/paraclinique"
I = []
for f in sorted(glob.glob(f"{P}/niveaux/*.json")):
    st = os.path.basename(f)[:-5]
    topo = glob.glob(f"{P}/topographie/*/{st}.json")
    I.append(lot(f"IMG_{st}", f"Imagerie — {st}", [f, f"{P}/fiches_flash/{st}.json", f"{P}/syndromes_radio/{st}.json", f"{P}/atlas_liens/{st}.json"] + topo,
                 "niveau d'indication, 1re intention, gold standard, syndrome radiologique, angle mort, doses d'irradiation, directives OFSP de radioprotection"))
ecrire("2_Paraclinique/Imagerie", I)
B = [lot("BIO_criteres_calculs", "Biologie — critères et calculs", [f"{P}/criteres.json", f"{P}/calculs.json", f"{P}/smarter_medicine.json"],
         "formules, seuils décisionnels, unités SI, Smarter Medicine")]
for f in sorted(glob.glob(f"{P}/biologie/**/*.json", recursive=True)):
    rel = os.path.relpath(f, f"{P}/biologie").replace("/", "_")[:-5]
    B.append(lot(f"BIO_{rel}", f"Biologie — {rel}", [f], "valeurs de référence suisses (unités SI), tubes, seuils d'alerte, Liste des analyses OFSP, causes"))
ecrire("2_Paraclinique/Biologie", B)
E = [lot(f"EXP_{os.path.basename(f)[:-5]}", f"Explorations — {os.path.basename(f)[:-5]}", [f], "indications, valeurs normales, seuils, contre-indications")
     for f in sorted(glob.glob(f"{P}/explorations/**/*.json", recursive=True))]
E.append(lot("EXP_techniques_visees", "Explorations — techniques et visées", [f"{P}/techniques_discriminants.json", f"{P}/visees_bilan.json"], "discriminants, visées du bilan"))
ecrire("2_Paraclinique/Explorations", E)

# 3. Transversal
ecrire("3_Transversal", [lot(f"TR_{os.path.basename(f)[:-5]}", f"Transversal — {os.path.basename(f)[:-5]}", [f],
                             "droit suisse de la santé, assurances sociales, santé publique OFSP, éthique, numéros suisses")
                         for f in sorted(glob.glob("conception/donnees/tetrade/transversales/**/*.json", recursive=True))])

# 4. Jeux 45 Spec : un lot par pathologie produite (notions + questions + correction, ~140 Ko) + SSP
D = []
for fq in sorted(glob.glob("content/questions/*/*.json")):
    sp, base = fq.split("/")[2], os.path.basename(fq)[:-5]
    D.append(lot(f"P45_{sp}_{base}", f"45 Spec — {sp} — {base}", [f"content/notions/{sp}/{base}.json", fq, f"content/corrections/{sp}/{base}.json"],
                 "bonne réponse juste, distracteurs, masquage du diagnostic, explications, chiffres et posologies suisses, sources réelles, conformité PROFILES et SSP"))
D += [lot(f"SSP_{os.path.basename(f)[:-5]}", f"45 Spec — {os.path.basename(f)[:-5]}", [f], "algorithme décisionnel de la SSP, conformité PROFILES")
      for f in sorted(glob.glob("data/ssp/SSP_*.json"))]
ecrire("4_Jeux_45_Spec", D)
