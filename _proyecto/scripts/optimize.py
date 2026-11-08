"""Post-proceso del sitio generado por build.py: rendimiento + SEO.

- Fuentes propias (woff2) en lugar de Google Fonts, con preload.
- Imágenes con variantes a la medida (srcset), width/height, lazy y decoding async.
- Pósters de video en WebP; reels con preload="none".
- Metadatos SEO completos, datos estructurados, robots.txt, sitemap.xml, íconos.
- Nombres de archivo con huella (hash) para poder cachear un año sin riesgo.
- Botón fijo de WhatsApp en móvil.
"""
import re, os, json, hashlib, shutil, datetime
from PIL import Image, ImageDraw

OUT = '/home/claude/daniela-amaro-web'
A = OUT + '/assets'
H = '/home/claude'
FONTS = '/home/claude/lh/node_modules/@fontsource'
SITE = 'https://amarodaniela.com/'
TODAY = datetime.date.today().isoformat()

html = open(OUT + '/index.html', encoding='utf-8').read()

# ---------------------------------------------------------------- fuentes
os.makedirs(A + '/fonts', exist_ok=True)
LATIN = ('U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+0304, '
         'U+0308, U+0329, U+2000-206F, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD')
font_files = [
    ('Sora', 'normal', 300, f'{FONTS}/sora/files/sora-latin-300-normal.woff2', 'sora-300.woff2'),
    ('Sora', 'normal', 400, f'{FONTS}/sora/files/sora-latin-400-normal.woff2', 'sora-400.woff2'),
    ('Sora', 'normal', 500, f'{FONTS}/sora/files/sora-latin-500-normal.woff2', 'sora-500.woff2'),
    ('Sora', 'normal', 600, f'{FONTS}/sora/files/sora-latin-600-normal.woff2', 'sora-600.woff2'),
    ('Cormorant Garamond', 'italic', 500, f'{FONTS}/cormorant-garamond/files/cormorant-garamond-latin-500-italic.woff2', 'cormorant-500-italic.woff2'),
]
faces = []
for fam, style, w, srcp, name in font_files:
    shutil.copy(srcp, f'{A}/fonts/{name}')
    faces.append(f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{w};font-display:swap;"
                 f"src:url(assets/fonts/{name}) format('woff2');unicode-range:{LATIN}}}")
font_css = '<style>' + ''.join(faces) + '</style>'
preloads = ''.join(f'<link rel="preload" href="assets/fonts/{n}" as="font" type="font/woff2" crossorigin>'
                   for n in ('sora-300.woff2', 'sora-500.woff2', 'cormorant-500-italic.woff2'))
html = html.replace('<link rel="preconnect" href="https://fonts.googleapis.com">', '')
html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/css2[^"]*">', preloads + font_css, html)
assert 'fonts.googleapis' not in html

# Kepler Std (kit web de Adobe Fonts), sin bloquear el render
TK = '<link rel="stylesheet" href="https://use.typekit.net/jpy5qtc.css">'
assert TK in html
html = html.replace(TK, '<link rel="preconnect" href="https://use.typekit.net" crossorigin>'
    '<link rel="preconnect" href="https://p.typekit.net" crossorigin>'
    '<link rel="stylesheet" href="https://use.typekit.net/jpy5qtc.css" media="print" onload="this.media=\'all\'">'
    '<noscript>' + TK + '</noscript>')

# ---------------------------------------------------------------- imágenes
def variant(src_path, out_name, width, quality=80):
    im = Image.open(src_path)
    im = im.convert('RGBA') if im.mode in ('RGBA', 'LA', 'P') else im.convert('RGB')
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(f'{A}/{out_name}', 'WEBP', quality=quality, method=6)
    return im.size

# nombre en el sitio -> (archivo fuente, anchos, sizes)
IMGS = {
    'daniela-retrato.webp': (H + '/hq/p_hero.webp', [520, 720, 920], '(max-width: 760px) 92vw, 460px'),
    'galeria-1.webp': (H + '/hq/p_sit.webp', [480, 640, 900], '(max-width: 760px) 76vw, 400px'),
    'galeria-2.webp': (H + '/hq/p_profile.webp', [480, 640, 900], '(max-width: 760px) 76vw, 400px'),
    'galeria-3.webp': (H + '/hq/p_kneel.webp', [480, 640, 900], '(max-width: 760px) 76vw, 400px'),
    'daniela-contacto.webp': (H + '/hq/p_alt.webp', [260], '124px'),
}
for i in range(1, 7):
    IMGS[f'feed-{i}.webp'] = (f'{H}/prof/t{i}.webp', [300], '(max-width: 760px) 30vw, 140px')
IMGS['destacada-yo.webp'] = (H + '/prof/hl_yo.webp', [120], '60px')
IMGS['destacada-trabajo.webp'] = (H + '/prof/hl_trabajo.webp', [120], '60px')

made = {}
for name, (srcp, widths, sizes) in IMGS.items():
    stem = name.rsplit('.', 1)[0]
    vs = []
    for w in widths:
        out = f'{stem}-{w}.webp'
        size = variant(srcp, out, w)
        vs.append((out, size))
    made[name] = (vs, sizes)
    if os.path.exists(f'{A}/{name}'):
        os.remove(f'{A}/{name}')

# avatar pequeño de la tarjeta de perfil (usa el retrato)
avatar_size = variant(H + '/hq/p_hero.webp', 'avatar-200.webp', 200)

def logo_dims(path):
    s = open(path, encoding='utf-8').read()
    m = re.search(r'viewBox="[\d.\-]+ [\d.\-]+ ([\d.]+) ([\d.]+)"', s)
    return float(m.group(1)), float(m.group(2))

def fix_img(m):
    tag = m.group(0)
    src = re.search(r'src="assets/([^"]+)"', tag).group(1)
    extra = ''
    if src == 'daniela-retrato.webp' and 'object-position: 50% 22%' in tag:
        out, (w, h) = 'avatar-200.webp', avatar_size
        tag = tag.replace('src="assets/daniela-retrato.webp"', f'src="assets/{out}"')
        extra = f' width="{w}" height="{h}"'
    elif src in made:
        vs, sizes = made[src]
        big, (w, h) = vs[-1]
        srcset = ', '.join(f'assets/{o} {sz[0]}w' for o, sz in vs)
        tag = tag.replace(f'src="assets/{src}"', f'src="assets/{big}" srcset="{srcset}" sizes="{sizes}"')
        extra = f' width="{w}" height="{h}"'
    elif src.endswith('.svg'):
        w, h = logo_dims(f'{A}/{src}')
        extra = f' width="{round(w)}" height="{round(h)}"'
    extra += ' loading="lazy" decoding="async"'
    return tag[:-1].rstrip() + extra + '>'

html = re.sub(r'<img\b[^>]*>', fix_img, html)

# pósters de video a WebP
for jpg in [f for f in os.listdir(A) if f.endswith('.jpg') and f != 'og-image.jpg']:
    stem = jpg[:-4]
    im = Image.open(f'{A}/{jpg}').convert('RGB')
    im.save(f'{A}/{stem}.webp', 'WEBP', quality=78, method=6)
    os.remove(f'{A}/{jpg}')
    html = html.replace(f'assets/{jpg}"', f'assets/{stem}.webp"')

# reels: no descargar nada hasta que se vean
html = html.replace('autoplay muted loop playsinline preload="metadata"', 'muted loop playsinline preload="metadata"')
assert 'autoplay muted loop' not in html

# ---------------------------------------------------------------- íconos
hero = Image.open(H + '/hq/p_hero.webp').convert('RGB')
side = min(hero.width, int(hero.height * 0.62))
crop = hero.crop(((hero.width - side) // 2, int(hero.height * 0.08), (hero.width - side) // 2 + side, int(hero.height * 0.08) + side))
icon = crop.resize((180, 180), Image.LANCZOS)
icon.save(OUT + '/apple-touch-icon.png', optimize=True)

# ---------------------------------------------------------------- huellas (cache de un año seguro)
rename = {}
for root, _, files in os.walk(A):
    for f in files:
        if f == 'og-image.jpg':
            continue
        p = os.path.join(root, f)
        digest = hashlib.md5(open(p, 'rb').read()).hexdigest()[:8]
        stem, ext = f.rsplit('.', 1)
        nf = f'{stem}.{digest}.{ext}'
        os.rename(p, os.path.join(root, nf))
        rel_old = os.path.relpath(p, OUT)
        rename[rel_old] = os.path.relpath(os.path.join(root, nf), OUT)
for old in sorted(rename, key=len, reverse=True):
    html = re.sub(r'(?<=["\s(,])' + re.escape(old) + r'(?=["\s),])', rename[old], html)
left = [r for r in re.findall(r'assets/[\w./-]+', html) if not re.search(r'\.[0-9a-f]{8}\.\w+$', r) and 'og-image' not in r]
assert not left, left

# ---------------------------------------------------------------- SEO
TITLE = 'Daniela Amaro · Modelo y creadora de contenido en Barquisimeto'
DESC = ('Daniela Amaro, Licenciada en Comunicación Social, modelo y creadora de contenido en Barquisimeto, '
        'Venezuela. Conoce su audiencia, sus colaboraciones con marcas y sus servicios de reels, '
        'modelaje comercial y embajadora de marca.')
OG_DESC = 'Modelo y creadora de contenido en Barquisimeto. +16.5K seguidores en Instagram. Servicios para marcas: reels, modelaje comercial y embajadora de marca.'
ld = {
    '@context': 'https://schema.org',
    '@type': 'Person',
    'name': 'Daniela Amaro',
    'jobTitle': 'Modelo y creadora de contenido',
    'description': DESC,
    'url': SITE,
    'image': SITE + rename.get('assets/' + made['daniela-retrato.webp'][0][-1][0], ''),
    'sameAs': ['https://www.instagram.com/amarodaniela_/'],
    'telephone': '+58 424-5625223',
    'address': {'@type': 'PostalAddress', 'addressLocality': 'Barquisimeto', 'addressRegion': 'Lara', 'addressCountry': 'VE'},
    'knowsAbout': ['Creación de contenido', 'Modelaje comercial', 'Comunicación social', 'Marketing de influencia'],
    'award': ['Madrina de Cardenales 2020', 'Reina del Deporte 2023'],
}
seo = f'''<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<link rel="canonical" href="{SITE}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="author" content="Daniela Amaro">
<meta name="theme-color" content="#EBCDD2">
<meta name="color-scheme" content="light">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="profile">
<meta property="og:locale" content="es_VE">
<meta property="og:site_name" content="Daniela Amaro">
<meta property="og:url" content="{SITE}">
<meta property="og:title" content="Daniela Amaro · Media Kit">
<meta property="og:description" content="{OG_DESC}">
<meta property="og:image" content="{SITE}assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Daniela Amaro, modelo y creadora de contenido">
<meta property="profile:first_name" content="Daniela">
<meta property="profile:last_name" content="Amaro">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Daniela Amaro · Media Kit">
<meta name="twitter:description" content="{OG_DESC}">
<meta name="twitter:image" content="{SITE}assets/og-image.jpg">
<link rel="preload" as="image" href="{rename['assets/hero-daniela.webp']}" fetchpriority="high">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
'''
html = re.sub(r'<title>.*?<meta name="twitter:card" content="summary_large_image">\n', lambda m: seo, html, flags=re.S)
assert html.count('<title>') == 1 and 'application/ld+json' in html

open(OUT + '/robots.txt', 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n')
open(OUT + '/sitemap.xml', 'w').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    f'  <url><loc>{SITE}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>1.0</priority></url>\n'
    '</urlset>\n')

# ---------------------------------------------------------------- JS: botón fijo de WhatsApp en móvil
cta_js = r'''
  // Botón fijo de WhatsApp en móvil: aparece tras el inicio y se oculta en contacto
  var cta = document.querySelector('.mcta');
  if (cta && hasIO) {
    var vis = {};
    var cobs = new IntersectionObserver(function (es) {
      es.forEach(function (e) { vis[e.target.id || e.target.tagName] = e.isIntersecting; });
      cta.classList.toggle('show', !vis.inicio && !vis.contacto && !vis.FOOTER);
    }, { threshold: 0 });
    ['inicio', 'contacto'].forEach(function (id) { var el = document.getElementById(id); if (el) cobs.observe(el); });
    var ft = document.querySelector('footer'); if (ft) cobs.observe(ft);
  }
'''
cta_js += r'''
  // Pestañas de servicios (móvil): al cambiar, deja el inicio del grupo justo debajo de las pestañas
  [].forEach.call(document.querySelectorAll('.svt'), function (inp) {
    inp.addEventListener('change', function () {
      var g = document.querySelector('.sg' + inp.id.slice(3)); var t = document.querySelector('.stabs');
      if (!g || !t) return;
      var off = t.getBoundingClientRect().bottom + 14, top = g.getBoundingClientRect().top;
      if (top < off) window.scrollTo({ top: window.pageYOffset + top - off, behavior: reduce ? 'auto' : 'smooth' });
    });
  });
'''
anchor = "  if (reduce || !hasIO || !window.requestAnimationFrame) return;"
assert anchor in html
html = html.replace(anchor, cta_js + anchor)

# Vercel Web Analytics (se activa en el panel de Vercel → Analytics)
html = html.replace('</body>', '<script defer src="/_vercel/insights/script.js"></script>\n</body>', 1)
open(OUT + '/index.html', 'w', encoding='utf-8').write(html)

vercel = {
    'cleanUrls': True,
    'redirects': [
        {'source': '/(.*)', 'has': [{'type': 'host', 'value': 'daniela-amaro.vercel.app'}], 'destination': 'https://amarodaniela.com/$1', 'permanent': True},
        {'source': '/(.*)', 'has': [{'type': 'host', 'value': 'www.amarodaniela.com'}], 'destination': 'https://amarodaniela.com/$1', 'permanent': True},
    ],
    'headers': [
        {'source': '/assets/(.*)', 'headers': [{'key': 'Cache-Control', 'value': 'public, max-age=31536000, immutable'}]},
        {'source': '/(.*)', 'headers': [
            {'key': 'X-Content-Type-Options', 'value': 'nosniff'},
            {'key': 'Referrer-Policy', 'value': 'strict-origin-when-cross-origin'},
        ]},
    ],
}
open(OUT + '/vercel.json', 'w').write(json.dumps(vercel, indent=2) + '\n')

total = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(OUT) for f in fs)
print('optimizado', len(html), 'bytes html;', round(total / 1e6, 2), 'MB en total')
