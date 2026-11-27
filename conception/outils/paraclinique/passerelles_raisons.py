#!/usr/bin/env python3
"""PASSERELLES_RAISONS — remplit, sans cognition, la raison (« pourquoi ») des passerelles importées avec « — » (audit A7).
Deux familles seulement, dont la raison découle du type de passerelle défini au cahier d'architecture § 5.2 :
  · Fondement → SF-<système>-physiologie : la fiche de physiologie fonde les valeurs normales ;
  · Suivi thérapeutique → PH-<système>-<classe>-<molécule> : le taux sanguin guide la posologie de la molécule.
Toute autre passerelle sans raison reste signalée par l'audit. Idempotent. Signature : AAI (Anthropic AI)
"""
import glob, json, os, re

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
FICHES = os.path.join(RAC, "conception", "donnees", "paraclinique", "biologie", "fiches")
SYS = {"S1": "nerveux", "S2": "de la tête et du cou", "S3": "cardiovasculaire", "S4": "respiratoire", "S5": "digestif et hépatobiliaire",
       "S6": "rénal et urinaire", "S7": "reproducteur", "S8": "endocrinien et métabolique", "S9": "locomoteur", "S10": "sanguin et immunitaire",
       "S11": "psychique et du sommeil", "S12": "cutané", "T": "transversal"}
MOL = {"valproate": "du valproate", "lamotrigine": "de la lamotrigine", "carbamazepine": "de la carbamazépine"}

n = 0
for p in sorted(glob.glob(os.path.join(FICHES, "*", "*.json"))):
    d = json.load(open(p, encoding="utf-8")); chg = False
    for s in d.get("passerelles") or []:
        if (s.get("pourquoi") or "").strip() != "—":
            continue
        c = s.get("cible", "")
        m = re.match(r"SF-(S\d+|T)-physiologie$", c)
        if s.get("type") == "Fondement" and m:
            s["pourquoi"] = f"Cette fiche rappelle la physiologie du système {SYS[m.group(1)]}, qui fonde les valeurs normales de l'examen."
            chg = True
        m = re.match(r"PH-S\d+-[a-z]+-([a-z]+)$", c)
        if s.get("type") == "Suivi thérapeutique" and m and m.group(1) in MOL:
            s["pourquoi"] = f"Le taux sanguin guide l'adaptation de la posologie {MOL[m.group(1)]} ; la fiche molécule donne la posologie."
            chg = True
    if chg:
        open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n"); n += 1
print(f"passerelles : {n} fiches complétées")
