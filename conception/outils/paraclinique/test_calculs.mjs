// Tests unitaires des calculateurs de la Biologie du jeu Paraclinique (plan § 21 : aucun calcul ne s'affiche sans test réussi).
// Valeurs attendues recalculées à la main depuis les formules de calculs.json. Lancer : node conception/outils/paraclinique/test_calculs.mjs
import { calculer, CALCS } from '../../prototypes/paraclinique/calculs.js';
const cas = [
  ['calc_trou_anionique', {}, 12], ['calc_trou_anionique_corrige', {}, 17], ['calc_trou_anionique_urinaire', {}, -20],
  ['calc_sodium_corrige_glycemie', {}, 138.457], ['calc_calcium_corrige', {}, 2.375],
  ['calc_ckd_epi_2021', { cr: 88.4, age: 60, femme: 0 }, 86.2], ['calc_ckd_epi_2021', { cr: 61.88, age: 50, femme: 1 }, 105.3],
  ['calc_cockcroft_gault', {}, 60.16], ['calc_friedewald', {}, 3.518], ['calc_homa_ir', {}, 2.444], ['calc_fib4', {}, 1.859],
  ['calc_apri', {}, 1.333], ['calc_rapport_pao2_fio2', {}, 57.14], ['calc_fena', {}, 0.357], ['calc_feun', {}, 37.5], ['calc_gradient_albumine_ascite', {}, 20]];
let ko = 0;
for (const [id, v, att] of cas) { const r = calculer(id, v); const ok = Math.abs(r.x - att) <= Math.max(0.01, Math.abs(att) * 0.002); if (!ok) { ko++; console.log('ÉCHEC', id, r.x, 'attendu', att); } }
const testes = new Set(cas.map(c => c[0])); for (const id of Object.keys(CALCS)) if (!testes.has(id)) { ko++; console.log('SANS TEST', id); }
console.log(`${cas.length - ko}/${cas.length} tests réussis`); process.exit(ko ? 1 : 0);
