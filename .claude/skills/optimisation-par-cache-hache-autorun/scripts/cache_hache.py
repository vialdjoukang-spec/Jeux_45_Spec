#!/usr/bin/env python3
"""cache_hache.py — exécute une commande seulement si ses entrées ont changé.
Empreinte = sha256(commande + contenu des fichiers d'entrée + variables déclarées).
Si l'empreinte est connue ET les sorties existent avec leur empreinte enregistrée → saut (0 coût).
Sinon → exécution, puis enregistrement des empreintes d'entrée et de sortie.
Usage :
  cache_hache.py -i 'content/**/*.json' -i scripts/x.py -o arene45/decks -- python scripts/x.py
  cache_hache.py --etat            (liste le registre)
  cache_hache.py --oublier NOM     (force la prochaine exécution)
Signature : AAI (Anthropic AI)"""
import argparse, glob, hashlib, json, os, subprocess, sys, time
REG = os.environ.get("CACHE_HACHE", ".cache_hache.json")

def h_fichier(p, hh):
    hh.update(p.encode()); 
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): hh.update(b)

def empreinte(motifs, extra=""):
    hh = hashlib.sha256(extra.encode())
    fichiers = sorted({f for m in motifs for f in glob.glob(m, recursive=True)
                       if os.path.isfile(f)} |
                      {os.path.join(r, n) for m in motifs if os.path.isdir(m)
                       for r, _, ns in os.walk(m) for n in ns})
    for f in sorted(set(fichiers)): h_fichier(f, hh)
    return hh.hexdigest(), len(fichiers)

def charger():
    try: return json.load(open(REG))
    except (FileNotFoundError, json.JSONDecodeError): return {}

def main():
    a = argparse.ArgumentParser()
    a.add_argument("-i", action="append", default=[], help="entrée (fichier, dossier ou motif glob)")
    a.add_argument("-o", action="append", default=[], help="sortie à vérifier")
    a.add_argument("-e", action="append", default=[], help="variable d'environnement qui compte")
    a.add_argument("-n", "--nom", help="nom de la tâche (défaut : la commande)")
    a.add_argument("--etat", action="store_true"); a.add_argument("--oublier")
    a.add_argument("cmd", nargs=argparse.REMAINDER)
    x = a.parse_args(); reg = charger()
    if x.etat:
        for k, v in reg.items(): print(f"{k}  {v['quand']}  {v['n']} fichiers  gain cumulé {v.get('sauts',0)} sauts")
        return
    if x.oublier: reg.pop(x.oublier, None); json.dump(reg, open(REG, "w"), indent=1); return
    cmd = [c for c in x.cmd if c != "--"]
    if not cmd: a.error("commande manquante après --")
    nom = x.nom or " ".join(cmd)
    extra = " ".join(cmd) + "".join(f"{e}={os.environ.get(e,'')}" for e in x.e)
    he, n = empreinte(x.i, extra)
    v = reg.get(nom, {})
    hs = empreinte(x.o)[0] if x.o else ""
    if v.get("entree") == he and v.get("sortie") == hs and all(os.path.exists(o) for o in x.o):
        v["sauts"] = v.get("sauts", 0) + 1; reg[nom] = v
        json.dump(reg, open(REG, "w"), indent=1)
        print(f"[cache] inchangé ({he[:10]}, {n} fichiers) → saut de : {nom}"); return
    t = time.time(); r = subprocess.run(cmd)
    if r.returncode: sys.exit(r.returncode)   # un échec n'est jamais mis en cache
    reg[nom] = {"entree": he, "sortie": empreinte(x.o)[0] if x.o else "", "n": n,
                "quand": time.strftime("%Y-%m-%d %H:%M"), "duree_s": round(time.time()-t, 1),
                "sauts": v.get("sauts", 0)}
    json.dump(reg, open(REG, "w"), indent=1)
    print(f"[cache] exécuté et enregistré ({he[:10]}) : {nom}")

if __name__ == "__main__": main()
