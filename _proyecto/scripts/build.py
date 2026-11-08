import re, os, shutil, sys
from PIL import Image

SRC = '/tmp/claude-0/-home-claude/84b7c6f6-8ee6-52ea-93fd-0c49172b1a87/scratchpad/canvas/project/Main.dc.html'
OUT = '/home/claude/daniela-amaro-web'
H = '/home/claude'

assets = {
    'd991e452260bc2e5eff4744cfe468f60': ('hq/p_hero.webp', 'daniela-retrato.webp'),
    '05b5859028400560358d23fc9d27cff4': ('hq/p_sit.webp', 'galeria-1.webp'),
    'ef1b4667cf56ec5a9de82850bb5d9abc': ('hq/p_profile.webp', 'galeria-2.webp'),
    '0fece43d449516676861b4794e665bf9': ('hq/p_kneel.webp', 'galeria-3.webp'),
    'a3420dc4e013469054bbe4ae91d8ae44': ('hq/p_alt.webp', 'daniela-contacto.webp'),
    'fd606f87a8832bc19df8a2c44a5660bd': ('vid/reel1.mp4', 'reel-casa-condimentos.mp4'),
    'd3795a5864048e365f39217539a8f258': ('vid/reel2.mp4', 'reel-now.mp4'),
    'c28a55f74af90174fb13a787f18a46dd': ('vid/reel3.mp4', 'reel-tiendas-montana.mp4'),
    'bd64ca493ae9735019f12c8f50d8e291': ('vid/reel1_poster.jpg', 'reel-casa-condimentos.jpg'),
    '66b0be23c481db8a2034b71a591a4e18': ('vid/reel2_poster.jpg', 'reel-now.jpg'),
    'ecd9058ee347ccc654a557386b397f0f': ('vid/reel3_poster.jpg', 'reel-tiendas-montana.jpg'),
    'de1d356521edecd9a62b31ebd765a569': ('prof/t1.webp', 'feed-1.webp'),
    '76868ca9b6103c8feb5f6e17e075f3be': ('prof/t2.webp', 'feed-2.webp'),
    '6d07175a4fe5fa1c1811ca10e45e5c19': ('prof/t3.webp', 'feed-3.webp'),
    '34f45aee5cb5a8c75b7c8dd13dffbc40': ('prof/t4.webp', 'feed-4.webp'),
    '9288bd54825250ced57d0b4075767b3c': ('prof/t5.webp', 'feed-5.webp'),
    '360d2e15ebf3fad3fc9a7cf6cd86e5d9': ('prof/t6.webp', 'feed-6.webp'),
    'fca1b3848f5eed69639e1a13a9c64be5': ('prof/hl_yo.webp', 'destacada-yo.webp'),
    'a0e58be245829c5ef67f5f4b4e1b96a7': ('prof/hl_trabajo.webp', 'destacada-trabajo.webp'),
    'e20fb62aff328b1c20b82678a8a2b1cd': ('logos/farmatodo.svg', 'logo-farmatodo.svg'),
    'd1f6746ad9a1fabff0d61464f9fca493': ('logos/farmaclinica.svg', 'logo-farmaclinica-verde.svg'),
    '55e4edecaaf78f2750174a3bd946d258': ('logos/natys.svg', 'logo-natys.svg'),
    'e2decef6b277cfde29fbb4e2e03b964d': ('logos/sazonova.svg', 'logo-sazonova.svg'),
    'd415abf817e81fa4176bb039c0c9e460': ('logos/hammer.svg', 'logo-hammer.svg'),
    '5347caf8684b54e31cd5efbaf29177a5': ('logos2/cachapas.svg', 'logo-cachapas-del-este.svg'),
    'd669d18f217ad6e74331d9241386ceb6': ('logos2/rucha.svg', 'logo-rucha.svg'),
    '5f46803c00cbadbfe071b867142dc733': ('vid2/hero.mp4', 'hero-daniela.mp4'),
    'e16149fc90e17219a9cbcc8bcf4328c6': ('vid2/hero_poster.jpg', 'hero-daniela.jpg'),
    '250629458de25dfe81db935f3b4c7208': ('vid2/reel4.mp4', 'reel-motores-vmj.mp4'),
    '644006c096893cc075d4e225155813a6': ('vid2/reel4_poster.jpg', 'reel-motores-vmj.jpg'),
    'c5d9ba8844c8571c77219469c816230e': ('vid2/reel5.mp4', 'reel-sazonova.mp4'),
    'ba1ebdebc0d2ceff77627eb7699d86c1': ('vid2/reel5_poster.jpg', 'reel-sazonova.jpg'),
    '1877b28c6073268d18571fd4b581efbe': ('vid2/reel6.mp4', 'reel-remesas-jj.mp4'),
    'bf912f5a39f352effa7c94f1720f087d': ('vid2/reel6_poster.jpg', 'reel-remesas-jj.jpg'),
}

src = open(SRC, encoding='utf-8').read()
helmet = re.search(r'<helmet>(.*?)</helmet>', src, re.S).group(1)
body = re.search(r'</helmet>(.*?)</x-dc>', src, re.S).group(1)

# --- strip DC-only bindings ---
body = body.replace(' ref="{{ reg }}"', '').replace(' ref="{{ vreg }}"', '').replace(' ref="{{ hreg }}"', '')
body = body.replace(' {{ heroHide }}', '').replace(' {{ ctaCls }}', '')
body = body.replace('muted="{{ true }}" playsInline="{{ true }}" preload="auto"', 'autoplay muted playsinline preload="auto"')
body = re.sub(r' \{\{ v\.\w+ \}\}', '', body)
body = body.replace(' {{ root }}', '')
body = body.replace('autoPlay="{{ true }}" muted="{{ true }}" loop="{{ true }}" playsInline="{{ true }}"',
                    'autoplay muted loop playsinline')

def cnt(to, dec=0, sfx='', comma=False):
    final = ('%.*f' % (dec, to))
    if comma: final = final.replace('.', ',')
    return '<span class="cnt" data-to="%s" data-dec="%d" data-sfx="%s" data-comma="%d">%s%s</span>' % (to, dec, sfx, 1 if comma else 0, final, sfx)

nums = {
    'hero.f': cnt(16.5, 1, 'K'), 'hero.vw': cnt(167, 0, 'K'), 'hero.fem': cnt(88, 0, '%'), 'hero.it': cnt(8.4, 1, 'K'),
    'aud.f': cnt(16.5, 1, 'K'), 'aud.vw': cnt(167, 0, 'K'), 'aud.it': cnt(8.4, 1, 'K'), 'aud.reach': cnt(10, 0, ''),
    'prof.posts': cnt(176, 0, ''), 'prof.f': cnt(16.5, 1, 'K'), 'prof.vw': cnt(167, 0, 'K'),
    'split.fem': cnt(88.2, 1, '%', True), 'split.masc': cnt(11.8, 1, '%', True),
    'split.femW': 'calc(88.2% * var(--p, 1))', 'split.mascW': 'calc(11.8% * var(--p, 1))',
    'split.deg': 'calc(317.52deg * var(--p, 1))',
}
for k, val in nums.items():
    body = body.replace('{{ %s }}' % k, val)
body = body.replace('data-rv="audSplit"', 'data-rv="audSplit" data-progress')

# --- assets ---
os.makedirs(OUT + '/assets', exist_ok=True)
for bid, (srcf, name) in assets.items():
    if '/_blob/' + bid in body:
        shutil.copy(os.path.join(H, srcf), OUT + '/assets/' + name)
        body = body.replace('/_blob/' + bid, 'assets/' + name)

left = re.findall(r'/_blob/\w+|\{\{[^}]*\}\}', body)
assert not left, left

# social preview image 1200x630
hero = Image.open(H + '/hq/p_hero.webp').convert('RGB')
og = Image.new('RGB', (1200, 630), (235, 205, 210))
w = 504; hh = int(hero.height * w / hero.width)
ph = hero.resize((w, hh), Image.LANCZOS).crop((0, int(hh*0.08), w, int(hh*0.08)+630))
og.paste(ph, (1200 - w, 0))
og.save(OUT + '/assets/og-image.jpg', quality=86)

favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="32" fill="#A9546A"/><text x="32" y="42" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-size="30" fill="#FFF4F6">DA</text></svg>'''
open(OUT + '/favicon.svg', 'w').write(favicon)

js = r'''
<script>
(function () {
  var reduce = false;
  try { reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}
  var hasIO = 'IntersectionObserver' in window;
  var page = document.querySelector('.page');

  // Video del hero: arranca de inmediato y se queda en el último cuadro.
  // Si el navegador bloquea la reproducción automática (p. ej. modo de ahorro de batería en iPhone),
  // se mantiene el primer cuadro y se reproduce al primer toque en la pantalla.
  var hv = document.querySelector('.herovid');
  var blocked = [];
  var tryPlay = function (v) {
    v.muted = true;
    try { var p = v.play(); if (p && p.catch) p.catch(function () { if (blocked.indexOf(v) < 0) blocked.push(v); }); }
    catch (e) { if (blocked.indexOf(v) < 0) blocked.push(v); }
  };
  var onGesture = function () {
    var list = blocked.slice(); blocked = [];
    list.forEach(function (v) { if (v === hv ? !v.ended : v._vis) tryPlay(v); });
  };
  ['touchend', 'pointerup', 'click', 'keydown'].forEach(function (ev) {
    document.addEventListener(ev, onGesture, { passive: true });
  });
  if (hv) {
    hv.addEventListener('error', function () { hv.classList.add('off'); });
    tryPlay(hv);
  }

  // Videos de reels: se precargan al acercarse a la sección y se reproducen solos al estar a la vista
  var vids = document.querySelectorAll('video:not(.herovid)');
  if (hasIO) {
    var near = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        var v = e.target; near.unobserve(v);
        if (v.preload !== 'auto') { v.preload = 'auto'; try { v.load(); } catch (x) {} }
      });
    }, { rootMargin: '1200px 1200px 1200px 1200px' });
    var vo = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var v = e.target; v._vis = e.isIntersecting;
        if (e.isIntersecting) tryPlay(v); else v.pause();
      });
    }, { threshold: 0.35 });
    vids.forEach(function (v) { near.observe(v); vo.observe(v); });
  } else {
    vids.forEach(function (v) { v._vis = true; tryPlay(v); });
  }
  if (reduce || !hasIO || !window.requestAnimationFrame) return;

  page.classList.add('armed');

  function fmt(el, p) {
    var to = parseFloat(el.getAttribute('data-to'));
    var d = parseInt(el.getAttribute('data-dec'), 10) || 0;
    var s = (to * (p >= 1 ? 1 : p)).toFixed(d);
    if (el.getAttribute('data-comma') === '1') s = s.replace('.', ',');
    el.textContent = s + (el.getAttribute('data-sfx') || '');
  }
  function animate(cb, dur, delay) {
    setTimeout(function () {
      var t0 = null;
      function step(t) {
        if (t0 === null) t0 = t;
        var k = Math.min(1, (t - t0) / dur);
        cb(k >= 1 ? 1 : 1 - Math.pow(2, -10 * k));
        if (k < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }, delay || 0);
  }

  // Apariciones al hacer scroll
  var ro = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      var key = e.target.getAttribute('data-rv');
      document.querySelectorAll('[data-rv="' + key + '"]').forEach(function (x) { x.classList.add('on'); ro.unobserve(x); });
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
  document.querySelectorAll('[data-rv]').forEach(function (el) { ro.observe(el); });

  // Cifras que suben y barras que se llenan
  var cnts = document.querySelectorAll('.cnt');
  var prog = document.querySelectorAll('[data-progress]');
  cnts.forEach(function (el) { fmt(el, 0); });
  prog.forEach(function (el) { el.style.setProperty('--p', 0); });
  var co = new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (!e.isIntersecting) return;
      var el = e.target; co.unobserve(el);
      if (el.classList.contains('cnt')) {
        animate(function (p) { fmt(el, p); }, 2200, el.closest('#inicio') ? 900 : 250);
      } else {
        animate(function (p) { el.style.setProperty('--p', p); }, 2000, 300);
      }
    });
  }, { threshold: 0.3 });
  cnts.forEach(function (el) { co.observe(el); });
  prog.forEach(function (el) { co.observe(el); });
})();
</script>
'''

head = '''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Daniela Amaro · Modelo y creadora de contenido</title>
<meta name="description" content="Daniela Amaro, Licenciada en Comunicación Social, modelo y creadora de contenido en Barquisimeto. Media kit, audiencia, servicios y contacto para marcas.">
<meta name="theme-color" content="#EBCDD2">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:title" content="Daniela Amaro · Media Kit">
<meta property="og:description" content="Modelo y creadora de contenido. +16.5K seguidores en Instagram. Servicios para marcas desde Barquisimeto.">
<meta property="og:image" content="assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
''' + helmet.strip() + '''
<style>section[id]{scroll-margin-top:72px}</style>
</head>
<body>
'''
html = head + body.strip() + '\n' + js + '</body>\n</html>\n'
open(OUT + '/index.html', 'w', encoding='utf-8').write(html)

open(OUT + '/vercel.json', 'w').write('''{
  "cleanUrls": true,
  "headers": [
    { "source": "/assets/(.*)", "headers": [{ "key": "Cache-Control", "value": "public, max-age=31536000, immutable" }] }
  ]
}
''')
print('ok', len(html), sorted(os.listdir(OUT + '/assets')))
