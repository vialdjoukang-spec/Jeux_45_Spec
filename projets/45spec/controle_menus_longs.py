"""Contrôle 0 token : compte les menus longs hors format (le jeu annonce « menu long : une à trois réponses »)
et revalide chaque fichier de la spécialité avec valider() de scripts/produire_notions_questions.py.
Usage : python projets/45spec/controle_menus_longs.py INF   → affiche 0 menu fautif, sinon code de sortie 1.
Signature : AAI (Anthropic AI)"""
import glob, json, os, sys

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, "scripts"))
import produire_notions_questions as P  # noqa: E402

sp = sys.argv[1] if len(sys.argv) > 1 else "INF"
fautifs, erreurs, n = [], [], 0
for fq in sorted(glob.glob(os.path.join(R, "content", "questions", sp, "*.json"))):
    base = os.path.basename(fq)[:-5]; n += 1
    dq = json.load(open(fq, encoding="utf-8"))
    for q in dq["questions"]:
        k = sum(o["correct"] for o in q["options"])
        if q["format"] == "MenuLong" and not 1 <= k <= 3:
            fautifs.append(f"{base} {q['id']} : {k} justes")
    c = {"codes": [sp], "id": base, "entite": {"nom": dq["entite"]}}
    for etape, dossier, sch in (("notions", "notions", P.SCH_NOTIONS), ("questions", "questions", P.SCH_QUESTIONS),
                                ("correction", "corrections", P.SCH_CORRECTION)):
        cles = sch["properties"]          # seules les clés du schéma : les métadonnées d'écriture restent hors validation
        p = os.path.join(R, "content", dossier, sp, base + ".json")
        if not os.path.exists(p):
            erreurs.append(f"{base} : {etape} absent"); continue
        d = json.load(open(p, encoding="utf-8"))
        corps = {k2: d[k2] for k2 in cles if k2 in d}
        if etape == "notions":            # « couverture » est ajoutée par ecrire() après validation
            prop = sch["properties"]["notions"]["items"]["properties"]
            corps["notions"] = [{k2: v for k2, v in x.items() if k2 in prop} for x in corps["notions"]]
        erreurs += [f"{base} {etape} : {e}" for e in P.valider(etape, corps, c)]
print(*fautifs, sep="\n") if fautifs else None
print(*erreurs, sep="\n") if erreurs else None
print(f"{sp} : {n} fichiers | menus longs fautifs : {len(fautifs)} | erreurs valider() : {len(erreurs)}")
sys.exit(1 if fautifs or erreurs else 0)
