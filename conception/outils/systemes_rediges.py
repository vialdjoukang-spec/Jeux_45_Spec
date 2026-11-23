"""Registre des systèmes rédigés (0 token) : un système s'ajoute ici en une ligne, avec son dossier de sources.
ids : organes dont l'identifiant reste stable (circuits pilotes rattachés). Signature : AAI (Anthropic AI)"""
from systeme_source import charger, PALIERS, PALIER_BULLE

REDIGES = {
    "Cardiovasculaire": {"dossier": "cardio", "prefixe": "cv_", "couleur": "#c0392b", "ids": {"Cœur : myocarde et cavités": "coe"}},
    "Respiratoire": {"dossier": "respi", "prefixe": "rs_", "couleur": "#2f6fd0", "ids": {"Poumons (lobes, segments, acinus)": "pou"}},
    "Digestif & hépatobiliaire": {"dossier": "digestif", "prefixe": "dg_", "couleur": "#c98a2b", "ids": {}},
    "Rénal & uro-génital": {"dossier": "renal", "prefixe": "rn_", "couleur": "#b8960f", "ids": {}},
    "Neurologique": {"dossier": "neuro", "prefixe": "ne_", "couleur": "#8e5cc4", "ids": {}},
}
SOURCES = {s: charger(c["dossier"]) for s, c in REDIGES.items()}
