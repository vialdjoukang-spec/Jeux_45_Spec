# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 00:15 (heure de Zurich).
Verdict : conforme après correction

Fichiers contrôlés :
- 1_Theorie/P09-08_Examens_Systeme_lymphatique_7-examens_production_XAi.json
- 2_Pratique/P09-08-PR_Examens_Systeme_lymphatique_7-examens_PRATIQUE_production_XAi.json

Contrôles faits : structure identique au squelette de main (clés, ordre, id, nom, _meta) ; JSON valide ; aucun champ vide hors smarterMedicine, radioAnatomieNormale, prelevementRef (referencePour vide seulement là où il l'est sur main) ; étiquettes de 45 caractères au plus ; sigles présents au glossaire ; aucune mention de fabrication du contenu ; doses comparées à l'enquête OFSP 2018 (tableaux 13, 14, 16) et à la directive R-06-06 ; chaque citation Smarter Medicine comparée mot pour mot aux listes Top 5 suisses publiées ; entrées à vérifier relues une à une.

Sources revérifiées en ligne :
- Bhardwaj et al. 2018 (PMC5863006) : ascite chyleuse si triglycérides > 200 mg/dl ; conversion 2,26 mmol/l recalculée (× 0,01129)
- Hart et Wall, NRPB-W4 (2002) : coefficient de 0,2 mSv/(Gy·cm²) « typical of trunk » pour la lymphographie confirmé ; le produit dose-surface de 0,3 Gy·cm² n’a pas pu être relu (PDF inaccessible), l’entrée à vérifier est maintenue

Corrections faites :
- P09-08 — valeur pré-remplie du squelette rétablie à l'identique de main (contre-audit 09-08) : « Liquide d’ascite : albumine (gradient) et polynucléaires » → « Liquide d'ascite : albumine (gradient) et polynucléaires »
- P09-08 — cohérence avec anomaliesElementaires (contre-audit 09-08) : « Adénite granulomateuse : [Granulome épithélioïde, Nécrose caséeuse] » → « [Granulome épithélioïde nécrosant] »

Remarques :
- prelevementRef « biopsies_tissulaires » sur la biopsie ganglionnaire : la règle le réserve à la biologie ; laissé à trancher par l’audit médical.
- syndromesParacliniques « Lymphome » cite « Population monoclonale » et « Immunophénotype anormal », qui relèvent de l’immunohistochimie et ne figurent pas dans anomaliesElementaires ; laissé tel quel.

## Seconde vérification des sources (23.11.2026 00:49, heure de Zurich)

Tirage au hasard parmi les affirmations chiffrées sourcées des fichiers de l'organe ; chaque source nommée a été relue en ligne le 23.11.2026 (PubMed, texte de la recommandation, PDF de l'OFSP téléchargé à nouveau). 5 affirmations vérifiées ; 0 erreur(s) corrigée(s) ; 0 non trouvée(s), ajoutée(s) à _lot.aVerifier.

| # | Affirmation vérifiée | Source relue | Résultat |
|---|---|---|---|
| 1 | Lymphoscintigraphie au Nanocoll : 80 MBq = 0,16 mSv, ou 20 MBq par injection = 0,04 mSv | OFSP, directive NRD de médecine nucléaire V2 du 1.2.2023 (drw-nuk.pdf, téléchargé à nouveau) | conforme |
| 2 | Pseudochylothorax : cholestérol > 5,18 mmol/l avec cristaux | BTS, Roberts et al., Thorax 2023 | conforme |
| 3 | Chylothorax : triglycérides > 1,24 mmol/l, cholestérol bas, sans cristaux | BTS, Roberts et al., Thorax 2023 | conforme |
| 4 | Ganglion cervical métastatique : rapport petit axe sur grand axe > 0,5, hile absent | Ahuja et Ying, Cancer Imaging 2008 (PMC2324368) | conforme |
| 5 | Filariose nocturne : prélèvement entre 22 h et 2 h ; antigène de W. bancrofti à toute heure | OMS, documents du programme d'élimination de la filariose lymphatique (iris.who.int) | conforme |
