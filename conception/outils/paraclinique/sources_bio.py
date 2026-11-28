#!/usr/bin/env python3
"""SOURCES_BIO — lecture 0 token des sources primaires de l'onglet Biologie, avec cache disque (requests-cache maison).

Sous-commandes :
  hug-cherche MOT [MOT…]   cherche dans l'index RPA des HUG (rpa.hug.ch) les analyses dont le nom contient tous les mots
  hug N                    affiche le texte de la fiche RPA n° N (conditions, valeurs usuelles, tarif OFAS, méthode)
  aips-cherche MOT [MOT…]  cherche dans data/references/aips_corpus_index.json les AIPS (SmPC) dont le nom contient les mots
  aips NUM_OU_URL [--tout] affiche une AIPS (n° Swissmedic ou URL refdata) : par défaut les rubriques Posologie,
                           Contre-indications, Mises en garde, Interactions, Grossesse ; --tout pour le texte entier
  url URL [--max N]        affiche le texte d'une page web quelconque (HTML → texte)

Cache : $SOURCES_BIO_CACHE ou ~/.cache/sources_bio (une page lue n'est jamais relue). Chaque sortie commence par la ligne
« SOURCE : <url> · lu le <date> » à recopier telle quelle dans la fiche.
Signature : AAI (Anthropic AI)
"""
import datetime, hashlib, html, json, os, re, sys, unicodedata, urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
IDX_AIPS = os.path.join(RAC, "data", "references", "aips_corpus_index.json")
CACHE = os.environ.get("SOURCES_BIO_CACHE", os.path.expanduser("~/.cache/sources_bio"))
RPA = "https://rpa.hug.ch/lvert/rpa/inf/"
AUJ = datetime.date.today().strftime("%d.%m.%Y")


def norm(s):
    return unicodedata.normalize("NFKD", s.replace("œ", "oe")).encode("ascii", "ignore").decode().lower()


def get(url, enc=None):
    os.makedirs(CACHE, exist_ok=True)
    p = os.path.join(CACHE, hashlib.sha1(url.encode()).hexdigest() + ".txt")
    if os.path.exists(p):
        return open(p, encoding="utf-8").read()
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; sources-bio/1.0)"})
    raw = urllib.request.urlopen(req, timeout=40).read()
    t = None
    for e in ([enc] if enc else []) + ["utf-8", "latin-1"]:
        try:
            t = raw.decode(e); break
        except Exception:
            continue
    open(p, "w", encoding="utf-8").write(t)
    return t


def texte(h):
    h = re.sub(r"(?is)<(script|style|head)\b.*?</\1>", "", h)
    h = re.sub(r"(?i)<br\s*/?>|</(p|tr|div|li|h\d|table|section)>", "\n", h)
    h = re.sub(r"(?i)</t[dh]>", " | ", h)
    t = html.unescape(re.sub(r"<[^>]+>", " ", h))
    t = re.sub(r"[ \t\xa0]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()


def entete(url):
    print(f"SOURCE : {url} · lu le {AUJ}")


def index_rpa():
    p = os.path.join(CACHE, "index_rpa.json")
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))
    idx = []
    for l in list("123ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        h = get(f"{RPA}web/analyse/{l}.html", "latin-1")
        for n, nom, reste in re.findall(r"visualisation\.html\?fiche=(\d+)'>([^<]+)</a>\s*([^<]*)", h):
            idx.append([n, html.unescape(nom).strip(), html.unescape(reste).strip()])
    json.dump(idx, open(p, "w", encoding="utf-8"), ensure_ascii=False)
    return idx


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "hug-cherche":
        mots = [norm(m) for m in args]
        for n, nom, reste in index_rpa():
            if all(m in norm(nom + " " + reste) for m in mots):
                print(n, "·", nom, reste)
    elif cmd == "hug":
        url = f"{RPA}fiches/FICHE_{args[0]}_.html"
        t = texte(get(url, "latin-1"))
        entete(f"https://rpa.hug.ch/lvert/rpa/inf/web/recherche/visualisation.html?fiche={args[0]}")
        print(t[:6000])
    elif cmd == "aips-cherche":
        mots = [norm(m) for m in args]
        for num, docs in json.load(open(IDX_AIPS, encoding="utf-8")).items():
            for nom, date, url in docs:
                if nom.startswith("SmPC") and all(m in norm(nom) for m in mots):
                    print(num, "·", nom, "·", date, "·", url)
    elif cmd == "aips":
        a = args[0]
        url = a
        if not a.startswith("http"):
            docs = json.load(open(IDX_AIPS, encoding="utf-8")).get(a) or []
            sm = [d for d in docs if d[0].startswith("SmPC")]
            if not sm:
                sys.exit(f"Aucune SmPC pour le n° {a}")
            url = sm[0][2]
            print(f"AIPS : {sm[0][0]} · n° Swissmedic {a} · version du {sm[0][1]}")
        t = texte(get(url))
        entete(url)
        if "--tout" in args:
            print(t); return
        m = re.search(r"Mise à jour de l.information\s*\n?\s*([^\n]+)", t)
        if m:
            print("Mise à jour de l'information :", m.group(1).strip()[:60])
        # rubriques principales de l'AIPS (une ligne = le titre seul) ; une rubrique finit au titre principal suivant
        titres = ["composition", "forme pharmaceutique et quantite de principe actif par unite", "indications/possibilites d'emploi",
                  "posologie/mode d'emploi", "contre-indications", "mises en garde et precautions", "interactions",
                  "grossesse, allaitement", "grossesse/allaitement", "effet sur l'aptitude a la conduite et l'utilisation de machines",
                  "effets indesirables", "surdosage", "proprietes/effets", "pharmacocinetique", "donnees precliniques",
                  "remarques particulieres", "numero d'autorisation", "titulaire de l'autorisation", "mise a jour de l'information"]
        voulus = {"indications/possibilites d'emploi": 2500, "posologie/mode d'emploi": 9000, "contre-indications": 3000,
                  "mises en garde et precautions": 5000, "interactions": 4000, "grossesse, allaitement": 2000, "grossesse/allaitement": 2000}
        if "--indic" not in args:
            voulus.pop("indications/possibilites d'emploi")
        L = t.split("\n")
        cle = lambda s: norm(re.sub("[\u2019\u2018`]", "'", s)).strip().rstrip(".").strip()
        marques = [(i, cle(x)) for i, x in enumerate(L) if cle(x) in titres]
        vus = set()
        for j, (i, k) in enumerate(marques):
            if k not in voulus or k in vus:
                continue
            vus.add(k)
            fin = marques[j + 1][0] if j + 1 < len(marques) else len(L)
            bloc = "\n".join(L[i:fin])
            lim = voulus[k]
            print("\n=====", L[i].strip(), "=====\n" + bloc[:lim] + (" […] (--tout pour la suite)" if len(bloc) > lim else ""))
    elif cmd == "url":
        mx = int(args[args.index("--max") + 1]) if "--max" in args else 12000
        t = texte(get(args[0]))
        entete(args[0])
        print(t[:mx])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
