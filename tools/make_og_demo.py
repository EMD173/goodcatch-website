#!/usr/bin/env python3
"""Generate og-demo.jpg — the link-preview card for goodcatchapp.com/demo.html.
Same family as og-card.jpg (green check, Georgia Bold), demo-specific copy."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
CREAM = (250, 251, 248)
INK = (15, 36, 25)
GREEN = (27, 122, 61)
GRAY = (90, 100, 94)

img = Image.new("RGB", (W, H), CREAM)
d = ImageDraw.Draw(img)

georgia = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
helv = "/System/Library/Fonts/Helvetica.ttc"
f_logo = ImageFont.truetype(georgia, 64)
f_head = ImageFont.truetype(georgia, 78)
f_sub = ImageFont.truetype(helv, 30)
f_badge = ImageFont.truetype(helv, 26)

# logo block: rounded green square + stroke-drawn check (glyph is tofu in Helvetica)
bx, by, bs = 80, 90, 120
d.rounded_rectangle([bx, by, bx + bs, by + bs], radius=26, fill=GREEN)
pts = [(bx + 28, by + 62), (bx + 52, by + 86), (bx + 94, by + 36)]
d.line(pts, fill="white", width=14, joint="curve")
for p in pts:
    d.ellipse([p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7], fill="white")
d.text((bx + bs + 36, by + 22), "GoodCatch", font=f_logo, fill=INK)

# PROTOTYPE badge
btxt = "CLICKABLE PROTOTYPE"
bw = d.textlength(btxt, font=f_badge)
px, py = 84, 280
d.rounded_rectangle([px, py, px + bw + 44, py + 52], radius=26, outline=GREEN, width=3)
d.text((px + 22, py + 11), btxt, font=f_badge, fill=GREEN)

# headline
d.text((80, 366), "Try it. Tap around.", font=f_head, fill=INK)
d.text((80, 458), "Nothing here is real.", font=f_head, fill=GREEN)

# subline
d.text((82, 566), "Demo data only · your feedback shapes the app · goodcatchapp.com/demo",
       font=f_sub, fill=GRAY)

img.save("/Users/elidavis/Desktop/goodcatch-website/og-demo.jpg", quality=90)
print("wrote og-demo.jpg")
