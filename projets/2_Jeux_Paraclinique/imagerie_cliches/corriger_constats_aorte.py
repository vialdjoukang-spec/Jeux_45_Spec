"""Corrige les constats Gemini 002, 003, 005, 007 du lot IMG_aorte_abdominale_et_vaisseaux_digestifs (couloir 3).
Sources lues le 28.11.2026 :
- ESVS 2025 (Koelemay et al., Eur J Vasc Endovasc Surg 2025;70(2):153-218, doi 10.1016/j.ejvs.2025.06.010, CC BY 4.0),
  texte intégral version éditeur déposée à Lund : https://lup.lub.lu.se/search/files/231452907/ESVS_GL_final.pdf
- EviPrev 2026, tableau avec annexe FR : https://eviprev.ch/wp-content/uploads/2026/10/EviPrev-tableau_avec_annexe_FR.pdf
Idempotent : relancer ne change rien. Signature : AAI (Anthropic AI)"""
import json, os
RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P = os.path.join(RAC, "conception", "donnees", "paraclinique")
E25 = "ESVS 2025, artères et veines mésentériques et rénales (Koelemay et al., Eur J Vasc Endovasc Surg 2025;70:153-218)"
EVI = "EviPrev 2026 (tableau et annexe, eviprev.ch, lu le 28.11.2026)"
lire = lambda f: json.load(open(f, encoding="utf-8"))
def ecrire(f, d): json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- niveaux (constat 002 ; EviPrev du constat 003)
f = os.path.join(P, "niveaux", "aorte_abdominale_et_vaisseaux_digestifs.json"); N = lire(f)
eco = N["Échographie de l'aorte abdominale"]
eco["Anévrisme de l'aorte abdominale"][2] = "ESVS 2024, anévrismes aorto-iliaques (Wanhainen et al., Eur J Vasc Endovasc Surg 2024;67), recommandations 7 et 11 ; " + EVI + " pour le dépistage suisse (recommandation modérée)"
for p in ("Ectasie aortique", "Aorte sous-anévrismale"):
    eco[p][3]["source"] = "ESVS 2024, anévrismes aorto-iliaques ; " + EVI
AIG = {"premiereIntention": "Angio-CT abdominal urgent aux temps artériel et veineux, quelle que soit la fonction rénale, sans attendre le lactate (un dosage isolé ne confirme ni n'exclut l'ischémie)",
       "goldStandard": "Angio-CT abdominal aux temps artériel et veineux, en coupes de 1 mm au plus",
       "source": E25 + ", recommandations 31 (IIIb C) et 33 (I B)"}
ct = N["Angio-CT abdominal"]
ct["Embolie mésentérique"][1:] = ["L'angio-CT urgent, aux temps artériel et veineux en coupes de 1 mm au plus, montre l'arrêt du contraste dans l'artère mésentérique supérieure.", E25 + ", recommandation 33 (I B)", AIG]
ct["Ischémie mésentérique aiguë"][1:] = ["L'angio-CT se fait en urgence, aux temps artériel et veineux, quelle que soit la fonction rénale.", E25 + ", recommandations 32 (I C) et 33 (I B)", AIG]
CHR = {"premiereIntention": "Échodoppler des artères mésentériques après au moins 4 heures de jeûne",
       "goldStandard": "Angio-CT, imagerie préférée pour le diagnostic et la planification du traitement",
       "source": E25 + ", recommandations 4 (I B) et 5 (I C)"}
dop = N["Échodoppler des artères digestives et rénales"]
dop["Ischémie mésentérique chronique"][1:] = ["Le doppler, après au moins 4 heures de jeûne, mesure les vitesses dans le tronc cœliaque et l'artère mésentérique supérieure.", E25 + ", recommandation 4 (I B)", CHR]
dop["Syndrome du ligament arqué médian"][2:] = [E25 + ", recommandations 26 (IIa C) et 27 (I C)",
    {"premiereIntention": "Échodoppler des artères mésentériques en inspiration puis en expiration",
     "goldStandard": "Aucun examen ne tranche seul : le diagnostic se pose par exclusion, en équipe multidisciplinaire ; l'angio-CT en expiration (sténose localisée, dilatation post-sténotique, sans plaque) le soutient",
     "source": E25 + ", § 3.5.3 et 4.1, recommandations 27 (I C) et 28 (I C)"}]
REN = {"premiereIntention": "Échodoppler des artères rénales", "goldStandard": "Angio-CT ou angio-IRM rénale, préférées à l'angiographie par cathéter pour le diagnostic et la planification",
       "source": E25 + ", recommandations 57 (échodoppler en première ligne) et 59 (angio-CT ou angio-IRM) ; ESC 2024, artères périphériques et aorte"}
dop["Sténose de l'artère rénale"][3] = REN
irm = N["Angio-IRM"]
irm["Ischémie mésentérique chronique"][1:] = ["L'angio-IRM peut remplacer l'angio-CT, sans irradiation, quand l'iode ou les rayons posent problème.", E25 + ", recommandation 6 (IIb C)", CHR]
irm["Sténose athéromateuse rénale"][3] = REN; irm["Sténose de l'artère rénale"][3] = REN
art = N["Artériographie"]
art["Embolie mésentérique"][1:] = ["L'artériographie suit l'angio-CT quand on désobstrue l'artère par voie endovasculaire, voie envisagée en première ligne.", E25 + ", recommandation 37 (IIa B)", AIG]
art["Ischémie mésentérique aiguë occlusive"][1:] = ["L'artériographie sert au geste endovasculaire, envisagé en première ligne, après l'angio-CT diagnostique.", E25 + ", recommandation 37 (IIa B)", AIG]
NOMI = {"premiereIntention": "Angio-CT abdominal aux temps artériel et veineux chez le patient en choc (défaut de rehaussement pariétal, épaississement du grêle, pneumatose, gaz portal, sans occlusion artérielle)",
        "goldStandard": "Artériographie mésentérique, référence historique, qui montre le spasme diffus et permet de perfuser un vasodilatateur",
        "source": E25 + ", § 6.4, recommandations 43 (I C) et 45 (IIb C)"}
for p in ("Ischémie non occlusive", "Ischémie mésentérique non occlusive"):
    art[p][1:] = ["L'artériographie, référence historique, montre le spasme diffus et permet de perfuser un vasodilatateur dans l'artère mésentérique supérieure.", E25 + ", § 6.4 et recommandation 45 (IIb C)", NOMI]
ecrire(f, N)

# ---------- fiches flash (constat 007)
f = os.path.join(P, "fiches_flash", "aorte_abdominale_et_vaisseaux_digestifs.json"); F = lire(f)
for p in ("Embolie mésentérique", "Ischémie mésentérique aiguë", "Ischémie mésentérique aiguë occlusive"):
    x = F[p]
    x["epi"] = "Son incidence atteint 8,7 pour 100 000 habitants par an, et 60,2 après 70 ans, dans un registre national estonien [ESVS 2025]."
    x["moyens"] = [{"general": "Anticoagulation", "specifiques": "héparine non fractionnée IV", "detail": "Dès le diagnostic [Tétrade] ; l'ESVS 2025 traite par héparine seule les petits emboles périphériques résiduels ; posologie à vérifier dans l'AIPS (Swissmedic)."},
                   {"general": "Revascularisation", "specifiques": "endovasculaire ou ouverte, avant la chirurgie intestinale", "detail": "La revascularisation précède la résection intestinale [ESVS 2025, rec. 35, IIa C] ; la voie endovasculaire est envisagée en première ligne pour l'occlusion thrombotique ou embolique de l'artère mésentérique supérieure [ESVS 2025, rec. 37, IIa B]."},
                   {"general": "Chirurgie intestinale", "specifiques": "résection, second look, antibiotiques", "detail": "Résection sans rétablissement immédiat, puis second look [ESVS 2025, rec. 40, IIa C] ; antibiothérapie [ESVS 2025, rec. 41, I C]."}]
    x["source"] = E25 + " ; Tétrade cardiovasculaire."
x = F["Ischémie mésentérique chronique"]
x["epi"] = "Son incidence annuelle atteint 9,2 pour 100 000 habitants dans un centre de référence néerlandais [ESVS 2025]."
x["moyens"] = [{"general": "Revascularisation", "specifiques": "stent de l'artère mésentérique supérieure, chirurgie ouverte", "detail": "Recommandée en cas d'atteinte de plusieurs vaisseaux [ESVS 2025, rec. 9, I B] ; voie endovasculaire d'abord [rec. 14, I B] ; stent plutôt que ballon seul [rec. 15, I C]."},
               {"general": "Traitement médical", "specifiques": "antiagrégant plaquettaire", "detail": "Double antiagrégation courte (au moins un mois, aspirine et clopidogrel) après stent [ESVS 2025, rec. 18, IIb C] ; posologie à vérifier dans l'AIPS (Swissmedic)."}]
x["source"] = E25 + "."
x = F["Syndrome du ligament arqué médian"]
x["meca"] = "La compression extrinsèque du tronc cœliaque, maximale en expiration, réduit son flux ; le diagnostic reste controversé et se pose par exclusion [ESVS 2025]."
x["moyens"] = [{"general": "Libération chirurgicale", "specifiques": "libération du tronc cœliaque par laparoscopie, voie rétropéritonéale vidéo-assistée ou laparotomie", "detail": "La laparoscopie ou la voie rétropéritonéale vidéo-assistée peut être préférée [ESVS 2025, rec. 30, IIb C] ; un bénéfice durable est rapporté dans 80 à 92 % des cas de deux cohortes [ESVS 2025]."}]
x["source"] = E25 + " ; Scand J Surg 2026 (doi 10.1177/14574969261499182) pour l'incidence."
for p in ("Ischémie non occlusive", "Ischémie mésentérique non occlusive"):
    x = F[p]
    x["epi"] = "Sa fréquence globale reste mal connue ; après chirurgie cardiaque, une série prospective l'a confirmée chez 78 de 865 patients (9 %) [ESVS 2025]."
    x["moyens"] = [{"general": "Correction de la cause", "specifiques": "réanimation hémodynamique, baisse de la pression intra-abdominale", "detail": "Laparotomie de décompression urgente en cas de syndrome du compartiment abdominal [ESVS 2025, rec. 44, I C]."},
                   {"general": "Traitement endovasculaire", "specifiques": "vasodilatateur intra-artériel (papavérine ou prostaglandine)", "detail": "Perfusion dans l'artère mésentérique supérieure sous héparine [ESVS 2025, rec. 45, IIb C] ; disponibilité en Suisse et posologie à vérifier sur compendium.ch (AIPS)."}]
    x["source"] = E25 + "."
ecrire(f, F)

# ---------- topographie (constats 003 et 005)
f = os.path.join(P, "topographie", "5_abdomen", "aorte_abdominale_et_vaisseaux_digestifs.json"); T = lire(f); ex = T["examens"]
e0 = ex[0]
e0["indication"] = e0["indication"].replace("selon les recommandations suisses EviPrev 2021 (grade B)", "selon les recommandations suisses EviPrev 2026 (recommandation modérée)").replace("au cas par cas (grade C)", "au cas par cas (recommandation faible)")
e0["bulle"]["retenir"] = e0["bulle"]["retenir"].replace("EviPrev 2021", "EviPrev 2026")
T["glossaire"]["EviPrev"] = "EviPrev est le programme suisse de recommandations de prévention et de dépistage en médecine de premier recours, dont la version citée date de 2026 (tableau et annexe publiés sur eviprev.ch)."
s0 = e0["syndromesParacliniques"][0]
if s0["syndrome"] == "Anévrisme de l'aorte abdominale":
    s0["syndrome"] = "Syndrome vasculaire (anévrisme)"
    s0["anomaliesQuiLeComposent"] = [a for a in s0["anomaliesQuiLeComposent"] if a != "Diamètre aortique d'au moins 30 mm"]
e1 = ex[1]
REN1 = {"Ischémie mésentérique aiguë": "Syndrome ischémique", "Rupture d'anévrisme": "Syndrome hémorragique"}
for s in e1["syndromesParacliniques"]:
    s["syndrome"] = REN1.get(s["syndrome"], s["syndrome"])
if any(a["anomalie"] == "Suspicion non mentionnée sur la demande" for a in e1["anomaliesElementaires"]):
    e1["anomaliesElementaires"] = [a for a in e1["anomaliesElementaires"] if a["anomalie"] != "Suspicion non mentionnée sur la demande"]
    e1["precautions"] += " Selon l'ESVS 2025 (recommandation 32, I C), le clinicien mentionne la suspicion d'ischémie mésentérique aiguë sur la demande d'angio-CT."
e4 = ex[4]
REN4 = {"Ischémie mésentérique non occlusive": "Syndrome vasculaire (vasoconstriction diffuse)", "Ischémie mésentérique aiguë": "Syndrome vasculaire (occlusion)"}
for s in e4["syndromesParacliniques"]:
    s["syndrome"] = REN4.get(s["syndrome"], s["syndrome"])
e4["anomaliesElementaires"] = [a for a in e4["anomaliesElementaires"] if a["anomalie"] != "Ischémie mésentérique non occlusive"]
for p in e4["pathologiesAssociees"]:
    if p["pathologie"] == "Ischémie mésentérique non occlusive" and p["anomalieTypique"] == "Ischémie mésentérique non occlusive":
        p["anomalieTypique"] = "Spasme diffus des branches"
ecrire(f, T)
print("constats 002, 003, 005, 007 : corrections appliquées")
