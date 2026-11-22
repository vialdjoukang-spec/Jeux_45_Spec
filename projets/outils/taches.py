"""Tâches des 4 projets (source unique) → projets/taches.json et projets/tableau_de_bord.html.
Répartition : Claude conçoit, audite et polit ; le gros œuvre (volumes de texte, recherche d'images) se fait ailleurs.
Usage : python projets/outils/taches.py"""
import json, os, re, sys, unicodedata, glob

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAC, "conception", "outils"))
from catalogue_paraclinique import TOPO, PRELEVEMENTS, MODALITES
from systemes import SYSTEMES

GH = "https://github.com/vialdjoukang-spec/Jeux_45_Spec/blob/main/"


def slug(t):
    t = t.replace("œ", "oe").replace("Œ", "Oe").replace("æ", "ae").replace("Æ", "Ae")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    t = re.sub(r"\(.*?\)", "", t)
    return re.sub(r"[^a-z0-9]+", "_", t).strip("_")[:40]


def nf(t):
    t = t.replace("œ", "oe").replace("Œ", "Oe").replace("é", "e").replace("É", "E")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[()',.:;«»]", " ", t)
    return re.sub(r"[^A-Za-z0-9-]+", "_", t).strip("_")


def court(x, n=34):
    return x if len(x) <= n else x[:n].rsplit("_", 1)[0]


MOD_COURT = {"IMG": "imagerie", "BIO": "biologie", "FCT": "explorations", "END": "endoscopies", "HIS": "anatomopathologie"}


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


def tache(projet, id, titre, ou, quoi, entrees=(), sortie="", prompt_txt="", dep=(), claude=False, dossier=None, nom=None, fragment=None):
    T.append({"projet": projet, "id": id, "titre": titre, "ou": ou, "quoi": quoi, "entrees": list(entrees), "sortie": sortie,
              "prompt": prompt_txt, "dependances": list(dep), "claude": claude, "dossier": list(dossier) if dossier else None, "nomLot": nom, "fragment": fragment})


# ---------------- 1. Tétrade ----------------
P = "1_Jeux_Tetrade_Fondation"
tache(P, "T01", "Valider la liste des organes, les volets et les fenêtres du système cardiovasculaire", "Claude (conception)",
      "Claude te propose la liste, tu valides ou tu corriges ; rien ne se produit avant ta validation.", ["conception/outils/systemes.py"], "systemes.py validé", claude=True)
DT = "1_Tetrade_Fondation"
for i, (s_nom, orgs) in enumerate(SYSTEMES.items()):
    dsys = f"{i + 1:02d}_{nf(s_nom)}"
    for o, (org, _, _) in enumerate(orgs, 1):
        f = f"conception/donnees/tetrade/{slug(s_nom)}/organes/{slug(org)}.json"
        tache(P, f"T{10 + i:02d}-{o:02d}", f"Anatomie et physiologie : {org} ({s_nom})", "Gemini (Pro)",
              "Un seul organe : anatomie (6 volets) et physiologie (5 volets).", [f], "fichier d'organe rempli",
              prompt("Tu es anatomiste et physiologiste, enseignant en faculté de médecine suisse. Tu remplis le fichier d'organe : anatomie et physiologie, volet par volet.", [f],
                     ["anatomie : pour chaque volet, 3 à 6 entrées {motCle, texte, fenetre} ; motCle en 1 à 4 mots ; texte en une ou deux phrases ; fenetre = « 3d ».",
                      "physiologie : pour chaque volet, du paramètre le plus simple au plus complexe ; fenetre = nom de la courbe ou du calculateur utile (ex. starling, pression_volume, ecg, clairance), sinon null.",
                      "bulle : {def, pourquoi, confusion, retenir} pour l'organe."],
                     ["Tu ne mets dans motCle qu'un nom court : le détail va dans texte.", "Tu ne dessines aucune courbe : tu nommes seulement la fenêtre."]),
              dep=["T01"], dossier=(DT, "1_Organes_Anatomie_Physiologie", dsys, f"{o:02d}_{nf(court(org.split(' (')[0], 40))}"),
              nom=f"T{10 + i:02d}-{o:02d}_Anatomie_Physiologie_{nf(org.split(' (')[0])[:40]}")
SEMIO = {"semiologie": ("Semiologie", "semiologie : chaque signe avec technique, nomConsacre, eponyme, termeSuisse, sensibilite, specificite, son, presentation (typique ou atypique) et bulle ; chaque symptôme avec questionAPoser et caracteristiques. Chaque temps d'examen (inspection, palpation, percussion, auscultation, examens spécifiques) porte 2 à 3 signes typiques."),
         "syndromes": ("Syndromes", "syndromes : signesMinimaux (2 ou 3), signes, symptomes, examenComplementaire, diagnostics (les plus fréquents, puis les rares graves), confusions possibles."),
         "physiopathologie": ("Physiopathologie", "physiopathologie : un mécanisme par signe majeur, en chaîne amorce → installation → maintien, et la liste des signes qu'il explique."),
         "criteres_cim10": ("Criteres_CIM-10", "criteres_cim10 : critères condensés du chapitre F, par groupe d'âge, avec le chef de file thérapeutique par profil.")}
for i, s_nom in enumerate(SYSTEMES):
    dsys = f"{i + 1:02d}_{nf(s_nom)}"
    for q, (fic, (lib, regle)) in enumerate(SEMIO.items(), 1):
        if fic == "criteres_cim10" and slug(s_nom) != "psyche":
            continue
        f = f"conception/donnees/tetrade/{slug(s_nom)}/{fic}.json"
        tache(P, f"T{40 + i}-{q}", f"{lib.replace('_', ' ')} : {s_nom}", "Gemini (Pro)", "Un seul fichier du système.", [f], "fichier rempli",
              prompt(f"Tu es clinicien enseignant. Pour le système « {s_nom} », tu remplis ce fichier.", [f],
                     [regle + (" Pour le système neurologique, tu couvres les 24 syndromes majeurs." if fic == "syndromes" and slug(s_nom) == "neurologique" else "")]),
              dossier=(DT, "2_Semiologie_Syndromes_Physiopathologie", dsys), nom=f"T{40 + i}-{q}_{lib}_{nf(s_nom)[:35]}")
tache(P, "T60", "Construire par script les graphes, l'arbre 3D et les exercices de la Tétrade", "Claude Code",
      "Les graphes se déduisent des fichiers remplis (0 token) : aucune IA de production n'y touche.", [], "tetrade/*/graphe.json, anatomie3d.json, exercices/*.json", claude=True)
for i, s_nom in enumerate(SYSTEMES):
    f = f"conception/donnees/pharmaco/{slug(s_nom)}/structures.json"
    tache(P, f"T{61 + i}", f"Pharmacologie : structures et cibles — {s_nom}", "Gemini (Pro)", "Structures malades et ciblables, avec leurs cibles moléculaires.", [f], "structures.json rempli",
          prompt(f"Tu es pharmacologue clinicien suisse. Pour le système « {s_nom} », tu listes les structures qui tombent malades et leurs cibles médicamenteuses.", [f],
                 ["structureId, nom, maillage3d (nom anatomique de la structure), cibles (récepteurs, enzymes, canaux, transporteurs) avec la classe qui les vise.",
                  "Tu relies chaque structure aux lettres VIT DIT CAFé qui la concernent."]), dep=["T01"],
          dossier=(DT, "3_Pharmacologie", f"{i + 1:02d}_{nf(s_nom)}"), nom=f"T{61 + i}_Pharmacologie_Structures_Cibles_{nf(s_nom)[:35]}")
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
DP = "2_Paraclinique"
# 2.1 Examens par région, puis un lot par organe (fragments courts, homogènes, faciles à répartir)
for r, (reg, orgs) in enumerate(TOPO.items(), 1):
    dreg = f"{r:02d}_{nf(reg.split('. ', 1)[-1])}"
    for o, (org, mods) in enumerate(orgs.items(), 1):
        f = f"conception/donnees/paraclinique/topographie/{slug(reg)}/{slug(org)}.json"
        n = sum(len(e) for e in mods.values())
        detail = " + ".join(f"{len(v)} {MOD_COURT[k]}" for k, v in mods.items() if v)
        dorg = f"{o:02d}_{nf(court(org, 40))}"
        parts = [(None, n)] if n <= 10 else [(MODALITES[k], len(v)) for k, v in mods.items() if v]
        for m, nb in parts:
            code = "" if m is None else "-" + {"Imagerie": "IMG", "Biologie": "BIO", "Exploration fonctionnelle": "FCT", "Endoscopie": "END", "Anatomopathologie / biopsie": "HIS"}[m]
            tache(P, f"P{r:02d}-{o:02d}{code}", f"Examens de l'organe {org}" + (f" — {m}" if m else "") + f" ({nb} examens{'' if m else ' : ' + detail})", f"Gemini (Pro) — compte {(r + o) % 4 + 1}",
                  "Un fragment court et homogène ; il se réassemble par script au retour.", [f], "examens remplis",
                  prompt("Tu es médecin interniste et radiologue suisse. Pour chaque examen du fragment, tu remplis tous les champs.", [f], CHAMPS_EXAMEN,
                         ["Biologie : tu ne donnes pas de valeurs de référence (elles vivent dans les fiches d'analyses) ; tu dis pourquoi on demande l'analyse pour cet organe, ce qu'on y cherche et le seuil décisionnel.",
                          "analysesRef est déjà rempli : tu ne le modifies pas."]),
                  dossier=(DP, "1_Examens_par_organe", dreg, dorg), nom=f"P{r:02d}-{o:02d}{code}_{nf(m) if m else 'Examens'}_{nf(org)[:35]}_{nb}-examens",
                  fragment={"cle": "examens", "champ": "modalite", "valeur": m} if m else None)
# 2.2 Biologie : analyses individuelles (source unique des valeurs), par famille
from analyses_biologiques import FAMILLES
for fam, (prel, lst) in sorted(FAMILLES.items()):
    k = int(fam[:2])
    f = f"conception/donnees/paraclinique/biologie/analyses/{fam.lower()}.json"
    lib = fam.split("_", 1)[1].replace("_", " ")
    tache(P, f"PB{k:02d}", f"Analyses biologiques : {lib} ({len(lst)} analyses)", "Gemini (Pro)",
          "Une fiche par analyse : unité SI, valeurs par âge, sexe et grossesse, seuils critiques, causes de hausse et de baisse.", [f], "fiches d'analyses remplies",
          prompt("Tu es biologiste médical FAMH en Suisse. Pour chaque analyse du fichier, tu remplis sa fiche complète.", [f],
                 ["tube : le tube et l'anticoagulant (ex. tube sec, EDTA, citrate, héparine).", "unite : l'unité SI suisse (mmol/l, µmol/l, g/l, kPa…).",
                  "valeursReference : adulteHomme, adulteFemme, enfant, grossesse, sujetAge ; une valeur ou un intervalle avec l'unité ; si la valeur ne diffère pas, tu écris « identique à l'adulte ».",
                  "seuilsCritiques : les valeurs qui imposent une action immédiate (valeurs d'alerte du laboratoire).", "variationsPhysiologiques : horaire, effort, repas, posture, âge.",
                  "augmentation et diminution : les causes, des plus fréquentes aux plus graves.", "interferences : médicaments et facteurs préanalytiques (hémolyse, garrot, biotine…).",
                  "delaiResultat : délai habituel du résultat.", "organes est déjà rempli : tu ne le modifies pas.", "bulle : {def, pourquoi, confusion, retenir}."],
                 ["Tu ne crées pas d'analyse nouvelle : si une analyse importante manque, tu la signales dans _lot.aVerifier."]),
          dossier=(DP, "2_Biologie", "1_Analyses_individuelles"), nom=f"PB{k:02d}_Analyses_{nf(lib)}_{len(lst)}-analyses")
GROUPES_PRELEVEMENTS = {
    "Sang": ["Sang veineux", "Sang artériel", "Sang capillaire", "Hémocultures"],
    "Liquides_de_ponction": ["Liquide céphalorachidien", "Liquide pleural", "Liquide d'ascite", "Liquide synovial", "Liquide péricardique", "Liquide amniotique", "Ponction de kyste, d'abcès ou de collection"],
    "Secretions_excreta_ecouvillons": ["Urine", "Selles", "Expectorations et lavage bronchoalvéolaire", "Prélèvements génitaux et urétraux", "Écouvillons nasopharyngés et de gorge", "Sperme", "Salive", "Air expiré"],
    "Tissus_et_divers": ["Moelle osseuse", "Biopsies tissulaires", "Cheveux et ongles", "Sueur"]}
_reste = [p for p in PRELEVEMENTS if not any(p.lower().startswith(x.lower()[:12]) for g in GROUPES_PRELEVEMENTS.values() for x in g)]
if _reste:
    GROUPES_PRELEVEMENTS["Tissus_et_divers"] += _reste
for k, (g, noms) in enumerate(GROUPES_PRELEVEMENTS.items(), 1):
    pres = [p for p in PRELEVEMENTS if any(p.lower().startswith(x.lower()[:12]) for x in noms)]
    fich = [f"conception/donnees/paraclinique/biologie/prelevements/{slug(p)}.json" for p in pres]
    tache(P, f"PP{k:02d}", f"Prélèvements : {g.replace('_', ' ')} ({len(pres)} prélèvements, technique)", "Gemini (Pro)",
          "Technique, tube, conditions, conservation ; les valeurs vivent dans les fiches d'analyses.", fich, "prélèvements remplis",
          prompt("Tu es biologiste médical FAMH. Pour chaque rubrique de chaque prélèvement, tu décris la technique.", fich,
                 ["technique : le geste de prélèvement, en étapes courtes.", "tube : tube, flacon ou milieu de transport.", "conditions : à jeun, horaire, position, arrêt de traitement.",
                  "conservationTransport : température et délai maximal avant analyse.", "interpretation : ce que la rubrique permet de conclure, sans valeurs (elles sont dans les fiches d'analyses).",
                  "analysesRef est déjà rempli : tu ne le modifies pas.", "bulle : {def, pourquoi, confusion, retenir}."]),
          dossier=(DP, "2_Biologie", "2_Prelevements_technique"), nom=f"PP{k:02d}_Prelevements_{g}_{len(pres)}-prelevements")
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
             ["conception/donnees/paraclinique/imagerie/cas/_modele.json"], ["Un examen inutile coûte des points : tu cites la recommandation Smarter Medicine quand elle existe."]), dep=[t["id"] for t in T if t["id"].startswith("P04-") and ("Poumons et voies" in t["titre"] or "Cœur et péricarde" in t["titre"])])
from catalogue_paraclinique import EXPLORATIONS, _cle
_ou = {}
for r, (reg, orgs) in enumerate(TOPO.items(), 1):
    for org, mods in orgs.items():
        for typ in ("FCT", "END"):
            for e in mods.get(typ, []):
                _ou.setdefault(_cle(e), (typ, r, reg))
_grp = {}
for e in EXPLORATIONS:
    typ, r, reg = _ou[_cle(e)]
    _grp.setdefault((typ, r, reg), []).append(e)
for (typ, r, reg), lst in sorted(_grp.items()):
    dt = "3_Explorations_fonctionnelles" if typ == "FCT" else "4_Endoscopies"
    dreg = f"{r:02d}_{nf(reg.split('. ', 1)[-1])}"
    nb = -(-len(lst) // 15); taille = -(-len(lst) // nb)
    for b in range(0, len(lst), taille):
        bloc = lst[b:b + taille]
        fich = [f"conception/donnees/paraclinique/explorations/{slug(e)}.json" for e in bloc]
        suf = f"-{b // taille + 1}" if nb > 1 else ""
        idt = f"P{'F' if typ == 'FCT' else 'E'}{r:02d}{suf}"
        lib = "Explorations fonctionnelles" if typ == "FCT" else "Endoscopies"
        tache(P, idt, f"{lib} — {reg.split('. ', 1)[-1]} ({len(bloc)} fiches)", "Gemini (Pro)",
              "Une fiche par technique : principe, aspect normal et pathologique, seuils, interprétation.", fich, "fiches remplies",
              prompt("Tu es médecin spécialiste des explorations fonctionnelles et de l'endoscopie. Pour chaque technique, tu remplis sa fiche.", fich,
                     ["fonction : ce que l'examen mesure, en une phrase.", "traces : l'aspect normal, puis les aspects pathologiques typiques, chacun nommé.",
                      "seuils : les valeurs qui séparent normal et pathologique, en unités SI.", "interpretation : la démarche de lecture, en étapes courtes.",
                      "diagnostics : les diagnostics que l'examen pose ou exclut.", "bulle : {def, pourquoi, confusion, retenir}."]),
              dossier=(DP, dt, dreg), nom=f"{idt}_{nf(lib)}_{nf(reg.split('. ', 1)[-1])[:30]}_{len(bloc)}-fiches")
tache(P, "P36", "Construire par script le graphe d'imagerie, les régions, l'index des prélèvements et les exercices", "Claude Code",
      "Tout se déduit du catalogue (0 token).", [], "imagerie/graphe.json, regions.json, biologie/prelevements.json, exercices/*.json", claude=True)
tache(P, "P30", "Auditer et intégrer chaque lot importé", "Claude (finition)", "Contrôle des champs, des sigles, des seuils et des sources ; correction ; commit.", [], "audit RÉUSSI + commit", claude=True)

# ---------------- 3. Transversal ----------------
P = "3_Transversal_Discip"
tache(P, "X01", "Fixer le schéma de leçon (9 parties) et rédiger 2 leçons pilotes (C : SPIKES, Q : Top 5)", "Claude (conception)", "Le pilote fixe la qualité attendue avant tout volume.", [], "schéma + 2 leçons", claude=True)
for f in sorted(glob.glob(os.path.join(RAC, "conception", "donnees", "tetrade", "transversales", "outils", "*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    dd = f"{d['lettre']}_{nf(d['nom'])[:40]}"
    for q, l in enumerate(d["lecons"], 1):
        fl = f"conception/donnees/tetrade/transversales/lecons/{d['lettre']}/{slug(l['id'])}.json"
        tache(P, f"X{d['lettre']}-{q:02d}", f"Leçon {d['lettre']} — {l['titre']}", "Gemini (Pro)", "Une leçon complète selon l'arbre en 9 parties, avec 5 QCM.", [fl, os.path.relpath(f, RAC).replace(os.sep, "/")], "leçon remplie",
              prompt(f"Tu es enseignant de médecine suisse, spécialiste de « {d['nom']} ». Tu rédiges la leçon « {l['titre']} » ; le fichier de la discipline t'est joint pour le contexte, tu ne le modifies pas.", [fl],
                     ["parties : cadre, notions, outils, décisions et seuils, applications par système, particularités par terrain, pièges, pratique suisse, exercices ; chaque partie en phrases verbales courtes.",
                      "casDOuverture : un cas suisse concret ; decisionFinale : la décision que l'apprenant doit savoir prendre.",
                      "items : 5 QCM (type A ou K') avec une explication pour chaque option.", "bulle : {def, pourquoi, confusion, retenir}."]),
              dep=["X01"], dossier=("3_Transversal_Discip", "1_Lecons_par_discipline", dd), nom=f"X{d['lettre']}-{q:02d}_Lecon_{nf(court(l['titre'], 45))}")

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
import shutil
for x in os.listdir(LOTS):
    if os.path.isdir(os.path.join(LOTS, x)):
        shutil.rmtree(os.path.join(LOTS, x))


def classer(t):
    """→ (dossier projet, dossier thème, nom explicite du lot)"""
    if t.get("dossier"):
        return t["dossier"][0], "/".join(t["dossier"][1:]), t["nomLot"]
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
            return "2_Paraclinique", "6_Formules_Criteres_SmarterMedicine", "P21_Formules_et_Criteres_diagnostiques"
        if n == 22:
            return "2_Paraclinique", "6_Formules_Criteres_SmarterMedicine", "P22_SmarterMedicine_recommandations_suisses"
        if n == 23:
            return "2_Paraclinique", "5_Imagerie_Images_et_Cas", "P23_Images_reelles_Thorax_URL_et_licences"
        if n == 25:
            return "2_Paraclinique", "5_Imagerie_Images_et_Cas", "P25_Cas_cliniques_Thorax_le_bon_examen"
        if 31 <= n <= 39:
            m = re.search(r"\((.+?) → (.+?)\)$", ti)
            return "2_Paraclinique", "5_Explorations_fonctionnelles_Endoscopies", f"{i}_Explorations_{court(nf(m.group(1)))}_a_{court(nf(m.group(2)))}"
    if i[0] == "X":
        m = re.search(r"de (\w) — (.+?) \(", ti)
        return "3_Transversal_Discip", "1_Lecons_par_discipline", f"{i}_Lecons_{m.group(1)}_{nf(m.group(2))[:45]}"
    if i[0] == "J":
        return "4_Jeux_45_Spec", "1_Fiches_par_specialite", f"{i}_Fiches_specialites_schema"
    return "0_Divers", "0_Divers", f"{i}_{nf(ti)[:50]}"
# ---------- jumeaux PRATIQUE : chaque lot théorique a son lot pratique (défis du jeu), rangés 1_Theorie / 2_Pratique ----------
sys.path.insert(0, os.path.join(RAC, "conception", "outils"))
from pratique import DEFIS, REGLES as REGLES_PRATIQUE
for t in list(T):
    if t["claude"] or not t["prompt"] or t["id"] in ("P21", "P22", "P23", "P25", "J03", "T33", "T80"):
        continue
    dp, dt, base = classer(t)
    t["dossier"], t["nomLot"] = [dp] + dt.split("/") + ["1_Theorie"], base
    src = [e for e in t["entrees"] if e.startswith("conception/donnees/") and "/transversales/outils/" not in e]
    pr = ["conception/donnees/pratique/" + e[len("conception/donnees/"):] for e in src]
    pr = [x for x in pr if os.path.exists(os.path.join(RAC, x))]
    if not pr:
        continue
    types = sorted({ty for f in pr for e in json.load(open(os.path.join(RAC, f), encoding="utf-8"))["entites"] for d in e["defis"] for ty in [d["type"]]})
    champs = [f"{ty} : " + ", ".join(k for k in next(c for g in DEFIS.values() for (tt, c, _) in g if tt == ty)) for ty in types]
    frag = dict(t["fragment"], cle="entites") if t.get("fragment") else None
    T.append({**t, "id": t["id"] + "-PR", "titre": "Pratique — " + t["titre"], "quoi": "Les défis du jeu pour chaque entité du lot théorique jumeau (à joindre une fois rempli).",
              "entrees": pr, "sortie": "défis remplis", "dependances": [t["id"]], "fragment": frag,
              "dossier": [dp] + dt.split("/") + ["2_Pratique"], "nomLot": base.replace(t["id"], t["id"] + "-PR", 1) + "_PRATIQUE",
              "prompt": prompt("Tu es concepteur de jeux pédagogiques médicaux et clinicien suisse. Pour chaque entité du fichier pratique, tu remplis ses défis. "
                               "Tu joins aussi le JSON théorique jumeau déjà rempli : chaque défi s'appuie sur lui.", pr,
                               ["Champs communs : id (ex. <ref>-1), type (déjà fixé), mode, niveau, points, tempsSec, correction {pourquoiJuste, pourquoiFaux}, sources."] + champs,
                               REGLES_PRATIQUE)})
for t in T:
    chemins = []
    for e in t["entrees"]:
        if not e.endswith(".json") or "*" in e:
            motif = e if "*" in e else e.rstrip("/") + "/*.json"
            chemins += sorted(os.path.relpath(x, RAC).replace(os.sep, "/") for x in glob.glob(os.path.join(RAC, motif)))
        elif os.path.exists(os.path.join(RAC, e)):
            chemins.append(e)
    fich = {c: json.load(open(os.path.join(RAC, c), encoding="utf-8")) for c in chemins if c.endswith(".json")}
    fr = t.get("fragment")
    if fr:  # fragment : seuls les éléments de la valeur demandée ; le script de fusion les replace par leur id
        for c, v in fich.items():
            if isinstance(v.get(fr["cle"]), list):
                v[fr["cle"]] = [x for x in v[fr["cle"]] if isinstance(x, dict) and x.get(fr["champ"]) == fr["valeur"]]
                v["_fragment"] = {**fr, "reassemblage": "projets/outils/fusionner_retours.py remet chaque élément à sa place par son id (ou ref)"}
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
        _p = t["lot"].split("/")[2:]
        dp, dt, nom = _p[0], "/".join(_p[1:-1]), _p[-1]
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

# ---------- INDEX_JSON.md : tous les JSON du dépôt avec liens ----------
import collections as _c
_B, _R = GH, "https://raw.githubusercontent.com/vialdjoukang-spec/Jeux_45_Spec/main/"
_fs = sorted(os.path.relpath(f, RAC).replace(os.sep, "/") for f in glob.glob(os.path.join(RAC, "**", "*.json"), recursive=True))
_g = _c.OrderedDict()
for f in _fs:
    _g.setdefault("/".join(f.split("/")[:-1]) or "(racine)", []).append(f)
_o = sorted(_g, key=lambda k: (0 if k.startswith("projets/lots") else 1 if "paraclinique" in k else 2 if "tetrade" in k else 3 if "pharmaco" in k else 4, k))
L = ["# Index de tous les fichiers JSON du dépôt Jeux_45_Spec", "", f"{len(_fs)} fichiers ; chemin exact, lien GitHub, lien brut (raw) lisible par une IA.",
     "Ordre : lots de production (projet → thème → région), paraclinique, tétrade, pharmacologie, puis le reste.", "", "## Sommaire", ""] + [f"- {k} — {len(_g[k])} fichiers" for k in _o]
for k in _o:
    L += ["", f"## {k}", ""] + [f"- `{f}` — [GitHub]({_B + f}) · [brut]({_R + f})" for f in _g[k]]
L += ["", f"Signature : {SIGNATURE}"]
open(os.path.join(RAC, "INDEX_JSON.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
