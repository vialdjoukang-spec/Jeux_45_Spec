"""Lecteur générique d'un système rédigé (0 token). Un dossier par système (cardio/, respi/…) contient :
  contenu.txt     « V volet | def | second » ; « # ORG nom » ; « O def || pourquoi || confusion || retenir » ;
                  « A volet » / « P volet » ; « - mot | texte | repère ou à retenir | fenêtre facultative »
  semiologie.txt  « # SEMIO organe » ; « T temps » ; « - signe | t/a/u | def | pourquoi | confusion | retenir »
  pathologies.txt « # PATHO organe » ; « @ TF|F|U|R | nom » ; « def:/pourquoi:/confusion:/retenir: » ;
                  « b visée / groupe | nom | signe et seuil » ; « t nom | posologie » ; « s source »
  glossaire.txt   « SIGLE = définition »
  temps.txt       « Temps | def | pourquoi | confusion | retenir » (bulles des temps d'examen du système)
Signature : AAI (Anthropic AI)"""
import os, re

RAC = os.path.dirname(os.path.abspath(__file__))
PALIERS = {"TF": ("Très fréquentes", "Très fréquente", "#1f7a4d"), "F": ("Fréquentes", "Fréquente", "#2f6fd0"),
           "U": ("Urgences", "Urgence", "#e0452b"), "R": ("Pièges (rares)", "Piège (rare)", "#7a5cc4")}
PALIER_BULLE = {
    "TF": ("Ce palier réunit les maladies que tu rencontreras chaque semaine.", "Tu dois les reconnaître vite et connaître leur traitement par cœur."),
    "F": ("Ce palier réunit les maladies courantes, moins fréquentes que les premières.", "Tu dois savoir les évoquer et lancer le bon bilan."),
    "U": ("Ce palier réunit les maladies qui tuent ou mutilent en quelques heures.", "Tu dois agir avant d'avoir toutes les preuves."),
    "R": ("Ce palier réunit une maladie rare qui imite une maladie fréquente.", "Elle te piège si tu ne cherches pas le signe qui la distingue.")}
UNIQUE = "Ce temps d'examen n'apporte qu'un signe typique fiable pour cet organe ; les autres y restent atypiques."


def charger(dossier):
    ici = os.path.join(RAC, dossier)

    def lignes(nom):
        p = os.path.join(ici, nom)
        if not os.path.exists(p):
            return
        for l in open(p, encoding="utf-8"):
            l = l.rstrip("\n")
            if l.strip() and not (l.startswith("#") and not l.startswith(("# ORG ", "# PATHO ", "# SEMIO "))):
                yield l

    volets, organes, org, esp = {}, {}, None, None
    for l in lignes("contenu.txt"):
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
            raise ValueError(f"Ligne illisible ({dossier}/contenu.txt) : {l}")

    pathos, org, cur = {}, None, None
    for l in lignes("pathologies.txt"):
        if l.startswith("# PATHO "):
            org = pathos.setdefault(l[8:].strip(), [])
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
            raise ValueError(f"Ligne illisible ({dossier}/pathologies.txt) : {l}")

    semio, org = {}, None
    for l in lignes("semiologie.txt"):
        if l.startswith("# SEMIO "):
            org = semio.setdefault(l[8:].strip(), [])
        elif l.startswith("T "):
            org.append((l[2:].strip(), []))
        elif l.startswith("- "):
            p = [x.strip() for x in l[2:].split("|")]
            sg = {"signe": p[0], "presentation": "atypique" if p[1] == "a" else "typique",
                  "bulle": dict(zip(["def", "pourquoi", "confusion", "retenir"], p[2:6]))}
            if p[1] == "u":
                sg["uniqueAssume"] = UNIQUE
            org[-1][1].append(sg)
        else:
            raise ValueError(f"Ligne illisible ({dossier}/semiologie.txt) : {l}")

    gloss = {}
    for l in lignes("glossaire.txt"):
        if " = " in l:
            k, v = l.split(" = ", 1)
            gloss[k.strip()] = v.strip()
    temps = {}
    for l in lignes("temps.txt"):
        p = [x.strip() for x in l.split("|")]
        temps[p[0]] = tuple(p[1:5])

    for o in list(pathos) + list(semio):
        assert o in organes, f"{dossier} : organe inconnu dans pathologies ou sémiologie : {o}"
    for o, ts in semio.items():
        for t, _ in ts:
            assert t in temps, f"{dossier} : temps « {t} » sans bulle dans temps.txt"
    return {"organes": organes, "volets": volets, "pathos": pathos, "semio": semio, "glossaire": gloss, "temps": temps}
