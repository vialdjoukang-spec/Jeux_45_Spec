"""Contrôle sans écran du jeu Paraclinique : captures à 1280 px et à 380 px de chaque onglet, erreurs de console, chargement du corps 3D.
Usage : python3 capture_paraclinique.py <racine du site assemblé (dossier qui contient jeux/)> <dossier des captures>
Chromium + SwiftShader (WebGL logiciel), comme shot.py du skill obsidian-like-complex-network. Signature : AAI (Anthropic AI)"""
import functools, http.server, json, os, socketserver, sys, threading
from playwright.sync_api import sync_playwright

racine, sortie = sys.argv[1], sys.argv[2]
os.makedirs(sortie, exist_ok=True)
H = functools.partial(http.server.SimpleHTTPRequestHandler, directory=racine); H.log_message = lambda *a: None
srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), H); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{port}/jeux/paraclinique/index.html"
err, bilan = [], {}

SCENES = [  # (nom, hash, script exécuté après le chargement)
    ("0_accueil_imagerie", "onglet=imagerie", ""),
    ("1_imagerie_theorie", "onglet=imagerie", "J.ouvrirChemin(['im_r4','im_r4_radiographie','im_r4_radiographie__radiographie_thoracique','im_r4_radiographie__radiographie_thoracique__poumons_et_voies_aeriennes']);"),
    ("2_imagerie_cliches", "onglet=imagerie", "J.action(J.etat.byId['im_r4_radiographie__radiographie_thoracique__poumons_et_voies_aeriennes__pneumonie_communautaire'],'cliches');"),
    ("3_biologie_theorie", "onglet=biologie", "J.ouvrirChemin(['bi_bp','bi_bp_liquide_pleural']);"),
    ("4_biologie_calcul", "onglet=biologie", "J.ouvrirChemin(['bi_bp','bi_bp_liquide_d_ascite']);J.action(J.etat.byId['bi_bp_liquide_d_ascite__calc_gradient_albumine_ascite'],'outil');"),
    ("5_explorations_theorie", "onglet=explorations", "const r=J.etat.N.find(n=>n.texte==='Respiratoire');const s=J.etat.N.find(n=>n.texte.startsWith('Spirométrie avec'));J.ouvrirChemin([r.id,s.id]);"),
    ("6_explorations_trace", "onglet=explorations", "const s=J.etat.N.find(n=>n.texte.startsWith('Spirométrie avec'));J.action(s,'trace');"),
    ("7_organe_poumons", "organe=poumons_et_voies_aeriennes", "const m=J.etat.N.find(n=>n.texte==='Imagerie');J.ouvrirChemin([m.id]);"),
    ("8_examen_spirometrie", "onglet=imagerie", "await window.__choisir((await window.__chercher('spirometrie'))[0]);"),
    ("9_pratique_imagerie", "onglet=imagerie&mode=pratique", "document.querySelector('#pratique [data-j=arene]').click();"),
    ("10_pratique_biologie", "onglet=biologie&mode=pratique", "document.querySelector('#pratique [data-j=arene]').click();document.querySelector('#pratique .opts button')?.click();"),
    ("11_pratique_explorations", "onglet=explorations&mode=pratique", "document.querySelector('#pratique [data-j=lecture]').click();document.querySelector('#pratique [data-voir]')?.click();"),
    ("12_bulle_examen", "onglet=imagerie", "J.ouvrirChemin(['im_r4','im_r4_radiographie']);J.montrer(J.etat.byId['im_r4_radiographie__radiographie_thoracique']);"),
]
with sync_playwright() as p:
    b = p.chromium.launch(args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    for larg, haut in ((1280, 800), (380, 820)):
        for nom, h, js in SCENES:
            if larg == 380 and nom in ("12_bulle_examen",):
                continue
            pg = b.new_page(viewport={"width": larg, "height": haut})
            pg.on("pageerror", lambda e, n=nom: err.append(f"{larg} {n} JS {e}"))
            pg.on("console", lambda m, n=nom: m.type == "error" and err.append(f"{larg} {n} console {m.text}"))
            pg.on("response", lambda r, n=nom: r.status >= 400 and err.append(f"{larg} {n} HTTP {r.status} {r.url}"))
            pg.goto(base + "#" + h)
            pg.wait_for_function("window.__pret===true", timeout=90000)
            pg.evaluate("async()=>{const J=window.__jeu;" + js + "}")
            pg.wait_for_timeout(2500)
            if nom.startswith("1_"):
                bilan[f"corps3d_{larg}"] = pg.evaluate("window.__corps||0")
            f = os.path.join(sortie, f"{nom}_{larg}.png"); pg.screenshot(path=f)
            pg.close()
    b.close()
srv.shutdown()
bilan["erreurs"] = len(err)
print(json.dumps(bilan, ensure_ascii=False)); [print(e) for e in err[:40]]
