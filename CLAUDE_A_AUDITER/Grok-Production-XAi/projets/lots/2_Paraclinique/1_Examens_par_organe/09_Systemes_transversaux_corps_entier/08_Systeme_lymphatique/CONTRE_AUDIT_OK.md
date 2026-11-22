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
