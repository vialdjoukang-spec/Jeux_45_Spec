"""Réassemble les JSON rendus par les IA de production dans conception/donnees (0 token).
Usage : python projets/outils/fusionner_retours.py <fichier_ou_dossier_rendu> [...] [--essai]
- Fusion PAR CHAMP (lot complet ou fragment) : chaque élément revient à sa place par son id (ou ref, ou nom) ;
  seuls les champs remplis du rendu écrasent le dépôt ; les champs du schéma actuel absents du rendu
  (lot produit sur une version antérieure) restent dans le dépôt, vides, prêts pour un lot de complément.
- Champs inventés : ignorés et signalés ; éléments inconnus : refusés. aVerifier du lot → _meta.aVerifier du fichier.
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
    aver = (rendu.get("_lot") or {}).get("aVerifier") or []
    for chemin, contenu in (rendu.get("fichiers") or {}).items():
        cible = os.path.join(RAC, chemin)
        if not os.path.exists(cible):
            rapport.append(f"❌ {chemin} : chemin inconnu dans le dépôt"); ko += 1; continue
        actuel = json.load(open(cible, encoding="utf-8"))
        fr = contenu.pop("_fragment", None)
        cles = [fr["cle"]] if fr else [k for k, v in actuel.items() if isinstance(v, list) and v and isinstance(v[0], dict)]
        inconnus, inventes, n = [], set(), 0
        for k in cles:
            index = {cle_de(x): x for x in actuel.get(k, [])}
            for x in contenu.get(k, []):
                cible_el = index.get(cle_de(x))
                if cible_el is None:
                    inconnus.append(cle_de(x)); continue
                for c, v in x.items():
                    if c not in cible_el: inventes.add(c); continue
                    if v not in (None, "", [], {}): cible_el[c] = v
                n += 1
        if inconnus:
            rapport.append(f"❌ {chemin} : éléments inconnus {inconnus[:5]}"); ko += 1; continue
        for g, v in (contenu.get("glossaire") or {}).items():
            actuel.setdefault("glossaire", {})[g] = v
        av = [a.split("›", 1)[1].strip() for a in aver if a.startswith(chemin)]
        if av: actuel.setdefault("_meta", {})["aVerifier"] = av
        nouveau, mode = actuel, f"{'fragment ' + str(fr.get('valeur')) if fr else 'fusion par champ'} ({n} éléments{', champs inventés ignorés : ' + ', '.join(sorted(inventes)) if inventes else ''})"
        nouveau.setdefault("_meta", {})["statut"] = "PRODUIT — à auditer"
        if not essai:
            json.dump(nouveau, open(cible, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        rapport.append(f"✅ {chemin} : {mode}"); ok += 1
os.makedirs(os.path.join(RAC, "projets", "retours"), exist_ok=True)
open(os.path.join(RAC, "projets", "retours", "rapport_fusion.md"), "w", encoding="utf-8").write(
    f"# Rapport de fusion — {datetime.datetime.now():%Y-%m-%d %H:%M}{' (essai, rien écrit)' if essai else ''}\n\n{ok} fusionnés, {ko} refusés.\n\n" + "\n".join(f"- {r}" for r in rapport) + "\n\nSignature : AAI (Anthropic AI)\n")
print(f"{ok} fusionnés, {ko} refusés → projets/retours/rapport_fusion.md")
