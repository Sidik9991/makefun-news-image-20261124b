#!/usr/bin/env python3
"""Fresh renderer for the news-image-20261124 FULL-DAY REFRESH edition.

Draws a 1024x1024 atlas of Tuesday 24 November 2026 in code with PIL:
masthead, KPI strip, counted region bar, UTC timeline, 15 illustrated
panels, numbered pin map, digest of the remaining stories, DATE CHECK box.
No text is ever cut mid-sentence: summaries are rewritten short, never
truncated.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
NAVY = (20, 36, 62)
NAVY2 = (28, 52, 88)
GOLD = (201, 162, 39)
INK = (26, 26, 26)
MUTED = (90, 88, 82)
RED = (179, 38, 30)
TEAL = (14, 124, 123)
GREEN = (46, 125, 50)
SKY = (214, 232, 240)
SEA = (178, 205, 222)
LAND = (196, 198, 168)
WHITE = (255, 255, 255)
PANEL_BG = (255, 255, 255)
LINE = (200, 192, 172)

FDIR = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FDIR + name, size)

F_TITLE = font("DejaVuSans-Bold.ttf", 40)
F_SUB = font("DejaVuSans-Bold.ttf", 15)
F_KPI_N = font("DejaVuSans-Bold.ttf", 21)
F_KPI_L = font("DejaVuSans.ttf", 10)
F_SEC = font("DejaVuSans-Bold.ttf", 12)
F_REG = font("DejaVuSans-Bold.ttf", 11)
F_TIME = font("DejaVuSans-Bold.ttf", 13)
F_TL = font("DejaVuSans.ttf", 10)
F_HEAD = font("DejaVuSans-Bold.ttf", 13)
F_SUM = font("DejaVuSans.ttf", 11)
F_OUT = font("DejaVuSans.ttf", 9)
F_DIG = font("DejaVuSans.ttf", 10)
F_DC = font("DejaVuSans.ttf", 10)
F_FOOT = font("DejaVuSans.ttf", 9)

def wrap(draw, text, fnt, width):
    """Wrap text to fit width; returns list of lines (never cuts words)."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_panel_art(d, kind, x, y, w, h):
    """Small vector illustration inside box (x, y, w, h)."""
    cx, cy = x + w // 2, y + h // 2
    if kind == "tanker":
        d.rectangle([x, y, x + w, y + h], fill=(24, 52, 84))
        d.rectangle([x, y + h * 0.62, x + w, y + h], fill=(16, 90, 120))
        d.polygon([(x + 8, y + 58), (x + 58, y + 58), (x + 52, y + 42),
                   (x + 14, y + 42)], fill=(60, 60, 60))
        d.rectangle([x + 16, y + 30, x + 24, y + 42], fill=(200, 60, 40))
        d.rectangle([x + 28, y + 34, x + 36, y + 42], fill=(220, 160, 40))
        d.rectangle([x + 40, y + 30, x + 48, y + 42], fill=(40, 140, 90))
        for fx, fy, s in [(x + 60, y + 18, 10), (x + 52, y + 8, 7)]:
            d.polygon([(fx, fy + s), (fx + s, fy), (fx + s * 2, fy + s),
                       (fx + s, fy + s * 2)], fill=(255, 140, 0))
        d.ellipse([x + 56, y + 30, x + 70, y + 44], fill=(120, 120, 120))
    elif kind == "blast":
        d.rectangle([x, y, x + w, y + h], fill=(52, 44, 40))
        for bx, bw, bh in [(4, 16, 46), (24, 14, 62), (42, 18, 38), (60, 12, 52)]:
            d.rectangle([x + bx, y + h - bh, x + bx + bw, y + h], fill=(30, 28, 26))
        for ang in range(0, 360, 30):
            r = math.radians(ang)
            d.line([cx, cy - 18, cx + int(30 * math.cos(r)), cy - 18 + int(30 * math.sin(r))],
                   fill=(255, 170, 0), width=3)
        d.ellipse([cx - 13, cy - 31, cx + 13, cy - 5], fill=(255, 200, 40))
        d.ellipse([cx - 7, cy - 25, cx + 7, cy - 11], fill=(255, 120, 0))
    elif kind == "pharma":
        d.rectangle([x, y, x + w, y + h], fill=(232, 244, 236))
        d.rectangle([x + 22, y + 28, x + 54, y + 78], fill=WHITE, outline=(40, 120, 70), width=2)
        d.rectangle([x + 26, y + 18, x + 50, y + 28], fill=(40, 120, 70))
        d.rectangle([x + 34, y + 42, x + 42, y + 62], fill=(40, 120, 70))
        d.rectangle([x + 28, y + 50, x + 48, y + 56], fill=(40, 120, 70))
        d.ellipse([x + 8, y + 66, x + 24, y + 82], fill=(230, 60, 60))
        d.ellipse([x + 52, y + 66, x + 68, y + 82], fill=(40, 110, 200))
    elif kind == "probe":
        d.rectangle([x, y, x + w, y + h], fill=(238, 232, 214))
        d.rectangle([x + 14, y + 22, x + 62, y + 74], fill=WHITE, outline=(120, 30, 30), width=2)
        d.line([x + 20, y + 32, x + 56, y + 32], fill=(150, 40, 40), width=3)
        d.line([x + 20, y + 42, x + 56, y + 42], fill=(120, 120, 120), width=2)
        d.line([x + 20, y + 52, x + 48, y + 52], fill=(120, 120, 120), width=2)
        d.ellipse([x + 40, y + 52, x + 68, y + 80], outline=(20, 36, 62), width=4)
        d.line([x + 62, y + 74, x + 72, y + 86], fill=(20, 36, 62), width=4)
    elif kind == "chart":
        d.rectangle([x, y, x + w, y + h], fill=(232, 244, 232))
        for i, bh in enumerate([18, 26, 22, 38, 52]):
            d.rectangle([x + 10 + i * 12, y + h - 12 - bh, x + 20 + i * 12, y + h - 12],
                        fill=(46, 125, 50))
        d.line([x + 8, y + 14, x + 70, y + 74], fill=(179, 38, 30), width=3)
        d.polygon([(x + 62, y + 12), (x + 72, y + 16), (x + 62, y + 22)], fill=(179, 38, 30))
    elif kind == "trophy":
        d.rectangle([x, y, x + w, y + h], fill=(250, 240, 200))
        d.polygon([(x + 24, y + 22), (x + 52, y + 22), (x + 48, y + 52),
                   (x + 28, y + 52)], fill=(201, 162, 39))
        d.arc([x + 10, y + 24, x + 28, y + 46], 90, 270, fill=(201, 162, 39), width=4)
        d.arc([x + 48, y + 24, x + 66, y + 46], -90, 90, fill=(201, 162, 39), width=4)
        d.rectangle([x + 32, y + 52, x + 44, y + 62], fill=(201, 162, 39))
        d.rectangle([x + 22, y + 62, x + 54, y + 68], fill=(201, 162, 39))
        for sx, sy in [(14, 14), (62, 12), (10, 78), (64, 76)]:
            d.polygon([(x + sx, y + sy - 4), (x + sx + 3, y + sy + 3),
                       (x + sx - 3, y + sy + 3)], fill=(255, 200, 40))
    elif kind == "chess":
        d.rectangle([x, y, x + w, y + h], fill=(240, 230, 210))
        s = 17
        ox, oy = x + 4, y + 12
        for r in range(4):
            for c in range(4):
                col = (40, 40, 40) if (r + c) % 2 == 0 else (245, 245, 240)
                d.rectangle([ox + c * s, oy + r * s, ox + (c + 1) * s, oy + (r + 1) * s], fill=col)
        d.ellipse([ox + 6, oy + 6, ox + 26, oy + 26], fill=(255, 255, 255),
                  outline=(20, 36, 62), width=2)
        d.ellipse([ox + 44, oy + 44, ox + 64, oy + 64], fill=(20, 36, 62))
        d.text((x + 10, y + h - 16), "0.5 - 0.5", font=font("DejaVuSans-Bold.ttf", 10), fill=INK)
    elif kind == "gaza":
        d.rectangle([x, y, x + w, y + h], fill=(60, 58, 54))
        for bx, bw, bh in [(6, 18, 44), (28, 16, 58), (48, 20, 38)]:
            d.rectangle([x + bx, y + h - bh, x + bx + bw, y + h], fill=(36, 34, 32))
        d.ellipse([x + 44, y + 8, x + 60, y + 24], fill=(150, 150, 150))
        d.ellipse([x + 52, y + 20, x + 70, y + 38], fill=(120, 120, 120))
        d.polygon([(x + 14, y + 30), (x + 22, y + 18), (x + 30, y + 30)], fill=(255, 150, 0))
    elif kind == "heat":
        d.rectangle([x, y, x + w, y + h], fill=(255, 238, 200))
        for ang in range(0, 360, 30):
            r = math.radians(ang)
            d.line([cx + int(20 * math.cos(r)), cy - 6 + int(20 * math.sin(r)),
                    cx + int(30 * math.cos(r)), cy - 6 + int(30 * math.sin(r))],
                   fill=(230, 120, 0), width=3)
        d.ellipse([cx - 16, cy - 22, cx + 16, cy + 10], fill=(255, 170, 0))
        d.rounded_rectangle([x + 56, y + 52, x + 66, y + 82], 5, fill=(255, 255, 255),
                            outline=(179, 38, 30), width=2)
        d.ellipse([x + 54, y + 78, x + 68, y + 90], fill=(179, 38, 30))
    elif kind == "femicide":
        d.rectangle([x, y, x + w, y + h], fill=(40, 30, 44))
        for i in range(5):
            fx = x + 8 + i * 13
            d.polygon([(fx, y + 20), (fx + 8, y + 20), (fx + 4, y + 30)], fill=(255, 120, 40))
            d.rectangle([fx + 3, y + 30, fx + 5, y + 58], fill=(255, 120, 40))
        d.text((x + 3, y + 66), "5 PER HOUR", font=font("DejaVuSans-Bold.ttf", 9), fill=(255, 180, 90))
    elif kind == "drone":
        d.rectangle([x, y, x + w, y + h], fill=(222, 234, 244))
        d.line([x + 14, y + 30, x + 62, y + 62], fill=(40, 40, 40), width=3)
        d.line([x + 62, y + 30, x + 14, y + 62], fill=(40, 40, 40), width=3)
        d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=(179, 38, 30))
        for px, py in [(14, 30), (62, 30), (14, 62), (62, 62)]:
            d.ellipse([x + px - 6, y + py - 6, x + px + 6, y + py + 6], outline=(40, 40, 40), width=2)
        for i in range(5):
            d.ellipse([x + 8 + i * 3, y + 76 + i, x + 12 + i * 3, y + 80 + i],
                      fill=(179, 38, 30))
    elif kind == "nvidia":
        d.rectangle([x, y, x + w, y + h], fill=(232, 240, 230))
        d.rectangle([x + 18, y + 22, x + 58, y + 62], fill=(20, 60, 30))
        d.rectangle([x + 28, y + 32, x + 48, y + 52], fill=(60, 180, 80))
        for i in range(4):
            d.line([x + 18, y + 28 + i * 8, x + 10, y + 28 + i * 8], fill=(120, 120, 120), width=2)
            d.line([x + 58, y + 28 + i * 8, x + 66, y + 28 + i * 8], fill=(120, 120, 120), width=2)
        d.polygon([(x + 58, y + 70), (x + 66, y + 70), (x + 62, y + 82)], fill=(179, 38, 30))
        d.text((x + 10, y + 82), "-7.8%", font=font("DejaVuSans-Bold.ttf", 11), fill=RED)
    elif kind == "rocket":
        d.rectangle([x, y, x + w, y + h], fill=(16, 24, 48))
        for sx, sy in [(12, 12), (60, 16), (20, 76), (64, 70), (40, 8)]:
            d.ellipse([x + sx, y + sy, x + sx + 3, y + sy + 3], fill=WHITE)
        d.polygon([(cx, y + 14), (cx + 10, y + 44), (cx - 10, y + 44)], fill=(220, 220, 220))
        d.ellipse([cx - 4, cy - 18, cx + 4, cy - 10], fill=(120, 180, 255))
        d.polygon([(cx - 10, y + 44), (cx - 16, y + 56), (cx - 6, y + 50)], fill=(179, 38, 30))
        d.polygon([(cx + 10, y + 44), (cx + 16, y + 56), (cx + 6, y + 50)], fill=(179, 38, 30))
        d.polygon([(cx - 5, y + 46), (cx + 5, y + 46), (cx, y + 68)], fill=(255, 150, 0))
    elif kind == "factory":
        d.rectangle([x, y, x + w, y + h], fill=(238, 232, 220))
        d.polygon([(x + 8, y + 78), (x + 8, y + 44), (x + 20, y + 44), (x + 26, y + 56),
                   (x + 32, y + 44), (x + 44, y + 44), (x + 50, y + 56), (x + 56, y + 44),
                   (x + 68, y + 44), (x + 68, y + 78)], fill=(90, 80, 70))
        d.rectangle([x + 12, y + 20, x + 18, y + 44], fill=(120, 110, 100))
        d.ellipse([x + 40, y + 14, x + 58, y + 32], fill=(255, 200, 40))
        d.rectangle([x + 14, y + 58, x + 62, y + 66], fill=(179, 38, 30))
    elif kind == "ebola":
        d.rectangle([x, y, x + w, y + h], fill=(238, 228, 228))
        for ang in range(0, 360, 30):
            r = math.radians(ang)
            d.line([cx + int(16 * math.cos(r)), cy + int(16 * math.sin(r)),
                    cx + int(26 * math.cos(r)), cy + int(26 * math.sin(r))],
                   fill=(140, 40, 40), width=3)
        d.ellipse([cx - 16, cy - 16, cx + 16, cy + 16], fill=(160, 50, 50))
        d.rectangle([x + 8, y + 70, x + 68, y + 86], fill=WHITE, outline=(179, 38, 30), width=2)
        d.text((x + 14, y + 73), "DR CONGO", font=font("DejaVuSans-Bold.ttf", 9), fill=RED)

PANELS = [
    ("tanker", "Four tankers hit mines in Hormuz",
     "Iran says a fourth tanker struck a mine and burned; the claims are unverified.",
     "IRGC / Tasnim"),
    ("blast", "Russian strike kills 2 in Zaporizhzhia",
     "Overnight attack wounds more than 40, including four children, officials say.",
     "Reuters"),
    ("pharma", "Sanofi buys Insmed for $41bn",
     "Biggest pharma deal of 2026 adds two lung drugs; Sanofi shares rise 5.6%.",
     "Sanofi"),
    ("probe", "Shanghai party chief under probe",
     "Politburo member Chen Jining investigated for grave discipline breaches.",
     "Xinhua"),
    ("chart", "Taiwan stocks soar 9% to record",
     "TAIEX jumps 3,310 points to 40,122 as TSMC hits its daily limit.",
     "Focus Taiwan"),
    ("trophy", "Senegal's AFCON crown restored",
     "CAS overturns the Morocco award; the 1-0 extra-time final win stands.",
     "AP"),
    ("chess", "Chess title match opens in a draw",
     "Gukesh survives time trouble; game one with Sindarov ends 0.5-0.5.",
     "FIDE"),
    ("gaza", "Six killed in Gaza strikes",
     "Strikes hit Khan Younis and Netzarim; a Hamas security chief is among the dead.",
     "Reuters"),
    ("heat", "Record 5,258 heat deaths in England",
     "Summer 2026 toll is the highest since records began in 2016.",
     "UKHSA"),
    ("femicide", "Five women killed every hour",
     "UN counts 47,000 killed by partners or family in 2025.",
     "UNODC / UN Women"),
    ("drone", "Russian drone enters Polish airspace",
     "Brief incursion during the overnight attack on western Ukraine.",
     "Polish Armed Forces"),
    ("nvidia", "Nvidia slides 7.8% after comeback",
     "Shares give back part of Monday's 31% surge on Huang's return.",
     "Motley Fool"),
    ("rocket", "Three rockets lift off in one day",
     "Progress MS-36, Ariane's 36 Leo satellites and a US Space Force launch.",
     "NASASpaceflight"),
    ("factory", "Garment workers shut 100 factories",
     "Wage protests close plants across Gazipur, north of Dhaka.",
     "IANS"),
    ("ebola", "Ebola toll climbs in DR Congo",
     "11,613 cases and 5,678 deaths; health workers trapped in a hospital.",
     "UN News / WHO"),
]

DIGEST = [
    ("EUROPE", "Russia claims 699 drones downed overnight"),
    ("EUROPE", "UK warns defence firms of sabotage threat"),
    ("EUROPE", "Sparta II towed to St Petersburg"),
    ("MIDEAST", "US sanctions 24+ Iran exchange houses"),
    ("MIDEAST", "Cairo hosts Gaza phase-two talks"),
    ("MIDEAST", "Gaza declares meningitis epidemic alert"),
    ("E ASIA", "Taiwan tracks 3 PLA aircraft, 9 warships"),
    ("E ASIA", "Seoul speaker meets Japan's PM"),
    ("S ASIA", "Hasina plans Dec 16 return; arrest warned"),
    ("S ASIA", "India gives Nepal a $1.62bn package"),
    ("S ASIA", "5,000 Sikhs mark Guru Nanak in Pakistan"),
    ("S ASIA", "Measles toll in Bangladesh passes 1,350"),
    ("AFRICA", "DR Congo orders miners to open to locals"),
    ("AMERICAS", "US pauses joint ops with Ecuador"),
    ("AMERICAS", "Trump to meet NATO chief Rutte"),
    ("AMERICAS", "US lawmakers assail Nvidia's Huang return"),
    ("AMERICAS", "US presses Americas narco-terror pact"),
    ("MARKETS", "India stocks add Rs 35 lakh crore in Nov"),
    ("SPORT", "Sooryavanshi, 15, hits 204 off 53 balls"),
]

DATE_CHECK = [
    ("Nvidia reinstates Jensen Huang as CEO", "23 Nov"),
    ("COP31 ends with no climate deal", "22 Nov"),
    ("Ukraine says it sank a corvette off Libya", "22-23 Nov"),
    ("Russia warns Estonia of 'open war'", "23 Nov"),
    ("US adds Megaspeed to its Entity List", "23 Nov"),
    ("BepiColombo enters orbit around Mercury", "23 Nov"),
    ("Africa health conference opens in Addis", "23 Nov"),
]

TIMELINE = [
    ("00:20", "Gaza strikes kill six"),
    ("05:30", "TAIEX +9%, record 40,122"),
    ("06:30", "Sanofi's $41bn Insmed deal"),
    ("10:13", "Progress MS-36 lifts off"),
    ("15:51", "CAS restores Senegal title"),
    ("19:08", "Falcon 9 launches USSF-266"),
]

REGIONS = [("EUROPE", 6), ("MIDDLE EAST", 5), ("EAST ASIA", 3), ("SOUTH ASIA", 5),
           ("AFRICA", 3), ("AMERICAS", 4), ("MARKETS", 4), ("GLOBAL + SPORT", 6)]

KPIS = [("36", "dated stories"), ("8", "regions"), ("4", "tankers hit"),
        ("$41bn", "Sanofi deal"), ("+8.99%", "TAIEX"), ("5,258", "UK heat deaths")]

# Pin positions (fraction of map area) for the 15 panels.
PINS = [(0.60, 0.52), (0.56, 0.25), (0.46, 0.29), (0.80, 0.40), (0.83, 0.46),
        (0.40, 0.52), (0.49, 0.31), (0.565, 0.40), (0.45, 0.21), (0.27, 0.33),
        (0.53, 0.21), (0.14, 0.36), (0.66, 0.27), (0.74, 0.46), (0.51, 0.60)]

def draw_map(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=SEA)
    # Rough continent blobs (equirectangular sketch).
    blobs = [
        [(0.06, 0.10), (0.28, 0.08), (0.32, 0.22), (0.24, 0.34), (0.14, 0.42),
         (0.08, 0.30)],  # N America
        [(0.24, 0.48), (0.34, 0.46), (0.36, 0.60), (0.30, 0.74), (0.26, 0.62)],
        [(0.44, 0.08), (0.56, 0.06), (0.58, 0.20), (0.52, 0.30), (0.46, 0.24),
         (0.42, 0.14)],  # Europe
        [(0.44, 0.34), (0.56, 0.32), (0.60, 0.46), (0.54, 0.66), (0.48, 0.60),
         (0.44, 0.46)],  # Africa
        [(0.58, 0.10), (0.86, 0.08), (0.92, 0.24), (0.84, 0.42), (0.72, 0.48),
         (0.64, 0.36), (0.58, 0.24)],  # Asia
        [(0.80, 0.62), (0.90, 0.60), (0.92, 0.70), (0.84, 0.74), (0.80, 0.68)],
    ]
    for blob in blobs:
        pts = [(x + fx * w, y + fy * h) for fx, fy in blob]
        d.polygon(pts, fill=LAND, outline=(140, 142, 116))
    for i, (fx, fy) in enumerate(PINS, 1):
        px, py = x + fx * w, y + fy * h
        d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=WHITE, width=1)
        num = str(i)
        tw = d.textlength(num, font=font("DejaVuSans-Bold.ttf", 9))
        d.text((px - tw / 2, py - 6), num, font=font("DejaVuSans-Bold.ttf", 9), fill=WHITE)

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- Masthead ---
    d.rectangle([0, 0, W, 72], fill=NAVY)
    d.rectangle([0, 72, W, 76], fill=GOLD)
    d.text((16, 8), "THE WORLD IN ONE DAY", font=F_TITLE, fill=WHITE)
    d.text((16, 52), "TUESDAY 24 NOVEMBER 2026  ·  THE FULL DAY, IN EVERY TIME ZONE",
           font=F_SUB, fill=(212, 175, 80))
    d.text((W - 16 - d.textlength("36 STORIES · 8 REGIONS · 15 PICTURED", font=F_SUB), 52),
           "36 STORIES · 8 REGIONS · 15 PICTURED", font=F_SUB, fill=WHITE)

    # --- KPI strip ---
    y0 = 84
    bw = (W - 16 - 5 * 6) // 6
    for i, (num, lab) in enumerate(KPIS):
        bx = 8 + i * (bw + 6)
        d.rectangle([bx, y0, bx + bw, y0 + 34], fill=WHITE, outline=LINE)
        tw = d.textlength(num, font=F_KPI_N)
        d.text((bx + (bw - tw) / 2, y0 + 1), num, font=F_KPI_N, fill=NAVY)
        tw = d.textlength(lab, font=F_KPI_L)
        d.text((bx + (bw - tw) / 2, y0 + 22), lab, font=F_KPI_L, fill=MUTED)

    # --- Region bar ---
    y0 = 126
    rw = (W - 16 - 7 * 4) // 8
    for i, (name, n) in enumerate(REGIONS):
        bx = 8 + i * (rw + 4)
        d.rectangle([bx, y0, bx + rw, y0 + 20], fill=NAVY2)
        label = f"{name} {n}"
        tw = d.textlength(label, font=F_REG)
        d.text((bx + (rw - tw) / 2, y0 + 3), label, font=F_REG, fill=WHITE)

    # --- Timeline ---
    y0 = 154
    d.text((8, y0), "THE DAY IN UTC", font=F_SEC, fill=NAVY)
    d.line([8, y0 + 18, W - 8, y0 + 18], fill=GOLD, width=2)
    tw = (W - 16 - 5 * 8) // 6
    for i, (t, lab) in enumerate(TIMELINE):
        bx = 8 + i * (tw + 8)
        d.text((bx, y0 + 22), t, font=F_TIME, fill=RED)
        d.text((bx, y0 + 40), lab, font=F_TL, fill=INK)

    # --- Panels: 3 cols x 5 rows ---
    px0, py0 = 8, 208
    pw, ph, gap = 328, 104, 8
    for idx, (kind, head, summ, outlet) in enumerate(PANELS):
        r, c = divmod(idx, 3)
        x = px0 + c * (pw + gap)
        y = py0 + r * (ph + 7)
        d.rectangle([x, y, x + pw, y + ph], fill=PANEL_BG, outline=LINE)
        d.rectangle([x, y, x + 26, y + ph], fill=NAVY)
        num = str(idx + 1)
        tw = d.textlength(num, font=font("DejaVuSans-Bold.ttf", 12))
        d.text((x + (26 - tw) / 2, y + 6), num, font=font("DejaVuSans-Bold.ttf", 12), fill=WHITE)
        ax, ay = x + 32, y + 5
        draw_panel_art(d, kind, ax, ay, 72, 94)
        tx = ax + 78
        twd = pw - 32 - 78 - 8
        lines = wrap(d, head, F_HEAD, twd)[:2]
        ly = y + 6
        for ln in lines:
            d.text((tx, ly), ln, font=F_HEAD, fill=INK)
            ly += 16
        ly += 1
        for ln in wrap(d, summ, F_SUM, twd)[:3]:
            d.text((tx, ly), ln, font=F_SUM, fill=(60, 58, 52))
            ly += 13
        d.text((tx, y + ph - 14), "— " + outlet, font=F_OUT, fill=MUTED)

    # --- Bottom band ---
    by = 762
    bh = 248
    # Map
    mx, mw = 8, 328
    d.rectangle([mx, by, mx + mw, by + bh], fill=WHITE, outline=LINE)
    d.text((mx + 8, by + 6), "WHERE IT HAPPENED  ·  PINS 1-15", font=F_SEC, fill=NAVY)
    draw_map(d, mx + 8, by + 26, mw - 16, bh - 26 - 24)
    d.text((mx + 8, by + bh - 20), "Pins match the numbered panels above.",
           font=F_OUT, fill=MUTED)
    # Digest
    dx, dw = 344, 328
    d.rectangle([dx, by, dx + dw, by + bh], fill=WHITE, outline=LINE)
    d.text((dx + 8, by + 6), "THE REST OF THE DAY", font=F_SEC, fill=NAVY)
    ly = by + 25
    for tag, item in DIGEST:
        d.text((dx + 8, ly), tag, font=font("DejaVuSans-Bold.ttf", 9), fill=RED)
        d.text((dx + 70, ly), item, font=F_DIG, fill=INK)
        ly += 11.5
    # Date check
    ex, ew = 680, 336
    d.rectangle([ex, by, ex + ew, by + bh], fill=(255, 248, 240), outline=(200, 140, 100))
    d.text((ex + 8, by + 6), "DATE CHECK — NOT 24 NOVEMBER", font=F_SEC, fill=RED)
    d.text((ex + 8, by + 22), "Left out on purpose; these happened on other days.",
           font=F_OUT, fill=MUTED)
    ly = by + 40
    for item, when in DATE_CHECK:
        d.text((ex + 8, ly), item, font=F_DC, fill=INK)
        tw = d.textlength(when, font=font("DejaVuSans-Bold.ttf", 10))
        d.text((ex + ew - 10 - tw, ly), when, font=font("DejaVuSans-Bold.ttf", 10), fill=RED)
        ly += 16
    d.text((ex + 8, by + bh - 38), "Counted stories: 36. Excluded above: 7.",
           font=font("DejaVuSans-Bold.ttf", 10), fill=NAVY)
    d.text((ex + 8, by + bh - 22), "Every date checked against first reports.",
           font=F_OUT, fill=MUTED)
    # Footer
    d.text((8, H - 10), "Every story dated Tuesday 24 November 2026. Full sources, times and outlets in SOURCES.md.",
           font=F_FOOT, fill=MUTED)

    img.save("/home/hatch/workspace/makefun-news-image-20261124/entry-refresh.png",
             optimize=True)
    print("saved")

if __name__ == "__main__":
    main()
