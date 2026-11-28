"""Captures Playwright des fenêtres à deux clichés ajoutées par le couloir 3 (patient + normal), à 1280 et 380 px, avec contrôle de la console.
Usage : python3 capture_cliches.py <site assemblé (contient jeux/)> <dossier de sortie> [n=6] [filtre=IMC-]
Ouvre, pour n pathologies dont le cliché vient d'un dossier « filtre », le chemin région → organe → modalité → examen → niveau → pathologie.
Signature : AAI (Anthropic AI)"""
import functools, http.server, json, os, socketserver, sys, threading
from playwright.sync_api import sync_playwright

racine, sortie = sys.argv[1], sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 6; filtre = sys.argv[4] if len(sys.argv) > 4 else "IMC-"
os.makedirs(sortie, exist_ok=True)
H = functools.partial(http.server.SimpleHTTPRequestHandler, directory=racine); H.log_message = lambda *a: None
srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), H); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{port}/jeux/paraclinique/index.html#onglet=imagerie"
R = json.load(open(os.path.join(racine, "jeux/paraclinique/donnees/reseau_imagerie.json"), encoding="utf-8"))
B = {x["id"]: x for x in R["noeuds"]}
cibles = [x for x in R["noeuds"] if x.get("cliches") and (filtre in json.dumps(x["cliches"]))][:n]
err, faits = [], []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=os.environ.get("CHROME", "/opt/pw-browsers/chromium"), args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    for larg, haut in ((1280, 800), (380, 820)):
        for x in cibles:
            ch, y = [], x
            while y:
                ch.insert(0, y["id"]); y = B.get((y.get("de") or [None])[0])
            pg = b.new_page(viewport={"width": larg, "height": haut})
            pg.on("pageerror", lambda e: err.append(f"{larg} JS {e}"))
            pg.on("console", lambda m: m.type == "error" and err.append(f"{larg} console {m.text}"))
            pg.on("response", lambda r: r.status >= 400 and err.append(f"{larg} HTTP {r.status} {r.url}"))
            pg.goto(base); pg.wait_for_function("window.__pret===true", timeout=90000)
            pg.evaluate("ids=>{const J=window.__jeu;J.ouvrirChemin(ids);}", ch)
            pg.wait_for_timeout(2500)
            f = os.path.join(sortie, f"{x['id'][-40:].replace('/', '_')}_{larg}.png"); pg.screenshot(path=f); faits.append(f)
            pg.close()
    b.close()
srv.shutdown()
print(json.dumps({"captures": len(faits), "erreurs": len(err), "cibles": [x["texte"] for x in cibles]}, ensure_ascii=False)); [print(e) for e in err[:30]]
