"""Rend les 4 chantiers : projets/<id>/chantier.json, chantier.html, chantier.pdf, audit_1.md, audit_2.md, README.md (0 token).
Usage : python projets/outils/rendre_chantiers.py"""
import json, os, sys, html, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chantiers import CHANTIERS, COMMUN

RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POL = os.path.join(os.path.dirname(RAC), "conception", "outils")
E = html.escape
f64 = lambda n: base64.b64encode(open(os.path.join(POL, n), "rb").read()).decode()
SIG = "DÉBUT : 2026-11-21 20:20 (EUROPE/ZURICH) · MODÈLE : CLAUDE OPUS 5.5 · PLATEFORME : CLAUDE.AI"

def liste(xs): return "<ul>" + "".join(f"<li>{E(x)}</li>" for x in xs) + "</ul>"
def table(rows, head): return "<table><tr>" + "".join(f"<th>{E(h)}</th>" for h in head) + "</tr>" + "".join("<tr>" + "".join(f"<td>{E(str(c))}</td>" for c in r) + "</tr>" for r in rows) + "</table>"

def rendre(c):
    S = [("vision", "Vision", f"<p>{E(c['vision'])}</p><p class=rang>Rang de coût : {c['rang']} sur 4 — {E(c['cout'])}</p>"),
         ("perimetre", "Périmètre", f"<h4>Inclus</h4>{liste(c['perimetre']['inclus'])}<h4>Exclus</h4>{liste(c['perimetre']['exclus'])}"),
         ("theorie", "Théorie et espace", f"<p>{E(c['theorie'])}</p><p><b>Visuel :</b> {E(c['visuel'])}</p>"),
         ("jeu", "Arène, aventure et puzzles", f"<p><b>Arène :</b> {E(c['arene'])}</p><p><b>Aventure :</b> {E(c['aventure'])}</p><h4>Puzzles</h4>{liste(c['puzzles'])}"),
         ("evaluation", "Évaluation, progression, maîtrise", table(COMMUN["evaluation"], ["Niveau", "Critère"])),
         ("donnees", "Données JSON → HTML", liste(c["donnees"]) + "<p>Un script valide chaque JSON contre son schéma, lance l'audit, puis injecte les données dans le HTML.</p>"),
         ("etapes", "Grandes étapes", table(c["etapes"], ["Étape", "Contenu"])),
         ("regles", "Règles communes bloquantes", liste(COMMUN["regles"])),
         ("audit1", "Audit 1 — fond et fonctionnement (corrigé)", table(c["audit1"], ["Constat", "Correction appliquée"])),
         ("audit2", "Audit 2 — psychologie du jeu et usage (corrigé)", table(c["audit2"], ["Constat", "Correction appliquée"])),
         ("demarrage", "Démarrage", "<ol>" + "".join(f"<li>{E(x)}</li>" for x in c["demarrage"]) + "</ol>")]
    nav = "".join(f"<a href='#{i}'><span>{n+1}</span>{E(t)}</a>" for n, (i, t, _) in enumerate(S))
    corps = "".join(f"<section id='{i}'><h2><span>{n+1}</span>{E(t)}</h2>{h}</section>" for n, (i, t, h) in enumerate(S))
    return f"""<!doctype html><html lang=fr><head><meta charset=utf-8><title>{E(c['titre'])}</title><style>
@font-face{{font-family:A;src:url(data:font/woff2;base64,{f64('atkinson-hyperlegible-latin-400-normal.woff2')})}}@font-face{{font-family:A;font-weight:700;src:url(data:font/woff2;base64,{f64('atkinson-hyperlegible-latin-700-normal.woff2')})}}
body{{margin:0;font:13px/1.5 A,sans-serif;color:#14181f;background:#faf8f4}}nav{{position:fixed;left:0;top:0;bottom:0;width:230px;padding:18px 12px;background:#fff;border-right:1px solid #e5e1da}}
nav a{{display:block;color:#14181f;text-decoration:none;padding:4px 6px;border-radius:6px;font-size:12px}}nav a span{{display:inline-block;width:20px;color:{c['couleur']};font-weight:700}}
main{{margin-left:250px;max-width:820px;padding:24px 28px}}h1{{font:700 23px Georgia,serif;margin:0 0 4px;color:{c['couleur']}}}h2{{font:700 16px Georgia,serif;border-bottom:2px solid {c['couleur']};padding-bottom:4px;margin-top:26px}}
h2 span{{display:inline-block;width:26px;color:{c['couleur']}}}h4{{margin:12px 0 4px}}table{{border-collapse:collapse;width:100%;margin:6px 0}}th{{background:{c['couleur']};color:#fff;text-align:left;font-size:12px}}
td,th{{border:1px solid #e5e1da;padding:5px 7px;vertical-align:top}}tr:nth-child(even) td{{background:#fff}}.rang{{background:#fff;border-left:5px solid {c['couleur']};padding:7px 10px}}
#sig{{position:fixed;right:12px;bottom:10px;background:#fff;border:2px solid #000;padding:4px 10px;font:700 11px/1.3 Arial;text-transform:uppercase}}
@media print{{nav{{display:none}}main{{margin:0;max-width:none}}#sig{{position:static;display:inline-block;margin-top:20px}}section{{break-inside:avoid-page}}}}
</style></head><body><nav><b style="color:{c['couleur']}">{E(c['id'])}</b><a href='../../conception/prototypes/veille/index.html' style='margin:6px 0 10px;font-weight:700;color:#1d4ed8'>Veille Examen fédéral</a>{nav}</nav><main><h1>{E(c['titre'])}</h1><p>Chantier · conception validée le 2026-11-21 · deux audits appliqués</p>{corps}<div id=sig>{SIG}</div></main></body></html>"""

def md_audit(c, k, titre):
    return f"# {titre} — {c['titre']}\n\n| Constat | Correction appliquée |\n|---|---|\n" + "\n".join(f"| {a} | {b} |" for a, b in c[k]) + "\n"

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    nav = p.chromium.launch()
    for c in sorted(CHANTIERS, key=lambda x: x["id"]):
        d = os.path.join(RAC, c["id"]); os.makedirs(d, exist_ok=True)
        json.dump(c, open(os.path.join(d, "chantier.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        h = rendre(c); open(os.path.join(d, "chantier.html"), "w", encoding="utf-8").write(h)
        open(os.path.join(d, "audit_1.md"), "w", encoding="utf-8").write(md_audit(c, "audit1", "Audit 1 — fond et fonctionnement"))
        open(os.path.join(d, "audit_2.md"), "w", encoding="utf-8").write(md_audit(c, "audit2", "Audit 2 — psychologie du jeu et usage"))
        pg = nav.new_page(); pg.set_content(h); pg.pdf(path=os.path.join(d, "chantier.pdf"), format="A4", print_background=True, margin={"top": "14mm", "bottom": "14mm", "left": "12mm", "right": "12mm"}); pg.close()
        print("rendu :", c["id"])
    nav.close()
