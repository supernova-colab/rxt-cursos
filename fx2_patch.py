"""Bloques bloqueados: difuminado + candado, y animación de desbloqueo."""
import sys, json, base64
F = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
s = open(F).read()
assert 'class="lk"' not in s and '.blk .lk' not in s, 'ya parcheado'
CSS = r"""
/* ===== FX2: candados ===== */
.blk{position:relative;overflow:hidden}
.blk.lock{opacity:1}
.blk.lock>span:not(.lk){filter:blur(5px) grayscale(.6);opacity:.45;transition:filter .7s,opacity .7s}
.blk .lk{position:absolute;inset:0;display:grid;place-items:center;pointer-events:none;background:color-mix(in srgb,var(--bg) 35%,transparent)}
.blk .lk i{display:grid;place-items:center;width:58px;height:58px;border-radius:50%;background:var(--ink);box-shadow:0 8px 22px rgba(0,0,0,.25)}
.blk .lk svg{width:28px;height:28px;fill:none;stroke:var(--bg);stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round;overflow:visible}
.blk .lk .sh{transition:transform .45s cubic-bezier(.3,1.6,.5,1);transform-origin:16.5px 11px}
.blk.lock:active .lk i{animation:shake .45s}
.blk.unl>span:not(.lk){animation:unblur .9s .7s both}
.blk.unl .lk{animation:lkout .5s 1.2s both}
.blk.unl .lk i{background:var(--red);animation:bump .4s .1s both}
.blk.unl .lk .sh{transform:translateY(-5px) rotate(28deg);transition-delay:.35s}
@keyframes unblur{from{filter:blur(5px) grayscale(.6);opacity:.45}to{filter:none;opacity:1}}
@keyframes lkout{to{opacity:0;transform:scale(1.4)}}
@media (prefers-reduced-motion:reduce){.blk.unl .lk{display:none}.blk.unl>span{animation:none!important}}
"""
LOCK = '<span class="lk" aria-hidden="true"><i><svg viewBox="0 0 24 24"><path class="sh" d="M7.5 11V8a4.5 4.5 0 0 1 9 0v3"/><rect x="5" y="11" width="14" height="10" rx="2.5"/><path d="M12 15v2.5"/></svg></i></span>'
OLD = "map:()=>{const bs=[...document.querySelectorAll('#map .blk')];bs.forEach((b,i)=>b.style.setProperty('--i',i));"
NEW = OLD + ("""const key='rxtUnl_'+(document.getElementById('who').textContent||'');let prev=null;try{prev=JSON.parse(localStorage.getItem(key)||'null')}catch(e){}
  const open=[];let fresh=[];bs.forEach((b,i)=>{if(b.classList.contains('lock'))b.insertAdjacentHTML('beforeend',LOCK);else{open.push(i);if(prev&&!prev.includes(i))fresh.push(b)}});
  fresh.forEach(b=>{b.classList.remove('next');b.insertAdjacentHTML('beforeend',LOCK);b.classList.add('unl');setTimeout(()=>{b.scrollIntoView({block:'center',behavior:'smooth'})},200);
   setTimeout(()=>{const[a,c]=ctr(b);boom(a,c,50,8);vib([20,40,20])},900);setTimeout(()=>{b.classList.remove('unl');const l=b.querySelector('.lk');if(l)l.remove()},2000)});
  try{localStorage.setItem(key,JSON.stringify(open))}catch(e){}""")
assert s.count(OLD) == 1
s = s.replace(OLD, NEW).replace('</style></head>', CSS + '</style></head>')
s = s.replace("const vib=p=>", "const LOCK='" + LOCK + "';const vib=p=>", 1)

# --- logos reales RXT en las ilustraciones ---
LOGO='data:image/png;base64,'+base64.b64encode(open('/home/claude/pdfs/cap/git/icon-192.png','rb').read()).decode()
J=lambda x: json.dumps(x)[1:-1]
app_old='<g class="a-pop d2"><rect class="r" x="176" y="58" width="18" height="18" rx="5"/><text class="tw" x="185" y="72" text-anchor="middle" style="font-size:9px">RXT</text></g>'
app_new='<g class="a-pop d2"><clipPath id="rxa"><rect x="173" y="55" width="24" height="24" rx="6"/></clipPath><image href="__LOGO__" x="173" y="55" width="24" height="24" clip-path="url(#rxa)"/></g>'
st_old='<g class="a-pop"><path class="r" d="M160 22l14 30 32 4-24 22 6 32-28-16-28 16 6-32-24-22 32-4z"/></g>\n<text class="tw" x="160" y="80" text-anchor="middle" style="font-size:15px">RXT</text>'
st_new='<g class="a-pop"><clipPath id="rxs"><rect x="122" y="30" width="76" height="76" rx="20"/></clipPath><rect class="r" x="118" y="34" width="84" height="84" rx="22" opacity=".25"/><image href="__LOGO__" x="122" y="30" width="76" height="76" clip-path="url(#rxs)"/></g>'
for o,n in ((app_old,app_new),(st_old,st_new)):
    assert s.count(J(o))==1,o[:40]; s=s.replace(J(o),J(n))
s=s.replace("${ILL[pick(b,l)]}","${ILL[pick(b,l)].split('__LOGO__').join(RXL)}",1)
assert 'RXL)' in s
s=s.replace("const LOCK='","const RXL='"+LOGO+"';const LOCK='",1)
open(F, 'w').write(s)
print('ok')
