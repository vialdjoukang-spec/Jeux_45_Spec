// Calculateurs de la Biologie (plan § 4 : « calculateurs exécutés par script, à partir de formules versionnées »).
// Chaque formule reprend mot pour mot conception/donnees/paraclinique/calculs.json ; les seuils affichés sont ceux que cite l'interprétation du même fichier.
// Tests : conception/outils/paraclinique/test_calculs.mjs (aucun calcul ne s'affiche sans test réussi, plan § 21). Signature : AAI (Anthropic AI)
const r1 = x => Math.round(x * 10) / 10, r2 = x => Math.round(x * 100) / 100;
export const CALCS = {
  calc_trou_anionique: { v: [['na', 'Na⁺', 'mmol/l', 140], ['cl', 'Cl⁻', 'mmol/l', 104], ['hco3', 'HCO₃⁻', 'mmol/l', 24]], u: 'mmol/l',
    f: v => v.na - (v.cl + v.hco3) },
  calc_trou_anionique_corrige: { v: [['ta', 'Trou anionique observé', 'mmol/l', 12], ['albn', 'Albumine normale du laboratoire', 'g/l', 40], ['alb', 'Albumine mesurée', 'g/l', 20]], u: 'mmol/l',
    f: v => v.ta + 0.25 * (v.albn - v.alb) },
  calc_trou_anionique_urinaire: { v: [['na', 'Na⁺ urinaire', 'mmol/l', 40], ['k', 'K⁺ urinaire', 'mmol/l', 30], ['cl', 'Cl⁻ urinaire', 'mmol/l', 90]], u: 'mmol/l',
    f: v => v.na + v.k - v.cl, lire: x => x < 0 ? 'Le trou est négatif : il oriente vers une perte digestive de bicarbonate (Batlle, 1988).' : 'Le trou est positif : il oriente vers un défaut d\'excrétion rénale d\'ammonium (Batlle, 1988).' },
  calc_sodium_corrige_glycemie: { v: [['na', 'Na⁺ mesuré', 'mmol/l', 128], ['glu', 'Glucose plasmatique', 'mmol/l', 30]], u: 'mmol/l',
    f: v => v.na + 2.4 * (v.glu - 5.6) / 5.6 },
  calc_calcium_corrige: { v: [['ca', 'Calcium total mesuré', 'mmol/l', 2.0], ['alb', 'Albumine', 'g/l', 25]], u: 'mmol/l',
    f: v => v.ca + 0.025 * (40 - v.alb) },
  calc_ckd_epi_2021: { v: [['cr', 'Créatinine sérique', 'µmol/l', 90], ['age', 'Âge', 'ans', 60], ['femme', 'Femme (1 = oui, 0 = non)', '', 0]], u: 'ml/min/1,73 m²',
    f: v => { const s = v.cr / 88.4, F = v.femme >= 0.5, k = F ? 0.7 : 0.9, a = F ? -0.241 : -0.302;
      return 142 * Math.pow(Math.min(s / k, 1), a) * Math.pow(Math.max(s / k, 1), -1.2) * Math.pow(0.9938, v.age) * (F ? 1.012 : 1); } },
  calc_cockcroft_gault: { v: [['age', 'Âge', 'ans', 70], ['poids', 'Poids', 'kg', 70], ['cr', 'Créatinine sérique', 'µmol/l', 100], ['femme', 'Femme (1 = oui, 0 = non)', '', 0]], u: 'ml/min',
    f: v => (140 - v.age) * v.poids / (72 * (v.cr / 88.4)) * (v.femme >= 0.5 ? 0.85 : 1) },
  calc_friedewald: { v: [['ct', 'Cholestérol total', 'mmol/l', 5.5], ['hdl', 'HDL-cholestérol', 'mmol/l', 1.3], ['tg', 'Triglycérides', 'mmol/l', 1.5]], u: 'mmol/l',
    f: v => v.ct - v.hdl - v.tg / 2.2 },
  calc_homa_ir: { v: [['glu', 'Glycémie à jeun', 'mmol/l', 5.5], ['ins', 'Insulinémie à jeun', 'µU/ml', 10]], u: '',
    f: v => v.glu * v.ins / 22.5 },
  calc_fib4: { v: [['age', 'Âge', 'ans', 55], ['asat', 'ASAT', 'U/l', 40], ['alat', 'ALAT', 'U/l', 35], ['plq', 'Plaquettes', '10⁹/l', 200]], u: '',
    f: v => v.age * v.asat / (v.plq * Math.sqrt(v.alat)),
    lire: x => x > 3.25 ? 'Le score dépasse 3,25 : la fibrose avancée devient probable (Sterling, 2006).' : x < 1.45 ? 'Le score reste sous 1,45 : il exclut bien une fibrose avancée (Sterling, 2006).' : 'Le score tombe dans la zone grise entre 1,45 et 3,25 : un second test (élastographie) tranche.' },
  calc_apri: { v: [['asat', 'ASAT', 'UI/l', 80], ['lsn', 'Limite supérieure normale de l\'ASAT', 'UI/l', 40], ['plq', 'Plaquettes', '10⁹/l', 150]], u: '',
    f: v => (v.asat / v.lsn) * 100 / v.plq },
  calc_rapport_pao2_fio2: { v: [['pao2', 'PaO₂', 'kPa', 12], ['fio2', 'FiO₂ (fraction)', '', 0.21]], u: 'kPa',
    f: v => v.pao2 / v.fio2,
    lire: x => { const mm = x / 0.1333; return `Le rapport vaut ${r1(mm)} mmHg. ` + (mm <= 100 ? 'Il classe un SDRA comme sévère (Berlin, 2012).' : mm <= 200 ? 'Il classe un SDRA comme modéré (Berlin, 2012).' : mm <= 300 ? 'Il classe un SDRA comme léger (Berlin, 2012).' : 'Il reste au-dessus du seuil de 300 mmHg (40 kPa) de la définition de Berlin.'); } },
  calc_fena: { v: [['nau', 'Na⁺ urinaire', 'mmol/l', 20], ['crp', 'Créatinine plasmatique', 'µmol/l', 200], ['nap', 'Na⁺ plasmatique', 'mmol/l', 140], ['cru', 'Créatinine urinaire', 'µmol/l', 8000]], u: '%',
    f: v => v.nau * v.crp / (v.nap * v.cru) * 100,
    lire: x => x < 1 ? 'La FENa reste sous 1 % : elle oriente vers une azotémie prérénale (Espinel, 1976).' : x > 3 ? 'La FENa dépasse 3 % : elle oriente vers une nécrose tubulaire aiguë (Espinel, 1976).' : 'La FENa tombe entre 1 et 3 % : elle ne tranche pas seule.' },
  calc_feun: { v: [['uu', 'Urée urinaire', 'mmol/l', 300], ['crp', 'Créatinine plasmatique', 'µmol/l', 200], ['up', 'Urée plasmatique', 'mmol/l', 20], ['cru', 'Créatinine urinaire', 'µmol/l', 8000]], u: '%',
    f: v => v.uu * v.crp / (v.up * v.cru) * 100,
    lire: x => x <= 35 ? 'La FEUN reste à 35 % ou moins : elle oriente vers une insuffisance rénale prérénale, même sous diurétiques (Carvounis, 2002).' : 'La FEUN dépasse 35 % : elle oriente plutôt vers une atteinte tubulaire (Carvounis, 2002).' },
  calc_gradient_albumine_ascite: { v: [['as', 'Albumine sérique', 'g/l', 30], ['aa', 'Albumine d\'ascite', 'g/l', 10]], u: 'g/l',
    f: v => v.as - v.aa,
    lire: x => x >= 11 ? 'Le gradient atteint 11 g/l ou plus : il signe une hypertension portale (Runyon, 1992).' : 'Le gradient reste sous 11 g/l : il oriente vers une cause non portale, comme une carcinose ou une tuberculose péritonéale.' }
};
export const arrondi = (x, u) => (Math.abs(x) >= 100 ? Math.round(x) : Math.abs(x) >= 10 ? r1(x) : r2(x));
export function calculer(id, valeurs) {
  const c = CALCS[id]; if (!c) return null;
  const v = Object.fromEntries(c.v.map(([k, , , d]) => [k, valeurs && valeurs[k] !== undefined ? +valeurs[k] : d]));
  const x = c.f(v); return { x, texte: arrondi(x) + (c.u ? ' ' + c.u : ''), lecture: c.lire ? c.lire(x) : '' };
}
