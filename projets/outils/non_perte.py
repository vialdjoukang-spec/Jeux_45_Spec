"""Garde de non-régression (0 token) : échoue si une valeur remplie sur main devient vide ou disparaît.

Compare chaque JSON de conception/donnees et SORTIES_DONNEES_FIABLES avec sa version sur une référence git
(par défaut origin/main). Une valeur modifiée reste permise ; une valeur perdue ne l'est jamais.
Usage : python non_perte.py [ref]      Signature : AAI (Anthropic AI)
"""
import json, os, subprocess, sys

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
VIDE = (None, "", [], {})

def feuilles(x, p="", double=False):
    """double=True (version locale) : chaque élément de liste est aussi repéré par sa position, pour qu'un
    élément dont l'id, vide sur main, vient d'être rempli ne compte pas comme perdu."""
    if isinstance(x, dict):
        for k, v in x.items():
            yield from feuilles(v, f"{p}/{k}", double)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            k = v.get("id") or v.get("ref") or v.get("nom") if isinstance(v, dict) else None
            yield from feuilles(v, f"{p}[{k if k else i}]", double)
            if double and k:
                yield from feuilles(v, f"{p}[{i}]", double)
    elif x not in VIDE:
        yield p

# renommages d'identifiants assumés (ancien préfixe → nouveau) : un chemin renommé n'est pas une perte
MIGR_F = os.path.join(RAC, "projets", "retours", "migrations_ids.json")
MIGR = json.load(open(MIGR_F, encoding="utf-8")) if os.path.exists(MIGR_F) else {}
def migrer(chemin):
    for a, n in MIGR.items():
        chemin = chemin.replace("[" + a, "[" + n)
    return chemin

git = lambda *a: subprocess.run(["git", "-C", RAC, *a], capture_output=True, text=True)
pertes = []
for chemin in git("ls-tree", "-r", "--name-only", REF, "--", "conception/donnees", "SORTIES_DONNEES_FIABLES").stdout.split("\n"):
    if not chemin.endswith(".json"):
        continue
    try:
        avant = {migrer(f) for f in feuilles(json.loads(git("show", f"{REF}:{chemin}").stdout))}
    except ValueError:
        continue
    local = os.path.join(RAC, chemin)
    apres = set(feuilles(json.load(open(local, encoding="utf-8")), double=True)) if os.path.exists(local) else set()
    perdu = {f for f in avant - apres if not f.startswith("/_meta/aCompleter")}  # liste de tâches : elle se vide quand le complément est fusionné
    if perdu:
        pertes.append((chemin, len(perdu), sorted(perdu)[:3]))
for c, n, ex in pertes:
    print(f"🟥 {c} : {n} valeur(s) perdue(s), ex. {ex}")
print(f"non-perte : {'ÉCHEC' if pertes else 'OK'} ({len(pertes)} fichier(s) en perte)")
sys.exit(1 if pertes else 0)
