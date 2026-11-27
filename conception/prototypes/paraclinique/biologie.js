// Onglet BIOLOGIE du jeu Paraclinique (BRIEF_BIOLOGIE_CLAUDE_CODE.md § 2, § 3, § 6).
// Chaîne : prélèvement (matrice) → examen → fiche à 3 temps (fenêtre centrée) → diagnostic → traitement avec posologie.
// Ce module ne rédige aucun texte médical : il affiche mot pour mot les champs des fiches (donnees/biologie/<id>.json).
// Couleurs à sens fixe : bleu = normal, rouge = pathologie, vert = traitement ; la discipline (axe secondaire) colore la case d'examen.
// Signature : AAI (Anthropic AI)

/* ---------------------------------------------------------------- vue : par prélèvement ou par système, filtre par discipline */
export function vueBio(N, { vue, discs }) {
  const ex = new Set(N.filter(n => n.nature === 'Examen' && (!discs.size || discs.has(n.disc))).map(n => n.id));
  const out = [];
  for (const n of N) {
    if (n.vue && n.vue !== vue) continue;
    if (n.id.startsWith('bx_') && !ex.has(n.id.split('__')[0])) continue;
    out.push(n.nature === 'Examen' && vue === 'systeme' && n.deSys ? { ...n, de: n.deSys } : n);
  }
  const parents = new Set(out.flatMap(n => n.de || []));
  return out.filter(n => !n.vue || parents.has(n.id));
}

/* ---------------------------------------------------------------- barre d'outils : bascule de vue et filtre par discipline */
export function barreBio(hote, disciplines, etat, rafraichir) {
  let b = document.getElementById('bioOutils');
  if (!b) { b = document.createElement('div'); b.id = 'bioOutils'; hote.appendChild(b); }
  const esc = t => String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
  b.innerHTML = `<div class=seg role=group aria-label="Ranger les fiches">
      <button data-vue=matrice aria-pressed=${etat.vue === 'matrice'} title="Tu pars du prélèvement : sang, moelle, urines, LCR…">Par prélèvement</button>
      <button data-vue=systeme aria-pressed=${etat.vue === 'systeme'} title="Tu ranges les mêmes fiches par système d'organes">Par système</button></div>
    <div class=discs role=group aria-label="Filtrer par discipline">${Object.entries(disciplines).map(([d, c]) =>
      `<button data-disc="${esc(d)}" style="--c:${c}" aria-pressed=${etat.discs.has(d)} title="Tu n'affiches que la discipline « ${esc(d)} » (re-clic pour la retirer)">${esc(d)}</button>`).join('')}</div>`;
  b.querySelectorAll('[data-vue]').forEach(x => x.onclick = () => { etat.vue = x.dataset.vue; rafraichir(); });
  b.querySelectorAll('[data-disc]').forEach(x => x.onclick = () => { const d = x.dataset.disc; etat.discs.has(d) ? etat.discs.delete(d) : etat.discs.add(d); rafraichir(); });
}

/* ---------------------------------------------------------------- fiche à 3 temps (gabarit identique partout, brief § 3) */
const AP = 'à produire';
const RUBQ = {
  entete: 'L\'en-tête nomme l\'examen, ses synonymes, son prélèvement avec ses conditions, et son bon usage en Suisse (Liste des analyses de l\'OFSP, Smarter Medicine).',
  t1: 'Le temps 1 dit quand tu demandes l\'examen : urgence, diagnostic et étiologie, dépistage et bilan préthérapeutique, suivi ; il dit aussi quand tu ne le demandes pas.',
  t2: 'Le temps 2 lit chaque paramètre seul : la valeur normale (bleu), l\'anomalie avec son seuil (rouge) et le seuil d\'alerte.',
  calc: 'Les calculs donnent la formule, son usage, un exemple résolu et la source ; le bouton 🧮 ouvre le calculateur actif.',
  t3: 'Le temps 3 part d\'une anomalie chiffrée, ajoute les anomalies associées et le syndrome clinique, puis conclut : confirmation, diagnostic, conduite.',
  trt: 'Le traitement donne le but, les moyens (général, puis spécifiques) et la posologie ; tu vérifies toujours la posologie dans l\'AIPS (Swissmedic).',
  pieges: 'Les pièges disent : si tu fais ceci, voici la conséquence pour le patient ; un moyen mnémotechnique aide dès trois entités.',
  src: 'Les sources sont datées avec leur date de lecture ; chaque passerelle donne son type, sa fiche cible et sa raison.'
};
const T1 = [['urgence_aigu', 'Urgence'], ['diagnostic_etiologie', 'Diagnostic et étiologie'], ['depistage_pretherapeutique', 'Dépistage et bilan préthérapeutique'],
  ['suivi_surveillance', 'Suivi'], ['suivi', 'Suivi'], ['ne_pas_demander', 'Ne pas demander']];

export function ficheBioHtml(d, { esc, gloser, outils, existe }) {
  const plein = v => typeof v === 'string' && v.trim() && v.trim() !== '—' && v.trim() !== AP;
  const P = v => plein(v) ? esc(v) : v === AP ? '<span class=apx>à produire</span>' : '<span class=tiret>—</span>';
  const H = (k, t, n) => `<h3 class=bh><span class=num>${n}</span><span class=terme tabindex=0 data-def="${esc(RUBQ[k])}">${t}</span></h3>`;
  const dl = rows => '<dl class=grille>' + rows.filter(([, v]) => v !== undefined).map(([t, v, c]) => `<dt>${t}</dt><dd${c ? ' class=' + c : ''}>${P(v)}</dd>`).join('') + '</dl>';
  const e = d.entete || {}, t1 = d.temps1_indications || {};
  let h = `<p class=meta><b>${esc(d.id)}</b> · système ${esc(d.systeme || '—')} · prélèvement : ${esc(d._matrice)} · discipline : ${esc((d.axe_secondaire || []).join(', '))}</p>`;
  h += H('entete', 'En-tête', 0) + dl([['Nom exact', e.nom_exact], ['Synonymes', e.synonymes], ['Prélèvement et conditions', e.prelevement_conditions], ['Bon usage suisse', e.bon_usage_suisse ?? e.bon_usage_ch]]);
  h += H('t1', 'Temps 1 · Indications', 1) + dl(T1.filter(([k]) => k in t1).map(([k, l]) => [l, t1[k], k === 'ne_pas_demander' ? 'npd' : '']));
  h += H('t2', 'Temps 2 · L\'examen', 2);
  h += Array.isArray(d.temps2_examen) ? d.temps2_examen.map(r => `<div class=param><b>${esc(r.parametre)}</b>${dl([['Normal', r.normal, 'nl'], ['Anomalie et seuil', r.anomalie, 'pa'], ['Seuil d\'alerte', r.seuil_alerte, 'al']])}</div>`).join('') : `<p>${P(d.temps2_examen)}</p>`;
  h += H('calc', 'Calculs', '∑');
  h += Array.isArray(d.calculs) ? d.calculs.map(c => `<div class=param><b>${esc(c.nom || 'Calcul')}</b>${dl([['Formule', c.formule], ['À quoi ça sert', c.a_quoi_ca_sert ?? c.usage], ['Exemple résolu', c.exemple ?? c.exemple_resolu], ['Source', c.source, 'src']])}</div>`).join('') : `<p>${P(d.calculs)}</p>`;
  const ou = (d._outils || []).filter(o => outils[o]);
  if (ou.length) h += '<p class=outils-bio>' + ou.map(o => `<button class=btn data-outil="${o}">🧮 ${esc(outils[o].nom)}</button>`).join(' ') + '</p>';
  h += H('t3', 'Temps 3 · Interprétation', 3);
  h += Array.isArray(d.temps3_interpretation) ? d.temps3_interpretation.map((r, i) => `<details${i ? '' : ' open'} class=t3><summary><span class=pa>${P(r.diagnostic)}</span></summary>${dl([
    ['1 · Anomalie chiffrée', r.entite_anormale_chiffree, 'pa'], ['2 · Associées présentes', r.associees_presentes], ['2 · À rechercher', r.associees_a_rechercher],
    ['3 · Anamnèse', r.syndrome_anamnese], ['3 · Status', r.syndrome_status], ['4 · Confirmation', r.confirmation], ['4 · Diagnostic', r.diagnostic, 'pa'], ['4 · Conduite', r.conduite, 'tt']])}</details>`).join('') : `<p>${P(d.temps3_interpretation)}</p>`;
  h += H('trt', 'Traitement', '℞');
  const tr = d.traitement;
  if (tr && typeof tr === 'object') {
    h += `<p class=tt><b>But.</b> ${P(tr.but)}</p>` + (tr.moyens || []).map(m => `<div class="param trt"><b class=tt>${P(m.specifiques)}</b>${dl([['Diagnostic', m.diagnostic, 'pa'], ['Moyen général', m.general, 'tt'], ['Posologie', m.posologie, 'poso'], ['Source', m.source, 'src']])}</div>`).join('');
  } else h += `<p>${P(tr)} : le bloc Traitement attend sa rédaction sourcée (but, moyens, posologie, renvoi à l'AIPS).</p>`;
  const pg = d.annexeA_pieges;
  h += H('pieges', 'Pièges', '!');
  h += pg && typeof pg === 'object' ? '<ul class=pieges>' + (pg.lignes || []).map(l => `<li>${esc(l.si)} <b>→</b> ${esc(l.consequence)}</li>`).join('') + '</ul>' + (plein(pg.mnemotechnique) ? `<p><b>Mnémotechnique.</b> ${esc(pg.mnemotechnique)}</p>` : '') : `<p>${P(pg)}</p>`;
  h += H('src', 'Sources et passerelles', '§');
  h += Array.isArray(d.sources) ? '<ol class=sources>' + d.sources.map(s => `<li>${esc(s)}</li>`).join('') + '</ol>' : `<p>${P(d.sources)}</p>`;
  if (Array.isArray(d.passerelles)) h += '<ul class=passerelles>' + d.passerelles.map(p => `<li><b>${esc(p.type)}</b> → ${existe(p.cible) ? `<a href="#" data-fiche="${esc(p.cible)}">${esc(p.cible)}</a>` : `<code>${esc(p.cible)}</code>`} : ${P(p.pourquoi)}</li>`).join('') + '</ul>';
  const o = d._origine || {};
  h += `<p class=mini>Origine : ${esc(o.depot || '')} · ${esc(o.chemin || '')} · commit ${esc(String(o.commit || '').slice(0, 10))}.</p>`;
  return gloser(h);
}
