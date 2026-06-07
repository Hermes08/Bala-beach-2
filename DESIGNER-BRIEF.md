# 🎨 Designer Brief — Bala Beach Rentals (revamp 100%)

> **Objetivo:** llevar este sitio de "muy bueno" a "world-class luxury rental".
> El sitio ya está **funcional, multi-idioma, SEO-ready y desplegado**. Tu trabajo es elevar el diseño visual, no reconstruir la arquitectura.

---

## 🔗 Enlaces

| Recurso | URL |
|---|---|
| **Live (auto-idioma por geo)** | https://hermes08.github.io/Bala-beach-2/ |
| 🇺🇸 English | https://hermes08.github.io/Bala-beach-2/en/ |
| 🇵🇦 Español | https://hermes08.github.io/Bala-beach-2/es/ |
| 🇩🇪 Deutsch | https://hermes08.github.io/Bala-beach-2/de/ |
| 🇧🇷 Português | https://hermes08.github.io/Bala-beach-2/pt/ |
| 🇫🇷 Français | https://hermes08.github.io/Bala-beach-2/fr/ |
| Repo (rama `gh-pages`) | https://github.com/Hermes08/Bala-beach-2/tree/gh-pages |

---

## 🧱 Cómo está construido (importante antes de tocar nada)

- **Sitio estático**, sin React ni build pesado. HTML generado por `build/generate.py` a partir del contenido en `build/content.py`.
- **No edites el HTML directamente** — se regenera y perderías los cambios. Edita:
  - **Texto / traducciones →** `build/content.py`
  - **Diseño / estilos →** `assets/css/styles.css` (este SÍ es la fuente de verdad del look)
  - **Interacción →** `assets/js/main.js`
- Tras editar contenido: `cd build && python3 generate.py` y commit a `gh-pages`.
- Estilos: editas el CSS y commiteas — no requiere regenerar.

### Design tokens actuales (`:root` en styles.css)
```
--ink:#0a2a43   (azul océano profundo)   --teal:#12a3a8 (turquesa caribe)
--gold:#f5b942  (oro cálido / CTA accent) --coral:#ff6f61
--sand:#f6f1e7  (arena)                   --serif: Cormorant Garamond
--sans: Manrope
```

---

## ✅ Lo que YA funciona (no romper)
- Detección de idioma por **geolocalización IP** + fallback de navegador + memoria en `localStorage`.
- `hreflang` recíproco, `canonical`, `sitemap.xml`, JSON-LD (`VacationRental`+`FAQPage`+`BreadcrumbList`), OG/Twitter por idioma. **Esto es lo que hace que rankee por idioma — no lo elimines.**
- Carrusel hero, menú de idioma, nav móvil, FAQ accordion, scroll-reveal, botón flotante de WhatsApp.
- Responsive (breakpoints 900 / 760 px).

---

## 🎯 Mejoras prioritarias (orden sugerido)

### P1 — Impacto alto / esfuerzo bajo
1. **Fotografía real de alta resolución.** Las imágenes actuales son de ImgBB comprimidas. Reemplazar por shots editoriales del apartamento (atardecer en el balcón, detalle de textiles, drone de la playa). Servirlas en **WebP/AVIF** + `srcset` responsive para Core Web Vitals.
2. **Hero:** añadir un sutil `Ken Burns` (zoom lento) ya presente — reforzarlo con un degradado inferior más rico y un micro-scroll-cue animado. Considerar **video loop** de la playa (mp4 muted, poster fallback) en desktop.
3. **Tipografía:** afinar escala. El H1 Cormorant se ve muy bien; ajustar `letter-spacing` y `line-height` en móvil para que no se corte feo.

### P2 — Refinamiento de marca
4. **Logo real** (actualmente es solo el wordmark "BALA BEACH"). Diseñar un monograma/favicon profesional (hoy es un SVG inline básico con la "B").
5. **Sistema de iconografía** consistente — los iconos son SVG inline tipo Feather; mantener stroke uniforme o cambiar a un set premium.
6. **Paleta:** validar contraste AA/AAA (el texto blanco sobre hero pasa, pero revisar `--slate` sobre arena).
7. **Microinteracciones:** hover en cards (ya hay lift), añadir transiciones a la galería tipo lightbox real (hoy abre la imagen en pestaña nueva).

### P3 — Conversión
8. **Sticky booking bar** en móvil (precio + botón WhatsApp siempre visible al hacer scroll).
9. **Sección de disponibilidad / calendario** (la app React original tenía iCal de Airbnb — se puede reincorporar como widget embebido).
10. **Prueba social:** badges "Superhost", logos Airbnb/Booking, contador de reseñas en vivo.
11. **Galería lightbox** con navegación teclado/swipe.

### P4 — Contenido SEO
12. Crear **páginas de blog/guía por idioma** (Portobelo, buceo, qué hacer en Colón) — enlaces internos potencian el ranking. Replicar el patrón `/<lang>/` con su propio `hreflang`.
13. Añadir **`ImageObject` schema** y alt text descriptivo localizado (hoy alt está en EN para todas).

---

## 📐 Entregables sugeridos del diseñador
- [ ] Set de fotografía editorial optimizada (WebP/AVIF + srcset)
- [ ] Logo + sistema de favicon (16/32/180/512)
- [ ] Ajustes de `styles.css` (tipografía, espaciado, microinteracciones)
- [ ] Lightbox de galería (`main.js`)
- [ ] Sticky booking bar móvil
- [ ] (Opcional) plantilla de blog multi-idioma

---

## ⚠️ Reglas de oro
1. **No tocar** la estructura de carpetas `/<lang>/` ni los tags `hreflang`/`canonical`/JSON-LD → es el motor de ranking por idioma.
2. **Mantener todo en los 5 idiomas** — si añades una sección, agrégala en `content.py` para los 5.
3. **No introducir frameworks pesados** (Bootstrap/Tailwind CDN/jQuery) → matarían el rendimiento. CSS vanilla es intencional.
4. Probar siempre en móvil real + Lighthouse antes de commitear.
5. WhatsApp `+507 6761-0315` y Airbnb listing son los CTAs principales — no enterrarlos.

> Cualquier duda sobre el pipeline de build, leer `README.md`.
