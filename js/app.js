/* FM27 Pozíciókalauz – fülek, lapozás (gombbal vagy oldalra húzással), felállás-váltó, gyorslista-ugrás.
   A gesztusok a KISPAD app Csapat fülének lapozóját követik. */
(function () {
  const $ = (s, el) => (el || document).querySelector(s);
  const $$ = (s, el) => Array.from((el || document).querySelectorAll(s));
  const store = {
    get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* privát mód */ } },
  };

  const TABS = $$('.tabbar button').map((b) => b.dataset.go);
  const pagers = {};   // fülenként: { page, setPage }
  let tab = null;

  // ---------- lapozó egy fülön belül ----------
  function initPager(section) {
    const key = section.dataset.tab;
    const seg = $('.seg', section); const thumb = $('.seg-thumb', seg);
    const btns = $$('button', seg);
    const pager = $('.pager', section); const track = $('.track', section);
    const pages = $$('.pg', section);
    const n = pages.length;
    const st = { page: 0 };
    let swallow = false;

    function setPage(p, instant) {
      st.page = Math.max(0, Math.min(n - 1, p));
      track.style.transition = instant ? 'none' : ''; thumb.style.transition = instant ? 'none' : '';
      track.style.transform = 'translateX(' + (-st.page * 100 / n) + '%)';
      thumb.style.transform = 'translateX(' + (st.page * 100) + '%)';
      btns.forEach((b, i) => b.setAttribute('aria-selected', String(i === st.page)));
      pages.forEach((pg, i) => { pg.inert = i !== st.page; });
      if (!instant) setCompact(pages[st.page].scrollTop > 30);
      store.set('pk.page.' + key, String(st.page));
    }
    seg.addEventListener('click', (e) => { const b = e.target.closest('button[data-page]'); if (b) setPage(Number(b.dataset.page)); });

    // oldalra húzás: a lapok az ujjat követik, a fenti kijelölés is vele mozog
    let d = null;
    pager.addEventListener('pointerdown', (e) => {
      if (e.pointerType === 'mouse' && e.button !== 0) return;
      d = { x: e.clientX, y: e.clientY, t: Date.now(), mode: null, w: pager.clientWidth };
    });
    pager.addEventListener('pointermove', (e) => {
      if (!d) return;
      const dx = e.clientX - d.x; const dy = e.clientY - d.y;
      if (!d.mode) {
        if (Math.abs(dx) > 10 && Math.abs(dx) > Math.abs(dy) * 1.3) { d.mode = 'x'; try { pager.setPointerCapture(e.pointerId); } catch (err) { /* nem baj */ } }
        else if (Math.abs(dy) > 10) { d = null; return; }
      }
      if (d.mode === 'x') {
        const edge = (dx > 0 && st.page === 0) || (dx < 0 && st.page === n - 1);
        const off = edge ? dx * 0.28 : dx;
        track.style.transition = 'none'; thumb.style.transition = 'none';
        track.style.transform = 'translateX(calc(' + (-st.page * 100 / n) + '% + ' + off + 'px))';
        const p = Math.max(0, Math.min(n - 1, st.page - off / d.w));
        thumb.style.transform = 'translateX(' + (p * 100) + '%)';
      }
    });
    const end = (e) => {
      if (!d) return;
      if (d.mode === 'x') {
        swallow = true; setTimeout(() => { swallow = false; }, 60);
        const dx = e.clientX - d.x; const fast = Date.now() - d.t < 260 && Math.abs(dx) > 30;
        if (dx < -d.w * 0.22 || (fast && dx < 0)) setPage(st.page + 1);
        else if (dx > d.w * 0.22 || (fast && dx > 0)) setPage(st.page - 1);
        else setPage(st.page);
      }
      d = null;
    };
    pager.addEventListener('pointerup', end);
    pager.addEventListener('pointercancel', () => { if (d && d.mode === 'x') setPage(st.page); d = null; });
    // húzás után ne süljön el a koppintás (pl. a gyorslistán)
    pager.addEventListener('click', (e) => { if (swallow) { e.stopPropagation(); e.preventDefault(); } }, true);

    const saved = Number(store.get('pk.page.' + key));
    setPage(saved >= 0 && saved < n ? saved : 0, true);
    pagers[key] = { setPage, get page() { return st.page; }, pages };
  }

  // ---------- összecsukódó alsó sáv ----------
  // Lefelé görgetve összemegy (csak piktogramok), felfelé görgetve vagy a lap tetején kinyílik (felirattal).
  // Kis ugrálásra nem reagál: egy irányban legalább 12 px görgetés kell a váltáshoz.
  const bar = $('#tabbar');
  let compact = false;
  const scrollSt = new WeakMap();
  function setCompact(c) {
    if (c === compact) return;
    compact = c;
    bar.classList.toggle('compact', c);
  }
  document.addEventListener('scroll', (e) => {
    const el = e.target;
    if (!el.classList || !el.classList.contains('pg')) return;
    const y = el.scrollTop;
    const max = el.scrollHeight - el.clientHeight;
    const s = scrollSt.get(el) || { y: 0, acc: 0 };
    const dy = y - s.y;
    s.y = y;
    if (y > max - 2 && dy < 0) { scrollSt.set(el, s); return; }   // az alján az iOS visszarugózása ne nyissa ki
    s.acc = (dy > 0) === (s.acc > 0) ? s.acc + dy : dy;
    scrollSt.set(el, s);
    if (y < 30) setCompact(false);
    else if (s.acc > 12) setCompact(true);
    else if (s.acc < -12) setCompact(false);
  }, { capture: true, passive: true });

  // ---------- fülek ----------
  function setTab(t) {
    if (!TABS.includes(t)) t = TABS[0];
    tab = t;
    setCompact(false);
    TABS.forEach((name) => { $('#tab-' + name).hidden = name !== t; });
    $$('.tabbar button').forEach((b) => { if (b.dataset.go === t) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current'); });
    $('#lens').style.transform = 'translateX(' + (TABS.indexOf(t) * 100) + '%)';
    store.set('pk.tab', t);
  }
  $('#tabbar').addEventListener('click', (e) => {
    const b = e.target.closest('button[data-go]');
    if (!b) return;
    if (b.dataset.go === tab) {   // az aktív fülre koppintva a lap tetejére görget
      const p = pagers[tab]; if (p) p.pages[p.page].scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }
    setTab(b.dataset.go);
  });

  // ---------- Felállás: labdával / labda nélkül ----------
  $$('.seg2').forEach((sg) => {
    const fig = document.getElementById('fig-' + sg.dataset.fig);
    sg.addEventListener('click', (e) => {
      const b = e.target.closest('button[data-show]');
      if (!b) return;
      const oop = b.dataset.show === 'oop';
      sg.classList.toggle('right', oop);
      $$('button', sg).forEach((x) => x.setAttribute('aria-selected', String(x === b)));
      $('.tf-ip', fig).hidden = oop; $('.tf-oop', fig).hidden = !oop;
    });
  });

  // ---------- Gyorslista: ugrás a szerepkör kártyájára ----------
  document.addEventListener('click', (e) => {
    const b = e.target.closest('button[data-jump]');
    if (!b) return;
    const card = document.getElementById('r' + b.dataset.jump);
    if (!card) return;
    setTab(b.dataset.tab);
    pagers[b.dataset.tab].setPage(Number(b.dataset.page), true);
    const pg = card.closest('.pg');
    requestAnimationFrame(() => {
      pg.scrollTop = card.offsetTop - 8;
      card.classList.remove('flash'); void card.offsetWidth; card.classList.add('flash');
    });
  });

  // ---------- indulás ----------
  $$('.tab').forEach(initPager);
  setTab(store.get('pk.tab') || TABS[0]);
  setTimeout(() => { const sp = document.getElementById('splash'); if (sp) sp.remove(); }, 1500);

  // offline működés + frissítés: előtérbe kerüléskor rákérdez az új változatra, és ha jött, egyszer újratölt
  if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost')) {
    const hadController = !!navigator.serviceWorker.controller;
    let reloaded = false;
    navigator.serviceWorker.addEventListener('controllerchange', () => {
      if (hadController && !reloaded) { reloaded = true; location.reload(); }
    });
    navigator.serviceWorker.register('sw.js', { updateViaCache: 'none' }).then((reg) => {
      const check = () => { reg.update().catch(() => { /* nincs net */ }); };
      document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') check(); });
      window.addEventListener('pageshow', check);
    }).catch(() => { /* offline mód nélkül is működik */ });
  }
})();
