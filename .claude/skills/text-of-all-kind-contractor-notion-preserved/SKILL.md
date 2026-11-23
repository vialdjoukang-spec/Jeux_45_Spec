---
name: text-of-all-kind-contractor-notion-preserved
description: Contracte n'importe quel texte (cours, rapport, courriel, prompt, skill, contrat, consigne, code commenté, transcription) pour en réduire fortement le volume sans perdre une seule notion, avec inventaire avant/après et contrôle automatique des ancres. S'active dès qu'on parle de raccourcir, résumer sans perte, condenser, densifier, alléger, « trop long », réduire les tokens d'un texte ou d'un prompt, même sans le mot « contracter ».
---

# Text-of-all-kind-contractor-notion-preserved

Ce skill réduit le volume de tout texte en gardant chaque notion. Une notion est une entité d'information autonome : un fait, un chiffre avec son unité, un nom, une date, une condition, une exception, une négation, un lien de cause, un degré de certitude, une instruction, une décision, une source. On contracte la forme ; le fond reste intact.

Pourquoi c'est difficile : un modèle qui raccourcit perd d'abord ce qui est petit et décisif (un « sauf », un « ne… pas », un « peut », une unité). Ce skill traque ces pertes avant et après.

## 0. Choisir le relais
- Texte médical : charger aussi `med-text-contractor`, qui ajoute les règles de dose, de voie et de source ; ce skill-ci reste la méthode générale.
- Prompt ou skill : les instructions, conditions de déclenchement et interdits sont des notions ; un exemple qui illustre une règle déjà écrite peut tomber, un exemple qui définit un cas limite reste.
- Texte juridique ou contractuel : chaque terme défini et chaque délai sont des notions ; aucune synonymie (« doit » ≠ « devrait »).
- Code commenté : on ne touche jamais au code ; on contracte seulement les commentaires et la documentation.

## 1. Inventorier avant de couper
Dresse la liste numérotée des notions du texte source. Note en priorité les conditions (« si », « sauf », « seulement »), les négations, les liens causaux, les modaux (« peut », « doit ») et les quantités, car ce sont elles qui disparaissent le plus souvent. Pour un texte de plus de ~3 000 mots, inventorie par section.

## 2. Contracter, dans cet ordre
1. Supprime les redites : une notion dite deux fois ne reste qu'une fois, là où elle sert.
2. Supprime le remplissage : introductions, précautions oratoires, transitions vides, métadiscours.
3. Fusionne les phrases qui partagent un sujet ou une cause.
4. Remplace chaque périphrase par le terme exact ; un sigle nouveau est défini une fois.
5. Factorise une énumération répétitive en tableau, ou en liste si les éléments sont vraiment parallèles.
6. Déplace le détail secondaire en note, infobulle ou annexe ; ne le supprime pas.

## 3. Ce qui ne se négocie pas
- Garde des phrases verbales et claires ; la contraction ne justifie pas le style télégraphique, sauf si le destinataire est une machine (prompt, configuration).
- Ne généralise pas : « chez l'adulte de plus de 65 ans » ne devient pas « chez l'adulte ».
- Ne change pas le degré de certitude ni la force d'une consigne.
- Garde la langue, le registre et la voix de l'auteur, sauf demande contraire.
- Si une coupe rend une notion ambiguë, garde-la : la qualité prime sur le gain.

## 4. Vérifier après
1. Reprends l'inventaire et coche chaque notion dans la version contractée.
2. Lance le contrôle automatique des ancres (0 token) :
   `python scripts/ancres.py avant.txt apres.txt`
   Il compare les nombres avec unité, sigles, noms propres et URL, et signale toute baisse de négations, conditions, liens causaux ou modaux. Une ancre « PERDUE » est rétablie ; une ligne « À VÉRIFIER » est relue, car une reformulation légitime peut la produire.
3. Livre :
   - le texte contracté ;
   - une ligne de bilan : volume avant → après (mots et %), notions conservées N/N ;
   - la liste de ce qui a été déplacé en note ou annexe, s'il y en a.

## 5. Repères de gain
Un texte rédigé sans contrainte perd souvent 30 à 50 % sans perte de fond ; un texte déjà dense, 10 à 20 %. Si le gain dépasse 60 %, relis l'inventaire deux fois : c'est là que les pertes se cachent.

Signature : AAI (Anthropic AI)
