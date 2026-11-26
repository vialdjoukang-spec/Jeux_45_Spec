"""Lit les pathologies rédigées de la Tétrade (conception/outils/<système>/pathologies.txt) pour la fiche flash de Paraclinique.
Rien n'est inventé : chaque champ vient d'une fiche Tétrade déjà sourcée et auditée. Signature : AAI (Anthropic AI)."""
import glob, os, re, unicodedata

R = os.path.join(os.path.dirname(__file__), "..")


def sa(s):
    return re.sub(r"[^a-z0-9 ]", " ", unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode()).strip()


def lire():
    F = {}
    for f in sorted(glob.glob(os.path.join(R, "*", "pathologies.txt"))):
        sysn = os.path.basename(os.path.dirname(f)); cur = None
        for l in open(f, encoding="utf-8"):
            l = l.rstrip("\n")
            m = re.match(r"@ (\w+) \| (.+)", l)
            if m:
                cur = {"systeme": sysn, "palier": m.group(1), "nom": m.group(2).strip(), "bilan": [], "traitements": []}
                F[sa(cur["nom"])] = cur; continue
            if not cur:
                continue
            m = re.match(r"(def|pourquoi|confusion|retenir): (.+)", l)
            if m:
                cur[m.group(1)] = m.group(2).strip(); continue
            m = re.match(r"b (\w+) / ([^|]+)\| ([^|]+)\| (.+)", l)
            if m:
                cur["bilan"].append({"visee": m.group(1), "groupe": m.group(2).strip(), "examen": m.group(3).strip(), "signe": m.group(4).strip()}); continue
            m = re.match(r"t ([^|]+)\| (.+)", l)
            if m:
                cur["traitements"].append({"nom": m.group(1).strip(), "detail": m.group(2).strip()}); continue
            if l.startswith("s "):
                cur["source"] = l[2:].strip()
    return F


SYN = {"insuffisance cardiaque gauche": "insuffisance cardiaque", "oedeme pulmonaire cardiogenique": "oedeme aigu du poumon cardiogenique",
       "bpco avec emphyseme": "bronchopneumopathie chronique obstructive", "cancer bronchique": "cancer bronchopulmonaire", "cancer bronchique precoce": "cancer bronchopulmonaire",
       "cancer bronchique non a petites cellules": "cancer bronchopulmonaire", "pneumonie": "pneumonie communautaire",
       "tuberculose": "tuberculose pulmonaire", "pneumothorax": "pneumothorax spontane", "htp tec": "hypertension pulmonaire",
       "bpco ou pneumonie": "bronchopneumopathie chronique obstructive"}


def trouver(F, nom):
    k = sa(nom)
    if k in F:
        return F[k]
    k2 = SYN.get(k)
    if k2:
        for c in F:
            if c.startswith(k2):
                return F[c]
    for c, v in F.items():
        # préfixe accepté seulement si les deux noms ont presque la même longueur : « tumeur ovarienne » ne doit pas
        # hériter de la fiche « tumeur ovarienne virilisante » (correction du 27.11.2026)
        if len(k) > 6 and (c.startswith(k) or k.startswith(c)) and min(len(k), len(c)) / max(len(k), len(c)) >= 0.85:
            return v
    return None


if __name__ == "__main__":
    F = lire(); print(len(F), "pathologies Tétrade")
    import json
    t = json.load(open(os.path.join(R, "..", "donnees", "paraclinique", "niveaux", "poumons_et_voies_aeriennes.json"), encoding="utf-8"))
    for ex, d in t.items():
        if ex.startswith("_"): continue
        for p in d:
            f = trouver(F, p); print(("OK " + f["nom"]) if f else "-- ", "|", p)
