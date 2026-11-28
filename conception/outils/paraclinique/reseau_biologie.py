"""RESEAU_BIOLOGIE — chaîne de l'onglet Biologie lue dans conception/donnees/paraclinique/biologie/fiches/ (BRIEF_BIOLOGIE § 2, § 4.4).

Chaîne exacte (aucun niveau ajouté, aucun retiré) :
  Prélèvement (matrice) → Examen (fiche ; 📄 ouvre la fiche à 3 temps en fenêtre centrée) → Diagnostic (temps 3) → Traitement (moyens et posologie)
  Les calculateurs et grilles (calculs.json, criteres.json) pendent à l'examen qui les nourrit et s'ouvrent au clic (🧮).
Bascule « par système » : les mêmes cases d'examen portent un second parent (`deSys`) ; la page choisit la vue.
Axe secondaire (discipline) : couleur de la case d'examen et filtre de la page (`disc`).
Aucun texte médical n'est rédigé ici : chaque bulle reprend mot pour mot un champ de la fiche ; un champ absent reste « à produire ».
Signature : AAI (Anthropic AI)
"""
import glob, json, os, re

MATRICES = [  # (libellé, organe d'ancrage, côté, couleur) — ordre du brief § 2
    ("Sang et buvard", "coeur", "d", "#9f1239"), ("Moelle", "femur", "g", "#7f1d1d"), ("Urines", "vessie", "d", "#a16207"),
    ("LCR", "cerveau", "g", "#6d28d9"), ("Selles", "colon", "g", "#78350f"), ("Sérosités et synovial", "foie", "g", "#0e7490"),
    ("Respiratoire et ORL", "trachee", "d", "#0369a1"), ("Génital et fœto-maternel", "bassin", "d", "#be185d"),
    ("Salive, sueur, calculs, peau", "crane", "g", "#57534e")]
MAT_DEF = {
    "Sang et buvard": "Tu prélèves du sang veineux, artériel ou capillaire, ou une goutte séchée sur papier buvard.",
    "Moelle": "Tu ponctionnes la moelle osseuse au sternum ou à la crête iliaque pour lire les lignées.",
    "Urines": "Tu recueilles les urines en milieu de jet, sur une miction ou sur 24 heures.",
    "LCR": "Tu recueilles le liquide céphalorachidien par ponction lombaire.",
    "Selles": "Tu recueilles un échantillon de selles frais, dans un pot stérile.",
    "Sérosités et synovial": "Tu ponctionnes un épanchement pleural, péritonéal ou articulaire.",
    "Respiratoire et ORL": "Tu prélèves une expectoration, un lavage bronchoalvéolaire ou un frottis de la tête et du cou.",
    "Génital et fœto-maternel": "Tu prélèves un frottis génital, du sperme, ou du sang maternel pour le fœtus.",
    "Salive, sueur, calculs, peau": "Tu recueilles la salive, la sueur, un calcul expulsé ou un prélèvement de peau et de phanères."}
SYSTEMES = [("S1", "Neurologie", "cerveau", "g"), ("S2", "Tête, cou, ORL et œil", "crane", "d"), ("S3", "Cardiovasculaire", "coeur", "d"),
            ("S4", "Respiratoire", "poumon_d", "g"), ("S5", "Digestif et hépato-bilio-pancréatique", "foie", "g"), ("S6", "Néphro-urologique", "reins", "d"),
            ("S7", "Reproduction et obstétrique", "bassin", "g"), ("S8", "Endocrino-métabolique", "pancreas", "d"), ("S9", "Appareil locomoteur", "femur", "d"),
            ("S10", "Sang et immunité", "rate", "d"), ("S11", "Psychiatrie et sommeil", "crane", "g"), ("S12", "Peau et phanères", "humerus", "g"),
            ("T", "Transversaux", "aorte", "d")]
# Axe secondaire : une couleur par discipline, hors des trois couleurs à sens fixe (bleu normal, rouge pathologie, vert traitement).
DISCIPLINES = {"Cytologie et hématologie": "#a21caf", "Hémostase": "#c2410c", "Biochimie": "#0f766e", "Immuno-hormonologie": "#6d28d9",
               "Microbiologie": "#a16207", "Pharmaco-toxicologie": "#475569"}
ROUGE, VERT, GRIS = "#b91c1c", "#15803d", "#9aa2b4"
# Calculateurs et grilles rattachés à la fiche qui fournit leurs variables (calculs.json, criteres.json) ; vérifiés à la construction.
OUTILS_FICHE = {
    "EX-1-S6-ionogramme-sodium-osmolalite": ["calc_sodium_corrige_glycemie", "crit_hyponatremie"],
    "EX-1-S6-equilibre-acide-base": ["calc_trou_anionique", "calc_trou_anionique_corrige", "calc_trou_anionique_urinaire"],
    "EX-1-S6-creatinine-dfg-uree": ["calc_ckd_epi_2021", "calc_cockcroft_gault", "calc_schwartz", "calc_fena", "calc_feun", "crit_kdigo_ira_definition", "crit_kdigo_ira_stades"],
    "EX-1-S6-ecbu": ["crit_kass_bacteriurie"],
    "EX-1-S6-proteinurie-albuminurie": ["crit_isshp_2021_preeclampsie"],
    "EX-1-S9-calcium-phosphate": ["calc_calcium_corrige"],
    "EX-1-S3-bilan-lipidique": ["calc_friedewald", "crit_syndrome_metabolique"],
    "EX-1-S3-hemocultures": ["crit_duke_iscvid_2023", "crit_sepsis_3"],
    "EX-1-S8-glycemie-hba1c": ["calc_homa_ir", "crit_iadpsg_diabete_gestationnel"],
    "EX-1-S5-bilan-hepatique-asat-alat-pal": ["calc_fib4", "calc_apri", "calc_meld_3"],
    "EX-1-S5-tp-facteur-v": ["calc_meld", "calc_meld_na"],
    "EX-1-S5-lipase": ["crit_bisap", "crit_atlanta_gravite_pancreatite"],
    "EX-1-S5-liquide-ascite": ["calc_gradient_albumine_ascite", "crit_gradient_albumine_ascite_seuil", "crit_infection_spontanee_ascite"],
    "EX-1-S4-gaz-sang-arteriels": ["calc_rapport_pao2_fio2", "crit_sdra_berlin_definition", "crit_sdra_berlin_gravite"],
    "EX-1-S4-liquide-pleural-criteres-light": ["crit_light_exsudat_pleural"],
    "EX-1-S9-liquide-synovial-cytologie-cristaux": ["crit_liquide_synovial_septique"],
    "EX-1-S9-facteur-rhumatoide-anti-ccp": ["crit_acr_eular_2010_polyarthrite"],
    "EX-1-S10-plaquettes": ["crit_4t_thrombopenie_heparine"],
    "EX-1-S10-fibrinogene-dimeres": ["crit_wells_ep", "crit_geneve_revise", "crit_perc"],
    "EX-1-S10-vitesse-sedimentation": ["crit_acr_eular_2022_acg"],
    "EX-1-S2-prelevement-gorge": ["crit_centor"],
    "EX-1-S11-bilan-etiologique-delirium": ["crit_cam_delirium"],
    "EX-1-S11-bilan-metabolique-antipsychotique": ["crit_syndrome_metabolique_seuils"],
}
AP = "à produire"


def _plein(v):
    return isinstance(v, str) and v.strip() not in ("", "—", AP)


def _txt(*vs, sep=" "):
    return sep.join(v.strip() for v in vs if _plein(v)) or None


TARIF = re.compile(r"Liste des analyses|\bpoints?\b|\b\d{4}\.\d{2}\b|\bposition", re.I)

ABREV = re.compile(r"(?:^|[\s(])(?:art|let|al|ch|cf|ex|env|resp|vol|fig|réf|p)\.$", re.I)  # « art. 13 let. b » ne coupe pas la phrase


def sans_tarif(s):
    """Retour de Vial (27.11) : les positions et points de la Liste des analyses ne servent pas l'apprenant ; on les masque à l'affichage
    (la fiche garde la donnée, contrôle de non-perte)."""
    if not isinstance(s, str):
        return s
    ph, d, c = [], 0, ""
    for i, ch in enumerate(s):  # découpe sur « . » ou « ; » + espace, hors parenthèses : une source « (OFSP … ; HUG …) » reste entière
        c += ch
        if ch == "(":
            d += 1
        elif ch == ")":
            d = max(0, d - 1)
        elif ch in ".;" and d == 0 and s[i + 1:i + 2].isspace() and not (ch == "." and ABREV.search(c)):
            ph.append(c.strip()); c = ""
    if c.strip():
        ph.append(c.strip())
    ph = [x for x in ph if not TARIF.search(x)]
    return " ".join(ph).strip() or None


def libelle_diag(s):
    """Libellé court de la case : le groupe nominal du diagnostic, sans sujet ni justification (la phrase entière reste dans la bulle)."""
    s = (s or "").strip()
    s = re.sub(r"^(?:Il|Elle|Cela|Ce tableau|Le patient|La patiente|L'enfant|Le nouveau-né)\s+(?:s'agit|a|fait|présente|souffre|signe|oriente vers|évoque|correspond à)\s+"
               r"(?:d'une?|de la|de l'|du|des|d'|à une?|vers une?|une?)?\s*", "", s, flags=re.I)
    s = re.sub(r"^On (?:retient|pose|évoque|suspecte)\s+(?:le diagnostic d[e'] ?)?(?:une?|la|le|l'|des)?\s*", "", s, flags=re.I)
    s = re.sub(r"^(?:Ce|Cette|Ces)\b.*?\b(?:oriente|orientent) vers\s+(?:une?|le|la|l'|des)?\s*", "", s, flags=re.I)
    s = re.split(r"\s*;\s*|,\s+car\s+|\s+car\s+|,\s+si\s+|\s+:\s+", s)[0]
    s = re.sub(r"\s*\([^)]*$", "", s)  # parenthèse coupée par la découpe
    s = s.rstrip(" .")
    return s[:1].upper() + s[1:] if s else s


def charger(fiches_dir):
    F = []
    for p in sorted(glob.glob(os.path.join(fiches_dir, "*", "EX-1-*.json"))):
        with open(p, encoding="utf-8") as f:
            F.append(json.load(f))
    return F


def construire(fiches_dir, noeud, court, CALC, CRIT, ecrire, developpe=None):
    """Renvoie (nœuds, outils) et écrit une fiche par examen dans donnees/biologie/<id>.json (fenêtre 📄)."""
    F = charger(fiches_dir)
    N, outils = [], {}

    def dev(s):  # brief § 6 : chaque sigle du libellé se développe (glossaire du jeu) ; le survol garde l'explication
        for _ in range(4):
            s2 = developpe(s)[0] if developpe else s
            if s2 == s:
                break
            s = s2
        return s
    mats = {m[0]: m for m in MATRICES}
    pres = {d["_matrice"] for d in F}
    for nom, mesh, cote, coul in MATRICES:
        k = sum(1 for d in F if d["_matrice"] == nom)
        N.append(noeud(f"bm_{MATRICES.index(mats[nom]) + 1}", "Prélèvement", nom, [], coul,
                       {"def": MAT_DEF[nom], "pourquoi": f"La matrice « {nom} » ouvre {k} fiche{'s' if k > 1 else ''} d'examen.",
                        "retenir": "Tu choisis la matrice, puis l'examen ; l'examen ouvre sa fiche à trois temps, puis le diagnostic et le traitement."},
                       "region", organe=mesh, cote=cote, type="Prélèvement", vue="matrice", aRediger=None if nom in pres else True))
    syspres = {d.get("systeme") for d in F}
    for code, nom, mesh, cote in SYSTEMES:
        if code not in syspres:
            continue
        k = sum(1 for d in F if d.get("systeme") == code)
        N.append(noeud(f"bs_{code}", "Système", f"{code} · {nom}", [], "#334155",
                       {"def": f"Le système « {nom} » réunit {k} fiche{'s' if k > 1 else ''} d'examen biologique.",
                        "retenir": "La vue par système range les mêmes fiches que la vue par prélèvement."},
                       "region", organe=mesh, cote=cote, type="Système", vue="systeme"))
    for d in sorted(F, key=lambda x: ([m[0] for m in MATRICES].index(x["_matrice"]), x.get("titre", ""))):
        i = d["id"]; e = d.get("entete") or {}
        disc = (d.get("axe_secondaire") or ["Biochimie"])[0]
        coul = DISCIPLINES.get(disc, "#475569")
        mi = [m[0] for m in MATRICES].index(d["_matrice"]) + 1
        eid = f"bx_{i}"
        tr = d.get("traitement")
        b = {"nom": e.get("nom_exact"), "syn": e.get("synonymes"), "prel": e.get("prelevement_conditions"),
             "usage": sans_tarif(e.get("bon_usage_suisse") or e.get("bon_usage_ch")), "disc": "Discipline : " + ", ".join(d.get("axe_secondaire") or [disc]) + "."}
        N.append(noeud(eid, "Examen", dev(d.get("titre") or e.get("nom_exact") or i), [f"bm_{mi}"], coul, {k: v for k, v in b.items() if v},
                       "bex", type=disc, maxc=60, deSys=[f"bs_{d.get('systeme')}"] if d.get("systeme") in syspres else None,
                       bioFiche=i, disc=disc, trtAProduire=True if not isinstance(tr, dict) else None))
        # calculateurs et grilles : au clic, la fenêtre du calcul s'ouvre
        for oid in OUTILS_FICHE.get(i, []):
            x = CALC.get(oid) or CRIT.get(oid)
            assert x, f"outil inconnu : {oid}"
            outils[oid] = x; calc = oid.startswith("calc_")
            N.append(noeud(f"{eid}__{oid}", "Calcul" if calc else "Critère", x["nom"], [eid], "#0f766e" if calc else "#6d28d9",
                           {"def": f"Ce calculateur exécute la formule « {x['nom']} » à partir de tes valeurs." if calc else f"Cette grille applique « {x['nom']} » élément par élément.",
                            "pourquoi": x.get("formule") or " ; ".join(x.get("elements") or []),
                            "retenir": (x.get("interpretation") or x.get("regleDeDecision") or "")[:420] or None, "source": x.get("source")},
                           "outil", type="Calcul utile" if calc else "Critère diagnostique", outil=oid, maxc=60))
        # diagnostics (temps 3) puis traitement (moyens reliés au diagnostic par l'indice t3)
        moyens = tr.get("moyens") if isinstance(tr, dict) else []
        for j, r in enumerate(d.get("temps3_interpretation") or []):
            if not isinstance(r, dict) or not _plein(r.get("diagnostic")):
                continue
            did = f"{eid}__d{j}"
            bd = {"entite": r.get("entite_anormale_chiffree"), "assoc": _txt(r.get("associees_presentes"), r.get("associees_a_rechercher")),
                  "syndrome": _txt(r.get("syndrome_anamnese"), r.get("syndrome_status")), "confirmation": r.get("confirmation"),
                  "diagnostic": r.get("diagnostic"), "conduite": r.get("conduite")}
            N.append(noeud(did, "Diagnostic", dev(libelle_diag(r["diagnostic"])), [eid], ROUGE, {k: v for k, v in bd.items() if _plein(v)}, "bdiag",
                           type="Diagnostic", maxc=90))
            lies = [m for m in moyens if isinstance(m, dict) and j in (m.get("t3") or [])]
            if not lies:
                N.append(noeud(f"{did}__trt", "Traitement", "Traitement : à produire", [did], GRIS,
                               {"general": "Le bloc Traitement de cette fiche attend sa rédaction sourcée (but, moyens, posologie, AIPS)."}, "btrt",
                               type="Traitement · à produire", aRediger=True))
            for k, m in enumerate(lies):
                bt = {"general": m.get("general"), "specifiques": m.get("specifiques"), "posologie": m.get("posologie"), "source": m.get("source")}
                lab = m.get("specifiques") if _plein(m.get("specifiques")) else m.get("general")
                N.append(noeud(f"{did}__t{k}", "Traitement", lab or "Traitement", [did], VERT, {k2: v for k2, v in bt.items() if _plein(v)}, "btrt",
                               type="Traitement", maxc=60))
        ecrire(f"biologie/{i}.json", {k: v for k, v in d.items() if k not in ("_matrice_raison",)} | {"_outils": OUTILS_FICHE.get(i, [])})
    rub = {"bex": [["nom", "Nom exact"], ["syn", "Synonymes"], ["prel", "Prélèvement et conditions"], ["usage", "Bon usage suisse"], ["disc", "Discipline"]],
           "bdiag": [["entite", "Anomalie chiffrée"], ["assoc", "Anomalies associées"], ["syndrome", "Syndrome (anamnèse · status)"],
                     ["confirmation", "Confirmation"], ["diagnostic", "Diagnostic"], ["conduite", "Conduite"]],
           "btrt": [["general", "Moyen général"], ["specifiques", "Moyens spécifiques"], ["posologie", "Posologie"], ["source", "Source"]]}
    return N, outils, rub, {"matrices": [m[0] for m in MATRICES], "disciplines": DISCIPLINES, "fiches": len(F)}
