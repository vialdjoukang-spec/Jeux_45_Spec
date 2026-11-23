"""Construit prototypes/moteur/tetrade.json depuis la source unique (systemes.py) + les circuits pilotes (0 token).
Racines = systèmes posés sur le corps ; chaque système déroule TOUS ses organes de haut en bas ;
chaque organe se déplie selon l'espace actif (anatomie, physiologie, sémiologie, physiopathologie).
Usage : python conception/outils/construire_config_tetrade.py"""
import json, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from systemes import SYSTEMES, PHYSIOLOGIE_POUMON, GLOSSAIRE
from systemes_rediges import REDIGES, SOURCES, PALIERS, PALIER_BULLE

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = os.path.join(ICI, "prototypes", "moteur", "tetrade.json")
slug = lambda t: re.sub(r"[^a-z0-9]+", "_", unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()).strip("_")[:30]
court = lambda t: t.split(" (")[0]                     # concision : la case garde le nom court ; le détail va dans l'infobulle
ancien = json.load(open(CFG, encoding="utf-8"))
A = {n["id"]: n for n in ancien["noeuds"]}

RACINES = {  # système : (ancre 3D, côté, couleur)
 "Cardiovasculaire": ("coeur", "d", "#c0392b"), "Psyché (psychiatrie)": ("cerveau", "d", "#3d8f5a"), "Digestif & hépatobiliaire": ("estomac", "d", "#c98a2b"),
 "Rénal & uro-génital": ("reins", "d", "#b8960f"), "Infectieux & immunitaire": ("rate", "d", "#16897b"), "Gynéco-obstétrical": ("bassin", "d", "#c2417a"),
 "Pédiatrique (croissance et développement)": ("cage", "d", "#e05aa0"),
 "Respiratoire": ("poumon_d", "g", "#2f6fd0"), "Neurologique": ("cerveau", "g", "#8e5cc4"), "Ophtalmologique & ORL": ("crane", "g", "#5b6574"),
 "Endocrinien & métabolique": ("trachee", "g", "#d9731a"), "Hématologique & oncologique": ("femur", "g", "#a33"), "Locomoteur & rhumatologique": ("bassin", "g", "#6b7280"),
 "Dermatologique": ("humerus", "g", "#b07a5a")}

VOLET_BULLE = {
 "Macroscopie": ("La macroscopie décrit la forme, les parties et l'organisation visibles à l'œil nu.", "Elle donne les repères de l'examen clinique et de l'imagerie."),
 "Microscopie": ("La microscopie décrit les tissus et les cellules qui portent la fonction.", "Elle explique ce que montrent la biopsie et l'histologie."),
 "Vascularisation": ("La vascularisation décrit les artères, les veines et les lymphatiques de l'organe.", "Elle explique les territoires d'ischémie et la diffusion des cancers."),
 "Innervation": ("L'innervation décrit les nerfs somatiques et autonomes de l'organe.", "Elle explique les douleurs projetées et les effets des médicaments autonomes."),
 "Rapports et projections": ("Les rapports situent l'organe par rapport à ses voisins ; les projections le placent sur la peau.", "Ils guident la palpation, l'auscultation et les ponctions."),
 "Embryologie et variantes": ("L'embryologie retrace la formation de l'organe ; les variantes décrivent les formes normales mais inhabituelles.", "Elles expliquent les malformations et les pièges d'imagerie."),
 "Paramètres simples": ("Les paramètres simples se mesurent au lit du malade.", "Tu les connais par cœur avec leurs valeurs normales."),
 "Régulation": ("La régulation décrit les capteurs et les effecteurs qui maintiennent la fonction.", "Elle explique les compensations que tu lis dans les examens."),
 "Lois physiques et biochimie": ("Les lois physiques et la biochimie mettent la fonction en équations et en courbes.", "Chaque formule ouvre une courbe ou un calculateur."),
 "Intégration avec les autres organes": ("L'intégration relie la fonction de l'organe à celle des autres organes.", "Elle prépare la lecture des examens complexes, comme les gaz du sang."),
 "Valeurs normales (unités SI)": ("Les valeurs normales s'expriment en unités SI, celles des laboratoires suisses.", "Tu raisonnes en kPa pour les gaz du sang."),
}
RETENIR = {"Fréquence respiratoire": "Une FR ≥ 30/min compte dans le score CRB-65.", "Volume courant": "Le respirateur se règle sur le poids idéal, pas sur le poids réel.",
 "Volumes et capacités": "Un rapport VEMS/CVF < 0,7 signe l'obstruction.", "Chémorécepteurs centraux": "Chez le BPCO hypercapnique, l'O₂ à haut débit peut aggraver l'hypercapnie.",
 "Chémorécepteurs périphériques": "Ils deviennent le moteur ventilatoire du patient hypercapnique chronique.", "Équation des gaz alvéolaires": "Un gradient A-a élevé désigne une cause pulmonaire de l'hypoxémie.",
 "Courbe de dissociation de l'hémoglobine": "Sous 8 kPa de PaO₂, la saturation chute brutalement.", "Effet Bohr et effet Haldane": "L'acidose aide les tissus à recevoir l'O₂.",
 "Henderson-Hasselbalch": "Le poumon corrige vite, le rein corrige lentement.", "Loi de Fick (diffusion)": "La fibrose épaissit la membrane : la DLCO baisse.",
 "Rapport ventilation / perfusion": "L'embolie crée de l'espace mort ; la pneumonie crée de l'effet shunt.", "Poumon et rein : équilibre acide-base": "Une compensation n'est jamais complète : un pH normal avec des valeurs anormales évoque un trouble mixte.",
 "Lecture des gaz du sang": "Tu lis toujours dans l'ordre : pH, cause primaire, compensation, gradient A-a, trou anionique.", "Gaz du sang artériel": "Tu convertis : 1 kPa = 7,5 mmHg."}

# organes rédigés : identifiant stable (circuits pilotes rattachés) ou préfixe du système
OID, REDIGE = {}, {}                                    # nom d'organe → id ; nom d'organe → système rédigé
for _s, _c in REDIGES.items():
    for _n in SOURCES[_s]["organes"]:
        OID[_n] = _c["ids"].get(_n) or _c["prefixe"] + slug(court(_n))
        REDIGE[_n] = _s
# organes partagés : une seule maison, l'autre système y renvoie (validé par Vial le 2026-11-21)
LIENS = {"Circulation pulmonaire": {"def": "La circulation pulmonaire relie le ventricule droit aux alvéoles puis à l'oreillette gauche.",
          "pourquoi": "Son contenu complet (anatomie, physiologie, pathologies) vit dans le système cardiovasculaire pour éviter une copie.",
          "confusion": "Les échanges gazeux eux-mêmes restent décrits ici, au poumon.",
          "retenir": "Tu ouvres Cardiovasculaire → Circulation pulmonaire pour l'embolie et l'hypertension pulmonaires."},
         "Pharynx": {"def": "Le pharynx est le carrefour musculaire où se croisent l'air et les aliments ; il assure le temps pharyngé de la déglutition.",
          "pourquoi": "Son contenu complet (anatomie, physiologie, sémiologie, pathologies) vit dans le système respiratoire pour éviter une copie.",
          "confusion": "La dysphagie haute (fausse route, toux au repas) vient du pharynx ; la dysphagie basse, rétrosternale, vient de l'œsophage.",
          "retenir": "Tu ouvres Respiratoire → Pharynx pour la déglutition, l'angine, l'abcès péri-amygdalien et l'apnée obstructive."},
         "Thymus": {"def": "Le thymus éduque les lymphocytes T dans l'enfance, puis il s'involue et se remplace par de la graisse chez l'adulte.",
          "pourquoi": "Son contenu complet (anatomie, physiologie, sémiologie, pathologies) vit dans le système endocrinien pour éviter une copie.",
          "confusion": "Une masse du médiastin antérieur peut être un thymome, un lymphome, une tumeur germinale ou un goitre plongeant : le lymphome se traite ici, aux ganglions lymphatiques.",
          "retenir": "Tu ouvres Endocrinien → Thymus pour le thymome, la myasthénie associée et le syndrome de DiGeorge."},
         "Organes lymphoïdes (moelle, thymus, rate, ganglions, MALT)": {"def": "Les organes lymphoïdes fabriquent les lymphocytes (moelle, thymus) puis les mettent au contact des antigènes (rate, ganglions, MALT).",
          "pourquoi": "Chaque organe a une seule maison pour éviter une copie : moelle, rate et ganglions au système hématologique, thymus au système endocrinien ; le MALT est décrit aux barrières.",
          "confusion": "Une adénopathie ou une grosse rate peuvent venir d'une infection (réponse immune) ou d'une hémopathie : la biopsie tranche quand elles persistent.",
          "retenir": "Tu ouvres Hématologique → Rate ou Ganglions lymphatiques, Endocrinien → Thymus, et Infectieux → Barrières pour le MALT."}}
N = []
for sysn, orgs in SYSTEMES.items():
    anc, cote, coul = RACINES[sysn]
    sid = "sys_" + slug(sysn)
    N.append({"id": sid, "type": "", "nature": "Système", "texte": court(sysn).replace("&", "et"), "organe": anc, "cote": cote, "couleur": coul,
              "rubriques": "systeme", "bulle": {"def": f"Le système {court(sysn).lower()} compte {len(orgs)} organes ou structures, déroulés de haut en bas.", "retenir": "Tu cliques un organe, puis tu choisis l'espace : anatomie, physiologie, sémiologie ou physiopathologie."}})
    for nom, _, topo in orgs:
        red = REDIGE.get(nom) == sysn
        oid = (OID[nom] if red else None) or ("pou" if nom.startswith("Poumons") else "org_" + slug(sysn)[:6] + "_" + slug(nom))
        b = A.get(oid, {}).get("bulle") if oid == "pou" else None
        if red and SOURCES[sysn]["organes"][nom]["bulle"]: b = SOURCES[sysn]["organes"][nom]["bulle"]
        if nom in LIENS and not red: b = LIENS[nom]
        o = {"id": oid, "type": "", "nature": "Organe", "texte": court(nom), "couleur": coul, "de": [sid], "rubriques": "organe",
             "bulle": b or {"def": f"{nom} : organe du système {court(sysn).lower()}.", "retenir": "Son contenu (anatomie, physiologie, sémiologie, physiopathologie) reste à produire."},
             "topo": topo}
        if not b:
            o["aProduire"] = True
        N.append(o)

# ---- systèmes rédigés : organes → volets → mots-clés (fenêtres) ; sémiologie ; physiopathologie → 4 paliers → pathologies ----
for sysn, conf in REDIGES.items():
    S, COUL = SOURCES[sysn], conf["couleur"]
    def bulle_volet(vol, esp):
        d, r = VOLET_BULLE.get(vol) or S["volets"][vol]
        return {"def": d, ("repere" if esp == "anatomie" else "retenir"): r}
    for nom, org in S["organes"].items():
        oid = OID[nom]
        for esp, cle in (("anatomie", "a"), ("physiologie", "p")):
            for i, (vol, items) in enumerate(org[esp]):
                vid = f"{oid}_{cle}{i}"
                N.append({"id": vid, "type": "", "nature": "Volet", "texte": court(vol), "couleur": COUL, "de": [oid], "espace": esp, "bulle": bulle_volet(vol, esp)})
                for j, (k, t, r, fen) in enumerate(items):
                    n = {"id": f"{vid}_{j}", "type": "", "nature": "Mot-clé", "texte": k, "couleur": COUL, "de": [vid], "espace": esp,
                         "bulle": {"def": t, ("repere" if esp == "anatomie" else "retenir"): r}}
                    fen = "3d" if esp == "anatomie" else fen
                    if fen: n["fenetre"] = fen
                    N.append(n)
        for i, (temps, signes) in enumerate(S["semio"].get(nom, [])):
            tid = f"{oid}_s{i}"
            d, p_, c_, r_ = S["temps"][temps]
            N.append({"id": tid, "type": "Interrogatoire" if temps == "Interrogatoire" else f"Temps {i + 1}", "texte": temps, "couleur": COUL, "de": [oid],
                      "espace": "semiologie", "bulle": {"def": d, "pourquoi": p_, "confusion": c_, "retenir": r_}})
            for j, sg in enumerate(signes):
                N.append({"id": f"{tid}_{j}", "type": "Signe", "texte": sg["signe"], "couleur": COUL, "de": [tid], "espace": "semiologie",
                          "presentation": sg["presentation"], "bulle": sg["bulle"], **({"uniqueAssume": sg["uniqueAssume"]} if sg.get("uniqueAssume") else {})})
        paliers = {}
        for p in S["pathos"].get(nom, []):
            pal = p["palier"]; nomp, typ, col = PALIERS[pal]
            if pal not in paliers:
                paliers[pal] = f"{oid}_x{pal.lower()}"
                d, c = PALIER_BULLE[pal]
                N.append({"id": paliers[pal], "type": "", "nature": "Palier", "texte": nomp, "couleur": col, "de": [oid], "espace": "physiopathologie", "bulle": {"def": d, "consequence": c}})
            N.append({"id": f"{paliers[pal]}_{slug(p['nom'])}", "type": "Diagnostic · " + typ, "nature": "Pathologie", "texte": p["nom"], "couleur": col,
                      "de": [paliers[pal]], "espace": "physiopathologie", "rubriques": "pathologie", "bulle": p["bulle"]})

# ---- physiologie du poumon : volets → mots-clés → courbes et calculateurs ----
POU_REDIGE = any(n.startswith("Poumons") and o["physiologie"] for S in SOURCES.values() for n, o in S["organes"].items())
for i, (vol, items) in enumerate({} if POU_REDIGE else PHYSIOLOGIE_POUMON.items()):
    vid = f"ph{i}"
    d, r = VOLET_BULLE[vol]
    N.append({"id": vid, "type": "", "nature": "Volet", "texte": court(vol), "couleur": "#2f6fd0", "de": ["pou"], "espace": "physiologie", "bulle": {"def": d, "retenir": r}})
    for j, (k, t, fen) in enumerate(items):
        n = {"id": f"{vid}_{j}", "type": "", "nature": "Mot-clé", "texte": k, "couleur": "#2f6fd0", "de": [vid], "espace": "physiologie", "bulle": {"def": t, "retenir": RETENIR[k]}}
        if fen: n["fenetre"] = fen
        N.append(n)

# ---- physiopathologie du cœur : fonction perturbée → mécanisme → signe ----
PP = [("pp1", "Dysfonction systolique", "Le ventricule gauche éjecte moins de sang à chaque battement.", "La fraction d'éjection baisse et le volume résiduel augmente."),
      ("pp2", "Pression télédiastolique ↑", "Le sang qui reste dans le ventricule élève sa pression en fin de diastole.", "Le remplissage brutal du ventricule produit le galop B3."),
      ("pp3", "Pression capillaire pulmonaire ↑", "La pression remonte dans l'oreillette gauche puis dans les capillaires pulmonaires.", "Au-delà d'environ 18 mmHg (2,4 kPa), le liquide quitte les capillaires."),
      ("pp4", "Œdème interstitiel et alvéolaire", "Le liquide envahit l'interstitium puis les alvéoles.", "Il produit les crépitants, l'orthopnée et, au maximum, l'œdème aigu du poumon.")]
prev = "coe"
for i, t, d, c in PP:
    N.append({"id": i, "type": "", "nature": "Mécanisme", "texte": t, "couleur": "#7a5cc4", "de": [prev], "espace": "physiopathologie", "bulle": {"def": d, "consequence": c}})
    prev = i

# ---- sémiologie : circuits pilotes conservés (temps d'examen rattachés à l'organe) ----
for n in ancien["noeuds"]:
    if n["id"].startswith(tuple(c["prefixe"] for c in REDIGES.values()) + tuple(i + "_" for c in REDIGES.values() for i in c["ids"].values())) \
            or n.get("nature") in ("Palier", "Pathologie"):
        continue
    if n["id"] in ("coe", "pou") or n.get("nature") in ("Système", "Organe", "Volet", "Mot-clé", "Mécanisme") or n["id"].startswith(("sys_", "org_", "an", "ph", "pp")) and not n["id"].startswith(("pt",)):
        continue
    if n.get("organe"):
        continue                                   # anciennes racines d'organes isolés : remplacées par les systèmes
    if n["id"].startswith(("t", "pt")) and n.get("de") in (["coe"], ["pou"]):
        n = dict(n, espace="semiologie")
    N.append(n)

cfg = {k: v for k, v in ancien.items() if k != "noeuds"}
cfg.update(noeuds=N, espace="anatomie", sousTitre="Systèmes sur le corps 3D · clic : organes de haut en bas · espaces : anatomie, physiologie, sémiologie, physiopathologie",
           rubriques={"anatomie": [["def", "Ce que c'est"], ["repere", "Repère clinique"]], "physiologie": [["def", "Ce que c'est"], ["retenir", "À retenir"]],
                      "physiopathologie": [["def", "Ce qui se passe"], ["consequence", "Conséquence clinique"]], "systeme": [["def", "Ce que c'est"], ["retenir", "Comment l'explorer"]],
                      "organe": [["def", "Ce que c'est"], ["pourquoi", "Pourquoi ici"], ["confusion", "Confusion possible"], ["retenir", "À retenir"]],
                      "pathologie": [["def", "Ce qui se passe"], ["pourquoi", "Pourquoi ces signes"], ["confusion", "Confusion possible"], ["retenir", "À retenir"]]},
           cible=[0, -90, 1000], dist=5400, glossaire={**ancien.get("glossaire", {}), **GLOSSAIRE, **{k: v for S in SOURCES.values() for k, v in S["glossaire"].items()}})
json.dump(cfg, open(CFG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("noeuds :", len(N), "| organes :", sum(1 for n in N if n.get("nature") == "Organe"), "| à produire :", sum(1 for n in N if n.get("aProduire")))
