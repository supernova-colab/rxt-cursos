# Cursos todos distintos: barra nueva, recep-pro reestructurado, rec sin duplicados, intro por curso
import sys, json, importlib
sys.path.insert(0, 'cursos')
h = open('index.html').read()

def build(m):
    M = importlib.import_module(m)
    for b in M.BLOCKS:
        for t in b['quiz']:
            assert sum(1 for q in M.QS if q[0] == t) >= 2, (m, t)
    for q in M.QS:
        assert any(q[0] in b['quiz'] for b in M.BLOCKS), (m, q[0])
    return {'id': M.ID, 'puestos': M.PUESTOS, 'title': M.TITLE, 'short': M.SHORT, 'code': M.CODE,
            'full': M.FULL, 'd': M.DESC, 'B': M.BLOCKS, 'Q': M.QS}

lines = h.split('\n')
def put(c):
    for i, ln in enumerate(lines):
        if ln.startswith('const NEWC='):
            arr = json.loads(ln[len('const NEWC='):-1])
            for k, x in enumerate(arr):
                if x['id'] == c['id']:
                    arr[k] = c; lines[i] = 'const NEWC=' + json.dumps(arr, ensure_ascii=False) + ';'; return
        if ln.startswith('NEWC.push(') and json.loads(ln[10:-2])['id'] == c['id']:
            lines[i] = 'NEWC.push(' + json.dumps(c, ensure_ascii=False) + ');'; return
    j = next(i for i, ln in enumerate(lines) if ln.startswith('NEWC.forEach('))
    lines.insert(j, 'NEWC.push(' + json.dumps(c, ensure_ascii=False) + ');')

for m in ['c_recep2', 'c_barra', 'c_tecnica', 'c_nutri', 'c_ventas']:
    put(build(m))
h = '\n'.join(lines)

# lema distinto para coach
a = '<b>Lema:</b> “No se trata de entrenar más. Se trata de entrenar mejor.”'
i = h.index('const BC=')
k = h.index(a, i)
h = h[:k] + '<b>Lema del coach RXT:</b> calidad antes que cantidad; cada repetición bien hecha cuenta.' + h[k+len(a):]

# rec sin barra, sin cobro/cashback (van en otros cursos) y sin seguimiento (curso de mensajes)
_k=h.index('const QB=');old_bb = h[h.index('const BB=(()=>'):h.index('\n',_k)+1]
new_bb = """const BRX=(()=>{const drop=new Set(['Seguimiento: el cliente que no contestó','Cobro, formas de pago y caja','Cashback y recordatorios de pago']);
  const out=BR.filter((b,i)=>i!==8&&i!==9).map(b=>{const x=_cl(b);x.lessons=x.lessons.filter(l=>!drop.has(l[0]));return x});
  out.forEach((b,i)=>{if(i)b.t='Bloque '+i});
  const q=out[out.length-1];q.n='Quejas';q.d='Cómo convertir una queja en un cliente fiel.';q.quiz=q.quiz.filter(t=>t==='Quejas');
  const b4=out[4];b4.quiz=b4.quiz.filter(t=>t!=='Seguimiento');return out})();
const QRX=(()=>{const tp=new Set();BRX.forEach(b=>b.quiz.forEach(t=>tp.add(t)));return QR.filter(q=>tp.has(q[0]))})();
"""
h = h.replace(old_bb, new_bb)
a = "{id:'rec',puestos:['rec'],title:'Atención en recepción',short:'Recepción',code:'R',full:'Curso de atención en recepción',B:BR,Q:QR,d:'Primer contacto, informes, WhatsApp, operación diaria, app RXT, barra, caja y quejas.'},"
k=h.index("{id:'rec',puestos:['rec'],title:");e=h.index('\n',k)
h=h[:k]+"{id:'rec',puestos:['rec'],title:'Atención en recepción',short:'Recepción',code:'R',full:'Curso de atención en recepción',B:BRX,Q:QRX,d:'Actitud, primer contacto, informes en persona y por WhatsApp, operación diaria, app RXT y quejas.'},"+h[e:]
import re
m = re.search(r"\n \{id:'barista'[^\n]*\n", h); assert m
h = h.replace(m.group(0), '\n')

# "Cómo funciona este curso" distinto en cada curso
a = "const CUR=()=>"
h = h.replace(a, """COURSES.forEach(c=>c.B.forEach(b=>b.lessons.forEach((l,i)=>{if(l[0]!=='Cómo funciona este curso')return;
  const bl=c.B.slice(1);const L2=_cl(l);L2[1]=`${c.title}: ${bl.length} bloques, un mini examen en cada uno y el examen final.`;
  L2[2]=[`Vas a ver, en este orden: ${bl.map((x,j)=>'<b>'+(j+1)+'.</b> '+x.n).join(' · ')}.`,...l[2].slice(1)];b.lessons[i]=L2})));
"""+a, 1)
open('index.html', 'w').write(h)
print('ok')
