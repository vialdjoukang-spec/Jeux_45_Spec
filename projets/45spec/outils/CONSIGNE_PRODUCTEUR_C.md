# Consigne — producteur d'UNE pathologie du groupe C (45 Spec)

Tu produis une seule pathologie, à la main, sans API. Le relecteur (session principale) fait ensuite les contrôles de fusion et git.

## Périmètre strict
- Tu crées : `projets/45spec/compact_C/<NOM_COMPACT>.py`, les trois JSON écrits par le constructeur, et un journal de preuves `<SCRATCH>/preuves_<ID>.md`.
- Tu ne lances **aucune** commande git qui modifie l'état (ni add, commit, checkout, pull, push, stash), ni `controles45.sh`, ni `couverture_notions.py`, ni `classer_rendement.py`. Tu ne modifies aucun autre fichier.
- Aucun sous-agent. Si un outil web est refusé, tu ne le contournes pas : tu prends une autre source lue, ou tu écris « (à vérifier) ».

## À lire d'abord (dans cet ordre)
1. `.claude/skills/agent-producteur-45spec/SKILL.md` **en entier** (méthode, schéma, leçons : obligatoire ; les chemins `/home/claude/outils/…` y valent `projets/45spec/outils/…`).
2. `projets/4_Jeux_45_Spec/BRIEF_REPRISE_CLAUDE_CODE.md` § 4, 5, 7, 7 bis.
3. Modèle de forme compacte : `projets/45spec/compact_C/c27_R15.py`.
4. Ta fiche : `python3 projets/45spec/outils/fiche.py <ID>` (entité, portes, SSP, circuit, amorces du catalogue, **voisines déjà produites** : prends l'angle des portes non couvertes).

## Sources : rien de mémoire
- Chaque source est **ouverte dans cette session** avant d'être citée (WebSearch, puis WebFetch sur l'URL renvoyée ; connecteur PubMed pour résumés et PMC). Vérifie auteur réel, année, et qu'aucune version plus récente n'existe. Les amorces du catalogue ne sont pas une source.
- Réseau : `curl` ne passe que pour `compendium.ch` et `hug.ch` ; tout le reste par WebSearch / WebFetch / PubMed.
- Ordre : sources suisses d'abord (OFSP, AIPS/Compendium, HUG, CHUV, sociétés suisses, SMW, Revue médicale suisse), puis NICE, ESC, EASL, etc. Une recommandation se cite d'après son propre texte.
- Une affirmation sans source lue s'écrit avec la source « Avis d'expert (à vérifier) ». Jamais de référence, de PMID ni de DOI inventés.
- **Posologies** : chacune est vérifiée sur compendium.ch (`mkdir -p /tmp/src; python3 projets/45spec/outils/aips.py "<nom commercial>" <motifs>` puis lis `/tmp/src/aips_<nom>.txt` ; contrôle le nom du produit renvoyé) et porte la mention exacte « posologies à vérifier dans l'AIPS (Swissmedic) ». Vérifie que le produit, la forme et la voie existent en Suisse ; cite la spécialité suisse ; signale toute discordance recommandation ↔ notice au lieu de trancher.
- Source citée ainsi : `[Organisme ou auteur, titre court (année), passage lu, lu le <date du jour>]` (`date +%d.%m.%Y`).
- Journal de preuves : pour chaque source, l'URL ouverte et, pour chaque chiffre, seuil, dose ou délai repris, la **citation mot pour mot** qui le fonde (une ligne par fait). Un fait sans citation part en « (à vérifier) ».

## Format (non négociable ; le constructeur et `valider()` contrôlent)
- 20 questions : 13–14 A (5 options, 1 juste), 4 Kprim (4 énoncés), 2 MenuLong (12 options, 1 à 3 justes, « Choisissez les N… »), une série progressive de 3–4 étapes.
- Au moins 5 questions `d` 4–5, diagnostic masqué (`m` omis) ; au moins 2 questions `d` 1–2. `m=0` dès que `st` ou `p` nomme ou paraphrase le diagnostic, l'agent ou l'acte.
- Notions : 27–28 (4 de poids 3, 9 de poids 2), les 15 rubriques toutes servies, natures de l'énumération `NATURES`, chaque notion de poids ≥ 2 dans deux questions d'angles différents, chaque notion servie au moins une fois, au plus 6 notions par question.
- Chaque distracteur porte un « why » bref et exact (la raison précise, pas seulement « Faux. »).
- Phrases entièrement verbales, contexte suisse, jamais CNP ni CPCM comme lieu d'un cas. Fond d'examen fédéral, sans érudition gratuite.

## Pièges de l'audit croisé (§ 7 bis) — relis ta copie contre chacun
1. Référence mal attribuée. 2. Kprim faux coté vrai (relis chaque énoncé comme un piège : vrai pour **tout** patient de la vignette ?). 3. Posologie non conforme à la spécialité suisse. 4. Produit ou forme absents en Suisse. 5. Contre-indication omise alors que la vignette pose le terrain. 6. Recommandation périmée. 7. Rien de mémoire.
- Une seule réponse juste par question A : aucun distracteur ne doit être défendable.

## Contrôles à passer avant de rendre la main (tous)
```
cd /home/user/Jeux_45_Spec
python3 projets/45spec/couverture_compacte.py projets/45spec/compact_C/<NOM_COMPACT>.py      # aucune sortie
PYTHONPATH=projets/45spec python3 projets/45spec/constructeur_agent_45spec.py projets/45spec/compact_C/<NOM_COMPACT>.py   # « non couvertes [] | err {} »
python3 projets/45spec/outils/masque.py projets/45spec/compact_C/<NOM_COMPACT>.py <mots et paraphrases du diagnostic>   # aucune ligne « contient » ; d45 masqués ≥ 5 ; d12 ≥ 2
python3 projets/45spec/controle_menus_longs.py <SPEC>     # fautifs : 0 | erreurs valider() : 0
python3 projets/45spec/outils/vueq.py projets/45spec/compact_C/<NOM_COMPACT>.py   # relecture finale : masquage, unicité, Kprim
```

## Rapport final (court, sans recopier de question)
`ID` · ligne de bilan du constructeur · sources ouvertes (titre, année, URL) · médicaments vérifiés au Compendium (produit exact) · points « à vérifier » · discordances de sources · mots testés par `masque.py` · tout écart à cette consigne.

Signature : AAI (Anthropic AI)
