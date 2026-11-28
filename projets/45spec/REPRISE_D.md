# Point de reprise — producteur groupe D (AAI), 28.11.2026

## Phrase de lancement

« Lis projets/4_Jeux_45_Spec/BRIEF_REPRISE_CLAUDE_CODE.md (y compris le § 7 bis) et projets/45spec/REPRISE_D.md, puis continue le groupe D. »

## État

- Groupe D : **124 / 725** sur `main` (lots D1 à D5 fusionnés). Groupes A et B clos (500/500 chacun). Le groupe C est produit par une autre session : ne pas y toucher.
- Branche de travail : `agent/45spec-D` (à jour avec `main`).
- Prochaines fiches, dans l'ordre du rang : `Z64.0__O1_8-E04` (ambivalence devant une grossesse), `Z71.3_1__O7_3-E05` (régimes végétarien et végétalien), `Z71.3_2__O7_21-E06` (compléments alimentaires), puis `Z71.8_15__O7_10-E06` (consentement du patient allophone).
- Liste à jour : `python projets/45spec/progression_groupe.py D D <spécialités>` puis les lignes « — » de `PROGRESSION_D.md`. Vérifier avant chaque fiche qu'elle n'existe sous aucune spécialité (`content/questions/*/<id>.json`).

## Méthode qui a fonctionné

1. `git fetch origin main` et `git merge origin/main` avant chaque lot.
2. Lire la fiche canonique (`P.canoniques(None)`) : `ssp`, `nomSSP`, `circuit`, portes. Reprendre `nomSSP` tel quel dans la forme compacte.
3. Ouvrir chaque source (curl, `pdftotext`, grep ciblé) ; le réseau est désormais sans restriction. Citer avec la date de lecture ; sinon « (à vérifier) ».
4. Écrire la forme compacte dans `projets/45spec/compact_D/dNN_<ID>.py` (modèles : `d01` à `d15`). Cible : 26 à 27 notions, 3 ou 4 de poids 3, au plus 9 de poids 2, les 15 rubriques couvertes ; 14 A, 4 Kprim, 2 menus longs à trois réponses justes ; 5 questions de difficulté 4 ou 5 masquées ; `PLAN = "non_monographique"` si le circuit l'indique.
5. Contrôler : `couverture_compacte.py` (aucune sortie), `outils/masque.py <forme> <mots interdits>`, puis `PYTHONPATH=projets/45spec python projets/45spec/constructeur_agent_45spec.py <forme>` jusqu'à `err {}`.
6. Par lot de trois : `bash projets/45spec/outils/controles45.sh .`, puis le test de l'arène.
7. Commit, push sur `agent/45spec-D`, puis `git push origin agent/45spec-D:main` (avance rapide, jamais de force).

## Pièges rencontrés

- **Test de l'arène** : `outils/test_arene.py` échoue ici (module Python Playwright absent). Rejouer le même test avec le Playwright Node préinstallé (serveur local sur la racine, ouverture de `conception/prototypes/arene45/index.html`, comptage des `pageerror`, erreurs console et réponses ≥ 400) ; attendu « erreurs: 0 ». Ne pas lancer `playwright install`.
- **Course sur `main`** : l'autre session et les jauges automatiques y poussent en continu. Après un rejet, refaire `fetch` et `merge` ; un conflit ne touche que des fichiers générés (`decks/MIG.json`, `specs.json`, `RANG_RENDEMENT.json`) : les régénérer par `controles45.sh`, vérifier l'absence de marqueurs, committer, pousser aussitôt.
- **Push vers `main`** : l'envoyer dans une commande à part ; enchaîné à d'autres étapes, il a été refusé une fois par le classificateur de permissions.
- **Angles** : une notion de poids 2 ou 3 doit servir dans deux questions d'angles différents (direct, application, piège) ; sinon la passer à poids 1.
- **Connecteur PubMed** : `get_article_metadata` renvoie des dizaines d'auteurs et `get_full_text_article` des textes entiers ; préférer curl sur la page source et un grep.
- **Compendium** : le résumé (Brevier) ne contient ni les règles d'oubli ni les interactions ; renvoyer à l'AIPS.

## Points « à vérifier » encore ouverts (lots D1 à D5)

- Z32.1_1 : interactions des contraceptifs avec les inducteurs enzymatiques (une question de difficulté 5 en dépend) ; conduite après oubli de pilule (source américaine).
- Z53.1 : adulte inconscient porteur d'un refus écrit — avis HUG 2004 contre droit de la protection de l'adulte de 2013 ; à relire dans le Code civil.
- Z50.8_1 : vitamine D 800 UI/j, non vérifiée sur compendium.ch.
- Z54.0 : indemnité de 80 % dès le 3e jour (rapport fédéral de 2009) ; liste des lésions assimilées.
- Z60.2_2 et Z63.8_2 : parties cliniques largement fondées sur des avis d'expert ; à reprendre avec des sources (réseau ouvert).
- Z60.2 : durée du congé pour un enfant gravement malade (14 semaines) non relue.
- Z63.4_2 : allocation de maternité après un enfant mort-né.
- Z60.8 et Z63.8_2 : articles du Code civil lus sur des reproductions, pas sur Fedlex.
- Détail par fiche : `projets/45spec/RESUME_SESSION_B_D_2026-11-28.md`.

## Règles de Vial (rappel)

Aucun contenu de question dans le chat. Après chaque lot : nombre de fiches, état des contrôles, points à vérifier, jauge. Jamais de push forcé ; une permission refusée s'arrête et se signale.

Signature : AAI (Anthropic AI)
