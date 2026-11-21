"""Tâches des 4 projets (source unique) → projets/taches.json et projets/tableau_de_bord.html.
Répartition : Claude conçoit, audite et polit ; le gros œuvre (volumes de texte, recherche d'images) se fait ailleurs.
Usage : python projets/outils/taches.py"""
import json, os, re, sys, unicodedata, glob

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAC, "conception", "outils"))
from catalogue_paraclinique import TOPO, PRELEVEMENTS
from systemes import SYSTEMES

GH = "https://github.com/vialdjoukang-spec/Jeux_45_Spec/blob/main/"


def slug(t):
    t = t.replace("œ", "oe").replace("Œ", "Oe").replace("æ", "ae").replace("Æ", "Ae")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    t = re.sub(r"\(.*?\)", "", t)
    return re.sub(r"[^a-z0-9]+", "_", t).strip("_")[:40]


REGLES = [
    "Tu appliques intégralement les instructions du producteur (fichier 00_INSTRUCTIONS_PRODUCTEUR.md, chargé dans tes instructions ou joint à ce message) ; en cas de doute, elles priment.",
    "Tu écris en français, en phrases verbales complètes, claires et concises ; jamais de phrase nominale dans une explication.",
    "Tu respectes la pratique suisse ; pour les posologies et les valeurs, tu suis la cascade : AIPS, Compendium, sociétés suisses, sociétés européennes.",
    "Tu donnes les valeurs en unités SI suisses (gaz du sang en kPa, glycémie en mmol/l).",
    "Tu définis dans « glossaire » chaque sigle, score ou terme technique que tu emploies.",
    "Tu écris des affirmations sourcées ; si un chiffre n'existe pas dans les sources, tu ne cites que les chiffres connus et tu n'écris jamais « donnée non disponible ».",
    "Tu ne modifies ni la structure, ni les clés, ni l'ordre des fichiers ; tu remplis seulement les valeurs.",
    "Tu rends le même objet JSON valide {\"fichiers\": {chemin: contenu}}, avec les chemins exacts, inchangés. Si ta réponse risque d'être coupée, tu rends un seul chemin par réponse, dans le même format, et tu attends « suite ».",
]

CHAMPS_EXAMEN = [
    "visees : liste prise parmi diagnostique, retentissement, etiologique, complications, therapeutique, sortie.",
    "signeRecherche : ce que l'examen cherche, en quelques mots (ex. « condensation alvéolaire avec bronchogramme aérien »).",
    "seuil : la valeur ou le critère qui rend l'examen positif, avec son unité SI.",
    "indication : une phrase qui dit quand on le demande.",
    "discriminant : ce que cet examen montre mieux que les autres.",
    "avantageSelectif : pourquoi on le choisit dans cette situation.",
    "plutotQue : l'examen qu'il remplace et pourquoi.",
    "limite : ce qu'il ne voit pas ou ses faux négatifs.",
    "referencePour : liste des diagnostics dont il est l'examen de référence (gold standard), sinon liste vide.",
    "smarterMedicine : la recommandation suisse qui limite son usage, ou null s'il n'y en a pas.",
    "radioAnatomieNormale : pour l'imagerie seulement, liste des repères normaux à reconnaître ; null pour les autres modalités.",
    "precautions : grossesse, enfant, insuffisance rénale, produit de contraste, implant (IRM) ; une phrase par précaution utile.",
    "irradiation_mSv : dose efficace typique en mSv (nombre) ; 0 si l'examen n'irradie pas.",
    "delai : « urgence (< 1 h) », « rapide (< 24 h) » ou « programmé ».",
    "prelevementRef : pour la biologie, le nom du fichier de prélèvement (ex. sang_veineux) ; null sinon.",
    "bulle : {def, pourquoi, confusion, retenir}, une phrase verbale chacune, de longueur comparable.",
]


def prompt(role, fichiers, champs, regles_plus=()):
    l = [role, "", "Le fichier joint LOT_<identifiant>.json contient, dans « fichiers », chaque fichier à remplir sous son chemin exact :"] + [f"- {f}" for f in fichiers]
    if champs:
        l += ["", "Contenu attendu de chaque champ :"] + [f"- {c}" for c in champs]
    l += ["", "Règles :"] + [f"- {r}" for r in list(regles_plus) + REGLES]
    return "\n".join(l)


T = []


def tache(projet, id, titre, ou, quoi, entrees=(), sortie="", prompt_txt="", dep=(), claude=False):
    T.append({"projet": projet, "id": id, "titre": titre, "ou": ou, "quoi": quoi, "entrees": list(entrees), "sortie": sortie,
              "prompt": prompt_txt, "dependances": list(dep), "claude": claude})


# ---------------- 1. Tétrade ----------------
P = "1_Jeux_Tetrade_Fondation"
tache(P, "T01", "Valider la liste des organes, les volets et les fenêtres du système cardiovasculaire", "Claude (conception)",
      "Claude te propose la liste, tu valides ou tu corriges ; rien ne se produit avant ta validation.", ["conception/outils/systemes.py"], "systemes.py validé", claude=True)
for i, (s, orgs) in enumerate(SYSTEMES.items()):
    fich = [f"conception/donnees/tetrade/{slug(s)}/organes/{slug(o)}.json" for o, _, _ in orgs]
    tache(P, f"T{10 + i:02d}", f"Rédiger les organes du système {s} ({len(orgs)} organes)", "Gemini (Pro)",
          "Tu joins les fichiers d'organes du système, tu colles le prompt, tu importes ici les JSON rendus.", fich,
          f"conception/donnees/tetrade/{slug(s)}/organes/*.json remplis",
          prompt("Tu es anatomiste et physiologiste, enseignant en faculté de médecine suisse. Tu remplis chaque fichier d'organe : anatomie et physiologie, volet par volet.", fich,
                 ["anatomie : pour chaque volet, 3 à 6 entrées {motCle, texte, fenetre} ; motCle en 1 à 4 mots ; texte en une ou deux phrases ; fenetre = « 3d ».",
                  "physiologie : pour chaque volet, du paramètre le plus simple au plus complexe ; fenetre = nom de la courbe ou du calculateur utile (ex. starling, pression_volume, ecg, clairance), sinon null.",
                  "bulle : {def, pourquoi, confusion, retenir} pour l'organe."],
                 ["Tu ne mets dans motCle qu'un nom court : le détail va dans texte.", "Tu ne dessines aucune courbe : tu nommes seulement la fenêtre."]),
          dep=["T01"] if i else ["T01"])
tache(P, "T30", "Rédiger les 24 syndromes neurologiques majeurs", "Gemini (Pro)", "Chaque syndrome reçoit ses signes typiques et atypiques, son minimum suffisant et ses confusions.",
      ["conception/donnees/tetrade/neurologique/syndromes.json"], "syndromes.json rempli",
      prompt("Tu es neurologue enseignant. Tu remplis chaque syndrome du fichier.", ["conception/donnees/tetrade/neurologique/syndromes.json"],
             ["signesMinimaux : 2 ou 3 signes qui suffisent à poser le syndrome.", "signes : chaque signe avec presentation « typique » ou « atypique » et sa bulle {def, pourquoi, confusion, retenir}.",
              "confusionsSyndromiques : les syndromes voisins et le signe qui les distingue.", "diagnostics : les diagnostics les plus fréquents, puis les rares graves."]))
tache(P, "T31", "Compléter le catalogue des sons réels (HLS-CMDS)", "Claude Code",
      "Script de téléchargement et de découpe des enregistrements (souffles, frottement, sibilants, ronchi).", ["conception/donnees/tetrade/sons.json"], "sons.json + fichiers MP3", claude=True)
tache(P, "T32", "Ajouter muscles et nerfs (Z-Anatomy) au corps 3D", "Claude Code", "Import, décimation et occultation pelvienne vérifiée.", ["skills/3d-images-upload-super/scripts/build_glb.py"], "corps.glb enrichi", claude=True)
tache(P, "T33", "Relier chaque organe à VIT DIT CAFé et aux classes de médicaments", "Gemini (Pro)", "Une ligne par lettre et par organe : diagnostic type et classe thérapeutique.",
      ["conception/donnees/pharmaco/mnemonique.json"], "pharmaco/*.json remplis",
      prompt("Tu es pharmacologue clinicien suisse. Pour chaque organe, tu relies chaque lettre de VIT DIT CAFé à un diagnostic type et à sa classe de médicaments disponible en Suisse.", ["conception/donnees/pharmaco/mnemonique.json"], []), dep=["T01"])

# ---------------- 2. Paraclinique ----------------
P = "2_Jeux_Paraclinique"
for i, (reg, orgs) in enumerate(TOPO.items()):
    fich = [f"conception/donnees/paraclinique/topographie/{slug(reg)}/{slug(o)}.json" for o in orgs]
    n = sum(len(e) for m in orgs.values() for e in m.values())
    tache(P, f"P{1 + i:02d}", f"Remplir les examens de la région {reg} ({len(orgs)} organes, {n} examens)", f"Gemini (Pro) — compte {i % 4 + 1}",
          "Tu traites un organe par réponse ; tu importes ici chaque JSON rendu.", fich, "fichiers de topographie remplis",
          prompt("Tu es médecin interniste et radiologue suisse. Pour chaque examen de chaque fichier, tu remplis tous les champs.", fich, CHAMPS_EXAMEN,
                 ["Tu commences par la région thoracique si tu dois choisir un ordre." if reg.startswith("4") else "Tu gardes l'ordre des examens du fichier."]))
fich = [f"conception/donnees/paraclinique/biologie/prelevements/{slug(p)}.json" for p in PRELEVEMENTS]
tache(P, "P20", f"Remplir la biologie ({len(PRELEVEMENTS)} prélèvements)", "Gemini (Pro)", "Source unique des valeurs de référence ; les organes y renvoient.", fich, "prélèvements remplis",
      prompt("Tu es biologiste médical FAMH. Pour chaque analyse, tu remplis technique, valeurs de référence et interprétation.", fich,
             ["technique : prélèvement, tube, conditions (à jeun, horaire, transport).", "valeursReference : adulte homme et femme, enfant, grossesse si différent ; unités SI suisses.",
              "interpretation : causes d'augmentation et de diminution, des plus fréquentes aux plus graves.", "bulle : {def, pourquoi, confusion, retenir}."]))
tache(P, "P21", "Écrire les formules (≈ 40) et les critères diagnostiques (≈ 80)", "Gemini (Pro)", "Formules testables par script ; critères avec leur règle de décision.",
      ["conception/donnees/paraclinique/calculs.json", "conception/donnees/paraclinique/criteres.json"], "calculs.json, criteres.json",
      prompt("Tu es médecin interniste. Tu remplis les formules (trou anionique, Winter, Light, gradient albumine, DFG CKD-EPI…) et les critères diagnostiques usuels.",
             ["conception/donnees/paraclinique/calculs.json", "conception/donnees/paraclinique/criteres.json"],
             ["formule : écrite en notation calculable (ex. Na - (Cl + HCO3)).", "variables : nom et unité SI.", "regleDeDecision : le seuil qui pose le diagnostic.", "source : société ou publication de référence."]))
tache(P, "P22", "Compléter Smarter Medicine (toutes les listes suisses)", "Gemini (Deep Research) ou Grok", "Liste par société, avec date et lien.",
      ["conception/donnees/paraclinique/smarter_medicine.json"], "smarter_medicine.json complet",
      prompt("Tu fais une recherche sur smartermedicine.ch : tu relèves toutes les recommandations « Top 5 » de chaque société suisse.", ["conception/donnees/paraclinique/smarter_medicine.json"],
             ["situation, recommandation, societe, annee, url."]))
tache(P, "P23", "Trouver les images du pilote thorax (cliché patient + cliché normal)", "Gemini (Deep Research) ou Grok",
      "Tu ne télécharges rien : tu rends une liste d'URL d'images réelles avec leur licence ; Claude Code les télécharge et les annote.",
      ["conception/donnees/paraclinique/topographie/4_thorax/"], "conception/donnees/paraclinique/imagerie/banque_thorax.json",
      prompt("Tu cherches des images médicales réelles réutilisables : pour chaque examen d'imagerie du thorax, une image pathologique typique et une image normale de la même technique.",
             ["conception/donnees/paraclinique/topographie/4_thorax/*.json"],
             ["Rends un JSON : [{examen, diagnostic, urlImagePathologique, urlImageNormale, source, licence, auteur}].",
              "Sources à privilégier : Wikimedia Commons, Open-i (NIH), MedPix ; licence obligatoire et vérifiée ; jamais de dessin ni de schéma."]))
tache(P, "P24", "Télécharger, annoter et brancher la banque d'images thorax", "Claude Code", "Repères normaux lettrés, lésions numérotées ; fenêtre à deux clichés.", [], "imagerie/cas/*.json", dep=["P23"], claude=True)
tache(P, "P25", "Écrire 20 cas « le bon examen » (thorax)", "Gemini (Pro)", "Cas de l'arène : cinq examens possibles, un juste, justification par le discriminant.",
      ["conception/donnees/paraclinique/imagerie/cas/_modele.json"], "20 fichiers de cas",
      prompt("Tu es médecin interniste enseignant. Tu écris 20 cas cliniques thoraciques courts, chacun avec cinq examens possibles, l'examen juste et la justification par son discriminant.",
             ["conception/donnees/paraclinique/imagerie/cas/_modele.json"], ["Un examen inutile coûte des points : tu cites la recommandation Smarter Medicine quand elle existe."]), dep=["P04"])
tache(P, "P30", "Auditer et intégrer chaque lot importé", "Claude (finition)", "Contrôle des champs, des sigles, des seuils et des sources ; correction ; commit.", [], "audit RÉUSSI + commit", claude=True)

# ---------------- 3. Transversal ----------------
P = "3_Transversal_Discip"
tache(P, "X01", "Fixer le schéma de leçon (9 parties) et rédiger 2 leçons pilotes (C : SPIKES, Q : Top 5)", "Claude (conception)", "Le pilote fixe la qualité attendue avant tout volume.", [], "schéma + 2 leçons", claude=True)
for f in sorted(glob.glob(os.path.join(RAC, "conception", "donnees", "tetrade", "transversales", "outils", "*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    rel = os.path.relpath(f, RAC).replace(os.sep, "/")
    tache(P, f"X{ord(d['lettre']) - 64 + 10:02d}", f"Rédiger les leçons de {d['lettre']} — {d['nom']} ({len(d['lecons'])} leçons)", "Gemini (Pro)",
          "Une leçon par réponse ; tu importes ici chaque JSON.", [rel], "transversales/lecons/<id>.json",
          prompt(f"Tu es enseignant de médecine suisse, spécialiste de « {d['nom']} ». Pour chaque leçon du fichier, tu rédiges la leçon complète selon l'arbre en 9 parties.", [rel],
                 ["arborescence : cadre, notions, outils, décisions et seuils, applications par système, particularités par terrain, pièges, pratique suisse, exercices.",
                  "Chaque leçon commence par un cas suisse concret et finit par une décision à prendre.", "items : 5 QCM (type A ou K') avec explication de chaque option fausse."]),
          dep=["X01"])

# ---------------- 4. Jeux_45_Spec ----------------
P = "4_Jeux_45_Spec"
tache(P, "J01", "Lancer le pilote cardiologie (2 fiches) sur ton PC", "Ton PC (terminal)", "Commande : python scripts/produire_fiches_claude.py pilote --spec CAR --n 2", ["scripts/produire_fiches_claude.py"], "content/fiches/CAR/*.json")
tache(P, "J02", "Auditer les 2 fiches pilotes et ajuster le prompt", "Claude (finition)", "Mesure du coût réel par fiche ; correction du prompt.", [], "prompt validé", dep=["J01"], claude=True)
tache(P, "J03", "Produire les fiches par spécialité (couche 1)", "Gemini (Pro) — 4 comptes en parallèle", "Même schéma que le pilote ; une spécialité par compte.", ["scripts/schema_fiche.json"], "content/fiches/<SPEC>/*.json",
      prompt("Tu es médecin spécialiste suisse et enseignant. Tu rédiges les fiches de raisonnement demandées, en suivant exactement le schéma joint.", ["scripts/schema_fiche.json"],
             ["glossaire obligatoire ; présentations atypiques ; chaque examen avec son signe recherché et sa visée."]), dep=["J02"])
tache(P, "J04", "Générer les cartes réflexes (couche 2, 0 token)", "Claude Code", "python scripts/generer_reflexes.py", ["scripts/generer_reflexes.py"], "content/reflexes/", dep=["J03"], claude=True)
tache(P, "J05", "Auditer chaque lot de fiches (REJECTOR_)", "Claude (finition) — crédits API en lot", "Rejet des fiches non conformes, régénération ciblée.", [], "lots validés", dep=["J03"], claude=True)

LOTS = os.path.join(RAC, "projets", "lots")
os.makedirs(LOTS, exist_ok=True)
for f in glob.glob(os.path.join(LOTS, "*.json")):
    os.remove(f)
for t in T:
    chemins = []
    for e in t["entrees"]:
        if not e.endswith(".json") or "*" in e:
            motif = e if "*" in e else e.rstrip("/") + "/*.json"
            chemins += sorted(os.path.relpath(x, RAC).replace(os.sep, "/") for x in glob.glob(os.path.join(RAC, motif)))
        elif os.path.exists(os.path.join(RAC, e)):
            chemins.append(e)
    fich = {c: json.load(open(os.path.join(RAC, c), encoding="utf-8")) for c in chemins if c.endswith(".json")}
    t["lot"] = None
    if fich and t["prompt"]:
        nom = f"LOT_{t['id']}.json"
        json.dump({"_lot": {"tache": t["id"], "titre": t["titre"], "projet": t["projet"], "nombreFichiers": len(fich),
                            "consigne": "Chaque clé de « fichiers » est le chemin exact du fichier dans le dépôt Jeux_45_Spec. Remplis les valeurs, garde les chemins et les clés, rends le même objet."},
                   "fichiers": fich}, open(os.path.join(LOTS, nom), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        t["lot"] = "projets/lots/" + nom
        t["prompt"] = t["prompt"].replace("LOT_<identifiant>.json", nom)
    t["liens"] = [GH + e for e in t["entrees"] if "*" not in e]
    if t["lot"]:
        t["liens"].append(GH + t["lot"])

json.dump({"genere": "projets/outils/taches.py", "taches": T}, open(os.path.join(RAC, "projets", "taches.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
gabarit = open(os.path.join(RAC, "projets", "outils", "tableau_de_bord.gabarit.html"), encoding="utf-8").read()
html = gabarit.replace("/*TACHES*/[]", json.dumps(T, ensure_ascii=False).replace("</", "<\\/"))
open(os.path.join(RAC, "projets", "tableau_de_bord.html"), "w", encoding="utf-8").write(html)
print(len(T), "tâches ;", {p: sum(1 for t in T if t["projet"] == p) for p in dict.fromkeys(t["projet"] for t in T)})
