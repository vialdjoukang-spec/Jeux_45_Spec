---
name: "systeme-jouable-builder"
description: "Rend un système d'organes jouable de bout en bout dans Jeux_45_Spec (organes, volets, sémiologie, 4 paliers de pathologies, fenêtres, glossaire, audits). S'active d'office dès qu'on attaque un nouveau système ou qu'on parle de « système suivant »."
---

# Systeme-jouable-builder

Un système est jouable quand l'apprenant peut, depuis le corps 3D, ouvrir chaque organe et parcourir ses 4 espaces (anatomie, physiologie, sémiologie, physiopathologie) jusqu'aux pathologies avec leur bilan, leur traitement et leurs infobulles. Ce skill fabrique ce résultat à partir de simples fichiers texte, à 0 token pour tout ce qui suit la rédaction.

Modèles terminés : `conception/outils/cardio/` (14 organes, 57 pathologies) et `conception/outils/respi/` (10 organes, 41 pathologies). Copie leur niveau, pas leur contenu.

## Relais avec les autres skills

- `organ-catalog-great-master` donne la liste des organes ; la source unique reste `conception/outils/systemes.py` (ordre haut → bas).
- `medical-accuracy-100` gouverne chaque phrase médicale, chaque seuil et chaque posologie.
- `medical-workout` fournit les examens du bilan (noms, visées).
- `obsidian-like-complex-network` dessine le réseau ; ce skill ne touche pas au rendu.
- `panoramic-skill-finder` fait le passage final d'optimisation.

## Architecture (déjà en place, ne pas la refaire)

- `conception/outils/systeme_source.py` lit un dossier de système.
- `conception/outils/systemes_rediges.py` est le registre : `dossier`, `prefixe` d'identifiant, `couleur`, `ids` stables (organes porteurs d'un circuit pilote, ex. `coe`, `pou`).
- `construire_config_tetrade.py` et `generer_json.py` parcourent le registre : aucun code par système.
- `.github/workflows/regeneration.yml` régénère et contrôle tout dès qu'une source change sur main.

## Méthode

1. **Cadrer.** Lire `REPRISE.md`, la liste du système dans `systemes.py` et les liens entre systèmes (`LIENS` dans le constructeur). Un organe partagé n'a qu'une maison : l'autre système y renvoie.
2. **Créer le dossier** `conception/outils/<systeme>/` avec 5 fichiers :
   - `contenu.txt` : volets propres (`V volet | def | second`), puis par organe `# ORG nom exact de systemes.py`, `O def || pourquoi || confusion || retenir`, `A volet` / `P volet`, `- mot | texte | repère ou à retenir | fenêtre facultative`.
   - `semiologie.txt` : `# SEMIO organe`, `T temps`, `- signe | t/a/u | def | pourquoi | confusion | retenir`. Chaque temps a 2 ou 3 signes typiques (`t`), ou un seul signe unique assumé (`u`) ; les signes atypiques (`a`) s'ajoutent librement.
   - `pathologies.txt` : par organe, les 4 paliers `TF`, `F`, `U`, `R` (au moins un piège rare qui imite une maladie fréquente). Chaque pathologie a def, pourquoi, confusion, retenir ; un bilan par visée (`diagnostique` avec un groupe `Gold standard`, `retentissement`, `etiologique`, `complications`, et `therapeutique` si utile) ; des traitements avec posologie ; une ligne `s` de source datée suivie de « posologies à vérifier dans l'AIPS (Swissmedic) ».
   - `glossaire.txt` : chaque sigle employé (`SIGLE = définition` en phrase verbale).
   - `temps.txt` : la bulle de chaque temps d'examen, adaptée au système.
3. **Inscrire le système** en une ligne dans `REDIGES` (`systemes_rediges.py`). Garder l'identifiant stable des organes qui portent un circuit pilote.
4. **Fenêtres.** Chaque mot-clé de physiologie qui gagne à être vu ouvre une courbe calculée dans `conception/prototypes/moteur/fenetres.js` (canvas, jamais de SVG). Réutiliser un modèle existant avant d'en créer un ; un nouveau modèle a des scénarios (`boutons`), des curseurs et une phrase qui interprète le résultat. Les tester sans écran avec Playwright (routage de fichiers, pas de serveur) : 0 erreur, valeurs physiologiques plausibles.
5. **Construire et contrôler.** `construire_config_tetrade.py`, `generer_json.py`, `audit_fond.py`, `auditer_conception.py` (34/34), `auditer_couverture.py`, `non_perte.py`. Un renommage d'identifiant assumé se déclare dans `projets/retours/migrations_ids.json`, jamais en contournant la garde.
6. **Relire médicalement** avant publication : chaque dose, seuil et source. Remplacer toute source incertaine par une source réelle, ou l'indiquer comme avis d'expert.
7. **Publier** : commit en français, push sur main, mise à jour de `REPRISE.md` (section datée) ; synchroniser le PC de Vial si le pont est disponible.

## Règles d'écriture (Vial)

- Phrases entièrement verbales, tutoiement de l'apprenant, unités SI (kPa), contexte suisse.
- Une case garde au plus 45 caractères ; le détail va dans l'infobulle ou la fenêtre.
- Tout sigle d'une infobulle figure au glossaire, sinon l'audit échoue.
- Le bilan affiche des noms courts (au plus 60 caractères) ; le signe recherché va en détail.
- Jamais d'image SVG ; les mots-clés d'anatomie ouvrent la vue 3D réelle.

## Pièges déjà rencontrés

- Une régénération peut effacer des données remplies : `conserver()` et `non_perte.py` l'empêchent ; ne jamais les désactiver.
- Un organe partagé (pharynx, circulation pulmonaire) écrit deux fois crée des doublons : choisir une maison.
- Une fenêtre non déclarée dans `fenetres.js` fait échouer l'audit : écrire le modèle avant de le référencer.
- Les sources citées de mémoire peuvent être fausses : vérifier l'année et l'éditeur.