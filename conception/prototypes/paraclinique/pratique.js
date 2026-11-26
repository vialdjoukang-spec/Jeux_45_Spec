// Onglet PRATIQUE du jeu Paraclinique (plan § 9, § 16, § 18, § 19) : « la pratique est le jeu ».
// Cinq jeux dans la page : Arène « le bon examen », Aventure par type d'examen, Lecture d'image et de tracé, Cas cliniques, Examen blanc.
// Les défis viennent des fichiers jumeaux conception/donnees/pratique/paraclinique (recopiés par construire_jeu_paraclinique.py) : rien n'est inventé ici.
// Règles du plan : erreur dangereuse = coût triple ; échelle de correction après chaque erreur ; revanche immédiate sur la même notion (points doublés) ;
// révisions du jour avant les nouveautés (boîtes de Leitner, en attendant FSRS) ; session de 12 minutes ; une série manquée ne retire aucun point. Signature : AAI (Anthropic AI)
const LS = 'paraclinique_progres_v1';
const AVANT = ['casClinique', 'situation', 'contexte', 'resultat', 'descriptionDuTrace', 'consigne', 'imageOuTraceAttendu', 'valeurAvecUnite', 'question'];
const APRES = [['reponse', 'Réponse'], ['decision', 'Décision'], ['aspectRecherche', 'Aspect recherché'], ['piege', 'Piège'], ['erreurFrequente', 'Erreur fréquente'],
  ['consequence', 'Conséquence'], ['bonneConduite', 'Bonne conduite'], ['justification', 'Justification']];
const QUESTION = { bon_examen: 'Quel examen choisis-tu ?', seuil_decision: 'Quelle décision prends-tu devant ce résultat ?', preanalytique: 'Quel piège guette ce prélèvement, et quelle conduite le déjoue ?', piege: 'Quel piège guette ici, et quelle conduite le déjoue ?',
  erreur_de_prelevement: 'Quelle erreur de prélèvement repères-tu, et comment la corriges-tu ?', lecture: 'Que lis-tu, et que conclus-tu ?' };
const ECHELLE = [['zeroD', '0-D : ce qui se passe'], ['mecanisme', 'Mécanisme'], ['semiologie', 'Sémiologie'], ['discriminant', 'Discriminant'], ['decision', 'Décision'], ['piege', 'Piège'], ['ancre', 'Ancre']];
const JOUR = 864e5, INTERVALLES = [0, 0, 1, 3, 7, 16, 30];
const melanger = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const norm = s => String(s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().trim();

export class Pratique {
  constructor(api) {
    Object.assign(this, api); this.el = document.querySelector('#pratique');
    try { this.p = JSON.parse(localStorage.getItem(LS)) || {}; } catch (e) { this.p = {}; }
    this.p.boites ??= {}; this.p.refs ??= {}; this.p.points ??= 0; this.p.reussites ??= 0; this.p.erreurs ??= 0;
    this.serie = 0; this.debut = Date.now(); this.file = []; this.ent = []; this.cas = []; this.actif = false;
  }
  sauver() { try { localStorage.setItem(LS, JSON.stringify(this.p)); } catch (e) { } }
  async ouvrirOnglet(o) {
    this.actif = true; this.onglet = o; this.file = [];
    if (o === 'organe') {
      const refs = new Set(this.etat.N.map(n => n.exRef).filter(Boolean)); this.ent = []; this.cas = [];
      for (const t of ['imagerie', 'biologie', 'explorations']) { const d = await this.charger('donnees/pratique_' + t + '.json'); this.ent.push(...d.entites.filter(e => refs.has(e.ref))); }
    } else { const d = await this.charger('donnees/pratique_' + o + '.json'); this.ent = d.entites; this.cas = d.cas || []; }
    this.defis = this.ent.flatMap(e => e.defis.map(d => Object.assign({ _ref: e.ref, _nom: e.nom }, d)));
    this.accueil(); this.marquer();
  }
  fermer() { this.actif = false; clearInterval(this.tic); for (const n of this.etat.N) { n.el.classList.remove('ok', 'ko'); const j = n.el.querySelector('.jouer'); if (j) j.hidden = true; } }
  /* les cases se colorent au fil des réussites (Aventure, plan § 18) */
  marquer() {
    if (!this.actif) return; const avec = new Set((this.ent || []).map(e => e.ref));
    for (const n of this.etat.N) {
      const r = n.exRef || n.explo, a = this.refsSous(n), j = n.el.querySelector('.jouer');
      if (j) j.hidden = !a.some(x => avec.has(x));
      const st = r ? this.p.refs[r] || (n.explo && this.p.refs[n.explo]) : null; n.el.classList.toggle('ok', st === 'ok'); n.el.classList.toggle('ko', st === 'ko');
    }
  }
  refsSous(n) { const out = [], vu = new Set(); const f = m => { if (vu.has(m.id)) return; vu.add(m.id); if (m.exRef) out.push(m.exRef); if (m.explo) out.push(m.explo); m.enf.forEach(i => f(this.etat.byId[i])); }; f(n); return out; }
  dus() { const t = Date.now(); return this.defis.filter(d => { const b = this.p.boites[d.id]; return b && b.due <= t; }); }
  /* ---------------------------------------------------------------- accueil du panneau */
  accueil() {
    clearInterval(this.tic); const nb = this.defis.length, dus = this.dus().length, esc = this.esc;
    const titre = { imagerie: 'Imagerie', biologie: 'Biologie', explorations: 'Explorations fonctionnelles', organe: 'Organe choisi' }[this.onglet];
    const jeux = [['arene', 'Arène « le bon examen »', 'Tu affrontes 8 duels chronométrés : choisir, indiquer ou décider.'],
      ['aventure', 'Aventure par type d\'examen', 'Tu traverses un groupe du réseau ; chaque réussite colore sa case ; un défi d\'expert clôt le voyage.'],
      ['lecture', 'Lecture d\'image et de tracé', 'Tu lis un cliché réel ou un tracé décrit, tu appliques le seuil, puis tu conclus.']];
    if (this.cas.length) jeux.push(['cas', 'Cas cliniques : le bon bilan', `Tu coches seulement les examens nécessaires (${this.cas.length} cas du thorax, corrigés sur sept échelons).`]);
    jeux.push(['blanc', 'Examen blanc', '12 questions à choix unique en bloc chronométré ; les corrections n\'apparaissent qu\'à la fin.']);
    this.el.innerHTML = `<h2>Pratique : ${esc(titre)}</h2><p class=mini>La théorie remplit l'arbre ; la pratique remplit le jeu, qui s'appuie sur elle (${nb} défis dans cet onglet).</p>
      <div class=tableau><div><b>${this.p.points}</b><small>points</small></div><div><b>${this.serie}</b><small>série</small></div><div><b>${this.p.reussites}</b><small>réussites</small></div><div><b>${dus}</b><small>révisions dues</small></div></div>
      <div class=jeux>${jeux.map(([k, t, s], i) => `<button data-j=${k}><span class=num>${i + 1}</span><span><b>${t}</b><small>${s}</small></span></button>`).join('')}</div>
      <p class=mini>🎯 sur une case du réseau lance aussitôt ses défis.</p>
      <p class=garde>Garde-fous : la session dure 12 minutes par défaut ; une série manquée ne retire aucun point ; les révisions du jour passent avant les nouveautés.</p>`;
    this.el.querySelectorAll('[data-j]').forEach(b => b.onclick = () => this[b.dataset.j]());
  }
  /* ---------------------------------------------------------------- les cinq jeux */
  tirer(pool, n) { const t = Date.now(), dus = melanger(pool.filter(d => (this.p.boites[d.id] || {}).due <= t)), neufs = melanger(pool.filter(d => !this.p.boites[d.id])), reste = melanger(pool.filter(d => this.p.boites[d.id] && this.p.boites[d.id].due > t));
    return dus.concat(neufs, reste).slice(0, n); }
  lancer(liste, nom, opts = {}) { this.file = liste.map(d => ({ d })); this.nomJeu = nom; this.opts = opts; this.res = []; this.debutJeu = Date.now(); if (!this.file.length) { this.vide(); return; } this.suivant(); }
  vide() { this.el.innerHTML = `<h2>${this.esc(this.nomJeu || 'Pratique')}</h2><p>Cet onglet n'offre encore aucun défi de ce type : tu choisis un autre jeu ou un autre onglet.</p><div class=actions><button data-r>Revenir aux jeux</button></div>`; this.el.querySelector('[data-r]').onclick = () => this.accueil(); }
  arene() { this.lancer(this.tirer(this.defis.filter(d => ['bon_examen', 'indication', 'seuil_decision'].includes(d.type)), 8), 'Arène « le bon examen »', { chrono: true }); }
  lecture() {
    const l = this.tirer(this.defis.filter(d => ['lecture', 'lire_le_trace'].includes(d.type)), 7);
    const cli = this.etat.N.find(n => n.cliches); if (cli) l.unshift({ type: 'cliche', id: 'cliche_' + cli.id, _n: cli, niveau: 1, points: 20, tempsSec: 60 });
    this.lancer(l, 'Lecture d\'image et de tracé', { chrono: true });
  }
  aventure() {
    const racines = this.etat.N.filter(n => !n.de.length).flatMap(r => this.onglet === 'organe' ? r.enf.map(i => this.etat.byId[i]) : [r]);
    const esc = this.esc, groupes = racines.map(r => ({ r, refs: new Set(this.refsSous(r)) })).map(g => ({ ...g, d: this.defis.filter(d => g.refs.has(d._ref)) })).filter(g => g.d.length);
    this.el.innerHTML = `<h2>Aventure par type d'examen</h2><p>Tu choisis un groupe du réseau : le voyage va du défi simple au piège d'expert, et chaque réussite colore la case de l'examen.</p>
      <div class=groupes>${groupes.map((g, i) => `<button data-i=${i}>${esc(g.r.texte)} (${g.d.length})</button>`).join('')}</div><div class=actions><button class=sec data-r>Revenir aux jeux</button></div>`;
    this.el.querySelector('[data-r]').onclick = () => this.accueil();
    this.el.querySelectorAll('[data-i]').forEach(b => b.onclick = () => { const g = groupes[+b.dataset.i], l = this.tirer(g.d, 9).sort((a, b) => (a.niveau || 1) - (b.niveau || 1));
      if (l.length > 1) l[l.length - 1] = Object.assign({}, l[l.length - 1], { _boss: true });
      if (!this.etat.ouvert.has(g.r.id)) { this.etat.ouvert.add(g.r.id); this.dessiner(); } this.lancer(l, 'Aventure : ' + g.r.texte, { chrono: false }); });
  }
  cas() { this.lancer(melanger(this.cas).slice(0, 5).map(c => ({ type: 'cas', id: c.id, _cas: c, niveau: 2, points: 30, tempsSec: 120 })), 'Cas cliniques : le bon bilan', { chrono: false }); }
  blanc() {
    const qcm = this.defis.filter(d => d.type === 'bon_examen' && d.options && d.bonneReponse), l = melanger(qcm).slice(0, this.cas.length ? 10 : 12);
    if (this.cas.length) l.push(...melanger(this.cas).slice(0, 2).map(c => ({ type: 'cas', id: c.id, _cas: c, points: 30 })));
    this.lancer(melanger(l), 'Examen blanc', { blanc: true, total: l.length * 75 });
  }
  jouerCase(n) { const refs = new Set(this.refsSous(n)), l = this.defis.filter(d => refs.has(d._ref)); this.lancer(this.tirer(l, 8), 'Défis de « ' + n.texte + ' »', { chrono: true }); }
  /* ---------------------------------------------------------------- un défi */
  suivant() {
    clearInterval(this.tic);
    if (!this.file.length) { this.bilan(); return; }
    const { d, revanche } = this.file.shift(), esc = this.esc, gl = this.gloser; this.cour = { d, revanche, debut: Date.now(), rep: null };
    const temps = this.opts.blanc ? null : Math.min(90, Math.max(60, d.tempsSec || 60));
    const meta = `<div class=meta><span>${esc(this.nomJeu)} · ${d._boss ? 'défi final · ' : ''}niveau ${d.niveau || 1} · ${(d.points || 10) * (revanche ? 2 : 1)} points${revanche ? ' (revanche : points doublés)' : ''}</span><span class=chrono></span></div>`;
    let corps = '';
    if (d.type === 'cas') { const c = d._cas; corps = `<p><b>${esc(c.titre)}</b></p><p>${gl(esc(c.stem))}</p><p><b>${esc(c.prompt)}</b></p><div class=opts>${c.options.map((o, i) => `<button data-i=${i} aria-pressed=false>${esc(o.text)}</button>`).join('')}</div><div class=actions><button data-v>Valider</button></div>`; }
    else if (d.type === 'cliche') { const f = d._n.cliches; corps = `<p>Tu cliques la lésion principale (l'opacité alvéolaire) sur le cliché brut du patient.</p><div style="position:relative"><img id=cl src="${esc(f.img)}" alt="Radiographie thoracique du patient" style="width:100%;border-radius:6px;cursor:crosshair"></div>`; }
    else {
      const av = AVANT.filter(k => d[k]).map(k => `<p>${k === 'question' ? '<b>' + gl(esc(d[k])) + '</b>' : k === 'valeurAvecUnite' ? 'Valeur : <b>' + esc(d[k]) + '</b>' : k === 'imageOuTraceAttendu' ? 'Ce que montre l\'examen : ' + gl(esc(d[k])) : gl(esc(d[k]))}</p>`).join('');
      const q = !d.question && QUESTION[d.type] ? `<p><b>${QUESTION[d.type]}</b></p>` : '';
      if (d.type === 'bon_examen' && d.options) corps = av + q + `<div class=opts>${melanger(d.options).map(o => `<button data-o="${esc(o)}">${esc(o)}</button>`).join('')}</div>`;
      else if (d.type === 'indication') corps = av + `<p><b>Demandes-tu « ${esc(d._nom || '')} » dans cette situation ?</b></p><div class=opts><button data-o=Oui>Oui, je le demande</button><button data-o=Non>Non, je ne le demande pas</button></div>`;
      else if (d.type === 'ordonner_le_geste' && d.etapesMelangees) { corps = av + `<p><b>Tu cliques les étapes dans l'ordre du geste.</b></p><ol class=etapes>${d.etapesMelangees.map(e => `<li><button data-e="${esc(e)}">${esc(e)}</button></li>`).join('')}</ol><p id=ordre class=mini></p>`; }
      else corps = av + q + `<div class=actions><button data-voir>Voir la réponse</button></div>`;
    }
    this.el.innerHTML = `<div class=q>${meta}${corps}<div class=corr hidden></div></div><div class=actions><button class=sec data-r>Revenir aux jeux</button></div>`;
    this.el.querySelector('[data-r]').onclick = () => { clearInterval(this.tic); this.accueil(); };
    const ch = this.el.querySelector('.chrono'), fin = temps ? Date.now() + temps * 1000 : null;
    const maj = () => { const s = Math.floor((Date.now() - this.debut) / 1000); if (fin) { const r = Math.max(0, Math.ceil((fin - Date.now()) / 1000)); ch.textContent = r + ' s'; ch.classList.toggle('bas', r <= 10); if (!r && !this.cour.rep) this.conclure(false, 'Le temps est écoulé.'); }
      else if (this.opts.blanc) { const r = Math.max(0, this.opts.total - Math.floor((Date.now() - this.debutJeu) / 1000)); ch.textContent = Math.floor(r / 60) + ' min ' + String(r % 60).padStart(2, '0'); if (!r) { this.file = []; this.bilan(); } }
      if (s >= 720 && !this.prevenu) { this.prevenu = true; const g = document.createElement('p'); g.className = 'garde'; g.textContent = 'La session atteint 12 minutes : tu peux t\'arrêter ici, ta progression reste enregistrée.'; this.el.appendChild(g); } };
    if (this.opts.chrono || this.opts.blanc) { maj(); this.tic = setInterval(maj, 500); }
    // interactions
    this.el.querySelectorAll('[data-o]').forEach(b => b.onclick = () => { if (this.cour.rep) return; const ok = norm(b.dataset.o) === norm(d.type === 'indication' ? d.faireOuNon : d.bonneReponse);
      b.classList.add(ok ? 'juste' : 'faux'); if (!ok) this.el.querySelectorAll('[data-o]').forEach(x => { if (norm(x.dataset.o) === norm(d.type === 'indication' ? d.faireOuNon : d.bonneReponse)) x.classList.add('juste'); }); this.conclure(ok); });
    const v = this.el.querySelector('[data-voir]'); if (v) v.onclick = () => { if (this.opts.blanc) return; v.parentElement.innerHTML = '<span class=mini>Tu compares avec ta réponse, puis tu juges honnêtement :</span> <button data-a=1>Je l\'avais</button><button class=sec data-a=0>Je ne l\'avais pas</button>';
      this.montrerCorrection(d, null, true); this.el.querySelectorAll('[data-a]').forEach(b => b.onclick = () => this.conclure(b.dataset.a === '1')); };
    if (d.type === 'ordonner_le_geste') { const choix = []; this.el.querySelectorAll('[data-e]').forEach(b => b.onclick = () => { if (b.disabled) return; b.disabled = true; choix.push(b.dataset.e); this.el.querySelector('#ordre').textContent = 'Ton ordre : ' + choix.map((c, i) => (i + 1) + '. ' + c).join(' → ');
      if (choix.length === d.etapesMelangees.length) this.conclure(choix.every((c, i) => norm(c) === norm((d.ordreCorrect || [])[i]))); }); }
    if (d.type === 'cas') { this.el.querySelectorAll('.opts button').forEach(b => b.onclick = () => { if (this.cour.rep) return; b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') !== 'true'); });
      this.el.querySelector('[data-v]').onclick = () => { if (this.cour.rep) return; const c = d._cas, sel = [...this.el.querySelectorAll('.opts button')].map(b => b.getAttribute('aria-pressed') === 'true');
        const ok = c.options.every((o, i) => !!o.correct === sel[i]); if (!this.opts.blanc) this.el.querySelectorAll('.opts button').forEach((b, i) => b.classList.add(c.options[i].correct ? 'juste' : (sel[i] ? 'faux' : 'x'))); this.conclure(ok); }; }
    if (d.type === 'cliche') { const img = this.el.querySelector('#cl'); img.onclick = e => { if (this.cour.rep) return; const r = img.getBoundingClientRect(), k = img.naturalWidth / r.width, X = (e.clientX - r.left) * k, Y = (e.clientY - r.top) * k, a = d._n.cliches.annotations[0];
      this.conclure(((X - a.x) / a.rx) ** 2 + ((Y - a.y) / a.ry) ** 2 <= 1.15, null); }; }
  }
  conclure(ok, msg) {
    if (this.cour.rep) return; clearInterval(this.tic); const { d, revanche } = this.cour; this.cour.rep = ok ? 'ok' : 'ko';
    const dangereuse = ['piege', 'erreur_de_prelevement'].includes(d.type) || d.niveau === 3, pts = (d.points || 10) * (revanche ? 2 : 1);
    this.res.push({ d, ok });
    if (this.opts.blanc) { this.suivant(); return; }
    if (ok) { this.p.points += pts; this.p.reussites++; this.serie++; } else { this.p.points = Math.max(0, this.p.points - (d.points || 10) * (dangereuse ? 3 : 1)); this.p.erreurs++; this.serie = 0; }
    const b = this.p.boites[d.id] || { b: 0 }; b.b = ok ? Math.min(6, b.b + 1) : 1; b.due = Date.now() + INTERVALLES[b.b] * JOUR + (ok ? 0 : 6e5); this.p.boites[d.id] = b;
    if (d._ref) this.p.refs[d._ref] = ok ? 'ok' : 'ko'; this.sauver(); this.marquer();
    const verdict = ok ? `<p class="verdict ok">Juste : +${pts} points.</p>` : `<p class="verdict ko">${msg ? this.esc(msg) + ' ' : ''}${dangereuse ? 'Erreur dangereuse : elle coûte trois fois plus (−' + (d.points || 10) * 3 + ' points).' : 'Erreur : −' + (d.points || 10) + ' points.'} L'échelle de correction s'ouvre.</p>`;
    this.montrerCorrection(d, verdict, ok);
    if (!ok && d._ref) { const autre = this.defis.find(x => x._ref === d._ref && x.id !== d.id && !this.res.some(r => r.d.id === x.id) && !this.file.some(f => f.d.id === x.id)); if (autre) this.file.unshift({ d: autre, revanche: true }); }
    const a = document.createElement('div'); a.className = 'actions'; a.innerHTML = `<button data-s>${this.file.length ? (this.file[0].revanche ? 'Jouer la revanche' : 'Défi suivant') : 'Voir le bilan'}</button>`; this.el.querySelector('.q').appendChild(a); a.querySelector('[data-s]').onclick = () => this.suivant();
    const tb = this.el.querySelector('.tableau'); if (tb) tb.remove();
  }
  montrerCorrection(d, verdict, court) {
    const esc = this.esc, gl = this.gloser, c = this.el.querySelector('.corr'); c.hidden = false; let h = verdict || '';
    if (d.type === 'cas') { const k = d._cas; h += '<dl>' + k.options.map(o => `<dt>${o.correct ? 'À demander' : 'Inutile'}</dt><dd><b>${esc(o.text)}</b> : ${gl(esc(o.why))}</dd>`).join('') + '</dl><h4 style="margin:8px 0 4px">Échelle de correction</h4><dl>' + ECHELLE.filter(([x]) => k.correction?.[x]).map(([x, l]) => `<dt>${l}</dt><dd>${gl(esc(k.correction[x]))}</dd>`).join('') + '</dl>' + (k.sources ? '<p class=mini>Sources : ' + esc(k.sources.join(' ; ')) + '</p>' : ''); }
    else if (d.type === 'cliche') { const f = d._n.cliches; h += `<p>La lésion se situe au repère 1 : ${esc(f.annotations[0].texte)}</p><p>${esc(f.diagnostic)}</p><p><button class=lien data-cl>Ouvrir la fenêtre à deux clichés</button></p>`; }
    else {
      const ap = APRES.filter(([k]) => d[k] && !(k === 'aspectRecherche' && d.type !== 'lecture')).map(([k, l]) => `<dt>${l}</dt><dd>${gl(esc(Array.isArray(d[k]) ? d[k].join(' → ') : d[k]))}</dd>`).join('');
      const bonne = d.bonneReponse ? `<dt>Bonne réponse</dt><dd>${esc(d.bonneReponse)}</dd>` : d.faireOuNon ? `<dt>Bonne réponse</dt><dd>${esc(d.faireOuNon)}</dd>` : d.ordreCorrect ? `<dt>Ordre juste</dt><dd>${esc(d.ordreCorrect.join(' → '))}</dd>` : '';
      h += '<dl>' + bonne + ap + (d.correction?.pourquoiJuste ? `<dt>Pourquoi c'est juste</dt><dd>${gl(esc(d.correction.pourquoiJuste))}</dd>` : '') + (d.correction?.pourquoiFaux ? `<dt>Pourquoi le reste est faux</dt><dd>${gl(esc(d.correction.pourquoiFaux))}</dd>` : '') + '</dl>' + (d.sources?.length ? '<p class=mini>Source : ' + esc(d.sources.join(' ; ')) + '</p>' : '');
    }
    c.innerHTML = h; const bc = c.querySelector('[data-cl]'); if (bc) bc.onclick = () => window.__jeu.action(d._n, 'cliches');
  }
  bilan() {
    clearInterval(this.tic); const esc = this.esc, ok = this.res.filter(r => r.ok).length, n = this.res.length;
    let h = `<h2>Bilan : ${esc(this.nomJeu)}</h2><p>Tu as réussi ${ok} défi${ok > 1 ? 's' : ''} sur ${n}.</p>`;
    if (this.opts.blanc) {
      for (const r of this.res) { const pts = r.ok ? 1 : 0; this.p.points += r.ok ? (r.d.points || 10) : 0; if (r.d._ref) this.p.refs[r.d._ref] = r.ok ? 'ok' : 'ko'; const b = this.p.boites[r.d.id] || { b: 0 }; b.b = r.ok ? Math.min(6, b.b + 1) : 1; b.due = Date.now() + INTERVALLES[b.b] * JOUR; this.p.boites[r.d.id] = b; void pts; }
      this.sauver(); this.marquer();
      h += '<p class=mini>Les corrections n\'apparaissent qu\'à la fin, comme à l\'examen.</p>' + this.res.map((r, i) => `<details class=q><summary>${i + 1}. ${r.ok ? '✓' : '✗'} ${esc(r.d._cas ? r.d._cas.titre : (r.d.casClinique || r.d.question || '').slice(0, 90))}</summary><div class=corr data-k=${i}></div></details>`).join('');
    }
    h += '<div class=actions><button data-r>Revenir aux jeux</button></div>'; this.el.innerHTML = h; this.el.querySelector('[data-r]').onclick = () => this.accueil();
    if (this.opts.blanc) this.el.querySelectorAll('[data-k]').forEach(c => { const r = this.res[+c.dataset.k]; const q = c.closest('.q'); const tmp = document.createElement('div'); tmp.className = 'corr'; q.replaceChild(tmp, c); this.montrerCorrectionDans(tmp, r.d, r.ok); });
  }
  montrerCorrectionDans(div, d, ok) { const sauve = this.el.querySelector; const ancien = div.className; div.className = 'corr'; const fake = { querySelector: () => div }; this.montrerCorrection.call(Object.assign(Object.create(this), { el: fake }), d, `<p class="verdict ${ok ? 'ok' : 'ko'}">${ok ? 'Juste.' : 'Faux.'}</p>`, ok); void sauve; void ancien; }
}
