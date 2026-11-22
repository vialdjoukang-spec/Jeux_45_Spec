"""Réassemble les JSON rendus par les IA de production dans conception/donnees (0 token).
Usage : python projets/outils/fusionner_retours.py <fichier_ou_dossier_rendu> [...] [--essai]
- Lot complet : chaque chemin de « fichiers » remplace le fichier du dépôt, si ses clés sont identiques.
- Fragment (_fragment) : chaque élément de la liste revient à sa place par son id (ou ref, ou nom) ; le reste du fichier ne bouge pas.
- Contrôles : chemin connu, clés inchangées, aucun élément inconnu ; rapport dans projets/retours/rapport_fusion.md.
Signature : AAI (Anthropic AI)"""
import json, os, sys, glob, datetime

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
essai = "--essai" in sys.argv
entrees = [a for a in sys.argv[1:] if a != "--essai"]
fichiers = []
for e in entrees:
    fichiers += sorted(glob.glob(os.path.join(e, "**", "*.json"), recursive=True)) if os.path.isdir(e) else [e]

cle_de = lambda x: x.get("id") or x.get("ref") or x.get("nom") if isinstance(x, dict) else x
rapport, ok, ko = [], 0, 0
for f in fichiers:
    try:
        rendu = json.load(open(f, encoding="utf-8"))
    except Exception as err:
        rapport.append(f"❌ {f} : JSON illisible ({err})"); ko += 1; continue
    for chemin, contenu in (rendu.get("fichiers") or {}).items():
        cible = os.path.join(RAC, chemin)
        if not os.path.exists(cible):
            rapport.append(f"❌ {chemin} : chemin inconnu dans le dépôt"); ko += 1; continue
        actuel = json.load(open(cible, encoding="utf-8"))
        fr = contenu.pop("_fragment", None)
        if fr:
            k = fr["cle"]
            index = {cle_de(x): i for i, x in enumerate(actuel.get(k, []))}
            inconnus = [cle_de(x) for x in contenu.get(k, []) if cle_de(x) not in index]
            if inconnus:
                rapport.append(f"❌ {chemin} : éléments inconnus {inconnus[:5]}"); ko += 1; continue
            for x in contenu.get(k, []):
                actuel[k][index[cle_de(x)]] = x
            for g, v in (contenu.get("glossaire") or {}).items():
                actuel.setdefault("glossaire", {})[g] = v
            nouveau, mode = actuel, f"fragment {fr.get('valeur')} ({len(contenu.get(k, []))} éléments)"
        else:
            manque = sorted(set(actuel) - set(contenu) - {"_meta"})
            if manque:
                rapport.append(f"❌ {chemin} : clés supprimées {manque}"); ko += 1; continue
            contenu["_meta"] = {**actuel.get("_meta", {}), **contenu.get("_meta", {})}
            nouveau, mode = contenu, "fichier complet"
        nouveau.setdefault("_meta", {})["statut"] = "PRODUIT — à auditer"
        if not essai:
            json.dump(nouveau, open(cible, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        rapport.append(f"✅ {chemin} : {mode}"); ok += 1
os.makedirs(os.path.join(RAC, "projets", "retours"), exist_ok=True)
open(os.path.join(RAC, "projets", "retours", "rapport_fusion.md"), "w", encoding="utf-8").write(
    f"# Rapport de fusion — {datetime.datetime.now():%Y-%m-%d %H:%M}{' (essai, rien écrit)' if essai else ''}\n\n{ok} fusionnés, {ko} refusés.\n\n" + "\n".join(f"- {r}" for r in rapport) + "\n\nSignature : AAI (Anthropic AI)\n")
print(f"{ok} fusionnés, {ko} refusés → projets/retours/rapport_fusion.md")
