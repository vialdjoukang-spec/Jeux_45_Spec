#!/usr/bin/env python3
"""Preuve du site Biologie : captures Playwright à 1280 et 380 px (accueil, une pathologie, un examen ouvert) et zéro erreur console.

Usage : python3 conception/outils/paraclinique/capture_site_biologie.py [dossier_sortie]
Sortie par défaut : projets/2_Jeux_Paraclinique/captures/biologie-site/. Le script sert conception/prototypes/ en local (le site importe
../paraclinique/biologie.js) et échoue (code 1) à la moindre erreur console, réseau ou de page, ou à tout défilement horizontal.
Signature : AAI (Anthropic AI)
"""
import functools
import http.server
import os
import sys
import threading

from playwright.sync_api import sync_playwright

RACINE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SERVI = os.path.join(RACINE, "conception", "prototypes")
SORTIE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(RACINE, "projets", "2_Jeux_Paraclinique", "captures", "biologie-site")
CHROME = os.environ.get("CHROME", "/opt/pw-browsers/chromium-1243/chrome-linux64/chrome")
PATHO = "hyperkaliemie-severe-sur-insuffisance-renale-aigue"
EXAMEN = "EX-1-S6-ionogramme-potassium"
VUES = [("accueil", ""), ("pathologie", f"#patho={PATHO}"), ("pathologie_tetrade", "#patho=acidocetose-diabetique"), ("pathologie_fiche_ouverte", f"#patho={PATHO}&fiche={EXAMEN}"),
        ("examen", f"#examen={EXAMEN}")]


def serveur():
    class Muet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    h = functools.partial(Muet, directory=SERVI)
    s = http.server.ThreadingHTTPServer(("127.0.0.1", 0), h)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s


def main():
    os.makedirs(SORTIE, exist_ok=True)
    s = serveur()
    base = f"http://127.0.0.1:{s.server_address[1]}/biologie-site/index.html"
    erreurs, produits = [], []
    with sync_playwright() as p:
        nav = p.chromium.launch(executable_path=CHROME if os.path.exists(CHROME) else None)
        for larg in (1280, 380):
            ctx = nav.new_context(viewport={"width": larg, "height": 900}, device_scale_factor=1, reduced_motion="reduce")
            pg = ctx.new_page()
            pg.on("console", lambda m, l=larg: m.type == "error" and erreurs.append(f"{l}px console : {m.text}"))
            pg.on("pageerror", lambda e, l=larg: erreurs.append(f"{l}px page : {e}"))
            pg.on("requestfailed", lambda r, l=larg: erreurs.append(f"{l}px réseau : {r.url}"))
            pg.on("response", lambda r, l=larg: r.status >= 400 and erreurs.append(f"{l}px HTTP {r.status} : {r.url}"))
            for nom, h in VUES:
                pg.goto("about:blank")
                pg.goto(base + h)
                pg.wait_for_selector("body[data-pret='1']")
                if "fiche=" in h:
                    pg.wait_for_selector("#fenetre:not([hidden])")
                pg.wait_for_timeout(300)
                deb = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
                if deb > 0:
                    erreurs.append(f"{larg}px {nom} : défilement horizontal de {deb} px")
                f = os.path.join(SORTIE, f"{nom}_{larg}.png")
                pg.screenshot(path=f, full_page="fiche=" not in h)
                produits.append(f)
            # Infobulle d'un sigle (encre blanche sur fond sombre).
            pg.goto("about:blank")
            pg.goto(base + f"#patho={PATHO}")
            pg.wait_for_selector("body[data-pret='1']")
            pg.hover("abbr.terme >> nth=0")
            pg.wait_for_selector("#bulle:not([hidden])")
            coul = pg.evaluate("[getComputedStyle(bulle).color, getComputedStyle(bulle).backgroundColor]")
            if coul[0] != "rgb(255, 255, 255)":
                erreurs.append(f"{larg}px infobulle : encre {coul[0]} au lieu du blanc pur")
            f = os.path.join(SORTIE, f"infobulle_{larg}.png")
            pg.screenshot(path=f)
            produits.append(f)
            # Recherche tolérante : une faute de frappe sans accent retrouve l'hyperkaliémie au clavier.
            pg.goto("about:blank")
            pg.goto(base)
            pg.wait_for_selector("body[data-pret='1']")
            pg.fill("#q", "hyperkaliemi")
            pg.wait_for_selector("#sugg li[data-i]")
            f = os.path.join(SORTIE, f"recherche_{larg}.png")
            pg.screenshot(path=f)
            produits.append(f)
            pg.keyboard.press("Enter")
            pg.wait_for_function("location.hash.startsWith('#patho=hyperkali')")
            ctx.close()
        nav.close()
    s.shutdown()
    print("\n".join(os.path.relpath(f, RACINE) for f in produits))
    if erreurs:
        print("ERREURS :\n" + "\n".join(erreurs))
        sys.exit(1)
    print(f"{len(produits)} captures, 0 erreur console, aucun défilement horizontal.")


if __name__ == "__main__":
    main()
