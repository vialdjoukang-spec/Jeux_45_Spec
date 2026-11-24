"""Régénère projets/45spec/PROGRESSION_<SPEC>.md (0 token) : pathologies canoniques, état notions/questions/correction.
Usage : python scripts/progression_manuel.py NEU   — Signature : AAI (Anthropic AI)"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import produire_notions_questions as P  # noqa: E402
sp = (sys.argv[1] if len(sys.argv) > 1 else "NEU").upper()
cs = P.canoniques(sp); faits = []; lignes = []
for c in cs:
    et = [e for e in ("notions", "questions", "correction") if os.path.exists(P.chemin(e, c))]
    if len(et) == 3:
        q = json.load(open(P.chemin("questions", c), encoding="utf-8")); n = json.load(open(P.chemin("notions", c), encoding="utf-8"))
        err = sum(len(json.load(open(P.chemin(e, c), encoding="utf-8"))["controles"]["erreurs"]) for e in ("notions", "questions", "correction"))
        faits.append(f"| {c['id']} | {c['entite']['nom']} | {len(n['notions'])} | {len(q['questions'])} | {err} |")
dbl = os.path.join(P.R, "projets", "45spec", f"DOUBLONS_{sp}.md")
ordre = os.path.join(P.R, "projets", "45spec", f"ORDRE_{sp}.txt")
prio = [l.strip() for l in open(ordre, encoding="utf-8") if l.strip() and not l.startswith("#")] if os.path.exists(ordre) else []
md = [f"# Progression {sp} — production manuelle sans API (agent 45spec-{sp})", "",
      f"Pathologies canoniques : {len(cs)} ; terminées (notions + questions + correction) : {len(faits)}.", "",
      "Méthode : source compacte `projets/45spec/sources_" + sp + "/*.py` → `python scripts/ecrire_manuel.py SOURCE --spec " + sp + "` (valider() et ecrire() du script de production).", "",
      "## Terminées", "", "| id | entité | notions | questions | erreurs valider() |", "|---|---|---|---|---|", *faits, "",
      "## Ordre de priorité retenu (importance pour l'examen)", "", *[f"{i}. {p}" + (" — fait" if any(f'| {p}' in f for f in faits) else "") for i, p in enumerate(prio, 1)], "",
      *(open(dbl, encoding="utf-8").read().rstrip().splitlines() + [""] if os.path.exists(dbl) else []),
      "Signature : AAI (Anthropic AI)"]
open(os.path.join(P.R, "projets", "45spec", f"PROGRESSION_{sp}.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
print(len(faits), "/", len(cs))
