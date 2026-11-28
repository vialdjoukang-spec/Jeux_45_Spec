# Résumé de session — groupe C (45 Spec), 27–28.11.2026

**9 pathologies produites et relues, 3 fusionnées sur `main`, 6 en attente sur la branche `agent/45spec-C-suite`.**

```
Groupe C  [█████░░░░░░░░░░░░░░░░░░░░░░░░░]  125 / 800 sur main  (15,6 %)
Branche   [█████░░░░░░░░░░░░░░░░░░░░░░░░░]  131 / 800  (+6 en attente de fusion)
```

## 1. Mise en route
- Le brief (dont le § 7 bis), le skill du producteur, `REPRISE_C.md` et les outils ont été lus.
- La branche `agent/45spec-C-suite` a été créée depuis `main`. Les contrôles de base étaient verts, après installation du module Python Playwright (1.63.0) qui manquait au test d'arène.
- Constat sur l'ordre : 678 pathologies restaient, dont 600 avec un rang antérieur au point de reprise (rangs 1001–1721). La production part de R16.2 vers le rang 1800, avec retour prévu au rang 1001.

## 2. Méthode adoptée
- Un producteur Opus par pathologie, trois en parallèle par lot, comme le brief le demande pour la production. La session principale (Fable 5.2) relit chaque copie contre les pièges du § 7 bis.
- Chaque producteur tient un journal de preuves : URL ouverte et citation mot pour mot pour chaque chiffre, dose ou délai. Les posologies sont vérifiées au Compendium.
- Outils ajoutés dans `projets/45spec/outils/` :
  - `CONSIGNE_PRODUCTEUR_C.md` : consigne d'un producteur ;
  - `fiche.py` : fiche canonique et voisines déjà produites ;
  - `suivant_C.py` : pathologies suivantes dans l'ordre du rang ;
  - `revue.py` : vue de relecture d'une forme compacte ;
  - `barre_C.py` : barre de progression ;
  - `fin_lot_C.sh` : contrôles et fusion dans un arbre séparé.

## 3. Production

| Lot | Pathologies | État |
|---|---|---|
| 10 | R16.2, R18, R23.2 | relu, contrôles verts, fusionné sur `main` |
| 11 | R26.0, R32, R33_1 | relu, contrôles verts, fusion bloquée |
| 12 | R41.8_1, R41.8, R50.2 | relu, `controles45.sh` pas encore lancé |

- La relecture a conduit à une seule correction : un énoncé Kprim de R50.2 donnait pour vrai un fait que deux sources chiffrent très différemment (bradycardie relative, 11 % contre plus de 80 %).

## 4. Incidents
- **Réseau** : l'environnement n'autorise que compendium.ch, hug.ch, chuv.ch et bag.admin.ch. NICE, SMW, Revue médicale suisse, EASL, sams.ch et fedlex sont refusés. Les producteurs sont passés par PubMed/PMC et les sites autorisés, sans contourner ; ce qui n'a pas pu être lu porte « à vérifier ».
- **Conflit sur `main`** : pendant la fusion du lot 11, un producteur du groupe B a poussé sur `main`. Deux fichiers régénérés de l'arène (`conception/prototypes/arene45/decks/MIG.json`, `specs.json`) sont entrés en conflit.
- **Permission refusée** : la commande de résolution a été bloquée par le classifieur. Tout ce qui touche `main` est arrêté depuis, et aucun nouveau lot n'a été lancé.
- **PR #54** : ouverte en brouillon, elle s'est fermée seule quand le lot 10 est entré sur `main`. Elle n'a pas été rouverte.

## 5. Points à vérifier
- **Lot 10** : seuil de 12 cm de la flèche hépatique (source princeps sans résumé) ; EASL 2018, AASLD 2021 et Baveno VIII non lus en entier ; posologie de la spironolactone dans la cirrhose (le résumé du Compendium renvoie à l'information professionnelle).
- **Lot 11** : Benerva (voie et posologie suisses, pas de résumé au Compendium) ; Pradif T marqué hors commerce ; articles de loi non lus dans leur texte (signalement d'un conducteur inapte, art. 383–385 CC).
- **Lot 12** : « causes d'incapacité énumérées de façon exhaustive » (avis d'éthique des HUG 2017) face à l'art. 16 CC, qui finit par « ou d'autres causes semblables » ; directives de l'ASSM non lues ; paliers du semainier LOA V 2026 d'après un extrait de recherche ; gravité et délais d'annonce à Swissmedic non lus à la source.
- **Discordances signalées sans trancher** : albumine après ponction d'ascite (BSG, ADQI, fiche HUG) ; 24 h contre 48 h d'albumine avant de retenir un syndrome hépatorénal ; terlipressine (seul Curapressin porte l'indication suisse) ; thiamine (EFNS contre HUG) ; moment de prise de la tamsulosine ; halopéridol sous-cutané contre voie i.m. enregistrée ; quétiapine hors indication suisse dans le delirium ; propranolol et anxiété (notice suisse contre S3 allemande).

## 6. Ce qui attend la décision de Vial
1. Soit autoriser la reprise des deux fichiers régénérés depuis `main`, la relance de `controles45.sh` et un push sans forcer : les lots 11 et 12 entrent alors sur `main` et la production reprend.
2. Soit laisser `main` de côté tant que le groupe B y travaille : la production continue sur la branche.
3. Pour NICE et les sources suisses manquantes : ajouter `www.nice.org.uk`, `smw.ch`, `www.revmed.ch` et `www.fedlex.admin.ch` aux hôtes autorisés de l'environnement.

Signature : AAI (Anthropic AI)
