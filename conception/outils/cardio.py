"""Système cardiovasculaire : lit cardio/contenu.txt (anatomie, physiologie) et cardio/pathologies.txt (4 paliers),
à 0 token. Fournit ORGANES (ordre haut → bas), VOLETS_BULLE, PATHOS, PALIERS et GLOSSAIRE_CV."""
import os, re

ICI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cardio")
PALIERS = {"TF": ("Très fréquentes", "Très fréquente", "#1f7a4d"), "F": ("Fréquentes", "Fréquente", "#2f6fd0"),
           "U": ("Urgences", "Urgence", "#e0452b"), "R": ("Pièges (rares)", "Piège (rare)", "#7a5cc4")}
PALIER_BULLE = {
    "TF": ("Ce palier réunit les maladies que tu rencontreras chaque semaine.", "Tu dois les reconnaître vite et connaître leur traitement par cœur."),
    "F": ("Ce palier réunit les maladies courantes, moins fréquentes que les premières.", "Tu dois savoir les évoquer et lancer le bon bilan."),
    "U": ("Ce palier réunit les maladies qui tuent ou mutilent en quelques heures.", "Tu dois agir avant d'avoir toutes les preuves."),
    "R": ("Ce palier réunit une maladie rare qui imite une maladie fréquente.", "Elle te piège si tu ne cherches pas le signe qui la distingue.")}


def _lignes(nom):
    for l in open(os.path.join(ICI, nom), encoding="utf-8"):
        l = l.rstrip("\n")
        if l.strip() and not (l.startswith("#") and not l.startswith(("# ORG ", "# PATHO ", "# SEMIO "))):
            yield l


def _contenu():
    volets, organes, org, esp = {}, {}, None, None
    for l in _lignes("contenu.txt"):
        if l.startswith("V "):
            n, d, s = [x.strip() for x in l[2:].split("|")]
            volets[n] = (d, s)
        elif l.startswith("# ORG "):
            org = organes.setdefault(l[6:].strip(), {"bulle": None, "anatomie": [], "physiologie": []})
        elif l.startswith("O "):
            org["bulle"] = dict(zip(["def", "pourquoi", "confusion", "retenir"], [x.strip() for x in l[2:].split("||")]))
        elif l[:2] in ("A ", "P "):
            esp = "anatomie" if l[0] == "A" else "physiologie"
            org[esp].append((l[2:].strip(), []))
        elif l.startswith("- "):
            p = [x.strip() for x in l[2:].split("|")]
            org[esp][-1][1].append((p[0], p[1], p[2], p[3] if len(p) > 3 and p[3] else None))
        else:
            raise ValueError("Ligne illisible (contenu.txt) : " + l)
    return volets, organes


def _pathos():
    out, org, cur = {}, None, None
    for l in _lignes("pathologies.txt"):
        if l.startswith("# PATHO "):
            org = out.setdefault(l[8:].strip(), [])
        elif l.startswith("@ "):
            pal, nom = [x.strip() for x in l[2:].split("|")]
            cur = {"palier": pal, "nom": nom, "bulle": {"bilan": {}, "traitement": []}}
            org.append(cur)
        elif re.match(r"^(def|pourquoi|confusion|retenir): ", l):
            k, v = l.split(": ", 1)
            cur["bulle"][k] = v.strip()
        elif l.startswith("b "):
            tete, nom, det = [x.strip() for x in l[2:].split("|")]
            vis, grp = [x.strip() for x in tete.split("/")]
            cur["bulle"]["bilan"].setdefault(vis, {}).setdefault(grp, []).append([nom, det])
        elif l.startswith("t "):
            nom, det = [x.strip() for x in l[2:].split("|")]
            cur["bulle"]["traitement"].append([nom, det])
        elif l.startswith("s "):
            cur["bulle"]["source"] = l[2:].strip()
        else:
            raise ValueError("Ligne illisible (pathologies.txt) : " + l)
    return out


VOLETS_BULLE, ORGANES = _contenu()
PATHOS = _pathos()
for _o in PATHOS:
    assert _o in ORGANES, "Pathologies d'un organe inconnu : " + _o

GLOSSAIRE_CV = {}  # complété plus bas (glossaire.txt)
_g = os.path.join(ICI, "glossaire.txt")
if os.path.exists(_g):
    for _l in open(_g, encoding="utf-8"):
        if " = " in _l and not _l.startswith("#"):
            _k, _v = _l.rstrip("\n").split(" = ", 1)
            GLOSSAIRE_CV[_k.strip()] = _v.strip()


# ---- sémiologie par organe (cardio/semiologie.txt) ----
TEMPS_BULLE = {
    "Interrogatoire": ("Tu fais raconter les symptômes, leur début, leur rythme et ce qui les soulage.", "Les mots du patient orientent l'examen avant tout geste.", "Un symptôme vague peut venir d'un autre organe : tu cherches le contexte.", "Un symptôme bien décrit vaut souvent plus qu'un signe isolé."),
    "Inspection": ("Tu regardes le patient avant de le toucher : couleur, gonflement, veines, mouvements.", "Beaucoup de signes vasculaires se voient à distance.", "Un éclairage pauvre cache la cyanose et les marbrures.", "Tu compares toujours les deux côtés."),
    "Palpation": ("Tu palpes les pouls, la peau, les masses et les zones douloureuses.", "La main perçoit la force, la symétrie et le retard des pouls.", "Tes propres pulsations dans le bout des doigts peuvent te tromper : tu palpes avec la pulpe de plusieurs doigts.", "Un pouls absent situe l'obstacle en amont."),
    "Percussion": ("Tu tapes sur la paroi pour juger de ce qu'elle recouvre.", "La matité révèle le liquide ou un organe plein.", "Une paroi épaisse amortit le son.", "Tu compares toujours les deux côtés."),
    "Auscultation": ("Tu écoutes le cœur et les vaisseaux à la membrane puis au pavillon.", "Les bruits naissent des valves et des flux turbulents.", "Un bruit respiratoire ou un frottement peuvent imiter un souffle.", "Tu situes chaque bruit dans le cycle cardiaque."),
    "Mesures au lit": ("Tu mesures ce que la main ne suffit pas à juger : PA aux deux bras, IPS, SpO₂.", "Un chiffre confirme ou chiffre un signe clinique.", "Une mesure unique et mal faite trompe.", "Tu répètes la mesure avant de conclure."),
}


def _semio():
    out, org = {}, None
    for l in _lignes("semiologie.txt"):
        if l.startswith("# SEMIO "):
            org = out.setdefault(l[8:].strip(), [])
        elif l.startswith("T "):
            org.append((l[2:].strip(), []))
        elif l.startswith("- "):
            p = [x.strip() for x in l[2:].split("|")]
            sg = {"signe": p[0], "presentation": "atypique" if p[1] == "a" else "typique",
                  "bulle": dict(zip(["def", "pourquoi", "confusion", "retenir"], p[2:6]))}
            if p[1] == "u":   # signe unique assumé : ce temps d'examen n'a qu'un signe typique fiable pour cet organe
                sg["uniqueAssume"] = "Ce temps d'examen n'apporte qu'un signe typique fiable pour cet organe ; les autres y restent atypiques."
            org[-1][1].append(sg)
        else:
            raise ValueError("Ligne illisible (semiologie.txt) : " + l)
    return out


SEMIO = _semio()
for _o in SEMIO:
    assert _o in ORGANES, "Sémiologie d'un organe inconnu : " + _o
