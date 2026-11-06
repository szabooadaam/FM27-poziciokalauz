/* Offline működés: az app fájljai a telefonon is tárolódnak.
 * Ha van net, mindig a friss fájlokat tölti le (így a kezdőképernyős app is frissül),
 * net nélkül a tárolt példányt mutatja. Új kiadásnál érdemes a VERSION-t is növelni.
 * A címbetűtípus (Google Fonts) az első letöltés után szintén eltárolódik. */
const VERSION = 'fm27-poziciokalauz-1.2-1';
const FONTS = 'fm27-poziciokalauz-fonts';
const FILES = [
  './',
  './index.html',
  './manifest.webmanifest',
  './css/app.css',
  './js/app.js',
  './fonts/inter-latin-wght-normal.woff2',
  './fonts/inter-latin-ext-wght-normal.woff2',
  './icons/icon-32.png',
  './icons/icon-180.png',
  './icons/icon-192.png',
  './icons/icon-512.png',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => c.addAll(FILES.map((u) => new Request(u, { cache: 'reload' })))).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== VERSION && k !== FONTS).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  // betűtípus: ha már megvan, a tárolt példány (gyors, offline is)
  if (url.hostname === 'fonts.googleapis.com' || url.hostname === 'fonts.gstatic.com') {
    e.respondWith(caches.open(FONTS).then((c) => c.match(e.request).then((hit) => hit || fetch(e.request).then((res) => {
      if (res && (res.ok || res.type === 'opaque')) c.put(e.request, res.clone());
      return res;
    }))));
    return;
  }
  if (url.origin !== location.origin) return;
  // előbb a hálózat (friss), ha nincs net, a tárolt példány
  e.respondWith(
    fetch(e.request, { cache: 'no-store' })
      .then((res) => {
        if (res && res.ok) { const copy = res.clone(); caches.open(VERSION).then((c) => c.put(e.request, copy)); }
        return res;
      })
      .catch(() => caches.open(VERSION).then((c) => c.match(e.request, { ignoreSearch: true })).then((hit) => hit || caches.match('./index.html')))
  );
});
