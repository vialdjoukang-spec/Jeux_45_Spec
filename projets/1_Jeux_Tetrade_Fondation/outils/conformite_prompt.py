"""Tableau de conformité phrase par phrase entre PROMPT_VIAL.md et chaque système de la Tétrade (0 token).
Mesures tirées des sources (conception/outils/<systeme>/), de systemes.py et du moteur (tetrade.json, reseau3d.html).
Usage : python3 conformite_prompt.py  → écrit projets/1_Jeux_Tetrade_Fondation/CONFORMITE_PROMPT.md
Signature : AAI (Anthropic AI)"""
import json, os, re, subprocess, sys, datetime
RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(RAC, "conception/outils"))
from systemes import SYSTEMES
from systemes_rediges import REDIGES, SOURCES

CFG = json.load(open(os.path.join(RAC, "conception/prototypes/moteur/tetrade.json"), encoding="utf-8"))
_src = open(os.path.join(RAC, "conception/outils/construire_config_tetrade.py"), encoding="utf-8").read()
LIENS = re.findall(r'^\s*"([^"]+)": \{"def"', _src.split("LIENS = ", 1)[1].split("\n}", 1)[0], re.M) + re.findall(r'^LIENS = \{"([^"]+)"', _src, re.M)
MOTEUR = open(os.path.join(RAC, "conception/prototypes/moteur/reseau3d.html"), encoding="utf-8").read()

def txt(o):
    return json.dumps(o, ensure_ascii=False).lower()

def mesure(nom, cfg):
    S = SOURCES[nom]; org = S["organes"]; attendu = [o[0] for o in SYSTEMES.get(nom, [])]
    present = [o for o in attendu if o in org or any(o.startswith(k) for k in LIENS)]
    ordre = [o for o in org if o in attendu] == [o for o in present if o in org]
    tet = sum(1 for o in org if org[o].get("anatomie") and org[o].get("physiologie") and S["semio"].get(o) and S["pathos"].get(o))
    ana = {k: sum(1 for o in org if re.search(rx, txt(org[o].get("anatomie", [])))) for k, rx in
           {"macro": r"situ|forme|trajet|segment|lobe|loge|rapport|taille|mesure|cavit|portion", "micro": r"micro|histolog|cellul|épithél|tunique|fibre|paroi|couche|glande|acin|tissu|neurone",
            "vasc": r"vascularis|artère|artéri|veine|veineu|capillaire|sang", "innerv": r"innerv|nerf|nerveu|sympath|vague|plexus"}.items()}
    anc = sum(1 for o in SYSTEMES.get(nom, []) if o[1])
    phys_f = sum(1 for o in org for v in org[o].get("physiologie", []) for m in v[1] if len(m) > 3 and m[3])
    phys_n = sum(len(v[1]) for o in org for v in org[o].get("physiologie", []))
    temps = [t for o in S["semio"] for t in S["semio"][o]]
    t_ok = sum(1 for t in temps if sum(1 for s in t[1] if s["presentation"] == "typique") >= 2 or any(s["presentation"] == "unique" for s in t[1]))
    signes = [s for t in temps for s in t[1]]
    epon = sum(1 for s in signes if re.search(r"\b(de|d'|du)\s?[A-ZÉ][a-zé]+|[A-Z][a-z]+-[A-Z]", s["signe"]))
    interro = [s for t in temps if t[0].lower().startswith(("interrogatoire", "anamn")) for s in t[1]]
    quest = sum(1 for s in interro if re.search(r"\?|tu demandes|demande|depuis quand|tu fais préciser|tu fais raconter|tu recherches", txt(s["bulle"])))
    pats = [p for o in S["pathos"] for p in S["pathos"][o]]
    gold = sum(1 for p in pats if "Gold standard" in json.dumps(p["bulle"].get("bilan", {}).get("diagnostique", {}), ensure_ascii=False))
    pal = {k: sum(1 for p in pats if p["palier"] == k) for k in ("TF", "F", "U", "R")}
    orgR = sum(1 for o in S["pathos"] if any(p["palier"] == "R" for p in S["pathos"][o]))
    trop = sum(1 for s in signes if len(s["signe"]) > 45) + sum(1 for p in pats if len(p["nom"]) > 45)
    pref = REDIGES[nom]["prefixe"]
    syn = sum(1 for n in cfg["noeuds"] if n.get("type") == "Syndrome" and (n.get("couleur") and any(
        m.get("id") in n.get("de", []) for m in cfg["noeuds"] if m.get("type") == "Symptôme")) and nom in ("Cardiovasculaire", "Respiratoire") and
              ((nom == "Cardiovasculaire") == (n["id"] == "sy")))
    av = int(subprocess.run(["grep", "-c", "à vérifier", os.path.join(RAC, "conception/outils", REDIGES[nom]["dossier"], "pathologies.txt")],
                            capture_output=True, text=True).stdout.strip() or 0)
    return dict(attendu=len(attendu), present=len(present), ordre=ordre, n=len(org), tet=tet, ana=ana, anc=anc, phys_f=phys_f, phys_n=phys_n,
                temps=len(temps), t_ok=t_ok, signes=len(signes), epon=epon, interro=len(interro), quest=quest, pats=len(pats), gold=gold,
                pal=pal, orgR=orgR, trop=trop, syn=syn, av=av)

def c(ok, s):
    return ("✅ " if ok else "⚠️ ") + s

def main():
    M = {nom: mesure(nom, CFG) for nom in REDIGES}
    noms = list(M)
    court = {n: REDIGES[n]["dossier"] for n in noms}
    L = ["# Conformité au prompt épinglé (PROMPT_VIAL.md) — système par système", "",
         "Généré par `projets/1_Jeux_Tetrade_Fondation/outils/conformite_prompt.py` le %s (0 token). ✅ conforme ; ⚠️ écart mesuré. Les chiffres comptent les sources `conception/outils/<système>/`." % datetime.date.today().isoformat(), "",
         "## 1. Exigences propres à chaque système", "", "| Phrase du prompt | " + " | ".join(court[n] for n in noms) + " |", "|---|" + "---|" * len(noms)]
    def ligne(phrase, f):
        L.append("| " + phrase + " | " + " | ".join(f(M[n]) for n in noms) + " |")
    ligne("« Cela concerne toute les systèmes possibles » ; « on déroule tous les organes du système, de haut en bas » (21.11)",
          lambda m: c(m["present"] == m["attendu"] and m["ordre"], "%d/%d organes%s" % (m["present"], m["attendu"], "" if m["ordre"] else ", ordre ≠")))
    ligne("« la TETRADE : Anatomie + Physiologie + Sémiologie + Physiopathologie » (chaque organe a ses 4 espaces)", lambda m: c(m["tet"] == m["n"], "%d/%d" % (m["tet"], m["n"])))
    ligne("« structure en image de taille réduite » (ancre 3D réelle de l'organe)", lambda m: c(m["anc"] == m["attendu"], "%d/%d" % (m["anc"], m["attendu"])))
    for k, lab in (("macro", "anatomie macro"), ("micro", "anatomie micro"), ("vasc", "vascularisation"), ("innerv", "innervation")):
        ligne("« %s » (organes dont l'anatomie en parle, mesure par mots-clés)" % lab, lambda m, k=k: c(m["ana"][k] == m["n"], "%d/%d" % (m["ana"][k], m["n"])))
    ligne("« le réseau physiologie : points de départ… schéma évidement » (mots-clés ouvrant une fenêtre de courbe)", lambda m: c(m["phys_f"] > 0, "%d/%d" % (m["phys_f"], m["phys_n"])))
    ligne("« au temps de l'examen clinique » (temps avec 2–3 signes typiques ou 1 unique)", lambda m: c(m["t_ok"] == m["temps"], "%d/%d" % (m["t_ok"], m["temps"])))
    ligne("« la technique exacte et le nom dédié du signe (éponyme ?) » (signes à éponyme)", lambda m: c(m["epon"] > 0, "%d/%d" % (m["epon"], m["signes"])))
    ligne("« par survol du symptôme on voit la question à poser et les caractéristiques » (symptômes d'interrogatoire dont l'infobulle formule la question)",
          lambda m: c(m["interro"] and m["quest"] == m["interro"], "%d/%d" % (m["quest"], m["interro"])))
    ligne("« La somme évolue vers le syndrome clinique » (circuits symptômes → syndrome → examen)", lambda m: c(m["syn"] > 0, "%d circuit(s)" % m["syn"]))
    ligne("« un signe paraclinique à préciser (type d'examen) » (pathologies avec Gold standard)", lambda m: c(m["gold"] == m["pats"], "%d/%d" % (m["gold"], m["pats"])))
    ligne("« le ou les diagnostics… par spécialité » (4 paliers TF/F/U/R ; organes avec un piège rare)",
          lambda m: c(all(m["pal"].values()) and m["orgR"] == m["n"], "%s ; R %d/%d" % ("/".join(str(m["pal"][k]) for k in ("TF", "F", "U", "R")), m["orgR"], m["n"])))
    ligne("« tout doit être tellement concis » (cases de plus de 45 caractères)", lambda m: c(m["trop"] == 0, "%d" % m["trop"]))
    ligne("Sources : mentions « à vérifier » restantes (règle commune « rien de mémoire »)", lambda m: c(m["av"] == 0, "%d" % m["av"]))
    G = [("« un être humain ultra 3D réaliste »", "three.js + GLTFLoader et maillages réels" in "" or ("GLTFLoader" in MOTEUR), "Moteur three.js, GLTFLoader, matériaux physiques (reseau3d.html) ; vagin sans source 3D libre, vulve exclue par règle."),
         ("« Le Manequin 3D… peut être retourné »", "pointerdown" in MOTEUR or "mousedown" in MOTEUR, "reseau3d.html n'écoute que la molette (zoom) : aucune rotation libre à la souris ou au doigt n'est codée."),
         ("« des traits… Obsidian connectant les composantes… à un cadre ayant le nom du système » ; traits droits en bus (21.11)", "lineTo" in MOTEUR, "Traits droits tracés en canvas (lineTo) depuis le nœud Système."),
         ("« chaque circuit issu d'un syndrome peut être rétracté ou révélé »", "replier" in MOTEUR, "Boutons « replier » dans reseau3d.html."),
         ("« chacun a son bouton qui permet de révéler son arborescence » (Anatomie, Physiologie, Sémiologie)", "#espaces" in MOTEUR, "Barre #espaces : un bouton par espace."),
         ("« la page active continue de s'étendre horizontalement »", "largeurColonne" in json.dumps(list(CFG)), "Colonnes horizontales (largeurColonne, ecartColonne dans tetrade.json)."),
         ("Théorie et Pratique, deux onglets ; recherche mode Organe et mode Examen (22.11)", False, "Aucun onglet Théorie/Pratique ni recherche Organe/Examen dans reseau3d.html : la pratique vit dans arene.html ; l'intégration reste à faire.")]
    L += ["", "## 2. Exigences du moteur (communes à tous les systèmes)", "", "| Phrase du prompt | État | Preuve |", "|---|---|---|"]
    L += ["| %s | %s | %s |" % (p, "✅" if ok else "⚠️", pr) for p, ok, pr in G]
    ec = [(n, k) for n in noms for k, v in (("organes", M[n]["present"] != M[n]["attendu"]), ("syndromes", M[n]["syn"] == 0), ("questions", M[n]["quest"] < M[n]["interro"]),
                                            ("gold", M[n]["gold"] < M[n]["pats"]), ("concision", M[n]["trop"] > 0), ("innervation", M[n]["ana"]["innerv"] < M[n]["n"])) if v]
    L += ["", "## 3. Écarts", "", "- Circuits symptômes → syndrome → examen → diagnostics : %s seulement ; les %d autres systèmes s'arrêtent aux signes et aux pathologies." % (
        ", ".join(court[n] for n in noms if M[n]["syn"]) or "aucun", sum(1 for n in noms if not M[n]["syn"])),
          "- Détail des écarts mesurés : " + " ; ".join("%s (%s)" % (court[n], ", ".join(k for m, k in ec if m == n)) for n in dict.fromkeys(n for n, _ in ec)) + ".",
          "- Les symptômes d'interrogatoire n'ont pas de champ « question à poser » : l'infobulle (def, pourquoi, confusion, retenir) décrit le symptôme sans formuler la question ni les caractéristiques à demander, comme le prompt l'exige.",
          "- Le mannequin 3D ne se retourne pas : reseau3d.html n'écoute que la molette ; le vagin n'a pas de source 3D libre et la vulve reste exclue par règle.",
          "- Théorie/Pratique et la recherche Organe/Examen vivent dans des pages séparées (arene.html) et non dans le réseau.", "",
          "## 4. Limites de la mesure", "",
          "- Anatomie macro, micro, vascularisation, innervation et questions : détection par mots-clés dans le texte ; un ⚠️ signale une absence probable à relire, pas une preuve.",
          "- Les organes renvoyés à un autre système (LIENS : pharynx, thymus, circulation pulmonaire, organes lymphoïdes, ORL partagés) comptent comme présents.",
          "- Les exigences du moteur sont vérifiées dans le code (reseau3d.html, tetrade.json), sans capture d'écran.", ""]
    open(os.path.join(RAC, "projets/1_Jeux_Tetrade_Fondation/CONFORMITE_PROMPT.md"), "w", encoding="utf-8").write("\n".join(L))
    print("\n".join(L[-4:]))

if __name__ == "__main__":
    main()
