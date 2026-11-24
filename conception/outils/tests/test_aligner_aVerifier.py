"""Test du correctif : un aVerifier retiré de pathologies.txt disparaît du JSON régénéré (generer_json.ecrire).
Usage : python conception/outils/tests/test_aligner_aVerifier.py"""
import ast, os, sys
ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ICI, "generer_json.py"), encoding="utf-8").read()
ns = {}
for n in ast.parse(src).body:   # on n'exécute que les deux fonctions pures, pas le générateur entier
    if isinstance(n, ast.FunctionDef) and n.name in ("conserver", "aligner_aVerifier"):
        exec(compile(ast.Module([n], []), "generer_json.py", "exec"), ns)
ns["VIDE"] = (None, "", [], {})
conserver, aligner = ns["conserver"], ns["aligner_aVerifier"]

neuf = {"pathologies": {"Fréquente": [{"nom": "Bursite", "bulle": {"def": "D", "retenir": "R"}}]},
        "noeuds": [{"id": "x", "label": "Bursite", "bulle": {"def": "D"}}, {"id": "y", "label": "Bursite", "bulle": {"def": "AUTRE"}}]}
ancien = {"pathologies": {"Fréquente": [{"nom": "Bursite", "bulle": {"def": "D", "retenir": "R", "aVerifier": "doute résolu"}}]},
          "noeuds": [{"id": "x", "label": "Bursite", "bulle": {"def": "D", "aVerifier": "doute résolu"}},
                     {"id": "y", "label": "Bursite", "bulle": {"def": "AUTRE", "aVerifier": "doute d'un autre système"}}]}
av = {("Bursite", "D"): None}
out = aligner(conserver(neuf, ancien), av)
assert "aVerifier" not in out["pathologies"]["Fréquente"][0]["bulle"], "doute retiré de la source : doit disparaître (organe)"
assert "aVerifier" not in out["noeuds"][0]["bulle"], "doute retiré de la source : doit disparaître (graphe)"
assert out["noeuds"][1]["bulle"]["aVerifier"] == "doute d'un autre système", "bulle d'une autre source (définition différente) : intacte"
out = aligner(conserver(neuf, ancien), {("Bursite", "D"): "nouveau doute"})
assert out["pathologies"]["Fréquente"][0]["bulle"]["aVerifier"] == "nouveau doute", "la source fait foi quand elle porte un doute"
print("OK : aligner_aVerifier (4 assertions)")
