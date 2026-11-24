"""Test sans écran de l'arène sur les paquets tetrade_* : chaque question s'affiche, se valide (bonne réponse), montre la correction,
et la page ne lève aucune erreur JS. Routage de fichiers, sans serveur. Usage : python conception/outils/tests/test_arene_tetrade.py
Signature : AAI (Anthropic AI)"""
import json, os, sys
from playwright.sync_api import sync_playwright

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
M = os.path.join(R, "conception/prototypes/moteur")
IDX = [x for x in json.load(open(f"{M}/arenes/index.json", encoding="utf-8")) if x["paquet"].startswith("tetrade")]
assert sum(x["n"] for x in IDX) >= 100, "moins de 100 questions Tétrade"
TYPES = {".html": "text/html", ".json": "application/json", ".js": "text/javascript", ".woff2": "font/woff2"}


def servir(route):
    chemin = os.path.join(M, route.request.url.split("://x.test/", 1)[1].split("#")[0].split("?")[0])
    if os.path.isfile(chemin):
        route.fulfill(body=open(chemin, "rb").read(), content_type=TYPES.get(os.path.splitext(chemin)[1], "application/octet-stream"))
    else:
        manquants.add(route.request.url); route.fulfill(status=404, body="")


erreurs, vues, manquants = [], 0, set()
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.on("pageerror", lambda e: erreurs.append(str(e)))
    pg.on("console", lambda m: m.type == "error" and "Failed to load resource" not in m.text and erreurs.append(m.text))
    pg.route("http://x.test/**", servir)
    for x in IDX:
        P = json.load(open(f"{M}/arenes/{x['paquet']}.json", encoding="utf-8"))
        pg.goto("about:blank"); pg.goto(f"http://x.test/arene.html#paquet={x['paquet']}"); pg.wait_for_function("document.title==='PRET'")
        for j, q in enumerate(P["questions"]):
            pg.eval_on_selector(f"#liste li[data-j='{j}']", "e=>e.click()")
            for o in q["options"]:
                sel = f".opt[data-k='{o['k']}']"
                if q["format"] == "Kprim":
                    pg.eval_on_selector(f"{sel} button[data-v='{1 if o['ok'] else 0}']", "e=>e.click()")
                elif o["ok"]:
                    pg.eval_on_selector(sel, "e=>e.click()")
            pg.eval_on_selector("#valider", "e=>e.click()")
            res = pg.inner_text("#res")
            if "Juste" not in res:
                erreurs.append(f"{q['id']} : la bonne réponse n'est pas reconnue ({res[:40]})")
            if not pg.inner_text("#src").startswith("Sources"):
                erreurs.append(f"{q['id']} : source absente")
            vues += 1
    b.close()
print(f"{vues} questions jouées sur {len(IDX)} paquets Tétrade ; {len(erreurs)} erreur(s)")
if manquants:
    print("ressources absentes (hors test) :", ", ".join(sorted(u.split("x.test/")[1] for u in manquants)))
for e in erreurs[:20]:
    print(" -", e)
sys.exit(1 if erreurs else 0)
