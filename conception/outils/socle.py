"""Socle commun aux trois plans de conception : règles, architecture, arène/aventure, évaluation, audits.
Chaque plan l'intègre, pour qu'un PDF reste lisible seul."""

SIGNATURE = {"start": "2026-11-21 16:02 (Europe/Zurich)", "model": "Opus 5.5", "platform": "Claude"}

PRINCIPES = [
    "Le contenu vit dans des fichiers JSON ; le code ne contient aucune donnée médicale.",
    "Un seul moteur d'affichage sert tous les systèmes, prélèvements ou régions : on ajoute des données, jamais de code.",
    "Chaque réseau est un graphe (nœuds typés + liens typés) ; la toile zoomable de style Obsidian le dessine.",
    "Aucune image n'est en SVG : le corps vient de vrais modèles 3D (BodyParts3D, Z-Anatomy), les clichés et photos viennent du web ; les organes génitaux externes sont toujours occultés.",
    "L'IA rédige une fois la source de vérité ; les scripts en tirent gratuitement les exercices, les calculs et les courbes.",
    "REJECTOR_ vérifie le fond de chaque source avant que le moindre exercice en dérive.",
    "Tout se replie par défaut ; l'utilisateur déplie un circuit à la fois, ce qui protège la lisibilité.",
    "Chaque texte se lit en phrases verbales, en Atkinson Hyperlegible, dans une colonne contenue.",
    "Les posologies suivent la cascade suisse : AIPS, Compendium, sociétés suisses, sociétés européennes ; les molécules s'écrivent en DCI, avec le nom commercial suisse entre parenthèses.",
]

ARCHITECTURE = [
    {"couche": "1. Source de vérité", "contenu": "Graphe JSON par unité (système, prélèvement, région ou exploration) et fiches de nœuds", "producteur": "IA (API Batch + cache), puis REJECTOR_", "cout": "Payé une fois"},
    {"couche": "2. Dérivés calculés", "contenu": "Exercices, calculateurs, courbes pharmacocinétiques, index de recherche", "producteur": "Scripts Python", "cout": "0 token"},
    {"couche": "3. Affichage", "contenu": "Toile zoomable (graphe), mannequin 3D, fenêtres de détail", "producteur": "Un seul moteur (TypeScript + three.js + canvas 2D, sans SVG)", "cout": "Écrit une fois"},
    {"couche": "4. Pratique", "contenu": "Arène, aventure, examen blanc (A, K', menus longs)", "producteur": "Moteur du jeu Jeux_45_Spec", "cout": "Partagé avec le jeu"},
]

TOILE = {
    "moteur": "three.js pour le mannequin 3D réel ; canvas 2D pour les traits ; HTML pour les cases ; skill « obsidian-like-complex-network »",
    "regles": [
        "Aucun trait ne traverse le corps, sauf le départ d'un organe : un segment horizontal sort du corps par le côté le plus proche, puis une horizontale ou une oblique rejoint la première case.",
        "Un parent émet une horizontale qui aboutit à une barre verticale ; cette barre regroupe ses enfants, placés de façon symétrique autour de lui, et chaque enfant reçoit une courte horizontale fléchée.",
        "Quand plusieurs parents mènent à une même entité, leurs horizontales aboutissent à une barre verticale commune, d'où part une seule horizontale fléchée vers l'entité.",
        "Les cases sont des rectangles arrondis, de largeur égale dans une colonne ; leur bord côté corps porte la couleur du type ; un « + » signale une suite cachée.",
        "Au départ, seules les cases posées sur le corps sont visibles ; un clic révèle la suite, un second clic la replie.",
        "Le bouton ↺ a deux issues : un clic replie le dernier circuit ouvert (repli sélectif), un double-clic replie tout (réinitialisation globale).",
        "Le bouton de thème fait défiler sept fonds contrastés : blanc, bleu ciel, champagne, or, menthe, nuit, anthracite ; les cases restent opaques et le texte presque noir (ou blanc sur fond sombre), pour que l'écrit domine toujours le fond.",
        "La largeur des colonnes s'ajuste automatiquement à l'écran, pour que tout le réseau reste visible.",
    ],
}

ARENE_AVENTURE = {
    "arene": [
        "Le joueur affronte des duels de 60 à 90 s, tirés des exercices du module.",
        "Une erreur dangereuse coûte trois fois plus qu'une erreur mineure.",
        "Après une erreur, l'échelle de correction s'ouvre : 0-D, mécanisme, sémiologie, discriminant, décision, piège, ancre.",
        "Le joueur rejoue aussitôt une variante de la même notion, et la réussir rapporte le double.",
    ],
    "aventure": [
        "Le joueur traverse un système comme un voyage : du normal à la perturbation, puis à la réparation.",
        "Chaque étape débloque un nœud de la toile ; la toile se colore au fil des réussites.",
        "Un boss clôt chaque système : un cas long en 6 étapes, du triage au suivi.",
    ],
    "retention": "La répétition espacée (FSRS) planifie chaque notion ; les révisions du jour passent avant les nouveautés.",
    "gardeFous": "Les sessions durent 12 minutes par défaut ; aucune notification de 22 h à 7 h ; une série manquée ne retire aucun point.",
}

EVALUATION = [
    {"format": "Type A", "regle": "5 options, 1 seule correcte ; chaque option porte son explication propre."},
    {"format": "K' (Kprim)", "regle": "4 affirmations vrai/faux ; barème suisse : 4 justes = 1 point, 3 justes = ½ point, sinon 0."},
    {"format": "Menu long", "regle": "Une vignette, puis une liste de 15 à 26 réponses possibles ; le candidat choisit la ou les bonnes."},
    {"format": "Examen blanc", "regle": "Blocs chronométrés : 60 % A, 40 % K', menus longs intégrés ; les corrections n'apparaissent qu'à la fin."},
]

AUDITS = [
    {"audit": "Fonctionnement", "controle": "Parcours complet de chaque écran (Playwright), rendu à 1280 px et 390 px, console sans erreur, accessibilité (axe-core)", "seuil": "100 % vert ; 0 violation grave"},
    {"audit": "Médical", "controle": "REJECTOR_ sur chaque source ; contre-audit par une IA d'un autre fournisseur ; posologies contrôlées contre l'index AIPS ; échantillon humain de 5 %", "seuil": "0 rejet de fond restant ; erreurs humaines < 2 %"},
    {"audit": "Psychologique", "controle": "Boucle échec → correction → revanche présente ; garde-fous respectés ; durée des sessions mesurée", "seuil": "Échelle affichée après 100 % des erreurs ; < 10 % de sessions au-delà du plafond"},
    {"audit": "Cohérence des données", "controle": "Chaque lien pointe vers un nœud existant ; chaque nœud médical porte une source ; aucun exercice ne contredit sa source", "seuil": "100 %"},
]

BLOCAGES_COMMUNS = [
    "Aucun exercice ne dérive d'une source sans verdict « pass » de REJECTOR_.",
    "Aucune posologie n'apparaît sans source de la cascade suisse.",
    "Aucune image anatomique ou sémiologique n'est dessinée par une IA.",
    "Aucun fichier HTML produit ne perd la signature de son agent (heure, modèle, plateforme).",
    "Aucune phrase nominale n'apparaît dans un texte didactique.",
]
