"""Génère TOUS les fichiers JSON des trois modules (squelettes à remplir + exemples réels), à 0 token.
Source : conception/plans/*.plan.json (champ « donnees ») + prototypes/moteur/tetrade.json (exemple rempli).
Sortie : conception/donnees/** , conception/donnees/INDEX.json , conception/donnees/schemas/*.schema.json
Usage : python conception/outils/generer_json.py"""
import json, os, re, unicodedata

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ICI, "donnees")


def slug(t):
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
                          "Les posologies suivent la cascade suisse : AIPS, Compendium, sociétés suisses, sociétés européennes."]},
            "elements": [el]}


def ecrire(chemin, obj):
    p = os.path.join(OUT, chemin)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return chemin


plans = {n: json.load(open(os.path.join(ICI, "plans", f"{n}.plan.json"), encoding="utf-8")) for n in ["tetrade", "pharmacologie", "paraclinique"]}
SYST = [s for s in plans["tetrade"]["perimetre"]["inclus"] if not s.startswith("Lien")]
SYS_SLUG = [slug(s) for s in SYST]
O = plans["paraclinique"]["onglets"]
EXPANS = {
    "<systeme>": SYS_SLUG,
    "<examen>": [slug(p) for p in O["biologie"]["prelevements"]],
    "<exploration>": [slug(e) for e in O["explorations"]["liste"]],
    "<onglet>": ["biologie", "imagerie", "explorations"],
    "<pathologie>": ["_modele"],
    "<dci>": ["_modele"],
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
                      "label": n["texte"], "organe": n.get("organe"), "bulle": n.get("bulle"), "son": n.get("son")} for n in noeuds],
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

# ---------- schémas de validation (un par famille de fichier) ----------
SCH = {
    "bulle": {"type": "object", "required": ["def", "pourquoi", "confusion", "retenir"], "properties": {k: {"type": "string", "minLength": 20} for k in ["def", "pourquoi", "confusion", "retenir"]}},
    "noeud_graphe": {"type": "object", "required": ["id", "type", "label"], "properties": {"type": {"enum": ["organe", "temps_examen", "signe", "symptome", "syndrome", "examen", "diagnostic", "specialite", "fonction", "mecanisme", "traitement"]}, "bulle": {"$ref": "bulle.schema.json"}}},
    "syndrome": {"type": "object", "required": ["syndromeId", "signesMinimaux", "signes", "bulle", "diagnostics"], "properties": {"signesMinimaux": {"type": "array", "minItems": 2, "maxItems": 3}}},
    "son": {"type": "object", "required": ["sonId", "nom", "fichier", "source", "licence"]},
}
for k, v in SCH.items():
    ecrits.append(ecrire(f"schemas/{k}.schema.json", {"$schema": "https://json-schema.org/draft/2020-12/schema", "title": k, **v}))

index = {"genere": "par conception/outils/generer_json.py (0 token)", "total": len(ecrits),
         "parModule": {m: sum(1 for e in ecrits if e.startswith(m)) for m in ["tetrade", "pharmaco", "paraclinique", "schemas"]},
         "fichiers": sorted(ecrits)}
json.dump(index, open(os.path.join(OUT, "INDEX.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(index["parModule"]), "total", index["total"])
