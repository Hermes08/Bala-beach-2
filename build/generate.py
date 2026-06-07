# -*- coding: utf-8 -*-
"""Static multilingual site generator for Bala Beach / María Chiquita."""
import os, json, html, datetime
from content import (SITE, LANGS, LANG_META, DEFAULT_LANG, GEO_MAP, IMAGES,
                     REVIEWS, C, FOOTER_KEYWORDS)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FULL = SITE["domain"] + SITE["base"]            # https://hermes08.github.io/Bala-beach-2
BASE = SITE["base"]                              # /Bala-beach-2
TODAY = datetime.date.today().isoformat()

ICONS = {
    "wifi": '<path d="M5 13a10 10 0 0 1 14 0"/><path d="M8.5 16.5a5 5 0 0 1 7 0"/><path d="M2 8.82a15 15 0 0 1 20 0"/><line x1="12" y1="20" x2="12.01" y2="20"/>',
    "ac": '<path d="M9.59 4.59A2 2 0 1 1 11 8H2m10.59 11.41A2 2 0 1 0 14 16H2m15.73-8.27A2.5 2.5 0 1 1 19.5 12H2"/>',
    "kitchen": '<path d="M3 11h18"/><path d="M12 3v8"/><path d="M5 11v10"/><path d="M19 11v10"/><path d="M9 7V3"/><path d="M15 7V3"/>',
    "tv": '<rect x="2" y="7" width="20" height="13" rx="2"/><polyline points="17 2 12 7 7 2"/>',
    "parking": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 17V7h4a3 3 0 0 1 0 6H9"/>',
    "bed": '<path d="M2 4v16"/><path d="M2 8h18a2 2 0 0 1 2 2v10"/><path d="M2 17h20"/><path d="M6 8V4h12"/>',
    "check": '<polyline points="20 6 9 17 4 12"/>',
    "x": '<line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>',
    "whatsapp": '<path d="M3 21l1.65-3.8a9 9 0 1 1 3.4 2.9L3 21"/><path d="M9 10a.5.5 0 0 0 1 0V9a.5.5 0 0 0-1 0v1a5 5 0 0 0 5 5h1a.5.5 0 0 0 0-1h-1a.5.5 0 0 0 0 1"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "star": '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "arrow": '<line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/>',
}

def icon(name, size=24, cls="ic"):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" '
            f'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')

def e(s):
    return html.escape(str(s), quote=True)

def lang_url(lang):
    return f"{FULL}/{lang}/"

def wa_link(lang):
    msg = C[lang]["wa_msg"]
    from urllib.parse import quote
    return f"https://wa.me/{SITE['whatsapp']}?text={quote(msg)}"

# ---------------- structured data ----------------
def jsonld(lang):
    t = C[lang]
    blocks = []
    blocks.append({
        "@context": "https://schema.org", "@type": "VacationRental",
        "name": SITE["property_name"], "headline": t["hero"]["title"],
        "description": t["meta_desc"],
        "url": lang_url(lang), "inLanguage": lang,
        "image": [IMAGES["hero"][0], IMAGES["hero"][1], IMAGES["gallery"][3][0]],
        "address": {"@type": "PostalAddress", "addressLocality": SITE["locality"],
                    "addressRegion": SITE["region"], "addressCountry": SITE["country"]},
        "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lng"]},
        "priceRange": f"${SITE['price_low']} - ${SITE['price_high']}",
        "telephone": SITE["phone_display"],
        "amenityFeature": [
            {"@type": "LocationFeatureSpecification", "name": "Private Beach Access", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Starlink WiFi", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Air Conditioning", "value": True},
            {"@type": "LocationFeatureSpecification", "name": "Swimming Pool", "value": True},
        ],
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": SITE["rating"],
                            "reviewCount": SITE["review_count"], "bestRating": "5"},
    })
    blocks.append({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}}
                       for q, a in t["faq"]["items"]],
    })
    blocks.append({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": FULL + "/"},
            {"@type": "ListItem", "position": 2, "name": t["hero"]["title"], "item": lang_url(lang)},
        ],
    })
    return "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
        for b in blocks)

def hreflang_tags(current):
    tags = [f'<link rel="alternate" hreflang="x-default" href="{FULL}/" />']
    for l in LANGS:
        tags.append(f'<link rel="alternate" hreflang="{LANG_META[l]["hreflang"]}" href="{lang_url(l)}" />')
    return "\n  ".join(tags)

# ---------------- components ----------------
def lang_switcher(current):
    opts = []
    for l in LANGS:
        m = LANG_META[l]
        active = " active" if l == current else ""
        opts.append(f'<a class="lang-opt{active}" href="{BASE}/{l}/" hreflang="{m["hreflang"]}" '
                    f'lang="{m["hreflang"]}">{m["flag"]} {m["name"]}</a>')
    return (f'<div class="lang-switch">'
            f'<button class="lang-btn" aria-haspopup="true" aria-expanded="false">'
            f'{icon("globe",18)} <span>{LANG_META[current]["flag"]} {LANG_META[current]["name"]}</span></button>'
            f'<div class="lang-menu">{"".join(opts)}</div></div>')

def header(lang):
    t = C[lang]
    nav = t["nav"]
    links = "".join(
        f'<a href="#{sec}">{e(nav[sec])}</a>'
        for sec in ["amenities", "gallery", "tours", "reviews", "faq"])
    return f'''<header class="site-head" id="top">
  <div class="wrap head-inner">
    <a class="brand" href="{BASE}/{lang}/">
      <span class="brand-mark">BALA</span><span class="brand-sub">BEACH · PANAMÁ</span>
    </a>
    <nav class="nav-links">{links}</nav>
    <div class="head-actions">
      {lang_switcher(lang)}
      <a class="btn btn-sm btn-primary" href="{wa_link(lang)}" target="_blank" rel="noopener">{e(nav["book"])}</a>
    </div>
    <button class="burger" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
  <nav class="mobile-nav">{links}<a class="btn btn-primary" href="{wa_link(lang)}" target="_blank" rel="noopener">{e(nav["book"])}</a></nav>
</header>'''

def hero(lang):
    t = C[lang]["hero"]
    slides = "".join(
        f'<div class="slide{" on" if i==0 else ""}" style="background-image:url(\'{s}\')"></div>'
        for i, s in enumerate(IMAGES["hero"]))
    dots = "".join(f'<button class="dot{" on" if i==0 else ""}" data-i="{i}" aria-label="Slide {i+1}"></button>'
                   for i in range(len(IMAGES["hero"])))
    return f'''<section class="hero" id="home">
  <div class="hero-bg">{slides}<div class="hero-veil"></div></div>
  <div class="wrap hero-inner">
    <span class="badge">{e(t["badge"])}</span>
    <h1>{e(t["title"])}</h1>
    <p class="hero-sub">{e(t["sub"])}</p>
    <div class="hero-cta">
      <a class="btn btn-primary btn-lg" href="{wa_link(lang)}" target="_blank" rel="noopener">{icon("whatsapp",20)} {e(t["cta"])}</a>
      <a class="btn btn-ghost btn-lg" href="{SITE["airbnb"]}" target="_blank" rel="noopener">{e(t["cta2"])}</a>
    </div>
    <div class="hero-price">{e(t["price"])} · ★ {SITE["rating"]}</div>
  </div>
  <div class="hero-dots">{dots}</div>
</section>'''

def trustbar(lang):
    items = "".join(f'<div class="trust-item">{icon("check",18)} <span>{e(x)}</span></div>'
                    for x in C[lang]["trust"])
    return f'<div class="trustbar"><div class="wrap trust-inner">{items}</div></div>'

def features(lang):
    f = C[lang]["features"]
    cards = "".join(
        f'<div class="feat-card"><div class="feat-ic">{icon(k,28)}</div>'
        f'<h3>{e(title)}</h3><p>{e(desc)}</p></div>'
        for k, title, desc in f["items"])
    return f'''<section class="section" id="amenities">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">{e(C[lang]["nav"]["amenities"])}</span>
      <h2>{e(f["title"])}</h2><p>{e(f["sub"])}</p></div>
    <div class="feat-grid">{cards}</div>
  </div>
</section>'''

def gallery(lang):
    g = C[lang]["gallery"]
    imgs = "".join(
        f'<a class="g-item" href="{src}" target="_blank" rel="noopener">'
        f'<img loading="lazy" src="{src}" alt="{e(alt)} — {SITE["property_name"]} {SITE["locality"]}" /></a>'
        for src, alt in IMAGES["gallery"])
    return f'''<section class="section section-alt" id="gallery">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">{e(C[lang]["nav"]["gallery"])}</span>
      <h2>{e(g["title"])}</h2><p>{e(g["sub"])}</p></div>
    <div class="gallery">{imgs}</div>
  </div>
</section>'''

def why(lang):
    w = C[lang]["why"]
    rows = ""
    for label, d, o in w["rows"]:
        dcell = f'<td class="yes">{icon("check",18)}</td>'
        ocell = f'<td class="no">{icon("x",18)}</td>'
        rows += f'<tr><td class="benefit">{e(label)}</td>{dcell}{ocell}</tr>'
    return f'''<section class="section" id="why">
  <div class="wrap narrow">
    <div class="sec-head"><span class="eyebrow">Direct booking</span>
      <h2>{e(w["title"])}</h2><p>{e(w["sub"])}</p></div>
    <div class="compare">
      <table>
        <thead><tr><th></th><th class="col-direct">{e(w["direct"])}</th><th>{e(w["ota"])}</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </div>
</section>'''

def tours(lang):
    tr = C[lang]["tours"]
    cards = "".join(
        f'<article class="tour-card"><div class="tour-img" style="background-image:url(\'{IMAGES["tours"][img]}\')"></div>'
        f'<div class="tour-body"><h3>{e(title)}</h3><p>{e(desc)}</p></div></article>'
        for title, desc, img in tr["items"])
    return f'''<section class="section section-alt" id="tours">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">{e(C[lang]["nav"]["tours"])}</span>
      <h2>{e(tr["title"])}</h2><p>{e(tr["sub"])}</p></div>
    <div class="tour-grid">{cards}</div>
  </div>
</section>'''

def reviews(lang):
    r = C[lang]["reviews"]
    cards = ""
    for author, loc, flag, rating, text in REVIEWS:
        stars = "".join(icon("star",14,"star") for _ in range(rating))
        cards += (f'<div class="rev-card"><div class="rev-stars">{stars}</div>'
                  f'<p class="rev-text">“{e(text)}”</p>'
                  f'<div class="rev-author"><span class="rev-flag">{flag}</span>'
                  f'<div><strong>{e(author)}</strong><span>{e(loc)}</span></div></div></div>')
    return f'''<section class="section" id="reviews">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">{e(r["source"])}</span>
      <h2>{e(r["title"])}</h2><p>{e(r["sub"])}</p>
      <div class="rev-score">★ {SITE["rating"]} · {SITE["review_count"]} reviews</div></div>
    <div class="rev-grid">{cards}</div>
  </div>
</section>'''

def faq(lang):
    f = C[lang]["faq"]
    items = ""
    for q, a in f["items"]:
        items += (f'<details class="faq-item"><summary>{e(q)}'
                  f'<span class="faq-plus">+</span></summary><p>{e(a)}</p></details>')
    return f'''<section class="section section-alt" id="faq">
  <div class="wrap narrow">
    <div class="sec-head"><span class="eyebrow">FAQ</span>
      <h2>{e(f["title"])}</h2><p>{e(f["sub"])}</p></div>
    <div class="faq">{items}</div>
  </div>
</section>'''

def location(lang):
    loc = C[lang]["location"]
    maps = f"https://www.google.com/maps/dir/?api=1&destination={SITE['lat']},{SITE['lng']}"
    embed = f"https://maps.google.com/maps?q={SITE['lat']},{SITE['lng']}&z=11&output=embed"
    return f'''<section class="section" id="location">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">{icon("pin",16)} {SITE["locality"]}, {SITE["region"]}</span>
      <h2>{e(loc["title"])}</h2><p>{e(loc["sub"])}</p></div>
    <div class="map-box">
      <iframe title="Map" loading="lazy" src="{embed}" allowfullscreen></iframe>
    </div>
    <div class="map-cta"><a class="btn btn-primary" href="{maps}" target="_blank" rel="noopener">{icon("pin",18)} {e(loc["directions"])}</a></div>
  </div>
</section>'''

def newsletter(lang):
    n = C[lang]["newsletter"]
    return f'''<section class="cta-band">
  <div class="wrap narrow cta-inner">
    <h2>{e(n["title"])}</h2><p>{e(n["sub"])}</p>
    <form class="nl-form" onsubmit="return false">
      <input type="email" placeholder="{e(n["placeholder"])}" aria-label="email" required />
      <button class="btn btn-primary" type="submit">{e(n["button"])}</button>
    </form>
    <small>{e(n["disclaimer"])}</small>
  </div>
</section>'''

def footer(lang):
    f = C[lang]["footer"]
    nav = C[lang]["nav"]
    links = "".join(f'<li><a href="#{s}">{e(nav[s])}</a></li>'
                    for s in ["amenities", "gallery", "tours", "reviews", "faq"])
    kw = "".join(f'<a href="{wa_link(lang)}" target="_blank" rel="noopener">{e(k)}</a>'
                 for k in FOOTER_KEYWORDS)
    langs = "".join(f'<a href="{BASE}/{l}/" hreflang="{l}">{LANG_META[l]["flag"]} {LANG_META[l]["name"]}</a>'
                    for l in LANGS)
    return f'''<footer class="site-foot">
  <div class="wrap foot-grid">
    <div class="foot-about">
      <span class="brand-mark light">BALA BEACH</span>
      <p>{e(f["about"])}</p>
      <a class="foot-phone" href="https://wa.me/{SITE["whatsapp"]}" target="_blank" rel="noopener">{icon("phone",16)} {SITE["phone_display"]}</a>
    </div>
    <div class="foot-col"><h4>{e(f["links"])}</h4><ul>{links}</ul></div>
    <div class="foot-col"><h4>{e(f["contact"])}</h4>
      <a class="btn btn-primary btn-sm" href="{wa_link(lang)}" target="_blank" rel="noopener">{icon("whatsapp",16)} WhatsApp</a>
      <div class="foot-langs">{langs}</div>
    </div>
  </div>
  <div class="foot-kw"><div class="wrap"><span>{e(f["keywords_title"])}:</span> {kw}</div></div>
  <div class="foot-bottom"><div class="wrap">© {datetime.date.today().year} {SITE["brand"]} · {SITE["locality"]}, {SITE["region"]}, {SITE["country_name"]}. {e(f["rights"])}</div></div>
</footer>'''

def float_wa(lang):
    return (f'<a class="fab-wa" href="{wa_link(lang)}" target="_blank" rel="noopener" '
            f'aria-label="WhatsApp">{icon("whatsapp",30)}</a>')

# ---------------- page ----------------
def page(lang):
    t = C[lang]
    m = LANG_META[lang]
    body = "\n".join([
        header(lang), hero(lang), trustbar(lang), features(lang), gallery(lang),
        why(lang), tours(lang), reviews(lang), faq(lang), location(lang),
        newsletter(lang), footer(lang), float_wa(lang),
    ])
    return f'''<!DOCTYPE html>
<html lang="{m["hreflang"]}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{e(t["title"])}</title>
  <meta name="description" content="{e(t["meta_desc"])}" />
  <meta name="keywords" content="{e(t["keywords"])}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="author" content="{SITE["brand"]}" />
  <link rel="canonical" href="{lang_url(lang)}" />
  {hreflang_tags(lang)}
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="{m["locale"]}" />
  <meta property="og:site_name" content="{SITE["brand"]}" />
  <meta property="og:title" content="{e(t["title"])}" />
  <meta property="og:description" content="{e(t["meta_desc"])}" />
  <meta property="og:url" content="{lang_url(lang)}" />
  <meta property="og:image" content="{IMAGES["og"]}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{e(t["title"])}" />
  <meta name="twitter:description" content="{e(t["meta_desc"])}" />
  <meta name="twitter:image" content="{IMAGES["og"]}" />
  <meta name="theme-color" content="#0a2a43" />
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230a2a43'/%3E%3Ctext x='16' y='22' font-size='17' font-family='Georgia' fill='%23f5b942' text-anchor='middle'%3EB%3C/text%3E%3C/svg%3E" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{BASE}/assets/css/styles.css" />
  {jsonld(lang)}
</head>
<body data-lang="{lang}">
{body}
<script src="{BASE}/assets/js/main.js" defer></script>
</body>
</html>'''

# ---------------- root redirect ----------------
def root_redirect():
    geo = json.dumps(GEO_MAP)
    langs = json.dumps(LANGS)
    links = "".join(f'<a href="{BASE}/{l}/">{LANG_META[l]["flag"]} {LANG_META[l]["name"]}</a>'
                    for l in LANGS)
    hl = hreflang_tags("x-default")
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{SITE["brand"]} — Beachfront Vacation Rental, María Chiquita, Colón, Panama</title>
  <meta name="description" content="Luxury beachfront vacation rental at Bala Beach, María Chiquita, Colón, Panama. Available in English, Español, Deutsch, Português, Français." />
  <link rel="canonical" href="{FULL}/" />
  {hl}
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&display=swap" rel="stylesheet" />
  <style>
    body{{font-family:Manrope,sans-serif;margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;
    background:#0a2a43 url('{IMAGES["hero"][1]}') center/cover;color:#fff;text-align:center}}
    .ov{{position:fixed;inset:0;background:linear-gradient(180deg,rgba(10,42,67,.7),rgba(10,42,67,.9))}}
    .box{{position:relative;z-index:1;padding:2rem}}
    .mark{{font-size:.8rem;letter-spacing:.3em;color:#f5b942;font-weight:800}}
    h1{{font-size:1.6rem;font-weight:800;margin:.6rem 0}}
    p{{opacity:.85;margin:0 0 1.4rem}}
    .sp{{width:34px;height:34px;border:3px solid rgba(255,255,255,.3);border-top-color:#f5b942;border-radius:50%;
    margin:1rem auto;animation:spin 1s linear infinite}}
    @keyframes spin{{to{{transform:rotate(360deg)}}}}
    .langs{{display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center;margin-top:1rem}}
    .langs a{{color:#fff;text-decoration:none;border:1px solid rgba(255,255,255,.35);padding:.5rem .9rem;
    border-radius:999px;font-weight:700;font-size:.9rem;transition:.2s}}
    .langs a:hover{{background:#f5b942;color:#0a2a43;border-color:#f5b942}}
  </style>
  <script>
    (function(){{
      var GEO={geo}, LANGS={langs}, DEF="{DEFAULT_LANG}", BASE="{BASE}";
      function go(l){{ if(LANGS.indexOf(l)<0) l=DEF; location.replace(BASE+"/"+l+"/"); }}
      // 1) remembered choice
      try{{ var s=localStorage.getItem("bb_lang"); if(s){{ go(s); return; }} }}catch(_e){{}}
      // 2) browser language (instant)
      var nav=(navigator.language||navigator.userLanguage||DEF).slice(0,2).toLowerCase();
      var browserHit = LANGS.indexOf(nav)>=0 ? nav : null;
      // 3) IP geolocation (country -> language), fall back to browser/default
      var done=false;
      var to=setTimeout(function(){{ if(!done){{ done=true; go(browserHit||DEF); }} }}, 1500);
      try{{
        fetch("https://ipapi.co/json/").then(function(r){{return r.json();}}).then(function(d){{
          if(done) return; done=true; clearTimeout(to);
          var cc=(d&&d.country_code||"").toUpperCase(), pick=null;
          for(var l in GEO){{ if(GEO[l].indexOf(cc)>=0){{ pick=l; break; }} }}
          go(pick||browserHit||DEF);
        }}).catch(function(){{ if(!done){{ done=true; clearTimeout(to); go(browserHit||DEF); }} }});
      }}catch(_e){{ if(!done){{ done=true; clearTimeout(to); go(browserHit||DEF); }} }}
    }})();
  </script>
</head>
<body>
  <div class="ov"></div>
  <div class="box">
    <div class="mark">BALA BEACH · PANAMÁ</div>
    <h1>Beachfront Vacation Rental</h1>
    <p>María Chiquita, Colón — Caribbean Panama</p>
    <div class="sp"></div>
    <noscript><p>Choose your language:</p></noscript>
    <div class="langs">{links}</div>
  </div>
</body>
</html>'''

# ---------------- sitemap & robots ----------------
def sitemap():
    urls = []
    def alts():
        a = [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{FULL}/"/>']
        for l in LANGS:
            a.append(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{lang_url(l)}"/>')
        return "\n".join(a)
    # root
    urls.append(f'''  <url>
    <loc>{FULL}/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
{alts()}
  </url>''')
    for l in LANGS:
        urls.append(f'''  <url>
    <loc>{lang_url(l)}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
{alts()}
  </url>''')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(urls) + "\n</urlset>\n")

def robots():
    return (f"User-agent: *\nAllow: /\n\nSitemap: {FULL}/sitemap.xml\n")

# ---------------- write ----------------
def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

if __name__ == "__main__":
    for l in LANGS:
        write(f"{l}/index.html", page(l))
    write("index.html", root_redirect())
    write("sitemap.xml", sitemap())
    write("robots.txt", robots())
    write(".nojekyll", "")
    print("done")
