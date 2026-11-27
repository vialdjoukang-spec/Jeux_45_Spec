#!/usr/bin/env python3
"""GENERER_ECRAN — prépare, sans token, les documents de l'écran temps réel (artefact « Data » + base partagée).

Entrées : un registre JSON tenu par l'orchestrateur (jauges, agents) et l'historique git de la branche de travail.
Sortie : un dossier de documents JSON + writes.json, la liste exacte des écritures à passer à
ArtifactData action="batch" (≤ 50 par appel ; le script découpe en lots writes_1.json, writes_2.json…).

Usage :
  python3 generer_ecran.py --registre REG.json --depuis <commit de départ> --sortie DOSSIER [--page ecran_modele.html]
Registre : {"titre": "...", "jauges": [{"id","quoi","fait","cible","poids","regle"}],
            "agents": [{"id","nom","perimetre","statut": "a_faire|en_cours|termine","produit"}],
            "matrices": [{"id","matrice","fiches","vertes","traitement","completes"}]   (facultatif)}
--page n'est passé qu'au premier envoi (ou quand la page change) : les données seules suffisent ensuite.
Signature : AAI (Anthropic AI)
"""
import argparse, json, os, subprocess

ap = argparse.ArgumentParser()
ap.add_argument("--registre", required=True); ap.add_argument("--depuis", required=True)
ap.add_argument("--sortie", required=True); ap.add_argument("--page")
a = ap.parse_args()
R = json.load(open(a.registre, encoding="utf-8"))
D = os.path.join(a.sortie, "docs"); os.makedirs(D, exist_ok=True)
W = []


def doc(col, did, data):
    p = os.path.join(D, f"{col.replace('/', '_')}__{did}.json")
    json.dump(data, open(p, "w", encoding="utf-8"), ensure_ascii=False)
    W.append({"op": "set", "collection": col, "doc_id": did, "file_path": os.path.abspath(p)})


if a.page:
    doc("dash", "meta", {"title": R.get("titre", "Écran temps réel"), "lang": "fr"})
    for k, ti, de in (("jauges", "Jauges", "Ce qui est fait sur la cible de chaque critère."),
                      ("agents", "Agents", "Chaque agent, son périmètre, son statut et ce qu'il a produit."),
                      ("flux", "Circulation des fichiers", "Chaque commit de la branche : heure, auteur, cible, fichiers."),
                      ("matrices", "Unités de travail", "Avancement par unité (matrice, lot, système).")):
        doc("datasets", k, {"title": ti, "description": de, "source": {"kind": "store", "path": f"data/live/{k}"}})
    doc("files", "index.html", {"text": open(a.page, encoding="utf-8").read()})
for i, j in enumerate(R.get("jauges", [])):
    doc("data/live/jauges", j["id"], {"ordre": i, **{k: j[k] for k in ("quoi", "fait", "cible", "poids", "regle")}})
for i, g in enumerate(R.get("agents", [])):
    doc("data/live/agents", g["id"], {"ordre": i, **{k: g[k] for k in ("nom", "perimetre", "statut", "produit")}})
for i, m in enumerate(R.get("matrices", [])):
    doc("data/live/matrices", m["id"], {"ordre": i, **{k: v for k, v in m.items() if k != "id"}})
log = subprocess.run(["git", "log", "--reverse", "--format=%h|%cd|%an|%s", "--date=format:%H:%M", f"{a.depuis}..HEAD"],
                     capture_output=True, text=True).stdout.splitlines()
for i, l in enumerate(log):
    h, heure, auteur, sujet = l.split("|", 3)
    st = subprocess.run(["git", "show", "--stat", "--format=", h], capture_output=True, text=True).stdout.strip().splitlines()
    n = int(st[-1].split()[0]) if st else 0
    agent = sujet.split("·")[1].split(":")[0].strip() if "·" in sujet else "Orchestrateur"
    doc("data/live/flux", f"{i:03d}", {"ordre": i, "heure": heure, "agent": agent, "cible": sujet.split(":")[0][:60],
                                       "fichiers": n, "commit": h, "quoi": sujet[:220]})
for k in range(0, len(W), 50):
    json.dump(W[k:k + 50], open(os.path.join(a.sortie, f"writes_{k // 50 + 1}.json"), "w"), ensure_ascii=False)
print(f"{len(W)} écritures en {-(-len(W) // 50)} lot(s) : {a.sortie}/writes_*.json")
