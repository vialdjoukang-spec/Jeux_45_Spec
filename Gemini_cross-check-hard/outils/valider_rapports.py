#!/usr/bin/env python3
"""Contrôle mécanique (0 token) des rapports déposés par Gemini : schéma, gravité, preuve, empreinte du lot.
Usage : python Gemini_cross-check-hard/outils/valider_rapports.py  → liste les rapports invalides et un tableau de synthèse."""
import glob, json, os, collections, hashlib, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); os.chdir(R)
G = "Gemini_cross-check-hard"
REQ = ["id", "gravite", "categorie", "fichier", "localisation", "texte_actuel", "probleme", "correction_proposee", "preuve", "confiance"]
ok = err = 0; grav = collections.Counter(); perime = []
for p in sorted(glob.glob(f"{G}/**/rapports/*.json", recursive=True)):
    try:
        r = json.load(open(p))
        assert all(k in r for k in ["lot", "auditeur", "date", "fichiers_audites", "verdict_lot", "constats"]), "champ racine manquant"
        for c in r["constats"]:
            assert all(k in c for k in REQ), f"{c.get('id')}: champ manquant"
            pr = c["preuve"]
            assert pr.get("lien") and pr.get("lu_le") and pr.get("extrait_court"), f"{c['id']}: preuve incomplète"
            assert len(pr["extrait_court"].split()) <= 25, f"{c['id']}: extrait trop long"
            grav[c["gravite"]] += 1
        for f in r["fichiers_audites"]:
            if os.path.isfile(f["chemin"]) and hashlib.sha256(open(f["chemin"], "rb").read()).hexdigest()[:16] != f["sha256"]:
                perime.append(p); break
        ok += 1
    except Exception as e:
        err += 1; print("INVALIDE", p, "→", e)
print(f"rapports valides {ok}, invalides {err}, périmés (source modifiée depuis) {len(perime)}")
print(dict(grav))
sys.exit(1 if err else 0)
