"""Capture PNG d'un réseau : python capturer.py reseau.html sortie.png ["tout" | "ouvrir=id1,id2"] [largeur hauteur]"""
import asyncio, os, sys
from playwright.async_api import async_playwright


async def m():
    html, png = sys.argv[1], sys.argv[2]
    h = sys.argv[3] if len(sys.argv) > 3 else ""
    w, ht = (int(sys.argv[4]), int(sys.argv[5])) if len(sys.argv) > 5 else (1600, 1000)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": w, "height": ht})
        err = []; pg.on("pageerror", lambda e: err.append(str(e)))
        await pg.goto("file://" + os.path.abspath(html) + ("#" + h if h else ""))
        await pg.wait_for_function("document.body.dataset.pret==='1'", timeout=20000)
        await pg.wait_for_timeout(400); await pg.screenshot(path=png); await b.close()
        print("erreurs JS :", err or "aucune")

asyncio.run(m())
