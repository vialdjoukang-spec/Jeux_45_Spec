# PROMPT DE VIAL — Jeux_Examens_Paraclinique (ÉPINGLÉ, ligne directrice)

> Texte original de Vial, conversation « Refonte frontend cartographie médicale », 21.11.2026 (tour 120), recopié sans retouche. Ce fichier prime sur tout plan dérivé ; tout agent le lit avant d'agir sur Paraclinique.

A présent le Dernier : Jeux_Examens_Paraclinique
Biologie : Un Onglet spécifique
sur prélèvement biologique
en fonction de la Nature du prélèvement : sang, urine, LCR, liquide de ponction d'ascite, Ponction biopsie, Liquide d'épanchement intra -articulaire, etc cite ce que je n'ai pas cité si existant biensur tu as compris le principe : tous les examens ont leur réseau, puis l'interprétations, les calculs utiles/importants à connaitre, les critères diagnostiques ( Critères de Kass par exemple) ...
on part d'un prélèvement on aboutit à l'interprétation avec diagnostiques et biensûr le traitement avec posologie

Imagerie : Un Onglet Spécifique à lui également
là on part par région : l'approche est donc Topographique
de la région le réseau après  clic laisse voir toute les examens possibles faisable dans cette régions : de chaque examen, un réseau de ligne type obsidian débouche sur un système d'organe, en cliquant sur chaque Organe, puis des pathologies et chaque Pathologie  après clic ouvre une fenêtre avec 02 clichés : peu importe d'où ils légalement viennent, dans toute la planète entière : ici particulièrement on s'en fou à droite on a une image avec les Lésions corroborant aux diagnostic avec une Parfaite concise et structuré, énumérative, descriptions des Lésions

Explorations des fonctions (sommeil, musculaire, neurologique . . . etc )
le raisonnement est transposable . . .
partie pratique aussi

## Consignes communes du même message (s'appliquent aussi à Paraclinique)
- N'oublie pas la Psyché.
- Débouché diagnostic : le traitement s'obtient au survol, ou au clic avec un réseau de type Obsidian (le plus adapté).
- Il y a le côté Arène et Aventure pour s'exercer.

## Image de référence validée
`conception/prototypes/paraclinique.png` : Région → examen → organe → pathologie → fenêtre à deux clichés (brut / annoté) sur radiographie réelle.

## Ajouts ultérieurs de Vial (22.11.2026)
- Progression toposystémique de la tête aux pieds, région par région, système par système, organe par organe, pour ne rien oublier.
- Mode Organe et mode Examen dans la barre de recherche ; Théorie et Pratique sont deux onglets distincts.

## Ajout de Vial du 26.11.2026 (17:20) — prime sur la chaîne Imagerie ci-dessus
Problème signalé : clic avec explosion non voulue ; arborescence non progressive ; pas de groupe issu d'une ligne aboutissant sur une perpendiculaire, capable de grouper les entités de même nature.
Imagerie : par région, puis organes ; pour un organe, ses explorations par imagerie, groupées par type (radiographie, scanner/TDM, IRM, TEP, échographie, scintigraphie, etc.) : l'organe fait émerger uniquement les imageries utilisées ; pour chaque examen, les pathologies de l'organe que l'on diagnostique avec cette imagerie (1re intention, etc.).
Chaîne appliquée : Région → Organe → Modalité → Examen → Pathologie → fenêtre à deux clichés.
Précisions vocales du 26.11.2026 (soir) : sous l'organe, chaque type d'imagerie forme un groupe (les neuf types du plan § 10 : radiographie, échographie et Doppler, scanner, IRM, scintigraphie, TEP-CT, angiographie, mammographie, ostéodensitométrie) ; sous chaque examen, les pathologies se rangent par niveau d'indication ; chaque pathologie reste courte (nom et signe), le détail relève d'autres disciplines. Prototype d'abord sur les poumons, validé par Vial avant toute extension.
Ajout de Vial du 26.11.2026 (18:48) : classer les imageries par type d'onde (rayons X d'abord, puis positons et gamma, puis ultrasons ; résonance magnétique en dernier) ; tout sigle développé, avec explication au survol ; pour toute pathologie qu'un examen ne fait qu'orienter, préciser au survol sa 1re intention et son gold standard (angle mort d'examen).
Ajout de Vial du 26.11.2026 (20:29) — fiche flash d'une pathologie en Imagerie (survol et clic) : Définition (vraie, concise) · Épidémiologie (une ligne) · Mécanisme (quelques mots) · Syndrome clinique (liste ; chaque syndrome survolable montre ses composantes cliniques, règle de la répétition espacée) · Sémiologie radiologique (syndromes et signes retrouvés) · Diagnostic (1re intention, gold standard) · Traitement (but ; moyen général avec moyens spécifiques entre parenthèses, chaque thème survolable) · Sources. Tout vient des sources, rien de mémoire. Minimaliste : c'est une révision flash ; la Biologie sera plus exigeante.

## Biologie — prompt élaboré et modèle préconstruit (épinglé le 27.11.2026, 01:05)
Ordre de Vial (27.11, 00:57) : « Les exigences sont dans le prompt le plus élaboré de Biologie, conçu avec ton clone et déposé sur GitHub… Lis le prompt et applique. Il y a aussi un modèle préconstruit de Biologie. »
- **Prompt** : `organigramme-examen-federal/Claude/_progression/CAHIER_ARCHITECTURE_v2.md` (v2, 13.11.2026), § 0 règles, § 5 sous-onglet 1 « Biologie médicale », § 5.1 gabarit de fiche, § 5.2 passerelles, § 7 cartographie des emplacements.
- **Modèle préconstruit** : 101 fiches `Claude/_progression/donnees/examens/EX-1-*.json`, toutes audit-ok (`audits/BIO_RESUME.md`), gabarits `donnees/gabarits.json`, captures `captures/bio_fiche_1280.png`, `bio_calculs_1280.png`.
- **Entrée primaire = matrice (prélèvement)** : sang et buvard, moelle, urines, LCR, selles, sérosités et synovial, respiratoire et ORL, génital et fœto-maternel, salive-sueur-calculs-peau ; bascule « par système » ; axe secondaire = discipline (cytologie-hématologie, hémostase, biochimie, immuno-hormonologie, microbiologie, pharmaco-toxicologie). Unité = un examen ou une lignée.
- **Gabarit de fiche, identique partout** : En-tête (nom exact, synonymes, systèmes, prélèvement et conditions, bon usage suisse : Liste des analyses, Smarter Medicine) · Temps 1 Indications (urgence · diagnostic-étiologie · dépistage-préthérapeutique · suivi · **ne pas demander**) · Temps 2 L'examen (paramètre · normal avec unité · anomalie et seuil · seuil d'alerte — un paramètre lu seul) · Calculs (formule, à quoi ça sert, exemple résolu, source) · Temps 3 Interprétation (entité anormale chiffrée → anomalies associées présentes / à rechercher → syndrome anamnèse / status → confirmation, diagnostic, conduite) · Pièges (si… → conséquence ; mnémotechnique dès 3 entités) · Sources · Passerelles (type, fiche cible, pourquoi).
- **Règles** : sources suisses d'abord (AIPS, HUG, CHUV, sociétés suisses) ; « Selon X » seulement si la page a été lue, sinon « non vérifié CH » ; Atkinson Hyperlegible ≈ 15 px ; une seule fenêtre ouverte ; couleurs à sens fixe (bleu normal, rouge pathologie, vert traitement).
- **Exigence du prompt Paraclinique (21.11)** maintenue : prélèvement → réseau des examens → interprétation, calculs, critères (Kass…) → diagnostic → traitement avec posologie. Vial (26.11) : « En biologie, je serai beaucoup plus exigeant. »
