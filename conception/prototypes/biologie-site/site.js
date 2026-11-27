// Site Biologie : sélectionner une pathologie (ou un examen) et voir son bilan biologique rangé par niveau d'intention.
// Données : donnees/*.json (conception/outils/paraclinique/construire_site_biologie.py, 0 token). Ce module ne rédige aucun texte
// médical : il affiche mot pour mot les fiches auditées et la Tétrade ; ses seules phrases expliquent l'interface.
// La fiche à 3 temps réutilise ficheBioHtml du jeu Paraclinique (../paraclinique/biologie.js).
// Signature : AAI (Anthropic AI)
import { ficheBioHtml } from '../paraclinique/biologie.js';

const $ = s => document.querySelector(s);
const esc = t => String(t ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const sansAccents = s => String(s ?? '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
const json = async u => { const r = await fetch(u); if (!r.ok) throw new Error(`${u} : ${r.status}`); return r.json(); };

const D = { meta: null, pathos: [], exams: [], P: {}, E: {}, glo: {}, GRE: null };
const cache = { fiche: {}, patho: {} };
const etat = { mode: 'patho', f: { mat: new Set(), sys: new Set(), niv: new Set() }, vue: '' };

/* ------------------------------------------------------------------ niveaux d'intention */
const VISEES = ['Diagnostique', 'Retentissement', 'Étiologique', 'Complications', 'Thérapeutique', 'Sortie'];
const T1 = ['Urgence', 'Diagnostic et étiologie', 'Dépistage et bilan préthérapeutique', 'Suivi'];
const T3 = 'Interprétation au temps 3 (niveau non précisé)';
const origineDe = n => n === T3 ? 'temps3' : T1.includes(n) ? 'temps1' : 'tetrade';
function rang(n) {
  const o = origineDe(n);
  if (o === 'tetrade') {
    const [v, g] = n.split(' · ');
    return VISEES.indexOf(v) * 10 + (g === '1re intention' ? 0 : g === 'Gold standard' ? 1 : 2);
  }
  return o === 'temps1' ? 100 + T1.indexOf(n) : 200;
}
// Catégories du filtre latéral (regroupent les niveaux de la Tétrade et ceux déduits du temps 1).
const CATS = [
  ['t-1re', '1re intention (Tétrade)', n => n === 'Diagnostique · 1re intention'],
  ['t-gold', 'Gold standard (Tétrade)', n => n === 'Diagnostique · Gold standard'],
  ['t-autre', 'Autres visées (Tétrade)', n => origineDe(n) === 'tetrade' && !/1re intention|Gold standard/.test(n)],
  ['urg', 'Urgence', n => n === 'Urgence'],
  ['diag', 'Diagnostic et étiologie', n => n === 'Diagnostic et étiologie'],
  ['dep', 'Dépistage et bilan préthérapeutique', n => n === 'Dépistage et bilan préthérapeutique'],
  ['suivi', 'Suivi', n => n === 'Suivi'],
  ['t3', 'Niveau non précisé', n => n === T3]
];
function couleur(n) {
  if (n === 'Diagnostique · 1re intention') return ['#b3122b', '#fdeef0'];
  if (n === 'Diagnostique · Gold standard') return ['#7a0c1e', '#f8e3e7'];
  if (origineDe(n) === 'tetrade') return ['#a15c00', '#fff4e2'];
  return { 'Urgence': ['#b93c0a', '#fff0e8'], 'Diagnostic et étiologie': ['#123c78', '#eaf1fa'],
    'Dépistage et bilan préthérapeutique': ['#2f6f9f', '#e9f4fb'], 'Suivi': ['#1d6b3a', '#e8f5ec'] }[n] || ['#5a687c', '#f1f3f6'];
}
function explication(n) {
  const o = origineDe(n);
  if (o === 'tetrade') { const [v, g] = n.split(' · '); return `La Tétrade range cet examen dans sa visée « ${v} », groupe « ${g} », pour cette pathologie.`; }
  if (o === 'temps1') return `La fiche demande l'examen dans la rubrique « ${n} » de son temps 1, et la phrase citée y nomme la pathologie.`;
  return 'La fiche interprète ce diagnostic au temps 3, sans dire à quel moment du parcours on demande l\'examen.';
}
const ORIG = { tetrade: ['Niveau tiré de la Tétrade', 'r'], temps1: ['Niveau déduit du temps 1', ''], temps3: ['Niveau non précisé', 'g'] };

/* ------------------------------------------------------------------ positions tarifaires masquées (retour de Vial) */
const NUM_TARIF = /\b\d{4}\.\d{2}\b/;
function sansTarif(s) {
  if (typeof s !== 'string') return s;
  const t = s.replace(/\s*\([^()]*\b\d{4}\.\d{2}\b[^()]*\)/g, '')
    .replace(/\s*\(\s*\d+(?:[.,]\d+)?\s*points?\s*\)/g, '')
    .replace(/positions et points lus/g, 'lu')
    .replace(/,?\s*position\s+\d{4}(?:\.\d{2})?/g, '')
    .replace(/\blimitation\s+\d{4}\.\d{2}/g, 'limitation');
  return t.split(/(?<=[.;!?])\s+/).filter(x => !(/Liste des analyses/.test(x) && (NUM_TARIF.test(x) || /\bpoints?\b/.test(x)))
    && !(NUM_TARIF.test(x) && /\bpoints?\b/.test(x))).join(' ').trim();
}
const masquer = o => typeof o === 'string' ? sansTarif(o) : Array.isArray(o) ? o.map(masquer)
  : o && typeof o === 'object' ? Object.fromEntries(Object.entries(o).map(([k, v]) => [k, k.startsWith('_') || k === 'id' ? v : masquer(v)])) : o;

/* ------------------------------------------------------------------ glossaire : sigles développés au survol */
function gloser(h) {
  if (!D.GRE) return h;
  const vus = new Set();
  return String(h).split(/(<[^>]+>)/).map(p => p.startsWith('<') ? p : p.replace(D.GRE, (m, a, b) => {
    if (vus.has(b)) return m;
    vus.add(b);
    return `${a}<abbr class=terme tabindex=0 data-def="${esc(b + ' : ' + D.glo[b])}">${b}</abbr>`;
  })).join('');
}

/* ------------------------------------------------------------------ recherche tolérante (fautes, accents) */
function osa(a, b) {
  const m = a.length, n = b.length, d = Array.from({ length: m + 1 }, (_, i) => [i, ...Array(n).fill(0)]);
  for (let j = 1; j <= n; j++) d[0][j] = j;
  for (let i = 1; i <= m; i++) for (let j = 1; j <= n; j++) {
    const c = a[i - 1] === b[j - 1] ? 0 : 1;
    d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + c);
    if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1);
  }
  return d[m][n];
}
function score(q, cible) {
  const c = sansAccents(cible);
  if (!q || !c) return 0;
  if (c.startsWith(q)) return 100 - c.length / 100;
  const i = c.indexOf(q);
  if (i >= 0) return 85 - i / 10;
  const mots = c.split(/[^a-z0-9]+/).filter(Boolean);
  let tot = 0;
  for (const t of q.split(/\s+/).filter(Boolean)) {
    const tol = t.length <= 3 ? 0 : t.length <= 5 ? 1 : t.length <= 8 ? 2 : 3;
    let best = 0;
    for (const w of mots) {
      if (w.startsWith(t)) { best = 1; break; }
      const dist = Math.min(osa(t, w.slice(0, t.length)), osa(t, w));
      if (dist <= tol) best = Math.max(best, 1 - dist / (t.length + 1));
    }
    if (!best) return 0;
    tot += best;
  }
  return 60 * tot / q.split(/\s+/).filter(Boolean).length;
}
function chercher(q) {
  const nq = sansAccents(q).trim().replace(/\s+/g, ' ');
  if (!nq) return [];
  const base = etat.mode === 'patho'
    ? D.pathos.map(p => ({ id: p.id, nom: p.nom, s: Math.max(score(nq, p.nom), score(nq, p.famille) - 5), sous: p.matrices.join(' · ') }))
    : D.exams.map(e => ({ id: e.id, nom: e.titre, sous: `${e.matrice} · ${D.meta.systemes[e.systeme] || ''}`,
        s: Math.max(score(nq, e.titre), score(nq, e.nom_exact || '') - 4, ...String(e.synonymes || '').split(/[;,]/).map(x => score(nq, x) - 6)) }));
  return base.filter(x => x.s > 0).sort((a, b) => b.s - a.s || a.nom.localeCompare(b.nom, 'fr')).slice(0, 9);
}
function surligner(nom, q) {
  const n = [...nom].map(ch => sansAccents(ch) || ch).join(''), nq = sansAccents(q).trim(), i = nq ? n.indexOf(nq) : -1;
  if (i < 0) return esc(nom);
  const ch = [...nom];
  return esc(ch.slice(0, i).join('')) + '<mark>' + esc(ch.slice(i, i + nq.length).join('')) + '</mark>' + esc(ch.slice(i + nq.length).join(''));
}

/* ------------------------------------------------------------------ barre de sélection */
let sel = -1, res = [];
function majSugg() {
  const q = $('#q').value, ul = $('#sugg');
  res = chercher(q);
  sel = res.length ? 0 : -1;
  if (!q.trim()) { ul.hidden = true; $('#q').setAttribute('aria-expanded', 'false'); return; }
  ul.innerHTML = res.length ? res.map((r, i) => `<li role=option id="s${i}" aria-selected=${i === sel} data-i=${i}><b>${surligner(r.nom, q)}</b><small>${esc(r.sous)}</small></li>`).join('')
    : `<li class=vide role=option aria-disabled=true>Aucune ${etat.mode === 'patho' ? 'pathologie' : 'fiche d\'examen'} ne correspond : essaie un autre mot ou bascule de mode.</li>`;
  ul.hidden = false;
  $('#q').setAttribute('aria-expanded', 'true');
  $('#q').setAttribute('aria-activedescendant', sel >= 0 ? 's' + sel : '');
}
function bouger(d) {
  if (!res.length) return;
  sel = (sel + d + res.length) % res.length;
  document.querySelectorAll('#sugg li').forEach((li, i) => li.setAttribute('aria-selected', i === sel));
  $('#q').setAttribute('aria-activedescendant', 's' + sel);
  document.getElementById('s' + sel)?.scrollIntoView({ block: 'nearest' });
}
function choisir(i) {
  const r = res[i];
  if (!r) return;
  $('#q').value = '';
  $('#sugg').hidden = true;
  $('#q').setAttribute('aria-expanded', 'false');
  location.hash = (etat.mode === 'patho' ? 'patho=' : 'examen=') + encodeURIComponent(r.id);
}
function majMode(m) {
  etat.mode = m;
  document.querySelectorAll('.bascule button').forEach(b => b.setAttribute('aria-checked', b.dataset.mode === m));
  $('#qLabel').textContent = m === 'patho' ? 'Chercher une pathologie' : 'Chercher un examen';
  $('#q').placeholder = m === 'patho' ? 'Ex. : hyperkaliémie, goutte, méningite…' : 'Ex. : potassium, lipase, ECBU, troponine…';
  majSugg();
}

/* ------------------------------------------------------------------ filtres latéraux */
const catsDe = niveaux => new Set(CATS.filter(([, , t]) => niveaux.some(t)).map(([k]) => k));
const coupe = (s, liste) => !s.size || liste.some(x => s.has(x));
const passePatho = p => coupe(etat.f.mat, p.matrices) && coupe(etat.f.sys, p.systemes) && coupe(etat.f.niv, [...catsDe(p.niveaux)]);
const passeExam = e => coupe(etat.f.mat, [e.matrice]) && coupe(etat.f.sys, [e.systeme]) && coupe(etat.f.niv, [...catsDe(e.niveaux)]);
function dessinerFiltres() {
  const puce = (grp, k, l) => `<button type=button class=puce data-g=${grp} data-k="${esc(k)}" aria-pressed=${etat.f[grp].has(k)}>${esc(l)}</button>`;
  $('#listeMat').innerHTML = D.meta.matrices.map(m => puce('mat', m, m)).join('');
  $('#listeSys').innerHTML = Object.entries(D.meta.systemes).map(([k, l]) => puce('sys', k, l)).join('');
  $('#listeNiv').innerHTML = CATS.map(([k, l]) => puce('niv', k, l)).join('');
}

/* ------------------------------------------------------------------ vues */
const main = () => $('#contenu');
function poser(html, titre) {
  main().innerHTML = html;
  document.title = titre ? `${titre} — Biologie` : 'Biologie — le bilan de chaque pathologie';
}

function vueAccueil() {
  etat.vue = 'accueil';
  const lettre = s => sansAccents(s)[0].toUpperCase();
  let cat = '';
  if (etat.mode === 'patho') {
    const L = D.pathos.filter(passePatho), G = {};
    for (const p of L) (G[lettre(p.nom)] ||= []).push(p);
    const ks = Object.keys(G).sort();
    const REP = { 't-1re': 'Diagnostique · 1re intention', 't-gold': 'Diagnostique · Gold standard', 't-autre': 'Retentissement · Biologie', t3: T3 };
    const legende = `<ul class=legende-niv aria-label="Couleur des pastilles">${CATS.map(([k, lab]) => `<li><span class=pt style="--c:${couleur(REP[k] || lab)[0]}"></span>${esc(lab)}</li>`).join('')}</ul>`;
    cat = `<div class=catalogue-tete><h2>Les pathologies</h2><p>Tu cliques sur une pathologie pour voir son bilan biologique ; chaque pastille marque un niveau d'intention présent dans son bilan.</p></div>${legende}
      ${ks.length ? `<ul class=lettres aria-label="Aller à la lettre">${ks.map(k => `<li><a href="#" data-lettre="${k}">${k}</a></li>`).join('')}</ul>` : ''}
      ${ks.map(k => `<section class=groupe-lettre id="l-${k}"><h3>${k}</h3><div class=grille>${G[k].map(p => `
        <a class=tuile href="#patho=${encodeURIComponent(p.id)}"><b>${esc(p.nom)}</b><small>${esc(p.matrices.join(' · '))}</small>
          <span class=pastilles><span class=vh>Niveaux : ${esc(p.niveaux.join(', '))}</span>${[...p.niveaux].sort((a, b) => rang(a) - rang(b)).map(n => `<span class=pt aria-hidden=true style="--c:${couleur(n)[0]}"></span>`).join('')}</span></a>`).join('')}</div></section>`).join('')
        || '<p class="carte vide-cat">Aucune pathologie ne répond à ces filtres : retire un filtre pour élargir le catalogue.</p>'}`;
  } else {
    const L = D.exams.filter(passeExam);
    cat = `<div class=catalogue-tete><h2>Les examens, par prélèvement</h2><p>Tu cliques sur un examen pour lire sa fiche complète.</p></div>
      ${D.meta.matrices.filter(m => L.some(e => e.matrice === m)).map(m => `<section class=groupe-lettre><h3>${esc(m)}</h3><div class=grille>${L.filter(e => e.matrice === m).map(e => `
        <a class=tuile href="#examen=${encodeURIComponent(e.id)}"><b>${esc(e.titre)}</b><small>${esc(D.meta.systemes[e.systeme] || '')} · ${esc(e.disciplines.join(', '))}</small></a>`).join('')}</div></section>`).join('')
        || '<p class="carte vide-cat">Aucun examen ne répond à ces filtres : retire un filtre pour élargir le catalogue.</p>'}`;
  }
  poser(`<section class="carte hero"><p class=sur>Jeu Paraclinique · onglet Biologie</p>
      <h1>Le bilan biologique de chaque pathologie</h1>
      <p class=lede>Tu choisis une pathologie dans la barre de sélection : le site range les examens qui l'investiguent par niveau d'intention et cite la phrase de la fiche qui justifie chaque examen. Tu bascules sur « Examen » pour partir d'une analyse.</p>
      <ol class=etapes>
        <li><b>Tu choisis</b>Tu tapes une pathologie ou un examen ; la recherche tolère les fautes et les accents.</li>
        <li><b>Tu lis le niveau</b>Les examens se rangent de la 1re intention au suivi, avec leur phrase source.</li>
        <li><b>Tu ouvres la fiche</b>Un clic ouvre la fiche à 3 temps : indications, examen, interprétation et traitement.</li>
      </ol></section>
    <section class=bloc aria-labelledby=hOrig><h2 id=hOrig>D'où vient le niveau d'intention</h2>
      <div class=origines>
        <div class=origine style="--c:#b3122b"><h3>La Tétrade</h3><p>Quand la Tétrade nomme la pathologie exactement et qu'une ligne de son bilan nomme l'examen, le site reprend sa visée et son groupe (1re intention, gold standard, retentissement…).</p></div>
        <div class=origine style="--c:#123c78"><h3>Le temps 1 de la fiche</h3><p>Sinon, le site déduit le niveau de la rubrique du temps 1 où la fiche nomme la pathologie : urgence, diagnostic et étiologie, dépistage, suivi.</p></div>
        <div class=origine style="--c:#5a687c"><h3>Le temps 3 seul</h3><p>Sinon, la fiche interprète le diagnostic au temps 3 sans dire quand on la demande : le site l'affiche « niveau non précisé ».</p></div>
      </div></section>
    <section class=bloc aria-label=Catalogue>${cat}</section>`);
}

function carteExamen(l) {
  const e = D.E[l.examen] || {}, [c] = couleur(l.niveau), [ol, oc] = ORIG[l.origine];
  const aussi = (l.temps1 || []).filter(x => x.niveau !== l.niveau);
  return `<article class=carte-ex data-fiche="${esc(l.examen)}" style="--c:${c}">
    <div class=t><b>${esc(l.titre)}</b><button type=button class=ouvrir data-fiche="${esc(l.examen)}" aria-label="Ouvrir la fiche ${esc(l.titre)}">Ouvrir la fiche →</button></div>
    <div class=meta><span class=etiq>${esc(e.matrice || '')}</span><span class="etiq ${oc}" tabindex=0 data-def="${esc(l.source)}">${ol}</span></div>
    <p class=phrase>${esc(sansTarif(l.phrase))}</p>
    ${aussi.length ? `<p class=aussi>La fiche le demande aussi en : ${aussi.map(x => `<span class=terme tabindex=0 data-def="${esc(sansTarif(x.phrase))}">${esc(x.niveau)}</span>`).join(', ')}.</p>` : ''}
  </article>`;
}

async function vuePatho(id) {
  const p = cache.patho[id] ||= await json(`donnees/pathologies/${encodeURIComponent(id)}.json`);
  etat.vue = 'patho:' + id;
  const G = {};
  for (const l of p.liens) (G[l.niveau] ||= []).push(l);
  const niveaux = Object.keys(G).sort((a, b) => rang(a) - rang(b));
  const sys = p.systemes.map(s => D.meta.systemes[s]).filter(Boolean);
  const tet = p.tetrade;
  const prov = tet
    ? `La Tétrade nomme exactement cette pathologie (« ${esc(tet.texte)} ») : <b>le niveau vient de son bilan</b> quand une ligne nomme l'examen ; sinon il se déduit du temps 1 de la fiche.`
    : `La Tétrade ne nomme pas cette pathologie sous ce libellé exact : <b>le niveau se déduit de la rubrique du temps 1</b> où la fiche nomme la pathologie, ou reste « non précisé ».`;
  let h = `<nav class=fil aria-label="Fil d'Ariane"><a href="#">Accueil</a><span aria-hidden=true>›</span><span>Pathologies</span><span aria-hidden=true>›</span><span aria-current=page>${esc(p.nom)}</span></nav>
    <header class="carte entete-page"><p class=fen-sur>Pathologie</p><h1>${esc(p.nom)}</h1>
      <div class=ligne-etiq>${p.matrices.map(m => `<span class=etiq>${esc(m)}</span>`).join('')}${sys.map(s => `<span class="etiq o">${esc(s)}</span>`).join('')}${tet ? '<span class="etiq r">Bilan présent dans la Tétrade</span>' : ''}</div>
      <p class=provenance><span>${prov}</span></p></header>`;
  h += `<section class=bloc aria-labelledby=hBilan><h2 id=hBilan>Le bilan biologique, par niveau d'intention</h2><div class=niveaux>${niveaux.map(n => {
    const [c, f] = couleur(n);
    return `<section class=niveau aria-label="${esc(n)}"><div class=niveau-tete style="--c:${c};--fondn:${f}"><h3>${esc(n)}</h3><p>${esc(explication(n))}</p></div>
      <div class=cartes-ex>${G[n].map(carteExamen).join('')}</div></section>`;
  }).join('')}</div></section>`;
  if (tet) {
    const parV = {};
    for (const l of tet.bilan) (parV[l.visee] ||= []).push(l);
    h += `<section class=bloc aria-labelledby=hTet><h2 id=hTet>Le bilan de référence de la Tétrade</h2>
      <p>La Tétrade donne, pour « ${esc(tet.texte)} », le bilan complet ; les lignes hors biologie restent grisées, et un lien ouvre la fiche quand elle existe.</p>
      <div class=table-defile><table class=tetrade><thead><tr><th scope=col>Groupe</th><th scope=col>Examen</th><th scope=col>Ce que l'examen montre</th><th scope=col>Fiche</th></tr></thead><tbody>
      ${Object.entries(parV).map(([v, ls]) => `<tr class=vis><td colspan=4>${esc(v)}</td></tr>` + ls.map(l => {
        const hors = /^(Imagerie|Clinique|Explorations|Endoscopie|ECG|Génétique|Score|Anatomopathologie)$/.test(l.groupe);
        return `<tr class="${hors ? 'horsbio' : ''}"><th scope=row>${esc(l.groupe)}</th><td>${esc(l.examen)}</td><td>${esc(l.signe)}</td><td>${l.fiches.length
          ? l.fiches.map(f => `<a href="#" data-fiche="${esc(f)}">${esc(D.E[f]?.titre || f)}</a>`).join('<br>') : '<span class=mini>—</span>'}</td></tr>`;
      }).join('')).join('')}</tbody></table></div>
      <p class=mini>Source de la Tétrade : ${esc(tet.source || '—')}</p></section>`;
  }
  if (p.conclusions.length) h += `<section class=bloc aria-labelledby=hConc><h2 id=hConc>Ce que concluent les fiches</h2><ul class=conclusions>${p.conclusions.map(c =>
    `<li><a href="#" data-fiche="${esc(c.examen)}"><b>${esc(D.E[c.examen]?.titre || c.examen)}</b></a><q>${esc(sansTarif(c.phrase))}</q></li>`).join('')}</ul></section>`;
  const vus = new Set(), moyens = p.traitements.filter(m => { const k = (m.specifiques || '') + '|' + (m.posologie || ''); if (vus.has(k)) return false; vus.add(k); return true; });
  if (moyens.length || tet?.traitement?.length) {
    h += `<section class=bloc aria-labelledby=hTrt><h2 id=hTrt>Le traitement</h2><div class=trt>${moyens.map(m => `<article class=moyen>
        <h3>${esc(sansTarif(m.specifiques) || 'Moyen général')}</h3><dl>
        ${m.general ? `<dt>Moyen général</dt><dd>${esc(sansTarif(m.general))}</dd>` : ''}
        ${m.posologie ? `<dt>Posologie</dt><dd>${esc(sansTarif(m.posologie))}</dd>` : ''}
        ${m.source ? `<dt>Source</dt><dd class=mini>${esc(sansTarif(m.source))}</dd>` : ''}
        <dt>Fiche</dt><dd><a href="#" data-fiche="${esc(m.examen)}">${esc(D.E[m.examen]?.titre || m.examen)}</a></dd></dl>
        <p class=aips>Tu vérifies la posologie dans l'AIPS de Swissmedic avant de l'appliquer : <a href="https://compendium.ch" target=_blank rel=noopener>compendium.ch</a>.</p></article>`).join('')}
      ${(tet?.traitement || []).map(([nom, det]) => `<article class=moyen><h3>${esc(nom)}</h3><dl><dt>Selon la Tétrade</dt><dd>${esc(det)}</dd></dl>
        <p class=aips>Tu vérifies la posologie dans l'AIPS de Swissmedic avant de l'appliquer : <a href="https://compendium.ch" target=_blank rel=noopener>compendium.ch</a>.</p></article>`).join('')}</div></section>`;
  }
  const vois = (p.voisines || []).map(v => D.P[v]).filter(Boolean);
  if (vois.length) h += `<section class=bloc aria-labelledby=hVois><h2 id=hVois>Les formes voisines</h2><p>Ces pathologies partagent le même terme de tête ; tu passes de l'une à l'autre en un clic.</p>
    <div class=voisines>${vois.map(v => `<a class="etiq r" href="#patho=${encodeURIComponent(v.id)}">${esc(v.nom)}</a>`).join('')}</div></section>`;
  const src = [...p.sources.map(sansTarif).filter(Boolean), ...(tet?.source ? ['Tétrade : ' + tet.source] : [])];
  h += `<section class=bloc aria-labelledby=hSrc><h2 id=hSrc>Les sources</h2><details class=repli><summary>Tu déplies les sources des fiches citées</summary><div><ol class=sources>${src.map(s => `<li>${esc(s)}</li>`).join('')}</ol></div></details></section>`;
  poser(gloser(h), p.nom);
}

async function fiche(id) {
  return cache.fiche[id] ||= masquer(await json(`donnees/fiches/${encodeURIComponent(id)}.json`));
}
const htmlFiche = d => ficheBioHtml(d, { esc, gloser, outils: {}, existe: x => !!D.E[x] });

async function vueExamen(id) {
  const d = await fiche(id), e = D.E[id];
  etat.vue = 'examen:' + id;
  const G = {};
  for (const x of e.pathologies) (G[x.niveau] ||= []).push(x);
  const niv = Object.keys(G).sort((a, b) => rang(a) - rang(b));
  let h = `<nav class=fil aria-label="Fil d'Ariane"><a href="#">Accueil</a><span aria-hidden=true>›</span><span>Examens</span><span aria-hidden=true>›</span><span aria-current=page>${esc(e.titre)}</span></nav>
    <header class="carte entete-page"><p class=fen-sur>Examen · ${esc(e.matrice)}</p><h1>${esc(e.titre)}</h1>
      <div class=ligne-etiq><span class="etiq o">${esc(D.meta.systemes[e.systeme] || '')}</span>${e.disciplines.map(x => `<span class=etiq>${esc(x)}</span>`).join('')}</div>
      <p class=lede>${esc(sansTarif(e.nom_exact || ''))}</p></header>`;
  h += `<section class=bloc aria-labelledby=hLiees><h2 id=hLiees>Les pathologies que cet examen diagnostique ou suit</h2>${niv.length ? `<div class="carte liees" style="padding:16px 20px">${niv.map(n =>
    `<div class=grp><span style="color:${couleur(n)[0]}">${esc(n)}</span>${G[n].map(x => `<a class="etiq r" href="#patho=${encodeURIComponent(x.id)}">${esc(x.nom)}</a>`).join('')}</div>`).join('')}</div>`
    : '<p class="carte vide-cat">Aucune pathologie indexée ne renvoie encore à cette fiche.</p>'}</section>`;
  h += `<section class=bloc aria-labelledby=hFiche><h2 id=hFiche>La fiche à 3 temps</h2><div class="carte fiche-page fiche">${htmlFiche(d)}</div></section>`;
  poser(gloser(h), e.titre);
}

/* ------------------------------------------------------------------ fenêtre de fiche */
let retourFocus = null;
async function ouvrirFiche(id) {
  const d = await fiche(id), e = D.E[id] || {};
  retourFocus = document.activeElement;
  $('#fenSur').textContent = 'Fiche à 3 temps · ' + (e.matrice || '');
  $('#fenTitre').textContent = e.titre || id;
  $('#fenPage').href = '#examen=' + encodeURIComponent(id);
  $('#fenCorps').innerHTML = htmlFiche(d);
  $('#fenCorps').scrollTop = 0;
  $('#voile').hidden = false; $('#fenetre').hidden = false;
  requestAnimationFrame(() => { $('#voile').classList.add('on'); $('#fenetre').classList.add('on'); });
  $('#fenFermer').focus();
}
function fermerFiche(majHash = true) {
  if ($('#fenetre').hidden) return;
  $('#voile').classList.remove('on'); $('#fenetre').classList.remove('on');
  $('#fenetre').hidden = true; $('#voile').hidden = !$('#filtres').classList.contains('ouvert');
  if (majHash) { const h = new URLSearchParams(location.hash.slice(1)); if (h.has('fiche')) { h.delete('fiche'); history.replaceState(null, '', '#' + h.toString()); } }
  retourFocus?.focus?.();
}

/* ------------------------------------------------------------------ routage par hash (#patho=…, #examen=…, &fiche=…) */
async function route() {
  const h = new URLSearchParams(location.hash.slice(1));
  const pa = h.get('patho'), ex = h.get('examen'), fi = h.get('fiche');
  const cle = pa ? 'patho:' + pa : ex ? 'examen:' + ex : 'accueil';
  try {
    if (cle !== etat.vue || cle === 'accueil') {
      fermerFiche(false);
      if (pa && D.P[pa]) await vuePatho(pa);
      else if (ex && D.E[ex]) await vueExamen(ex);
      else vueAccueil();
      if (cle !== 'accueil' || location.hash) { window.scrollTo(0, 0); main().focus({ preventScroll: true }); }
    }
    if (fi && D.E[fi]) await ouvrirFiche(fi); else fermerFiche(false);
  } catch (err) {
    poser(`<section class="carte entete-page"><h1>La page ne s'ouvre pas</h1><p>Le fichier de données ne répond pas : tu recharges la page ou tu reviens à l'<a href="#">accueil</a>.</p><p class=mini>${esc(err.message)}</p></section>`);
  }
}
function allerFiche(id) {
  const h = new URLSearchParams(location.hash.slice(1));
  if (h.get('patho')) { h.set('fiche', id); location.hash = h.toString(); }
  else location.hash = 'examen=' + encodeURIComponent(id);
}

/* ------------------------------------------------------------------ infobulle (encre blanche sur fond sombre) */
let ancre = null;
function montrerBulle(el) {
  const b = $('#bulle'), t = el.getAttribute('data-def');
  ancre = el;
  if (!t) return;
  b.textContent = t; b.hidden = false;
  const r = el.getBoundingClientRect(), bw = b.offsetWidth, bh = b.offsetHeight;
  let x = Math.min(Math.max(12, r.left), innerWidth - bw - 12), y = r.bottom + 8;
  if (y + bh > innerHeight - 8) y = Math.max(8, r.top - bh - 8);
  b.style.left = x + 'px'; b.style.top = y + 'px';
}
const cacherBulle = () => { $('#bulle').hidden = true; ancre = null; };
// Au défilement, l'infobulle suit son ancre tant que celle-ci reste visible.
const suivreBulle = () => { if (!ancre) return; const r = ancre.getBoundingClientRect();
  if (r.bottom < 0 || r.top > innerHeight || !ancre.isConnected) cacherBulle(); else montrerBulle(ancre); };

/* ------------------------------------------------------------------ démarrage */
async function demarrer() {
  const [meta, pathos, exams, glo] = await Promise.all(['meta', 'pathologies', 'examens', 'glossaire'].map(n => json(`donnees/${n}.json`)));
  Object.assign(D, { meta, pathos, exams, glo });
  pathos.forEach(p => { D.P[p.id] = p; });
  exams.forEach(e => { D.E[e.id] = e; });
  const ks = Object.keys(glo).filter(k => k.length >= 2 && /[A-Z]/.test(k) && /[A-Za-z0-9+]$/.test(k)).sort((a, b) => b.length - a.length);
  D.GRE = ks.length ? new RegExp('(^|[^\\wÀ-ÿ\\-])(' + ks.map(t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')(?![\\wÀ-ÿ])', 'g') : null;
  dessinerFiltres();

  const q = $('#q');
  q.addEventListener('input', majSugg);
  q.addEventListener('focus', () => q.value && majSugg());
  q.addEventListener('keydown', ev => {
    if (ev.key === 'ArrowDown') { ev.preventDefault(); if ($('#sugg').hidden) majSugg(); else bouger(1); }
    else if (ev.key === 'ArrowUp') { ev.preventDefault(); bouger(-1); }
    else if (ev.key === 'Enter') { ev.preventDefault(); choisir(sel >= 0 ? sel : 0); }
    else if (ev.key === 'Escape') { $('#sugg').hidden = true; q.setAttribute('aria-expanded', 'false'); }
  });
  $('#selecteur').addEventListener('submit', ev => ev.preventDefault());
  $('#sugg').addEventListener('mousedown', ev => { const li = ev.target.closest('li[data-i]'); if (li) { ev.preventDefault(); choisir(+li.dataset.i); } });
  q.addEventListener('blur', () => setTimeout(() => { $('#sugg').hidden = true; q.setAttribute('aria-expanded', 'false'); }, 120));
  document.querySelectorAll('.bascule button').forEach(b => b.addEventListener('click', () => {
    majMode(b.dataset.mode);
    if (etat.vue === 'accueil') vueAccueil();
    q.focus();
  }));
  document.addEventListener('keydown', ev => {
    if (ev.key === '/' && !/INPUT|TEXTAREA/.test(document.activeElement.tagName)) { ev.preventDefault(); q.focus(); }
    if (ev.key === 'Escape') { cacherBulle(); fermerFiche(); fermerFiltres(); }
    if (ev.key === 'Tab' && !$('#fenetre').hidden) {
      const f = [...$('#fenetre').querySelectorAll('a[href],button,summary,[tabindex="0"]')].filter(x => x.offsetParent);
      if (f.length) { const a = f[0], z = f[f.length - 1];
        if (ev.shiftKey && document.activeElement === a) { ev.preventDefault(); z.focus(); }
        else if (!ev.shiftKey && document.activeElement === z) { ev.preventDefault(); a.focus(); } }
    }
  });

  // Filtres latéraux (et tiroir sur petit écran).
  $('#filtres').addEventListener('click', ev => {
    const b = ev.target.closest('.puce');
    if (!b) return;
    const s = etat.f[b.dataset.g];
    s.has(b.dataset.k) ? s.delete(b.dataset.k) : s.add(b.dataset.k);
    b.setAttribute('aria-pressed', s.has(b.dataset.k));
    if (etat.vue !== 'accueil') location.hash = ''; else vueAccueil();
  });
  $('#raz').addEventListener('click', () => { Object.values(etat.f).forEach(s => s.clear()); dessinerFiltres(); if (etat.vue === 'accueil') vueAccueil(); });
  $('#btnFiltres').addEventListener('click', () => {
    const o = !$('#filtres').classList.contains('ouvert');
    $('#filtres').classList.toggle('ouvert', o); $('#btnFiltres').setAttribute('aria-expanded', o);
    $('#voile').hidden = !o && $('#fenetre').hidden; if (o) $('#voile').classList.add('on');
  });
  $('#voile').addEventListener('click', () => { fermerFiche(); fermerFiltres(); });

  // Délégation : cartes d'examen, liens vers une fiche, lettres du catalogue.
  document.addEventListener('click', ev => {
    const l = ev.target.closest('[data-lettre]');
    if (l) { ev.preventDefault(); document.getElementById('l-' + l.dataset.lettre)?.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); return; }
    const f = ev.target.closest('[data-fiche]');
    if (f && !ev.target.closest('.terme,[data-def]:not([data-fiche])')) { ev.preventDefault(); allerFiche(f.dataset.fiche); }
  });
  ['mouseover', 'focusin'].forEach(t => document.addEventListener(t, ev => { const el = ev.target.closest?.('[data-def]'); if (el) montrerBulle(el); }));
  ['mouseout', 'focusout'].forEach(t => document.addEventListener(t, ev => { if (ev.target.closest?.('[data-def]')) cacherBulle(); }));
  addEventListener('scroll', suivreBulle, { passive: true });
  addEventListener('hashchange', route);
  $('#fenFermer').addEventListener('click', () => fermerFiche());
  $('#fenPage').addEventListener('click', () => fermerFiche(false));
  await route();
  document.body.dataset.pret = '1';
}
function fermerFiltres() {
  if (!$('#filtres').classList.contains('ouvert')) return;
  $('#filtres').classList.remove('ouvert'); $('#btnFiltres').setAttribute('aria-expanded', 'false');
  if ($('#fenetre').hidden) { $('#voile').classList.remove('on'); $('#voile').hidden = true; }
}
demarrer().catch(err => {
  main().innerHTML = `<section class="carte entete-page"><h1>Le site ne démarre pas</h1><p>Les données ne se chargent pas : tu ouvres le site par un serveur web (GitHub Pages ou un serveur local), pas en fichier local.</p><p class=mini>${esc(err.message)}</p></section>`;
});
