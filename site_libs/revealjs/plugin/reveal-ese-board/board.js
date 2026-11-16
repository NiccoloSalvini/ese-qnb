/* ESE Board — write over reveal.js slides and draw on a blank board.
 *
 *   C  draw on the slide          B  blank board (one per slide, with pages)
 *   P  pen   H  highlighter   L  laser pointer   E  eraser (or right-drag, or the pen's eraser end)
 *   1–6 colour   [ ] size   Shift while drawing: straight line (snaps to horizontal/vertical)
 *   ⌘Z / ⌘⇧Z undo / redo   Delete clear this page (⇧Delete: the whole deck)   G board background
 *   N new board page   Esc stop drawing
 *
 * Ink is vector (SVG) in slide coordinates, so it stays put when the window is resized.
 * It is saved in the browser (localStorage), can be downloaded and reloaded as JSON,
 * a board page can be saved as PNG, and annotations are printed with ?print-pdf.
 * Strokes are drawn with perfect-freehand (MIT, Steve Ruiz). The rest: MIT, Niccolò Salvini, 2026.
 */
(function () {
  'use strict';

  var NS = 'http://www.w3.org/2000/svg';
  var LIGHT = ['#1d1d1f', '#AF1F25', '#2471A3', '#1E8449', '#B7791F', '#7D3C98'];
  var DARK = ['#F7F5F0', '#FF8A80', '#8EC5F0', '#86E0A8', '#F5D27A', '#D2AEF0'];
  var COLOR_NAMES = ['Ink', 'Red', 'Blue', 'Green', 'Gold', 'Purple'];
  var SIZES = { pen: [2.5, 4.5, 8], hl: [14, 22, 34], eraser: [10, 20, 34], laser: [7, 7, 7] };
  var BGS = [
    ['plain', 'Plain'], ['grid', 'Squared'], ['dots', 'Dots'], ['lines', 'Ruled'],
    ['axes', 'Axes'], ['quadrant', 'First quadrant'], ['dark', 'Dark board']
  ];
  var LASER_MS = 520;

  var I = {
    pen: '<path d="M4 20l1.2-4.6L15.4 5.2a2 2 0 0 1 2.8 0l.6.6a2 2 0 0 1 0 2.8L8.6 18.8z"/><path d="M13.6 7l3.4 3.4"/>',
    hl: '<path d="M9.5 10.5l-5 5V19h3.5l5-5"/><path d="M9.5 10.5l5.8-5.8a1.6 1.6 0 0 1 2.3 0l1.7 1.7a1.6 1.6 0 0 1 0 2.3L13.5 14.5z"/><path d="M13 21h7"/>',
    laser: '<circle cx="12" cy="12" r="3.2"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1"/>',
    eraser: '<path d="M8 20h12"/><path d="M4.7 14.3l8.6-8.6a2 2 0 0 1 2.8 0l2.2 2.2a2 2 0 0 1 0 2.8L10 19H7.4l-2.7-2.7a1.4 1.4 0 0 1 0-2z"/><path d="M9.3 9.7l5 5"/>',
    undo: '<path d="M9 14L4 9l5-5"/><path d="M4 9h10.5a5.5 5.5 0 0 1 0 11H11"/>',
    redo: '<path d="M15 14l5-5-5-5"/><path d="M20 9H9.5a5.5 5.5 0 0 0 0 11H13"/>',
    trash: '<path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/>',
    board: '<rect x="3" y="4" width="18" height="12.5" rx="2"/><path d="M8.5 21l3.5-4.5 3.5 4.5"/>',
    slide: '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M7 21h10"/>',
    bg: '<rect x="3.5" y="3.5" width="17" height="17" rx="2"/><path d="M3.5 9.2h17M3.5 14.8h17M9.2 3.5v17M14.8 3.5v17"/>',
    prev: '<path d="M14.5 6l-6 6 6 6"/>',
    next: '<path d="M9.5 6l6 6-6 6"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    more: '<circle cx="5.5" cy="12" r="1.2"/><circle cx="12" cy="12" r="1.2"/><circle cx="18.5" cy="12" r="1.2"/>',
    close: '<path d="M6 6l12 12M18 6L6 18"/>'
  };
  function icon(name) {
    return '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">' + I[name] + '</svg>';
  }

  function load(key) { try { return JSON.parse(localStorage.getItem(key)); } catch (e) { return null; } }
  function store_(key, val) { try { localStorage.setItem(key, JSON.stringify(val)); return true; } catch (e) { return false; } }
  function r1(n) { return Math.round(n * 10) / 10; }

  /* ---------- stroke geometry ---------- */

  var pathCache = new WeakMap();

  function outlineToPath(pts) {
    if (!pts.length) return '';
    var d = ['M', pts[0][0].toFixed(1), pts[0][1].toFixed(1), 'Q'];
    for (var i = 0; i < pts.length; i++) {
      var a = pts[i], b = pts[(i + 1) % pts.length];
      d.push(a[0].toFixed(1), a[1].toFixed(1), ((a[0] + b[0]) / 2).toFixed(1), ((a[1] + b[1]) / 2).toFixed(1));
    }
    d.push('Z');
    return d.join(' ');
  }

  function strokeOptions(st, live) {
    var line = !!st.ln;
    if (st.t === 'hl') {
      return { size: st.s, thinning: 0, smoothing: 0.6, streamline: 0.5, simulatePressure: false, last: !live };
    }
    return {
      size: st.s,
      thinning: line ? 0 : (st.sp ? 0.55 : 0.68),
      smoothing: 0.6,
      streamline: line ? 0 : 0.42,
      simulatePressure: !line && !!st.sp,
      last: !live
    };
  }

  function strokePath(st, live) {
    if (!live && pathCache.has(st)) return pathCache.get(st);
    var d = outlineToPath(window.PerfectFreehand.getStroke(st.p, strokeOptions(st, live)));
    if (!live) pathCache.set(st, d);
    return d;
  }

  // a highlighter multiplies on paper and screens on a dark background
  function strokeMarkup(st, onDark) {
    var attrs = st.t === 'hl'
      ? ' fill="' + st.c + '" fill-opacity="' + (onDark ? 0.42 : 0.34) + '" style="mix-blend-mode:' + (onDark ? 'screen' : 'multiply') + '"'
      : ' fill="' + st.c + '"';
    return '<path d="' + strokePath(st) + '"' + attrs + '/>';
  }

  function segDist2(px, py, ax, ay, bx, by) {
    var dx = bx - ax, dy = by - ay, l2 = dx * dx + dy * dy;
    var t = l2 ? Math.max(0, Math.min(1, ((px - ax) * dx + (py - ay) * dy) / l2)) : 0;
    var x = ax + t * dx - px, y = ay + t * dy - py;
    return x * x + y * y;
  }

  function hits(st, x, y, r) {
    var rr = r + st.s / 2, rr2 = rr * rr, p = st.p;
    if (p.length === 1) { var dx = p[0][0] - x, dy = p[0][1] - y; return dx * dx + dy * dy <= rr2; }
    for (var i = 1; i < p.length; i++) {
      if (segDist2(x, y, p[i - 1][0], p[i - 1][1], p[i][0], p[i][1]) <= rr2) return true;
    }
    return false;
  }

  /* ---------- board backgrounds (SVG, shared by screen and PNG export) ---------- */

  function bgMarkup(bg, W, H) {
    var paper = '#fdfcf8', out = '';
    var gridLine = 'rgba(36,113,163,0.15)', gridMajor = 'rgba(36,113,163,0.26)';
    function grid(cell, minor, major) {
      var s = '';
      for (var x = cell; x < W; x += cell) s += '<line x1="' + x + '" y1="0" x2="' + x + '" y2="' + H + '" stroke="' + ((x / cell) % 5 ? minor : major) + '" stroke-width="1"/>';
      for (var y = cell; y < H; y += cell) s += '<line x1="0" y1="' + y + '" x2="' + W + '" y2="' + y + '" stroke="' + ((y / cell) % 5 ? minor : major) + '" stroke-width="1"/>';
      return s;
    }
    function axis(x1, y1, x2, y2) {
      var a = Math.atan2(y2 - y1, x2 - x1), L = 14, w = 6;
      var p1 = [x2 - L * Math.cos(a) + w * Math.sin(a), y2 - L * Math.sin(a) - w * Math.cos(a)];
      var p2 = [x2 - L * Math.cos(a) - w * Math.sin(a), y2 - L * Math.sin(a) + w * Math.cos(a)];
      return '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="#3a3a3c" stroke-width="2"/>' +
        '<polygon points="' + x2 + ',' + y2 + ' ' + p1.join(',') + ' ' + p2.join(',') + '" fill="#3a3a3c"/>';
    }
    function label(x, y, t) {
      return '<text x="' + x + '" y="' + y + '" font-family="Source Sans 3, Source Sans Pro, Helvetica, Arial, sans-serif" font-style="italic" font-size="26" fill="#3a3a3c">' + t + '</text>';
    }
    switch (bg) {
      case 'plain':
        out = '<rect width="' + W + '" height="' + H + '" fill="' + paper + '"/>';
        break;
      case 'dots':
        out = '<rect width="' + W + '" height="' + H + '" fill="' + paper + '"/>';
        for (var dx = 32; dx < W; dx += 32) for (var dy = 32; dy < H; dy += 32) out += '<circle cx="' + dx + '" cy="' + dy + '" r="1.7" fill="rgba(29,29,31,0.22)"/>';
        break;
      case 'lines':
        out = '<rect width="' + W + '" height="' + H + '" fill="' + paper + '"/>';
        for (var ly = 80; ly < H; ly += 40) out += '<line x1="0" y1="' + ly + '" x2="' + W + '" y2="' + ly + '" stroke="rgba(36,113,163,0.24)" stroke-width="1"/>';
        out += '<line x1="104" y1="0" x2="104" y2="' + H + '" stroke="rgba(175,31,37,0.38)" stroke-width="1.5"/>';
        break;
      case 'axes':
        out = '<rect width="' + W + '" height="' + H + '" fill="' + paper + '"/>' + grid(32, 'rgba(36,113,163,0.10)', 'rgba(36,113,163,0.18)') +
          axis(40, H / 2, W - 40, H / 2) + axis(W / 2, H - 30, W / 2, 30) +
          label(W - 52, H / 2 + 32, 'x') + label(W / 2 + 14, 52, 'y') + label(W / 2 - 24, H / 2 + 28, 'O');
        break;
      case 'quadrant':
        var ox = 96, oy = H - 80;
        out = '<rect width="' + W + '" height="' + H + '" fill="' + paper + '"/>' + grid(32, 'rgba(36,113,163,0.10)', 'rgba(36,113,163,0.18)') +
          axis(ox - 24, oy, W - 48, oy) + axis(ox, oy + 24, ox, 36) +
          label(W - 60, oy + 34, 'x') + label(ox + 14, 58, 'y') + label(ox - 30, oy + 30, 'O');
        break;
      case 'dark':
        out = '<rect width="' + W + '" height="' + H + '" fill="#1f2b27"/>' + grid(32, 'rgba(255,255,255,0.045)', 'rgba(255,255,255,0.08)');
        break;
      default: // grid
        out = '<rect width="' + W + '" height="' + H + '" fill="' + paper + '"/>' + grid(32, gridLine, gridMajor);
    }
    return out;
  }

  /* ---------- colour of what is under the ink ---------- */

  function parseColor(c) {
    if (!c) return null;
    c = c.trim();
    var m = c.match(/^#([0-9a-f]{3}|[0-9a-f]{6})$/i);
    if (m) {
      var h = m[1].length === 3 ? m[1].replace(/./g, '$&$&') : m[1];
      return [parseInt(h.slice(0, 2), 16), parseInt(h.slice(2, 4), 16), parseInt(h.slice(4, 6), 16), 1];
    }
    m = c.match(/rgba?\(([^)]+)\)/i);
    if (m) {
      var v = m[1].split(/[\s,\/]+/).filter(Boolean).map(parseFloat);
      return [v[0], v[1], v[2], v.length > 3 ? v[3] : 1];
    }
    return null;
  }
  function isDarkColor(c) {
    var v = parseColor(c);
    if (!v || v[3] < 0.5) return null;
    var lum = (0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2]) / 255;
    return lum < 0.5;
  }

  /* ---------- the plugin ---------- */

  function setup(deck) {
    if (deck.isSpeakerNotes && deck.isSpeakerNotes()) return;
    var cfg = deck.getConfig();
    var W = typeof cfg.width === 'number' ? cfg.width : 1280;
    var H = typeof cfg.height === 'number' ? cfg.height : 720;
    var opts = Object.assign({ storage: true }, cfg.eseboard || {});
    var printing = /print-pdf/i.test(window.location.search);
    var STORE_KEY = 'eseboard:v1:' + window.location.pathname;
    var PREF_KEY = 'eseboard:prefs:v1';

    var data = (opts.storage && load(STORE_KEY)) || { v: 1, slides: {}, boards: {} };
    if (!data.slides) data.slides = {};
    if (!data.boards) data.boards = {};
    var prefs = Object.assign({ tool: 'pen', color: 0, size: 1, bg: 'grid' }, load(PREF_KEY) || {});

    var mode = 'off', modeBeforeBoard = 'off', dark = false, overview = false;
    var undoStacks = {}, redoStacks = {};
    var drawing = null, laserPts = [], laserRAF = 0, liveRAF = 0, saveTimer = 0;

    function slideKey(slide) {
      var i = deck.getIndices(slide);
      return i.h + '.' + (i.v || 0);
    }
    function boardOf(key) {
      if (!data.boards[key]) data.boards[key] = { bg: prefs.bg, pages: [[]], page: 0 };
      return data.boards[key];
    }
    function targetId() {
      var k = slideKey();
      return mode === 'board' ? 'b:' + k + ':' + boardOf(k).page : 's:' + k;
    }
    function getStrokes(tid) {
      var parts = tid.split(':');
      if (parts[0] === 's') return data.slides[parts[1]] || (data.slides[parts[1]] = []);
      var b = boardOf(parts[1]);
      var p = +parts[2];
      while (b.pages.length <= p) b.pages.push([]);
      return b.pages[p];
    }
    function setStrokes(tid, arr) {
      var parts = tid.split(':');
      if (parts[0] === 's') data.slides[parts[1]] = arr;
      else boardOf(parts[1]).pages[+parts[2]] = arr;
    }
    function palette() { return dark ? DARK : LIGHT; }

    function save() {
      if (!opts.storage) return;
      clearTimeout(saveTimer);
      saveTimer = setTimeout(function () {
        Object.keys(data.slides).forEach(function (k) { if (!data.slides[k].length) delete data.slides[k]; });
        Object.keys(data.boards).forEach(function (k) {
          var b = data.boards[k];
          if (b.pages.every(function (p) { return !p.length; }) && b.pages.length <= 1) delete data.boards[k];
        });
        if (!store_(STORE_KEY, data)) toast('Browser storage is full: download the ink to keep it.');
      }, 350);
    }
    function savePrefs() { store_(PREF_KEY, prefs); }

    /* history */
    function pushUndo(tid, snapshot) {
      (undoStacks[tid] = undoStacks[tid] || []).push(snapshot || getStrokes(tid).slice());
      if (undoStacks[tid].length > 200) undoStacks[tid].shift();
      redoStacks[tid] = [];
    }
    function undo() {
      var tid = targetId(), u = undoStacks[tid];
      if (!u || !u.length) return;
      (redoStacks[tid] = redoStacks[tid] || []).push(getStrokes(tid).slice());
      setStrokes(tid, u.pop());
      renderInk(); save(); updateToolbar();
    }
    function redo() {
      var tid = targetId(), r = redoStacks[tid];
      if (!r || !r.length) return;
      (undoStacks[tid] = undoStacks[tid] || []).push(getStrokes(tid).slice());
      setStrokes(tid, r.pop());
      renderInk(); save(); updateToolbar();
    }
    function clearPage() {
      var tid = targetId();
      if (!getStrokes(tid).length) return;
      pushUndo(tid);
      setStrokes(tid, []);
      renderInk(); save(); updateToolbar();
    }
    function clearAll() {
      if (!window.confirm('Erase all the ink in this deck — every slide and every board?')) return;
      data = { v: 1, slides: {}, boards: {} };
      undoStacks = {}; redoStacks = {};
      render(); save();
    }

    /* ---------- DOM ---------- */

    var revealEl = deck.getRevealElement();
    var slidesEl = deck.getSlidesElement();

    var layer = document.createElement('div');
    layer.className = 'eb-layer';
    layer.innerHTML =
      '<svg class="eb-svg" xmlns="' + NS + '" viewBox="0 0 ' + W + ' ' + H + '" preserveAspectRatio="none">' +
      '<g class="eb-bg"></g><g class="eb-ink"></g><path class="eb-live"/><path class="eb-laser"/></svg>';
    var svg = layer.querySelector('svg');
    var bgG = svg.querySelector('.eb-bg');
    var inkG = svg.querySelector('.eb-ink');
    var liveEl = svg.querySelector('.eb-live');
    var laserEl = svg.querySelector('.eb-laser');

    var cursor = document.createElement('div');
    cursor.className = 'eb-cursor';

    var launch = document.createElement('div');
    launch.className = 'eb-launch';
    launch.innerHTML =
      '<button type="button" data-act="draw" title="Draw on the slide (C)" aria-label="Draw on the slide">' + icon('pen') + '</button>' +
      '<button type="button" data-act="board" title="Blank board (B)" aria-label="Blank board">' + icon('board') + '</button>';

    var bar = document.createElement('div');
    bar.className = 'eb-bar';
    bar.setAttribute('role', 'toolbar');
    bar.setAttribute('aria-label', 'Drawing tools');
    var swatches = COLOR_NAMES.map(function (n, i) {
      return '<button type="button" class="eb-swatch" data-color="' + i + '" title="' + n + ' (' + (i + 1) + ')" aria-label="' + n + '"><span></span></button>';
    }).join('');
    var sizes = [0, 1, 2].map(function (i) {
      return '<button type="button" class="eb-size" data-size="' + i + '" title="' + ['Fine', 'Medium', 'Bold'][i] + ' ([ / ])" aria-label="' + ['Fine', 'Medium', 'Bold'][i] + '"><span style="--d:' + [5, 8, 12][i] + 'px"></span></button>';
    }).join('');
    bar.innerHTML =
      '<div class="eb-group">' +
      '<button type="button" class="eb-tool" data-tool="pen" title="Pen (P)" aria-label="Pen">' + icon('pen') + '</button>' +
      '<button type="button" class="eb-tool" data-tool="hl" title="Highlighter (H)" aria-label="Highlighter">' + icon('hl') + '</button>' +
      '<button type="button" class="eb-tool" data-tool="laser" title="Laser pointer (L)" aria-label="Laser pointer">' + icon('laser') + '</button>' +
      '<button type="button" class="eb-tool" data-tool="eraser" title="Eraser (E, or right-drag)" aria-label="Eraser">' + icon('eraser') + '</button>' +
      '</div><i class="eb-sep"></i>' +
      '<div class="eb-group eb-colors">' + swatches + '</div><i class="eb-sep"></i>' +
      '<div class="eb-group eb-sizes">' + sizes + '</div><i class="eb-sep"></i>' +
      '<div class="eb-group">' +
      '<button type="button" data-act="undo" title="Undo (⌘Z)" aria-label="Undo">' + icon('undo') + '</button>' +
      '<button type="button" data-act="redo" title="Redo (⌘⇧Z)" aria-label="Redo">' + icon('redo') + '</button>' +
      '<button type="button" data-act="clear" title="Clear this page (Delete)" aria-label="Clear this page">' + icon('trash') + '</button>' +
      '</div><i class="eb-sep"></i>' +
      '<div class="eb-group eb-boardtools">' +
      '<button type="button" data-act="bgmenu" title="Board background (G)" aria-label="Board background">' + icon('bg') + '</button>' +
      '<button type="button" data-act="prevpage" title="Previous board page" aria-label="Previous board page">' + icon('prev') + '</button>' +
      '<span class="eb-page" aria-live="polite">1/1</span>' +
      '<button type="button" data-act="nextpage" title="Next board page" aria-label="Next board page">' + icon('next') + '</button>' +
      '<button type="button" data-act="newpage" title="New board page (N)" aria-label="New board page">' + icon('plus') + '</button>' +
      '<i class="eb-sep"></i></div>' +
      '<div class="eb-group">' +
      '<button type="button" data-act="board" class="eb-boardbtn" title="Blank board (B)" aria-label="Blank board">' + icon('board') + '</button>' +
      '<button type="button" data-act="more" title="More" aria-label="More">' + icon('more') + '</button>' +
      '<button type="button" data-act="off" title="Stop drawing (Esc)" aria-label="Stop drawing">' + icon('close') + '</button>' +
      '</div>';

    var pop = document.createElement('div');
    pop.className = 'eb-pop';
    pop.hidden = true;

    var toastEl = document.createElement('div');
    toastEl.className = 'eb-toast';

    var fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = 'application/json,.json';
    fileInput.hidden = true;

    if (!printing) {
      slidesEl.appendChild(layer);
      revealEl.appendChild(cursor);
      revealEl.appendChild(launch);
      revealEl.appendChild(bar);
      revealEl.appendChild(pop);
      revealEl.appendChild(toastEl);
      revealEl.appendChild(fileInput);
    }

    var toastTimer = 0;
    function toast(msg) {
      toastEl.textContent = msg;
      toastEl.classList.add('eb-show');
      clearTimeout(toastTimer);
      toastTimer = setTimeout(function () { toastEl.classList.remove('eb-show'); }, 2200);
    }

    /* ---------- rendering ---------- */

    function slideDark() {
      var slide = deck.getCurrentSlide();
      if (!slide) return false;
      var c = slide.getAttribute('data-background-color');
      var d = isDarkColor(c);
      if (d !== null) return d;
      var bgEl = deck.getSlideBackground && deck.getSlideBackground(slide);
      if (bgEl) {
        d = isDarkColor(getComputedStyle(bgEl).backgroundColor);
        if (d !== null) return d;
      }
      d = isDarkColor(getComputedStyle(revealEl).backgroundColor);
      if (d !== null) return d;
      return isDarkColor(getComputedStyle(document.body).backgroundColor) || false;
    }

    function renderInk() {
      inkG.innerHTML = getStrokes(targetId()).map(function (st) { return strokeMarkup(st, dark); }).join('');
    }

    function render() {
      var k = slideKey();
      var inBoard = mode === 'board';
      layer.classList.toggle('eb-active', mode !== 'off' && !overview);
      layer.classList.toggle('eb-boardmode', inBoard);
      layer.classList.toggle('eb-hidden', overview);
      revealEl.classList.toggle('eb-drawing', mode !== 'off');
      bgG.innerHTML = inBoard ? bgMarkup(boardOf(k).bg, W, H) : '';
      dark = inBoard ? boardOf(k).bg === 'dark' : slideDark();
      renderInk();
      updateToolbar();
      updateCursorStyle();
    }

    function updateToolbar() {
      var show = mode !== 'off' && !overview;
      bar.classList.toggle('eb-show', show);
      launch.classList.toggle('eb-show', mode === 'off' && !overview);
      bar.classList.toggle('eb-inboard', mode === 'board');
      bar.querySelectorAll('.eb-tool').forEach(function (b) { b.classList.toggle('eb-on', b.dataset.tool === prefs.tool); });
      var pal = palette();
      bar.querySelectorAll('.eb-swatch').forEach(function (b) {
        var i = +b.dataset.color;
        b.style.setProperty('--c', pal[i]);
        b.classList.toggle('eb-on', i === prefs.color);
      });
      bar.querySelectorAll('.eb-size').forEach(function (b) {
        b.style.setProperty('--c', pal[prefs.color]);
        b.classList.toggle('eb-on', +b.dataset.size === prefs.size);
      });
      var tid = targetId();
      bar.querySelector('[data-act="undo"]').disabled = !(undoStacks[tid] && undoStacks[tid].length);
      bar.querySelector('[data-act="redo"]').disabled = !(redoStacks[tid] && redoStacks[tid].length);
      bar.querySelector('[data-act="clear"]').disabled = !getStrokes(tid).length;
      var bb = bar.querySelector('.eb-boardbtn');
      bb.innerHTML = icon(mode === 'board' ? 'slide' : 'board');
      bb.title = mode === 'board' ? 'Back to the slide (B)' : 'Blank board (B)';
      bb.setAttribute('aria-label', bb.title);
      if (mode === 'board') {
        var b = boardOf(slideKey());
        bar.querySelector('.eb-page').textContent = (b.page + 1) + '/' + b.pages.length;
        bar.querySelector('[data-act="prevpage"]').disabled = b.page === 0;
        bar.querySelector('[data-act="nextpage"]').disabled = b.page >= b.pages.length - 1;
      }
    }

    function updateCursorStyle() {
      var t = prefs.tool, scale = layer.getBoundingClientRect().width / W || 1;
      cursor.className = 'eb-cursor eb-c-' + t;
      var d;
      if (t === 'eraser') d = SIZES.eraser[prefs.size] * 2 * scale;
      else if (t === 'laser') d = 14;
      else d = Math.max(5, SIZES[t][prefs.size] * scale);
      cursor.style.setProperty('--d', d + 'px');
      cursor.style.setProperty('--c', t === 'laser' ? '#ff2a2a' : palette()[prefs.color]);
    }

    /* ---------- modes and tools ---------- */

    function setMode(m) {
      if (m === mode) return;
      if (m === 'board' && mode !== 'board') modeBeforeBoard = mode;
      mode = m;
      closePop();
      endLaser();
      render();
    }
    function toggleBoard() { setMode(mode === 'board' ? (modeBeforeBoard === 'draw' ? 'draw' : 'off') : 'board'); }
    function toggleDraw() { setMode(mode === 'off' ? 'draw' : 'off'); }
    function setTool(t) { prefs.tool = t; savePrefs(); if (t !== 'laser') endLaser(); updateToolbar(); updateCursorStyle(); }
    function setColor(i) { prefs.color = i; if (prefs.tool === 'eraser' || prefs.tool === 'laser') prefs.tool = 'pen'; savePrefs(); updateToolbar(); updateCursorStyle(); }
    function setSize(i) { prefs.size = Math.max(0, Math.min(2, i)); savePrefs(); updateToolbar(); updateCursorStyle(); }
    function setBg(bg) {
      var b = boardOf(slideKey());
      b.bg = bg; prefs.bg = bg; savePrefs(); save(); render();
    }
    function cycleBg() {
      var b = boardOf(slideKey());
      var i = BGS.findIndex(function (x) { return x[0] === b.bg; });
      setBg(BGS[(i + 1) % BGS.length][0]);
      toast(BGS[(i + 1) % BGS.length][1]);
    }
    function goPage(delta) {
      var b = boardOf(slideKey());
      b.page = Math.max(0, Math.min(b.pages.length - 1, b.page + delta));
      save(); render();
    }
    function newPage() {
      var b = boardOf(slideKey());
      b.pages.splice(b.page + 1, 0, []);
      b.page += 1;
      save(); render();
      toast('Board page ' + (b.page + 1));
    }

    /* ---------- pointer input ---------- */

    function toLocal(e) {
      var r = layer.getBoundingClientRect();
      return [(e.clientX - r.left) * W / r.width, (e.clientY - r.top) * H / r.height];
    }
    function pressureOf(e) {
      return e.pointerType === 'pen' ? Math.max(0.05, e.pressure || 0.5) : 0.5;
    }

    function moveCursor(e) {
      cursor.style.transform = 'translate(' + e.clientX + 'px,' + e.clientY + 'px)';
      cursor.classList.add('eb-visible');
    }

    function drawLive() {
      liveRAF = 0;
      if (!drawing || drawing.kind !== 'ink') { liveEl.setAttribute('d', ''); return; }
      var st = drawing.st;
      liveEl.setAttribute('d', strokePath(st, true));
      liveEl.setAttribute('fill', st.c);
      if (st.t === 'hl') { liveEl.setAttribute('fill-opacity', dark ? '0.42' : '0.34'); liveEl.style.mixBlendMode = dark ? 'screen' : 'multiply'; }
      else { liveEl.removeAttribute('fill-opacity'); liveEl.style.mixBlendMode = ''; }
    }
    function scheduleLive() { if (!liveRAF) liveRAF = requestAnimationFrame(drawLive); }

    function snapLine(o, p) {
      var dx = p[0] - o[0], dy = p[1] - o[1];
      var a = Math.abs(Math.atan2(dy, dx) * 180 / Math.PI);
      if (a < 5 || a > 175) return [p[0], o[1], p[2]];
      if (Math.abs(a - 90) < 5) return [o[0], p[1], p[2]];
      return p;
    }

    function eraseAlong(from, to) {
      var tid = drawing.tid, arr = getStrokes(tid), r = SIZES.eraser[prefs.size];
      var steps = Math.max(1, Math.ceil(Math.hypot(to[0] - from[0], to[1] - from[1]) / (r / 2)));
      var keep = arr.filter(function (st) {
        for (var i = 0; i <= steps; i++) {
          var t = i / steps;
          if (hits(st, from[0] + (to[0] - from[0]) * t, from[1] + (to[1] - from[1]) * t, r)) return false;
        }
        return true;
      });
      if (keep.length !== arr.length) {
        if (!drawing.changed) { pushUndo(tid, drawing.snapshot); drawing.changed = true; }
        setStrokes(tid, keep);
        renderInk();
      }
    }

    function laserFrame() {
      laserRAF = 0;
      var now = performance.now();
      while (laserPts.length && now - laserPts[0][3] > LASER_MS) laserPts.shift();
      if (!laserPts.length) { laserEl.setAttribute('d', ''); return; }
      var pts = laserPts.map(function (p) { return [p[0], p[1], 0.5]; });
      laserEl.setAttribute('d', outlineToPath(window.PerfectFreehand.getStroke(pts, {
        size: SIZES.laser[0], thinning: 0, smoothing: 0.6, streamline: 0.35, simulatePressure: false,
        start: { taper: true }, last: false
      })));
      laserRAF = requestAnimationFrame(laserFrame);
    }
    function addLaser(p) {
      laserPts.push([p[0], p[1], 0.5, performance.now()]);
      if (!laserRAF) laserRAF = requestAnimationFrame(laserFrame);
    }
    function endLaser() { laserPts = []; laserEl.setAttribute('d', ''); }

    function onDown(e) {
      if (mode === 'off' || overview) return;
      e.stopPropagation();
      if (e.button === 1) return;
      e.preventDefault();
      closePop();
      try { layer.setPointerCapture(e.pointerId); } catch (err) { /* synthetic events */ }
      moveCursor(e);
      var p = toLocal(e);
      var tid = targetId();
      if (e.button === 2 || (e.buttons & 32) || prefs.tool === 'eraser') {
        drawing = { kind: 'erase', tid: tid, snapshot: getStrokes(tid).slice(), changed: false, last: p, id: e.pointerId };
        cursor.classList.add('eb-c-erasing');
        eraseAlong(p, p);
        return;
      }
      if (prefs.tool === 'laser') {
        drawing = { kind: 'laser', id: e.pointerId };
        addLaser(p);
        return;
      }
      var tool = prefs.tool === 'hl' ? 'hl' : 'pen';
      var st = { t: tool, c: palette()[prefs.color], s: SIZES[tool][prefs.size], p: [[r1(p[0]), r1(p[1]), pressureOf(e)]] };
      if (e.pointerType !== 'pen') st.sp = 1;
      drawing = { kind: 'ink', st: st, tid: tid, origin: st.p[0], id: e.pointerId };
      scheduleLive();
    }

    function onMove(e) {
      if (mode === 'off' || overview) return;
      e.stopPropagation();
      moveCursor(e);
      if (!drawing) {
        if (prefs.tool === 'laser' && e.pointerType === 'mouse') addLaser(toLocal(e));
        return;
      }
      if (e.pointerId !== drawing.id) return;
      var events = (e.getCoalescedEvents && e.getCoalescedEvents()) || [];
      if (!events.length) events = [e];
      if (drawing.kind === 'erase') {
        var p = toLocal(e);
        eraseAlong(drawing.last, p);
        drawing.last = p;
        return;
      }
      if (drawing.kind === 'laser') { events.forEach(function (ev) { addLaser(toLocal(ev)); }); return; }
      var st = drawing.st;
      if (e.shiftKey || st.ln) {
        var q = toLocal(e);
        st.ln = 1;
        st.p = [drawing.origin, snapLine(drawing.origin, [r1(q[0]), r1(q[1]), 0.5])];
      } else {
        events.forEach(function (ev) {
          var q = toLocal(ev), last = st.p[st.p.length - 1];
          if (Math.abs(q[0] - last[0]) < 0.4 && Math.abs(q[1] - last[1]) < 0.4) return;
          st.p.push([r1(q[0]), r1(q[1]), pressureOf(ev)]);
        });
      }
      scheduleLive();
    }

    function onUp(e) {
      if (!drawing || (e.pointerId !== undefined && e.pointerId !== drawing.id)) return;
      e.stopPropagation();
      var d = drawing;
      drawing = null;
      cursor.classList.remove('eb-c-erasing');
      if (d.kind === 'ink') {
        if (liveRAF) { cancelAnimationFrame(liveRAF); liveRAF = 0; }
        liveEl.setAttribute('d', '');
        pushUndo(d.tid);
        getStrokes(d.tid).push(d.st);
        if (d.tid === targetId()) inkG.insertAdjacentHTML('beforeend', strokeMarkup(d.st, dark));
        save();
      } else if (d.kind === 'erase' && d.changed) {
        save();
      }
      updateToolbar();
    }

    layer.addEventListener('pointerdown', onDown);
    layer.addEventListener('pointermove', onMove);
    layer.addEventListener('pointerup', onUp);
    layer.addEventListener('pointercancel', onUp);
    layer.addEventListener('pointerleave', function () { cursor.classList.remove('eb-visible'); });
    layer.addEventListener('contextmenu', function (e) { if (mode !== 'off') e.preventDefault(); });
    ['touchstart', 'touchmove', 'touchend', 'mousedown', 'click', 'dblclick', 'wheel'].forEach(function (t) {
      layer.addEventListener(t, function (e) { if (mode !== 'off') e.stopPropagation(); }, { passive: true });
    });

    /* ---------- toolbar and popovers ---------- */

    function closePop() { pop.hidden = true; pop.innerHTML = ''; }
    function openPop(anchor, html, onPick) {
      pop.innerHTML = html;
      pop.hidden = false;
      var a = anchor.getBoundingClientRect(), host = revealEl.getBoundingClientRect();
      var pw = pop.offsetWidth;
      var left = Math.min(Math.max(8, a.left + a.width / 2 - pw / 2 - host.left), host.width - pw - 8);
      pop.style.left = left + 'px';
      pop.style.bottom = (host.bottom - a.top + 10) + 'px';
      pop.onclick = function (ev) {
        var it = ev.target.closest('[data-pick]');
        if (!it) return;
        onPick(it.dataset.pick);
      };
    }

    function bgMenu(anchor) {
      var cur = boardOf(slideKey()).bg;
      openPop(anchor, '<div class="eb-pop-title">Board background</div>' + BGS.map(function (b) {
        return '<button type="button" class="eb-item' + (b[0] === cur ? ' eb-on' : '') + '" data-pick="' + b[0] + '"><span class="eb-prev eb-prev-' + b[0] + '"></span>' + b[1] + '</button>';
      }).join(''), function (v) { setBg(v); closePop(); });
    }

    function moreMenu(anchor) {
      var items = [];
      if (mode === 'board') items.push(['png', 'Save this board page as PNG']);
      items.push(['json', 'Download all ink (.json)'], ['load', 'Load ink from a file…'], ['wipe', 'Erase all ink in this deck']);
      openPop(anchor, items.map(function (it) {
        return '<button type="button" class="eb-item" data-pick="' + it[0] + '">' + it[1] + '</button>';
      }).join('') +
        '<div class="eb-keys"><b>C</b> draw · <b>B</b> board · <b>P H L E</b> tools · <b>1–6</b> colour · <b>[ ]</b> size · <b>Shift</b> straight line · <b>⌘Z</b> undo · <b>Del</b> clear · <b>G</b> background · <b>N</b> new page · <b>Esc</b> stop</div>',
        function (v) {
          closePop();
          if (v === 'png') exportPNG();
          else if (v === 'json') exportJSON();
          else if (v === 'load') fileInput.click();
          else if (v === 'wipe') clearAll();
        });
    }

    bar.addEventListener('pointerdown', function (e) { e.stopPropagation(); });
    bar.addEventListener('click', function (e) {
      e.stopPropagation();
      var b = e.target.closest('button');
      if (!b || b.disabled) return;
      if (b.dataset.tool) return setTool(b.dataset.tool);
      if (b.dataset.color) return setColor(+b.dataset.color);
      if (b.dataset.size) return setSize(+b.dataset.size);
      switch (b.dataset.act) {
        case 'undo': undo(); break;
        case 'redo': redo(); break;
        case 'clear': clearPage(); break;
        case 'board': toggleBoard(); break;
        case 'off': setMode('off'); break;
        case 'bgmenu': pop.hidden ? bgMenu(b) : closePop(); break;
        case 'more': pop.hidden ? moreMenu(b) : closePop(); break;
        case 'prevpage': goPage(-1); break;
        case 'nextpage': goPage(1); break;
        case 'newpage': newPage(); break;
      }
    });
    launch.addEventListener('click', function (e) {
      e.stopPropagation();
      var b = e.target.closest('button');
      if (!b) return;
      if (b.dataset.act === 'draw') setMode('draw');
      else if (b.dataset.act === 'board') toggleBoard();
    });
    pop.addEventListener('pointerdown', function (e) { e.stopPropagation(); });

    /* ---------- export / import ---------- */

    function deckName() {
      var f = window.location.pathname.split('/').pop() || 'deck';
      return f.replace(/\.html?$/i, '') || 'deck';
    }
    function download(blob, name) {
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = name;
      document.body.appendChild(a);
      a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 1000);
    }
    function exportJSON() {
      download(new Blob([JSON.stringify(data)], { type: 'application/json' }), deckName() + '-ink.json');
    }
    function exportPNG() {
      var k = slideKey(), b = boardOf(k), scale = 2;
      var markup = '<svg xmlns="' + NS + '" width="' + W * scale + '" height="' + H * scale + '" viewBox="0 0 ' + W + ' ' + H + '">' +
        bgMarkup(b.bg, W, H) + b.pages[b.page].map(function (st) { return strokeMarkup(st, b.bg === 'dark'); }).join('') + '</svg>';
      var img = new Image();
      img.onload = function () {
        var c = document.createElement('canvas');
        c.width = W * scale; c.height = H * scale;
        c.getContext('2d').drawImage(img, 0, 0);
        c.toBlob(function (blob) { download(blob, deckName() + '-board-' + k.replace('.', '-') + '-p' + (b.page + 1) + '.png'); }, 'image/png');
      };
      img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(markup);
    }
    fileInput.addEventListener('change', function () {
      var f = fileInput.files && fileInput.files[0];
      if (!f) return;
      f.text().then(function (txt) {
        var d = JSON.parse(txt);
        if (!d || typeof d !== 'object' || !d.slides || !d.boards) throw new Error('not an ink file');
        data = d; undoStacks = {}; redoStacks = {};
        render(); save(); toast('Ink loaded');
      }).catch(function () { toast('That file is not ink from this board.'); });
      fileInput.value = '';
    });

    /* ---------- keyboard ---------- */

    function typing(t) {
      return t && (t.isContentEditable || /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName));
    }
    function onKey(e) {
      if (printing || typing(e.target)) return;
      if (deck.isOverview && deck.isOverview()) return;
      var k = e.key, lower = k.length === 1 ? k.toLowerCase() : k, handled = true;
      if (e.metaKey || e.ctrlKey) {
        if (mode === 'off') return;
        if (lower === 'z') { if (e.shiftKey) redo(); else undo(); }
        else if (lower === 'y') redo();
        else return;
      } else if (e.altKey) {
        return;
      } else if (lower === 'c') toggleDraw();
      else if (lower === 'b') toggleBoard();
      else if (lower === 'l' && mode === 'off') { setMode('draw'); setTool('laser'); }
      else if (mode === 'off') return;
      else {
        switch (lower) {
          case 'p': setTool('pen'); break;
          case 'h': setTool('hl'); break;
          case 'l': setTool('laser'); break;
          case 'e': setTool('eraser'); break;
          case '1': case '2': case '3': case '4': case '5': case '6': setColor(+lower - 1); break;
          case '[': setSize(prefs.size - 1); break;
          case ']': setSize(prefs.size + 1); break;
          case 'Delete': case 'Backspace': if (e.shiftKey) clearAll(); else clearPage(); break;
          case 'Escape': if (!pop.hidden) closePop(); else setMode('off'); break;
          case 'g': if (mode === 'board') cycleBg(); else handled = false; break;
          case 'n': if (mode === 'board') newPage(); else handled = false; break;
          default: handled = false;
        }
      }
      if (handled) { e.preventDefault(); e.stopImmediatePropagation(); }
    }
    window.addEventListener('keydown', onKey, true);

    if (deck.addKeyBinding) {
      // listed in reveal's help overlay (?); the keys themselves are handled above
      deck.addKeyBinding({ keyCode: 67, key: 'C', description: 'Draw on the slide' }, toggleDraw);
      deck.addKeyBinding({ keyCode: 66, key: 'B', description: 'Blank board' }, toggleBoard);
    }

    /* ---------- reveal events ---------- */

    deck.on('ready', render);
    deck.on('slidechanged', function () {
      if (drawing) onUp({ pointerId: drawing.id, stopPropagation: function () {} });
      closePop(); endLaser();
      render();
      layer.classList.remove('eb-fade'); void layer.offsetWidth; layer.classList.add('eb-fade');
    });
    deck.on('overviewshown', function () { overview = true; closePop(); render(); });
    deck.on('overviewhidden', function () { overview = false; render(); });
    deck.on('resize', updateCursorStyle);

    /* ---------- print: annotations go into the PDF ---------- */

    if (printing) {
      deck.on('pdf-ready', function () {
        deck.getSlides().forEach(function (slide) {
          var strokes = data.slides[slideKey(slide)];
          if (!strokes || !strokes.length) return;
          var s = document.createElementNS(NS, 'svg');
          s.setAttribute('class', 'eb-print');
          s.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
          s.setAttribute('width', W);
          s.setAttribute('height', H);
          var onDark = !!isDarkColor(slide.getAttribute('data-background-color'));
          s.innerHTML = strokes.map(function (st) { return strokeMarkup(st, onDark); }).join('');
          var page = slide.closest('.pdf-page') || slide;
          var top = parseFloat(slide.style.top) || 0, left = parseFloat(slide.style.left) || 0;
          s.style.top = top + 'px';
          s.style.left = left + 'px';
          page.appendChild(s);
        });
      });
    }
  }

  window.RevealEseBoard = { id: 'eseboard', init: setup };
})();
