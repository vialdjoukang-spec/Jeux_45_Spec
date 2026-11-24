"""Chaîne Notions → Questions du jeu 45 Spec (pipeline i-Med, API Anthropic, lots à moitié prix).

Hiérarchie : Spécialité → Pathologie (entité de la Cartographie Renouveau, plan monographique en 15 rubriques ou plan
non monographique du SSP) → Notions atomiques → Questions (A à 5 options, Kprim à 4 affirmations, Menu long,
séries progressives à diagnostic masqué) → couverture (une notion se coche quand des questions auditées l'explorent).

Une NOTION est l'une des entités informationnelles individuelles que l'on peut tirer de la pathologie : un chiffre, un seuil,
un critère, un mécanisme, un signe, un examen et son résultat, une décision, une molécule et sa posologie, un piège, une
particularité suisse, une complication, un pronostic, une mesure de prévention.

Étape 1 « notions »   : python scripts/produire_notions_questions.py notions   pilote|soumettre|recuperer --spec END [--n 3] [--id ID]
Étape 2 « questions » : python scripts/produire_notions_questions.py questions pilote|soumettre|recuperer --spec END [--n 3] [--id ID]
Couverture (0 token)  : python scripts/couverture_notions.py
Signature : AAI (Anthropic AI)"""
import argparse, datetime as dt, json, os, re, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import produire_fiches_claude as PF  # noqa: E402  (cibles, client, options apprises, rivaux)

R = PF.RACINE; MODELE = PF.MODELE_DEFAUT
DOS = {"notions": os.path.join(R, "content", "notions"), "questions": os.path.join(R, "content", "questions"), "correction": os.path.join(R, "content", "corrections")}
PEC = {k: v for k, v in json.load(open(os.path.join(R, "conception", "donnees", "schemas", "prise_en_charge.json"), encoding="utf-8")).items() if not k.startswith(("$", "_", "title"))}
SUIVI = os.path.join(R, "scripts", "batchs_notions_questions.json")
RUBRIQUES = ["definition", "epidemiology", "basicSciences", "anamnesis", "clinicalExam", "presumptionRedFlags", "workupGoldStandard",
             "workupAlternatives", "positiveDiagnosis", "acuteManagement", "chronicManagement", "hospitalizationComplications",
             "prognosisDischarge", "surveillance", "followUpNetwork"]
NATURES = ["chiffre", "seuil", "critère", "mécanisme", "signe", "symptôme", "examen", "résultat", "décision", "molécule", "posologie",
           "piège", "contexte suisse", "complication", "pronostic", "prévention", "terrain particulier", "diagnostic différentiel"]
S = lambda d="", **k: {"type": "string", **({"description": d} if d else {}), **k}
L = lambda it, a, b, d="": {"type": "array", "minItems": a, "maxItems": b, "items": it, **({"description": d} if d else {})}
O = lambda p, req=None: {"type": "object", "additionalProperties": False, "required": req or list(p), "properties": p}

SCH_NOTIONS = O({
    "plan": {"type": "string", "enum": ["monographique", "non_monographique"]},
    "notions": L(O({"id": S("N01, N02…"), "rubrique": {"type": "string", "enum": RUBRIQUES}, "nature": {"type": "string", "enum": NATURES},
                    "enonce": S("Phrase verbale, exacte et sourcée si chiffrée : ce que le candidat doit savoir."),
                    "poids": {"type": "integer", "minimum": 1, "maximum": 3}, "suisse": {"type": "boolean"},
                    "source": S("[Société, année] ou AIPS ; chaîne vide pour une notion de mécanisme universel.")}), 25, 70),
    "anglesMorts": L(S("Notion qu'un examinateur suisse pourrait demander et qu'un candidat ignore souvent, déjà incluse ci-dessus."), 3, 8)})
QUESTION = O({
    "id": S("Q01…"), "format": {"type": "string", "enum": ["A", "Kprim", "MenuLong"]},
    "situation": {"type": "string", "enum": ["starting_point", "monographique"],
                  "description": "starting_point : le cas part d'une plainte ou d'un résultat, sans nommer la pathologie ; monographique : la pathologie est nommée comme outil de travail."},
    "diagnosticMasque": {"type": "boolean"},
    "serie": {"anyOf": [O({"id": S("S1, S2…"), "etape": {"type": "integer"}, "total": {"type": "integer"}}), {"type": "null"}],
              "description": "Cas progressif : le même patient est suivi d'une question à l'autre ; null pour une question isolée."},
    "stem": S("Vignette clinique suisse réaliste (lieu, âge, contexte), sans indice du diagnostic si diagnosticMasque."),
    "prompt": S("La question posée."),
    "options": L(O({"key": S(), "text": S(), "correct": {"type": "boolean"}, "why": S("Pourquoi elle est juste ou fausse, une phrase.")}), 0, 20,
                 "A : exactement 5 options, une seule juste. MenuLong : 12 à 20 options, une à trois justes. Kprim : liste vide."),
    "statements": L(O({"text": S(), "true": {"type": "boolean"}, "why": S()}), 0, 4, "Kprim : exactement 4 affirmations ; sinon liste vide."),
    "notions": L(S("Identifiant de notion couverte"), 1, 6), "angle": {"type": "string", "enum": ["direct", "application", "piège"]},
    "difficulte": {"type": "integer", "minimum": 1, "maximum": 5},
    "ladder": O({k: S() for k in ("zeroD", "mechanism", "semiology", "discriminant", "decision", "trap", "anchor")}),
    "sources": L(S(), 1, 4)})
SCH_QUESTIONS = O({"questions": L(QUESTION, 16, 24)})
CELLULE = {"anyOf": [S(), L(O({"t": S("Terme surligné"), "i": S("POURQUOI, en une à deux phrases : mécanisme, essai ou conséquence, et pourquoi pas les autres.")}), 1, 6)]}
NOEUD = O({"id": S("n1, n2…"), "parent": {"anyOf": [S(), {"type": "null"}]}, "t": S("Texte court de la case"),
           "i": S("Pourquoi, seuil ou définition : aucune case muette."), "pec": {"anyOf": [S("Clé d'un plan de priseEnCharge ci-dessous"), {"type": "null"}]},
           "notion": {"anyOf": [S("id d'une notion de cours ci-dessous"), {"type": "null"}]}})
SCH_CORRECTION = O({
    "theme": S(),
    "notions": L(O({"id": S("c1, c2…"), "titre": S(), "rubriques": L({"type": "string", "enum": RUBRIQUES}, 1, 4),
                    "comment": S("Une phrase verbale : comment raisonner."),
                    "tableau": {"anyOf": [O({"colonnes": L(S(), 2, 6), "lignes": L(L(CELLULE, 2, 6), 2, 20, "La 1re colonne répète la classe sur chaque ligne de ses sous-classes.")}), {"type": "null"}]},
                    "arbre": {"anyOf": [L(NOEUD, 3, 30, "Arbre décisionnel à plat : chaque nœud cite son parent (null pour la racine)."), {"type": "null"}]},
                    "points": L(S(), 1, 5), "sources": L(S(), 1, 4)}), 4, 9),
    "ssp": O({"code": S(), "nom": S(), "officiel": {"type": "boolean"}, "algorithme": L(NOEUD, 6, 40, "Algorithme décisionnel du SSP à plat ; chaque feuille porte un « i » et, si c'est un aboutissement thérapeutique, une clé « pec ».")}),
    "priseEnCharge": L(O({"cle": S(), "titre": S(), **PEC["properties"]}, ["cle", "titre"] + PEC["required"]), 1, 4)})


REGLES = """RÈGLES BLOQUANTES (examen fédéral suisse de médecine humaine, format PROFILES)
1. Français ; chaque phrase contient un verbe conjugué ; aucune phrase nominale.
2. Exactitude absolue : recommandations suisses d'abord (AIPS Swissmedic, OFSP, sociétés suisses), puis européennes ; un chiffre incertain n'est pas écrit.
3. Question à se poser en permanence : « Sur cette pathologie, en contexte suisse, que pourrait-on demander au candidat qu'il ne saurait pas ? » Aucun angle mort.
4. Concision dense : chaque énoncé et chaque « why » tient en une phrase de 30 mots au plus."""

SYS_N = f"""Tu es examinateur de l'examen fédéral suisse. Tu dresses la LISTE EXHAUSTIVE DES NOTIONS d'une pathologie : chaque notion est une entité informationnelle individuelle que l'on peut tirer de la pathologie et sur laquelle on peut poser une question.
{REGLES}
5. Plan monographique : couvre les 15 rubriques ; le nombre de notions d'une rubrique suit son poids (poids 1 : 1 à 3 notions ; poids 2 : 3 à 5 ; poids 3 : 5 à 8). Plan non monographique : centre-toi sur la démarche du SSP (drapeaux rouges, discriminants face aux rivaux, examen qui tranche, décision).
5bis. Poids de la notion : poids 3 pour au plus 15 % des notions (le noyau indispensable), poids 2 pour au plus 35 %, poids 1 pour le reste.
6. Une notion = une seule information vérifiable ; pas de doublon ; marque « suisse » ce qui dépend de la pratique, du droit, des assurances ou des recommandations suisses.
Tu réponds UNIQUEMENT en appelant l'outil emettre_notions."""

SYS_Q = f"""Tu es examinateur de l'examen fédéral suisse. À partir de la liste des notions d'une pathologie, tu écris des QUESTIONS de niveau examen qui explorent les contours de chaque notion.
{REGLES}
5. Formats, dans la proportion de l'examen fédéral : environ 70 % de type A (exactement 5 options dont une seule juste, distracteurs plausibles du même registre), 20 % de Kprim (exactement 4 affirmations vrai/faux) et 10 % de menu long (12 à 20 options homogènes : diagnostics, examens ou molécules ; une à trois justes).
6. Situation as Starting Point d'abord : la majorité des vignettes partent d'une plainte, d'un signe ou d'un résultat, et le diagnostic n'y figure pas (diagnosticMasque = true) ; aucun mot de la vignette, du titre ou de la question ne trahit le diagnostic.
7. Écris au moins une SÉRIE progressive de 3 à 5 étapes : le même patient, suivi du premier contact à la sortie ou au suivi, chaque étape révélant de nouvelles données ; le diagnostic reste masqué jusqu'à ce qu'une étape demande de le poser.
8. Chaque question cite 1 à 6 notions couvertes ; chaque notion de poids 2 ou 3 est couverte au moins deux fois sous deux angles différents (direct, application, piège).
8bis. BUDGET DE SORTIE STRICT : produis entre 18 et 20 questions, pas davantage, sinon la réponse est tronquée. Chaque question cite 3 à 6 notions ; les Kprim et les menus longs servent à couvrir beaucoup de notions à la fois. Vignettes de 60 mots au plus, « why » de 15 mots au plus, ladder de 12 mots par champ, un seul source par question. Le jeu comporte environ 14 type A, 4 Kprim, 2 menus longs.
8ter. COUVERTURE OBLIGATOIRE (contrôle automatique après ta réponse) : avant d'émettre, dresse mentalement la liste de TOUTES les notions de poids 2 ou 3 ; chacune doit figurer dans le champ « notions » d'au moins DEUX questions, dont les « angle » diffèrent (par ex. direct puis application ou piège). Répartis-les : une question en cite 3 à 6, JAMAIS plus de 6 (le schéma rejette 7 ou plus). Les notions de poids 1 se glissent dans les Kprim et les menus longs. Vérifie à la fin que aucune notion de poids ≥ 2 n'est citée une seule fois.
9. ladder : zéro-D → mécanisme → sémiologie → discriminant → décision → piège → ancre, une phrase chacun.
Tu réponds UNIQUEMENT en appelant l'outil emettre_questions."""
SYS_C = f"""Tu es examinateur de l'examen fédéral suisse et pédagogue. Tu écris la CORRECTION ENRICHIE d'une pathologie, qui sert de révision après chaque question.
{REGLES}
5. notions : 4 à 9 notions de cours, ordonnées simplement ; chacune a une phrase « comment » et, si c'est utile, un TABLEAU (ex. classe | sous-classe | chef de file | discriminant | particularité) dont chaque discriminant et chaque particularité est une cellule {{t, i}} où « i » dit POURQUOI (et pourquoi pas les autres), ou un ARBRE (escalade, démarche) dont chaque case porte son « i ».
6. ssp : le SSP de départ le plus représentatif parmi les portes d'entrée (officiel PROFILES ou additionnel) et son algorithme décisionnel complet ; aucune case muette ; les aboutissements thérapeutiques renvoient à un plan « pec » ; une case qui sort du cadre dit vers quel SSP elle renvoie.
7. priseEnCharge : 1 à 4 plans (par exemple urgence, forme non compliquée, long cours) au schéma holistique : but, moyens (accueil, pharmacologique avec posologies suisses, non pharmacologique, disciplines transversales), conduite en équipe urgence | hors urgence, pronostic, surveillance et critères de sortie, prévention ; dense et concis.
Tu réponds UNIQUEMENT en appelant l'outil emettre_correction."""


def cle(s):
    return re.sub(r"[^a-z0-9]+", " ", unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()).strip()


def canon(c):
    """Pathologie canonique : une même maladie apparaît dans plusieurs SSP (portes d'entrée) ; ses notions ne se produisent qu'une fois."""
    return (c["entite"].get("cim10") or "").strip() or cle(c["entite"]["nom"])[:40]


def canoniques(spec=None):
    VIDE = {"de", "du", "la", "le", "les", "des", "et", "ou", "sur", "avec", "sans", "par", "aigue", "aigu", "chronique", "syndrome", "maladie", "severe"}
    mots = lambda c: {m for m in cle(c["entite"]["nom"]).split() if len(m) > 2 and m not in VIDE}
    import glob
    FUS = {e: g["nom"] for f in glob.glob(os.path.join(R, "content", "pathologies", "fusions_*.json")) for g in json.load(open(f, encoding="utf-8"))["groupes"] for e in g["entites"]}
    grp = {}
    for c in PF.cibles():
        if spec and spec.upper() not in c["codes"]:
            continue
        if c["entite"]["id"] in FUS:                 # fusion validée par Claude (content/pathologies/fusions_<SPEC>.json)
            grp.setdefault("F:" + FUS[c["entite"]["id"]], []).append(c); continue
        k0 = canon(c); m = mots(c); n = 0
        while True:                    # même CIM-10 mais noms sans rapport (ex. diabète et mal perforant) : grappes distinctes
            k = k0 if n == 0 else f"{k0}~{n}"
            if k not in grp or any(len(m & mots(x)) / max(1, min(len(m), len(mots(x)))) >= 0.5 for x in grp[k]):
                grp.setdefault(k, []).append(c); break
            n += 1
    out = []
    for k, L in grp.items():
        rep = min(L, key=lambda c: (len(re.sub(r"\s*\(.*?\)", "", c["entite"]["nom"])), c["id"]))   # nom le plus monographique
        if k.startswith("F:"):
            rep = {**rep, "entite": {**rep["entite"], "nom": k[2:]}}; k = (rep["entite"].get("cim10") or "F") + "_" + cle(k[2:])[:20].replace(" ", "_")
        out.append({**rep, "freq": min(c["freq"] for c in L), "urgent": any(c["urgent"] for c in L),
                    "codes": sorted({x for c in L for x in c["codes"]}, key=lambda x: (x not in rep["codes"], x)),
                    "id": re.sub(r"[^A-Za-z0-9_.-]", "_", k)[:40] + "__" + min(c["id"] for c in L),
                    "portes": [{"ssp": c["ssp"], "nomSSP": c["nomSSP"], "entite": c["entite"]["nom"], "entiteId": c["entite"]["id"]} for c in L]})
    return sorted(out, key=lambda c: (c["freq"], c["id"]))


def chemin(etape, c):
    return os.path.join(DOS[etape], (c["codes"] or ["SANS_SPEC"])[0], c["id"] + ".json")


def message(etape, c):
    base = PF.message(c) + "\n\nPORTES D'ENTRÉE (situations où cette pathologie se présente ; chacune fournit des starting points) :\n" + \
        "\n".join(f"- SSP {p['ssp']} « {p['nomSSP']} » : {p['entite']}" for p in c.get("portes", []))
    if etape == "notions":
        return base + f"\n\nPlan attendu : {'monographique' if c['circuit'] != 'NON_MONOGRAPHIQUE' else 'non_monographique'}."
    n = json.load(open(chemin("notions", c), encoding="utf-8"))
    if etape == "correction":
        return base + "\n\nNOTIONS DE LA PATHOLOGIE (à reprendre en cours ordonnés) :\n" + "\n".join(f"{x['id']} [{x['rubrique']}] {x['enonce']}" for x in n["notions"])
    return base + "\n\nNOTIONS À COUVRIR :\n" + "\n".join(f"{x['id']} [{x['rubrique']}, {x['nature']}, poids {x['poids']}] {x['enonce']}" for x in n["notions"])


def params(etape, c):
    opt = json.load(open(PF.OPTIONS)) if os.path.exists(PF.OPTIONS) else {}
    sch, sysp, nom = {"notions": (SCH_NOTIONS, SYS_N, "emettre_notions"), "questions": (SCH_QUESTIONS, SYS_Q, "emettre_questions"),
                      "correction": (SCH_CORRECTION, SYS_C, "emettre_correction")}[etape]
    return {"model": MODELE, "max_tokens": 60000, **({"thinking": {"type": "disabled"}} if opt.get("thinking_desactivable", True) else {}),
            "system": [{"type": "text", "text": sysp, "cache_control": {"type": "ephemeral"}}],
            "tools": [{"name": nom, "description": "Émet le résultat structuré.", "input_schema": sch}], "tool_choice": {"type": "auto"},
            "messages": [{"role": "user", "content": message(etape, c)}]}


def valider(etape, d, c):
    import jsonschema
    try:
        jsonschema.validate(d, {"notions": SCH_NOTIONS, "questions": SCH_QUESTIONS, "correction": SCH_CORRECTION}[etape])
    except jsonschema.ValidationError as ex:
        return [f"SCHEMA: {ex.message[:160]}"]
    err = []
    if etape == "notions":
        ids = [n["id"] for n in d["notions"]]
        if len(ids) != len(set(ids)):
            err.append("identifiants de notions en double")
        manque = set(RUBRIQUES) - {n["rubrique"] for n in d["notions"]} if d["plan"] == "monographique" else set()
        if manque:
            err.append(f"rubriques sans notion : {sorted(manque)}")
        return err
    if etape == "correction":
        cles = {p["cle"] for p in d["priseEnCharge"]}; ids_n = {n["id"] for n in d["notions"]}
        for nom, arbre in [("ssp", d["ssp"]["algorithme"])] + [(n["id"], n["arbre"] or []) for n in d["notions"]]:
            ids = {x["id"] for x in arbre}; parents = {x["parent"] for x in arbre}
            for x in arbre:
                if x["parent"] and x["parent"] not in ids:
                    err.append(f"{nom} : parent inconnu {x['parent']}")
                if x["id"] not in parents and not (x["i"] or x["pec"] or x["notion"]):
                    err.append(f"{nom} : feuille muette « {x['t'][:30]} »")
                if x["pec"] and x["pec"] not in cles:
                    err.append(f"{nom} : plan pec inconnu {x['pec']}")
                if x["notion"] and x["notion"] not in ids_n:
                    err.append(f"{nom} : notion inconnue {x['notion']}")
        return err
    nid = {n["id"] for n in json.load(open(chemin("notions", c), encoding="utf-8"))["notions"]}
    mots = [m for m in cle(c["entite"]["nom"]).split() if len(m) > 4][:3]
    for q in d["questions"]:
        f = q["format"]; no = len(q["options"]); ns = len(q["statements"])
        if f == "A" and (no != 5 or sum(o["correct"] for o in q["options"]) != 1):
            err.append(f"{q['id']} : un type A exige 5 options et une seule juste")
        if f == "Kprim" and ns != 4:
            err.append(f"{q['id']} : un Kprim exige 4 affirmations")
        if f == "MenuLong" and not 12 <= no <= 20:
            err.append(f"{q['id']} : un menu long exige 12 à 20 options")
        if q["diagnosticMasque"] and mots and all(m in cle(q["stem"] + " " + q["prompt"]) for m in mots):
            err.append(f"{q['id']} : la vignette nomme le diagnostic masqué")
        if set(q["notions"]) - nid:
            err.append(f"{q['id']} : notions inconnues {sorted(set(q['notions']) - nid)}")
    return err


def ecrire(etape, c, d, usage, err):
    p = chemin(etape, c); os.makedirs(os.path.dirname(p), exist_ok=True)
    if etape == "notions":
        for n in d["notions"]:
            n["couverture"] = {"questions": [], "cochee": False}
    out = {"id": c["id"], "portes": c.get("portes", []), "entite": c["entite"]["nom"], "cim10": c["entite"].get("cim10"), "ssp": c["ssp"], "specialites": c["codes"],
           "circuit": c["circuit"], **d, "controles": {"erreurs": err}, "usage": usage,
           "signature": {"date": dt.datetime.now().isoformat(timespec="seconds"), "modele": MODELE, "auteur": "AAI (Anthropic AI)"},
           "audit": {"rejector": None, "claude": None}}
    json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def selection(etape, a):
    vus, cs = set(), []
    for sp in (a.spec.split(",") if a.spec else [None]):          # plusieurs spécialités en un seul lot ; une pathologie commune n'est produite qu'une fois
        for c in canoniques(sp):
            if c["id"] not in vus and (not a.id or any(x in c["id"] for x in a.id.split(","))):
                vus.add(c["id"]); cs.append(c)
    cs = [c for c in cs if not os.path.exists(chemin(etape, c))]
    if etape in ("questions", "correction"):
        cs = [c for c in cs if os.path.exists(chemin("notions", c))]
    rang = os.path.join(R, "content", "pathologies", "RANG_RENDEMENT.json")    # classement par rendement à l'examen (scripts/classer_rendement.py)
    RG = json.load(open(rang, encoding="utf-8"))["pathologies"] if os.path.exists(rang) else {}
    SUF = {k.split("__")[-1]: v for k, v in RG.items()}      # pathologie fusionnée : id canonique nouveau → meilleur rang de ses portes d'entrée
    def rg(c):
        m = [SUF[p["entiteId"].replace(".", "_")] for p in c.get("portes", []) if p["entiteId"].replace(".", "_") in SUF]
        return RG.get(c["id"]) or (min(m, key=lambda x: x["rang"]) if m else {})
    if getattr(a, "groupe", None):
        cs = [c for c in cs if rg(c).get("groupe") in a.groupe.split(",")]
    cs.sort(key=lambda c: (rg(c).get("rang", 10 ** 6), c["freq"], c["id"]))
    return cs[: a.max] if a.max else cs


def pilote(etape, a):
    cl = PF.client()
    for c in selection(etape, a)[: a.n]:
        with cl.messages.stream(**params(etape, c)) as fl:
            m = fl.get_final_message()
        b = next((x for x in m.content if x.type == "tool_use"), None)
        if b is None:
            print(c["id"], ": pas d'appel d'outil"); continue
        err = valider(etape, b.input, c); ecrire(etape, c, b.input, {**m.usage.model_dump(), "_mode": "direct"}, err)
        print(f"{etape} {c['id']} : {len(err)} erreur(s), {m.usage.output_tokens} tokens de sortie → {os.path.relpath(chemin(etape, c), R)}")


def soumettre(etape, a):
    cs = selection(etape, a); print(f"{etape} : {len(cs)} entité(s) à produire.")
    if not cs:
        return
    cl = PF.client(); suivi = json.load(open(SUIVI)) if os.path.exists(SUIVI) else []
    ids = {f"{etape[0]}{i:05d}": c["id"] for i, c in enumerate(cs)}       # custom_id : ^[a-zA-Z0-9_-]{1,64}$ exigé par l'API
    b = cl.messages.batches.create(requests=[{"custom_id": k, "params": params(etape, next(c for c in cs if c["id"] == v))} for k, v in ids.items()])
    suivi.append({"batch": b.id, "etape": etape, "n": len(cs), "recupere": False, "ids": ids}); json.dump(suivi, open(SUIVI, "w"), indent=1); print("lot", b.id)


def recuperer(etape, a):
    cl = PF.client(); suivi = json.load(open(SUIVI)) if os.path.exists(SUIVI) else []; idx = {c["id"]: c for c in canoniques()}
    for s in suivi:
        if s["recupere"] or s["etape"] != etape or cl.messages.batches.retrieve(s["batch"]).processing_status != "ended":
            continue
        ok = ko = 0
        for r in cl.messages.batches.results(s["batch"]):
            c = idx.get(s.get("ids", {}).get(r.custom_id) or r.custom_id.split("|", 1)[-1])
            b = next((x for x in r.result.message.content if x.type == "tool_use"), None) if r.result.type == "succeeded" else None
            if c is None or b is None:
                ko += 1; continue
            ecrire(etape, c, b.input, {**r.result.message.usage.model_dump(), "_mode": "lot"}, valider(etape, b.input, c)); ok += 1
        s["recupere"] = True; print(f"{s['batch']} : {ok} écrites, {ko} échecs.")
    json.dump(suivi, open(SUIVI, "w"), indent=1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("etape", choices=["notions", "questions", "correction"]); ap.add_argument("mode", choices=["pilote", "soumettre", "recuperer"])
    ap.add_argument("--spec"); ap.add_argument("--id"); ap.add_argument("--n", type=int, default=3); ap.add_argument("--max", type=int); ap.add_argument("--groupe", help="groupes de rendement A,B,C,D (RANG_RENDEMENT.json)")
    a = ap.parse_args(); {"pilote": pilote, "soumettre": soumettre, "recuperer": recuperer}[a.mode](a.etape, a)
