"""Agrega animaciones, ilustraciones e interacción a la Academia RXT (index.html)."""
import sys
F = sys.argv[1] if len(sys.argv) > 1 else 'index.html'
s = open(F).read()
assert 'id="fxjs"' not in s, 'ya parcheado'

CSS = r"""
/* ===== FX: animación e interacción ===== */
@keyframes vin{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
@keyframes lin{from{opacity:0;transform:translateX(-14px)}to{opacity:1;transform:none}}
@keyframes ipop{0%,100%{transform:scale(1)}12%{transform:scale(1.12)}24%{transform:scale(1)}}
@keyframes ibob{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes ispin{to{transform:rotate(360deg)}}
@keyframes iwave{0%,60%,100%{transform:rotate(0)}10%,30%,50%{transform:rotate(-22deg)}20%,40%{transform:rotate(10deg)}}
@keyframes ifade{0%,100%{opacity:.15}50%{opacity:1}}
@keyframes iup{0%{opacity:0;transform:translateY(10px) scale(.6)}20%{opacity:1}100%{opacity:0;transform:translateY(-46px) scale(1)}}
@keyframes idraw{0%{stroke-dashoffset:var(--L)}35%,85%{stroke-dashoffset:0}100%{stroke-dashoffset:0;opacity:0}}
@keyframes iin{0%,8%{opacity:0;transform:translateY(8px) scale(.7)}18%,88%{opacity:1;transform:none}100%{opacity:0}}
@keyframes imA{0%,42%{opacity:1}50%,92%{opacity:0}100%{opacity:1}}@keyframes imB{0%,42%{opacity:0}50%,92%{opacity:1}100%{opacity:0}}
@keyframes ilift{0%,100%{transform:translateY(16px)}45%,60%{transform:translateY(-14px)}}
@keyframes idrop{0%{opacity:0;transform:translateY(-40px)}15%{opacity:1}55%,100%{opacity:0;transform:translateY(22px)}}
@keyframes itap{0%,100%{transform:translate(14px,18px)}40%,55%{transform:translate(0,0) scale(.92)}}
@keyframes ibeat{0%,40%,100%{transform:scale(1)}10%,30%{transform:scale(1.14)}20%{transform:scale(1.04)}}
@keyframes shake{10%,90%{transform:translateX(-2px)}20%,80%{transform:translateX(4px)}30%,50%,70%{transform:translateX(-7px)}40%,60%{transform:translateX(7px)}}
@keyframes bump{0%{transform:scale(.6);opacity:0}60%{transform:scale(1.15);opacity:1}100%{transform:scale(1)}}
@keyframes glow{0%,100%{box-shadow:0 0 0 0 color-mix(in srgb,var(--red) 45%,transparent)}50%{box-shadow:0 0 0 8px transparent}}
@keyframes stamp{0%{opacity:0;transform:rotate(14deg) scale(2.4)}60%{opacity:1;transform:rotate(14deg) scale(.92)}100%{transform:rotate(14deg) scale(1)}}
.fxv{animation:vin .45s cubic-bezier(.2,.8,.2,1) both}
.ill{position:relative;height:160px;margin:-6px -6px 18px;border-radius:18px;overflow:hidden;
 background:radial-gradient(circle at 1px 1px,color-mix(in srgb,var(--ink) 14%,transparent) 1px,transparent 1.5px) 0 0/16px 16px,color-mix(in srgb,var(--red) 7%,var(--bg))}
.ill svg{position:absolute;inset:0;width:100%;height:100%}
.ill .k{fill:none;stroke:var(--ink);stroke-width:4;stroke-linecap:round;stroke-linejoin:round}
.ill .r{fill:var(--red)}.ill .rk{fill:none;stroke:var(--red);stroke-width:4;stroke-linecap:round;stroke-linejoin:round}
.ill .w{fill:var(--card)}.ill .s{fill:color-mix(in srgb,var(--ink) 18%,transparent)}.ill .ok{fill:var(--ok)}
.ill .t{font:800 15px "Inter Tight",Inter,sans-serif;fill:var(--ink)}.ill .tw{font:800 13px Inter;fill:#fff}
.ill *{transform-box:fill-box;transform-origin:center}
.a-pop{animation:ipop 2.6s infinite}.a-bob{animation:ibob 2.4s ease-in-out infinite}.a-spin{animation:ispin 6s linear infinite}.a-spinf{animation:ispin 1.2s linear infinite}
.a-in{animation:iin 4s infinite both}.a-fade{animation:ifade 1.4s infinite}.a-up{animation:iup 2.8s ease-out infinite both}
.a-draw{stroke-dasharray:var(--L);animation:idraw 3.6s ease-in-out infinite both}.a-lift{animation:ilift 2.2s ease-in-out infinite}
.a-drop{animation:idrop 2.2s ease-in infinite both}.a-beat{animation:ibeat 1.3s infinite}.a-tap{animation:itap 2s ease-in-out infinite}
.a-wave{animation:iwave 2.4s ease-in-out infinite;transform-box:view-box!important}
.d1{animation-delay:.4s!important}.d2{animation-delay:.8s!important}.d3{animation-delay:1.2s!important}.d4{animation-delay:1.6s!important}.d5{animation-delay:2s!important}
.hint{font:600 13px Inter;color:var(--soft);margin:14px 0 0}
ol.pp li{animation:lin .45s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--i)*90ms + .15s);cursor:pointer;border-radius:10px;transition:background .25s;-webkit-tap-highlight-color:transparent}
ol.pp li::before{transition:background .25s,color .25s,transform .25s}
ol.pp li.chk::before{content:"✓";background:var(--ok);border-color:var(--ok);color:#fff;animation:bump .4s both}
ol.pp li.chk>span{opacity:.75}
.vs .flip{all:unset;box-sizing:border-box;position:relative;border-radius:14px;padding:12px 14px;font-size:15px;line-height:1.6;cursor:pointer;background:var(--okbg);border:1.5px solid color-mix(in srgb,var(--ok) 40%,transparent);overflow:hidden;min-height:120px;-webkit-tap-highlight-color:transparent}
.vs .flip strong{display:block;font:800 12px Inter;margin-bottom:4px;color:var(--ok)}
.vs .flip .fr{display:block;transition:opacity .35s .1s,filter .35s .1s;opacity:0;filter:blur(6px)}
.vs .flip .cv{position:absolute;inset:0;display:grid;place-items:center;text-align:center;font:700 14px/1.35 Inter;color:#fff;background:var(--ok);transition:transform .5s cubic-bezier(.7,0,.3,1)}
.vs .flip .cv b{display:block;font-size:30px;animation:ibob 1.4s ease-in-out infinite}
.vs .flip.open .fr{opacity:1;filter:none}.vs .flip.open .cv{transform:translateY(-102%)}
.vs .m{animation:vin .45s .3s both}
.streak{display:inline-flex;align-items:center;gap:6px;margin-left:8px;padding:3px 10px;border-radius:999px;background:color-mix(in srgb,var(--red) 14%,transparent);color:var(--red);font:800 12px Inter;animation:bump .4s both}
.opt{transition:transform .15s,border-color .2s,background .2s}.opt:active{transform:scale(.98)}
.opt.fxs{animation:bump .3s}.opt.bad.fxs{animation:shake .5s}.opt.good.fxs{animation:bump .45s}
.fb{animation:vin .35s both}
.ring{position:relative;width:170px;height:170px;margin:4px 0 10px}.ring svg{width:100%;height:100%;transform:rotate(-90deg)}
.ring .rt{position:absolute;inset:0;display:grid;place-items:center;font:900 44px "Inter Tight",Inter,sans-serif}
.ring .rt small{display:block;font:700 12px Inter;color:var(--soft);text-align:center;margin-top:-6px}
.emj{font-size:42px;display:inline-block;animation:bump .6s .9s both}
.map .blk{animation:vin .45s cubic-bezier(.2,.8,.2,1) both;animation-delay:calc(var(--i)*60ms)}
.map .blk.next{border-color:color-mix(in srgb,var(--red) 55%,transparent)}.map .blk.next .st{background:var(--red);color:#fff;animation:glow 1.8s infinite}
.map .blk.done .n{animation:bump .5s both;animation-delay:calc(var(--i)*60ms + .2s)}
.bar i{transition:width .9s cubic-bezier(.2,.8,.2,1)}
.certi .seal{animation:stamp .7s .5s both}
#fxc{position:fixed;inset:0;width:100vw;height:100vh;pointer-events:none;z-index:9999}
@media (prefers-reduced-motion:reduce){.ill *,ol.pp li,.map .blk,.fxv,.streak,.emj,.certi .seal{animation:none!important}}
"""

ILL = {
 'chat': '''<rect class="k w" x="118" y="12" width="84" height="136" rx="16"/><rect class="s" x="146" y="20" width="28" height="5" rx="3"/>
<g class="a-in"><rect class="s" x="128" y="38" width="50" height="18" rx="9"/></g>
<g class="a-in d1"><rect class="r" x="142" y="62" width="50" height="18" rx="9"/></g>
<g class="a-in d2"><rect class="s" x="128" y="86" width="38" height="18" rx="9"/><circle class="k" cx="139" cy="95" r="1"/><circle class="k a-fade" cx="147" cy="95" r="1"/><circle class="k a-fade d1" cx="155" cy="95" r="1"/></g>
<g class="a-pop"><circle class="r" cx="202" cy="16" r="13"/><text class="tw" x="202" y="21" text-anchor="middle">3</text></g>
<g class="a-bob"><path class="rk" d="M58 70c0-14 12-24 26-24s26 10 26 24-12 24-26 24c-4 0-8-1-11-2l-12 5 4-10c-4-5-7-10-7-17z"/><circle class="r" cx="74" cy="70" r="3"/><circle class="r" cx="84" cy="70" r="3"/><circle class="r" cx="94" cy="70" r="3"/></g>
<g class="a-bob d2"><path class="k" d="M228 98h46a10 10 0 0 1 10 10v8a10 10 0 0 1-10 10h-30l-12 8 2-8a10 10 0 0 1-6-10v-8a10 10 0 0 1 10-10z"/><text class="t" x="252" y="118" text-anchor="middle">👍</text></g>''',
 'hello': '''<circle class="k w" cx="130" cy="44" r="18"/><circle class="r" cx="124" cy="42" r="2.5"/><circle class="r" cx="136" cy="42" r="2.5"/><path class="rk" d="M123 51q7 6 14 0"/>
<path class="k" d="M130 62v44M130 106l-14 34M130 106l14 34M130 74l-22 22"/>
<g class="a-wave" style="transform-origin:130px 74px"><path class="k" d="M130 74l26-24"/><circle class="k w" cx="159" cy="47" r="6"/></g>
<g class="a-in d1"><path class="k w" d="M182 20h86a12 12 0 0 1 12 12v18a12 12 0 0 1-12 12h-60l-16 12 4-12h-14a12 12 0 0 1-12-12V32a12 12 0 0 1 12-12z"/><text class="t" x="225" y="47" text-anchor="middle">¡Hola! 👋</text></g>
<g class="a-up d2"><path class="r" d="M246 112c-5-6-14-1-10 6l10 10 10-10c4-7-5-12-10-6z"/></g>
<g class="a-up d4"><path class="r" d="M216 124c-4-5-11-1-8 5l8 8 8-8c3-6-4-10-8-5z"/></g>''',
 'app': '''<rect class="k w" x="112" y="10" width="96" height="140" rx="18"/>
<rect class="s" x="126" y="32" width="18" height="18" rx="5"/><rect class="s" x="151" y="32" width="18" height="18" rx="5"/><rect class="s" x="176" y="32" width="18" height="18" rx="5"/>
<rect class="s" x="126" y="58" width="18" height="18" rx="5"/><rect class="s" x="151" y="58" width="18" height="18" rx="5"/>
<g class="a-pop d2"><rect class="r" x="176" y="58" width="18" height="18" rx="5"/><text class="tw" x="185" y="72" text-anchor="middle" style="font-size:9px">RXT</text></g>
<rect class="s" x="126" y="84" width="18" height="18" rx="5"/><rect class="s" x="151" y="84" width="18" height="18" rx="5"/>
<g class="a-tap"><text x="182" y="112" style="font-size:38px">👆</text></g>
<g class="a-up"><text x="236" y="70" style="font-size:22px">✨</text></g><g class="a-up d3"><text x="62" y="90" style="font-size:22px">📲</text></g>''',
 'drink': '''<path class="k w" d="M128 46h64l-8 92q-24 8-48 0z"/><path class="r" d="M131 76q15-7 29 0t29 0l-6 61q-23 7-46 0z" opacity=".85"/>
<path class="k" d="M168 46l14-34h20"/><rect class="k" x="122" y="38" width="76" height="10" rx="5"/>
<g class="a-bob"><rect class="k w" x="140" y="86" width="14" height="14" rx="3"/></g><g class="a-bob d2"><rect class="k w" x="164" y="96" width="12" height="12" rx="3"/></g>
<circle class="w a-up" cx="150" cy="124" r="3"/><circle class="w a-up d2" cx="172" cy="126" r="2.5"/><circle class="w a-up d4" cx="160" cy="128" r="2"/>
<g class="a-up d1"><text x="226" y="96" style="font-size:24px">💧</text></g><g class="a-up d3"><text x="74" y="104" style="font-size:24px">💪</text></g>''',
 'money': '''<rect class="k w" x="104" y="66" width="112" height="72" rx="12"/><rect class="s" x="120" y="82" width="80" height="22" rx="6"/>
<text class="t" x="160" y="98" text-anchor="middle">$ ✓</text><rect class="k" x="138" y="58" width="44" height="8" rx="4"/>
<g class="a-drop"><circle class="r" cx="160" cy="40" r="12"/><text class="tw" x="160" y="45" text-anchor="middle">$</text></g>
<g class="a-drop d3"><circle class="r" cx="146" cy="36" r="10"/><text class="tw" x="146" y="41" text-anchor="middle" style="font-size:11px">$</text></g>
<g class="a-bob"><rect class="k w" x="236" y="58" width="50" height="34" rx="6"/><rect class="r" x="236" y="66" width="50" height="7"/></g>
<g class="a-bob d2"><text x="46" y="100" style="font-size:28px">🧾</text></g>''',
 'face': '''<circle class="k w" cx="160" cy="78" r="46"/><circle class="r" cx="145" cy="68" r="4"/><circle class="r" cx="175" cy="68" r="4"/>
<path class="rk" d="M142 98q18-14 36 0" style="animation:imA 4s infinite"/><path class="rk" d="M142 92q18 16 36 0" style="animation:imB 4s infinite"/>
<g class="a-up"><path class="r" d="M230 72c-5-6-14-1-10 6l10 10 10-10c4-7-5-12-10-6z"/></g><g class="a-up d3"><path class="r" d="M90 86c-5-6-14-1-10 6l10 10 10-10c4-7-5-12-10-6z"/></g>
<g class="a-bob d1"><text x="236" y="130" style="font-size:22px">🤝</text></g>''',
 'check': '''<rect class="k w" x="108" y="18" width="104" height="128" rx="12"/><rect class="r" x="138" y="10" width="44" height="16" rx="6"/>
<rect class="k" x="124" y="44" width="16" height="16" rx="4"/><path class="s" d="M150 48h46v8h-46z"/><path class="rk a-draw" style="--L:24" d="M127 52l5 5 9-11"/>
<rect class="k" x="124" y="74" width="16" height="16" rx="4"/><path class="s" d="M150 78h40v8h-40z"/><path class="rk a-draw d2" style="--L:24" d="M127 82l5 5 9-11"/>
<rect class="k" x="124" y="104" width="16" height="16" rx="4"/><path class="s" d="M150 108h34v8h-34z"/><path class="rk a-draw d4" style="--L:24" d="M127 112l5 5 9-11"/>
<g class="a-bob"><path class="k" d="M246 120l26-56 10 5-26 56-12 6z"/><path class="r" d="M272 64l10 5 4-8-10-5z"/></g>''',
 'clock': '''<circle class="k w" cx="160" cy="78" r="54"/><circle class="r" cx="160" cy="78" r="5"/>
<path class="k" d="M160 30v8M160 118v8M112 78h8M200 78h8"/>
<g class="a-spin" style="animation-duration:24s;transform-origin:160px 78px;transform-box:view-box"><path class="k" d="M160 78v-26"/></g>
<g class="a-spinf" style="animation-duration:2s;transform-origin:160px 78px;transform-box:view-box"><path class="rk" d="M160 78v-40"/></g>
<g class="a-bob"><text x="232" y="56" style="font-size:24px">⏰</text></g><g class="a-bob d2"><text x="62" y="124" style="font-size:24px">✅</text></g>''',
 'clean': '''<path class="k w" d="M138 66h44v74q-22 8-44 0z"/><rect class="k" x="146" y="44" width="28" height="22" rx="4"/><path class="k" d="M174 50h22l6 8"/>
<rect class="r" x="146" y="88" width="28" height="24" rx="4"/>
<g class="a-in"><text x="208" y="54" style="font-size:22px">✨</text></g><g class="a-in d2"><text x="232" y="88" style="font-size:18px">✨</text></g><g class="a-in d4"><text x="206" y="116" style="font-size:16px">✨</text></g>
<circle class="s a-up" cx="80" cy="110" r="10"/><circle class="s a-up d2" cx="96" cy="120" r="7"/><circle class="s a-up d4" cx="70" cy="126" r="5"/><g class="a-bob d1"><text x="68" y="70" style="font-size:26px">🧼</text></g>''',
 'voice': '''<path class="k w" d="M112 66v24l20 2 44 26V38l-44 26z"/><path class="r" d="M112 66h20v26h-20z"/><path class="k" d="M122 92l6 26h12l-4-24"/>
<path class="rk a-fade" d="M190 62q10 16 0 32"/><path class="rk a-fade d1" d="M204 52q18 26 0 52"/><path class="rk a-fade d2" d="M218 42q26 36 0 72"/>
<g class="a-bob"><text x="238" y="44" style="font-size:22px">🔥</text></g><g class="a-in d2"><text x="244" y="128" class="t">¡Arriba!</text></g>''',
 'likes': '''<rect class="k w" x="110" y="16" width="100" height="126" rx="14"/><circle class="r" cx="128" cy="32" r="7"/><path class="s" d="M140 28h40v8h-40z"/><rect class="s" x="120" y="46" width="80" height="62" rx="8"/>
<text x="160" y="88" text-anchor="middle" style="font-size:26px">🏋️</text><path class="rk" d="M122 124c-3-4-9-1-7 4l7 7 7-7c2-5-4-8-7-4z"/>
<g class="a-up"><path class="r" d="M232 108c-5-6-14-1-10 6l10 10 10-10c4-7-5-12-10-6z"/></g><g class="a-up d2"><path class="r" d="M254 120c-4-5-11-1-8 5l8 8 8-8c3-6-4-10-8-5z"/></g>
<g class="a-up d4"><path class="r" d="M224 126c-4-5-11-1-8 5l8 8 8-8c3-6-4-10-8-5z"/></g><g class="a-bob d1"><text x="62" y="72" style="font-size:26px">📸</text></g>''',
 'pulse': '''<g class="a-beat"><path class="r" d="M160 128c-40-28-58-48-58-70 0-16 12-26 26-26 12 0 22 8 32 18 10-10 20-18 32-18 14 0 26 10 26 26 0 22-18 42-58 70z"/></g>
<path class="k a-draw" style="--L:420;stroke:var(--card);stroke-width:5" d="M104 78h30l8-18 12 36 10-26 6 8h46"/>
<g class="a-bob d2"><text x="248" y="50" style="font-size:22px">🧬</text></g><g class="a-bob"><text x="48" y="120" style="font-size:22px">⚡</text></g>''',
 'moon': '''<path class="k w" d="M178 26a52 52 0 1 0 38 82 44 44 0 0 1-38-82z"/><g class="a-up"><text x="214" y="58" class="t" style="font-size:20px">z</text></g>
<g class="a-up d2"><text x="228" y="44" class="t" style="font-size:16px">z</text></g><g class="a-in"><text x="86" y="44" style="font-size:16px">⭐</text></g>
<g class="a-in d2"><text x="244" y="118" style="font-size:14px">⭐</text></g><g class="a-in d4"><text x="70" y="114" style="font-size:12px">⭐</text></g><g class="a-bob"><text x="126" y="146" style="font-size:22px">🔋</text></g>''',
 'food': '''<ellipse class="k w" cx="160" cy="96" rx="66" ry="40"/><ellipse class="s" cx="160" cy="96" rx="48" ry="26"/>
<g class="a-bob"><circle class="r" cx="142" cy="90" r="13"/></g><g class="a-bob d1"><text x="156" y="104" style="font-size:24px">🥦</text></g><g class="a-bob d2"><text x="176" y="90" style="font-size:20px">🍚</text></g>
<path class="k" d="M76 52v76M68 52v18q8 8 16 0V52M244 52q14 20 0 40v36"/><g class="a-drop"><text x="250" y="40" style="font-size:22px">💧</text></g>''',
 'bulb': '''<g class="a-pop"><path class="w k" d="M160 22a38 38 0 0 0-22 69c5 4 8 10 8 16h28c0-6 3-12 8-16a38 38 0 0 0-22-69z"/><path class="r" d="M150 74l10-20 10 20-10 16z" opacity=".9"/></g>
<rect class="k" x="146" y="112" width="28" height="10" rx="4"/><rect class="k" x="150" y="126" width="20" height="8" rx="4"/>
<path class="rk a-fade" d="M100 60h-14M220 60h14M112 26l-10-10M208 26l10-10"/><g class="a-bob d2"><text x="238" y="128" style="font-size:22px">🧠</text></g><g class="a-bob"><text x="58" y="128" style="font-size:22px">💪</text></g>''',
 'lift': '''<path class="k" d="M110 140h100"/><g class="a-lift"><path class="k" d="M96 66h128"/><rect class="r" x="100" y="46" width="14" height="40" rx="4"/><rect class="r" x="206" y="46" width="14" height="40" rx="4"/>
<rect class="k w" x="116" y="54" width="10" height="24" rx="3"/><rect class="k w" x="194" y="54" width="10" height="24" rx="3"/></g>
<path class="s a-fade" d="M70 70h16M66 84h20M234 70h16M234 84h20"/><g class="a-in d2"><text x="246" y="40" style="font-size:22px">💪</text></g><g class="a-bob"><text x="46" y="44" style="font-size:20px">🏆</text></g>''',
 'star': '''<g class="a-pop"><path class="r" d="M160 22l14 30 32 4-24 22 6 32-28-16-28 16 6-32-24-22 32-4z"/></g>
<text class="tw" x="160" y="80" text-anchor="middle" style="font-size:15px">RXT</text>
<g class="a-in"><text x="86" y="52" style="font-size:20px">✨</text></g><g class="a-in d2"><text x="222" y="50" style="font-size:20px">✨</text></g>
<g class="a-in d4"><text x="230" y="130" style="font-size:16px">🎉</text></g><g class="a-bob"><text x="72" y="132" style="font-size:22px">🤝</text></g>''',
}

JS = r"""<script id="fxjs">
(()=>{const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
const ILL=__ILL__;
const RULES=[[/whatsapp|instagram|respuesta|seguimiento/i,'chat'],[/app de rxt|socio|\bapp\b/i,'app'],[/pol[ií]tica/i,'check'],[/higiene/i,'clean'],
[/barra|servir|recomienda|paquete|hora pico/i,'drink'],[/cobro|caja|cashback|pago/i,'money'],[/queja|presionar|pensar/i,'face'],
[/apuntar|preguntas|filtrar|autoevalu/i,'check'],[/apertura|s[áa]bado|minutos antes|60 min|partes de la clase/i,'clock'],[/voz|frases|cues/i,'voice'],
[/historias|comunidad/i,'likes'],[/sueño|recuperaci|simp[áa]tico/i,'moon'],[/ciclo|estr[óo]geno|menopausia|hormona|suprarrenal|energ[ée]tico/i,'pulse'],
[/nutrici|comer|hidrata|suplemento|recomendar/i,'food'],[/mentalidad|disciplina/i,'bulb'],
[/informes|contacto|nombre|atender|actitud|calidad|recorrido/i,'hello'],
[/fuerza|hipertrofia|biomec|sentadilla|patrones|ejercicio|piso|mirar|seguridad|lubricaci|programaci/i,'lift']];
const pick=(b,l)=>{for(const[r,k]of RULES)if(r.test(l[0]))return k;for(const[r,k]of RULES)if(r.test(b.n))return k;return 'star'};
// confeti
let cv,cx,P=[],run=false;const COL=['#E3242F','#ffffff','#FFC83D','#3cc486','#121115','#ff8a8f'];
function loop(){cx.clearRect(0,0,cv.width,cv.height);const d=devicePixelRatio||1;P=P.filter(p=>p.l>0);
 for(const p of P){p.vy+=0.32;p.vx*=0.985;p.x+=p.vx;p.y+=p.vy;p.r+=p.vr;p.l--;cx.save();cx.globalAlpha=Math.min(1,p.l/30);cx.translate(p.x*d,p.y*d);cx.rotate(p.r);cx.fillStyle=p.c;
 if(p.s)cx.fillRect(-5*d,-3*d,10*d,6*d);else{cx.beginPath();cx.arc(0,0,3.5*d,0,7);cx.fill()}cx.restore()}
 if(P.length)requestAnimationFrame(loop);else{run=false;cx.clearRect(0,0,cv.width,cv.height)}}
function boom(x,y,n=60,sp=9){if(RM)return;if(!cv){cv=document.createElement('canvas');cv.id='fxc';document.body.appendChild(cv);cx=cv.getContext('2d')}
 const d=devicePixelRatio||1;if(cv.width!==innerWidth*d){cv.width=innerWidth*d;cv.height=innerHeight*d}
 for(let i=0;i<n;i++){const a=Math.random()*Math.PI*2,v=sp*(.35+Math.random()*.8);P.push({x,y,vx:Math.cos(a)*v,vy:Math.sin(a)*v-sp*.55,r:Math.random()*6,vr:(Math.random()-.5)*.4,c:COL[i%COL.length],s:Math.random()<.6,l:70+Math.random()*50})}
 if(!run){run=true;requestAnimationFrame(loop)}}
const ctr=el=>{const r=el.getBoundingClientRect();return[r.left+r.width/2,r.top+r.height/2]};
const vib=p=>{try{navigator.vibrate&&navigator.vibrate(p)}catch(e){}};
window.FX={boom,
 ill:(b,l)=>`<div class="ill" aria-hidden="true"><svg viewBox="0 0 320 160" preserveAspectRatio="xMidYMid meet">${ILL[pick(b,l)]}</svg></div>`,
 view:v=>{const e=document.getElementById(v);if(!e)return;e.classList.remove('fxv');void e.offsetWidth;e.classList.add('fxv')},
 lesson:()=>{const root=document.getElementById('vLesson');const lis=[...root.querySelectorAll('ol.pp li')];const nx=document.getElementById('ln');
  lis.forEach(li=>li.onclick=()=>{li.classList.toggle('chk');vib(12);if(lis.every(x=>x.classList.contains('chk'))&&nx){nx.style.animation='glow 1.6s infinite';const[a,b]=ctr(li);boom(a,b,24,6)}});
  const f=root.querySelector('.flip');if(f)f.onclick=()=>{if(f.classList.contains('open'))return;f.classList.add('open');vib(20);const[a,b]=ctr(f);boom(a,b,30,7)}},
 streak:(ok,ans,p)=>{let s=0;for(let i=p-1;i>=0;i--){if(ans[i]===ok[i])s++;else break}if(ans[p]!==undefined&&ans[p]===ok[p])s++;return s>=2?`<span class="streak">🔥 Racha de ${s}</span>`:''},
 quiz:k=>{if(!k)return;const el=document.querySelector('#vQuiz .opt.'+(k==='sel'?'sel':k==='good'?'good':'bad'));if(!el)return;el.classList.add('fxs');
  if(k==='good'){const[a,b]=ctr(el);boom(a,b,40,8);vib(25)}else if(k==='bad')vib([40,50,40]);else vib(10)},
 ring:(pct,pass)=>{const C=2*Math.PI*52;return `<svg viewBox="0 0 120 120"><circle cx="60" cy="60" r="52" fill="none" stroke="var(--line)" stroke-width="10"/><circle id="rgc" cx="60" cy="60" r="52" fill="none" stroke="${pass?'var(--ok)':'var(--red)'}" stroke-width="10" stroke-linecap="round" stroke-dasharray="${C}" stroke-dashoffset="${C}" data-c="${C}" data-p="${pct}" style="transition:stroke-dashoffset 1.3s cubic-bezier(.2,.8,.2,1)"/></svg><div class="rt"><div><span id="rgn">0</span>%<small>${pass?'¡Aprobado!':'Sigue intentando'}</small></div></div>`},
 result:(pct,pass)=>{const c=document.getElementById('rgc'),n=document.getElementById('rgn');if(!c)return;
  requestAnimationFrame(()=>requestAnimationFrame(()=>{c.style.strokeDashoffset=c.dataset.c*(1-pct/100)}));
  const t0=performance.now();const st=t=>{const k=Math.min(1,(t-t0)/1300),e=1-Math.pow(1-k,3);n.textContent=Math.round(pct*e);if(k<1)requestAnimationFrame(st);else if(pass){const[a,b]=ctr(c);boom(a,b,90,11);setTimeout(()=>boom(innerWidth*.2,innerHeight*.35,50,9),250);setTimeout(()=>boom(innerWidth*.8,innerHeight*.35,50,9),450);vib([30,60,30])}else{c.closest('.card').style.animation='shake .5s';vib(60)}};
  RM?(n.textContent=pct):requestAnimationFrame(st);
  const p=document.querySelector('#vQuiz .pill');if(p)p.insertAdjacentHTML('beforebegin',`<span class="emj">${pass?'🎉':'💪'}</span> `)},
 map:()=>{const bs=[...document.querySelectorAll('#map .blk')];bs.forEach((b,i)=>b.style.setProperty('--i',i));const nx=bs.find(b=>!b.classList.contains('done')&&!b.classList.contains('lock'));if(nx)nx.classList.add('next');
  const bar=document.getElementById('mapBar');if(bar&&!RM){const w=bar.style.width;bar.style.transition='none';bar.style.width='0';void bar.offsetWidth;bar.style.transition='';bar.style.width=w}},
 cert:()=>{setTimeout(()=>{const s=document.querySelector('#vCert .seal');const[a,b]=s?ctr(s):[innerWidth/2,innerHeight/3];boom(a,b,80,10);vib([20,40,20])},1000);setTimeout(()=>boom(innerWidth/2,innerHeight*.25,80,12),1300)}};
})();
</script>"""

import json
JS = JS.replace('__ILL__', json.dumps(ILL, ensure_ascii=False))

def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:80], s.count(old))
    s = s.replace(old, new)

rep('</style></head>', CSS + '</style></head>')
rep('<script>\nconst BR=', JS + '\n<script>\nconst BR=')
rep("const show=v=>{views.forEach(x=>$(x).classList.toggle('hide',x!==v));", "const show=v=>{views.forEach(x=>$(x).classList.toggle('hide',x!==v));FX.view(v);")
rep('<div class="card"><h2>${l[0]}</h2>', '<div class="card">${FX.ill(b,l)}<h2>${l[0]}</h2>')
rep("<ol class=\"pp\">${l[2].map(x=>`<li><span>${x}</span></li>`).join('')}</ol>",
    "<p class=\"hint\">👆 Toca cada paso cuando lo leas</p><ol class=\"pp\">${l[2].map((x,i)=>`<li style=\"--i:${i}\"><span>${x}</span></li>`).join('')}</ol>")
rep('<div class="y"><strong>✓ ASÍ SÍ</strong>${l[3][1]}</div>',
    '<button class="flip" type="button"><span class="fr"><strong>✓ ASÍ SÍ</strong>${l[3][1]}</span><span class="cv"><span><b>👆</b>Toca para ver<br>cómo se hace bien</span></span></button>')
rep("map()};show('vLesson');", "map()};show('vLesson');FX.lesson();")
rep('<div class="note">Pregunta ${p+1} de ${list.length} · ${q[0]}</div>',
    '<div class="note">Pregunta ${p+1} de ${list.length} · ${q[0]}${fin?\'\':FX.streak(list.map(i=>Q[i][3]),ans,p)}</div>')
rep("ans[p]=+b.dataset.o;r()", "ans[p]=+b.dataset.o;window.FXQ=fin?'sel':(ans[p]===q[3]?'good':'bad');r()")
rep("if(p<list.length-1){p++;r()}else done()};\n  }", "if(p<list.length-1){p++;r()}else done()};\n    FX.quiz(window.FXQ);window.FXQ=null;\n  }")
rep('<div class="card"><div class="big">${pct}%</div>', '<div class="card"><div class="ring">${FX.ring(pct,pass)}</div>')
rep("$('bk').onclick=map;\n  }", "$('bk').onclick=map;FX.result(pct,pass);\n  }")
rep("$('map').innerHTML=items.join('');show('vMap');", "$('map').innerHTML=items.join('');show('vMap');FX.map();")
rep("$('cpn').textContent=link}};\n  show('vCert');", "$('cpn').textContent=link}};\n  show('vCert');FX.cert();")
open(F, 'w').write(s)
print('ok', len(s))
