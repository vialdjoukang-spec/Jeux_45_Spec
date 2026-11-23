# CONTRE_AUDIT_OK

Contre-audit croisé interne terminé le 23.11.2026 02:30 (heure de Zurich).
Verdict : conforme après correction

Fichiers couverts :
- 1_Theorie/PF07_Explorations_fonctionnelles_Membres_et_appareil_locomoteur_14-fiches_production_XAi.json
- 2_Pratique/PF07-PR_Explorations_fonctionnelles_Membres_et_appareil_locomoteur_14-fiches_PRATIQUE_production_XAi.json

Contrôles : structure identique au squelette de main (clés, ordre, chemins, _meta, nom/id), JSON valide, sens de chaque champ (fonction, traces avec description de ce qu'on voit, seuils, interprétation, diagnostics), défis pratiques (cohérence cas/réponse/justification, réponses courtes ≤ 45 caractères), sigles du glossaire, citations Smarter Medicine comparées mot pour mot aux listes Top 5 suisses, aucune mention de production ; `controle` : PASS.

Valeurs revérifiées en ligne :
- ESC 2024 (artères périphériques) : IPS ≤ 0,90 confirme l'AOMI, > 1,40 incompressible, index orteil-bras ≤ 0,70, chute > 20 % à l'effort — concordant
- IWGDF/ESVS/SVS 2023 : IPS < 0,9 ou > 1,3, index orteil-bras < 0,70 ; ischémie sévère IPS < 0,4, cheville < 50 mmHg, orteil < 30 mmHg — concordant
- Smarter Medicine : SSA 2024 n° 2 (MAOP) et swiss orthopaedics 2024 n° 4 (décompression sous-acromiale) — textes exacts du corpus, cités mot pour mot

Cherché, non trouvé (déclaré dans _lot.aVerifier) :
- Rupture partielle d'Achille (mouvement conservé) : déduit, non relu dans Maffulli 1998

Corrections faites :
- Doublon tranché : les deux IPS étaient identiques ; l'un est centré sur le pied diabétique (IWGDF 2023, médiacalcose), l'autre sur la claudication (ESC 2024)
- EMG des membres : cas d'indication réaligné sur le profil myogène ; la copie en Rachis a été réécrite (voir 03)
- 2 paraphrases Smarter Medicine remplacées par la citation mot pour mot
- 6 réponses tautologiques remplacées (capillaroscopie, TcPO2, tapis, tests autonomes, EMG, IPS)
- Thompson : diagnostic contradictoire « entorse de cheville » retiré
- Indication : 2 cas « Non » ajoutés (tapis avec IPS de repos déjà pathologique, Lachman sur genou très douloureux) ; avant : 14 Oui sur 14
