#!/usr/bin/env python3
"""Veille Examen fédéral de médecine humaine (0 token, bibliothèque standard + pdftotext).

Télécharge les pages officielles OFSP/MEBEKO et leurs PDF (Tableau des délais, Informations, Exigences,
Directives) seulement quand ils changent, extrait les faits utiles, écrit :
  veille/examen_federal.json            faits sourcés (URL, date de consultation, sha256 de la source)
  veille/HISTORIQUE.md                  journal des changements
  veille/cache/*.txt                    texte extrait de chaque source (diff lisible)
  conception/prototypes/veille/donnees.js  copie pour la page (fonctionne aussi en file://)
  veille/.issue.md                      corps de l'issue à ouvrir (seulement si un fait change ou si le tableau N+1 paraît)
User-agent honnête ; un refus (403/429) est noté tel quel, sans contournement.
Signature : AAI (Anthropic AI)
"""
import datetime as dt, hashlib, html.parser, json, os, re, shutil, subprocess, sys, tempfile, urllib.error, urllib.parse, urllib.request

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(RACINE, "veille")
SOCLE = os.path.join(V, "socle.json")
SORTIE = os.path.join(V, "examen_federal.json")
ETAT = os.path.join(V, "etat_sources.json")
HISTO = os.path.join(V, "HISTORIQUE.md")
CACHE = os.path.join(V, "cache")
PAGE_JS = os.path.join(RACINE, "conception", "prototypes", "veille", "donnees.js")
ISSUE = os.path.join(V, ".issue.md")
UA = "Jeux45Spec-veille/1.0 (veille non commerciale de l'examen federal; +https://github.com/vialdjoukang-spec/Jeux_45_Spec)"
AUJ = dt.date.today().isoformat()
MOIS = {m: i + 1 for i, m in enumerate("janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split())}
MOIS.update({"fevrier": 2, "aout": 8, "decembre": 12})
VILLES = ["Bâle", "Berne", "Fribourg", "Genève", "Lausanne", "Lugano", "Zurich"]
RE_DATE = re.compile(r"(\d{1,2})(?:er)?\s*\.?\s*(janvier|février|fevrier|mars|avril|mai|juin|juillet|août|aout|septembre|octobre|novembre|décembre|decembre)\s+(\d{4})", re.I)


# ---------- téléchargement ----------
def get(url, etat):
    """GET conditionnel (ETag / Last-Modified). Renvoie (statut, octets|None, entêtes)."""
    e = etat.get(url, {})
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "fr-CH,fr;q=0.9"})
    if e.get("etag"): req.add_header("If-None-Match", e["etag"])
    if e.get("last_modified"): req.add_header("If-Modified-Since", e["last_modified"])
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read(), dict(r.headers)
    except urllib.error.HTTPError as x:
        return x.code, None, dict(x.headers or {})
    except Exception as x:  # réseau
        print(f"  ! {url} : {x}", file=sys.stderr)
        return 0, None, {}


class Texte(html.parser.HTMLParser):
    """Texte visible + liens (texte, href) d'une page HTML."""
    def __init__(s, base):
        super().__init__(); s.base, s.t, s.liens, s._href, s._lt, s._skip = base, [], [], None, [], 0
    def handle_starttag(s, tag, a):
        if tag in ("script", "style", "noscript"): s._skip += 1
        if tag == "a": s._href, s._lt = dict(a).get("href"), []
        if tag in ("p", "li", "tr", "h1", "h2", "h3", "h4", "br", "div", "td"): s.t.append("\n")
    def handle_endtag(s, tag):
        if tag in ("script", "style", "noscript"): s._skip = max(0, s._skip - 1)
        if tag == "a" and s._href:
            s.liens.append((" ".join("".join(s._lt).split()), urllib.parse.urljoin(s.base, s._href))); s._href = None
    def handle_data(s, d):
        if s._skip: return
        s.t.append(d)
        if s._href is not None: s._lt.append(d)


def pdf_texte(octets):
    exe = shutil.which("pdftotext")
    if not exe: return ""
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(octets); f.flush()
        r = subprocess.run([exe, "-layout", f.name, "-"], capture_output=True)
        return r.stdout.decode("utf-8", "replace")


def norm(t): return re.sub(r"[ \t ]+", " ", re.sub(r"\n\s*\n+", "\n", t)).strip()
def sha(t): return hashlib.sha256(t.encode("utf-8")).hexdigest()
def iso(m): return f"{int(m.group(3)):04d}-{MOIS[m.group(2).lower()]:02d}-{int(m.group(1)):02d}"
def nom_cache(url): return re.sub(r"[^A-Za-z0-9]+", "_", urllib.parse.unquote(url.split("/")[-1]))[:80] + "_" + sha(url)[:8] + ".txt"


def lire_source(url, etat, journal, pdf=False):
    """Renvoie le texte normalisé de la source (depuis le cache si inchangée)."""
    cache = os.path.join(CACHE, nom_cache(url))
    st, b, h = get(url, etat)
    e = etat.setdefault(url, {})
    e["dernier_statut"], e["consulte_le"] = st, AUJ
    if st == 304 and os.path.exists(cache):
        return open(cache, encoding="utf-8").read(), []
    if st != 200 or b is None:
        journal.append(f"- {AUJ} : source inaccessible ({st or 'réseau'}) : {url} — valeur précédente conservée, aucun contournement.")
        return (open(cache, encoding="utf-8").read() if os.path.exists(cache) else None), []
    liens = []
    if pdf or b[:4] == b"%PDF":
        t = norm(pdf_texte(b))
    else:
        p = Texte(url); p.feed(b.decode("utf-8", "replace")); t, liens = norm("".join(p.t)), p.liens
    e.update(etag=h.get("ETag") or h.get("Etag"), last_modified=h.get("Last-Modified"))
    if t:
        nouveau = sha(t)
        if e.get("sha256") and e["sha256"] != nouveau:
            journal.append(f"- {AUJ} : le contenu de la source a changé : {url}")
        e["sha256"] = nouveau
        os.makedirs(CACHE, exist_ok=True); open(cache, "w", encoding="utf-8").write(t)
    e["liens"] = [l for l in liens if l[1].lower().endswith(".pdf") or "pdf" in l[1].lower()][:60] if liens else e.get("liens", [])
    return t, e["liens"]


# ---------- extraction ----------
def classer_pdf(texte, url):
    s = (texte + " " + urllib.parse.unquote(url)).lower()
    an = re.search(r"(20\d\d)", urllib.parse.unquote(url.split("/")[-1])) or re.search(r"(20\d\d)", texte)
    an = int(an.group(1)) if an else None
    for cle, mots in (("tableau", ("délais", "delais", "termintabelle")), ("directives", ("directives", "weisungen")),
                      ("exigences", ("exigences", "anforderungen")), ("infotext", ("infotext", "informations concernant"))):
        if any(m in s for m in mots): return cle, an
    return None, an


def lignes_avec(t, *mots):
    return [l for l in t.split("\n") if any(m.lower() in l.lower() for m in mots)]


def dates(l): return [iso(m) for m in RE_DATE.finditer(l)]


def extraire_tableau(t, an):
    f = {}
    for cle, mots in (("delai_inscription", ("inscription", "délai d'inscription")), ("qcm", ("QCM", "choix multiple")),
                      ("cs", ("Clinical Skills", "ECOS")), ("reserve", ("réserve",))):
        ds = []
        for l in lignes_avec(t, *mots):
            if cle != "reserve" and "réserve" in l.lower(): continue
            ds += [d for d in dates(l) if d.startswith(str(an))]
        if cle == "reserve": ds = ds[:1]
        if cle == "delai_inscription": ds = ds[:1]
        if ds: f[cle] = sorted(set(ds))
    vs = [v for v in VILLES if v.lower() in t.lower()]
    if vs: f["lieux"] = vs
    return f


def chercher(t, motif, groupe=0):
    m = re.search(motif, t, re.I | re.S)
    return (m.group(groupe), t[max(0, m.start() - 60): m.end() + 60].replace("\n", " ")) if m else (None, None)


# ---------- programme ----------
def main():
    socle = json.load(open(SOCLE, encoding="utf-8"))
    ancien = json.load(open(SORTIE, encoding="utf-8")) if os.path.exists(SORTIE) else {"faits": []}
    etat = json.load(open(ETAT, encoding="utf-8")) if os.path.exists(ETAT) else {}
    journal, sources = [], {}

    # 1. pages HTML
    for cle, url in socle["pages"].items():
        t, liens = lire_source(url, etat, journal)
        sources[cle] = {"url": url, "texte": t, "sha256": etat.get(url, {}).get("sha256"), "titre": socle.get("titres_pages", {}).get(cle, cle)}
        if cle == "examen":
            for (lt, href) in liens:
                typ, an = classer_pdf(lt, href)
                if typ: sources.setdefault(f"pdf_{typ}_{an}", {"url": href, "titre": lt, "annee": an, "type": typ})

    # 1 bis. PDF connus du socle (au cas où la page ne les liste plus ou reste inaccessible)
    connus = {s["url"] for s in sources.values()}
    for f in socle["faits"] + socle["liens"]:
        u = f.get("source") or f.get("url")
        if u and u.lower().endswith(".pdf") and u not in connus:
            typ, an = classer_pdf("", u); connus.add(u)
            sources.setdefault(f"pdf_{typ or 'autre'}_{an}", {"url": u, "titre": urllib.parse.unquote(u.split("/")[-1]), "annee": an, "type": typ})

    # 2. PDF (seulement si nouveaux ou modifiés : GET conditionnel)
    for k, s in list(sources.items()):
        if k.startswith("pdf_"):
            t, _ = lire_source(s["url"], etat, journal, pdf=True)
            s["texte"], s["sha256"] = t, etat.get(s["url"], {}).get("sha256")

    # 3. faits : socle d'abord, puis confirmation / mise à jour automatique
    faits = {f["id"]: dict(f) for f in socle["faits"]}
    for f in faits.values():
        src = next((s for s in sources.values() if s["url"] == f["source"]), None)
        if src and src.get("sha256"):
            f["sha256"], f["consulte_le"] = src["sha256"], AUJ
        if src and src.get("texte") and f.get("motif"):
            v, ext = chercher(src["texte"], f["motif"])
            f["verifie_auto"] = bool(v)
            if ext: f["extrait"] = " ".join(ext.split())

    # 4. sessions : tableau des délais de chaque année publiée
    tableaux = {s["annee"]: s for k, s in sources.items() if k.startswith("pdf_tableau_") and s.get("annee")}
    session_suiv = socle["session_suivante"]
    for an, s in sorted(tableaux.items()):
        if not s.get("texte"): continue
        ex = extraire_tableau(s["texte"], an)
        for cle, val in ex.items():
            fid = f"{cle}_{an}"
            base = faits.get(fid, {"id": fid, "rubrique": f"Session {an}", "libelle": cle})
            base.update(valeur=val, statut="officiel", source=s["url"], consulte_le=AUJ, sha256=s.get("sha256"), verifie_auto=True,
                        extrait=f"Tableau des délais {an} (PDF officiel)")
            base.pop("attendu", None)
            faits[fid] = base
    if session_suiv not in tableaux:
        print(f"Tableau des délais {session_suiv} : non publié (attendu, déduction conservée).")

    # 5. changements
    prec = {f["id"]: f for f in ancien.get("faits", [])}
    changes = []
    for fid, f in faits.items():
        p = prec.get(fid)
        if p and p.get("valeur") != f.get("valeur"):
            changes.append(f"- **{f.get('libelle', fid)}** : `{p.get('valeur')}` → `{f.get('valeur')}` ([source]({f.get('source')}))")
    nouveau_tableau = session_suiv in tableaux and not ancien.get("tableau_publie", {}).get(str(session_suiv))
    if nouveau_tableau:
        changes.insert(0, f"- **Le Tableau des délais {session_suiv} est publié** : {tableaux[session_suiv]['url']}")

    ordre = {f["id"]: i for i, f in enumerate(socle["faits"])}
    sortie = {
        "titre": "Veille Examen fédéral de médecine humaine (Suisse)",
        "genere_le": AUJ, "genere_par": "veille/veille_examen.py (GitHub Actions, 0 token)",
        "session_courante": socle["session_courante"], "session_suivante": session_suiv,
        "tableau_publie": {str(a): s["url"] for a, s in tableaux.items()} | {k: v for k, v in ancien.get("tableau_publie", {}).items()},
        "sources": [{"cle": k, "url": s["url"], "titre": s.get("titre", k), "sha256": s.get("sha256"),
                     "statut_http": etat.get(s["url"], {}).get("dernier_statut"), "consulte_le": etat.get(s["url"], {}).get("consulte_le")}
                    for k, s in sources.items()],
        "liens": socle["liens"], "rubriques": socle["rubriques"],
        "faits": sorted(faits.values(), key=lambda f: (socle["rubriques"].index(f["rubrique"]) if f["rubrique"] in socle["rubriques"] else 99, ordre.get(f["id"], 999), f["id"])),
        "signature": "AAI (Anthropic AI)",
    }
    for f in sortie["faits"]: f.pop("motif", None)

    txt = json.dumps(sortie, ensure_ascii=False, indent=1)
    open(SORTIE, "w", encoding="utf-8").write(txt + "\n")
    os.makedirs(os.path.dirname(PAGE_JS), exist_ok=True)
    open(PAGE_JS, "w", encoding="utf-8").write("/* Généré par veille/veille_examen.py — ne pas éditer. AAI (Anthropic AI) */\nwindow.VEILLE=" + txt + ";\n")
    json.dump(etat, open(ETAT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    if changes or journal:
        h = open(HISTO, encoding="utf-8").read() if os.path.exists(HISTO) else "# Historique de la veille Examen fédéral\n\nSignature : AAI (Anthropic AI)\n"
        bloc = f"\n## {AUJ}\n" + "\n".join(changes + journal) + "\n"
        open(HISTO, "w", encoding="utf-8").write(h.rstrip("\n") + "\n" + bloc)
    if changes:
        open(ISSUE, "w", encoding="utf-8").write(
            f"La veille automatique a détecté {len(changes)} changement(s) le {AUJ} :\n\n" + "\n".join(changes) +
            "\n\nDétail : `veille/examen_federal.json` et `veille/HISTORIQUE.md`.\n\nSignature : AAI (Anthropic AI)\n")
    print(f"{len(faits)} faits · {len(changes)} changement(s) · {len(journal)} note(s) de journal · tableaux : {sorted(tableaux)}")


if __name__ == "__main__":
    main()
