#!/usr/bin/env python3
"""Construit les données du site Biologie (conception/prototypes/biologie-site/donnees/), sans appel d'API (0 token).

Demande de Vial (27.11.2026) : « UN VÉRITABLE SITE INTERNET permettant de sélectionner les Pathologies et voir les bilans
biologiques d'investigation associés, le niveau d'intention. »

Entrées (lues, jamais réécrites) :
  - conception/donnees/paraclinique/biologie/fiches/*/EX-1-*.json : 101 fiches auditées (gabarit à 3 temps) ;
  - conception/prototypes/moteur/tetrade.json : bilans des diagnostics de la Tétrade (visée → groupe → [examen, signe]).
Sorties :
  - donnees/pathologies.json : index des pathologies (libellé normalisé), examens liés avec niveau d'intention et phrase source ;
  - donnees/examens.json : index des examens, avec les pathologies qu'ils diagnostiquent ou suivent ;
  - donnees/fiches/<id>.json : copie exacte de chaque fiche (le site est autonome) ;
  - donnees/meta.json : systèmes, matrices, disciplines, règles de dérivation, comptes.

Le script ne rédige aucun texte médical : il découpe et regroupe les phrases des fiches et de la Tétrade, mot pour mot.
Niveau d'intention, par ordre de priorité :
  1. Tétrade, si le libellé normalisé de la pathologie égale exactement (casse ignorée) le texte d'un diagnostic de la Tétrade
     et si une ligne de son bilan nomme l'examen : le niveau est la visée et le groupe de la Tétrade (ex. « Diagnostique · Gold standard ») ;
  2. sinon, dérivation : la rubrique du temps 1 de la fiche dont une phrase nomme la pathologie (urgence, diagnostic et étiologie,
     dépistage et bilan préthérapeutique, suivi) ;
  3. sinon « Interprétation au temps 3 (niveau non précisé) » : la fiche interprète ce diagnostic sans dire à quel moment on la demande.
Signature : AAI (Anthropic AI)
"""
import glob
import hashlib
import json
import os
import re
import shutil
import unicodedata

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
FICHES = os.path.join(RACINE, "conception/donnees/paraclinique/biologie/fiches")
TETRADE = os.path.join(RACINE, "conception/prototypes/moteur/tetrade.json")
SORTIE = os.path.join(RACINE, "conception/prototypes/biologie-site/donnees")

SYSTEMES = {"S1": "Neurologie", "S2": "Tête, cou, ORL et œil", "S3": "Cardiovasculaire", "S4": "Respiratoire",
            "S5": "Digestif et hépato-bilio-pancréatique", "S6": "Néphro-urologique", "S7": "Reproduction et obstétrique",
            "S8": "Endocrino-métabolique", "S9": "Appareil locomoteur", "S10": "Sang et immunité", "S11": "Psychiatrie et sommeil",
            "S12": "Peau et phanères", "T": "Transversaux"}  # repris de reseau_biologie.py (SYSTEMES)
MATRICES = ["Sang et buvard", "Moelle", "Urines", "LCR", "Selles", "Sérosités et synovial", "Respiratoire et ORL",
            "Génital et fœto-maternel", "Salive, sueur, calculs, peau"]
T1 = [("urgence_aigu", "Urgence"), ("diagnostic_etiologie", "Diagnostic et étiologie"),
      ("depistage_pretherapeutique", "Dépistage et bilan préthérapeutique"), ("suivi_surveillance", "Suivi")]
VISEES = {"diagnostique": "Diagnostique", "retentissement": "Retentissement", "etiologique": "Étiologique",
          "complications": "Complications", "therapeutique": "Thérapeutique", "sortie": "Sortie"}
NIVEAU_T3 = "Interprétation au temps 3 (niveau non précisé)"

# Tête de phrase à retirer pour obtenir le libellé (« Il s'agit d'une goutte. » → « goutte »).
ART = r"(?=une? |des |la |le |les |l'|d'|de )"
TETE = re.compile(r"^(?:il s'agit (?:probablement |plutôt |alors |donc |sans doute )?|il peut s'agir |"
                  r"(?:le patient|la patiente|l'enfant|le nourrisson|le nouveau-né|il|elle) (?:a|fait|présente|souffre d'|développe)(?: probablement)? " + ART + "|"
                  r"on (?:retient|suspecte|évoque|pose|diagnostique|confirme) (?:le diagnostic d[e'] ?)?|"
                  r"(?:ce|cette|ces|le|la|cela)\b[^,.;]{0,60}? (?:oriente vers|évoque|fait évoquer|signe) |"
                  r"(?:le )?diagnostic (?:est|retenu) :? ?)", re.I)
INDUIT = re.compile(r"^(?:le |la |l')?[\w'-]+ a (?:induit|provoqué|déclenché)(?: ou démasqué)? (?=une? |des )", re.I)
ARTICLE = re.compile(r"^(?:d'une |d'un |de la |du |des |de l'|d'|de |une |un |la |le |les |l')", re.I)
# Conclusion qui n'est pas une entité nosologique : on ne l'indexe pas comme pathologie (la fiche la garde au temps 3).
NON_PATHO = re.compile(r"\b(?:exclu|exclue|écart|douteux|ininterprétable|ne peut pas|on ne peut|normale?s?\b|est immun|"
                       r"porteur sain|efficace|reste |non cardiaque|probablement d'origine non|indéterminée|on doit |"
                       r"faux|faussement|artefact|pas de |aucun|aucune|n'est pas|ne s'agit pas|il ne s'agit|contamin|"
                       r"erreur d'identification)", re.I)
VERBE = re.compile(r" (?:a|ont|est|sont|se|reste|rend|menace|masquent?|constitue|atteint|fait|peut|doit|augmente|baisse|monte|"
                   r"élève|abaisse|traduit|signe|montre|indique|confirme|oriente|suggère|évoque|explique|cause|provoque|reflète|"
                   r"correspond|devient|paraît|parait|reste) ", re.I)
COUPE = re.compile(r",| \(| : | car | parce que | qui | dont | ;|;| donc | alors que | puisque | lorsque | quand | si ")
GENERIQUES = {"syndrome", "maladie", "insuffisance", "carence", "deficit", "infection", "hepatite", "anemie", "cancer", "tumeur",
              "leucemie", "lymphome", "diabete", "hypertension", "intoxication", "grossesse", "epanchement", "ascite", "arthrite",
              "meningite", "encephalite", "encephalopathie", "peritonite", "pneumonie", "allergie", "neutropenie", "thrombopenie",
              "acidose", "alcalose", "hemorragie", "thrombose", "purpura", "crise", "atteinte", "lesion", "trouble", "surdosage",
              "toxicite", "colite", "gastro-enterite", "uveite", "hemopathie", "myelome", "polyarthrite", "spondyloarthrite",
              "vascularite", "nephropathie", "glomerulonephrite", "cirrhose", "pancreatite", "thyroidite", "hypothyroidie",
              "hyperthyroidie", "hyperparathyroidie", "hypogonadisme", "cholestase", "colique", "fievre", "sepsis", "choc"}
LIENS = {"de", "d", "du", "des", "la", "le", "l", "a", "à", "en", "au", "aux", "par", "sur", "sous", "avec"}
# Mots qui ne suffisent pas à reconnaître un examen dans une ligne de bilan de la Tétrade.
VIDES = {"dosage", "serique", "plasmatique", "sanguin", "sanguine", "urinaire", "urinaires", "total", "totale", "totales", "libre",
         "anticorps", "bilan", "examen", "taux", "recherche", "culture", "test", "tests", "valeur", "niveau", "sang", "serum",
         "plasma", "urine", "urines", "liquide", "analyse", "standard", "profil", "selles", "suivi", "controle", "mesure",
         "rapport", "index", "indice", "score", "panel", "fonction", "marqueurs", "cellules", "chimie", "numeration", "formule",
         "ponction", "prelevement", "fiche", "rapide", "aigue", "chronique", "contre", "entre", "apres", "avant", "pendant",
         "autres", "autre", "selon", "chaque", "toutes", "plusieurs", "ionogramme", "biochimie", "serologie", "serologies",
         "dosages", "proteines", "glucose", "acide", "complet", "complete", "normal", "precoce", "systematique", "biopsie",
         "imagerie", "clinique", "examens", "tubes", "heures", "jours"}


def sans_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def jetons(s):
    return [m for m in re.split(r"[^a-z0-9+-]+", sans_accents(s)) if m]


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", sans_accents(s))).strip("-")[:80]


def libelle(phrase):
    """Libellé normalisé d'une conclusion de fiche, ou None si ce n'est pas une entité nosologique."""
    s = (phrase or "").strip()
    if not s or NON_PATHO.search(s):
        return None
    if TETE.match(s):
        t = TETE.sub("", s)
    elif INDUIT.match(s):
        t = INDUIT.sub("", s)
    elif VERBE.search(" " + s + " "):
        return None  # phrase verbale qui ne nomme pas une entité (« La carence en fer se corrige. »)
    else:
        t = s
    t = ARTICLE.sub("", t.strip())
    t = COUPE.split(t)[0].strip().rstrip(".").strip()
    t = re.sub(r" ou (?:d'une?|une?|de la|du|des) ", " ou ", t)
    t = re.sub(r"\s+", " ", t)
    if not t or len(t) < 4 or len(t) > 90 or VERBE.search(" " + t + " "):
        return None
    if t[0].isupper() and not (len(t) > 1 and t[1].isupper()):
        t = t[0].lower() + t[1:]
    return t


SUFFIXES = re.compile(r"(?:emie|urie|ite|ose|ome|pathie|penie|cytose|isme|algie|rragie|thorax|ectasie|plasie|oedeme|ase)$")


def noyau(lib):
    """Terme de famille (« hyperkaliémie médicamenteuse modérée » → « hyperkaliémie ») ; sert aux voisines et à la recherche dans le temps 1."""
    mots = lib.split(" ")
    if sans_accents(mots[0]) not in GENERIQUES:
        return mots[0]
    pris = [mots[0]]
    for k, m in enumerate(mots[1:], 1):
        if sans_accents(m) in ("ou", "et", "sans", "avec"):
            break
        pris.append(m)
        if sans_accents(m).strip("'") not in LIENS and not m.endswith("'") and sans_accents(m) != "non":
            if k + 1 < len(mots) and re.fullmatch(r"[A-Z][A-Z0-9-]{0,5}", mots[k + 1]):
                pris.append(mots[k + 1])
            break
    return " ".join(pris)


def noyau_cherchable(n):
    """Le terme de famille sert à repérer la pathologie dans le temps 1 seulement s'il est assez précis."""
    if " " in n:
        return True
    return len(n) >= 7 and SUFFIXES.search(sans_accents(n)) is not None


def phrases(texte):
    return [p.strip() for p in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-ÖØ-Þ«])", texte or "") if p.strip()]


def contient(texte, terme):
    """Le terme (sans accents, en mots entiers) figure-t-il dans le texte ?"""
    a, b = sans_accents(texte), sans_accents(terme)
    return re.search(r"(?<![a-z])" + re.escape(b) + r"(?![a-z])", a) is not None


def charger_fiches():
    F = {}
    for f in sorted(glob.glob(os.path.join(FICHES, "*", "EX-1-*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        F[d["id"]] = d
    return F


def charger_tetrade():
    d = json.load(open(TETRADE, encoding="utf-8"))
    T = {}
    for n in d["noeuds"]:
        b = n.get("bulle")
        if isinstance(b, dict) and isinstance(b.get("bilan"), dict):
            T.setdefault(n["texte"].strip().lower(), n)
    return T


def mots_examen(d):
    """Mots distinctifs d'un examen (titre, nom exact, synonymes, paramètres) pour le reconnaître dans une ligne de la Tétrade."""
    e = d.get("entete") or {}
    src = [d.get("titre", ""), e.get("nom_exact", ""), e.get("synonymes", "")]
    src += [p.get("parametre", "") for p in d.get("temps2_examen") or [] if isinstance(p, dict)]
    m = set()
    for s in src:
        for j in jetons(s):
            if len(j) >= 5 and j not in VIDES:
                m.add(j)
    # Sigles courts écrits en capitales (PTH, TSH, BNP, CRP…) : on les garde tels quels.
    for s in src:
        for sig in re.findall(r"\b[A-Z][A-Z0-9-]{1,6}\b", s):
            if len(sig) >= 2:
                m.add(sans_accents(sig))
    return m


def ligne_nomme(ligne, mots):
    js = set(jetons(ligne))
    return sorted(js & mots)


def main():
    F = charger_fiches()
    T = charger_tetrade()
    MOTS = {i: mots_examen(d) for i, d in F.items()}

    P = {}  # clé = libellé normalisé (minuscules) → pathologie

    def patho(lib):
        k = lib.lower()
        if k not in P:
            P[k] = {"id": slug(lib), "nom": lib[0].upper() + lib[1:], "cle": k, "famille": noyau(lib),
                    "conclusions": [], "examens": {}, "traitements": [], "systemes": set(), "matrices": set(),
                    "disciplines": set(), "sources": []}
        return P[k]

    for i, d in F.items():
        for j, t in enumerate(d.get("temps3_interpretation") or []):
            lib = libelle(t.get("diagnostic"))
            if not lib:
                continue
            p = patho(lib)
            p["conclusions"].append({"examen": i, "t3": j, "phrase": t.get("diagnostic")})
            p["examens"].setdefault(i, {"t3": [], "trt": []})["t3"].append(j)
        for j, m in enumerate((d.get("traitement") or {}).get("moyens") or []):
            lib = libelle(m.get("diagnostic"))
            if not lib:
                continue
            p = patho(lib)
            p["examens"].setdefault(i, {"t3": [], "trt": []})["trt"].append(j)
            p["traitements"].append({"examen": i, "moyen": j, "diagnostic": m.get("diagnostic"), "general": m.get("general"),
                                     "specifiques": m.get("specifiques"), "posologie": m.get("posologie"), "source": m.get("source")})

    # Examens qui citent la pathologie (libellé complet ou terme de famille) dans une rubrique du temps 1, sans l'interpréter au temps 3.
    for p in P.values():
        termes = [p["cle"]] + ([p["famille"]] if noyau_cherchable(p["famille"]) else [])
        for i, d in F.items():
            t1 = d.get("temps1_indications") or {}
            for k, _ in T1:
                for ph in phrases(t1.get(k, "")):
                    if any(contient(ph, t) for t in termes if len(t) >= 5):
                        p["examens"].setdefault(i, {"t3": [], "trt": []}).setdefault("t1", []).append({"rubrique": k, "phrase": ph})
                        break

    # Niveau d'intention de chaque lien pathologie → examen.
    nb_tetrade = 0
    for p in P.values():
        n = T.get(p["cle"])
        tet = None
        if n:
            b = n["bulle"]
            tet = {"id": n["id"], "texte": n["texte"], "type": n.get("type"), "source": b.get("source"),
                   "traitement": b.get("traitement") or [], "bilan": []}
            for vis, groupes in b["bilan"].items():
                for gr, lignes in groupes.items():
                    for li in lignes:
                        nom, signe = (li + ["", ""])[:2]
                        lie = [i for i in F if ligne_nomme(nom, MOTS[i])]
                        tet["bilan"].append({"visee": VISEES.get(vis, vis), "groupe": gr, "examen": nom, "signe": signe, "fiches": lie})
            nb_tetrade += 1
        p["tetrade"] = tet
        liens = []
        for i, x in p["examens"].items():
            d = F[i]
            niv = None
            if tet:
                for li in tet["bilan"]:
                    if i in li["fiches"]:
                        niv = {"niveau": f"{li['visee']} · {li['groupe']}", "origine": "tetrade",
                               "phrase": f"{li['examen']} : {li['signe']}", "source": f"Tétrade : {tet['texte']} ({tet['source'] or 'source de la Tétrade'})"}
                        break
            if not niv and x.get("t1"):
                r = x["t1"][0]
                niv = {"niveau": dict(T1)[r["rubrique"]], "origine": "temps1", "rubrique": r["rubrique"], "phrase": r["phrase"],
                       "source": f"Temps 1 de la fiche {i}, rubrique « {dict(T1)[r['rubrique']]} »"}
            if not niv:
                ph = d["temps3_interpretation"][x["t3"][0]]["diagnostic"] if x["t3"] else d["traitement"]["moyens"][x["trt"][0]]["diagnostic"]
                niv = {"niveau": NIVEAU_T3, "origine": "temps3", "phrase": ph, "source": f"Temps 3 de la fiche {i}"}
            autres = [{"rubrique": r["rubrique"], "niveau": dict(T1)[r["rubrique"]], "phrase": r["phrase"]} for r in x.get("t1", [])]
            liens.append({"examen": i, "titre": d.get("titre"), "t3": x["t3"], "trt": x["trt"], **niv, "temps1": autres})
            p["systemes"].add(d.get("systeme"))
            p["matrices"].add(d.get("_matrice"))
            p["disciplines"].update(d.get("axe_secondaire") or [])
            for s in d.get("sources") or []:
                if s not in p["sources"]:
                    p["sources"].append(s)
        p["liens"] = sorted(liens, key=lambda l: (not l["t3"] and not l["trt"], l["titre"] or ""))

    # Une pathologie n'est indexée que si au moins une fiche l'interprète (temps 3) ou la traite (traitement).
    sortie = []
    vus = {}
    for p in sorted(P.values(), key=lambda p: sans_accents(p["nom"])):
        if not p["conclusions"] and not p["traitements"]:
            continue
        base = p["id"] or "pathologie"
        vus[base] = vus.get(base, 0) + 1
        pid = base if vus[base] == 1 else f"{base}-{vus[base]}"
        sortie.append({"id": pid, "nom": p["nom"], "famille": p["famille"], "conclusions": p["conclusions"],
                       "liens": p["liens"], "traitements": p["traitements"], "tetrade": p["tetrade"],
                       "systemes": sorted(x for x in p["systemes"] if x), "matrices": sorted(x for x in p["matrices"] if x),
                       "disciplines": sorted(p["disciplines"]), "sources": p["sources"]})
    # Voisines : même terme de famille.
    fam = {}
    for p in sortie:
        fam.setdefault(sans_accents(p["famille"]), []).append(p["id"])
    for p in sortie:
        p["voisines"] = [x for x in fam[sans_accents(p["famille"])] if x != p["id"]]

    ex = []
    for i, d in F.items():
        e = d.get("entete") or {}
        ps = [p["id"] for p in sortie if any(l["examen"] == i for l in p["liens"])]
        ex.append({"id": i, "titre": d.get("titre"), "nom_exact": e.get("nom_exact"), "synonymes": e.get("synonymes"),
                   "systeme": d.get("systeme"), "matrice": d.get("_matrice"), "disciplines": d.get("axe_secondaire") or [],
                   "pathologies": ps})
    ex.sort(key=lambda x: sans_accents(x["titre"] or ""))

    os.makedirs(os.path.join(SORTIE, "fiches"), exist_ok=True)
    for i, d in F.items():
        src = glob.glob(os.path.join(FICHES, "*", i + ".json"))[0]
        shutil.copyfile(src, os.path.join(SORTIE, "fiches", i + ".json"))
    for f in glob.glob(os.path.join(SORTIE, "fiches", "*.json")):
        if os.path.basename(f)[:-5] not in F:
            os.remove(f)
    ecrire = lambda nom, obj: json.dump(obj, open(os.path.join(SORTIE, nom), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    ecrire("pathologies.json", sortie)
    ecrire("examens.json", ex)
    emp = hashlib.sha256("".join(sorted(json.dumps(d, sort_keys=True, ensure_ascii=False) for d in F.values())).encode()).hexdigest()[:16]
    meta = {"systemes": SYSTEMES, "matrices": MATRICES,
            "disciplines": sorted({a for d in F.values() for a in d.get("axe_secondaire") or []}),
            "niveaux_tetrade": [f"{v} · {g}" for v in VISEES.values() for g in ("1re intention", "Gold standard")],
            "niveaux_derives": [l for _, l in T1] + [NIVEAU_T3],
            "regle": ("Le niveau d'intention vient de la Tétrade (conception/prototypes/moteur/tetrade.json) quand le nom de la pathologie y figure "
                      "exactement et qu'une ligne de son bilan nomme l'examen ; sinon il se déduit de la rubrique du temps 1 de la fiche "
                      "dont une phrase nomme la pathologie ; sinon la fiche interprète le diagnostic au temps 3 sans préciser le moment."),
            "comptes": {"fiches": len(F), "pathologies": len(sortie), "avec_tetrade": sum(1 for p in sortie if p["tetrade"]),
                        "liens": sum(len(p["liens"]) for p in sortie)},
            "empreinte_fiches": emp, "signature": "AAI (Anthropic AI)"}
    ecrire("meta.json", meta)
    print(f"{len(F)} fiches | {len(sortie)} pathologies ({meta['comptes']['avec_tetrade']} avec bilan de la Tétrade) | "
          f"{meta['comptes']['liens']} liens pathologie → examen | {len(ex)} examens")


if __name__ == "__main__":
    main()
