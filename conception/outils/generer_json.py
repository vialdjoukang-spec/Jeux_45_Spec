"""Génère TOUS les fichiers JSON des trois modules (squelettes à remplir + exemples réels), à 0 token.
Source : conception/plans/*.plan.json (champ « donnees ») + prototypes/moteur/tetrade.json (exemple rempli).
Sortie : conception/donnees/** , conception/donnees/INDEX.json , conception/donnees/schemas/*.schema.json
Usage : python conception/outils/generer_json.py"""
import json, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalogue_paraclinique import TOPO, PRELEVEMENTS, EXPLORATIONS, MODALITES, SYSTEMES as SYS_ORG, TECHNIQUES, VISEES, SMARTER
from transversales import OUTILS, LENTILLES, ARBORESCENCE, REF as TREF

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ICI, "donnees")


def slug(t):
    t = t.replace("œ", "oe").replace("Œ", "Oe").replace("æ", "ae").replace("Æ", "Ae")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    t = re.sub(r"\(.*?\)", "", t)
    return re.sub(r"[^a-z0-9]+", "_", t).strip("_")[:40]


def cle(champ):
    """« valeursReference (SI, âge) » → ('valeursReference', False) ; « examens[] » → ('examens', True)."""
    tete = re.split(r"[ :(]", champ.strip(), maxsplit=1)[0]
    return tete.replace("[]", ""), tete.endswith("[]") or "[]" in champ.split(":")[0]


def squelette(d):
    el = {}
    for ch in d["champs"]:
        k, liste = cle(ch)
        el[k] = [] if liste else None
    return {"_meta": {"fichier": d["fichier"], "role": d["role"], "producteur": d["producteur"], "volume": d["volume"],
                      "champs": d["champs"], "statut": "À REMPLIR", "regles": [
                          "Chaque texte destiné à l'apprenant s'écrit en phrases verbales.",
                          "Chaque signe, symptôme et syndrome porte une « bulle » à 4 rubriques : def, pourquoi, confusion, retenir.",
                          "Chaque temps d'examen compte 2 ou 3 signes ; un seul ne suffit jamais.",
                          "Les posologies suivent la cascade suisse : AIPS, Compendium, sociétés suisses, sociétés européennes.",
                          "Tout sigle, score ou terme technique (ex. « atypique ») cité dans un texte doit exister dans « glossaire » avec sa définition : aucun renvoi hors de l'application.",
                          "Chaque signe ou symptôme porte « presentation » : « typique » ou « atypique » (affiché en rouge).",
                          "Le bilan se range par visée (diagnostique avec « 1re intention » et « Gold standard », retentissement, étiologique, complications, thérapeutique si applicable, sortie si hospitalisation), puis par groupe (Biologie, Imagerie, Score, Explorations, Clinique) ; chaque examen s'écrit [nom affiché, détail en infobulle : signe recherché et seuil]."]},
            "elements": [el], "glossaire": {}}


VIDE = (None, "", [], {})


def conserver(neuf, ancien):
    """Fusion conservatrice : le squelette régénéré garde toute valeur déjà remplie (lots fusionnés, audit)."""
    if isinstance(neuf, dict) and isinstance(ancien, dict):
        out = {k: (ancien[k] if k == "statut" and ancien.get(k) else conserver(v, ancien[k])) if k in ancien else v for k, v in neuf.items()}
        out.update({k: v for k, v in ancien.items() if k not in neuf and v not in VIDE})
        return out
    cle = lambda x: x.get("id") or x.get("ref") or x.get("nom") if isinstance(x, dict) else None
    if isinstance(neuf, list) and isinstance(ancien, list) and neuf and all(cle(x) for x in neuf):
        idx = {cle(x): x for x in ancien if cle(x)}
        return [conserver(x, idx[cle(x)]) if cle(x) in idx else x for x in neuf]
    if isinstance(neuf, list) and isinstance(ancien, list) and any(isinstance(x, dict) for x in neuf + ancien):
        # éléments sans identifiant (ex. défis du squelette, id nul) : appariement par position, rien de rempli ne se perd
        return [conserver(neuf[i], ancien[i]) if i < len(ancien) else neuf[i] for i in range(len(neuf))] + ancien[len(neuf):]
    return ancien if neuf in VIDE and ancien not in VIDE else neuf


def ecrire(chemin, obj):
    p = os.path.join(OUT, chemin)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if os.path.exists(p):   # ne jamais écraser un champ rempli (lots fusionnés, audit de fond)
        try:
            obj = conserver(obj, json.load(open(p, encoding="utf-8")))
        except ValueError:
            pass
    json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return chemin


plans = {n: json.load(open(os.path.join(ICI, "plans", f"{n}.plan.json"), encoding="utf-8")) for n in ["tetrade", "pharmacologie", "paraclinique"]}
SYST = [s for s in plans["tetrade"]["perimetre"]["inclus"] if not s.startswith("Lien")]
SYS_SLUG = [slug(s) for s in SYST]
O = plans["paraclinique"]["onglets"]
EXPANS = {
    "<systeme>": SYS_SLUG,
    "<prelevement>": [],
    "<famille>": [],
    "<exploration>": [slug(e) for e in O["explorations"]["liste"]],
    "<onglet>": ["biologie", "imagerie", "explorations"],
    "<pathologie>": ["_modele"],
    "<dci>": ["_modele"],
    "<lettre>": [],   # produit plus bas, rempli depuis la Cartographie
    "<region>": [],   # produit plus bas depuis le catalogue topographique
    "<organe>": [],
}

ecrits = []
for nom, p in plans.items():
    for d in p["donnees"]:
        f = d["fichier"]
        jokers = [j for j in EXPANS if j in f]
        cibles = [f]
        for j in jokers:
            cibles = [c.replace(j, v) for c in cibles for v in EXPANS[j]]
        for c in cibles:
            ecrits.append(ecrire(c, squelette(d)))

# ---------- exemples réels remplis (tirés du prototype validé) ----------
cfg = json.load(open(os.path.join(ICI, "prototypes", "moteur", "tetrade.json"), encoding="utf-8"))
noeuds = cfg["noeuds"]
TYPE = {"Signe": "signe", "Symptôme": "symptome", "Syndrome": "syndrome", "Examen": "examen"}
graphe = {"_meta": {"fichier": "tetrade/cardiovasculaire/graphe.json", "statut": "EXEMPLE RÉEL — circuit de l'insuffisance cardiaque gauche, à auditer par REJECTOR_"},
          "noeuds": [{"id": n["id"], "type": TYPE.get(n.get("type"), "temps_examen" if n.get("type", "").startswith(("Temps", "Interrogatoire")) else ("organe" if n.get("organe") else "diagnostic")),
                      "label": n["texte"], "organe": n.get("organe"), "bulle": n.get("bulle"), "son": n.get("son"), "particularites": n.get("particularites"), "uniqueAssume": n.get("uniqueAssume", False)} for n in noeuds],
          "liens": [{"de": p, "vers": n["id"]} for n in noeuds for p in n.get("de", [])]}
ecrits.append(ecrire("tetrade/cardiovasculaire/graphe.exemple_ic_gauche.json", graphe))
semio = {"_meta": {"fichier": "tetrade/cardiovasculaire/semiologie.json", "statut": "EXEMPLE RÉEL — à auditer par REJECTOR_"},
         "elements": [{"id": n["id"], "nature": "symptome" if n.get("type") == "Symptôme" else "signe", "temps": n["de"][0], "nomConsacre": n["texte"],
                       "bulle": n["bulle"], "son": n.get("son")} for n in noeuds if n.get("type") in ("Signe", "Symptôme")]}
ecrits.append(ecrire("tetrade/cardiovasculaire/semiologie.exemple_ic_gauche.json", semio))
sy = next(n for n in noeuds if n["id"] == "sy")
ecrits.append(ecrire("tetrade/cardiovasculaire/syndromes.exemple_ic_gauche.json", {"_meta": {"statut": "EXEMPLE RÉEL"}, "elements": [{
    "syndromeId": "insuffisance_cardiaque_gauche", "signesMinimaux": ["s41", "s42", "s52"], "signes": [x for x in sy["de"]], "bulle": sy["bulle"],
    "examenComplementaire": "ex", "diagnostics": [{"id": "dg", "specialite": "Cardiologie"}],
    "confusionsSyndromiques": ["Insuffisance cardiaque droite (turgescence jugulaire, reflux hépatojugulaire, œdèmes déclives)"]}]}))
ecrits.append(ecrire("tetrade/sons.json", {"_meta": {"statut": "AMORCÉ — 2 sons réels, catalogue à compléter"}, "elements": [
    {"sonId": "galop_b3", "nom": "Galop B3", "fichier": "sons/galop_B3_apex.mp3", "foyer": "Apex", "temps": "auscultation",
     "source": "HLS-CMDS (Torabi, Shirani, Reilly 2025), F_S3_A.wav", "licence": "MIT (dépôt) / CC BY 4.0 (données)"},
    {"sonId": "crepitants_fins", "nom": "Crépitants fins", "fichier": "sons/crepitants_fins_base_droite.mp3", "foyer": "Base droite", "temps": "auscultation",
     "source": "HLS-CMDS (Torabi, Shirani, Reilly 2025), M_FC_RLA.wav", "licence": "MIT (dépôt) / CC BY 4.0 (données)"}]}))
DEF = {"Vasculaire": "Le tissu souffre d'un défaut d'apport sanguin, d'une thrombose, d'une embolie ou d'une hémorragie.",
       "Infectieux": "Un agent infectieux (bactérie, virus, champignon, parasite) envahit le tissu.",
       "Traumatique": "Une force mécanique, thermique ou chimique lèse le tissu.",
       "Dégénératif": "Le tissu s'use ou perd ses cellules avec l'âge ou la surcharge.",
       "Inflammatoire": "Une réaction inflammatoire non infectieuse altère le tissu.",
       "Tumoral": "Une prolifération cellulaire bénigne ou maligne remplace ou comprime le tissu.",
       "Congénital": "Une anomalie présente dès la naissance (génétique ou du développement) modifie le tissu.",
       "Auto-immun": "Le système immunitaire attaque le tissu de son propre organisme.",
       "Fonctionnel": "L'organe fonctionne mal sans lésion structurelle démontrable.",
       "Endocrinien": "Un excès ou un défaut hormonal, ou un trouble métabolique, perturbe le tissu."}
mn = plans["pharmacologie"]["mnemonique"]
ecrits.append(ecrire("pharmaco/mnemonique.json", {"_meta": {"statut": "REMPLI — validé par Vial le 2026-11-21 ; définitions à auditer"},
    "elements": [{"lettre": a, "famille": b, "definition": DEF.get(b.split(" ")[0], None), "couleur": None} for a, b in mn["lettres"]]}))
neu = json.load(open(os.path.join(OUT, "tetrade/neurologique/syndromes.json"), encoding="utf-8"))
gab = neu["elements"][0]
neu["elements"] = [dict(gab, syndromeId=slug(x), nom=x) for x in plans["tetrade"]["neuro"]]
neu["_meta"]["statut"] = f"AMORCÉ — {len(neu['elements'])} syndromes majeurs listés, contenu à remplir"
ecrire("tetrade/neurologique/syndromes.json", neu)
ecrits.append(ecrire("paraclinique/imagerie/cas/pneumonie_lobaire_moyenne.json", {"_meta": {"statut": "EXEMPLE RÉEL — à auditer"},
    "clicheBrut": {"src": "rx.jpg", "url": "https://github.com/ieee8023/covid-chestxray-dataset (pneumococcal-pneumonia-day0.jpg)"},
    "clicheAnnote": {"src": "rx.jpg", "reperes": [{k: a[k] for k in ("n", "x", "y", "rx", "ry", "texte")} for a in json.load(open(os.path.join(ICI, "prototypes", "moteur", "paraclinique.json"), encoding="utf-8"))["fenetres"][0]["annotations"]]},
    "diagnostic": "Pneumonie à pneumocoque du lobe moyen", "conduite": None}))

# ---------- catalogue topographique rempli : 1 fichier par organe ; analyses individuelles ; prélèvements (technique) ----------
from analyses_biologiques import FAMILLES, analyses as _analyses
ANALYSES = _analyses()


def _norm(t):
    t = unicodedata.normalize("NFKD", t.replace("œ", "oe").replace("Œ", "Oe")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


from analyses_biologiques import ALIAS as _ALIAS


def _cles(nom):
    base = _norm(re.sub(r"\(.*?\)", "", nom))
    return [base] + _ALIAS.get(base, [])


import functools
@functools.lru_cache(maxsize=None)
def analyses_de(examen):
    n = " " + _norm(examen) + " "
    return tuple(sorted({a for _, a, _ in ANALYSES for c in _cles(a) if c and (" " + c + " ") in n}))


for reg, orgs in TOPO.items():
    for org, mods in orgs.items():
        ecrits.append(ecrire(f"paraclinique/topographie/{slug(reg)}/{slug(org)}.json", {"_meta": {"region": reg, "organe": org, "statut": "LISTE COMPLÈTE — indication, principe, interprétation et bulle à remplir",
                "regles": ["Biologie : les valeurs de référence vivent dans biologie/analyses ; ici, tu dis pourquoi on demande l'analyse pour cet organe et ce qu'on y cherche."]},
            "examens": [{"id": slug(org) + "__" + slug(e), "modalite": MODALITES[k], "nom": e, "visees": [], "signeRecherche": None, "seuil": None, "indication": None, "discriminant": None, "avantageSelectif": None, "plutotQue": None, "limite": None, "referencePour": [], "smarterMedicine": None, "radioAnatomieNormale": None, "precautions": None, "irradiation_mSv": None, "delai": None, "prelevementRef": None,
                         **({"analysesRef": list(analyses_de(e))} if k == "BIO" else {}), "synonymes": [], "aspectNormal": None, "anomaliesElementaires": [], "syndromesParacliniques": [], "pathologiesAssociees": [], "bulle": None} for k, v in mods.items() for e in v], "glossaire": {}}))
ORGANES_DE = {}
for _r, _os in TOPO.items():
    for _o, _m in _os.items():
        for _e in _m.get("BIO", []):
            for _a in analyses_de(_e):
                ORGANES_DE.setdefault(_a, set()).add(_o)
for fam, (prel, lst) in FAMILLES.items():
    ecrits.append(ecrire(f"paraclinique/biologie/analyses/{fam.lower()}.json", {"_meta": {"famille": fam, "statut": "LISTE COMPLÈTE — une analyse = une fiche ; valeurs SI suisses à remplir",
            "regles": ["Source unique des valeurs de référence biologiques.", "Unités SI suisses ; valeurs par âge, sexe et grossesse quand elles diffèrent.", "Causes de hausse et de baisse : des plus fréquentes aux plus graves."]},
        "analyses": [{"id": slug(a), "nom": a, "prelevement": p, "tube": None, "unite": None,
                      "valeursReference": {"adulteHomme": None, "adulteFemme": None, "enfant": None, "grossesse": None, "sujetAge": None},
                      "seuilsCritiques": None, "variationsPhysiologiques": None, "augmentation": [], "diminution": [], "interferences": None, "delaiResultat": None,
                      "organes": sorted(ORGANES_DE.get(a, ())),
                      "synonymes": [], "parametres": [], "anomaliesElementaires": [], "syndromesParacliniques": [], "pathologiesAssociees": [], "bulle": None}
                     for f2, a, p in ANALYSES if f2 == fam], "glossaire": {}}))
for pre, exs in PRELEVEMENTS.items():
    ecrits.append(ecrire(f"paraclinique/biologie/prelevements/{slug(pre)}.json", {"_meta": {"prelevement": pre, "statut": "LISTE COMPLÈTE — technique de prélèvement à remplir (les valeurs vivent dans biologie/analyses)"},
        "examens": [{"nom": e, "technique": None, "tube": None, "conditions": None, "conservationTransport": None, "interpretation": [], "analysesRef": list(analyses_de(e)), "bulle": None} for e in exs], "glossaire": {}}))
ecrits.append(ecrire("paraclinique/explorations/liste.json", {"_meta": {"statut": "LISTE COMPLÈTE"}, "elements": EXPLORATIONS}))
for sysn, orgs in SYS_ORG.items():
    ecrits.append(ecrire(f"tetrade/{slug(sysn)}/examens.json", {"_meta": {"systeme": sysn, "progression": ["topo-systemique", "topo-organe"], "statut": "RELIÉ AU CATALOGUE"},
        "organes": [{"organe": o, "region": next(r for r, og in TOPO.items() if o in og), "examens": [slug(o) + "__" + slug(e) for v in next(og[o] for og in TOPO.values() if o in og).values() for e in v]} for o in orgs]}))

# ---------- techniques, visées, smarter medicine, disciplines transversales (remplis) ----------
ecrits.append(ecrire("paraclinique/techniques_discriminants.json", {"_meta": {"statut": "REMPLI — à auditer"}, "familles": {f: [dict(zip(["technique", "discriminant", "preferQuand", "plutotQue", "limite"], l)) for l in lst] for f, lst in TECHNIQUES.items()}}))
ecrits.append(ecrire("paraclinique/visees_bilan.json", {"_meta": {"statut": "REMPLI"}, "visees": [{"id": a, "but": b} for a, b in VISEES]}))
ecrits.append(ecrire("paraclinique/smarter_medicine.json", {"_meta": {"statut": "AMORCÉ — à compléter liste par liste sur smartermedicine.ch"}, "recommandations": [{"situation": a, "recommandation": b} for a, b in SMARTER]}))
ecrits.append(ecrire("tetrade/transversales/lentilles.json", {"_meta": {"statut": "REMPLI"}, "lentilles": LENTILLES}))
for t in TREF["transversales"]:
    ecrits.append(ecrire(f"tetrade/transversales/outils/{t['letter']}_{slug(t['name'])}.json", {"_meta": {"statut": "STRUCTURE REMPLIE — cours à rédiger"},
        "lettre": t["letter"], "nom": t["name"], "sousOnglets": [s["name"] for s in t["subIcons"]],
        "lecons": [{"id": l["tileId"], "titre": l["name"], "sousOnglet": l["subIconId"], "strate": l["stratumCode"]} for l in t["lessons"]],
        "arborescence": [{"partie": a, "consigne": b, "contenu": None} for a, b in ARBORESCENCE], "liensTetrade": [], "liensSSP": []}))
    for l in t["lessons"]:  # une leçon = un fichier (fragment de production autonome)
        ecrits.append(ecrire(f"tetrade/transversales/lecons/{t['letter']}/{slug(l['tileId'])}.json", {"_meta": {"statut": "À REMPLIR", "discipline": f"{t['letter']} — {t['name']}",
                "regles": ["La leçon commence par un cas suisse concret et finit par une décision à prendre.", "Phrases verbales ; tout sigle figure au glossaire.", "Elle renvoie aux SSP sans les recopier."]},
            "id": l["tileId"], "titre": l["name"], "lettre": t["letter"], "sousOnglet": l["subIconId"], "strate": l["stratumCode"],
            "casDOuverture": None, "parties": {a: None for a, _ in ARBORESCENCE}, "decisionFinale": None,
            "items": [{"type": None, "enonce": None, "options": [], "bonneReponse": None, "explicationParOption": {}} for _ in range(5)],
            "liensSSP": [], "bulle": None, "glossaire": {}}))
ecrits.append(ecrire("tetrade/cardiovasculaire/anatomie3d.exemple_coeur.json", {"_meta": {"statut": "EXEMPLE — fenêtre de structure du prototype"}, "structureId": "coeur", "parent": "thorax",
    "niveau": ["Paroi thoracique et péricarde", "Faces et bords du cœur", "Cavités et valves", "Vascularisation coronaire", "Tissu de conduction et innervation"],
    "vues3D": ["antérieure", "latérale gauche", "postérieure", "supérieure"], "trajetRenforce": ["aorte"], "modele": "BodyParts3D (FMA7088, FMA3734)",
    "radioAnatomie": ["Rx thorax PA : bord droit = oreillette droite ; bord gauche = ventricule gauche ; bouton aortique = crosse", "CT injecté axial : crosse, puis quatre cavités", "IRM cardiaque : petit axe et quatre cavités"]}))

# ---------- systèmes → organes (liste complète) ; organe déplié par espace ----------
from systemes import SYSTEMES as SYS_O, VOLETS_ANATOMIE, VOLETS_PHYSIOLOGIE, PHYSIOLOGIE_POUMON
from cardio import ORGANES as CV, PATHOS as CV_PATHOS, PALIERS, SEMIO as CV_SEMIO
for sysn, orgs in SYS_O.items():
    ecrits.append(ecrire(f"tetrade/{slug(sysn)}/organes.json", {"_meta": {"systeme": sysn, "ordre": "haut → bas", "statut": "LISTE COMPLÈTE"},
        "organes": [{"organe": o, "ancre3D": a, "topo": t, "fichier": f"organes/{slug(o)}.json"} for o, a, t in orgs]}))
    for o, a, t in orgs:
        rempli = {"Poumons (lobes, segments, acinus)": ("physiologie", PHYSIOLOGIE_POUMON)}.get(o)
        an = {v: [] for v in VOLETS_ANATOMIE}; ph = {v: [] for v in VOLETS_PHYSIOLOGIE}; pa = None
        if rempli and rempli[0] == "physiologie": ph = {v: [{"motCle": x[0], "texte": x[1], "fenetre": x[2]} for x in l] for v, l in rempli[1].items()}
        if o in CV:   # cardiovasculaire : volets adaptés par type d'organe + pathologies en 4 paliers
            rempli = True
            an = {v: [{"motCle": k, "texte": t, "repere": r, "fenetre": "3d"} for k, t, r, _ in l] for v, l in CV[o]["anatomie"]}
            ph = {v: [{"motCle": k, "texte": t, "retenir": r, "fenetre": f} for k, t, r, f in l] for v, l in CV[o]["physiologie"]}
            pa = {PALIERS[c][0]: [{"nom": x["nom"], "bulle": x["bulle"]} for x in CV_PATHOS.get(o, []) if x["palier"] == c] for c in PALIERS}
        ecrits.append(ecrire(f"tetrade/{slug(sysn)}/organes/{slug(o)}.json", {"_meta": {"systeme": sysn, "organe": o, "statut": ("RÉDIGÉ — à auditer" if o in CV else "EXEMPLE RÉEL") if rempli else "À REMPLIR",
            "regles": ["La case garde un nom court ; le texte va en infobulle ; la courbe ou l'image 3D va en fenêtre.", "Chaque mot-clé d'anatomie ouvre une image 3D réelle (jamais de SVG).",
                       "Chaque mot-clé de physiologie ouvre une courbe calculée, un tracé ou un détail ; unités SI (kPa).", "Phrases verbales ; tout sigle figure au glossaire."]},
            "organe": o, "ancre3D": a, "topo": t, "anatomie": an, "physiologie": ph, "semiologie": {t: sg for t, sg in CV_SEMIO.get(o, [])} if o in CV else None, "pathologies": pa, "bulle": CV[o]["bulle"] if o in CV else None, "glossaire": {}}))

# ---------- schémas de validation (un par famille de fichier) ----------
SCH = {
    "bulle": {"type": "object", "required": ["def", "pourquoi", "confusion", "retenir"], "properties_note": "un diagnostic ajoute bilan (6 visées) et traitement[] avec source", "properties": {k: {"type": "string", "minLength": 20} for k in ["def", "pourquoi", "confusion", "retenir"]}},
    "noeud_graphe": {"type": "object", "required": ["id", "type", "label"], "properties": {"type": {"enum": ["organe", "temps_examen", "signe", "symptome", "syndrome", "examen", "diagnostic", "specialite", "fonction", "mecanisme", "traitement"]}, "bulle": {"$ref": "bulle.schema.json"}}},
    "syndrome": {"type": "object", "required": ["syndromeId", "signesMinimaux", "signes", "bulle", "diagnostics"], "properties": {"signesMinimaux": {"type": "array", "minItems": 2, "maxItems": 3}}},
    "son": {"type": "object", "required": ["sonId", "nom", "fichier", "source", "licence"]},
}
for k, v in SCH.items():
    ecrits.append(ecrire(f"schemas/{k}.schema.json", {"$schema": "https://json-schema.org/draft/2020-12/schema", "title": k, **v}))

# ---------- INDEX DE RECHERCHE du jeu (mode Organe, mode Examen) ----------
def _cles_rech(t):
    n = _norm(t); base = _norm(re.sub(r"\\(.*?\\)", "", t))
    return sorted({n, base} | {w for w in base.split() if len(w) > 3})
_org_rech, _ex_rech = [], {}
for reg, orgs in TOPO.items():
    for org, mods in orgs.items():
        f = f"paraclinique/topographie/{slug(reg)}/{slug(org)}.json"
        _org_rech.append({"organe": org, "region": reg, "fichier": f, "cles": _cles_rech(org), "nbExamens": sum(len(v) for v in mods.values())})
        for k, v in mods.items():
            for e in v:
                x = _ex_rech.setdefault(_norm(e), {"examen": e, "modalite": MODALITES[k], "organes": [], "cles": _cles_rech(e), "analyses": list(analyses_de(e)) if k == "BIO" else []})
                x["organes"].append({"organe": org, "fichier": f, "id": slug(org) + "__" + slug(e)})
for fam, (prel, lst) in FAMILLES.items():
    for _, a_, p_ in [x for x in ANALYSES if x[0] == fam]:
        x = _ex_rech.setdefault(_norm(a_), {"examen": a_, "modalite": "Analyse biologique", "organes": [], "cles": _cles_rech(a_), "analyses": [a_]})
        x["ficheAnalyse"] = f"paraclinique/biologie/analyses/{fam.lower()}.json"
        for o in sorted(ORGANES_DE.get(a_, ())):
            if not any(y["organe"] == o for y in x["organes"]):
                reg = next(r for r, os_ in TOPO.items() if o in os_)
                x["organes"].append({"organe": o, "fichier": f"paraclinique/topographie/{slug(reg)}/{slug(o)}.json"})
ecrits.append(ecrire("recherche/index.json", {"_meta": {"statut": "GÉNÉRÉ PAR SCRIPT (0 token)", "usage": [
        "Mode Organe : la barre sert de sélecteur ; l'organe apparaît seul au centre, puis se déplie nœud après nœud (modalités → examens → contenu).",
        "Mode Examen : l'organe en 3D au centre et une seule ligne horizontale vers l'examen ; même contenu que le mode Organe, accès court-circuité.",
        "Recherche insensible à la casse et aux accents ; propositions même mal orthographiées (trigrammes + distance d'édition) ; les synonymes produits enrichissent les clés."]},
    "organes": _org_rech, "examens": sorted(_ex_rech.values(), key=lambda x: x["examen"])}))

# ---------- PARTIE PRATIQUE : un jumeau par fichier théorique (défis du jeu, entité par entité) ----------
from pratique import genre, defis_pour, MODES, REGLES as REGLES_PRATIQUE
PROJET_DE = {"examen": "2_Jeux_Paraclinique", "analyse": "2_Jeux_Paraclinique", "prelevement": "2_Jeux_Paraclinique", "exploration": "2_Jeux_Paraclinique",
             "lecon": "3_Transversal_Discip"}
for ch in sorted(set(ecrits)):
    g = genre("/" + ch)
    if not g or ch.startswith("pratique/") or ch.endswith("liste.json") or "exemple" in ch:
        continue
    th = json.load(open(os.path.join(OUT, ch), encoding="utf-8"))
    liste = next((k for k in ("examens", "analyses", "elements") if isinstance(th.get(k), list)), None)
    if liste:
        ents = [{"ref": x.get("id") or x.get("nom") if isinstance(x, dict) else x, "nom": x.get("nom") if isinstance(x, dict) else x,
                 **({"modalite": x["modalite"]} if isinstance(x, dict) and x.get("modalite") else {}),
                 "defis": defis_pour(g, x.get("modalite") if isinstance(x, dict) else None)} for x in th[liste]]
        gabarit = not any(e["nom"] for e in ents)
    else:
        ents = [{"ref": th.get("id") or th.get("organe"), "nom": th.get("titre") or th.get("organe"), "defis": defis_pour(g)}]
        gabarit = False
    projet = PROJET_DE.get(g, "1_Jeux_Tetrade_Fondation")
    ecrits.append(ecrire("pratique/" + ch, {"_meta": {"source": ch, "genre": g, "projet": projet, "modes": MODES[projet], "statut": "À REMPLIR",
            "regles": REGLES_PRATIQUE + (["La théorie de ce fichier est un gabarit : tu crées une entité par élément produit dans la théorie, avec ses défis."] if gabarit else [])},
        "entites": ents, "glossaire": {}}))

ecrits = sorted(set(ecrits))
index = {"genere": "par conception/outils/generer_json.py (0 token)", "total": len(ecrits),
         "parModule": {m: sum(1 for e in ecrits if e.startswith(m)) for m in ["tetrade", "pharmaco", "paraclinique", "pratique", "recherche", "schemas"]},
         "fichiers": sorted(ecrits)}
json.dump(index, open(os.path.join(OUT, "INDEX.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(index["parModule"]), "total", index["total"])
