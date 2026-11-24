#!/usr/bin/env python3
"""Test sans écran (Playwright) : page Veille, suivi de préparation, branchement des deux arènes.
Vérifie 0 erreur JS, l'enregistrement des réponses, l'export JSON + CSV + PNG, le résumé pour Claude
et l'absence de tout contenu non joué. Usage : python3 conception/outils/tests/test_veille_suivi.py [--capture dossier]
Signature : AAI (Anthropic AI)"""
import functools, http.server, json, os, socketserver, sys, threading, time
from playwright.sync_api import sync_playwright

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
CAP = sys.argv[sys.argv.index("--capture") + 1] if "--capture" in sys.argv else None
class Muet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
H = functools.partial(Muet, directory=RACINE)
srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), H); PORT = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
BASE = f"http://127.0.0.1:{PORT}/conception/prototypes"
erreurs, echecs = [], []
def ok(cond, msg): print(("OK   " if cond else "ÉCHEC") + " " + msg); cond or echecs.append(msg)

with sync_playwright() as p:
    b = p.chromium.launch()
    ctx = b.new_context(accept_downloads=True, viewport={"width": 1280, "height": 900})
    ctx.grant_permissions(["clipboard-read", "clipboard-write"], origin=f"http://127.0.0.1:{PORT}")
    ctx.route("**/fonts.googleapis.com/**", lambda r: r.abort()); ctx.route("**/fonts.gstatic.com/**", lambda r: r.abort())
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: erreurs.append(f"{pg.url} : {e}"))

    # 1. arène commune : la réponse jouée s'enregistre
    pg.goto(f"{BASE}/moteur/arene.html#paquet=transversal_A&valider")
    pg.wait_for_function("document.title==='PRET'", timeout=20000); pg.wait_for_timeout(600)
    n1 = pg.evaluate("JSON.parse(localStorage.getItem('suivi_examen_v1')||'{\"r\":[]}').r.length")
    ok(n1 == 1, f"arène commune : 1 réponse enregistrée ({n1})")
    r = pg.evaluate("JSON.parse(localStorage.getItem('suivi_examen_v1')).r[0]")
    ok(r["jeu"] == "Transversal" and r["sp"].startswith("Transversal") and r["n"] not in ("", "—"), f"champs jeu/spécialité/notion : {r['jeu']} | {r['sp']} | {r['n'][:40]}")
    ok(pg.locator("#svBtn").count() == 1 and pg.locator("a[href='../veille/index.html']").count() == 1, "arène commune : bouton « Ma préparation » et lien vers la veille")

    # 2. arène 45 : une étape jouée, série abandonnée : le diagnostic ne doit apparaître nulle part
    pg.goto(f"{BASE}/arene45/index.html#END"); pg.wait_for_function("document.documentElement.dataset.pret==='1'", timeout=20000)
    pg.click("#go"); pg.wait_for_selector(".opt")
    fmt = pg.evaluate("document.querySelector('.opt button')?'Kprim':'autre'")
    if fmt == "Kprim":
        for o in pg.locator(".opt").all(): o.locator("button").first.click()
    else: pg.locator(".opt").first.click()
    pg.click("#val"); pg.wait_for_timeout(300)
    d = pg.evaluate("JSON.parse(localStorage.getItem('suivi_examen_v1'))")
    ok(len(d["r"]) == 2 and d["r"][1]["jeu"] == "45 Spec", f"arène 45 : réponse enregistrée ({len(d['r'])})")
    serie = d["r"][1].get("s"); deck = json.load(open(os.path.join(RACINE, "conception/prototypes/arene45/decks/END.json"), encoding="utf-8"))
    patho = next((s["revele"].get("pathologie") for s in deck["series"] if s["id"] == serie), None)
    pg.click("#abandon"); pg.evaluate("Suivi.ouvrir()"); pg.wait_for_selector("#svCorps canvas")
    txt = pg.inner_text("#svVoile")
    ok(patho and patho not in txt and patho not in pg.evaluate("Suivi.resume()"), f"zéro spoiler : « {patho} » absent du tableau et du résumé")

    # 3. historique synthétique sur 12 jours pour les courbes, la tendance et la projection
    pg.evaluate("""()=>{const d=JSON.parse(localStorage.getItem('suivi_examen_v1'));const sp=['CAR','END','PNE','Transversal · A'];
      for(let j=12;j>=1;j--)for(let k=0;k<8;k++){const ok=Math.random()<0.45+0.03*(12-j);d.r.push({d:new Date(Date.now()-j*864e5).toISOString(),jeu:'45 Spec',sp:sp[k%4],ssp:'F1.'+(k%3),n:'Notion test '+(k%6),f:['A','Kprim','MenuLong'][k%3],ok,pts:ok?1:0,max:1,t:60+k,q:'test/'+j+'/'+k});}
      localStorage.setItem('suivi_examen_v1',JSON.stringify(d));}""")

    # 4. page Veille
    pg.goto(f"{BASE}/veille/index.html"); pg.wait_for_function("document.documentElement.dataset.pret==='1'", timeout=20000)
    ok(pg.locator("#sommaire li").count() >= 10, f"sommaire numéroté : {pg.locator('#sommaire li').count()} entrées")
    ok(pg.locator(".cd").count() >= 2, f"compte à rebours : {pg.locator('.cd').count()} cartes")
    t = pg.inner_text("#page")
    ok("Non publié" in t and "31 mars 2027" in t and "déduction" in t.lower(), "session 2027 : non publié + délai déduit du 31 mars 2027")
    ok("4 août 2026" in t and "Lugano" in t and "1500" in t.replace("'", ""), "session 2026 et taxes affichées")
    ok(pg.evaluate("getComputedStyle(document.body).fontFamily").startswith('"Atkinson Hyperlegible"'), "police Atkinson Hyperlegible")
    ok(pg.locator("svg").count() == 0, "aucun SVG")
    ok(pg.locator("#suivi canvas").count() == 2, "tableau de bord : 2 courbes canvas")
    A = pg.evaluate("Suivi.analyser()")
    ok(len(A["plan"]) == 7 and len(A["faibles"]) >= 1 and A["projection"] is not None, f"analyse : plan 7 j, {len(A['faibles'])} points faibles, projection {round(A['projection']['taux_examen']*100)} %")
    pg.hover("#suivi canvas >> nth=1", position={"x": 300, "y": 21}); ok(pg.is_visible("#svBulle"), "infobulle au survol d'une barre")

    # 5. exports
    recus = []
    pg.on("download", lambda dl: recus.append(dl))
    pg.click("#suivi [data-a='exp']"); t0 = time.time()
    while len(recus) < 3 and time.time() - t0 < 10: pg.wait_for_timeout(200)
    noms = sorted(dl.suggested_filename.rsplit(".", 1)[1] for dl in recus)
    ok(noms == ["csv", "json", "png"], f"export : {noms}")
    for dl in recus:
        chemin = dl.path(); taille = os.path.getsize(chemin)
        if dl.suggested_filename.endswith(".json"): ok(len(json.load(open(chemin, encoding="utf-8"))["reponses"]) == 98, "JSON : 98 réponses")
        if dl.suggested_filename.endswith(".csv"): ok(open(chemin, encoding="utf-8-sig").read().count("\n") == 98, "CSV : en-tête + 98 lignes")
        if dl.suggested_filename.endswith(".png"): ok(taille > 5000, f"PNG des courbes : {taille} octets")
    pg.click("#suivi [data-a='cop']"); pg.wait_for_timeout(400)
    md = pg.input_value("#suivi textarea")
    ok(all(s in md for s in ("## Scores", "## 10 points faibles", "## Plan des 7 prochains jours", "## Questions à poser à Claude")), f"résumé Claude : {len(md)} caractères")
    ok(pg.evaluate("navigator.clipboard.readText()") == md, "résumé copié dans le presse-papiers")
    if CAP:
        os.makedirs(CAP, exist_ok=True); pg.evaluate("scrollTo({top:0,behavior:'instant'})"); pg.screenshot(path=os.path.join(CAP, "veille_haut.png"))
        pg.evaluate("document.getElementById('preparation').scrollIntoView({behavior:'instant'})"); pg.screenshot(path=os.path.join(CAP, "veille_suivi.png"))

    # 6. localStorage indisponible : aucune erreur
    pg2 = ctx.new_page(); pg2.on("pageerror", lambda e: erreurs.append(f"(sans stockage) {e}"))
    pg2.add_init_script("Object.defineProperty(window,'localStorage',{get(){throw new Error('bloqué')}})")
    pg2.goto(f"{BASE}/veille/index.html"); pg2.wait_for_function("document.documentElement.dataset.pret==='1'", timeout=20000)
    pg2.evaluate("Suivi.enregistrer({jeu:'x',juste:true})")
    b.close()
srv.shutdown()
ok(not erreurs, f"0 erreur JS ({len(erreurs)})"); [print("   ", e) for e in erreurs]
print(f"\n{'RÉUSSI' if not echecs else 'ÉCHEC : ' + str(len(echecs))}")
sys.exit(1 if echecs else 0)
