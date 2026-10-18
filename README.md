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
- Sora va incluida en `assets/fonts`.
- Kepler Std se carga desde el kit web de Adobe Fonts `ajz6lrn` (dominios: daniela-amaro.vercel.app, *.vercel.app, localhost).
  Si conectas un dominio propio, agrégalo al kit en fonts.adobe.com → Web Projects.
  Mientras carga, o si el kit falla, se muestra Cormorant Garamond.

## Estadísticas
- Vercel Web Analytics: en vercel.com → proyecto → Analytics → Enable.
