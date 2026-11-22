"""Catalogue des analyses biologiques INDIVIDUELLES (une analyse = une valeur de référence).
Source unique des valeurs : biologie/analyses/<famille>.json. Les prélèvements ne portent que la technique.
Chaque famille : (prélèvement par défaut, [analyses]). Une analyse peut préciser son prélèvement : "nom | prelevement"."""

FAMILLES = {
    "01_Hematologie": ("sang_veineux", [
        "Hémoglobine", "Hématocrite", "Érythrocytes", "VGM", "TCMH", "CCMH", "RDW", "Réticulocytes",
        "Leucocytes", "Neutrophiles", "Lymphocytes", "Monocytes", "Éosinophiles", "Basophiles", "Thrombocytes",
        "Frottis sanguin (schistocytes, blastes, sphérocytes)", "Vitesse de sédimentation (VS)", "Ferritine", "Fer sérique",
        "Transferrine et coefficient de saturation", "Vitamine B12", "Holotranscobalamine", "Acide folique", "Haptoglobine",
        "Bilirubine libre", "Test de Coombs direct", "Test de Kleihauer", "Cytométrie en flux (immunophénotypage)", "JAK2 V617F, CALR, MPL", "Électrophorèse de l'hémoglobine", "Typage sanguin ABO-Rhésus et recherche d'agglutinines irrégulières"]),
    "02_Hemostase": ("sang_veineux", [
        "TP (Quick) et INR", "aPTT", "Fibrinogène", "D-dimères", "Temps de thrombine", "Activité anti-Xa",
        "Facteur VIII", "Facteur IX", "Facteur de von Willebrand (antigène et activité)", "Antithrombine", "Protéine C", "Protéine S",
        "Facteur V Leiden", "Mutation de la prothrombine G20210A", "Anticoagulant lupique", "Anticorps anticardiolipine et anti-β2-glycoprotéine I",
        "Anticorps anti-PF4/héparine (TIH)", "Bilan de thrombophilie (panel)"]),
    "03_Electrolytes_Rein_Acide-base": ("sang_veineux", [
        "Sodium", "Potassium", "Chlorure", "Bicarbonate", "Calcium total", "Calcium ionisé", "Phosphate", "Magnésium",
        "Créatinine", "Urée", "DFG estimé (CKD-EPI)", "Cystatine C", "Acide urique", "Osmolalité plasmatique",
        "pH artériel | sang_arteriel", "PaO2 | sang_arteriel", "PaCO2 | sang_arteriel", "Excès de base | sang_arteriel", "Lactate",
        "SaO2 | sang_arteriel", "Carboxyhémoglobine | sang_arteriel", "Méthémoglobine | sang_arteriel"]),
    "04_Foie_Pancreas_Digestif": ("sang_veineux", [
        "ASAT", "ALAT", "GGT", "Phosphatase alcaline", "Bilirubine totale", "Bilirubine conjuguée", "Albumine", "Protéines totales",
        "Préalbumine", "Ammoniémie", "Lipase", "Amylase", "Céruloplasmine", "Cuivre urinaire | urine", "Alpha-1-antitrypsine",
        "Calprotectine fécale | selles", "Élastase fécale | selles", "Test immunochimique de sang occulte fécal (FIT) | selles",
        "Antigène Helicobacter pylori fécal | selles", "Test respiratoire à l'urée C13 | air_expire",
        "Anticorps anti-transglutaminase IgA", "IgA totales",
        "Sérologie hépatite A (IgM anti-VHA)", "Hépatite B : AgHBs, anti-HBs, anti-HBc, ADN du VHB", "Hépatite C : anti-VHC et ARN du VHC", "Hépatite D : anticorps anti-VHD", "Hépatite E : IgM anti-VHE et ARN", "IgG4 sériques", "Test respiratoire à l'hydrogène | air_expire"]),
    "05_Cardiaque_Vasculaire_Lipides": ("sang_veineux", [
        "Troponine T hypersensible", "Troponine I hypersensible", "CK", "CK-MB", "Myoglobine", "NT-proBNP", "BNP",
        "Cholestérol total", "LDL-cholestérol", "HDL-cholestérol", "Triglycérides", "Lp(a)", "Apolipoprotéine B", "Homocystéine"]),
    "06_Diabete_Thyroide_Phosphocalcique": ("sang_veineux", [
        "Glucose", "HbA1c", "Insuline", "Peptide C", "Cétonémie (β-hydroxybutyrate)", "Glycémie capillaire | sang_capillaire",
        "TSH", "T4 libre", "T3 libre", "Anticorps anti-TPO", "Anticorps anti-thyroglobuline", "TRAb (anti-récepteur de la TSH)",
        "Thyroglobuline", "Calcitonine", "PTH", "25-OH-vitamine D", "CTX (télopeptide C)", "P1NP", "Phosphatase alcaline osseuse", "HGPO 75 g (hyperglycémie provoquée orale)"]),
    "15_Surrenales_Gonades_Hypophyse_Neuroendocrine": ("sang_veineux", [
        "Cortisol sérique", "ACTH", "Cortisol salivaire nocturne | salive",
        "Cortisol libre urinaire de 24 h | urine", "Aldostérone", "Rénine", "Métanéphrines plasmatiques libres", "Métanéphrines urinaires | urine",
        "DHEA-S", "17-OH-progestérone", "Testostérone", "SHBG", "LH", "FSH", "Œstradiol", "Progestérone", "Prolactine",
        "β-hCG", "AMH", "IGF-1", "Hormone de croissance (GH)", "Copeptine", "Chromogranine A", "Gastrine", "Rapport sFlt-1/PlGF", "Fibronectine fœtale | prelevements_genitaux_et_uretraux"]),
    "07_Inflammation_Infection_Microbiologie": ("sang_veineux", [
        "CRP", "Procalcitonine", "Hémocultures | hemocultures", "Test VIH combiné (antigène p24 et anticorps)", "Charge virale VIH",
        "Lymphocytes T CD4", "Syphilis : TPPA et VDRL/RPR", "Sérologie CMV", "Sérologie EBV", "Sérologie toxoplasmose", "Sérologie rubéole",
        "Sérologie varicelle-zona", "Sérologie de la borréliose (avec immunoblot)", "Test de libération d'interféron gamma (IGRA)",
        "Galactomannane aspergillaire", "β-D-glucane", "Antigènes urinaires pneumocoque et légionelle | urine",
        "Recherche de paludisme (frottis, goutte épaisse, test rapide)", "PCR respiratoire multiplex | ecouvillons_nasopharynges_et_de_gorge",
        "Test rapide du streptocoque A | ecouvillons_nasopharynges_et_de_gorge", "Sérologie parvovirus B19", "Recherche de microfilaires", "Sérologies du voyageur (dengue, chikungunya, schistosomiase)", "Précipitines (pneumopathie d'hypersensibilité)"]),
    "08_Immunologie_Autoimmunite_Allergie": ("sang_veineux", [
        "Anticorps antinucléaires (ANA)", "Anticorps anti-ADN natif", "Anticorps anti-ENA", "ANCA (anti-PR3, anti-MPO)", "Anticorps anti-MBG",
        "Anticorps anti-PLA2R", "Facteur rhumatoïde", "Anticorps anti-CCP", "Complément C3", "Complément C4", "CH50",
        "Immunoglobulines IgG, IgA, IgM", "IgE totales", "IgE spécifiques", "Tryptase sérique", "Électrophorèse des protéines sériques",
        "Immunofixation sérique et urinaire", "Chaînes légères libres sériques (kappa, lambda)", "Cryoglobulines",
        "Anticorps des myosites (anti-Jo-1, anti-HMGCR, anti-SRP, anti-Mi-2)", "Anticorps anti-récepteur de l'acétylcholine", "Anticorps anti-MuSK",
        "Anticorps anti-AQP4", "Anticorps anti-MOG", "Anticorps anti-neuronaux (encéphalites auto-immunes)", "Anticorps anti-gangliosides", "Anticorps anti-MAG",
        "Anticorps anti-facteur intrinsèque", "Anticorps anti-cellules pariétales", "Auto-anticorps hépatiques (anti-muscle lisse, anti-LKM1, AMA)", "HLA-B27", "Anticorps anti-SSA et anti-SSB", "Enzyme de conversion de l'angiotensine (ECA)", "Électrophorèse des protéines urinaires | urine", "Immunofluorescence indirecte cutanée (dermatoses bulleuses)"]),
    "09_Marqueurs_tumoraux": ("sang_veineux", [
        "PSA total et libre", "ACE", "CA 19-9", "CA-125", "HE4", "CA 15-3", "AFP", "LDH", "NSE", "β2-microglobuline"]),
    "10_Toxicologie_Dosages_medicamenteux": ("sang_veineux", [
        "Éthanolémie", "CDT (transferrine carboxy-déficiente)", "PEth (phosphatidyléthanol)", "Paracétamolémie", "Salicylémie",
        "Lithiémie", "Digoxinémie", "Valproate", "Carbamazépine", "Phénytoïne", "Lamotrigine", "Clozapine et norclozapine",
        "Vancomycine", "Aminosides (gentamicine, amikacine)", "Tacrolimus", "Ciclosporine",
        "Dépistage urinaire des drogues (immunoessai) | urine", "Cholinestérases", "Plombémie", "Toxicologie capillaire | cheveux_et_ongles"]),
    "11_Urines": ("urine", [
        "Bandelette urinaire", "Sédiment urinaire", "Uroculture", "Rapport protéines/créatinine urinaire", "Rapport albumine/créatinine urinaire",
        "Sodium urinaire", "Potassium urinaire", "Chlorure urinaire", "Créatinine urinaire", "Osmolalité urinaire", "Calciurie de 24 h",
        "Cytologie urinaire", "Analyse de calcul urinaire", "Test de grossesse urinaire (β-hCG)"]),
    "12_Genetique": ("sang_veineux", [
        "Caryotype", "CGH-array (analyse chromosomique sur puce)", "FISH", "Mutation HFE (hémochromatose)",
        "Test de la sueur (chlorures) | sueur", "Pharmacogénétique (CYP2D6, CYP2C19, HLA-B*57:01, HLA-B*15:02)", "Séquençage de panel de gènes, exome, génome", "BRCA1/2", "Test prénatal non invasif (ADN fœtal libre)", "Dépistage néonatal (carte de Guthrie) | sang_capillaire"]),
    "13_Microbiologie_Prelevements_locaux": ("ecouvillons_nasopharynges_et_de_gorge", [
        "Coproculture et PCR multiplex des selles | selles", "Toxines de Clostridioides difficile | selles", "Parasitologie des selles | selles",
        "Expectorations : Gram, culture, BAAR, PCR tuberculose | expectorations_et_lavage_bronchoalveolaire", "PCR Chlamydia trachomatis et gonocoque | prelevements_genitaux_et_uretraux",
        "Prélèvement vaginal : examen direct, pH, culture | prelevements_genitaux_et_uretraux", "Frottis cervical et test HPV | prelevements_genitaux_et_uretraux",
        "PCR HSV et VZV sur lésion", "Examen mycologique direct et culture | cheveux_et_ongles", "Prélèvement conjonctival (culture, PCR)",
        "Spermogramme et spermoculture | sperme", "Uricult (culture d'urine) | urine", "Culture de pus ou de prélèvement profond (abcès, plaie, otorrhée)", "Streptocoque B (frottis vagino-rectal) | prelevements_genitaux_et_uretraux", "Cytologie d'un écoulement mamelonnaire"]),
    "14_LCR_Liquides_de_ponction": ("liquide_cephalorachidien", [
        "LCR : cellules et formule", "LCR : protéines", "LCR : glucose et rapport LCR/sang", "LCR : lactate", "LCR : Gram, culture, PCR multiplex",
        "LCR : bandes oligoclonales et index IgG", "LCR : xanthochromie (spectrophotométrie)", "LCR : cytologie", "LCR : Aβ42, tau, p-tau",
        "Neurofilaments à chaîne légère (NfL) | sang_veineux",
        "Liquide pleural : protéines et LDH (critères de Light) | liquide_pleural", "Liquide pleural : pH, glucose, cellules | liquide_pleural",
        "Liquide d'ascite : albumine (gradient) et polynucléaires | liquide_d_ascite", "Liquide synovial : cellules et cristaux | liquide_synovial",
        "Liquide péricardique : cellules, culture, cytologie | liquide_pericardique", "Humeur aqueuse (ponction de chambre antérieure) : PCR"]),
}


# Synonymes employés dans les fiches d'organes (clé normalisée de l'analyse → expressions qui la désignent)
ALIAS = {
    "sodium": ["ionogramme", "natremie"], "potassium": ["ionogramme", "kaliemie"], "chlorure": ["ionogramme"], "bicarbonate": ["ionogramme", "bicarbonates"],
    "hemoglobine": ["fsc", "formule sanguine"], "hematocrite": ["fsc"], "erythrocytes": ["fsc"], "vgm": ["fsc"], "leucocytes": ["fsc", "formule sanguine"],
    "neutrophiles": ["fsc", "formule leucocytaire"], "lymphocytes": ["fsc", "formule leucocytaire"], "thrombocytes": ["fsc", "plaquettes"],
    "cholesterol total": ["bilan lipidique", "lipides"], "ldl cholesterol": ["bilan lipidique", "lipides"], "hdl cholesterol": ["bilan lipidique"], "triglycerides": ["bilan lipidique"],
    "ph arteriel": ["gazometrie"], "pao2": ["gazometrie"], "paco2": ["gazometrie"], "exces de base": ["gazometrie"], "sao2": ["gazometrie"],
    "tp quick et inr": ["tp inr", "inr"], "troponine t hypersensible": ["troponine"], "troponine i hypersensible": ["troponine"], "cortisol serique": ["cortisol"],
    "ethanolemie": ["alcoolemie"], "lithiemie": ["lithium"], "digoxinemie": ["digoxine"], "vancomycine": ["vancomycine"], "tacrolimus": ["tacrolimus"],
    "valproate": ["antiepileptiques"], "carbamazepine": ["antiepileptiques"], "lamotrigine": ["antiepileptiques"], "phenytoine": ["antiepileptiques"],
    "aminosides": ["aminosides"], "clozapine et norclozapine": ["psychotropes"], "test vih combine": ["vih"], "syphilis tppa et vdrl rpr": ["syphilis"],
    "vitesse de sedimentation": ["vs"], "dfg estime": ["dfg"], "anticorps antinucleaires": ["ana"], "anca": ["anca"],
    "anticorps anti adn natif": ["anti adn natif"], "anticorps anti ena": ["anti ena"], "anticorps anti mbg": ["anti mbg"], "anticorps anti pla2r": ["anti pla2r"],
    "complement c3": ["c3"], "complement c4": ["c4"], "ch50": ["ch50"], "electrophorese des proteines seriques": ["electrophorese des proteines", "electrophorese et immunofixation"],
    "immunofixation serique et urinaire": ["immunofixation"], "chaines legeres libres seriques": ["chaines legeres libres"], "tryptase serique": ["tryptase"],
    "immunoglobulines igg iga igm": ["immunoglobulines", "igg igm"], "lymphocytes t cd4": ["cd4"], "igg4 seriques": ["igg4"],
    "hepatite b agHBs anti hbs anti hbc adn du vhb": ["hepatites"], "hepatite b aghbs anti hbs anti hbc adn du vhb": ["hepatites", "hepatite b"],
    "hepatite c anti vhc et arn du vhc": ["hepatites", "hepatite c"], "hepatite e igm anti vhe et arn": ["hepatites"], "hepatite d anticorps anti vhd": ["hepatites"],
    "serologie hepatite a": ["hepatites"], "serologie de la borreliose": ["lyme"], "serologie parvovirus b19": ["parvovirus"],
    "test de liberation d interferon gamma": ["igra"], "antigenes urinaires pneumocoque et legionelle": ["antigenuries"],
    "test immunochimique de sang occulte fecal": ["fit"], "antigene helicobacter pylori fecal": ["antigene helicobacter"],
    "facteur viii": ["facteurs de coagulation"], "facteur ix": ["facteurs de coagulation"], "facteur de von willebrand": ["von willebrand"],
    "bilan de thrombophilie": ["thrombophilie"], "jak2 v617f calr mpl": ["jak2"], "cytometrie en flux": ["cytometrie en flux", "immunophenotypage"],
    "typage sanguin abo rhesus et recherche d agglutinines irregulieres": ["groupe sanguin"], "hgpo 75 g": ["hgpo"], "rapport sflt 1 plgf": ["sflt 1 plgf"],
    "ctx": ["ctx"], "p1np": ["p1np"], "gastrine": ["gastrinemie"], "precipitines": ["precipitines"], "recherche de microfilaires": ["microfilaires"],
    "electrophorese des proteines urinaires": ["electrophorese des proteines urinaires"], "immunofluorescence indirecte cutanee": ["immunofluorescence indirecte"],
    "sequencage de panel de genes exome genome": ["panel de genes", "tests genetiques"], "brca1 2": ["brca1"], "test prenatal non invasif": ["test prenatal non invasif"],
    "depistage neonatal": ["guthrie"], "test respiratoire a l hydrogene": ["hydrogene"], "toxicologie capillaire": ["toxicologie"],
    "depistage urinaire des drogues": ["screening toxicologique", "toxicologie sanguine et urinaire"],
    "coproculture et pcr multiplex des selles": ["coproculture"], "toxines de clostridioides difficile": ["clostridioides"], "parasitologie des selles": ["parasitologie des selles"],
    "expectorations gram culture baar pcr tuberculose": ["expectorations"], "pcr chlamydia trachomatis et gonocoque": ["chlamydia"],
    "prelevement vaginal examen direct ph culture": ["prelevements vaginaux"], "frottis cervical et test hpv": ["frottis cervical"], "pcr hsv et vzv sur lesion": ["pcr hsv"],
    "examen mycologique direct et culture": ["mycologique"], "prelevement conjonctival": ["conjonctival"], "spermogramme et spermoculture": ["spermogramme", "culture d urine et de sperme"],
    "uricult": ["uricult", "culture d urine"], "uroculture": ["culture d urine", "uricult"], "test rapide du streptocoque a": ["streptocoque a"],
    "pcr respiratoire multiplex": ["ecouvillon nasopharynge", "pcr virales", "panels multiplex"],
    "lcr cellules et formule": ["lcr", "ponction lombaire"], "lcr proteines": ["lcr", "dissociation albuminocytologique"], "lcr glucose et rapport lcr sang": ["lcr"],
    "lcr lactate": ["lcr"], "lcr gram culture pcr multiplex": ["lcr gram"], "lcr bandes oligoclonales et index igg": ["bandes oligoclonales", "lcr myelite"],
    "lcr xanthochromie": ["xanthochromie"], "lcr cytologie": ["lcr cytologie"], "lcr a 42 tau p tau": ["neurodegenerescence"], "neurofilaments a chaine legere": ["nfl"],
    "liquide pleural proteines et ldh": ["liquide pleural", "light"], "liquide pleural ph glucose cellules": ["liquide pleural"],
    "liquide d ascite albumine et polynucleaires": ["ascite"], "liquide synovial cellules et cristaux": ["liquide synovial"],
    "liquide pericardique cellules culture cytologie": ["liquide pericardique"], "humeur aqueuse pcr": ["chambre anterieure"],
    "phosphatase alcaline osseuse": ["remodelage"],
    "anticorps anti ssa et anti ssb": ["anti ssa"], "enzyme de conversion de l angiotensine": ["enzyme de conversion"],
    "culture de pus ou de prelevement profond": ["culture d abces", "prelevement profond", "otorrhee"], "streptocoque b": ["streptocoque b"],
    "cytologie d un ecoulement mamelonnaire": ["ecoulement mamelonnaire"], "serologies du voyageur": ["serologies du voyageur"],
    "fibronectine foetale": ["fibronectine"], "test de kleihauer": ["kleihauer"],
    "serologie ebv": ["serologies ebv", "mononucleose", "ebv"], "serologie cmv": ["cmv"], "test de liberation d interferon gamma": ["igra", "interferon gamma"],
    "liquide synovial cellules et cristaux": ["liquide synovial", "ponction articulaire", "ponction de hanche", "ponction du 1er metatarso"],
    "prelevement vaginal examen direct ph culture": ["prelevements vaginaux", "prelevement vaginal"],
}


def analyses():
    """→ liste [(famille, nom, prelevement)]"""
    out = []
    for fam, (prel, lst) in FAMILLES.items():
        for a in lst:
            nom, _, p = a.partition(" | ")
            out.append((fam, nom.strip(), (p or prel).strip()))
    return out
