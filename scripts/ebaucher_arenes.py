"""Ébauche complète des 45 arènes de MedSuisse Arena 45, à 0 token, depuis la Cartographie Renouveau (data/ssp).

Pour chaque spécialité, l'arène liste toutes ses tuiles (entités), de la plus banale à la plus rare, avec :
  - ses SSP d'origine, son CIM-10, son système, sa fréquence et son urgence ;
  - ses rubriques de notions et leur poids (une notion de poids n exige au moins n questions) ;
  - la cible de questions (total, part « zéro-D » d'au moins 30 %, cas long en 6 étapes) ;
  - l'état de production de chaque couche (fiche, réflexes, questions), relu à chaque passage.
Sortie : content/arenes/<CODE>/arene.json, content/arenes/INDEX.json, content/arenes/ETAT.md
Relançable sans risque : l'ébauche se recalcule, l'état de production se relit sur disque.
Signature : AAI (Anthropic AI)"""
import glob, json, os, re
from collections import defaultdict

RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = json.load(open(os.path.join(RAC, "data", "references", "entite_specialites.json"), encoding="utf-8"))
SORTIE = os.path.join(RAC, "content", "arenes")
FREQ = {"TF": (1, "très fréquente"), "F": (2, "fréquente"), None: (3, "urgence"), "MF": (4, "peu fréquente"), "R": (5, "rare")}
ZERO_D = {"definition", "basicSciences", "pathophysiology"}
LIB = {"definition": "Définition", "epidemiology": "Épidémiologie", "biostatistics": "Biostatistiques", "basicSciences": "Sciences fondamentales",
       "pathophysiology": "Physiopathologie", "anamnesis": "Anamnèse", "clinicalExam": "Examen physique", "presumptionRedFlags": "Drapeaux rouges",
       "positiveDiagnosis": "Diagnostic positif", "workupGoldStandard": "Examen de référence", "workupAlternatives": "Examens alternatifs",
       "acuteManagement": "Prise en charge aiguë", "chronicManagement": "Prise en charge chronique",
       "hospitalizationComplications": "Hospitalisation et complications", "surveillance": "Surveillance",
       "prognosisDischarge": "Pronostic et sortie", "followUpNetwork": "Suivi et réseau"}
sid = lambda i: re.sub(r"[^A-Za-z0-9_-]", "_", i)[:64]


def etat(code, eid):
    f = os.path.join(RAC, "content", "fiches", code, sid(eid) + ".json")
    r = os.path.join(RAC, "content", "reflexes", code, sid(eid) + ".json")
    it = glob.glob(os.path.join(RAC, "content", "items", code, sid(eid), "*.json"))
    return {"fiche": "produite" if os.path.exists(f) else "a_produire", "reflexes": "produits" if os.path.exists(r) else "a_produire",
            "rubriquesAvecQuestions": len(it)}


tuiles = defaultdict(dict)
for f in sorted(glob.glob(os.path.join(RAC, "data", "ssp", "SSP_*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    for e in d["entites"]:
        for s in SPEC["entiteVersSpecialites"].get(e["id"], []):
            t = tuiles[s].setdefault(e["id"], {"id": e["id"], "nom": e["nom"], "cim10": e.get("cim10"), "systeme": e.get("systeme"),
                                               "strate": e.get("strate"), "urgence": e.get("urgence"), "urgenceTable": "urgence" in (e.get("tables") or []),
                                               "ssp": [], "notions": e["notions"], "poidsTotal": e.get("poidsTotal") or sum(n["poids"] for n in e["notions"])})
            t["ssp"].append({"code": d["ssp"], "nom": d["nom"], "circuit": d["circuit"]})

index, lignes = [], []
for s, info in SPEC["specialites"].items():
    code = info["code"]
    ts = sorted(tuiles.get(s, {}).values(), key=lambda t: (FREQ.get(t["strate"], FREQ[None])[0], not t["urgenceTable"], t["nom"]))
    out = []
    for rang, t in enumerate(ts, 1):
        q = sum(n["poids"] for n in t["notions"])
        q0 = sum(n["poids"] for n in t["notions"] if n["rubrique"] in ZERO_D)
        out.append({"rang": rang, "id": t["id"], "nom": t["nom"], "cim10": t["cim10"], "systeme": t["systeme"],
                    "palier": FREQ.get(t["strate"], FREQ[None])[1], "urgenceVitale": t["urgenceTable"] or t["urgence"] == "urgence",
                    "ssp": t["ssp"], "deverrouillage": "3 réussites espacées (FSRS) sur ses questions",
                    "rubriques": [{"rubrique": n["rubrique"], "libelle": LIB.get(n["rubrique"], n["rubrique"]), "poids": n["poids"],
                                   "questionsMin": n["poids"], "zeroD": n["rubrique"] in ZERO_D} for n in t["notions"]],
                    "cibleQuestions": {"total": q, "zeroD": max(q0, round(0.3 * q)), "formats": ["A", "K'"], "casLong": "1 cas en 6 étapes × 2 questions"},
                    "production": etat(code, t["id"])})
    paliers = defaultdict(int)
    for t in out:
        paliers[t["palier"]] += 1
    arene = {"_meta": {"specialite": s, "code": code, "nom": info["nom"], "signature": "AAI (Anthropic AI)",
                       "regles": ["Pas de cours : la correction commentée en 7 marches tient lieu de cours (zéro-D → mécanisme → sémiologie → discriminant → décision → piège → ancre).",
                                  "Chaque option fausse reçoit son explication.", "Ordre de production : très fréquentes → fréquentes → urgences → peu fréquentes → rares.",
                                  "Couches : fiche de raisonnement (source de vérité) → cartes réflexes (script, 0 token) → questions A et K' par rubrique."]},
             "resume": {"tuiles": len(out), "paliers": dict(paliers), "questionsCibles": sum(t["cibleQuestions"]["total"] for t in out),
                        "fichesProduites": sum(t["production"]["fiche"] == "produite" for t in out)},
             "modes": {"arene": "Duels chronométrés : du réflexe (premier geste) au raisonnement (vignette longue).",
                       "aventure": "Une carte par spécialité ; chaque poste traite un palier (très fréquentes → rares).",
                       "puzzles": ["Ordonner les premiers gestes", "Choisir le discriminant", "Repérer le drapeau rouge", "Chiffre clé"]},
             "tuiles": out}
    os.makedirs(os.path.join(SORTIE, code), exist_ok=True)
    json.dump(arene, open(os.path.join(SORTIE, code, "arene.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    index.append({"specialite": s, "code": code, "nom": info["nom"], **arene["resume"], "fichier": f"{code}/arene.json"})
    lignes.append(f"| {code} | {info['nom']} | {len(out)} | {arene['resume']['questionsCibles']} | {arene['resume']['fichesProduites']} |")

tot = {k: sum(x[k] for x in index) for k in ("tuiles", "questionsCibles", "fichesProduites")}
json.dump({"_meta": {"source": "Cartographie Renouveau (data/ssp) × tuiles du jeu v1 (entite_specialites.json)", "signature": "AAI (Anthropic AI)"},
           "total": tot, "arenes": index}, open(os.path.join(SORTIE, "INDEX.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(os.path.join(SORTIE, "ETAT.md"), "w", encoding="utf-8").write(
    "# État des 45 arènes (généré par scripts/ebaucher_arenes.py)\n\n"
    f"Tuiles (une entité peut ouvrir plusieurs arènes) : {tot['tuiles']} · questions cibles : {tot['questionsCibles']} · fiches produites : {tot['fichesProduites']}.\n\n"
    "| Code | Spécialité | Tuiles | Questions cibles | Fiches produites |\n|---|---|---|---|---|\n" + "\n".join(lignes) + "\n\nSignature : AAI (Anthropic AI)\n")
print(f"arènes : {len(index)} | tuiles : {tot['tuiles']} | questions cibles : {tot['questionsCibles']} | fiches : {tot['fichesProduites']}")
