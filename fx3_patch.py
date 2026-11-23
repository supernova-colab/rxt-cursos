"""Evaluación bloqueada: puntos obligatorios, confirmación antes del examen, sin regresar a la info."""
import sys, time, re
F = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
s = open(F).read()
assert 'FX.confirm' not in s, 'ya parcheado'

def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:90], s.count(old))
    s = s.replace(old, new)

CSS = r"""
/* ===== FX3: evaluación ===== */
.btn.lockbtn{background:color-mix(in srgb,var(--ink) 22%,var(--bg));color:color-mix(in srgb,var(--ink) 60%,transparent)}
.need{font:700 13px Inter;color:var(--red);min-height:18px;margin-top:10px}
ol.pp li.miss{background:color-mix(in srgb,var(--red) 10%,transparent);animation:shake .45s}
.cfo{position:fixed;inset:0;z-index:9000;background:rgba(10,10,12,.55);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);display:grid;place-items:end center;padding:16px;animation:vin .25s both}
.cfb{width:min(520px,100%);background:var(--card);color:var(--ink);border-radius:26px;padding:26px 22px 20px;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,.35);animation:vin .35s cubic-bezier(.2,.8,.2,1) both;margin-bottom:max(12px,env(safe-area-inset-bottom))}
.cfb .ic{width:64px;height:64px;margin:0 auto 12px;border-radius:50%;background:var(--red);display:grid;place-items:center;animation:bump .5s .15s both}
.cfb .ic svg{width:30px;height:30px;fill:none;stroke:#fff;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.cfb h3{font:800 24px/1.15 "Inter Tight",Inter,sans-serif;margin:0 0 8px}.cfb p{margin:0 0 6px;color:var(--soft);font-size:15px}
.cfb ul{text-align:left;margin:12px 0 4px;padding:0;list-style:none}.cfb li{padding:8px 0 8px 30px;position:relative;font-size:15px;border-top:1px dashed var(--line)}
.cfb li::before{content:"•";position:absolute;left:10px;color:var(--red);font-weight:900}
.cfb .row{justify-content:center}.cfb .btn{flex:1 1 140px}
.evb{display:flex;align-items:center;gap:8px;font:700 12px Inter;color:var(--soft);margin:-6px 0 12px}.evb svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
"""
rep('</style></head>', CSS + '</style></head>')

# --- FX: lesson con puntos obligatorios + confirm ---
LESSON_OLD = s[s.index("lesson:()=>{"):s.index(" streak:")]
LESSON_NEW = r"""lesson:(pre,onRead)=>{const root=document.getElementById('vLesson');const lis=[...root.querySelectorAll('ol.pp li')];const nx=document.getElementById('ln');
  const row=nx&&nx.closest('.row');let need=root.querySelector('.need');if(!need&&row){row.insertAdjacentHTML('beforebegin','<div class="need" id="need"></div>');need=root.querySelector('.need')}
  const all=()=>lis.every(x=>x.classList.contains('chk'));
  const upd=()=>{if(!nx)return;const ok=all();nx.classList.toggle('lockbtn',!ok);if(ok){need.textContent='';nx.style.animation='glow 1.6s infinite';onRead&&onRead()}else nx.style.animation=''};
  if(pre)lis.forEach(li=>li.classList.add('chk'));
  lis.forEach(li=>li.onclick=()=>{if(li.classList.contains('chk'))return;li.classList.add('chk');li.classList.remove('miss');vib(12);if(all()){const[a,b]=ctr(li);boom(a,b,24,6)}upd()});
  if(nx)nx.addEventListener('click',e=>{if(all())return;e.stopImmediatePropagation();e.preventDefault();const m=lis.filter(x=>!x.classList.contains('chk'));
   m.forEach(x=>{x.classList.remove('miss');void x.offsetWidth;x.classList.add('miss')});need.textContent='👆 Marca todos los puntos para continuar ('+(lis.length-m.length)+' de '+lis.length+')';vib([40,50,40]);
   m[0].scrollIntoView({block:'center',behavior:'smooth'})},true);
  upd();
  const f=root.querySelector('.flip');if(f)f.onclick=()=>{if(f.classList.contains('open'))return;f.classList.add('open');vib(20);const[a,b]=ctr(f);boom(a,b,30,7)}},
 confirm:(go,fin)=>{const o=document.createElement('div');o.className='cfo';o.innerHTML=`<div class="cfb" role="dialog" aria-modal="true"><div class="ic"><svg viewBox="0 0 24 24"><path d="M7.5 11V8a4.5 4.5 0 0 1 9 0v3"/><rect x="5" y="11" width="14" height="10" rx="2.5"/><path d="M12 15v2.5"/></svg></div>
  <h3>¿Estás seguro?</h3><p>${fin?'Vas a empezar el examen final.':'Vas a empezar la evaluación del bloque.'}</p>
  <ul><li>Si empiezas, <b>ya no puedes regresar a ver la información</b> hasta terminar.</li><li>Necesitas <b>80%</b> para aprobar${fin?' y obtener tu certificado':' y abrir el siguiente bloque'}.</li><li>Si no apruebas, puedes repasar y volver a intentarlo.</li></ul>
  <div class="row"><button class="btn ghost" id="cfn">Todavía no</button><button class="btn" id="cfy">Sí, empezar</button></div></div>`;
  document.body.appendChild(o);vib(15);const close=()=>o.remove();o.querySelector('#cfn').onclick=close;o.onclick=e=>{if(e.target===o)close()};o.querySelector('#cfy').onclick=()=>{close();go()}},
"""
s = s.replace(LESSON_OLD, LESSON_NEW, 1)

# --- lección: botones ---
rep("${last?(b.quiz.length?'Ir al mini examen':'Terminar introducción'):'Siguiente lección'}</button></div>`;",
    "${last?(b.quiz.length?(S.done.includes(k)?'Volver a bloques':'Iniciar evaluación'):'Terminar introducción'):'Siguiente lección'}</button></div>${last&&b.quiz.length&&S.done.includes(k)?'<div class=\"row\" style=\"margin-top:8px\"><button class=\"btn ghost\" id=\"lr\">Repetir evaluación</button></div>':''}`;")
rep("if(b.quiz.length)return quiz(k);", "if(b.quiz.length){if(S.done.includes(k))return map();return FX.confirm(()=>quiz(k))}")
rep("map()};show('vLesson');FX.lesson();",
    "map()};if($('lr'))$('lr').onclick=()=>FX.confirm(()=>quiz(k));show('vLesson');FX.lesson(S.done.includes(k)||!!(S.read&&S.read.includes(k+'-'+j)),()=>{S.read=S.read||[];if(!S.read.includes(k+'-'+j)){S.read.push(k+'-'+j);save()}});")
# --- examen final con confirmación ---
rep("if(S.final&&S.final.pass)cert();else quiz('F');", "if(S.final&&S.final.pass)cert();else FX.confirm(()=>quiz('F'),true);")
rep("$('rt').onclick=()=>fin?quiz('F'):lesson(k,0);", "$('rt').onclick=()=>fin?FX.confirm(()=>quiz('F'),true):lesson(k,0);")
# --- sin salir a la info durante el examen ---
rep("<button class=\"btn ghost\" id=\"qb\">${p?'Anterior':'Salir'}</button>", "${p?'<button class=\"btn ghost\" id=\"qb\">Anterior</button>':''}")
rep("$('qb').onclick=()=>p?(p--,r()):map();", "if($('qb'))$('qb').onclick=()=>{p--;r()};")
rep("<div class=\"kick\">${title.toUpperCase()}</div><div class=\"bar\"><i style=\"width:${p/list.length*100}%\"></i></div>",
    "<div class=\"kick\">${title.toUpperCase()}</div><div class=\"bar\"><i style=\"width:${p/list.length*100}%\"></i></div><div class=\"evb\"><svg viewBox=\"0 0 24 24\"><path d=\"M7.5 11V8a4.5 4.5 0 0 1 9 0v3\"/><rect x=\"5\" y=\"11\" width=\"14\" height=\"10\" rx=\"2.5\"/></svg>Evaluación en curso · la información se abre al terminar</div>")
rep("v==='vMap'||HASHVIEW", "v==='vMap'||v==='vQuiz'||HASHVIEW")
# versión para auto-actualización
s = re.sub(r'name="rxt-ver" content="\d+"', 'name="rxt-ver" content="' + time.strftime('%Y%m%d%H%M') + '"', s, 1)
open(F, 'w').write(s)
print('ok')
