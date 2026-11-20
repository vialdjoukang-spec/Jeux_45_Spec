"""Production des QCM du jeu en fichiers JSON, avec l'API Claude (Message Batches + cache de prompt).

Une requête = une rubrique d'une entité de la Cartographie. Elle produit `poids` items (au moins 1).
Sortie : content/items/<SSP>/<entityId>/<rubrique>.json  (+ registre_production.csv)

Usage (PowerShell, depuis la racine du dépôt) :
  python scripts/produire_items_claude.py pilote --ssp G1 --n 3          # 3 requêtes immédiates, pour juger la qualité et le coût
  python scripts/produire_items_claude.py soumettre --ssp G1             # un SSP entier en batch (−50 %)
  python scripts/produire_items_claude.py soumettre --priorite --max 2000 # les 2000 requêtes les plus prioritaires
  python scripts/produire_items_claude.py statut                          # état des batchs lancés
  python scripts/produire_items_claude.py recuperer                       # télécharge, valide et écrit les JSON
  python scripts/produire_items_claude.py bilan                           # avancement global
Options : --modele (défaut claude-sonnet-5-5), --sec (simulation sans appel API).
Clé : variable d'environnement ANTHROPIC_API_KEY.
"""
import argparse, csv, datetime as dt, glob, json, os, re, sys, time

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(RACINE, "data", "ssp")
SORTIE = os.path.join(RACINE, "content", "items")
SUIVI = os.path.join(RACINE, "scripts", "batchs.json")
REGISTRE = os.path.join(RACINE, "registre_production.csv")
SCHEMA = json.load(open(os.path.join(RACINE, "scripts", "schema_item.json"), encoding="utf-8"))
MODELE_DEFAUT = "claude-sonnet-5-5"
DEBUT = dt.datetime.now().strftime("%Y-%m-%d %H:%M")

RUBRIQUES_ZERO_D = {"definition", "basicSciences", "pathophysiology"}
LIBELLES = {"definition": "Définition", "epidemiology": "Épidémiologie", "biostatistics": "Biostatistiques",
            "basicSciences": "Sciences fondamentales", "pathophysiology": "Physiopathologie", "anamnesis": "Anamnèse",
            "clinicalExam": "Examen physique", "presumptionRedFlags": "Drapeaux rouges", "positiveDiagnosis": "Diagnostic positif",
            "workupGoldStandard": "Examen de référence", "workupAlternatives": "Examens alternatifs", "acuteManagement": "Prise en charge aiguë",
            "chronicManagement": "Prise en charge chronique", "hospitalizationComplications": "Hospitalisation et complications",
            "surveillance": "Surveillance", "prognosisDischarge": "Pronostic et sortie", "followUpNetwork": "Suivi et réseau"}

SYSTEME = """Tu es Professeur de médecine et concepteur d'items de l'examen fédéral suisse de médecine humaine. Tu produis des QCM pour le jeu « MedSuisse Arena 45 », dont le principe est : le candidat échoue, puis il apprend par une correction qui part de la science fondamentale (zéro-D) et monte jusqu'à la décision clinique suisse.

RÈGLES BLOQUANTES
1. Langue : français. Chaque phrase de chaque champ contient un verbe conjugué. Aucune phrase nominale.
2. Fond : exactitude absolue. Posologies selon la cascade suisse : AIPS Swissmedic, puis Compendium.ch, puis sociétés savantes et hôpitaux universitaires suisses, puis sociétés européennes. Mécanismes universels : références internationales de premier plan. Si tu n'es pas certain d'un chiffre, tu ne l'écris pas.
3. Format : type A = 5 options, 1 seule correcte, errorType = null pour la bonne réponse et un type d'erreur pour chaque distracteur. Type K' (Kprim) = 4 affirmations vrai/faux, sans champ options. Vise 60 % de A et 40 % de K' sur l'ensemble.
4. Chaque distracteur reproduit une erreur réelle de raisonnement ; son « why » nomme cette erreur et la corrige. Aucune justification générique ni répétée.
5. Échelle de correction (ladder), toujours propre à l'item : zeroD (science fondamentale qui rend l'entité possible) → mechanism (naissance et installation de la perturbation) → semiology (pourquoi chaque signe découle du mécanisme) → discriminant (ce qui sépare l'entité de ses rivales) → decision (conduite suisse et ordre) → trap (l'erreur que les distracteurs incarnent) → anchor (une phrase mémorable qui condense la notion).
6. Vignettes cliniques suisses réalistes (âge, contexte : cabinet, urgences CHUV/HUG/Inselspital, 144, permanence), sans identifiant de patient.
7. Difficulté de 1 (moyen) à 5 (grand maître) ; varie les niveaux.
8. Chaque item développe la notion indiquée ; ne recopie jamais l'amorce telle quelle.
9. transversalIds : lettres TRANS_A à TRANS_S pertinentes (A assurances, B biostatistique, C communication, D cybersanté, E diversité, F droit, G épidémiologie, H éthique, I génétique, J hygiène, K travail, L médecine légale, M palliatif, N prévention OFSP, O pharmacologie et sécurité, P qualité et erreur, Q radioprotection et Smarter Medicine, R santé planétaire, S urgences et triage), ou liste vide.
10. mediaQuery : une requête Wikimedia Commons pour une image réelle utile (ECG, imagerie, photo clinique), ou une chaîne vide.
Tu réponds UNIQUEMENT en appelant l'outil emettre_items."""

OUTIL = {"name": "emettre_items", "description": "Émet les items QCM produits pour la rubrique demandée.",
         "input_schema": {k: v for k, v in SCHEMA.items() if k not in ("$schema", "title")}}


def charger_cibles():
    """Liste ordonnée des requêtes : (custom_id, ssp, entité, rubrique, notion)."""
    cibles = []
    for f in sorted(glob.glob(os.path.join(DATA, "SSP_*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        for e in d["entites"]:
            urgent = "urgence" in (e.get("tables") or [])
            prio = (0 if urgent else {"TF": 1, "F": 2, "MF": 3, "R": 4}.get(e.get("strate"), 5))
            for n in e["notions"]:
                cid = re.sub(r"[^A-Za-z0-9_-]", "_", f"{e['id']}__{n['rubrique']}")[:64]
                cibles.append({"id": cid, "prio": prio, "lot": d["lot"], "ssp": d["ssp"], "nomSSP": d["nom"], "circuit": d["circuit"],
                               "entite": e, "rubrique": n["rubrique"], "poids": max(1, int(n["poids"] or 1)), "amorce": n["amorce"]})
    return cibles


def chemin_sortie(c):
    return os.path.join(SORTIE, c["ssp"].replace(".", "_"), c["entite"]["id"].replace(".", "_"), f"{c['rubrique']}.json")


def message_utilisateur(c):
    e = c["entite"]
    zero_d = "Au moins un item porte sur la science fondamentale (zéro-D)." if c["rubrique"] in RUBRIQUES_ZERO_D else \
             "La marche zeroD de chaque item rattache la notion à sa science fondamentale."
    pres = json.dumps(e.get("presentation") or {}, ensure_ascii=False)[:1500]
    return (f"SSP {c['ssp']} « {c['nomSSP']} » (circuit {c['circuit']}).\n"
            f"Entité : {e['nom']} (CIM-10 {e.get('cim10')}, système {e.get('systeme')}, urgence {e.get('urgence')}).\n"
            f"Note : {e.get('note')}\n"
            f"Présentation (typique/atypique) : {pres}\n\n"
            f"Rubrique : {LIBELLES.get(c['rubrique'], c['rubrique'])}.\n"
            f"Amorce de la notion à développer : « {c['amorce']} »\n"
            f"Poids : {c['poids']} → produis exactement {c['poids']} item(s), distincts et complémentaires, qui couvrent toutes les notions exigibles de cette rubrique. {zero_d}")


def params(c, modele):
    return {"model": modele, "max_tokens": 4000 * c["poids"] + 2000,
            "system": [{"type": "text", "text": SYSTEME, "cache_control": {"type": "ephemeral"}}],
            "tools": [OUTIL], "tool_choice": {"type": "tool", "name": "emettre_items"},
            "messages": [{"role": "user", "content": message_utilisateur(c)}]}


def valider(items_obj, c):
    """Contrôles 0 token : schéma + règles A/K' + longueur de l'échelle. Retourne la liste d'erreurs."""
    import jsonschema
    err = []
    try:
        jsonschema.validate(items_obj, SCHEMA)
    except jsonschema.ValidationError as ex:
        return [f"SCHEMA: {ex.message[:160]}"]
    for i, it in enumerate(items_obj["items"]):
        if it["format"] == "A":
            opts = it.get("options") or []
            if len(opts) != 5 or sum(o["correct"] for o in opts) != 1:
                err.append(f"item{i}: type A sans exactement 1 bonne réponse sur 5")
            if any((o["errorType"] is None) == (not o["correct"]) for o in opts):
                err.append(f"item{i}: errorType incohérent")
        else:
            if len(it.get("statements") or []) != 4:
                err.append(f"item{i}: K' sans 4 affirmations")
    if len(items_obj["items"]) < c["poids"]:
        err.append(f"{len(items_obj['items'])} item(s) pour un poids de {c['poids']}")
    return err


def ecrire(c, items_obj, modele, usage, erreurs):
    p = chemin_sortie(c); os.makedirs(os.path.dirname(p), exist_ok=True)
    sig = {"start": DEBUT, "model": modele, "platform": "API Claude (Message Batches)"}
    for k, it in enumerate(items_obj["items"], 1):
        it["id"] = f"{c['id']}-{k:02d}"
        it.update({"ssp": c["ssp"], "entityId": c["entite"]["id"], "rubric": c["rubrique"],
                   "notionRefs": [f"{c['ssp']}/{c['entite']['id']}/{c['rubrique']}"], "signature": sig,
                   "audit": {"A": None, "B": None, "rejector": None, "human": None}})
    out = {"ssp": c["ssp"], "entite": c["entite"]["nom"], "rubrique": c["rubrique"], "poids": c["poids"],
           "controles": {"erreurs": erreurs}, "items": items_obj["items"]}
    json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    neuf = not os.path.exists(REGISTRE)
    with open(REGISTRE, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        if neuf:
            w.writerow(["date", "custom_id", "ssp", "rubrique", "poids", "items", "erreurs", "modele", "in", "cache_lu", "out"])
        w.writerow([dt.datetime.now().isoformat(timespec="seconds"), c["id"], c["ssp"], c["rubrique"], c["poids"], len(items_obj["items"]),
                    len(erreurs), modele, usage.get("input_tokens"), usage.get("cache_read_input_tokens"), usage.get("output_tokens")])


def selection(args):
    cibles = [c for c in charger_cibles() if not os.path.exists(chemin_sortie(c))]
    if args.ssp:
        cibles = [c for c in cibles if c["ssp"] == args.ssp]
    if getattr(args, "priorite", False):
        cibles.sort(key=lambda c: (c["prio"], -c["lot"]))     # urgences d'abord, puis SSP du 248 vers le 001
    else:
        cibles.sort(key=lambda c: (-c["lot"], c["id"]))        # ordre rétrograde 248 → 001
    return cibles[: args.max] if args.max else cibles


def client():
    import anthropic
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY absente : voir PROCEDURE_CREDITS_CLAUDE.md, étape 2.")
    return anthropic.Anthropic()


def cmd_pilote(args):
    cibles = selection(args)[: args.n]
    if args.sec:
        print(json.dumps(params(cibles[0], args.modele), ensure_ascii=False, indent=1)[:3000]); return
    cl = client()
    for c in cibles:
        t = time.time(); m = cl.messages.create(**params(c, args.modele))
        bloc = next(b for b in m.content if b.type == "tool_use")
        err = valider(bloc.input, c); ecrire(c, bloc.input, args.modele, m.usage.model_dump(), err)
        print(f"{c['id']}: {len(bloc.input.get('items', []))} item(s), {len(err)} erreur(s), "
              f"{m.usage.output_tokens} tokens de sortie, {time.time()-t:.0f} s → {chemin_sortie(c)}")
    print("Coût réel : Console Anthropic > Usage. Relis les JSON avant de lancer un batch.")


def cmd_soumettre(args):
    cibles = selection(args)
    if not cibles:
        print("Rien à produire pour cette sélection."); return
    print(f"{len(cibles)} requête(s), {sum(c['poids'] for c in cibles)} item(s) attendus, de {cibles[0]['id']} à {cibles[-1]['id']}.")
    if args.sec:
        return
    cl = client(); suivi = json.load(open(SUIVI)) if os.path.exists(SUIVI) else []
    for i in range(0, len(cibles), 10000):                    # sous la limite de 100 000 requêtes et 256 Mo par batch
        tranche = cibles[i:i + 10000]
        b = cl.messages.batches.create(requests=[{"custom_id": c["id"], "params": params(c, args.modele)} for c in tranche])
        suivi.append({"batch": b.id, "modele": args.modele, "ids": [c["id"] for c in tranche], "recupere": False,
                      "cree": dt.datetime.now().isoformat(timespec="seconds")})
        print(f"Batch {b.id} : {len(tranche)} requêtes soumises.")
    json.dump(suivi, open(SUIVI, "w"), indent=1)
    print("Les résultats arrivent en général en moins d'une heure (24 h au plus). Puis : recuperer.")


def cmd_statut(args):
    cl = client()
    for s in json.load(open(SUIVI)) if os.path.exists(SUIVI) else []:
        b = cl.messages.batches.retrieve(s["batch"])
        print(s["batch"], b.processing_status, b.request_counts.model_dump(), "récupéré" if s["recupere"] else "")


def cmd_recuperer(args):
    cl = client(); suivi = json.load(open(SUIVI)) if os.path.exists(SUIVI) else []
    index = {c["id"]: c for c in charger_cibles()}
    for s in suivi:
        if s["recupere"] or cl.messages.batches.retrieve(s["batch"]).processing_status != "ended":
            continue
        ok = ko = 0
        for r in cl.messages.batches.results(s["batch"]):
            c = index.get(r.custom_id)
            if r.result.type != "succeeded" or c is None:
                ko += 1; continue
            m = r.result.message; bloc = next((b for b in m.content if b.type == "tool_use"), None)
            if bloc is None:
                ko += 1; continue
            err = valider(bloc.input, c); ecrire(c, bloc.input, s["modele"], m.usage.model_dump(), err); ok += 1
        s["recupere"] = True; print(f"{s['batch']} : {ok} écrites, {ko} échecs (relancer « soumettre » les reprendra).")
    json.dump(suivi, open(SUIVI, "w"), indent=1)


def cmd_bilan(args):
    cibles = charger_cibles(); faits = [c for c in cibles if os.path.exists(chemin_sortie(c))]
    pt = sum(c["poids"] for c in cibles); pf = sum(c["poids"] for c in faits)
    print(f"Rubriques produites : {len(faits)}/{len(cibles)} · items ≈ {pf}/{pt} ({100*pf/max(pt,1):.1f} %)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
    for nom in ("pilote", "soumettre", "statut", "recuperer", "bilan"):
        p = sp.add_parser(nom)
        p.add_argument("--ssp"); p.add_argument("--max", type=int); p.add_argument("--n", type=int, default=3)
        p.add_argument("--priorite", action="store_true"); p.add_argument("--modele", default=MODELE_DEFAUT); p.add_argument("--sec", action="store_true")
    a = ap.parse_args(); globals()["cmd_" + a.cmd](a)
