"""Catálogo de cursos por puesto: Recepcionista, Barista, Coach (fácil de agregar más cursos)."""
import sys, re, time
F = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
s = open(F).read()
assert 'const COURSES=' not in s, 'ya parcheado'

def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (old[:90], s.count(old))
    s = s.replace(old, new)

# --- textos viejos del curso (80% y "10 bloques") en los datos ---
k = s.index('<script>\nconst BR='); e = s.index('\n{\nconst $', k)
data = s[k:e]
data = data.replace('Con 80% se abre el siguiente', 'Con 90% se abre el siguiente').replace('Si no llegas a 80%', 'Si no llegas a 90%')
data = data.replace('"10 bloques cortos, un mini examen por bloque y un examen final."', '"Bloques cortos, un mini examen por bloque y un examen final."')
data = data.replace('Al terminar los 10 bloques', 'Al terminar todos los bloques').replace('Al terminar los 11 bloques', 'Al terminar todos los bloques')
data = data.replace('"11 bloques cortos, un mini examen por bloque y un examen final."', '"Bloques cortos, un mini examen por bloque y un examen final."')
s = s[:k] + data + s[e:]

CAT = r"""
// ===== Catálogo de cursos =====
// Para agregar un curso nuevo: se agrega un objeto a COURSES con sus bloques (B) y preguntas (Q).
const PUESTOS=[{id:'rec',name:'Recepcionista',ic:'R',d:'Atención en persona y por WhatsApp, informes, operación y caja.'},
 {id:'barista',name:'Barista',ic:'B',d:'Energy Bar: higiene, preparación, servicio y ventas en la barra.'},
 {id:'coach',name:'Coach',ic:'C',d:'Clase, técnica, programación, nutrición y mentalidad.'}];
const _cl=o=>JSON.parse(JSON.stringify(o));
const BB=(()=>{const intro=_cl(BR[0]);intro.d='Qué es Roxet, cómo funciona este curso y la regla de oro de la barra.';
  intro.lessons[0][1]='Formas parte de la Familia Roxet. Desde la barra eres parte de la experiencia de cada cliente.';
  intro.lessons[0][3]=['“Yo nomás preparo bebidas.”','“Cada bebida que sirvo hace que el cliente quiera volver.”'];
  return [intro,...[1,8,9,10].map((i,n)=>Object.assign(_cl(BR[i]),{t:'Bloque '+(n+1)}))]})();
const QB=(()=>{const tp=new Set();BB.forEach(b=>b.quiz.forEach(t=>tp.add(t)));return QR.filter(q=>tp.has(q[0]))})();
const COURSES=[
 {id:'rec',puestos:['rec'],title:'Atención en recepción',short:'Recepción',code:'R',full:'Curso de atención en recepción',B:BR,Q:QR,d:'Primer contacto, informes, WhatsApp, operación diaria, app RXT, barra, caja y quejas.'},
 {id:'barista',puestos:['barista'],title:'Barra y Energy Bar',short:'Barra',code:'B',full:'Curso de barra y Energy Bar',B:BB,Q:QB,d:'Actitud, higiene, preparación, hora pico, vender más, cobro y quejas en la barra.'},
 {id:'coach',puestos:['coach'],title:'Coach RXT',short:'Coach',code:'C',full:'Curso del coach RXT',B:BC,Q:QC,d:'Clase, voz de mando, piso, técnica, biomecánica, fisiología, programación, nutrición y mentalidad.'}];
const SOON={rec:['Ventas y seguimiento avanzado'],barista:['Recetario de la Energy Bar'],coach:['HYROX y entrenamiento híbrido','Rehabilitación y lesiones']};
const CUR=()=>COURSES.find(c=>c.id===ROLE)||COURSES[0];
let PUESTO='rec';
"""
rep("let ROLE='rec',B=BR,Q=QR,S={name:'',done:[],final:null};",
    CAT + "let ROLE='rec',B=BR,Q=QR,S={name:'',done:[],final:null};")
rep("const RN={rec:'Curso de atención en recepción',coach:'Curso del coach RXT'};",
    "const RN={};COURSES.forEach(c=>RN[c.id]=c.full);")
rep("const load=r=>{ROLE=r;B=r==='coach'?BC:BR;Q=r==='coach'?QC:QR;",
    "const load=r=>{const c=COURSES.find(x=>x.id===r)||COURSES[0];ROLE=c.id;B=c.B;Q=c.Q;")
rep("localStorage.setItem('rxtRole',ROLE)}catch(e){}};", "localStorage.setItem('rxtRole',ROLE);localStorage.setItem('rxtPuesto',PUESTO);if(S.name)localStorage.setItem('rxtName',S.name)}catch(e){}};")
rep("const views=['vCover','vStart','vMap',", "const views=['vCover','vStart','vCourses','vMap',")
rep("v==='vCover'||v==='vStart'||v==='vMap'||", "v==='vCover'||v==='vStart'||v==='vCourses'||v==='vMap'||")
rep("(ROLE==='coach'?'Coach':'Recepción')", "CUR().title")
rep("f.folio='RXT-'+(ROLE==='coach'?'C':'R')+'-'", "f.folio='RXT-'+CUR().code+'-'", 2)

# --- pantalla de inicio: puestos ---
old_btns = s[s.index('<div class="map"><button class="blk" data-role="rec">'):s.index('</div></div>\n</section>\n<section id="vMap"')]
rep(old_btns, '<div class="map" id="puestos"></div>')
rep('<p class="lead">Elige tu curso. Son bloques cortos: lees cada lección, contestas un mini examen y se abre el siguiente bloque. Al final haces el examen completo y obtienes tu constancia.</p>',
    '<p class="lead">Escribe tu nombre y elige tu puesto. Ahí verás todos los cursos que te tocan: bloques cortos, mini examen en cada uno y al final tu certificado.</p>')
rep('<section id="vMap" class="hide">',
    '<section id="vCourses" class="hide"><div class="kick" id="cwho"></div><h1 id="ctitle">Mis cursos</h1><p class="lead" id="clead"></p><div class="map" id="clist"></div>'
    '<p class="note" style="margin-top:14px"><button class="btn ghost" id="cpu" style="min-height:40px;padding:0 14px;font-size:13px">Cambiar de puesto</button></p></section>\n<section id="vMap" class="hide">')
rep('id="chg" style="min-height:40px;padding:0 14px;font-size:13px;margin-left:6px">Cambiar de curso</button>',
    'id="chg" style="min-height:40px;padding:0 14px;font-size:13px;margin-left:6px">← Mis cursos</button>')

CSS = """
/* ===== FX5: catálogo ===== */
.blk .pr{display:block;height:5px;border-radius:5px;background:var(--line);margin-top:8px;overflow:hidden}.blk .pr i{display:block;height:100%;background:var(--red)}
.blk.soon{opacity:.55;border-style:dashed;cursor:default}.blk.soon .st{background:transparent;border:1px dashed var(--line);color:var(--soft)}
.blk.pu .n{background:var(--ink);color:var(--bg)}
"""
rep('</style></head>', CSS + '</style></head>')

# --- lógica: puestos y lista de cursos ---
FN = r"""
const courseStat=id=>{const c=COURSES.find(x=>x.id===id);let st=null;try{st=JSON.parse(localStorage.getItem('rxtCurso_'+id)||'null')}catch(e){}
  const nm=(localStorage.getItem('rxtName')||'');if(!st||st.name!==nm)return{n:0,t:c.B.length+1,pass:false};
  return{n:(st.done||[]).length+(st.final&&st.final.pass?1:0),t:c.B.length+1,pass:!!(st.final&&st.final.pass)}};
function puestos(){const nb=COURSES.reduce((a,c)=>a+c.B.length,0);
  $('puestos').innerHTML=PUESTOS.map(p=>{const n=COURSES.filter(c=>c.puestos.includes(p.id)).length;
    return `<button class="blk pu" data-puesto="${p.id}"><span class="n">${p.ic}</span><span><b>Soy ${p.name.toLowerCase()}</b><small>${n} curso${n>1?'s':''} · ${p.d}</small></span><span class="st">Ver cursos</span></button>`}).join('');
  $('puestos').querySelectorAll('[data-puesto]').forEach(b=>b.onclick=()=>{const n=$('nm').value.trim();if(n.length<3){$('nmErr').textContent='Escribe tu nombre completo y luego elige tu puesto.';return}
    try{localStorage.setItem('rxtName',n);localStorage.setItem('rxtPuesto',b.dataset.puesto)}catch(e){}PUESTO=b.dataset.puesto;courses()});}
function courses(){const p=PUESTOS.find(x=>x.id===PUESTO)||PUESTOS[0];const nm=localStorage.getItem('rxtName')||S.name||'';
  $('cwho').textContent=(nm?nm+' · ':'')+p.name.toUpperCase();$('ctitle').textContent='Cursos de '+p.name.toLowerCase();
  $('clead').textContent='Elige un curso. Tu avance de cada curso se guarda por separado en este celular.';
  const list=COURSES.filter(c=>c.puestos.includes(p.id));
  $('clist').innerHTML=list.map(c=>{const st=courseStat(c.id);const pct=Math.round(st.n/st.t*100);
    return `<button class="blk ${st.pass?'done':''}" data-course="${c.id}"><span class="n">${st.pass?'✓':c.code}</span><span><b>${c.title}</b><small>Introducción + ${c.B.length-1} bloques · ${c.d}</small><span class="pr"><i style="width:${pct}%"></i></span></span><span class="st">${st.pass?'Certificado':st.n?'Continuar':'Empezar'}</span></button>`}).join('')
   +(SOON[p.id]||[]).map(t=>`<div class="blk soon"><span class="n">+</span><span><b>${t}</b><small>Muy pronto en la Academia RXT.</small></span><span class="st">Próximamente</span></div>`).join('');
  $('clist').querySelectorAll('[data-course]').forEach(b=>b.onclick=()=>{const n=localStorage.getItem('rxtName')||'';load(b.dataset.course);if(S.name!==n){S={name:n,done:[],final:null}}save();map()});
  show('vCourses');FX.map&&FX.view('vCourses');
  [...$('clist').children].forEach((b,i)=>{b.style.animation='vin .45s both';b.style.animationDelay=(i*70)+'ms'})}
$('cpu').onclick=()=>show('vStart');
puestos();
"""
rep("document.querySelectorAll('[data-role]').forEach(b=>b.onclick=()=>{const n=$('nm').value.trim();if(n.length<3){$('nmErr').textContent='Escribe tu nombre completo y luego elige tu curso.';return}\n  load(b.dataset.role);if(S.name!==n){S={name:n,done:[],final:null}}save();map()});",
    FN)
rep("$('chg').onclick=()=>{show('vStart')};", "$('chg').onclick=()=>courses();")
rep("function boot(){if(fromHash())return;show('vCover');try{const r=localStorage.getItem('rxtRole');if(r){load(r);if(S.name){$('nm').value=S.name;",
    "function boot(){if(fromHash())return;show('vCover');try{PUESTO=localStorage.getItem('rxtPuesto')||'';const r=localStorage.getItem('rxtRole');if(!PUESTO&&r)PUESTO=r==='coach'?'coach':'rec';if(!PUESTO)PUESTO='rec';const nm=localStorage.getItem('rxtName');if(nm)$('nm').value=nm;if(r){load(r);if(S.name){$('nm').value=S.name;try{if(!nm)localStorage.setItem('rxtName',S.name)}catch(e){}")
# portada: número de cursos y bloques
rep('<div class="cg"><div><b>2</b><span>cursos</span></div><div><b>22</b><span>bloques</span></div>',
    '<div class="cg"><div><b id="ncur">3</b><span>cursos</span></div><div><b id="nblk">27</b><span>bloques</span></div>')
rep("puestos();\n", "puestos();\ntry{$('ncur').textContent=COURSES.length;$('nblk').textContent=COURSES.reduce((a,c)=>a+c.B.length-1,0)}catch(e){}\n")
rep("$('cb2').onclick=()=>{HASHVIEW=false;try{history.replaceState(null,'',' ')}catch(e){}show('vStart')};", "$('cb2').onclick=()=>{HASHVIEW=false;try{history.replaceState(null,'',' ')}catch(e){}show('vStart')};")
s = re.sub(r'name="rxt-ver" content="\d+"', 'name="rxt-ver" content="' + time.strftime('%Y%m%d%H%M') + '"', s, count=1)
open(F, 'w').write(s)
print('ok')
