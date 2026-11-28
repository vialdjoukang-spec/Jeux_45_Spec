"""Confronte les posologies (lignes « t ») d'un système de la Tétrade au texte AIPS Swissmedic (0 token).
Source : base AmiKo FR (ywesee, pillbox.oddb.org/amiko_db_full_idx_fr.zip), copie des informations
professionnelles publiées par Swissmedic (AIPS). La base n'est pas versionnée : chemin dans AMIKO_DB.
Usage : AMIKO_DB=/chemin/amiko_db_full_idx_fr.db python3 verifier_aips.py <systeme> [--tout] [--json sortie]
Sortie : par pathologie portant « à vérifier », chaque molécule → spécialité suisse (n° d'autorisation,
date de mise à jour), doses retrouvées ou non dans la rubrique « Posologie/Mode d'emploi ».
Signature : AAI (Anthropic AI)"""
import html, json, os, re, sqlite3, sys, unicodedata

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DB = os.environ.get("AMIKO_DB", "amiko_db_full_idx_fr.db")
IMPORT_PARALLELE = re.compile(r"eurim|orifarm|abacus|medicopharm|kohlpharma|axapharm|pharmafocus|spirig import", re.I)

def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))

def texte(h):
    h = re.sub(r"<(/p|br|/div|/tr|/li)[^>]*>", "\n", h)
    return re.sub(r"[ \t]+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()

def sections(content, ids, titres):
    out = {}
    for i, t in zip(ids.split(","), titres.split(";")):
        m = re.search(r'id="%s">(.*?)(?=<div class="paragraph" id=|$)' % re.escape(i), content, re.S)
        if m:
            out[t] = texte(m.group(1))
    return out

class Index:
    def __init__(self, db=DB):
        c = sqlite3.connect(db)
        self.fi = []
        for _id, title, auth, atc, regnrs, ids, titres in c.execute(
                "select _id,title,auth,atc,regnrs,ids_str,titles_str from amikodb where type='FI'"):
            subst = (atc or "").split(";", 1)[1] if ";" in (atc or "") else ""
            self.fi.append(dict(id=_id, titre=title, auth=auth, atc=(atc or "").split(";")[0], subst=subst,
                                regnr=regnrs, n_titre=norm(title), n_subst=norm(subst), ids=ids, titres=titres))
        self.c = c

    def cherche(self, nom, marque=None):
        """Renvoie les fiches candidates : d'abord la marque, sinon la substance (DCI)."""
        cands = []
        if marque:
            nm = re.sub(r"\s+", " ", norm(marque).replace("®", "")).strip()
            cands = [f for f in self.fi if f["n_titre"].replace("®", "").replace("  ", " ").startswith(nm)] or \
                    [f for f in self.fi if nm.split()[0] == f["n_titre"].replace("®", " ").split()[0]] if nm else []
        if not cands and nom:
            nn = norm(nom).strip()
            cands = [f for f in self.fi if f["n_subst"] == nn] or \
                    [f for f in self.fi if nn and re.search(r"(^|[ ,/])%s($|[ ,/])" % re.escape(nn), f["n_subst"])]
            if not cands and len(nn) >= 6 and " " not in nn:
                st = nn[:max(6, len(nn) - 2)]
                cands = [f for f in self.fi if f["n_subst"].startswith(st)] or \
                        [f for f in self.fi if f["n_titre"].startswith(st)]
        cands.sort(key=lambda f: (bool(IMPORT_PARALLELE.search(f["auth"] or "")), len(f["titre"])))
        return cands

    def fiche(self, f):
        content = self.c.execute("select content from amikodb where _id=?", (f["id"],)).fetchone()[0]
        s = sections(content, f["ids"], f["titres"])
        pos = next((v for k, v in s.items() if k.lower().startswith("posologie")), "")
        ind = next((v for k, v in s.items() if k.lower().startswith("indications")), "")
        maj = next((v for k, v in s.items() if k.lower().startswith("mise à jour")), "")
        maj = html.unescape(maj).replace("Mise à jour de l’information", "").strip().split("\n")[0].strip()
        return dict(posologie=pos, indications=ind, maj=maj[:20])

DOSE = re.compile(r"(\d+(?:[.,]\d+)?)(?:\s*[–\-à]\s*(\d+(?:[.,]\d+)?))?\s*(mg/kg|µg/kg|mg/m2|mg/m²|UI/kg|mg|µg|mcg|g|UI|U|ml|mmol)\b")

def doses(t):
    out = []
    for a, b, u in DOSE.findall(t):
        out += [(a, u)] + ([(b, u)] if b else [])
    return out

def present(val, unite, txt):
    v = val.replace(".", ",")
    alts = {v, v.replace(",", ".")}
    u = re.escape(unite).replace("µg", "(?:µg|mcg|microgrammes?)").replace("mg", "mg")
    return any(re.search(r"(?<![\d,.])%s\s*(?:[-–à]\s*\d+(?:[.,]\d+)?\s*)?%s" % (re.escape(a), u), txt) or
               re.search(r"(?<![\d,.])%s\s*(?:[-–à/]|et|ou)\s*" % re.escape(a), txt) and re.search(u, txt)
               for a in alts) if txt else False

GESTE = re.compile(r"chirurg|exérèse|ablation|angioplast|stent|endoprot|prothèse|pause|ventilation|oxygène|pacemaker|stimulat|défibrillat|"
                   r"myectomie|alcoolisation|thrombectomie|remplacement|endartériectomie|drainage|ponction|résection|greffe|transplant|dialyse|"
                   r"radioth|psychoth|kinési|physioth|régime|arrêt|éducation|surveillance|abstention|repos|contention|bas |immobilis|réduction|"
                   r"intervention|traitement|prise en charge|correction|éviction|sevrage|exercice|activité|réhabilitation|rééducation|"
                   r"vaccin|dépistage|conseil|suivi|hydratation|remplissage|transfusion|perte de poids|cure|plastie|dérivation|embolisation|"
                   r"dilatation|cathéter|implant|valve|TAVI|pontage|PCI|ICP|cardioversion|choc|massage|RCP|décompression|fermeture|ligature|"
                   r"anticoag|antiagrég|diurétique|bêtabloquant|statine|IEC|ARA|antibio|corticoïde|immunosuppress|biothérap|anti-|inhibiteur|"
                   r"chimio|hormonoth|analog|supplément|substitution|lumière|photo|laser|cryo|orthèse|plâtre|attelle|lunettes|appareil", re.I)

MARQUE = re.compile(r"([A-ZÀ-Ý][\wÀ-ÿ\- ]*?)®")

def molecules(nom):
    """« Clopidogrel (Plavix®) ou prasugrel (Efient®) » → [(dci, marque), …]"""
    out = []
    for morceau in re.split(r"\s+(?:ou|puis|et|\+)\s+|,\s*|/", nom):
        m = re.match(r"\s*([^()]+?)\s*(?:\(([^)]*)\))?\s*$", morceau)
        if not m:
            continue
        dci = re.sub(r"\b(IV|PO|SC|IM|oral[e]?|inhalé[e]?|en perfusion|topique)\b", "", m.group(1)).strip(" ,;")
        mq = MARQUE.findall(m.group(2) or "") or MARQUE.findall(m.group(1))
        out.append((dci, mq[0].strip() if mq else None))
    return out

def parse(systeme):
    pats, cur, org = [], None, None
    for l in open(os.path.join(RAC, "conception/outils", systeme, "pathologies.txt"), encoding="utf-8"):
        l = l.rstrip("\n")
        if l.startswith("# PATHO "):
            org = l[8:]
        elif l.startswith("@ "):
            cur = dict(organe=org, nom=l.split("|", 1)[1].strip(), t=[], s="", aV=[])
            pats.append(cur)
        elif cur and l.startswith("t "):
            cur["t"].append(l[2:])
        elif cur and l.startswith("s "):
            cur["s"] = l[2:]
        elif cur and l.startswith("aVerifier: "):
            cur["aV"].append(l[11:])
    return pats

def main():
    sysn = sys.argv[1]
    tout = "--tout" in sys.argv
    idx = Index()
    cache = {}
    rapport = []
    for p in parse(sysn):
        if not tout and "à vérifier" not in p["s"] + " ".join(p["t"]) + " ".join(p["aV"]):
            continue
        lignes = []
        for t in p["t"]:
            nom, _, pos = t.partition("|")
            ds = doses(pos)
            for dci, mq in molecules(nom):
                cands = idx.cherche(dci, mq)
                if not cands:
                    lignes.append(dict(t=t, dci=dci, marque=mq, aips=None, doses=ds))
                    continue
                f = cands[0]
                if f["id"] not in cache:
                    cache[f["id"]] = idx.fiche(f)
                fi = cache[f["id"]]
                ok = [(v, u, present(v, u, fi["posologie"])) for v, u in ds]
                preuve = []
                if any(not o for _, _, o in ok) or not ds:
                    mots = {w for w in re.findall(r"\w{5,}", norm(p["nom"]))}
                    phr = [x.strip() for x in re.split(r"(?<=[.:;])\s+|\n", fi["posologie"]) if re.search(r"\d", x)]
                    phr.sort(key=lambda x: -sum(w in norm(x) for w in mots))
                    preuve = [x[:230] for x in phr[:2]]
                lignes.append(dict(t=t, dci=dci, marque=mq, aips=dict(titre=f["titre"], auth=f["auth"], regnr=f["regnr"],
                                   atc=f["atc"], maj=fi["maj"]), doses=ok, preuve=preuve, autres=len(cands) - 1))
        revue = []
        for L in lignes:
            if L["aips"] is None:
                if L["doses"] or not GESTE.search(L["dci"]):
                    revue.append("absente:" + L["dci"])
            elif any(not o for _, _, o in L["doses"]):
                revue.append("dose:" + L["dci"])
        rapport.append(dict(organe=p["organe"], nom=p["nom"], s=p["s"], aV=p["aV"], lignes=lignes, revue=revue))
    if "--json" in sys.argv:
        json.dump(rapport, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rev = "--revue" in sys.argv
    print("AUTO (doses toutes retrouvées) : %d / %d" % (sum(not r["revue"] for r in rapport), len(rapport)))
    if rev:
        print(" ; ".join(r["nom"] for r in rapport if not r["revue"]))
    for r in rapport:
        if rev and not r["revue"]:
            continue
        print("\n## %s — %s" % (r["nom"], r["organe"]))
        vu = None
        for L in r["lignes"]:
            if L["t"] != vu:
                vu = L["t"]; print("  t %s" % L["t"][:200])
            a = L["aips"]
            if not a:
                print("    ✗ %s (%s) : aucune AIPS" % (L["dci"], L["marque"]))
                continue
            d = " ".join(("✓" if o else "✗") + v + u for v, u, o in L["doses"]) if L["doses"] else "—"
            print("    • %s → %s [%s, %s] %s" % (L["dci"], a["titre"][:40], a["regnr"], a["maj"], d))
            for x in L.get("preuve", []):
                print("        « %s »" % x)

if __name__ == "__main__":
    main()
