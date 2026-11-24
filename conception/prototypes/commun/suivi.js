/* Suivi de préparation commun aux 4 jeux (Tétrade, Paraclinique, Transversal, 45 Spec).
 * Enregistre chaque réponse jouée dans localStorage, calcule les points faibles (taux lissé, oubli selon Leitner,
 * tendance), propose un plan de 7 jours, projette la courbe jusqu'à la date d'examen, dessine les courbes en canvas,
 * exporte JSON + CSV + PNG et copie un résumé Markdown compact pour Claude.
 * Règle : le module ne connaît que les questions déjà jouées ; il n'affiche jamais le contenu d'un QCM non joué.
 * Signature : AAI (Anthropic AI) */
(function () {
  'use strict';
  const CLE = 'suivi_examen_v1', MAX = 20000, JOUR = 864e5;
  const INTERVALLES = [0, 1, 3, 7, 14]; // jours d'attente par boîte de Leitner (0 à 4)
  const esc = t => String(t ?? '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const jour = d => new Date(d).toISOString().slice(0, 10);
  const pct = x => Math.round(x * 100);
  let POIDS = {}; // poids relatif par spécialité, fourni par le jeu (défaut 1)

  function lire() {
    try { const d = JSON.parse(localStorage.getItem(CLE) || 'null'); if (d && Array.isArray(d.r)) return d; } catch (e) { }
    return { v: 1, r: [], noms: {} };
  }
  function ecrire(d) {
    try { localStorage.setItem(CLE, JSON.stringify(d)); return true; }
    catch (e) { try { d.r = d.r.slice(-Math.floor(d.r.length / 2)); localStorage.setItem(CLE, JSON.stringify(d)); } catch (e2) { } return false; }
  }

  /* r = {jeu, specialite, ssp, notion, format, juste, points, max, temps, qid, serie} */
  function enregistrer(r) {
    try {
      const d = lire();
      d.r.push({
        d: new Date().toISOString(), jeu: String(r.jeu || '?'), sp: String(r.specialite || '—'), ssp: String(r.ssp || '—'),
        n: String(r.notion || '—'), f: String(r.format || '?'), ok: !!r.juste, pts: +r.points || (r.juste ? 1 : 0), max: +r.max || 1,
        t: Math.max(0, Math.round(+r.temps || 0)), q: String(r.qid || ''), s: r.serie ? String(r.serie) : undefined
      });
      if (d.r.length > MAX) d.r = d.r.slice(-MAX);
      ecrire(d); majBouton();
    } catch (e) { /* le jeu continue même si le stockage échoue */ }
  }
  /* Révèle le vrai nom d'une notion masquée (ex. diagnostic d'une série de l'arène 45), seulement après sa révélation en jeu. */
  function nommer(cle, libelle) { try { const d = lire(); d.noms[cle] = String(libelle); ecrire(d); } catch (e) { } }
  const nomNotion = (d, x) => (x.s && d.noms[x.s]) ? d.noms[x.s] + ' · ' + x.n : x.n;

  /* ---------- date d'examen (veille) ---------- */
  function dateExamen() {
    const V = window.VEILLE; const auj = jour(Date.now());
    if (V && V.faits) {
      for (const an of [V.session_courante, V.session_suivante]) {
        const f = V.faits.find(x => x.id === 'qcm_' + an);
        if (f && Array.isArray(f.valeur) && f.valeur[0] >= auj) return { iso: f.valeur[0], officiel: true, an };
        if (f && f.attendu_iso && f.attendu_iso >= auj) return { iso: f.attendu_iso, officiel: false, an };
      }
    }
    const an = new Date().getUTCFullYear() + (new Date().getUTCMonth() > 7 ? 1 : 0);
    return { iso: an + '-08-03', officiel: false, an };
  }

  /* ---------- analyse ---------- */
  function analyser() {
    const d = lire(), R = d.r, now = Date.now(), auj = jour(now);
    const agreg = cle => {
      const m = {};
      for (const x of R) { const k = cle(x); const a = m[k] = m[k] || { cle: k, n: 0, ok: 0, pts: 0, max: 0, t: 0, der: 0, sp: x.sp, jeu: x.jeu, recents: [] };
        a.n++; a.ok += x.ok; a.pts += x.pts; a.max += x.max; a.t += x.t; a.der = Math.max(a.der, Date.parse(x.d)); a.recents.push(x.ok); }
      return Object.values(m).map(a => ({ ...a, taux: a.ok / a.n, lisse: (a.ok + 1) / (a.n + 2), tmoy: a.t / a.n, recents: a.recents.slice(-5) }));
    };
    // Leitner : la boîte de chaque question se recalcule depuis l'historique (juste : +1, faux : 0)
    const boites = {};
    for (const x of R) { const k = x.q || (x.jeu + '|' + x.n); const b = boites[k] = boites[k] || { b: 0, der: 0, n: x.n, sp: x.sp, s: x.s, jeu: x.jeu };
      b.b = x.ok ? Math.min(4, b.b + 1) : 0; b.der = Date.parse(x.d); }
    const dues = [];
    for (const [k, b] of Object.entries(boites)) {
      const echeance = b.der + INTERVALLES[b.b] * JOUR, retard = (now - echeance) / JOUR;
      b.echeance = echeance; b.oubli = Math.max(0, Math.min(1, retard / Math.max(1, INTERVALLES[b.b] || 1)));
      if (echeance <= now + 6 * JOUR) dues.push({ k, ...b });
    }
    const oubliNotion = {};
    for (const b of Object.values(boites)) { const k = b.n; oubliNotion[k] = Math.max(oubliNotion[k] || 0, b.oubli); }
    const parSp = agreg(x => x.sp), parSsp = agreg(x => x.ssp).filter(a => a.cle !== '—'), parNotion = agreg(x => x.n);
    const poids = sp => POIDS[sp] ?? 1;
    // score de faiblesse : (1 − taux lissé) × poids d'examen × (1 + oubli) × (1 + 0,3 si les 3 dernières réponses contiennent une erreur)
    for (const a of parNotion) {
      const erreurRecente = a.recents.slice(-3).includes(false) ? 0.3 : 0;
      a.oubli = oubliNotion[a.cle] || 0; a.poids = poids(a.sp);
      a.faiblesse = (1 - a.lisse) * a.poids * (1 + a.oubli) * (1 + erreurRecente);
      a.libelle = nomNotion(d, R.findLast ? R.findLast(x => x.n === a.cle) : R.filter(x => x.n === a.cle).pop());
    }
    for (const a of parSp) { a.poids = poids(a.cle); a.faiblesse = (1 - a.lisse) * a.poids; }
    // série quotidienne
    const parJour = {};
    for (const x of R) { const j = jour(x.d); const p = parJour[j] = parJour[j] || { j, n: 0, ok: 0 }; p.n++; p.ok += x.ok; }
    const serie = Object.values(parJour).sort((a, b) => a.j < b.j ? -1 : 1).map(p => ({ ...p, taux: p.ok / p.n }));
    serie.forEach((p, i) => { const f = serie.slice(Math.max(0, i - 6), i + 1); p.mm7 = f.reduce((s, q) => s + q.ok, 0) / f.reduce((s, q) => s + q.n, 0); });
    // tendance : 7 derniers jours contre les 7 précédents
    const fen = (a, b) => R.filter(x => { const t = (now - Date.parse(x.d)) / JOUR; return t >= a && t < b; });
    const t7 = fen(0, 7), t14 = fen(7, 14), taux = L => L.length ? L.filter(x => x.ok).length / L.length : null;
    const tendance = { recent: taux(t7), avant: taux(t14), n7: t7.length, n14: t14.length };
    tendance.delta = tendance.recent != null && tendance.avant != null ? tendance.recent - tendance.avant : null;
    // projection : régression linéaire pondérée par le volume sur les 30 derniers jours
    const ex = dateExamen(), jrest = Math.max(0, Math.ceil((Date.parse(ex.iso) - now) / JOUR));
    const pts = serie.filter(p => (now - Date.parse(p.j)) / JOUR <= 30);
    let projection = null;
    if (pts.length >= 3) {
      const X = pts.map(p => Date.parse(p.j) / JOUR), W = pts.map(p => p.n), Y = pts.map(p => p.taux), sw = W.reduce((a, b) => a + b, 0);
      const mx = X.reduce((s, x, i) => s + x * W[i], 0) / sw, my = Y.reduce((s, y, i) => s + y * W[i], 0) / sw;
      let num = 0, den = 0; X.forEach((x, i) => { num += W[i] * (x - mx) * (Y[i] - my); den += W[i] * (x - mx) ** 2; });
      // projection prudente : la pente des 30 derniers jours s'applique au plus sur 30 jours, puis le niveau se stabilise
      const pente = den ? num / den : 0, dernier = serie[serie.length - 1].mm7, horizon = Math.min(jrest, 30);
      const brute = dernier + pente * horizon;
      projection = { pente_par_semaine: pente * 7, taux_examen: Math.max(0, Math.min(1, brute)), plafonnee: brute > 1 || brute < 0, horizon_jours: horizon };
    }
    const rythme = t7.length / 7;
    const faibles = parNotion.filter(a => a.ok < a.n || a.oubli > 0).sort((a, b) => b.faiblesse - a.faiblesse).slice(0, 10);
    // plan de 7 jours : chaque jour reçoit les révisions Leitner qui tombent ce jour-là et 3 cibles faibles, en rotation
    const cibles = parNotion.filter(a => a.lisse < 0.85 || a.oubli > 0).sort((a, b) => b.faiblesse - a.faiblesse);
    const spFaibles = parSp.slice().sort((a, b) => b.faiblesse - a.faiblesse);
    const plan = [];
    for (let k = 0; k < 7; k++) {
      const debut = new Date(auj).getTime() + k * JOUR, fin = debut + JOUR;
      const aRevoir = Object.values(boites).filter(b => (k === 0 ? b.echeance < fin : b.echeance >= debut && b.echeance < fin)).length;
      const c = cibles.length ? [0, 1, 2].map(j => cibles[(k * 3 + j) % cibles.length]).filter((v, i, t) => t.indexOf(v) === i) : [];
      const sp = spFaibles.length ? spFaibles[k % Math.min(3, spFaibles.length)] : null;
      plan.push({ jour: jour(debut), revisions: aRevoir, cibles: c.map(x => x.libelle), specialite: sp ? sp.cle : null,
        questions: Math.max(10, Math.round(aRevoir + 5 * c.length + (sp ? 10 * sp.poids : 0))) });
    }
    const tot = { n: R.length, ok: R.filter(x => x.ok).length, pts: R.reduce((s, x) => s + x.pts, 0), max: R.reduce((s, x) => s + x.max, 0),
      t: R.length ? R.reduce((s, x) => s + x.t, 0) / R.length : 0, jours: serie.length };
    const parFormat = agreg(x => x.f), parJeu = agreg(x => x.jeu);
    return { tot, parSp, parSsp, parNotion, parFormat, parJeu, serie, tendance, faibles, plan, dues: dues.length, examen: ex, jrest, projection, rythme };
  }

  /* ---------- courbes (canvas) ---------- */
  const C = { ink: '#1d2230', sous: '#5b6275', trait: '#c7d3df', serie: '#2f6fd0', pale: '#9dbcec', ok: '#1f8a4c', ko: '#c0392b', fond: '#ffffff' };
  function prepCanvas(cv, h) {
    const r = window.devicePixelRatio || 1, pe = cv.parentElement, cs = pe ? getComputedStyle(pe) : null;
    const w = pe ? Math.max(280, (pe.clientWidth || 640) - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight)) : 640;
    cv.width = w * r; cv.height = h * r; cv.style.width = w + 'px'; cv.style.height = h + 'px';
    const g = cv.getContext('2d'); g.setTransform(r, 0, 0, r, 0, 0); g.fillStyle = C.fond; g.fillRect(0, 0, w, h);
    g.font = '12px "Atkinson Hyperlegible", A, sans-serif'; return { g, w, h };
  }
  function courbe(cv, A, bulle) {
    const { g, w, h } = prepCanvas(cv, 240), m = { l: 40, r: 14, t: 14, b: 28 }, S = A.serie;
    if (!S.length) { g.fillStyle = C.sous; g.fillText('Joue quelques questions : la courbe apparaîtra ici.', m.l, h / 2); cv._pts = []; return; }
    const t0 = Date.parse(S[0].j), tex = Date.parse(A.examen.iso), tl = Date.parse(S[S.length - 1].j), t1 = Math.max(t0 + 6 * JOUR, A.projection ? Math.min(tex, tl + 30 * JOUR) : tl), tp = Math.min(tex, t1);
    const X = t => m.l + (t - t0) / (t1 - t0) * (w - m.l - m.r), Y = v => m.t + (1 - v) * (h - m.t - m.b);
    g.strokeStyle = C.trait; g.lineWidth = 1; g.fillStyle = C.sous;
    for (const v of [0, .25, .5, .75, 1]) { g.beginPath(); g.moveTo(m.l, Y(v)); g.lineTo(w - m.r, Y(v)); g.stroke(); g.fillText(pct(v) + ' %', 4, Y(v) + 4); }
    g.fillText(S[0].j.slice(5).split('-').reverse().join('.'), m.l, h - 8);
    const fin = new Date(t1).toISOString().slice(5, 10).split('-').reverse().join('.'); g.fillText(fin, w - m.r - g.measureText(fin).width, h - 8);
    // points quotidiens (pâles) puis moyenne mobile 7 jours (trait)
    cv._pts = [];
    for (const p of S) { const x = X(Date.parse(p.j)), y = Y(p.taux); g.fillStyle = C.pale; g.beginPath(); g.arc(x, y, 4, 0, 7); g.fill();
      cv._pts.push({ x, y, txt: `${p.j.split('-').reverse().join('.')} : ${pct(p.taux)} % juste sur ${p.n} question(s) · moyenne 7 jours ${pct(p.mm7)} %` }); }
    g.strokeStyle = C.serie; g.lineWidth = 2; g.lineJoin = 'round'; g.beginPath();
    S.forEach((p, i) => { const x = X(Date.parse(p.j)), y = Y(p.mm7); i ? g.lineTo(x, y) : g.moveTo(x, y); }); g.stroke();
    if (A.projection) {
      const l = S[S.length - 1]; g.setLineDash([5, 5]); g.beginPath(); g.moveTo(X(tl), Y(l.mm7)); g.lineTo(X(tp), Y(A.projection.taux_examen)); g.stroke(); g.setLineDash([]);
      if (tex <= t1) { g.strokeStyle = C.ko; g.beginPath(); g.moveTo(X(tex), m.t); g.lineTo(X(tex), h - m.b); g.stroke(); }
      g.fillStyle = C.ink; const lab = `${tex <= t1 ? 'examen' : 'puis stable jusqu\u2019à l\u2019examen (J\u2212' + A.jrest + ')'} : ${pct(A.projection.taux_examen)} %`;
      const ly = A.projection.taux_examen > .5 ? h - m.b - 10 : m.t + 14;
      g.fillText(lab, Math.max(m.l, X(tp) - g.measureText(lab).width - 4), ly);
      cv._pts.push({ x: X(tp), y: Y(A.projection.taux_examen), txt: `Projection linéaire au ${A.examen.iso.split('-').reverse().join('.')} : ${pct(A.projection.taux_examen)} % (indicatif)` });
    }
    branchBulle(cv, bulle);
  }
  function barres(cv, A, bulle) {
    const L = A.parSp.slice().sort((a, b) => a.taux - b.taux).slice(0, 12), hb = 22, { g, w, h } = prepCanvas(cv, Math.max(80, 20 + L.length * (hb + 6)));
    const l = 150, r = 50; cv._pts = [];
    if (!L.length) { g.fillStyle = C.sous; g.fillText('Aucune spécialité jouée pour l\'instant.', 10, 40); return; }
    L.forEach((a, i) => {
      const y = 10 + i * (hb + 6), lw = (w - l - r) * a.taux;
      g.fillStyle = C.ink; const nom = a.cle.length > 22 ? a.cle.slice(0, 21) + '…' : a.cle; g.fillText(nom, 6, y + 15);
      g.fillStyle = '#eef3f8'; g.fillRect(l, y, w - l - r, hb);
      g.fillStyle = C.serie; if (lw > 0) { g.beginPath(); (g.roundRect ? g.roundRect(l, y, Math.max(lw, 4), hb, [0, 4, 4, 0]) : g.rect(l, y, lw, hb)); g.fill(); }
      g.fillStyle = C.ink; g.fillText(pct(a.taux) + ' %', w - r + 6, y + 15);
      cv._pts.push({ x: l + lw, y: y + hb / 2, rect: [0, y, w, hb], txt: `${a.cle} : ${a.ok}/${a.n} juste(s), ${pct(a.taux)} % · temps moyen ${Math.round(a.tmoy)} s` });
    });
    branchBulle(cv, bulle);
  }
  function branchBulle(cv, bulle) {
    if (!bulle || cv._bb) return; cv._bb = 1;
    cv.addEventListener('mousemove', e => {
      const b = cv.getBoundingClientRect(), x = e.clientX - b.left, y = e.clientY - b.top; let best = null, dmin = 30;
      for (const p of cv._pts || []) { const d = p.rect ? (y >= p.rect[1] && y <= p.rect[1] + p.rect[3] ? 0 : 99) : Math.hypot(p.x - x, p.y - y); if (d < dmin) { dmin = d; best = p; } }
      if (!best) { bulle.style.display = 'none'; return; }
      bulle.textContent = best.txt; bulle.style.display = 'block'; bulle.style.left = (e.clientX + 12) + 'px'; bulle.style.top = (e.clientY + 12) + 'px';
    });
    cv.addEventListener('mouseleave', () => { bulle.style.display = 'none'; });
  }

  /* ---------- résumé Markdown pour Claude ---------- */
  function resume(A) {
    A = A || analyser(); const T = A.tot, f = x => x == null ? '—' : pct(x) + ' %';
    const L = [];
    L.push(`# Ma préparation à l'examen fédéral — résumé du ${new Date().toLocaleDateString('fr-CH')}`);
    L.push(`Examen : ${A.examen.iso.split('-').reverse().join('.')} (${A.examen.officiel ? 'date officielle' : 'date estimée, non publiée'}) · J−${A.jrest}`);
    L.push('', '## Scores');
    L.push(`- Global : ${T.ok}/${T.n} juste (${f(T.n ? T.ok / T.n : null)}), points ${T.pts.toFixed(1)}/${T.max}, temps moyen ${Math.round(T.t)} s, ${T.jours} jour(s) d'entraînement`);
    L.push(`- 7 derniers jours : ${f(A.tendance.recent)} sur ${A.tendance.n7} q. ; 7 jours d'avant : ${f(A.tendance.avant)} sur ${A.tendance.n14} q.${A.tendance.delta != null ? ` (tendance ${A.tendance.delta >= 0 ? '+' : ''}${pct(A.tendance.delta)} points)` : ''}`);
    L.push(`- Par jeu : ${A.parJeu.map(a => `${a.cle} ${f(a.taux)} (${a.n})`).join(' ; ') || '—'}`);
    L.push(`- Par format : ${A.parFormat.map(a => `${a.cle} ${f(a.taux)} (${a.n})`).join(' ; ') || '—'}`);
    L.push(`- Par spécialité (les plus faibles) : ${A.parSp.slice().sort((a, b) => a.taux - b.taux).slice(0, 6).map(a => `${a.cle} ${f(a.taux)} (${a.n})`).join(' ; ') || '—'}`);
    if (A.projection) L.push(`- Projection linéaire au jour de l'examen : ${f(A.projection.taux_examen)} (pente ${(A.projection.pente_par_semaine * 100).toFixed(1)} points/semaine, indicatif)`);
    L.push('', '## 10 points faibles');
    A.faibles.forEach((a, i) => L.push(`${i + 1}. ${a.libelle} — ${a.sp} — ${a.ok}/${a.n} juste${a.oubli > 0 ? ', révision en retard' : ''}`));
    if (!A.faibles.length) L.push('- Aucun pour l\'instant.');
    L.push('', '## Plan des 7 prochains jours');
    A.plan.forEach(p => L.push(`- ${p.jour.split('-').reverse().join('.')} : ${p.questions} q. dont ${p.revisions} révision(s) Leitner${p.specialite ? ` ; bloc ${p.specialite}` : ''}${p.cibles.length ? ` ; cibles : ${p.cibles.join(' / ')}` : ''}`));
    L.push('', '## Questions à poser à Claude');
    const q = A.faibles.slice(0, 5).map(a => `- Explique-moi « ${a.libelle} » (${a.sp}) de la coque vers le centre : mécanisme, discriminant, décision et piège typique de l'examen fédéral, puis pose-moi 3 questions Kprim.`);
    if (A.parSp.length) { const s = A.parSp.slice().sort((a, b) => a.taux - b.taux)[0]; q.push(`- Quelles situations de départ PROFILES (SSP) de ${s.cle} dois-je prioriser avec ${f(s.taux)} de réussite ?`); }
    q.push(`- Mon rythme est de ${A.rythme.toFixed(1)} question(s) par jour à J−${A.jrest} : ce plan est-il réaliste, et que changerais-tu ?`);
    L.push(...q, '', '_Généré par le suivi de préparation de Jeux_45_Spec. AAI (Anthropic AI)_');
    return L.join('\n');
  }

  /* ---------- exports ---------- */
  function telecharger(nom, contenu, type) {
    const b = contenu instanceof Blob ? contenu : new Blob([contenu], { type }), a = document.createElement('a');
    a.href = URL.createObjectURL(b); a.download = nom; document.body.appendChild(a); a.click();
    setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
  }
  function csv() {
    const d = lire(), q = v => /[";\n]/.test(String(v)) ? '"' + String(v).replace(/"/g, '""') + '"' : String(v ?? '');
    const t = ['date;jeu;specialite;ssp;notion;format;juste;points;max;temps_s;question'];
    for (const x of d.r) t.push([x.d, x.jeu, x.sp, x.ssp, nomNotion(d, x), x.f, x.ok ? 1 : 0, x.pts, x.max, x.t, x.q].map(q).join(';'));
    return '﻿' + t.join('\n');
  }
  function png(racine) {
    const cvs = [...(racine || document).querySelectorAll('canvas[data-suivi]')];
    if (!cvs.length) return null;
    const r = window.devicePixelRatio || 1, W = Math.max(...cvs.map(c => c.width)), H = cvs.reduce((s, c) => s + c.height + 40 * r, 0);
    const o = document.createElement('canvas'); o.width = W; o.height = H; const g = o.getContext('2d'); g.fillStyle = '#fff'; g.fillRect(0, 0, W, H);
    let y = 0; g.fillStyle = C.ink; g.font = `${14 * r}px sans-serif`;
    for (const c of cvs) { g.fillText(c.getAttribute('aria-label') || '', 8 * r, y + 24 * r); y += 36 * r; g.drawImage(c, 0, y); y += c.height + 4 * r; }
    return o;
  }
  function exporter(racine) {
    const A = analyser(), d = lire(), stamp = jour(Date.now());
    const { parNotion, ...court } = A;
    telecharger(`preparation_${stamp}.json`, JSON.stringify({ genere_le: new Date().toISOString(), reponses: d.r, noms: d.noms, analyse: { ...court, parNotion } }, null, 1), 'application/json');
    telecharger(`preparation_${stamp}.csv`, csv(), 'text/csv;charset=utf-8');
    const o = png(racine);
    if (o) o.toBlob(b => b && telecharger(`preparation_courbes_${stamp}.png`, b, 'image/png'), 'image/png');
    return { json: true, csv: true, png: !!o };
  }
  async function copier(texte) {
    try { await navigator.clipboard.writeText(texte); return true; } catch (e) { }
    try { const t = document.createElement('textarea'); t.value = texte; t.style.position = 'fixed'; t.style.opacity = '0'; document.body.appendChild(t); t.select();
      const ok = document.execCommand('copy'); t.remove(); return ok; } catch (e) { return false; }
  }

  /* ---------- tableau de bord ---------- */
  const CSS = `.sv{font:14px/1.55 "Atkinson Hyperlegible",A,sans-serif;color:#1d2230}.sv h3{font:700 17px Georgia,serif;margin:22px 0 8px}
.sv .kpi{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:8px 0 4px}.sv .kpi div{background:#fff;border:1px solid #c7d3df;border-radius:8px;padding:8px 10px}
.sv .kpi b{display:block;font-size:20px}.sv .kpi span{color:#5b6275;font-size:12.5px}.sv .cadre{background:#fff;border:1px solid #c7d3df;border-radius:8px;padding:8px}
.sv table{border-collapse:collapse;width:100%;font-size:13px;background:#fff}.sv th,.sv td{border-bottom:1px solid #e1e8ef;padding:5px 7px;text-align:left;vertical-align:top}.sv th{color:#5b6275;font-weight:700}
.sv .act{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}.sv button{font:700 13.5px "Atkinson Hyperlegible",A,sans-serif;border:0;border-radius:6px;padding:8px 14px;background:#2f6fd0;color:#fff;cursor:pointer}
.sv button.sec{background:#fff;color:#2f6fd0;border:1px solid #2f6fd0}.sv button:focus-visible{outline:3px solid #f0b429;outline-offset:2px}.sv .note{color:#5b6275;font-size:12.5px}
.sv textarea{width:100%;min-height:160px;font:12.5px/1.4 ui-monospace,monospace;border:1px solid #c7d3df;border-radius:6px;padding:8px}.sv [data-i]{border-bottom:1px dotted #5b6275;cursor:help}
#svBulle{position:fixed;z-index:10001;display:none;max-width:300px;background:#1d2230;color:#fff;font:13px/1.45 "Atkinson Hyperlegible",A,sans-serif;padding:7px 10px;border-radius:6px;pointer-events:none}
#svVoile{position:fixed;inset:0;z-index:10000;background:rgba(29,34,48,.45);display:none;overflow:auto}#svVoile .boite{max-width:860px;margin:30px auto;background:#e3f2fd;border-radius:10px;padding:18px 24px 26px}
#svBtn{position:fixed;right:16px;bottom:16px;z-index:9999;font:700 13.5px "Atkinson Hyperlegible",A,sans-serif;border:0;border-radius:20px;padding:9px 16px;background:#2f6fd0;color:#fff;box-shadow:0 2px 8px rgba(0,0,0,.2);cursor:pointer}`;
  function style() { if (document.getElementById('svStyle')) return; const s = document.createElement('style'); s.id = 'svStyle'; s.textContent = CSS; document.head.appendChild(s);
    const b = document.createElement('div'); b.id = 'svBulle'; b.setAttribute('role', 'tooltip'); document.body.appendChild(b);
    document.addEventListener('mouseover', e => { const h = e.target.closest && e.target.closest('.sv [data-i]'); if (!h) return; const r = h.getBoundingClientRect(); b.textContent = h.dataset.i; b.style.display = 'block'; b.style.left = Math.min(r.left, innerWidth - 320) + 'px'; b.style.top = (r.bottom + 6) + 'px'; });
    document.addEventListener('mouseout', e => { if (e.target.closest && e.target.closest('.sv [data-i]')) b.style.display = 'none'; }); }

  function monter(el) {
    style(); const A = analyser(), T = A.tot, f = x => x == null ? '—' : pct(x) + ' %', bulle = document.getElementById('svBulle');
    const ex = A.examen.iso.split('-').reverse().join('.');
    el.classList.add('sv');
    el.innerHTML = `
<div class="kpi">
 <div><b>${T.n}</b><span>questions jouées</span></div>
 <div><b>${f(T.n ? T.ok / T.n : null)}</b><span>réponses justes</span></div>
 <div><b>${f(A.tendance.recent)}</b><span data-i="Le taux des 7 derniers jours se compare aux 7 jours précédents (${f(A.tendance.avant)}).">7 derniers jours ${A.tendance.delta == null ? '' : (A.tendance.delta >= 0 ? '▲' : '▼') + ' ' + Math.abs(pct(A.tendance.delta)) + ' pt'}</span></div>
 <div><b>${A.dues}</b><span data-i="Une question revient après 0, 1, 3, 7 puis 14 jours selon sa boîte de Leitner ; une erreur la renvoie en boîte 0.">révisions dues sous 7 jours</span></div>
 <div><b>J−${A.jrest}</b><span data-i="${A.examen.officiel ? 'La date vient du Tableau des délais officiel (veille OFSP).' : 'Le tableau officiel n’est pas publié : la date est déduite (début août, comme chaque année).'}">QCM le ${ex}${A.examen.officiel ? '' : ' (estimé)'}</span></div>
</div>
<h3>Évolution de la réussite</h3>
<div class="cadre"><canvas data-suivi aria-label="Réussite quotidienne et moyenne mobile sur 7 jours, avec projection jusqu'à l'examen" role="img"></canvas></div>
<p class="note">Les points montrent chaque jour ; le trait suit la moyenne sur 7 jours ; le pointillé prolonge la tendance des 30 derniers jours sur 30 jours au plus, puis la suppose stable jusqu'à l'examen. ${A.projection ? `La projection atteint ${f(A.projection.taux_examen)}${A.projection.plafonnee ? ' (valeur bornée entre 0 et 100 %)' : ''} : elle reste indicative, car l'OFSP fixe le seuil de réussite après l'examen (méthodes Angoff et Hofstee).` : 'La projection demande au moins 3 jours d’entraînement.'}</p>
<h3>Réussite par spécialité</h3>
<div class="cadre"><canvas data-suivi aria-label="Taux de réussite par spécialité (les plus faibles en haut)" role="img"></canvas></div>
<h3>Les 10 points faibles</h3>
<p class="note" data-i="Le score multiplie l'échec lissé (1 − (justes + 1) / (réponses + 2)) par le poids de la spécialité, par (1 + retard de révision) et par 1,3 si une des 3 dernières réponses est fausse.">Le classement combine l'échec, le poids de la spécialité, l'oubli selon Leitner et les erreurs récentes.</p>
${A.faibles.length ? `<table><thead><tr><th>#</th><th>Notion jouée</th><th>Spécialité</th><th>Justes</th><th>Oubli</th></tr></thead><tbody>${A.faibles.map((a, i) => `<tr><td>${i + 1}</td><td>${esc(a.libelle)}</td><td>${esc(a.sp)}</td><td>${a.ok}/${a.n}</td><td>${a.oubli > 0 ? 'révision en retard' : '—'}</td></tr>`).join('')}</tbody></table>` : '<p class="note">Aucun point faible pour l’instant : joue une première série.</p>'}
${A.parSsp.length ? `<h3>Situations de départ (SSP)</h3><table><thead><tr><th>SSP</th><th>Justes</th><th>Taux</th></tr></thead><tbody>${A.parSsp.sort((a, b) => a.taux - b.taux).slice(0, 10).map(a => `<tr><td>${esc(a.cle)}</td><td>${a.ok}/${a.n}</td><td>${f(a.taux)}</td></tr>`).join('')}</tbody></table>` : ''}
<h3>Plan des 7 prochains jours</h3>
<table><thead><tr><th>Jour</th><th>Questions</th><th data-i="Les révisions Leitner sont les questions déjà jouées dont l'échéance tombe ce jour-là.">Révisions</th><th>Bloc</th><th>Cibles</th></tr></thead><tbody>
${A.plan.map(p => `<tr><td>${new Date(p.jour).toLocaleDateString('fr-CH', { weekday: 'short', day: '2-digit', month: '2-digit' })}</td><td>${p.questions}</td><td>${p.revisions}</td><td>${esc(p.specialite || '—')}</td><td>${esc(p.cibles.join(' · ') || '—')}</td></tr>`).join('')}</tbody></table>
<div class="act"><button data-a="exp">Exporter (JSON, CSV, PNG)</button><button data-a="cop" class="sec">Copier le résumé pour Claude</button><button data-a="raz" class="sec">Effacer mon historique</button></div>
<p class="note" data-r></p><textarea data-md readonly hidden aria-label="Résumé Markdown pour Claude"></textarea>`;
    const cv = el.querySelectorAll('canvas[data-suivi]'); courbe(cv[0], A, bulle); barres(cv[1], A, bulle);
    el.querySelector('[data-a="exp"]').onclick = () => { const r = exporter(el); el.querySelector('[data-r]').textContent = `Trois fichiers sont téléchargés : JSON, CSV${r.png ? ' et PNG des courbes' : ''}.`; };
    el.querySelector('[data-a="cop"]').onclick = async () => { const t = resume(A), ta = el.querySelector('[data-md]'); ta.value = t; ta.hidden = false;
      el.querySelector('[data-r]').textContent = (await copier(t)) ? 'Le résumé est copié : colle-le dans Claude.' : 'La copie automatique échoue : sélectionne le texte ci-dessous et copie-le.'; };
    el.querySelector('[data-a="raz"]').onclick = () => { if (confirm('Effacer tout l’historique de préparation de ce navigateur ?')) { try { localStorage.removeItem(CLE); } catch (e) { } monter(el); } };
    return A;
  }
  function ouvrir() {
    style(); let v = document.getElementById('svVoile');
    if (!v) { v = document.createElement('div'); v.id = 'svVoile'; v.setAttribute('role', 'dialog'); v.setAttribute('aria-modal', 'true');
      v.innerHTML = '<div class="boite"><div style="display:flex;justify-content:space-between;align-items:center"><h2 style="font:700 20px Georgia,serif;margin:0">Ma préparation</h2><button id="svFermer" style="font:700 13px sans-serif;border:1px solid #2f6fd0;background:#fff;color:#2f6fd0;border-radius:6px;padding:6px 12px;cursor:pointer">Fermer</button></div><div id="svCorps"></div></div>';
      document.body.appendChild(v); v.addEventListener('click', e => { if (e.target === v || e.target.id === 'svFermer') v.style.display = 'none'; });
      document.addEventListener('keydown', e => { if (e.key === 'Escape') v.style.display = 'none'; }); }
    v.style.display = 'block'; monter(document.getElementById('svCorps'));
  }
  function majBouton() { const b = document.getElementById('svBtn'); if (b) b.textContent = `Ma préparation (${lire().r.length})`; }
  function bouton() {
    if (document.getElementById('svBtn')) return; style();
    const b = document.createElement('button'); b.id = 'svBtn'; b.type = 'button'; b.onclick = ouvrir; document.body.appendChild(b); majBouton();
  }

  window.Suivi = { enregistrer, nommer, analyser, resume, exporter, csv, monter, ouvrir, bouton, dateExamen, copier,
    definirPoids: p => { POIDS = Object.assign({}, POIDS, p || {}); }, _cle: CLE };
  if (document.currentScript && document.currentScript.dataset.bouton !== 'non') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', bouton); else bouton();
  }
})();
