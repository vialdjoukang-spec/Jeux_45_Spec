"""Arène 45 Spec — données du frontend (0 token). Écrit conception/prototypes/arene45/specs.json (45 spécialités, icônes,
pathologies canoniques, notions cochées, questions) et decks/<CODE>.json (séries et questions isolées, à diagnostic masqué).
Le nom de la pathologie n'est livré qu'à part, dans le champ « revele », que l'interface n'affiche qu'à la fin de la série.
Signature : AAI (Anthropic AI)"""
import collections, glob, json, os, sys

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))); os.chdir(R)
sys.path.insert(0, "scripts")
OUT = "conception/prototypes/arene45"; os.makedirs(OUT + "/decks", exist_ok=True)
ICONES = {"ALL": "allergy", "ANE": "airware", "ANG": "vital_signs", "CAR": "cardiology", "CHI": "surgical", "CCT": "ecg_heart",
          "CMA": "back_hand", "CMF": "dentistry", "ORT": "orthopedics", "CPE": "child_care", "CPL": "face_retouching_natural",
          "CTH": "pulmonology", "CVA": "blood_pressure", "DER": "dermatology", "END": "endocrinology", "GAS": "gastroenterology",
          "GEN": "genetics", "GYN": "gynecology", "HEM": "hematology", "INF": "coronavirus", "MTR": "engineering", "INT": "monitor_heart",
          "MIG": "stethoscope", "LEG": "gavel", "NUC": "radiology", "PHA": "medication", "MPR": "physical_therapy", "TRO": "travel_explore",
          "NEP": "nephrology", "NCH": "neurology", "NEU": "neurology", "ONC": "oncology", "OPH": "ophthalmology", "ORL": "hearing",
          "PAT": "biotech", "PED": "pediatrics", "TOX": "science", "PNE": "pulmonology", "PSP": "public", "PSY": "psychology",
          "PEA": "psychiatry", "RON": "radiology", "RAD": "radiology", "RHU": "rheumatology", "URO": "urology"}
ref = json.load(open("data/references/entite_specialites.json", encoding="utf-8"))["specialites"]
try:
    import produire_notions_questions as P
    canon = {c: len(P.canoniques(c)) for c in [v["code"] for v in ref.values()]}
except Exception as ex:      # la carte reste utilisable sans la chaîne de production
    print("canoniques indisponibles :", ex); canon = {}
def imbriquer(plat):
    """Arbre à plat (id, parent) → arbre imbriqué {t, i, e, pec, notion} lu par l'interface."""
    if not plat:
        return None
    if isinstance(plat, dict):
        return plat
    par = {}
    for x in plat:
        par.setdefault(x.get("parent"), []).append(x)
    def n(x):
        return {k: v for k, v in {"t": x["t"], "i": x.get("i"), "pec": x.get("pec"), "notion": x.get("notion"),
                                  "e": [n(y) for y in par.get(x["id"], [])]}.items() if v}
    return n(par[None][0])


def correction(cid, spec):
    """Correction enrichie d'une pathologie : produite (content/corrections) ou référence d'or (conception/donnees/corrections)."""
    f = f"content/corrections/{spec}/{cid}.json"
    if not os.path.exists(f):
        return None
    d = json.load(open(f, encoding="utf-8"))
    # Correction rejetée à l'audit ou de forme invalide (sortie tronquée) : la série reste jouable, sans correction.
    if (d.get("audit") or {}).get("rejector") == "rejet" or not isinstance(d.get("ssp"), dict) or not isinstance(d.get("notions"), list):
        return None
    return {"theme": d["theme"], "ssp": {**d["ssp"], "algorithme": imbriquer(d["ssp"]["algorithme"])},
            "notions": [{"id": x["id"], "titre": x["titre"], "rubriques": x.get("rubriques", []), "comment": x["comment"], "sources": x.get("sources", []),
                         "cours": {k: v for k, v in {"tableau": x.get("tableau"), "arbre": imbriquer(x.get("arbre")), "points": x.get("points")}.items() if v}} for x in d["notions"]],
            "pec": {p["cle"]: p for p in d.get("priseEnCharge", [])}}


specs = []
for k, v in ref.items():
    c = v["code"]; N = [json.load(open(f, encoding="utf-8")) for f in glob.glob(f"content/notions/{c}/*.json")]
    notions = [n for d in N for n in d["notions"]]; qfiles = sorted(glob.glob(f"content/questions/{c}/*.json")); deck = []
    for i, f in enumerate(qfiles):
        d = json.load(open(f, encoding="utf-8"))
        if (d.get("audit") or {}).get("rejector") == "rejet":
            continue
        par = collections.defaultdict(list)
        for q in d["questions"]:
            par[(q.get("serie") or {}).get("id") or "isolee_" + q["id"]].append(q)
        for sid, qs in par.items():
            qs.sort(key=lambda q: (q.get("serie") or {}).get("etape", 0))
            deck.append({"id": f"P{i + 1:03d}-{sid}", "progressive": not sid.startswith("isolee_"),
                         "questions": [{kk: q[kk] for kk in ("format", "situation", "diagnosticMasque", "stem", "prompt", "options", "statements", "notions", "angle", "difficulte", "ladder", "sources") if kk in q} for q in qs],
                         "revele": {"pathologie": d["entite"], "cim10": d.get("cim10"), "notions": {n["id"]: n["enonce"] for n in json.load(open(f.replace("questions", "notions"), encoding="utf-8"))["notions"]} if os.path.exists(f.replace("questions", "notions")) else {}},
                         "audite": (d.get("audit") or {}).get("rejector") == "pass",
                         "correction": correction(os.path.basename(f)[:-5], c)})
    if deck:
        json.dump({"code": c, "series": deck}, open(f"{OUT}/decks/{c}.json", "w", encoding="utf-8"), ensure_ascii=False)
    specs.append({"code": c, "nom": v["nom"], "icone": ICONES.get(c, "medical_services"), "pathologies": canon.get(c, 0),
                  "notions": len(notions), "cochees": sum(n.get("couverture", {}).get("cochee", False) for n in notions),
                  "questions": sum(len(s["questions"]) for s in deck), "series": len(deck)})
G = {k: v for k, v in json.load(open("conception/donnees/glossaire_sigles.json", encoding="utf-8")).items() if not k.startswith("_")}
json.dump(G, open(f"{OUT}/sigles.json", "w", encoding="utf-8"), ensure_ascii=False)
import shutil
shutil.copy("conception/prototypes/commun/correction.js", f"{OUT}/correction.js")
json.dump({"specs": specs}, open(f"{OUT}/specs.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"arène 45 : {len(specs)} spécialités, {sum(s['questions'] for s in specs)} questions, {sum(s['pathologies'] for s in specs)} pathologies canoniques")
