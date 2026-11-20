"""COUCHE 1 — Fiches de raisonnement (1 par entité, 3 975 au total), via l'API Claude (Batch + cache).

La fiche est la SOURCE UNIQUE DE VÉRITÉ d'une entité : quoi faire en premier, drapeaux rouges, discriminants,
examens dans l'ordre, traitement suisse, chiffres clés sourcés, échelle 0-D → ancre, pièges, notions couvertes.
REJECTOR_ vérifie la fiche (3 975 audits au lieu de 119 242). Les items du jeu en dérivent ensuite :
  - couche 2 : generer_reflexes.py, par script, à 0 token ;
  - couche 3 : produire_items_claude.py, vignettes riches A/K', à partir de la fiche.

Ordre de production : du plus banal au plus rare (très fréquent → fréquent → urgences → peu fréquent → rare),
spécialité par spécialité. Les urgences vitales sont marquées dans chaque fiche.

Usage :
  python scripts/produire_fiches_claude.py pilote --spec CAR --n 2
  python scripts/produire_fiches_claude.py soumettre --spec CAR
  python scripts/produire_fiches_claude.py soumettre --max 500
  python scripts/produire_fiches_claude.py statut | recuperer | bilan
Options : --modele (défaut claude-sonnet-5-5), --sec (simulation sans appel API).
"""
import argparse, csv, datetime as dt, glob, json, os, re, sys, time

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(RACINE, "data", "ssp")
SORTIE = os.path.join(RACINE, "content", "fiches")
SUIVI = os.path.join(RACINE, "scripts", "batchs_fiches.json")
REGISTRE = os.path.join(RACINE, "registre_fiches.csv")
SCHEMA = json.load(open(os.path.join(RACINE, "scripts", "schema_fiche.json"), encoding="utf-8"))
SPEC = json.load(open(os.path.join(RACINE, "data", "references", "entite_specialites.json"), encoding="utf-8"))
MODELE_DEFAUT = "claude-sonnet-5-5"
DEBUT = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
FREQ = {"TF": 1, "F": 2, None: 3, "MF": 4, "R": 5}   # None = entités issues de la table des urgences, sans strate de fréquence
CODE_SPEC = {k: v["code"] for k, v in SPEC["specialites"].items()}

SYSTEME = """Tu es Professeur de médecine et examinateur de l'examen fédéral suisse de médecine humaine. Tu rédiges la FICHE DE RAISONNEMENT d'une entité clinique pour le jeu « MedSuisse Arena 45 ». Cette fiche est la source unique de vérité : tous les QCM et réflexes du jeu en seront dérivés automatiquement. Son but est de rendre le candidat brillant et instantané : savoir quoi faire EN PREMIER, puis ensuite, puis ensuite, en comprenant pourquoi.

RÈGLES BLOQUANTES
1. Français ; chaque phrase contient un verbe conjugué ; aucune phrase nominale (les champs courts comme « signe », « valeur » ou « examen » peuvent être nominaux).
2. Exactitude absolue. Posologies selon la cascade suisse : AIPS Swissmedic, puis Compendium.ch, puis sociétés savantes et hôpitaux universitaires suisses, puis sociétés européennes. Mécanismes universels : références internationales de premier plan. Un chiffre dont tu n'es pas certain n'est pas écrit.
3. premiersGestes : l'ordre exact de la conduite réelle ; le geste 1 est celui qui sauve ou qui oriente le plus vite. Chaque geste dit pourquoi il vient à ce rang.
4. presentation.typique : chaque élément est relié à son mécanisme (pourquoi le signe existe).
5. discriminants : les rivaux réels de l'entité dans ce SSP, et l'élément précis qui tranche.
6. examens et traitement : dans l'ordre chronologique, chacun avec son pourquoi ; traitement avec posologie complète si un médicament est en jeu.
7. ladder : zeroD (science fondamentale qui rend l'entité possible) → mechanism → semiology → discriminant → decision → trap → anchor (une phrase mémorable).
8. pieges : les erreurs réelles des candidats, typées, avec leur correction.
9. notionsCouvertes : une entrée par rubrique fournie, qui DÉVELOPPE toutes les notions exigibles de la rubrique (le poids indique combien), sans recopier l'amorce.
10. Les phrases génériques interchangeables d'une entité à l'autre sont interdites.
Tu réponds UNIQUEMENT en appelant l'outil emettre_fiche."""

OUTIL = {"name": "emettre_fiche", "description": "Émet la fiche de raisonnement de l'entité.",
         "input_schema": {k: v for k, v in SCHEMA.items() if k != "title"}}


def cibles():
    out = []
    for f in sorted(glob.glob(os.path.join(DATA, "SSP_*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for e in d["entites"]:
            specs = SPEC["entiteVersSpecialites"].get(e["id"], [])
            out.append({"id": re.sub(r"[^A-Za-z0-9_-]", "_", e["id"])[:64], "ssp": d["ssp"], "nomSSP": d["nom"], "circuit": d["circuit"],
                        "lot": d["lot"], "entite": e, "specs": specs, "codes": [CODE_SPEC.get(s, s) for s in specs],
                        "freq": FREQ.get(e.get("strate"), 3), "urgent": "urgence" in (e.get("tables") or [])})
    return out


def chemin(c):
    dossier = c["codes"][0] if c["codes"] else "SANS_SPEC"
    return os.path.join(SORTIE, dossier, f"{c['id']}.json")


def message(c):
    e = c["entite"]
    rub = "\n".join(f"- {n['rubrique']} [poids {n['poids']}] : « {n['amorce']} »" for n in e["notions"])
    rivaux = ", ".join(x["nom"] for x in json.load(open(glob.glob(os.path.join(DATA, f"SSP_{c['lot']:03d}_*.json"))[0], encoding="utf-8"))["entites"]
                       if x["id"] != e["id"])[:1500]
    return (f"SSP {c['ssp']} « {c['nomSSP']} » (circuit {c['circuit']}). Spécialités : {', '.join(c['codes']) or 'non attribuée'}.\n"
            f"Entité : {e['nom']} (CIM-10 {e.get('cim10')}, système {e.get('systeme')}, fréquence {e.get('strate')}, urgence {e.get('urgence')}).\n"
            f"Note : {e.get('note')}\nPrésentation connue : {json.dumps(e.get('presentation') or {}, ensure_ascii=False)[:1500]}\n"
            f"Autres entités du même SSP (rivaux possibles) : {rivaux}\n\nRubriques et notions à développer :\n{rub}")


def params(c, modele):
    return {"model": modele, "max_tokens": 16000,
            "system": [{"type": "text", "text": SYSTEME, "cache_control": {"type": "ephemeral"}}],
            "tools": [OUTIL], "tool_choice": {"type": "tool", "name": "emettre_fiche"},
            "messages": [{"role": "user", "content": message(c)}]}


def valider(fiche, c):
    import jsonschema
    try:
        jsonschema.validate(fiche, SCHEMA)
    except jsonschema.ValidationError as ex:
        return [f"SCHEMA: {ex.message[:160]}"]
    err = []
    attendues = {n["rubrique"] for n in c["entite"]["notions"]}
    vues = {n["rubrique"] for n in fiche["notionsCouvertes"]}
    if attendues - vues:
        err.append(f"rubriques non couvertes : {sorted(attendues - vues)}")
    if [g["ordre"] for g in fiche["premiersGestes"]] != list(range(1, len(fiche["premiersGestes"]) + 1)):
        err.append("premiersGestes mal numérotés")
    return err


def ecrire(c, fiche, modele, usage, err):
    p = chemin(c); os.makedirs(os.path.dirname(p), exist_ok=True)
    out = {"id": c["entite"]["id"], "ssp": c["ssp"], "entite": c["entite"]["nom"], "cim10": c["entite"].get("cim10"),
           "specialtyIds": c["specs"], "notionRefs": [f"{c['ssp']}/{c['entite']['id']}/{n['rubrique']}" for n in c["entite"]["notions"]],
           "poidsNotions": c["entite"].get("poidsTotal"), **fiche,
           "controles": {"erreurs": err}, "signature": {"start": DEBUT, "model": modele, "platform": "API Claude (Message Batches)"},
           "audit": {"rejector": None, "human": None}}
    json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    neuf = not os.path.exists(REGISTRE)
    with open(REGISTRE, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        if neuf:
            w.writerow(["date", "entite", "spec", "erreurs", "modele", "in", "cache_lu", "out"])
        w.writerow([dt.datetime.now().isoformat(timespec="seconds"), c["id"], "/".join(c["codes"]), len(err), modele,
                    usage.get("input_tokens"), usage.get("cache_read_input_tokens"), usage.get("output_tokens")])


def selection(a):
    cs = [c for c in cibles() if not os.path.exists(chemin(c))]
    if a.spec:
        cs = [c for c in cs if a.spec.upper() in c["codes"]]
    if a.ssp:
        cs = [c for c in cs if c["ssp"] == a.ssp]
    cs.sort(key=lambda c: (c["freq"], (c["codes"] or ["ZZZ"])[0], c["id"]))   # du plus banal au plus rare
    return cs[: a.max] if a.max else cs


def client():
    import anthropic
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY absente : voir PROCEDURE_CREDITS_CLAUDE.md.")
    return anthropic.Anthropic()


def pilote(a):
    cs = selection(a)[: a.n]
    if a.sec:
        print(params(cs[0], a.modele)["messages"][0]["content"][:2500]); return
    cl = client()
    for c in cs:
        t = time.time(); m = cl.messages.create(**params(c, a.modele))
        b = next(x for x in m.content if x.type == "tool_use"); err = valider(b.input, c)
        ecrire(c, b.input, a.modele, m.usage.model_dump(), err)
        print(f"{c['id']} ({'/'.join(c['codes'])}) : {len(err)} erreur(s), {m.usage.output_tokens} tokens de sortie, {time.time()-t:.0f} s → {chemin(c)}")


def soumettre(a):
    cs = selection(a)
    print(f"{len(cs)} fiche(s) à produire" + (f", de {cs[0]['id']} à {cs[-1]['id']}." if cs else "."))
    if a.sec or not cs:
        return
    cl = client(); suivi = json.load(open(SUIVI)) if os.path.exists(SUIVI) else []
    for i in range(0, len(cs), 5000):
        tr = cs[i:i + 5000]
        b = cl.messages.batches.create(requests=[{"custom_id": c["id"], "params": params(c, a.modele)} for c in tr])
        suivi.append({"batch": b.id, "modele": a.modele, "n": len(tr), "recupere": False}); print(f"Batch {b.id} : {len(tr)} fiches.")
    json.dump(suivi, open(SUIVI, "w"), indent=1)


def statut(a):
    cl = client()
    for s in json.load(open(SUIVI)) if os.path.exists(SUIVI) else []:
        b = cl.messages.batches.retrieve(s["batch"]); print(s["batch"], b.processing_status, b.request_counts.model_dump())


def recuperer(a):
    cl = client(); suivi = json.load(open(SUIVI)) if os.path.exists(SUIVI) else []; idx = {c["id"]: c for c in cibles()}
    for s in suivi:
        if s["recupere"] or cl.messages.batches.retrieve(s["batch"]).processing_status != "ended":
            continue
        ok = ko = 0
        for r in cl.messages.batches.results(s["batch"]):
            c = idx.get(r.custom_id)
            b = next((x for x in r.result.message.content if x.type == "tool_use"), None) if r.result.type == "succeeded" else None
            if c is None or b is None:
                ko += 1; continue
            ecrire(c, b.input, s["modele"], r.result.message.usage.model_dump(), valider(b.input, c)); ok += 1
        s["recupere"] = True; print(f"{s['batch']} : {ok} fiches écrites, {ko} échecs (relancer « soumettre » les reprend).")
    json.dump(suivi, open(SUIVI, "w"), indent=1)


def bilan(a):
    cs = cibles(); faites = [c for c in cs if os.path.exists(chemin(c))]
    print(f"Fiches : {len(faites)}/{len(cs)} ({100*len(faites)/len(cs):.1f} %)")
    for k, lib in ((1, "très fréquentes"), (2, "fréquentes"), (3, "urgences"), (4, "peu fréquentes"), (5, "rares")):
        t = [c for c in cs if c["freq"] == k]; f = [c for c in t if os.path.exists(chemin(c))]
        print(f"  {lib:15s} {len(f)}/{len(t)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    for nom in ("pilote", "soumettre", "statut", "recuperer", "bilan"):
        p = sp.add_parser(nom); p.add_argument("--spec"); p.add_argument("--ssp"); p.add_argument("--max", type=int)
        p.add_argument("--n", type=int, default=2); p.add_argument("--modele", default=MODELE_DEFAUT); p.add_argument("--sec", action="store_true")
    a = ap.parse_args(); globals()[a.cmd](a)
