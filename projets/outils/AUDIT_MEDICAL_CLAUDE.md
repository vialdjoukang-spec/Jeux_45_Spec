# Protocole d'audit médical par Claude (après la veille)

La veille répare, fusionne et audite mécaniquement chaque nouveau lot sur la branche `veille/audit-medical`.
Rien n'arrive sur `main` sans cet audit médical. Claude reste garant de la qualité du contenu médical.

## 0. Vérifier s'il y a du travail (coût quasi nul)

```
git fetch origin main veille/audit-medical
git merge-base --is-ancestor origin/veille/audit-medical origin/main && echo RIEN
```

S'il n'y a rien en attente, la session s'arrête aussitôt.

## 0 bis. Ce que contient la branche

La branche reçoit deux sources : les lots réparés par la veille, et le travail de l'ouvrier en chaîne (`.github/workflows/ouvrier.yml`), qui exécute par l'API Anthropic les tâches de `projets/ouvrier/FILE_PROCESSUS.json` (systèmes rédigés, lots de compléments). Lis `projets/ouvrier/RAPPORT_OUVRIER.md` : tout ce que l'ouvrier a écrit passe par le même audit médical que les lots de Grok. Une tâche marquée « fait » que ton audit refuse repasse à « en_cours » dans la file, avec la raison dans son résumé.

## 1. Auditer médicalement

1. Basculer sur `veille/audit-medical` et lire `CLAUDE_A_AUDITER/EN_ATTENTE_AUDIT_MEDICAL.json` puis `RAPPORT_VEILLE.md`.
2. Lire le diff des données : `git diff origin/main...origin/veille/audit-medical -- conception/donnees SORTIES_DONNEES_FIABLES`.
3. Contrôler chaque valeur ajoutée ou modifiée selon le skill `medical-accuracy-100` : seuils, doses (mSv), posologies,
   indications, délais, tarifs suisses. Toute valeur douteuse se vérifie sur une source primaire ou une recommandation en vigueur.
4. Corriger directement. Une correction qui servira encore s'ajoute à `CORRECTIONS` ou `RESOLUTIONS` dans `projets/outils/audit_fond.py`.
5. Un doute impossible à trancher reste dans `aVerifierOuverts` avec la raison ; il ne bloque pas le reste.
6. Un lot refusé (illisible) se répare à la main ou se renvoie à Grok par un lot de complément.

## 2. Contrôler puis publier

1. Relancer `audit_fond.py`, `lots_complement.py`, `auditer_conception.py` et `auditer_couverture.py` et `non_perte.py` (aucune valeur remplie sur main ne doit disparaître) : tout doit passer.
2. Déplacer les entrées traitées de `EN_ATTENTE_AUDIT_MEDICAL.json` vers `projets/retours/audits_medicaux.json`
   (verdict, corrections, sources), puis vider la file d'attente (`[]`).
3. Committer sur `veille/audit-medical`, pousser, ouvrir la PR vers `main`, puis la fusionner :

```
gh api repos/vialdjoukang-spec/Jeux_45_Spec/pulls -f head=veille/audit-medical -f base=main -f title="Audit médical : …" -f body="…"
gh api -X PUT repos/vialdjoukang-spec/Jeux_45_Spec/pulls/<n>/merge -f merge_method=merge
```

GitHub met quelques secondes à calculer si la PR est fusionnable : réessayer la fusion toutes les 10 s (au plus 6 fois) tant que la réponse est « not mergeable » avec `mergeable_state` inconnu.

Le corps de la PR liste les lots, les corrections médicales avec leurs sources et les doutes restés ouverts.
La veille suivante voit que la branche est fusionnée et repart de `main`.

Signature : AAI (Anthropic AI)
