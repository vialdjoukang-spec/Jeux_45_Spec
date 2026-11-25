"""Veille GitHub gratuite (0 token) : détecte les nouveaux lots déposés par les IA de production, les répare,
les audite, les fusionne, puis relance l'audit de fond et les contrôles. Lancée par .github/workflows/veille.yml.
Sources surveillées : CLAUDE_A_AUDITER/, « POUR CLAUDE A AUDITER/ », Production_XAi/Lots_traites/, sur main et sur
toutes les branches production-xai-* (sur ces branches, seulement après le contre-audit XAi : fichier CONTRE_AUDIT_OK). Un lot déjà traité (même empreinte) n'est jamais refusionné, ce qui évite qu'un
ancien lot écrase une valeur plus récente.
Usage : python projets/outils/veille.py [--essai] [--amorcer]
  --amorcer : enregistre les lots existants comme déjà traités, sans rien fusionner (premier lancement).
Cache d'échec (skill optimisation-par-cache-hache-autorun) : un échec n'est jamais mis en cache comme réussite, mais son
empreinte (lots nouveaux + données + outils) est notée dans projets/retours/veille_echec.json. Tant qu'elle ne change pas,
la veille ne refait ni la fusion ni le rapport : pas de nouveau commit, donc pas de nouvelle session d'audit Claude pour
le même échec. Un nouveau lot, une donnée ou un outil modifié, ou la suppression du fichier relancent tout.
Signature : AAI (Anthropic AI)"""
import hashlib, json, os, re, subprocess, sys, tempfile, datetime

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRE = os.path.join(RAC, "projets", "retours", "veille_traites.json")
RAPPORT = os.path.join(RAC, "CLAUDE_A_AUDITER", "RAPPORT_VEILLE.md")
ATTENTE = os.path.join(RAC, "CLAUDE_A_AUDITER", "EN_ATTENTE_AUDIT_MEDICAL.json")
ECHEC = os.path.join(RAC, "projets", "retours", "veille_echec.json")
DOSSIERS = ("CLAUDE_A_AUDITER/", "POUR CLAUDE A AUDITER/", "Production_XAi/Lots_traites/")
essai, amorcer = "--essai" in sys.argv, "--amorcer" in sys.argv
git = lambda *a: subprocess.run(["git", "-C", RAC, *a], capture_output=True, text=True).stdout
py = lambda *a: subprocess.run([sys.executable, *a], cwd=RAC, capture_output=True, text=True)


def reparer(texte):
    """Réparations mécaniques sans effet sur le fond : BOM, balises markdown, texte autour, virgules finales."""
    t = texte.lstrip("﻿").strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t)
    if "{" in t and "}" in t:
        t = t[t.find("{"): t.rfind("}") + 1]
    t = re.sub(r",(\s*[}\]])", r"\1", t)
    obj = json.loads(t)
    if isinstance(obj.get("fichiers"), dict):   # chemins Windows → chemins du dépôt
        obj["fichiers"] = {k.replace("\\", "/").lstrip("./"): v for k, v in obj["fichiers"].items()}
    return obj


# 1. Inventaire des lots, sur main et sur les branches production-xai-*
refs = ["HEAD"] + [l.strip() for l in git("branch", "-r", "--list", "origin/production-xai-*").splitlines() if l.strip()]
registre = json.load(open(REGISTRE, encoding="utf-8")) if os.path.exists(REGISTRE) else {}
nouveaux, vus, sans_contre_audit = [], set(), []
for ref in refs:
    arbre = git("ls-tree", "-r", "--name-only", ref).splitlines()
    # Sur une branche production-xai-*, un lot n'est pris qu'après le contre-audit de l'orchestrateur XAi :
    # un fichier CONTRE_AUDIT_OK (toute extension) dans son dossier ou un dossier parent le déclare.
    valides = {os.path.dirname(c) for c in arbre if os.path.basename(c).split(".")[0] == "CONTRE_AUDIT_OK"}
    for chemin in arbre:
        if not chemin.startswith(DOSSIERS) or not chemin.endswith(".json") or "RAPPORT" in chemin or "EN_ATTENTE" in chemin:
            continue
        if ref != "HEAD" and not any(chemin.startswith(v + "/") for v in valides):
            sans_contre_audit.append(f"{ref.split('/')[-1]} › {chemin}"); continue
        brut = subprocess.run(["git", "-C", RAC, "show", f"{ref}:{chemin}"], capture_output=True).stdout
        h = hashlib.sha256(brut).hexdigest()
        if h in registre or h in vus:
            continue
        vus.add(h)
        nouveaux.append((ref, chemin, h, brut.decode("utf-8", "replace")))

if amorcer:
    for ref, chemin, h, _ in nouveaux:
        registre[h] = {"chemin": chemin, "ref": ref, "etat": "existant avant la veille"}
    json.dump(registre, open(REGISTRE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"amorçage : {len(nouveaux)} lots enregistrés comme déjà traités"); sys.exit(0)
if sans_contre_audit:
    print(f"veille : {len(sans_contre_audit)} lot(s) de branche en attente du contre-audit XAi (CONTRE_AUDIT_OK absent)")
if not nouveaux:
    print("veille : aucun nouveau lot"); sys.exit(0)

# 1 bis. Même échec que le dernier passage (mêmes lots, mêmes données, mêmes outils) : rien à refaire
arbres = [git("rev-parse", f"HEAD:{d}").strip() for d in ("conception/donnees", "SORTIES_DONNEES_FIABLES", "projets/outils", "conception/outils")]
empreinte = hashlib.sha256(json.dumps([sorted(h for _, _, h, _ in nouveaux), arbres]).encode()).hexdigest()
dernier = json.load(open(ECHEC, encoding="utf-8")) if os.path.exists(ECHEC) else {}
if not essai and dernier.get("empreinte") == empreinte:
    print(f"veille : {len(nouveaux)} lot(s) en échec déjà signalé le {dernier.get('heure')} (même empreinte) ; rien à refaire")
    sys.exit(0)

# 2. Réparation, puis fusion dans l'ordre des chemins (les sous-lots d'un même organe restent groupés)
lignes, fusionnes, refuses = [], 0, 0
attente = json.load(open(ATTENTE, encoding="utf-8")) if os.path.exists(ATTENTE) else []
with tempfile.TemporaryDirectory() as tmp:
    a_fusionner = []
    for ref, chemin, h, texte in sorted(nouveaux, key=lambda x: x[1]):
        try:
            obj = reparer(texte)
            if not isinstance(obj.get("fichiers"), dict):
                raise ValueError("pas de clé « fichiers »")
        except Exception as err:
            refuses += 1; lignes.append(f"- 🟥 `{chemin}` ({ref}) : illisible même après réparation ({err})")
            registre[h] = {"chemin": chemin, "ref": ref, "etat": "refusé",
                           "heure": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")}
            attente.append({"chemin": chemin, "ref": ref.replace("origin/", ""), "sha256": h, "etat": "refusé", "heure": registre[h]["heure"]})
            continue
        p = os.path.join(tmp, f"{len(a_fusionner):04d}.json")
        json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False)
        a_fusionner.append((p, ref, chemin, h))
    for p, ref, chemin, h in a_fusionner:
        r = py("projets/outils/fusionner_retours.py", p, *(["--essai"] if essai else []))
        ok = r.returncode == 0 and " 0 refusés" in r.stdout
        fusionnes += ok; refuses += not ok
        lignes.append(f"- {'🟩' if ok else '🟧'} `{chemin}` ({ref.replace('origin/', '')}) : {r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr.strip()[-200:]}")
        registre[h] = {"chemin": chemin, "ref": ref, "etat": "fusionné" if ok else "partiel", "date": str(datetime.date.today()),
                      "heure": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")}
        attente.append({"chemin": chemin, "ref": ref.replace("origin/", ""), "sha256": h, "etat": registre[h]["etat"], "heure": registre[h]["heure"]})

# 3. Audit de fond (corrections automatiques, tri des doutes, données fiables), lots de complément, contrôles
etapes = [("Audit de fond", "projets/outils/audit_fond.py"), ("Lots de complément", "projets/outils/lots_complement.py"),
          ("Audit de conception", "conception/outils/auditer_conception.py"), ("Audit de couverture", "conception/outils/auditer_couverture.py"),
          ("Non-perte face à main", "projets/outils/non_perte.py")]
resultats, echec = [], False
for nom, script in etapes:
    if essai and script.endswith(("audit_fond.py", "lots_complement.py")):
        continue
    r = py(script)
    der = (r.stdout.strip().splitlines() or [r.stderr.strip()[-200:]])[-1]
    echec |= r.returncode != 0 or "ÉCHEC" in r.stdout
    resultats.append(f"- {nom} : {der}")

os.makedirs(os.path.dirname(RAPPORT), exist_ok=True)
open(RAPPORT, "w", encoding="utf-8").write(
    f"# Veille automatique — {datetime.datetime.now():%Y-%m-%d %H:%M}\n\n{len(nouveaux)} nouveau(x) lot(s) : "
    f"{fusionnes} fusionné(s), {refuses} refusé(s) ou partiel(s).\n\n## Lots\n" + "\n".join(lignes) +
    "\n\n## Contrôles après fusion\n" + "\n".join(resultats) +
    ("\n\n⚠️ Un contrôle échoue : rien n'est publié ; Claude reprend à la main.\n" if echec else
     "\n\nLes lots réparés attendent sur la branche `veille/audit-medical`. Claude les audite médicalement, "
     "corrige, puis ouvre et fusionne la PR vers main. Rien n'arrive sur main sans cet audit.\n") +
    "\nSignature : AAI (Anthropic AI)\n")
if not essai:
    if echec:
        json.dump({"empreinte": empreinte, "lots": len(nouveaux), "heure": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")},
                  open(ECHEC, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    elif os.path.exists(ECHEC):
        os.remove(ECHEC)
    json.dump(attente, open(ATTENTE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(registre, open(REGISTRE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"veille : {len(nouveaux)} nouveaux, {fusionnes} fusionnés, {refuses} refusés ; {'ÉCHEC' if echec else 'OK'}")
sys.exit(1 if echec else 0)
