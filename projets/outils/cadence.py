"""Curseur de fréquence de la veille (0 token).

GitHub réveille la veille toutes les 5 minutes (son minimum). Ce script décide si le passage est utile :
plus des lots sont arrivés récemment, plus la veille passe souvent.

  lots reçus dans la dernière heure ≥ 3  → toutes les 5 min
  lots reçus dans la dernière heure 1–2  → toutes les 10 min
  rien depuis 1 h, mais des lots dans les 6 h → toutes les 20 min
  rien depuis 6 h                        → toutes les 60 min

Un dépôt sur main déclenche la veille immédiatement, sans passer par ce curseur.
Usage : python cadence.py <fichier_etat>   → écrit « due=true|false » dans $GITHUB_OUTPUT (ou sur la sortie).
Signature : AAI (Anthropic AI)
"""
import datetime, json, os, sys

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRE = os.path.join(RAC, "projets", "retours", "veille_traites.json")
etat_f = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RAC, ".veille_cadence.json")
maint = datetime.datetime.now(datetime.timezone.utc)

heures = []
if os.path.exists(REGISTRE):
    for v in json.load(open(REGISTRE, encoding="utf-8")).values():
        if v.get("heure"):
            heures.append(datetime.datetime.fromisoformat(v["heure"]))
age = lambda h: (maint - h).total_seconds() / 60
h1, h6 = sum(age(h) <= 60 for h in heures), sum(age(h) <= 360 for h in heures)
intervalle = 5 if h1 >= 3 else 10 if h1 >= 1 else 20 if h6 else 60

etat = json.load(open(etat_f)) if os.path.exists(etat_f) else {}
dernier = datetime.datetime.fromisoformat(etat["dernier"]) if etat.get("dernier") else None
due = dernier is None or age(dernier) >= intervalle - 1   # 1 min de marge : le cron GitHub dérive
if due:
    json.dump({"dernier": maint.isoformat(timespec="seconds"), "intervalle": intervalle}, open(etat_f, "w"))
ligne = f"due={'true' if due else 'false'}\n"
print(f"cadence : {h1} lot(s) dans l'heure, {h6} dans les 6 h → intervalle {intervalle} min ; passage {'utile' if due else 'sauté'}")
if os.environ.get("GITHUB_OUTPUT"):
    open(os.environ["GITHUB_OUTPUT"], "a").write(ligne)
