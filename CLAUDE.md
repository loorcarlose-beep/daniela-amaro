# Proyecto: Web Media Kit de Daniela Amaro (amarodaniela.com)

Antes de hacer cualquier cosa, lee `_proyecto/RESUMEN.md`: ahí está quién es Daniela, el objetivo de la web, cada sección con sus textos y precios, accesos, identidad visual, decisiones tomadas y pendientes.

## Cómo trabajar
- El sitio publicado es `index.html` + `assets/` en la raíz (estático, sin build). Para cambios, edita `index.html` directamente.
- Cada push a `main` lo publica Vercel automáticamente en https://amarodaniela.com (1–2 min).
- Los assets llevan un hash en el nombre (caché inmutable): si reemplazas un archivo, usa un nombre nuevo y actualiza las referencias en `index.html`.
- Prioridad: versión móvil (la mayoría de clientes la ven en el teléfono). Revisa siempre a 390 px de ancho.
- Estilo: femenino, delicado y profesional. Sora para textos; Kepler Std cursiva (Adobe Fonts, kit `jpy5qtc`) para títulos, con Cormorant Garamond de respaldo. Color principal #A9546A.
- Textos en español, primera persona femenina (voz de Daniela).
- `_proyecto/` (diseño fuente, scripts, originales, este resumen) NO se publica: está excluido en `.vercelignore`.
- Carlos (el dueño) prefiere que le propongas ideas y le preguntes lo que necesites en lugar de ejecutar en silencio.
