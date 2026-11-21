"""Transforme chaque plan JSON en HTML coloré, puis en PDF, après un auto-audit.
Usage : python conception/outils/rendre_plans.py [chemin_polices]
Sorties : conception/html/<id>.html, conception/pdf/<id>.pdf, conception/plans/<id>.plan.json (champ auditConception)."""
import base64, glob, html, json, os, sys

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POL = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ICI, "outils")
E = html.escape
from pathlib import Path
BASE = Path(ICI)


def b64(nom):
    p = os.path.join(POL, nom)
    return base64.b64encode(open(p, "rb").read()).decode() if os.path.exists(p) else ""


F4, F7 = b64("atkinson-hyperlegible-latin-400-normal.woff2"), b64("atkinson-hyperlegible-latin-700-normal.woff2")

# ---------- auto-audit ----------
OBLIG = ["objectif", "principes", "perimetre", "decisions", "architecture", "ecrans", "parcours", "donnees", "exercices",
         "production", "areneAventure", "evaluation", "audits", "blocages", "construction", "prototype"]


def auditer(p):
    r = []
    for k in OBLIG:
        r.append((f"Section « {k} » présente et non vide", bool(p.get(k))))
    r.append(("Chaque écran a une règle locale et un exemple", all(e.get("regleLocale") and e.get("exemple") for e in p["ecrans"])))
    r.append(("Chaque écran a des zones et des interactions", all(e.get("zones") and e.get("interactions") for e in p["ecrans"])))
    r.append(("Chaque fichier de données a ses champs, son producteur et son volume", all(d.get("champs") and d.get("producteur") and d.get("volume") for d in p["donnees"])))
    r.append(("Chaque exercice indique sa source de génération", all(x.get("generation") for x in p["exercices"])))
    r.append(("Le parcours est numéroté sans trou", [s["n"] for s in p["parcours"]] == list(range(1, len(p["parcours"]) + 1))))
    r.append(("La construction est numérotée sans trou", [s["n"] for s in p["construction"]] == list(range(1, len(p["construction"]) + 1))))
    r.append(("Chaque phase de construction a un critère de sortie", all(s.get("sortie") for s in p["construction"])))
    r.append(("Chaque décision donne sa raison", all(d.get("raison") for d in p["decisions"])))
    r.append(("Au moins un exercice est généré à 0 token", any("Script" in d["producteur"] for d in p["donnees"])))
    r.append(("REJECTOR_ figure dans les blocages ou la production", "REJECTOR_" in json.dumps(p, ensure_ascii=False)))
    r.append(("Le prototype a au moins 4 colonnes", len(p["prototype"].get("colonnes", [])) >= 4))
    r.append(("Le prototype est une image réelle (PNG 3D), pas un SVG", str(p["prototype"].get("image","")).endswith(".png") and (BASE / p["prototype"]["image"]).exists()))
    r.append(("La règle des infobulles symétriques est présente", len(p.get("semiologie", {}).get("infobulle", {}).get("rubriques", [])) == 4))
    r.append(("Aucune question ouverte sur VIT DIT CAFé", "VIT DIT" not in " ".join(p.get("questionsOuvertes", []))))
    brut = json.dumps({k: v for k, v in p.items() if k != "auditConception"})
    r.append(("Aucun marqueur de travail inachevé (TODO, XXX)", "TODO" not in brut and "XXX" not in brut))
    return r


# ---------- prototype : image 3D réelle (aucun SVG) ----------
def img_prototype(p):
    import base64
    b = base64.b64encode((BASE / p["prototype"]["image"]).read_bytes()).decode()
    return f'<img alt="Simulation du prototype" src="data:image/png;base64,{b}" style="width:100%;border-radius:10px;border:1px solid #e5e1da">'

# ---------- ancien prototype SVG (abandonné, conservé pour mémoire) ----------
def svg_prototype(p):
    pr, c = p["prototype"], p["couleur"]
    cols = pr["colonnes"]; W = 1180; H = 520; x0 = 250; dx = (W - x0 - 40) / len(cols)
    out = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" style="width:100%;background:#fbfaf8;border:1px solid #e5e1da;border-radius:10px">',
           f'<defs><linearGradient id="g{p["id"]}" x1="0" x2="1"><stop offset="0" stop-color="{c}" stop-opacity=".9"/><stop offset="1" stop-color="{c}" stop-opacity=".35"/></linearGradient></defs>']
    # figure centrale
    if pr.get("centre") == "tube":
        out.append(f'<g transform="translate(95,120)"><rect x="20" y="0" width="50" height="230" rx="25" fill="#fff" stroke="{c}" stroke-width="4"/><rect x="24" y="110" width="42" height="116" rx="20" fill="{c}" opacity=".45"/><rect x="12" y="-14" width="66" height="22" rx="6" fill="{c}"/></g>')
    else:
        out.append(f'<g transform="translate(70,40)" fill="#efe9e2" stroke="{c}" stroke-width="2.5"><circle cx="70" cy="40" r="32"/><path d="M30 85 Q70 70 110 85 L125 230 Q118 240 108 232 L100 150 L98 300 L112 440 Q100 452 86 442 L72 320 L58 442 Q44 452 32 440 L46 300 L44 150 L36 232 Q26 240 19 230 Z"/>'
                   f'<ellipse cx="78" cy="128" rx="14" ry="17" fill="{c}" opacity=".75"/></g>')
    out.append(f'<rect x="20" y="{H-58}" width="200" height="40" rx="8" fill="{c}"/><text x="120" y="{H-33}" text-anchor="middle" font-family="Arial" font-weight="700" font-size="14" fill="#fff">{E(pr["cadre"])}</text>')
    pos = []
    for i, col in enumerate(cols):
        x = x0 + i * dx; n = len(col); hh = min(56, (H - 60) / max(n, 1)); y0 = (H - n * hh) / 2
        pos.append([(x, y0 + j * hh + hh / 2) for j in range(n)])
    # liens
    for (fx, fy) in pos[0]:
        out.append(f'<path d="M190 {H-38} C 210 {fy}, {fx-60} {fy}, {fx} {fy}" fill="none" stroke="{c}" stroke-opacity=".35" stroke-width="1.6"/>')
    for i in range(len(pos) - 1):
        a, b = pos[i], pos[i + 1]
        for j, (ax, ay) in enumerate(a):
            k = round(j * (len(b) - 1) / max(len(a) - 1, 1)) if len(a) > 1 else 0
            for kk in {k, min(k + 1, len(b) - 1)}:
                bx, by = b[kk]; w = dx - 20
                out.append(f'<path d="M{ax+w} {ay} C {ax+w+30} {ay}, {bx-30} {by}, {bx} {by}" fill="none" stroke="url(#g{p["id"]})" stroke-width="2"/>')
    for i, col in enumerate(cols):
        for j, lab in enumerate(col):
            x, y = pos[i][j]; w = dx - 20
            maxc = int(w / 6.6); mots = lab.split(); l1 = ""; l2 = ""
            for m in mots:
                if len((l1 + " " + m).strip()) <= maxc and not l2: l1 = (l1 + " " + m).strip()
                else: l2 = (l2 + " " + m).strip()
            if len(l2) > maxc: l2 = l2[:maxc - 1] + "…"
            out.append(f'<rect x="{x}" y="{y-19}" width="{w}" height="38" rx="9" fill="#fff" stroke="{c}" stroke-width="1.8"/>')
            if l2:
                out.append(f'<text text-anchor="middle" font-family="Arial" font-size="11" fill="#222"><tspan x="{x+w/2}" y="{y-3}">{E(l1)}</tspan><tspan x="{x+w/2}" y="{y+11}">{E(l2)}</tspan></text>')
            else:
                out.append(f'<text x="{x+w/2}" y="{y+4}" text-anchor="middle" font-family="Arial" font-size="11.5" fill="#222">{E(l1)}</text>')
    out.append("</svg>")
    return "".join(out)


# ---------- HTML ----------
def table(rows, cols):
    h = "<div class='t'><table><tr>" + "".join(f"<th>{E(c[1])}</th>" for c in cols) + "</tr>"
    for r in rows:
        h += "<tr>" + "".join(f"<td>{fmt(r.get(c[0], ''))}</td>" for c in cols) + "</tr>"
    return h + "</table></div>"


def fmt(v):
    if isinstance(v, list):
        return "<ul>" + "".join(f"<li>{fmt(x)}</li>" for x in v) + "</ul>"
    if isinstance(v, dict):
        return "<br>".join(f"<b>{E(str(k))}</b> : {fmt(x)}" for k, x in v.items())
    return E(str(v))


def liste(v):
    return "<ul>" + "".join(f"<li>{E(x)}</li>" for x in v) + "</ul>"


def rendre(p, audit):
    S = []  # (id, titre, contenu)
    S.append(("objectif", "Objectif", liste(p["objectif"])))
    S.append(("principes", "Principes de conception", liste(p["principes"])))
    S.append(("perimetre", "Périmètre", f"<h4>Inclus</h4>{liste(p['perimetre']['inclus'])}<h4>Exclus</h4>{liste(p['perimetre']['exclus'])}"))
    S.append(("decisions", "Décisions de conception", table(p["decisions"], [("question", "Question"), ("choix", "Choix retenu"), ("raison", "Raison")])))
    S.append(("architecture", "Architecture en couches", table(p["architecture"], [("couche", "Couche"), ("contenu", "Contenu"), ("producteur", "Producteur"), ("cout", "Coût")])))
    S.append(("toile", "Toile zoomable (réseau de style Obsidian)", f"<p>{E(p['toile']['moteur'])}.</p>{liste(p['toile']['regles'])}"))
    if p.get("semiologie"):
        sm = p["semiologie"]
        S.append(("semiologie", "Infobulles symétriques, seuils de signes et sons réels",
                  f"<p>{E(sm['infobulle']['regle'])}</p>" + table([{"r": a, "c": b} for a, b in sm["infobulle"]["rubriques"]], [("r", "Rubrique"), ("c", "Contenu attendu")])
                  + f"<p>{E(sm['infobulle']['symetrie'])}</p><h4>Seuils</h4>{liste(sm['seuils'])}<h4>Sons</h4><p>{E(sm['sons']['regle'])}</p>{liste(sm['sons']['catalogue'])}<p>{E(sm['sons']['source'])}</p>"))
    if p.get("neuro"):
        S.append(("neuro", "Système nerveux : syndromes majeurs à identifier", "<p>Le système nerveux concentre le travail le plus lourd : chaque syndrome ci-dessous reçoit son circuit complet (signes par temps d'examen, symptômes, infobulles, examens, diagnostics).</p>" + liste(p["neuro"])))
    if p.get("mnemonique"):
        m = p["mnemonique"]
        S.append(("mnemonique", f"Mnémonique {m['nom']}", f"<p class='ok'><b>{E(m['statut'])}</b></p>" + table([{"l": a, "f": b} for a, b in m["lettres"]], [("l", "Lettre"), ("f", "Famille d'altération du tissu ou de l'organe")]) + f"<p>{E(m['regle'])}</p>"))
    if p.get("onglets"):
        o = p["onglets"]
        S.append(("onglets", "Contenu des trois onglets",
                  f"<h4>Biologie : prélèvements</h4>{liste(o['biologie']['prelevements'])}<p><b>Chaîne :</b> {E(o['biologie']['chaine'])}.</p>"
                  f"<h4>Calculs à maîtriser</h4>{liste(o['biologie']['calculs'])}<h4>Critères diagnostiques</h4>{liste(o['biologie']['criteres'])}"
                  f"<h4>Imagerie : régions</h4>{liste(o['imagerie']['regions'])}<h4>Imagerie : examens</h4>{liste(o['imagerie']['examens'])}"
                  f"<p><b>Chaîne :</b> {E(o['imagerie']['chaine'])}.</p><p><b>Fenêtre à deux clichés :</b> {E(o['imagerie']['fenetre'])}</p>"
                  f"<h4>Explorations fonctionnelles</h4>{liste(o['explorations']['liste'])}<p><b>Chaîne :</b> {E(o['explorations']['chaine'])}.</p>"))
    if p.get("topographie"):
        t = p["topographie"]
        lignes = "".join(f"<tr><td><b>{E(r)}</b><br>{E(o)}</td>" + "".join(f"<td>{E(' · '.join(m.get(lab, [])))}</td>" for lab in t["modalites"].values()) + "</tr>" for r, org in t["regions"].items() for o, m in org.items())
        S.append(("topographie", "Catalogue topographique des examens (rien ne manque)", f"<p><b>Progression :</b> {E(t['progression'])}.</p><p><b>Couverture :</b> " + " · ".join(f"{k} : {v}" for k, v in t["compte"].items()) + "</p>"
                  + "<table class='petit'><tr><th>Région · organe</th>" + "".join(f"<th>{E(l)}</th>" for l in t["modalites"].values()) + "</tr>" + lignes + "</table>"))
    S.append(("ecrans", "Écrans, zones, interactions et règles locales", "".join(
        f"<div class='carte'><div class='ct'><span class='id'>{E(e['id'])}</span> {E(e['nom'])} <span class='but'>— {E(e['but'])}</span></div>"
        f"<div class='g2'><div><h5>Zones</h5>{liste(e['zones'])}</div><div><h5>Interactions</h5>{liste(e['interactions'])}</div></div>"
        f"<div class='regle'><b>Règle locale :</b> {E(e['regleLocale'])}<br><b>Exemple :</b> {E(e['exemple'])}</div></div>" for e in p["ecrans"])))
    S.append(("parcours", "Parcours utilisateur, étape par étape", table(p["parcours"], [("n", "#"), ("etape", "Étape"), ("resultat", "Résultat")])))
    S.append(("donnees", "Fichiers JSON (modèle de données)", table(p["donnees"], [("fichier", "Fichier"), ("role", "Rôle"), ("champs", "Champs"), ("producteur", "Producteur"), ("volume", "Volume")])))
    S.append(("exercices", "Exercices générés", table(p["exercices"], [("type", "Type"), ("exemple", "Exemple"), ("generation", "Généré depuis")])))
    S.append(("production", "Production du contenu", table(p["production"], [("n", "#"), ("etape", "Étape"), ("outil", "Outil"), ("cout", "Coût"), ("controle", "Contrôle")])))
    a = p["areneAventure"]
    S.append(("arene", "Arène, aventure et rétention", f"<h4>Arène</h4>{liste(a['arene'])}<h4>Aventure</h4>{liste(a['aventure'])}<p><b>Rétention :</b> {E(a['retention'])}</p><p><b>Garde-fous :</b> {E(a['gardeFous'])}</p>"))
    S.append(("evaluation", "Évaluation type examen", table(p["evaluation"], [("format", "Format"), ("regle", "Règle")])))
    S.append(("audits", "Audits obligatoires", table(p["audits"], [("audit", "Audit"), ("controle", "Contrôle"), ("seuil", "Seuil")])))
    S.append(("blocages", "Blocages", "<ul class='bloc'>" + "".join(f"<li>🛑 {E(b)}</li>" for b in p["blocages"]) + "</ul>"))
    S.append(("construction", "Construction, étape par étape", table(p["construction"], [("n", "#"), ("phase", "Phase"), ("livrable", "Livrable"), ("sortie", "Critère de sortie")])))
    if p.get("questionsOuvertes"):
        S.append(("questions", "Questions ouvertes pour Vial", liste(p["questionsOuvertes"])))
    S.append(("prototype", "Simulation du prototype", f"<p><b>{E(p['prototype']['titre'])}</b></p>{img_prototype(p)}<p class='leg'>{E(p['prototype']['legende'])}</p>"))
    ok = sum(1 for _, v in audit if v)
    S.append(("audit", "Auto-audit de conception", f"<p><b>{ok} / {len(audit)} contrôles réussis.</b></p>" +
              "<div class='t'><table><tr><th>Contrôle</th><th>Résultat</th></tr>" + "".join(f"<tr><td>{E(k)}</td><td class='{'ok' if v else 'ko'}'>{'✅' if v else '❌'}</td></tr>" for k, v in audit) + "</table></div>"))
    c = p["couleur"]; sig = p["signature"]
    nav = "".join(f"<a href='#{i}'><b>{n}</b>{E(t)}</a>" for n, (i, t, _) in enumerate(S, 1))
    corps = "".join(f"<h2 id='{i}'><span>{n}</span>{E(t)}</h2>{h}" for n, (i, t, h) in enumerate(S, 1))
    return f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><title>{E(p['titre'])} — plan de conception</title><style>
@font-face{{font-family:AH;src:url(data:font/woff2;base64,{F4})}}@font-face{{font-family:AH;font-weight:700;src:url(data:font/woff2;base64,{F7})}}
:root{{--c:{c}}}*{{box-sizing:border-box}}body{{margin:0;font:14.5px/1.55 AH,Arial,sans-serif;color:#222;background:#fff}}
aside{{position:fixed;top:0;left:0;width:240px;height:100vh;overflow:auto;padding:18px 12px;background:#faf8f5;border-right:1px solid #e7e2da}}
aside h3{{font:700 .75rem Arial;letter-spacing:.1em;text-transform:uppercase;color:var(--c);margin:0 0 10px}}aside a{{display:flex;gap:8px;padding:5px 6px;color:#333;text-decoration:none;font-size:.82rem;border-radius:6px}}aside a:hover{{background:#f0ebe4}}aside b{{color:var(--c);min-width:20px}}
main{{margin-left:240px;padding:0 0 70px}}.col{{max-width:900px;margin:auto;padding:0 32px}}
header{{background:linear-gradient(120deg,var(--c),#222);color:#fff;padding:38px 32px 30px}}header h1{{font:700 2rem Georgia,serif;margin:0}}header p{{margin:.5em 0 0;opacity:.92}}header .st{{display:inline-block;margin-top:12px;background:#fff2;padding:3px 10px;border-radius:12px;font-size:.8rem}}
table.petit td,table.petit th{{font-size:9.5px;vertical-align:top}}p.ok{{background:#e8f6ee;border-left:4px solid #2e9e5b;padding:8px 12px;border-radius:6px}}h2{{font:700 1.2rem Georgia,serif;color:var(--c);margin:2em 0 .6em;padding-top:.6em;border-top:2px solid var(--c);display:flex;gap:10px;align-items:center}}h2 span{{background:var(--c);color:#fff;border-radius:50%;width:28px;height:28px;display:inline-flex;align-items:center;justify-content:center;font-size:.85rem}}
h4{{color:var(--c);margin:1em 0 .3em}}h5{{margin:.2em 0;color:#555}}.t{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;font-size:.84rem;margin:.4em 0 1em}}th{{background:var(--c);color:#fff;text-align:left;padding:6px 8px}}td{{padding:6px 8px;border-bottom:1px solid #eee;vertical-align:top}}tr:nth-child(even) td{{background:#fbf9f6}}td ul,.carte ul{{margin:0;padding-left:18px}}
.carte{{border:1px solid #e3ddd4;border-left:5px solid var(--c);border-radius:8px;padding:10px 14px;margin:10px 0;break-inside:avoid}}.ct{{font-weight:700}}.id{{background:var(--c);color:#fff;border-radius:6px;padding:1px 7px;font-size:.8rem}}.but{{font-weight:400;color:#666}}.g2{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}.regle{{background:#f7f4ef;border-radius:6px;padding:7px 10px;margin-top:6px;font-size:.88rem}}
.alerte{{background:#fde8e6;color:#9b1c13;border-radius:6px;padding:8px 12px;font-weight:700}}.bloc li{{margin:.25em 0}}.ok{{color:#2f7d32;font-weight:700}}.ko{{color:#b3261e;font-weight:700}}.leg{{color:#555;font-size:.85rem}}
#signature-ia{{position:fixed;right:12px;bottom:10px;z-index:9999;background:#fff;border:2px solid #000;padding:4px 10px;font:700 11px/1.3 Arial,sans-serif;text-transform:uppercase;color:#000}}
@media print{{aside{{display:none}}main{{margin-left:0}}h2{{break-after:avoid}}tr,.carte{{break-inside:avoid}}#signature-ia{{position:fixed}}}}
</style></head><body><aside><h3>Sommaire</h3>{nav}</aside><main><header><div class="col"><h1>{E(p['titre'])}</h1><p>{E(p['sousTitre'])}</p><span class="st">{E(p['statut'])} · v{E(p['version'])} · {E(p['date'])}</span></div></header><div class="col">{corps}</div></main>
<div id="signature-ia">DÉBUT : {E(sig['start']).upper()} · MODÈLE : {E(sig['model']).upper()} · PLATEFORME : {E(sig['platform']).upper()}</div></body></html>"""


def main():
    os.makedirs(os.path.join(ICI, "html"), exist_ok=True); os.makedirs(os.path.join(ICI, "pdf"), exist_ok=True)
    plans = sorted(glob.glob(os.path.join(ICI, "plans", "*.plan.json")))
    for f in plans:
        p = json.load(open(f, encoding="utf-8")); au = auditer(p)
        p["auditConception"] = [{"controle": k, "resultat": v} for k, v in au]
        json.dump(p, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        open(os.path.join(ICI, "html", f"{p['id']}.html"), "w", encoding="utf-8").write(rendre(p, au))
        print(f"{p['id']} : {sum(v for _, v in au)}/{len(au)} contrôles réussis")
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            b = pw.chromium.launch(); pg = b.new_page()
            for f in plans:
                i = os.path.basename(f).split(".")[0]
                pg.goto("file://" + os.path.join(ICI, "html", f"{i}.html")); pg.wait_for_timeout(300)
                pg.pdf(path=os.path.join(ICI, "pdf", f"{i}.pdf"), format="A4", print_background=True, margin={"top": "12mm", "bottom": "14mm", "left": "10mm", "right": "10mm"})
            b.close()
        print("PDF générés.")
    except ImportError:
        print("Playwright absent : HTML seulement.")


if __name__ == "__main__":
    main()
