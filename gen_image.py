#!/usr/bin/env python3
"""Generate the 21 November 2026 world-news image (1024x1024 PNG).

Draws a newspaper front page with PIL: masthead with the date, a lead
story (Russia's massive strike on Ukraine, missiles landing in Poland)
with a night-skyline illustration, six more stories in a grid, and an
"also in the news" footer. Deterministic: no randomness, no network,
fixed fonts and colours, so re-running writes identical bytes.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (248, 244, 233)      # newsprint
INK = (20, 20, 20)
RED = (163, 22, 33)
NAVY = (18, 38, 66)
BLUE = (29, 53, 87)
GOLD = (180, 140, 30)
GREY = (90, 90, 84)
LIGHT = (238, 232, 214)

FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SERIF = FD + "DejaVuSerif.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"
SANS = FD + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, color=INK, width=2):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


# ---------------------------------------------------------------- lead art
def lead_illustration(draw, x0, y0, x1, y1):
    """Night sky over a Kyiv-style skyline: missile arcs, explosions."""
    draw.rectangle([x0, y0, x1, y1], fill=NAVY)
    # stars (fixed positions)
    stars = [(18, 22), (70, 60), (130, 18), (180, 44), (235, 14), (300, 52),
             (350, 20), (410, 64), (455, 30), (95, 92), (260, 84), (390, 100),
             (40, 120), (330, 130), (480, 110)]
    for sx, sy in stars:
        draw.ellipse([x0 + sx - 2, y0 + sy - 2, x0 + sx + 2, y0 + sy + 2],
                     fill=(240, 235, 200))
    # moon
    draw.ellipse([x0 + 448, y0 + 16, x0 + 492, y0 + 60], fill=(235, 228, 190))
    draw.ellipse([x0 + 458, y0 + 24, x0 + 468, y0 + 34], fill=(215, 206, 165))
    # missile arcs: top-half arches, fully inside the illustration
    draw.arc([x0 + 10, y0 + 30, x0 + 330, y0 + 250], 180, 360,
             fill=(255, 90, 60), width=5)
    draw.arc([x0 + 120, y0 + 10, x0 + 480, y0 + 220], 180, 360,
             fill=(255, 140, 80), width=5)
    draw.arc([x0 + 200, y0 + 60, x0 + 520, y0 + 260], 180, 360,
             fill=(255, 90, 60), width=4)
    for hx, hy in [(330, 140), (480, 115), (520, 160)]:
        draw.ellipse([x0 + hx - 7, y0 + hy - 7, x0 + hx + 7, y0 + hy + 7],
                     fill=(255, 220, 120))
    # explosion bursts
    def burst(cx, cy, r, col):
        pts = []
        import math
        for i in range(16):
            ang = math.pi * i / 8
            rr = r if i % 2 == 0 else r * 0.45
            pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
        draw.polygon(pts, fill=col)
    burst(x0 + 120, y0 + 185, 34, (255, 170, 40))
    burst(x0 + 120, y0 + 185, 18, (255, 230, 130))
    burst(x0 + 380, y0 + 205, 26, (255, 170, 40))
    burst(x0 + 380, y0 + 205, 13, (255, 230, 130))
    # smoke
    for sx, sy, sr in [(150, 150, 26), (180, 138, 20), (400, 175, 22)]:
        draw.ellipse([x0 + sx - sr, y0 + sy - sr // 2, x0 + sx + sr,
                      y0 + sy + sr // 2], fill=(120, 120, 125))
    # skyline silhouette
    base = y1
    buildings = [(0, 90, 70, 210), (75, 60, 60, 240), (140, 100, 80, 190),
                 (225, 55, 55, 245), (285, 95, 75, 195), (365, 70, 60, 230),
                 (430, 105, 70, 185)]
    for bx, bh, bw, _ in buildings:
        draw.rectangle([x0 + bx, base - bh, x0 + bx + bw, base], fill=(8, 10, 16))
        # lit windows
        for wy in range(base - bh + 12, base - 10, 22):
            for wx in range(x0 + bx + 10, x0 + bx + bw - 8, 18):
                if (wx * 7 + wy * 13) % 5 < 2:
                    draw.rectangle([wx, wy, wx + 6, wy + 8],
                                   fill=(255, 205, 90))
    # caption bar
    draw.rectangle([x0, y1 - 30, x1, y1], fill=(0, 0, 0))
    draw.text((x0 + 12, y1 - 26), "KYIV UNDER FIRE — OVERNIGHT, 20–21 NOV",
              font=font(SANS_B, 15), fill=(255, 255, 255))


# ------------------------------------------------------------------- icons
def icon_chart(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], outline=RED, width=2)
    pts = [(x + 8, y + s - 16), (x + 22, y + s - 30), (x + 34, y + s - 24),
           (x + 48, y + s - 44), (x + 62, y + s - 52)]
    draw.line(pts, fill=RED, width=4)
    draw.polygon([(x + 62, y + s - 52), (x + 54, y + s - 50),
                  (x + 62, y + s - 40)], fill=RED)


def icon_scales(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], outline=BLUE, width=2)
    draw.line([(x + s // 2, y + 10), (x + s // 2, y + s - 12)], fill=BLUE, width=3)
    draw.line([(x + 12, y + 16), (x + s - 12, y + 16)], fill=BLUE, width=3)
    for cx in (x + 16, x + s - 16):
        draw.line([(cx, y + 16), (cx - 9, y + 34)], fill=BLUE, width=2)
        draw.line([(cx, y + 16), (cx + 9, y + 34)], fill=BLUE, width=2)
        draw.arc([cx - 10, y + 30, cx + 10, y + 48], 0, 180, fill=BLUE, width=2)
    draw.line([(x + 18, y + s - 12), (x + s - 18, y + s - 12)], fill=BLUE, width=3)


def icon_globe(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], outline=(46, 110, 70), width=2)
    cx, cy, r = x + s // 2, y + s // 2, 24
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(46, 110, 70), width=3)
    draw.ellipse([cx - 10, cy - r, cx + 10, cy + r], outline=(46, 110, 70), width=2)
    draw.line([(cx - r, cy), (cx + r, cy)], fill=(46, 110, 70), width=2)
    draw.arc([cx - r, cy - 14, cx + r, cy + 14], 0, 360,
             fill=(46, 110, 70), width=2)


def icon_gta(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], fill=(20, 20, 20))
    draw.text((x + 8, y + 8), "VI", font=font(SERIF_B, 44), fill=(255, 200, 60))
    draw.line([(x + 8, y + s - 12), (x + s - 8, y + s - 12)], fill=(255, 200, 60),
              width=3)


def icon_pill(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], outline=(150, 40, 90), width=2)
    draw.ellipse([x + 10, y + 26, x + 34, y + 50], fill=(200, 60, 90))
    draw.ellipse([x + 34, y + 26, x + 58, y + 50], fill=(240, 240, 240),
                 outline=(200, 60, 90), width=2)
    draw.line([(x + 34, y + 26), (x + 34, y + 50)], fill=(200, 60, 90), width=2)


def icon_podium(draw, x, y, s):
    draw.rectangle([x, y, x + s, y + s], outline=RED, width=2)
    draw.rectangle([x + 14, y + 36, x + s - 14, y + s - 10], fill=NAVY)
    draw.line([(x + s // 2, y + 12), (x + s // 2, y + 36)], fill=INK, width=3)
    draw.ellipse([x + s // 2 - 6, y + 8, x + s // 2 + 6, y + 20], fill=INK)
    draw.text((x + 20, y + 42), "$", font=font(SANS_B, 18), fill=(255, 255, 255))


ICONS = {"chart": icon_chart, "scales": icon_scales, "globe": icon_globe,
         "gta": icon_gta, "pill": icon_pill, "podium": icon_podium}

STORIES = [
    ("MARKETS", RED, "chart",
     "S&P 500 falls into correction",
     "Nasdaq erases its 2026 gains as tech shares plunge."),
    ("JUSTICE", BLUE, "scales",
     "ICJ: Myanmar genocide ruling",
     "The Hague finds Myanmar guilty of genocide against the Rohingya."),
    ("CLIMATE", (46, 110, 70), "globe",
     "COP31 runs into overtime",
     "Nearly 200 nations in Antalya fail to agree on fossil fuels."),
    ("CULTURE", (20, 20, 20), "gta",
     "GTA VI: $3.8bn in one day",
     "Rockstar's launch sets an entertainment record."),
    ("HEALTH", (150, 40, 90), "pill",
     "Cancer pill breakthrough",
     "Trial pill clears tumours in 1 in 12 pancreatic patients."),
    ("POLITICS", RED, "podium",
     "Trump's AI-centre tax threat",
     "US firms building data centres abroad face a penalty."),
]


def card(draw, x0, y0, cw, ch, kicker, kcolor, icon, headline, body):
    draw.rectangle([x0, y0, x0 + cw, y0 + ch], fill=(255, 255, 255),
                   outline=(200, 192, 170), width=1)
    draw.rectangle([x0, y0, x0 + cw, y0 + 5], fill=kcolor)
    pad = 14
    y = y0 + 16
    draw.text((x0 + pad, y), kicker, font=font(SANS_B, 15), fill=kcolor)
    ICONS[icon](draw, x0 + cw - 78, y0 + 12, 64)
    y += 24
    hl = wrap(draw, headline, font(SERIF_B, 24), cw - 2 * pad - 72)
    y = draw_lines(draw, hl[:2], x0 + pad, y + 2, font(SERIF_B, 24), INK, 29)
    bl = wrap(draw, body, font(SANS, 17), cw - 2 * pad)
    draw_lines(draw, bl[:3], x0 + pad, y + 6, font(SANS, 17), (60, 60, 56), 22)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # outer border
    d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=3)
    d.rectangle([16, 16, W - 17, H - 17], outline=INK, width=1)

    # masthead (title auto-fits the page width)
    d.text((W // 2, 34), "THE WORLD IN ONE IMAGE",
           font=font(SANS_B, 20), fill=GREY, anchor="ma")
    tsize = 56
    while tsize > 36 and d.textlength("SATURDAY, 21 NOVEMBER 2026",
                                     font=font(SERIF_B, tsize)) > W - 56:
        tsize -= 2
    d.text((W // 2, 62), "SATURDAY, 21 NOVEMBER 2026",
           font=font(SERIF_B, tsize), fill=INK, anchor="ma")
    rule(d, 28, 128, W - 28, RED, 4)
    rule(d, 28, 134, W - 28, INK, 2)

    # lead panel
    ly0, ly1 = 146, 478
    lead_illustration(d, 28, ly0, 560, ly1)
    tx = 584
    d.text((tx, ly0 + 6), "WAR IN EUROPE  •  LEAD STORY",
           font=font(SANS_B, 17), fill=RED)
    hl = wrap(d, "Russia's massive strike on Ukraine — missiles land in Poland",
              font(SERIF_B, 32), W - 28 - tx)
    y = draw_lines(d, hl, tx, ly0 + 36, font(SERIF_B, 32), INK, 40)
    rule(d, tx, y + 10, W - 28, (200, 192, 170), 1)
    body = ("More than 400 drones and 110 missiles hit Ukraine overnight; "
            "at least 8 were killed in Kyiv. Two Russian missiles and a drone "
            "landed in Poland; PM Donald Tusk called it a deliberate provocation.")
    bl = wrap(d, body, font(SANS, 19), W - 28 - tx)
    draw_lines(d, bl, tx, y + 22, font(SANS, 19), (40, 40, 38), 24)

    # story grid: 3 x 2
    gx, gy = 28, 494
    cw, ch = 312, 196
    gap = 16
    for i, (kicker, kcolor, icon, headline, body) in enumerate(STORIES):
        cx = gx + (i % 3) * (cw + gap)
        cy = gy + (i // 3) * (ch + gap)
        card(d, cx, cy, cw, ch, kicker, kcolor, icon, headline, body)

    # footer ticker
    fy = 902
    rule(d, 28, fy, W - 28, INK, 2)
    d.text((28, fy + 10), "ALSO IN THE NEWS",
           font=font(SANS_B, 16), fill=RED)
    also = ("Gen Z protests sweep 25 European countries  •  UK and EU sign the "
            "biggest post-Brexit deal  •  FBI crime database hacked  •  "
            "Bitcoin slides toward $62,000")
    al = wrap(d, also, font(SANS, 18), W - 56)
    draw_lines(d, al, 28, fy + 34, font(SANS, 18), (50, 50, 48), 23)
    d.text((W // 2, H - 40), "Sources: wire reports, 21 November 2026  •  One day, one picture",
           font=font(SANS, 14), fill=GREY, anchor="ma")

    img.save("entry.png", format="PNG", optimize=True)


if __name__ == "__main__":
    main()
