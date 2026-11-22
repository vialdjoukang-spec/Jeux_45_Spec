"""Circuit d'images de la paraclinique (0 token) : vrais clichés sous licence libre pour chaque examen et chaque analyse.
Tourne dans GitHub Actions (accès Internet gratuit) : .github/workflows/cliches.yml.
Usage : python projets/outils/chercher_cliches.py [--limite N] [--tout] [--filtre texte]
Sources : Wikimedia Commons (licences libres vérifiées dans les métadonnées, jamais de SVG),
          puis Open-i (NIH, figures d'articles en accès libre ; licence marquée « à vérifier »).
Sortie : conception/donnees/images/<même chemin que la donnée>.json
         {"cliches": {id: [{titre, url, vignette, page, licence, auteur, source, requete, statut, montre}]}}
statut « candidat » → validé ou rejeté par l'IA de validation, puis contre-audit Claude.
Signature : AAI (Anthropic AI)"""
import json, os, sys, glob, re, time, urllib.parse, urllib.request, datetime

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = [("paraclinique/topographie", "examens"), ("paraclinique/biologie", "analyses")]
UA = {"User-Agent": "Jeux45Spec-cliches/1.0 (https://github.com/vialdjoukang-spec/Jeux_45_Spec; contenu pédagogique)"}
LIBRES = re.compile(r"^(cc0|cc[- ]by(-sa)?([- ][0-9.]+)?|public domain|pd|attribution|gfdl)", re.I)
INTERDIT = re.compile(r"\b(nc|nd)\b", re.I)
PAR_EXAMEN, PAR_REQUETE = 6, 5

FR_EN = {  # jetons médicaux FR → EN (Commons et Open-i indexent surtout en anglais)
 "radiographie": "radiograph", "radio": "radiograph", "thorax": "chest", "thoracique": "chest", "ct": "CT", "scanner": "CT scan",
 "irm": "MRI", "échographie": "ultrasound", "echographie": "ultrasound", "doppler": "Doppler", "scintigraphie": "scintigraphy",
 "pet-ct": "PET-CT", "pet": "PET", "angiographie": "angiography", "angio-ct": "CT angiography", "artériographie": "arteriography",
 "mammographie": "mammography", "densitométrie": "DEXA", "spirométrie": "spirometry flow-volume", "pléthysmographie": "plethysmography",
 "électrocardiogramme": "electrocardiogram", "ecg": "ECG", "holter": "Holter ECG", "électroencéphalogramme": "EEG", "eeg": "EEG",
 "électromyographie": "electromyography", "emg": "EMG", "audiogramme": "audiogram", "audiométrie": "audiogram", "tympanométrie": "tympanogram",
 "fond": "fundus", "œil": "fundus", "oeil": "eye", "rétinographie": "retinal photograph", "oct": "optical coherence tomography",
 "endoscopie": "endoscopy", "gastroscopie": "gastroscopy", "coloscopie": "colonoscopy", "bronchoscopie": "bronchoscopy", "cystoscopie": "cystoscopy",
 "laryngoscopie": "laryngoscopy", "biopsie": "biopsy", "histologie": "histology", "cytologie": "cytology", "frottis": "smear",
 "sanguin": "blood", "sang": "blood", "urine": "urine", "urines": "urine", "culture": "culture", "gram": "Gram stain",
 "électrophorèse": "electrophoresis", "protéines": "protein", "hémogramme": "blood smear", "formule": "blood count",
 "poumon": "lung", "poumons": "lung", "cœur": "heart", "coeur": "heart", "foie": "liver", "rein": "kidney", "reins": "kidney",
 "cerveau": "brain", "cérébrale": "brain", "encéphale": "brain", "rachis": "spine", "genou": "knee", "épaule": "shoulder", "hanche": "hip",
 "abdominal": "abdominal", "abdomen": "abdomen", "pelvien": "pelvic", "thyroïde": "thyroid", "pancréas": "pancreas", "rate": "spleen",
 "vessie": "bladder", "prostate": "prostate", "utérus": "uterus", "ovaires": "ovary", "sein": "breast", "côlon": "colon", "estomac": "stomach",
 "œsophage": "esophagus", "oesophage": "esophagus", "pneumonie": "pneumonia", "fracture": "fracture", "épanchement": "effusion",
 "pleural": "pleural", "plèvre": "pleura", "test": "test", "effort": "exercise", "marche": "walk", "gazométrie": "arterial blood gas",
 "polysomnographie": "polysomnography", "fibroscopie": "fiberoptic endoscopy", "lavage": "lavage", "bronchoalvéolaire": "bronchoalveolar",
 "opacité": "opacity", "alvéolaire": "consolidation", "bronchogramme": "air bronchogram", "nodule": "nodule", "masse": "mass",
 "pneumothorax": "pneumothorax", "atélectasie": "atelectasis", "emphysème": "emphysema", "fibrose": "fibrosis", "verre": "ground-glass",
 "dépoli": "opacity", "kyste": "cyst", "abcès": "abscess", "lithiase": "stone", "calcul": "stone", "sténose": "stenosis", "thrombose": "thrombosis",
 "embolie": "embolism", "hémorragie": "hemorrhage", "infarctus": "infarction", "ischémie": "ischemia", "tumeur": "tumor", "cancer": "cancer",
 "obstructif": "obstructive", "restrictif": "restrictive", "courbe": "curve", "débit-volume": "flow-volume", "sus-décalage": "ST elevation",
 "granulome": "granuloma", "granulomes": "granuloma", "inflammation": "inflammation", "dilatation": "dilatation", "normal": "normal", "normale": "normal",
 "ponction": "puncture", "lombaire": "lumbar", "lcr": "cerebrospinal fluid", "articulaire": "joint", "liquide": "fluid",
}
VIDE = {"de", "du", "des", "la", "le", "les", "et", "avec", "sans", "en", "au", "aux", "à", "d", "l", "par", "pour", "sur"}


def anglais(t):
    mots = re.findall(r"[\wœéèêàâîôûç'-]+", t or "")
    garde = [FR_EN[m.lower()] if m.lower() in FR_EN else m for m in mots
             if m.lower() in FR_EN or (m.isupper() and len(m) > 1) or re.search(r"\d", m)]
    return " ".join(garde)[:90]


def get(url):
    for essai in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
                return json.load(r)
        except Exception:
            time.sleep(2 + 3 * essai)
    return {}


def commons(q):
    p = {"action": "query", "format": "json", "generator": "search", "gsrnamespace": 6, "gsrlimit": 12,
         "gsrsearch": q + " filetype:bitmap", "prop": "imageinfo", "iiprop": "url|mime|extmetadata", "iiurlwidth": 640}
    pages = (get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(p)).get("query") or {}).get("pages") or {}
    out = []
    for pg in sorted(pages.values(), key=lambda x: x.get("index", 99)):
        ii = (pg.get("imageinfo") or [{}])[0]
        md = ii.get("extmetadata") or {}
        lic = (md.get("LicenseShortName") or {}).get("value", "")
        if "svg" in ii.get("mime", "") or not LIBRES.search(lic.strip()) or INTERDIT.search(lic):
            continue
        aut = re.sub("<[^>]+>", "", (md.get("Artist") or {}).get("value", ""))[:120]
        out.append({"titre": pg["title"].replace("File:", ""), "url": ii.get("url"), "vignette": ii.get("thumburl"),
                    "page": ii.get("descriptionurl"), "licence": lic, "auteur": aut, "source": "Wikimedia Commons"})
    return out[:PAR_REQUETE]


def openi(q):
    d = get("https://openi.nlm.nih.gov/api/search?" + urllib.parse.urlencode({"query": q, "m": 1, "n": PAR_REQUETE}))
    out = []
    for it in d.get("list") or []:
        img = it.get("imgLarge") or it.get("imgThumbLarge")
        if not img:
            continue
        out.append({"titre": ((it.get("image") or {}).get("caption") or it.get("title") or "")[:160],
                    "url": "https://openi.nlm.nih.gov" + img, "vignette": "https://openi.nlm.nih.gov" + (it.get("imgThumb") or img),
                    "page": it.get("pmc_url") or ("https://openi.nlm.nih.gov/detailedresult?img=" + str(it.get("uid", ""))),
                    "licence": "à vérifier (article en accès libre PMC)", "auteur": it.get("journal_title", ""), "source": "Open-i (NIH)"})
    return out


def requetes(x, defis):
    nom = x.get("nom", "")
    en = anglais(nom)
    q = [en] if len(en.split()) >= 2 else [en, re.sub(r"\(.*?\)", "", nom).strip()]
    for a in (x.get("anomaliesElementaires") or [])[:1] + [d.get("aspectRecherche") for d in defis if d.get("aspectRecherche")][:2]:
        if isinstance(a, dict): a = a.get("nom") or a.get("aspect")
        if a: q.append((anglais(nom) + " " + anglais(a)).strip())
    return [s for i, s in enumerate(q) if s and s not in q[:i]][:3]


args = sys.argv[1:]
limite = int(args[args.index("--limite") + 1]) if "--limite" in args else 10 ** 6
filtre = args[args.index("--filtre") + 1].lower() if "--filtre" in args else ""
tout, faits, bilan = "--tout" in args, 0, {"examens": 0, "avec_cliches": 0, "sans": []}
for sous, cle in SRC:
    for f in sorted(glob.glob(os.path.join(RAC, "conception/donnees", sous, "**/*.json"), recursive=True)):
        rel = os.path.relpath(f, os.path.join(RAC, "conception/donnees"))
        if filtre and filtre not in rel.lower():
            continue
        d = json.load(open(f, encoding="utf-8"))
        prat = os.path.join(RAC, "conception/donnees/pratique", rel)
        defis = {e.get("ref") or e.get("id"): e.get("defis", []) for e in (json.load(open(prat, encoding="utf-8")).get("entites", []) if os.path.exists(prat) else [])}
        sortie = os.path.join(RAC, "conception/donnees/images", rel)
        img = json.load(open(sortie, encoding="utf-8")) if os.path.exists(sortie) else {"_meta": {"source": rel, "signature": "AAI (Anthropic AI)"}, "cliches": {}}
        for x in d.get(cle, []):
            bilan["examens"] += 1
            deja = img["cliches"].get(x["id"], [])
            if (len(deja) >= 3 and not tout) or faits >= limite:
                bilan["avec_cliches"] += bool(deja); continue
            vus, cands = {c["url"] for c in deja}, list(deja)
            for q in requetes(x, defis.get(x["id"], [])):
                for c in commons(q) + (openi(q) if len(cands) < 3 else []):
                    if c["url"] and c["url"] not in vus and len(cands) < PAR_EXAMEN:
                        vus.add(c["url"]); cands.append({**c, "requete": q, "statut": "candidat", "montre": None})
                time.sleep(0.3)
            img["cliches"][x["id"]] = cands
            faits += 1
            bilan["avec_cliches"] += bool(cands)
            if not cands: bilan["sans"].append(f"{rel} › {x['nom']}")
        os.makedirs(os.path.dirname(sortie), exist_ok=True)
        img["_meta"]["maj"] = f"{datetime.datetime.now():%Y-%m-%d %H:%M}"
        json.dump(img, open(sortie, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
r = os.path.join(RAC, "conception/donnees/images/RAPPORT_CLICHES.md")
os.makedirs(os.path.dirname(r), exist_ok=True)
open(r, "w", encoding="utf-8").write(
    f"# Couverture en clichés — {datetime.datetime.now():%Y-%m-%d %H:%M}\n\n{bilan['avec_cliches']}/{bilan['examens']} entités ont au moins un candidat.\n\n"
    "## Sans aucun candidat (requête à affiner)\n" + "\n".join(f"- {s}" for s in bilan["sans"]) + "\n\nSignature : AAI (Anthropic AI)\n")
print(f"{bilan['avec_cliches']}/{bilan['examens']} avec candidats ; {len(bilan['sans'])} sans → {os.path.relpath(r, RAC)}")
