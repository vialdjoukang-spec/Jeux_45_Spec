"""Bible de l'examen fédéral (0 token) : résumé scripté du catalogue PROFILES 2 (248 SSP) et du catalogue étendu des points de départ.
Lit data/references/CATALOGUE_OFFICIEL_PROFILES_248.md, data/ssp/SSP_*.json (pathologies par SSP, circuit) et data/ssp_etendus/*.json s'ils existent.
Écrit conception/catalogue/bible_profiles.html (sommaire numéroté, Atkinson Hyperlegible, colonne contenue). Signature : AAI (Anthropic AI)"""
import collections, glob, html, json, os, re

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))); os.chdir(R)
E = html.escape
lignes = [l for l in open("data/references/CATALOGUE_OFFICIEL_PROFILES_248.md", encoding="utf-8") if l.startswith("| `")]
ssp = []
for l in lignes:
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    ssp.append({"code": c[0].strip("`"), "cat": c[1], "en": c[2], "fr": c[3], "etio": int(c[4]), "cible": int(re.sub(r"\D", "", c[5]))})
info = {}
for f in glob.glob("data/ssp/SSP_*.json"):
    d = json.load(open(f, encoding="utf-8")); info[d["ssp"]] = {"circuit": d["circuit"], "n": len(d["entites"]),
        "patho": [e["nom"] for e in sorted(d["entites"], key=lambda e: {"TF": 0, "F": 1, "MF": 3, "R": 4}.get(e.get("strate"), 2))]}
ext = collections.defaultdict(list)
for f in sorted(glob.glob("data/ssp_etendus/*.json")):
    if f.endswith("INDEX.json"):
        continue
    d = json.load(open(f, encoding="utf-8")); L = d if isinstance(d, list) else d.get("entrees") or d.get("ssp") or []
    for x in L:
        ext[x.get("categorie", "?")[:1].upper()].append(x)
CAT = [("G", "Plaintes et symptômes généraux"), ("S", "Signes et symptômes par système"), ("F", "Anomalies des examens (findings)"), ("O", "Autres situations")]
nav, corps = [], []
tot = sum(s["cible"] for s in ssp)
corps.append(f"""<section id="s0"><h2>1. Ce que l'examen attend</h2>
<p>PROFILES 2, validé le 1er novembre 2023 par la Commission interfacultaire médicale suisse, est le référentiel de l'examen fédéral. Il réunit trois dimensions liées : les rôles et compétences (CanMEDS), les activités professionnelles confiables (EPA), que le médecin doit exécuter dès son premier jour d'assistanat, et les situations de départ (SSP), dans lesquelles ces activités s'exercent. La révision de 2023 a ajouté trois axes : santé planétaire, diversité-équité-inclusion et numérique.</p>
<p>Le catalogue compte {len(ssp)} SSP : {sum(1 for s in ssp if s['cat']=='G')} G, {sum(1 for s in ssp if s['cat']=='S')} S, {sum(1 for s in ssp if s['cat']=='F')} F et {sum(1 for s in ssp if s['cat']=='O')} O. Le modèle de production y attache {sum(s['etio'] for s in ssp)} étiologies et vise {format(tot, ",").replace(",", " ")} questions (A, K', menu long).</p>
<p class="note">Le texte intégral de PROFILES 2 n'a pas pu être téléchargé automatiquement (le site de l'Université de Genève refuse les robots) : dépose le PDF pour que cette page en résume aussi les EPA et les rôles, mot pour mot.</p></section>""")
nav.append('<a href="#s0"><b>1</b>Ce que l\'examen attend</a>')
for i, (k, nom) in enumerate(CAT, 2):
    L = [s for s in ssp if s["cat"] == k]; X = ext.get(k, [])
    nav.append(f'<a href="#c{k}"><b>{i}</b>{k} · {E(nom)} <i>{len(L)}{" + " + str(len(X)) if X else ""}</i></a>')
    rows = "".join(f"<tr><td><code>{E(s['code'])}</code></td><td>{E(s['fr'])}<div class='en'>{E(s['en'])}</div></td><td class=n>{info.get(s['code'],{}).get('n',s['etio'])}</td><td class=n>{s['cible']}</td>"
                   f"<td><details><summary>{E((info.get(s['code'],{}).get('circuit') or '').replace('_',' ').lower())}</summary>{E(' · '.join(info.get(s['code'],{}).get('patho',[])[:40]))}</details></td></tr>" for s in L)
    xr = "".join(f"<tr><td><code>{E(x.get('code',''))}</code></td><td>{E(x.get('intitule',''))}<div class='en'>{E(x.get('systeme') or x.get('famille') or '')}</div></td><td colspan=3>{E(x.get('pourquoi',''))}</td></tr>" for x in X)
    corps.append(f"""<section id="c{k}"><h2>{i}. {k} · {E(nom)}</h2><p>{len(L)} SSP officiels{f" et {len(X)} points de départ ajoutés hors catalogue ISFM" if X else " ; le catalogue étendu de cette catégorie est en production"}.</p>
<table><thead><tr><th>Code</th><th>Situation de départ</th><th>Pathologies</th><th>Questions visées</th><th>Circuit et diagnostics</th></tr></thead><tbody>{rows}</tbody></table>
{f"<h3>Points de départ ajoutés</h3><table><tbody>{xr}</tbody></table>" if X else ""}</section>""")
page = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Bible PROFILES 2</title>
<link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Fraunces:opsz,wght@9..144,600&display=swap" rel="stylesheet">
<style>:root{{color-scheme:light dark;--bg:light-dark(#f7f6f2,#12151b);--c:light-dark(#fff,#1b1f28);--ink:light-dark(#18202e,#e9ebf1);--sous:light-dark(#5a6275,#9aa3b6);--t:light-dark(#e3e0d8,#2b3140);--r:#c8102e}}
*{{box-sizing:border-box;min-width:0}}body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 "Atkinson Hyperlegible",sans-serif}}h1,h2,h3{{font-family:Fraunces,Georgia,serif;font-weight:600}}
nav{{position:fixed;inset:0 auto 0 0;width:260px;padding:22px 12px;border-right:1px solid var(--t);overflow:auto}}nav a{{display:flex;gap:8px;padding:7px 8px;border-radius:8px;color:inherit;text-decoration:none;font-size:13.5px}}nav a:hover{{background:var(--c)}}nav b{{color:var(--sous);min-width:18px}}nav i{{margin-left:auto;font-style:normal;color:var(--sous);font-size:12px}}
main{{margin-left:260px;padding:28px clamp(16px,4vw,48px)}}.col{{max-width:900px;margin:auto}}h1{{font-size:30px;margin:0}}h2{{margin-top:36px;border-top:1px solid var(--t);padding-top:12px}}
table{{width:100%;border-collapse:collapse;background:var(--c);font-size:13.5px;border-radius:8px;overflow:hidden}}td,th{{padding:7px 9px;border-bottom:1px solid var(--t);vertical-align:top;text-align:left}}th{{color:var(--sous);font-size:12.5px}}.n{{text-align:right;font-variant-numeric:tabular-nums}}
.en{{color:var(--sous);font-size:12px}}code{{font-weight:700;color:var(--r)}}.note{{color:var(--sous);font-size:13px}}details summary{{cursor:pointer;color:var(--sous)}}
@media(max-width:800px){{nav{{position:static;width:auto;border:0}}main{{margin:0}}}}</style></head><body>
<nav><div class="note" style="padding:0 8px 8px">Bible de l'examen fédéral</div>{''.join(nav)}</nav><main><div class="col"><h1>Bible PROFILES 2 — situations de départ</h1>
<p class="note">Résumé automatique du catalogue officiel et du catalogue étendu, régénéré à chaque mise à jour. AAI (Anthropic AI)</p>{''.join(corps)}</div></main></body></html>"""
os.makedirs("conception/catalogue", exist_ok=True); open("conception/catalogue/bible_profiles.html", "w", encoding="utf-8").write(page)
print(f"bible : {len(ssp)} SSP officiels, {sum(len(v) for v in ext.values())} points de départ étendus")
