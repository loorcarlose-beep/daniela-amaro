# Proyecto: Web Media Kit de Daniela Amaro (amarodaniela.com)

Antes de hacer cualquier cosa, lee `_proyecto/RESUMEN.md`: ahí está quién es Daniela, el objetivo de la web, cada sección con sus textos y precios, accesos, identidad visual, decisiones tomadas y pendientes.

## Contexto del traspaso
Este proyecto se hizo con Carlos en otra cuenta de Claude y se trasladó aquí en noviembre de 2026. Todo lo importante está en este repositorio; no hay nada pendiente en la cuenta anterior salvo el diseño editable de Claude Design, cuyo archivo fuente está en `_proyecto/diseno-claude-design/`.

## Primeros pasos (la primera vez)
1. Lee `_proyecto/RESUMEN.md` completo.
2. Comprueba que puedes subir cambios: haz un cambio mínimo o `git push --dry-run`. Si GitHub responde 403, la app de Claude solo tiene permiso de lectura: pídele a Carlos que en github.com/settings/installations → Claude → Configure ponga Contents en "Read and write" e incluya este repositorio.
3. Confírmale a Carlos en 3–4 líneas lo que entendiste del proyecto y pregúntale qué quiere hacer.

## Accesos (todo es de Carlos)
- GitHub: loorcarlose-beep/daniela-amaro (rama main = producción).
- Vercel: proyecto daniela-amaro, despliega solo desde GitHub. No necesitas acceso a Vercel.
- Dominio: amarodaniela.com en Namecheap, ya configurado (A @ → 216.198.79.1, CNAME www → cname.vercel-dns.com). No tocar.
- Adobe Fonts: kit `jpy5qtc` en la cuenta de Adobe de Carlos (Kepler Std cursiva 400/500).
- Pendiente de Carlos: activar Vercel Analytics y dar de alta Google Search Console.

## Cómo trabajar
- El sitio publicado es `index.html` + `assets/` en la raíz (estático, sin build). Para cambios, edita `index.html` directamente.
- Cada push a `main` lo publica Vercel automáticamente en https://amarodaniela.com (1–2 min).
- Los assets llevan un hash en el nombre (caché inmutable): si reemplazas un archivo, usa un nombre nuevo y actualiza las referencias en `index.html`.
- Prioridad: versión móvil (la mayoría de clientes la ven en el teléfono). Revisa siempre a 390 px de ancho.
- Estilo: femenino, delicado y profesional. Sora para textos; Kepler Std cursiva (Adobe Fonts, kit `jpy5qtc`) para títulos, con Cormorant Garamond de respaldo. Color principal #A9546A.
- Textos en español, primera persona femenina (voz de Daniela).
- `_proyecto/` (diseño fuente, scripts, originales, este resumen) NO se publica: está excluido en `.vercelignore`.
- Verifica cada cambio antes de decir que está listo (captura a 390 px y a escritorio) y confirma en la web en vivo después del push.
- Carlos (el dueño) prefiere que le propongas ideas y le preguntes lo que necesites en lugar de ejecutar en silencio.
