// Jeu PARACLINIQUE livré seul : réseau de style Obsidian posé sur le vrai corps 3D, onglets Théorie et Pratique,
// trois onglets de contenu (Imagerie, Biologie, Explorations fonctionnelles), recherche tolérante, mode Organe et mode Examen.
// Le dessin des liens (horizontale, barre verticale qui groupe, flèche) et la disposition symétrique reprennent ../moteur/reseau3d.html ;
// les fenêtres de tracés calculés viennent de ../moteur/fenetres.js (import, sans modification). Signature : AAI (Anthropic AI)
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { ouvrirFenetre } from '../moteur/fenetres.js';
import { CALCS, calculer } from './calculs.js';
import { Pratique } from './pratique.js';

const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
const Q = new URLSearchParams(location.hash.slice(1));
const esc = t => String(t ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
const sansAccent = s => String(s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
const charger = (() => { const c = {}; return u => c[u] ??= fetch(u).then(r => { if (!r.ok) throw new Error(u + ' : ' + r.status); return r.json(); }); })();

const ONGLETS = {
  imagerie: { titre: 'Examens paracliniques — imagerie topographique', chaine: 'Région → organe → modalité (radiographie, échographie, scanner, IRM, TEP, scintigraphie…) → examen → pathologie → fenêtre à deux clichés' },
  biologie: { titre: 'Examens paracliniques — biologie par prélèvement', chaine: 'Prélèvement → examens → interprétation, calculs et critères → diagnostic → traitement avec posologie' },
  explorations: { titre: 'Examens paracliniques — explorations des fonctions', chaine: 'Fonction → exploration → tracé ou résultat → interprétation (seuils) → diagnostic → traitement' }
};
const MODES = {
  theorie: 'La théorie remplit l\'arbre que tu consultes : tu survoles une case pour lire son explication, puis tu ouvres la fiche (📄).',
  pratique: 'La pratique remplit le jeu : tu joues les défis de l\'onglet dans le panneau, et les cases se colorent au fil de tes réussites.'
};
const CORPS = { voile: [-58, -230, 630, 58, -60, 790], opacitePeau: .2, cible: [470, -90, 1080], dist: 4500, fov: 22 };
const TH = [['blanc', 'Blanc'], ['ciel', 'Bleu ciel'], ['champagne', 'Champagne'], ['or', 'Or pâle'], ['menthe', 'Vert pâle'], ['nuit', 'Nuit'], ['anthracite', 'Anthracite']];
let G = 40; const GF = 9, GC = 20;

const etat = { onglet: 'imagerie', mode: 'theorie', N: [], byId: {}, ouvert: new Set(), pile: [], vue: { tx: 0, ty: 0, s: 1 }, organe: null, glo: {}, rub: {} };
const scene = $('#scene'), monde = $('#monde'), cases = $('#cases'), gl = $('#gl'), ln = $('#ln'), bulle = $('#bulle');
let W = 0, H = 0, mobile = false;

/* ======================================================================== 3D réelle */
const R = new THREE.WebGLRenderer({ canvas: gl, antialias: true, alpha: true, preserveDrawingBuffer: true });
R.setPixelRatio(Math.min(1.5, devicePixelRatio || 1)); R.outputColorSpace = THREE.SRGBColorSpace; R.toneMapping = THREE.ACESFilmicToneMapping;
const S = new THREE.Scene(); S.add(new THREE.HemisphereLight(0xffffff, 0x5a4a40, 1.5));
const d1 = new THREE.DirectionalLight(0xffffff, 2.2); d1.position.set(-600, -1200, 1900); S.add(d1);
const d2 = new THREE.DirectionalLight(0xbcd0ff, 1); d2.position.set(900, -300, 600); S.add(d2);
const cam = new THREE.PerspectiveCamera(CORPS.fov, 1, 10, 20000); cam.up.set(0, 0, 1);
let corps = null, M = {}, groupeOrgane = null, cible = CORPS.cible, dist = CORPS.dist, decal = 0, L = 0, Rr = 0;
const proj = v => { const p = v.clone().project(cam); return [(p.x + 1) / 2 * W, (1 - p.y) / 2 * H]; };
function rendre() { R.render(S, cam); }
function poserCamera() { cam.aspect = W / H; cam.updateProjectionMatrix(); cam.position.set(cible[0] + decal, cible[1] - dist, cible[2] + 120); cam.lookAt(cible[0] + decal, cible[1], cible[2]); cam.updateMatrixWorld(); }
function bornes(obj) {
  const bb = new THREE.Box3().setFromObject(obj); let l = 1e9, r = -1e9;
  for (const x of [bb.min.x, bb.max.x]) for (const y of [bb.min.y, bb.max.y]) for (const z of [bb.min.z, bb.max.z]) { const p = proj(new THREE.Vector3(x, y, z)); l = Math.min(l, p[0]); r = Math.max(r, p[0]); }
  L = l - 10; Rr = r + 10; document.documentElement.style.setProperty('--cx', ((L + Rr) / 2 / W * 100) + '%');
}
async function chargerCorps() {
  if (corps) return corps;
  const g = await new GLTFLoader().loadAsync('../moteur/corps.glb');
  g.scene.traverse(o => {
    if (!o.isMesh) return; const k = o.name.replace(/_\d+$/, ''); o.name = k; M[k] = o; o.geometry.computeVertexNormals();
    const col = o.geometry.attributes.color, c = col ? new THREE.Color(col.getX(0), col.getY(0), col.getZ(0)) : new THREE.Color(.8, .6, .5), peau = k === 'peau';
    const m = new THREE.MeshPhysicalMaterial({ color: peau ? new THREE.Color(.62, .52, .48) : c, roughness: peau ? .5 : .45, clearcoat: peau ? 0 : .35, transparent: peau, opacity: peau ? CORPS.opacitePeau : 1, depthWrite: !peau, side: peau ? THREE.FrontSide : THREE.DoubleSide });
    if (peau) { const B = CORPS.voile; /* occultation des organes génitaux externes (skill 3d-images-upload-super) */
      m.onBeforeCompile = s => { s.vertexShader = s.vertexShader.replace('#include <common>', '#include <common>\nvarying vec3 vW;').replace('#include <begin_vertex>', '#include <begin_vertex>\nvW=position;');
        s.fragmentShader = s.fragmentShader.replace('#include <common>', '#include <common>\nvarying vec3 vW;').replace('void main() {', `void main() {\nif(vW.x>${B[0]}.&&vW.x<${B[3]}.&&vW.y>${B[1]}.&&vW.y<${B[4]}.&&vW.z>${B[2]}.&&vW.z<${B[5]}.)discard;`); }; }
    o.material = m;
  });
  corps = g.scene; window.__corps = Object.keys(M).length; return corps;
}
function montrerCorps(focus) {
  if (groupeOrgane) { S.remove(groupeOrgane); groupeOrgane = null; }
  if (!corps.parent) S.add(corps);
  for (const [k, o] of Object.entries(M)) { o.visible = true; if (k !== 'peau') { o.material.transparent = !!focus && k !== focus; o.material.opacity = focus && k !== focus ? .18 : 1; o.material.depthWrite = !(focus && k !== focus); } }
  if (focus && M[focus]) { const c = new THREE.Box3().setFromObject(M[focus]).getCenter(new THREE.Vector3()); cible = [c.x, c.y, c.z]; dist = 2300; }
  else { cible = CORPS.cible; dist = CORPS.dist; }
  decal = 0; poserCamera(); bornes(M.peau || corps);
}
async function montrerOrgane3D(a3d) {
  const g = (await new GLTFLoader().loadAsync('../moteur/anatomie3d/' + a3d + '.glb')).scene;
  g.traverse(o => { if (o.isMesh) { o.geometry.computeVertexNormals(); o.material = new THREE.MeshPhysicalMaterial({ color: new THREE.Color(getComputedStyle(document.body).getPropertyValue('--acc').trim() || '#7c3aed').lerp(new THREE.Color('#d9a08a'), .55), roughness: .45, clearcoat: .4, side: THREE.DoubleSide }); } });
  if (corps && corps.parent) S.remove(corps); if (groupeOrgane) S.remove(groupeOrgane);
  groupeOrgane = g; S.add(g);
  const bb = new THREE.Box3().setFromObject(g), c = bb.getCenter(new THREE.Vector3()), t = bb.getSize(new THREE.Vector3());
  cible = [c.x, c.y, c.z]; dist = Math.max(t.x, t.z, 60) / (2 * Math.tan(CORPS.fov * Math.PI / 360)) * 2.6; decal = 0; poserCamera(); bornes(g);
}
const ancre = n => {
  if (n.ancreCentre && groupeOrgane) return proj(new THREE.Box3().setFromObject(groupeOrgane).getCenter(new THREE.Vector3()));
  const m = M[n.organe]; if (!m) return [(L + Rr) / 2, H / 2]; return proj(new THREE.Box3().setFromObject(m).getCenter(new THREE.Vector3()));
};

/* ======================================================================== taille de la scène et vue (déplacement, zoom) */
function mesurer() {
  const r = scene.getBoundingClientRect(); mobile = r.width < 700; W = Math.round(r.width); H = Math.round(r.height); G = W < 1500 ? 30 : 40;
  R.setSize(W, H, false); gl.style.width = W + 'px'; gl.style.height = H + 'px';
}
function appliquerVue() { const v = etat.vue; monde.style.transform = `translate(${v.tx}px,${v.ty}px) scale(${v.s})`; }
function zoomer(f, cx = W / 2, cy = H / 2) { const v = etat.vue; if (!f) { v.tx = 0; v.ty = 0; v.s = 1; } else { const s = Math.min(2.5, Math.max(.4, v.s * f)); v.tx = cx - (cx - v.tx) * s / v.s; v.ty = cy - (cy - v.ty) * s / v.s; v.s = s; } appliquerVue(); }
$$('#zoom button').forEach(b => b.onclick = () => zoomer(+b.dataset.z));
scene.addEventListener('wheel', e => { if (e.target.closest('#bulle,#fen,#fdet')) return; e.preventDefault();
  if (e.ctrlKey) { const r = scene.getBoundingClientRect(); zoomer(e.deltaY < 0 ? 1.1 : .91, e.clientX - r.left, e.clientY - r.top); } else { etat.vue.tx -= e.deltaX * .8; etat.vue.ty -= e.deltaY * .8; appliquerVue(); } }, { passive: false });
{ let drag = null; scene.addEventListener('pointerdown', e => { if (e.target.closest('.n,#zoom,#pastilles,button,a,input')) return; drag = [e.clientX, e.clientY, etat.vue.tx, etat.vue.ty]; scene.setPointerCapture(e.pointerId); });
  scene.addEventListener('pointermove', e => { if (!drag) return; etat.vue.tx = drag[2] + e.clientX - drag[0]; etat.vue.ty = drag[3] + e.clientY - drag[1]; appliquerVue(); });
  scene.addEventListener('pointerup', () => drag = null); scene.addEventListener('pointercancel', () => drag = null); }

/* ======================================================================== graphe : construction */
function construire(noeuds) {
  cases.innerHTML = ''; bulle.style.display = 'none'; etat.ouvert.clear(); etat.pile.length = 0; etat.vue = { tx: 0, ty: 0, s: 1 }; appliquerVue();
  const N = noeuds.map(n => ({ ...n, de: n.de || [], enf: [] })), byId = Object.fromEntries(N.map(n => [n.id, n]));
  N.forEach(n => n.de.forEach(p => byId[p] && byId[p].enf.push(n.id)));
  const prof = n => n._p ?? (n._p = n.de.length ? 1 + Math.max(...n.de.map(p => prof(byId[p]))) : 0); N.forEach(prof);
  for (const n of N) { if (mobile) n.cote = 'd'; else if (!n.cote) n.cote = (function c(m) { return m.cote || c(byId[m.de[0]]); })(n); }
  for (const n of N) {
    const el = document.createElement('div'); el.className = 'n cache ' + n.cote + (n.enf.length || n.cliches ? '' : ' feuille') + (n.de.length ? '' : ' racine') + (n.aRediger ? ' gris' : '');
    el.style.setProperty('--c', n.couleur || '#64748b'); el.tabIndex = -1;
    const ics = [];
    if (n.enf.length || n.cliches) ics.push('<span class=plus>+</span>');
    if (n.fiche && n.exRef) ics.push('<span data-a=fiche title="Ouvrir la fiche complète">📄</span>');
    if (n.fenetre) ics.push('<span data-a=trace title="Ouvrir le tracé calculé">📈</span>');
    if (n.cliches) ics.push('<span data-a=cliches title="Ouvrir la fenêtre à deux clichés">🖼</span>');
    if (n.clichesAProduire) ics.push('<span class=apx title="Les deux clichés de cette pathologie restent à produire">🖼</span>');
    if (n.outil) ics.push('<span data-a=outil title="Ouvrir le calculateur ou la grille">🧮</span>');
    if (n.a3d) ics.push('<span data-a=3d title="Tourner l\'organe en 3D">🧊</span>');
    ics.push('<span data-a=jouer class=jouer title="Jouer les défis de cette case" hidden>🎯</span>');
    el.innerHTML = (n.type ? '<b class=ty>' + esc(n.type) + '</b>' : '') + esc(n.texte) + '<span class=ics>' + ics.join('') + '</span>';
    el.style.setProperty('--ni', ics.length);
    cases.appendChild(el); n.el = el;
    if (n.cliches) n.fenEl = fenetreCliches(n);
    el.addEventListener('click', e => { const a = e.target.closest('[data-a]'); if (a) { e.stopPropagation(); action(n, a.dataset.a); return; } basculer(n); });
    el.addEventListener('mouseenter', () => montrer(n)); el.addEventListener('mouseleave', () => cacherBulle());
    el.addEventListener('focus', () => montrer(n)); el.addEventListener('blur', () => cacherBulle());
  }
  etat.N = N; etat.byId = byId;
  const prof2 = Math.max(0, ...N.map(n => n._p));
  etat.colMax = prof2;
  if (pratique) pratique.marquer();
}
function basculer(n) {
  if (!n.enf.length && !n.cliches) { if (n.outil) action(n, 'outil'); else if (n.fenetre) action(n, 'trace'); else if (n.flash) ouvrirFen(n.texte, n.couleur, ficheFlash(n)); return; }
  if (etat.ouvert.has(n.id)) replier(n.id);
  else { /* un circuit à la fois (plan § 2) : ouvrir une case replie ses sœurs ouvertes */
    const soeurs = n.de.length ? etat.byId[n.de[0]].enf : etat.N.filter(m => !m.de.length && m.cote === n.cote).map(m => m.id);
    for (const s of soeurs) if (s !== n.id && etat.ouvert.has(s)) replier(s);
    etat.ouvert.add(n.id); etat.pile.push(n.id); }
  dessiner(); if (etat.ouvert.has(n.id)) montrerSuite(n);
}
function montrerSuite(n) { /* la vue glisse pour montrer la suite qu'on vient d'ouvrir */
  const ks = n.enf.map(i => etat.byId[i]).filter(k => !k.el.classList.contains('cache')); if (!ks.length) return;
  const v = etat.vue, xs = ks.map(k => k.x + (k.cote === 'd' ? k.w / 2 : -k.w / 2)), ys = ks.flatMap(k => [k.y - k.h / 2, k.y + k.h / 2]);
  const droite = Math.max(...xs) * v.s + v.tx, gauche = Math.min(...xs) * v.s + v.tx, bas2 = Math.max(...ys) * v.s + v.ty, haut2 = Math.min(...ys) * v.s + v.ty;
  if (droite > W - 12) v.tx -= droite - W + 24; if (gauche < 12) v.tx += 24 - gauche;
  
  monde.style.transition = 'transform .35s'; appliquerVue(); setTimeout(() => monde.style.transition = '', 400);
}
function replier(id) { etat.ouvert.delete(id); for (const c of etat.byId[id].enf) replier(c); }
/* focus : quand une case ouverte a plus de 6 sœurs, les sœurs fermées s'effacent (un circuit à la fois, plan § 2) ; un nouveau clic sur la case ouverte les fait revenir */
const FOCUS = 2;
/* quand la fenêtre à deux clichés est ouverte, la chaîne qui y mène reste seule (pilote) : la fenêtre garde toute la place sous elle */
const fenOuverte = () => etat.N.some(n => n.cliches && etat.ouvert.has(n.id));
const focusDe = P => { if (!etat.ouvert.has(P.id) || P.enf.length <= 1 || (P.enf.length <= FOCUS && !fenOuverte())) return null; const o = P.enf.filter(i => etat.ouvert.has(i)); return o.length ? P.enf.filter(i => etat.ouvert.has(i) || ['Calcul', 'Critère'].includes(etat.byId[i].nature)) : null; };
{ let t = null; const rb = $('#repli');
  rb.onclick = () => { clearTimeout(t); t = setTimeout(() => { while (etat.pile.length) { const id = etat.pile.pop(); if (etat.ouvert.has(id)) { replier(id); break; } } dessiner(); }, 240); };
  rb.ondblclick = () => { clearTimeout(t); etat.ouvert.clear(); etat.pile.length = 0; dessiner(); }; }

/* ======================================================================== disposition symétrique (recalculée à chaque clic sur les cases visibles) */
const visible = n => !n.de.length || n.de.some(p => { if (!etat.ouvert.has(p) || !visible(etat.byId[p])) return false; const f = focusDe(etat.byId[p]); return !f || f.includes(n.id); });
let COL = 160;
function recadrer(dR, dLft) { /* le corps glisse vers le côté opposé au développement */
  const bodyW = Rr - L, cibleC = mobile ? 132 : 168, needR = (dR + 1) * (cibleC + G), needL = (dLft + 1) * (cibleC + G), dispo = W - 24 - bodyW;
  const minL = (dLft + 1) * ((mobile ? 112 : 116) + G);
  const gauche = needR + needL <= dispo ? 12 + needL + (dispo - needL - needR) / 2 : 12 + Math.min(needL, Math.max(minL, dispo * needL / Math.max(1, needL + needR)));
  const dpx = gauche + bodyW / 2 - (L + Rr) / 2; if (Math.abs(dpx) < 4) return;
  const p0 = proj(new THREE.Vector3(...cible)), p1 = proj(new THREE.Vector3(cible[0] + 100, cible[1], cible[2])), pxmm = (p1[0] - p0[0]) / 100;
  decal -= dpx / pxmm; poserCamera(); L += dpx; Rr += dpx; document.documentElement.style.setProperty('--cx', ((L + Rr) / 2 / W * 100) + '%');
}
function disposer() {
  const N = etat.N, vis = N.filter(visible), byId = etat.byId;
  for (const n of N) n.el.classList.toggle('cache', !vis.includes(n));
  const dR = Math.max(-1, ...vis.filter(n => n.cote === 'd').map(n => n._p)), dLft = Math.max(-1, ...vis.filter(n => n.cote === 'g').map(n => n._p));
  recadrer(dR, dLft);
  const fit = (place, d) => d < 0 ? 1e9 : (place - G * (d + 1)) / (d + 1);
  COL = Math.round(Math.max(mobile ? 112 : 116, Math.min(mobile ? 140 : 178, fit(W - 12 - Rr, dR), fit(L - 12, dLft))));
  cases.style.setProperty('--w', COL + 'px');
  for (const n of vis) { n.el.style.minHeight = ''; }
  for (const n of vis) { n.w = n.el.offsetWidth; n.h = n.el.offsetHeight; const pas = (COL + G) * n._p; n.x = n.cote === 'd' ? Rr + G + pas + COL / 2 : L - G - pas - COL / 2; }
  const grp = {}; vis.filter(n => n.de.length === 1).forEach(n => (grp[n.de[0]] ??= []).push(n));
  for (const f of Object.values(grp)) { const h = Math.max(...f.map(n => n.h)); f.forEach(n => { if (n.h < h) { n.el.style.minHeight = h + 'px'; n.h = h; } }); }
  const haut = mobile ? 112 : 88, bas = H - (mobile ? 50 : 14);
  const fils = n => etat.ouvert.has(n.id) ? n.enf.map(i => byId[i]).filter(c => c && visible(c)) : [];
  const gap = (a, b) => (fils(a).length || fils(b).length) ? GC : GF;
  const span = n => { const ks = fils(n); if (!ks.length) return n.h; let t = 0; ks.forEach((k, i) => t += span(k) + (i ? gap(ks[i - 1], k) : 0)); return Math.max(n.h, t); };
  const poser = (n, cy, acc) => { n.y = cy; acc.push(n); const ks = fils(n); if (!ks.length) return; let tot = 0; ks.forEach((k, i) => tot += span(k) + (i ? gap(ks[i - 1], k) : 0));
    let y = cy - tot / 2; ks.forEach((k, i) => { if (i) y += gap(ks[i - 1], k); poser(k, y + span(k) / 2, acc); y += span(k); }); };
  for (const cote of ['g', 'd']) { /* l'arbre ouvert garde sa place près de son organe ; les racines fermées se rangent autour, au plus près de leur organe */
    const rs = vis.filter(n => !n.de.length && n.cote === cote).map(r => (r.o = ancre(r), r)).sort((a, b) => a.o[1] - b.o[1]);
    const arbres = rs.map(r => { const a = []; poser(r, r.o[1], a); a.r = r; return a; });
    const haut_ = a => Math.min(...a.map(m => m.y - m.h / 2)), bas_ = a => Math.max(...a.map(m => m.y + m.h / 2)), dec = (a, d) => a.forEach(m => m.y += d);
    const grands = arbres.filter(a => a.length > 1), petits = arbres.filter(a => a.length === 1), pris = [], pris0 = [];
    const focus = [...etat.pile].reverse().find(id => etat.ouvert.has(id));
    for (const a of grands) { const t = haut_(a), b = bas_(a), f = a.find(m => m.id === focus);
      /* arbre plus haut que l'écran : la case ouverte en dernier vient au milieu, et la molette fait défiler le reste */
      dec(a, b - t > bas - haut ? (f ? Math.min(haut - t, Math.max(bas - b, (haut + bas) / 2 - f.y)) : haut - t) : t < haut ? haut - t : b > bas ? bas - b : 0);
      for (const [t0, b0] of pris) { const t1 = haut_(a), b1 = bas_(a); if (t1 < b0 + GC && b1 > t0 - GC) dec(a, b0 + GC - t1); } pris.push([haut_(a), bas_(a)]); for (const m of a) if (m._p === a.r._p) pris0.push([m.y - m.h / 2, m.y + m.h / 2]); }
    for (const a of petits) { const h = a[0].h, y0 = Math.min(Math.max(a[0].y, haut + h / 2), bas - h / 2); let best = null;
      const libre = y => pris0.every(([t0, b0]) => y + h / 2 + GF <= t0 || y - h / 2 - GF >= b0);
      for (let k = 0; k < 400 && best === null; k++) for (const y of [y0 + k * 6, y0 - k * 6]) if (best === null && y - h / 2 >= haut && libre(y)) best = y;
      if (best === null) best = Math.max(...pris0.map(p => p[1]), haut) + GF + h / 2;
      a[0].y = best; pris0.push([best - h / 2, best + h / 2]); }
  }
  /* fenêtre à deux clichés posée dans la toile sous la pathologie, comme le pilote : la chaîne remonte en bloc si la fenêtre déborde */
  for (const n of N) { if (!n.fenEl) continue; const on = etat.ouvert.has(n.id) && vis.includes(n); n.fenEl.hidden = !on; if (!on) continue;
    const ww = mobile ? W - 16 : Math.min(480, W - 24); n.fenEl.style.width = ww + 'px'; const wh = n.fenEl.offsetHeight;
    const racineDe = m => { while (m.de.length) m = byId[m.de[0]]; return m; }, rac = racineDe(n);
    const wx = mobile ? 8 : n.cote === 'd' ? Math.max(Rr + 8, Math.min(W - 12 - ww, n.x + n.w / 2 - ww)) : Math.min(L - 8 - ww, Math.max(12, n.x - n.w / 2));
    const arbre = vis.filter(m => m !== rac && racineDe(m) === rac), dessous = m => m.x + m.w / 2 > wx && m.x - m.w / 2 < wx + ww && m.y >= n.y - 1;
    const wyDe = () => Math.max(n.y + n.h / 2 + 26, ...arbre.filter(dessous).map(m => m.y + m.h / 2 + 18));
    const hautArbre = Math.min(...arbre.map(m => m.y - m.h / 2)), d = Math.max(haut - hautArbre, Math.min(0, bas - wyDe() - wh));
    if (d) arbre.forEach(m => m.y += d);
    n.fx = [wx, wyDe(), ww, wh]; n.fenEl.style.left = wx + 'px'; n.fenEl.style.top = n.fx[1] + 'px'; }
  let maxX = W, maxY = H;
  for (const n of N) if (n.fx && !n.fenEl.hidden) { maxX = Math.max(maxX, n.fx[0] + n.fx[2] + 16); maxY = Math.max(maxY, n.fx[1] + n.fx[3] + 16); }
  for (const n of vis) { n.el.style.left = (n.x - n.w / 2) + 'px'; n.el.style.top = n.y + 'px'; maxX = Math.max(maxX, n.x + n.w / 2 + 16); maxY = Math.max(maxY, n.y + n.h / 2 + 16); }
  ln.width = maxX; ln.height = maxY; ln.style.width = maxX + 'px'; ln.style.height = maxY + 'px';
  rendre();
  return vis;
}
/* ======================================================================== traits droits : départ horizontal depuis l'organe, puis bus en éventail */
function dessiner() {
  const vis = disposer(), x = ln.getContext('2d'), trait = getComputedStyle(document.documentElement).getPropertyValue('--trait').trim() || '#2c3644';
  x.clearRect(0, 0, ln.width, ln.height);
  for (const n of etat.N) n.el.classList.toggle('ouvert', etat.ouvert.has(n.id));
  const bord = (n, droite) => droite ? n.x + n.w / 2 : n.x - n.w / 2;
  const seg = (pts, col, w = 2) => { x.strokeStyle = col; x.lineWidth = w; x.lineJoin = 'round'; x.beginPath(); x.moveTo(...pts[0]); for (const p of pts.slice(1)) x.lineTo(...p); x.stroke(); };
  const pointe = (b, d, col) => { x.fillStyle = col; x.beginPath(); x.moveTo(...b); x.lineTo(b[0] - 9 * d, b[1] - 5); x.lineTo(b[0] - 9 * d, b[1] + 5); x.fill(); };
  const rond = (p, col, r = 3.2) => { x.fillStyle = col; x.beginPath(); x.arc(...p, r, 0, 7); x.fill(); };
  for (const n of vis) { if (n.de.length) continue; const col = n.couleur || trait, d = n.cote === 'd' ? 1 : -1, bc = d > 0 ? Rr : L, e = [bord(n, d < 0), n.y];
    seg([n.o, [bc, n.o[1]], e], col, 2.2); pointe(e, d, col); x.beginPath(); x.arc(...n.o, 5, 0, 7); x.fillStyle = col; x.fill(); x.strokeStyle = '#fff'; x.lineWidth = 1.5; x.stroke(); }
  for (const P of vis) {
    if (!etat.ouvert.has(P.id)) continue; const K = P.enf.map(i => etat.byId[i]).filter(k => vis.includes(k)); if (!K.length) continue;
    const d = K[0].cote === 'd' ? 1 : -1, col = P.couleur || trait, x0 = bord(P, d > 0), xb = x0 + d * G * .32, ys = K.map(k => k.y).concat([P.y]);
    seg([[x0, P.y], [xb, P.y]], col, 2.2); if (K.length > 1 || Math.abs(K[0].y - P.y) > 1) seg([[xb, Math.min(...ys)], [xb, Math.max(...ys)]], col, 2.2); rond([xb, P.y], col);
    for (const k of K) { const e = [bord(k, d < 0), k.y]; seg([[xb, k.y], e], col, 1.9); pointe(e, d, col); }
    const f = focusDe(P); if (f && P.enf.length > f.length) { const k = etat.byId[f.find(i => etat.ouvert.has(i))], reste = P.enf.length - f.length; /* sœurs effacées : leur nombre reste lisible sous la case ouverte */
      x.font = '11px ' + (getComputedStyle(document.body).fontFamily || 'sans-serif'); x.fillStyle = getComputedStyle(document.documentElement).getPropertyValue('--sous').trim() || '#3b4b5c';
      x.textAlign = d > 0 ? 'left' : 'right'; x.fillText('+ ' + reste + ' autre' + (reste > 1 ? 's' : '') + ' (re-clic)', bord(k, d < 0), k.y + k.h / 2 + 13); x.textAlign = 'left'; }
  }
  for (const n of vis) { if (!n.fx || n.fenEl.hidden) continue; const col = n.couleur || trait, [wx, wy, ww] = n.fx, xs = Math.min(Math.max(n.x, wx + 24), wx + ww - 24);
    seg([[xs, n.y + n.h / 2], [xs, wy]], col, 2.2); x.fillStyle = col; x.beginPath(); x.moveTo(xs, wy); x.lineTo(xs - 5, wy - 9); x.lineTo(xs + 5, wy - 9); x.fill(); }
}

/* ======================================================================== infobulle symétrique + glossaire */
let GRE = null;
function preparerGlossaire(G0) {
  etat.glo = G0; const ks = Object.keys(G0).filter(k => k.length >= 2).sort((a, b) => b.length - a.length);
  GRE = ks.length ? new RegExp('(^|[^\\wÀ-ÿ\\-])(' + ks.map(t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')(?![\\wÀ-ÿ])', 'g') : null;
}
const gloser = h => GRE ? String(h).split(/(<[^>]+>)/).map(p => p.startsWith('<') ? p : p.replace(GRE, (m, a, b) => a + '<span class=terme tabindex=0 data-def="' + esc(etat.glo[b]) + '">' + b + '</span>')).join('') : h;
const rubHtml = (RUB, B) => RUB.filter(([k]) => B[k] || B[k + '_h']).map(([k, l]) => '<dt>' + l + '</dt><dd' + (B[k] === 'à produire' ? ' class=apx' : '') + '>' + (B[k + '_h'] || esc(B[k])) + '</dd>').join('');
/* Fiche flash (gabarit de Vial, 26.11) : le clic sur une pathologie l'ouvre en fenêtre ; chaque syndrome et chaque moyen de traitement se survole. */
const ficheFlash = n => gloser('<dl class=flash>' + rubHtml(etat.rub[n.rubriques] || [], n.bulle) + '</dl>');
function montrer(n) {
  if (!n.bulle || n.el.classList.contains('cache')) return;
  const RUB = etat.rub[n.rubriques] || etat.rub.region || [['def', 'Ce que c\'est']], B = n.bulle;
  const lignes = rubHtml(RUB, B)
    + (B.traitement ? '<dt class=trt>Traitement</dt><dd>' + B.traitement.map(([m, p]) => '<b>' + esc(m) + '</b> : ' + esc(p)).join('<br>') + (B.source ? '<div class=src>Source : ' + esc(B.source) + '</div>' : '') + '</dd>' : '');
  const pied = [n.fiche && n.exRef ? '📄 ouvre la fiche complète' : '', n.fenetre ? '📈 ouvre le tracé calculé' : '', n.cliches ? 'un clic ouvre les deux clichés et la fiche flash' : n.clichesAProduire ? (n.flash ? 'un clic ouvre la fiche flash · ' : '') + 'les deux clichés restent à produire' : '', n.outil ? '🧮 ouvre le calculateur' : '', n.enf.length ? 'un clic révèle la suite' : ''].filter(Boolean).join(' · ');
  bulle.innerHTML = gloser('<h4>' + esc(n.texte) + '</h4><dl>' + lignes + '</dl>') + (pied ? '<div class=pied>' + pied + '.</div>' : '');
  bulle.style.setProperty('--c', n.couleur || 'var(--acc)'); bulle.style.display = 'block';
  const r = n.el.getBoundingClientRect(), bw = bulle.offsetWidth, bh = bulle.offsetHeight;
  /* comme le moteur reseau3d : l'infobulle se pose du côté du corps, pour ne pas couvrir la suite du circuit */
  let bx = n.cote === 'd' ? r.left - bw - 12 : r.right + 12; if (bx < 8) bx = r.right + 12; if (bx + bw > innerWidth - 8) bx = r.left - bw - 12; if (bx < 8) bx = Math.max(8, Math.min(innerWidth - bw - 8, r.left));
  let by = Math.min(Math.max(r.top + r.height / 2 - bh / 2, 8), innerHeight - bh - 8); if (mobile) by = r.bottom + 8 + bh > innerHeight ? Math.max(8, r.top - bh - 8) : r.bottom + 8;
  bulle.style.left = bx + 'px'; bulle.style.top = by + 'px';
}
let tb = null; function cacherBulle() { clearTimeout(tb); tb = setTimeout(() => { if (!bulle.matches(':hover')) bulle.style.display = 'none'; }, 120); }
bulle.addEventListener('mouseleave', cacherBulle);

/* ======================================================================== fenêtres : fiche (cours), clichés, calculateur, tracé, 3D */
const fen = $('#fen');
function ouvrirFen(titre, couleur, html) {
  const fd = document.getElementById('fdet'); if (fd) fd.remove();
  $('#fenTitre').textContent = titre; fen.style.setProperty('--c', couleur || 'var(--acc)'); $('#fenCorps').innerHTML = html; fen.hidden = false; fen.scrollTop = 0; return $('#fenCorps');
}
$('#fenFermer').onclick = () => fen.hidden = true;
{ let d = null; fen.querySelector('.fh').addEventListener('pointerdown', e => { if (e.target.closest('button')) return; const r = fen.getBoundingClientRect(); d = [e.clientX - r.left, e.clientY - r.top]; fen.setPointerCapture(e.pointerId); });
  fen.addEventListener('pointermove', e => { if (!d) return; fen.style.left = (e.clientX - d[0]) + 'px'; fen.style.top = Math.max(0, e.clientY - d[1]) + 'px'; fen.style.right = 'auto'; });
  fen.addEventListener('pointerup', () => d = null); }
const VIS = { diagnostique: 'diagnostique', etiologique: 'étiologique', therapeutique: 'thérapeutique', retentissement: 'retentissement', complications: 'suivi des complications', sortie: 'sortie' };
async function ficheExamen(stem, exId, couleur) {
  const o = await charger('donnees/organes/' + stem + '.json'), e = o.examens.find(x => x.id === exId); if (!e) return;
  const b = e.bulle || {}, L2 = (t, v) => v ? `<dt>${t}</dt><dd>${esc(v)}</dd>` : '';
  const liste = (xs, f) => xs && xs.length ? '<ul>' + xs.map(f).join('') + '</ul>' : '';
  let h = `<p><b>${esc(o.nom)}</b> · ${esc(e.modalite)}${e.visees ? ' · visées : ' + e.visees.map(v => VIS[v] || v).join(', ') : ''}</p>`;
  h += '<h3>Ce que c\'est et pourquoi ici</h3><dl class=grille>' + L2('Ce que c\'est', b.def) + L2('Pourquoi ici', b.pourquoi) + L2('Confusion possible', b.confusion) + L2('À retenir', b.retenir) + '</dl>';
  h += '<h3>Choisir l\'examen : facteur discriminant et avantage sélectif</h3><dl class=grille>' + L2('Indication', e.indication) + L2('Signe recherché', e.signeRecherche) + L2('Seuil', e.seuil) + L2('Pourquoi lui', e.discriminant) +
    L2('Avantage sélectif', e.avantageSelectif) + L2('Plutôt que', e.plutotQue) + L2('Limite', e.limite) + L2('Smarter Medicine', e.smarterMedicine) + L2('Précautions', e.precautions) +
    (e.irradiation_mSv != null ? `<dt>Irradiation</dt><dd>La fiche estime la dose efficace à ${String(e.irradiation_mSv).replace('.', ',')} mSv ; ce chiffre permet de comparer les examens entre eux et de préférer le moins irradiant à question égale.</dd>` : '') + L2('Délai', e.delai) + '</dl>';
  if (e.aspectNormal || e.radioAnatomieNormale) h += '<details open><summary>Aspect normal</summary><p>' + esc(e.aspectNormal || '') + '</p>' + liste(e.radioAnatomieNormale, x => '<li>' + esc(x) + '</li>') + '</details>';
  if (e.anomaliesElementaires) h += '<details><summary>Anomalies élémentaires (' + e.anomaliesElementaires.length + ')</summary>' + liste(e.anomaliesElementaires, a => `<li><b>${esc(a.anomalie)}</b> : ${esc(a.signification)}</li>`) + '</details>';
  if (e.syndromesParacliniques) h += '<details><summary>Syndromes paracliniques (' + e.syndromesParacliniques.length + ')</summary>' + liste(e.syndromesParacliniques, s => `<li><b>${esc(s.syndrome)}</b> : le syndrome réunit ${esc((s.anomaliesQuiLeComposent || []).join(', ').toLowerCase())}.</li>`) + '</details>';
  if (e.pathologiesAssociees) h += '<details><summary>Pathologies associées (' + e.pathologiesAssociees.length + ')</summary>' + liste(e.pathologiesAssociees, p => `<li><b>${esc(p.pathologie)}</b> : l'examen montre typiquement ${esc((p.anomalieTypique || '').toLowerCase())}.</li>`) + '</details>';
  const c = ouvrirFen(e.nom, couleur, gloser(h) + (o.a3d ? '<p><button class=btn id=voir3d>🧊 Tourner l\'organe en 3D</button></p>' : ''));
  const b3 = c.querySelector('#voir3d'); if (b3) b3.onclick = () => { fen.hidden = true; ouvrirFenetre('3d', o.nom, couleur, o.a3d); };
}
function fenetreCliches(n) {
  /* Fenêtre du pilote (conception/prototypes/paraclinique.png) : patient à gauche (lésions numérotées, bouton Annoté / Brut),
     radio-anatomie normale à droite (repères lettrés), puis la description énumérative des lésions et des repères. */
  const f = n.cliches, w = document.createElement('div'); w.className = 'fcli'; w.hidden = true; w.style.setProperty('--c', '#2a9d8f');
  w.innerHTML = `<div class=ft>${esc(f.titre)}</div><div class=duo>
    <figure><figcaption><span>Cliché du patient</span><button class=basc title="Afficher ou masquer les lésions numérotées">Annoté</button></figcaption><div class=cadre><img class=ipat alt="Radiographie thoracique de face du patient" src="${esc(f.img)}"><canvas class=cpat></canvas></div></figure>
    <figure><figcaption><span>Radio-anatomie normale</span></figcaption><div class=cadre><img class=inor alt="Radiographie thoracique de face normale" src="${esc(f.normal.img)}"><canvas class=cnor></canvas></div></figure></div>
    <div class=duo><ol class=les>${f.annotations.map(a => '<li>' + esc(a.texte) + '</li>').join('')}</ol><ul class=rep>${f.normal.reperes.map(a => '<li><b>' + esc(a.n) + '.</b> ' + esc(a.texte) + '</li>').join('')}</ul></div>
    ${n.flash ? '<details open><summary>Fiche flash</summary>' + ficheFlash(n) + '</details>' : ''}<details><summary>Diagnostic, conduite et source</summary><p>${esc(f.diagnostic)}</p><p>${esc(f.conduite)}</p><p class=mini>${esc(f.source || '')}</p></details>`;
  const des = (img, cv, rep) => { const go = () => { cv.width = img.clientWidth; cv.height = img.clientHeight; const q = cv.getContext('2d'), k = img.clientWidth / img.naturalWidth;
      for (const a of rep) { q.strokeStyle = a.couleur || '#2a9d8f'; q.lineWidth = 2; q.setLineDash(a.pointille ? [5, 4] : []); q.beginPath(); q.ellipse(a.x * k, a.y * k, a.rx * k, a.ry * k, 0, 0, 7); q.stroke(); q.setLineDash([]);
        const cx = a.x * k + a.rx * k * .75, cy = a.y * k - a.ry * k * .75; q.fillStyle = a.couleur || '#2a9d8f'; q.beginPath(); q.arc(cx, cy, 9, 0, 7); q.fill(); q.fillStyle = '#111'; q.font = '700 11px Atk'; q.textAlign = 'center'; q.fillText(a.n, cx, cy + 4); } };
    img.complete && img.naturalWidth ? go() : img.addEventListener('load', go); new ResizeObserver(() => img.naturalWidth && img.clientWidth && go()).observe(img); };
  const cp = w.querySelector('.cpat'); des(w.querySelector('.ipat'), cp, f.annotations); des(w.querySelector('.inor'), w.querySelector('.cnor'), f.normal.reperes);
  w.querySelector('.basc').onclick = e => { e.stopPropagation(); const v = cp.style.display === 'none'; cp.style.display = v ? 'block' : 'none'; e.target.textContent = v ? 'Annoté' : 'Brut'; };
  w.querySelectorAll('img').forEach(im => im.addEventListener('load', () => etat.N.length && dessiner()));
  w.addEventListener('pointerdown', e => e.stopPropagation()); w.querySelector('details').addEventListener('toggle', () => dessiner());
  cases.appendChild(w); return w;
}
function fenetreOutil(n) {
  const x = (etat.outils || {})[n.outil]; if (!x) return; const calc = CALCS[n.outil];
  if (calc) {
    const c = ouvrirFen(x.nom, '#0f766e', `<p><b>Formule.</b> ${esc(x.formule)}</p><p class=mini>${esc(x.variables || '')}</p><div class=calc>${calc.v.map(([k, l, u, d]) => `<label><span>${esc(l)}</span><input type=number step=any data-k="${k}" value="${d}"><span>${esc(u)}</span></label>`).join('')}</div>
      <p class=res id=res></p><p id=lect></p><h3>Interprétation</h3><p>${gloser(esc(x.interpretation || ''))}</p><p class=mini>Source : ${esc(x.source || '')}</p><p class=mini>Le calcul s'exécute dans la page ; ses tests unitaires (conception/outils/paraclinique/test_calculs.mjs) réussissent avant publication.</p>`);
    const maj = () => { const v = Object.fromEntries([...c.querySelectorAll('input')].map(i => [i.dataset.k, i.value])); const r = calculer(n.outil, v);
      c.querySelector('#res').textContent = isFinite(r.x) ? 'Résultat : ' + r.texte.replace('.', ',') : 'Tu complètes les valeurs pour obtenir le résultat.'; c.querySelector('#lect').textContent = isFinite(r.x) ? r.lecture : ''; };
    c.querySelectorAll('input').forEach(i => i.oninput = maj); maj(); return;
  }
  const c = ouvrirFen(x.nom, '#6d28d9', `<p>Tu coches chaque élément présent chez ton patient ; la règle de décision s'affiche en dessous.</p><div class=calc>${(x.elements || []).map((el, i) => `<label style="grid-template-columns:22px 1fr"><input type=checkbox data-i="${i}"><span>${esc(el)}</span></label>`).join('')}</div>
    <p class=res id=res></p><h3>Règle de décision</h3><p>${gloser(esc(x.regleDeDecision || ''))}</p><p class=mini>Source : ${esc(x.source || '')}</p>`);
  const maj = () => { const k = c.querySelectorAll('input:checked').length; let t = `Tu as coché ${k} élément${k > 1 ? 's' : ''} sur ${(x.elements || []).length}.`;
    if (n.outil === 'crit_light_exsudat_pleural') t += k >= 1 ? ' Au moins un critère est rempli : l\'épanchement est un exsudat (Light, 1972).' : ' Aucun critère n\'est rempli : l\'épanchement est un transsudat (Light, 1972).';
    if (n.outil === 'crit_kdigo_ira_definition') t += k >= 1 ? ' Un seul élément suffit : tu retiens une insuffisance rénale aiguë (KDIGO, 2012).' : '';
    c.querySelector('#res').textContent = t; };
  c.querySelectorAll('input').forEach(i => i.onchange = maj); maj();
}
function action(n, a) {
  bulle.style.display = 'none';
  if (a === 'fiche') ficheExamen(n.fiche, n.exRef, n.couleur);
  else if (a === 'trace') { fen.hidden = true; ouvrirFenetre(n.fenetre, n.texte, n.couleur, null); }
  else if (a === 'cliches') { if (!etat.ouvert.has(n.id)) basculer(n); }
  else if (a === 'outil') fenetreOutil(n);
  else if (a === '3d') { fen.hidden = true; ouvrirFenetre('3d', n.texte, n.couleur, n.a3d); }
  else if (a === 'jouer' && pratique) pratique.jouerCase(n);
}

/* ======================================================================== onglets, modes et thème */
async function ouvrirOnglet(o, garderVue) {
  etat.onglet = o; etat.organe = null; document.body.dataset.onglet = o; $('#pastilles').hidden = true;
  $$('.sommaire button').forEach(b => b.classList.toggle('actif', b.dataset.onglet === o));
  $('#titre').textContent = ONGLETS[o].titre; $('#chaine').textContent = ONGLETS[o].chaine; $('#etat').textContent = 'Le réseau de l\'onglet se charge…';
  const d = await charger('donnees/reseau_' + o + '.json'); etat.rub = d.rubriques; etat.outils = d.outils || etat.outils;
  await chargerCorps(); montrerCorps(); construire(d.noeuds); dessiner();
  $('#etat').textContent = `${d.noeuds.length} cases · le réseau se replie par défaut ; tu déplies un circuit à la fois.`;
  if (pratique && etat.mode === 'pratique') await pratique.ouvrirOnglet(o);
  history.replaceState(null, '', '#' + new URLSearchParams({ onglet: o, mode: etat.mode }).toString());
}
async function changerMode(m) {
  etat.mode = m; document.body.dataset.mode = m; $$('.modes button').forEach(b => b.setAttribute('aria-selected', b.dataset.mode === m));
  $('#aideMode').textContent = MODES[m]; $('#pratique').hidden = m !== 'pratique';
  mesurer(); if (etat.N.length) { if (etat.organe) await montrerCorpsOuOrgane(); else montrerCorps(); dessiner(); }
  if (m === 'pratique') await pratique.ouvrirOnglet(etat.organe ? 'organe' : etat.onglet); else pratique.fermer();
}
$$('.modes button').forEach(b => b.onclick = () => changerMode(b.dataset.mode));
$$('.sommaire button').forEach(b => b.onclick = () => { document.body.classList.remove('cote-ouvert'); ouvrirOnglet(b.dataset.onglet); });
let ti = Math.max(0, TH.findIndex(t => t[0] === (Q.get('theme') || 'blanc')));
const setTheme = () => { document.documentElement.dataset.theme = TH[ti][0]; $('#theme span').textContent = TH[ti][1]; if (etat.N.length) dessiner(); };
$('#theme').onclick = () => { ti = (ti + 1) % TH.length; setTheme(); };
$('#ouvrirCote').onclick = () => { const o = document.body.classList.toggle('cote-ouvert'); $('#ouvrirCote').setAttribute('aria-expanded', o); };

/* ======================================================================== recherche tolérante : mode Organe et mode Examen */
let IDX = null;
const tri = s => { const t = new Set(), x = '  ' + s + ' '; for (let i = 0; i < x.length - 2; i++) t.add(x.slice(i, i + 3)); return t; };
const lev = (a, b) => { if (Math.abs(a.length - b.length) > 3) return 9; const d = Array.from({ length: b.length + 1 }, (_, i) => i); for (let i = 1; i <= a.length; i++) { let p = d[0]; d[0] = i; for (let j = 1; j <= b.length; j++) { const t = d[j]; d[j] = Math.min(d[j] + 1, d[j - 1] + 1, p + (a[i - 1] === b[j - 1] ? 0 : 1)); p = t; } } return d[b.length]; };
function score(q, cle) {
  if (!cle) return 0; if (cle.startsWith(q)) return 3; if (cle.includes(q)) return 2.4;
  const mots = cle.split(/[^a-z0-9]+/).filter(Boolean), qs = q.split(/\s+/).filter(Boolean);
  let s = 0; for (const w of qs) { let best = 0; for (const m of mots) { if (m.startsWith(w)) best = Math.max(best, 1); else if (w.length > 3 && lev(w, m.slice(0, w.length + 1)) <= (w.length > 6 ? 2 : 1)) best = Math.max(best, .8); } s += best; }
  s = s / Math.max(1, qs.length) * 2;
  const A = tri(q), B = tri(cle); let c = 0; A.forEach(t => B.has(t) && c++); return Math.max(s, 2 * c / (A.size + B.size) * 1.6);
}
async function chercher(q) {
  IDX ??= await charger('donnees/recherche.json'); q = sansAccent(q).trim(); if (q.length < 2) return [];
  const r = [];
  for (const o of IDX.organes) { const s = Math.max(score(q, sansAccent(o.n)), score(q, sansAccent(o.s.replace(/_/g, ' ')))); if (s > .9) r.push({ s: s + .2, t: 'o', o }); }
  for (const e of IDX.examens) { const s = Math.max(score(q, sansAccent(e.n)), ...e.s.map(x => score(q, x) * .95)); if (s > .9) r.push({ s, t: 'e', e }); }
  return r.sort((a, b) => b.s - a.s).slice(0, 9);
}
{ const inp = $('#q'), ul = $('#propositions'); let res = [], sel = -1;
  const afficher = () => { ul.hidden = !res.length; ul.innerHTML = res.map((r, i) => `<li role=option aria-selected=${i === sel} data-i=${i}>${r.t === 'o' ? '<b>' + esc(r.o.n) + '</b><small>Mode Organe · ' + esc(r.o.r) + ' · ' + r.o.k + ' examens</small>' : esc(r.e.n) + '<small>Mode Examen · ' + esc(r.e.m) + ' · ' + r.e.o.length + ' organe' + (r.e.o.length > 1 ? 's' : '') + '</small>'}</li>`).join(''); };
  inp.oninput = async () => { res = await chercher(inp.value); sel = res.length ? 0 : -1; afficher(); };
  inp.onkeydown = e => { if (e.key === 'ArrowDown') { sel = Math.min(res.length - 1, sel + 1); afficher(); e.preventDefault(); } else if (e.key === 'ArrowUp') { sel = Math.max(0, sel - 1); afficher(); e.preventDefault(); } else if (e.key === 'Enter' && res[sel]) choisir(res[sel]); else if (e.key === 'Escape') ul.hidden = true; };
  ul.onclick = e => { const li = e.target.closest('li'); if (li) choisir(res[+li.dataset.i]); };
  const choisir = r => { ul.hidden = true; inp.value = r.t === 'o' ? r.o.n : r.e.n; document.body.classList.remove('cote-ouvert'); if (r.t === 'o') modeOrgane(r.o.s); else modeExamen(r.e, 0); };
  window.__chercher = chercher; window.__choisir = choisir; }

/* mode Organe : l'organe seul au centre, puis modalités → examens → contenu (anomalies élémentaires, syndromes, pathologies) */
const MODC = { 'Imagerie': '#1d4ed8', 'Biologie': '#b91c1c', 'Exploration fonctionnelle': '#15803d', 'Endoscopie': '#475569', 'Anatomopathologie / biopsie': '#a16207' };
function bulleEx(e) { const b = e.bulle || {}; return Object.fromEntries(Object.entries({ def: b.def || ('L\'examen « ' + e.nom + ' » attend encore sa fiche rédigée.'), pourquoi: b.pourquoi, confusion: b.confusion, retenir: b.retenir, signe: e.signeRecherche, seuil: e.seuil, discriminant: e.discriminant, avantage: e.avantageSelectif, plutot: e.plutotQue, limite: e.limite, smarter: e.smarterMedicine }).filter(([, v]) => v)); }
function contenuExamen(N, eid, e) {
  const grp = (k, nom, items, f) => { if (!items || !items.length) return; const gid = eid + '_' + k; N.push({ id: gid, nature: 'Groupe', type: 'Contenu', texte: nom, de: [eid], couleur: '#475569', rubriques: 'region', bulle: { def: `Ce groupe réunit ${items.length} élément${items.length > 1 ? 's' : ''} de la fiche de l'examen.` } });
    items.forEach((it, i) => N.push(Object.assign({ id: gid + '_' + i, de: [gid] }, f(it)))); };
  grp('an', 'Anomalies élémentaires', e.anomaliesElementaires, a => ({ nature: 'Anomalie', type: 'Anomalie élémentaire', texte: court(a.anomalie), couleur: '#c2410c', rubriques: 'region', bulle: { def: a.anomalie + '.', pourquoi: a.signification } }));
  grp('sy', 'Syndromes paracliniques', e.syndromesParacliniques, s => ({ nature: 'Syndrome', type: 'Syndrome paraclinique', texte: court(s.syndrome), couleur: '#7c3aed', rubriques: 'region', bulle: { def: `Le syndrome « ${s.syndrome} » réunit : ${(s.anomaliesQuiLeComposent || []).join(', ').toLowerCase()}.`, retenir: 'Un seul signe ne suffit jamais : le syndrome se pose sur deux ou trois anomalies concordantes.' } }));
  grp('pa', 'Pathologies associées', e.pathologiesAssociees, p => ({ nature: 'Pathologie', type: 'Pathologie', texte: court(p.pathologie), couleur: '#9f1239', rubriques: 'patho', bulle: { def: `La pathologie « ${p.pathologie} » se recherche par cet examen.`, signe: p.anomalieTypique ? 'L\'examen montre typiquement : ' + p.anomalieTypique.charAt(0).toLowerCase() + p.anomalieTypique.slice(1) + '.' : '' } }));
}
const court = (t, n = 46) => { t = String(t || '').replace(/\s*\(.*?\)/g, '').trim(); return t.length <= n ? t : t.slice(0, n - 1).replace(/\s+\S*$/, '') + '…'; };
let organeCourant = null;
async function montrerCorpsOuOrgane() { const o = organeCourant; if (!o) return; if (o.a3d) { try { await montrerOrgane3D(o.a3d); return; } catch (e) { /* modèle absent : corps voilé */ } } await chargerCorps(); montrerCorps(o.mesh); }
async function preparerOrgane(stem) {
  const o = await charger('donnees/organes/' + stem + '.json'); organeCourant = o; etat.organe = stem; etat.onglet = 'organe'; document.body.dataset.onglet = 'organe';
  $$('.sommaire button').forEach(b => b.classList.remove('actif')); await montrerCorpsOuOrgane();
  if (!Object.keys(etat.rub).length) etat.rub = (await charger('donnees/reseau_imagerie.json')).rubriques;
  return o;
}
async function modeOrgane(stem) {
  const o = await preparerOrgane(stem), rid = 'org_' + stem, N = [{ id: rid, nature: 'Organe', type: o.region, texte: o.nom, de: [], couleur: o.couleur, ancreCentre: true, organe: o.mesh, cote: 'd', rubriques: 'region', a3d: o.a3d,
    bulle: { def: `L'organe « ${o.nom} » s'explore par ${o.examens.length} examens répartis en ${new Set(o.examens.map(e => e.modalite)).size} modalités.`, retenir: 'Tu déplies l\'organe nœud après nœud : modalités, examens, puis contenu (anomalies élémentaires, syndromes paracliniques, pathologies associées).' } }];
  for (const m of Object.keys(MODC)) { const L0 = o.examens.filter(e => e.modalite === m); if (!L0.length) continue; const mid = rid + '_' + m.slice(0, 3);
    N.push({ id: mid, nature: 'Modalité', type: 'Modalité', texte: m, de: [rid], couleur: MODC[m], rubriques: 'region', bulle: { def: `${L0.length} examen${L0.length > 1 ? 's' : ''} de cette modalité explorent l'organe.`, retenir: 'Tu choisis la modalité selon la question clinique, puis l\'examen le plus discriminant et le plus économe.' } });
    L0.forEach((e, i) => { const eid = mid + '_' + i; N.push({ id: eid, nature: 'Examen', type: 'Examen', texte: court(e.nom), de: [mid], couleur: MODC[m], rubriques: 'examen', bulle: bulleEx(e), fiche: stem, exRef: e.id }); contenuExamen(N, eid, e); }); }
  $('#titre').textContent = 'Mode Organe : ' + o.nom; $('#chaine').textContent = 'Organe → modalité → examen → anomalies élémentaires, syndromes paracliniques, pathologies associées';
  $('#pastilles').hidden = true; construire(N); etat.ouvert.add(rid); dessiner(); $('#etat').textContent = o.a3d ? 'Le modèle 3D réel de l\'organe occupe le centre ; 🧊 le fait tourner.' : 'Aucun modèle isolé n\'existe pour cet organe : le corps voilé le situe.';
  if (etat.mode === 'pratique') pratique.ouvrirOnglet('organe');
  history.replaceState(null, '', '#' + new URLSearchParams({ organe: stem, mode: etat.mode }).toString());
}
async function modeExamen(ex, k) {
  const [stem, exId] = ex.o[k], o = await preparerOrgane(stem), e = o.examens.find(x => x.id === exId), rid = 'org_' + stem, eid = rid + '_ex';
  const N = [{ id: rid, nature: 'Organe', type: o.region, texte: o.nom, de: [], couleur: o.couleur, ancreCentre: true, organe: o.mesh, cote: 'd', rubriques: 'region', a3d: o.a3d, bulle: { def: `L'examen choisi explore l'organe « ${o.nom} ».` } },
    { id: eid, nature: 'Examen', type: e.modalite, texte: court(e.nom), de: [rid], couleur: MODC[e.modalite] || o.couleur, rubriques: 'examen', bulle: bulleEx(e), fiche: stem, exRef: e.id }];
  contenuExamen(N, eid, e);
  $('#titre').textContent = 'Mode Examen : ' + e.nom; $('#chaine').textContent = 'L\'organe au centre, une seule ligne vers l\'examen ; même contenu que le mode Organe, par un accès court-circuité.';
  const pa = $('#pastilles'); pa.hidden = ex.o.length < 2;
  if (ex.o.length > 1) { const noms = await Promise.all(ex.o.map(([s]) => charger('donnees/organes/' + s + '.json').then(x => x.nom)));
    pa.innerHTML = '<span class=mini style="align-self:center">Cet examen explore aussi :</span>' + noms.map((nm, i) => `<button data-i=${i} class="${i === k ? 'actif' : ''}">${esc(nm)}</button>`).join('');
    pa.querySelectorAll('button').forEach(b => b.onclick = () => modeExamen(ex, +b.dataset.i)); }
  construire(N); etat.ouvert.add(rid); etat.ouvert.add(eid); etat.pile.push(rid, eid); dessiner(); montrerSuite(etat.byId[eid]); $('#etat').textContent = 'Tu déplies le contenu de l\'examen ; 📄 ouvre sa fiche complète.';
  if (etat.mode === 'pratique') pratique.ouvrirOnglet('organe');
}

/* ======================================================================== démarrage */
const pratique = new Pratique({ etat, charger, dessiner, gloser, esc, allerOnglet: o => ouvrirOnglet(o) });
addEventListener('resize', () => { const m = mobile; mesurer(); if (!etat.N.length) return; if (m !== mobile) { if (etat.organe) modeOrgane(etat.organe); else ouvrirOnglet(etat.onglet); return; }
  if (etat.organe) montrerCorpsOuOrgane().then(dessiner); else { montrerCorps(); dessiner(); } });
(async () => {
  try {
    mesurer(); setTheme();
    preparerGlossaire(await charger('donnees/glossaire.json'));
    const o = Q.get('onglet') || 'imagerie';
    if (Q.get('organe')) await modeOrgane(Q.get('organe')); else await ouvrirOnglet(ONGLETS[o] ? o : 'imagerie');
    if (Q.get('mode') === 'pratique') await changerMode('pratique');
    if (Q.get('ouvrir')) { Q.get('ouvrir').split(',').forEach(i => etat.byId[i] && etat.ouvert.add(i)); dessiner(); }
    document.title = 'Paraclinique — choisir, lire et interpréter l\'examen'; window.__pret = true;
  } catch (e) { $('#etat').textContent = 'Le chargement a échoué : ' + e.message; console.error(e); }
})();
const ouvrirChemin = ids => { for (const i of ids) if (etat.byId[i]) { etat.ouvert.add(i); etat.pile.push(i); } dessiner(); const l = etat.byId[ids[ids.length - 1]]; if (l) montrerSuite(l); };
window.__jeu = { etat, ouvrirChemin, ouvrirOnglet, modeOrgane, modeExamen, changerMode, action, dessiner, montrer };
