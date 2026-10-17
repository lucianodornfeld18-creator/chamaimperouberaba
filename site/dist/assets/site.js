/* Chácara Império — interações leves (sem dependências) */
(function () {
  "use strict";

  /* Menu do celular */
  var toggle = document.querySelector("[data-nav-toggle]");
  var header = document.querySelector("[data-header]");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    });
  }

  /* Vídeo do topo: horizontal (1920x1080) no computador, em pé (720x1280) no celular. Só carrega depois
     da página, e não carrega com economia de dados ativa ou preferência por menos movimento.
     A foto continua sendo a imagem principal até o vídeo começar. */
  var video = document.querySelector("[data-hero-video]");
  if (video) {
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var conn = navigator.connection || {};
    var slow = conn.saveData || /(^|-)2g$/.test(conn.effectiveType || "");
    var wide = window.matchMedia && window.matchMedia("(min-width: 768px)").matches;
    var AV1 = 'video/mp4; codecs="av01.0.08M.08"';
    var sources = wide ? [["data-av1", AV1], ["data-mp4", "video/mp4"]] : [["data-mav1", AV1], ["data-mmp4", "video/mp4"]];
    if (!reduce && !slow) {
      var start = function () {
        sources.forEach(function (s) {
          var url = video.getAttribute(s[0]);
          if (url) {
            var el = document.createElement("source");
            el.src = url; el.type = s[1];
            video.appendChild(el);
          }
        });
        if (!video.querySelector("source")) { return; }
        video.load();
        var p = video.play();
        if (p && p.then) {
          p.then(function () { video.classList.add("is-playing"); }).catch(function () {});
        }
        video.addEventListener("playing", function () { video.classList.add("is-playing"); });
      };
      var delay = wide ? 300 : 900;
      if (document.readyState === "complete") { setTimeout(start, delay); }
      else { window.addEventListener("load", function () { setTimeout(start, delay); }); }
    }
  }

  /* Monta a mensagem e abre o WhatsApp — nada é enviado ao site */
  var form = document.querySelector("[data-composer]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var f = form.elements;
      var lines = ["Olá! Cheguei pelo site da Chácara Império."];
      lines.push("Quero consultar: " + (f.tipo.value || "uma data"));
      if (f.data.value) {
        var d = f.data.value.split("-");
        lines.push("Data: " + d[2] + "/" + d[1] + "/" + d[0]);
      }
      if (f.pessoas.value) { lines.push("Número de pessoas: " + f.pessoas.value); }
      if (f.nome.value.trim()) { lines.push("Meu nome: " + f.nome.value.trim()); }
      var url = "https://wa.me/" + form.getAttribute("data-wa") + "?text=" + encodeURIComponent(lines.join("\n"));
      window.open(url, "_blank", "noopener");
    });
  }

  /* Galeria: filtros + visualizador */
  var gallery = document.querySelector("[data-gallery]");
  if (gallery) {
    var links = Array.prototype.slice.call(gallery.querySelectorAll("a[data-full]"));
    var buttons = document.querySelectorAll("[data-filter]");
    Array.prototype.forEach.call(buttons, function (b) {
      b.addEventListener("click", function () {
        var cat = b.getAttribute("data-filter");
        Array.prototype.forEach.call(buttons, function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        links.forEach(function (a) {
          a.hidden = !(cat === "todas" || a.getAttribute("data-cat") === cat);
        });
      });
    });
    var dlg = document.querySelector("[data-lightbox]");
    if (dlg && dlg.showModal) {
      var im = dlg.querySelector("img"), cap = dlg.querySelector("figcaption"), idx = 0;
      var visible = function () { return links.filter(function (a) { return !a.hidden; }); };
      var show = function (i) {
        var list = visible(); if (!list.length) { return; }
        idx = (i + list.length) % list.length;
        var a = list[idx];
        im.src = a.getAttribute("data-full");
        im.alt = a.querySelector("img").alt;
        cap.textContent = a.getAttribute("data-caption") || "";
      };
      links.forEach(function (a) {
        a.addEventListener("click", function (e) {
          e.preventDefault();
          show(visible().indexOf(a));
          dlg.showModal();
        });
      });
      dlg.querySelector("[data-prev]").addEventListener("click", function () { show(idx - 1); });
      dlg.querySelector("[data-next]").addEventListener("click", function () { show(idx + 1); });
      dlg.querySelector("[data-close]").addEventListener("click", function () { dlg.close(); });
      dlg.addEventListener("click", function (e) { if (e.target === dlg) { dlg.close(); } });
      document.addEventListener("keydown", function (e) {
        if (!dlg.open) { return; }
        if (e.key === "ArrowLeft") { show(idx - 1); }
        if (e.key === "ArrowRight") { show(idx + 1); }
      });
      var hash = location.hash.replace("#foto-", "");
      if (hash) {
        var target = document.getElementById("foto-" + hash);
        if (target) { setTimeout(function () { target.click(); }, 200); }
      }
    }
  }
})();
