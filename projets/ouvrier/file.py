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


def sortie(**kv):
    lignes = "".join(f"{k}={v}\n" for k, v in kv.items())
    print(lignes, end="")
    if os.environ.get("GITHUB_OUTPUT"):
        open(os.environ["GITHUB_OUTPUT"], "a").write(lignes)


def budget():
    b = F["budget"]
    total = sum(x["cout"] for x in D)
    reste = b["credit_usd"] - b["reserve_usd"] - total
    fin = datetime.datetime.fromisoformat(b["expire"])
    jours = max(1, math.ceil((fin - maint).total_seconds() / 86400))
    jour = sum(x["cout"] for x in D if x["jour"] == aujourd)
    plafond_jour = max(0.0, reste + jour) / jours
    return total, reste, plafond_jour, jour, fin


PREAMBULE = """Tu es Claude, ouvrier automatique du projet Jeux_45_Spec de Dr Vial (psychiatre, préparation de l'examen fédéral suisse), lancé par GitHub Actions.
Lis d'abord REPRISE.md. Écris en français, en phrases entièrement verbales. Les skills du projet sont dans .claude/skills/ : utilise-les.
La qualité médicale prime sur la quantité : une donnée incertaine reste vide avec une note, jamais inventée. Tu travailles sur la branche courante ; ne pousse rien, ne change pas de branche : le workflow publie après toi.
À la fin, écris projets/ouvrier/statut.json : {"tache": "<id>", "etat": "fait" | "en_cours" | "bloque", "resume": "<3 phrases>"}.

Tâche « %s » : %s
"""

if sys.argv[1] == "prendre":
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
    open("/tmp/prompt.txt", "w", encoding="utf-8").write(PREAMBULE % (t["id"], t["prompt"]))
    sortie(tache=t["id"], modele=t["modele"], budget=b)

elif sys.argv[1] == "terminer":
    tid, res = sys.argv[2], sys.argv[3]
    try:
        r = json.load(open(res, encoding="utf-8"))
    except Exception as e:
        r = {"is_error": True, "total_cost_usd": 0, "result": f"sortie illisible : {e}"}
    cout = float(r.get("total_cost_usd") or 0)
    st = json.load(open(STAT, encoding="utf-8")) if os.path.exists(STAT) else {}
    t = next(x for x in F["taches"] if x["id"] == tid)
    etat = st.get("etat") if st.get("tache") == tid and st.get("etat") in ("fait", "en_cours", "bloque") else "en_cours"
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
