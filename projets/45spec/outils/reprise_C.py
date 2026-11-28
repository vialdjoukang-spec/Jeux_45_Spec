# Met à jour REPRISE_C.md après un lot (0 token) : reprise_C.py <n° lot> "<ligne du lot>" "<points à vérifier>" <dernier cNN> (AAI)
import sys, re, subprocess, os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
n, ligne, av, cnn = sys.argv[1:5]
p = R + "/projets/45spec/REPRISE_C.md"; s = open(p, encoding="utf-8").read()
s = re.sub(r"\(mise à jour après le lot \d+\)", f"(mise à jour après le lot {n})", s)
suiv = subprocess.run(["python3", R + "/projets/45spec/outils/suivant_C.py", "6"], capture_output=True, text=True).stdout.split("\n")
ids = [l.split()[1] for l in suiv[1:] if l.strip()]
fait = 800 - int(suiv[0].split()[1])
s = re.sub(r"- Compte du groupe C : \d+ / 800", f"  - lot {n} : {ligne}\n- Points restés « à vérifier » (lot {n}) : {av}\n- Compte du groupe C : {fait} / 800", s, count=1)
s = re.sub(r"- Pathologie suivante : .*\n", "- Pathologie suivante : " + ", ".join(ids[:3]) + " ; puis " + ", ".join(ids[3:]) + ".\n", s)
s = re.sub(r"c01…c\d+", "c01…" + cnn, s)
open(p, "w", encoding="utf-8").write(s); print("reprise à jour :", fait, ids[:3])
