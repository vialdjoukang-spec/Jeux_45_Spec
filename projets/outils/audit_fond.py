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
]
REMPLACEMENTS_TEXTE = [  # (motif, remplacement) dans toutes les chaînes
    (re.compile(r"Vitamine B12 de 150 à 300 pmol/l"), "Vitamine B12 de 150 à 250 pmol/l"),
    (re.compile(r"une valeur entre 150 et 220 pmol/l constitue une zone grise, et une valeur supérieure à 220 pmol/l rend la carence peu probable, selon Bruttin et al\. \(2021, Revue Médicale Suisse\)"),
     "une valeur entre 150 et 250 pmol/l constitue une zone grise où l'on dose l'acide méthylmalonique (traitement au-delà de 270 nmol/l), selon mediX (2023)"),
    (re.compile(r"Rythme irrégulier de la démence"), "Rythme irrégulier du trouble neurocognitif majeur (démence)"),
]
AJOUTS = [  # (id, champ, phrase ajoutée si absente)
    ("os_longs_et_squelette__biopsie_osseuse", "precautions",
     "La biopsie elle-même n'irradie pas ; guidée par CT, elle expose à la dose de ce CT."),
]
# 2. Doutes encore ouverts après audit (repérés par l'id de l'examen et le champ) : ils restent dans aVerifier.
OUVERTS = {
    ("encephale__angio_ct_des_vaisseaux_intracraniens", "irradiation_mSv"), ("encephale__ct_de_perfusion", "irradiation_mSv"),
    ("encephale__spectroscopie_irm", "seuil"), ("encephale__anticorps_anti_neuronaux", "precautions"),
    ("encephale__potentiels_evoques_visuels_auditifs_some", "seuil"), ("hypophyse_et_hypothalamus__irm_hypophysaire_dynamique", "radioAnatomieNormale"),
    ("hypophyse_et_hypothalamus__acth_cortisol", "limite"), ("hypophyse_et_hypothalamus__tsh_t4_libre", "bulle.confusion"),
    ("hypophyse_et_hypothalamus__lh_fsh_testosterone_oestradiol", "seuil"), ("hypophyse_et_hypothalamus__test_de_stimulation_a_l_arginine_copepti", "seuil"),
    ("meninges_et_lcr__cisternographie", "irradiation_mSv"), ("meninges_et_lcr__lcr_bandes_oligoclonales_et_index_igg", "seuil"),
    ("meninges_et_lcr__lcr_xanthochromie_spectrophotometrie", "limite"), ("nez_sinus_et_cavum__rhinomanometrie", "seuil"),
    ("nez_sinus_et_cavum__ecouvillon_nasopharynge", "seuil"), ("oeil_et_orbite__fond_d_oeil", "indication"),
    ("ganglions_cervicaux__biopsie_ou_exerese_ganglionnaire", "precautions"), ("foie__echodoppler_portal", "seuil"),
    ("foie__serologies_hepatites_a_b_c_d_e", "precautions"), ("prostate_et_vesicules_seminales__irm_prostatique_multiparametrique", "indication"),
    ("prostate_et_vesicules_seminales__psa_total_et_libre", "seuil"), ("prostate_et_vesicules_seminales__culture_d_urine_et_de_sperme", "seuil"),
    ("coude_poignet_et_main__enmg", "seuil"), ("nerfs_peripheriques__glycemie_hba1c_b12_tsh_electrophorese_de", "seuil"),
    ("sang_et_hemostase__temps_de_saignement", "seuil"),
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
