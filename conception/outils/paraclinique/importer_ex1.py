#!/usr/bin/env python3
"""IMPORTER_EX1 — onglet Biologie du jeu Paraclinique (BRIEF_BIOLOGIE_CLAUDE_CODE.md § 4, étapes 2 et 3). Script 0 token.

1. Copie les 101 fiches EX-1-*.json du dépôt organigramme-examen-federal (Claude/_progression/donnees/examens/)
   dans conception/donnees/paraclinique/biologie/fiches/<n>_<matrice>/, SANS réécrire leur contenu :
   seuls s'ajoutent « _origine » (dépôt, chemin, commit) et, pour un bloc du gabarit absent, la valeur « à produire ».
2. Range chaque fiche par matrice d'après entree_primaire[0] (ordre fixé par le brief § 2).
3. Cartographie les trous (blocs vides, bloc Traitement absent, analyses de biologie/analyses/*.json sans fiche)
   dans projets/2_Jeux_Paraclinique/FILE_BIOLOGIE.json, avec un statut « à faire », « en cours » ou « fait » par fiche.

Non-perte : une fiche déjà importée n'est jamais écrasée ; le script vérifie seulement que chaque champ rempli de la
source y figure encore (sinon il s'arrête en code 1). Relance idempotente : 0 fiche écrite si rien n'a changé.
Usage : python3 conception/outils/paraclinique/importer_ex1.py [--source CHEMIN_DU_DEPOT_ORGANIGRAMME]
Signature : AAI (Anthropic AI)
"""
import argparse, glob, json, os, re, subprocess, sys, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(os.path.dirname(ICI))
RAC = os.path.dirname(RAC) if os.path.basename(RAC) == "conception" else RAC
BIO = os.path.join(RAC, "conception", "donnees", "paraclinique", "biologie")
FICHES = os.path.join(BIO, "fiches")
FILE = os.path.join(RAC, "projets", "2_Jeux_Paraclinique", "FILE_BIOLOGIE.json")
REL_SRC = "Claude/_progression/donnees/examens"

MATRICES = ["Sang et buvard", "Moelle", "Urines", "LCR", "Selles", "Sérosités et synovial", "Respiratoire et ORL",
            "Génital et fœto-maternel", "Salive, sueur, calculs, peau"]
# Rangement d'une fiche dont entree_primaire ne nomme aucune matrice de la liste fermée (décision tracée dans la fiche).
RANGEMENT_FORCE = {"EX-1-S2-prelevement-oculaire": ("Respiratoire et ORL",
                   "La liste fermée ne compte aucune matrice oculaire ; le frottis conjonctival se range avec les frottis de surface de la tête (S2).")}
# Huit blocs du gabarit (brief § 3) ; « sources » et « passerelles » forment le 8e bloc.
BLOCS = ["entete", "temps1_indications", "temps2_examen", "calculs", "temps3_interpretation", "traitement", "annexeA_pieges", "sources", "passerelles"]
AP = "à produire"


def slug(s):
    s = unicodedata.normalize("NFKD", s.replace("œ", "oe")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")


def dossier_matrice(m):
    return f"{MATRICES.index(m) + 1}_{slug(m)}"


def lire(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def ecrire(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    txt = json.dumps(obj, ensure_ascii=False, indent=1) + "\n"
    if os.path.exists(p) and open(p, encoding="utf-8").read() == txt:
        return False
    with open(p, "w", encoding="utf-8") as f:
        f.write(txt)
    return True


def vide(v):
    if v is None:
        return True
    if isinstance(v, str):
        return v.strip() in ("", "—", "-", AP)
    if isinstance(v, (list, dict)):
        return len(v) == 0 or all(vide(x) for x in (v.values() if isinstance(v, dict) else v))
    return False


def feuilles(v, chemin=""):
    """Toutes les valeurs remplies (chemin → texte) : base du contrôle de non-perte."""
    if isinstance(v, dict):
        for k, x in v.items():
            yield from feuilles(x, f"{chemin}.{k}" if chemin else k)
    elif isinstance(v, list):
        for i, x in enumerate(v):
            yield from feuilles(x, f"{chemin}[{i}]")
    elif not vide(v):
        yield chemin, v


def matrice_de(d):
    if d["id"] in RANGEMENT_FORCE:
        return RANGEMENT_FORCE[d["id"]]
    ep = d.get("entree_primaire") or []
    for m in ep:
        if m in MATRICES:
            return m, None
    raise SystemExit(f"Matrice inconnue pour {d['id']} : {ep}")


def trous(d):
    t = []
    for b in BLOCS:
        v = d.get(b)
        if b not in d:
            t.append({"bloc": b, "nature": "absent"})
        elif vide(v):
            t.append({"bloc": b, "nature": "vide ou à produire"})
        else:
            for ch, x in _cases_vides(v, b):
                t.append({"bloc": b, "nature": "« — » déclaré" if isinstance(x, str) and x.strip() == "—" else "case vide", "case": ch})
    return t


def _cases_vides(v, chemin):
    if isinstance(v, dict):
        for k, x in v.items():
            yield from _cases_vides(x, f"{chemin}.{k}")
    elif isinstance(v, list):
        for i, x in enumerate(v):
            yield from _cases_vides(x, f"{chemin}[{i}]")
    elif vide(v):
        yield chemin, v


def norm(s):
    s = unicodedata.normalize("NFKD", (s or "").replace("œ", "oe")).encode("ascii", "ignore").decode().lower()
    return " " + re.sub(r"[^a-z0-9]+", " ", s).strip() + " "


def texte_couverture(d):
    e = d.get("entete", {})
    parts = [d.get("titre", ""), e.get("nom_exact", ""), e.get("synonymes", "")]
    parts += [p.get("parametre", "") for p in d.get("temps2_examen", []) if isinstance(p, dict)]
    return norm(" ; ".join(parts))


def analyses_sans_fiche(fiches):
    couv = " | ".join(texte_couverture(d) for d in fiches)
    r = []
    for f in sorted(glob.glob(os.path.join(BIO, "analyses", "*.json"))):
        for a in lire(f)["analyses"]:
            noms = [a["nom"]] + (a.get("synonymes") or [])
            cles = [norm(re.sub(r"\s*\(.*?\)", "", n)) for n in noms]
            if not any(len(k.strip()) >= 3 and k in couv for k in cles):
                r.append({"id": a.get("id"), "nom": a["nom"], "fichier": os.path.basename(f), "prelevement": a.get("prelevement"),
                          "statut": "à faire"})
    return r


def statut(d, t):
    tr = d.get("traitement")
    if not t:
        return "fait"
    if tr and not vide(tr):
        return "en cours"
    return "à faire"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", default=os.environ.get("ORGANIGRAMME", os.path.join(os.path.dirname(RAC), "vialdjoukang-spec", "organigramme-examen-federal")))
    a = ap.parse_args()
    src = os.path.join(a.source, REL_SRC)
    fs = sorted(glob.glob(os.path.join(src, "EX-1-*.json")))
    if not fs:
        sys.exit(f"Aucune fiche EX-1 dans {src}")
    commit = subprocess.run(["git", "-C", a.source, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip() or "inconnu"
    ecrites, gardees, pertes, ids = 0, 0, [], {}
    for f in fs:
        d = lire(f)
        if d["id"] in ids:
            sys.exit(f"Identifiant dupliqué à la source : {d['id']}")
        m, raison = matrice_de(d)
        dest = os.path.join(FICHES, dossier_matrice(m), d["id"] + ".json")
        ids[d["id"]] = dest
        # non-perte : un import antérieur (éventuellement complété) n'est jamais écrasé
        anciens = glob.glob(os.path.join(FICHES, "*", d["id"] + ".json"))
        if anciens:
            cur = lire(anciens[0])
            for ch, val in feuilles(d):
                if ch.startswith("_"):
                    continue
                if dict(feuilles(cur)).get(ch) is None:
                    pertes.append(f"{d['id']} : {ch}")
            gardees += 1
            continue
        out = dict(d)
        for b in BLOCS:
            if b not in out:
                out[b] = AP
        out["_origine"] = {"depot": "vialdjoukang-spec/organigramme-examen-federal", "chemin": f"{REL_SRC}/{os.path.basename(f)}", "commit": commit}
        out["_matrice"] = m
        if raison:
            out["_matrice_raison"] = raison
        ecrites += ecrire(dest, out)
    if pertes:
        print("NON-PERTE ROUGE :", *pertes[:30], sep="\n  ")
        sys.exit(1)
    # cartographie des trous (sur l'état courant du dépôt, donc après complétion éventuelle)
    fiches = [lire(p) for p in sorted(glob.glob(os.path.join(FICHES, "*", "EX-1-*.json")))]
    lignes = []
    for d in sorted(fiches, key=lambda x: (MATRICES.index(x["_matrice"]), x["id"])):
        t = trous(d)
        lignes.append({"id": d["id"], "titre": d.get("titre"), "matrice": d["_matrice"], "systeme": d.get("systeme"),
                       "axe_secondaire": d.get("axe_secondaire"), "traitement_absent": vide(d.get("traitement")),
                       "trous": t, "statut": statut(d, t)})
    asf = analyses_sans_fiche(fiches)
    resume = {"fiches": len(lignes), "importees_depuis_source": len(fs),
              "par_matrice": {m: sum(1 for x in lignes if x["matrice"] == m) for m in MATRICES},
              "traitement_absent": sum(x["traitement_absent"] for x in lignes),
              "statuts": {s: sum(1 for x in lignes if x["statut"] == s) for s in ("à faire", "en cours", "fait")},
              "analyses_sans_fiche": len(asf)}
    ecrire(FILE, {"_meta": {"role": "File d'attente de l'onglet Biologie : trous par fiche et analyses sans fiche (BRIEF § 4.3).",
                            "producteur": "conception/outils/paraclinique/importer_ex1.py (0 token)", "source_commit": commit,
                            "statuts": "à faire = bloc Traitement absent ; en cours = Traitement commencé, trous restants ; fait = aucun trou"},
                  "resume": resume, "fiches": lignes, "analyses_sans_fiche": asf})
    print(f"importées : {ecrites} écrites, {gardees} déjà présentes (non écrasées) · source {commit[:10]}")
    print(json.dumps(resume, ensure_ascii=False))


if __name__ == "__main__":
    main()
