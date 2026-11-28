# Synthèse — audit croisé Transversal (couloir 5)

Audit du 28.11.2026 : **248 lots sur 248**. Chaque constat porte une source ouverte, sa date de lecture et un extrait de 25 mots au plus. Les corrections 🟥 et 🟧 prouvées sont appliquées dans les leçons ; les 🟨 et 🟦 restent en proposition.

## Constats par gravité

| Gravité | Constats | Corrigés dans les sources |
|---|---|---|
| 🟥 critique | 6 | 6 |
| 🟧 majeur | 38 | 36 |
| 🟨 mineur | 69 | 0 |
| 🟦 forme | 6 | 0 |
| **Total** | **119** | **42** |

## Verdict des lots

| Verdict | Lots |
|---|---|
| 🟩 conforme | 158 |
| 🟨 mineurs seulement | 53 |
| 🟧 majeurs | 31 |
| 🟥 critique | 6 |

## Familles d'erreurs

| Gravité | Catégorie | Constats |
|---|---|---|
| 🟥 critique | source_fausse_ou_invente | 5 |
| 🟥 critique | posologie | 1 |
| 🟧 majeur | source_fausse_ou_invente | 13 |
| 🟧 majeur | recommandation_obsolete | 8 |
| 🟧 majeur | logique_ou_contradiction | 4 |
| 🟧 majeur | droit_suisse | 4 |
| 🟧 majeur | chiffre_suisse | 4 |
| 🟧 majeur | critere_ou_score | 2 |
| 🟧 majeur | indication_ou_niveau | 1 |
| 🟧 majeur | posologie | 1 |
| 🟧 majeur | examen_federal | 1 |
| 🟨 mineur | droit_suisse | 19 |
| 🟨 mineur | source_fausse_ou_invente | 9 |
| 🟨 mineur | chiffre_suisse | 8 |
| 🟨 mineur | recommandation_obsolete | 7 |
| 🟨 mineur | posologie | 6 |
| 🟨 mineur | logique_ou_contradiction | 5 |
| 🟨 mineur | critere_ou_score | 4 |
| 🟨 mineur | seuil_ou_valeur | 4 |
| 🟨 mineur | indication_ou_niveau | 2 |
| 🟨 mineur | langue_ou_sigle | 2 |
| 🟨 mineur | examen_federal | 1 |
| 🟨 mineur | unite | 1 |
| 🟨 mineur | omission_grave | 1 |
| 🟦 forme | langue_ou_sigle | 5 |
| 🟦 forme | droit_suisse | 1 |

## Constats 🟥 critique

| Constat | Localisation | Problème | Source | Corrigé |
|---|---|---|---|---|
| TR_trans_k_s2_01-001 | _meta.sources[0] | La référence Allergy 2019;74:261-272 existe, mais ce n'est pas un « EAACI position paper » sur la prise en charge de l'asthme lié au travail : PubMed (PMID 29956349) y range une étude de cohorte E-PHOCAS sur les phénotypes d'asthme professionnel selon le poids | [PubMed, PMID 29956349 (Vandenplas O et al., Allergy 2019;74(2):261-272](https://doi.org/10.1111/all.13542) | oui |
| TR_trans_k_s3_01-001 | _meta.sources[1] | Les critères d'Helsinki 2014 ne sont ni un document ERS/ATS ni un article de l'Eur Respir J : PubMed les range sous Wolff H et al., Scand J Work Environ Health 2015;41(1):5-15 (consensus du Finnish Institute of Occupational Health). La référence citée n'existe | [PubMed, PMID 25299403](https://doi.org/10.5271/sjweh.3462) | oui |
| TR_trans_m_s3_01-001 | _meta.sources[3] | Cette référence n'existe pas : PubMed ne contient aucun article aux Annals of Oncology 2012;23:1957, et aucun article de Maltoni ne porte ce titre. Les deux travaux réels sont l'étude prospective multicentrique (Ann Oncol 2009;20:1163-1169) et la revue systéma | [PubMed, PMID 19542532 (Maltoni M et al., Ann Oncol 2009;20(7):1163-9)](https://doi.org/10.1093/annonc/mdp048) | oui |
| TR_trans_m_s4_02-001 | _meta.sources[2] et parties > 8. Pratique suisse | Cette source n'existe pas : la liste BIGORIO de palliative.ch compte douze recommandations (dyspnée, nausées, délire, sédation, exacerbation douloureuse, iléus, spiritualité, hydratation, proches, anxiété, pharmacothérapie, fatigue) et aucune ne porte sur les  | [HUG, Soins palliatifs — aide-mémoire destiné aux soignants, Urgences :](https://www.hug.ch/soins-palliatifs-aide-memoire-destine-aux-soignants/urgences-hemorragie-aigue) | oui |
| TR_trans_m_s4_03-001 | _meta.sources[3] | Cette référence n'existe pas : PubMed ne contient aucun article aux Annals of Oncology 2012;23:1957 et aucun article de Maltoni ne porte ce titre. La revue systématique de 2012 est parue au Journal of Clinical Oncology. | [PubMed, PMID 22412129 (Maltoni M et al., J Clin Oncol 2012;30(12):1378](https://doi.org/10.1200/JCO.2011.37.3795) | oui |
| TR_trans_q_s3_03-002 | parties > 3. Outils et méthodes ; decisionFinale ; items[1]  | Le cas (eGFR 26) et le QCM 2 (eGFR 25) font reprendre la metformine après 48 heures chez des patients dont la fonction rénale se situe sous 30 mL/min. L'information suisse contre-indique la metformine en cas d'insuffisance rénale sévère (clairance < 30 mL/min) | [compendium.ch, Glucophage cpr pell 1000 mg, résumé de l'information pr](https://compendium.ch/fr/product/122963-glucophage-cpr-pell-1000-mg) | oui |

## Constats 🟧 majeur

| Constat | Localisation | Problème | Source | Corrigé |
|---|---|---|---|---|
| TR_S_urgences_vitales_triage-001 | lecons[id=TRANS_S-S1-03].titre | Le titre attribue 5 degrés à l'« Échelle suisse de triage » et l'assimile à l'ESI. L'échelle suisse (SETS, en français EST) compte 4 degrés ; seule l'ESI, américaine, en compte 5. Le titre contredit le corps de la leçon, son glossaire et son QCM 3. Le même tit | [Rutschmann OT et al., Reliability of the revised Swiss Emergency Triag](https://pubmed.ncbi.nlm.nih.gov/28099182/) | non |
| TR_trans_a_s4_03-001 | parties['4. Décisions et seuils'] | L'art. 70 al. 2 LPGA ne désigne pas l'AI parmi les assurances tenues à la prise en charge provisoire. Il désigne l'assurance-maladie, l'assurance-chômage, l'assurance-accidents (face à l'assurance militaire) et la prévoyance professionnelle. L'AI y figure seul | [LPGA (RS 830.1), art. 70 al. 2, texte consolidé Fedlex](https://www.fedlex.admin.ch/eli/cc/2002/510/fr) | oui |
| TR_trans_c_s2_03-001 | _meta.sources[1] | La référence est fausse : l'article de Matthys a paru dans le British Journal of General Practice (2009;59:29-36), et non dans Family Practice 2009;26:117. PubMed ne trouve aucun article à Fam Pract 2009;26:117 pour cet auteur. | [PubMed, notice PMID 19105913 (Matthys J, Elwyn G et al., Br J Gen Prac](https://doi.org/10.3399/bjgp09X394833) | oui |
| TR_trans_e_s1_01-001 | decisionFinale ; parties.3 ; parties.7 ; bulle.retenir | La leçon fait appliquer un seuil de troponine propre au sexe dans l'algorithme ESC 0 h/1 h et présente le seuil unique comme un piège. Les recommandations ESC 2023, que la leçon cite, gardent des seuils uniformes, propres à chaque dosage ; l'étudiant répondrai | [Déclaration de consensus ESC ACVC/EAPCI/HFA/EHRA, Eur Heart J Open 202](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11020263/fullTextXML) | oui |
| TR_trans_e_s3_03-001 | _meta.sources[2] | La référence est mal attribuée : l'article existe, mais il a paru dans Culture, Medicine and Psychiatry 2010;34(2):209-218 (PMID 20407812). PubMed ne trouve aucun article à Depress Anxiety 2010;27:1129. L'article lui-même soutient le contenu de la leçon ; seul | [PubMed, PMID 20407812](https://doi.org/10.1007/s11013-010-9175-x) | oui |
| TR_trans_f_s4_03-001 | parties > 8. Pratique suisse ; _meta > sources[2] | Ce titre est celui de l'ancienne version (2011). La version en vigueur, approuvée le 16.5.2017, s'intitule « Diagnostic de la mort en vue de la transplantation d'organes et préparation du prélèvement d'organes » ; l'ASSM la révise pour l'introduction du consen | [ASSM, Don d'organes de personnes décédées : diagnostic de la mort](https://www.samw.ch/fr/Ethique/Apercu-des-themes/Transplantation-d-organes/Don-d-organes-diagnostic-de-la-mort.html) | oui |
| TR_trans_g_s1_03-001 | parties["4. Décisions et seuils"] | La tranche d'âge est périmée : depuis le 1.7.2026, l'art. 12e let. d OPAS prend en charge le dépistage du cancer du côlon de 50 à 74 ans (nouvelle teneur du 9.6.2026, RO 2026 336). Les méthodes et intervalles (sang occulte tous les 2 ans, coloscopie tous les 1 | [OPAS (RS 832.112.31), art. 12e let. d, état au 1.8.2026](https://www.fedlex.admin.ch/eli/cc/1995/4964_4964_4964/fr) | oui |
| TR_trans_g_s3_03-001 | parties["3. Outils et méthodes"] | Le schéma est périmé pour l'enfant : la recommandation OFSP en vigueur (Bulletin 4 du 20.1.2025, publication de mai 2022 adaptée) place la ciprofloxacine en dose unique orale en premier choix à tout âge (20 mg/kg, max. 500 mg), hors grossesse. La rifampicine ( | [OFSP, Prophylaxie post-expositionnelle des contacts d'une maladie inva](https://www.bag.admin.ch/dam/fr/sd-web/GY6zb1jQocCU/3_fr_empf-kontakt-invasive-meningokokkenerkrankung.pdf) | oui |
| TR_trans_h_s3_01-001 | parties.« 8. Pratique suisse » | La Stratégie nationale en matière de soins palliatifs a couru de 2010 à 2015 et elle est terminée. La Confédération et les cantons l'ont transformée en « plate-forme nationale Soins palliatifs », lancée le 27.4.2017. Le présent de l'indicatif enseigne un dispo | [OFSP, page « Soins palliatifs » (étapes)](https://www.bag.admin.ch/fr/soins-palliatifs) | oui |
| TR_trans_h_s4_01-001 | items[0].explicationParOption.D | Cette explication contredit la leçon (parties 4, décision finale, QCM 2) et les directives ASSM-SSMI version 4 : la règle « premier arrivé, premier servi » ne doit pas être appliquée, même pour départager. Reliquat de la version d'avant l'audit du 24.11.2026 ; | [ASSM-SSMI, Triage en soins intensifs en cas de pénurie exceptionnelle ](https://www.samw.ch/dam/jcr:56861dfa-1c96-40b1-acec-e4c3937e5e9c/directives_v4_assm_triage_soins_intensifs_penurie_ressources_20210923.pdf) | oui |
| TR_trans_j_s4_02-001 | parties['8. Pratique suisse'] ; _meta.sources[0] et [4] | La base légale citée est abrogée : l'OMCJ du 20.11.2002 (RS 818.101.21) a été abrogée par l'art. 107 de l'ordonnance sur les épidémies, entrée en vigueur le 1.1.2016 ; elle ne figure plus au recueil systématique. La règle (134 °C, vapeur saturée, 18 minutes) e | [Ordonnance sur les épidémies (OEp, RS 818.101.1), art. 25 al. 1 let. b](https://www.fedlex.admin.ch/eli/cc/2015/298/fr) | oui |
| TR_trans_j_s4_03-001 | parties['2. Notions fondamentales'] | La définition suisse en vigueur (OSAV/OFSP, module 7 révisé le 30.6.2026) est plus large : la légionellose est associée aux soins dès qu'un séjour ou des soins ont eu lieu dans les 10 jours précédant le début de la maladie ; elle n'exige pas 10 jours d'hospita | [OSAV/OFSP, Légionelles et légionellose, module 7 Légionellose associée](https://www.blv.admin.ch/dam/fr/sd-web/vbLOLP9kCCBj/Module%207%20L%C3%A9gionellose%20associ%C3%A9e%20aux%20soins.pdf) | oui |
| TR_trans_j_s4_03-002 | parties['2. Notions fondamentales'], parties['8. Pratique su | La leçon s'appuie sur le module 12 du 20.8.2018, remplacé par une révision totale du 30.6.2026 (nouveau titre). La version en vigueur recommande, en plus de la valeur légale de 1000 UFC/L, une concentration maximale de 100 UFC/L dans toute l'installation des h | [OSAV/OFSP, Légionelles et légionellose, module 12 Hôpitaux, cliniques ](https://www.blv.admin.ch/dam/fr/sd-web/jpWE1N73sJAk/Module%2012%20H%C3%B4pitaux%20cliniques%20sp%C3%A9cialis%C3%A9es%20et%20institutions%20m%C3%A9dico-sociales.pdf) | oui |
| TR_trans_k_s3_01-002 | _meta.sources[2] | L'article existe, mais il a paru dans Respirology et non dans Lancet Respiratory Medicine. | [PubMed, PMID 35302259 (Respirology 2022;27(6):387-398)](https://doi.org/10.1111/resp.14242) | oui |
| TR_trans_k_s4_01-001 | _meta.sources[3] | Aucune ordonnance fédérale ne porte ce titre. L'OChim (RS 813.11) est l'« ordonnance sur la protection contre les substances et les préparations dangereuses (ordonnance sur les produits chimiques) » ; le glossaire de la leçon la définit d'ailleurs correctement | [OChim (RS 813.11), titre, état au 24.4.2026](https://www.fedlex.admin.ch/eli/cc/2015/366/fr) | oui |
| TR_trans_l_s1_03-001 | parties → « 6. Particularités par terrain » | L'art. 2 al. 2ter OCR prévoit l'inverse : pour la personne qui prouve une prise sur prescription médicale, la seule présence de THC ne suffit pas à établir l'incapacité de conduire ; l'appréciation devient individuelle. | [Ordonnance sur les règles de la circulation routière (OCR, RS 741.11),](https://www.fedlex.admin.ch/eli/cc/1962/1364_1409_1420/fr) | oui |
| TR_trans_l_s3_03-001 | parties → « 6. Particularités par terrain » ; items[0].expli | Le sens est inversé. Les directives 2019 n'imposent pas 2 ans d'inaptitude : des crises exclusivement liées au sommeil depuis au moins 2 ans permettent au contraire de RÉDUIRE le délai d'un an sans crise. | [Ligue suisse contre l'épilepsie, Commission de la circulation routière](https://sgrm.ch/inhalte/Verkehrsmedizin/fms_2019_08402.pdf) | oui |
| TR_trans_l_s3_03-002 | decisionFinale (cas d'ouverture : EEG avec pointes temporale | Le cas décrit un EEG épileptiforme et un traitement débuté : si le neurologue retient un diagnostic d'épilepsie selon la définition de 2014, les directives appliquent le délai de l'épilepsie (1 an sans crise) et non 6 mois. La décision ne le dit pas. | [Ligue suisse contre l'épilepsie, Commission de la circulation routière](https://sgrm.ch/inhalte/Verkehrsmedizin/fms_2019_08402.pdf) | oui |
| TR_trans_m_s1_01-001 | parties > 5. Applications par système | La leçon porte sur la douleur cancéreuse et propose le naloxégol. En Suisse, le naloxégol (Moventig) n'a d'indication, et de limitation LS, que pour la constipation induite par les opioïdes dans les douleurs non cancéreuses ; la méthylnaltrexone (Relistor, SC) | [compendium.ch, MOVENTIG cpr pell 12.5 mg (naloxégol), Brevier et limit](https://compendium.ch/fr/product/1302715-moventig-cpr-pell-12-5-mg) | oui |
| TR_trans_m_s2_01-001 | _meta.sources[2] et parties > 8. Pratique suisse | Aucune recommandation « BIGORIO douleur » n'existe : la liste de palliative.ch compte douze documents (2003-2013), dont un seul sur la douleur, limité à l'exacerbation douloureuse (2006). La source est donc mal nommée et le texte prête à palliative.ch une reco | [palliative.ch, Recommandations de meilleures pratiques BIGORIO (liste ](https://www.palliative.ch/fr/notre-engagement/groupes-de-travail/recommandations-de-meilleures-pratiques-bigorio) | oui |
| TR_trans_m_s2_02-001 | _meta.sources[2] et parties > 8. Pratique suisse | La liste BIGORIO de palliative.ch ne contient aucune recommandation sur la « phase terminale ». Les nausées (2003) et le délire (2004) existent ; les râles du mourant sont traités dans le document sur la dyspnée (2003). | [palliative.ch, Recommandations de meilleures pratiques BIGORIO (liste ](https://www.palliative.ch/fr/notre-engagement/groupes-de-travail/recommandations-de-meilleures-pratiques-bigorio) | oui |
| TR_trans_m_s3_01-002 | _meta.sources[1] et parties > 8. Pratique suisse | La leçon cite la version de 2005 comme référence suisse en vigueur. Le groupe Bigorio a publié en 2024 des recommandations révisées (Swiss Medical Weekly), qui remplacent le document de quatre pages de 2005. | [Swiss Medical Weekly, Palliative sedation – revised recommendations (g](https://smw.ch/index.php/smw/article/download/3590/5856?inline=1) | oui |
| TR_trans_m_s3_01-003 | parties > 4. Décisions et seuils | La leçon propose la lévomépromazine en deuxième ligne sans signaler que sa forme parentérale n'est plus officiellement disponible en Suisse (elle s'obtient par importation). La règle du dépôt impose de signaler tout produit absent du marché suisse. | [Swiss Medical Weekly, Palliative sedation – revised recommendations (g](https://smw.ch/index.php/smw/article/download/3590/5856?inline=1) | oui |
| TR_trans_m_s3_02-001 | parties > 8. Pratique suisse | La phrase laisse croire que l'octréotide est remboursé dans l'occlusion maligne. Sa limitation LS ne couvre que les tumeurs endocrines gastro-entéro-pancréatiques et l'acromégalie ; BIGORIO 2007 précise que l'indication n'est pas reconnue en Suisse et qu'une d | [compendium.ch, SANDOSTATINE sol inj 0.1 mg/ml, limitation LS](https://compendium.ch/fr/product/10555-sandostatine-sol-inj-0-1-mg-ml) | oui |
| TR_trans_m_s4_01-001 | _meta.sources[2] | PubMed ne contient aucun article de Mercadante sur l'hyperalgésie dans Supportive Care in Cancer, ni aucun article portant ce titre. L'article de 2019 de cet auteur sur le sujet est paru dans CNS Drugs sous un autre titre. | [PubMed, PMID 31578704 (Mercadante S, Arcuri E, Santoni A, CNS Drugs 20](https://doi.org/10.1007/s40263-019-00660-0) | oui |
| TR_trans_m_s4_01-002 | _meta.sources[3] et parties > 8. Pratique suisse | Aucune recommandation « BIGORIO douleur » n'existe : le seul document BIGORIO sur la douleur traite l'exacerbation douloureuse (2006) et n'aborde pas l'hyperalgésie. | [palliative.ch, Recommandations de meilleures pratiques BIGORIO (liste ](https://www.palliative.ch/fr/notre-engagement/groupes-de-travail/recommandations-de-meilleures-pratiques-bigorio) | oui |
| TR_trans_m_s4_02-002 | _meta.sources[1] | L'article existe mais la revue, le titre complet et les pages sont faux : il est paru dans BMJ Supportive & Palliative Care 2012;2(4):294-300, et non dans le British Journal of Hospital Medicine 2012;73:30-34. | [PubMed, PMID 24654210 (Ubogagu E, Harris DG, BMJ Support Palliat Care ](https://pubmed.ncbi.nlm.nih.gov/24654210/) | oui |
| TR_trans_n_s1_02-001 | parties['8. Pratique suisse'] | La tranche d'âge remboursée est périmée : depuis le 1er juillet 2026, l'art. 12e let. d OPAS couvre le dépistage du cancer du côlon de 50 à 74 ans (RO 2026 336). | [OPAS (RS 832.112.31), art. 12e let. d, état au 1.8.2026](https://www.fedlex.admin.ch/eli/cc/1995/4964_4964_4964/fr) | oui |
| TR_trans_n_s2_01-001 | parties['2. Notions fondamentales'], parties['4. Décisions e | La leçon fait vacciner l'adulte asplénique contre Hib et en fait la bonne réponse du QCM 1. Le Plan de vaccination suisse 2026 ne prévoit aucune vaccination Hib spécifique pour les groupes à risque ; pour l'asplénie, il recommande pneumocoques, méningocoques e | [OFSP et CFV, Plan de vaccination suisse 2026](https://www.bag.admin.ch/dam/fr/sd-web/Oj0BSN-w-Ggs/Plan%20de%20vaccination%20suisse_2026_FR_Web_final%20(3).pdf) | oui |
| TR_trans_n_s2_02-001 | _meta.sources[3] | La référence est mal attribuée : l'article de validation du DiPCare-Q est paru dans BMJ Open 2012;2:e000692 (PMID 22307103), et non dans BMC Public Health 2012;12:56. L'article existe, mais la revue, le volume et la page cités sont faux. | [PubMed, PMID 22307103 (Vaucher P et al., BMJ Open 2012;2(1):e000692)](https://doi.org/10.1136/bmjopen-2011-000692) | oui |
| TR_trans_o_s2_02-001 | items[3].explicationParOption.A | Le QCM présente le glucagon comme l'antidote de l'intoxication grave aux bêtabloquants sans nuance. La liste suisse des antidotes 2026/2027 juge sa pertinence clinique discutable, privilégie l'insuline à haute dose (hyperinsulinémie euglycémique) aux soins int | [Groupe de travail Antidotes (OFSP, OFPP, Pharmacie de l'armée, Tox Inf](https://www.toxinfo.ch/customer/files/931/Liste-des-antidotes.pdf) | oui |
| TR_trans_p_s1_01-001 | parties['8. Pratique suisse'] | La convention de qualité H+/santésuisse/curafutura porte la date du 20.12.2023, mais le Conseil fédéral ne l'a approuvée que le 22.5.2024 (art. 58a al. 4 LAMal : approbation requise). Elle ne lie donc pas les hôpitaux « depuis 2023 ». | [Conseil fédéral, communiqué « Le Conseil fédéral approuve la conventio](https://www.admin.ch/gov/fr/accueil/documentation/communiques.msg-id-101094.html) | oui |
| TR_trans_p_s2_01-001 | parties['8. Pratique suisse'] | Le Conseil national a adopté la motion 18.4210 le 29.10.2020, mais le Conseil des États ne l'a adoptée que le 20.9.2021 : le Parlement ne l'a donc transmise qu'en 2021. Au 28.11.2026, Curia Vista indique encore l'état « rapport sur l'état d'avancement disponib | [Parlement suisse, Curia Vista, objet 18.4210 (service web officiel : d](https://ws-old.parlament.ch/affairs/20184210?format=json&lang=fr) | oui |
| TR_trans_r_s1_02-001 | parties['8. Pratique suisse'] et _meta.sources[3] | Smarter Medicine – Choosing Wisely Switzerland ne publie aucune liste Top 5 de pneumologie : la page des listes énumère 30 spécialités sans la pneumologie, et les listes Pharmacie 2025, Médecine interne générale ambulatoire 2021 et Anesthésiologie ne contienne | [Smarter Medicine – Choosing Wisely Switzerland, page « Listes Top 5 »](https://www.smartermedicine.ch/fr/liste-top-5) | oui |
| TR_trans_r_s2_03-001 | _meta.sources[3] | Les pages 1930-1943 du Lancet 2009;374 correspondent à l'article de Woodcock J et al. (urban land transport, PMID 19942277). L'article de Haines A et al. de cette série (overview and implications for policy makers, PMID 19942281) occupe les pages 2104-2114. La | [PubMed, notice PMID 19942281](https://pubmed.ncbi.nlm.nih.gov/19942281/) | oui |
| TR_trans_r_s4_03-001 | _meta.sources[3] | Les rapports annuels du Lancet Countdown on health and climate change ont pour première auteure Romanello M (éditions 2023, 2024, 2025 et 2026 selon PubMed), et non Salas RN. La référence attribue les rapports à une auteure qui ne les signe pas en premier. | [PubMed, notice PMID 42950876](https://pubmed.ncbi.nlm.nih.gov/42950876/) | oui |
| TR_trans_s_s1_03-001 | titre | Le titre attribue 5 degrés à l'« Échelle suisse de triage » et l'assimile à l'ESI. L'échelle suisse (SETS, en français EST) compte 4 degrés ; seule l'ESI, américaine, en compte 5. Le titre contredit le corps de la leçon, son glossaire et son QCM 3. Le même tit | [Rutschmann OT et al., Reliability of the revised Swiss Emergency Triag](https://pubmed.ncbi.nlm.nih.gov/28099182/) | non |
| TR_trans_s_s3_01-001 | parties.4. Décisions et seuils ; decisionFinale ; items[2] ( | La durée « au moins 72 heures » vient des recommandations 2021. La version 2025, que la leçon cite, fixe la prévention de la fièvre à 36 à 72 heures chez le patient resté comateux. La source inscrite dans _meta.sources ne dit donc pas « ≥ 72 h ». Le délai de 7 | [Resuscitation Council UK, 2025 Post-resuscitation care guidelines (fon](https://www.resus.org.uk/professional-library/2025-resuscitation-guidelines/post-resuscitation-care-guidelines) | oui |

## Points non vérifiés et sites bloqués

Les rapports listent **466 points non vérifiés** (champ `non_verifies`, avec l'endroit où vérifier). Aucun n'est devenu un constat faute de source lue.

| Site | Rapports concernés |
|---|---|
| compendium.ch | 30 |
| fmh.ch | 26 |
| bger.ch | 22 |
| pubmed.ncbi.nlm.nih.gov | 14 |
| annalsofoncology.org | 12 |
| hug.ch | 12 |
| icd.who.int | 12 |
| swissmedicinfo.ch | 6 |
| eur-lex.europa.eu | 3 |
| smartermedicine.ch | 3 |
| tbinfo.ch | 3 |
| pmc.ncbi.nlm.nih.gov | 2 |
| contens30.fmh.ch | 2 |
| ssi.guidelines.ch | 2 |
| resuscitationjournal.com | 2 |
| bmj.com | 1 |
| health.ec.europa.eu | 1 |
| academic.oup.com | 1 |
| liguepulmonaire.ch | 1 |
| bag.admin.ch | 1 |
| siwf.ch | 1 |
| nccn.org | 1 |
| ncbi.nlm.nih.gov | 1 |
| clinicalmicrobiologyandinfection.org | 1 |
| core.ac.uk | 1 |
| nara-antibiotic-resistance.ch | 1 |
| suva.ch | 1 |
| epi.ch | 1 |
| mediq.ch | 1 |
| parlament.ch | 1 |
| england.nhs.uk | 1 |
| ekl.admin.ch | 1 |
| theworld.org | 1 |
| resuscitation.ch | 1 |
| resus.org.uk | 1 |
| rega.ch | 1 |
| link.springer.com | 1 |
| ccforum.biomedcentral.com | 1 |

## Reste à trancher hors du couloir

- Le titre de TRANS_S-S1-03 prête 5 degrés à l'Échelle suisse de triage, qui en compte 4 (🟧, non corrigé) : le titre vient de `data/references/transversales_19_et_systemes.json` et se propage aux noms de fichiers de `projets/lots/`, à `projets/taches.json` et à `data/references/game_payload_v1.json`.
- `conception/outils/generer_json.py` régénère sur `main` cinq fichiers d'autres couloirs (paraclinique, cardiovasculaire, index de recherche), et `non_perte.py` y signale alors 2 pertes ; ces fichiers ont été restaurés et ne sont pas dans cette branche.
- Le rapport Imagerie `IMG_aorte_abdominale_et_vaisseaux_digestifs.json` est périmé (source modifiée depuis), hors du couloir 5.

Skills chargés : medical-accuracy-100, i-never-waste-token, gemini-cross-check-hard (SKILL.md du dossier).

Signature : AAI (Anthropic AI)
