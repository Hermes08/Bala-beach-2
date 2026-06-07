# Bala Beach — Beachfront Vacation Rental (María Chiquita, Colón, Panamá)

Sitio **estático multi-idioma** optimizado para SEO y GitHub Pages.
Una página completa por idioma (mejor ranking por idioma que un SPA), detección por **geolocalización**, `hreflang` recíproco, `sitemap.xml`, datos estructurados (JSON-LD) y Core Web Vitals altos (CSS propio, sin frameworks pesados).

🔗 **Live:** https://hermes08.github.io/Bala-beach-2/

## Idiomas
`/en/` · `/es/` · `/de/` · `/pt/` · `/fr/` — el `index.html` raíz detecta el idioma por **IP (ipapi.co)** con respaldo en `navigator.language` y recuerda la elección en `localStorage`.

## Estructura
```
index.html                  Splash + redirect por geolocalización (x-default)
en|es|de|pt|fr/index.html   Páginas completas por idioma
assets/css/styles.css       Tema premium (océano/turquesa/oro/arena)
assets/js/main.js           Carrusel, menú idioma, nav móvil, scroll-reveal
sitemap.xml                 Todas las URLs con alternates hreflang
robots.txt
build/content.py            Diccionario de contenido (5 idiomas) <- editar aquí el texto
build/generate.py           Generador estático -> python3 build/generate.py
```

## Cómo editar y regenerar
1. Edita textos en `build/content.py` o estilos en `assets/css/styles.css`.
2. Regenera: `cd build && python3 generate.py`
3. Commit + push a la rama `gh-pages` -> GitHub Pages publica automáticamente.

## SEO incluido
- `hreflang` (x-default + 5 idiomas) recíproco en todas las páginas
- `canonical` por idioma + URLs indexables separadas
- JSON-LD: `VacationRental` + `FAQPage` + `BreadcrumbList`
- Open Graph + Twitter Card por idioma/locale
- `sitemap.xml` con `xhtml:link` alternates + `robots.txt`
- Meta title/description/keywords localizados por mercado

Ver `DESIGNER-BRIEF.md` para mejorar el diseño 100%.
