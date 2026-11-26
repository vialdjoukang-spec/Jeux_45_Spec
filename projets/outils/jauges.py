"""Jauges « jouable » des 4 jeux, mesurées dans le dépôt (0 token). Écrit projets/jauges.json (avec historique) et projets/JAUGES.md.
« Jouable » : l'apprenant ouvre le jeu, joue une partie complète avec score, et apprend de la correction, sans contenu vide.
Chaque jauge est une moyenne pondérée de critères mesurables ; les poids sont écrits ci-dessous. Signature : AAI (Anthropic AI)"""
import datetime as dt, glob, json, os, re, sys

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); os.chdir(R)
J = lambda p: json.load(open(p, encoding="utf-8"))


def lire_tout(motif):
    for f in glob.glob(motif, recursive=True):
        try:
            yield f, J(f)
        except Exception:
            pass


def jeu(nom, criteres):
    total = sum(p for _, _, _, p in criteres)
    return {"nom": nom, "pct": round(100 * sum(min(1, v / c) * p for _, v, c, p in criteres if c) / total),
            "criteres": [{"quoi": q, "fait": v, "cible": c, "poids": p} for q, v, c, p in criteres]}


# 1. Tétrade
red = len(re.findall(r'^\s+"[^"]+": \{"dossier"', open("conception/outils/systemes_rediges.py", encoding="utf-8").read(), re.M))
interp = J("conception/prototypes/moteur/interpretations.json"); n_int = sum(len(v) for k, v in interp.items() if k != "_meta" and isinstance(v, dict))
# Organes 3D : on ne compte que les .glb réellement servis sur le site publié (manifeste écrit par .github/workflows/site.yml),
# et non les entrées d'index.json, car les .glb sont exclus de git et n'existent que dans le site déployé.
SERVIS = "projets/organes_servis.json"
o3d = len({x["organe"] for x in J(SERVIS)["fichiers"] if x.get("organe")}) if os.path.exists(SERVIS) else 0
IDX = J("conception/prototypes/moteur/arenes/index.json") if os.path.exists("conception/prototypes/moteur/arenes/index.json") else []
moteur = os.path.exists("conception/prototypes/moteur/arene.html")
paquet = lambda pre: sum(x["n"] for x in IDX if x["paquet"].startswith(pre)) if moteur else 0   # questions jouables dans l'arène commune
# Les 9 processus (immunité innée, adaptative, complément, barrières, 5 processus pédiatriques) ne sont pas des objets : décision de Vial du
# 26.11.2026, on ne leur invente pas d'objet 3D, donc ils sortent de la cible « 3D réelle » (124 organes - 9 processus = 115 objets).
T = jeu("Tétrade Fondation", [("systèmes rédigés", red, 14, 45), ("interprétations de courbes", n_int, 119, 10), ("organes en 3D réelle (hors 9 processus)", o3d, 115, 15), ("questions et puzzles jouables dans l'arène", paquet("tetrade"), 100, 30)])

# 2. Paraclinique
ex = [e for _, d in lire_tout("conception/donnees/paraclinique/topographie/*/*.json") for e in d.get("examens", [])]
rempli = sum(1 for e in ex if e.get("discriminant") and e.get("seuil"))
ent = cli = 0
for _, d in lire_tout("conception/donnees/images/paraclinique/**/*.json"):
    so = d.get("sansObjet") or {}; ent += len(so); cli += len(so)
    for c in (d.get("cliches") or {}).values() if isinstance(d.get("cliches"), dict) else d.get("cliches") or []:
        ent += 1; cli += bool(c.get("candidats") if isinstance(c, dict) else c)
cas = len(glob.glob("conception/donnees/paraclinique/cas/**/*.json", recursive=True))
P = jeu("Paraclinique", [("examens complets", rempli, max(len(ex), 1), 30), ("entités avec cliché", cli, max(ent, 1), 15),
                         ("réseau complet sur le corps 3D", int(os.path.exists("conception/prototypes/moteur/paraclinique_complet.json")), 1, 20),
                         ("cas de l'arène « le bon examen »", cas, 20, 20), ("paquet jouable dans l'arène", int(paquet("paraclinique") > 0), 1, 15)])

# 3. Transversal
lec = [d for _, d in lire_tout("conception/donnees/tetrade/transversales/lecons/**/*.json")]
ok = sum(1 for d in lec if d.get("parties") and all(d["parties"].values()))
qcm = sum(1 for d in lec if any(i.get("enonce") for i in d.get("items") or []))
X = jeu("Transversal", [("structure A → S et lentilles", 1, 1, 10), ("leçons rédigées", ok, 228, 55), ("leçons avec QCM", qcm, 228, 20), ("paquet jouable dans l'arène", int(paquet("transversal") > 0), 1, 15)])

# 4. 45 Spec
fi = [d for f, d in lire_tout("content/fiches/**/*.json") if "_archives" not in f]
ok45 = sum(1 for d in fi if (d.get("audit") or {}).get("rejector") == "pass")
pec = sum(1 for d in fi if d.get("priseEnCharge"))
items = len({os.path.dirname(f) for f in glob.glob("content/items/**/*.json", recursive=True)})
items += len(glob.glob("content/questions/*/*.json"))   # pipeline notions → questions → correction (une entité = un fichier)
_rr = J("content/pathologies/RANG_RENDEMENT.json")["_meta"]["groupes"]
faits45 = sum(g["faits"] for g in _rr.values()); total45 = sum(g["total"] for g in _rr.values())
qcm45 = 0
for _f in glob.glob("content/questions/*/*.json"):
    _d = J(_f); qcm45 += len(_d.get("questions", _d) if isinstance(_d, dict) else _d)
# 45 Spec : on mesure le contenu réellement jouable (pathologies traitées, QCM dans l'arène), aligné sur RANG_RENDEMENT.
S = jeu("45 Spec", [("pathologies traitées (groupes A à D)", faits45, total45, 70),
                    ("QCM jouables dans l'arène (20 par pathologie)", qcm45, total45 * 20, 30)])

maint = dt.datetime.now(dt.timezone(dt.timedelta(hours=1))).strftime("%d.%m.%Y %H:%M")
jeux = [T, P, X, S]; etat = J("projets/jauges.json") if os.path.exists("projets/jauges.json") else {"historique": []}
avant = etat["historique"][-1]["pct"] if etat["historique"] else None
if avant != [j["pct"] for j in jeux] or "--force" in sys.argv:
    etat["historique"] = (etat["historique"] + [{"date": maint, "pct": [j["pct"] for j in jeux]}])[-300:]
etat.update({"maj": maint, "jeux": jeux}); json.dump(etat, open("projets/jauges.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
barre = lambda p: "█" * (p // 5) + "░" * (20 - p // 5)
md = [f"# Jauges « jouable » des 4 jeux\n\nMesure automatique du dépôt, mise à jour toutes les 5 minutes environ. Dernière mesure : **{maint}**.\n"]
for j, a in zip(jeux, (etat["historique"][-2]["pct"] if len(etat["historique"]) > 1 else [None] * 4)):
    d = "" if a is None or a == j["pct"] else f" ({'+' if j['pct'] > a else ''}{j['pct'] - a})"
    md.append(f"## {j['nom']} — {j['pct']} %{d}\n\n`{barre(j['pct'])}`\n\n| Critère | Fait | Cible | Poids |\n|---|---:|---:|---:|")
    md += [f"| {c['quoi']} | {c['fait']} | {c['cible']} | {c['poids']} |" for c in j["criteres"]]; md.append("")
md.append("## Historique\n\n| Date | Tétrade | Paraclinique | Transversal | 45 Spec |\n|---|---:|---:|---:|---:|")
md += [f"| {h['date']} | " + " | ".join(f"{p} %" for p in h["pct"]) + " |" for h in reversed(etat["historique"][-20:])]
open("projets/JAUGES.md", "w", encoding="utf-8").write("\n".join(md) + "\n\nSignature : AAI (Anthropic AI)\n")
print(" · ".join(f"{j['nom']} {j['pct']} %" for j in jeux))
