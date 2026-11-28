"""Justifie chaque cliché encore manquant et écrit le bilan dans FILE_IMAGERIE.json (clé « cliches »). 0 réseau.
Motifs, par ordre : organe génital externe exclu ; candidats rejetés au contrôle visuel ; aucune image libre pertinente trouvée
(requêtes Commons tracées dans lots/requetes_NN.json, candidats dans lots/candidats_NN.json) ; non encore cherché (limite de débit Wikimedia).
Normal manquant : aucun normal libre apparié (même modalité, plan, région) dans normaux.json ni dans l'atlas local.
Usage : python3 justifier_manques.py (après mesurer_cliches.py)   Signature : AAI (Anthropic AI)"""
import json, os, glob, re, datetime
ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
E = json.load(open(os.path.join(ICI, "ETAT_CLICHES.json"), encoding="utf-8"))
GEN = re.compile(r"penis_et_uretre|testicules_et_scrotum|vulve")
URETRE_ANT = re.compile(r"Rupture de l'urètre|Sténose de l'urètre")
REQ, CAND, CHOIX = {}, {}, {}
for f in glob.glob(os.path.join(ICI, "lots", "requetes_*.json")):
    REQ.update(json.load(open(f, encoding="utf-8")))
for f in glob.glob(os.path.join(ICI, "lots", "candidats_*.json")):
    CAND.update(json.load(open(f, encoding="utf-8")))
for f in glob.glob(os.path.join(ICI, "lots", "choix_*.json")):
    CHOIX.update(json.load(open(f, encoding="utf-8")))
REJ = json.load(open(os.path.join(ICI, "REJETS.json"), encoding="utf-8")) if os.path.exists(os.path.join(ICI, "REJETS.json")) else {}
manques = []
for u in E["unites"]:
    if u["etat"] == "complet":
        continue
    k = f"{u['organe']} | {u['pathologie']} | {u['modalite'] if u['modalite'] != 'Scanner' else 'Scanner'}"
    if u["etat"] == "normal manquant":
        motif = "Aucun cliché normal libre apparié (même modalité, même plan, même région) trouvé à ce jour dans normaux.json ni dans l'atlas local."
    elif GEN.search(u["organe"]) or (u["organe"] == "vessie_et_uretre" and URETRE_ANT.search(u["pathologie"])):
        motif = "Exclu par règle : organes génitaux externes (l'urétrographie de l'urètre antérieur montre la verge)."
    elif k in REQ and k in CAND:
        rj = [c["titre"] for c in CAND[k] if c.get("page") in REJ]
        if k in CHOIX and CHOIX[k].get("c") is not None:
            motif = "Candidat choisi non encore téléchargé (fichier Wikimedia étranglé : Retry-After 600 s) ; reprise au passage suivant."
        elif rj:
            motif = "Candidats rejetés au contrôle visuel : " + "; ".join(rj[:2]) + "."
        else:
            n = len(CAND[k])
            motif = (f"Aucune image libre pertinente : {n} candidat(s) Commons écarté(s) à la lecture (hors sujet, autre modalité ou autre région) ; requêtes : "
                     if n else "Aucune image libre trouvée sur Wikimedia Commons ; requêtes : ") + " ; ".join(REQ[k]["q"]) + "."
    else:
        motif = "Non encore cherché : la limite de débit de Wikimedia (≈ 1 requête/50 s, 429) a borné la session ; la requête est prête dans CIBLES.tsv."
    manques.append({"organe": u["organe"], "pathologie": u["pathologie"], "modalite": u["modalite"], "manque": u["etat"], "motif": motif})
fi = os.path.join(RAC, "projets", "2_Jeux_Paraclinique", "FILE_IMAGERIE.json"); F = json.load(open(fi, encoding="utf-8"))
F["cliches"] = {"_role": "Bilan des clichés de la fenêtre à deux clichés (couloir 3) : chaque manque porte son motif.", "mesure_le": datetime.date.today().isoformat(),
                "unites": E["unites_organe_pathologie_modalite"], "noeuds": E["noeuds_pathologie"],
                "outils": "projets/2_Jeux_Paraclinique/imagerie_cliches/ (mesurer_cliches.py, outil_cliches.py, justifier_manques.py)",
                "motifs": {m: sum(1 for x in manques if x["motif"].startswith(m)) for m in ("Exclu par règle", "Candidats rejetés", "Aucune image libre", "Aucun cliché normal", "Non encore cherché", "Candidat choisi")},
                "manques": manques}
json.dump(F, open(fi, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(F["cliches"]["motifs"], ensure_ascii=False))
