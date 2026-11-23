"""Résout un conflit de fusion sur les fichiers de suivi de l'ouvrier (0 token).
FILE_PROCESSUS.json : la file distante (tâches ajoutées par Claude) sert de base ; l'état des tâches que l'ouvrier vient de traiter
(etat, essais, dernier) vient de la version locale. depense.json : union des lignes. Autres fichiers de projets/ouvrier : version locale.
Sort en erreur si un conflit touche un autre fichier (données : jamais de résolution aveugle)."""
import json, subprocess, sys

f = subprocess.run(["git", "diff", "--name-only", "--diff-filter=U"], capture_output=True, text=True).stdout.split()
if not f or any(not x.startswith("projets/ouvrier/") for x in f):
    sys.exit(f"conflit hors suivi : {f}")
lire = lambda cote, p: json.loads(subprocess.run(["git", "show", f":{cote}:{p}"], capture_output=True, text=True, check=True).stdout)
for p in f:
    if p.endswith("FILE_PROCESSUS.json"):
        nous, eux = lire(2, p), lire(3, p); loc = {t["id"]: t for t in nous["taches"]}; vus = set()
        for t in eux["taches"]:
            vus.add(t["id"])
            if t["id"] in loc:
                for k in ("etat", "essais", "dernier"):
                    if k in loc[t["id"]]:
                        t[k] = loc[t["id"]][k]
        eux["taches"] += [t for t in nous["taches"] if t["id"] not in vus]
        json.dump(eux, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    elif p.endswith("depense.json"):
        a, b = lire(2, p), lire(3, p); cle = lambda x: json.dumps(x, sort_keys=True)
        u = {cle(x): x for x in (b + a)} if isinstance(a, list) else a
        json.dump(sorted(u.values(), key=lambda x: x.get("date", "")) if isinstance(a, list) else a, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    else:
        subprocess.run(["git", "checkout", "--ours", p], check=True)
    subprocess.run(["git", "add", p], check=True)
subprocess.run(["git", "commit", "-q", "--no-edit"], check=True); print("conflit de suivi résolu :", f)
