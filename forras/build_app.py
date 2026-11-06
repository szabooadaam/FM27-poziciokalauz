# -*- coding: utf-8 -*-
# Az app index.html-jét állítja elő a szerepkör- és taktikaadatokból.
# Futtatás a forras mappából:  python build_app.py
import os, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from roles_data import R, GROUPS
from tactics_data import COMBOS, ATT, DEF

E = html.escape
VERSION = '1.2'

# ---------- pályarajzok ----------
def pitch_lines(w=68, h=105):
    L = 'class="pl"'
    s = [f'<rect x="0" y="0" width="{w}" height="{h}" class="grass"/>']
    s += [f'<rect x="0" y="{i*h/7:.1f}" width="{w}" height="{h/7:.1f}" class="stripe"/>' for i in range(0, 7, 2)]
    s.append(f'<rect x="1" y="1" width="{w-2}" height="{h-2}" {L}/>')
    s.append(f'<line x1="1" y1="{h/2}" x2="{w-1}" y2="{h/2}" {L}/>')
    s.append(f'<circle cx="{w/2}" cy="{h/2}" r="9.15" {L}/>')
    s.append(f'<rect x="{w/2-20.16}" y="1" width="40.32" height="16.5" {L}/>')
    s.append(f'<rect x="{w/2-9.16}" y="1" width="18.32" height="5.5" {L}/>')
    s.append(f'<rect x="{w/2-20.16}" y="{h-17.5}" width="40.32" height="16.5" {L}/>')
    s.append(f'<rect x="{w/2-9.16}" y="{h-6.5}" width="18.32" height="5.5" {L}/>')
    s.append(f'<path d="M {w/2-7.3} 17.5 A 9.15 9.15 0 0 0 {w/2+7.3} 17.5" {L}/>')
    s.append(f'<path d="M {w/2-7.3} {h-17.5} A 9.15 9.15 0 0 1 {w/2+7.3} {h-17.5}" {L}/>')
    return ''.join(s)

def defs(uid):
    return (f'<defs><marker id="ai{uid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="3.2" markerHeight="3.2" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 z" class="hip"/></marker>'
            f'<marker id="ao{uid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="3.2" markerHeight="3.2" orient="auto-start-reverse">'
            f'<path d="M0 0 L10 5 L0 10 z" class="hoop"/></marker></defs>')

def arrow(a, uid, width=1.1):
    x1, y1, x2, y2, t = a
    cls, m = ('aip', f'ai{uid}') if t == 'ip' else ('aoop', f'ao{uid}')
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" stroke-width="{width}" marker-end="url(#{m})"/>'

def dot(x, y, label, cls='dot', r=3.1):
    return f'<circle cx="{x}" cy="{y}" r="{r}" class="{cls}"/><text x="{x}" y="{y+1.2}" class="dott" text-anchor="middle">{E(label[:3])}</text>'

def mini_pitch(r, uid):
    ph = 'labdával' if r['phase'] == 'IP' else 'labda nélkül'
    s = [f'<svg viewBox="0 0 68 105" role="img" aria-label="{E(r["name"])} {ph}: kiinduló hely és fő mozgások">', defs(uid), pitch_lines()]
    cx, cy, rx, ry = r['zone']
    s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" class="zone {"zip" if r["phase"] == "IP" else "zoop"}"/>')
    s += [arrow(a, uid) for a in r['arrows']]
    s.append(dot(r['base'][0], r['base'][1], r['abbr']))
    s.append('</svg>')
    return ''.join(s)

def combo_svg(players, uid, title):
    s = [f'<svg viewBox="0 0 68 105" role="img" aria-label="{E(title)}: mozgások a pályán">', defs(uid), pitch_lines()]
    for pos, lbl, arrows in players:
        s += [arrow(a, uid) for a in arrows]
    for pos, lbl, arrows in players:
        s.append(dot(pos[0], pos[1], lbl))
    s.append('</svg>')
    return ''.join(s)

def tactic_svg(t, which, uid):
    kind = 'ip' if which == 'ip' else 'oop'
    lbl = 'labdával' if kind == 'ip' else 'labda nélkül'
    s = [f'<svg viewBox="0 0 68 105" role="img" aria-label="{E(t["title"])}, {lbl}: mozgások az alapfelállásból">', defs(uid), pitch_lines()]
    for b in t['base']:
        s.append(f'<circle cx="{b[1]}" cy="{b[2]}" r="2.4" class="ghost"/>')
    for b, p in zip(t['base'], t[which]):
        if abs(b[1]-p[1]) + abs(b[2]-p[2]) > 3:
            s.append(arrow((b[1], b[2], p[1], p[2], kind), uid, 0.8))
    for p in t[which]:
        s.append(dot(p[1], p[2], p[0], 'dot ' + ('dip' if kind == 'ip' else 'doop'), 3.3))
    s.append('</svg>')
    return ''.join(s)

# ---------- kártyák ----------
def chips(items):
    return ''.join(f'<li>{E(a)}</li>' for a in items)

def role_card(r):
    ph = '<span class="ph ph-ip">Labdával</span>' if r['phase'] == 'IP' else '<span class="ph ph-oop">Labda nélkül</span>'
    combo = ''
    if r['good']:
        combo += f'<div class="combo"><h5>Jól kombinálható</h5><ul>{chips(r["good"])}</ul></div>'
    if r['avoid']:
        combo += f'<div class="combo bad"><h5>Kerüld</h5><ul>{chips(r["avoid"])}</ul></div>'
    return f'''<article class="group role" id="r{r["uid"]}">
<div class="role-top"><div class="mini">{mini_pitch(r, r["uid"])}</div>
<div class="role-head"><span class="abbr">{E(r["abbr"])}</span><h3>{E(r["name"])}</h3><p class="hu">{E(r["hu"])}</p>{ph}</div></div>
<p class="desc">{E(r["desc"])}</p>
<h5>Kulcstulajdonságok</h5><ul class="attrs">{chips(r["attrs"])}</ul>
{combo}
</article>'''

GMAP = {g[0]: g for g in GROUPS}

def group_page(gkey):
    g = GMAP[gkey]
    ip = [r for r in R if r['group'] == gkey and r['phase'] == 'IP']
    oop = [r for r in R if r['group'] == gkey and r['phase'] == 'OOP']
    return (f'<div class="pos-head"><span class="gpos">{E(g[2])}</span><h2>{E(g[1])}</h2></div>'
            f'<p class="intro">{E(g[3])}</p>'
            f'<div class="group-label ip">LABDÁVAL · IN POSSESSION <span>{len(ip)}</span></div>' + ''.join(role_card(r) for r in ip) +
            f'<div class="group-label oop">LABDA NÉLKÜL · OUT OF POSSESSION <span>{len(oop)}</span></div>' + ''.join(role_card(r) for r in oop))

# szerepkör-azonosítók és helyük (fül, lap) a gyorslista ugrásaihoz
TABDEF = [
    ('def', 'Védelem', [('gk', 'Kapus'), ('cb', 'Középhátvéd'), ('fb', 'Szélső hátvéd')]),
    ('mid', 'Középpálya', [('dm', 'Védekező'), ('cm', 'Középső'), ('wm', 'Szélső')]),
    ('att', 'Támadás', [('am', 'Tízes'), ('w', 'Szélső'), ('st', 'Csatár')]),
]
uid = 0
WHERE = {}
for tkey, tname, pages in TABDEF:
    for pi, (gkey, _) in enumerate(pages):
        for r in [x for x in R if x['group'] == gkey and x['phase'] == 'IP'] + [x for x in R if x['group'] == gkey and x['phase'] == 'OOP']:
            uid += 1
            r['uid'] = uid
            WHERE[uid] = (tkey, pi)

# ---------- Taktika › Alapok ----------
LEGEND = f'''<svg viewBox="0 0 68 40" class="legend-svg" role="img" aria-label="Jelmagyarázat: sárga folytonos nyíl a labdás mozgás, piros szaggatott nyíl a labda nélküli mozgás">{defs('lg')}
<rect x="0" y="0" width="68" height="40" class="grass"/>
<line x1="6" y1="10" x2="28" y2="10" class="aip" stroke-width="1.1" marker-end="url(#ailg)"/>
<line x1="6" y1="22" x2="28" y2="22" class="aoop" stroke-width="1.1" marker-end="url(#aolg)"/>
{dot(10, 33, 'CM')}
<text x="33" y="11.2" class="lgt">labdával</text><text x="33" y="23.2" class="lgt">labda nélkül</text><text x="16" y="34.2" class="lgt">kiinduló hely</text>
</svg>'''

BASICS = f'''<div class="group pad text">
<p>Az FM26 megszüntette a duty-kat (Védekező, Támogató, Támadó). Helyettük minden mezőnyjátékos <b>két szerepet</b> kap: egyet arra az időre, amikor a csapatodnál van a labda (<b>In Possession, IP</b>), és egyet arra, amikor az ellenfélnél (<b>Out of Possession, OOP</b>). A labdás és a labda nélküli formációt is külön állíthatod, így például labdával 3-2-5-ben támadhatsz, labda nélkül pedig 4-4-2-ben védekezhetsz. Az FM27 erre a rendszerre épít tovább.</p>
<p>Labdával a szerep azt dönti el, <i>hová mozog és mit csinál a labdával</i> a játékos: szélességet ad, befelé húzódik, visszalép, mélységbe fut, irányít. Labda nélkül azt, <i>milyen magasan és milyen agresszívan védekezik</i>: letámad (Pressing), kilép (Stopping), tartja a vonalat (Covering, Screening), visszazár (Tracking, Dropping, Holding), kisegít a szélen (Wide Covering), vagy fent marad kontrára (Outlet).</p>
<p>A hivatalos SI-leírás szerint az FM26-ban megszűnt a <b>Mezzala, az Enganche és a Trequartista</b>. Ezek viselkedését ma a Channel Midfielder, az Advanced Playmaker és a Free Role, illetve az IP és OOP szerepek párosítása adja vissza. A régi Carrilero védekező fele a Wide Covering CM, a Segundo Volante labdás fele a Box-to-Box Playmaker lett.</p>
</div>
<div class="group-label">JELMAGYARÁZAT</div>
<div class="group pad text">{LEGEND}
<p>A pályarajzokon a te csapatod mindig <b>felfelé</b> támad. Az oldalsó szerepeket a jobb oldalon ábrázoljuk; a bal oldal ennek tükörképe. A sárga folt a játékos fő működési területe labdával, a piros labda nélkül.</p></div>
<div class="group-label">DUPLA RÖVIDÍTÉSEK</div>
<div class="group pad text">
<p><span class="abbr sm">WCM</span> labdával a Wide Central Midfielder, labda nélkül a Wide Covering Central Midfielder.</p>
<p><span class="abbr sm">PWB</span> labdával a Playmaking Wing-Back, labda nélkül a Pressing Wing-Back.</p>
<p><span class="abbr sm">CFD</span> a középcsatár (Centre Forward), mert a CF a régi Complete Forwardé.</p>
<p class="note">A szerepneveket a magyar nyelvi fájlhoz igazodva angolul hagytuk, ahogy a játékban is látod.</p></div>
<div class="group-label">AZ EGYENSÚLY HÁROM SZABÁLYA</div>
<div class="rules">
<div class="group rule"><b>1</b><p><strong>Minden sávba egy ember.</strong> A támadásban öt sávod van (két szél, két félterület, közép). Ha egy sávba ketten futnak (pl. Channel Midfielder és Inside Forward ugyanazon az oldalon), egy másik üresen marad.</p></div>
<div class="group rule"><b>2</b><p><strong>Tartó, alkotó, futó.</strong> A középpályán legyen egy, aki a helyén marad, egy, aki a labdát kéri és szervez, és egy, aki mélységbe fut. Két irányító futó nélkül lassú, két futó tartó nélkül sebezhető.</p></div>
<div class="group rule"><b>3</b><p><strong>Minden előretörő mögé biztosítás.</strong> Ha a szárnyvédő felmegy, a széles középhátvéd vagy egy kisegítő középpályás zárja mögötte a teret. Ha egy szélső fent marad (Outlet), mögötte valakinek ki kell segítenie.</p></div>
</div>'''

PAIRS = '<p class="intro">A szerepek ereje abból jön, hogyan egészítik ki egymást. Ezeket a párosokat a könyvek, a játék saját leírásai és a közösségi útmutatók egybehangzóan ajánlják.</p>' + ''.join(
    f'<article class="group role pair"><div class="role-top"><div class="mini">{combo_svg(pl, "c"+str(i), t)}</div><div class="role-head"><h3>{E(t)}</h3></div></div><p class="desc">{E(d)}</p></article>'
    for i, (t, d, pl) in enumerate(COMBOS))

def quick_list():
    out = ['<p class="intro">Minden szerepkör egy mondatban. Koppints egy sorra, és a részletes leíráshoz ugrasz.</p>']
    for gkey, gname, gpos, _ in GROUPS:
        out.append(f'<div class="group-label">{E(gname.upper())} <span>{E(gpos)}</span></div><div class="group">')
        for r in [x for x in R if x['group'] == gkey]:
            first = r['desc'].split('. ')[0].rstrip('.') + '.'
            ph = '<i class="ph ph-ip">IP</i>' if r['phase'] == 'IP' else '<i class="ph ph-oop">OOP</i>'
            tk, pi = WHERE[r['uid']]
            out.append(f'<button type="button" class="ql" data-jump="{r["uid"]}" data-tab="{tk}" data-page="{pi}"><span class="abbr sm">{E(r["abbr"])}</span>'
                       f'<span class="ql-t"><b>{E(r["name"])}</b><small>{E(first)}</small></span>{ph}</button>')
        out.append('</div>')
    return ''.join(out)

SOURCES = '''<div class="group-label">A JÁTÉKBÓL ÉS A FUTBALL MAPPÁBÓL</div>
<div class="group pad text"><ul class="src">
<li>FM27 nyelvi fájl (example.ltf és magyar_fm27.ltf): szerepkörnevek, rövidítések, a szerepek hivatalos leírásai</li>
<li>Mastering Football Manager (magyar A4-es változat): 8–13. fejezet a szerepekről, 14. fejezet a felépítésről</li>
<li>The Art of Football Management (magyar változat): öt sáv, egyensúly, szerepek és egyéni utasítások</li>
<li>Guide to FM, 1. és 2. kiadás (magyar fordítás): felállások, mentalitások</li>
<li>A fordított piramis – A futballtaktika története: regista, enganche, carrilero, libero, Hidegkuti szerepe</li>
<li>Beregi István: A magyar futball filozófiája – helycserés, sokmozgásos játék, 4-2-3-1 és 4-3-3</li>
</ul></div>
<div class="group-label">WEBES FORRÁSOK</div>
<div class="group pad text"><ul class="src">
<li><a href="https://www.footballmanager.com/fm26/features/possession-out-possession-fm26s-new-tactical-evolution">SI: In Possession, Out of Possession – FM26’s New Tactical Evolution</a></li>
<li><a href="https://www.fmscout.com/a-football-manager-2026-player-roles.html">FM Scout: FM26 Player Roles – What’s New, Changed &amp; Removed</a></li>
<li><a href="https://www.passion4fm.com/?p=20957">Passion4FM: The Channel Midfielder</a></li>
<li><a href="https://www.passion4fm.com/football-manager-26-overpowered-player-roles/">Passion4FM: FM26 legerősebb szerepek</a></li>
<li><a href="https://www.fmscout.com/c-fm27-tactics.html">FM Scout: FM27 taktikák (közösségi, saját bevallású eredmények)</a></li>
<li><a href="https://footballmanager27.wiki/tactics/best-tactics/">Football Manager 27 Wiki: Best Tactics</a></li>
<li><a href="https://everythingedinburgh.com/games/gaming/fm27-best-tactics/">FM27 Best Tactics: Top Formations</a></li>
</ul></div>
<div class="group-label">NÉVJEGY</div>
<div class="group pad text"><p>FM27 Pozíciókalauz ''' + VERSION + ''' · Készítette: Szabó Ádám</p>
<p class="note">Összeállítva 2026. november 6-án. A kulcstulajdonságok javaslatok; a játékban a szerepkör kiválasztásakor kiemelt tulajdonságok a mérvadók. A szerepkörök és a leírások az FM27 nyelvi fájlból származnak.</p></div>'''

ABOUT = '''<div class="group-label">NÉVJEGY</div>
<div class="group pad text"><p>FM27 Pozíciókalauz ''' + VERSION + ''' · Készítette: Szabó Ádám</p>
<p class="note">A szerepkörök és a leírások az FM27 nyelvi fájlból, a Futball mappa könyveiből és a Sports Interactive, az FM Scout és a Passion4FM oldalairól származnak. A kulcstulajdonságok javaslatok; a játékban a szerepkör kiválasztásakor kiemelt tulajdonságok a mérvadók.</p></div>'''

def tactic_page(t, key):
    roles = ''.join(f'<div class="tr-row"><div class="tr-pos">{E(a)}</div><div class="tr-roles"><span><i class="ph ph-ip">IP</i>{E(b)}</span><span><i class="ph ph-oop">OOP</i>{E(c)}</span></div><p>{E(d)}</p></div>' for a, b, c, d in t['roles'])
    steps = ''.join(f'<li>{E(x)}</li>' for x in t['steps'])
    instr = ''.join(f'<div class="kv"><span class="k">{E(a)}</span><span class="v">{E(b)}</span></div>' for a, b in t['instr'])
    return f'''<h2 class="t-title first">{E(t["title"])}</h2>
<div class="seg2" data-fig="{key}" role="tablist" aria-label="Alakzat"><span class="seg2-thumb"></span>
<button type="button" role="tab" data-show="ip" aria-selected="true">Labdával</button><button type="button" role="tab" data-show="oop" aria-selected="false">Labda nélkül</button></div>
<div class="group tfig" id="fig-{key}"><div class="tf tf-ip">{tactic_svg(t, 'ip', key+'i')}</div><div class="tf tf-oop" hidden>{tactic_svg(t, 'oop', key+'o')}</div>
<p class="cap">Halvány kör: alapfelállás; színes kör: hová mozdul a játékos.</p></div>
<div class="group-label">SZEREPKÖRÖK POSZTONKÉNT</div><div class="group">{roles}</div>
<div class="group-label">MOZGÁSOK LÉPÉSRŐL LÉPÉSRE</div><div class="group pad text"><ol class="steps">{steps}</ol></div>
<div class="group-label">CSAPATUTASÍTÁSOK</div><div class="group">{instr}</div>
<div class="group-label">MIÉRT JÓ?</div><div class="group pad text why"><p>{E(t["why"])}</p></div>'''

FM27_NOTE = '<p class="intro">Az FM27 november 10-i teljes megjelenéséig még nincs független, ellenőrzött teszt arról, melyik taktika a legerősebb. A közösségi taktikák (FM Scout, saját bevallású eredmények) a 4-3-3-at és a 4-2-3-1-et emelik ki. Ez a két felállás ezekre, a könyvek elveire és a szerepek játékon belüli leírására épül. Kezdd velük, és a saját keretedhez igazítsd őket. A csapatutasítások neve a játékban kissé eltérhet.</p>'

# ---------- fülek ----------
# alsó sáv piktogramjai (24 × 24): kapu hálóval, felülnézeti pálya, lövésben lévő labda,
# felállás a pályán, taktikai tábla X-szel, O-val és nyíllal
ICONS = {
    'def': '<path d="M12 2.6l7.9 2.9v6.1c0 4.7-3.3 8.4-7.9 10.3-4.6-1.9-7.9-5.6-7.9-10.3V5.5z"/><path class="thin" d="M12 2.6v19.3M4.1 10.4h15.8"/>',
    'mid': '<rect x="2.5" y="5" width="19" height="14" rx="1.6"/><path d="M12 5v14"/><circle cx="12" cy="12" r="2.9"/><path class="thin" d="M2.5 9.3h2.6v5.4H2.5M21.5 9.3h-2.6v5.4h2.6"/>',
    'att': '<defs><mask id="mAtt"><rect width="24" height="24" fill="#fff"/><circle cx="15.4" cy="10.6" r="5" fill="#000"/></mask></defs><path d="M2 20V5.5h20V20"/><path class="thin" mask="url(#mAtt)" d="M2 12.8h20M8.6 5.5V20M15.4 5.5V20"/><circle cx="15.4" cy="10.6" r="3.9"/><path class="thin" d="M15.4 9.1l1.43 1.04-.55 1.68h-1.76l-.55-1.68z"/>',
    'form': '<rect x="4.5" y="2.5" width="15" height="19" rx="1.6"/><path class="thin" d="M4.5 12h15"/><circle class="f" cx="12" cy="18.6" r="1.25"/><circle class="f" cx="8.4" cy="15.2" r="1.25"/><circle class="f" cx="15.6" cy="15.2" r="1.25"/><circle class="f" cx="12" cy="9.6" r="1.25"/><circle class="f" cx="8.2" cy="6.2" r="1.25"/><circle class="f" cx="15.8" cy="6.2" r="1.25"/>',
    'tac': '<circle cx="12" cy="12" r="9.3"/><path d="M12 10.8v6"/><circle class="f" cx="12" cy="7.4" r="1.3"/>',
}

def tab_section(key, title, pages):
    n = len(pages)
    seg = ''.join(f'<button type="button" role="tab" data-page="{i}">{E(lbl)}</button>' for i, (lbl, _) in enumerate(pages))
    pg = ''.join(f'<div class="pg scroll" role="tabpanel" aria-label="{E(lbl)}">{body}</div>' for lbl, body in pages)
    return f'''<section class="tab" id="tab-{key}" data-tab="{key}" hidden>
<div class="tab-head"><h1 class="page-title">{E(title)}</h1>
<div class="seg" role="tablist" aria-label="{E(title)} lapjai" style="--n:{n}"><span class="seg-thumb"></span>{seg}</div></div>
<div class="pager"><div class="track" style="--n:{n}">{pg}</div></div>
</section>'''

sections = []
for tkey, tname, pages in TABDEF:
    sections.append(tab_section(tkey, tname, [(lbl, group_page(g)) for g, lbl in pages]))
sections.append(tab_section('form', 'Felállás', [('Támadó', tactic_page(ATT, 'att')), ('Védekező', tactic_page(DEF, 'def'))]))
sections.append(tab_section('tac', 'Infó', [('Alapok', BASICS + ABOUT), ('Párosítások', PAIRS), ('Gyorslista', quick_list())]))

TABBAR = [('def', 'Védelem'), ('mid', 'Középpálya'), ('att', 'Támadás'), ('form', 'Felállás'), ('tac', 'Infó')]
bar = ''.join(f'<button type="button" data-go="{k}" aria-label="{E(n)}"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[k]}</svg><span class="lbl">{E(n)}</span></button>' for k, n in TABBAR)

SPLASH = [(440, 956, 3, '1320x2868'), (402, 874, 3, '1206x2622'), (420, 912, 3, '1260x2736'), (430, 932, 3, '1290x2796'),
          (393, 852, 3, '1179x2556'), (390, 844, 3, '1170x2532'), (428, 926, 3, '1284x2778'), (375, 812, 3, '1125x2436'),
          (414, 896, 3, '1242x2688'), (414, 896, 2, '828x1792'), (375, 667, 2, '750x1334')]
splash_links = '\n'.join(f'<link rel="apple-touch-startup-image" media="(device-width: {w}px) and (device-height: {h}px) and (-webkit-device-pixel-ratio: {r}) and (orientation: portrait)" href="icons/splash/splash-{n}.png">' for w, h, r, n in SPLASH)

doc = f'''<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>FM27 Pozíciókalauz</title>
<meta name="description" content="Az FM26 és FM27 összes szerepköre pályarajzokkal, bevált párosítások és FM27 felállások.">
<meta name="theme-color" content="#eef2ee" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0d1310" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Pozíciókalauz">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-32.png" type="image/png" sizes="32x32">
<link rel="icon" href="icons/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="icons/icon-180.png">
{splash_links}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@600;700&amp;display=swap">
<link rel="stylesheet" href="css/app.css">
</head>
<body>
<div class="splash" id="splash" aria-hidden="true"><img src="icons/icon-512.png" alt="" width="168" height="168"></div>
<div class="app" id="app">
{''.join(sections)}
<div class="statusbar-scrim" aria-hidden="true"></div>
<nav class="tabbar" id="tabbar" aria-label="Fő navigáció"><span class="lens" id="lens"></span>{bar}</nav>
</div>
<script src="js/app.js"></script>
</body>
</html>
'''
with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(doc)
print('index.html', len(doc), 'szerepkör', len(R))
