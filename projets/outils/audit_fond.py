"""Audit de fond des données paracliniques (0 token) : applique les corrections décidées par Claude,
range les notes « à vérifier » (justification acceptée ou doute encore ouvert) et publie les données fiables
dans SORTIES_DONNEES_FIABLES/. Relançable : les corrections sont idempotentes.
Usage : python projets/outils/audit_fond.py
Signature : AAI (Anthropic AI)"""
import json, glob, os, re, datetime

RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TOPO = os.path.join(RAC, "conception/donnees/paraclinique/topographie")
SORTIE = os.path.join(RAC, "SORTIES_DONNEES_FIABLES")
COEUR = ["visees", "signeRecherche", "seuil", "indication", "discriminant", "avantageSelectif", "plutotQue", "limite", "precautions", "irradiation_mSv", "delai"]
COMPLEMENT = ["synonymes", "aspectNormal", "anomaliesElementaires", "syndromesParacliniques", "pathologiesAssociees"]

# 1. Corrections de fond décidées par Claude (audit du 2026-11-22) : (id, champ, ancienne valeur ou motif, nouvelle valeur)
CORRECTIONS = [
    ("colon_rectum_et_anus__colo_ct", "irradiation_mSv", 7.6, 4.4),
    ("plaies_ulceres_et_escarres__irm", "smarterMedicine", re.compile(r"MAOP"), None),
    ("encephale__angio_ct_des_vaisseaux_intracraniens", "irradiation_mSv", 3.5, 1.9),
    ("encephale__ct_de_perfusion", "irradiation_mSv", 4.0, 4.5),
    ("encephale__spectroscopie_irm", "seuil", re.compile(r"^Rapport Cho/NAA >1,5-2"),
     "Un rapport Cho/NAA augmenté, un pic de lactate ou de lipides orientent vers une lésion tumorale ou nécrotique ; le seuil dépend du centre et de la séquence."),
    ("encephale__potentiels_evoques_visuels_auditifs_some", "seuil", re.compile(r"^Latence P100 >115 ms"),
     "Une latence P100 allongée au-delà des normes du laboratoire, ou une asymétrie entre les deux yeux, signe un ralentissement de la conduction visuelle."),
    ("meninges_et_lcr__lcr_bandes_oligoclonales_et_index_igg", "seuil", re.compile(r"^Présence de bandes oligoclonales ou index IgG élevé$"),
     "Au moins deux bandes oligoclonales propres au LCR, ou un index IgG supérieur à 0,7, signent une synthèse intrathécale d'IgG, selon Tibbling et al. (1977) et les critères de McDonald 2017."),
    # audit du 2026-11-23 : typiques adultes OFSP 2018 appliqués à tort à des examens pédiatriques → valeurs pédiatriques sourcées de main
    ("os_du_crane_et_de_la_face__radiographie_du_crane", "irradiation_mSv", 0.3, 0.04),
    ("os_longs_et_squelette__bilan_radiologique_du_squelette", "irradiation_mSv", 3.06, 0.26),
    ("os_longs_et_squelette__age_osseux", "irradiation_mSv", 0.01, 0.0002),
    ("croissance_et_developpement_de_l_enfant__age_osseux", "irradiation_mSv", 0.01, 0.0002),
    ("os_longs_et_squelette__age_osseux", "precautions", re.compile(r"^La dose efficace typique retenue est 0,01 mSv pour les radiographies des membres"),
     "La dose efficace d'une radiographie de la main pour l'âge osseux est d'environ 0,0002 mSv, selon Hart, Wall, Hillier et Shrimpton (rapport HPA-CRCE-012, 2010) ; Mettler et al. (2008) indiquent 0,001 mSv pour les extrémités. On irradie une seule main, habituellement la gauche, et l'on évite de répéter le cliché sans indication."),
    ("croissance_et_developpement_de_l_enfant__age_osseux", "precautions", re.compile(r"^La dose d’une radiographie des membres est d’environ 0,01 mSv"),
     "La dose d'une radiographie de la main pour l'âge osseux est d'environ 0,0002 mSv, selon Hart, Wall, Hillier et Shrimpton (rapport HPA-CRCE-012, 2010). La maturation osseuse s’objective à partir de 3 ans (PEDLAUS, retard de croissance)."),
]
RESOLUTIONS = {  # justification de Claude ajoutée dans _meta.resolutionsClaude
    "encephale__angio_ct_des_vaisseaux_intracraniens": "irradiation_mSv : 1,9 mSv mesurés par dosimètres LiF-TLD pour l'angio-CT intracrânien (Cohnen et al., AJNR 2006).",
    "encephale__ct_de_perfusion": "irradiation_mSv : 4,5 mSv = protocole standard (4,47 ± 0,85 mSv, 391 patients, cohorte d'AVC 2021) ; 2,2 mSv en basse dose.",
    "encephale__spectroscopie_irm": "seuil : chiffre retiré faute de seuil universel ; formulation qualitative.",
    "encephale__potentiels_evoques_visuels_auditifs_some": "seuil : 115 ms retiré, renvoi aux normes du laboratoire.",
    "meninges_et_lcr__lcr_bandes_oligoclonales_et_index_igg": "seuil : index IgG > 0,7 (Tibbling 1977) et ≥ 2 bandes (McDonald 2017), valeurs classiques.",
    "os_du_crane_et_de_la_face__radiographie_du_crane": "irradiation_mSv : 0,3 mSv (typique adulte OFSP 2018) remplacé par 0,04 mSv, borne haute pédiatrique de Mathijssen et al. (2021) : l'indication est le bilan squelettique de l'enfant de moins de 2 ans.",
    "os_longs_et_squelette__bilan_radiologique_du_squelette": "irradiation_mSv : 3,06 mSv (somme de typiques adultes OFSP, sans mesure propre) remplacé par 0,26 mSv, bilan pédiatrique initial et suivi selon Sait et al. (Pediatric Radiology, 2023), cohérent avec le champ precautions.",
    "os_longs_et_squelette__age_osseux": "irradiation_mSv : 0,01 mSv (typique adulte des membres, OFSP 2018) remplacé par 0,0002 mSv, main pour l'âge osseux selon Hart et al. (HPA-CRCE-012, 2010).",
    "croissance_et_developpement_de_l_enfant__age_osseux": "irradiation_mSv : aligné sur 0,0002 mSv (Hart et al., HPA-CRCE-012, 2010), comme l'examen jumeau des os longs.",
    "oeil_et_orbite__fond_d_oeil": "indication : seuil 180/110 non relu dans le texte intégral, remplacé par « hypertension sévère ou urgence hypertensive ».",
}
REMPLACEMENTS_TEXTE = [  # (motif, remplacement) dans toutes les chaînes
    (re.compile(r"Vitamine B12 de 150 à 300 pmol/l"), "Vitamine B12 de 150 à 250 pmol/l"),
    (re.compile(r"une valeur entre 150 et 220 pmol/l constitue une zone grise, et une valeur supérieure à 220 pmol/l rend la carence peu probable, selon Bruttin et al\. \(2021, Revue Médicale Suisse\)"),
     "une valeur entre 150 et 250 pmol/l constitue une zone grise où l'on dose l'acide méthylmalonique (traitement au-delà de 270 nmol/l), selon mediX (2023)"),
    (re.compile(r"Rythme irrégulier de la démence"), "Rythme irrégulier du trouble neurocognitif majeur (démence)"),
    (re.compile(r"une pression artérielle supérieure ou égale à 180/110 mmHg \(24,0/14,7 kPa\)"), "une hypertension sévère ou une urgence hypertensive"),
]
AJOUTS = [  # (id, champ, phrase ajoutée si absente)
    ("os_longs_et_squelette__biopsie_osseuse", "precautions",
     "La biopsie elle-même n'irradie pas ; guidée par CT, elle expose à la dose de ce CT."),
]
# 2. Doutes encore ouverts après audit (repérés par l'id de l'examen et le champ) : ils restent dans aVerifier.
OUVERTS = {  # après l'audit du 2026-11-22 : un seul doute reste ouvert (aucune dose efficace publiée retrouvée)
    ("meninges_et_lcr__cisternographie", "irradiation_mSv"),
    ("hanche_et_bassin__radiographie_du_bassin_de_l_enfant", "irradiation_mSv"),
    # audit du 2026-11-23 (F2_examens_vides) : doses laissées à null faute de valeur sourcée
    ("aorte_thoracique_et_arteres_pulmonaires__catheterisme_cardiaque_droit", "irradiation_mSv"),
    ("mediastin__biopsie_de_masse_mediastinale", "irradiation_mSv"),
    ("ureteres__scintigraphie_mag3", "irradiation_mSv"),
}
VIDES = (None, "", [], {})


def cle_note(note):
    m = re.search(r"([a-z0-9_]+__[a-z0-9_]+)\s*›\s*([\w.]+)", note)
    return (m.group(1), m.group(2)) if m else (None, None)


def coeur_rempli(e):
    return all(e.get(k) not in VIDES for k in COEUR if k in e)


def remplacer(x):
    if isinstance(x, str):
        for m, r in REMPLACEMENTS_TEXTE:
            x = m.sub(r, x)
        return x
    if isinstance(x, list):
        return [remplacer(v) for v in x]
    if isinstance(x, dict):
        return {k: remplacer(v) for k, v in x.items()}
    return x


bilan = {"corrections": 0, "acceptees": 0, "ouvertes": 0, "fiables": 0, "examens": 0}
lignes = []
for f in sorted(glob.glob(os.path.join(TOPO, "*", "*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    avant = json.dumps(d, ensure_ascii=False)
    d["examens"] = remplacer(d["examens"])
    idx = {e["id"]: e for e in d["examens"]}
    for i, champ, ancien, nouveau in CORRECTIONS:
        e = idx.get(i)
        if e and (e.get(champ) == ancien or (hasattr(ancien, "search") and isinstance(e.get(champ), str) and ancien.search(e[champ]))):
            e[champ] = nouveau
    for i, champ, phrase in AJOUTS:
        e = idx.get(i)
        if e and phrase not in (e.get(champ) or ""):
            e[champ] = ((e.get(champ) or "") + " " + phrase).strip()
    if json.dumps(d, ensure_ascii=False) != avant:
        bilan["corrections"] += 1
    # tri des notes
    meta = d["_meta"]
    notes = meta.pop("aVerifier", []) + meta.get("aVerifierOuverts", [])
    ouverts, acceptes = [], meta.get("justificationsAcceptees", [])
    for n in dict.fromkeys(notes):
        (ouverts if cle_note(n) in OUVERTS else acceptes).append(n)
    meta["aVerifierOuverts"], meta["justificationsAcceptees"] = ouverts, list(dict.fromkeys(acceptes))
    res = [f"{i} › {t}" for i, t in RESOLUTIONS.items() if i in idx]
    if res:
        meta["resolutionsClaude"] = res
    meta["auditFond"] = "Audit Claude du 2026-11-22 : corrections appliquées, justifications acceptées, doutes ouverts listés."
    bilan["acceptees"] += len(meta["justificationsAcceptees"]); bilan["ouvertes"] += len(ouverts)
    json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # sortie fiable : examens remplis à ≥ 85 % et sans doute ouvert
    ids_ouverts = {cle_note(n)[0] for n in ouverts}
    fiables = [e for e in d["examens"] if coeur_rempli(e) and e["id"] not in ids_ouverts]
    a_completer = [e["id"] for e in fiables if any(e.get(k) in VIDES for k in COMPLEMENT if k in e)]
    bilan["aCompleter"] = bilan.get("aCompleter", 0) + len(a_completer)
    bilan["examens"] += len(d["examens"]); bilan["fiables"] += len(fiables)
    rel = os.path.relpath(f, TOPO)
    if fiables:
        cible = os.path.join(SORTIE, "paraclinique", rel)
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        json.dump({"_meta": {"region": meta.get("region"), "organe": meta.get("organe"), "source": "conception/donnees/paraclinique/topographie/" + rel,
                             "critere": "cœur clinique rempli et aucun doute ouvert après l'audit de fond Claude", "aCompleter": a_completer},
                   "examens": fiables}, open(cible, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    lignes.append(f"| {meta.get('organe')} | {len(d['examens'])} | {len(fiables)} | {len(ouverts)} |")

os.makedirs(SORTIE, exist_ok=True)
open(os.path.join(SORTIE, "00_LISEZ_MOI.md"), "w", encoding="utf-8").write(
    "# Sorties de données fiables\n\nCe dossier ne contient que les données qui ont passé l'audit de fond de Claude : "
    "un examen y entre si son cœur clinique est rempli (" + ", ".join(COEUR) + ") et si aucun doute ne reste ouvert sur lui. "
    "La liste aCompleter de chaque fichier nomme les examens fiables auxquels il manque encore les champs de présentation (" + ", ".join(COMPLEMENT) + ") : ils partent en lot de complément. "
    "Le jeu peut les charger telles quelles. Les sources de travail restent dans `conception/donnees/` ; "
    "ce dossier est régénéré par `python projets/outils/audit_fond.py`.\n\n"
    f"Mise à jour : {datetime.date.today()} · {bilan['fiables']} examens fiables sur {bilan['examens']} · "
    f"{bilan.get('aCompleter', 0)} à compléter en présentation · {bilan['acceptees']} justifications acceptées · {bilan['ouvertes']} doutes encore ouverts.\n\n"
    "| Organe | Examens | Fiables | Doutes ouverts |\n|---|---|---|---|\n" + "\n".join(lignes) + "\n\nSignature : AAI (Anthropic AI)\n")
print(bilan)
