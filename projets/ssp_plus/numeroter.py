#!/usr/bin/env python3
"""Construit ssp_plus_v2.json et attribue les codes (+) de façon déterministe.

Entrées (lecture seule) : data/ssp/INDEX.json (248 officiels), data/ssp_etendus/*.json (1094 SSP+),
projets/ssp_plus/inventaire.json (ordre ancien), decisions_v2.tsv (arbitrages), ajouts_v2.json (ajouts sourcés).
Numérotation : G continue après G16 ; S, F et O continuent après le dernier numéro officiel du groupe parent.
Ordre : rang du parent dans le catalogue, puis ancien ordre (inventaire), les ajouts en dernier.
"""
import json, re, csv, pathlib, hashlib

R = pathlib.Path(__file__).resolve().parents[2]
ICI = R / "projets/ssp_plus"
off = json.load(open(R / "data/ssp/INDEX.json"))["ssp"]
RANG = {o["ssp"]: i for i, o in enumerate(off)}
NOM = {o["ssp"]: o["nom"] for o in off}
inv = json.load(open(ICI / "inventaire.json"))
ORDRE = {e["code"]: i for i, e in enumerate(inv)}
NATURE = {"G": "plainte générale", "S": "symptôme ou signe", "F": "résultat d'examen", "O": "situation ou contexte"}

# Parents F par défaut quand un fichier F pointait vers une autre lettre (modalité de l'examen).
F_DEFAUT = {"F-ANAPATH": "F2.10", "F-IMGAB": "F2.4", "F-IMGOA": "F2.4", "F-IMGTH": "F2.4",
            "F-NEUROIMG": "F2.4", "F-MICRO": "F2.19", "F-IMM": "F2.19", "F-ENDO": "F2.14"}
NOTE_F = {"F2.4": "SSP F d'imagerie le plus proche.", "F2.19": "F2.19 sert d'ancrage aux résultats biologiques et microbiologiques, faute de SSP F dédié.",
          "F2.14": "Seul SSP F de dosage hormonal ; aucun SSP F pour les hormones non thyroïdiennes.", "F2.10": "Histologie, cytologie ou génétique."}
# Intitulés diagnostiques plutôt que points de départ : signalés, non retirés (aucun statut ne le prévoit).
DIAG = {"S-PED-X04", "S-PED-X06", "S-PED-X32", "S-PED-X33", "S-INF-X16", "S-INF-X21", "S-INF-X26", "S-INF-X27",
        "S-INF-X29", "S-OPHORL-X09", "S-OPHORL-X15", "S-OPHORL-X22", "S-OPHORL-X31", "S-URO-X08", "S-URO-X27",
        "S-URO-X31", "S-ENDO-X14", "S-ENDO-X29", "S-GYN-X09", "S-GYN-X14", "S-CV-X35", "S-LOCO-X15"}

def lettre(c): return c[0]
def prefixe(c): return c.split("-X")[0]

dec = {}
for ligne in open(ICI / "decisions_v2.tsv", encoding="utf-8"):
    if ligne.startswith("#") or not ligne.strip(): continue
    a, st, cat, par, cible, just = ligne.rstrip("\n").split("\t")
    dec[a] = dict(statut=st, categorie=cat, parent=par, cible=cible, justification=just)

entrees = []
for f in sorted((R / "data/ssp_etendus").glob("*.json")):
    if f.name == "INDEX.json": continue
    for e in json.load(open(f, encoding="utf-8")):
        a, p = e["code"], e["parentOfficiel"]
        o = dict(code="", ancienCode=a, statut="garde", categorie=lettre(a), parentOfficiel=p,
                 intitule=e["intitule"], intituleEN=e.get("intituleEN", ""), typeDepart=e.get("typeDepart", ""),
                 pourquoi=e.get("pourquoi", ""), diagnosticsDifferentiels=e.get("pathologies", []),
                 justification="", sources=[], _ordre=ORDRE[a])
        if a in dec:
            d = dec[a]; o["statut"] = d["statut"]; o["justification"] = d["justification"]
            if d["statut"] in ("garde", "deplace"):
                o["categorie"], o["parentOfficiel"] = d["categorie"], d["parent"]
            elif d["statut"] == "retire_doublon_catalogue":
                o["doublonDe"] = d["cible"]
            else:
                o["fusionneDans"] = d["cible"]
        elif lettre(a) != lettre(p):
            if lettre(a) == "F" and prefixe(a) in F_DEFAUT:
                np_ = F_DEFAUT[prefixe(a)]
                o.update(statut="deplace", parentOfficiel=np_,
                         justification=f"Résultat d'examen : parent {np_} de même lettre au lieu de {p}. {NOTE_F[np_]}")
            else:
                c = lettre(p)
                o.update(statut="deplace", categorie=c,
                         justification=f"Sa nature ({NATURE[c]}) suit son parent {p} : catégorie {c} au lieu de {lettre(a)}.")
        else:
            o["justification"] = f"Point de départ plus spécifique que {p} ({NOM[p]}), absent du catalogue."
        if a in DIAG:
            o["justification"] += " Intitulé diagnostique : à reformuler en point de départ."
        if o["statut"] == "garde" and o["categorie"] == "F" and o["parentOfficiel"] == "F2.14" and a.startswith("F-ENDO") \
                and not re.search(r"TSH|T4|TPO|calcitonine", o["intitule"], re.I):
            o["justification"] += " " + NOTE_F["F2.14"]
        entrees.append(o)

for i, aj in enumerate(json.load(open(ICI / "ajouts_v2.json", encoding="utf-8"))):
    entrees.append(dict(code="", ancienCode="", statut="ajoute", categorie=aj["categorie"], parentOfficiel=aj["parentOfficiel"],
                        intitule=aj["intitule"], intituleEN=aj["intituleEN"], typeDepart=aj["typeDepart"], pourquoi=aj["pourquoi"],
                        diagnosticsDifferentiels=aj["diagnosticsDifferentiels"], justification=aj["justification"],
                        sources=aj["sources"], _ordre=10**6 + i))

# Numérotation déterministe
actifs = sorted([e for e in entrees if e["statut"] in ("garde", "deplace", "ajoute")],
                key=lambda e: (RANG[e["parentOfficiel"]], e["_ordre"]))
dernier = {}
for c in RANG:
    g = "G" if c.startswith("G") else c.split(".")[0]
    n = int(re.findall(r"\d+", c)[-1])
    dernier[g] = max(dernier.get(g, 0), n)
for e in actifs:
    p = e["parentOfficiel"]; g = "G" if p.startswith("G") else p.split(".")[0]
    dernier[g] += 1
    e["code"] = (f"G{dernier[g]}" if g == "G" else f"{g}.{dernier[g]}") + "(+)"

nouveau = {e["ancienCode"]: e["code"] for e in entrees if e["ancienCode"]}
for e in entrees:
    if e["statut"] == "fusionne_dans":
        e["fusionneDans"] = nouveau[e["fusionneDans"]] + f" (ancien {e['fusionneDans']})"
    e.pop("_ordre")

entrees.sort(key=lambda e: (e["code"] == "", RANG.get(e["parentOfficiel"], 999), e["code"], e["ancienCode"]))
cles = ["code", "ancienCode", "statut", "categorie", "parentOfficiel", "intitule", "intituleEN", "typeDepart", "pourquoi",
        "diagnosticsDifferentiels", "doublonDe", "fusionneDans", "justification", "sources"]
sortie = [{k: e[k] for k in cles if k in e} for e in entrees]
txt = json.dumps(sortie, ensure_ascii=False, indent=1)
(ICI / "ssp_plus_v2.json").write_text(txt + "\n", encoding="utf-8")
print(f"{len(sortie)} entrées écrites ; sha256 {hashlib.sha256(txt.encode()).hexdigest()[:12]}")
