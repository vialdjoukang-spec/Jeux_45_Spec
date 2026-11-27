#!/usr/bin/env python3
"""AUDITER_BIOLOGIE — audit mécanique BLOQUANT des fiches de l'onglet Biologie (BRIEF_BIOLOGIE_CLAUDE_CODE.md § 5). 0 token.

Contrôles (code · règle du brief) :
  A1 blocs        chaque fiche contient les 8 blocs du § 3 ; un bloc absent porte « à produire ».
  A2 source       chaque valeur chiffrée (normale, anomalie, seuil d'alerte, dose) porte une source ; une ligne de temps 2
                  dont la valeur normale est sourcée couvre les seuils de la même ligne (même référence de laboratoire).
  A3 aips         chaque posologie rédigée se termine par « vérifier dans l'AIPS (Swissmedic) ».
  A4 si           unités SI suisses : une unité non SI (mg/dL, mEq, mmHg hors pression artérielle…) n'apparaît qu'à côté
                  de sa valeur SI dans le même champ.
  A5 verbal       aucune phrase nominale : toute phrase de ≥ 4 mots d'une rubrique rédigée contient un verbe conjugué
                  (détecteur repris de organigramme-examen-federal/Claude/_outils/controle3.py, complété du tutoiement).
  A6 ids          aucun identifiant dupliqué ; le nom du fichier égale l'identifiant.
  A7 passerelles  chaque passerelle donne type, cible et raison ; la cible existe (fiches Biologie ou instantané
                  passerelles_cibles.json du dépôt organigramme-examen-federal).
  A8 non_perte    aucune valeur remplie ne disparaît d'une génération à l'autre (instantané .non_perte.json).
  A9 sources      chaque source est datée (année) et porte sa date de lecture (« lu le jj.mm.aaaa ») ou « à vérifier ».
  A10 traitement  un bloc Traitement rédigé porte but, moyens (général, spécifiques, posologie, source).

Usage : python3 conception/outils/paraclinique/auditer_biologie.py [--maj] [--liste] [--cibles CHEMIN_ORGANIGRAMME]
  --maj    : si tout est vert, met à jour l'instantané de non-perte (union : une valeur une fois remplie y reste).
  --liste  : affiche chaque défaut.
Sortie : projets/2_Jeux_Paraclinique/AUDIT_BIOLOGIE.json ; code 1 si un défaut bloquant subsiste.
Signature : AAI (Anthropic AI)
"""
import argparse, glob, hashlib, json, os, re, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
BIO = os.path.join(RAC, "conception", "donnees", "paraclinique", "biologie")
FICHES = os.path.join(BIO, "fiches")
NONPERTE = os.path.join(BIO, ".non_perte.json")
CIBLES = os.path.join(BIO, "passerelles_cibles.json")
RAPPORT = os.path.join(RAC, "projets", "2_Jeux_Paraclinique", "AUDIT_BIOLOGIE.json")
AP = "à produire"
BLOCS = ["entete", "temps1_indications", "temps2_examen", "calculs", "temps3_interpretation", "traitement", "annexeA_pieges", "sources", "passerelles"]

# ---------------------------------------------------------------- A2 : marque de source
SRC = re.compile(r"\([^()]*(?:\b(?:19|20)\d{2}\b|\b[A-Z][A-Za-zé]*[A-Z]\w*\b|\b[A-Z][a-zé]{2,}\b|non vérifié CH|à vérifier|lu le)[^()]*\)"
                 r"|\b[Ss]elon\b|non vérifié CH|à vérifier|\bfiche (?:EX|SF|PH|PS)-", re.U)
NUM = re.compile(r"\d")
# ---------------------------------------------------------------- A3 : renvoi AIPS
AIPS = re.compile(r"v[ée]rifier dans l.AIPS \(Swissmedic\)\.?\s*$", re.I)
# ---------------------------------------------------------------- A4 : unités
NON_SI = re.compile(r"\b(?:mg|g|µg|ng|pg)\s?/\s?dL\b|\bmEq\b|\bmg\s?%|\bmmHg\b|\b°F\b|\bmg/dl\b|\bg/dl\b", re.I)
SI = re.compile(r"mmol\s?/\s?[lL]|µmol\s?/\s?[lL]|nmol\s?/\s?[lL]|pmol\s?/\s?[lL]|\bg\s?/\s?[lL]\b|\bkPa\b|mmol/mol|µmol/s|\bU\s?/\s?[lL]\b|mol/[lL]")
PA = re.compile(r"\bPA\b|pression artérielle|tension|systolique|diastolique", re.I)
# ---------------------------------------------------------------- A5 : détecteur verbal (controle3.py, organigramme-examen-federal)
VERBES = set("""propose proposent recommande recommandent conseille conseillent mentionne mentionnent contient contiennent figure figurent
résulte résultent ajoute ajoutent dépend dépendent rassemble rassemblent résume résument précise précisent indique indiquent décrit décrivent
est sont a ont fait font peut peuvent doit doivent reste restent devient deviennent va vont semble semblent permet permettent signe signent
oriente orientent impose imposent confirme confirment élimine éliminent exclut excluent traite traitent associe associent survient surviennent
provoque provoquent entraîne entraînent exige exigent reçoit reçoivent touche touchent atteint atteignent dépasse dépassent varie varient
augmente augmentent diminue diminuent baisse baissent réduit réduisent favorise favorisent explique expliquent précède précèdent suit suivent
recherche recherchent mesure mesurent montre montrent révèle révèlent définit définissent correspond correspondent comprend comprennent
repose reposent consiste consistent représente représentent constitue constituent nécessite nécessitent justifie justifient prescrit prescrivent
administre administrent évite évitent limite limitent dure durent persiste persistent apparaît apparaissent disparaît disparaissent évolue
évoluent aggrave aggravent protège protègent prévient préviennent dépiste dépistent détecte détectent distingue distinguent sépare séparent
conduit conduisent mène mènent aboutit aboutissent cause causent déclenche déclenchent libère libèrent active activent inhibe inhibent bloque
bloquent stimule stimulent fixe fixent lie lient agit agissent remplace remplacent compte comptent atteste attestent rappelle rappellent
signale signalent pose posent écarte écartent retient retiennent ordonne ordonnent adapte adaptent surveille surveillent contrôle contrôlent
corrige corrigent restaure restaurent normalise prolonge prolongent était étaient avait avaient sera seront aura auront serait seraient
pourrait pourraient devrait devraient faut suffit suffisent vise visent cible ciblent porte portent concerne concernent relève relèvent
donne donnent dose dosent calcule calculent vérifie vérifient prélève prélèvent demande demandent arrête arrêtent garde gardent""".split())
VERBE_RE = re.compile(r"\b(?:\w+(?:ent|ait|aient|era|eront|erait|eraient|ise|isent|it|issent|es|ons|ez))\b", re.I)
PRONOM_VERBE = re.compile(r"\b(?:je|j'|tu|il|elle|ils|elles|on|nous|vous|qui|cela|ce|celle-ci|celui-ci)\s+(?:ne\s+|n'|se\s+|s'|te\s+|t'|l'|le\s+|la\s+|les\s+|y\s+|en\s+)*\w+", re.I)
REFLEXIF = re.compile(r"\b(?:s'|s’|se\s+)[a-zà-ÿ]{3,}", re.I)  # s'élève, s'explique, se recueille
EXEMPTS = {"id", "module", "type", "titre", "sous_onglet", "systeme", "etiquettes", "entree_primaire", "axe_secondaire", "nom_exact",
           "synonymes", "sources", "parametre", "normal", "seuil_alerte", "cible", "nom", "source", "_origine", "_matrice", "_matrice_raison",
           "outil", "mnemotechnique", "formule", "exemple", "specifiques", "general"}


def est_verbale(ph):
    mots = {m.lower() for m in re.findall(r"[\w'’-]+", ph)}
    return bool(mots & VERBES or PRONOM_VERBE.search(ph) or VERBE_RE.search(ph) or REFLEXIF.search(ph))


def phrases(v, chemin):
    if isinstance(v, dict):
        for k, x in v.items():
            if k not in EXEMPTS:
                yield from phrases(x, chemin + [k])
    elif isinstance(v, list):
        for i, x in enumerate(v):
            yield from phrases(x, chemin + [str(i)])
    elif isinstance(v, str) and v.strip() not in ("", "—", AP):
        for ph in re.split(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý«(])|\n", v):
            if len(re.findall(r"[A-Za-zÀ-ÿ]{2,}", ph)) >= 4:
                yield ".".join(chemin), ph.strip()


def vide(v):
    if v is None:
        return True
    if isinstance(v, str):
        return v.strip() in ("", "—", AP)
    if isinstance(v, (list, dict)):
        return len(v) == 0 or all(vide(x) for x in (v.values() if isinstance(v, dict) else v))
    return False


def feuilles(v, chemin=""):
    if isinstance(v, dict):
        for k, x in v.items():
            if not k.startswith("_"):
                yield from feuilles(x, f"{chemin}.{k}" if chemin else k)
    elif isinstance(v, list):
        for i, x in enumerate(v):
            yield from feuilles(x, f"{chemin}[{i}]")
    elif not vide(v):
        yield chemin, hashlib.sha1(str(v).encode()).hexdigest()[:12]


def lire(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def cibles_depuis(depot):
    ids = {}
    base = os.path.join(depot, "Claude", "_progression")
    for p in glob.glob(os.path.join(base, "donnees", "**", "*.json"), recursive=True):
        try:
            d = lire(p)
        except Exception:
            continue
        if isinstance(d, dict) and isinstance(d.get("id"), str):
            ids[d["id"]] = os.path.relpath(p, depot)
    commit = subprocess.run(["git", "-C", depot, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    obj = {"_meta": {"role": "Instantané des identifiants de fiches du dépôt organigramme-examen-federal (cibles de passerelles), pour un audit hors ligne.",
                     "source": "vialdjoukang-spec/organigramme-examen-federal, Claude/_progression/donnees/**", "commit": commit,
                     "producteur": "auditer_biologie.py --cibles"}, "ids": dict(sorted(ids.items()))}
    with open(CIBLES, "w", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False, indent=1) + "\n")
    print(f"cibles : {len(ids)} identifiants (commit {commit[:10]})")


def auditer_fiche(d, ids_bio, cibles):
    D = []
    def faute(code, ou, txt=""):
        D.append({"code": code, "ou": ou, "texte": str(txt)[:200]})
    # A1
    for b in BLOCS:
        if b not in d:
            faute("A1", b, "bloc absent sans « à produire »")
        elif vide(d[b]) and d[b] != AP:
            faute("A1", b, "bloc vide : il doit porter « à produire »")
    # A2 + A4 sur le temps 2
    t2 = d.get("temps2_examen")
    if isinstance(t2, list):
        for i, r in enumerate(t2):
            if not isinstance(r, dict):
                continue
            ligne_sourcee = bool(SRC.search(str(r.get("normal", ""))))
            for k in ("normal", "anomalie", "seuil_alerte"):
                v = str(r.get(k, ""))
                if NUM.search(v) and not SRC.search(v) and not (k != "normal" and ligne_sourcee):
                    faute("A2", f"temps2_examen[{i}].{k}", v)
                if NON_SI.search(v) and not SI.search(v) and not (re.search(r"mmHg", v, re.I) and PA.search(v) and not re.search(r"(?i)mg/dl|mEq", v)):
                    faute("A4", f"temps2_examen[{i}].{k}", v)
    # A2 + A3 + A10 sur le traitement
    tr = d.get("traitement")
    if isinstance(tr, dict):
        if vide(tr.get("but")):
            faute("A10", "traitement.but", "but absent")
        moy = tr.get("moyens")
        if not isinstance(moy, list) or not moy:
            faute("A10", "traitement.moyens", "aucun moyen")
        else:
            for i, m in enumerate(moy):
                for k in ("general", "specifiques", "posologie", "source"):
                    if k not in m or (isinstance(m.get(k), str) and not m[k].strip()):
                        faute("A10", f"traitement.moyens[{i}].{k}", "champ absent ou vide")
                p = str(m.get("posologie", ""))
                if p.strip() and p.strip() not in ("—", AP):
                    if not AIPS.search(p):
                        faute("A3", f"traitement.moyens[{i}].posologie", p)
                    if NUM.search(p) and not (SRC.search(p) or not vide(m.get("source"))):
                        faute("A2", f"traitement.moyens[{i}].posologie", p)
                    if NON_SI.search(p) and not SI.search(p):
                        faute("A4", f"traitement.moyens[{i}].posologie", p)
    elif tr != AP:
        faute("A10", "traitement", "bloc Traitement mal formé")
    # A5
    for champ, ph in phrases(d, []):
        if not est_verbale(ph):
            faute("A5", champ, ph)
    # A7
    pas = d.get("passerelles")
    if isinstance(pas, list):
        for i, p in enumerate(pas):
            if not isinstance(p, dict):
                faute("A7", f"passerelles[{i}]", p); continue
            for k in ("type", "cible", "pourquoi"):
                if vide(p.get(k)):
                    faute("A7", f"passerelles[{i}].{k}", f"{p.get('cible')} : {k} manquant")
            c = p.get("cible")
            if c and c not in ids_bio and c not in cibles:
                faute("A7", f"passerelles[{i}].cible", f"cible inexistante : {c}")
    # A9
    src = d.get("sources")
    if isinstance(src, list):
        for i, s in enumerate(src):
            s = str(s)
            if not re.search(r"à vérifier", s) and not (re.search(r"\b(?:19|20)\d{2}\b", s) and re.search(r"\b(?:lu|consulté)(?:e|s|es)? le \d{1,2}\.\d{1,2}\.\d{4}", s)):
                faute("A9", f"sources[{i}]", s)
    return D


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--maj", action="store_true")
    ap.add_argument("--liste", action="store_true")
    ap.add_argument("--cibles")
    a = ap.parse_args()
    if a.cibles:
        cibles_depuis(a.cibles)
    cibles = lire(CIBLES)["ids"] if os.path.exists(CIBLES) else {}
    chemins = sorted(glob.glob(os.path.join(FICHES, "*", "*.json")))
    fiches, defauts, vus = {}, {}, {}
    for p in chemins:
        d = lire(p)
        i = d.get("id")
        if i in vus:
            defauts.setdefault(i, []).append({"code": "A6", "ou": "id", "texte": f"dupliqué : {vus[i]} et {p}"})
        vus[i] = p
        if os.path.basename(p)[:-5] != i:
            defauts.setdefault(i, []).append({"code": "A6", "ou": "id", "texte": f"fichier {os.path.basename(p)} ≠ id"})
        fiches[i] = d
    for i, d in fiches.items():
        defauts.setdefault(i, []).extend(auditer_fiche(d, set(fiches), cibles))
    # A8 non-perte
    ancien = lire(NONPERTE)["fiches"] if os.path.exists(NONPERTE) else {}
    actuel = {i: dict(feuilles(d)) for i, d in fiches.items()}
    for i, champs in ancien.items():
        if i not in actuel:
            defauts.setdefault(i, []).append({"code": "A8", "ou": "fiche", "texte": "fiche disparue"}); continue
        for ch in champs:
            if ch not in actuel[i]:
                defauts[i].append({"code": "A8", "ou": ch, "texte": "valeur remplie disparue"})
    vertes = [i for i in fiches if not defauts.get(i)]
    par_code = {}
    for i, L in defauts.items():
        for x in L:
            par_code[x["code"]] = par_code.get(x["code"], 0) + 1
    completes = [i for i, d in fiches.items() if all(not (isinstance(d.get(b), str) and d[b] == AP) for b in BLOCS)]
    rapport = {"_meta": {"producteur": "conception/outils/paraclinique/auditer_biologie.py (0 token)",
                         "regle": "vert = 0 défaut A1–A10 ; complète = aucun bloc « à produire »"},
               "resume": {"fiches": len(fiches), "vertes": len(vertes), "rouges": len(fiches) - len(vertes),
                          "completes": len(completes), "defauts_par_code": dict(sorted(par_code.items()))},
               "defauts": {i: L for i, L in sorted(defauts.items()) if L}}
    with open(RAPPORT, "w", encoding="utf-8") as f:
        f.write(json.dumps(rapport, ensure_ascii=False, indent=1) + "\n")
    if a.liste:
        for i, L in sorted(defauts.items()):
            for x in L:
                print(f"{x['code']} · {i} · {x['ou']} · {x['texte'][:140]}")
    vert = len(vertes) == len(fiches)
    print(f"AUDIT BIOLOGIE : {len(vertes)}/{len(fiches)} fiches vertes · {len(completes)} complètes · défauts {rapport['resume']['defauts_par_code']}")
    if a.maj and (vert or not os.path.exists(NONPERTE)):  # 1re génération : l'instantané de base se pose même si l'audit est rouge
        fus = {i: {**ancien.get(i, {}), **actuel.get(i, {})} for i in set(ancien) | set(actuel)}
        with open(NONPERTE, "w", encoding="utf-8") as f:
            f.write(json.dumps({"_meta": {"role": "Instantané de non-perte (chemin → empreinte) ; union des générations."},
                                "fiches": dict(sorted(fus.items()))}, ensure_ascii=False, indent=0, sort_keys=True) + "\n")
        print("instantané de non-perte mis à jour")
    sys.exit(0 if vert else 1)


if __name__ == "__main__":
    main()
