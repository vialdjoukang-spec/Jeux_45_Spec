"""File de processus en chaîne (0 token pour la gestion ; seule la tâche appelle l'API).
  python file.py prendre            → choisit la tâche, fixe le budget du passage, écrit /tmp/prompt.txt et les sorties GitHub
  python file.py terminer <id> <resultat.json> → enregistre le coût, l'état et le rapport
Le budget journalier répartit le crédit restant sur les jours qui restent avant son expiration.
Signature : AAI (Anthropic AI)"""
import datetime, json, math, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
FF, DEP, STAT = (os.path.join(ICI, n) for n in ("FILE_PROCESSUS.json", "depense.json", "statut.json"))
RAPPORT = os.path.join(ICI, "RAPPORT_OUVRIER.md")
F = json.load(open(FF, encoding="utf-8"))
D = json.load(open(DEP, encoding="utf-8")) if os.path.exists(DEP) else []
maint = datetime.datetime.now(datetime.timezone.utc)
aujourd = maint.astimezone(datetime.timezone(datetime.timedelta(hours=1))).date().isoformat()
# Refus définitifs de l'API : réessayer ne sert à rien. Au premier, l'ouvrier se met en pause (F["pause"]) et ne repasse
# qu'après levée de la pause par Vial (supprimer la clé « pause » de FILE_PROCESSUS.json). Fermeté du 24.11.2026.
FATAL = ("credit balance is too low", "insufficient credit", "billing", "invalid x-api-key", "authentication_error",
         "permission_error", "api key", "account has been disabled")
def fatal(texte):
    t = str(texte).lower()
    return next((m for m in FATAL if m in t), None)


def sortie(**kv):
    lignes = "".join(f"{k}={v}\n" for k, v in kv.items())
    print(lignes, end="")
    if os.environ.get("GITHUB_OUTPUT"):
        open(os.environ["GITHUB_OUTPUT"], "a").write(lignes)


def budget():
    b = F["budget"]
    total = sum(x["cout"] for x in D)
    plafond = min(b["credit_usd"] - b["reserve_usd"], b.get("plafond_total_usd", b["credit_usd"]))   # plafond fixé par Vial dans FILE_PROCESSUS.json
    reste = plafond - total
    fin = datetime.datetime.fromisoformat(b["expire"])
    jours = max(1, math.ceil((fin - maint).total_seconds() / 86400))
    jour = sum(x["cout"] for x in D if x["jour"] == aujourd)
    plafond_jour = max(0.0, reste + jour) / (1 if b.get("sans_repartition_journaliere") else jours)   # Vial 23.11 : pleine vitesse jusqu'au plafond total
    return total, reste, plafond_jour, jour, fin


PREAMBULE = """Tu es Claude, ouvrier automatique du projet Jeux_45_Spec de Dr Vial (psychiatre, préparation de l'examen fédéral suisse), lancé par GitHub Actions.
Lis d'abord REPRISE.md. Écris en français, en phrases entièrement verbales. Les skills du projet sont dans .claude/skills/ : utilise-les.
La qualité médicale prime sur la quantité : une donnée incertaine reste vide avec une note, jamais inventée. Tu travailles sur la branche courante ; ne pousse rien, ne change pas de branche : le workflow publie après toi.
À la fin, écris projets/ouvrier/statut.json : {"tache": "<id>", "etat": "fait" | "en_cours" | "bloque", "resume": "<3 phrases>"}.

Tâche « %s » : %s
"""

if sys.argv[1] == "prendre":
    if F.get("pause"):
        sortie(tache="", raison=f"ouvrier en pause depuis {F['pause'].get('date')} : {F['pause'].get('raison')}"); sys.exit(0)
    total, reste, pj, jour, fin = budget()
    if maint >= fin or reste <= 0.5:
        sortie(tache="", raison="crédit épuisé ou expiré"); sys.exit(0)
    dispo = pj - jour
    t = next((x for x in F["taches"] if x["etat"] in ("en_cours", "a_faire")), None)
    if not t:
        sortie(tache="", raison="file vide"); sys.exit(0)
    b = round(min(t["budget_usd"], F["budget"]["plafond_par_passage_usd"], dispo, reste), 2)
    if b < 0.5:
        sortie(tache="", raison=f"plafond du jour atteint ({jour:.2f} / {pj:.2f} USD)"); sys.exit(0)
    if t.get("commande"):                       # tâche de type script : appel direct de l'API par un script du dépôt
        open("/tmp/commande.sh", "w", encoding="utf-8").write(t["commande"] + "\n")
        sortie(tache=t["id"], modele=t.get("modele", ""), budget=b, mode="script")
    else:
        open("/tmp/prompt.txt", "w", encoding="utf-8").write(PREAMBULE % (t["id"], t["prompt"]))
        sortie(tache=t["id"], modele=t["modele"], budget=b, mode="claude")

# prix par million de tokens (platform.claude.com, novembre 2026) : entrée, lecture de cache, sortie ; lot = moitié prix
PRIX = {"claude-sonnet-5-5": (2.0, 0.10, 10.0), "claude-haiku-5-5": (0.10, 0.01, 0.50), "claude-opus-5-5": (4.0, 0.20, 20.0)}
REGISTRES = ["registre_fiches.csv", "registre_production.csv"]


def cout_registres():
    """Coût cumulé des appels faits par les scripts de production (fiches, items), lu dans leurs registres."""
    import csv
    rac = os.path.dirname(os.path.dirname(ICI)); total = 0.0
    for nom in REGISTRES:
        p = os.path.join(rac, nom)
        if not os.path.exists(p):
            continue
        for r in csv.DictReader(open(p, encoding="utf-8"), delimiter=";"):
            pi, pc, po = PRIX.get(r.get("modele", ""), PRIX["claude-sonnet-5-5"])
            f = 0.5 if "lot" in (r.get("mode") or "lot") else 1.0
            n = lambda k: float(r.get(k) or 0)
            total += f * (n("in") * pi + n("cache_lu") * pc + n("out") * po) / 1e6
    return total


if sys.argv[1] == "comptabiliser":
    deja = sum(x["cout"] for x in D if x.get("source") == "registres")
    neuf = round(cout_registres() - deja, 4)
    if neuf > 0:
        D.append({"jour": aujourd, "date": maint.isoformat(timespec="seconds"), "tache": "scripts de production", "source": "registres", "cout": neuf})
        json.dump(D, open(DEP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"registres : {neuf:.4f} USD ajoutés")

elif sys.argv[1] == "terminer":
    tid, res = sys.argv[2], sys.argv[3]
    try:
        r = json.load(open(res, encoding="utf-8")) if res != "-" else {"is_error": False, "total_cost_usd": 0, "result": open("/tmp/sortie_script.txt", encoding="utf-8").read()[-300:]}
    except Exception as e:
        r = {"is_error": True, "total_cost_usd": 0, "result": f"sortie illisible : {e}"}
    cout = float(r.get("total_cost_usd") or 0)
    st = json.load(open(STAT, encoding="utf-8")) if os.path.exists(STAT) else {}
    t = next(x for x in F["taches"] if x["id"] == tid)
    etat = st.get("etat") if st.get("tache") == tid and st.get("etat") in ("fait", "en_cours", "bloque") else "en_cours"
    if res == "-":                                     # tâche de type script : l'état vient du code de sortie et de la condition de fin
        ok = open("/tmp/script_ok").read().strip() == "0" if os.path.exists("/tmp/script_ok") else False
        r["is_error"] = not ok
        if ok and t.get("fin") == "lots_recuperes":
            racine = os.path.dirname(os.path.dirname(ICI)); sv = t.get("suivi", "batchs_fiches.json"); suivi = os.path.join(racine, sv if sv.startswith("scripts/") else os.path.join("scripts", sv))   # « scripts/x.json » ou « x.json »
            lots = json.load(open(suivi)) if os.path.exists(suivi) else []
            etat = "fait" if lots and all(x.get("recupere") for x in lots) else "en_cours"
        else:
            etat = "fait" if ok else "en_cours"
    texte = f"{r.get('result', '')} {st.get('resume', '')}"
    if os.path.exists("/tmp/erreurs.txt"):
        texte += open("/tmp/erreurs.txt", encoding="utf-8", errors="ignore").read()[-3000:]
    if res == "-" and os.path.exists("/tmp/sortie_script.txt"):
        texte += open("/tmp/sortie_script.txt", encoding="utf-8", errors="ignore").read()[-3000:]
    m = fatal(texte) if etat != "fait" else None
    if m:                                              # refus définitif : pause immédiate, aucun essai ni échec compté, rien à publier
        F["pause"] = {"date": maint.isoformat(timespec="seconds"), "tache": tid, "raison": f"refus définitif de l'API (« {m} »)"}
        json.dump(F, open(FF, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        if os.path.exists(STAT):
            os.remove(STAT)
        sortie(fatal="1", raison=F["pause"]["raison"])
        print(f"PAUSE : {tid} → {F['pause']['raison']} ; l'ouvrier s'arrête sans réessayer."); sys.exit(0)
    t["essais"] += 1
    api = "API Error" in str(r.get("result", ""))          # panne d'accès à l'API : ce n'est pas un échec de la tâche
    if r.get("is_error") and etat != "fait" and not api:
        t["echecs"] = t.get("echecs", 0) + 1
    if api:
        t["essais"] -= 1
    t["etat"] = "bloque" if t.get("echecs", 0) >= 3 else etat
    t["dernier"] = {"date": maint.isoformat(timespec="seconds"), "cout_usd": round(cout, 3), "resume": st.get("resume") or str(r.get("result", ""))[:300]}
    D.append({"jour": aujourd, "date": maint.isoformat(timespec="seconds"), "tache": tid, "modele": os.environ.get("MODELE", ""), "cout": round(cout, 4)})
    json.dump(F, open(FF, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(D, open(DEP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    total, reste, pj, jour, fin = budget()
    lignes = [f"| {x['id']} | {x['etat']} | {x['essais']} | {x.get('dernier', {}).get('cout_usd', '')} |" for x in F["taches"]]
    open(RAPPORT, "w", encoding="utf-8").write(
        f"# Ouvrier automatique — {maint:%Y-%m-%d %H:%M} UTC\n\nDernier passage : **{tid}** → {t['etat']} ({cout:.2f} USD).\n\n"
        f"{t['dernier']['resume']}\n\n**Crédit** : {total:.2f} USD dépensés, {reste:.2f} USD disponibles avant le {fin:%d.%m.%Y} ; "
        f"aujourd'hui {jour:.2f} / {pj:.2f} USD.\n\n| Tâche | État | Passages | Dernier coût (USD) |\n|---|---|---|---|\n" + "\n".join(lignes) +
        "\n\nSignature : AAI (Anthropic AI)\n")
    if os.path.exists(STAT):
        os.remove(STAT)
    print(f"terminé : {tid} → {t['etat']}, {cout:.3f} USD")
