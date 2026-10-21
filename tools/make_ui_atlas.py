"""UI sprite sheet (1024x1024) for Build Your Dream Zoo!  Safari theme: carved wood, parchment, jungle leaves.

Regions (x, y, w, h) are listed in REGIONS and printed as Lua at the end, so the game's UI module can
slice the sheet with ImageRectOffset / ImageRectSize (and SliceCenter for the 9-slice pieces).
Tintable pieces (button, bar fill, paw, glow, sparkle, rays) are drawn in white/grey so ImageColor3
can colour them; outlines stay dark because tinting multiplies.
"""
import math
import random

import cairosvg

DARK = "#3C2D23"
WOOD, WOOD_LIGHT, WOOD_DARK, WOOD_GRAIN = "#B97A45", "#D69C60", "#8A5530", "#9C6438"
PAPER, PAPER_EDGE = "#FFF6E2", "#EAD7B0"
OUT = "/tmp/claude-0/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/scratchpad/icons/"

parts = []
REGIONS = {}  # name -> (x, y, w, h, slice) where slice = (left, top, right, bottom) in region pixels or None


def region(name, x, y, w, h, slice_=None):
    REGIONS[name] = (x, y, w, h, slice_)


def defs():
    return f'''<defs>
  <linearGradient id="woodV" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{WOOD_LIGHT}"/><stop offset="1" stop-color="{WOOD}"/></linearGradient>
  <linearGradient id="woodH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{WOOD_LIGHT}"/><stop offset="1" stop-color="{WOOD}"/></linearGradient>
  <linearGradient id="btn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#DADADA"/></linearGradient>
  <linearGradient id="trackG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4A3424"/><stop offset="1" stop-color="#6A4A33"/></linearGradient>
  <linearGradient id="leafA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8FD45E"/><stop offset="1" stop-color="#4E9E3C"/></linearGradient>
  <linearGradient id="leafB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6CC04F"/><stop offset="1" stop-color="#2F7A39"/></linearGradient>
  <radialGradient id="glow"><stop offset="0" stop-color="#FFFFFF" stop-opacity="1"/><stop offset="0.45" stop-color="#FFFFFF" stop-opacity="0.45"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
  <linearGradient id="ticket" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB27A"/><stop offset="1" stop-color="#FF7F4A"/></linearGradient>
  <linearGradient id="red" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF7A6E"/><stop offset="1" stop-color="#D9473F"/></linearGradient>
  <linearGradient id="gold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE27A"/><stop offset="1" stop-color="#F2B230"/></linearGradient>
</defs>'''


def nail(x, y, r=7):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#6B5A4E" stroke="{DARK}" stroke-width="3"/>'
            f'<circle cx="{x - r * 0.3}" cy="{y - r * 0.3}" r="{r * 0.35}" fill="#B8AA9E"/>')


def grain_h(x0, x1, y0, y1, n, rng, color=WOOD_GRAIN):
    s = []
    for i in range(n):
        y = y0 + (y1 - y0) * (i + 0.5) / n + rng.uniform(-2, 2)
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{color}" stroke-width="{rng.choice([2, 2.5, 3])}" opacity="0.55" stroke-linecap="round"/>')
    return "".join(s)


def grain_v(y0, y1, x0, x1, n, rng, color=WOOD_GRAIN):
    s = []
    for i in range(n):
        x = x0 + (x1 - x0) * (i + 0.5) / n + rng.uniform(-2, 2)
        s.append(f'<line x1="{x:.1f}" y1="{y0}" x2="{x:.1f}" y2="{y1}" stroke="{color}" stroke-width="{rng.choice([2, 2.5, 3])}" opacity="0.55" stroke-linecap="round"/>')
    return "".join(s)


rng = random.Random(7)

# ---------------------------------------------------------------- A. panel: carved wood frame + parchment (9-slice 64)
x, y = 0, 0
parts.append(f'<rect x="{x + 4}" y="{y + 4}" width="248" height="248" rx="42" fill="{WOOD}" stroke="{DARK}" stroke-width="7"/>')
# grain: horizontal on the top/bottom bars, vertical on the side bars (so 9-slice stretching keeps it straight)
parts.append(grain_h(x + 64, x + 192, y + 10, y + 36, 3, rng) + grain_h(x + 64, x + 192, y + 220, y + 246, 3, rng))
parts.append(grain_v(y + 64, y + 192, x + 10, x + 36, 3, rng) + grain_v(y + 64, y + 192, x + 220, x + 246, 3, rng))
parts.append(f'<rect x="{x + 8}" y="{y + 8}" width="240" height="240" rx="38" fill="none" stroke="{WOOD_LIGHT}" stroke-width="3" opacity="0.8"/>')
parts.append(f'<rect x="{x + 38}" y="{y + 38}" width="180" height="180" rx="16" fill="{PAPER}" stroke="{DARK}" stroke-width="5"/>')
parts.append(f'<rect x="{x + 44}" y="{y + 44}" width="168" height="168" rx="12" fill="none" stroke="{PAPER_EDGE}" stroke-width="5"/>')
for nx, ny in ((22, 22), (234, 22), (22, 234), (234, 234)):
    parts.append(nail(x + nx, y + ny))
region("Panel", x, y, 256, 256, (64, 64, 192, 192))

# ---------------------------------------------------------------- B. plank sign header (9-slice 72 left/right)
x, y = 256, 0
parts.append(f'<rect x="{x + 6}" y="{y + 14}" width="500" height="100" rx="30" fill="url(#woodV)" stroke="{DARK}" stroke-width="7"/>')
parts.append(grain_h(x + 72, x + 440, y + 30, y + 100, 4, rng))
parts.append(f'<path d="M{x + 30},{y + 26} L{x + 482},{y + 26}" stroke="#F2C08A" stroke-width="4" opacity="0.8" stroke-linecap="round"/>')
parts.append(f'<path d="M{x + 30},{y + 104} L{x + 482},{y + 104}" stroke="{WOOD_DARK}" stroke-width="5" opacity="0.7" stroke-linecap="round"/>')
parts.append(nail(x + 36, y + 64, 8) + nail(x + 476, y + 64, 8))
region("Plank", x, y, 512, 128, (72, 40, 440, 88))

# ---------------------------------------------------------------- C. chunky button (white, tintable; 9-slice 36)
x, y = 768, 0
parts.append(f'<rect x="{x + 4}" y="{y + 6}" width="120" height="116" rx="28" fill="{DARK}"/>')            # outline + drop
parts.append(f'<rect x="{x + 10}" y="{y + 12}" width="108" height="100" rx="22" fill="#9C9C9C"/>')       # the lip (darker when tinted)
parts.append(f'<rect x="{x + 10}" y="{y + 10}" width="108" height="90" rx="22" fill="url(#btn)"/>')       # face
parts.append(f'<rect x="{x + 20}" y="{y + 18}" width="88" height="22" rx="11" fill="#FFFFFF" opacity="0.7"/>')  # shine
region("Button", x, y, 128, 128, (36, 40, 92, 84))

# ---------------------------------------------------------------- D. round close button (full colour)
x, y = 896, 0
cx, cy = x + 64, y + 62
parts.append(f'<circle cx="{cx}" cy="{cy + 4}" r="54" fill="{DARK}"/>')
parts.append(f'<circle cx="{cx}" cy="{cy}" r="48" fill="#B23A33"/>')
parts.append(f'<circle cx="{cx}" cy="{cy - 4}" r="46" fill="url(#red)"/>')
parts.append(f'<ellipse cx="{cx}" cy="{cy - 26}" rx="28" ry="10" fill="#FFFFFF" opacity="0.45"/>')
d = 20  # the X: dark strokes first, white on top, so the outline never crosses the middle
xs = f'M{cx - d},{cy - 3 - d} L{cx + d},{cy - 3 + d} M{cx + d},{cy - 3 - d} L{cx - d},{cy - 3 + d}'
parts.append(f'<path d="{xs}" stroke="{DARK}" stroke-width="26" stroke-linecap="round"/>')
parts.append(f'<path d="{xs}" stroke="#FFFFFF" stroke-width="15" stroke-linecap="round"/>')
region("Close", x, y, 128, 128)


# ---------------------------------------------------------------- E. jungle leaf cluster (corner ornament) + mirror
def leaf(px, py, length, width, angle, fill):
    # a pointed leaf from (px, py) along `angle`, with a midrib
    a = math.radians(angle)
    ex, ey = px + math.cos(a) * length, py + math.sin(a) * length
    nx, ny = -math.sin(a) * width, math.cos(a) * width
    mx, my = px + math.cos(a) * length * 0.45, py + math.sin(a) * length * 0.45
    d = (f'M{px:.1f},{py:.1f} Q{mx + nx:.1f},{my + ny:.1f} {ex:.1f},{ey:.1f} '
         f'Q{mx - nx:.1f},{my - ny:.1f} {px:.1f},{py:.1f} Z')
    return (f'<path d="{d}" fill="{fill}" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="M{px:.1f},{py:.1f} L{px + math.cos(a) * length * 0.8:.1f},{py + math.sin(a) * length * 0.8:.1f}" stroke="#2E6B2E" stroke-width="3" opacity="0.7" stroke-linecap="round"/>')


def leaves(ox, oy, mirror=False):
    g = [f'<g transform="translate({ox + (256 if mirror else 0)} {oy}) scale({-1 if mirror else 1} 1)">']
    spec = [(26, 30, 175, 46, 8, "url(#leafB)"), (20, 24, 150, 40, 38, "url(#leafA)"), (30, 20, 190, 44, 62, "url(#leafB)"),
            (24, 26, 140, 36, 84, "url(#leafA)"), (18, 34, 120, 32, -14, "url(#leafA)")]
    for px, py, length, width, ang, fill in spec:
        g.append(leaf(px, py, length, width, ang, fill))
    # a little flower in the cluster
    fx, fy = 70, 66
    for k in range(5):
        a = k / 5 * math.tau
        g.append(f'<ellipse cx="{fx + math.cos(a) * 11:.1f}" cy="{fy + math.sin(a) * 11:.1f}" rx="10" ry="7" transform="rotate({math.degrees(a):.0f} {fx + math.cos(a) * 11:.1f} {fy + math.sin(a) * 11:.1f})" fill="#FF8FB1" stroke="{DARK}" stroke-width="3"/>')
    g.append(f'<circle cx="{fx}" cy="{fy}" r="7" fill="#FFD84A" stroke="{DARK}" stroke-width="3"/>')
    g.append('</g>')
    return "".join(g)


parts.append(leaves(0, 256))
parts.append(leaves(256, 256, mirror=True))
region("LeavesLeft", 0, 256, 256, 256)
region("LeavesRight", 256, 256, 256, 256)


# ---------------------------------------------------------------- F. paw print tile (white, tileable)
def paw(cx, cy, s, rot, fill="#FFFFFF", stroke=None):
    st = f' stroke="{stroke}" stroke-width="3"' if stroke else ""  # scaled with the group, so ~3*s px
    g = [f'<g transform="translate({cx} {cy}) rotate({rot}) scale({s})">',
         f'<ellipse cx="0" cy="8" rx="15" ry="12" fill="{fill}"{st}/>']
    for tx, ty in ((-16, -8), (-6, -17), (6, -17), (16, -8)):
        g.append(f'<ellipse cx="{tx}" cy="{ty}" rx="5.5" ry="7" fill="{fill}"{st}/>')
    g.append('</g>')
    return "".join(g)


x, y = 512, 256
for px, py, s, r in ((64, 64, 1.4, -20), (190, 104, 1.2, 25), (100, 190, 1.3, 10), (210, 222, 1.0, -35), (30, 150, 0.9, 40)):
    parts.append(paw(x + px, y + py, s, r))
region("PawTile", x, y, 256, 256)

# ---------------------------------------------------------------- G-J. glow, sparkle, solid paw, ticket
x, y = 768, 256
parts.append(f'<circle cx="{x + 64}" cy="{y + 64}" r="62" fill="url(#glow)"/>')
region("Glow", x, y, 128, 128)
x, y = 896, 256
s = 56
cx, cy = x + 64, y + 64
parts.append(f'<path d="M{cx},{cy - s} Q{cx + s * 0.16},{cy - s * 0.16} {cx + s},{cy} Q{cx + s * 0.16},{cy + s * 0.16} {cx},{cy + s} '
             f'Q{cx - s * 0.16},{cy + s * 0.16} {cx - s},{cy} Q{cx - s * 0.16},{cy - s * 0.16} {cx},{cy - s} Z" fill="#FFFFFF"/>')
region("Sparkle", x, y, 128, 128)
x, y = 768, 384
parts.append(paw(x + 64, y + 70, 2.6, 0, "#FFFFFF", DARK))
region("Paw", x, y, 128, 128)
x, y = 896, 384
parts.append(f'<g transform="rotate(-12 {x + 64} {y + 64})">'
             f'<rect x="{x + 14}" y="{y + 34}" width="100" height="62" rx="12" fill="url(#ticket)" stroke="{DARK}" stroke-width="6"/>'
             f'<line x1="{x + 42}" y1="{y + 42}" x2="{x + 42}" y2="{y + 88}" stroke="#FFE3D0" stroke-width="5" stroke-dasharray="7 6"/>'
             f'<circle cx="{x + 80}" cy="{y + 65}" r="11" fill="#FFE3D0" stroke="{DARK}" stroke-width="3"/></g>')
region("Ticket", x, y, 128, 128)

# ---------------------------------------------------------------- K-M. progress bar track + fill, dark wood tag
x, y = 0, 512
parts.append(f'<rect x="{x + 4}" y="{y + 4}" width="248" height="56" rx="28" fill="url(#trackG)" stroke="{DARK}" stroke-width="6"/>')
parts.append(f'<rect x="{x + 14}" y="{y + 12}" width="228" height="10" rx="5" fill="#000000" opacity="0.25"/>')
region("BarTrack", x, y, 256, 64, (32, 28, 224, 36))
x, y = 256, 512
parts.append(f'<rect x="{x + 4}" y="{y + 6}" width="248" height="52" rx="26" fill="#B5B5B5"/>')
parts.append(f'<rect x="{x + 4}" y="{y + 4}" width="248" height="46" rx="23" fill="#FFFFFF"/>')
parts.append(f'<rect x="{x + 18}" y="{y + 10}" width="220" height="12" rx="6" fill="#FFFFFF" opacity="0.9"/>')
region("BarFill", x, y, 256, 64, (30, 28, 226, 36))
x, y = 0, 576
parts.append(f'<rect x="{x + 4}" y="{y + 6}" width="248" height="84" rx="30" fill="#6E4A2F" stroke="{DARK}" stroke-width="6"/>')
parts.append(grain_h(x + 40, x + 216, y + 20, y + 80, 3, rng, "#5A3B25"))
parts.append(f'<path d="M{x + 30},{y + 18} L{x + 226},{y + 18}" stroke="#9A6E4A" stroke-width="4" opacity="0.8" stroke-linecap="round"/>')
region("Tag", x, y, 256, 96, (40, 40, 216, 56))

# ---------------------------------------------------------------- N. sunburst rays (white)
x, y = 512, 512
cx, cy, n = x + 256, y + 256, 16
for i in range(n):
    a0 = i / n * math.tau
    a1 = a0 + math.pi / n
    parts.append(f'<path d="M{cx},{cy} L{cx + math.cos(a0) * 256:.1f},{cy + math.sin(a0) * 256:.1f} '
                 f'L{cx + math.cos(a1) * 256:.1f},{cy + math.sin(a1) * 256:.1f} Z" fill="#FFFFFF"/>')
region("Rays", x, y, 512, 512)

# ---------------------------------------------------------------- O. gate door (one half of the zoo gates)
x, y = 0, 672
parts.append(f'<rect x="{x}" y="{y}" width="256" height="352" fill="{DARK}"/>')
pw = 256 / 5
for i in range(5):
    px = x + i * pw
    parts.append(f'<rect x="{px + 3:.1f}" y="{y + 3}" width="{pw - 6:.1f}" height="346" rx="6" fill="{[WOOD, WOOD_LIGHT, WOOD, "#C58550", WOOD][i]}"/>')
    parts.append(grain_v(y + 10, y + 342, px + 10, px + pw - 10, 2, rng))
for by in (y + 70, y + 282):
    parts.append(f'<rect x="{x}" y="{by - 14}" width="256" height="28" fill="#4E4A4A" stroke="{DARK}" stroke-width="4"/>')
    for k in range(6):
        parts.append(f'<circle cx="{x + 20 + k * 43}" cy="{by}" r="5" fill="#9A9494" stroke="{DARK}" stroke-width="2"/>')
region("GateDoor", x, y, 256, 352)

# ---------------------------------------------------------------- render
svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">{defs()}{"".join(parts)}</svg>'
cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT + "ui_atlas.png", output_width=1024, output_height=1024)

lua = ["UI.Sprites = { -- name = { x, y, w, h, slice? }  (slice = Rect in region pixels)"]
for name, (rx, ry, rw, rh, sl) in REGIONS.items():
    sls = f", Rect.new({sl[0]}, {sl[1]}, {sl[2]}, {sl[3]})" if sl else ""
    lua.append(f"\t{name} = {{ {rx}, {ry}, {rw}, {rh}{sls} }},")
lua.append("}")
print("\n".join(lua))
