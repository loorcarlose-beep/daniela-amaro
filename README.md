# Daniela Amaro · Landing

Sitio estático (HTML + CSS + JS, sin compilación). Todo está en `index.html` y la carpeta `assets/`.

## Publicar en Vercel

### Opción A: desde la Terminal de tu Mac (la más rápida)
1. Descomprime esta carpeta.
2. Abre la Terminal y entra a la carpeta: `cd ruta/a/daniela-amaro-web`
3. Ejecuta: `npx vercel`
4. La primera vez te pedirá iniciar sesión en Vercel (se abre el navegador). Acepta las opciones por defecto.
5. Para publicar la versión definitiva: `npx vercel --prod`

### Opción B: con GitHub
1. Crea un repositorio en GitHub y sube el contenido de esta carpeta.
2. En vercel.com → Add New → Project → importa ese repositorio.
3. Framework Preset: "Other". No hace falta comando de build ni carpeta de salida.
4. Cada cambio que subas a GitHub se publica solo.

## Tipografías
- Sora se carga desde Google Fonts.
- Kepler Std se usa si está instalada en el dispositivo; si no, se muestra Cormorant Garamond.
  Para que todos vean Kepler, crea un kit web en Adobe Fonts (fonts.adobe.com → Web Projects),
  agrega Kepler Std y pega el `<link>` del kit dentro de `<head>` en `index.html`.
