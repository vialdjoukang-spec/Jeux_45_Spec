"""Clichés ciblés (passage ouvrier P3) : requêtes anglaises écrites à la main pour les entités sans cliché, par ordre de fréquence clinique.
Réutilise commons() et openi() de chercher_cliches.py ; filtre le titre sur des mots obligatoires (pertinence) ; jamais de SVG ; génital externe exclu.
Usage : python projets/outils/cliches_cibles.py [début fin]   Signature : AAI (Anthropic AI)"""
import json, os, re, sys, glob, time
RAC = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src = open(os.path.join(RAC, "projets/outils/chercher_cliches.py"), encoding="utf-8").read().split("args = sys.argv")[0]
exec(src)
# id : (requêtes, mots obligatoires dans le titre)
CIBLES = [
 ("seins__mammographie", ["mammography BI-RADS", "mammogram breast cancer"], r"mammo"),
 ("aorte_thoracique_et_arteres_pulmonaires__radiographie_thoracique", ["chest radiograph widened mediastinum aortic dissection"], r"mediastin|aort"),
 ("diaphragme_et_muscles_respiratoires__radiographie_thoracique", ["chest radiograph elevated hemidiaphragm"], r"diaphragm"),
 ("poumons_et_voies_aeriennes__echographie_pulmonaire", ["lung ultrasound B-lines", "lung ultrasound consolidation"], r"lung|pulmon|B-line|pleural"),
 ("thyroide__echographie_thyroidienne", ["thyroid ultrasound nodule", "thyroid sonography TIRADS"], r"thyroid"),
 ("thyroide__scintigraphie_thyroidienne", ["thyroid scintigraphy", "thyroid scan technetium"], r"thyroid"),
 ("vesicule_et_voies_biliaires__echographie_abdominale", ["gallbladder ultrasound gallstones", "cholecystitis ultrasound"], r"gallbladder|gallstone|cholecyst|biliary"),
 ("vesicule_et_voies_biliaires__ct_abdominal", ["CT abdomen cholecystitis", "CT gallbladder"], r"gallbladder|cholecyst|biliary"),
 ("vesicule_et_voies_biliaires__scintigraphie_hepatobiliaire", ["HIDA scan hepatobiliary scintigraphy"], r"HIDA|hepatobiliary|cholescint"),
 ("ureteres__echographie", ["hydronephrosis ultrasound"], r"hydroneph|ureter"),
 ("ureteres__scintigraphie_mag3", ["MAG3 renography"], r"MAG3|renogra|renal scint"),
 ("reins__scintigraphie_dmsa", ["DMSA scan renal scarring"], r"DMSA|renal"),
 ("reins__echodoppler_des_arteres_renales", ["renal artery stenosis Doppler ultrasound"], r"renal artery"),
 ("coeur_et_pericarde__scintigraphie_de_perfusion_myocardique", ["myocardial perfusion SPECT"], r"myocard|SPECT|perfusion"),
 ("coeur_et_pericarde__echocardiographie_de_stress", ["stress echocardiography"], r"stress echo|echocardiograph"),
 ("aorte_thoracique_et_arteres_pulmonaires__echocardiographie_transthoracique", ["transthoracic echocardiogram parasternal long axis"], r"echocardio|parasternal|TTE"),
 ("aorte_thoracique_et_arteres_pulmonaires__scintigraphie_de_ventilation_perfusion", ["ventilation perfusion scan pulmonary embolism"], r"ventilation|V/Q|perfusion"),
 ("aorte_thoracique_et_arteres_pulmonaires__angiographie_pulmonaire", ["CT pulmonary angiography embolism", "pulmonary angiography"], r"pulmonary|embol"),
 ("estomac_et_duodenum__radiographie_de_l_abdomen_debout", ["pneumoperitoneum erect abdominal radiograph", "free air under diaphragm radiograph"], r"pneumoperiton|free air|perforat"),
 ("estomac_et_duodenum__gastroscopie_avec_biopsies", ["gastroscopy Helicobacter pylori gastritis", "endoscopy gastric ulcer"], r"gastr|ulcer|helicobacter|pylori"),
 ("oesophage__oesophagogastroduodenoscopie_avec_biopsi", ["esophagogastroduodenoscopy esophagitis", "endoscopy Barrett esophagus"], r"oesoph|esoph|barrett|endoscop"),
 ("veines_caves_et_systeme_porte__gastroscopie", ["esophageal varices endoscopy"], r"varic"),
 ("colon_rectum_et_anus__colo_ct", ["CT colonography virtual colonoscopy"], r"colonograph|virtual colonoscop|CT colon"),
 ("colon_rectum_et_anus__biopsies_coliques", ["colon biopsy histology ulcerative colitis", "microscopic colitis histology"], r"colitis|colon|crohn"),
 ("intestin_grele__echographie_des_anses", ["Crohn disease bowel ultrasound wall thickening"], r"crohn|bowel|ultraso"),
 ("appendice__irm_sans_injection", ["MRI appendicitis"], r"appendic"),
 ("rate__echographie_abdominale", ["spleen ultrasound splenomegaly"], r"splen"),
 ("rate__pet_ct", ["spleen lymphoma PET-CT"], r"splen|lymphoma"),
 ("moelle_osseuse_et_ganglions__pet_ct", ["lymphoma PET-CT Deauville", "lymphoma FDG PET"], r"lymphoma|PET|FDG"),
 ("moelle_osseuse_et_ganglions__biopsie_osteomedullaire", ["bone marrow biopsy trephine histology"], r"marrow|trephine"),
 ("moelle_osseuse_et_ganglions__ct_thoraco_abdominopelvien", ["CT chest abdomen pelvis lymphadenopathy"], r"CT|lymph"),
 ("urgences_et_point_of_care__echographie_au_lit_du_patient", ["point of care ultrasound FAST", "POCUS lung ultrasound BLUE protocol"], r"FAST|POCUS|point.of.care|BLUE|ultraso"),
 ("rachis_osseux__radiographie_du_rachis_entier", ["scoliosis radiograph whole spine", "EOS scoliosis"], r"scolio"),
 ("rachis_osseux__scintigraphie_osseuse", ["bone scintigraphy whole body metastases"], r"scintigra|bone scan"),
 ("paroi_thoracique_et_cotes__scintigraphie_osseuse", ["bone scan rib fracture", "bone scintigraphy"], r"scintigra|bone scan"),
 ("rachis_osseux__osteodensitometrie", ["DXA bone density lumbar spine"], r"DXA|DEXA|densitom|bone density"),
 ("os_longs_et_squelette__osteodensitometrie", ["DEXA scan T-score osteoporosis"], r"DXA|DEXA|densitom|bone density"),
 ("rachis_osseux__ponction_biopsie_vertebrale", ["spondylodiscitis MRI", "CT guided vertebral biopsy"], r"spondyl|vertebr|discitis"),
 ("genou__radiographie_du_genou", ["knee radiograph anteroposterior lateral", "knee osteoarthritis radiograph"], r"knee"),
 ("genou__arthroscopie", ["knee arthroscopy meniscus"], r"arthroscop|menisc"),
 ("articulations_et_synoviale__echographie_articulaire", ["joint ultrasound synovitis power Doppler"], r"synov|joint|Doppler"),
 ("coude_poignet_et_main__echographie", ["carpal tunnel ultrasound median nerve"], r"carpal|median nerve"),
 ("coude_poignet_et_main__ct", ["scaphoid fracture CT"], r"scaphoid"),
 ("coude_poignet_et_main__irm_du_poignet", ["wrist MRI"], r"wrist"),
 ("nerfs_peripheriques__echographie_nerveuse", ["nerve ultrasound median nerve"], r"nerve"),
 ("larynx_et_pharynx__irm_cervicale", ["neck MRI"], r"neck|cervical|pharyn|laryn"),
 ("larynx_et_pharynx__pet_ct", ["head and neck cancer PET-CT"], r"head and neck|PET"),
 ("larynx_et_pharynx__biopsie_laryngee_ou_pharyngee", ["laryngeal carcinoma histology", "laryngoscopy laryngeal tumor"], r"laryn|pharyn"),
 ("nez_sinus_et_cavum__nasofibroscopie", ["nasal endoscopy", "nasopharyngoscopy"], r"nasal|nasopharyn|endoscop"),
 ("nez_sinus_et_cavum__rhinoscopie", ["rhinoscopy nasal polyps", "anterior rhinoscopy"], r"rhinoscop|nasal|polyp"),
 ("nez_sinus_et_cavum__biopsie_du_cavum", ["nasopharyngeal carcinoma histology"], r"nasopharyn"),
 ("oeil_et_orbite__retinophotographie", ["fundus photograph retina", "diabetic retinopathy fundus photography"], r"fundus|retin"),
 ("oeil_et_orbite__ct_et_irm_orbitaires", ["orbit CT", "orbit MRI"], r"orbit"),
 ("oeil_et_orbite__biopsie_de_l_artere_temporale", ["temporal arteritis biopsy histology giant cell"], r"temporal|giant cell"),
 ("encephale__arteriographie_cerebrale", ["cerebral angiography DSA aneurysm"], r"cerebral|angiogra|aneurysm|DSA"),
 ("parathyroides__scintigraphie_au_sestamibi", ["sestamibi parathyroid scan"], r"sestamibi|parathyroid"),
 ("parathyroides__ct_4d", ["parathyroid adenoma CT"], r"parathyroid"),
 ("surrenales__scintigraphie_mibg", ["MIBG scintigraphy pheochromocytoma"], r"MIBG|pheochromo"),
 ("pancreas__pet_au_ga_68_dotatate", ["Ga-68 DOTATATE PET neuroendocrine"], r"DOTA|neuroendocrine"),
 ("surrenales__pet_au_ga_68_dotatate", ["DOTATATE PET"], r"DOTA"),
 ("pancreas__echo_endoscopie_avec_ponction", ["endoscopic ultrasound pancreas fine needle aspiration"], r"endoscopic ultrasound|EUS"),
 ("prostate_et_vesicules_seminales__irm_prostatique_multiparametrique", ["prostate MRI PI-RADS"], r"prostate"),
 ("prostate_et_vesicules_seminales__pet_psma", ["PSMA PET prostate"], r"PSMA"),
 ("prostate_et_vesicules_seminales__echographie_transrectale", ["transrectal ultrasound prostate"], r"prostate|transrectal"),
 ("uterus_col_ovaires_et_annexes__echographie_pelvienne_endovaginale_et_su", ["transvaginal ultrasound uterus", "ovarian cyst ultrasound"], r"transvaginal|uter|ovar|pelvic"),
 ("uterus_col_ovaires_et_annexes__hysteroscopie", ["hysteroscopy uterine cavity polyp"], r"hysteroscop"),
 ("uterus_col_ovaires_et_annexes__coelioscopie_diagnostique", ["laparoscopy endometriosis"], r"laparoscop|endometrio"),
 ("grossesse_foetus_et_placenta__irm_foetale", ["fetal MRI"], r"fetal|foetal"),
]
exec(open(os.path.join(RAC, 'projets/outils/cibles_p3b.py'), encoding='utf-8').read()); CIBLES += CIBLES2   # 2e passage
exec(open(os.path.join(RAC, 'projets/outils/cibles_p3c.py'), encoding='utf-8').read()); CIBLES += CIBLES3   # 3e passage
a = int(sys.argv[1]) if len(sys.argv) > 2 else 0
b = int(sys.argv[2]) if len(sys.argv) > 2 else len(CIBLES)
GENITAL = re.compile(r"penis|penile|vulva|scrot|genital|testic", re.I)
index = {}
for f in glob.glob(os.path.join(RAC, "conception/donnees/images/paraclinique/**/*.json"), recursive=True):
    for k in json.load(open(f, encoding="utf-8")).get("cliches", {}): index[k] = f
bilan = []
for eid, qs, pat in CIBLES[a:b]:
    eid = next((k for k in index if k == eid or k.startswith(eid)), eid)   # préfixe accepté
    f = index.get(eid)
    if not f: print("?", eid); continue
    d = json.load(open(f, encoding="utf-8"))
    if d["cliches"].get(eid): continue
    cands, vus = [], set()
    for q in qs:
        for c in commons(q) + openi(q):
            t = c["titre"]
            if c["url"] in vus or not re.search(pat, t + " " + (c.get("auteur") or ""), re.I) or GENITAL.search(t) or c["url"].lower().split("?")[0].endswith(".svg"): continue
            vus.add(c["url"]); cands.append({**c, "requete": q, "statut": "candidat", "montre": None})
        time.sleep(0.3)
    cands = cands[:3]
    if cands:
        d["cliches"][eid] = cands
        d["_meta"]["maj"] = f"{datetime.datetime.now():%Y-%m-%d %H:%M}"
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(cands), eid, flush=True); bilan.append((eid, len(cands)))
print(sum(1 for _, n in bilan if n), "/", len(bilan), "entités remplies")
