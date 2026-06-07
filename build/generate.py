# -*- coding: utf-8 -*-
"""Static multilingual EDITORIAL site generator for Bala Beach.
Implements the design handoff (Bala Beach.html + bala.css + app.js), editorial
palette only, ported into per-language indexable pages (SEO: hreflang, canonical,
JSON-LD, sitemap). Run: python3 build/generate.py
"""
import os, json, html, datetime
from urllib.parse import quote
from content import (SITE, LANGS, LANG_META, DEFAULT_LANG, GEO_MAP, IMAGES,
                     REVIEWS, C, SEO, FOOTER_KEYWORDS)
from guides import GUIDES, GUIDE_ORDER, GUIDES_LABEL

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUSTOM = SITE.get("custom_domain", "").strip()
if CUSTOM:
    FULL = "https://" + CUSTOM        # apex domain, served at root
    BASE = ""                          # root-relative asset/link paths
else:
    FULL = SITE["domain"] + SITE["base"]
    BASE = SITE["base"]
TODAY = datetime.date.today().isoformat()

import hashlib
def asset_ver(relpath):
    """Short content hash for cache-busting (?v=...) so updates bypass immutable cache."""
    try:
        with open(os.path.join(ROOT, relpath), "rb") as f:
            return hashlib.md5(f.read()).hexdigest()[:8]
    except OSError:
        return "1"
CSS_VER = asset_ver("assets/css/styles.css")
JS_VER = asset_ver("assets/js/main.js")

def img_src(slug, w=1600):
    return f"{BASE}/assets/img/{slug}-{w}.webp"
def img_srcset(slug):
    return f"{BASE}/assets/img/{slug}-800.webp 800w, {BASE}/assets/img/{slug}-1600.webp 1600w"

# ---- icon set (ported from design app.js) ----
I = {
    "wifi": '<path d="M5 12.5a10 10 0 0 1 14 0M8 15.5a6 6 0 0 1 8 0M11 18.5a1.5 1.5 0 0 1 2 0"/><circle cx="12" cy="19" r=".4" fill="currentColor" stroke="none"/>',
    "ac": '<rect x="3" y="5" width="18" height="9" rx="1.5"/><path d="M7 18c0 1.2 1 1.5 1 2.5M12 18c0 1.2 1 1.5 1 2.5M17 18c0 1.2 1 1.5 1 2.5M6 11h.01M9 11h6"/>',
    "kitchen": '<path d="M7 3v6a2 2 0 0 0 2 2 2 2 0 0 0 2-2V3M9 3v8M9 11v10M16 3c-1.5 0-2.5 2-2.5 5s1 4 2.5 4 2.5-1 2.5-4-1-5-2.5-5zM16 16v5"/>',
    "tv": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M8 20h8M12 16v4"/>',
    "parking": '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 16V8h3.5a2.5 2.5 0 0 1 0 5H9"/>',
    "bed": '<path d="M3 18v-6a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v6M3 14h18M7 10V8a1 1 0 0 1 1-1h3M3 18v2M21 18v2"/>',
    "shield": '<path d="M12 3l7 3v5c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9.5 12l1.8 1.8L15 10"/>',
    "waves": '<path d="M2 8c2 0 2 1.5 4 1.5S8 8 10 8s2 1.5 4 1.5S16 8 18 8s2 1.5 4 1.5M2 13c2 0 2 1.5 4 1.5S8 13 10 13s2 1.5 4 1.5S16 13 18 13s2 1.5 4 1.5M2 18c2 0 2 1.5 4 1.5S8 18 10 18s2 1.5 4 1.5"/>',
    "pool": '<path d="M3 20c1.5 0 1.5-1 3-1s1.5 1 3 1 1.5-1 3-1 1.5 1 3 1 1.5-1 3-1M7 16V6a2 2 0 0 1 4 0v10M17 16V6a2 2 0 0 0-4 0M7 9h6"/>',
    "gold": '<path d="M12 3l2.5 5.5L20 9l-4 4 1 6-5-3-5 3 1-6-4-4 5.5-.5z"/>',
    "star": '<path d="M12 3l2.6 5.7 6.2.7-4.6 4.2 1.3 6.1L12 16.8 6.5 19.7l1.3-6.1L3.2 9.4l6.2-.7z"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "chevron": '<path d="M6 9l6 6 6-6"/>',
    "expand": '<path d="M8 3H5a2 2 0 0 0-2 2v3M16 3h3a2 2 0 0 1 2 2v3M21 16v3a2 2 0 0 1-2 2h-3M3 16v3a2 2 0 0 0 2 2h3"/>',
    "pin": '<path d="M12 21s-7-5.5-7-11a7 7 0 0 1 14 0c0 5.5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "car": '<path d="M5 11l1.5-4.5A2 2 0 0 1 8.4 5h7.2a2 2 0 0 1 1.9 1.5L19 11M5 11h14v5H5zM7 16v1.5M17 16v1.5M7 13h.5M16.5 13h.5"/>',
    "whatsapp": '<path d="M12 3a9 9 0 0 0-7.7 13.6L3 21l4.6-1.2A9 9 0 1 0 12 3z"/><path d="M8.5 8.5c-.3 0-.6.1-.8.4-.3.3-.9.9-.9 2.1s.9 2.4 1 2.6c.1.2 1.8 2.9 4.5 3.9 2.2.9 2.7.7 3.2.7.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2-.1-.1-.3-.2-.6-.4l-1.5-.7c-.2-.1-.4-.1-.6.1l-.6.8c-.1.2-.3.2-.5.1-.7-.3-1.4-.6-2.3-1.6-.4-.5-.7-1-.8-1.2-.1-.2 0-.3.1-.4l.4-.5c.1-.2.1-.3.2-.5 0-.2 0-.3-.1-.4l-.7-1.6c-.2-.5-.4-.4-.6-.4z" fill="currentColor" stroke="none"/>',
    "check": '<path d="M5 12.5l4.5 4.5L19 6.5"/>',
    "minus": '<path d="M6 12h12"/>',
    "sparkle": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6.5 6.5l2 2M15.5 15.5l2 2M17.5 6.5l-2 2M8.5 15.5l-2 2"/>',
    "soundoff": '<path d="M4 9.5v5h3.5L12 18V6L7.5 9.5H4z"/><path d="M21 10l-5 4M16 10l5 4"/>',
}

def svg(name, size=22, sw=1.6, cls="ic"):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" '
            f'fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round">{I.get(name,"")}</svg>')

def star_row(n, sz=13):
    one = svg("star", sz, 0).replace('fill="none"', 'fill="currentColor"')
    return one * n

def e(s):
    return html.escape(str(s), quote=True)

def lang_url(l):
    return f"{FULL}/{l}/"

def wa(lang):
    return f"https://wa.me/{SITE['whatsapp']}?text={quote(C[lang]['wa'])}"

MONO = ('<svg class="brand-mono" viewBox="0 0 56 56" fill="none" aria-hidden="true">'
        '<circle class="ring" cx="28" cy="28" r="26.6" stroke="currentColor" stroke-width="1"/>'
        '<circle class="ring2" cx="28" cy="28" r="22.6" stroke="currentColor" stroke-width=".7"/>'
        '<path class="sun" d="M17 31.4a11 11 0 0 1 22 0" stroke="#c8a24e" stroke-width="1.5" stroke-linecap="round"/>'
        '<g class="rays" stroke="#c8a24e" stroke-width="1.4" stroke-linecap="round">'
        '<path d="M28 11v3.4"/><path d="M40.2 16l-2.3 2.4"/><path d="M15.8 16l2.3 2.4"/></g>'
        '<path class="horizon" d="M15 35.4h26" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>'
        '<path class="wave" d="M17.6 39.8c2.1 0 2.3 1.3 4.6 1.3s2.4-1.3 4.7-1.3 2.4 1.3 4.7 1.3 2.4-1.3 4.6-1.3" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>'
        '</svg>')

# Lifestyle wordmark (Concept J) — COLÓN in a thin frame, adaptive via currentColor
BRAND_LS = ('<span class="ls-box"><span class="ls-word">COLÓN</span>'
            '<span class="ls-sub"><i class="r"></i>Beach Rentals<i class="r"></i></span></span>')
BRAND = f'<a href="#top" class="brand brand-ls">{BRAND_LS}</a>'

# ---------------- structured data ----------------
def jsonld(lang):
    t = C[lang]
    blocks = [
        {"@context": "https://schema.org", "@type": "VacationRental",
         "name": SITE["property_name"], "headline": t["hero"]["title"], "description": SEO[lang]["desc"],
         "url": lang_url(lang), "inLanguage": lang,
         "image": [FULL + f"/assets/img/{s}-1600.webp" for s in ["ocean-view", "balcony", "living-room"]],
         "address": {"@type": "PostalAddress", "addressLocality": SITE["locality"],
                     "addressRegion": SITE["region"], "addressCountry": SITE["country"]},
         "geo": {"@type": "GeoCoordinates", "latitude": SITE["lat"], "longitude": SITE["lng"]},
         "priceRange": f"${SITE['price_low']} - ${SITE['price_high']}", "telephone": SITE["phone_display"],
         "amenityFeature": [
             {"@type": "LocationFeatureSpecification", "name": "Private Beach Access", "value": True},
             {"@type": "LocationFeatureSpecification", "name": "Starlink WiFi", "value": True},
             {"@type": "LocationFeatureSpecification", "name": "Air Conditioning", "value": True},
             {"@type": "LocationFeatureSpecification", "name": "Swimming Pool", "value": True}],
         "aggregateRating": {"@type": "AggregateRating", "ratingValue": SITE["rating"],
                             "reviewCount": SITE["review_count"], "bestRating": "5"}},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]["items"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList",
         "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Home", "item": FULL + "/"},
             {"@type": "ListItem", "position": 2, "name": t["hero"]["title"], "item": lang_url(lang)}]},
    ]
    return "\n".join(f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>'
                     for b in blocks)

def hreflang_tags():
    tags = [f'<link rel="alternate" hreflang="x-default" href="{FULL}/" />']
    for l in LANGS:
        tags.append(f'<link rel="alternate" hreflang="{LANG_META[l]["hreflang"]}" href="{lang_url(l)}" />')
    return "\n  ".join(tags)

# ---------------- components ----------------
def header(lang, home=True):
    t = C[lang]; nav = t["nav"]
    # On the home page anchors are local (#x); on sub-pages they jump back to the home.
    hp = "" if home else f"{BASE}/{lang}/"
    # On the home page the lang switcher swaps to other home pages; on a guide it swaps to that guide's translation (handled by caller via opts override is overkill — keep home switch).
    opts = "".join(
        f'<a class="lang-opt {"active" if l==lang else ""}" href="{BASE}/{l}/" hreflang="{l}">'
        f'<span class="fl">{LANG_META[l]["flag"]}</span><span>{LANG_META[l]["name"]}</span>'
        f'<span class="muted">{LANG_META[l]["short"]}</span></a>' for l in LANGS)
    glabel = GUIDES_LABEL[lang]["nav"]
    navlinks = "".join(f'<a href="{hp}#{s}">{e(nav[s])}</a>'
                       for s in ["amenities", "gallery", "tours", "reviews", "faq"])
    navlinks += f'<a href="{BASE}/{lang}/guides/">{e(glabel)}</a>'
    chev = svg("chevron", 14, 2, "ic chev")
    return f'''<header class="site-head" id="site-head">
  <div class="wrap head-inner">
    {BRAND}
    <nav class="nav-links">{navlinks}</nav>
    <div class="head-actions">
      <div class="lang-switch" id="langSwitch">
        <button class="lang-btn">{LANG_META[lang]["flag"]} {LANG_META[lang]["short"]} {chev}</button>
        <div class="lang-menu">{opts}</div>
      </div>
      <a class="btn btn-primary btn-sm desk-only" href="{wa(lang)}" target="_blank" rel="noopener">{e(nav["book"])}</a>
      <button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<nav class="mobile-nav" id="mobile-nav">{navlinks}
  <a class="btn btn-primary btn-lg" href="{wa(lang)}" target="_blank" rel="noopener">{svg("whatsapp",18)} {e(t["hero"]["cta"])}</a>
</nav>
<div class="mobile-scrim" id="mobile-scrim"></div>'''

def hero(lang):
    t = C[lang]; h = t["hero"]
    slides = "".join(
        f'<div class="slide {"on" if i==0 else ""}" data-i="{i}" style="background-image:url(\'{img_src(s)}\')"></div>'
        for i, (s, _a) in enumerate(IMAGES["hero"]))
    dots = "".join(f'<button class="dot {"on" if i==0 else ""}" data-i="{i}" aria-label="Slide {i+1}"></button>'
                   for i in range(len(IMAGES["hero"])))
    return f'''<section class="hero" id="hero">
  <div class="hero-bg">{slides}</div>
  <div class="hero-veil"></div>
  <div class="hero-inner"><div class="wrap">
    <div class="hero-grid">
      <div class="hero-main">
        <div class="hero-overline"><span class="ov-rule"></span>{e(h["kicker"])}</div>
        <h1>{e(h["title"])}</h1>
        <p class="hero-sub">{e(h["sub"])}</p>
        <div class="hero-actions">
          <a class="btn btn-primary btn-lg" href="{wa(lang)}" target="_blank" rel="noopener">{svg("whatsapp",18)} {e(h["cta"])}</a>
          <a class="btn btn-ghost btn-lg" href="{SITE["airbnb"]}" target="_blank" rel="noopener">{e(h["cta2"])} {svg("arrow",15)}</a>
        </div>
        <div class="hero-meta">
          <div class="hm-price"><b>{e(h["price"])}</b><span>{e(h["per"])}</span></div>
          <span class="hm-div"></span>
          <div class="hm-note">{svg("gold",14)} {e(h["badge"])}</div>
        </div>
      </div>
      <aside class="hero-aside"><div class="hero-rating">
        <span class="num">{SITE["rating"]}</span>
        <span class="stars">{star_row(5,13)}</span>
        <small>{SITE["review_count"]} {e(t["reviews"]["kicker"])}</small>
      </div></aside>
    </div>
    <div class="hero-foot">
      <div class="hero-dots">{dots}</div>
      <span class="scroll-cue">Scroll<span class="line"></span></span>
    </div>
  </div></div>
</section>'''

def trust(lang):
    icons = ["waves", "wifi", "shield", "pool"]
    items = "".join(f'<div class="trust-item">{svg(icons[i],22)}<span>{e(x)}</span></div>'
                    for i, x in enumerate(C[lang]["trust"]))
    return f'<section class="trust" id="trust"><div class="wrap"><div class="trust-inner">{items}</div></div></section>'

def amenities(lang):
    f = C[lang]["features"]
    items = "".join(
        f'<div class="feat-item" data-reveal data-d="{(i%4)+1}"><span class="feat-ic">{svg(it[0],20)}</span>'
        f'<div><h3>{e(it[1])}</h3><p>{e(it[2])}</p></div></div>'
        for i, it in enumerate(f["items"]))
    return f'''<section class="section" id="amenities"><div class="wrap amen-grid">
    <div class="amen-media" data-reveal>
      <div class="ph" style="background-image:url('{img_src("living-room")}')"></div>
      <div class="ph-2" style="background-image:url('{img_src("bedroom-1", 800)}')"></div>
      <span class="amen-tag">{svg("sparkle",15)} {e(f["kicker"])}</span>
    </div>
    <div class="amen-copy">
      <div class="sec-head" data-reveal><div class="eyebrow">{e(f["kicker"])}</div>
        <h2 class="display">{e(f["title"])}</h2><p class="lede">{e(f["sub"])}</p></div>
      <div class="feat-list">{items}</div>
    </div>
  </div></section>'''

GAL_CLASSES = ["wide tall", "", "", "tall", "", "wide", "", "tall", "", "", "wide", ""]
def gallery(lang):
    g = C[lang]["gallery"]
    tiles = "".join(
        f'<figure class="g-item {GAL_CLASSES[i] if i < len(GAL_CLASSES) else ""}" data-i="{i}" data-reveal data-d="{(i%4)+1}">'
        f'<img src="{img_src(slug, 800)}" srcset="{img_srcset(slug)}" sizes="(max-width:720px) 50vw, 25vw" '
        f'width="800" height="600" alt="{e(cap)} — {SITE["property_name"]} {SITE["locality"]}, Colón Panamá" '
        f'loading="lazy" decoding="async">'
        f'<span class="g-expand">{svg("expand",16)}</span><figcaption class="g-cap">{e(cap)}</figcaption></figure>'
        for i, (slug, cap) in enumerate(IMAGES["gallery"]))
    return f'''<section class="section section-sand" id="gallery"><div class="wrap">
    <div class="gal-head" data-reveal>
      <div class="sec-head" style="margin-bottom:0"><div class="eyebrow">{e(g["kicker"])}</div>
        <h2 class="display">{e(g["title"])}</h2><p class="lede">{e(g["sub"])}</p></div>
      <button class="tlink" id="galAll">{e(g["all"])} {svg("arrow",16)}</button>
    </div>
    <div class="gallery" id="gallery-grid">{tiles}</div>
  </div></section>'''

def film(lang):
    fm = C[lang]["film"]
    return f'''<section class="section section-ink" id="film"><div class="wrap">
    <div class="sec-head center" data-reveal><div class="eyebrow light center">{e(fm["kicker"])}</div>
      <h2 class="display">{e(fm["title"])}</h2><p class="lede">{e(fm["sub"])}</p></div>
    <div class="film-frame" data-reveal data-d="1">
      <video id="filmVideo" autoplay muted loop playsinline preload="metadata" poster="{img_src(IMAGES["film_poster"])}">
        <source src="{BASE}/assets/media/bala-tour.mp4" type="video/mp4">
      </video>
      <div class="film-vignette"></div>
      <button class="film-sound" id="filmSound" aria-label="{e(fm["cta"])}">
        <span class="fs-ic">{svg("soundoff",18)}</span><span class="fs-label">{e(fm["cta"])}</span>
      </button>
    </div>
  </div></section>'''

def why(lang):
    t = C[lang]; w = t["why"]
    rows = "".join(
        f'<div class="compare-row"><div class="benefit">{e(r)}</div>'
        f'<div class="direct"><span class="mark-yes">{svg("check",16,2.2)}</span></div>'
        f'<div class="ota"><span class="mark-no">{svg("minus",16,2)}</span></div></div>'
        for r in w["rows"])
    return f'''<section class="section" id="why"><div class="wrap why-grid">
    <div class="why-copy" data-reveal>
      <div class="eyebrow">{e(w["kicker"])}</div>
      <h2 class="display">{e(w["title"])}</h2><p class="lede">{e(w["sub"])}</p>
      <div class="save-note">{svg("gold",18)} <span class="pill">-15-20%</span> {e(t["reviews"]["source"])}</div>
      <a class="btn btn-dark btn-lg" href="{wa(lang)}" target="_blank" rel="noopener" style="margin-top:1.6rem">{svg("whatsapp",18)} {e(t["hero"]["cta"])}</a>
    </div>
    <div class="compare" data-reveal data-d="1">
      <div class="compare-head"><div class="lead">&nbsp;</div>
        <div class="direct"><span class="pin">{e(w["direct"])}</span>{e(SITE["brand"])}</div>
        <div class="ota">{e(w["ota"])}</div></div>
      {rows}
    </div>
  </div></section>'''

def tours(lang):
    tr = C[lang]["tours"]
    cards = "".join(
        f'<article class="tour-card" data-reveal data-d="{(i%4)+1}">'
        f'<div class="timg" style="background-image:url(\'{img_src(IMAGES["tours"][it[2]], 800)}\')"></div>'
        f'<div class="tour-body"><span class="tour-num">0{i+1}</span><h3>{e(it[0])}</h3><p>{e(it[1])}</p></div></article>'
        for i, it in enumerate(tr["items"]))
    return f'''<section class="section section-sand" id="tours"><div class="wrap">
    <div class="sec-head center" data-reveal><div class="eyebrow center">{e(tr["kicker"])}</div>
      <h2 class="display">{e(tr["title"])}</h2><p class="lede">{e(tr["sub"])}</p></div>
    <div class="tour-grid">{cards}</div>
  </div></section>'''

def reviews(lang):
    r = C[lang]["reviews"]
    cards = "".join(
        f'<article class="rev-card" data-reveal data-d="{(i%4)+1}"><div class="rev-stars">{star_row(rv[3],14)}</div>'
        f'<p class="rev-quote">“{e(rv[4])}”</p><div class="rev-author"><span class="rev-flag">{rv[2]}</span>'
        f'<div><strong>{e(rv[0])}</strong><span>{e(rv[1])}</span></div></div></article>'
        for i, rv in enumerate(REVIEWS))
    return f'''<section class="section section-ink" id="reviews"><div class="wrap">
    <div class="rev-top">
      <div class="sec-head" style="margin-bottom:0" data-reveal><div class="eyebrow light">{e(r["kicker"])}</div>
        <h2 class="display">{e(r["title"])}</h2></div>
      <div class="rev-score" data-reveal data-d="1">
        <div class="score-big"><b>{SITE["rating"]}</b><span class="stars">{star_row(5,15)}</span></div>
        <div class="score-meta"><span class="superhost">{svg("gold",14)} {e(r["superhost"])}</span><br>
          <span>{e(r["source"])}</span><br>
          <span>{SITE["review_count"]} {e(r["rated"])} {e(r["kicker"].lower())}</span></div>
      </div>
    </div>
    <div class="rev-grid">{cards}</div>
  </div></section>'''

def faq(lang):
    t = C[lang]; f = t["faq"]
    items = "".join(
        f'<div class="faq-item {"open" if i==0 else ""}"><button class="faq-q">{e(q)}<span class="faq-plus"></span></button>'
        f'<div class="faq-a"><p>{e(a)}</p></div></div>'
        for i, (q, a) in enumerate(f["items"]))
    return f'''<section class="section" id="faq"><div class="wrap faq-grid">
    <div class="sec-head" data-reveal style="position:sticky;top:100px"><div class="eyebrow">{e(f["kicker"])}</div>
      <h2 class="display">{e(f["title"])}</h2><p class="lede">{e(f["sub"])}</p>
      <a class="tlink" href="{wa(lang)}" target="_blank" rel="noopener" style="margin-top:1.2rem">{svg("whatsapp",16)} {e(t["hero"]["cta"])} {svg("arrow",15)}</a></div>
    <div class="faq" data-reveal data-d="1">{items}</div>
  </div></section>'''

def location(lang):
    l = C[lang]["location"]
    facts = [("pin", SITE["locality"], f'{SITE["region"]} · {SITE["country_name"]}'),
             ("car", "90 min", "Panama City"), ("clock", "15 min", "Portobelo")]
    facts_html = "".join(f'<div class="loc-fact">{svg(fk,22)}<div><b>{e(fa)}</b><span>{e(fb)}</span></div></div>'
                         for fk, fa, fb in facts)
    embed = f"https://maps.google.com/maps?q={SITE['lat']},{SITE['lng']}&z=12&output=embed"
    maps = f"https://www.google.com/maps?q={SITE['lat']},{SITE['lng']}"
    return f'''<section class="section section-sand" id="location"><div class="wrap loc-grid">
    <div class="loc-copy" data-reveal><div class="eyebrow">{e(l["kicker"])}</div>
      <h2 class="display">{e(l["title"])}</h2><p class="lede">{e(l["sub"])}</p>
      <div class="loc-facts">{facts_html}</div>
      <a class="btn btn-outline btn-lg" href="{maps}" target="_blank" rel="noopener" style="margin-top:1.6rem">{svg("pin",18)} {e(l["directions"])}</a></div>
    <div class="map-box" data-reveal data-d="1"><iframe loading="lazy" src="{embed}" title="Map"></iframe></div>
  </div></section>'''

def cta(lang):
    n = C[lang]["newsletter"]
    return f'''<section class="cta-band" id="cta">
    <div class="cb-img" style="background-image:url('{img_src("ocean-view")}')"></div>
    <div class="cb-veil"></div>
    <div class="cta-inner wrap"><div class="narrow" data-reveal>
      <div class="eyebrow light center">{e(n["kicker"])}</div>
      <h2>{e(n["title"])}</h2><p class="lede">{e(n["sub"])}</p>
      <form class="nl-form" onsubmit="return false">
        <input type="email" placeholder="{e(n["placeholder"])}" required>
        <button class="btn btn-primary btn-lg" type="submit">{e(n["button"])}</button>
      </form>
      <small>{e(n["disclaimer"])}</small>
    </div></div>
  </section>'''

def footer(lang):
    t = C[lang]; f = t["footer"]; nav = t["nav"]
    langbtns = "".join(f'<a href="{BASE}/{l}/" class="{"active" if l==lang else ""}" hreflang="{l}">{LANG_META[l]["flag"]} {LANG_META[l]["short"]}</a>'
                       for l in LANGS)
    kw = "".join(f'<a href="{wa(lang)}" target="_blank" rel="noopener">{e(k)}</a>' for k in FOOTER_KEYWORDS)
    links = "".join(f'<li><a href="#{s}">{e(nav[s])}</a></li>'
                    for s in ["amenities", "gallery", "tours", "reviews", "faq"])
    maps = f"https://www.google.com/maps?q={SITE['lat']},{SITE['lng']}"
    return f'''<footer class="site-foot" id="site-foot"><div class="wrap">
    <div class="foot-signoff">
      <div class="fs-copy"><span class="fs-eyebrow">{SITE["locality"]} · {SITE["region"]} · {SITE["country_name"]}</span>
        <h2 class="fs-title">{e(t["hero"]["title"])}</h2></div>
      <a class="btn btn-primary btn-lg" href="{wa(lang)}" target="_blank" rel="noopener">{svg("whatsapp",18)} {e(nav["book"])}</a>
    </div>
    <div class="foot-grid">
      <div class="foot-about">
        <a href="#top" class="brand brand-ls" style="color:#fff">{BRAND_LS}</a>
        <p>{e(f["about"])}</p>
        <a class="foot-phone" href="{wa(lang)}" target="_blank" rel="noopener">{svg("whatsapp",18)} {SITE["phone_display"]}</a>
      </div>
      <div class="foot-col"><h4>{e(f["links"])}</h4><ul>{links}</ul></div>
      <div class="foot-col"><h4>{e(f["contact"])}</h4><ul>
        <li><a href="{wa(lang)}" target="_blank" rel="noopener">WhatsApp</a></li>
        <li><a href="{SITE["airbnb"]}" target="_blank" rel="noopener">Airbnb</a></li>
        <li><a href="{maps}" target="_blank" rel="noopener">{e(t["location"]["directions"])}</a></li></ul></div>
      <div class="foot-col langs-col"><h4>Language</h4><div class="foot-langs">{langbtns}</div></div>
    </div>
    <div class="foot-kw"><span class="lab">{e(f["popular"])}</span>{kw}</div>
    <div class="foot-bottom">
      <span>© {datetime.date.today().year} {SITE["brand"]} Rentals · {e(f["rights"])}</span>
      <span>{SITE["property_name"]} · {SITE["locality"]}, {SITE["region"]}</span>
    </div>
  </div></footer>'''

def book_bar(lang):
    t = C[lang]; h = t["hero"]
    star = svg("star", 16).replace('fill="none"', 'fill="currentColor"')
    return f'''<div class="book-bar" id="book-bar"><div class="book-inner">
    <div class="book-price"><b>{e(h["price"])}<span> {e(h["per"])}</span></b>
      <small>{svg("gold",13)} {e(t["why"]["rows"][0])}</small></div>
    <div class="book-spacer"></div>
    <div class="book-rating">{star} {SITE["rating"]} <span>· {SITE["review_count"]}</span></div>
    <div class="book-actions">
      <a class="btn btn-outline cta2" href="{SITE["airbnb"]}" target="_blank" rel="noopener">Airbnb</a>
      <a class="btn btn-primary" href="{wa(lang)}" target="_blank" rel="noopener">{svg("whatsapp",17)} {e(t["nav"]["book"])}</a>
    </div>
  </div></div>'''

def lightbox():
    return '''<div class="lightbox" id="lightbox">
  <button class="lb-close" id="lbClose" aria-label="Close"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
  <div class="lb-stage">
    <button class="lb-btn lb-prev" id="lbPrev" aria-label="Previous"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 6l-6 6 6 6"/></svg></button>
    <img class="lb-img" id="lbImg" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" alt="">
    <button class="lb-btn lb-next" id="lbNext" aria-label="Next"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l6 6-6 6"/></svg></button>
    <div class="lb-cap"><span class="count" id="lbCount"></span><span id="lbCapText"></span></div>
  </div>
</div>'''

def fab(lang):
    return (f'<a class="fab-wa" id="fab-wa" href="{wa(lang)}" target="_blank" rel="noopener" aria-label="WhatsApp">'
            f'{svg("whatsapp",28)}</a>')

# ---------------- guides (content hub) ----------------
def guide_url(lang, slug):
    return f"{FULL}/{lang}/guides/{slug}/"

def hreflang_guides_tags(slug=None):
    """hreflang for a guide (slug set) or the guides index (slug None)."""
    def u(l):
        return guide_url(l, slug) if slug else f"{FULL}/{l}/guides/"
    xd = u(DEFAULT_LANG)
    tags = [f'<link rel="alternate" hreflang="x-default" href="{xd}" />']
    for l in LANGS:
        tags.append(f'<link rel="alternate" hreflang="{LANG_META[l]["hreflang"]}" href="{u(l)}" />')
    return "\n  ".join(tags)

def sub_head(lang, title, desc, kw, canonical, hreflang_block, jsonld_str, og_img=None):
    m = LANG_META[lang]
    og = og_img or IMAGES["og"]
    return f'''<!DOCTYPE html>
<html lang="{m["hreflang"]}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{e(title)}</title>
  <meta name="description" content="{e(desc)}" />
  <meta name="keywords" content="{e(kw)}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <link rel="canonical" href="{canonical}" />
  {hreflang_block}
  <meta property="og:type" content="article" />
  <meta property="og:locale" content="{m["locale"]}" />
  <meta property="og:site_name" content="{SITE["brand"]}" />
  <meta property="og:title" content="{e(title)}" />
  <meta property="og:description" content="{e(desc)}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{og}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{e(title)}" />
  <meta name="twitter:description" content="{e(desc)}" />
  <meta name="twitter:image" content="{og}" />
  <meta name="theme-color" content="#06202f" />
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 56'%3E%3Crect width='56' height='56' rx='9' fill='%2306202f'/%3E%3Cpath d='M39 18 A20 20 0 1 0 39 38' fill='none' stroke='%23fbf8f1' stroke-width='7' stroke-linecap='round'/%3E%3Cpath d='M14 45h28' stroke='%23c39a4a' stroke-width='3.4' stroke-linecap='round'/%3E%3C/svg%3E" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{BASE}/assets/css/styles.css?v={CSS_VER}" />
  {jsonld_str}
</head>'''

def guide_cta(lang):
    g = GUIDES_LABEL[lang]
    return f'''<section class="cta-band" id="cta">
    <div class="cb-img" style="background-image:url('{img_src("balcony")}')"></div>
    <div class="cb-veil"></div>
    <div class="cta-inner wrap"><div class="narrow" data-reveal>
      <div class="eyebrow light center">{e(GUIDES_LABEL[lang]["nav"])}</div>
      <h2>{e(g["cta_title"])}</h2><p class="lede">{e(g["cta_sub"])}</p>
      <div style="display:flex;gap:.7rem;justify-content:center;flex-wrap:wrap;margin-top:1.6rem">
        <a class="btn btn-primary btn-lg" href="{BASE}/{lang}/">{e(g["cta_btn"])} {svg("arrow",16)}</a>
        <a class="btn btn-ghost btn-lg" href="{wa(lang)}" target="_blank" rel="noopener">{svg("whatsapp",18)} WhatsApp</a>
      </div>
    </div></div>
  </section>'''

def render_blocks(blocks):
    out = []
    for h2, items in blocks:
        out.append(f'<h2 class="display" style="font-size:clamp(1.6rem,3vw,2.2rem);margin:2.4rem 0 1rem">{e(h2)}</h2>')
        for it in items:
            if isinstance(it, tuple) and it[0] == "ul":
                lis = "".join(f"<li>{li}</li>" for li in it[1])
                out.append(f'<ul style="margin:0 0 1rem;padding-left:1.1rem;display:flex;flex-direction:column;gap:.5rem">{lis}</ul>')
            else:
                out.append(f'<p style="margin:0 0 1rem">{it}</p>')
    return "\n".join(out)

def guide_page(lang, slug):
    g = GUIDES[slug]; gd = g[lang]; lab = GUIDES_LABEL[lang]
    canonical = guide_url(lang, slug)
    og_img = FULL + f"/assets/img/{g['image']}-1600.webp"
    jsonld = "\n".join(f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>' for b in [
        {"@context": "https://schema.org", "@type": "Article", "headline": gd["h1"],
         "description": gd["desc"], "inLanguage": lang, "image": og_img,
         "mainEntityOfPage": canonical,
         "author": {"@type": "Organization", "name": SITE["brand"]},
         "publisher": {"@type": "Organization", "name": SITE["brand"]}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{FULL}/{lang}/"},
            {"@type": "ListItem", "position": 2, "name": lab["nav"], "item": f"{FULL}/{lang}/guides/"},
            {"@type": "ListItem", "position": 3, "name": gd["h1"], "item": canonical}]},
    ])
    # related = the other guides
    rel = [s for s in GUIDE_ORDER if s != slug]
    rel_cards = "".join(
        f'<a class="tour-card" href="{BASE}/{lang}/guides/{s}/" style="text-decoration:none">'
        f'<div class="timg" style="background-image:url(\'{img_src(GUIDES[s]["image"], 800)}\')"></div>'
        f'<div class="tour-body"><h3>{e(GUIDES[s][lang]["h1"])}</h3>'
        f'<p style="max-height:none;opacity:1;margin-top:.3rem">{e(GUIDES[s][lang]["desc"][:90])}…</p></div></a>'
        for s in rel)
    head = sub_head(lang, gd["title"], gd["desc"], gd["kw"], canonical,
                    hreflang_guides_tags(slug), jsonld, og_img)
    body = f'''<body id="top" data-lang="{lang}">
{header(lang, home=False)}
<main>
  <article class="section" style="padding-top:7rem">
    <div class="wrap narrow">
      <nav class="eyebrow" aria-label="Breadcrumb" style="margin-bottom:1.2rem">
        <a href="{BASE}/{lang}/" style="color:var(--teal-d)">Home</a> ·
        <a href="{BASE}/{lang}/guides/" style="color:var(--teal-d)">{e(lab["nav"])}</a>
      </nav>
      <h1 class="display">{e(gd["h1"])}</h1>
      <p class="lede" style="max-width:46ch">{e(gd["lead"])}</p>
      <div class="guide-hero" style="margin:1.8rem 0;border-radius:var(--r-lg);overflow:hidden;box-shadow:var(--shadow)">
        <img src="{img_src(g["image"])}" srcset="{img_srcset(g["image"])}" sizes="(max-width:900px) 100vw, 760px"
          width="1600" height="1067" alt="{e(gd["h1"])}" decoding="async" style="width:100%;display:block">
      </div>
      <div class="guide-body" style="font-size:1.05rem;line-height:1.75;color:var(--ink-90)">
        {render_blocks(gd["blocks"])}
      </div>
      <p style="margin-top:2rem"><a class="btn btn-outline" href="{BASE}/{lang}/guides/">{svg("arrow",15)} {e(lab["back"])}</a></p>
    </div>
  </article>
  <section class="section section-sand">
    <div class="wrap">
      <div class="sec-head center"><div class="eyebrow center">{e(lab["related"])}</div></div>
      <div class="tour-grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{rel_cards}</div>
    </div>
  </section>
  {guide_cta(lang)}
</main>
{footer(lang)}
{book_bar(lang)}
{fab(lang)}
<script src="{BASE}/assets/js/main.js?v={JS_VER}" defer></script>
</body>
</html>'''
    return head + "\n" + body

def guides_index(lang):
    lab = GUIDES_LABEL[lang]
    canonical = f"{FULL}/{lang}/guides/"
    jsonld = f'<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"CollectionPage","name":lab["title"],"inLanguage":lang,"url":canonical}, ensure_ascii=False)}</script>'
    cards = "".join(
        f'<a class="tour-card" href="{BASE}/{lang}/guides/{s}/" style="text-decoration:none">'
        f'<div class="timg" style="background-image:url(\'{img_src(GUIDES[s]["image"], 800)}\')"></div>'
        f'<div class="tour-body"><h3>{e(GUIDES[s][lang]["h1"])}</h3>'
        f'<p style="max-height:none;opacity:1;margin-top:.3rem">{e(GUIDES[s][lang]["desc"][:110])}…</p>'
        f'<span class="tlink" style="margin-top:.6rem;color:#fff">{e(lab["read"])} {svg("arrow",15)}</span></div></a>'
        for s in GUIDE_ORDER)
    head = sub_head(lang, lab["title"] + f' | {SITE["brand"]}', lab["sub"],
                    "panama caribbean travel guide, things to do colon panama, maria chiquita",
                    canonical, hreflang_guides_tags(None), jsonld)
    body = f'''<body id="top" data-lang="{lang}">
{header(lang, home=False)}
<main>
  <section class="section" style="padding-top:7rem">
    <div class="wrap">
      <div class="sec-head"><div class="eyebrow">{e(lab["nav"])}</div>
        <h1 class="display">{e(lab["title"])}</h1><p class="lede">{e(lab["sub"])}</p></div>
      <div class="tour-grid" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr))">{cards}</div>
    </div>
  </section>
  {guide_cta(lang)}
</main>
{footer(lang)}
{book_bar(lang)}
{fab(lang)}
<script src="{BASE}/assets/js/main.js?v={JS_VER}" defer></script>
</body>
</html>'''
    return head + "\n" + body

# ---------------- page ----------------
def page(lang):
    t = C[lang]; m = LANG_META[lang]; s = SEO[lang]
    gallery_json = json.dumps([[img_src(slug), cap] for slug, cap in IMAGES["gallery"]], ensure_ascii=False)
    body = "\n".join([
        header(lang),
        '<main>',
        hero(lang), trust(lang), amenities(lang), gallery(lang), film(lang),
        why(lang), tours(lang), reviews(lang), faq(lang), location(lang), cta(lang),
        '</main>',
        footer(lang), book_bar(lang), fab(lang), lightbox(),
    ])
    return f'''<!DOCTYPE html>
<html lang="{m["hreflang"]}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{e(s["title"])}</title>
  <meta name="description" content="{e(s["desc"])}" />
  <meta name="keywords" content="{e(s["kw"])}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="author" content="{SITE["brand"]}" />
  <link rel="canonical" href="{lang_url(lang)}" />
  {hreflang_tags()}
  <meta property="og:type" content="website" />
  <meta property="og:locale" content="{m["locale"]}" />
  <meta property="og:site_name" content="{SITE["brand"]}" />
  <meta property="og:title" content="{e(s["title"])}" />
  <meta property="og:description" content="{e(s["desc"])}" />
  <meta property="og:url" content="{lang_url(lang)}" />
  <meta property="og:image" content="{IMAGES["og"]}" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{e(s["title"])}" />
  <meta name="twitter:description" content="{e(s["desc"])}" />
  <meta name="twitter:image" content="{IMAGES["og"]}" />
  <meta name="theme-color" content="#06202f" />
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 56 56'%3E%3Crect width='56' height='56' rx='9' fill='%2306202f'/%3E%3Cpath d='M39 18 A20 20 0 1 0 39 38' fill='none' stroke='%23fbf8f1' stroke-width='7' stroke-linecap='round'/%3E%3Cpath d='M14 45h28' stroke='%23c39a4a' stroke-width='3.4' stroke-linecap='round'/%3E%3C/svg%3E" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{BASE}/assets/css/styles.css?v={CSS_VER}" />
  {jsonld(lang)}
</head>
<body id="top" data-lang="{lang}">
{body}
<script>window.GALLERY={gallery_json};window.FILM={json.dumps({"cta":t["film"]["cta"],"on":t["film"]["on"]}, ensure_ascii=False)};</script>
<script src="{BASE}/assets/js/main.js?v={JS_VER}" defer></script>
</body>
</html>'''

# ---------------- root redirect ----------------
def root_redirect():
    geo = json.dumps(GEO_MAP); langs = json.dumps(LANGS)
    links = "".join(f'<a href="{BASE}/{l}/">{LANG_META[l]["flag"]} {LANG_META[l]["name"]}</a>' for l in LANGS)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{SITE["brand"]} — Beachfront Vacation Rental, María Chiquita, Colón, Panama</title>
  <meta name="description" content="Luxury beachfront vacation rental at Bala Beach, María Chiquita, Colón, Panama. Available in English, Español, Deutsch, Português, Français." />
  <link rel="canonical" href="{FULL}/" />
  {hreflang_tags()}
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet" />
  <style>
    body{{font-family:Manrope,sans-serif;margin:0;min-height:100svh;display:flex;align-items:center;justify-content:center;
    background:#06202f url('{img_src("ocean-view")}') center/cover;color:#fff;text-align:center}}
    .ov{{position:fixed;inset:0;background:linear-gradient(180deg,rgba(6,32,47,.6),rgba(6,32,47,.92))}}
    .box{{position:relative;z-index:1;padding:2rem}}
    .mark{{font-size:.62rem;letter-spacing:.34em;color:#dcb978;font-weight:700}}
    h1{{font-family:"Cormorant Garamond",Georgia,serif;font-weight:600;font-size:2rem;margin:.6rem 0;letter-spacing:-.01em}}
    p{{opacity:.82;margin:0 0 1.4rem;font-size:.95rem}}
    .sp{{width:32px;height:32px;border:2px solid rgba(255,255,255,.25);border-top-color:#dcb978;border-radius:50%;
    margin:1.2rem auto;animation:spin 1s linear infinite}}
    @keyframes spin{{to{{transform:rotate(360deg)}}}}
    .langs{{display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center;margin-top:1rem}}
    .langs a{{color:#fff;text-decoration:none;border:1px solid rgba(255,255,255,.3);padding:.5rem .9rem;
    border-radius:2px;font-weight:700;font-size:.88rem;transition:.2s}}
    .langs a:hover{{background:#c39a4a;color:#06202f;border-color:#c39a4a}}
  </style>
  <script>
    (function(){{
      var GEO={geo}, LANGS={langs}, DEF="{DEFAULT_LANG}", BASE="{BASE}";
      function go(l){{ if(LANGS.indexOf(l)<0) l=DEF; location.replace(BASE+"/"+l+"/"); }}
      try{{ var s=localStorage.getItem("bb_lang"); if(s){{ go(s); return; }} }}catch(_e){{}}
      var nav=(navigator.language||navigator.userLanguage||DEF).slice(0,2).toLowerCase();
      var bh = LANGS.indexOf(nav)>=0 ? nav : null;
      var done=false, to=setTimeout(function(){{ if(!done){{done=true;go(bh||DEF);}} }},1500);
      try{{
        fetch("https://ipapi.co/json/").then(function(r){{return r.json();}}).then(function(d){{
          if(done)return; done=true; clearTimeout(to);
          var cc=(d&&d.country_code||"").toUpperCase(), pick=null;
          for(var l in GEO){{ if(GEO[l].indexOf(cc)>=0){{pick=l;break;}} }}
          go(pick||bh||DEF);
        }}).catch(function(){{ if(!done){{done=true;clearTimeout(to);go(bh||DEF);}} }});
      }}catch(_e){{ if(!done){{done=true;clearTimeout(to);go(bh||DEF);}} }}
    }})();
  </script>
</head>
<body>
  <div class="ov"></div>
  <div class="box">
    <div class="mark">BALA BEACH · MARÍA CHIQUITA · PANAMÁ</div>
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
    def alts():
        a = [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{FULL}/"/>']
        for l in LANGS:
            a.append(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{lang_url(l)}"/>')
        return "\n".join(a)
    urls = [f'''  <url>
    <loc>{FULL}/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
{alts()}
  </url>''']
    for l in LANGS:
        urls.append(f'''  <url>
    <loc>{lang_url(l)}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
{alts()}
  </url>''')
    # guides index (per language)
    def galts(slug=None):
        a = [f'    <xhtml:link rel="alternate" hreflang="x-default" href="{FULL}/{DEFAULT_LANG}/guides/{(slug+"/") if slug else ""}"/>']
        for l in LANGS:
            loc = f"{FULL}/{l}/guides/{(slug+'/') if slug else ''}"
            a.append(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{loc}"/>')
        return "\n".join(a)
    for l in LANGS:
        urls.append(f'''  <url>
    <loc>{FULL}/{l}/guides/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
{galts()}
  </url>''')
    for slug in GUIDE_ORDER:
        for l in LANGS:
            urls.append(f'''  <url>
    <loc>{FULL}/{l}/guides/{slug}/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
{galts(slug)}
  </url>''')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")

def robots():
    return f"User-agent: *\nAllow: /\n\nSitemap: {FULL}/sitemap.xml\n"

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

if __name__ == "__main__":
    for l in LANGS:
        write(f"{l}/index.html", page(l))
        write(f"{l}/guides/index.html", guides_index(l))
        for slug in GUIDE_ORDER:
            write(f"{l}/guides/{slug}/index.html", guide_page(l, slug))
    write("index.html", root_redirect())
    write("sitemap.xml", sitemap())
    write("robots.txt", robots())
    write(".nojekyll", "")
    if CUSTOM and SITE.get("host", "github") == "github":
        write("CNAME", CUSTOM + "\n")
        print("custom domain (GitHub Pages CNAME):", CUSTOM)
    elif CUSTOM:
        print("custom domain:", CUSTOM, "(host:", SITE.get("host"), "- no CNAME)")
    print("done")
