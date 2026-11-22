"""Transforme une structure de données (dossier, fichiers JSON, lots) en réseau Obsidian-like interactif.
Usage : python data_vers_reseau.py <dossier|fichier.json> -o reseau.html [--titre T] [--niveaux "Projet,Thème,Région,Lot"]
        [--contenu 2] [--github https://github.com/u/r/blob/main/] [--canvas reseau.canvas] [--signature "AAI (Anthropic AI)"]
Sortie : une page HTML autonome (données incluses) + optionnellement un fichier JSON Canvas 1.0 (ouvrable dans Obsidian)."""
import argparse, json, os, re, sys

PALETTE = ["#1E3A8A", "#16897b", "#c0392b", "#7a5cc4", "#d97706", "#0e7490", "#be185d", "#4d7c0f", "#b45309", "#334155", "#9333ea", "#0369a1", "#a16207", "#15803d", "#6b21a8", "#9f1239"]
ICI = os.path.dirname(os.path.abspath(__file__))


def lisible(o):
    """Nom humain d'un dossier ou fichier : préfixes numériques gardés, _ → espace."""
    return re.sub(r"\.json$", "", o).replace("_", " ")


def resume_json(v):
    if isinstance(v, dict):
        if "fichiers" in v and isinstance(v["fichiers"], dict):
            if len(v["fichiers"]) == 1:
                return resume_json(next(iter(v["fichiers"].values())))
            return f"{len(v['fichiers'])} fichiers inclus"
        for k in ("examens", "analyses", "entites", "elements", "lecons", "noeuds"):
            if isinstance(v.get(k), list):
                return f"{len(v[k])} {k}"
        return f"{len([k for k in v if not k.startswith('_')])} clés"
    if isinstance(v, list):
        return f"{len(v)} éléments"
    return ""


def nom_item(x, i):
    if isinstance(x, dict):
        for k in ("nom", "titre", "label", "texte", "id"):
            if isinstance(x.get(k), str):
                return x[k]
    return x if isinstance(x, str) else f"élément {i + 1}"


def main():
    a = argparse.ArgumentParser()
    a.add_argument("source"); a.add_argument("-o", "--sortie", default="reseau.html")
    a.add_argument("--titre"); a.add_argument("--niveaux", default=""); a.add_argument("--contenu", type=int, default=1)
    a.add_argument("--github", default=""); a.add_argument("--racine-depot", default=""); a.add_argument("--canvas")
    a.add_argument("--signature", default=""); a.add_argument("--max-items", type=int, default=60); a.add_argument("--largeur", type=int, default=230); a.add_argument("--grouper-par", default="", help="champ qui groupe les éléments d'une liste avant de les montrer (ex. modalite)"); a.add_argument("--type-par", default="", help="champ d'un élément JSON qui donne sa couleur (ex. modalite)")
    o = a.parse_args()
    niveaux = [x.strip() for x in o.niveaux.split(",") if x.strip()]
    N, types = [], []

    def typ(d, defaut):
        t = niveaux[d] if d < len(niveaux) else defaut
        if t not in types:
            types.append(t)
        return t

    def ajout(id, parent, label, t, resume="", info=None):
        N.append({"id": id, "parent": parent, "label": label, "type": t, "resume": resume, "info": info or {}})

    def json_enfants(v, pid, d, prof):
        if prof <= 0:
            return
        if isinstance(v, dict) and isinstance(v.get("fichiers"), dict):
            if len(v["fichiers"]) == 1:  # un lot d'un seul fichier : on montre directement son contenu
                return json_enfants(next(iter(v["fichiers"].values())), pid, d, prof)
            for i, (ch, cont) in enumerate(v["fichiers"].items()):
                cid = f"{pid}/f{i}"
                ajout(cid, pid, lisible(os.path.basename(ch)), typ(d, "Fichier inclus"), resume_json(cont),
                      {"chemin exact": ch, "contenu": resume_json(cont), "statut": (cont.get("_meta") or {}).get("statut", "") if isinstance(cont, dict) else ""})
                json_enfants(cont, cid, d + 1, prof - 1)
            return
        items, sing = [], None
        if isinstance(v, dict):
            for k in ("examens", "analyses", "entites", "elements", "lecons", "noeuds"):
                if isinstance(v.get(k), list):
                    items = v[k]; sing = {"examens": "Examen", "analyses": "Analyse", "elements": "Élément", "lecons": "Leçon", "noeuds": "Nœud", "entites": "Entité"}[k]; break
            else:
                for k, x in v.items():
                    if not k.startswith("_") and isinstance(x, (dict, list)):
                        cid = f"{pid}/{k}"
                        ajout(cid, pid, k, typ(d, "Clé"), resume_json(x), {"clé": k, "contenu": resume_json(x)})
                        json_enfants(x, cid, d + 1, prof - 1)
                return
        elif isinstance(v, list):
            items = v
        if o.grouper_par and items and all(isinstance(x, dict) and isinstance(x.get(o.grouper_par), str) for x in items):
            groupes = {}
            for x in items:
                groupes.setdefault(x[o.grouper_par], []).append(x)
            if len(groupes) > 1:
                for gi, (g, lst) in enumerate(groupes.items()):
                    if g not in types:
                        types.append(g)
                    gid = f"{pid}/g{gi}"
                    ajout(gid, pid, g, g, f"{len(lst)} {(sing or 'élément').lower()}{'s' if len(lst) > 1 else ''}", {o.grouper_par: g, "nombre": str(len(lst))})
                    for i, x in enumerate(lst[:o.max_items]):
                        inf = {k: (", ".join(map(str, y)) if isinstance(y, list) else str(y)) for k, y in x.items() if y not in (None, [], {}, "") and not isinstance(y, dict)}
                        ajout(f"{gid}/i{i}", gid, nom_item(x, i)[:90], g, "", dict(list(inf.items())[:8]))
                return
        for i, x in enumerate(items[:o.max_items]):
            inf = {k: (", ".join(map(str, y)) if isinstance(y, list) else str(y)) for k, y in (x.items() if isinstance(x, dict) else []) if y not in (None, [], {}, "") and not isinstance(y, dict)}
            t = x.get(o.type_par) if (o.type_par and isinstance(x, dict) and isinstance(x.get(o.type_par), str)) else None
            if t and t not in types:
                types.append(t)
            ajout(f"{pid}/i{i}", pid, nom_item(x, i)[:90], t or typ(99, sing or "Élément"), "", dict(list(inf.items())[:8]))
        if len(items) > o.max_items:
            ajout(f"{pid}/plus", pid, f"… {len(items) - o.max_items} autres", typ(d, "Élément"))

    src = os.path.abspath(o.source)
    racine_depot = os.path.abspath(o.racine_depot) if o.racine_depot else None

    def lien(p):
        if o.github and racine_depot:
            return o.github + os.path.relpath(p, racine_depot).replace(os.sep, "/")
        return ""

    def parcourir(p, pid, d):
        noms = sorted(os.listdir(p))
        for n in noms:
            q = os.path.join(p, n); cid = (pid + "/" + n)
            if os.path.isdir(q):
                nb = sum(len([f for f in fs if f.endswith(".json")]) for _, _, fs in os.walk(q))
                ajout(cid, pid, lisible(n), typ(d, "Dossier"), f"{nb} fichier{'s' if nb > 1 else ''} JSON", {"dossier": os.path.relpath(q, src), "fichiers JSON": str(nb), **({"GitHub": lien(q).replace("/blob/", "/tree/")} if lien(q) else {})})
                parcourir(q, cid, d + 1)
            elif n.endswith(".json"):
                try:
                    v = json.load(open(q, encoding="utf-8"))
                except Exception as e:
                    ajout(cid, pid, lisible(n), typ(d, "Fichier"), "illisible", {"erreur": str(e)}); continue
                lot = v.get("_lot", {}) if isinstance(v, dict) else {}
                info = {"fichier": os.path.relpath(q, src), "taille": f"{os.path.getsize(q) // 1024} Ko", "contenu": resume_json(v)}
                if lot:
                    info.update({"tâche": lot.get("tache", ""), "titre": lot.get("titre", ""), "signature": lot.get("signature", "")})
                if lien(q):
                    info["GitHub"] = lien(q)
                tf = "Lot" if lot else (niveaux[d] if d < len(niveaux) and niveaux[d] != "Lot" else "Fichier")
                if tf not in types:
                    types.append(tf)
                ajout(cid, pid, lisible(n), tf, resume_json(v), info)
                json_enfants(v, cid, d + 1, o.contenu)

    titre = o.titre or lisible(os.path.basename(src.rstrip("/")))
    if os.path.isdir(src):
        nb = sum(len([f for f in fs if f.endswith(".json")]) for _, _, fs in os.walk(src))
        ajout("R", None, titre, "Racine", f"{nb} fichier{'s' if nb > 1 else ''} JSON", {"dossier": src})
        types.insert(0, "Racine") if "Racine" not in types else None
        parcourir(src, "R", 0)
    else:
        v = json.load(open(src, encoding="utf-8"))
        ajout("R", None, titre, "Racine", resume_json(v), {"fichier": src}); types.insert(0, "Racine")
        json_enfants(v, "R", 0, o.contenu + 1)
    utilises = {n["type"] for n in N}
    types = [t for t in types if t in utilises]
    coul = {t: PALETTE[i % len(PALETTE)] for i, t in enumerate(types)}
    data = {"titre": titre, "couleurs": coul, "noeuds": N, "signature": o.signature, "largeur": o.largeur}
    g = open(os.path.join(ICI, "..", "assets", "reseau_donnees.html"), encoding="utf-8").read()
    open(o.sortie, "w", encoding="utf-8").write(g.replace("/*DONNEES*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
    if o.canvas:  # JSON Canvas 1.0, disposition en arbre simple
        prof = {"R": 0}; ys = {}; nodes = []; edges = []
        for n in N:
            d = 0 if not n["parent"] else prof[n["parent"]] + 1; prof[n["id"]] = d; ys[d] = ys.get(d, 0) + 1
            nodes.append({"id": n["id"], "type": "text", "text": f"**{n['label']}**\n{n['resume']}", "x": d * 320, "y": ys[d] * 90, "width": 260, "height": 70, "color": coul[n["type"]]})
            if n["parent"]:
                edges.append({"id": "e" + n["id"], "fromNode": n["parent"], "fromSide": "right", "toNode": n["id"], "toSide": "left", "toEnd": "arrow"})
        json.dump({"nodes": nodes, "edges": edges}, open(o.canvas, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(N)} nœuds, {len(types)} types → {o.sortie}" + (f" + {o.canvas}" if o.canvas else ""))


if __name__ == "__main__":
    main()
