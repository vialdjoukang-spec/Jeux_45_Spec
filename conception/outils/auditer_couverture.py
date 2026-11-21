"""Audit de couverture des examens complémentaires (0 token). Bloquant si un contrôle échoue.
Usage : python conception/outils/auditer_couverture.py  → conception/audit/couverture.md + couverture.json"""
import json, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalogue_paraclinique import TOPO, PRELEVEMENTS, MODALITES, SYSTEMES

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
norm = lambda t: unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
TOUT = norm(json.dumps([TOPO, PRELEVEMENTS], ensure_ascii=False))

# Chaque système de la Tétrade doit trouver ses organes dans le catalogue.

# Examens témoins : un examinateur s'attend à les trouver ; leur absence signe un oubli.
TEMOINS = ["ECG", "Holter", "échocardiographie transthoracique", "transœsophagienne", "coronarographie", "troponine", "NT-proBNP", "D-dimères", "score calcique",
           "spirométrie", "DLCO", "gazométrie", "bronchoscopie", "CT thoracique", "ventilation-perfusion", "polysomnographie", "test de marche",
           "EEG", "ENMG", "IRM cérébrale", "LCR", "potentiels évoqués", "fond d'œil", "champ visuel", "audiométrie", "VNG", "DaTSCAN",
           "TSH", "échographie thyroïdienne", "cytoponction", "PTH", "cortisol", "métanéphrines", "aldostérone", "HGPO", "HbA1c", "prolactine",
           "gastroscopie", "coloscopie", "CPRE", "écho-endoscopie", "vidéocapsule", "élastographie", "lipase", "ALAT", "calprotectine", "test respiratoire", "anti-transglutaminase",
           "échographie abdominale", "uro-CT", "créatinine", "bandelette", "Kass", "cystoscopie", "urodynamique", "PSA", "IRM prostatique", "spermogramme",
           "mammographie", "HPV", "β-hCG", "échographie obstétricale", "cardiotocographie", "colposcopie", "hystéroscopie",
           "ostéodensitométrie", "scintigraphie osseuse", "liquide synovial", "anti-CCP", "HLA-B27", "CK", "IPS", "capillaroscopie", "échodoppler veineux", "thrombophilie",
           "formule sanguine", "frottis sanguin", "TP/INR", "myélogramme", "cytométrie", "électrophorèse", "hémocultures", "procalcitonine", "IGRA", "paludisme", "tryptase",
           "PET-CT", "CT corps entier", "eFAST", "caryotype", "test de la sueur", "dermatoscopie", "biopsie cutanée", "patch", "prick",
           "toxicologique", "lithium", "alcoolémie", "carboxyhémoglobine", "échelles psychométriques", "bilan neuropsychologique"]

r = {"controles": [], "manques": [], "remarques": []}
def ctrl(nom, ok, detail=""):
    r["controles"].append({"controle": nom, "ok": bool(ok), "detail": detail})

organes = {o: m for reg in TOPO.values() for o, m in reg.items()}
for s, orgs in SYSTEMES.items():
    absents = [o for o in orgs if o not in organes]
    ctrl(f"Système « {s} » relié au catalogue", not absents, ", ".join(absents))
non_relies = [o for o in organes if not any(o in v for v in SYSTEMES.values())]
r["remarques"].append(f"Organes du catalogue non rattachés à un système (navigation topographique seule) : {', '.join(non_relies) or 'aucun'}.")
pauvres = [o for o, m in organes.items() if len(m) < 2 and o not in ("Génétique", "Toxicologie et médicaments", "Corps entier (bilan d'extension et trauma)", "Sommeil et vigilance", "Épaule", "Hanche et bassin", "Cheville et pied", "Os du crâne et de la face", "Paroi thoracique et côtes", "Uretères")]
ctrl("Chaque organe couvre au moins deux modalités (sauf exceptions justifiées)", not pauvres, ", ".join(pauvres))
doublons = [(o, e) for o, m in organes.items() for k, v in m.items() for e in set(v) if v.count(e) > 1]
ctrl("Aucun doublon dans un même organe", not doublons, str(doublons))
manq = [t for t in TEMOINS if norm(t) not in TOUT]
r["manques"] = manq
ctrl(f"Les {len(TEMOINS)} examens témoins sont présents", not manq, ", ".join(manq))
ctrl("Chaque prélèvement liste ses examens", all(PRELEVEMENTS.values()))
compte = {"regions": len(TOPO), "organes": len(organes), "prelevements": len(PRELEVEMENTS), **{MODALITES[k]: sum(len(m.get(k, [])) for m in organes.values()) for k in MODALITES}}
r["compte"] = compte
r["verdict"] = "RÉUSSI" if all(c["ok"] for c in r["controles"]) else "ÉCHEC"

os.makedirs(os.path.join(ICI, "audit"), exist_ok=True)
json.dump(r, open(os.path.join(ICI, "audit", "couverture.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
md = [f"# Audit de couverture des examens — {r['verdict']}", "", "| Contrôle | Résultat | Détail |", "|---|---|---|"]
md += [f"| {c['controle']} | {'✅' if c['ok'] else '❌'} | {c['detail']} |" for c in r["controles"]]
md += ["", "**Couverture :** " + " · ".join(f"{k} : {v}" for k, v in compte.items()), ""] + [f"- {x}" for x in r["remarques"]]
open(os.path.join(ICI, "audit", "couverture.md"), "w", encoding="utf-8").write("\n".join(md))
print(r["verdict"], compte); [print(" ❌", c["controle"], "→", c["detail"]) for c in r["controles"] if not c["ok"]]
sys.exit(0 if r["verdict"] == "RÉUSSI" else 1)
