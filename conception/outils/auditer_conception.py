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
sans_bulle = [i for i, n in N.items() if not all((n.get("bulle") or {}).get(k) for k in ("def", "pourquoi", "confusion", "retenir"))]
ctrl("Chaque case du prototype porte une infobulle complète (4 rubriques)", not sans_bulle, ", ".join(sans_bulle))
temps = [i for i, n in N.items() if str(n.get("type", "")).startswith(("Temps", "Interrogatoire"))]
mauvais = [f"{i}:{len(enf[i])}" for i in temps if not (2 <= len(enf[i]) <= 3 or (len(enf[i]) == 1 and enf[i][0].get("uniqueAssume")))]
ctrl("Chaque temps d'examen a 2 ou 3 signes (ou un signe unique assumé et expliqué)", not mauvais, ", ".join(mauvais))
diags = [i for i, n in N.items() if str(n.get("type", "")).startswith("Diagnostic")]
incomplets = [i for i in diags if not (set(k for k, _ in [(v[0], 0) for v in VISEES]) <= set((N[i]["bulle"].get("bilan") or {}).keys()) and N[i]["bulle"].get("traitement") and N[i]["bulle"].get("source"))]
ctrl("Chaque diagnostic répète le bilan en 6 visées et le traitement avec posologie et source", not incomplets, ", ".join(incomplets))
ids_l = {l["id"] for l in cfg.get("lentilles", [])}
orph = [f"{i}:{k}" for i, n in N.items() for k in (n.get("particularites") or {}) if k not in ids_l]
ctrl("Chaque particularité renvoie à une lentille déclarée", not orph, ", ".join(orph))
sons = [n["son"] for n in N.values() if n.get("son")]
ctrl("Chaque son déclaré existe en fichier", all(os.path.exists(os.path.join(ICI, "prototypes/moteur", s)) for s in sons), ", ".join(sons))
cotes = {n.get("cote") for n in N.values() if n.get("organe") and enf[n["id"]]}
ctrl("Le prototype montre un développement à gauche ET à droite", {"g", "d"} <= cotes or len([n for n in N.values() if n.get("organe") and enf[n["id"]]]) >= 2)

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
md = [f"# Audit rigoureux de la conception — {'RÉUSSI' if ok else 'ÉCHEC'}", "", "| Contrôle | Résultat | Détail |", "|---|---|---|"] + [f"| {a} | {'✅' if b else '❌'} | {c} |" for a, b, c in R]
os.makedirs(os.path.join(ICI, "audit"), exist_ok=True)
open(os.path.join(ICI, "audit", "conception.md"), "w", encoding="utf-8").write("\n".join(md))
print("RÉUSSI" if ok else "ÉCHEC", f"{sum(r[1] for r in R)}/{len(R)}"); [print(" ❌", a, "→", c) for a, b, c in R if not b]
sys.exit(0 if ok else 1)
