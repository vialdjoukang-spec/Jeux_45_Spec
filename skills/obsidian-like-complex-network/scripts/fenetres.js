// Fenêtres de détail : courbes et calculateurs calculés (canvas 2D, jamais de SVG) + vue 3D.
export function ouvrirFenetre(type, titre, couleur){
  let f=document.getElementById('fdet');if(f)f.remove();
  f=document.createElement('div');f.id='fdet';f.style.setProperty('--c',couleur||'#2f6fd0');
  f.innerHTML=`<div class=fh><b>${titre}</b><button title="Fermer">✕</button></div><div class=fc></div>`;document.body.appendChild(f);
  f.querySelector('button').onclick=()=>f.remove();const C=f.querySelector('.fc');
  (MODELES[type]||MODELES.inconnu)(C);return f;}
const kPa=mm=>mm*0.1333, mm=k=>k/0.1333;
function axes(x,W,H,m,xr,yr,xl,yl){x.clearRect(0,0,W,H);x.strokeStyle='#8a94a3';x.lineWidth=1;x.font='11px A';x.fillStyle='#3a4556';
 x.beginPath();x.moveTo(m,H-m);x.lineTo(W-10,H-m);x.moveTo(m,H-m);x.lineTo(m,10);x.stroke();
 for(let i=0;i<=5;i++){const vx=xr[0]+(xr[1]-xr[0])*i/5,vy=yr[0]+(yr[1]-yr[0])*i/5;const px=m+(W-m-10)*i/5,py=H-m-(H-m-10)*i/5;
  x.fillText((+vx.toFixed(1)).toString(),px-8,H-m+14);x.textAlign='right';x.fillText((+vy.toFixed(2)).toString(),m-5,py+4);x.textAlign='left';x.strokeStyle='#e3e7ec';x.beginPath();x.moveTo(px,H-m);x.lineTo(px,10);x.moveTo(m,py);x.lineTo(W-10,py);x.stroke();}
 x.fillText(xl,W-150,H-6);x.save();x.translate(9,H/2+30);x.rotate(-Math.PI/2);x.fillText(yl,0,0);x.restore();
 return (vx,vy)=>[m+(vx-xr[0])/(xr[1]-xr[0])*(W-m-10),H-m-(vy-yr[0])/(yr[1]-yr[0])*(H-m-10)];}
function curseur(C,lab,min,max,pas,val,cb){const d=document.createElement('label');d.className='cur';d.innerHTML=`<span>${lab}</span><input type=range min=${min} max=${max} step=${pas} value=${val}><output>${val}</output>`;
 C.appendChild(d);const i=d.querySelector('input'),o=d.querySelector('output');i.oninput=()=>{o.textContent=i.value;cb();};return ()=>+i.value;}
function toile(C,W=520,H=300){const c=document.createElement('canvas');c.width=W;c.height=H;C.appendChild(c);return c.getContext('2d');}
const MODELES={
 odc(C){const x=toile(C);const note=document.createElement('p');const pH=curseur(C,'pH',7.0,7.7,0.01,7.40,d),T=curseur(C,'Température (°C)',34,41,0.1,37,d),D=curseur(C,'2,3-DPG (mmol/l)',3,8,0.1,5,d);C.appendChild(note);
  function sat(P,p50){const n=2.7;return Math.pow(P,n)/(Math.pow(P,n)+Math.pow(p50,n))*100;}
  function d(){const P=axes(x,520,300,40,[0,16],[0,100],'PaO₂ (kPa)','SaO₂ (%)');const p0=3.55,p50=p0*Math.pow(10,-0.48*(pH()-7.4)+0.024*(T()-37)+0.03*(D()-5));
   for(const [pp,col,w] of [[p0,'#9aa3ad',1.5],[p50,getComputedStyle(C).getPropertyValue('--c')||'#2f6fd0',2.5]]){x.strokeStyle=col;x.lineWidth=w;x.beginPath();for(let k=0;k<=160;k++){const v=k/10;const [a,b]=P(v,sat(v,pp));k?x.lineTo(a,b):x.moveTo(a,b);}x.stroke();}
   const [a,b]=P(p50,50);x.fillStyle='#d11';x.beginPath();x.arc(a,b,4,0,7);x.fill();x.fillText('P50 = '+p50.toFixed(2)+' kPa',a+6,b-6);
   const s=p50>p0+0.05?'La courbe se déplace à droite : l\'hémoglobine libère plus facilement l\'O₂ aux tissus (effet Bohr).':p50<p0-0.05?'La courbe se déplace à gauche : l\'hémoglobine retient l\'O₂ (alcalose, hypothermie, HbF, CO).':'La courbe est normale : P50 ≈ 3,5 kPa.';
   note.textContent=s+' À 8 kPa de PaO₂, la saturation vaut '+sat(8,p50).toFixed(0)+' % : sous ce seuil, elle chute vite.';}d();},
 hh(C){const x=toile(C);const note=document.createElement('p');const H=curseur(C,'HCO₃⁻ (mmol/l)',5,45,1,24,d),K=curseur(C,'PaCO₂ (kPa)',2,12,0.1,5.3,d);C.appendChild(note);
  function d(){const P=axes(x,520,300,40,[2,12],[6.9,7.8],'PaCO₂ (kPa)','pH');for(const h of [12,24,36]){x.strokeStyle='#b8c1cc';x.beginPath();for(let k=0;k<=100;k++){const pc=2+k/10;const ph=6.1+Math.log10(h/(0.23*pc));const [a,b]=P(pc,Math.max(6.9,Math.min(7.8,ph)));k?x.lineTo(a,b):x.moveTo(a,b);}x.stroke();const [a,b]=P(11.5,Math.min(7.78,Math.max(6.92,6.1+Math.log10(h/(0.23*11.5)))));x.fillText('HCO₃⁻ '+h,a-30,b-4);}
   const [n1,n2]=P(4.7,7.45),[n3,n4]=P(6.0,7.35);x.fillStyle='#2a9d8f22';x.fillRect(n1,n2,n3-n1,n4-n2);
   const ph=6.1+Math.log10(H()/(0.23*K()));const [a,b]=P(K(),Math.max(6.9,Math.min(7.8,ph)));x.fillStyle='#d11';x.beginPath();x.arc(a,b,5,0,7);x.fill();
   note.textContent='pH = 6,1 + log(HCO₃⁻ / (0,23 × PaCO₂)) = '+ph.toFixed(2)+'. Le rectangle vert marque la zone normale ; le poumon déplace le point horizontalement (PaCO₂), le rein le fait changer d\'isoplèthe (HCO₃⁻).';}d();},
 alveolaire(C){const note=document.createElement('p');const F=curseur(C,'FiO₂',0.21,1,0.01,0.21,d),Pa=curseur(C,'Pression atmosphérique (kPa ; 101,3 au niveau de la mer, ≈ 90 à La Chaux-de-Fonds)',60,102,0.1,101.3,d),K=curseur(C,'PaCO₂ (kPa)',2,12,0.1,5.3,d),O=curseur(C,'PaO₂ mesurée (kPa)',3,60,0.1,12,d),A=curseur(C,'Âge (ans)',18,95,1,40,d);C.appendChild(note);
  function d(){const PA=F()*(Pa()-6.3)-K()/0.8,g=PA-O(),gn=kPa(A()/4+4);note.innerHTML='PAO₂ = FiO₂ × (Patm − 6,3) − PaCO₂ / 0,8 = <b>'+PA.toFixed(1)+' kPa</b>. Gradient A-a = <b>'+g.toFixed(1)+' kPa</b> (attendu ≤ '+gn.toFixed(1)+' kPa pour l\'âge). '+(g>gn+0.3?'Le gradient est élevé : l\'hypoxémie vient d\'un trouble pulmonaire (shunt, V/Q, diffusion).':'Le gradient est normal : une hypoxémie viendrait d\'une hypoventilation ou d\'une FiO₂ basse.');}d();},
 gazometrie(C){const note=document.createElement('p');const p=curseur(C,'pH',6.9,7.7,0.01,7.25,d),K=curseur(C,'PaCO₂ (kPa)',2,12,0.1,3.2,d),H=curseur(C,'HCO₃⁻ (mmol/l)',5,45,1,10,d);C.appendChild(note);
  function d(){const ph=p(),k=K(),h=H();let t;if(ph<7.35){if(h<22){const att=kPa(1.5*h+8);t='Acidose métabolique. PaCO₂ attendue (Winter) = '+(att-kPa(2)).toFixed(1)+'–'+(att+kPa(2)).toFixed(1)+' kPa : '+(k<att-kPa(2)?'acidose avec alcalose respiratoire associée.':k>att+kPa(2)?'acidose respiratoire associée.':'compensation respiratoire adaptée.')+' Calcule ensuite le trou anionique.';}
   else if(k>6){const dm=mm(k)-40;t='Acidose respiratoire. HCO₃⁻ attendu : '+(24+dm/10).toFixed(0)+' (aigu) à '+(24+3.5*dm/10).toFixed(0)+' mmol/l (chronique).';}else t='Acidémie sans cause évidente : revois les valeurs.';}
   else if(ph>7.45){if(h>26){const att=kPa(0.7*h+21);t='Alcalose métabolique. PaCO₂ attendue ≈ '+att.toFixed(1)+' ± 0,3 kPa.';}else if(k<4.7){const dm=40-mm(k);t='Alcalose respiratoire. HCO₃⁻ attendu : '+(24-2*dm/10).toFixed(0)+' (aigu) à '+(24-5*dm/10).toFixed(0)+' mmol/l (chronique).';}else t='Alcalémie sans cause évidente : revois les valeurs.';}
   else t=(k>6&&h>26)||(k<4.7&&h<22)?'pH normal avec PaCO₂ et HCO₃⁻ anormaux : trouble mixte ou compensation complète.':'Gaz du sang dans les normes.';
   const calc=6.1+Math.log10(h/(0.23*k));note.innerHTML='<b>'+t+'</b><br>Contrôle de cohérence : pH calculé = '+calc.toFixed(2)+(Math.abs(calc-ph)>0.03?' : les valeurs saisies ne concordent pas.':' : les valeurs concordent.');}d();},
 spiro(C){const x=toile(C);const note=document.createElement('p');const b=document.createElement('div');b.className='boutons';C.prepend(b);C.appendChild(note);let mode='normal';
  for(const [k,l] of [['normal','Normal'],['obstructif','Obstructif'],['restrictif','Restrictif']]){const e=document.createElement('button');e.textContent=l;e.onclick=()=>{mode=k;d();};b.appendChild(e);}
  function boucle(V,pic,conc){const pts=[];for(let i=0;i<=100;i++){const v=V*i/100;let f=i<12?pic*i/12:pic*Math.pow((V-v)/(V*0.88),conc);pts.push([v,f]);}for(let i=100;i>=0;i--){const v=V*i/100;pts.push([v,-0.6*pic*Math.sin(Math.PI*i/100)]);}return pts;}
  function d(){const P=axes(x,520,300,40,[0,6],[-6,10],'Volume (l)','Débit (l/s)');const ref=boucle(5,9,1),cur=mode==='normal'?ref:mode==='obstructif'?boucle(5.2,5,2.2):boucle(3,7.5,1);
   for(const [pts,col,w] of [[ref,'#9aa3ad',1.5],[cur,'#2f6fd0',2.5]]){x.strokeStyle=col;x.lineWidth=w;x.beginPath();pts.forEach(([v,f],i)=>{const [a,c]=P(v,f);i?x.lineTo(a,c):x.moveTo(a,c);});x.stroke();}
   note.textContent={normal:'La boucle normale monte vite au débit de pointe puis décroît en ligne droite.',obstructif:'Le trouble obstructif creuse la courbe expiratoire (concavité) : le rapport VEMS/CVF passe sous 0,7.',restrictif:'Le trouble restrictif rétrécit la boucle : les volumes baissent, le rapport VEMS/CVF reste normal ou élevé.'}[mode];}d();},
 '3d'(C){C.innerHTML='<iframe src="anatomie.html" style="width:760px;height:460px;border:0;border-radius:8px"></iframe>';},
 inconnu(C){C.textContent='Fenêtre à produire.';}};
