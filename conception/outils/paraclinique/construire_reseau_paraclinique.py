"""Réseau paraclinique complet (0 token) : 9 régions → organes → modalités → examens, sur le corps 3D réel.
Lit conception/donnees/paraclinique/topographie/<région>/<organe>.json et écrit conception/prototypes/moteur/paraclinique_complet.json.
Chaque examen porte son infobulle (ce que c'est, pourquoi, confusion, à retenir) puis sa fiche d'examen (signe, seuil, discriminant…).
Le prototype paraclinique.json (fenêtre à deux clichés) reste intact. Signature : AAI (Anthropic AI)"""
import glob, json, os, re

ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
TOPO = os.path.join(RAC, "conception", "donnees", "paraclinique", "topographie")
SORTIE = os.path.join(RAC, "conception", "prototypes", "moteur", "paraclinique_complet.json")
REG = {"1_tete_et_encephale": ("Tête et encéphale", "cerveau", "g", "#8e5cc4"), "2_cou": ("Cou", "trachee", "d", "#2a9d8f"),
       "3_rachis_moelle_et_racines": ("Rachis, moelle et racines", "rachis", "g", "#7a6a4f"), "4_thorax": ("Thorax", "poumon_d", "d", "#3d7fd6"),
       "5_abdomen": ("Abdomen", "foie", "g", "#c98a2b"), "6_pelvis": ("Pelvis", "vessie", "d", "#b5527a"),
       "7_membres_et_appareil_locomoteur": ("Membres et appareil locomoteur", "femur", "g", "#5f7f3a"),
       "8_peau_et_phaneres": ("Peau et phanères", "humerus", "d", "#c0623b"), "9_systemes_transversaux": ("Systèmes transversaux", "coeur", "g", "#6b7280")}
MOD = {"Imagerie": "IMG", "Biologie": "BIO", "Exploration fonctionnelle": "FCT", "Endoscopie": "END", "Anatomopathologie / biopsie": "HIS"}
cle = lambda s: re.sub(r"[^a-z0-9]+", "_", s.lower())[:40].strip("_")


def court(t, n=45):
    t = re.sub(r"\s*\(.*?\)", "", t).strip()
    return t if len(t) <= n else t[: n - 1].rsplit(" ", 1)[0] + "…"


N = []
for rd in sorted(os.listdir(TOPO)):
    if rd not in REG:
        continue
    nom, org, cote, coul = REG[rd]; rid = "pr_" + rd.split("_")[0]
    fichiers = sorted(glob.glob(os.path.join(TOPO, rd, "*.json")))
    N.append({"id": rid, "nature": "Région", "type": "", "texte": nom, "organe": org, "cote": cote, "couleur": coul, "rubriques": "region",
              "bulle": {"def": f"La région « {nom} » regroupe {len(fichiers)} organes ou systèmes explorables.",
                        "retenir": "Tu cliques un organe, puis une modalité, puis l'examen dont tu veux la fiche."}})
    for f in fichiers:
        d = json.load(open(f, encoding="utf-8")); on = d["_meta"]["organe"]; oid = f"{rid}_{cle(on)}"
        ex = d.get("examens", [])
        N.append({"id": oid, "nature": "Organe", "type": "", "texte": court(on), "de": [rid], "couleur": coul, "rubriques": "region",
                  "bulle": {"def": f"{on} s'explore par {len(ex)} examens répartis en {len({e['modalite'] for e in ex})} modalités.",
                            "retenir": "Tu choisis la modalité selon la question clinique, puis l'examen le plus discriminant et le plus économe."}})
        for m in [m for m in MOD if any(e["modalite"] == m for e in ex)]:
            mid = f"{oid}_{MOD[m].lower()}"; liste = [e for e in ex if e["modalite"] == m]
            N.append({"id": mid, "nature": "Modalité", "type": "", "texte": m, "de": [oid], "couleur": coul, "rubriques": "region",
                      "bulle": {"def": f"{len(liste)} examen(s) de {m.lower()} pour {on.lower()}.", "retenir": "Chaque examen porte son signe recherché, son seuil et ce qui le fait préférer."}})
            for e in liste:
                b = e.get("bulle") or {}
                vide = not e.get("discriminant")
                N.append({"id": "px_" + e["id"][:70], "nature": "Examen", "type": "Examen · à compléter" if vide else "Examen · " + ", ".join(e.get("visees") or [])[:40],
                          "texte": court(e["nom"]), "de": [mid], "couleur": "#9aa2b4" if vide else coul, "rubriques": "examen",
                          "bulle": {k: v for k, v in {"def": b.get("def") or e["nom"] + " reste à compléter.", "pourquoi": b.get("pourquoi") or "", "confusion": b.get("confusion") or "",
                                    "retenir": b.get("retenir") or "", "signe": e.get("signeRecherche") or "", "seuil": e.get("seuil") or "",
                                    "discriminant": e.get("discriminant") or "", "avantage": e.get("avantageSelectif") or "", "plutot": e.get("plutotQue") or "",
                                    "limite": e.get("limite") or "", "smarter": e.get("smarterMedicine") or ""}.items() if v}})
base = json.load(open(os.path.join(os.path.dirname(SORTIE), "paraclinique.json"), encoding="utf-8"))
conf = {k: base[k] for k in ("theme", "voile", "opacitePeau", "cible", "dist", "fov", "largeurColonne", "ecartColonne") if k in base}
conf.update({"titre": "Paraclinique — tous les examens, de la tête aux pieds", "sousTitre": "Région → organe → modalité → examen ; infobulle : signe recherché, seuil, pourquoi lui",
             "rubriques": {"region": [["def", "Ce que c'est"], ["retenir", "Comment avancer"]],
                           "examen": [["def", "Ce que c'est"], ["signe", "Signe recherché"], ["seuil", "Seuil"], ["discriminant", "Pourquoi lui"], ["avantage", "Avantage sélectif"],
                                      ["plutot", "Plutôt que"], ["limite", "Limite"], ["confusion", "Confusion possible"], ["smarter", "Smarter Medicine"], ["retenir", "À retenir"]]},
             "noeuds": N})
json.dump(conf, open(SORTIE, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
nx = sum(1 for n in N if n["nature"] == "Examen")
print(f"réseau paraclinique : {sum(1 for n in N if n['nature']=='Organe')} organes, {nx} examens, {sum(1 for n in N if n['type']=='Examen · à compléter')} à compléter → {os.path.relpath(SORTIE, RAC)}")
