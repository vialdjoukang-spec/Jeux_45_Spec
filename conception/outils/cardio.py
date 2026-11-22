"""Compatibilité : le système cardiovasculaire se lit désormais par systeme_source.charger("cardio")."""
from systeme_source import charger, PALIERS, PALIER_BULLE

_S = charger("cardio")
ORGANES, VOLETS_BULLE, PATHOS, SEMIO, GLOSSAIRE_CV, TEMPS_BULLE = _S["organes"], _S["volets"], _S["pathos"], _S["semio"], _S["glossaire"], _S["temps"]
