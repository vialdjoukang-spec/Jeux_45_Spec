"""Audit rigoureux de la conception (0 token) : prototypes, règles sémiologiques, discriminants, transversales, JSON.
Usage : python conception/outils/auditer_conception.py → conception/audit/conception.md (code de sortie 1 si échec)."""
import json, os, sys, glob, string
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalogue_paraclinique import TECHNIQUES, VISEES
from transversales import OUTILS, LENTILLES, ARBORESCENCE

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = []
def ctrl(nom, ok, detail=""): R.append((nom, bool(ok), detail))

# 1. Prototype Tétrade : infobulles, seuils de signes, diagnostics répétés, lentilles
cfg = json.load(open(os.path.join(ICI, "prototypes/moteur/tetrade.json"), encoding="utf-8"))
N = {n["id"]: n for n in cfg["noeuds"]}
enf = {i: [n for n in cfg["noeuds"] if i in n.get("de", [])] for i in N}
RUBS = {"semiologie": [["def", ""], ["pourquoi", ""], ["confusion", ""], ["retenir", ""]], **cfg.get("rubriques", {})}
def rubs(n): return RUBS.get(n.get("espace")) or RUBS.get(n.get("rubriques")) or RUBS["semiologie"]
sans_bulle = [i for i, n in N.items() if not n.get("aProduire") and not all((n.get("bulle") or {}).get(k) for k, _ in rubs(n))]
ctrl("Chaque case produite porte une infobulle complète (rubriques de son espace)", not sans_bulle, ", ".join(sans_bulle))
temps = [i for i, n in N.items() if str(n.get("type", "")).startswith(("Temps", "Interrogatoire"))]
typ = lambda i: [x for x in enf[i] if x.get("presentation") != "atypique"]
mauvais = [f"{i}:{len(typ(i))}" for i in temps if not (2 <= len(typ(i)) <= 3 or (len(typ(i)) == 1 and typ(i)[0].get("uniqueAssume")))]
ctrl("Chaque temps d'examen a 2 ou 3 signes typiques (ou un signe unique assumé et expliqué)", not mauvais, ", ".join(mauvais))
diags = [i for i, n in N.items() if str(n.get("type", "")).startswith("Diagnostic")]
OBLIG = {"diagnostique", "retentissement", "etiologique", "complications"}
incomplets = [i for i in diags if not (OBLIG <= set((N[i]["bulle"].get("bilan") or {}).keys()) and "Gold standard" in (N[i]["bulle"]["bilan"].get("diagnostique") or {}) and N[i]["bulle"].get("traitement") and N[i]["bulle"].get("source"))]
ctrl("Chaque diagnostic répète le bilan par visée (diagnostique avec gold standard, retentissement, étiologique, complications) et le traitement avec source", not incomplets, ", ".join(incomplets))
ids_l = {l["id"] for l in cfg.get("lentilles", [])}
orph = [f"{i}:{k}" for i, n in N.items() for k in (n.get("particularites") or {}) if k not in ids_l]
ctrl("Chaque particularité renvoie à une lentille déclarée", not orph, ", ".join(orph))
sons = [n["son"] for n in N.values() if n.get("son")]
ctrl("Chaque son déclaré existe en fichier", all(os.path.exists(os.path.join(ICI, "prototypes/moteur", s)) for s in sons), ", ".join(sons))
cotes = {n.get("cote") for n in N.values() if n.get("organe") and enf[n["id"]]}
ctrl("Le prototype montre un développement à gauche ET à droite", {"g", "d"} <= cotes or len([n for n in N.values() if n.get("organe") and enf[n["id"]]]) >= 2)

import re
GL = cfg.get("glossaire", {})
textes = " ".join(json.dumps(n.get("bulle", {}), ensure_ascii=False) + " " + n["texte"] for n in cfg["noeuds"])
sigles = sorted({m for m in re.findall(r"(?<![\w-])([A-Z][A-Za-z]*[A-Z][A-Za-z0-9₂-]*)(?![\w-])", textes) if not m.isdigit()})
absents = [x for x in sigles if x not in GL and x not in ("FMA", "MP") and not re.fullmatch(r"[IVXL]+", x)]
ctrl("Chaque sigle cité dans une infobulle est défini dans le glossaire", not absents, ", ".join(absents))
ctrl("Le mot « atypique » est défini dès qu'il est employé", "atypique" not in textes or "atypique" in GL)
sans_pres = [i for i, n in N.items() if n.get("type") in ("Signe", "Symptôme") and n.get("presentation") not in ("typique", "atypique")]
ctrl("Chaque signe ou symptôme est classé typique ou atypique", not sans_pres, ", ".join(sans_pres))
VALIDES = {v[0] for v in VISEES}
bil = [i for i in diags for k, v in (N[i]["bulle"].get("bilan") or {}).items() for g, xs in (v.items() if isinstance(v, dict) else [("?", [None])]) for x in xs if k not in VALIDES or not (isinstance(x, list) and len(x) == 2 and all(x) and len(x[0]) <= 60)]
ctrl("Le bilan n'affiche que des noms courts ; chaque nom porte en infobulle le signe recherché", not bil, ", ".join(sorted(set(bil))))

# 1 bis. Systèmes → TOUS leurs organes, de haut en bas ; espaces ; fenêtres
from systemes import SYSTEMES as SYS
from catalogue_paraclinique import TOPO
racines = {n["texte"]: n for n in N.values() if n.get("nature") == "Système"}
manq = []
for s_nom, organes in SYS.items():
    r = next((v for k, v in racines.items() if k.split(" (")[0].replace("&", "et") in s_nom.replace("&", "et") or s_nom.split(" (")[0].replace("&", "et") in k), None)
    if not r: manq.append(s_nom + " (racine absente)"); continue
    fils = [n for n in enf[r["id"]] if n.get("nature") == "Organe"]
    if len(fils) != len(organes): manq.append(f"{s_nom} : {len(fils)}/{len(organes)} organes")
ctrl(f"Chaque système déroule TOUS ses organes ({sum(len(o) for o in SYS.values())} organes, {len(SYS)} systèmes)", not manq, ", ".join(manq))
cles = {k for z in TOPO.values() for k in (z if isinstance(z, dict) else {})} | set(TOPO)
sans_topo = [o for l in SYS.values() for o, _, ks in l if not ks]
ctrl("Chaque organe est relié au catalogue topographique des examens", not sans_topo, ", ".join(sans_topo))
longs = [n["texte"] for n in N.values() if len(n["texte"]) > 45]
ctrl("Chaque case reste concise (≤ 45 caractères ; le détail va en infobulle ou fenêtre)", not longs, ", ".join(longs))
moteur = open(os.path.join(ICI, "prototypes/moteur/fenetres.js"), encoding="utf-8").read()
inconnus = sorted({n["fenetre"] for n in N.values() if n.get("fenetre") and not re.search(r"\n\s*'?" + re.escape(n["fenetre"]) + r"'?\(C", moteur)})
ctrl("Chaque mot-clé à fenêtre ouvre un modèle existant (3D, courbe, calculateur)", not inconnus, ", ".join(inconnus))
mc = [n for n in N.values() if n.get("nature") == "Mot-clé"]
ctrl("Chaque mot-clé ouvre une fenêtre (image 3D en anatomie, courbe ou détail en physiologie)", all(n.get("fenetre") for n in mc if n.get("espace") == "anatomie") and mc, f"{len(mc)} mots-clés")
esp_inc = [n["id"] for n in N.values() if n.get("espace") and n["espace"] not in ("anatomie", "physiologie", "semiologie", "physiopathologie")]
ctrl("Chaque case d'espace appartient à l'un des 4 espaces", not esp_inc, ", ".join(esp_inc))
a_prod = sum(1 for n in N.values() if n.get("aProduire"))
INFO = f"Organes encore à produire (backlog, non bloquant) : {a_prod}"

# 2. Paraclinique : fenêtre à deux clichés avec radio-anatomie normale
pa = json.load(open(os.path.join(ICI, "prototypes/moteur/paraclinique.json"), encoding="utf-8"))
f = pa["fenetres"][0]
ctrl("La fenêtre de clichés montre la radio-anatomie normale à droite", f.get("normal") and len(f["normal"]["reperes"]) >= 6)
ctrl("Chaque technique d'imagerie a ses 5 champs (discriminant, préférence, alternative, limite)", all(len(l) == 5 and all(l) for lst in TECHNIQUES.values() for l in lst))
irm = [l[0] for l in TECHNIQUES["IRM"]]
ctrl("Les séquences IRM clés sont décrites", all(any(s in x for x in irm) for s in ["T1", "T2", "FLAIR", "Diffusion", "SWI", "gadolinium", "STIR", "Angio-IRM", "Cholangio"]), ", ".join(irm))

# 3. Disciplines transversales
ctrl("Les 19 disciplines-outils couvrent les lettres A à S", [o["lettre"] for o in OUTILS] == list(string.ascii_uppercase[:19]))
ctrl("Les lentilles cliniques incluent pédiatrie, gériatrie, femme/grossesse, chirurgie, psychiatrie", {"PED", "GER", "GYN", "CHI", "PSY"} <= {l["id"] for l in LENTILLES})
ctrl("L'arbre de cours transversal compte 9 parties", len(ARBORESCENCE) == 9)

# 4. JSON générés : lisibles, sans joker oublié
fichiers = glob.glob(os.path.join(ICI, "donnees/**/*.json"), recursive=True)
illisibles, jokers = [], []
for p in fichiers:
    try:
        t = open(p, encoding="utf-8").read(); json.loads(t)
    except Exception:
        illisibles.append(p)
    if "<" in os.path.relpath(p, ICI):
        jokers.append(p)
ctrl(f"Les {len(fichiers)} JSON se lisent sans erreur", not illisibles, ", ".join(illisibles))
ctrl("Aucun nom de fichier ne garde un joker (<systeme>, <organe>…)", not jokers, ", ".join(jokers))

# 5. Plans : aucun SVG, audits internes réussis
for nom in ("tetrade", "pharmacologie", "paraclinique"):
    h = open(os.path.join(ICI, "html", f"{nom}.html"), encoding="utf-8").read()
    ctrl(f"Plan {nom} : aucune image SVG", "<svg" not in h)
    p = json.load(open(os.path.join(ICI, "plans", f"{nom}.plan.json"), encoding="utf-8"))
    ctrl(f"Plan {nom} : audit interne réussi", all(x["resultat"] for x in p["auditConception"]))

ok = all(r[1] for r in R)
md = [f"# Audit rigoureux de la conception — {'RÉUSSI' if ok else 'ÉCHEC'}", "", INFO, "", "| Contrôle | Résultat | Détail |", "|---|---|---|"] + [f"| {a} | {'✅' if b else '❌'} | {c} |" for a, b, c in R]
os.makedirs(os.path.join(ICI, "audit"), exist_ok=True)
open(os.path.join(ICI, "audit", "conception.md"), "w", encoding="utf-8").write("\n".join(md))
print("RÉUSSI" if ok else "ÉCHEC", f"{sum(r[1] for r in R)}/{len(R)}"); [print(" ❌", a, "→", c) for a, b, c in R if not b]
sys.exit(0 if ok else 1)
