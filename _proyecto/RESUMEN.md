# Web Media Kit de Daniela Amaro: resumen completo del proyecto

Documento de traspaso. Reúne todo lo necesario para continuar el proyecto desde otra cuenta de Claude sin perder información ni accesos.
Última actualización: 8 de noviembre de 2026.

---

## 1. Quién es Daniela

- **Nombre:** Daniela Amaro.
- **Instagram:** @amarodaniela_ (https://www.instagram.com/amarodaniela_/).
- **Profesión:** Licenciada en Comunicación Social, modelo y creadora de contenido.
- **Ubicación:** Barquisimeto, Venezuela. Puede viajar, con condiciones que se conversan con cada cliente.
- **Reconocimientos:** Madrina de Cardenales (2020) y Reina del Deporte (2023).
- **Trabajo:**
  - Crea contenido para marcas: reels con guion propio, menciones en historias y colaboraciones.
  - Trabaja como modelo comercial (foto y video).
  - Es embajadora de marca.
  - Trabaja como promotora o impulsadora en eventos y activaciones.
- **WhatsApp de contacto:** +58 424-5625223.
- **Su propuesta:** "Creo piezas para marcas que no solo se ven bien: se sienten cercanas y genuinas". Lema de la web: *comunicar es conectar*.

## 2. Para qué es la web

Daniela tenía su media kit en PDF (archivo `MEDIA KIT - DANIELA AMARO.pdf`). La web convierte ese PDF en una página de presentación profesional para enviar a marcas y agencias.

La página muestra quién es Daniela, su audiencia, su trabajo reciente y las marcas con las que ha trabajado. También presenta sus servicios con precios y lleva al cliente a escribirle por WhatsApp.

- **Prioridad: el celular.** Casi todos los clientes la abren desde el teléfono, normalmente con un enlace enviado por WhatsApp o Instagram.
- **Estilo:** femenino, delicado y profesional, igual que el PDF original pero más "pro". Lleva animaciones suaves de aparición al hacer scroll y números que suben (count-up).

---

## 3. Dónde vive todo (accesos)

| Qué | Dónde | Notas |
|---|---|---|
| **Web en vivo** | https://amarodaniela.com | Dominio principal |
| Dirección antigua | https://daniela-amaro.vercel.app | Redirige sola a amarodaniela.com |
| **Código (repositorio)** | GitHub: `loorcarlose-beep/daniela-amaro`, rama `main` | Es la fuente de verdad: todo el sitio está ahí |
| **Hosting** | Vercel, proyecto `daniela-amaro`, conectado al repo | Cada cambio subido a `main` se publica solo en 1–2 minutos |
| **Dominio** | Namecheap: `amarodaniela.com` | DNS (Advanced DNS): registro **A** `@` → `216.198.79.1`; **CNAME** `www` → `cname.vercel-dns.com` |
| **Tipografía Kepler** | Adobe Fonts, kit web **`jpy5qtc`** ("Daniela Amaro web (amarodaniela.com)") en la cuenta de Adobe de Carlos | Dominios del kit: amarodaniela.com, www.amarodaniela.com, daniela-amaro.vercel.app, *.vercel.app, localhost. Hay un kit viejo, `ajz6lrn`, que ya no se usa y se puede borrar |
| **Diseño editable (Claude Design)** | Artifact "Daniela Amaro" en la cuenta vieja de Claude (versión 27) | No se transfiere entre cuentas. Su código fuente está en (`_proyecto/diseno-claude-design/Main.dc.html`) |
| Estadísticas | Vercel Web Analytics | **Pendiente activarlo:** Vercel → proyecto → Analytics → Enable |

### Para que la cuenta nueva de Claude pueda publicar sola
1. En la cuenta nueva, conecta GitHub (Configuración → Conectores).
2. En GitHub, entra a **github.com/settings/installations → Claude → Configure**.
   - En **Repository access**, incluye `daniela-amaro`.
   - En **Permissions → Contents**, pon **Read and write**. Sin esto, Claude solo puede leer el repositorio y no puede subir cambios: es el error 403 que tuvimos al principio.
3. Pídele a Claude que clone `loorcarlose-beep/daniela-amaro`, haga los cambios y los suba a `main`. Vercel publica solo.

---

## 4. Identidad visual

- **Colores principales:**
  - Rosa vino (botones y acentos): `#A9546A`.
  - Vino oscuro (textos destacados): `#8C4255` y `#7E3346`.
  - Ciruela (textos): `#5B3940`, `#6E4A51` y `#6B3A45`.
  - Fondos rosados: `#F3DDE1`, `#EBCDD2`, `#EED6DA` y `#F8ECEE`.
  - Fondo general (crema): `#FBF7F6`.
  - Rosa muy claro (texto sobre fondos oscuros): `#FFF4F6`.
  - Blanco: `#FFFFFF`.
- **Tipografías:**
  - **Sora** (300/400/500/600) para textos, botones y datos. Va incluida dentro de la web, en `assets/fonts`.
  - **Kepler Std**, en cursiva 400 y 500, para títulos, el nombre y los números grandes. Se carga desde el kit de Adobe Fonts.
  - Mientras Kepler carga, o si falla, se muestra **Cormorant Garamond** 500 cursiva, también incluida.
- **Animaciones:**
  - Los bloques aparecen suavemente al hacer scroll.
  - Las métricas cuentan hacia arriba.
  - Hay una franja de texto en movimiento y una tira de logos en movimiento.
  - Las tarjetas se elevan al pasar el ratón (solo en computadora).
  - Se respeta "reducir movimiento" del sistema, salvo en los videos.
- **Tono:** cercano, en primera persona y en femenino ("armamos juntas"). Elegante, sin exagerar.

---

## 5. La web, sección por sección (en orden)

### 5.1 Encabezado fijo
- A la izquierda, "Daniela Amaro" en Kepler. A la derecha, el botón **"Trabajemos juntos"**, que lleva a Contacto.
- En computadora también hay menú: Sobre mí · Audiencia · Reels · Servicios.
- Una línea fina debajo muestra el progreso del scroll. En el celular el fondo es sólido.
- *Se quitó a propósito* un botón flotante de WhatsApp porque era redundante con este botón.

### 5.2 Inicio (hero)
- **Video de Daniela** (`hero-daniela.mp4`, de unos 9,7 s) dentro de un marco en forma de arco.
  - Se reproduce una vez al cargar y se queda en el último cuadro.
  - Si el iPhone bloquea la reproducción automática (ahorro de batería), se queda en el primer cuadro y arranca al primer toque.
  - **En el celular el video va primero, arriba del texto**, para que lo primero que se vea sea ella.
- **Etiquetas flotantes sobre el video:** "Instagram @amarodaniela_" y "8.4K Interacciones".
- **Antetítulo:** "// Media Kit · Barquisimeto, Venezuela".
- **Título:** "Daniela Amaro".
- **Texto:** "Licenciada en Comunicación Social y creadora de contenido. Creo piezas para marcas que no solo se ven bien: se sienten cercanas y genuinas."
- **Botones:** "Ver servicios" y "Ver mi trabajo".
- **Mini métricas:** +16.5K Seguidores · 167K Visualizaciones · 88% Audiencia femenina.

### 5.3 Franja en movimiento
Repite: "Madrina de Cardenales 2020 ✦ Reina del Deporte 2023 ✦ Comunicación Social ✦ Estrategia visual ✦ Presencia de marca ✦ Contenido auténtico ✦".

### 5.4 Galería
Tres fotos de Daniela con la frase "comunicar es conectar" y la indicación "Desliza →", que en el celular es un carrusel horizontal.

### 5.5 Sobre mí
- **Tarjeta tipo perfil de Instagram**, rediseñada para que se viera mejor que el mockup de teléfono del PDF:
  - Avatar, @amarodaniela_ y "Amaro Daniela · Modelo".
  - 176 Publicaciones · 16.5K Seguidores · 167K Visualizaciones.
  - Bio: Licenciada en Comunicación Social / Creadora de contenido / Barquisimeto.
  - Destacadas "Yo" y "Trabajo", una cuadrícula del feed y el botón "Ver perfil en Instagram".
  - Se ocultaron las "personas en común" a pedido de Carlos.
  - **En el celular es más compacta:** sin destacadas y con una sola fila de 3 fotos.
- **Texto:** "¡Hola! Mi nombre es Daniela." Habla de la Comunicación Social y de que comunicar es generar conexiones reales. Menciona la disciplina y la gracia de Madrina de Cardenales 2020 y Reina del Deporte 2023, y que hoy potencia la identidad de marcas comerciales.
- **4 tarjetas** (en 2×2 en el celular):
  - Estrategia visual: "Cada pieza pensada para tu marca".
  - Presencia de marca: "Imagen coherente y memorable".
  - Comunicación auténtica: "Cercana, genuina, que conecta".
  - Desde Barquisimeto: "Disponibilidad de viaje. Ciertas condiciones aplican".

### 5.6 Audiencia
- **Título:** "Una comunidad que mira, siente y responde."
- **Nota:** "Datos de Instagram @amarodaniela_ · últimos 90 días". El periodo de 90 días estaba pendiente de confirmar con Daniela.
- **Tarjetas:**
  - Seguidores +16.5K: comunidad orgánica.
  - Visualizaciones 167K: alcance 10× mayor que su comunidad.
  - Interacciones 8.4K: likes, comentarios, guardados y compartidos.
- **Perfil de la audiencia:** 88,2 % mujeres y 11,8 % hombres. "Ideal para marcas de moda, belleza, bienestar y estilo de vida."
- ⚠️ Conviene actualizar estas cifras cada cierto tiempo.

### 5.7 Contenido reciente ("Así cuento historias")
Hay seis reels de colaboraciones con marcas. Se ven como tarjetas con el video en loop y sin sonido de fondo, en un carrusel horizontal en el celular. Cada uno enlaza a su publicación en Instagram:

| # | Marca | Rubro | Instagram de la marca | Publicación |
|---|---|---|---|---|
| 01 | Casa Condimentos | Alimentos | @casa_condimentos28 | instagram.com/p/Dd2GrdCzD_O |
| 02 | NOW | Movilidad | @nowappve | instagram.com/p/DcMsLsvhk-e |
| 03 | Motores VMJ | Automotriz | @motoresvmjla42 | instagram.com/p/DadQ-z5xkLG |
| 04 | Tiendas Montana | Hogar | @tiendasmontanalancolor | instagram.com/p/DYDf2sMobbS |
| 05 | Sazonova | Alimentos | @sazonovave | instagram.com/p/DWpTJYoJXmr |
| 06 | Remesas JJ | Envíos | @remesasjj_ | instagram.com/p/DUZPELSiGoy |

- Los videos empiezan a cargar un poco antes de llegar a la sección y se reproducen solos al estar a la vista. Se pausan al salir de la vista.
- Debajo está el botón "Ver más en Instagram".

### 5.8 Marcas ("Han confiado en mí")
- Texto: "Marcas de salud, belleza, alimentos y hogar que ya han trabajado conmigo."
- Siete logos en una **tira horizontal que se desplaza sola**, al estilo de la franja del inicio. En computadora se detiene al pasar el ratón.
- Logos: **Farmaclínica Verde, Farmatodo, Naty's, Sazonova, Hammer, Cachapas del Este y Rucha**.

### 5.9 Servicios ("Hagamos crecer tu marca")
- Subtítulo: "Desde una mención puntual hasta una alianza de largo plazo…"
- **En el celular** los servicios van en **4 pestañas: Contenido · Modelo · Alianzas · Eventos**. Las pestañas quedan fijas mientras se recorre la sección. En computadora se ve todo a la vez.

**Contenido**
- **Reel orgánico: $80.**
  - Incluye guion personalizado, edición y publicación en el perfil de Daniela, más menciones en historias, y queda 60 días en el feed.
  - Tiene opción de colab: el reel aparece en el feed de la marca y en el de Daniela.
- **Mención en historias: $10 c/u.** Activación rápida, se cobra por unidad.

**Modelo e imagen comercial**
- Es la participación como modelo cuando el cliente o la agencia ya tiene su propio equipo de producción y edición. "¿Sin equipo? Puedo incluir al equipo de la agencia con un costo adicional."
- **1 video:** $40.
- **3 videos:** $90 ($30 por video).
- **5 videos:** $125 ($25 por video). Es el **"Más elegido"**.
  - Solo este paquete incluye grabación en hasta 2 visitas.
  - Solo este paquete tiene **opción de colab en 1 video por +$55**.
- *Condición de la colab:* el video aparece en el feed de la marca y en el de Daniela, permanece publicado 60 días y debe ir acorde al contenido de su cuenta.

**Alianzas**
- **Embajadora de marca: $300/mes.** Incluye:
  - Uso de imagen como embajadora oficial por 1 mes.
  - 2 visitas al mes, de hasta 5 h cada una.
  - Creación de contenido.
  - Menciones en historias.
  - Recomendación orgánica a la comunidad.
  - Exclusividad de rubro.
  - Opción de un video en colab.
- **Alianza de 3 meses: $500 en total**, con la etiqueta "Ahorras $400".
  - Incluye todo lo del plan mensual, presencia continua por 3 meses y exclusividad total frente a la competencia.
  - **Recuadro destacado: "Sin pagar todo de una vez"**. El pago se puede dividir en cuotas mensuales o quincenales, como mejor les convenga a ambas partes, y equivale a menos de $170 al mes.
  - Botón "Quiero esta alianza".

**Eventos**
- **Promotora / Impulsadora: $12–15 por hora.**
  - La tarifa depende del calzado, el lugar y el horario.
  - Mínimo 3 horas.
  - En jornadas de más de 5 horas o en horario de comida, el cliente cubre el almuerzo o la cena.

**Incluido en todos mis servicios** (bloque rosado; en el celular va al final de la sección)
- Título: "Más que grabar: pienso tu contenido contigo".
- Asesoría creativa personalizada: "Te oriento sobre tendencias y el tipo de contenido que mejor le funciona a tu marca."
- Ideas y guiones propios: "Propongo ideas y escribo el guion, con la naturalidad que conecta con tu audiencia."
- *Se quitó a propósito* "Audio profesional".

**Nota final:** "Precios en dólares (USD). Pago en bolívares a tasa BCV del día."

### 5.10 Contacto ("¡Trabajemos juntos!")
- Texto: "Cuéntame sobre tu marca y armamos juntas la propuesta ideal."
- **Botón "Escríbeme por WhatsApp"**: abre wa.me/584245625223 con el mensaje "Hola Daniela, me gustaría trabajar contigo".
- Botón **@amarodaniela_**, que lleva a Instagram.
- **Datos en tarjeta:**
  - Barquisimeto, Venezuela.
  - "Disponibilidad de viaje – Ciertas condiciones aplican" (texto exacto pedido por Carlos).
  - +58 424-5625223.

### 5.11 Pie de página
"Daniela Amaro", y debajo "Lcda. Comunicación Social · Media Kit". En el celular va centrado.

---

## 6. Parte técnica (para quien continúe)

- **Tipo de sitio:** estático, con HTML, CSS y JS en un solo `index.html` más la carpeta `assets/`. No necesita compilación.
- **Rendimiento:** en Lighthouse, el celular saca 95 en rendimiento y 100 en accesibilidad, buenas prácticas y SEO. La computadora saca 100 en todo. La carga inicial pesa unos 1,3 MB.
- **Fotos:** en WebP, en varios tamaños según el dispositivo, con carga diferida.
- **Archivos con huella:** los nombres llevan un código (p. ej. `logo-rucha.133d2c99.svg`) para que el caché sea permanente. Si se reemplaza un archivo, cambia su nombre.
- **SEO:**
  - Título: "Daniela Amaro · Modelo y creadora de contenido en Barquisimeto".
  - Descripción, canonical y Open Graph apuntan a `https://amarodaniela.com/`. La vista previa al compartir usa `assets/og-image.jpg`.
  - Datos estructurados JSON-LD (Person): Instagram, teléfono, Barquisimeto/Lara y reconocimientos.
  - También están `robots.txt`, `sitemap.xml` y `apple-touch-icon.png`.
- **`vercel.json`:** redirige daniela-amaro.vercel.app y www.amarodaniela.com hacia amarodaniela.com, pone caché permanente en `/assets/` y agrega encabezados de seguridad.
- **Cómo se fabricaba:**
  - El diseño se editaba en Claude Design (`Main.dc.html`).
  - Luego dos scripts lo convertían en la web final: `build.py` (de diseño a HTML) y `optimize.py` (imágenes, fuentes, SEO, nombres con código).
  - Ambos scripts tienen rutas fijas de la sesión vieja, así que sirven de referencia.
  - **Para cambios futuros lo más simple es editar directamente `index.html` en el repositorio** y subirlo.
- **Bugs ya resueltos, por si reaparecen:**
  - **Scroll trabado:** era `overflow-x:hidden` en el contenedor; se cambió a `overflow-x:clip`.
  - **Pie de página invisible al final en el celular:** la animación de aparición no se disparaba; se le quitó la animación al pie.
  - **Video del inicio sustituido por foto en iPhone:** pasaba con ahorro de batería o "reducir movimiento"; ahora se reproduce al primer toque.

---

## 7. Pendientes e ideas

1. **Activar Vercel Analytics** (Vercel → Analytics → Enable). Mientras tanto, la web muestra un error interno invisible que no afecta nada.
2. **Google Search Console:** dar de alta amarodaniela.com, agregar el código de verificación a la web y enviar el sitemap.
3. **Confirmar con Daniela el periodo de las métricas** (90 días) y actualizar las cifras periódicamente.
4. **Pruebas sociales:** preguntarle a Daniela por frases de marcas o resultados de cada reel (p. ej. "+12K vistas"). Convencen más que solo los logos.
5. Borrar el kit viejo de Adobe Fonts `ajz6lrn`.
6. Cuando haya reels o marcas nuevas, se cambian el video, el póster, el logo y el enlace en `index.html`.

---

## 8. Otros trabajos de Carlos con Daniela (contexto)

- Edición de sus reels de Instagram (efectos, subtítulos): look sutil, femenino y profesional; texto blanco + champagne, sin letras enormes. Los memes los agrega Daniela.
- Carruseles de Instagram para su marca personal (en Claude Design), usando la identidad de esta web (fuentes y colores) con un estilo limpio.

---

## 9. Qué hay en la carpeta `_proyecto/` de este repositorio

- **`diseno-claude-design/`:** `Main.dc.html` y `canvas.json`, la fuente del diseño editable.
- **`scripts/`:** `build.py` y `optimize.py`, de referencia.
- **`originales/`:**
  - El PDF del media kit.
  - Fotos en alta calidad.
  - Video original del inicio (los reels ya están en `assets/`).
  - Logos SVG de las marcas.
  - Imágenes del perfil.
