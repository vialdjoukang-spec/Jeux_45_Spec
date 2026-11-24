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
    "Pédiatrique (croissance et développement)": {"dossier": "pediatrie", "prefixe": "pe_", "couleur": "#2e8b57", "ids": {"Croissance staturo-pondérale": "org_pediat_croissance_staturo_ponderale", "Développement psychomoteur": "org_pediat_developpement_psychomoteur", "Puberté": "org_pediat_puberte", "Adaptation néonatale (vie extra-utérine)": "org_pediat_adaptation_neonatale_vie_extra", "Génétique et dysmorphies": "org_pediat_genetique_et_dysmorphies"}},
}
SOURCES = {s: charger(c["dossier"]) for s, c in REDIGES.items()}
