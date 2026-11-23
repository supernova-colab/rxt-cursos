"""PDF de resultado, examen más difícil y aprobación con 90%."""
import sys, time, re
F = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
s = open(F).read()
assert 'FX.pdf' not in s, 'ya parcheado'

def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (old[:90], s.count(old))
    s = s.replace(old, new)

PDFJS = r"""pdf:(d)=>{try{
  const W=1240,H=1754,M=90,CW=W-2*M;const pages=[];let c,x,y;
  const FONT='-apple-system,"SF Pro Text","Inter",system-ui,sans-serif';
  const font=(w,sz)=>x.font=`${w} ${sz}px ${FONT}`;
  const wrap=(t,sz,w,col,lh,mw)=>{font(w,sz);x.fillStyle=col;const words=String(t).replace(/<[^>]+>/g,'').split(/\s+/);let line='';const out=[];
    for(const wd of words){const tt=line?line+' '+wd:wd;if(x.measureText(tt).width>mw&&line){out.push(line);line=wd}else line=tt}if(line)out.push(line);return out};
  const logo=document.querySelector('header img');
  const newPage=()=>{c=document.createElement('canvas');c.width=W;c.height=H;x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,W,H);
    x.fillStyle='#121115';x.fillRect(0,0,W,150);x.fillStyle='#E3242F';x.fillRect(0,150,W,8);
    try{if(logo&&logo.naturalWidth){const h=56,w=logo.naturalWidth*h/logo.naturalHeight;x.drawImage(logo,M,47,w,h)}}catch(e){}
    font('700',24);x.fillStyle='#ffffff';x.textAlign='right';x.fillText('REPORTE DE EVALUACIÓN',W-M,72);font('500',20);x.fillStyle='#bbbbbb';x.fillText('Academia RXT · Roxet Training Club',W-M,104);x.textAlign='left';
    pages.push(c);y=220};
  const foot=()=>pages.forEach((p,i)=>{const g=p.getContext('2d');g.font=`500 18px ${FONT}`;g.fillStyle='#8a8a8a';g.textAlign='left';g.fillText('Roxet Training Club · Coatepec, Ver.',M,H-50);g.textAlign='right';g.fillText(`Página ${i+1} de ${pages.length}`,W-M,H-50)});
  const ensure=h=>{if(y+h>H-110)newPage()};
  newPage();
  // encabezado
  font('600',22);x.fillStyle='#E3242F';x.fillText(d.course.toUpperCase(),M,y);y+=56;
  for(const l of wrap(d.name,52,'800','#121115',0,CW)){font('800',52);x.fillStyle='#121115';x.fillText(l,M,y);y+=60}
  font('500',24);x.fillStyle='#5d5a60';x.fillText(`Fecha: ${d.date}${d.folio?'   ·   Folio: '+d.folio:''}`,M,y+4);y+=50;
  // tarjeta de resultado
  const col=d.pass?'#1F8A5B':'#E3242F',bg=d.pass?'#e9f5ee':'#fbedee';
  x.fillStyle=bg;x.beginPath();x.roundRect(M,y,CW,230,28);x.fill();
  font('900',120);x.fillStyle=col;x.fillText(d.pct+'%',M+40,y+150);
  font('800',36);x.fillText(d.pass?'APROBADO':'NO APROBADO',M+430,y+95);
  font('500',26);x.fillStyle='#121115';x.fillText(`${d.ok} de ${d.total} respuestas correctas`,M+430,y+140);
  x.fillStyle='#5d5a60';x.fillText('Calificación mínima: 90%',M+430,y+180);y+=280;
  if(d.bad.length){font('700',26);x.fillStyle='#121115';x.fillText('Temas para repasar',M,y);y+=40;
    for(const l of wrap(d.bad.join(' · '),24,'500','#5d5a60',0,CW)){font('500',24);x.fillStyle='#5d5a60';x.fillText(l,M,y);y+=34}y+=20}
  // detalle
  font('800',32);x.fillStyle='#121115';x.fillText('Detalle de respuestas',M,y+10);y+=40;x.fillStyle='#e2ddd8';x.fillRect(M,y,CW,3);y+=40;
  d.items.forEach((it,i)=>{const ql=wrap(it.q,25,'700','#121115',0,CW-80),al=wrap((it.ok?'✓ ':'✗ ')+'Su respuesta: '+it.a,22,'500',it.ok?'#1F8A5B':'#E3242F',0,CW-80),
    cl=it.ok?[]:wrap('Respuesta correcta: '+it.c,22,'600','#1F8A5B',0,CW-80);const h=34+ql.length*34+al.length*30+cl.length*30+28;ensure(h);
    x.fillStyle=it.ok?'#1F8A5B':'#E3242F';x.beginPath();x.arc(M+24,y+8,24,0,7);x.fill();font('800',20);x.fillStyle='#fff';x.textAlign='center';x.fillText(i+1,M+24,y+15);x.textAlign='left';
    font('600',18);x.fillStyle='#8a8a8a';x.fillText(it.t.toUpperCase(),M+80,y+2);y+=34;
    for(const l of ql){font('700',25);x.fillStyle='#121115';x.fillText(l,M+80,y);y+=34}
    for(const l of al){font('500',22);x.fillStyle=it.ok?'#1F8A5B':'#E3242F';x.fillText(l,M+80,y);y+=30}
    for(const l of cl){font('600',22);x.fillStyle='#1F8A5B';x.fillText(l,M+80,y);y+=30}
    y+=10;x.fillStyle='#eeeae6';x.fillRect(M+80,y,CW-80,2);y+=24});
  ensure(200);y+=30;x.fillStyle='#121115';x.fillRect(M,y+60,360,2);x.fillRect(W-M-360,y+60,360,2);font('500',20);x.fillStyle='#5d5a60';x.fillText('Firma del colaborador',M,y+90);x.textAlign='right';x.fillText('Firma de quien revisa',W-M,y+90);x.textAlign='left';
  foot();
  // armar PDF (una imagen JPEG por página)
  const E=new TextEncoder(),parts=[],offs=[];let len=0;const push=b=>{if(typeof b==='string')b=E.encode(b);parts.push(b);len+=b.length};
  const obj=(n,body)=>{offs[n]=len;push(n+' 0 obj\n');(Array.isArray(body)?body:[body]).forEach(push);push('\nendobj\n')};
  push('%PDF-1.4\n');const N=pages.length;const kids=pages.map((_,i)=>(3+3*i)+' 0 R').join(' ');
  obj(1,'<< /Type /Catalog /Pages 2 0 R >>');obj(2,`<< /Type /Pages /Kids [${kids}] /Count ${N} >>`);
  pages.forEach((p,i)=>{const b=atob(p.toDataURL('image/jpeg',.86).split(',')[1]),jp=new Uint8Array(b.length);for(let k=0;k<b.length;k++)jp[k]=b.charCodeAt(k);
    const pn=3+3*i,im=pn+1,cn=pn+2,cs='q 595.28 0 0 841.89 0 0 cm /Im0 Do Q';
    obj(pn,`<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595.28 841.89] /Resources << /XObject << /Im0 ${im} 0 R >> >> /Contents ${cn} 0 R >>`);
    obj(im,[`<< /Type /XObject /Subtype /Image /Width ${W} /Height ${H} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length ${jp.length} >>\nstream\n`,jp,'\nendstream']);
    obj(cn,`<< /Length ${cs.length} >>\nstream\n${cs}\nendstream`)});
  const xr=len,tot=3+3*N;let t=`xref\n0 ${tot}\n0000000000 65535 f \n`;for(let n=1;n<tot;n++)t+=String(offs[n]).padStart(10,'0')+' 00000 n \n';
  push(t+`trailer\n<< /Size ${tot} /Root 1 0 R >>\nstartxref\n${xr}\n%%EOF`);
  const name=('Resultado-RXT-'+d.name).normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[^\w-]+/g,'-')+'.pdf';
  const blob=new Blob(parts,{type:'application/pdf'}),file=new File([blob],name,{type:'application/pdf'});
  if(navigator.canShare&&navigator.canShare({files:[file]})){navigator.share({files:[file],title:'Resultado Academia RXT'}).catch(()=>{});return}
  const u=URL.createObjectURL(blob),a=document.createElement('a');a.href=u;a.download=name;document.body.appendChild(a);a.click();setTimeout(()=>{a.remove();URL.revokeObjectURL(u)},4000);
 }catch(e){alert('No se pudo crear el PDF: '+e.message)}},
 """
rep(" cert:()=>{setTimeout(", " " + PDFJS + "cert:()=>{setTimeout(")
# 90 %
rep("pass=pct>=80", "pass=pct>=90")
rep("'Necesitas 80%. '", "'Necesitas 90%. '")
rep("Se aprueba con 80%.", "Se aprueba con 90%.")
rep("Necesitas <b>80%</b> para aprobar", "Necesitas <b>90%</b> para aprobar")
# examen final más largo
rep("shuffle(items).slice(0,40)", "shuffle(items).slice(0,50)")
rep("${Math.min(40,Q.length)} preguntas", "${Math.min(50,Q.length)} preguntas")
# sin retroalimentación inmediata ni racha en mini exámenes
rep("shown=!fin&&a!==undefined", "shown=false")
rep("window.FXQ=fin?'sel':(ans[p]===q[3]?'good':'bad');", "window.FXQ='sel';")
rep("${fin?'':FX.streak(list.map(i=>Q[i][3]),ans,p)}", "")
# guardar respuestas del final y botón PDF
rep("timeStyle:'short'}),bad};save()}", "timeStyle:'short'}),bad,qs:list,an:ans.map(x=>x===undefined?null:x)};save()}")
rep("<div class=\"row\">${fin&&pass?'<button class=\"btn\" id=\"dc\">Ver mi constancia</button>':''}",
    "<div class=\"row\">${fin?'<button class=\"btn\" id=\"pdf\">📄 Enviar PDF del resultado</button>':''}${fin&&pass?'<button class=\"btn ghost\" id=\"dc\">Ver mi certificado</button>':''}")
rep("$('bk').onclick=map;FX.result(pct,pass);", "$('bk').onclick=map;if($('pdf'))$('pdf').onclick=()=>FX.pdf(report());FX.result(pct,pass);")
rep("const URL0=", """const report=()=>{const f=S.final;if(f.pass&&!f.folio){f.folio='RXT-'+(ROLE==='coach'?'C':'R')+'-'+Date.now().toString(36).toUpperCase().slice(-6);save()}
  return{name:S.name,course:RN[ROLE],date:f.date,pct:f.pct,ok:f.ok,total:f.total,pass:f.pass,folio:f.folio||'',bad:f.bad||[],
  items:(f.qs||[]).map((qi,x)=>{const q=Q[qi];if(!q)return null;const a=f.an?f.an[x]:null;return{t:q[0],q:q[1],a:a===null||a===undefined?'Sin respuesta':q[2][a],c:q[2][q[3]],ok:a===q[3]}}).filter(Boolean)}};
const URL0=""")
rep("<button class=\"btn ghost\" id=\"cpl\">Copiar link del certificado</button>",
    "<button class=\"btn ghost\" id=\"cpdf\">📄 PDF del resultado</button><button class=\"btn ghost\" id=\"cpl\">Copiar link del certificado</button>")
rep("$('cb').onclick=map;$('cpl').onclick", "$('cb').onclick=map;$('cpdf').onclick=()=>FX.pdf(report());$('cpl').onclick")

# --- examen final más difícil: 45 s por pregunta, sin regresar ---
rep("</style></head>", ".tmr{display:flex;align-items:center;gap:10px;margin:0 0 14px}.tmr div{flex:1;height:8px;border-radius:8px;background:var(--line);overflow:hidden}.tmr i{display:block;height:100%;background:var(--ink);transition:width 1s linear,background .3s}.tmr span{font:800 14px Inter;min-width:44px;text-align:right}</style></head>")
rep("function r(){keep();", "function r(){clearInterval(window.__qt);keep();")
rep("function done(){S.qs=null;", "function done(){clearInterval(window.__qt);S.qs=null;")
rep("${p?'<button class=\"btn ghost\" id=\"qb\">Anterior</button>':''}", "${p&&!fin?'<button class=\"btn ghost\" id=\"qb\">Anterior</button>':''}")
rep("<p class=\"q\">${q[1]}</p>", "${fin?'<div class=\"tmr\"><div><i id=\"tmb\"></i></div><span id=\"tmt\">45 s</span></div>':''}<p class=\"q\">${q[1]}</p>")
rep("FX.quiz(window.FXQ);window.FXQ=null;", "FX.quiz(window.FXQ);window.FXQ=null;if(fin&&ans[p]===undefined){let tl=45;const tb=$('tmb'),tt=$('tmt');const tick=()=>{tt.textContent=tl+' s';tb.style.width=(tl/45*100)+'%';tb.style.background=tl<=10?'var(--red)':'var(--ink)'};tick();window.__qt=setInterval(()=>{tl--;tick();if(tl<=0){clearInterval(window.__qt);if(ans[p]===undefined)ans[p]=-1;try{navigator.vibrate&&navigator.vibrate(80)}catch(e){}if(p<list.length-1){p++;r()}else done()}},1000)}else if(fin){$('tmt').textContent='✓';$('tmb').style.width='100%'}")
rep("a===null||a===undefined?'Sin respuesta'", "a===null||a===undefined||a<0?'Sin respuesta (se acabó el tiempo)'")
rep("<li>Si no apruebas, puedes repasar y volver a intentarlo.</li>", "${fin?'<li><b>50 preguntas</b> al azar, <b>45 segundos</b> por pregunta y sin regresar a la anterior. Si se acaba el tiempo, cuenta como incorrecta.</li>':''}<li>Si no apruebas, puedes repasar y volver a intentarlo.</li>")
s = re.sub(r'name="rxt-ver" content="\d+"', 'name="rxt-ver" content="' + time.strftime('%Y%m%d%H%M') + '"', s, count=1)
open(F, 'w').write(s)
print('ok')
