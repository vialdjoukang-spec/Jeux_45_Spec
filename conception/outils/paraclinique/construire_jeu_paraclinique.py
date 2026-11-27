"""Jeu PARACLINIQUE livré seul (0 token) : fabrique les données de conception/prototypes/paraclinique/ à partir des sources du dépôt.

Le plan de conception (conception/html/paraclinique.html) fixe la forme :
  - Imagerie       : région → examens faisables → système d'organe → organe → pathologie → fenêtre à deux clichés (prompt de Vial, § 10, X3, X4) ;
  - Biologie       : prélèvement → (famille d'analyses si > 14 examens) → examen → interprétation, calculs, critères → diagnostic → traitement (§ 10, X1, X2) ;
  - Explorations   : fonction → exploration → tracé → interprétation (seuils) → diagnostic → traitement ; tracé calculé en fenêtre (§ 10, X5) ;
  - Traitements    : repris tels quels de la Tétrade (posologie et source) ; sans correspondance exacte, case grisée « à produire » ;
  - Mode Organe    : un fichier par organe (examens de toutes modalités, anomalies élémentaires, syndromes, pathologies) (§ 8) ;
  - Pratique       : les défis jumeaux (conception/donnees/pratique/paraclinique) et les 20 cas du thorax (§ 9, § 18, § 19).
Le script ne rédige rien : il range, relie et recopie les textes déjà produits et audités. Les clichés « candidats » non validés
(conception/donnees/images) ne sont pas affichés, car aucun n'a été vérifié.
Sortie : conception/prototypes/paraclinique/donnees/*.json. Signature : AAI (Anthropic AI)"""
import glob, html, json, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(__file__))
import fiches_tetrade as FT

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

QUATRE = [["def", "Ce que c'est"], ["pourquoi", "Pourquoi ici"], ["confusion", "Confusion possible"], ["retenir", "À retenir"]]
# Toutes les infobulles gardent le même cadre de 4 rubriques (plan § 7) ; la fiche complète de l'examen s'ouvre en fenêtre (📄).
RUB = {"region": QUATRE, "examen": QUATRE, "patho": QUATRE, "trace": QUATRE,
       "outil": [["def", "Ce que c'est"], ["pourquoi", "Formule ou éléments"], ["confusion", "Confusion possible"], ["retenir", "À retenir"], ["source", "Source"]]}


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
    n = {"id": id_, "nature": nature, "type": kw.pop("type", nature), "texte": court(texte, kw.pop("maxc", 46)), "de": de, "couleur": couleur, "rubriques": rub, "bulle": bulle}
    n.update({k: v for k, v in kw.items() if v is not None})
    return n


# Libellés de pathologie : sens imposé par le contexte de l'imagerie (le glossaire général peut donner un autre sens).
SIGLE_LIBELLE = {"ACG": "artérite à cellules géantes"}


def developpe(nom):
    """Remplace un sigle du libellé par son nom complet ; renvoie (libellé, définition du sigle).
    On ne développe que si le glossaire donne un groupe nominal (pas une phrase) et si le sigle n'est pas élidé (l'HPV)."""
    for tok in re.findall(r"\b[A-Z][A-Z0-9-]{2,}\b", nom):
        g = SIGLE_LIBELLE.get(tok) or GLO.get(tok)
        if not g:
            continue
        plein = re.split(r"[:,(]", g)[0].strip().rstrip(".").strip()
        phrase = re.search(r"\b(est|sont|relie|désigne|mesure|permet|correspond)\b", plein) or re.match(r"(L'|L’|Le |La |Les )", plein)
        elide = re.search(r"[lLdD][’']" + re.escape(tok), nom)
        if tok in SIGLE_LIBELLE:
            phrase = None
        if phrase or elide or len(plein.split()) > 8:
            return nom, f"{tok} = {GLO.get(tok, g)}"
        rep = plein if nom.startswith(tok) else plein[0].lower() + plein[1:]
        return nom.replace(tok, rep, 1), f"{tok} = {SIGLE_LIBELLE.get(tok) or g}"
    return nom, None


def accroche_pathos(N, pid, e, coul, lim=7):
    for p in (e.get("pathologiesAssociees") or [])[:lim]:
        nid = f"{pid}__{cle(p['pathologie'])}"
        if not any(x["id"] == nid for x in N):
            N.append(noeud(nid, "Pathologie", p["pathologie"], [pid], "#c2410c", bulle_patho(p, e), "patho", exRef=e["id"]))



# ---------------------------------------------------------------- traitements : repris tels quels des diagnostics de la Tétrade (posologie et source déjà audités)
# Aucune posologie n'est rédigée ici : un diagnostic sans correspondance exacte dans la Tétrade reçoit une case grisée « à produire ».
def cle_diag(s):
    return re.sub(r"[^a-z0-9]+", " ", sans_accent(re.sub(r"\s*\(.*?\)", "", s or ""))).strip()


TRT = {}
for n in lire(os.path.join(RAC, "conception", "prototypes", "moteur", "tetrade.json"))["noeuds"]:
    b = n.get("bulle") or {}
    if b.get("traitement"):
        TRT.setdefault(cle_diag(n["texte"]), {"traitement": b["traitement"], "source": b.get("source")})
RUB["diag"] = [["def", "Ce que c'est"], ["pourquoi", "Pourquoi ici"], ["confusion", "Confusion possible"], ["retenir", "À retenir"], ["premiere", "1re intention de cette pathologie"], ["gold", "Gold standard de cette pathologie"], ["source", "Source"]]
RUB["trt"] = [["def", "Ce que c'est"], ["posologie", "Posologie"], ["retenir", "À retenir"], ["source", "Source"]]


def ajouter_traitement(N, did, nom_diag, coul="#15803d"):
    """Débouché diagnostic → traitement : réseau au clic (une case par molécule) ; la même information s'affiche au survol du diagnostic."""
    t = TRT.get(cle_diag(nom_diag))
    if not t:
        N.append(noeud(did + "__trt", "Traitement", "Traitement : à produire", [did], "#9aa2b4",
                       {"def": f"Le traitement de « {nom_diag} » attend sa fiche validée (molécule, posologie, source suisse)."}, "trt",
                       type="Traitement · à produire", aRediger=True))
        return None
    for i, (nom, poso) in enumerate(t["traitement"][:4]):
        N.append(noeud(f"{did}__trt{i}", "Traitement", nom, [did], coul,
                       {"def": f"Cette molécule sert le traitement de « {nom_diag} ».", "posologie": poso,
                        "retenir": "Tu vérifies la posologie dans l'information professionnelle suisse (AIPS, Swissmedic) avant de prescrire.",
                        "source": t.get("source")}, "trt", type="Traitement"))
    return t


def bulle_diag(nom, signe=None, syndrome=None, signif=None, examen=None):
    """Infobulle à 4 rubriques d'un diagnostic, puis le traitement au survol (repris de la Tétrade)."""
    b = {"def": f"Le diagnostic « {nom} » se pose ici à partir de l'examen « {court(examen, 60)} »." if examen else f"Le diagnostic « {nom} » se pose sur cette exploration.",
         "pourquoi": signe or "La fiche de l'examen ne précise pas encore l'anomalie typique.",
         "confusion": syndrome or "Aucune confusion fréquente n'est documentée dans la fiche.",
         "retenir": signif or "Un seul résultat ne suffit jamais : tu le confrontes à la clinique."}
    t = TRT.get(cle_diag(nom))
    if t:
        b["traitement"] = t["traitement"][:4]; b["source"] = t.get("source")
    return b


# ---------------------------------------------------------------- fiche flash d'une pathologie d'imagerie (gabarit de Vial, 26.11.2026 20:29)
# Définition · Épidémiologie · Mécanisme · Syndrome clinique · Sémiologie radiologique · Diagnostic · Traitement · Sources.
# Chaque champ vient d'une fiche sourcée (Tétrade, fiches de Paraclinique, table des niveaux) ; sinon il porte « à produire ».
FT_F = FT.lire()
FLASH = {}       # repli par nom : la fiche la plus complète l'emporte (et non la dernière lue)
FLASH_ORG = {}   # (organe, nom) : la fiche de l'organe affiché l'emporte toujours
_fp = os.path.join(P, "fiches_flash")


def _pleins(v):
    return sum(1 for x in v.values() if x not in (None, "", [], {})) if isinstance(v, dict) else 0


if os.path.isdir(_fp):
    for f in sorted(glob.glob(os.path.join(_fp, "*.json"))):
        st_ = os.path.basename(f)[:-5]
        for k_, v_ in lire(f).items():
            if not k_.startswith("_"):
                FLASH_ORG[(st_, FT.sa(k_))] = v_
                if _pleins(v_) >= _pleins(FLASH.get(FT.sa(k_))):
                    FLASH[FT.sa(k_)] = v_
RUB["patho_img"] = [["def", "Définition"], ["epi", "Épidémiologie"], ["meca", "Mécanisme"], ["synd", "Syndrome clinique"], ["radio", "Sémiologie radiologique"],
                    ["diag", "Diagnostic"], ["trt", "Traitement"], ["source", "Sources"]]
AP = "à produire"


def terme(lib, defi):
    return f'<span class=terme tabindex=0 data-def="{html.escape(defi, quote=True)}">{html.escape(lib)}</span>'


# Sémiologie radiologique : un « syndrome » est un groupement élémentaire d'images (masse, épanchement, obstruction…),
# jamais une maladie. Retour de Vial (27.11) : « Syndrome : cancer pancréatique ? ». Le champ source nomme souvent la maladie :
# on le traduit vers le syndrome radiologique élémentaire, et on n'affiche rien si aucune règle ne s'applique.
SYNDROMES_RADIO = [
    (r"maltraitance", "Syndrome traumatique"), (r"d[eé]bord discal|protrusion discale", "Syndrome compressif"),
    (r"rupture|fracture|traumat", "Syndrome traumatique"), (r"ur[eè]tr", "Syndrome obstructif"), (r"thrombectomie|occlusion (d'une |de l')?art", "Syndrome ischémique"),
    (r"asthme|bronchopneumopathie|\bBPCO\b", "Syndrome bronchique"), (r"polyradicul|d[eé]my[eé]lin", "Syndrome inflammatoire"),
    (r"congestive", "Syndrome vasculaire"),
    (r"m[eé]ningit|enc[eé]phalit|ventriculit", "Syndrome infectieux"), (r"fistule art[eé]rio|malformation art[eé]rio|cavernome", "Syndrome vasculaire"),
    (r"arthrite|spondylarthr|polyarthrite", "Syndrome inflammatoire"), (r"an[eé]vrism", "Syndrome vasculaire"),
    (r"alv[eé]ol", "Syndrome alvéolaire"), (r"interstiti|fibrose pulm|pneumopathie interst", "Syndrome interstitiel"),
    (r"bronch(ectas|iol)|emphys|trapping", "Syndrome bronchique"), (r"atélect|collapsus", "Syndrome d'atélectasie"),
    (r"pneumothorax|pneumop[eé]ritoine|pneumom[eé]diastin|air libre", "Syndrome aérique extra-digestif (gaz anormal)"),
    (r"h[eé]morrag|h[eé]matome|h[eé]mopéritoine|h[eé]mothorax|saignement", "Syndrome hémorragique"),
    (r"isch[eé]m|infarctus|p[eé]nombre|\bAVC\b|\bAIT\b|n[eé]crose avasculaire|ost[eé]on[eé]crose", "Syndrome ischémique"),
    (r"fractur|traumat|rupture|l[eé]sion de la rate|contusion|luxation|d[eé]chirure|entorse", "Syndrome traumatique"),
    (r"lithias|calcul|obstruct|occlusion intestinale|dilatation|hydron[eé]phrose|ict[eè]re|colique|jonction py[eé]lo|r[eé]tention|st[eé]nose (de la voie|bili|ur[eé]t)", "Syndrome obstructif"),
    (r"st[eé]nose|thrombos|occlusion art|embol|an[eé]vrism|dissection|art[eé]riopathie|ath[eé]ro|vasospasme|varic|insuffisance veineuse|budd|hypertension portale|malformation art[eé]rio", "Syndrome vasculaire"),
    (r"[eé]panchement|ascite|pleur[eé]sie|p[eé]ricardite|hydarthrose|chyl", "Syndrome d'épanchement"),
    (r"cancer|carcinom|ad[eé]nocarcinom|tumeu?r|m[eé]tastas|lymphom|my[eé]lom|sarcom|ad[eé]nome|nodule|masse|n[eé]oplas|m[eé]ningiom|gliom|carcinose|polype|incidentalome|l[eé]sion (suspecte|tumorale|focale)|tipmp|kyste dermo|h[eé]mangiom|ph[eé]ochrom", "Syndrome de masse (tumoral)"),
    (r"kyste|pseudokyste|polykyst", "Syndrome kystique"),
    (r"abc[eè]s|infect|ost[eé]omy[eé]lit|spondylodisc|pyo|tubercul|sepsis|empy[eè]me|cellulite|fasciite", "Syndrome infectieux"),
    (r"(it|ites)\b|inflamm|vascularite|sarco|crohn|arthrit|myosit|bursit|tendinop|enth[eé]s|sclérose en plaques|démyélin", "Syndrome inflammatoire"),
    (r"conflit|hernie discale|compression|canal [eé]troit|myélopathie|radicul|plexopath|canal carpien|syndrome du d[eé]fil[eé]", "Syndrome compressif"),
    (r"d[eé]g[eé]n[eé]r|arthrose|d[eé]mence|atrophi|ost[eé]opor|ost[eé]op[eé]n|discopathie|cicatrice", "Syndrome dégénératif ou atrophique"),
    (r"malformat|cong[eé]nital|dysplasi|agén[eé]s|hypoplas|ectopi|ectop", "Syndrome malformatif"),
]


def syndrome_radio(nom):
    nom = unicodedata.normalize("NFC", nom or "")
    if re.match(r"(?i)syndrome (pleural|alv|interstit|nodulaire|de masse|aortique|kystique|bronchique|d'[eé]panchement|m[eé]diastin|obstructif|occlusif|cavitaire|osseux|lytique)", nom or ""):
        return nom
    for motif, syn in SYNDROMES_RADIO:
        if re.search(motif, nom or "", re.I):
            return syn
    return None


def fiche_flash(nom, e, p, niv, libelle=None, syn_force=None, organe=None):
    """Renvoie (bulle, flash) : la bulle garde du texte brut ; les champs *_h portent le HTML survolable."""
    f = FT.trouver(FT_F, nom) or {}
    x = FLASH_ORG.get((organe, FT.sa(nom))) or FLASH.get(FT.sa(nom)) or {}
    b = {"def": x.get("def") or f.get("def") or AP, "epi": x.get("epi") or AP, "meca": x.get("meca") or f.get("pourquoi") or AP}
    sy = x.get("syndromesCliniques") or []
    b["synd"] = ", ".join(s["nom"] for s in sy) if sy else AP
    if sy:
        b["synd_h"] = ", ".join(terme(s["nom"], s["composantes"]) for s in sy)
    sig = p.get("anomalieTypique")
    syn = next((s for s in e.get("syndromesParacliniques") or [] if sig and any(sans_accent(a)[:14] in sans_accent(sig) or sans_accent(sig)[:14] in sans_accent(a) for a in s.get("anomaliesQuiLeComposent") or [])), None)
    rad = []
    if syn_force is not None:  # tableau validé par un radiologue : il l'emporte sur les mots-clés ("" = aucun syndrome)
        if syn_force:
            rad.append(("Syndrome radiologique", syn_force[9:] if syn_force.startswith("Syndrome ") else syn_force,
                        "Ce syndrome radiologique réunit ici : " + (", ".join((syn or {}).get("anomaliesQuiLeComposent") or []).lower() or "les anomalies du signe ci-après") + "."))
    elif syn:
        sr = syndrome_radio(libelle or nom) or syndrome_radio(syn["syndrome"])
        if sr:
            rad.append(("Syndrome radiologique", sr[0].lower() + sr[1:] if not sr.startswith("Syndrome ") else sr[9:], "Ce syndrome radiologique réunit ici : " + ", ".join(syn.get("anomaliesQuiLeComposent") or []).lower() + "."))
    if sig:
        rad.append(("Signe", sig, f"Sur « {court(e['nom'], 60)} », la pathologie montre typiquement : {sig[0].lower() + sig[1:]}."))
    b["radio"] = " ; ".join(f"{a} : {l}" for a, l, _ in rad) if rad else AP
    if rad:
        b["radio_h"] = " ; ".join(f"{a} : " + terme(l, d) for a, l, d in rad)
    pi = gs = None
    if niv and len(niv) > 3:
        pi, gs = niv[3]["premiereIntention"], niv[3]["goldStandard"]
    else:
        for bl in f.get("bilan") or []:
            if bl["visee"] == "diagnostique" and "1re" in bl["groupe"]:
                pi = pi or bl["examen"]
            if bl["visee"] == "diagnostique" and "Gold" in bl["groupe"]:
                gs = gs or bl["examen"]
    b["diag"] = (f"Cet examen : {niv[1]} " if niv else "") + f"1re intention : {pi or AP} ; gold standard : {gs or AP}."
    tr = f.get("traitements") or []
    but = (x.get("butTraitement") or "").strip().rstrip(".") or None
    moy = x.get("moyensGeneraux")
    if x.get("moyens"):  # gabarit de Vial : but, puis moyen général (moyens spécifiques), chacun survolable
        mo = x["moyens"]
        b["trt"] = f"But : {but or AP}. Moyens : " + ", ".join(f"{m['general']} ({m['specifiques']})" for m in mo)
        b["trt_h"] = f"But : {html.escape(but or AP)}. Moyens : " + ", ".join(terme(f"{m['general']} ({m['specifiques']})", m.get("detail") or m["specifiques"]) for m in mo)
    elif tr or but:
        b["trt"] = f"But : {but or AP}. Moyens : " + (moy or ", ".join(t_["nom"] for t_ in tr))
        b["trt_h"] = f"But : {html.escape(but or AP)}. Moyens : " + ", ".join(terme(t_["nom"], t_["detail"]) for t_ in tr)
    else:
        b["trt"] = AP
    src = [s_ for s_ in (x.get("source"), f.get("source"), niv[2] if niv else None, (niv[3]["source"] if niv and len(niv) > 3 else None)) if s_]
    src = [s_.strip().rstrip(".") for s_ in src]
    src = [s_ for i, s_ in enumerate(src) if not any(j != i and s_ in o for j, o in enumerate(src)) and s_ not in src[:i]]
    b["source"] = " ; ".join(src) + "." if src else AP
    return b

# ---------------------------------------------------------------- 1. IMAGERIE : région → organe → modalité → examen → pathologie → fenêtre à deux clichés
# Chaîne exacte du prompt de Vial (projets/2_Jeux_Paraclinique/PROMPT_VIAL.md) et du plan § 10 ; aucun niveau « technique ».
SYS = {"Système nerveux": ("#7c3aed", "encephale meninges_et_lcr nerfs_craniens moelle_epiniere queue_de_cheval_et_cone_terminal racines_et_plexus nerfs_peripheriques"),
       "Système ORL et ophtalmologique": ("#0e7490", "oeil_et_orbite oreille_et_equilibre nez_sinus_et_cavum larynx_et_pharynx cavite_buccale_et_glandes_salivaires masses_cervicales_et_kystes"),
       "Système endocrinien": ("#a16207", "hypophyse_et_hypothalamus thyroide parathyroides surrenales metabolisme_et_endocrinologie"),
       "Système respiratoire": ("#2563eb", "poumons_et_voies_aeriennes plevre diaphragme_et_muscles_respiratoires mediastin"),
       "Système cardiovasculaire": ("#b91c1c", "coeur_et_pericarde aorte_thoracique_et_arteres_pulmonaires vaisseaux_du_cou_et_de_la_tete aorte_abdominale_et_vaisseaux_digestifs veines_caves_et_systeme_porte arteres_des_membres veines_des_membres"),
       "Système digestif": ("#c2410c", "oesophage estomac_et_duodenum intestin_grele colon_rectum_et_anus appendice foie vesicule_et_voies_biliaires pancreas peritoine_et_ascite paroi_abdominale_et_hernies"),
       "Système urinaire": ("#ca8a04", "reins ureteres vessie_et_uretre retroperitoine"),
       "Système génital et obstétrical": ("#be185d", "prostate_et_vesicules_seminales testicules_et_scrotum penis_et_uretre_masculin uterus_col_ovaires_et_annexes vulve_vagin_et_perinee grossesse_foetus_et_placenta post_partum_et_allaitement plancher_pelvien seins"),
       "Appareil locomoteur": ("#5f7f3a", "articulation_temporo_mandibulaire_et_den os_du_crane_et_de_la_face rachis_osseux paroi_thoracique_et_cotes hanche_et_bassin epaule coude_poignet_et_main genou cheville_et_pied muscles tendons_et_ligaments os_longs_et_squelette articulations_et_synoviale"),
       "Système hématologique et immunitaire": ("#9f1239", "rate ganglions_cervicaux moelle_osseuse_et_ganglions sang_et_hemostase systeme_lymphatique infection_et_immunite"),
       "Peau et phanères": ("#c0623b", "peau ongles_et_cheveux plaies_ulceres_et_escarres"),
       "Psyché": ("#6d28d9", "psyche sommeil_et_vigilance"),
       "Approche globale": ("#6b7280", "corps_entier croissance_et_developpement_de_l_enfant evaluation_geriatrique_globale genetique toxicologie_et_medicaments urgences_et_point_of_care")}
SYS_DE = {s: nom for nom, (c, ss) in SYS.items() for s in ss.split()}
for o in ORGANES:
    assert o["stem"] in SYS_DE, "organe sans système : " + o["stem"]

PILOTE = lire(os.path.join(RAC, "conception", "prototypes", "moteur", "paraclinique.json"))
CAS_CLICHE = PILOTE["fenetres"][0]
PIL = {n["id"]: n["bulle"] for n in PILOTE["noeuds"]}
BULLE_REG = {"1": PIL["cr"], "4": PIL["th"], "5": PIL["ab"], "6": PIL["pe"]}  # infobulles validées du pilote


def cliches_pneumonie():
    cas = lire(os.path.join(P, "imagerie", "cas", "pneumonie_lobaire_moyenne.json"))
    c = {k: CAS_CLICHE[k] for k in ("titre", "annotations")}
    c["img"] = "../moteur/" + CAS_CLICHE["img"]; c["normal"] = dict(CAS_CLICHE["normal"], img="../moteur/" + CAS_CLICHE["normal"]["img"])
    c["diagnostic"] = cas["diagnostic"] + " : une opacité alvéolaire nouvelle efface le bord droit du cœur (signe de la silhouette)."
    c["conduite"] = "Tu évalues la gravité par le score CURB-65 (grille des critères), puis tu traites selon les recommandations de la Société suisse d'infectiologie (SSI)."
    c["source"] = "Cliché du patient : " + cas["clicheBrut"]["url"] + " ; cliché normal : " + CAS_CLICHE["normal"]["source"] + "."
    return c


# ---------------------------------------------------------------- atlas radiologique (dépôt organigramme-examen-federal, imagerie_GROK/harnais, branché le 27.11.2026)
# Une paire de l'atlas ne s'affiche que si sa modalité est celle de l'examen (pas de radiographie sous un scanner).
from PIL import Image as _Img
ATL_D = os.path.join(P, "atlas", "manifest"); ATL_I = os.path.join(RAC, "conception", "prototypes", "paraclinique", "atlas")
# Syndromes radiologiques validés par un radiologue, un fichier par organe : {pathologie (nom source): "Syndrome …" ou ""}.
_DSV = os.path.join(P, "syndromes_radio")
SYN_VALIDE = {f[:-5]: {k_: v_ for k_, v_ in lire(os.path.join(_DSV, f)).items() if not k_.startswith("_")}
              for f in sorted(os.listdir(_DSV)) if f.endswith(".json")} if os.path.isdir(_DSV) else {}
ATLAS_LIEN = {f[:-5]: {k_: v_ for k_, v_ in lire(os.path.join(P, "atlas_liens", f)).items() if not k_.startswith("_")}
              for f in os.listdir(os.path.join(P, "atlas_liens"))} if os.path.isdir(os.path.join(P, "atlas_liens")) else {}
MOD_ATL = {"Radiographie": "RX", "Mammographie": "RX", "Scanner (CT)": "TDM", "Échographie et Doppler": "US", "Scintigraphie": "MN", "TEP-CT": "MN", "IRM": "IRM", "Angiographie": "INT"}
ROLE_C = {"principale": "#e0a400", "associée": "#0891b2", "associee": "#0891b2", "complication": "#db2777"}


def cliches_atlas(stem, patho, modalite):
    lien = (ATLAS_LIEN.get(stem) or {}).get(patho)
    i = lien.get("atlas") if isinstance(lien, dict) else lien
    nor_aj = lien.get("normal") if isinstance(lien, dict) else None
    f = os.path.join(ATL_D, f"{i}.json") if i else None
    if not f or not os.path.exists(f):
        return None
    m = lire(f); pa = m.get("patho") or {}; no = m.get("normal") or {}
    if not pa.get("file") or not (m.get("cliche") or "").startswith(MOD_ATL.get(modalite, "?")):
        return None
    img = os.path.join(ATL_I, pa["file"].replace("images/", "")); W, H = _Img.open(img).size
    ann = []
    for j, a in enumerate(pa.get("arrows") or [], 1):
        if a.get("contour"):
            xs = [q[0] for q in a["contour"]]; ys = [q[1] for q in a["contour"]]
            x, y, rx, ry = (min(xs) + max(xs)) / 2 * W, (min(ys) + max(ys)) / 2 * H, max(.02, (max(xs) - min(xs)) / 2) * W, max(.02, (max(ys) - min(ys)) / 2) * H
        else:
            x, y, rx, ry = a["tip"][0] * W, a["tip"][1] * H, .045 * W, .045 * W
        ann.append({"n": j, "x": round(x), "y": round(y), "rx": round(rx), "ry": round(ry), "couleur": ROLE_C.get(a.get("role", ""), "#e0a400"),
                    "texte": f"{a.get('label', '')} ({a.get('role', 'lésion')}) : {a.get('definition', '')}".strip()})
    c = {"titre": f"Preuve d'imagerie — {m['cliche']} : patient et normal", "annotations": ann, "img": "atlas/" + pa["file"].replace("images/", ""),
         "diagnostic": m["dx"] + ". " + (m.get("pair_match") or ""), "conduite": ("À vérifier : " + " ; ".join(m["a_verifier"])) if m.get("a_verifier") else "",
         "source": f"Cliché du patient : {pa.get('author', '?')}, {pa.get('license', '?')}, {pa.get('source_url', '')}"
                   + (f" ; cliché normal : {no.get('author', '?')}, {no.get('license', '?')}, {no.get('source_url', '')}" if no.get("file") else "") + f" ; atlas {i}."}
    c["normal"] = {"img": "atlas/" + no["file"].replace("images/", ""), "source": no.get("source_url"), "reperes": []} if no.get("file") else None
    if not c["normal"] and nor_aj:  # cliché normal apparié choisi et vérifié par un agent (même technique, même plan)
        c["normal"] = {"img": nor_aj["img"], "source": nor_aj.get("source"), "reperes": []}
        c["source"] += f" ; cliché normal : {nor_aj.get('auteur', '?')}, {nor_aj.get('licence', '?')}, {nor_aj.get('source', '')}"
    return c

# Chaîne fixée par Vial le 26.11.2026 (PROMPT_VIAL.md, § Ajout du 26.11) : région → organes de la région → modalités d'imagerie de l'organe
# (groupe par nature, barre perpendiculaire) → examens de la modalité → pathologies de l'organe diagnostiquées par cet examen → fenêtre à deux clichés.
# Les neuf types d'imagerie du plan (§ 10, « Imagerie : examens »), dans son ordre ; aucun groupe hors plan.
MODALITES = [("TEP-CT", r"\bTEP\b|\bPET\b|PET-|TEP-"), ("Scintigraphie", r"scintigraph|\bSPECT\b|DaTSCAN|MIBG|DMSA|MAG3|HIDA|sestamibi|DOTATATE"),
             ("Mammographie", r"mammograph|tomosynth"), ("Ostéodensitométrie", r"DXA|ost[ée]odensito"),
             ("Angiographie", r"art[ée]riograph|angiograph|coronarograph|DSA|cavograph|phl[ée]bograph|lymphograph|py[ée]lograph"),
             ("IRM", r"\bIRM\b|IRM |-IRM|neurographie"), ("Scanner (CT)", r"\bCT\b|-CT\b|scanner|TDM|tomodensito|cone beam|cisternograph"),
             ("Échographie et Doppler", r"[ée]cho|doppler|POCUS|eFAST|[ée]lastograph|CEUS"),
             ("Radiographie", r"radiograph|clich|transit|orthopantomo|d[ée]f[ée]cograph|cystograph|ur[ée]trograph|hyst[ée]ros|[âa]ge osseux|bilan radiologique|radioscopie|EOS")]
# Ordre physique demandé par Vial (26.11) : rayons X, puis rayonnements nucléaires (gamma, positons), puis ultrasons, puis résonance magnétique.
ORDRE_PLAN = ["Radiographie", "Mammographie", "Ostéodensitométrie", "Scanner (CT)", "Angiographie", "Scintigraphie", "TEP-CT", "Échographie et Doppler", "IRM"]
ONDE = {"Radiographie": "rayons X", "Mammographie": "rayons X", "Ostéodensitométrie": "rayons X", "Scanner (CT)": "rayons X", "Angiographie": "rayons X",
        "Scintigraphie": "rayons gamma", "TEP-CT": "positons", "Échographie et Doppler": "ultrasons", "IRM": "résonance magnétique"}
HORS_PLAN = []
MODCOUL = {"Radiographie": "#475569", "Échographie et Doppler": "#0f766e", "Scanner (CT)": "#1d4ed8", "IRM": "#7c3aed", "TEP-CT": "#b45309",
           "Scintigraphie": "#a16207", "Angiographie": "#b91c1c", "Mammographie": "#be185d", "Ostéodensitométrie": "#5f7f3a"}
MODBUL = {"Radiographie": "Elle superpose les plans mais répond vite, à faible dose, au lit du malade.",
          "Échographie et Doppler": "Elle n'irradie pas et voit les interfaces liquide-solide et les flux, mais dépend de l'opérateur.",
          "Scanner (CT)": "Il voit l'os, le sang frais et les organes pleins en coupes fines, au prix d'une irradiation.",
          "IRM": "Elle caractérise les tissus mous sans rayons, mais reste longue et peu disponible en urgence.",
          "TEP-CT": "Elle montre l'activité métabolique d'une lésion, surtout pour stadifier un cancer ou chercher un foyer.",
          "Scintigraphie": "Elle mesure la fonction d'un tissu plutôt que sa forme.",
          "Angiographie": "Elle opacifie une lumière (vaisseau, voie urinaire, voie biliaire) et permet souvent un geste dans le même temps.",
          "Ostéodensitométrie": "Elle mesure la densité minérale osseuse pour poser le diagnostic d'ostéoporose.",
          "Mammographie": "Elle dépiste et caractérise les lésions du sein, avec la classification BI-RADS."}
NIV = {f[:-5]: lire(os.path.join(P, "niveaux", f)) for f in os.listdir(os.path.join(P, "niveaux"))} if os.path.isdir(os.path.join(P, "niveaux")) else {}
NIV_ORDRE = ["Première intention", "Examen de référence", "Deuxième intention", "Dépistage", "Stadification", "Orientation : à confirmer", "Diagnostic différentiel"]
NIV_COUL = {"Première intention": "#15803d", "Examen de référence": "#1d4ed8", "Deuxième intention": "#0e7490", "Dépistage": "#a16207",
            "Stadification": "#7c3aed", "Orientation : à confirmer": "#c2410c", "Diagnostic différentiel": "#6b7280"}


def modalites_de(nom):
    """Un examen double (« CT et IRM orbitaires ») va dans ses deux modalités ; une angiographie à la fluorescéine n'est pas de l'imagerie à rayonnement."""
    if re.search(r"fluoresc|indocyanine", nom, flags=re.I):
        return []
    if re.search(r"\bCT\b.*\bet\b.*\bIRM\b|\bIRM\b.*\bet\b.*\bCT\b", nom):
        return ["Scanner (CT)", "IRM"]
    m = modalite_de(nom)
    return [m] if m else []


def modalite_de(nom):
    for m, rx in MODALITES:
        if re.search(rx, nom, flags=re.I):
            return m


N = []
for r, (rnom, mesh, cote, coul) in REG.items():
    orgs = [o for o in ORGANES if o["region"] == r and any(e["modalite"] == "Imagerie" for e in o["examens"])]
    if not orgs:
        continue
    rid = f"im_r{r}"
    br = BULLE_REG.get(r) or {"def": f"La région « {rnom} » contient {len(orgs)} organes explorés par l'imagerie.",
                              "pourquoi": "Tu pars de la région, puis tu choisis l'organe : l'imagerie se demande pour un organe ciblé.",
                              "confusion": "Aucune confusion fréquente.",
                              "retenir": "Tu cliques l'organe, puis la modalité, l'examen et la pathologie : la fenêtre à deux clichés s'ouvre sur la pathologie."}
    N.append(noeud(rid, "Région", rnom, [], coul, br, "region", organe=mesh, cote=cote, type="Région"))
    for o in orgs:
        oid = f"{rid}__{o['stem'][:30]}"; ocoul = SYS[SYS_DE[o["stem"]]][0]
        ex = [e for e in o["examens"] if e["modalite"] == "Imagerie"]
        par_m = {}
        for e in ex:
            ms_ = modalites_de(e["nom"])
            if not ms_:
                HORS_PLAN.append(f"{o['nom']} : {e['nom']}"); continue
            for m_ in ms_:
                par_m.setdefault(m_, []).append(e)
        ex = list({id(e): e for L in par_m.values() for e in L}.values())
        N.append(noeud(oid, "Organe", o["nom"], [rid], ocoul,
                       {"def": f"L'organe « {o['nom']} » s'explore par {len(ex)} examens d'imagerie, rangés en {len(par_m)} modalités.",
                        "pourquoi": "L'organe est la cible de l'investigation : tu choisis ensuite la modalité qui répond à ta question.",
                        "confusion": "Aucune confusion fréquente.", "retenir": "Modalités : " + ", ".join(m for m in ORDRE_PLAN if m in par_m) + "."},
                       "region", type="Organe", fiche=o["stem"]))
        for m in [m for m in ORDRE_PLAN if m in par_m]:
            mid = f"{oid}__m{cle(m)[:16]}"; L_ = par_m[m]
            N.append(noeud(mid, "Modalité", m, [oid], MODCOUL[m],
                           {"def": f"La modalité « {m} » offre {len(L_)} examen{'s' if len(L_) > 1 else ''} pour cet organe.",
                            "pourquoi": MODBUL[m], "confusion": "Aucune confusion fréquente.",
                            "retenir": "Examens : " + ", ".join(court(e["nom"], 40) for e in L_) + "."}, "examen", type="Modalité · " + ONDE[m]))
            for e in L_:
                eid = f"{mid}__{cle(court(e['nom'], 80))[:36]}"; b = bulle_examen(e)
                if o["stem"] == "poumons_et_voies_aeriennes" and cle(court(e["nom"], 80)) == "radiographie_thoracique":
                    b = dict(b, **PIL["e1"])  # infobulle validée du pilote (radiographie thoracique PA)
                N.append(noeud(eid, "Examen", e["nom"], [mid], "#2a9d8f" if b.get("pourquoi") else "#9aa2b4", b, "examen",
                               type="Examen" if b.get("pourquoi") else "Examen · à produire", exRef=e["id"], fiche=o["stem"], aRediger=None if b.get("pourquoi") else True))
                ref = [sans_accent(x)[:18] for x in e.get("referencePour") or []]
                tab = next((v for k_, v in (NIV.get(o["stem"]) or {}).items() if not k_.startswith("_") and sans_accent(e["nom"]).startswith(sans_accent(k_))), None)
                for p in (e.get("pathologiesAssociees") or [])[:7]:
                    parent = eid; niv = None
                    if tab:
                        niv = tab.get(p["pathologie"])
                        assert niv, f"niveau manquant : {e['nom']} / {p['pathologie']}"
                        parent = f"{eid}__n{cle(niv[0])[:14]}"
                        if parent not in {x["id"] for x in N}:
                            N.append(noeud(parent, "Niveau", niv[0], [eid], NIV_COUL[niv[0]],
                                           {"def": f"Ce groupe réunit les pathologies pour lesquelles cet examen intervient au niveau « {niv[0].lower()} ».",
                                            "pourquoi": "Le niveau d'indication te dit si tu demandes cet examen d'emblée, pour trancher, pour dépister, pour stadifier ou seulement pour orienter.",
                                            "confusion": "Un examen qui oriente ne confirme pas : un autre examen tranche ensuite.",
                                            "retenir": "Les niveaux suivent l'ordre : première intention, référence, deuxième intention, dépistage, stadification, orientation, diagnostic différentiel."},
                                           "examen", type="Niveau d'indication", ordre=NIV_ORDRE.index(niv[0])))
                    pid = f"{parent}__{cle(p['pathologie'])[:30]}"
                    if any(x["id"] == pid for x in N):
                        continue
                    bp = bulle_patho(p, e)
                    bd = bulle_diag(p["pathologie"], bp.get("signe"), bp.get("syndrome"), bp.get("retenir"), e["nom"])
                    gold = any(x and x in sans_accent(p["pathologie"]) for x in ref)
                    if niv:
                        bd = dict(bd, retenir=niv[1], source=niv[2])
                        if len(niv) > 3:  # angle mort : l'examen oriente seulement ; la survol donne l'examen qui pose le diagnostic
                            bd = dict(bd, premiere=niv[3]["premiereIntention"] + ".", gold=niv[3]["goldStandard"] + ".", source=niv[2] if niv[3]["source"] in niv[2] else niv[2] + " ; " + niv[3]["source"])
                    lib, sig = developpe(p["pathologie"])
                    bd = fiche_flash(p["pathologie"], e, p, niv, lib, (SYN_VALIDE.get(o["stem"]) or {}).get(p["pathologie"]), o["stem"])
                    if sig and sig.split(" = ")[0] not in bd["def"]:
                        bd["def"] = sig + " " + bd["def"]
                    pn = noeud(pid, "Pathologie", lib, [parent], "#d64545", bd, "patho_img", maxc=72, flash=True, type="Pathologie" if niv else ("Pathologie · examen de référence" if gold else "Pathologie"), exRef=e["id"], signe=p.get("anomalieTypique"))
                    if o["stem"] == "poumons_et_voies_aeriennes" and cle(court(e["nom"], 80)) == "radiographie_thoracique" and "pneumonie" in cle(p["pathologie"]):
                        pn["cliches"] = cliches_pneumonie()  # la fiche flash (gabarit du 26.11) remplace l'infobulle du pilote
                    else:
                        ca = cliches_atlas(o["stem"], p["pathologie"], m)
                        if ca:
                            pn["cliches"] = ca
                        else:
                            pn["clichesAProduire"] = True
                    N.append(pn)
_nv = {}
for x in N:
    if x["nature"] == "Niveau":
        _nv.setdefault(x["de"][0], []).append(x)
_vus, _N2 = set(), []
for x in N:
    if x["nature"] == "Niveau":
        if x["de"][0] not in _vus:
            _vus.add(x["de"][0]); _N2 += sorted(_nv[x["de"][0]], key=lambda y: y["ordre"])
    else:
        _N2.append(x)
N = _N2
IMG = N
print('hors plan (exclus de l\'Imagerie) :', len(HORS_PLAN), HORS_PLAN)

# ---------------------------------------------------------------- 2. BIOLOGIE : prélèvement → examens → interprétation, calculs, critères → diagnostics → traitement
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

# Chaîne du prompt : prélèvement → examens → interprétation, calculs et critères → diagnostics → traitement avec posologie.
# Le sang veineux compte près de 200 examens : ils se rangent par famille d'analyses (plan § 10), seul niveau intermédiaire, réservé aux prélèvements de plus de 30 examens.
PCOTE = {"sang_veineux": ("coeur", "d"), "sang_arteriel": ("aorte", "g"), "sang_capillaire": ("humerus", "d"), "hemocultures": ("coeur", "g"),
         "moelle_osseuse": ("femur", "g"), "urine": ("vessie", "d"), "liquide_cephalorachidien": ("cerveau", "g"), "liquide_pleural": ("poumon_d", "g"),
         "liquide_pericardique": ("coeur", "d"), "liquide_d_ascite": ("foie", "g"), "liquide_synovial": ("femur", "d"),
         "ponction_de_kyste_d_abces_ou_de_collecti": ("rate", "d"), "liquide_amniotique": ("bassin", "g"), "selles": ("colon", "g"),
         "expectorations_et_lavage_bronchoalveolai": ("poumon_g", "d"), "ecouvillons_nasopharynges_et_de_gorge": ("trachee", "d"), "air_expire": ("trachee", "g"),
         "prelevements_genitaux_et_uretraux": ("bassin", "d"), "sperme": ("vessie", "g"), "biopsies_tissulaires": ("foie", "d"), "sueur": ("humerus", "g"),
         "salive": ("crane", "d"), "cheveux_et_ongles": ("crane", "g")}
PCOUL = {"sang_veineux": "#b91c1c", "sang_arteriel": "#dc2626", "sang_capillaire": "#e11d48", "hemocultures": "#9f1239", "moelle_osseuse": "#7f1d1d",
         "urine": "#ca8a04", "liquide_cephalorachidien": "#7c3aed", "liquide_pleural": "#0e7490", "liquide_pericardique": "#0369a1", "liquide_d_ascite": "#c98a2b",
         "liquide_synovial": "#5f7f3a", "ponction_de_kyste_d_abces_ou_de_collecti": "#92400e", "liquide_amniotique": "#be185d", "selles": "#78350f",
         "expectorations_et_lavage_bronchoalveolai": "#2563eb", "ecouvillons_nasopharynges_et_de_gorge": "#0891b2", "air_expire": "#0284c7",
         "prelevements_genitaux_et_uretraux": "#db2777", "sperme": "#a21caf", "biopsies_tissulaires": "#a16207", "sueur": "#c0623b", "salive": "#ea580c", "cheveux_et_ongles": "#6b7280"}
# Calculs et critères rattachés à l'examen qui les nourrit (regex sur le nom de l'examen) ; sans examen correspondant, ils restent au niveau du prélèvement.
OUTILS_EX = [("sang_veineux", r"ionogramme|natr[ée]mie|sodium", ["calc_trou_anionique", "calc_trou_anionique_corrige", "calc_sodium_corrige_glycemie", "crit_hyponatremie"]),
             ("sang_veineux", r"cr[ée]atinin", ["calc_ckd_epi_2021", "calc_cockcroft_gault", "crit_kdigo_ira_definition", "crit_kdigo_ira_stades"]),
             ("sang_veineux", r"calc[ée]mie|calcium", ["calc_calcium_corrige"]), ("sang_veineux", r"lipid|cholest", ["calc_friedewald"]),
             ("sang_veineux", r"insulin|hba1c|glyc[ée]mie", ["calc_homa_ir"]), ("sang_veineux", r"transaminase|asat|alat|bilan h[ée]patique", ["calc_fib4", "calc_apri", "calc_meld_3"]),
             ("sang_arteriel", r"gazom", ["calc_rapport_pao2_fio2", "crit_sdra_berlin_definition", "crit_sdra_berlin_gravite"]),
             ("urine", r"natriur|fraction d.excr", ["calc_fena", "calc_feun"]), ("urine", r"ionogramme urinaire|trou anionique|natriur", ["calc_trou_anionique_urinaire"]),
             ("liquide_pleural", r"light|pleural", ["crit_light_exsudat_pleural"]),
             ("liquide_d_ascite", r"gradient", ["calc_gradient_albumine_ascite", "crit_gradient_albumine_ascite_seuil"])]
# Critères du plan § 10 encore absents de criteres.json : case grisée « à produire », sans aucun seuil rédigé ici.
A_PRODUIRE = [("liquide_cephalorachidien", r"aspect|cellules", "Profils du LCR")]
OUTILS_EX += [("urine", r"culture d.urine|uricult|bandelette|s[ée]diment", ["crit_kass_bacteriurie"]),
              ("liquide_d_ascite", r"gradient|polynucl|cellul|ascite", ["crit_infection_spontanee_ascite"]),
              ("liquide_synovial", r"cellules|cristaux|liquide synovial|ponction", ["crit_liquide_synovial_septique"])]
N = []
parP = {}
for o in ORGANES:
    for e in o["examens"]:
        if e["modalite"] == "Biologie":
            parP.setdefault(prelevement_de(e), []).append((o, e))
places = set()


def outils_de(p, nom_ex):
    s = sans_accent(nom_ex); r = []
    for pp, rx, ids in OUTILS_EX:
        if pp == p and re.search(sans_accent(rx), s):
            r += [i for i in ids if i not in r]
    return r


# Départs posés sur le corps : douze natures de prélèvement (prompt : sang, urine, LCR, ascite, ponction-biopsie, liquide articulaire…) ;
# une nature qui réunit plusieurs prélèvements (le sang) les déplie au clic. Le côté suit l'organe d'ancrage pour que le trait sorte par le bord le plus proche.
DEPARTS = [("sang", "Sang", "coeur", "d", "#b91c1c", ["sang_veineux", "sang_arteriel", "sang_capillaire", "hemocultures"]),
           ("urine", "Urine", "vessie", "d", "#ca8a04", ["urine"]),
           ("lcr", "Liquide céphalorachidien", "cerveau", "g", "#7c3aed", ["liquide_cephalorachidien"]),
           ("pleural", "Liquide pleural", "poumon_d", "g", "#0e7490", ["liquide_pleural"]),
           ("ascite", "Liquide d'ascite", "foie", "g", "#c98a2b", ["liquide_d_ascite"]),
           ("synovial", "Liquide articulaire (synovial)", "femur", "d", "#5f7f3a", ["liquide_synovial"]),
           ("pericarde", "Liquide péricardique", "coeur", "d", "#0369a1", ["liquide_pericardique"]),
           ("ponction", "Ponctions et biopsies", "rate", "d", "#92400e", ["biopsies_tissulaires", "moelle_osseuse", "ponction_de_kyste_d_abces_ou_de_collecti"]),
           ("selles", "Selles", "colon", "g", "#78350f", ["selles"]),
           ("resp", "Voies respiratoires et air expiré", "trachee", "d", "#2563eb", ["expectorations_et_lavage_bronchoalveolai", "ecouvillons_nasopharynges_et_de_gorge", "air_expire"]),
           ("genital", "Génital et obstétrical", "bassin", "g", "#be185d", ["prelevements_genitaux_et_uretraux", "sperme", "liquide_amniotique"]),
           ("secretions", "Sueur, salive, cheveux et ongles", "crane", "g", "#6b7280", ["sueur", "salive", "cheveux_et_ongles"])]
assert sorted(p for d in DEPARTS for p in d[5]) == sorted(PNOM), "prélèvement oublié"
for did_, dnom, mesh, cote, dcoul, membres in DEPARTS:
    if len(membres) > 1:
        N.append(noeud(f"bi_{did_}", "Prélèvement", dnom, [], dcoul,
                       {"def": f"La nature « {dnom} » réunit {len(membres)} prélèvements : " + ", ".join(PNOM[m].lower() for m in membres) + ".",
                        "pourquoi": "Tu pars du prélèvement parce que le geste, le tube et le transport décident de la fiabilité du résultat.",
                        "confusion": "Aucune confusion fréquente.", "retenir": "Tu choisis le prélèvement exact, puis l'examen, l'interprétation, le diagnostic et le traitement."},
                       "region", organe=mesh, cote=cote, type="Prélèvement"))
    for p in membres:
        coul = PCOUL[p]; pid = f"bi_{p[:24]}"; liste = parP.get(p, []); pj = PREL.get(p, {})
        seul = len(membres) == 1
        N.append(noeud(pid, "Prélèvement", dnom if seul else PNOM[p], [] if seul else [f"bi_{did_}"], dcoul if seul else coul,
                       {"def": f"Le prélèvement « {PNOM[p]} » sert {len(liste) or len(pj.get('examens', []))} examens du catalogue.",
                        "pourquoi": "Tu pars du prélèvement parce que le geste, le tube et le transport décident de la fiabilité du résultat.",
                        "confusion": "Aucune confusion fréquente.",
                        "retenir": "La chaîne va du prélèvement à l'examen, puis à l'interprétation, au diagnostic et au traitement."},
                       "region", organe=mesh if seul else None, cote=cote if seul else None, type="Prélèvement"))
        groupes = {}
        for o, e in liste:
            g = FAMN.get(famille_analyse(e["nom"]) or "", "Autres analyses") if len(liste) > 30 else None
            groupes.setdefault(g, []).append((o, e))
        vus = set()
        for g, items in sorted(groupes.items(), key=lambda kv: (kv[0] is None, kv[0] or "")):
            parent = pid
            if g:
                parent = f"{pid}__{cle(g)[:24]}"
                N.append(noeud(parent, "Famille d'analyses", g, [pid], coul,
                               {"def": f"La famille « {g} » regroupe {len(items)} examens de ce prélèvement.",
                                "pourquoi": "Le sang veineux sert près de deux cents examens : la famille d'analyses garde la toile lisible (plan § 10).",
                                "confusion": "Aucune confusion fréquente.", "retenir": "Les familles suivent les quinze fichiers d'analyses, source unique des valeurs SI."},
                               "region", type="Famille d'analyses"))
            for o, e in items:
                k = cle(court(e["nom"], 80))[:40]; eid = f"{pid}__{k}"
                if eid in vus:
                    continue
                vus.add(eid); b = bulle_examen(e); ok = bool(e.get("seuil") or e.get("signeRecherche"))
                N.append(noeud(eid, "Examen", e["nom"], [parent], coul, b, "examen", type="Examen", exRef=e["id"], fiche=o["stem"]))
                # interprétation : signe recherché et seuil de la fiche de l'examen, puis les diagnostics qu'elle oriente
                iid = eid + "__int"
                syn = (e.get("syndromesParacliniques") or [None])[0]
                N.append(noeud(iid, "Interprétation", court(re.sub(r"^(Selon|D.apr[eè]s) [^,]{2,90}, *", "", e.get("seuil")).capitalize()[:1] + re.sub(r"^(Selon|D.apr[eè]s) [^,]{2,90}, *", "", e.get("seuil"))[1:], 70) if e.get("seuil") else "Seuil à produire", [eid], coul if ok else "#9aa2b4",
                               {"def": e.get("signeRecherche") or "La fiche ne précise pas encore le signe recherché.",
                                "pourquoi": e.get("seuil") or "La fiche ne précise pas encore le seuil.",
                                "confusion": e.get("limite") or (e.get("bulle") or {}).get("confusion") or "Aucune confusion fréquente.",
                                "retenir": (f"Le syndrome « {syn['syndrome']} » réunit : " + ", ".join(syn.get("anomaliesQuiLeComposent") or []).lower() + ".") if syn else ((e.get("bulle") or {}).get("retenir") or "Tu confrontes le résultat à la clinique.")},
                               "diag", type="Seuil" if ok else "Seuil · à produire", aRediger=None if ok else True))
                for po in (e.get("pathologiesAssociees") or [])[:6]:
                    did = f"{iid}__{cle(po['pathologie'])[:30]}"
                    if any(x["id"] == did for x in N):
                        continue
                    bp = bulle_patho(po, e)
                    N.append(noeud(did, "Diagnostic", po["pathologie"], [iid], "#d64545", bulle_diag(po["pathologie"], bp.get("signe"), bp.get("syndrome"), bp.get("retenir"), e["nom"]),
                                   "diag", type="Diagnostic"))
                    ajouter_traitement(N, did, po["pathologie"])
                for oid in outils_de(p, e["nom"]):
                    x = CALC.get(oid) or CRIT.get(oid)
                    if not x:
                        continue
                    places.add((p, oid)); calc = oid.startswith("calc_")
                    N.append(noeud(f"{eid}__{oid}", "Calcul" if calc else "Critère", x["nom"], [eid], "#0f766e" if calc else "#6d28d9",
                                   {"def": f"Ce calculateur exécute la formule « {x['nom']} » à partir de tes valeurs." if calc else f"Cette grille applique « {x['nom']} » élément par élément.",
                                    "pourquoi": x.get("formule") or " ; ".join(x.get("elements") or []),
                                    "confusion": "Aucune confusion fréquente.", "retenir": (x.get("interpretation") or x.get("regleDeDecision") or "")[:420], "source": x.get("source")},
                                   "outil", type="Calcul utile" if calc else "Critère diagnostique", outil=oid))
                for pp, rx, nom in A_PRODUIRE:
                    if pp == p and re.search(sans_accent(rx), sans_accent(e["nom"])) and not any(x["id"] == f"{pid}__ap_{cle(nom)}" for x in N):
                        N.append(noeud(f"{pid}__ap_{cle(nom)}", "Critère", nom, [eid], "#9aa2b4",
                                       {"def": f"La grille « {nom} » figure au plan (§ 10) ; sa fiche sourcée reste à produire."}, "outil",
                                       type="Critère · à produire", aRediger=True))
        # examens de la fiche technique du prélèvement, absents du catalogue et non couverts par un examen déjà posé
        deja = " | ".join(sans_accent(e["nom"]) for _, e in liste)
        for x in pj.get("examens", []):
            s = sans_accent(re.sub(r"\s*\(.*?\)", "", x["nom"])).strip()
            if s in deja or f"{pid}__fp_{cle(s)[:36]}" in vus:
                continue
            vus.add(f"{pid}__fp_{cle(s)[:36]}")
            a = next((ANAB[r_] for r_ in x.get("analysesRef") or [] if r_ in ANAB), None)
            b = dict(a["bulle"]) if a else {"def": f"L'examen « {x['nom']} » figure dans la fiche technique du prélèvement ; son interprétation reste à produire."}
            N.append(noeud(f"{pid}__fp_{cle(s)[:36]}", "Examen", x["nom"], [pid], coul if a else "#9aa2b4", b, "examen",
                           type="Examen" if a else "Examen · à produire", aRediger=None if a else True))
        for oid in OUTILS.get(p, []):  # outils sans examen correspondant : rattachés au prélèvement
            x = CALC.get(oid) or CRIT.get(oid)
            if not x or (p, oid) in places:
                continue
            calc = oid.startswith("calc_")
            N.append(noeud(f"{pid}__{oid}", "Calcul" if calc else "Critère", x["nom"], [pid], "#0f766e" if calc else "#6d28d9",
                           {"def": f"Ce calculateur exécute la formule « {x['nom']} » à partir de tes valeurs." if calc else f"Cette grille applique « {x['nom']} » élément par élément.",
                            "pourquoi": x.get("formule") or " ; ".join(x.get("elements") or []), "confusion": "Aucune confusion fréquente.",
                            "retenir": (x.get("interpretation") or x.get("regleDeDecision") or "")[:420], "source": x.get("source")},
                           "outil", type="Calcul utile" if calc else "Critère diagnostique", outil=oid))
BIO = N

# ---------------------------------------------------------------- 3. EXPLORATIONS FONCTIONNELLES : fonction → exploration → tracé → interprétation → diagnostic → traitement
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
# Chaîne du prompt : fonction → exploration → tracé ou résultat → interprétation (seuils) → diagnostic → traitement.
# Le sommeil appartient à la Psyché (règle de Vial, plan § 4) : ses diagnostics portent l'étiquette « Psyché ».
FNOM = {"fc": "Psyché, cognition et gériatrie", "fs": "Sommeil et vigilance (Psyché)"}
N = []
for fid, fnom, mesh, cote, coul, rx in FONC:
    N.append(noeud(f"fx_{fid}", "Fonction", FNOM.get(fid, fnom), [], coul, None, "region", organe=mesh, cote=cote, type="Fonction"))
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
    el = el[0] if len(el) == 1 and isinstance(el[0], dict) else {}
    b = bulle_examen(e) if e else {"def": el.get("fonction") or f"L'exploration « {nom} » attend sa fiche."}
    if el.get("fonction") and not (e or {}).get("bulle", {}).get("def"):
        b["def"] = el["fonction"]
    b.setdefault("pourquoi", "Tu choisis l'exploration quand la question porte sur ce que l'organe fait, et non sur ce à quoi il ressemble.")
    b.setdefault("confusion", "Aucune confusion fréquente."); b.setdefault("retenir", "Tu lis le tracé, tu appliques le seuil, puis tu conclus.")
    fen = next((w for r_, w in FEN if re.search(sans_accent(r_), s)), None)
    xid = f"fx_{fid}__{slug[:40]}"; coulf = next(f[4] for f in FONC if f[0] == fid)
    cnt[fid] = cnt.get(fid, 0) + 1
    parent = f"fx_{fid}"
    if fid in SOUS:
        sg = next((g for g, r_ in SOUS[fid] if re.search(sans_accent(r_), s)), SOUS[fid][-1][0])
        parent = f"fx_{fid}_{cle(sg)}"
        if not any(n["id"] == parent for n in N):
            N.append(noeud(parent, "Groupe", sg, [f"fx_{fid}"], coulf, {"def": f"Ce groupe réunit les explorations « {sg.lower()} ».",
                                                                       "pourquoi": "La fonction compte trop d'explorations pour une seule colonne : le groupe garde la toile lisible.",
                                                                       "confusion": "Aucune confusion fréquente.",
                                                                       "retenir": "Tu ouvres le groupe, puis l'exploration dont tu veux le tracé et l'interprétation."}, "region", type="Groupe"))
    plein = bool(el.get("traces") or el.get("diagnostics"))
    N.append(noeud(xid, "Exploration", nom, [parent], coulf if plein or e else "#9aa2b4", b, "examen", type="Endoscopie" if fid == "fx" else "Exploration",
                   exRef=e["id"] if e else None, fiche=o["stem"] if o else None, fenetre=fen, explo=slug if slug in EXPL else None))
    if not plein:
        N.append(noeud(xid + "__ap", "Tracé", "Tracé et interprétation : à produire", [xid], "#9aa2b4",
                       {"def": "Le tracé type, ses seuils et ses diagnostics restent à produire pour cette exploration."}, "trace", type="Tracé · à produire", aRediger=True))
        continue
    tr = el.get("traces") or []
    for i, t in enumerate(tr[:5]):
        norm = t.get("type") == "normal"
        N.append(noeud(f"{xid}__t{i}", "Tracé", t.get("aspect") or t.get("type"), [xid], "#15803d" if norm else "#c2410c",
                       {"def": t.get("description") or "La fiche ne décrit pas encore ce tracé.",
                        "pourquoi": "Le tracé normal sert de référence : tu compares chaque anomalie à lui." if norm else "Ce tracé pathologique s'écarte du tracé normal et oriente l'interprétation.",
                        "confusion": "Aucune confusion fréquente.",
                        "retenir": "Tu appliques ensuite le seuil de la case « Interprétation » pour conclure."}, "trace",
                       type="Tracé normal" if norm else "Tracé pathologique", fenetre=fen))
    iid = xid + "__int"
    seuils = el.get("seuils") or []
    N.append(noeud(iid, "Interprétation", "Interprétation et seuils", [xid], coulf,
                   {"def": (el.get("interpretation") or "La fiche ne détaille pas encore l'interprétation.")[:600],
                    "pourquoi": seuils[0][:600] if seuils else "La fiche ne précise pas encore le seuil.",
                    "confusion": seuils[1][:400] if len(seuils) > 1 else "Aucune confusion fréquente.",
                    "retenir": "Un seuil s'applique sur un tracé de bonne qualité : tu vérifies d'abord la technique."}, "trace", type="Seuils"))
    for i, dg in enumerate((el.get("diagnostics") or [])[:5]):
        nomd = dg.get("diagnostic") or ""; did = f"{iid}__d{i}"; psy = fid in ("fs", "fc")
        arg = dg.get("argument")
        bd = bulle_diag(nomd, arg and f"L'argument décisif est : {arg[0].lower() + arg[1:]}.", None,
                        "Le sommeil appartient à la Psyché : ce diagnostic se prend en charge avec la psychiatrie (plan § 4)." if fid == "fs" else None, nom)
        N.append(noeud(did, "Diagnostic", nomd, [iid], "#6d28d9" if psy else "#d64545", bd, "diag", type="Diagnostic · Psyché" if psy else "Diagnostic"))
        ajouter_traitement(N, did, nomd, "#6d28d9" if psy else "#15803d")
for n in N:
    if n["nature"] == "Fonction":
        k = n["id"][3:]
        n["bulle"] = {"def": f"La fonction « {n['texte']} » se teste par {cnt.get(k, 0)} explorations.",
                      "pourquoi": "Tu pars d'une fonction parce qu'une exploration mesure ce que l'organe fait, et non ce à quoi il ressemble.",
                      "confusion": "Aucune confusion fréquente.",
                      "retenir": "Chaîne du plan : fonction → exploration → tracé ou résultat → interprétation (seuil) → diagnostic → traitement."}
        if k == "fs":
            n["bulle"]["retenir"] = "Le sommeil renvoie à la Psyché : la polysomnographie appartient aux explorations, mais ses diagnostics relèvent de la psychiatrie (plan § 4)."
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
for _k in ("La", "Ta", "Pi"):  # sigles qui sont aussi des mots français courants : le survol se tromperait
    GLO.pop(_k, None)
GLO["PIC"] = "Sigle à deux sens : pression intracrânienne en neurologie ; pneumopathie interstitielle commune (en anglais UIP) en pneumologie, aspect typique de la fibrose pulmonaire idiopathique."
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
