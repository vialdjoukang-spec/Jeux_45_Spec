---
name: "organ-catalog-great-master"
description: "Catalogue exhaustif des organes du corps humain en progression topo (région) → systémo (système) → organe, avec filet anti-oubli. S'active d'office dès qu'on organise un travail, cours, jeu, plan ou lot sur un organe, un système ou une région."
---

# Organ catalog great master

Ce skill garantit qu'aucun organe ne manque quand on structure un travail médical. Un plan qui oublie un organe crée un trou que personne ne voit ensuite : le catalogue sert de liste de contrôle avant toute production.

## Méthode (dans l'ordre)
1. **Situe la demande** : elle porte sur une région (topo), un système (systémo) ou un organe.
2. **Déroule les trois axes**, de la coque vers le centre : la région donne ses organes ; chaque organe appartient à un système ; chaque système liste tous ses organes de haut en bas. Tu ne réduis jamais un système à son organe phare (le cardiovasculaire ne se réduit pas au cœur).
3. **Croise les deux axes** : chaque organe d'un système doit se retrouver dans une région, et inversement. Un organe présent d'un seul côté signale soit un oubli, soit une structure transversale qu'il faut nommer comme telle.
4. **Passe le filet anti-oubli** ci-dessous sur la zone traitée.
5. **Complète si besoin** : si la demande descend plus fin que le catalogue (segments, noyaux, muscles nommés, variantes, embryologie, pédiatrie), lance une recherche approfondie, puis range les entités trouvées sous l'organe parent sans casser la hiérarchie.
6. **Rends** un arbre ou un tableau région → système → organe, compté à chaque niveau, avec les ajouts signalés.

## Filet anti-oubli (pour chaque région et chaque système)
Enveloppes et séreuses (méninges, plèvre, péricarde, péritoine, capsules) · vaisseaux nourriciers et retours veineux · lymphatiques et ganglions de drainage · nerfs somatiques, autonomes et plexus · glandes annexes et endocrines incluses · squelette, articulations, muscles et fascias de la zone · peau et phanères en regard · orifices, sphincters et jonctions (œsogastrique, iléocæcale, pyélo-urétérale) · organes pairs, côté droit et côté gauche · organes propres au sexe, à la grossesse et au post-partum · organes propres à l'enfant (thymus actif, fontanelles, cartilages de croissance) et au sujet âgé · reliquats embryonnaires cliniquement utiles (canal artériel, ouraque, canal thyréoglosse) · espaces et loges (médiastin, rétropéritoine, loges de jambe, espaces profonds du cou).

## Catalogue de référence
Source : dépôt Jeux_45_Spec (`conception/outils/systemes.py`, `conception/donnees/paraclinique/topographie/`). Le détail de chaque organe y vit ; ce skill garde la carte.

## A. Topo : 9 régions → 82 organes (balayage scannographique tête → pieds)
- **1. Tête et encéphale** (10) : Articulation temporo-mandibulaire et dents · Cavité buccale et glandes salivaires · Encéphale · Hypophyse et hypothalamus · Méninges et LCR · Nerfs crâniens · Nez, sinus et cavum · Œil et orbite · Oreille et équilibre · Os du crâne et de la face
- **2. Cou** (6) : Ganglions cervicaux · Larynx et pharynx · Masses cervicales et kystes · Parathyroïdes · Thyroïde · Vaisseaux du cou et de la tête
- **3. Rachis, moelle et racines** (4) : Moelle épinière · Queue de cheval et cône terminal · Rachis osseux · Racines et plexus
- **4. Thorax** (9) : Aorte thoracique et artères pulmonaires · Cœur et péricarde · Diaphragme et muscles respiratoires · Médiastin · Œsophage · Paroi thoracique et côtes · Plèvre · Poumons et voies aériennes · Seins
- **5. Abdomen** (16) : Aorte abdominale et vaisseaux digestifs · Appendice · Côlon, rectum et anus · Estomac et duodénum · Foie · Intestin grêle · Pancréas · Paroi abdominale et hernies · Péritoine et ascite · Rate · Reins · Rétropéritoine · Surrénales · Uretères · Veines caves et système porte · Vésicule et voies biliaires
- **6. Pelvis** (9) : Grossesse, fœtus et placenta · Pénis et urètre masculin · Plancher pelvien · Post-partum et allaitement · Prostate et vésicules séminales · Testicules et scrotum · Utérus, col, ovaires et annexes · Vessie et urètre · Vulve, vagin et périnée
- **7. Membres et appareil locomoteur** (12) : Artères des membres · Articulations et synoviale · Cheville et pied · Coude, poignet et main · Épaule · Genou · Hanche et bassin · Muscles · Nerfs périphériques · Os longs et squelette · Tendons et ligaments · Veines des membres
- **8. Peau et phanères** (3) : Ongles et cheveux · Peau · Plaies, ulcères et escarres
- **9. Systèmes transversaux (corps entier)** (13) : Corps entier (bilan d'extension et trauma) · Croissance et développement de l'enfant · Évaluation gériatrique globale · Génétique · Infection et immunité · Métabolisme et endocrinologie · Moelle osseuse et ganglions · Psyché · Sang et hémostase · Sommeil et vigilance · Système lymphatique · Toxicologie et médicaments · Urgences et point-of-care

## B. Systémo : 14 systèmes → 124 organes (de haut en bas dans chaque système)
- **Cardiovasculaire** (14) : Troncs supra-aortiques · Aorte thoracique et crosse · Péricarde · Cœur : myocarde et cavités · Cœur : valves · Cœur : tissu de conduction · Cœur : circulation coronaire · Circulation pulmonaire · Veines caves · Aorte abdominale et artères viscérales · Artères des membres · Veines des membres · Microcirculation · Système lymphatique
- **Respiratoire** (11) : Fosses nasales et sinus · Pharynx · Larynx · Trachée · Bronches et bronchioles · Poumons · Circulation pulmonaire · Plèvre · Diaphragme et muscles respiratoires · Paroi thoracique · Centres respiratoires et chémorécepteurs
- **Neurologique** (13) : Méninges et LCR · Hémisphères cérébraux · Noyaux gris centraux et thalamus · Système limbique et hypothalamus · Tronc cérébral · Cervelet · Nerfs crâniens · Vascularisation cérébrale · Moelle épinière · Racines et plexus · Nerfs périphériques · Jonction neuromusculaire · Système nerveux autonome
- **Psyché** (7) : Fonctions cognitives · Perception et pensée · Affects et humeur · Pulsions, motivation et comportement · Conscience de soi et personnalité · Sommeil et vigilance · Circuits de la récompense et addictions
- **Endocrinien et métabolique** (10) : Hypothalamus et hypophyse · Épiphyse · Thyroïde · Parathyroïdes · Thymus · Pancréas endocrine · Surrénales · Gonades · Tissu adipeux et métabolisme énergétique · Métabolisme phosphocalcique et osseux
- **Digestif et hépatobiliaire** (13) : Cavité buccale et glandes salivaires · Pharynx · Œsophage · Estomac · Duodénum · Foie · Vésicule et voies biliaires · Pancréas exocrine · Jéjunum et iléon · Côlon · Rectum et canal anal · Péritoine · Vascularisation digestive et système porte
- **Rénal et uro-génital** (6) : Reins · Uretères · Vessie · Urètre · Prostate et vésicules séminales · Testicules, épididymes, voies spermatiques, scrotum et pénis
- **Hématologique et oncologique** (7) : Moelle osseuse · Sang : globules rouges · Sang : globules blancs · Plaquettes et hémostase · Rate · Ganglions lymphatiques · Thymus
- **Infectieux et immunitaire** (5) : Barrières · Immunité innée · Immunité adaptative · Complément · Organes lymphoïdes
- **Locomoteur et rhumatologique** (11) : Crâne et face · Rachis · Ceinture scapulaire et épaule · Coude, poignet et main · Bassin et hanche · Genou · Cheville et pied · Os · Articulations et synoviale · Muscles striés squelettiques · Tendons, ligaments et bourses
- **Dermatologique** (6) : Épiderme · Derme et hypoderme · Annexes : poils et cheveux · Annexes : ongles · Glandes sudorales et sébacées · Muqueuses
- **Ophtalmologique et ORL** (9) : Paupières et voies lacrymales · Globe oculaire · Voies optiques · Oreille externe et moyenne · Oreille interne · Nez et sinus · Cavité buccale et pharynx · Larynx · Glandes salivaires
- **Gynéco-obstétrical** (7) : Seins · Ovaires · Trompes · Utérus et col · Vagin et vulve · Plancher pelvien · Placenta et unité fœto-placentaire
- **Pédiatrique** (5) : Croissance staturo-pondérale · Développement psychomoteur · Puberté · Adaptation néonatale · Génétique et dysmorphies