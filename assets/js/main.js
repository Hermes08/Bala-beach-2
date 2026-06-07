/* Bala Beach — interactions: header, lang menu, mobile nav, hero carousel, reveal */
(function () {
  "use strict";

  // remember chosen language for the root geo-redirect
  try {
    var lang = document.body.getAttribute("data-lang");
    if (lang) localStorage.setItem("bb_lang", lang);
  } catch (e) {}

  var head = document.querySelector(".site-head");
  function onScroll() {
    if (window.scrollY > 40) head.classList.add("solid");
    else head.classList.remove("solid");
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  // language dropdown
  var ls = document.querySelector(".lang-switch");
  if (ls) {
    var lb = ls.querySelector(".lang-btn");
    lb.addEventListener("click", function (ev) {
      ev.stopPropagation();
      ls.classList.toggle("open");
      lb.setAttribute("aria-expanded", ls.classList.contains("open"));
    });
    document.addEventListener("click", function () { ls.classList.remove("open"); });
  }

  // mobile nav
  var burger = document.querySelector(".burger");
  var mnav = document.querySelector(".mobile-nav");
  if (burger && mnav) {
    burger.addEventListener("click", function () { mnav.classList.toggle("open"); });
    mnav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { mnav.classList.remove("open"); });
    });
  }

  // hero carousel
  var slides = Array.prototype.slice.call(document.querySelectorAll(".slide"));
  var dots = Array.prototype.slice.call(document.querySelectorAll(".dot"));
  if (slides.length > 1) {
    var cur = 0, timer;
    function show(i) {
      slides[cur].classList.remove("on");
      if (dots[cur]) dots[cur].classList.remove("on");
      cur = (i + slides.length) % slides.length;
      slides[cur].classList.add("on");
      if (dots[cur]) dots[cur].classList.add("on");
    }
    function next() { show(cur + 1); }
    function start() { timer = setInterval(next, 5000); }
    function reset() { clearInterval(timer); start(); }
    dots.forEach(function (d, i) {
      d.addEventListener("click", function () { show(i); reset(); });
    });
    start();
  }

  // scroll reveal
  var io;
  var targets = document.querySelectorAll(".sec-head, .feat-card, .tour-card, .rev-card, .compare, .faq, .map-box");
  targets.forEach(function (el) { el.setAttribute("data-reveal", ""); });
  if ("IntersectionObserver" in window) {
    io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
      });
    }, { threshold: 0.12 });
    targets.forEach(function (el) { io.observe(el); });
  } else {
    targets.forEach(function (el) { el.classList.add("in"); });
  }

  // smooth-scroll offset for fixed header
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (ev) {
      var id = a.getAttribute("href");
      if (id.length < 2) return;
      var el = document.querySelector(id);
      if (!el) return;
      ev.preventDefault();
      var y = el.getBoundingClientRect().top + window.scrollY - 64;
      window.scrollTo({ top: y, behavior: "smooth" });
    });
  });
})();
