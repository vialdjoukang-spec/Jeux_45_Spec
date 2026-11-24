"""Régénère projets/45spec/PROGRESSION_<NOM>.md pour un groupe de rendement et une liste de spécialités (codes[0]) (0 token). AAI (Anthropic AI)
Usage : python projets/45spec/progression_groupe.py A2 A ORL,OPH,GYN,OBS,URO,MIG,HEM,TOX,DER,RHU"""
import sys, os, json, glob
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
nom, grp, specs = sys.argv[1], sys.argv[2], set(sys.argv[3].split(","))
RG = json.load(open(os.path.join(R, "content", "pathologies", "RANG_RENDEMENT.json"), encoding="utf-8"))["pathologies"]
L = sorted((v["rang"], k, v) for k, v in RG.items() if v["groupe"] == grp and v["codes"][0] in specs)
ok = lambda k, v: all(os.path.exists(os.path.join(R, "content", e, v["codes"][0], k + ".json")) for e in ("notions", "questions", "corrections"))
fait = [(r, k, v) for r, k, v in L if ok(k, v)]
lig = [f"# Progression 45 Spec — {nom} (groupe {grp} ; {', '.join(sorted(specs))})", "",
       f"Production par l'agent Claude sans appel API, branche `agent/45spec-{nom}`, ordre du rang de `content/pathologies/RANG_RENDEMENT.json`.", "",
       f"**{len(fait)} / {len(L)} pathologies produites sur cette branche** (les pathologies déjà produites ailleurs sont sautées).", "",
       "Statut d'audit : en attente (`audit.rejector = null`). Chiffres incertains : « à vérifier » dans `source`.", "",
       "| # | Rang | Id | Spécialité | Pathologie | Statut |", "|---|---|---|---|---|---|"]
lig += [f"| {i} | {r} | `{k}` | {v['codes'][0]} | {v['nom']} | {'produite' if ok(k, v) else '—'} |" for i, (r, k, v) in enumerate(L, 1)]
open(os.path.join(R, "projets", "45spec", f"PROGRESSION_{nom}.md"), "w", encoding="utf-8").write("\n".join(lig + ["", "Signature : AAI (Anthropic AI)", ""]))
print(len(fait), "/", len(L))
