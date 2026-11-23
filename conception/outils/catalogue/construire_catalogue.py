"""Catalogue de captures des systèmes jouables (0 token) : 3 planches par système rédigé, sur le corps 3D réel.
1. construit corps.glb depuis BodyParts3D s'il manque (mêmes étapes que le skill 3d-images-upload-super) ;
2. ouvre reseau3d.html sans écran (Chromium + SwiftShader) et capture : vue d'ensemble, physiopathologie dépliée avec infobulle, fenêtre de courbe ;
3. écrit conception/catalogue/ (index.html, img/, polices Atkinson).
Lancé par .github/workflows/catalogue.yml à chaque changement de tetrade.json. Signature : AAI (Anthropic AI)"""
import collections, html, json, os, shutil, subprocess, sys, time

ICI = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(ICI); RAC = os.path.dirname(os.path.dirname(OUT))
MOT = os.path.join(RAC, "conception", "prototypes", "moteur"); CAT = os.path.join(RAC, "conception", "catalogue")
sys.path.insert(0, OUT)
from systemes_rediges import REDIGES, SOURCES  # noqa: E402
PREF = {"Cardiovasculaire": "coe", "Respiratoire": "pou", "Digestif et hépatobiliaire": "dg_foie"}
LEG = ["La vue d'ensemble montre le système ouvert sur le corps 3D réel, avec ses organes rangés du haut vers le bas.",
       "L'espace physiopathologie déplie les 4 paliers ; l'infobulle donne le mécanisme, le bilan par visée, le traitement et la source.",
       "La fenêtre de courbe calcule le phénomène en direct : les boutons changent de scénario et les curseurs bougent les paramètres."]


def corps():
    glb = os.path.join(MOT, "corps.glb")
    if os.path.exists(glb):
        return glb
    sk = os.path.join(RAC, "skills", "3d-images-upload-super", "scripts")
    os.makedirs("/tmp/w", exist_ok=True)
    if not os.path.isdir("/tmp/bp3d"):
        subprocess.run(["git", "clone", "-q", "--filter=blob:none", "--no-checkout", "https://github.com/Kevin-Mattheus-Moerman/BodyParts3D.git", "/tmp/bp3d"], check=True)
        subprocess.run(["git", "-C", "/tmp/bp3d", "-c", "gc.auto=0", "checkout", "HEAD", "--", "assets/BodyParts3D_data/composite_parts.txt"], check=True)
    subprocess.run([sys.executable, os.path.join(sk, "expand.py")], check=True, cwd="/tmp/w")
    R = json.load(open("/tmp/w/parts.json"))
    open("/tmp/w/paths.txt", "w").write("\n".join(f"assets/BodyParts3D_data/stl/{p}.stl" for v in R.values() for p in v) + "\n")
    subprocess.run(["git", "-C", "/tmp/bp3d", "-c", "gc.auto=0", "checkout", "HEAD", "--pathspec-from-file=/tmp/w/paths.txt"], check=True)
    subprocess.run([sys.executable, os.path.join(sk, "build_glb.py")], check=True, cwd="/tmp/w")
    shutil.copy("/tmp/w/corps.glb", glb)
    return glb


def plan():
    c = json.load(open(os.path.join(MOT, "tetrade.json"), encoding="utf-8")); N = c["noeuds"]; B = {n["id"]: n for n in N}
    global B3; B3 = B
    kids = collections.defaultdict(list)
    for n in N:
        for d in n.get("de") or []:
            kids[d].append(n["id"])
    def desc(i):
        for k in kids[i]:
            yield k; yield from desc(k)
    racines = {n["texte"]: n["id"] for n in N if not n.get("de")}
    P = []
    for nom, conf in REDIGES.items():
        sid = racines.get(nom) or next((i for t, i in racines.items() if t.split(" ")[0] == nom.split(" ")[0]), None)
        if not sid:
            continue
        orgs = kids[sid]; sc = lambda o: sum(1 for k in kids[o] if B[k].get("nature") == "Palier")
        org = PREF.get(nom) if PREF.get(nom) in orgs and sc(PREF[nom]) else max(orgs, key=sc)
        pal = [k for k in kids[org] if B[k].get("nature") == "Palier"]
        cap = [("Vue d'ensemble du système (anatomie)", f"cfg=tetrade.json&espace=anatomie&ouvrir={sid}", 0)]
        if pal:
            u = next((k for k in pal if k.endswith("_xu")), pal[0]); pa = kids[u][0]
            cap.append((f"{B[org]['texte']} : 4 paliers, infobulle « {B[pa]['texte']} »", f"cfg=tetrade.json&espace=physiopathologie&ouvrir={sid},{org},{','.join(pal)}&bulle={pa}", 1))
        fen = next((k for k in desc(sid) if B[k].get("fenetre") not in (None, "3d") and B[k].get("espace") == "physiologie"), None)
        if fen:
            cap.append((f"Fenêtre de courbe : {B[fen]['texte']}", f"cfg=tetrade.json&espace=physiologie&ouvrir={sid}&fenetre={fen}", 2))
        f3 = next(iter(sorted((k for k in desc(sid) if B[k].get("fenetre") == "3d" and ORG3D.get(org3d(k), {}).get("statut") == "produit"), key=lambda k: org3d(k) != org)), None)
        if f3:
            cap.append((f"Organe 3D réel rotatif : {ORG3D[org3d(f3)]['nom']}", f"cfg=tetrade.json&espace={B[f3].get('espace','anatomie')}&ouvrir={sid}&fenetre={f3}", 2))
        S = SOURCES[nom]
        P.append({"nom": nom, "couleur": conf["couleur"], "stat": f"{len(S['organes'])} organes · {sum(len(v) for v in S['pathos'].values())} pathologies", "captures": cap})
    return P


ORG3D = json.load(open(os.path.join(MOT, "anatomie3d", "index.json"), encoding="utf-8"))["organes"] if os.path.exists(os.path.join(MOT, "anatomie3d", "index.json")) else {}


def org3d(k):
    m = B3[k]
    while m and m["id"] not in ORG3D:
        m = B3.get((m.get("de") or [None])[0])
    return m["id"] if m else None


def captures(P):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    os.makedirs(os.path.join(CAT, "img"), exist_ok=True)
    for f in ("atkinson-hyperlegible-latin-400-normal.woff2", "atkinson-hyperlegible-latin-700-normal.woff2"):
        shutil.copy(os.path.join(OUT, f), os.path.join(MOT, "atk" + f.split("-")[3] + ".woff2"))
        shutil.copy(os.path.join(OUT, f), os.path.join(CAT, "atk" + f.split("-")[3] + ".woff2"))
    srv = subprocess.Popen([sys.executable, "-m", "http.server", "8765", "-d", MOT], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); time.sleep(1)
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
            pg = b.new_page(viewport={"width": 1600, "height": 1000})
            for i, s in enumerate(P):
                for j, (_, cfg, _k) in enumerate(s["captures"]):
                    pg.goto("about:blank"); pg.goto("http://localhost:8765/reseau3d.html#" + cfg + "&capture")
                    pg.wait_for_function("document.title==='PRET'", timeout=120000)
                    if "Organe 3D" in s["captures"][j][0]:
                        pg.wait_for_function("window.__v3d===1", timeout=90000); pg.wait_for_timeout(2500)
                    pg.wait_for_timeout(1500)
                    png = f"/tmp/cap_{i}_{j}.png"; pg.screenshot(path=png)
                    Image.open(png).convert("RGB").save(os.path.join(CAT, "img", f"cap_{i}_{j}.jpg"), quality=82, optimize=True)
                    print("capture", s["nom"], j, flush=True)
            b.close()
    finally:
        srv.kill()


def page(P):
    nav = "".join(f'<a href="#s{i}"><b>{i + 1}</b>{html.escape(p["nom"])}</a>' for i, p in enumerate(P)); sec = ""
    for i, p in enumerate(P):
        figs = "".join(f'<figure><button class="z" data-src="img/cap_{i}_{j}.jpg" aria-label="Agrandir"><img src="img/cap_{i}_{j}.jpg" alt="{html.escape(t)}" loading="lazy"></button>'
                       f'<figcaption><strong>{html.escape(t)}</strong> {LEG[k]}</figcaption></figure>'
                       for j, (t, _, k) in enumerate(p["captures"]))
        sec += f'<section id="s{i}" style="--c:{p["couleur"]}"><h2><span>{i + 1}</span>{html.escape(p["nom"])}</h2><p class="m">{p["stat"]}</p>{figs}</section>'
    gabarit = open(os.path.join(ICI, "gabarit.html"), encoding="utf-8").read()
    out = gabarit.replace("{{NAV}}", nav).replace("{{SECTIONS}}", sec).replace("{{N}}", str(len(P))).replace("{{DATE}}", time.strftime("%d.%m.%Y"))
    open(os.path.join(CAT, "index.html"), "w", encoding="utf-8").write(out)


if __name__ == "__main__":
    corps(); P = plan(); captures(P); page(P)
    print(f"catalogue : {len(P)} systèmes, {sum(len(p['captures']) for p in P)} planches")
