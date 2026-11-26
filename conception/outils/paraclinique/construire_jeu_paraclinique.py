"""Jeu PARACLINIQUE livré seul (0 token) : fabrique les données de conception/prototypes/paraclinique/ à partir des sources du dépôt.

Le plan de conception (conception/html/paraclinique.html) fixe la forme :
  - Imagerie       : région → technique → examen → organe → pathologie → fenêtre à deux clichés (§ 10, X3, X4) ;
  - Biologie       : famille de prélèvements → prélèvement → (famille d'analyses) → examen → pathologie, plus calculateurs et critères (§ 10, X1, X2) ;
  - Explorations   : fonction → exploration → tracé ou diagnostic, fenêtre de tracé calculé quand le moteur en possède une (§ 10, X5) ;
  - Mode Organe    : un fichier par organe (examens de toutes modalités, anomalies élémentaires, syndromes, pathologies) (§ 8) ;
  - Pratique       : les défis jumeaux (conception/donnees/pratique/paraclinique) et les 20 cas du thorax (§ 9, § 18, § 19).
Le script ne rédige rien : il range, relie et recopie les textes déjà produits et audités. Les clichés « candidats » non validés
(conception/donnees/images) ne sont pas affichés, car aucun n'a été vérifié.
Sortie : conception/prototypes/paraclinique/donnees/*.json. Signature : AAI (Anthropic AI)"""
import glob, json, os, re, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__)); RAC = os.path.dirname(os.path.dirname(os.path.dirname(ICI)))
D = os.path.join(RAC, "conception", "donnees"); P = os.path.join(D, "paraclinique"); PR = os.path.join(D, "pratique", "paraclinique")
OUT = os.path.join(RAC, "conception", "prototypes", "paraclinique", "donnees")
lire = lambda p: json.load(open(p, encoding="utf-8"))


def ecrire(nom, obj):
    os.makedirs(os.path.dirname(os.path.join(OUT, nom)), exist_ok=True)
    json.dump(obj, open(os.path.join(OUT, nom), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))


def sans_accent(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


cle = lambda s: re.sub(r"[^a-z0-9]+", "_", sans_accent(s))[:48].strip("_")


def court(t, n=46):
    t = re.sub(r"\s*\(.*?\)", "", t or "").strip()
    return t if len(t) <= n else t[: n - 1].rsplit(" ", 1)[0] + "…"


# ---------------------------------------------------------------- organes : maillage du corps (ancre) et modèle 3D isolé (mode Organe)
REG = {"1": ("Tête et encéphale", "cerveau", "g", "#8e5cc4"), "2": ("Cou", "trachee", "d", "#2a9d8f"),
       "3": ("Rachis, moelle et racines", "rachis", "g", "#7a6a4f"), "4": ("Thorax", "poumon_d", "d", "#3d7fd6"),
       "5": ("Abdomen", "foie", "g", "#c98a2b"), "6": ("Pelvis", "vessie", "d", "#b5527a"),
       "7": ("Membres et appareil locomoteur", "femur", "g", "#5f7f3a"), "8": ("Peau et phanères", "humerus", "d", "#c0623b"),
       "9": ("Systèmes transversaux", "coeur", "g", "#6b7280")}
# Organes génitaux externes : aucun modèle isolé (occultation, plan § 2) ; le mode Organe montre alors le corps voilé.
ORG3D = {"articulation_temporo_mandibulaire_et_den": ("lo_crane_et_face", "crane"), "cavite_buccale_et_glandes_salivaires": ("dg_cavite_buccale_et_glandes_sali", "crane"),
         "encephale": ("ne_hemispheres_cerebraux", "cerveau"), "hypophyse_et_hypothalamus": ("en_hypothalamus_et_hypophyse", "cerveau"),
         "meninges_et_lcr": ("ne_meninges_et_lcr", "cerveau"), "nerfs_craniens": ("ne_nerfs_craniens", "cerveau"), "nez_sinus_et_cavum": ("rs_fosses_nasales_et_sinus", "crane"),
         "oeil_et_orbite": ("or_globe_oculaire", "crane"), "oreille_et_equilibre": ("or_oreille_interne", "crane"), "os_du_crane_et_de_la_face": ("lo_crane_et_face", "crane"),
         "ganglions_cervicaux": ("he_ganglions_lymphatiques", "trachee"), "larynx_et_pharynx": ("rs_larynx", "trachee"), "masses_cervicales_et_kystes": (None, "trachee"),
         "parathyroides": ("en_parathyroides", "trachee"), "thyroide": ("en_thyroide", "trachee"), "vaisseaux_du_cou_et_de_la_tete": ("cv_troncs_supra_aortiques", "aorte"),
         "moelle_epiniere": ("ne_moelle_epiniere", "rachis"), "queue_de_cheval_et_cone_terminal": ("ne_racines_et_plexus", "rachis"), "rachis_osseux": ("lo_rachis", "rachis"),
         "racines_et_plexus": ("ne_racines_et_plexus", "rachis"), "aorte_thoracique_et_arteres_pulmonaires": ("cv_aorte_thoracique_et_crosse", "aorte"),
         "coeur_et_pericarde": ("coe", "coeur"), "diaphragme_et_muscles_respiratoires": ("rs_diaphragme_et_muscles_respirat", "diaphragme"), "mediastin": ("en_thymus", "coeur"),
         "oesophage": ("dg_sophage", "oesophage"), "paroi_thoracique_et_cotes": ("rs_paroi_thoracique", "cage"), "plevre": ("rs_plevre", "poumon_d"),
         "poumons_et_voies_aeriennes": ("pou", "poumon_d"), "seins": ("org_gyneco_seins", "cage"), "aorte_abdominale_et_vaisseaux_digestifs": ("cv_aorte_abdominale_et_arteres_vi", "aorte"),
         "appendice": ("dg_colon", "colon"), "colon_rectum_et_anus": ("dg_colon", "colon"), "estomac_et_duodenum": ("dg_estomac", "estomac"), "foie": ("dg_foie", "foie"),
         "intestin_grele": ("dg_jejunum_et_ileon", "grele"), "pancreas": ("dg_pancreas_exocrine", "pancreas"), "paroi_abdominale_et_hernies": (None, "grele"),
         "peritoine_et_ascite": ("dg_peritoine", "grele"), "rate": ("he_rate", "rate"), "reins": ("rn_reins", "reins"), "retroperitoine": (None, "reins"),
         "surrenales": ("en_surrenales", "reins"), "ureteres": ("rn_ureteres", "reins"), "veines_caves_et_systeme_porte": ("cv_veines_caves", "foie"),
         "vesicule_et_voies_biliaires": ("dg_vesicule_et_voies_biliaires", "foie"), "grossesse_foetus_et_placenta": ("org_gyneco_placenta_et_unite_fto_placenta", "bassin"),
         "penis_et_uretre_masculin": (None, "vessie"), "plancher_pelvien": ("org_gyneco_plancher_pelvien", "bassin"), "post_partum_et_allaitement": ("org_gyneco_uterus_et_col", "bassin"),
         "prostate_et_vesicules_seminales": ("rn_prostate_et_vesicules_seminale", "vessie"), "testicules_et_scrotum": (None, "vessie"),
         "uterus_col_ovaires_et_annexes": ("org_gyneco_uterus_et_col", "bassin"), "vessie_et_uretre": ("rn_vessie", "vessie"), "vulve_vagin_et_perinee": (None, "bassin"),
         "arteres_des_membres": ("cv_arteres_des_membres", "femur"), "articulations_et_synoviale": ("lo_articulations_et_synoviale", "femur"),
         "cheville_et_pied": ("lo_cheville_et_pied", "femur"), "coude_poignet_et_main": ("lo_coude_poignet_et_main", "humerus"),
         "epaule": ("lo_ceinture_scapulaire_et_epaule", "humerus"), "genou": ("lo_genou", "femur"), "hanche_et_bassin": ("lo_bassin_et_hanche", "bassin"),
         "muscles": ("lo_muscles_stries_squelettiques", "femur"), "nerfs_peripheriques": ("ne_nerfs_peripheriques", "humerus"), "os_longs_et_squelette": ("lo_os", "femur"),
         "tendons_et_ligaments": ("lo_tendons_ligaments_et_bourses", "femur"), "veines_des_membres": ("cv_veines_des_membres", "femur"),
         "ongles_et_cheveux": ("de_annexes_ongles", "humerus"), "peau": ("de_epiderme", "humerus"), "plaies_ulceres_et_escarres": ("de_derme_et_hypoderme", "femur"),
         "corps_entier": (None, "coeur"), "croissance_et_developpement_de_l_enfant": (None, "femur"), "evaluation_geriatrique_globale": (None, "cerveau"),
         "genetique": (None, "coeur"), "infection_et_immunite": ("org_infect_organes_lymphoides_moelle_thym", "rate"),
         "metabolisme_et_endocrinologie": ("en_pancreas_endocrine", "pancreas"), "moelle_osseuse_et_ganglions": ("he_moelle_osseuse", "femur"),
         "psyche": ("org_psyche_affects_et_humeur", "cerveau"), "sang_et_hemostase": ("he_sang_globules_rouges", "coeur"),
         "sommeil_et_vigilance": ("org_psyche_sommeil_et_vigilance", "cerveau"), "systeme_lymphatique": ("cv_systeme_lymphatique", "rate"),
         "toxicologie_et_medicaments": (None, "foie"), "urgences_et_point_of_care": (None, "coeur")}
IDX3D = lire(os.path.join(RAC, "conception", "prototypes", "moteur", "anatomie3d", "index.json"))["organes"]

ORGANES = []  # {stem, nom, region, couleur, fichier, examens}
for f in sorted(glob.glob(os.path.join(P, "topographie", "*", "*.json"))):
    rd = os.path.basename(os.path.dirname(f)); stem = os.path.basename(f)[:-5]; d = lire(f)
    a3d, mesh = ORGANES_MAP = ORG3D.get(stem, (None, REG[rd[0]][1]))
    if a3d and a3d not in IDX3D:
        a3d = None
    ORGANES.append({"stem": stem, "nom": d["_meta"]["organe"], "region": rd[0], "regionNom": REG[rd[0]][0], "couleur": REG[rd[0]][3],
                    "a3d": a3d, "mesh": mesh, "examens": d.get("examens", []), "glossaire": d.get("glossaire", {})})
EXID = {e["id"]: (o, e) for o in ORGANES for e in o["examens"]}

# ---------------------------------------------------------------- glossaire unique (infobulle de définition sur chaque sigle)
GLO = {}
for p in [os.path.join(D, "glossaire_sigles.json")] + glob.glob(os.path.join(P, "**", "*.json"), recursive=True):
    try:
        g = lire(p)
    except Exception:
        continue
    src = g if p.endswith("glossaire_sigles.json") else (g.get("glossaire") if isinstance(g, dict) else None)
    for k, v in (src or {}).items():
        if k != "_meta" and isinstance(v, str) and 1 < len(k) <= 24 and v.strip():
            GLO.setdefault(k, v.strip())

RUB = {"region": [["def", "Ce que c'est"], ["pourquoi", "Pourquoi ici"], ["confusion", "Confusion possible"], ["retenir", "À retenir"]],
       "examen": [["def", "Ce que c'est"], ["pourquoi", "Pourquoi ici"], ["confusion", "Confusion possible"], ["retenir", "À retenir"],
                  ["signe", "Signe recherché"], ["seuil", "Seuil"], ["discriminant", "Pourquoi lui"], ["avantage", "Avantage sélectif"],
                  ["plutot", "Plutôt que"], ["limite", "Limite"], ["smarter", "Smarter Medicine"], ["visees", "Visées du bilan"]],
       "patho": [["def", "Ce que c'est"], ["signe", "Anomalie typique"], ["syndrome", "Syndrome paraclinique"], ["retenir", "À retenir"]],
       "trace": [["def", "Ce que c'est"], ["seuil", "Seuil"], ["retenir", "À retenir"]],
       "outil": [["def", "Ce que c'est"], ["formule", "Formule"], ["retenir", "À retenir"], ["source", "Source"]]}


VIS = {"diagnostique": "diagnostique", "etiologique": "étiologique", "therapeutique": "thérapeutique", "retentissement": "retentissement",
       "complications": "complications", "sortie": "sortie"}


def bulle_examen(e):
    b = e.get("bulle") or {}
    r = {"def": b.get("def") or f"L'examen « {e['nom']} » attend encore sa fiche rédigée.", "pourquoi": b.get("pourquoi"), "confusion": b.get("confusion"),
         "retenir": b.get("retenir"), "signe": e.get("signeRecherche"), "seuil": e.get("seuil"), "discriminant": e.get("discriminant"),
         "avantage": e.get("avantageSelectif"), "plutot": e.get("plutotQue"), "limite": e.get("limite"), "smarter": e.get("smarterMedicine"),
         "visees": ("L'examen sert la visée " + ", ".join(VIS.get(x, x) for x in e["visees"]) + " du bilan.") if e.get("visees") else None}
    return {k: v for k, v in r.items() if v}


def bulle_patho(p, e):
    """Pathologie vue par un examen : le texte vient de la fiche de l'examen (anomalie typique, syndrome qui la contient)."""
    an = p.get("anomalieTypique") or ""
    syn = next((s for s in e.get("syndromesParacliniques") or [] if any(sans_accent(a)[:14] in sans_accent(an) or sans_accent(an)[:14] in sans_accent(a)
                                                                         for a in s.get("anomaliesQuiLeComposent") or [])), None)
    sig = next((a.get("signification") for a in e.get("anomaliesElementaires") or [] if sans_accent(a.get("anomalie", ""))[:14] in sans_accent(an)
                or sans_accent(an)[:14] in sans_accent(a.get("anomalie", ""))), None)
    r = {"def": f"La pathologie « {p['pathologie']} » se recherche ici par l'examen « {court(e['nom'], 60)} ».",
         "signe": f"L'examen montre typiquement : {an[0].lower() + an[1:] if an else 'une anomalie non précisée'}.",
         "syndrome": (f"Cette anomalie appartient au syndrome « {syn['syndrome']} », qui réunit : " + ", ".join(syn["anomaliesQuiLeComposent"]).lower() + ".") if syn else None,
         "retenir": sig}
    return {k: v for k, v in r.items() if v}


def visees(e):
    return "Examen"


def noeud(id_, nature, texte, de, couleur, bulle, rub, **kw):
    n = {"id": id_, "nature": nature, "type": kw.pop("type", nature), "texte": court(texte), "de": de, "couleur": couleur, "rubriques": rub, "bulle": bulle}
    n.update({k: v for k, v in kw.items() if v is not None})
    return n


def accroche_pathos(N, pid, e, coul, lim=7):
    for p in (e.get("pathologiesAssociees") or [])[:lim]:
        nid = f"{pid}__{cle(p['pathologie'])}"
        if not any(x["id"] == nid for x in N):
            N.append(noeud(nid, "Pathologie", p["pathologie"], [pid], "#c2410c", bulle_patho(p, e), "patho", exRef=e["id"]))


# ---------------------------------------------------------------- 1. IMAGERIE : région → technique → examen → organe → pathologie
TECH = [("Médecine nucléaire", r"scintig|\bpet\b|pet-|tep|spect|datscan|i(ode)? ?131"),
        ("Angiographie", r"art[ée]riograph|angiograph|coronarograph|phl[ée]bograph|\bdsa\b|cavograph|lymphograph"),
        ("IRM", r"\birm|angio-irm|cholangio-irm|ent[ée]ro-irm|sialo-irm|spectroscopie|neurograph"),
        ("Scanner (CT)", r"\bct\b|ct |-ct|scanner|cone beam|tomodensito|colo-ct|uro-ct|myélo-ct|arthro-ct"),
        ("Échographie et Doppler", r"[ée]cho|doppler|[ée]lastograph|pocus|efast|fibroscan"),
        ("Radiographie", r"radiograph|radioscop|mammograph|tomosynth|orthopantomo|ost[ée]odensito|dxa|eos|transit|d[ée]f[ée]cograph|hyst[ée]ro|cystograph|ur[ée]t[ée]ro|ur[ée]trograph|[âa]ge osseux|bilan radiologique|clich"),
        ("Autres imageries", r".")]
TECHC = {"Radiographie": "#4b5563", "Échographie et Doppler": "#0f766e", "Scanner (CT)": "#1d4ed8", "IRM": "#7c3aed", "Médecine nucléaire": "#b45309",
         "Angiographie": "#be123c", "Autres imageries": "#64748b"}
TECHB = {k: v for k, v in [(r["Technique"] if False else None, None) for r in []]}


def technique(nom):
    s = sans_accent(nom)
    for t, rx in TECH:
        if re.search(sans_accent(rx), s):
            return t


DISC = {}  # plan § 11 : facteur discriminant de chaque technique (texte repris du plan, chapitre « Choisir l'examen »)
DISC_PLAN = {"Radiographie": ("Elle montre les contrastes os, air et tissus mous : fractures, pneumothorax, condensation, pneumopéritoine.",
                              "Tu la préfères quand tu veux une réponse immédiate, peu irradiante, au lit du malade.",
                              "Elle superpose les plans et voit mal les tissus mous."),
             "Échographie et Doppler": ("Elle montre les interfaces liquide et solide, et le Doppler mesure le sens et la vitesse du flux.",
                                        "Tu la préfères sans irradiation, au lit, chez l'enfant ou la femme enceinte, et pour chercher une thrombose ou une sténose.",
                                        "Elle dépend de l'opérateur, et l'air ou l'os l'arrêtent."),
             "Scanner (CT)": ("Il montre le sang frais, les calcifications, l'os et, injecté, les organes pleins et les vaisseaux.",
                              "Tu le préfères en urgence pour une hémorragie, une lithiase, une embolie ou un bilan d'extension.",
                              "Il irradie et, injecté, il exige un rein fonctionnel et expose au produit iodé."),
             "IRM": ("Elle distingue finement les tissus mous selon la séquence : T1, T2, FLAIR, diffusion, gadolinium.",
                     "Tu la préfères pour le cerveau, la moelle, les articulations, le pelvis ou pour éviter les rayons.",
                     "Elle est longue, moins disponible, et certains implants la contre-indiquent."),
             "Médecine nucléaire": ("Elle montre la fonction d'un tissu : fixation, perfusion, métabolisme du glucose ou cible moléculaire.",
                                    "Tu la préfères quand la question porte sur la fonction plutôt que sur l'anatomie.",
                                    "Sa résolution spatiale reste faible et plusieurs tissus fixent normalement le traceur."),
             "Angiographie": ("Elle opacifie la lumière des vaisseaux et permet souvent un geste dans le même temps.",
                              "Tu la préfères quand un traitement endovasculaire est probable.",
                              "Elle est invasive : on la réserve après l'imagerie en coupe non invasive."),
             "Autres imageries": ("Elle regroupe des imageries de surface ou spécialisées : OCT, dermatoscopie, photographie.",
                                  "Tu la choisis quand l'organe se voit directement ou par une optique dédiée.",
                                  "Elle ne renseigne que sur la structure qu'elle vise.")}

CAS_CLICHE = lire(os.path.join(RAC, "conception", "prototypes", "moteur", "paraclinique.json"))["fenetres"][0]

N = []
for r, (rnom, mesh, cote, coul) in REG.items():
    orgs = [o for o in ORGANES if o["region"] == r]
    exs = [(o, e) for o in orgs for e in o["examens"] if e["modalite"] == "Imagerie"]
    if not exs:
        continue
    rid = f"im_r{r}"
    techs = []
    for o, e in exs:
        t = technique(e["nom"])
        if t not in techs:
            techs.append(t)
    techs.sort(key=lambda t: [x[0] for x in TECH].index(t) if t != "Radiographie" else -1)
    N.append(noeud(rid, "Région", rnom, [], coul, {"def": f"La région « {rnom} » s'explore par {len(exs)} examens d'imagerie, répartis en {len(techs)} techniques.",
                                                   "pourquoi": "Tu pars de la région parce que l'imagerie se demande pour une zone du corps, puis tu choisis la technique qui répond à ta question.",
                                                   "retenir": "Tu cliques une technique, puis l'examen, l'organe et la pathologie : la fenêtre à deux clichés s'ouvre quand le cliché réel existe."},
                   "region", organe=mesh, cote=cote, type="Région"))
    for t in techs:
        tid = f"{rid}_{cle(t)}"; dv, pq, lm = DISC_PLAN[t]
        N.append(noeud(tid, "Technique", t, [rid], TECHC[t], {"def": dv, "pourquoi": pq, "confusion": lm,
                                                             "retenir": "Le chapitre 11 du plan donne pour chaque technique ce qu'elle voit le mieux, ce qu'elle remplace et sa limite."},
                       "region", type="Technique"))
        vus = {}
        for o, e in exs:
            if technique(e["nom"]) != t:
                continue
            k = cle(court(e["nom"], 80))
            eid = f"{tid}__{k}"
            if eid not in vus:
                vus[eid] = True
                N.append(noeud(eid, "Examen", e["nom"], [tid], TECHC[t], bulle_examen(e), "examen", type=visees(e),
                               exRef=e["id"], fiche=o["stem"]))
            oid = f"{eid}__{o['stem'][:30]}"
            N.append(noeud(oid, "Organe", o["nom"], [eid], coul, {k2: v for k2, v in {"def": f"L'examen explore ici l'organe « {o['nom']} ».",
                                                                                        "signe": e.get("signeRecherche"), "seuil": e.get("seuil"),
                                                                                        "retenir": e.get("indication")}.items() if v},
                           "examen", type="Organe", exRef=e["id"], fiche=o["stem"]))
            accroche_pathos(N, oid, e, coul)
            if o["stem"] == "poumons_et_voies_aeriennes" and t == "Radiographie":
                pn = next((n for n in N if n["de"] == [oid] and "pneumonie" in n["id"]), None)
                if pn:
                    pn["cliches"] = {k2: CAS_CLICHE[k2] for k2 in ("titre", "img", "annotations", "normal")}
                    pn["cliches"]["img"] = "../moteur/" + CAS_CLICHE["img"]; pn["cliches"]["normal"] = dict(CAS_CLICHE["normal"], img="../moteur/" + CAS_CLICHE["normal"]["img"])
                    CAS_PNEU = lire(os.path.join(P, "imagerie", "cas", "pneumonie_lobaire_moyenne.json"))
                    pn["cliches"]["diagnostic"] = CAS_PNEU["diagnostic"] + " : une opacité alvéolaire nouvelle efface le bord droit du cœur (signe de la silhouette)."
                    pn["cliches"]["conduite"] = "Tu évalues la gravité par le score CURB-65 (grille des critères), puis tu traites selon les recommandations de la Société suisse d'infectiologie (SSI)."
                    pn["cliches"]["source"] = "Cliché du patient : " + CAS_PNEU["clicheBrut"]["url"] + " ; cliché normal : " + CAS_CLICHE["normal"]["source"] + "."
IMG = N

# ---------------------------------------------------------------- 2. BIOLOGIE : famille de prélèvements → prélèvement → (famille d'analyses) → examen → pathologie
PREL = {p: lire(os.path.join(P, "biologie", "prelevements", p + ".json")) for p in
        [os.path.basename(x)[:-5] for x in glob.glob(os.path.join(P, "biologie", "prelevements", "*.json"))]}
PNOM = {"sang_veineux": "Sang veineux", "sang_arteriel": "Sang artériel", "sang_capillaire": "Sang capillaire", "hemocultures": "Hémocultures",
        "moelle_osseuse": "Moelle osseuse", "urine": "Urine", "liquide_cephalorachidien": "Liquide céphalorachidien", "liquide_pleural": "Liquide pleural",
        "liquide_pericardique": "Liquide péricardique", "liquide_d_ascite": "Liquide d'ascite", "liquide_synovial": "Liquide synovial",
        "ponction_de_kyste_d_abces_ou_de_collecti": "Ponction de kyste, d'abcès ou de collection", "liquide_amniotique": "Liquide amniotique",
        "selles": "Selles", "expectorations_et_lavage_bronchoalveolai": "Expectorations et lavage bronchoalvéolaire",
        "ecouvillons_nasopharynges_et_de_gorge": "Écouvillons nasopharyngés et de gorge", "air_expire": "Air expiré",
        "prelevements_genitaux_et_uretraux": "Prélèvements génitaux et urétraux", "sperme": "Sperme", "biopsies_tissulaires": "Biopsies tissulaires",
        "sueur": "Sueur", "salive": "Salive", "cheveux_et_ongles": "Cheveux et ongles"}
FAM = [("bs", "Sang", "coeur", "d", "#b91c1c", ["sang_veineux", "sang_arteriel", "sang_capillaire", "hemocultures", "moelle_osseuse"]),
       ("bl", "Liquide céphalorachidien", "cerveau", "g", "#7c3aed", ["liquide_cephalorachidien"]),
       ("bp", "Liquides des séreuses et des articulations", "poumon_g", "d", "#0e7490", ["liquide_pleural", "liquide_pericardique", "liquide_d_ascite", "liquide_synovial", "ponction_de_kyste_d_abces_ou_de_collecti"]),
       ("br", "Voies respiratoires et air expiré", "trachee", "g", "#2563eb", ["expectorations_et_lavage_bronchoalveolai", "ecouvillons_nasopharynges_et_de_gorge", "air_expire"]),
       ("bt", "Tissus", "foie", "g", "#a16207", ["biopsies_tissulaires"]),
       ("bd", "Selles", "colon", "g", "#92400e", ["selles"]),
       ("bu", "Urine", "vessie", "d", "#ca8a04", ["urine"]),
       ("bg", "Prélèvements génitaux et obstétricaux", "bassin", "d", "#be185d", ["prelevements_genitaux_et_uretraux", "sperme", "liquide_amniotique"]),
       ("bc", "Peau, phanères et sécrétions", "humerus", "d", "#c0623b", ["sueur", "salive", "cheveux_et_ongles"])]
REGLES_P = [("liquide_cephalorachidien", r"\blcr\b|c[ée]phalorachid|ponction lombaire"), ("liquide_pleural", r"pleural"), ("liquide_d_ascite", r"ascite"),
            ("liquide_synovial", r"synovial|ponction articulaire|ponction de hanche|ponction du 1er|bursal"), ("liquide_pericardique", r"p[ée]ricardique"),
            ("liquide_amniotique", r"amnio|liquide amniotique|choriocent"), ("sang_arteriel", r"gazom[ée]trie|gaz du sang"), ("hemocultures", r"h[ée]moculture"),
            ("urine", r"urin|bandelette|uroculture|uricult|calciurie|diur|ecbu|natriur|premier jet"), ("selles", r"selles|f[ée]cal|coproculture|clostrid|parasitolog"),
            ("air_expire", r"test respiratoire|feno|air expir"), ("ecouvillons_nasopharynges_et_de_gorge", r"[ée]couvillon|nasopharyng|frottis de gorge|streptocoque a|pcr respiratoire"),
            ("expectorations_et_lavage_bronchoalveolai", r"expector|lavage bronch|\blba\b"), ("sperme", r"sperm"),
            ("prelevements_genitaux_et_uretraux", r"vaginal|cervical|\bhpv\b|ur[ée]tral|chlamydia|gonocoque|mycoplasma"), ("sueur", r"sueur"),
            ("salive", r"saliv"), ("cheveux_et_ongles", r"mycolog|ungu[ée]al|cheveu|capillaire \(tox|toxicologie capillaire"),
            ("moelle_osseuse", r"my[ée]logramme|ost[ée]om[ée]dullaire|moelle"), ("sang_capillaire", r"glyc[ée]mie capillaire|hemocue|guthrie"),
            ("ponction_de_kyste_d_abces_ou_de_collecti", r"abc[eè]s|\bpus\b|kyste|collection|pr[ée]l[èe]vement profond|plaie|chambre ant|otorrh"),
            ("biopsies_tissulaires", r"biopsie|cytoponction|histolog|immunohisto")]


def prelevement_de(e):
    s = sans_accent(e["nom"])
    for p, rx in REGLES_P:
        if re.search(sans_accent(rx), s):
            return p
    ref = e.get("prelevementRef")
    if ref:
        for p in PNOM:
            if p.startswith(ref[:30]):
                return p
    return "sang_veineux"


IDX = lire(os.path.join(D, "recherche", "index.json"))
ANAB = {a["nom"]: a for f in glob.glob(os.path.join(P, "biologie", "analyses", "*.json")) for a in lire(f)["analyses"] if a.get("bulle")}
ANA = []  # (nom normalisé, famille) : les 15 fichiers d'analyses rangent chaque analyse dans sa famille
for f in sorted(glob.glob(os.path.join(P, "biologie", "analyses", "*.json"))):
    fam = re.sub(r"^\d+_", "", os.path.basename(f)[:-5]).replace("_", " ").capitalize()
    for a in lire(f)["analyses"]:
        for nm in [a["nom"]] + (a.get("synonymes") or []):
            k = sans_accent(re.sub(r"\s*\(.*?\)", "", nm)).strip()
            if len(k) >= 3:
                ANA.append((k, fam))
ANA.sort(key=lambda x: -len(x[0]))


def famille_analyse(nom):
    s = " " + sans_accent(nom) + " "
    for k, fam in ANA:
        if re.search(r"(?<![a-z0-9])" + re.escape(k) + r"(?![a-z0-9])", s):
            return fam
    for rx, fam in ((r"s[ée]rolog|interf[ée]ron|mononucl|antig[eè]n|cryptocoque|l[ée]gionelle", "Inflammation infection microbiologie"),
                    (r"tropon|\bck\b|lipid", "Cardiaque vasculaire lipides"), (r"\bfsc\b|groupe sanguin|immunoph[ée]notyp|h[ée]mogramme", "Hematologie"),
                    (r"coagulation|willebrand", "Hemostase"), (r"toxicolog|dosage|alcool|[ée]thanol|psychotrope", "Toxicologie dosages medicamenteux"),
                    (r"g[ée]n[ée]ti|exome|g[ée]nome", "Genetique"), (r"\big[gam]\b|tryptase|immunofluorescence", "Immunologie autoimmunite allergie"),
                    (r"gastrin", "Surrenales gonades hypophyse neuroendocrine"), (r"fib-4|meld|child", "Foie pancreas digestif")):
        if re.search(rx, s):
            return fam
    return None
FAMN = {"Hematologie": "Hématologie", "Hemostase": "Hémostase", "Electrolytes rein acide-base": "Électrolytes, rein et acide-base",
        "Foie pancreas digestif": "Foie, pancréas et digestif", "Cardiaque vasculaire lipides": "Cœur, vaisseaux et lipides",
        "Diabete thyroide phosphocalcique": "Diabète, thyroïde et phosphocalcique", "Inflammation infection microbiologie": "Inflammation et infection",
        "Immunologie autoimmunite allergie": "Immunologie, auto-immunité et allergie", "Marqueurs tumoraux": "Marqueurs tumoraux",
        "Toxicologie dosages medicamenteux": "Toxicologie et dosages", "Urines": "Urines", "Genetique": "Génétique",
        "Microbiologie prelevements locaux": "Microbiologie locale", "Lcr liquides de ponction": "LCR et liquides de ponction",
        "Surrenales gonades hypophyse neuroendocrine": "Hormonologie"}
CALC = {e["id"]: e for e in lire(os.path.join(P, "calculs.json"))["elements"]}
CRIT = {e["id"]: e for e in lire(os.path.join(P, "criteres.json"))["elements"]}
OUTILS = {"sang_veineux": ["calc_trou_anionique", "calc_trou_anionique_corrige", "calc_sodium_corrige_glycemie", "calc_calcium_corrige", "calc_ckd_epi_2021",
                           "calc_cockcroft_gault", "calc_friedewald", "calc_homa_ir", "calc_fib4", "calc_apri", "crit_hyponatremie", "crit_kdigo_ira_definition"],
          "sang_arteriel": ["calc_rapport_pao2_fio2", "crit_sdra_berlin_gravite"], "urine": ["calc_fena", "calc_feun", "calc_trou_anionique_urinaire"],
          "liquide_pleural": ["crit_light_exsudat_pleural"], "liquide_d_ascite": ["calc_gradient_albumine_ascite", "crit_gradient_albumine_ascite_seuil"]}

N = []
parP = {}
for o in ORGANES:
    for e in o["examens"]:
        if e["modalite"] == "Biologie":
            parP.setdefault(prelevement_de(e), []).append((o, e))
for fid, fnom, mesh, cote, coul, prels in FAM:
    rid = f"bi_{fid}"; nb = sum(len(parP.get(p, [])) for p in prels)
    N.append(noeud(rid, "Famille", fnom, [], coul, {"def": f"Cette famille regroupe {len(prels)} prélèvement(s) et {nb} examens biologiques reliés aux organes.",
                                                  "pourquoi": "Tu pars du prélèvement parce que le geste, le tube et le transport décident de la fiabilité du résultat.",
                                                  "retenir": "La chaîne va du prélèvement à l'examen, puis à l'interprétation, au syndrome biologique et au diagnostic."},
                   "region", organe=mesh, cote=cote, type="Famille"))
    for p in prels:
        pid = f"{rid}_{p[:24]}"; liste = parP.get(p, []); pj = PREL.get(p, {})
        noms_j = [x["nom"] for x in pj.get("examens", [])]
        N.append(noeud(pid, "Prélèvement", PNOM[p], [rid], coul, {"def": f"Le prélèvement « {PNOM[p]} » sert {len(liste)} examens reliés aux organes du catalogue.",
                                                                   "pourquoi": ("Sa fiche technique liste : " + ", ".join(noms_j[:8]) + ("…" if len(noms_j) > 8 else "") + ".") if noms_j else None,
                                                                   "retenir": "Tu cliques le prélèvement, puis l'examen : l'infobulle donne le signe recherché, le seuil et ce qui le fait préférer."} ,
                       "region", type="Prélèvement"))
        groupes = {}
        for o, e in liste:
            g = FAMN.get(famille_analyse(e["nom"]) or "", "Autres analyses") if len(liste) > 14 else None
            groupes.setdefault(g, []).append((o, e))
        for g, items in sorted(groupes.items(), key=lambda kv: (kv[0] is None, kv[0] or "")):
            parent = pid
            if g:
                parent = f"{pid}__{cle(g)}"
                N.append(noeud(parent, "Famille d'analyses", g, [pid], coul, {"def": f"La famille « {g} » regroupe {len(items)} examens de ce prélèvement.",
                                                                              "retenir": "Les familles suivent les 15 fichiers d'analyses, source unique des valeurs SI."}, "region", type="Analyses"))
            vus = set()
            for o, e in items:
                eid = f"{parent}__{cle(court(e['nom'], 80))}"
                if eid in vus:
                    continue
                vus.add(eid)
                N.append(noeud(eid, "Examen", e["nom"], [parent], coul, bulle_examen(e), "examen", type=visees(e),
                               exRef=e["id"], fiche=o["stem"]))
                accroche_pathos(N, eid, e, coul, 6)
        # Examens de la fiche technique du prélèvement absents du catalogue des organes : la bulle vient de l'analyse liée, si elle est rédigée.
        deja = {cle(court(e["nom"], 80)) for _, e in liste}
        for x in pj.get("examens", []):
            if cle(court(x["nom"], 80)) in deja:
                continue
            a = next((ANAB[r_] for r_ in x.get("analysesRef") or [] if r_ in ANAB), None)
            b = dict(a["bulle"]) if a else {"def": f"L'examen « {x['nom']} » figure dans la fiche technique du prélèvement ; sa fiche d'interprétation reste à rédiger."}
            if a and a.get("seuilsCritiques"):
                b["seuil"] = a["seuilsCritiques"]
            N.append(noeud(f"{pid}__fp_{cle(court(x['nom'], 80))}", "Examen", x["nom"], [pid], coul if a else "#9aa2b4", b, "examen",
                           type="Analyse", aRediger=None if a else True))
        for oid in OUTILS.get(p, []):
            x = CALC.get(oid) or CRIT.get(oid)
            if not x:
                continue
            calc = oid.startswith("calc_")
            b = {"def": (f"Ce calculateur exécute la formule « {x['nom']} » à partir de tes valeurs." if calc else f"Cette grille applique « {x['nom']} » élément par élément."),
                 "formule": x.get("formule") or " ; ".join(x.get("elements") or []), "retenir": (x.get("interpretation") or x.get("regleDeDecision") or "")[:420],
                 "source": x.get("source")}
            N.append(noeud(f"{pid}__{oid}", "Calcul" if calc else "Critère", x["nom"], [pid], "#0f766e" if calc else "#6d28d9", {k: v for k, v in b.items() if v},
                           "outil", type="Calculateur" if calc else "Critère diagnostique", outil=oid))
BIO = N

# ---------------------------------------------------------------- 3. EXPLORATIONS FONCTIONNELLES : fonction → exploration → tracé / diagnostic
FONC = [("fm", "Endocrinien et métabolique", "pancreas", "g", "#a16207", r"hgpo|synacth|dexam[ée]thasone|charge sod|restriction hydrique|arginine|hypoglyc[ée]mie insulin|je[ûu]ne de 72|cortisol|veines surr[ée]nal|calorim|holter glyc|mesure continue du glucose|croissance|tanner"),
        ("fs", "Sommeil et vigilance", "cerveau", "d", "#4338ca", r"sommeil|polygraph|polysomno|tile|latence d.endormissement|maintien de l.[ée]veil|actim[ée]trie|epworth"),
        ("fu", "Urinaire, pelvien et obstétrical", "vessie", "d", "#ca8a04", r"urodynam|d[ée]bitm|calendrier mictionnel|pad-test|r[ée]sidu post|cardiotoco|[ée]rection|sensibilit[ée] p[ée]rin|epds|debout et en toux"),
        ("fe", "Électrique et hémodynamique du cœur", "coeur", "g", "#b91c1c", r"\becg\b|holter|pacemaker|d[ée]fibrill|loop|enregistreur|[ée]lectrophysiolog|effort|tilt|sinus carotidien|cath[ée]t[ée]risme cardiaque|mapa"),
        ("fr", "Respiratoire", "poumon_d", "d", "#2563eb", r"spirom|pl[ée]thysmo|dlco|diffusion du co|gazom|peak|feno|pimax|methacholine|m[ée]thacholine|provocation bronchique|ergospiro|marche de 6|capnograph|oxym[ée]trie"),
        ("fn", "Neurologique et neuromusculaire", "cerveau", "g", "#7c3aed", r"\beeg\b|eeg |vid[ée]o-eeg|enmg|[ée]lectromyograph|[ée]lectroneuromyo|potentiels [ée]voqu|nerfs cr[âa]niens|pression intracr|doppler transcr|blink|autonomes|schober"),
        ("fo", "Neurosensoriel : œil, oreille, nez, goût", "crane", "d", "#0e7490", r"acuit|r[ée]fraction|lampe [àa] fente|\btonom|dentaire|pachym|gonio|fond d.oeil|fond d.œil|champ visuel|ishihara|couleurs|[ée]lectror[ée]tino|schirmer|audiom|tympano|otoscop|oto[ée]mission|nystagmo|vhit|head impulse|vemp|hallpike|olfacto|gustom|rhinomano|d[ée]pistage auditif"),
        ("fd", "Digestif", "estomac", "g", "#92400e", r"manom[ée]trie|ph-m[ée]trie|imp[ée]dancem|transit colique|s[ée]cr[ée]tine|gradient de pression h[ée]patique|d[ée]glutition|salivaire|sialom"),
        ("fv", "Vasculaire et locomoteur", "femur", "d", "#15803d", r"pression systolique|\bips\b|tcpo2|pression d.orteil|marche sur tapis|capillaro|monofilament|thompson|lachman|tiroir|mcmurray|ligamentaire|sous-acromial|wells|perc|tietze|palpation"),
        ("fp", "Peau et allergie", "humerus", "d", "#c0623b", r"prick|patch|[ée]picutan|lampe de wood|phototest|tricho|braden|provocation \(m"),
        ("fc", "Cognitif, psychométrique et gériatrique", "cerveau", "g", "#be185d", r"neuropsycho|moca|mini-cog|psychom[ée]tri|personnalit|adl|iadl|\bmna\b|nutritional|gds|g[ée]riatrique|timed up|tinetti|denver|d[ée]veloppement|beers|m[ée]dication|glasgow"),
        ("fh", "Hémostase au lit du malade", "coeur", "d", "#9f1239", r"pfa-100|saignement|rotem|thrombo[ée]lasto"),
        ("fx", "Vision directe : endoscopie", "oesophage", "d", "#475569", r"scopie|endoscop|ebus|eus|cpre|vid[ée]ocapsule|ent[ée]roscop|cœlioscop|coelioscop|laparoscop|m[ée]diastinoscop|cholangioscop|stroboscop")]
EXPL = {os.path.basename(f)[:-5]: lire(f) for f in glob.glob(os.path.join(P, "explorations", "*.json"))}
FEN = [(r"spirom", "spiro"), (r"\becg\b|holter", "ecg"), (r"gazom", "gazometrie"), (r"pression systolique|\bips\b", "ips"), (r"audiom", "or_audio"),
       (r"tonom", "or_pio"), (r"r[ée]fraction|acuit", "or_refraction"), (r"enmg|[ée]lectroneuromyo|vitesses de conduction", "ne_conduction"),
       (r"hgpo|mesure continue du glucose|holter glyc", "en_glycemie"), (r"synacth|dexam[ée]thasone|cortisol", "en_cortisol"), (r"restriction hydrique|arginine", "en_adh"),
       (r"cath[ée]t[ée]risme cardiaque droit", "hemodyn"), (r"pression intracr", "ne_ppc"), (r"glasgow", "ne_glasgow"), (r"dlco|diffusion du co", "alveolaire"),
       (r"rotem|thrombo[ée]lasto|pfa-100", "he_coag"), (r"gradient de pression h[ée]patique", "porte"), (r"[ée]preuve d.effort", "pa")]
SOUS = {"fx": [("Endoscopie digestive haute et biliopancréatique", r"gastro|oesophag|œsophag|cpre|cholangio|biliopancr|ent[ée]roscop|vid[ée]ocapsule|[ée]cho-endoscopie$|avec ponction"),
               ("Endoscopie digestive basse", r"colo|recto|anuscop|rectale"),
               ("Endoscopie respiratoire et médiastinale", r"bronch|ebus|m[ée]diastino|thoracoscop"),
               ("Endoscopie ORL", r"laryng|naso|rhinoscop|stroboscop|panendoscop"),
               ("Endoscopie urologique et gynécologique", r"cysto|ur[ée]t[ée]roscop|hyst[ée]roscop|colposcop|vulvoscop"),
               ("Cœlioscopie et arthroscopie", r".")],
        "fo": [("Œil et vision", r"acuit|r[ée]fraction|lampe|tonom|pachym|gonio|fond d|champ visuel|ishihara|couleurs|r[ée]tino|schirmer"),
               ("Oreille et équilibre", r"audiom|tympano|otoscop|oto[ée]mission|nystagmo|head impulse|vhit|vemp|hallpike|auditif"),
               ("Nez, goût et bouche", r".")],
        "fn": [("Électroencéphalographie", r"eeg"), ("Nerf et muscle", r"enmg|[ée]lectromyo|[ée]lectroneuro|blink|autonomes"),
               ("Potentiels évoqués", r"potentiels"), ("Examens cliniques et pressions", r".")]}
fx_exs = {}
for o in ORGANES:
    for e in o["examens"]:
        if e["modalite"] in ("Exploration fonctionnelle", "Endoscopie"):
            fx_exs.setdefault(e["id"].split("__", 1)[1], []).append((o, e))
N = []
for fid, fnom, mesh, cote, coul, rx in FONC:
    N.append(noeud(f"fx_{fid}", "Fonction", fnom, [], coul, None, "region", organe=mesh, cote=cote, type="Fonction"))
cnt = {}
for slug in sorted(set(fx_exs) | set(k for k in EXPL if len(EXPL[k].get("elements", [])) == 1)):
    paires = fx_exs.get(slug, []); o, e = paires[0] if paires else (None, None)
    nom = e["nom"] if e else slug.replace("_", " ").capitalize()
    s = sans_accent(nom)
    fid = next((f[0] for f in FONC if f[0] != "fx" and re.search(sans_accent(f[5]), s)), None)
    if (e and e["modalite"] == "Endoscopie") or (not fid and re.search(sans_accent(FONC[-1][5]), s)):
        fid = "fx"
    fid = fid or "fc"
    el = (EXPL.get(slug) or {}).get("elements") or [{}]
    el = el[0] if len(el) == 1 else {}
    b = bulle_examen(e) if e else {"def": el.get("fonction") or f"L'exploration « {nom} » attend sa fiche."}
    if el.get("fonction") and "def" not in (e or {}).get("bulle", {}) :
        b["def"] = el["fonction"]
    fen = next((w for r_, w in FEN if re.search(sans_accent(r_), s)), None)
    xid = f"fx_{fid}__{slug[:40]}"; coulf = next(f[4] for f in FONC if f[0] == fid)
    cnt[fid] = cnt.get(fid, 0) + 1
    parent = f"fx_{fid}"
    if fid in SOUS:
        sg = next((g for g, r_ in SOUS[fid] if re.search(sans_accent(r_), s)), SOUS[fid][-1][0])
        parent = f"fx_{fid}_{cle(sg)}"
        if not any(n["id"] == parent for n in N):
            N.append(noeud(parent, "Groupe", sg, [f"fx_{fid}"], coulf, {"def": f"Ce groupe réunit les explorations « {sg.lower()} ».",
                                                                       "retenir": "Tu ouvres le groupe, puis l'exploration dont tu veux le tracé et l'interprétation."}, "region", type="Groupe"))
    N.append(noeud(xid, "Exploration", nom, [parent], coulf, b, "examen", type="Endoscopie" if fid == "fx" else "Exploration",
                   exRef=e["id"] if e else None, fiche=o["stem"] if o else None, fenetre=fen, explo=slug if slug in EXPL else None))
    for i, t in enumerate((el.get("traces") or [])[:6]):
        N.append(noeud(f"{xid}__t{i}", "Tracé", t.get("aspect") or t.get("type"), [xid], "#15803d" if t.get("type") == "normal" else "#c2410c",
                       {"def": t.get("description"), "seuil": (el.get("seuils") or [None])[0] if t.get("type") != "normal" else None,
                        "retenir": "Tu lis le tracé, tu appliques le seuil, puis tu conclus (plan, écran X5)."}, "trace",
                       type="Tracé normal" if t.get("type") == "normal" else "Tracé pathologique"))
    for i, dg in enumerate((el.get("diagnostics") or [])[:5]):
        N.append(noeud(f"{xid}__d{i}", "Diagnostic", dg.get("diagnostic"), [xid], "#9f1239",
                       {"def": f"L'exploration oriente vers « {dg.get('diagnostic')} ».", "signe": dg.get("argument") and f"L'argument décisif est : {dg['argument'][0].lower() + dg['argument'][1:]}.",
                        "retenir": "Sommeil : la polysomnographie appartient aux explorations, mais ses diagnostics relèvent de la Psyché (décision du plan, § 4)." if fid == "fs" else None},
                       "patho", type="Diagnostic"))
for n in N:
    if n["nature"] == "Fonction":
        k = n["id"][3:]
        n["bulle"] = {"def": f"La fonction « {n['texte']} » se teste par {cnt.get(k, 0)} explorations.",
                      "pourquoi": "Tu pars d'une fonction parce qu'une exploration mesure ce que l'organe fait, et non ce à quoi il ressemble.",
                      "retenir": "Chaîne du plan : fonction → exploration → tracé ou résultat → interprétation (seuil) → diagnostic → traitement."}
FX = [n for n in N if n["nature"] != "Fonction" or cnt.get(n["id"][3:], 0)]

# ---------------------------------------------------------------- vérifications de cohérence (audit « chaque lien pointe vers un nœud existant »)
for nom, R in (("imagerie", IMG), ("biologie", BIO), ("explorations", FX)):
    ids = [n["id"] for n in R]
    assert len(ids) == len(set(ids)), f"{nom} : identifiants en double"
    S = set(ids)
    for n in R:
        for p in n["de"]:
            assert p in S, f"{nom} : {n['id']} pointe vers {p} absent"

ecrire("reseau_imagerie.json", {"onglet": "imagerie", "rubriques": RUB, "noeuds": IMG})
ecrire("reseau_biologie.json", {"onglet": "biologie", "rubriques": RUB, "noeuds": BIO, "outils": {k: (CALC.get(k) or CRIT.get(k)) for v in OUTILS.values() for k in v if (CALC.get(k) or CRIT.get(k))}})
ecrire("reseau_explorations.json", {"onglet": "explorations", "rubriques": RUB, "noeuds": FX})
ecrire("glossaire.json", GLO)

# ---------------------------------------------------------------- mode Organe : un fichier par organe (fiche complète de chaque examen)
GARDE = ("id", "modalite", "nom", "visees", "signeRecherche", "seuil", "indication", "discriminant", "avantageSelectif", "plutotQue", "limite", "smarterMedicine",
         "radioAnatomieNormale", "precautions", "irradiation_mSv", "delai", "aspectNormal", "anomaliesElementaires", "syndromesParacliniques", "pathologiesAssociees", "bulle", "synonymes")
for o in ORGANES:
    ecrire(f"organes/{o['stem']}.json", {"stem": o["stem"], "nom": o["nom"], "region": o["regionNom"], "couleur": o["couleur"], "a3d": o["a3d"], "mesh": o["mesh"],
                                         "examens": [{k: e.get(k) for k in GARDE if e.get(k) not in (None, [], "")} for e in o["examens"]]})

# ---------------------------------------------------------------- index de recherche (mode Organe et mode Examen), tolérant aux fautes côté page
onglet_de = {"Imagerie": "imagerie", "Biologie": "biologie", "Exploration fonctionnelle": "explorations", "Endoscopie": "explorations", "Anatomopathologie / biopsie": "organe"}
ex_idx = {}
for o in ORGANES:
    for e in o["examens"]:
        k = cle(court(e["nom"], 80))
        x = ex_idx.setdefault(k, {"n": e["nom"], "m": e["modalite"], "o": [], "s": sorted({sans_accent(s) for s in (e.get("synonymes") or [])})[:6]})
        x["o"].append([o["stem"], e["id"]])
ecrire("recherche.json", {"organes": [{"s": o["stem"], "n": o["nom"], "r": o["regionNom"], "c": o["couleur"], "a": o["a3d"], "m": o["mesh"], "k": len(o["examens"])} for o in ORGANES],
                          "examens": list(ex_idx.values())})

# ---------------------------------------------------------------- PRATIQUE : défis jumeaux (remplis seulement) + cas du thorax
def defi_ok(d):
    return d.get("id") and d.get("correction", {}).get("pourquoiJuste") and any(d.get(k) for k in ("question", "casClinique", "situation", "consigne", "descriptionDuTrace", "resultat", "contexte"))


PRAT = {"imagerie": [], "biologie": [], "explorations": []}
for f in glob.glob(os.path.join(PR, "**", "*.json"), recursive=True):
    d = lire(f)
    for ent in d.get("entites", []):
        ref = ent.get("ref"); mod = ent.get("modalite")
        if ref in EXID:
            mod = EXID[ref][1]["modalite"]
        tab = onglet_de.get(mod) or ("explorations" if "/explorations/" in f else "biologie" if "/biologie/" in f else None)
        if tab not in PRAT:
            continue
        ds = [{k: v for k, v in x.items() if v not in (None, [], "")} for x in ent.get("defis", []) if defi_ok(x)]
        if ds:
            PRAT[tab].append({"ref": ref, "nom": ent.get("nom"), "defis": ds})
CAS = []
for f in sorted(glob.glob(os.path.join(P, "cas", "*", "*.json"))):
    c = lire(f)
    CAS.append({k: c[k] for k in ("id", "titre", "stem", "prompt", "options", "correction", "sources") if k in c})
for t, L in PRAT.items():
    ecrire(f"pratique_{t}.json", {"onglet": t, "entites": L, "cas": CAS if t == "imagerie" else []})
print("imagerie", len(IMG), "| biologie", len(BIO), "| explorations", len(FX), "| organes", len(ORGANES), "| glossaire", len(GLO),
      "| défis", {t: sum(len(e["defis"]) for e in L) for t, L in PRAT.items()}, "| cas", len(CAS))
