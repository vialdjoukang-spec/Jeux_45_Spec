"""File de production des 5 chantiers hors 45 Spec : mesure le dépôt (0 token) et écrit
projets/file_production/FILE_PRODUCTION.json (source unique de l'état) et FILE_PRODUCTION.md.
  python3 projets/outils/file_production.py
Les prompts vivent dans projets/PROMPTS_CHANTIERS_RESTANTS.md ; ce script ne les recopie pas.
Signature : AAI (Anthropic AI)"""
import datetime, glob, json, os, re

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = lambda *a: os.path.join(R, *a)
J = lambda *a: json.load(open(P(*a), encoding="utf-8"))
SORTIE = P("projets", "file_production", "FILE_PRODUCTION.json")


def biologie():
    return 140 - len(J("projets/2_Jeux_Paraclinique/FILE_BIOLOGIE.json")["analyses_sans_fiche"]), 140


def explorations():
    n = t = 0
    for f in glob.glob(P("conception/donnees/paraclinique/explorations/*.json")):
        s = str(json.load(open(f, encoding="utf-8")).get("_meta", {}).get("statut", ""))
        if s.startswith(("PRODUIT", "AUDITÉ")):
            t += 1
            n += s.startswith("AUDITÉ")
    return n, t


def imagerie():
    for j in J("projets/jauges.json")["jeux"]:
        for c in j["criteres"]:
            if j["nom"] == "Paraclinique" and "cliché" in c["quoi"]:
                return c["fait"], c["cible"]
    return 0, 1


def tetrade():
    n = sum(open(f, encoding="utf-8").read().count("à vérifier") for f in glob.glob(P("conception/outils/*/pathologies.txt")))
    return max(0, 613 - n), 613


def transversal():
    lots = J("Gemini_cross-check-hard/3_Transversal/MANIFESTE_LOTS.json")["lots"]
    faits = {os.path.basename(f)[:-5] for f in glob.glob(P("Gemini_cross-check-hard/3_Transversal/rapports/*.json"))}
    return sum(l["lot"] in faits for l in lots), len(lots)


CHANTIERS = [  # ordre = ordre de la file ; role fixe le modèle (règle de Vial : rédaction Opus, audit Fable)
    (1, "Paraclinique · Biologie", "paraclinique-biologie-suite", "rédaction", "fiches rédigées sur les 140 sans fiche", biologie),
    (2, "Paraclinique · Explorations", "paraclinique-explorations-audit", "audit", "fiches au statut AUDITÉ", explorations),
    (3, "Paraclinique · Imagerie", "paraclinique-imagerie-cliches", "rédaction", "entités avec cliché (jauge)", imagerie),
    (4, "Tétrade", "tetrade-finition", "rédaction", "« à vérifier » levés sur 613", tetrade),
    (5, "Transversal", "transversal-audit", "audit", "lots audités du manifeste", transversal),
]


def main():
    ancien = {c["id"]: c for c in json.load(open(SORTIE, encoding="utf-8"))["chantiers"]} if os.path.exists(SORTIE) else {}
    quand = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=1))).strftime("%d.%m.%Y %H:%M")
    ch = []
    for i, nom, branche, role, unite, mesure in CHANTIERS:
        try:
            fait, cible = mesure()
        except Exception as e:  # une mesure cassée ne bloque pas la file
            fait, cible = ancien.get(i, {}).get("fait", 0), ancien.get(i, {}).get("cible", 1)
            print(f"mesure {i} en échec : {e}")
        a = ancien.get(i, {})
        etat = "fait" if fait >= cible else a.get("etat", "a_faire")
        ch.append({"id": i, "chantier": nom, "branche": branche, "role": role,
                   "modele": "opus (effort élevé)" if role == "rédaction" else "fable",
                   "prompt": f"projets/PROMPTS_CHANTIERS_RESTANTS.md § {i}", "unite": unite,
                   "fait": fait, "cible": cible, "pct": int(100 * fait / max(1, cible)),
                   "etat": etat, "session": a.get("session"), "pr": a.get("pr"), "note": a.get("note", "")})
    tot = int(sum(c["pct"] for c in ch) / len(ch))
    json.dump({"_regles": "Source unique de l'état des 5 chantiers hors 45 Spec. États : a_faire, en_cours, a_auditer, fusionne, fait, bloque. "
               "Un couloir = une branche = une session ; l'œil (Claude, session chat) audite et fusionne une branche à la fois. "
               "Les champs etat, session, pr et note sont tenus par l'œil ; fait, cible et pct sont mesurés.",
               "mesure_le": quand, "progression_pct": tot, "chantiers": ch},
              open(SORTIE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    L = [f"# File de production — 5 chantiers hors 45 Spec\n", f"Mesure automatique du {quand}. Progression d'ensemble : **{tot} %**.\n",
         "| # | Chantier | Branche | Modèle | Fait | Cible | % | État | Session | PR |", "|---|---|---|---|---:|---:|---:|---|---|---|"]
    for c in ch:
        L.append(f"| {c['id']} | {c['chantier']} | `{c['branche']}` | {c['modele']} | {c['fait']} | {c['cible']} | {c['pct']} | {c['etat']} | {c['session'] or '—'} | {c['pr'] or '—'} |")
    L += ["", "Unités mesurées : " + " ; ".join(f"{c['id']} = {c['unite']}" for c in ch) + ".", ""]
    L += [f"- Chantier {c['id']} : {c['note']}" for c in ch if c["note"]]
    L += ["", "Signature : AAI (Anthropic AI)", ""]
    open(P("projets", "file_production", "FILE_PRODUCTION.md"), "w", encoding="utf-8").write("\n".join(L))
    print(f"progression {tot} % ; " + " ; ".join(f"{c['id']}:{c['fait']}/{c['cible']}" for c in ch))


if __name__ == "__main__":
    main()
