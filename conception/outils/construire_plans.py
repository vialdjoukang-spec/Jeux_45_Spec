"""Écrit les trois plans de conception en JSON (source de vérité des plans). Usage : python conception/outils/construire_plans.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from socle import *

ICI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYSTEMES = ["Cardiovasculaire", "Respiratoire", "Neurologique", "Psyché (psychiatrie)", "Endocrinien & métabolique", "Digestif & hépatobiliaire",
            "Rénal & uro-génital", "Hématologique & oncologique", "Infectieux & immunitaire", "Locomoteur & rhumatologique", "Dermatologique",
            "Ophtalmologique & ORL", "Gynéco-obstétrical", "Pédiatrique (croissance et développement)"]


def plan(**k):
    base = {"version": "1.0", "date": "2026-11-21", "statut": "Conception — non implémentée", "signature": SIGNATURE,
            "principes": PRINCIPES, "architecture": ARCHITECTURE, "toile": TOILE, "areneAventure": ARENE_AVENTURE,
            "evaluation": EVALUATION, "audits": AUDITS, "semiologie": SEMIOLOGIE}
    base.update(k)
    base["blocages"] = BLOCAGES_COMMUNS + k.get("blocages", [])
    return base


NEURO_SYNDROMES = ["Syndrome pyramidal (déficit moteur central, spasticité, Babinski)", "Syndrome extrapyramidal (parkinsonien et hyperkinétique)", "Syndrome cérébelleux (statique et cinétique)",
    "Syndrome vestibulaire (central et périphérique)", "Syndrome méningé", "Hypertension intracrânienne", "Syndrome confusionnel", "Syndrome démentiel",
    "Syndromes lobaires : frontal, pariétal, temporal, occipital", "Aphasies (Broca, Wernicke, conduction, transcorticales, globale)", "Héminégligence et apraxies",
    "Syndromes du tronc cérébral et syndromes alternes (Wallenberg, Weber, Millard-Gubler)", "Atteintes des nerfs crâniens (I à XII)", "Syndrome thalamique",
    "Syndromes médullaires : section complète, hémisection (Brown-Séquard), centromédullaire (syringomyélique), cordonal postérieur, spinal antérieur",
    "Syndrome du cône terminal et syndrome de la queue de cheval", "Syndrome radiculaire (cervical, lombosacré)", "Syndrome plexique (brachial, lombosacré)",
    "Polyneuropathie, mononeuropathie et mononeuropathie multiple", "Syndrome de la jonction neuromusculaire (myasthénique, Lambert-Eaton)", "Syndrome myogène",
    "Syndrome dysautonomique", "Syndrome épileptique (crises focales et généralisées)", "Syndrome neurovasculaire par territoire artériel"]

TETRADE = plan(
    id="tetrade", titre="Tétrade topo-systémique", couleur="#7a1f3d",
    sousTitre="Anatomie · Physiologie · Sémiologie · Physiopathologie, et la Psyché : du signe au diagnostic, puis au traitement",
    objectif=[
        "Le médecin se réapproprie, système par système, la chaîne qui relie la structure, la fonction, le signe, le syndrome et le diagnostic.",
        "Il sait quelle technique d'examen rechercher, comment s'appelle le signe, quel syndrome il compose et vers quels diagnostics il oriente.",
        "Il comprend pourquoi chaque signe existe, ce qui ancre le raisonnement pour la vie.",
    ],
    perimetre={"inclus": SYSTEMES + ["Lien vers les 3 975 entités de la Cartographie et vers le jeu"],
               "exclus": ["Contenu rédigé dans le code", "Anatomie 3D générée par une IA"]},
    neuro=NEURO_SYNDROMES,
    decisions=[
        {"question": "Infobulles : où ?", "choix": "Partout, de façon systématique : signes, symptômes, syndromes, temps d'examen, examens, diagnostics ; quatre rubriques fixes et symétriques", "raison": "L'explication au survol transforme la liste en raisonnement, surtout là où l'anatomie, la physiologie et la sémiologie sont complexes (système nerveux)."},
        {"question": "Combien de signes par temps d'examen ?", "choix": "Deux ou trois, jamais un seul ; le syndrome nomme son minimum suffisant", "raison": "Un signe isolé n'autorise pas à parler d'un syndrome ; deux ou trois signes concordants le posent."},
        {"question": "Sons d'auscultation ?", "choix": "Enregistrements réels (base HLS-CMDS), bouton 🔊 sur la case et dans l'infobulle", "raison": "Le galop ou les crépitants s'apprennent à l'oreille, pas à la lecture."},
        {"question": "Page qui s'étend horizontalement, ou toile zoomable ?", "choix": "Toile zoomable avec mini-carte", "raison": "Le mannequin et la racine restent visibles ; une page qui s'allonge fait perdre le fil."},
        {"question": "Mannequin 3D : généré ou existant ?", "choix": "Vrais modèles 3D existants (BodyParts3D, Z-Anatomy) ; organes génitaux externes occultés (peau retirée dans une boîte pelvienne) ; jamais de SVG", "raison": "Une IA ne produit pas d'anatomie 3D fiable ; ces modèles sont exacts, gratuits et déjà validés dans le prototype (skill « 3d-images-upload-super »)."},
        {"question": "Accès au traitement depuis un diagnostic : survol ou clic ?", "choix": "Les deux : le survol ouvre un aperçu (1re ligne + posologie adulte) ; le clic déplie le réseau complet (lignes, âges, situations spéciales)", "raison": "Le survol entraîne le réflexe ; le clic sert l'approfondissement, sans encombrer la toile."},
        {"question": "Psyché : avec la neurologie ou à part ?", "choix": "Système distinct ; le sommeil y appartient ; diagnostics en CIM-10 ; présentation par groupe d'âge", "raison": "Ce sont tes règles de structure pour toute la plateforme."},
    ],
    ecrans=[
        {"id": "E1", "nom": "Accueil des systèmes", "but": "Choisir un système", "zones": ["Grille des 14 systèmes, chacun dans sa couleur", "Progression par système"], "interactions": ["Clic : ouvre le système"], "regleLocale": "Tu choisis un système ; sa couleur te suit dans toutes ses pages.", "exemple": "Le système cardiovasculaire s'ouvre en rouge carmin."},
        {"id": "E2", "nom": "Page d'un système", "but": "Voir la structure et lancer un réseau", "zones": ["Mannequin 3D au centre, organes du système surlignés", "Cadre du système, relié aux organes par des courbes", "Barre des 4 boutons de la tétrade", "Mini-carte et légende"], "interactions": ["Rotation à 360° par glisser", "Survol d'un organe : surlignage et nom", "Clic sur un organe : fiche d'organe", "Clic sur un bouton : affiche ou masque son calque"], "regleLocale": "Tu fais tourner le mannequin, puis tu actives un seul calque à la fois pour garder la toile lisible.", "exemple": "Le calque Sémiologie fait apparaître les temps de l'examen cardiaque autour du cadre."},
        {"id": "E3", "nom": "Chaîne sémiologique", "but": "Aller du geste d'examen au diagnostic", "zones": ["Colonne 1 : temps de l'examen", "Colonne 2 : signes", "Colonne 3 : symptômes", "Colonne 4 : syndromes", "Colonne 5 : examen paraclinique complémentaire", "Colonne 6 : diagnostics par spécialité"], "interactions": ["Clic sur un temps : déplie ses signes", "Survol d'un signe : technique exacte et nom consacré", "Survol d'un symptôme : question à poser et caractéristiques à préciser", "Clic sur un syndrome : déplie ou replie son circuit", "Survol d'un diagnostic : aperçu du traitement ; clic : réseau complet"], "regleLocale": "Tu suis un circuit de gauche à droite ; chaque syndrome se replie pour libérer l'espace.", "exemple": "Palpation → choc de pointe dévié vers la gauche → dyspnée d'effort → syndrome d'insuffisance cardiaque gauche → NT-proBNP et échocardiographie → insuffisance cardiaque (cardiologie)."},
        {"id": "E4", "nom": "Fiche d'organe (Anatomie)", "but": "Connaître la structure", "zones": ["Vignette réduite", "Anatomie macroscopique", "Anatomie microscopique", "Vascularisation", "Innervation", "Rapports"], "interactions": ["Clic sur un champ : déplie son contenu", "Clic sur la vignette : agrandissement"], "regleLocale": "Chaque champ se lit seul en trois phrases au plus.", "exemple": "Cœur : l'artère coronaire droite vascularise le nœud sinusal chez environ 60 % des sujets."},
        {"id": "E5", "nom": "Réseau de physiologie", "but": "Comprendre la fonction", "zones": ["Points de départ : les fonctions et régulations du système", "Schéma de chaque fonction", "Valeurs normales en unités SI suisses"], "interactions": ["Clic sur une fonction : surligne les organes qui la portent", "Survol d'une valeur : sa signification"], "regleLocale": "Tu pars d'une fonction et tu vois quels organes la portent.", "exemple": "Débit cardiaque = fréquence cardiaque × volume d'éjection systolique."},
        {"id": "E6", "nom": "Physiopathologie", "but": "Relier la fonction perturbée au signe", "zones": ["Mécanisme en chaîne : amorce → installation → maintien", "Lien vers le signe et vers le symptôme qu'il explique"], "interactions": ["Clic sur un mécanisme : surligne le signe correspondant"], "regleLocale": "Chaque mécanisme dit pourquoi un signe apparaît.", "exemple": "La congestion veineuse pulmonaire augmente la pression capillaire, ce qui fait transsuder le liquide et produit des crépitants."},
        {"id": "E7", "nom": "Psyché : examen psychiatrique", "but": "Appliquer la tétrade à la psychiatrie", "zones": ["Anatomie fonctionnelle des circuits (cortico-limbique, préfrontal, noyaux gris)", "Neurotransmission (sérotonine, dopamine, noradrénaline, GABA, glutamate)", "Temps de l'examen psychiatrique (AMDP) : présentation, contact, conscience, orientation, attention, mémoire, pensée formelle, contenu, perceptions, affects, psychomotricité, pulsions, sommeil, appétit, suicidalité, insight", "Syndromes (dépressif, maniaque, psychotique, anxieux, obsessionnel, confusionnel, addictif)", "Diagnostics CIM-10 par groupe d'âge (enfant, adolescent, adulte, sujet âgé), critères condensés au survol"], "interactions": ["Survol d'un critère CIM-10 : condensé du critère", "Clic sur un diagnostic : chef de file thérapeutique selon le profil clinique"], "regleLocale": "Tu relèves les signes AMDP, ils composent un syndrome, puis le diagnostic CIM-10 propose son traitement.", "exemple": "Humeur dépressive + anhédonie + réveil précoce → syndrome dépressif mélancolique → F32.2 → chef de file adapté au profil mélancolique."},
        {"id": "E8", "nom": "Espace d'exercices", "but": "S'entraîner sur le système", "zones": ["Exercices générés depuis le graphe", "Accès à l'arène et à l'aventure du système"], "interactions": ["Choix d'un type d'exercice", "Correction commentée après chaque réponse"], "regleLocale": "Tu t'exerces d'abord sur les notions dues aujourd'hui.", "exemple": "« Quelle manœuvre recherche le signe de Murphy ? »"},
    ],
    parcours=[
        {"n": 1, "etape": "Choisir un système", "resultat": "Le mannequin s'affiche, les organes du système sont surlignés."},
        {"n": 2, "etape": "Activer le calque Anatomie", "resultat": "Les organes se relient au cadre ; un clic ouvre la fiche d'organe."},
        {"n": 3, "etape": "Activer le calque Physiologie", "resultat": "Les fonctions apparaissent comme points de départ, avec leurs schémas."},
        {"n": 4, "etape": "Activer le calque Sémiologie", "resultat": "Les temps de l'examen se déplient vers les signes."},
        {"n": 5, "etape": "Suivre un circuit", "resultat": "Signe → symptôme → syndrome → examen → diagnostic."},
        {"n": 6, "etape": "Survoler ou cliquer le diagnostic", "resultat": "Aperçu du traitement au survol, réseau complet au clic."},
        {"n": 7, "etape": "Activer le calque Physiopathologie", "resultat": "Chaque signe s'explique par son mécanisme."},
        {"n": 8, "etape": "S'exercer", "resultat": "Exercices, puis arène et aventure du système."},
    ],
    donnees=[
        {"fichier": "tetrade/systemes.json", "role": "Index des 14 systèmes", "champs": ["id", "nom", "couleur", "icone", "organes[]", "ordre"], "producteur": "Script", "volume": "1 fichier"},
        {"fichier": "tetrade/<systeme>/graphe.json", "role": "Source de vérité : nœuds et liens", "champs": ["noeuds[] : id, type (organe | temps_examen | signe | symptome | syndrome | examen | diagnostic | specialite | fonction | mecanisme | traitement), label, refs", "liens[] : de, vers, type (recherche | compose | complete | oriente | explique | traite | porte)", "sources[]"], "producteur": "IA, puis REJECTOR_", "volume": "14 fichiers"},
        {"fichier": "tetrade/<systeme>/anatomie.json", "role": "Fiches d'organes", "champs": ["organeId", "vignette", "macro", "micro", "vascularisation", "innervation", "rapports", "maillage3d", "sources"], "producteur": "IA", "volume": "≈ 15 à 40 organes par système"},
        {"fichier": "tetrade/<systeme>/physiologie.json", "role": "Fonctions et régulations", "champs": ["fonctionId", "enoncé", "formule", "valeursNormales (SI)", "organes[]", "schema"], "producteur": "IA", "volume": "≈ 10 à 25 fonctions par système"},
        {"fichier": "tetrade/<systeme>/semiologie.json", "role": "Temps d'examen, signes, symptômes", "champs": ["signe : technique, nomConsacre, eponyme, termeSuisse, sensibilite, specificite, son", "bulle : def, pourquoi, confusion, retenir (4 rubriques symétriques, obligatoires)", "symptome : questionAPoser, caracteristiques[] (siège, irradiation, type, intensité, horaire, facteurs)"], "producteur": "IA", "volume": "≈ 40 à 120 signes par système"},
        {"fichier": "tetrade/sons.json", "role": "Catalogue des sons d'auscultation réels", "champs": ["sonId", "nom", "fichier", "foyer", "temps", "source", "licence"], "producteur": "Script (téléchargement + conversion MP3)", "volume": "≈ 40 sons"},
        {"fichier": "tetrade/<systeme>/syndromes.json", "role": "Composition des syndromes et débouchés", "champs": ["syndromeId", "signesMinimaux[] (2 ou 3)", "signes[]", "symptomes[]", "examenComplementaire", "diagnostics[] (entité de la Cartographie, spécialité)"], "producteur": "IA", "volume": "≈ 10 à 30 syndromes par système"},
        {"fichier": "tetrade/<systeme>/physiopathologie.json", "role": "Pourquoi les signes existent", "champs": ["mecanismeId", "chaine (amorce, installation, maintien)", "explique[] (signes, symptômes)"], "producteur": "IA", "volume": "Un mécanisme par signe majeur"},
        {"fichier": "tetrade/psyche/criteres_cim10.json", "role": "Critères CIM-10 condensés, par groupe d'âge", "champs": ["code", "libelle", "criteresCondenses", "groupeAge", "cheffileParProfil"], "producteur": "IA, puis REJECTOR_", "volume": "Chapitre F"},
        {"fichier": "tetrade/modeles3d.json", "role": "Correspondance maillage ↔ organe", "champs": ["modele", "licence", "auteur", "maillageId", "organeId"], "producteur": "Toi + script", "volume": "1 fichier"},
        {"fichier": "tetrade/liens.json", "role": "Diagnostics ↔ Cartographie ↔ jeu", "champs": ["diagnosticId", "entiteCartographie", "specialites[]", "ficheDeRaisonnement"], "producteur": "Script", "volume": "1 fichier"},
        {"fichier": "tetrade/exercices/<systeme>.json", "role": "Exercices générés", "champs": ["type", "question", "options[] (texte, correct, why)", "refs"], "producteur": "Script, 0 token", "volume": "Plusieurs milliers"},
    ],
    exercices=[
        {"type": "Technique → signe", "exemple": "Quelle manœuvre recherche le signe de Murphy ?", "generation": "Lien « recherche » du graphe"},
        {"type": "Signe → mécanisme", "exemple": "Pourquoi le choc de pointe est-il dévié ?", "generation": "Lien « explique »"},
        {"type": "Symptômes → syndrome", "exemple": "Ces trois éléments composent quel syndrome ?", "generation": "Lien « compose »"},
        {"type": "Syndrome → examen", "exemple": "Quel examen complète ce syndrome ?", "generation": "Lien « complete »"},
        {"type": "Syndrome → diagnostics", "exemple": "Classe ces diagnostics par spécialité.", "generation": "Lien « oriente »"},
        {"type": "Organe → vascularisation / innervation", "exemple": "Quelle artère vascularise le nœud sinusal ?", "generation": "anatomie.json"},
        {"type": "Mannequin muet", "exemple": "Clique l'organe responsable de ce signe.", "generation": "maillage3d + lien « porte »"},
        {"type": "Tracer le chemin", "exemple": "Relie le signe au diagnostic sur la toile.", "generation": "Chemin du graphe"},
        {"type": "Psyché : signe AMDP → syndrome → CIM-10", "exemple": "Ces signes composent-ils un épisode dépressif F32 ?", "generation": "criteres_cim10.json"},
    ],
    production=[
        {"n": 1, "etape": "Écrire les schémas JSON des 11 fichiers", "outil": "Toi ou l'agent d'architecture", "cout": "0 token d'IA de contenu", "controle": "Validation JSON Schema"},
        {"n": 2, "etape": "Produire le graphe et les fiches d'un système pilote (cardiovasculaire)", "outil": "API Claude, Batch + cache", "cout": "Payant, une fois", "controle": "Schéma + cohérence des liens"},
        {"n": 3, "etape": "Faire auditer le pilote par REJECTOR_", "outil": "IA d'un autre fournisseur", "cout": "Faible", "controle": "0 rejet de fond"},
        {"n": 4, "etape": "Générer les exercices du pilote", "outil": "Script", "cout": "0 token", "controle": "Chaque exercice cite son nœud source"},
        {"n": 5, "etape": "Valider le pilote avec Vial", "outil": "Toi", "cout": "—", "controle": "GO écrit"},
        {"n": 6, "etape": "Produire les 13 autres systèmes, du plus fréquent en pratique au plus rare", "outil": "API Batch", "cout": "Payant", "controle": "Mêmes portes"},
    ],
    construction=[
        {"n": 1, "phase": "Schémas et données pilotes", "livrable": "11 schémas + système cardiovasculaire complet", "sortie": "Schémas valides, REJECTOR_ vert"},
        {"n": 2, "phase": "Moteur de toile", "livrable": "Toile zoomable, repli et dépli, survols, mini-carte", "sortie": "Le pilote s'affiche sans code spécifique au système"},
        {"n": 3, "phase": "Mannequin 3D", "livrable": "Modèle libre chargé, rotation, surlignage d'organe", "sortie": "60 images/s sur un portable ordinaire"},
        {"n": 4, "phase": "Calques de la tétrade", "livrable": "Anatomie, Physiologie, Sémiologie, Physiopathologie", "sortie": "Chaque calque s'active seul"},
        {"n": 5, "phase": "Débouché thérapeutique", "livrable": "Aperçu au survol, réseau au clic", "sortie": "Chaque diagnostic montre son traitement sourcé"},
        {"n": 6, "phase": "Psyché", "livrable": "Examen AMDP, CIM-10 par âge, chefs de file par profil", "sortie": "Critères condensés au survol"},
        {"n": 7, "phase": "Exercices, arène, aventure", "livrable": "Générateurs, branchement sur le moteur du jeu", "sortie": "Correction commentée après chaque réponse"},
        {"n": 8, "phase": "Extension aux 13 autres systèmes", "livrable": "Données seulement", "sortie": "Les quatre audits sont verts"},
    ],
    questionsOuvertes=["Faut-il un système « Pédiatrique » à part, ou une dimension « âge » transversale à chaque système ?"],
    prototype={"titre": "Prototype : Tétrade — clic sur le cœur, circuit sémiologique déplié", "image": "prototypes/tetrade.png", "centre": "mannequin", "cadre": "Système cardiovasculaire",
               "colonnes": [["Inspection", "Palpation", "Auscultation"], ["Choc de pointe dévié", "Galop B3", "Turgescence jugulaire"], ["Dyspnée d'effort", "Orthopnée", "Œdèmes déclives"], ["Insuffisance cardiaque gauche", "Insuffisance cardiaque droite"], ["NT-proBNP", "Échocardiographie"], ["Insuffisance cardiaque (CAR)", "Valvulopathie (CAR)"]],
               "legende": "Les courbes relient chaque élément à l'étape suivante ; survoler le diagnostic ouvre l'aperçu du traitement."},
)

PHARMACO = plan(
    id="pharmacologie", titre="Pharmacologie systémique", couleur="#1d6b4f",
    sousTitre="Du système à la cible malade, de la perturbation au diagnostic, du diagnostic à la médication",
    objectif=[
        "Le médecin relie chaque classe médicamenteuse à la structure qu'elle cible et à la perturbation qu'elle corrige.",
        "Il choisit la molécule selon le diagnostic, l'âge et la situation, avec sa posologie suisse.",
        "Il comprend la pharmacocinétique et la pharmacodynamique de chaque molécule grâce à leurs courbes.",
    ],
    perimetre={"inclus": SYSTEMES + ["Classes et molécules disponibles en Suisse (AIPS, Compendium)"], "exclus": ["Molécules non autorisées en Suisse, sauf mention explicite"]},
    mnemonique={"nom": "VIT DIT CAFé", "statut": "CONFIRMÉ PAR VIAL (2026-11-21) : les lettres nomment les différentes altérations d'un tissu ou d'un organe.",
                "lettres": [["V", "Vasculaire"], ["I", "Infectieux"], ["T", "Traumatique"], ["D", "Dégénératif"], ["I", "Inflammatoire ou immunologique"], ["T", "Tumoral"], ["C", "Congénital"], ["A", "Auto-immun"], ["F", "Fonctionnel"], ["é", "Endocrinien et métabolique"]],
                "regle": "Le fichier mnemonique.json porte la signification ; le moteur l'affiche sans aucune valeur codée en dur."},
    decisions=[
        {"question": "Le traitement : survol ou clic ?", "choix": "Clic obligatoire, avec réseau complet", "raison": "Ici, la médication est l'objectif : elle mérite toute la toile (âges, PK/PD, courbes, interactions)."},
        {"question": "Les courbes PK : dessinées ou calculées ?", "choix": "Calculées par script à partir des paramètres (t½, Tmax, Vd, biodisponibilité, posologie)", "raison": "Le calcul est exact, gratuit et cohérent pour toutes les molécules."},
        {"question": "Organisation des molécules", "choix": "DCI, nom commercial suisse entre parenthèses, par classe ; chef de file selon le profil clinique", "raison": "Ce sont tes règles de structure pour la pharmacologie."},
    ],
    ecrans=[
        {"id": "P1", "nom": "Accueil des systèmes", "but": "Choisir un système", "zones": ["Grille des 14 systèmes"], "interactions": ["Clic : ouvre le système"], "regleLocale": "Tu choisis un système ; chaque structure ciblable s'y affiche.", "exemple": "Cardiovasculaire."},
        {"id": "P2", "nom": "Maquette 3D du système", "but": "Voir les structures malades et ciblables", "zones": ["Mannequin 3D", "Structures ciblables surlignées (organes, tissus, récepteurs symboliques)", "Cadre du système"], "interactions": ["Rotation", "Clic sur une structure : déplie son réseau de perturbations"], "regleLocale": "Tu cliques une structure pour voir comment elle peut tomber malade.", "exemple": "Clic sur le myocarde → réseau VIT DIT CAFé."},
        {"id": "P3", "nom": "Réseau des perturbations (VIT DIT CAFé)", "but": "Classer les mécanismes de maladie", "zones": ["Une branche par lettre du mnémonique", "Diagnostics au bout de chaque branche"], "interactions": ["Clic sur une lettre : déplie ses diagnostics", "Survol d'un diagnostic : définition en une phrase"], "regleLocale": "Chaque lettre ouvre une famille de mécanismes, puis ses diagnostics.", "exemple": "V (vasculaire) → cardiopathie ischémique."},
        {"id": "P4", "nom": "Réseau thérapeutique d'un diagnostic", "but": "Choisir la médication", "zones": ["Buts du traitement", "Lignes : 1re, 2e, 3e", "Classes → molécules (DCI + nom suisse)", "Tranches d'âge : nouveau-né, enfant, adolescent, adulte, sujet âgé", "Situations spéciales : grossesse, allaitement, insuffisance rénale (DFG), insuffisance hépatique (Child-Pugh)"], "interactions": ["Clic sur une classe : déplie ses molécules", "Clic sur une molécule : fiche pharmacologique"], "regleLocale": "Tu descends du but du traitement jusqu'à la molécule adaptée à l'âge et à la situation.", "exemple": "Cardiopathie ischémique → antiagrégants → acide acétylsalicylique (Aspirine Cardio®) 100 mg/j."},
        {"id": "P5", "nom": "Fiche pharmacologique d'une molécule", "but": "Maîtriser la molécule", "zones": ["Pharmacodynamie : cible, mécanisme, effet, relation dose-effet", "Pharmacocinétique : absorption, biodisponibilité, Tmax, Vd, liaison protéique, métabolisme (CYP), élimination, t½", "Courbe concentration-temps calculée, avec fenêtre thérapeutique", "Courbe dose-effet", "Posologie par âge et ajustements", "Effets indésirables, contre-indications, interactions majeures", "Grossesse et allaitement (texte AIPS)", "Source de la cascade"], "interactions": ["Curseurs : dose, intervalle, fonction rénale → la courbe se recalcule", "Survol d'un paramètre : sa définition"], "regleLocale": "Tu modifies la dose ou le DFG et tu vois la courbe changer.", "exemple": "Doubler l'intervalle avec un DFG à 30 mL/min ramène la concentration dans la fenêtre."},
        {"id": "P6", "nom": "Pratique", "but": "S'évaluer", "zones": ["Arène", "Aventure du système", "Examen blanc : A, K', menus longs"], "interactions": ["Correction commentée après chaque réponse"], "regleLocale": "Tu t'entraînes d'abord sur les molécules dues aujourd'hui.", "exemple": "Menu long : choisis les 3 molécules contre-indiquées chez cette patiente enceinte."},
    ],
    parcours=[
        {"n": 1, "etape": "Choisir un système", "resultat": "La maquette 3D montre les structures ciblables."},
        {"n": 2, "etape": "Cliquer une structure", "resultat": "Le réseau VIT DIT CAFé se déplie."},
        {"n": 3, "etape": "Cliquer une lettre", "resultat": "Les diagnostics de cette famille apparaissent."},
        {"n": 4, "etape": "Cliquer un diagnostic", "resultat": "Le réseau thérapeutique s'ouvre."},
        {"n": 5, "etape": "Choisir une classe, puis une molécule", "resultat": "La fiche pharmacologique s'affiche, avec ses courbes."},
        {"n": 6, "etape": "Ajuster âge, dose ou fonction rénale", "resultat": "La posologie et la courbe s'adaptent."},
        {"n": 7, "etape": "S'évaluer", "resultat": "Arène, aventure, examen blanc."},
    ],
    donnees=[
        {"fichier": "pharmaco/mnemonique.json", "role": "Signification des lettres VIT DIT CAFé", "champs": ["lettre", "famille", "definition", "couleur"], "producteur": "Script (signification validée par Vial)", "volume": "1 fichier"},
        {"fichier": "pharmaco/<systeme>/structures.json", "role": "Structures malades et ciblables", "champs": ["structureId", "nom", "maillage3d", "cibles[] (récepteurs, enzymes, canaux, transporteurs)"], "producteur": "IA", "volume": "14 fichiers"},
        {"fichier": "pharmaco/<systeme>/graphe.json", "role": "Structure → perturbation → diagnostic → traitement", "champs": ["noeuds[] : structure | perturbation | diagnostic | but | ligne | classe | molecule", "liens[] : souffre_de | produit | traite_par | contient | cible"], "producteur": "IA, puis REJECTOR_", "volume": "14 fichiers"},
        {"fichier": "pharmaco/classes.json", "role": "Classes médicamenteuses", "champs": ["classeId", "nom", "mecanisme", "indications[]", "chefDeFile[] par profil"], "producteur": "IA", "volume": "≈ 300 classes"},
        {"fichier": "pharmaco/molecules/<dci>.json", "role": "Fiche de molécule", "champs": ["dci", "nomsSuisses[]", "pd {cible, mecanisme, effet}", "pk {F, Tmax, Vd, liaison, metabolisme, CYP, elimination, t12}", "posologies[] {age, indication, dose, voie, rythme, duree}", "ajustements {DFG, ChildPugh}", "EI[]", "CI[]", "interactions[]", "grossesse", "allaitement", "source {niveau, ref, date}"], "producteur": "IA + index AIPS, puis REJECTOR_", "volume": "≈ 1 000 molécules"},
        {"fichier": "pharmaco/courbes/<dci>.json", "role": "Courbes calculées", "champs": ["concentration-temps (modèle à 1 compartiment)", "fenêtre thérapeutique", "dose-effet (Emax)"], "producteur": "Script, 0 token", "volume": "1 par molécule"},
        {"fichier": "pharmaco/exercices/<systeme>.json", "role": "Exercices générés", "champs": ["type", "question", "options[] (texte, correct, why)", "refs"], "producteur": "Script, 0 token", "volume": "Plusieurs milliers"},
    ],
    exercices=[
        {"type": "Diagnostic → classe de 1re ligne", "exemple": "Quelle classe traite en premier cette pathologie ?", "generation": "Lien « traite_par » + ligne 1"},
        {"type": "Molécule → mécanisme", "exemple": "Quelle cible cette molécule bloque-t-elle ?", "generation": "molecules/<dci>.pd"},
        {"type": "Courbe → paramètre", "exemple": "Quelle demi-vie cette courbe montre-t-elle ?", "generation": "courbes/<dci>"},
        {"type": "Ajustement", "exemple": "Quelle dose donner avec un DFG à 25 mL/min ?", "generation": "ajustements"},
        {"type": "Contre-indication", "exemple": "Menu long : quelles molécules éviter pendant la grossesse ?", "generation": "CI + grossesse"},
        {"type": "Interaction", "exemple": "Quel inhibiteur du CYP3A4 augmente ce taux ?", "generation": "interactions"},
        {"type": "Lettre → famille de mécanisme", "exemple": "À quelle lettre de VIT DIT CAFé appartient ce diagnostic ?", "generation": "mnemonique + graphe"},
    ],
    production=[
        {"n": 1, "etape": "Écrire mnemonique.json depuis la signification validée de VIT DIT CAFé", "outil": "Script", "cout": "0 token", "controle": "10 lettres, 10 familles d'altération"},
        {"n": 2, "etape": "Extraire les données AIPS (posologies, grossesse, CI) de l'index local", "outil": "Script", "cout": "0 token", "controle": "Numéro Swissmedic par spécialité"},
        {"n": 3, "etape": "Produire le système pilote (cardiovasculaire) : graphe, classes, molécules", "outil": "API Claude, Batch + cache", "cout": "Payant, une fois", "controle": "Schémas + concordance AIPS"},
        {"n": 4, "etape": "Calculer les courbes", "outil": "Script", "cout": "0 token", "controle": "Courbe cohérente avec t½ et Tmax"},
        {"n": 5, "etape": "REJECTOR_ sur le pilote", "outil": "IA d'un autre fournisseur", "cout": "Faible", "controle": "0 rejet de fond"},
        {"n": 6, "etape": "Étendre aux 13 autres systèmes (infectiologie en second)", "outil": "API Batch", "cout": "Payant", "controle": "Mêmes portes"},
    ],
    construction=[
        {"n": 1, "phase": "Mnémonique, schémas, extraction AIPS", "livrable": "mnemonique.json, 7 schémas, index AIPS exploitable", "sortie": "Schémas valides"},
        {"n": 2, "phase": "Pilote cardiovasculaire", "livrable": "Graphe, classes et molécules du système", "sortie": "REJECTOR_ vert"},
        {"n": 3, "phase": "Moteur de courbes", "livrable": "Modèle à 1 compartiment, Emax, curseurs", "sortie": "Recalcul en moins de 50 ms"},
        {"n": 4, "phase": "Toile et maquette 3D", "livrable": "Réutilisation du moteur de la Tétrade", "sortie": "Aucun code spécifique au système"},
        {"n": 5, "phase": "Réseau thérapeutique et fiches", "livrable": "Âges, situations spéciales, PK/PD", "sortie": "Chaque posologie porte sa source"},
        {"n": 6, "phase": "Pratique", "livrable": "Exercices, arène, aventure, examen blanc", "sortie": "Correction commentée partout"},
        {"n": 7, "phase": "Extension", "livrable": "Infectiologie, puis les autres systèmes", "sortie": "Les quatre audits sont verts"},
    ],
    blocages=["Aucune courbe ne s'affiche sans ses paramètres sourcés.", "Aucune molécule ne s'affiche sans son nom commercial suisse, ou sans la mention « non commercialisée en Suisse »."],
    questionsOuvertes=[],
    prototype={"titre": "Prototype : myocarde → VIT DIT CAFé → diagnostics → réseau thérapeutique", "image": "prototypes/pharmacologie.png", "centre": "mannequin", "cadre": "Système cardiovasculaire",
               "colonnes": [["Myocarde", "Valves", "Artères coronaires"], ["V", "I", "T", "D", "I", "T", "C", "A", "F"], ["Cardiopathie ischémique", "Myocardite"], ["Antiagrégants", "Bêtabloquants", "Statines"], ["Acide acétylsalicylique", "Clopidogrel"], ["Courbe C(t)", "Posologie par âge"]],
               "legende": "Chaque clic déplie le niveau suivant ; la fiche de molécule affiche les courbes calculées."},
)

PARACLINIQUE = plan(
    id="paraclinique", titre="Jeux_Examens_Paraclinique", couleur="#1f4e8c",
    sousTitre="Biologie par prélèvement · Imagerie par région · Explorations fonctionnelles : de l'examen à l'interprétation, au diagnostic et au traitement",
    objectif=[
        "Le médecin part d'un prélèvement, d'une région ou d'une fonction, et aboutit à l'interprétation, au diagnostic, puis au traitement avec sa posologie.",
        "Il maîtrise les calculs et les critères diagnostiques qui tranchent.",
        "Il lit une image en comparant un cliché brut et un cliché annoté.",
    ],
    perimetre={"inclus": ["Onglet Biologie", "Onglet Imagerie", "Onglet Explorations fonctionnelles"], "exclus": ["Images dessinées en SVG"]},
    decisions=[
        {"question": "Images d'imagerie : quelle source ?", "choix": "Toute source du web convient (décision de Vial) ; chaque image garde son URL d'origine dans son JSON pour pouvoir être remplacée ; aucune image en SVG", "raison": "Vial privilégie le réalisme ; la traçabilité de l'URL suffit à maintenir la banque (skill « 3d-images-upload-super »)."},
        {"question": "Calculs : rédigés ou calculés ?", "choix": "Calculateurs exécutés par script, à partir de formules versionnées", "raison": "Le calcul est exact, et le joueur peut faire varier les valeurs."},
        {"question": "Le sommeil", "choix": "La polysomnographie relève des explorations fonctionnelles, mais ses diagnostics renvoient à la Psyché", "raison": "Ta règle : le sommeil appartient à la psychiatrie."},
    ],
    onglets={
        "biologie": {
            "prelevements": ["Sang veineux (hématologie, biochimie, hémostase, sérologies, hormonologie)", "Sang artériel (gazométrie)", "Sang capillaire (glycémie, lactate)", "Hémocultures", "Urine (bandelette, sédiment, culture, spot, urines de 24 h)", "Liquide céphalorachidien", "Liquide pleural", "Liquide d'ascite", "Liquide synovial (articulaire)", "Liquide péricardique", "Selles (coproculture, parasitologie, calprotectine, sang occulte)", "Expectorations et lavage broncho-alvéolaire", "Moelle osseuse (myélogramme, biopsie ostéomédullaire)", "Biopsies (rein, foie, peau, ganglion, prostate, sein…)", "Prélèvements génitaux et urétraux", "Écouvillons naso-pharyngés", "Liquide amniotique", "Test de la sueur", "Sperme (spermogramme)", "Ponction de kyste ou d'abcès"],
            "chaine": "Prélèvement → examens possibles → valeurs (unités SI suisses) → interprétation → syndrome biologique → diagnostics → traitement avec posologie",
            "calculs": ["Trou anionique et trou anionique corrigé par l'albumine", "Osmolalité calculée et trou osmolaire", "DFG (CKD-EPI) et clairance (Cockcroft-Gault)", "Fraction d'excrétion du sodium et de l'urée", "Calcémie corrigée", "Natrémie corrigée par la glycémie", "Gradient albumine sérum-ascite", "Gradient alvéolo-artériel en O₂", "Formule de Winter", "Rapport protéines/créatinine urinaires", "Index de saturation de la transferrine"],
            "criteres": ["Critères de Kass (bactériurie ≥ 10⁵ UFC/mL)", "Critères de Light (exsudat ou transsudat)", "Infection d'ascite (PNN ≥ 250/mm³)", "Profils du LCR (bactérien, viral, tuberculeux, fongique)", "Liquide synovial : mécanique, inflammatoire, septique", "Diagnostic biologique du diabète (HbA1c, glycémie à jeun, HGPO)"],
        },
        "imagerie": {
            "regions": ["Tête et crâne", "Cou", "Thorax", "Cœur et gros vaisseaux", "Sein", "Abdomen", "Pelvis", "Rachis", "Membre supérieur", "Membre inférieur", "Vaisseaux périphériques"],
            "examens": ["Radiographie", "Échographie et Doppler", "Scanner (CT)", "IRM", "Scintigraphie", "TEP-CT", "Angiographie", "Mammographie", "Ostéodensitométrie"],
            "chaine": "Région → examens faisables → système d'organe → organe → pathologies → fenêtre à deux clichés",
            "fenetre": "À gauche le cliché brut (« Observez d'abord ») ; à droite le cliché annoté avec repères numérotés ; dessous, la description des lésions en liste numérotée, concise et structurée (siège, taille, densité ou signal, rehaussement, effet de masse, signes associés), puis le diagnostic et la conduite.",
        },
        "explorations": {
            "liste": ["Spirométrie, pléthysmographie, DLCO", "ECG, Holter, MAPA", "Épreuve d'effort et épreuve cardio-pulmonaire (VO₂max)", "Test de marche de 6 minutes", "Test de Schellong et tilt-test", "EEG", "ENMG (électroneuromyographie)", "Potentiels évoqués (visuels, auditifs, somesthésiques)", "Polysomnographie et polygraphie (diagnostics renvoyés vers la Psyché)", "Audiométrie et tympanométrie", "Champ visuel et OCT", "Manométrie œsophagienne et pH-impédancemétrie", "Bilan urodynamique", "Tests endocriniens dynamiques"],
            "chaine": "Fonction → exploration → tracé ou résultat → interprétation (valeurs seuils) → diagnostic → traitement",
        },
    },
    ecrans=[
        {"id": "X1", "nom": "Onglet Biologie", "but": "Partir d'un prélèvement", "zones": ["Liste des prélèvements, chacun avec son icône", "Réseau des examens du prélèvement"], "interactions": ["Clic sur un prélèvement : déplie ses examens", "Clic sur un examen : fiche d'interprétation"], "regleLocale": "Tu choisis un prélèvement, puis un examen, puis tu interprètes.", "exemple": "Liquide d'ascite → PNN, protéines, gradient albumine."},
        {"id": "X2", "nom": "Fiche d'interprétation", "but": "Interpréter et conclure", "zones": ["Valeurs de référence", "Calculateurs", "Critères diagnostiques", "Syndrome biologique → diagnostics → traitement avec posologie"], "interactions": ["Saisie de valeurs : le calcul et l'interprétation se mettent à jour", "Clic sur un diagnostic : réseau thérapeutique"], "regleLocale": "Tu saisis tes valeurs, le calcul s'exécute et le critère tranche.", "exemple": "PNN à 320/mm³ → infection d'ascite → céfotaxime, posologie et source."},
        {"id": "X3", "nom": "Onglet Imagerie", "but": "Partir d'une région", "zones": ["Mannequin 3D découpé en régions", "Réseau région → examens → organes → pathologies"], "interactions": ["Clic sur une région : déplie ses examens", "Clic sur un organe : ses pathologies", "Clic sur une pathologie : fenêtre à deux clichés"], "regleLocale": "Tu pars d'une région, puis tu choisis l'examen, l'organe et la pathologie.", "exemple": "Thorax → radiographie → plèvre → pneumothorax."},
        {"id": "X4", "nom": "Fenêtre à deux clichés", "but": "Lire une image", "zones": ["Cliché brut à gauche", "Cliché annoté à droite (repères numérotés)", "Description numérotée des lésions", "Diagnostic et conduite"], "interactions": ["Survol d'un repère : sa description", "Bouton « masquer les repères »"], "regleLocale": "Tu observes d'abord le cliché brut, puis tu compares avec l'annoté.", "exemple": "Pneumothorax : ligne pleurale visible, absence de trame au-delà."},
        {"id": "X5", "nom": "Onglet Explorations fonctionnelles", "but": "Partir d'une fonction", "zones": ["Liste des fonctions (respiratoire, cardiaque, neurologique, musculaire, sommeil…)", "Tracés types, normaux et pathologiques"], "interactions": ["Clic sur une exploration : tracé et interprétation", "Curseurs sur certains tracés (par exemple le rapport VEMS/CVF)"], "regleLocale": "Tu lis le tracé, tu appliques le seuil, puis tu conclus.", "exemple": "VEMS/CVF < 0,70 après bronchodilatateur → trouble ventilatoire obstructif."},
        {"id": "X6", "nom": "Pratique", "but": "S'évaluer", "zones": ["Arène, aventure, examen blanc (A, K', menus longs)"], "interactions": ["Correction commentée"], "regleLocale": "Tu interprètes sous contrainte de temps, comme à l'examen.", "exemple": "Menu long : choisis les 2 diagnostics compatibles avec ce LCR."},
    ],
    parcours=[
        {"n": 1, "etape": "Choisir un onglet", "resultat": "Biologie, Imagerie ou Explorations."},
        {"n": 2, "etape": "Choisir le point de départ", "resultat": "Un prélèvement, une région ou une fonction."},
        {"n": 3, "etape": "Choisir l'examen", "resultat": "La fiche d'interprétation ou la fenêtre à deux clichés s'ouvre."},
        {"n": 4, "etape": "Interpréter", "resultat": "Le calcul, le critère ou la lecture d'image conclut."},
        {"n": 5, "etape": "Débouché", "resultat": "Diagnostic, puis traitement avec posologie sourcée."},
        {"n": 6, "etape": "S'évaluer", "resultat": "Arène, aventure, examen blanc."},
    ],
    donnees=[
        {"fichier": "paraclinique/biologie/prelevements.json", "role": "Index des prélèvements", "champs": ["prelevementId", "nom", "icone", "examens[]"], "producteur": "IA", "volume": "≈ 20"},
        {"fichier": "paraclinique/biologie/examens/<examen>.json", "role": "Fiche d'examen biologique", "champs": ["valeursReference (SI, âge, sexe)", "interpretation[] (seuil → signification)", "calculs[]", "criteres[]", "syndromes[]", "diagnostics[]", "sources[]"], "producteur": "IA, puis REJECTOR_", "volume": "≈ 300"},
        {"fichier": "paraclinique/calculs.json", "role": "Formules versionnées", "champs": ["id", "nom", "formule", "variables (unités)", "interpretation", "source"], "producteur": "IA, puis vérification par tests", "volume": "≈ 40"},
        {"fichier": "paraclinique/criteres.json", "role": "Critères diagnostiques", "champs": ["id", "nom", "elements[]", "regleDeDecision", "source"], "producteur": "IA, puis REJECTOR_", "volume": "≈ 80"},
        {"fichier": "paraclinique/imagerie/regions.json", "role": "Régions et examens faisables", "champs": ["regionId", "maillage3d", "examens[]"], "producteur": "IA", "volume": "11 régions"},
        {"fichier": "paraclinique/imagerie/graphe.json", "role": "Région → examen → organe → pathologie", "champs": ["noeuds[]", "liens[]"], "producteur": "IA", "volume": "1 fichier"},
        {"fichier": "paraclinique/imagerie/cas/<pathologie>.json", "role": "Fenêtre à deux clichés", "champs": ["clicheBrut {src, licence, auteur, url}", "clicheAnnote {src, reperes[] {n, x, y, texte}}", "lesions[] {n, siege, taille, aspect, signesAssocies}", "diagnostic", "conduite", "sourceLocaleUniquement (oui/non)"], "producteur": "Script (Wikimedia Commons) + IA pour la description", "volume": "≈ 600"},
        {"fichier": "paraclinique/explorations/<exploration>.json", "role": "Explorations fonctionnelles", "champs": ["fonction", "traces[] (normal, pathologique)", "seuils[]", "interpretation", "diagnostics[]"], "producteur": "IA", "volume": "≈ 15"},
        {"fichier": "paraclinique/exercices/<onglet>.json", "role": "Exercices générés", "champs": ["type", "question", "options[] (texte, correct, why)", "refs"], "producteur": "Script, 0 token", "volume": "Plusieurs milliers"},
    ],
    exercices=[
        {"type": "Calcul guidé", "exemple": "Calcule le trou anionique, puis conclus.", "generation": "calculs.json + valeurs tirées au hasard dans des plages cliniques"},
        {"type": "Critère", "exemple": "Ce liquide pleural est-il un exsudat selon Light ?", "generation": "criteres.json"},
        {"type": "Prélèvement → examen", "exemple": "Quel examen demander sur ce LCR ?", "generation": "prelevements.json"},
        {"type": "Lecture d'image", "exemple": "Clique la lésion sur le cliché brut.", "generation": "repères du cliché annoté"},
        {"type": "Région → examen de 1re intention", "exemple": "Quel examen d'imagerie faire d'abord ?", "generation": "imagerie/graphe.json"},
        {"type": "Tracé → interprétation", "exemple": "Ce tracé spirométrique est-il obstructif ?", "generation": "explorations"},
    ],
    production=[
        {"n": 1, "etape": "Écrire et tester les formules de calculs.json", "outil": "IA + tests unitaires", "cout": "Faible", "controle": "Chaque formule vérifiée sur des cas connus"},
        {"n": 2, "etape": "Pilote Biologie : sang veineux, urine, LCR, ascite", "outil": "API Claude, Batch", "cout": "Payant, une fois", "controle": "REJECTOR_ vert"},
        {"n": 3, "etape": "Pilote Imagerie : thorax", "outil": "Script Wikimedia + IA pour les descriptions", "cout": "Faible", "controle": "Licences vérifiées"},
        {"n": 4, "etape": "Pilote Explorations : spirométrie, ECG", "outil": "API Batch", "cout": "Faible", "controle": "Seuils sourcés"},
        {"n": 5, "etape": "Extension à tous les prélèvements, régions et explorations", "outil": "API Batch", "cout": "Payant", "controle": "Mêmes portes"},
    ],
    construction=[
        {"n": 1, "phase": "Schémas, formules et critères", "livrable": "9 schémas, calculs.json testé, criteres.json", "sortie": "100 % des tests de formules passent"},
        {"n": 2, "phase": "Pilote Biologie", "livrable": "4 prélèvements complets", "sortie": "REJECTOR_ vert"},
        {"n": 3, "phase": "Pilote Imagerie", "livrable": "Thorax, fenêtre à deux clichés", "sortie": "Licences conformes"},
        {"n": 4, "phase": "Pilote Explorations", "livrable": "Spirométrie, ECG", "sortie": "Seuils sourcés"},
        {"n": 5, "phase": "Toile, calculateurs et visionneuse", "livrable": "Réutilisation du moteur commun", "sortie": "Aucun code spécifique à un examen"},
        {"n": 6, "phase": "Pratique", "livrable": "Exercices, arène, aventure, examen blanc", "sortie": "Correction commentée partout"},
        {"n": 7, "phase": "Extension complète", "livrable": "Données seulement", "sortie": "Les quatre audits sont verts"},
    ],
    blocages=["Aucune image n'est produite en SVG : clichés et photos réels, corps en 3D réelle, organes génitaux externes occultés.", "Aucun calcul ne s'affiche sans test unitaire réussi.", "Aucun cliché annoté ne s'affiche sans sa description numérotée des lésions."],
    questionsOuvertes=[],
    prototype={"titre": "Prototype : Imagerie → thorax → Rx PA → poumon droit → pneumonie, fenêtre à deux clichés", "image": "prototypes/paraclinique.png", "centre": "corps 3D", "cadre": "Thorax",
               "colonnes": [["Région : Thorax"], ["Rx thoracique PA", "Échographie pleurale", "CT thoracique injecté"], ["Poumon droit"], ["Pneumonie lobaire", "Pneumonie à pneumocoque"], ["Fenêtre : cliché brut / cliché annoté"]],
               "legende": "La région ouvre ses examens ; l'examen de première intention mène à l'organe, à la pathologie, puis à la preuve d'imagerie annotée."}
)

# ---------- examens complémentaires : catalogue topographique exhaustif (source unique) ----------
from catalogue_paraclinique import TOPO, PRELEVEMENTS, EXPLORATIONS, MODALITES
_nb = lambda k: sum(len(o.get(k, [])) for r in TOPO.values() for o in r.values())
PARACLINIQUE["topographie"] = {"progression": "Région (de la tête aux pieds, puis systèmes transversaux) → organe ciblé → modalités → examens",
    "modalites": MODALITES, "regions": {r: {o: {MODALITES[k]: v for k, v in m.items()} for o, m in org.items()} for r, org in TOPO.items()},
    "compte": {"regions": len(TOPO), "organes": sum(len(r) for r in TOPO.values()), **{MODALITES[k]: _nb(k) for k in MODALITES}}}
PARACLINIQUE["onglets"]["biologie"]["prelevements"] = [f"{k} : {', '.join(v)}" for k, v in PRELEVEMENTS.items()]
PARACLINIQUE["onglets"]["imagerie"]["regions"] = list(TOPO.keys())
PARACLINIQUE["onglets"]["explorations"]["liste"] = EXPLORATIONS
PARACLINIQUE["decisions"].insert(0, {"question": "Comment garantir que rien ne manque ?", "choix": "Un catalogue topographique unique (région → organe → imagerie, biologie, exploration fonctionnelle, endoscopie, anatomopathologie) alimente tous les onglets et la Tétrade ; un script d'audit contrôle la couverture",
    "raison": "Les organes sont toujours la cible des investigations ; une progression topographique de la tête aux pieds rend les oublis visibles."})
PARACLINIQUE["ecrans"].insert(0, {"id": "X0", "nom": "Navigation topographique", "but": "Aller d'une région à l'organe, puis à ses examens",
    "zones": ["Corps 3D réel avec les 9 régions cliquables", "Colonne des organes de la région", "Cinq colonnes de modalités : imagerie, biologie, explorations, endoscopie, anatomopathologie"],
    "interactions": ["Clic sur une région : ses organes apparaissent", "Clic sur un organe : ses examens apparaissent par modalité", "Survol d'un examen : infobulle symétrique (indication, principe, limite, à retenir)"],
    "regleLocale": "Un organe sans examen dans une modalité pertinente bloque la publication (audit de couverture).", "exemple": "Thorax → Cœur → ECG, échocardiographie, troponine, coronarographie, biopsie endomyocardique."})
PARACLINIQUE["blocages"].append("Aucun organe du catalogue ne reste sans examen ; l'audit de couverture doit réussir avant publication.")
TETRADE["ecrans"].append({"id": "E9", "nom": "Onglet Examens complémentaires", "but": "Investiguer un système ou un organe dans un onglet unique",
    "zones": ["Sélecteur de progression : topo-systémique (système → régions → organes) ou topo-organe (organe → modalités)", "Colonnes des modalités : imagerie, biologie, explorations, endoscopie, anatomopathologie", "Lien vers la fiche d'interprétation de la Paraclinique"],
    "interactions": ["Clic sur un organe : ses examens se déploient par modalité", "Survol : infobulle symétrique", "Bouton « Voir dans Paraclinique » : ouvre la fiche complète"],
    "regleLocale": "Les espaces Anatomie et Physiologie ne listent aucun examen : ils renvoient à cet onglet.", "exemple": "Système cardiovasculaire → Cœur → ECG, Holter, échocardiographie, IRM, troponine, NT-proBNP, coronarographie."})
TETRADE["decisions"].insert(0, {"question": "Où placer les examens complémentaires dans la Tétrade ?", "choix": "Dans un onglet singulier, en progression topo-systémique ou topo-organe, alimenté par le catalogue de la Paraclinique",
    "raison": "Les espaces Anatomie et Physiologie restent centrés sur la structure et la fonction ; un seul onglet évite les doublons et les oublis."})
TETRADE["donnees"].append({"fichier": "tetrade/<systeme>/examens.json", "role": "Examens du système en progression topographique (renvois au catalogue)", "champs": ["organe", "region", "examens[] (id du catalogue, modalité)", "progression (topo-systémique | topo-organe)"], "producteur": "Script depuis le catalogue", "volume": "1 fichier par système"})
TETRADE["toile"] = dict(TETRADE["toile"], regles=TETRADE["toile"]["regles"] + ["La navigation horizontale part du corps vers la droite et vers la gauche : ce sens est validé."])

os.makedirs(os.path.join(ICI, "plans"), exist_ok=True)
for p in (TETRADE, PHARMACO, PARACLINIQUE):
    json.dump(p, open(os.path.join(ICI, "plans", f"{p['id']}.plan.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("écrit :", p["id"])
