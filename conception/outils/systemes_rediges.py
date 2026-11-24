"""Registre des systèmes rédigés (0 token) : un système s'ajoute ici en une ligne, avec son dossier de sources.
ids : organes dont l'identifiant reste stable (circuits pilotes rattachés). Signature : AAI (Anthropic AI)"""
from systeme_source import charger, PALIERS, PALIER_BULLE

REDIGES = {
    "Cardiovasculaire": {"dossier": "cardio", "prefixe": "cv_", "couleur": "#c0392b", "ids": {"Cœur : myocarde et cavités": "coe"}},
    "Respiratoire": {"dossier": "respi", "prefixe": "rs_", "couleur": "#2f6fd0", "ids": {"Poumons (lobes, segments, acinus)": "pou"}},
    "Digestif & hépatobiliaire": {"dossier": "digestif", "prefixe": "dg_", "couleur": "#c98a2b", "ids": {}},
    "Rénal & uro-génital": {"dossier": "renal", "prefixe": "rn_", "couleur": "#b8960f", "ids": {}},
    "Neurologique": {"dossier": "neuro", "prefixe": "ne_", "couleur": "#8e5cc4", "ids": {}},
    "Endocrinien & métabolique": {"dossier": "endocrino", "prefixe": "en_", "couleur": "#d9731a", "ids": {}},
    "Hématologique & oncologique": {"dossier": "hemato", "prefixe": "he_", "couleur": "#a33", "ids": {}},
    "Infectieux & immunitaire": {"dossier": "infectio", "prefixe": "ii_", "couleur": "#16897b", "ids": {}},
    "Ophtalmologique & ORL": {"dossier": "orl", "prefixe": "or_", "couleur": "#5b6574", "ids": {}},
    "Locomoteur & rhumatologique": {"dossier": "loco", "prefixe": "lo_", "couleur": "#6b7280", "ids": {}},
    "Dermatologique": {"dossier": "derma", "prefixe": "de_", "couleur": "#b07a5a", "ids": {}},
    "Gynéco-obstétrical": {"dossier": "gyneco", "prefixe": "gy_", "couleur": "#c2185b", "ids": {"Seins": "org_gyneco_seins", "Ovaires": "org_gyneco_ovaires", "Trompes": "org_gyneco_trompes", "Utérus et col": "org_gyneco_uterus_et_col", "Vagin et vulve": "org_gyneco_vagin_et_vulve", "Plancher pelvien": "org_gyneco_plancher_pelvien", "Placenta et unité fœto-placentaire": "org_gyneco_placenta_et_unite_fto_placenta"}},
}
SOURCES = {s: charger(c["dossier"]) for s, c in REDIGES.items()}
