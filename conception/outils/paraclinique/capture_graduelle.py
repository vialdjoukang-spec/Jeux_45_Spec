"""Captures graduelles d'UN examen de Biologie, du prélèvement au traitement (demande de Vial, 27.11.2026).
Usage : python3 capture_graduelle.py <racine du site assemblé> <dossier de sortie> [id de fiche, défaut EX-1-S6-ionogramme-potassium] [largeur]
Étapes : 1 matrices sur le corps · 2 matrice ouverte · 3 examen ouvert · 4 survol de l'examen · 5–9 fiche à 3 temps (en-tête, temps 1,
temps 2 et calculs, temps 3, traitement) · 10 diagnostic ouvert sur ses traitements · 11 survol d'un traitement (posologie).
0 erreur de console exigée (code 1 sinon). Signature : AAI (Anthropic AI)"""
import functools, http.server, json, os, socketserver, sys, threading
from playwright.sync_api import sync_playwright

racine, sortie = sys.argv[1], sys.argv[2]
fid = sys.argv[3] if len(sys.argv) > 3 else "EX-1-S6-ionogramme-potassium"
larg = int(sys.argv[4]) if len(sys.argv) > 4 else 1280
os.makedirs(sortie, exist_ok=True)


class Muet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


srv = socketserver.ThreadingTCPServer(("127.0.0.1", 0), functools.partial(Muet, directory=racine)); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
R = json.load(open(os.path.join(racine, "jeux", "paraclinique", "donnees", "reseau_biologie.json"), encoding="utf-8"))
N = {n["id"]: n for n in R["noeuds"]}
ex = f"bx_{fid}"; mat = N[ex]["de"][0]
diag = next(n["id"] for n in R["noeuds"] if n["de"] == [ex] and n["nature"] == "Diagnostic")
trt = next(n["id"] for n in R["noeuds"] if n["de"] == [diag] and n["nature"] == "Traitement")
fiche = "J.action(J.etat.byId[%s],'fiche');" % json.dumps(ex)
defile = "await new Promise(r=>setTimeout(r,500));const h=[...document.querySelectorAll('#fen h3.bh')][%d];if(h){const f=document.querySelector('#fen');f.scrollTop=h.offsetTop-60;}"
ETAPES = [("01_matrices_sur_le_corps", ""),
          ("02_matrice_ouverte", f"J.ouvrirChemin({json.dumps([mat])});"),
          ("03_examen_ouvert", f"J.ouvrirChemin({json.dumps([mat, ex])});"),
          ("04_survol_examen", f"J.ouvrirChemin({json.dumps([mat, ex])});J.montrer(J.etat.byId[{json.dumps(ex)}]);"),
          ("05_fiche_entete", fiche),
          ("06_fiche_temps1_indications", fiche + defile % 1),
          ("07_fiche_temps2_et_calculs", fiche + defile % 2),
          ("08_fiche_temps3_interpretation", fiche + defile % 4),
          ("09_fiche_traitement", fiche + defile % 5),
          ("10_diagnostic_vers_traitements", f"J.ouvrirChemin({json.dumps([mat, ex, diag])});"),
          ("11_survol_traitement_posologie", f"J.ouvrirChemin({json.dumps([mat, ex, diag])});J.montrer(J.etat.byId[{json.dumps(trt)}]);")]
err = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=os.environ.get("CHROME") or None, args=["--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist"])
    for nom, js in ETAPES:
        pg = b.new_page(viewport={"width": larg, "height": 800 if larg > 600 else 820})
        pg.on("pageerror", lambda e, n=nom: err.append(f"{n} JS {e}"))
        pg.on("console", lambda m, n=nom: m.type == "error" and err.append(f"{n} console {m.text}"))
        pg.goto(f"http://127.0.0.1:{port}/jeux/paraclinique/index.html#onglet=biologie")
        pg.wait_for_function("window.__pret===true", timeout=90000)
        pg.evaluate("async()=>{const J=window.__jeu;" + js + "}")
        pg.wait_for_timeout(1500)
        pg.screenshot(path=os.path.join(sortie, f"{fid}_{nom}_{larg}.png"))
        pg.close()
    b.close()
srv.shutdown()
print(json.dumps({"fiche": fid, "etapes": len(ETAPES), "erreurs": len(err)}, ensure_ascii=False)); [print(e) for e in err]
sys.exit(1 if err else 0)
