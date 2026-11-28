"""Chaîne des clichés de l'Imagerie (couloir 3) : chercher → regarder → appliquer. Python 3 stdlib + Pillow.
Sources : Wikimedia Commons uniquement (licence lue dans extmetadata.LicenseShortName ; liste blanche CC0 / PD / CC BY / CC BY-SA ;
NC et ND refusés ; jamais de SVG ; organes génitaux externes exclus par mots du titre et de la description).
Open-i n'est pas retenu : sa licence n'est pas lisible dans l'API (« à vérifier »), ce que la règle interdit.

  python3 outil_cliches.py chercher <requetes.json> <dossier_sortie>
      requetes.json : {cle: {"q": ["requête anglaise", ...], "re": "regex obligatoire titre+description"}}
      → <sortie>/candidats.json + planches PNG (8 cibles × 4 candidats) à regarder avec Read.
  python3 outil_cliches.py appliquer <choix.json> <candidats.json>
      choix.json : {cle: {"c": rang choisi (0-3) | null, "pourquoi": "...", "normal": clé de normaux.json | null,
                          "dx": "diagnostic FR", "cliche": "US — mode B", "region": "...", "plan": "..."}}
      → atlas/manifest/IMC-xxxx.json, atlas/patho/IMC-xxxx_patho.jpg, atlas_liens/<organe>.json.
  python3 outil_cliches.py normal <cle> <Fichier Commons> <modalite> <region> <plan>   → ajoute un normal vérifié à normaux.json
Signature : AAI (Anthropic AI)"""
import json, os, re, sys, time, hashlib, io, urllib.parse, urllib.request, urllib.error
from PIL import Image, ImageDraw, ImageFont

ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
P = os.path.join(RAC, "conception", "donnees", "paraclinique")
ATL_M = os.path.join(P, "atlas", "manifest"); ATL_I = os.path.join(RAC, "conception", "prototypes", "paraclinique", "atlas")
CACHE = os.environ.get("CLICHES_CACHE", "/tmp/cliches_cache"); os.makedirs(CACHE, exist_ok=True)
UA = {"User-Agent": "EduRadiologyAtlas/1.0 (educational, non-commercial; python-urllib)"}
LIBRES = re.compile(r"^(cc0|cc[- ]by(-sa)?([- ][0-9.]+)?( [a-z]{2,})?|public domain|pd|attribution|gfdl)$", re.I)
INTERDIT = re.compile(r"\b(nc|nd)\b", re.I)
GENITAL = re.compile(r"penis|penile|scrot|testi|testic|vulv|labia|clitor|glans|foreskin|phimos|hypospad|epididym", re.I)
NORMAUX = os.path.join(ICI, "normaux.json")


def get(url, binaire=False, essais=7):
    """GET avec cache disque ; respecte Retry-After sur 429 (limites Wikimedia), rythme ≥ 1,5 s entre deux appels réseau."""
    k = os.path.join(CACHE, hashlib.sha256(url.encode()).hexdigest()[:24])
    if os.path.exists(k):
        b = open(k, "rb").read(); return b if binaire else json.loads(b)
    for e in range(essais):
        try:
            time.sleep(1.5)
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                b = r.read()
            open(k, "wb").write(b)
            return b if binaire else json.loads(b)
        except urllib.error.HTTPError as ex:
            att = int(ex.headers.get("Retry-After") or 0) if ex.code == 429 else 0
            print("   ⚠", ex.code, f"attente {max(att, 5 * (e + 1))} s", url[:80], flush=True); time.sleep(max(att, 5 * (e + 1)) + 1)
        except Exception as ex:
            print("   ⚠", type(ex).__name__, str(ex)[:80], url[:80], flush=True); time.sleep(3 + 6 * e)
    return None


def nettoie(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h or "")).strip()


def commons(q, n=15):
    p = {"action": "query", "format": "json", "generator": "search", "gsrnamespace": 6, "gsrlimit": n,
         "gsrsearch": q + " filetype:bitmap", "prop": "imageinfo", "iiprop": "url|mime|size|extmetadata", "iiurlwidth": 300,
         "iiextmetadatafilter": "LicenseShortName|LicenseUrl|Artist|ImageDescription"}
    pages = (((get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(p)) or {}).get("query") or {}).get("pages") or {})
    out = []
    for pg in sorted(pages.values(), key=lambda x: x.get("index", 99)):
        ii = (pg.get("imageinfo") or [{}])[0]; md = ii.get("extmetadata") or {}
        lic = nettoie((md.get("LicenseShortName") or {}).get("value", ""))
        if "svg" in ii.get("mime", "") or ii.get("mime", "") not in ("image/jpeg", "image/png", "image/gif", "image/webp", "image/tiff"):
            continue
        if not LIBRES.search(lic) or INTERDIT.search(lic):
            continue
        desc = nettoie((md.get("ImageDescription") or {}).get("value", ""))[:600]
        titre = pg["title"].replace("File:", "")
        if GENITAL.search(titre + " " + desc):
            continue
        out.append({"titre": titre, "page": ii.get("descriptionurl"), "url": ii.get("url"), "vignette": ii.get("thumburl"),
                    "licence": lic, "licence_url": nettoie((md.get("LicenseUrl") or {}).get("value", "")),
                    "auteur": nettoie((md.get("Artist") or {}).get("value", ""))[:160], "description": desc,
                    "taille": [ii.get("width"), ii.get("height")], "requete": q})
    return out


def police(t):
    for f in ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/dejavu/DejaVuSans.ttf"):
        if os.path.exists(f):
            return ImageFont.truetype(f, t)
    return ImageFont.load_default()


def chercher(freq, sortie):
    R = json.load(open(freq, encoding="utf-8")); os.makedirs(sortie, exist_ok=True)
    C = {}
    for k, v in R.items():
        if k.startswith("_"):
            continue
        rx = re.compile(v.get("re") or ".", re.I); vus, L = set(), []
        for q in v["q"]:
            for c in commons(q):
                if c["page"] in vus or not rx.search(c["titre"] + " " + c["description"]):
                    continue
                vus.add(c["page"]); L.append(c)
            if len(L) >= 4:
                break
        C[k] = L[:4]; print(f"{len(C[k])} {k}", flush=True)
    json.dump(C, open(os.path.join(sortie, "candidats.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    planches(C, sortie)


def planches(C, sortie, par=8, w=300, h=230):
    f1, f2 = police(15), police(12); cles = list(C)
    for i in range(0, len(cles), par):
        S = Image.new("RGB", (w * 4 + 10, (h + 46) * min(par, len(cles) - i)), "white"); d = ImageDraw.Draw(S)
        for j, k in enumerate(cles[i:i + par]):
            y = j * (h + 46); d.text((4, y + 2), f"[{i + j}] {k}"[:150], fill="black", font=f1)
            for r, c in enumerate(C[k]):
                b = get(c["vignette"], True) if c.get("vignette") else None
                try:
                    im = Image.open(io.BytesIO(b)).convert("RGB"); im.thumbnail((w - 6, h - 4)); S.paste(im, (r * w + 2, y + 22))
                except Exception:
                    d.text((r * w + 8, y + 60), "image illisible", fill="red", font=f2)
                d.text((r * w + 4, y + h + 22), f"{r}: {c['titre'][:40]}", fill="#333", font=f2)
        S.save(os.path.join(sortie, f"planche_{i // par:02d}.png"))


def prochain_id():
    n = [int(m.group(1)) for f in os.listdir(ATL_M) for m in [re.match(r"IMC-(\d+)\.json$", f)] if m]
    return f"IMC-{(max(n) if n else 0) + 1:04d}"


def jpeg(b, dest, cote=1024):
    im = Image.open(io.BytesIO(b)).convert("RGB"); im.thumbnail((cote, cote))
    os.makedirs(os.path.dirname(dest), exist_ok=True); im.save(dest, "JPEG", quality=85, optimize=True)
    return im.size


def vignette_1024(page_titre):
    p = {"action": "query", "format": "json", "titles": "File:" + page_titre, "prop": "imageinfo", "iiprop": "url|mime", "iiurlwidth": 1024}
    pg = next(iter(((get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(p)) or {}).get("query") or {}).get("pages", {}).values()), {})
    ii = (pg.get("imageinfo") or [{}])[0]
    return ii.get("thumburl") or ii.get("url")


def appliquer(fchoix, fcand):
    CH = json.load(open(fchoix, encoding="utf-8")); CA = json.load(open(fcand, encoding="utf-8"))
    NO = json.load(open(NORMAUX, encoding="utf-8")) if os.path.exists(NORMAUX) else {}
    faits = []
    for k, v in CH.items():
        if k.startswith("_") or v.get("c") is None:
            continue
        organe, patho, mod = k.split(" | ")
        c = CA[k][v["c"]]
        liens_f = os.path.join(P, "atlas_liens", organe + ".json")
        L = json.load(open(liens_f, encoding="utf-8")) if os.path.exists(liens_f) else {"_meta": {"role": "Pathologie de Paraclinique → dossier de l'atlas (IMG-xxx), seulement si la modalité du dossier est celle de l'examen.", "signature": "AAI (Anthropic AI)"}}
        deja = L.get(patho); deja = deja if isinstance(deja, list) else ([deja] if deja else [])
        if any(isinstance(x, str) and x.startswith("IMC-") and json.load(open(os.path.join(ATL_M, x + ".json"), encoding="utf-8"))["patho"]["source_url"] == c["page"] for x in deja):
            continue
        i = prochain_id(); dest = os.path.join(ATL_I, "patho", f"{i}_patho.jpg")
        b = get(vignette_1024(c["titre"]), True)
        if not b:
            print("   ✗ téléchargement", k); continue
        W, H = jpeg(b, dest)
        m = {"id": i, "dx": v["dx"], "cliche": v["cliche"], "statut": "partiel",
             "pair_match": v.get("pourquoi", ""),
             "a_verifier": ["Lésion non annotée sur le cliché : contour et flèche à placer par un radiologue."],
             "queries": ["commons search: " + c["requete"]], "couloir": "3 (paraclinique-imagerie-cliches), 28.11.2026",
             "patho": {"file": f"images/patho/{i}_patho.jpg", "source_url": c["page"], "license": c["licence"], "license_url": c.get("licence_url", ""),
                       "author": c["auteur"] or "?", "modality": v["cliche"].split(" — ")[0], "sequence": v["cliche"].split(" — ")[-1],
                       "plane": v.get("plan", "non précisé"), "region": v.get("region", ""), "caption_source": c["description"][:400], "arrows": []}}
        nk = v.get("normal")
        if nk and nk in NO:
            n = NO[nk]
            m["normal"] = {"file": n["file"], "source_url": n["source_url"], "license": n["license"], "license_url": n.get("license_url", ""),
                           "author": n["author"], "modality": n["modality"], "plane": n["plane"], "region": n["region"], "caption_source": n.get("caption_source", "")}
            m["pair_match"] += f" Normal apparié : {n['modality']}, {n['region']}, {n['plane']} (normaux.json « {nk} »)."
        json.dump(m, open(os.path.join(ATL_M, i + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        L[patho] = deja + [i] if deja else i
        json.dump(L, open(liens_f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        faits.append(i); print(f"   ✓ {i} {k} ({W}×{H})", flush=True)
    print(len(faits), "dossiers créés")


def normal(cle, titre, modalite, region, plan):
    NO = json.load(open(NORMAUX, encoding="utf-8")) if os.path.exists(NORMAUX) else {"_meta": {"role": "Clichés normaux vérifiés (regardés) du couloir 3, réutilisables à modalité, région et plan identiques.", "signature": "AAI (Anthropic AI)"}}
    p = {"action": "query", "format": "json", "titles": "File:" + titre, "prop": "imageinfo", "iiprop": "url|mime|extmetadata", "iiurlwidth": 1024}
    pg = next(iter(get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(p))["query"]["pages"].values()))
    ii = pg["imageinfo"][0]; md = ii["extmetadata"]; lic = nettoie(md.get("LicenseShortName", {}).get("value", ""))
    assert LIBRES.search(lic) and not INTERDIT.search(lic) and "svg" not in ii["mime"], f"licence refusée : {lic}"
    f = f"images/normal/IMC-N-{cle}.jpg"; jpeg(get(ii.get("thumburl") or ii["url"], True), os.path.join(ATL_I, "normal", f"IMC-N-{cle}.jpg"))
    NO[cle] = {"file": f, "source_url": ii["descriptionurl"], "license": lic, "license_url": nettoie(md.get("LicenseUrl", {}).get("value", "")),
               "author": nettoie(md.get("Artist", {}).get("value", ""))[:160], "modality": modalite, "region": region, "plane": plan,
               "caption_source": nettoie(md.get("ImageDescription", {}).get("value", ""))[:300]}
    json.dump(NO, open(NORMAUX, "w", encoding="utf-8"), ensure_ascii=False, indent=1); print("normal", cle, lic)


if __name__ == "__main__":
    a = sys.argv[1:]
    {"chercher": lambda: chercher(a[1], a[2]), "appliquer": lambda: appliquer(a[1], a[2]), "normal": lambda: normal(*a[1:6])}[a[0]]()
