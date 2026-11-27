#!/usr/bin/env python3
"""Audit croisé automatique par l'API Gemini (Gemini 4 Neon + recherche Google).

Lit <jeu>/MANIFESTE_LOTS.json, envoie chaque lot non encore audité (ou dont les sources ont changé) à Gemini,
valide le rapport JSON au schéma, l'écrit dans <jeu>/rapports/<lot>.json et journalise le coût dans couts.jsonl.
La clé vient UNIQUEMENT de la variable d'environnement GEMINI_API_KEY (secret GitHub) : jamais dans un fichier.

Usage : python Gemini_cross-check-hard/outils/audit_gemini.py --jeu 2_Paraclinique/Imagerie --max-lots 1 --max-usd 2
"""
import argparse, datetime, hashlib, json, os, re, sys, time, urllib.request, urllib.error

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(R)
G = "Gemini_cross-check-hard"
PRIX_ENTREE, PRIX_SORTIE, PRIX_RECHERCHE = 3.00, 15.00, 0.014  # $/M tokens (Neon) ; $/requête au-delà du quota gratuit
REQ = ["id", "gravite", "categorie", "fichier", "localisation", "texte_actuel", "probleme", "correction_proposee", "preuve", "confiance"]


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]


def a_jour(lot):
    p = lot["rapport"]
    if not os.path.exists(p):
        return False
    try:
        r = json.load(open(p))
        vu = {f["chemin"]: f["sha256"] for f in r.get("fichiers_audites", [])}
        return all(vu.get(f["chemin"]) == sha(f["chemin"]) for f in lot["fichiers"] if os.path.exists(f["chemin"]))
    except Exception:
        return False


def consignes():
    sch = open(f"{G}/outils/SCHEMA_RAPPORT.json").read()
    return (open(f"{G}/PROMPT_GEMINI.md").read() + "\n\n" + open(f"{G}/SKILL.md").read()
            + "\n\n## Format de sortie OBLIGATOIRE\nRéponds par UN SEUL bloc ```json contenant le rapport conforme à ce schéma, et rien d'autre :\n" + sch)


def message(lot, date):
    parts = [f"Lot à auditer : {lot['lot']} — {lot['titre']}\nFocus : {lot['focus']}\nDate du jour : {date}\n"
             "OBLIGATOIRE : utilise l'outil google_search pour retrouver et ouvrir CHAQUE source avant de la citer ; "
             "une preuve non retrouvée par la recherche porte \"confiance\": \"à confirmer\".\n"
             f"Recopie dans fichiers_audites exactement ces empreintes : "
             + json.dumps([{"chemin": f["chemin"], "sha256": f["sha256"]} for f in lot["fichiers"]], ensure_ascii=False)]
    for f in lot["fichiers"]:
        if os.path.exists(f["chemin"]):
            parts.append(f"\n===== FICHIER {f['chemin']} =====\n" + open(f["chemin"], encoding="utf-8").read())
    return "\n".join(parts)


def appeler(modele, cle, systeme, texte, effort):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modele}:generateContent"
    corps = {"systemInstruction": {"parts": [{"text": systeme}]},
             "contents": [{"role": "user", "parts": [{"text": texte}]}],
             "tools": [{"google_search": {}}],
             "generationConfig": {"temperature": 0.2, "thinkingConfig": {"thinkingLevel": effort}}}
    req = urllib.request.Request(url, data=json.dumps(corps).encode(), headers={"Content-Type": "application/json", "x-goog-api-key": cle})
    for essai in range(3):
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=2400) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            detail = e.read().decode()[:600]
            print(f"HTTP {e.code} après {round(time.time() - t0)} s : {detail}", flush=True)
            if e.code in (429, 500, 503, 504) and essai < 2:
                time.sleep(30 * (essai + 1)); continue
            raise SystemExit(f"API Gemini : HTTP {e.code} — {detail}")
        except (TimeoutError, urllib.error.URLError, ConnectionError) as e:
            print(f"Pas de réponse après {round(time.time() - t0)} s ({e}) ; essai {essai + 1}/3", flush=True)
            if essai < 2:
                continue
            raise SystemExit("API Gemini : aucune réponse après 3 essais (délai dépassé)")


def extraire(rep):
    cand = (rep.get("candidates") or [{}])[0]
    txt = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []) if not p.get("thought"))
    m = re.search(r"```json\s*(\{.*\})\s*```", txt, re.S) or re.search(r"(\{.*\})", txt, re.S)
    if not m:
        raise ValueError("pas de JSON dans la réponse")
    r = json.loads(m.group(1))
    sources_web = [c.get("web", {}).get("uri") for c in cand.get("groundingMetadata", {}).get("groundingChunks", []) if c.get("web")]
    recherches = len(cand.get("groundingMetadata", {}).get("webSearchQueries", []) or [])
    return r, sources_web, recherches


def valider(r):
    for k in ["lot", "auditeur", "date", "fichiers_audites", "verdict_lot", "constats"]:
        assert k in r, f"champ racine manquant : {k}"
    for c in r["constats"]:
        assert all(k in c for k in REQ), f"{c.get('id')} : champ manquant"
        p = c["preuve"]
        assert p.get("lien") and p.get("lu_le") and p.get("extrait_court"), f"{c['id']} : preuve incomplète"


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--jeu", required=True); a.add_argument("--max-lots", type=int, default=1)
    a.add_argument("--max-usd", type=float, default=2.0); a.add_argument("--modele", default="gemini-4-neon")
    a.add_argument("--effort", default="medium", help="low | medium | high | xhigh")
    a.add_argument("--lot", default=None, help="auditer seulement ce lot")
    o = a.parse_args()
    cle = os.environ.get("GEMINI_API_KEY")
    if not cle:
        sys.exit("GEMINI_API_KEY absente : ajoute-la dans les secrets du dépôt (jamais dans un fichier).")
    man = json.load(open(f"{G}/{o.jeu}/MANIFESTE_LOTS.json"))
    a_faire = [l for l in man["lots"] if (o.lot is None or l["lot"] == o.lot) and not a_jour(l)]
    print(f"{o.jeu} : {len(a_faire)} lot(s) à auditer ; plafond {o.max_lots} lot(s) et {o.max_usd} $")
    systeme, total, date = consignes(), 0.0, datetime.date.today().isoformat()
    for lot in a_faire[:o.max_lots]:
        if total >= o.max_usd:
            print("Plafond de dépense atteint : arrêt."); break
        t0 = time.time()
        print(f"→ lot {lot['lot']} : {sum(f['octets'] for f in lot['fichiers'])} octets envoyés à {o.modele} ({o.effort})", flush=True)
        rep = appeler(o.modele, cle, systeme, message(lot, date), o.effort)
        u = rep.get("usageMetadata", {})
        tin = u.get("promptTokenCount", 0); tout = u.get("candidatesTokenCount", 0) + u.get("thoughtsTokenCount", 0)
        statut = "ok"
        try:
            r, web, nrech = extraire(rep)
            r["lot"] = lot["lot"]; r["auditeur"] = f"{o.modele} ({o.effort})"; r["date"] = date
            r["fichiers_audites"] = [{"chemin": f["chemin"], "sha256": f["sha256"]} for f in lot["fichiers"]]
            r["_sources_web_consultees"] = web
            valider(r)
            os.makedirs(os.path.dirname(lot["rapport"]), exist_ok=True)
            json.dump(r, open(lot["rapport"], "w"), ensure_ascii=False, indent=1)
        except Exception as e:
            nrech, statut = 0, f"rejeté : {e}"
            os.makedirs(f"{G}/{o.jeu}/rapports/_rejets", exist_ok=True)
            json.dump(rep, open(f"{G}/{o.jeu}/rapports/_rejets/{lot['lot']}.json", "w"), ensure_ascii=False, indent=1)
        cout = tin / 1e6 * PRIX_ENTREE + tout / 1e6 * PRIX_SORTIE
        total += cout
        ligne = {"date": datetime.datetime.now().isoformat(timespec="seconds"), "jeu": o.jeu, "lot": lot["lot"], "modele": o.modele,
                 "tokens_entree": tin, "tokens_sortie_et_reflexion": tout, "recherches_web": nrech, "cout_usd_hors_recherche": round(cout, 4),
                 "duree_s": round(time.time() - t0), "statut": statut}
        open(f"{G}/couts.jsonl", "a").write(json.dumps(ligne, ensure_ascii=False) + "\n")
        print(json.dumps(ligne, ensure_ascii=False))
    print(f"Coût total de cette passe (hors recherches au-delà des 5 000 gratuites) : {total:.2f} $")


if __name__ == "__main__":
    main()
