/* ============================================================
   BALA BEACH — main.js (editorial, static multi-page)
   Wires interactions onto server-rendered DOM:
   header solid + lang menu + mobile nav, hero carousel, film
   sound toggle, FAQ accordion, gallery lightbox, scroll reveal,
   sticky booking bar. Language switching is via /<lang>/ links.
   ============================================================ */
(function () {
  "use strict";

  // remember chosen language for the root geo-redirect
  try {
    var lang = document.body.getAttribute("data-lang");
    if (lang) localStorage.setItem("bb_lang", lang);
  } catch (e) {}

  var GALLERY = window.GALLERY || [];
  var FILM = window.FILM || { cta: "Play with sound", on: "Sound on" };

  function soundIcon(off) {
    var base = '<svg class="ic" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">';
    var on = '<path d="M4 9.5v5h3.5L12 18V6L7.5 9.5H4z"/><path d="M15.5 9.5a3.2 3.2 0 0 1 0 5M18 7.2a6.5 6.5 0 0 1 0 9.6"/>';
    var muted = '<path d="M4 9.5v5h3.5L12 18V6L7.5 9.5H4z"/><path d="M21 10l-5 4M16 10l5 4"/>';
    return base + (off ? muted : on) + "</svg>";
  }

  /* ---------- header: solid on scroll + lang dropdown ---------- */
  var head = document.getElementById("site-head");
  var ls = document.getElementById("langSwitch");
  if (ls) {
    var lb = ls.querySelector(".lang-btn");
    lb.addEventListener("click", function (ev) { ev.stopPropagation(); ls.classList.toggle("open"); });
    document.addEventListener("click", function () { ls.classList.remove("open"); });
  }

  /* ---------- mobile nav ---------- */
  var burger = document.getElementById("burger");
  var mnav = document.getElementById("mobile-nav");
  var scrim = document.getElementById("mobile-scrim");
  if (burger && mnav && scrim) {
    var closeMenu = function () { burger.classList.remove("on"); mnav.classList.remove("open"); scrim.classList.remove("on"); };
    burger.addEventListener("click", function () {
      var open = mnav.classList.toggle("open");
      burger.classList.toggle("on", open); scrim.classList.toggle("on", open);
    });
    scrim.addEventListener("click", closeMenu);
    mnav.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", closeMenu); });
  }

  /* ---------- hero carousel ---------- */
  (function () {
    var slides = [].slice.call(document.querySelectorAll(".hero .slide"));
    var dots = [].slice.call(document.querySelectorAll(".hero .dot"));
    if (slides.length < 2) return;
    var cur = 0, timer;
    function go(n) {
      cur = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) { s.classList.toggle("on", i === cur); });
      dots.forEach(function (d, i) { d.classList.toggle("on", i === cur); });
    }
    function start() { timer = setInterval(function () { go(cur + 1); }, 6000); }
    function restart() { clearInterval(timer); start(); }
    dots.forEach(function (d, i) { d.addEventListener("click", function () { go(i); restart(); }); });
    start();
  })();

  /* ---------- film video sound toggle ---------- */
  (function () {
    var v = document.getElementById("filmVideo");
    var btn = document.getElementById("filmSound");
    if (!v || !btn) return;
    if (v.play) v.play().catch(function () {});
    function sync() {
      btn.querySelector(".fs-ic").innerHTML = soundIcon(v.muted);
      btn.querySelector(".fs-label").textContent = v.muted ? FILM.cta : FILM.on;
      btn.classList.toggle("live", !v.muted);
    }
    btn.addEventListener("click", function () {
      v.muted = !v.muted;
      if (!v.muted) v.play().catch(function () {});
      sync();
    });
    sync();
  })();

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll(".faq-item").forEach(function (item) {
    var q = item.querySelector(".faq-q");
    var a = item.querySelector(".faq-a");
    function set(open) { item.classList.toggle("open", open); a.style.maxHeight = open ? a.scrollHeight + "px" : 0; }
    if (item.classList.contains("open")) requestAnimationFrame(function () { set(true); });
    q.addEventListener("click", function () { set(!item.classList.contains("open")); });
  });

  /* ---------- gallery lightbox ---------- */
  (function () {
    var lb = document.getElementById("lightbox");
    if (!lb || !GALLERY.length) return;
    var img = document.getElementById("lbImg");
    var capText = document.getElementById("lbCapText");
    var count = document.getElementById("lbCount");
    var idx = 0;

    function update() {
      var im = GALLERY[idx];
      img.style.opacity = 0;
      var pre = new Image();
      pre.onload = function () { img.src = im[0]; img.style.opacity = 1; };
      pre.src = im[0];
      capText.textContent = im[1];
      count.textContent = (idx + 1) + " / " + GALLERY.length;
    }
    function open(i) { idx = i; lb.classList.add("on"); document.body.style.overflow = "hidden"; update(); }
    function close() { lb.classList.remove("on"); document.body.style.overflow = ""; }
    function step(d) { idx = (idx + d + GALLERY.length) % GALLERY.length; update(); }

    document.querySelectorAll(".g-item").forEach(function (it) {
      it.addEventListener("click", function () { open(+it.dataset.i); });
    });
    var all = document.getElementById("galAll");
    if (all) all.addEventListener("click", function () { open(0); });
    document.getElementById("lbClose").addEventListener("click", close);
    document.getElementById("lbPrev").addEventListener("click", function (e) { e.stopPropagation(); step(-1); });
    document.getElementById("lbNext").addEventListener("click", function (e) { e.stopPropagation(); step(1); });
    lb.addEventListener("click", function (e) {
      if (e.target.id === "lightbox" || e.target.classList.contains("lb-stage")) close();
    });
    document.addEventListener("keydown", function (e) {
      if (!lb.classList.contains("on")) return;
      if (e.key === "Escape") close();
      if (e.key === "ArrowLeft") step(-1);
      if (e.key === "ArrowRight") step(1);
    });
    var sx = 0, stage = lb.querySelector(".lb-stage");
    stage.addEventListener("touchstart", function (e) { sx = e.touches[0].clientX; }, { passive: true });
    stage.addEventListener("touchend", function (e) {
      var dx = e.changedTouches[0].clientX - sx;
      if (Math.abs(dx) > 45) step(dx < 0 ? 1 : -1);
    });
  })();

  /* ---------- scroll reveal ---------- */
  (function () {
    var targets = document.querySelectorAll("[data-reveal]");
    if (!("IntersectionObserver" in window)) {
      targets.forEach(function (el) { el.classList.add("in"); });
      return;
    }
    var io = new IntersectionObserver(function (ents) {
      ents.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" });
    targets.forEach(function (el) { io.observe(el); });
  })();

  /* ---------- scroll: header solid + sticky book bar + fab ---------- */
  function onScroll() {
    var y = window.scrollY;
    if (head) head.classList.toggle("solid", y > 40);
    var heroEl = document.getElementById("hero");
    var heroH = (heroEl ? heroEl.offsetHeight : 600) * 0.85;
    var nearFoot = (window.innerHeight + y) > (document.body.offsetHeight - 460);
    var show = y > heroH && !nearFoot;
    var bar = document.getElementById("book-bar");
    if (bar) bar.classList.toggle("on", show);
    var fab = document.getElementById("fab-wa");
    if (fab) fab.classList.toggle("lifted", show);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- smooth-scroll offset for fixed header ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (ev) {
      var id = a.getAttribute("href");
      if (id.length < 2) return;
      var el = document.querySelector(id);
      if (!el) return;
      ev.preventDefault();
      var y = el.getBoundingClientRect().top + window.scrollY - 70;
      window.scrollTo({ top: y, behavior: "smooth" });
    });
  });
})();
