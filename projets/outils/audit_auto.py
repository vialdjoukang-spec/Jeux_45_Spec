"""Audit automatique (0 token) des lots rendus par les IA de production.
Usage : python projets/outils/audit_auto.py <dossier_ou_fichier> [...] [-o rapport.md]
Contrôles par fichier rendu, contre le squelette ACTUEL du dépôt (référence vivante) :
  1. JSON lisible et au format lot ({_lot, fichiers}) ou fragment ;
  2. chaque chemin existe dans le dépôt ;
  3. chaque élément (id) existe, aucun élément manquant ni inventé ;
  4. schéma : champs manquants (dérive de version) et champs inventés ;
  5. remplissage : part des champs attendus réellement remplis, marqueurs <...> restants ;
  6. aVerifier : nombre de doutes déclarés par le producteur.
Verdict : 🟩 intégrable · 🟧 à compléter · 🟥 refusé. Le contrôle médical du fond reste à Claude.
Signature : AAI (Anthropic AI)"""
import json, os, sys, glob, re, datetime

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
args = sys.argv[1:]
sortie = None
if "-o" in args:
    i = args.index("-o"); sortie = args[i + 1]; del args[i:i + 2]
fichiers = []
for e in args:
    fichiers += sorted(glob.glob(os.path.join(e, "**", "*.json"), recursive=True)) if os.path.isdir(e) else [e]

vide = lambda v: v is None or v == "" or v == [] or v == {}
marque = re.compile(r"<[^<>]{1,40}>|À REMPLIR|TODO|WILL_BE_REPLACED", re.I)
cle_de = lambda x: (x.get("id") or x.get("ref") or x.get("nom")) if isinstance(x, dict) else None


def listes_par_id(d):
    return {k: v for k, v in d.items() if isinstance(v, list) and v and all(isinstance(x, dict) and cle_de(x) for x in v)}


def auditer_contenu(chemin, contenu, notes):
    cible = os.path.join(RAC, chemin)
    if not os.path.exists(cible):
        notes.append(f"🟥 `{chemin}` : chemin absent du dépôt"); return None
    ref = json.load(open(cible, encoding="utf-8"))
    fr = contenu.get("_fragment")
    st = {"attendus": 0, "remplis": 0, "manquants": set(), "inventes": set(), "marques": 0, "absents": [], "intrus": []}
    for k, lref in listes_par_id(ref).items():
        if fr and fr.get("cle") != k:
            continue
        rendus = {cle_de(x): x for x in contenu.get(k, []) if isinstance(x, dict)}
        idx_ref = {cle_de(x): x for x in lref}
        if not fr:
            st["absents"] += [i for i in idx_ref if i not in rendus]
        st["intrus"] += [i for i in rendus if i not in idx_ref]
        for i, x in rendus.items():
            r = idx_ref.get(i)
            if not r:
                continue
            st["manquants"] |= set(r) - set(x)
            st["inventes"] |= set(x) - set(r)
            for c in r:
                if c in ("id", "nom", "modalite"):
                    continue
                st["attendus"] += 1
                v = x.get(c)
                if not vide(v):
                    st["remplis"] += 1
                st["marques"] += len(marque.findall(json.dumps(v, ensure_ascii=False))) if v is not None else 0
    return st


lignes, bilan = [], {"🟩": 0, "🟧": 0, "🟥": 0}
for f in fichiers:
    nom = os.path.relpath(f, RAC)
    notes = []
    try:
        rendu = json.load(open(f, encoding="utf-8"))
    except Exception as err:
        lignes.append(f"### 🟥 `{nom}`\n- JSON illisible : {str(err)[:80]}\n"); bilan["🟥"] += 1; continue
    contenus = rendu.get("fichiers") if isinstance(rendu, dict) else None
    if not contenus:
        lignes.append(f"### 🟥 `{nom}`\n- Format inconnu : la clé « fichiers » manque (format lot attendu).\n"); bilan["🟥"] += 1; continue
    av = (rendu.get("_lot") or {}).get("aVerifier") or []
    pire, det = "🟩", []
    for chemin, contenu in contenus.items():
        st = auditer_contenu(chemin, contenu, notes)
        if st is None:
            pire = "🟥"; continue
        taux = st["remplis"] / st["attendus"] * 100 if st["attendus"] else 0
        v = "🟩"
        if st["intrus"] or st["inventes"]:
            v = "🟥"
        elif st["absents"] or st["manquants"] or st["marques"] or taux < 85:
            v = "🟧"
        pire = max(pire, v, key="🟩🟧🟥".index)
        d = f"- {v} `{os.path.basename(chemin)}` : remplissage {taux:.0f} % ({st['remplis']}/{st['attendus']})"
        if st["manquants"]: d += f" · champs absents (ancien schéma ?) : {', '.join(sorted(st['manquants']))}"
        if st["inventes"]: d += f" · champs inventés : {', '.join(sorted(st['inventes']))}"
        if st["absents"]: d += f" · {len(st['absents'])} élément(s) non rendu(s)"
        if st["intrus"]: d += f" · éléments inconnus : {', '.join(st['intrus'][:3])}"
        if st["marques"]: d += f" · {st['marques']} marqueur(s) <…> restant(s)"
        det.append(d)
    bilan[pire] += 1
    lignes.append(f"### {pire} `{nom}`\n" + "\n".join(notes + det) + (f"\n- aVerifier déclarés : {len(av)}" if av else "") + "\n")

texte = (f"# Audit automatique — {datetime.datetime.now():%Y-%m-%d %H:%M}\n\n"
         f"{len(fichiers)} fichier(s) : {bilan['🟩']} 🟩 intégrables · {bilan['🟧']} 🟧 à compléter · {bilan['🟥']} 🟥 refusés.\n\n"
         "Légende : 🟩 schéma conforme et ≥ 85 % rempli · 🟧 incomplet ou ancien schéma · 🟥 illisible, chemin ou élément inventé.\n"
         "Le fond médical (exactitude, sources, phrases verbales) reste audité par Claude.\n\n" + "\n".join(lignes) +
         "\nSignature : AAI (Anthropic AI)\n")
if sortie:
    os.makedirs(os.path.dirname(os.path.abspath(sortie)), exist_ok=True)
    open(sortie, "w", encoding="utf-8").write(texte)
print(texte if not sortie else f"{bilan} → {sortie}")
