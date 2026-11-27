"""Preuve visuelle de l'onglet Biologie (BRIEF_BIOLOGIE § 4.7) : une fiche par matrice, à 1280 et à 380 px, 0 erreur de console.
Usage : python3 capture_biologie.py <racine du site assemblé (dossier qui contient jeux/)> <dossier des captures>
Chaque scène ouvre la chaîne matrice → examen → diagnostic, puis la fiche à 3 temps en fenêtre centrée ; deux scènes montrent la
vue « par système » et un calculateur. Chromium + SwiftShader, comme capture_paraclinique.py. Signature : AAI (Anthropic AI)"""
import functools, http.server, json, os, socketserver, sys, threading
from playwright.sync_api import sync_playwright

racine, sortie = sys.argv[1], sys.argv[2]
os.makedirs(sortie, exist_ok=True)
class Muet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


H = functools.partial(Muet, directory=racine)
srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), H); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{port}/jeux/paraclinique/index.html#onglet=biologie"
reseau = json.load(open(os.path.join(racine, "jeux", "paraclinique", "donnees", "reseau_biologie.json"), encoding="utf-8"))
N = reseau["noeuds"]
enf = {}
for n in N:
    for p in n.get("de", []):
        enf.setdefault(p, []).append(n)
SC = []
for i, m in enumerate(reseau["bio"]["matrices"], 1):
    ex = [n for n in enf.get(f"bm_{i}", []) if n["nature"] == "Examen"]
    if not ex:
        continue
    # la fiche montrée : de préférence une fiche dont le Traitement est rédigé, avec un calculateur
    ex.sort(key=lambda n: (bool(n.get("trtAProduire")), not any(k["nature"] in ("Calcul", "Critère") for k in enf.get(n["id"], []))))
    e = ex[0]; d = next((k for k in enf.get(e["id"], []) if k["nature"] == "Diagnostic"), None)
    chemin = [f"bm_{i}", e["id"]] + ([d["id"]] if d else [])
    SC.append((f"B{i}_reseau_{e['bioFiche']}", f"J.ouvrirChemin({json.dumps(chemin)});"))
    SC.append((f"B{i}_fiche_{e['bioFiche']}", f"J.ouvrirChemin({json.dumps(chemin)});J.action(J.etat.byId[{json.dumps(e['id'])}],'fiche');"))
SC.append(("B10_vue_systeme", "document.querySelector('#bioOutils [data-vue=systeme]').click();await new Promise(r=>setTimeout(r,800));J.ouvrirChemin(['bs_S6']);"))
SC.append(("B11_calculateur_ascite", "J.ouvrirChemin(['bm_6','bx_EX-1-S5-liquide-ascite']);J.action(J.etat.byId['bx_EX-1-S5-liquide-ascite__calc_gradient_albumine_ascite'],'outil');"))
err, bilan = [], {"scenes": 0}
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=os.environ.get("CHROME") or None, args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    for larg, haut in ((1280, 800), (380, 820)):
        for nom, js in SC:
            pg = b.new_page(viewport={"width": larg, "height": haut})
            pg.on("pageerror", lambda e, n=nom: err.append(f"{larg} {n} JS {e}"))
            pg.on("console", lambda m, n=nom: m.type == "error" and err.append(f"{larg} {n} console {m.text}"))
            pg.on("response", lambda r, n=nom: r.status >= 400 and err.append(f"{larg} {n} HTTP {r.status} {r.url}"))
            pg.goto(base)
            pg.wait_for_function("window.__pret===true", timeout=90000)
            pg.evaluate("async()=>{const J=window.__jeu;" + js + "}")
            pg.wait_for_timeout(1800)
            hs = pg.evaluate("document.documentElement.scrollWidth>innerWidth||document.body.scrollWidth>innerWidth")
            if hs:
                err.append(f"{larg} {nom} défilement horizontal")
            pg.screenshot(path=os.path.join(sortie, f"{nom}_{larg}.png")); bilan["scenes"] += 1
            pg.close()
    b.close()
srv.shutdown()
bilan["erreurs"] = len(err)
print(json.dumps(bilan, ensure_ascii=False)); [print(e) for e in err[:40]]
sys.exit(1 if err else 0)
