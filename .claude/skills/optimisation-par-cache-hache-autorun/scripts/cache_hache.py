#!/usr/bin/env python3
"""Cache haché : ne relance une commande déterministe que si ses entrées, sa commande, ses variables
déclarées ou ses sorties ont changé. Ne met jamais un échec en cache.

Usage :
  python cache_hache.py [--nom N] -i 'motif/**/*.json' [-i ...] [-o sortie/ ...] [-e VAR ...] -- commande args...
  python cache_hache.py --etat            liste les tâches, leur date, leurs fichiers et leurs sauts
  python cache_hache.py --oublier N       retire une tâche du registre (la prochaine exécution relance)
Options : --forcer (exécute quand même), --registre CHEMIN (défaut : .cache_hache.json à la racine git).

L'empreinte des entrées est prise APRÈS l'exécution : un script idempotent qui corrige ses propres
entrées (ex. audit_fond.py) n'est donc pas relancé pour rien au passage suivant.
Signature : AAI (Anthropic AI)"""
import argparse, datetime, glob, hashlib, json, os, subprocess, sys

BLOC = 1 << 20


def racine():
    try:
        return subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return os.getcwd()


def hacher_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for b in iter(lambda: f.read(BLOC), b""):
            h.update(b)
    return h.hexdigest()


def fichiers_de(motifs):
    vus = set()
    for m in motifs:
        trouves = glob.glob(m, recursive=True)
        if not trouves:
            vus.add(("absent", m))
        for t in trouves:
            if os.path.isdir(t):
                for d, _, fs in os.walk(t):
                    vus.update(("f", os.path.join(d, x)) for x in fs if "__pycache__" not in d)
            else:
                vus.add(("f", t))
    return sorted(vus)


def empreinte(motifs):
    h, n = hashlib.sha256(), 0
    for genre, chemin in fichiers_de(motifs):
        h.update(f"{genre}\0{os.path.normpath(chemin)}\0".encode())
        if genre == "f" and os.path.isfile(chemin):
            h.update(hacher_fichier(chemin).encode())
            n += 1
    return h.hexdigest(), n


def lire(reg):
    try:
        return json.load(open(reg, encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def ecrire(reg, donnees):
    tmp = reg + ".tmp"
    json.dump(donnees, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    os.replace(tmp, reg)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("-i", "--entree", action="append", default=[])
    p.add_argument("-o", "--sortie", action="append", default=[])
    p.add_argument("-e", "--env", action="append", default=[])
    p.add_argument("--nom")
    p.add_argument("--registre")
    p.add_argument("--forcer", action="store_true")
    p.add_argument("--etat", action="store_true")
    p.add_argument("--oublier")
    p.add_argument("commande", nargs=argparse.REMAINDER)
    a = p.parse_args()
    reg = a.registre or os.path.join(racine(), ".cache_hache.json")
    donnees = lire(reg)

    if a.etat:
        if not donnees:
            print("Registre vide :", reg)
        for nom, t in sorted(donnees.items()):
            print(f"{nom:32} {t['date']}  {t['fichiers']:>6} fichiers  {t['sauts']:>4} sauts  {t['duree_s']:>7.1f} s/exécution  ≈{t['sauts'] * t['duree_s']:.0f} s économisées")
        return 0
    if a.oublier:
        donnees.pop(a.oublier, None)
        ecrire(reg, donnees)
        return 0

    cmd = a.commande[1:] if a.commande[:1] == ["--"] else a.commande
    if not cmd:
        p.error("commande manquante après --")
    if not a.entree:
        p.error("au moins une entrée (-i) est requise : sans entrée, rien ne prouve que le résultat est à jour")
    nom = a.nom or hashlib.sha256("\0".join(cmd).encode()).hexdigest()[:12]
    signature = hashlib.sha256(json.dumps([cmd, {v: os.environ.get(v) for v in sorted(a.env)}]).encode()).hexdigest()

    t = donnees.get(nom)
    if t and not a.forcer and t.get("signature") == signature:
        e, _ = empreinte(a.entree)
        s, _ = empreinte(a.sortie) if a.sortie else ("", 0)
        if e == t["entrees"] and s == t["sorties"]:
            t["sauts"] += 1
            ecrire(reg, donnees)
            print(f"⏭  {nom} : entrées et sorties inchangées, exécution sautée ({t['sauts']} sauts).")
            return 0

    debut = datetime.datetime.now()
    rc = subprocess.run(cmd).returncode
    duree = (datetime.datetime.now() - debut).total_seconds()
    donnees = lire(reg)  # relu : une autre tâche a pu écrire pendant l'exécution
    if rc != 0:
        donnees.pop(nom, None)  # jamais d'échec en cache
        ecrire(reg, donnees)
        return rc
    e, n = empreinte(a.entree)
    s, _ = empreinte(a.sortie) if a.sortie else ("", 0)
    ancien = donnees.get(nom, {})
    donnees[nom] = {"commande": cmd, "signature": signature, "entrees": e, "sorties": s, "fichiers": n,
                    "date": debut.strftime("%Y-%m-%d %H:%M"), "duree_s": round(duree, 2), "sauts": ancien.get("sauts", 0)}
    ecrire(reg, donnees)
    return 0


if __name__ == "__main__":
    sys.exit(main())
