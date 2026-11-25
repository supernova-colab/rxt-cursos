"""Agrega los cursos nuevos (carpeta cursos/) al catálogo y el fondo tipo lava rojo/azul."""
import sys, json, re, time, importlib
sys.path.insert(0, 'cursos')
F = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
s = open(F).read()
assert 'const NEWC=' not in s, 'ya parcheado'

MODS = ['c_recep', 'c_ventas', 'c_calent', 'c_tecnica', 'c_hyrox', 'c_rehab']
newc = []
for m in MODS:
    M = importlib.import_module(m)
    # validar
    topics = set(q[0] for q in M.QS)
    for b in M.BLOCKS:
        for t in b['quiz']:
            n = sum(1 for q in M.QS if q[0] == t)
            assert n >= 2, (m, t, n)
        for l in b['lessons']:
            assert len(l) == 4 and isinstance(l[2], list) and len(l[3]) == 2, (m, l[0])
    for q in M.QS:
        assert any(q[0] in b['quiz'] for b in M.BLOCKS), (m, q[0])
    newc.append({'id': M.ID, 'puestos': M.PUESTOS, 'title': M.TITLE, 'short': M.SHORT, 'code': M.CODE,
                 'full': M.FULL, 'd': M.DESC, 'B': M.BLOCKS, 'Q': M.QS})
    print(m, len(M.BLOCKS), 'bloques', sum(len(b['lessons']) for b in M.BLOCKS), 'lecciones', len(M.QS), 'preguntas')

js = 'const NEWC=' + json.dumps(newc, ensure_ascii=False) + ';\n'

def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (old[:90], s.count(old))
    s = s.replace(old, new)

rep('// ===== Catálogo de cursos =====', js + '// ===== Catálogo de cursos =====')
rep("const SOON={rec:['Ventas y seguimiento avanzado'],barista:['Recetario de la Energy Bar'],coach:['HYROX y entrenamiento híbrido','Rehabilitación y lesiones']};",
    "NEWC.forEach(c=>COURSES.push(c));\n"
    "const ORDER=['rec','recep-pro','barista','ventas-barra','coach','calent','tecnica14','hyrox','rehab'];COURSES.sort((a,b)=>ORDER.indexOf(a.id)-ORDER.indexOf(b.id));\n"
    "const SOON={rec:['Ventas y seguimiento avanzado'],barista:['Recetario de la Energy Bar'],coach:['Entrenamiento femenino y ciclo hormonal','Nutrición y suplementación']};")

# --- fondo lava rojo / azul ---
CSS = """
/* ===== FX6: fondo lava ===== */
.lava{position:fixed;inset:0;z-index:-1;overflow:hidden;pointer-events:none;background:var(--bg)}
.lava i{position:absolute;border-radius:50%;filter:blur(70px);opacity:.38;mix-blend-mode:multiply;will-change:transform}
.lava i:nth-child(1){width:62vmax;height:62vmax;left:-18vmax;top:-20vmax;background:radial-gradient(circle at 40% 40%,#ff3b47,#c2121c 70%);animation:lv1 26s ease-in-out infinite alternate}
.lava i:nth-child(2){width:55vmax;height:55vmax;right:-20vmax;top:10vmax;background:radial-gradient(circle at 50% 50%,#3d6bff,#1530a8 70%);animation:lv2 30s ease-in-out infinite alternate}
.lava i:nth-child(3){width:48vmax;height:48vmax;left:10vmax;bottom:-24vmax;background:radial-gradient(circle at 50% 50%,#7b2cff,#2a49d8 70%);animation:lv3 34s ease-in-out infinite alternate;opacity:.28}
.lava i:nth-child(4){width:36vmax;height:36vmax;right:0;bottom:-6vmax;background:radial-gradient(circle,#ff5a64,#E3242F 70%);animation:lv4 22s ease-in-out infinite alternate;opacity:.3}
@keyframes lv1{0%{transform:translate(0,0) scale(1)}50%{transform:translate(18vmax,14vmax) scale(1.15)}100%{transform:translate(6vmax,30vmax) scale(.9)}}
@keyframes lv2{0%{transform:translate(0,0) scale(1)}50%{transform:translate(-20vmax,10vmax) scale(.9)}100%{transform:translate(-8vmax,-12vmax) scale(1.2)}}
@keyframes lv3{0%{transform:translate(0,0) scale(1)}50%{transform:translate(16vmax,-14vmax) scale(1.2)}100%{transform:translate(-10vmax,-6vmax) scale(.95)}}
@keyframes lv4{0%{transform:translate(0,0) scale(1)}100%{transform:translate(-26vmax,-30vmax) scale(1.3)}}
@media (prefers-color-scheme:dark){.lava i{mix-blend-mode:screen;opacity:.33}}
@media (prefers-reduced-motion:reduce){.lava i{animation:none}}
body{background:transparent!important}
main .card,.blk{backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
"""
rep('</style></head>', CSS + '</style></head>')
s = re.sub(r'<body([^>]*)>', r'<body\1><div class="lava" aria-hidden="true"><i></i><i></i><i></i><i></i></div>', s, count=1)
s = re.sub(r'name="rxt-ver" content="\d+"', 'name="rxt-ver" content="' + time.strftime('%Y%m%d%H%M') + '"', s, count=1)
open(F, 'w').write(s)
print('ok', len(s))
