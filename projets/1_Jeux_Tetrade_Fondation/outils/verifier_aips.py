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
        self.vocab = {}
        for f in self.fi:
            for nomv in re.split(r"[,;/]| et ", f["n_subst"]):
                w = nomv.strip()
                if len(w) >= 6 and not re.search(r"\d|associ|inhibit|derive|combinaison|autres|divers", w):
                    self.vocab.setdefault(w, f)
        self.vocab_rx = re.compile(r"\b(%s)\b" % "|".join(sorted(map(re.escape, self.vocab), key=len, reverse=True)))

    def dans_texte(self, t):
        """Substances suisses nommées dans un texte libre."""
        vus, out = set(), []
        for m in self.vocab_rx.finditer(norm(t)):
            if m.group(1) not in vus:
                vus.add(m.group(1)); out.append(m.group(1))
        return out

    def cherche(self, nom, marque=None):
        """Renvoie les fiches candidates : d'abord la marque, sinon la substance (DCI), sinon l'ATC connu."""
        cands = []
        atc = SYN_ATC.get(norm(nom or "").strip())
        if atc and not marque:
            cands = [f for f in self.fi if f["atc"].startswith(atc)]
            if cands:
                cands.sort(key=lambda f: (bool(IMPORT_PARALLELE.search(f["auth"] or "")), len(f["titre"])))
                return cands
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
        if not cands and nom and " " in nom.strip():
            mots = nom.strip().split()
            for k in (2, 1):
                if len(mots) > k:
                    cands = self.cherche(" ".join(mots[:k]))
                    if cands:
                        return cands
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

# DCI française → code ATC, quand le nom de la substance dans la base diffère
SYN_ATC = {"acide acetylsalicylique": "B01AC06", "noradrenaline": "C01CA03", "nitroglycerine": "C01DA02", "heparine non fractionnee": "B01AB01",
           "heparine": "B01AB01", "penicilline v": "J01CE02", "piperacilline": "J01CR05", "amoxicilline": "J01CA04", "dornase alfa": "R05CB13",
           "sulfate de magnesium": "B05XA05", "magnesium": "B05XA05", "naloxone": "V03AB15", "dexamethasone": "H02AB02", "salbutamol": "R03AC02",
           "hydrocortisone": "H02AB09", "methylprednisolone": "H02AB04", "prednisolone": "H02AB06", "insuline": "A10A", "adrenaline": "C01CA24",
           "cotrimoxazole": "J01EE01", "trimethoprime-sulfamethoxazole": "J01EE01", "fer": "B03A", "vitamine k": "B02BA01", "glucose": "B05BA03",
           "amoxicilline-acide clavulanique": "J01CR02", "amoxicilline/acide clavulanique": "J01CR02", "piperacilline-tazobactam": "J01CR05",
           "trimethoprime-sulfamethoxazole": "J01EE01", "cotrimoxazole": "J01EE01", "varenicline": "N07BA03", "mometasone nasale": "R01AD09",
           "sacubitril/valsartan": "C09DX04", "nivolumab-ipilimumab": "L01FF01", "ipilimumab": "L01FX04"}
SYN_ATC_VOIE = {"salbutamol": ("R03AC02", "inhal"), "dexamethasone": ("H02AB02", "")}
MEDIC = re.compile(r"(ine|ol|ide|ate|one|mab|nib|pril|sartan|statine|azole|cycline|mycine|cilline|floxacine|parine|xaban|vir|tide|mide|zine|pam|lam|ane|ase|ium|ène|ine V)$", re.I)

DOSE = re.compile(r"(\d+(?:[.,]\d+)?)(?:\s*[–\-à]\s*(\d+(?:[.,]\d+)?))?\s*(mg/kg|µg/kg|mg/m2|mg/m²|UI/kg|mg|µg|mcg|g|UI|U|ml|mmol)\b")

def doses(t):
    out = []
    for a, b, u in DOSE.findall(t):
        out += [(a, u)] + ([(b, u)] if b else [])
    return out

def _num(x):
    return float(x.replace("'", "").replace("’", "").replace(" ", "").replace(",", "."))

RANGE = re.compile(r"(\d+(?:[.,]\d+)?)\s*(?:mg|g|µg|mcg|ml|UI|U\.I\.)?\s*(?:–|-|à|jusqu'à)\s*(\d+(?:['’ ]?\d{3})*(?:[.,]\d+)?)\s*(mg/kg|µg/kg|mg/m2|mg/m²|mg|g|µg|mcg|microgrammes|ml|mmol|UI|U\.I\.)")
CONV = {"g": [("mg", 1000)], "mg": [("g", 0.001), ("µg", 1000)], "µg": [("mg", 0.001)]}

def dans_intervalle(val, unite, txt):
    v = _num(val)
    for a, b, u in RANGE.findall(txt):
        u = u.replace("m2", "m²").replace("mcg", "µg").replace("microgrammes", "µg").replace("U.I.", "UI")
        f = 1 if u == unite else dict(CONV.get(unite, [])).get(u)
        if f and _num(a) <= v * f <= _num(b):
            return True
    return False

def present(val, unite, txt):
    if not txt:
        return False
    if _present(val, unite, txt) or dans_intervalle(val, unite, txt):
        return True
    for u2, f in CONV.get(unite, []):
        w = _num(val) * f
        ws = ("%g" % w)
        alt = {ws, ws.replace(".", ","), "{:,}".format(int(w)).replace(",", "'") if w == int(w) else ws, "{:,}".format(int(w)).replace(",", " ") if w == int(w) else ws}
        if any(re.search(r"(?<![\d,.'])%s\s*%s\b" % (re.escape(a), re.escape(u2)), txt) for a in alt):
            return True
    return False

def _present(val, unite, txt):
    v = val.replace(".", ",")
    alts = {v, v.replace(",", ".")}
    u = re.escape(unite).replace("µg", "(?:µg|mcg|microgrammes?)").replace("m²", "m(?:²|2)").replace("UI", "(?:UI|U\\.I\\.|unités)")
    return any(re.search(r"(?<![\d,.])%s\s*(?:(?:[-–à/]|et|ou)\s*\d+(?:[.,]\d+)?\s*)?%s" % (re.escape(a), u), txt) or
               re.search(r"(?<![\d,.])\d+(?:[.,]\d+)?\s*(?:[-–à/]|et|ou)\s*%s\s*%s" % (re.escape(a), u), txt)
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
    nom = re.sub(r"(\w{5,})-(\w{5,})", r"\1/\2", nom)
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
            nn = norm(nom.split("(")[0]).strip()
            mols = [(nom.split("(")[0].strip(), (MARQUE.findall(nom) or [None])[0])] if nn in SYN_ATC and ("-" in nn or "/" in nn) else molecules(nom)
            fiches, noms_ok, absentes, autres = [], [], [], []
            for dci, mq in mols:
                cands = idx.cherche(dci, mq)
                if cands:
                    fiches.append(cands[0]); noms_ok.append(dci)
                    autres += cands[1:30]
                else:
                    absentes.append((dci, mq))
            for w in idx.dans_texte(nom + " " + pos):
                f = idx.cherche(w) or [idx.vocab[w]]
                if f[0]["id"] not in {x["id"] for x in fiches}:
                    fiches.append(f[0]); noms_ok.append(w)
            for w in list(noms_ok[len(mols) - len(absentes):]):
                pass
            for f in fiches + autres:
                if f["id"] not in cache:
                    cache[f["id"]] = idx.fiche(f)
            pos_all = "\n".join(cache[f["id"]]["posologie"] for f in fiches + autres)
            ok = [(v, u, present(v, u, pos_all)) for v, u in ds]
            preuve = []
            if fiches and any(not o for _, _, o in ok):
                mots = {w for w in re.findall(r"\w{5,}", norm(p["nom"]))}
                phr = [x.strip() for x in re.split(r"(?<=[.:;])\s+|\n", pos_all) if re.search(r"\d", x)]
                phr.sort(key=lambda x: -sum(w in norm(x) for w in mots))
                preuve = [x[:230] for x in phr[:2]]
            aips = [dict(dci=n_, titre=f["titre"], auth=f["auth"], regnr=f["regnr"], atc=f["atc"], maj=cache[f["id"]]["maj"]) for n_, f in zip(noms_ok, fiches)]
            lignes.append(dict(t=t, aips=aips, absentes=absentes, doses=ok, preuve=preuve))
        revue = []
        for L in lignes:
            for dci, mq in L["absentes"]:
                if (L["doses"] and not L["aips"]) or (MEDIC.search(dci.split()[0] if dci else "") and not GESTE.search(dci)):
                    revue.append("absente:" + dci)
            if any(not o for _, _, o in L["doses"]) and L["aips"]:
                revue.append("dose:" + L["t"].split("|")[0].strip()[:30])
        rapport.append(dict(organe=p["organe"], nom=p["nom"], s=p["s"], aV=p["aV"], lignes=lignes, revue=revue))
    if "--json" in sys.argv:
        json.dump(rapport, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    rev = "--revue" in sys.argv
    print("AUTO (doses toutes retrouvées) : %d / %d" % (sum(not r["revue"] for r in rapport), len(rapport)))
    for r in rapport:
        if rev and not r["revue"]:
            continue
        print("\n## %s — %s   [%s]" % (r["nom"], r["organe"], ", ".join(r["revue"])))
        for L in r["lignes"]:
            pb = any(not o for _, _, o in L["doses"]) and L["aips"] or any(("absente:" + d) in r["revue"] for d, _ in L["absentes"])
            if rev and not pb:
                continue
            print("  t %s" % L["t"][:230])
            print("    AIPS : %s" % " ; ".join("%s → %s [%s, %s]" % (a["dci"], a["titre"][:30], a["regnr"], a["maj"]) for a in L["aips"]) if L["aips"] else "    AIPS : aucune")
            if L["doses"]:
                print("    doses : " + " ".join(("✓" if o else "✗") + v + u for v, u, o in L["doses"]))
            for d, m in L["absentes"]:
                if ("absente:" + d) in r["revue"]:
                    print("    ✗ sans AIPS : %s" % d)
            for x in L["preuve"]:
                print("        « %s »" % x)

if __name__ == "__main__":
    main()
