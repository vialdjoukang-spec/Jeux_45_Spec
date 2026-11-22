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
    l = [role, "", "Le fichier de lot joint (LOT_<identifiant>.json) contient, dans « fichiers », chaque fichier à remplir sous son chemin exact :"] + [f"- {f}" for f in fichiers]
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
for i, s_nom in enumerate(SYSTEMES):
    d = f"conception/donnees/tetrade/{slug(s_nom)}/"
    fich = [d + "semiologie.json", d + "syndromes.json", d + "physiopathologie.json"] + ([d + "criteres_cim10.json"] if slug(s_nom) == "psyche" else [])
    tache(P, f"T{40 + i}", f"Sémiologie, syndromes et physiopathologie : {s_nom}", "Gemini (Pro)",
          "Signes et symptômes par temps d'examen, syndromes et mécanismes du système ; un fichier par réponse.", fich, "fichiers du système remplis",
          prompt(f"Tu es clinicien enseignant de sémiologie. Pour le système « {s_nom} », tu remplis la sémiologie, les syndromes et la physiopathologie.", fich,
                 ["semiologie : chaque signe avec technique, nomConsacre, eponyme, termeSuisse, sensibilite, specificite, son, presentation (typique ou atypique) et bulle ; chaque symptôme avec questionAPoser et caracteristiques.",
                  "Chaque temps d'examen (inspection, palpation, percussion, auscultation, examens spécifiques) porte 2 à 3 signes typiques.",
                  "syndromes : signesMinimaux (2 ou 3), signes, symptomes, examenComplementaire, diagnostics (les plus fréquents, puis les rares graves), confusions possibles."
                  + (" Pour le système neurologique, tu couvres les 24 syndromes majeurs." if slug(s_nom) == "neurologique" else ""),
                  "physiopathologie : un mécanisme par signe majeur, en chaîne amorce → installation → maintien, et la liste des signes qu'il explique."]
                 + (["criteres_cim10 : critères condensés du chapitre F, par groupe d'âge, avec le chef de file thérapeutique par profil."] if slug(s_nom) == "psyche" else [])))
tache(P, "T60", "Construire par script les graphes, l'arbre 3D et les exercices de la Tétrade", "Claude Code",
      "Les graphes se déduisent des fichiers remplis (0 token) : aucune IA de production n'y touche.", [], "tetrade/*/graphe.json, anatomie3d.json, exercices/*.json", claude=True)
for i, s_nom in enumerate(SYSTEMES):
    f = f"conception/donnees/pharmaco/{slug(s_nom)}/structures.json"
    tache(P, f"T{61 + i}", f"Pharmacologie : structures et cibles — {s_nom}", "Gemini (Pro)", "Structures malades et ciblables, avec leurs cibles moléculaires.", [f], "structures.json rempli",
          prompt(f"Tu es pharmacologue clinicien suisse. Pour le système « {s_nom} », tu listes les structures qui tombent malades et leurs cibles médicamenteuses.", [f],
                 ["structureId, nom, maillage3d (nom anatomique de la structure), cibles (récepteurs, enzymes, canaux, transporteurs) avec la classe qui les vise.",
                  "Tu relies chaque structure aux lettres VIT DIT CAFé qui la concernent."]), dep=["T01"])
tache(P, "T80", "Classes médicamenteuses (≈ 300)", "Gemini (Pro)", "Classe, mécanisme, indications et chef de file par profil, selon le Compendium suisse.",
      ["conception/donnees/pharmaco/classes.json"], "classes.json rempli",
      prompt("Tu es pharmacologue clinicien suisse. Tu remplis les classes médicamenteuses disponibles en Suisse.", ["conception/donnees/pharmaco/classes.json"],
             ["classeId, nom, mecanisme (une phrase), indications, chefDeFile par profil (adulte, enfant, grossesse, sujet âgé, insuffisance rénale)."]))
tache(P, "T81", "Fixer la liste des molécules (index AIPS) avant leur rédaction", "Claude (conception)", "Liste issue de l'AIPS, puis lots de fiches de molécules.", ["conception/donnees/pharmaco/molecules/_modele.json"], "liste validée", claude=True)
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
from catalogue_paraclinique import EXPLORATIONS
for i in range(0, len(EXPLORATIONS), 27):
    bloc = EXPLORATIONS[i:i + 27]
    fich = [f"conception/donnees/paraclinique/explorations/{slug(e)}.json" for e in bloc]
    tache(P, f"P{31 + i // 27}", f"Explorations fonctionnelles et endoscopies {i + 1} à {i + len(bloc)} ({bloc[0]} → {bloc[-1]})", "Gemini (Pro)",
          "Une fiche par exploration : principe, tracé normal et pathologique, seuils, interprétation.", fich, "fiches d'exploration remplies",
          prompt("Tu es médecin spécialiste des explorations fonctionnelles. Pour chaque exploration, tu remplis sa fiche.", fich,
                 ["fonction : ce que l'examen mesure, en une phrase.", "traces : le tracé ou l'aspect normal, puis les aspects pathologiques typiques, chacun nommé.",
                  "seuils : les valeurs qui séparent normal et pathologique, en unités SI.", "interpretation : la démarche de lecture, en étapes courtes.",
                  "diagnostics : les diagnostics que l'examen pose ou exclut.", "bulle : {def, pourquoi, confusion, retenir}."]))
tache(P, "P36", "Construire par script le graphe d'imagerie, les régions, l'index des prélèvements et les exercices", "Claude Code",
      "Tout se déduit du catalogue (0 token).", [], "imagerie/graphe.json, regions.json, biologie/prelevements.json, exercices/*.json", claude=True)
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

SIGNATURE = "AAI (Anthropic AI)"
LOTS = os.path.join(RAC, "projets", "lots")
os.makedirs(LOTS, exist_ok=True)
for f in glob.glob(os.path.join(LOTS, "**", "*.json"), recursive=True):
    os.remove(f)


def nf(t):
    t = t.replace("œ", "oe").replace("Œ", "Oe").replace("é", "e").replace("É", "E")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[()',.:;«»]", " ", t)
    return re.sub(r"[^A-Za-z0-9-]+", "_", t).strip("_")


def court(x, n=34):
    return x if len(x) <= n else x[:n].rsplit("_", 1)[0]


def classer(t):
    """→ (dossier projet, dossier thème, nom explicite du lot)"""
    i, ti = t["id"], t["titre"]
    sysn = re.search(r"(?:système |: |— )(.+?)(?: \(|$)", ti)
    sysn = nf(sysn.group(1)) if sysn else ""
    if i[0] == "T":
        n = int(i[1:])
        if 10 <= n < 30:
            m = re.search(r"\((\d+) organes\)", ti)
            return "1_Tetrade_Fondation", "1_Organes_Anatomie_Physiologie", f"{i}_Anatomie_Physiologie_{sysn}_{m.group(1)}-organes"
        if 40 <= n < 60:
            return "1_Tetrade_Fondation", "2_Semiologie_Syndromes_Physiopathologie", f"{i}_Semiologie_Syndromes_Physiopathologie_{sysn}"
        if 61 <= n <= 74:
            return "1_Tetrade_Fondation", "3_Pharmacologie", f"{i}_Pharmacologie_Structures_Cibles_{nf(ti.split('— ')[-1])}"
        if n == 80:
            return "1_Tetrade_Fondation", "3_Pharmacologie", "T80_Pharmacologie_Classes_medicamenteuses_Suisse"
        if n == 33:
            return "1_Tetrade_Fondation", "3_Pharmacologie", "T33_Pharmacologie_VIT-DIT-CAFe_par_organe"
    if i[0] == "P":
        n = int(i[1:])
        if n < 20:
            m = re.search(r"région \d+\. (.+?) \((\d+) organes, (\d+) examens\)", ti)
            return "2_Paraclinique", "1_Examens_par_region", f"{i}_Examens_{nf(m.group(1))}_{m.group(2)}-organes_{m.group(3)}-examens"
        if n == 20:
            return "2_Paraclinique", "2_Biologie", "P20_Biologie_23-prelevements_valeurs_SI_interpretation"
        if n == 21:
            return "2_Paraclinique", "3_Formules_Criteres_SmarterMedicine", "P21_Formules_et_Criteres_diagnostiques"
        if n == 22:
            return "2_Paraclinique", "3_Formules_Criteres_SmarterMedicine", "P22_SmarterMedicine_recommandations_suisses"
        if n == 23:
            return "2_Paraclinique", "4_Imagerie_Images_et_Cas", "P23_Images_reelles_Thorax_URL_et_licences"
        if n == 25:
            return "2_Paraclinique", "4_Imagerie_Images_et_Cas", "P25_Cas_cliniques_Thorax_le_bon_examen"
        if 31 <= n <= 39:
            m = re.search(r"\((.+?) → (.+?)\)$", ti)
            return "2_Paraclinique", "5_Explorations_fonctionnelles_Endoscopies", f"{i}_Explorations_{court(nf(m.group(1)))}_a_{court(nf(m.group(2)))}"
    if i[0] == "X":
        m = re.search(r"de (\w) — (.+?) \(", ti)
        return "3_Transversal_Discip", "1_Lecons_par_discipline", f"{i}_Lecons_{m.group(1)}_{nf(m.group(2))[:45]}"
    if i[0] == "J":
        return "4_Jeux_45_Spec", "1_Fiches_par_specialite", f"{i}_Fiches_specialites_schema"
    return "0_Divers", "0_Divers", f"{i}_{nf(ti)[:50]}"
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
        dp, dt, base = classer(t)
        nom = base + ".json"
        rel = f"{dp}/{dt}/{nom}"
        os.makedirs(os.path.join(LOTS, dp, dt), exist_ok=True)
        json.dump({"_lot": {"tache": t["id"], "titre": t["titre"], "projet": t["projet"], "nombreFichiers": len(fich), "signature": SIGNATURE,
                            "consigne": "Chaque clé de « fichiers » est le chemin exact du fichier dans le dépôt Jeux_45_Spec. Remplis les valeurs, garde les chemins et les clés, rends le même objet."},
                   "fichiers": fich}, open(os.path.join(LOTS, dp, dt, nom), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        t["lot"] = "projets/lots/" + rel
        t["prompt"] = t["prompt"].replace("LOT_<identifiant>.json", nom)
    t["liens"] = [GH + e for e in t["entrees"] if "*" not in e]
    if t["lot"]:
        t["liens"].append(GH + t["lot"])

json.dump({"genere": "projets/outils/taches.py", "taches": T}, open(os.path.join(RAC, "projets", "taches.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
gabarit = open(os.path.join(RAC, "projets", "outils", "tableau_de_bord.gabarit.html"), encoding="utf-8").read()
html = gabarit.replace("/*TACHES*/[]", json.dumps(T, ensure_ascii=False).replace("</", "<\\/"))
open(os.path.join(RAC, "projets", "tableau_de_bord.html"), "w", encoding="utf-8").write(html)
print(len(T), "tâches ;", {p: sum(1 for t in T if t["projet"] == p) for p in dict.fromkeys(t["projet"] for t in T)})

# ---------- 00_LISEZ_MOI.md : arborescence des lots ----------
L = ["# LOTS JSON — mode d'emploi et arborescence", "",
     "1. Une seule fois par plateforme : tu colles 00_INSTRUCTIONS_PRODUCTEUR.md dans les instructions permanentes (Gem, instructions personnalisées).",
     "2. Pour chaque tâche : tu ouvres le dossier du projet, puis le dossier du thème ; tu joins le lot et tu colles son prompt (tableau de bord : https://claude.ai/artifact/N7VUBhFLfp3gq6rTsPt88v).",
     "3. Tu importes la réponse dans la tâche du tableau de bord.", "",
     "Le nom de chaque lot dit son contenu : identifiant de tâche, sujet, système ou région, volume.", ""]
arbre = {}
for t in T:
    if t.get("lot"):
        dp, dt, nom = t["lot"].split("/")[2:5]
        arbre.setdefault(dp, {}).setdefault(dt, []).append((nom, t))
for dp in sorted(arbre):
    L += ["", f"## {dp}"]
    for dt in sorted(arbre[dp]):
        L += ["", f"### {dp}/{dt}"]
        for nom, t in arbre[dp][dt]:
            n = json.load(open(os.path.join(RAC, t["lot"]), encoding="utf-8"))["_lot"]["nombreFichiers"]
            L.append(f"- **{nom}** — {t['titre']} ({n} fichiers JSON)")
L += ["", f"Signature : {SIGNATURE}"]
open(os.path.join(LOTS, "00_LISEZ_MOI.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
