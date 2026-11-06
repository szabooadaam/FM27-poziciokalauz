# -*- coding: utf-8 -*-
# App-ikon és iOS indítóképek: csíkos gyep, pályavonalak, „FM27” felirat, sárga labdás és piros labda nélküli nyíl.
# Futtatás a forras mappából:  python make_icons.py   (Pillow és a Windows Bahnschrift betűtípusa kell hozzá)
import os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), 'icons')
FONT = r'C:\Windows\Fonts\bahnschrift.ttf'
GRASS, GRASS2, WHITE, IP, OOP = (47, 122, 77), (42, 112, 71), (255, 255, 255), (242, 182, 50), (255, 109, 97)

def font(size, style='Bold Condensed'):
    f = ImageFont.truetype(FONT, size)
    try:
        f.set_variation_by_name(style)
    except Exception:
        pass
    return f

def arrow(d, p1, p2, color, w, dashed=False):
    import math
    x1, y1 = p1; x2, y2 = p2
    L = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / L, (y2 - y1) / L
    head = w * 3.2
    ex, ey = x2 - ux * head * 0.8, y2 - uy * head * 0.8
    if dashed:
        seg, gap, t = w * 2.6, w * 1.8, 0.0
        tot = math.hypot(ex - x1, ey - y1)
        while t < tot:
            a = t; b = min(t + seg, tot)
            d.line([(x1 + ux * a, y1 + uy * a), (x1 + ux * b, y1 + uy * b)], fill=color, width=w)
            t += seg + gap
    else:
        d.line([(x1, y1), (ex, ey)], fill=color, width=w)
    px, py = -uy, ux
    bx, by = x2 - ux * head, y2 - uy * head
    d.polygon([(x2, y2), (bx + px * head * 0.62, by + py * head * 0.62), (bx - px * head * 0.62, by - py * head * 0.62)], fill=color)

def icon(S=1024):
    im = Image.new('RGB', (S, S), GRASS)
    d = ImageDraw.Draw(im)
    band = S / 7
    for i in range(0, 7, 2):
        d.rectangle([0, i * band, S, (i + 1) * band], fill=GRASS2)
    lw = max(2, S // 110)
    line = (255, 255, 255, 150)
    ov = Image.new('RGBA', (S, S), (0, 0, 0, 0)); o = ImageDraw.Draw(ov)
    o.line([(0, S * 0.58), (S, S * 0.58)], fill=line, width=lw)
    r = S * 0.2
    o.ellipse([S / 2 - r, S * 0.58 - r, S / 2 + r, S * 0.58 + r], outline=line, width=lw)
    o.rectangle([S * 0.22, -lw, S * 0.78, S * 0.16], outline=line, width=lw)
    im.paste(ov, (0, 0), ov)
    d = ImageDraw.Draw(im)
    # nyilak: sárga a labdás, piros szaggatott a labda nélküli mozgás
    arrow(d, (S * 0.2, S * 0.9), (S * 0.36, S * 0.66), IP, max(3, S // 40))
    arrow(d, (S * 0.82, S * 0.66), (S * 0.68, S * 0.9), OOP, max(3, S // 40), dashed=True)
    f = font(int(S * 0.36))
    txt = 'FM27'
    bb = d.textbbox((0, 0), txt, font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    d.text(((S - w) / 2 - bb[0], S * 0.43 - h / 2 - bb[1]), txt, font=f, fill=WHITE)
    return im

def main():
    os.makedirs(os.path.join(OUT, 'splash'), exist_ok=True)
    big = icon(1024)
    for s in (32, 180, 192, 512):
        big.resize((s, s), Image.LANCZOS).save(os.path.join(OUT, f'icon-{s}.png'))
    # indítóképek: a logó 168 pont méretben, középen (mint a KISPAD-ben), lekerekítve
    sizes = [(1320, 2868, 3), (1206, 2622, 3), (1260, 2736, 3), (1290, 2796, 3), (1179, 2556, 3), (1170, 2532, 3),
             (1284, 2778, 3), (1125, 2436, 3), (1242, 2688, 3), (828, 1792, 2), (750, 1334, 2)]
    for w, h, sc in sizes:
        im = Image.new('RGB', (w, h), (31, 82, 52))
        L = 168 * sc
        logo = big.resize((L, L), Image.LANCZOS)
        mask = Image.new('L', (L, L), 0)
        ImageDraw.Draw(mask).rounded_rectangle([0, 0, L - 1, L - 1], radius=38 * sc, fill=255)
        im.paste(logo, ((w - L) // 2, (h - L) // 2), mask)
        im.save(os.path.join(OUT, 'splash', f'splash-{w}x{h}.png'), optimize=True)
    print('ikonok és indítóképek kész')

if __name__ == '__main__':
    main()
