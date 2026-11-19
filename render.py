#!/usr/bin/env python3
"""Render the 19 Nov 2026 world-news image (1024x1024 PNG) with Pillow locally.

This is a LOCAL build tool only. It is NOT run by the make.fun grader.
The submission program is main.py (Python stdlib only), which copies
entry.png to /output/entry.png, exactly as the starter entry does.

Headlines are the events reported on Thursday 19 November 2026,
checked against BBC / NYT / Sky News / AP reporting that day
(see README.md for the source list).
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 244, 232)
INK = (20, 20, 20)
NAVY = (22, 40, 63)
RED = (180, 35, 24)
TEAL = (14, 107, 107)
BLUE = (29, 78, 137)
GOLD = (201, 138, 27)
GREY = (90, 90, 90)
WHITE = (255, 255, 255)
CARD = (255, 255, 255)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
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

def draw_text_block(draw, x, y, text, fnt, color, max_w, leading):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y

def panel(draw, x, y, w, h, tag, tag_color, headline, summary):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=CARD, outline=(210, 200, 180), width=2)
    draw.rectangle([x, y, x + w, y + 6], fill=tag_color)
    # tag
    draw.text((x + 16, y + 16), tag, font=font(SANS_B, 17), fill=tag_color)
    # headline, 2-3 lines
    yy = draw_text_block(draw, x + 16, y + 44, headline, font(SERIF_B, 25), INK, w - 32, 30)
    # summary
    draw_text_block(draw, x + 16, yy + 6, summary, font(SANS, 18), (60, 60, 60), w - 32, 23)

def skyline(draw, x0, y0, x1, y1):
    # sunset bands
    bands = [(255, 170, 80), (255, 140, 90), (230, 110, 110), (120, 70, 110)]
    bh = (y1 - y0) // len(bands)
    for i, c in enumerate(bands):
        draw.rectangle([x0, y0 + i * bh, x1, y0 + (i + 1) * bh], fill=c)
    # sun
    cx, cy, r = (x0 + x1) // 2, y0 + 62, 34
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 230, 150))
    # buildings
    import random
    rnd = random.Random(19)
    bx = x0 + 8
    while bx < x1 - 30:
        bw = rnd.randint(28, 52)
        bhgt = rnd.randint(60, 150)
        by = y1 - 42 - bhgt
        draw.rectangle([bx, by, bx + bw, y1 - 42], fill=(30, 30, 50))
        for wy in range(by + 10, y1 - 52, 18):
            for wx in range(bx + 6, bx + bw - 6, 14):
                if rnd.random() < 0.5:
                    draw.rectangle([wx, wy, wx + 6, wy + 8], fill=(255, 220, 120))
        bx += bw + 6
    # road
    draw.rectangle([x0, y1 - 42, x1, y1], fill=(40, 40, 40))
    draw.rectangle([x0, y1 - 24, x1, y1 - 20], fill=(255, 255, 255))

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # Masthead
    d.rectangle([0, 0, W, 132], fill=NAVY)
    d.text((24, 14), "WORLD NEWS", font=font(SERIF_B, 72), fill=WHITE)
    d.text((24, 96), "THURSDAY  19  NOVEMBER  2026", font=font(SANS_B, 22), fill=(255, 210, 120))
    d.text((700, 96), "ONE DAY  •  ONE IMAGE", font=font(SANS_B, 20), fill=(200, 210, 220))
    d.rectangle([0, 132, W, 138], fill=GOLD)
    # Lead story
    lx, ly, lw, lh = 24, 152, 976, 252
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=12, fill=CARD, outline=(210, 200, 180), width=2)
    d.rectangle([lx, ly, lx + lw, ly + 6], fill=RED)
    d.text((lx + 20, ly + 18), "LEAD STORY  —  CULTURE & GAMES", font=font(SANS_B, 18), fill=RED)
    draw_text_block(d, lx + 20, ly + 48, "GTA VI ROLLS OUT WORLDWIDE", font(SERIF_B, 42), INK, 560, 48)
    draw_text_block(d, lx + 20, ly + 152, "Gamers enter Vice City as Grand Theft Auto VI begins its global rollout.", font(SANS, 23), (60, 60, 60), 560, 30)
    d.text((lx + 20, ly + 214), "The year's most awaited game launch.", font=font(SANS_B, 19), fill=NAVY)
    skyline(d, lx + 600, ly + 14, lx + lw - 14, ly + lh - 14)
    # Grid 2 x 3
    panels = [
        ("GEOPOLITICS", NAVY, "TRUMP, XI AND PUTIN TO MEET IN SHENZHEN",
         "Trilateral talks planned at the APEC summit in China."),
        ("MIDDLE EAST", RED, "ISRAELI TROOPS LAUNCH GAZA GROUND OPERATION",
         "Troops advance beyond the ceasefire line; aid access urged."),
        ("EUROPE", BLUE, "CRIMEAN BRIDGE ATTACKED AGAIN",
         "Traffic halted after a new strike. EU proposes a \u20ac45bn Ukraine loan."),
        ("TECH & ECONOMY", TEAL, "ANTHROPIC IN RECORD $81.3BN IPO",
         "AI firm makes the biggest stock-market debut ever."),
        ("SCIENCE", (31, 107, 58), "VOYAGER 1 REACHES ONE LIGHT-DAY",
         "NASA probe, nearly 50 years out, hits a new milestone."),
        ("CULTURE", (91, 58, 142), "VAN GOGH SELLS FOR RECORD $190.4M",
         "Painting fetches a record price after a row over its Nazi history."),
    ]
    px, py = 24, 420
    pw, ph, gap = 480, 176, 16
    for i, (tag, col, head, summ) in enumerate(panels):
        x = px + (i % 2) * (pw + gap)
        y = py + (i // 2) * (ph + gap)
        panel(d, x, y, pw, ph, tag, col, head, summ)
    # Also today strip
    y = 964
    d.text((24, y), "ALSO TODAY:  Cyclone Akvan nears India  •  Myanmar genocide verdict  •  France protests",
           font=font(SANS_B, 15), fill=GREY)
    img.save("entry.png", "PNG", optimize=True)
    print("saved entry.png", img.size)

if __name__ == "__main__":
    main()
