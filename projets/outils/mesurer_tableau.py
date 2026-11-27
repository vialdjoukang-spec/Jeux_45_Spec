"""Tableau de bord live : mesure le dépôt (0 token) et écrit tableau/donnees/*.json + historique.jsonl.
Réutilise projets/jauges.json (jauges des 4 jeux, écrites par jauges.py toutes les 5 min) au lieu de les recalculer.
Chaque chiffre publié porte sa règle et le fichier qui le prouve. Jamais de contenu de QCM, de réponse ou de secret : des comptes.
Usage : python3 projets/outils/mesurer_tableau.py   (variables facultatives : GITHUB_TOKEN, GITHUB_REPOSITORY)
Signature : AAI (Anthropic AI)"""
import collections, datetime as dt, glob, json, os, re, subprocess, urllib.request

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); os.chdir(R)
OUT = "tableau/donnees"; os.makedirs(OUT, exist_ok=True)
TZ = dt.timezone(dt.timedelta(hours=1)); NOW = dt.datetime.now(TZ)
REPO = os.environ.get("GITHUB_REPOSITORY", "vialdjoukang-spec/Jeux_45_Spec")
GROUPES = "ABCD"; COUT_REEL_PATHO = 0.33


def J(p, defaut=None):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return defaut


def git(*a):
    try:
        return subprocess.run(["git", *a], capture_output=True, text=True, timeout=60).stdout
    except Exception:
        return ""


def git_json(ref, chemin):
    try:
        return json.loads(git("show", f"{ref}:{chemin}"))
    except Exception:
        return None


def ecrire(nom, obj):
    json.dump(obj, open(f"{OUT}/{nom}", "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def date_jauge(s):
    return dt.datetime.strptime(s, "%d.%m.%Y %H:%M").replace(tzinfo=TZ)


# ---------- 1. Jeux : jauges réutilisées, tendance, vitesse, achèvement projeté ----------
jg = J("projets/jauges.json", {"jeux": [], "historique": []})
points = [(date_jauge(h["date"]), h["pct"]) for h in jg.get("historique", [])]
if os.path.exists(f"{OUT}/historique.jsonl"):
    for l in open(f"{OUT}/historique.jsonl", encoding="utf-8"):
        try:
            h = json.loads(l); points.append((dt.datetime.fromisoformat(h["date"]), h["pct"]))
        except Exception:
            pass
points.sort(key=lambda x: x[0])


def valeur_a(t, i):
    """Dernière valeur connue avant t (fonction en escalier) ; None avant le premier point."""
    v = None
    for d, p in points:
        if d > t:
            break
        v = p[i]
    return v


def regression(i):
    """Pente (points de % par jour) par moindres carrés sur un échantillon horaire des 7 derniers jours."""
    if not points:
        return None
    debut = max(points[0][0], NOW - dt.timedelta(days=7)); xs, ys = [], []
    t = debut
    while t <= NOW:
        v = valeur_a(t, i)
        if v is not None:
            xs.append((t - debut).total_seconds() / 86400); ys.append(v)
        t += dt.timedelta(hours=1)
    if len(xs) < 3 or max(xs) - min(xs) < 0.25:
        return None
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    den = sum((x - mx) ** 2 for x in xs)
    return round(sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den, 2) if den else None


jeux = []
for i, j in enumerate(jg.get("jeux", [])):
    pct = j["pct"]; premier = points[0][1][i] if points else None   # historique plus court que la fenêtre : écart depuis le premier point
    v24 = valeur_a(NOW - dt.timedelta(hours=24), i); v7 = valeur_a(NOW - dt.timedelta(days=7), i)
    v24 = premier if v24 is None else v24; v7 = premier if v7 is None else v7
    pente = regression(i); fin = None
    if pct >= 100:
        fin = "atteint"
    elif pente and pente > 0.05:
        fin = (NOW + dt.timedelta(days=(100 - pct) / pente)).strftime("%Y-%m-%d")
    total = sum(c["poids"] for c in j["criteres"])
    jeux.append({"nom": j["nom"], "pct": pct,
                 "tendance24h": None if v24 is None else pct - v24, "tendance7j": None if v7 is None else pct - v7,
                 "depuis": points[0][0].isoformat() if points else None,
                 "jours_historique": round((NOW - points[0][0]).total_seconds() / 86400, 1) if points else 0,
                 "vitesse_pct_jour": pente, "achevement_projete": fin,
                 "criteres": [{**c, "part": round(100 * min(1, c["fait"] / c["cible"]) if c["cible"] else 0), "contribution": round(100 * min(1, c["fait"] / c["cible"]) * c["poids"] / total, 1) if c["cible"] else 0} for c in j["criteres"]]})
glob_pct = round(sum(j["pct"] for j in jeux) / len(jeux)) if jeux else 0

# ---------- 2. Grille 45 Spec : spécialités × groupes de rendement ----------
SPECS = {v["code"]: v["nom"] for v in (J("data/references/entite_specialites.json", {}) or {}).get("specialites", {}).values()}
RANG = (J("content/pathologies/RANG_RENDEMENT.json", {}) or {}).get("pathologies", {})
qfiles = {os.path.basename(f)[:-5]: f for f in glob.glob("content/questions/*/*.json")}
ligne = lambda: {g: {"cible": 0, "produit": 0, "audite": 0, "attente": 0} for g in GROUPES + "H"}   # H = hors rang
grille = collections.defaultdict(ligne); jouables = collections.Counter(); rejets = collections.Counter(); corr = collections.Counter()
for k, v in RANG.items():
    grille[v["codes"][0]][v["groupe"]]["cible"] += 1
for k, f in qfiles.items():
    spec = f.split(os.sep)[2]; g = RANG[k]["groupe"] if k in RANG else "H"; d = J(f, {}) or {}
    rej = (d.get("audit") or {}).get("rejector")
    grille[spec][g]["produit"] += 1
    grille[spec][g]["audite"] += rej == "pass"
    if rej == "rejet":
        rejets[spec] += 1
    else:
        jouables[spec] += len(d.get("questions") or [])        # même règle que construire_arene45.py
    corr[spec] += os.path.exists(f.replace("questions", "corrections"))
# Production en attente sur les branches agent/45spec-* (fichiers ajoutés, pas encore sur main)
branches = sorted(l.split("refs/heads/")[1] for l in git("ls-remote", "--heads", "origin").splitlines() if "refs/heads/" in l)
attente_branche = {}
for b in [b for b in branches if b.startswith("agent/45spec-")]:
    noms = [n for n in git("diff", "--name-only", "--diff-filter=A", f"origin/main...origin/{b}", "--", "content/questions").split() if n.endswith(".json")]
    attente_branche[b] = len(noms)
    for n in noms:
        k = os.path.basename(n)[:-5]; spec = n.split("/")[2]
        if k in qfiles:
            continue
        grille[spec][RANG[k]["groupe"] if k in RANG else "H"]["attente"] += 1
lignes = []
for code in sorted(set(SPECS) | set(grille)):
    c = grille[code]; tot = {x: sum(c[g][x] for g in c) for x in ("cible", "produit", "audite", "attente")}
    lignes.append({"code": code, "nom": SPECS.get(code, code), "groupes": c, "total": tot, "jouables": jouables[code], "rejets": rejets[code], "corrections": corr[code]})
totaux = {g: {x: sum(l["groupes"][g][x] for l in lignes) for x in ("cible", "produit", "audite", "attente")} for g in GROUPES + "H"}
ecrire("grille.json", {"maj": NOW.isoformat(), "lignes": lignes, "totaux": totaux, "attente_par_branche": attente_branche,
                       "jouables": sum(jouables.values()), "regles": {
    "cible": "Pathologies classées dans content/pathologies/RANG_RENDEMENT.json, rangées par leur première spécialité (codes[0]) et leur groupe A/B/C/D.",
    "produit": "Fichier content/questions/<SPEC>/<id>.json présent sur main (les notions et la correction vont de pair).",
    "audite": "Même fichier avec audit.rejector == \"pass\".",
    "attente": "Fichier de questions ajouté sur une branche agent/45spec-* et absent de main (git diff origin/main...branche).",
    "jouables": "Questions des fichiers non rejetés, comptées comme construire_arene45.py les livre à l'arène 45.",
    "H": "Hors rang : pathologie produite dont l'identifiant ne figure pas dans RANG_RENDEMENT.json (id changé à la fusion)."}})

# ---------- 3. Travail en cours : branches agent/* et file API ----------
br = []
for b in [b for b in branches if b.startswith("agent/")]:
    sha, quand, sujet = (git("log", "-1", "--format=%h%x1f%cI%x1f%s", f"origin/{b}").strip().split("\x1f") + ["", "", ""])[:3]
    br.append({"branche": b, "sha": sha, "date": quand, "sujet": sujet[:140],
               "en_avance": int(git("rev-list", "--count", f"origin/main..origin/{b}").strip() or 0),
               "questions_en_attente": attente_branche.get(b)})
br.sort(key=lambda x: x["date"], reverse=True)
fp = git_json("origin/veille/audit-medical", "projets/ouvrier/FILE_PROCESSUS.json") or J("projets/ouvrier/FILE_PROCESSUS.json", {}) or {}
taches = [{"id": t.get("id"), "titre": t.get("titre"), "etat": t.get("etat"), "modele": t.get("modele"), "essais": t.get("essais", 0),
           "budget_usd": t.get("budget_usd"), "date": (t.get("dernier") or {}).get("date"), "cout_usd": (t.get("dernier") or {}).get("cout_usd")}
          for t in fp.get("taches", [])]                       # ni prompt ni résumé : uniquement l'état
ecrire("travail.json", {"maj": NOW.isoformat(), "branches": br, "file": {"source": "veille/audit-medical:projets/ouvrier/FILE_PROCESSUS.json",
        "etats": collections.Counter(t["etat"] for t in taches), "taches": taches}})

# ---------- 4. Coûts API ----------
dep = git_json("origin/veille/audit-medical", "projets/ouvrier/depense.json") or J("projets/ouvrier/depense.json", []) or []
if len(J("projets/ouvrier/depense.json", []) or []) > len(dep):
    dep = J("projets/ouvrier/depense.json", [])
par_jour, par_modele = collections.defaultdict(float), collections.defaultdict(float)
for x in dep:
    par_jour[x.get("jour", "?")] += x.get("cout", 0); par_modele[x.get("modele") or x.get("source") or "autre"] += x.get("cout", 0)
bud = fp.get("budget", {}); compte = round(sum(par_jour.values()), 2); n_patho = len(qfiles)
ecrire("couts.json", {"maj": NOW.isoformat(), "compte_usd": compte, "plafond_usd": bud.get("plafond_total_usd"), "credit_usd": bud.get("credit_usd"),
                      "reserve_usd": bud.get("reserve_usd"), "expire": bud.get("expire"),
                      "reste_usd": round(bud["plafond_total_usd"] - compte, 2) if bud.get("plafond_total_usd") else None,
                      "par_jour": {k: round(v, 2) for k, v in sorted(par_jour.items())}, "par_modele": {k: round(v, 2) for k, v in sorted(par_modele.items(), key=lambda x: -x[1])},
                      "lignes": len(dep), "pathologies_produites": n_patho, "cout_reel_par_pathologie": COUT_REEL_PATHO,
                      "estimation_haute_usd": round(n_patho * COUT_REEL_PATHO, 2),
                      "avertissement": "depense.json ne compte pas les lots batch (Message Batches) : le coût réel vaut environ 0,33 USD par pathologie. "
                                       "L'estimation haute multiplie ce coût par toutes les pathologies produites, y compris celles des agents sans API."})

# ---------- 5. Blocages et décisions en attente (section dédiée de REPRISE.md) ----------
txt = open("REPRISE.md", encoding="utf-8").read() if os.path.exists("REPRISE.md") else ""
m = re.search(r"^## Blocages et décisions en attente.*?$(.*?)(?=^## |\Z)", txt, re.M | re.S); bloc = []
for l in (m.group(1) if m else "").splitlines():
    x = re.match(r"\s*- \[([^\]]+)\]\s*(.+)", l)
    if x:
        bloc.append({"qui": x.group(1).strip(), "quoi": x.group(2).strip()})
bloc += [{"qui": "File API", "quoi": f"Tâche {t['id']} : état « {t['etat']} » ({t['essais']} essais)."} for t in taches if t["etat"] in ("bloque", "attente_decision")]
ecrire("blocages.json", {"maj": NOW.isoformat(), "source": "REPRISE.md, section « Blocages et décisions en attente », et tâches bloquées de la file API", "items": bloc})

# ---------- 6. Journal : fusions, audits, échecs de workflow ----------
ev = []
for l in git("log", "origin/main", "-60", "--format=%h%x1f%cI%x1f%P%x1f%s").splitlines():
    sha, quand, parents, sujet = l.split("\x1f")
    if len(parents.split()) > 1 or re.search(r"\bfusion\b", sujet, re.I):
        ev.append({"type": "fusion", "date": quand, "texte": sujet[:160], "ref": sha})
    elif re.search(r"audit", sujet, re.I):
        ev.append({"type": "audit", "date": quand, "texte": sujet[:160], "ref": sha})
try:
    rq = urllib.request.Request(f"https://api.github.com/repos/{REPO}/actions/runs?status=failure&per_page=20", headers={"Accept": "application/vnd.github+json"})
    if os.environ.get("GITHUB_TOKEN"):
        rq.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    for r in json.load(urllib.request.urlopen(rq, timeout=20)).get("workflow_runs", []):
        ev.append({"type": "echec", "date": r["created_at"], "texte": f"Échec du workflow « {r['name']} » ({r.get('event')})", "ref": r["html_url"]})
except Exception as ex:
    print("API GitHub indisponible :", ex)
ev.sort(key=lambda e: dt.datetime.fromisoformat(e["date"].replace("Z", "+00:00")), reverse=True)
ecrire("journal.json", {"maj": NOW.isoformat(), "evenements": ev[:20]})

# ---------- 6 bis. Chantier Biologie (onglet Biologie du jeu Paraclinique, BRIEF_BIOLOGIE_CLAUDE_CODE.md) ----------
# Source : la référence (main ou branche) dont AUDIT_BIOLOGIE.json a été commité en dernier ; on lit les rapports des scripts
# auditer_biologie.py et importer_ex1.py, jamais une estimation. Aucun contenu médical n'est publié : des comptes.
PB = "projets/2_Jeux_Paraclinique"; FB = "conception/donnees/paraclinique/biologie/fiches"
refs = ["origin/main"] + [r for r in git("for-each-ref", "--format=%(refname:short)", "refs/remotes/origin").split() if r not in ("origin/main", "origin/HEAD", "origin")]
cand = [(int(git("log", "-1", "--format=%ct", r, "--", f"{PB}/AUDIT_BIOLOGIE.json").strip() or 0), r) for r in refs]
cand = [c for c in cand if c[0]]
bio = None
if cand:
    t_bio, ref_bio = max(cand)
    AUD = git_json(ref_bio, f"{PB}/AUDIT_BIOLOGIE.json") or {}; FIL = git_json(ref_bio, f"{PB}/FILE_BIOLOGIE.json") or {}
    CA = git_json(ref_bio, f"{PB}/CONTRE_AUDIT_BIOLOGIE.json") or {}
    fiches_b = FIL.get("fiches", []); nfb = len(fiches_b); rouges = set(AUD.get("defauts", {}))
    caps = [x for x in git("ls-tree", "-r", "--name-only", ref_bio, f"{PB}/captures/biologie/").split() if re.search(r"_fiche_.*_(1280|380)\.png$", x)]
    a_verif = sum(int(l.rsplit(":", 1)[1]) for l in git("grep", "-c", "à vérifier", ref_bio, "--", FB).splitlines() if ":" in l)
    trt = sum(1 for f in fiches_b if not f.get("traitement_absent"))
    comp = (AUD.get("resume") or {}).get("completes", 0); vertes = nfb - len(rouges & {f["id"] for f in fiches_b})
    ech = max(1, -(-nfb // 10)); ca_fait = len(CA.get("fiches", []))
    crit = [("fiches importées ou créées (101 EX-1 au départ)", nfb, 101, 10), ("fiches vertes à l'audit mécanique A1–A10", vertes, max(nfb, 1), 25),
            ("fiches avec bloc Traitement rédigé (posologie → AIPS)", trt, max(nfb, 1), 35), ("fiches complètes (aucun bloc « à produire »)", comp, max(nfb, 1), 15),
            ("contre-audit médical de 10 % des fiches (session neuve)", ca_fait, ech, 10), ("captures 1280 et 380 px d'une fiche par matrice", len(caps), 18, 5)]
    tp = sum(p for *_, p in crit)
    mats = []
    for m in (FIL.get("resume") or {}).get("par_matrice", {}):
        L = [f for f in fiches_b if f.get("matrice") == m]
        mats.append({"matrice": m, "fiches": len(L), "vertes": sum(1 for f in L if f["id"] not in rouges),
                     "traitement": sum(1 for f in L if not f.get("traitement_absent")), "faites": sum(1 for f in L if f.get("statut") == "fait")})
    bio = {"maj": NOW.isoformat(), "ref": ref_bio.replace("origin/", ""), "ref_date": dt.datetime.fromtimestamp(t_bio, TZ).isoformat(),
           "pct": round(100 * sum(min(1, v / c) * p for _, v, c, p in crit if c) / tp),
           "criteres": [{"quoi": q, "fait": v, "cible": c, "poids": p, "part": round(100 * min(1, v / c)) if c else 0,
                         "contribution": round(100 * min(1, v / c) * p / tp, 1) if c else 0} for q, v, c, p in crit],
           "matrices": mats, "defauts": (AUD.get("resume") or {}).get("defauts_par_code", {}), "a_verifier": a_verif,
           "statuts": (FIL.get("resume") or {}).get("statuts", {}), "analyses_sans_fiche": (FIL.get("resume") or {}).get("analyses_sans_fiche"),
           "regles": {"jauge": "Moyenne pondérée des 6 critères (fait / cible plafonné à 1) ; mesure des rapports commités par auditer_biologie.py et importer_ex1.py.",
                      "ref": "Référence lue : la branche ou main où AUDIT_BIOLOGIE.json a été commité en dernier.",
                      "vertes": "Fiche sans aucun défaut A1–A10 dans AUDIT_BIOLOGIE.json.",
                      "a_verifier": "Nombre de mentions « à vérifier » dans les fiches : chaque mention dit où vérifier ; elle reste visible tant qu'aucune source lue ne la lève.",
                      "defauts": {"A1": "Bloc du gabarit absent ou vide sans « à produire ».", "A2": "Valeur chiffrée sans source.", "A3": "Posologie sans renvoi final à l'AIPS.",
                                  "A4": "Unité non SI sans son équivalent SI.", "A5": "Phrase nominale (sans verbe conjugué).", "A6": "Identifiant dupliqué.",
                                  "A7": "Passerelle sans raison ou vers une fiche inexistante.", "A8": "Valeur remplie disparue (non-perte).",
                                  "A9": "Source sans année ou sans date de lecture.", "A10": "Bloc Traitement incomplet (but, moyens, posologie, source)."}}}
ecrire("biologie.json", bio or {"maj": NOW.isoformat(), "absent": "Aucun AUDIT_BIOLOGIE.json commité sur main ni sur une branche."})

# ---------- 7. État global + historique ----------
bas = min(jeux, key=lambda j: j["pct"]) if jeux else None
n_att = sum(attente_branche.values())
verdict = (f"Le chantier atteint {glob_pct} % ; {bas['nom']} freine l'ensemble à {bas['pct']} %, "
           f"{n_att} pathologies attendent leur fusion et {len(bloc)} blocages restent ouverts.") if bas else "Les jauges n'ont pas encore été mesurées."
etat = {"maj": NOW.isoformat(), "jauges_maj": jg.get("maj"), "global_pct": glob_pct, "verdict": verdict, "jeux": jeux,
        "historique_jeux": [{"date": date_jauge(h["date"]).isoformat(), "pct": h["pct"]} for h in jg.get("historique", [])],
        "regles": {"global": "Moyenne simple des 4 jauges.", "jauge": "Moyenne pondérée des critères (fait / cible plafonné à 1), calculée par projets/outils/jauges.py.",
                   "tendance": "Écart avec la dernière valeur connue il y a 24 h et 7 j (historique de projets/jauges.json et tableau/donnees/historique.jsonl) ; si l'historique est plus court, écart depuis le premier point.",
                   "vitesse": "Pente par moindres carrés, en points de % par jour, sur un échantillon horaire des 7 derniers jours.",
                   "achevement": "Date où la droite atteint 100 % ; vide si la vitesse est nulle ou négative ; fragile tant que l'historique couvre moins de 3 jours."}}
ecrire("etat.json", etat)
H = f"{OUT}/historique.jsonl"; neuf = {"date": NOW.isoformat(timespec="minutes"), "pct": [j["pct"] for j in jeux], "global": glob_pct,
                                     "produit": sum(totaux[g]["produit"] for g in totaux), "audite": sum(totaux[g]["audite"] for g in totaux),
                                     "attente": n_att, "jouables": sum(jouables.values()), "cout": compte, "bio": bio["pct"] if bio else None}
dernier = None
if os.path.exists(H):
    l = [x for x in open(H, encoding="utf-8").read().splitlines() if x.strip()]
    dernier = json.loads(l[-1]) if l else None
if not dernier or {k: v for k, v in dernier.items() if k != "date"} != {k: v for k, v in neuf.items() if k != "date"}:
    open(H, "a", encoding="utf-8").write(json.dumps(neuf, ensure_ascii=False) + "\n")
print(verdict)
