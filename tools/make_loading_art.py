"""Loading art sheet (1024x1024): a savanna/zoo scene (0, 0, 1024, 576) and the game logo (0, 600, 1024, 400)."""
import math
import sys

import cairosvg

sys.path.insert(0, "/tmp/claude-0/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/scratchpad/icons")
from make_icons import DARK, OUT, outlined_text, sparkle  # noqa: E402
from make_game_icon import lion  # noqa: E402

W = 1024
S = []


def cloud(x, y, s):
    g = [f'<g transform="translate({x} {y}) scale({s})">']
    for cx, cy, r in ((0, 0, 34), (40, -16, 42), (84, 0, 32), (42, 12, 34)):
        g.append(f'<circle cx="{cx}" cy="{cy}" r="{r + 4}" fill="{DARK}" opacity="0.18"/>')
    for cx, cy, r in ((0, 0, 34), (40, -16, 42), (84, 0, 32), (42, 12, 34)):
        g.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#FFFFFF"/>')
    g.append('</g>')
    return "".join(g)


def hill(d, fill, outline=True):
    st = f' stroke="{DARK}" stroke-width="6" stroke-linejoin="round"' if outline else ""
    return f'<path d="{d}" fill="{fill}"{st}/>'


def acacia(x, y, s):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-6,0 L6,0 L8,-58 L30,-92 L22,-97 L3,-70 L-16,-98 L-24,-93 L-6,-58 Z" fill="#7A4B2A" stroke="{DARK}" stroke-width="5" stroke-linejoin="round"/>'
            f'<ellipse cx="0" cy="-104" rx="82" ry="20" fill="#5E8F3A" stroke="{DARK}" stroke-width="5"/>'
            f'<ellipse cx="-16" cy="-116" rx="50" ry="16" fill="#79AE4C" stroke="{DARK}" stroke-width="5"/>'
            f'<ellipse cx="-24" cy="-121" rx="22" ry="6" fill="#9BCB66"/></g>')


def round_tree(x, y, s, a="#6DBE4B", b="#4E9E3C"):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-9,0 L9,0 L7,-60 L-7,-60 Z" fill="#7A4B2A" stroke="{DARK}" stroke-width="5"/>'
            f'<circle cx="-26" cy="-72" r="34" fill="{b}" stroke="{DARK}" stroke-width="5"/>'
            f'<circle cx="26" cy="-74" r="32" fill="{b}" stroke="{DARK}" stroke-width="5"/>'
            f'<circle cx="0" cy="-98" r="40" fill="{a}" stroke="{DARK}" stroke-width="5"/>'
            f'<circle cx="-12" cy="-110" r="12" fill="#9BD86F"/></g>')


def giraffe(x, y, s):
    Y, SP = "#FFCB4A", "#C9822E"
    g = [f'<g transform="translate({x} {y}) scale({s})">']
    for lx in (-44, -24, 26, 46):  # legs
        g.append(f'<rect x="{lx - 7}" y="-10" width="14" height="96" rx="6" fill="{Y}" stroke="{DARK}" stroke-width="5"/>')
        g.append(f'<rect x="{lx - 8}" y="78" width="16" height="12" rx="4" fill="#6B4A32" stroke="{DARK}" stroke-width="4"/>')
    g.append(f'<path d="M-62,-8 Q-86,10 -80,40" fill="none" stroke="{DARK}" stroke-width="9" stroke-linecap="round"/>')  # tail
    g.append(f'<path d="M-62,-8 Q-86,10 -80,40" fill="none" stroke="{Y}" stroke-width="4" stroke-linecap="round"/>')
    g.append(f'<ellipse cx="0" cy="-16" rx="70" ry="42" fill="{Y}" stroke="{DARK}" stroke-width="6"/>')
    g.append(f'<path d="M30,-40 L58,-190 L86,-182 L66,-30 Z" fill="{Y}" stroke="{DARK}" stroke-width="6" stroke-linejoin="round"/>')  # neck
    g.append(f'<path d="M50,-170 Q40,-120 46,-60" fill="none" stroke="#B4692A" stroke-width="7" stroke-linecap="round"/>')  # mane
    for sx, sy, r in ((-30, -24, 13), (2, -36, 11), (28, -10, 12), (-6, 2, 9), (-48, -2, 9), (62, -110, 9), (70, -150, 7), (60, -70, 9)):
        g.append(f'<ellipse cx="{sx}" cy="{sy}" rx="{r}" ry="{r * 0.8}" fill="{SP}"/>')
    # head
    for ox in (-10, 8):
        g.append(f'<line x1="{80 + ox}" y1="-210" x2="{82 + ox}" y2="-236" stroke="{DARK}" stroke-width="11" stroke-linecap="round"/>')
        g.append(f'<line x1="{80 + ox}" y1="-210" x2="{82 + ox}" y2="-236" stroke="{Y}" stroke-width="5" stroke-linecap="round"/>')
        g.append(f'<circle cx="{82 + ox}" cy="-240" r="7" fill="{SP}" stroke="{DARK}" stroke-width="4"/>')
    g.append(f'<ellipse cx="58" cy="-208" rx="16" ry="8" transform="rotate(-25 58 -208)" fill="{Y}" stroke="{DARK}" stroke-width="5"/>')
    g.append(f'<ellipse cx="88" cy="-196" rx="34" ry="24" transform="rotate(14 88 -196)" fill="{Y}" stroke="{DARK}" stroke-width="6"/>')
    g.append(f'<ellipse cx="112" cy="-186" rx="16" ry="13" fill="#FFE7A8" stroke="{DARK}" stroke-width="4"/>')
    g.append(f'<ellipse cx="88" cy="-204" rx="5" ry="7" fill="{DARK}"/><circle cx="90" cy="-207" r="2.2" fill="#FFFFFF"/>')
    g.append(f'<ellipse cx="102" cy="-196" rx="7" ry="4" fill="#F59A8C" opacity="0.8"/>')
    g.append('</g>')
    return "".join(g)


def elephant(x, y, s):
    G, G2 = "#A9B3C2", "#8E99AA"
    g = [f'<g transform="translate({x} {y}) scale({s})">']
    for lx in (-58, -22, 28, 62):
        g.append(f'<rect x="{lx - 17}" y="0" width="34" height="62" rx="10" fill="{G2 if lx in (-22, 62) else G}" stroke="{DARK}" stroke-width="6"/>')
        for t in (-8, 0, 8):
            g.append(f'<circle cx="{lx + t}" cy="58" r="3.5" fill="#F2EEE6"/>')
    g.append(f'<path d="M92,-20 Q112,-8 106,18" fill="none" stroke="{DARK}" stroke-width="8" stroke-linecap="round"/>')  # tail
    g.append(f'<ellipse cx="10" cy="-20" rx="96" ry="64" fill="{G}" stroke="{DARK}" stroke-width="6"/>')
    # head (facing left), trunk, ear
    g.append(f'<path d="M-112,-6 Q-140,30 -126,60 Q-120,70 -110,62 Q-120,34 -96,8" fill="{G}" stroke="{DARK}" stroke-width="6" stroke-linejoin="round"/>')
    g.append(f'<circle cx="-86" cy="-40" r="50" fill="{G}" stroke="{DARK}" stroke-width="6"/>')
    g.append(f'<ellipse cx="-44" cy="-36" rx="38" ry="50" fill="{G2}" stroke="{DARK}" stroke-width="6"/>')
    g.append(f'<ellipse cx="-42" cy="-34" rx="24" ry="34" fill="#F2B8C0" opacity="0.8"/>')
    g.append(f'<path d="M-104,-6 Q-96,12 -82,8" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round"/>')  # tusk
    g.append(f'<ellipse cx="-100" cy="-50" rx="6" ry="8" fill="{DARK}"/><circle cx="-98" cy="-53" r="2.5" fill="#FFFFFF"/>')
    g.append(f'<ellipse cx="-80" cy="-28" rx="9" ry="5" fill="#F59A8C" opacity="0.7"/>')
    g.append('</g>')
    return "".join(g)


def tuft(x, y, s, color="#4E9E3C"):
    blades = [(-10, -26), (-3, -36), (5, -30), (12, -22)]
    return "".join(f'<path d="M{x + bx * 0.4 * s},{y} Q{x + bx * s},{y + by * 0.5 * s} {x + bx * 1.2 * s},{y + by * s}" fill="none" stroke="{DARK}" stroke-width="{7 * s}" stroke-linecap="round"/>'
                   f'<path d="M{x + bx * 0.4 * s},{y} Q{x + bx * s},{y + by * 0.5 * s} {x + bx * 1.2 * s},{y + by * s}" fill="none" stroke="{color}" stroke-width="{3.5 * s}" stroke-linecap="round"/>'
                   for bx, by in blades)


def flower(x, y, color):
    g = [f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + 18}" stroke="{DARK}" stroke-width="6"/><line x1="{x}" y1="{y}" x2="{x}" y2="{y + 18}" stroke="#4E9E3C" stroke-width="3"/>']
    for k in range(5):
        a = k / 5 * math.tau
        g.append(f'<circle cx="{x + math.cos(a) * 7:.1f}" cy="{y + math.sin(a) * 7:.1f}" r="6" fill="{color}" stroke="{DARK}" stroke-width="2.5"/>')
    g.append(f'<circle cx="{x}" cy="{y}" r="4.5" fill="#FFD84A" stroke="{DARK}" stroke-width="2"/>')
    return "".join(g)


# ---------------------------------------------------------------- the scene (0, 0, 1024, 576)
S.append('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4FAEEB"/><stop offset="1" stop-color="#C9EDFF"/></linearGradient>'
         '<radialGradient id="sun"><stop offset="0" stop-color="#FFF6C8"/><stop offset="0.5" stop-color="#FFE27A" stop-opacity="0.6"/><stop offset="1" stop-color="#FFE27A" stop-opacity="0"/></radialGradient>'
         '<clipPath id="scene"><rect x="0" y="0" width="1024" height="576"/></clipPath></defs>')
S.append('<g clip-path="url(#scene)">')
S.append('<rect width="1024" height="576" fill="url(#sky)"/>')
S.append('<circle cx="860" cy="96" r="140" fill="url(#sun)"/><circle cx="860" cy="96" r="46" fill="#FFF3B0" stroke="#F7C948" stroke-width="6"/>')
S.append(cloud(110, 90, 1.0) + cloud(420, 60, 0.75) + cloud(640, 130, 0.9))
S.append(hill("M-20,360 Q160,290 340,340 T700,320 T1044,330 L1044,600 L-20,600 Z", "#A6DC8C", outline=False))
S.append(acacia(210, 345, 0.7) + acacia(760, 330, 0.6) + round_tree(560, 340, 0.55, "#7CC85A", "#5DAA45"))
S.append(hill("M-20,420 Q180,350 380,400 T780,385 T1044,390 L1044,600 L-20,600 Z", "#7CCB5B"))
S.append(elephant(800, 408, 0.95))
S.append(acacia(950, 430, 0.85))
S.append(giraffe(190, 380, 0.92))
S.append(hill("M-20,488 Q220,440 520,470 T1044,462 L1044,600 L-20,600 Z", "#5DB24A"))
S.append(lion(120, 520, 62))
for tx, ty, ts in ((40, 560, 1.3), (230, 548, 1.1), (420, 540, 1.0), (620, 548, 1.2), (900, 556, 1.3), (990, 540, 1.0), (330, 566, 1.4), (720, 566, 1.3)):
    S.append(tuft(tx, ty, ts, "#3F8F3A"))
for fx, fy, c in ((280, 520, "#FF8FB1"), (500, 515, "#FFFFFF"), (690, 520, "#B48CFF"), (960, 515, "#FF8FB1"), (560, 540, "#FFD84A")):
    S.append(flower(fx, fy, c))
S.append('</g>')

# ---------------------------------------------------------------- the logo (0, 600, 1024, 400)
LY = 600


def ribbon(cx, y, width, h, fill):
    x0, x1 = cx - width / 2, cx + width / 2
    tail = 70
    s = []
    for side in (-1, 1):  # folded tails behind the banner
        ex = x0 if side < 0 else x1
        tx = ex + side * tail
        s.append(f'<path d="M{ex - side * 10},{y + 24} L{tx},{y + 24} L{tx - side * 26},{y + 24 + h / 2} L{tx},{y + 24 + h} L{ex - side * 10},{y + 24 + h} Z" fill="#B23A33" stroke="{DARK}" stroke-width="10" stroke-linejoin="round"/>')
    s.append(f'<path d="M{x0},{y} L{x1},{y} L{x1},{y + h} Q{cx},{y + h + 26} {x0},{y + h} Z" transform="translate(8 12)" fill="#000" opacity="0.22"/>')
    s.append(f'<path d="M{x0},{y} Q{cx},{y - 22} {x1},{y} L{x1},{y + h} Q{cx},{y + h - 22} {x0},{y + h} Z" fill="{fill}" stroke="{DARK}" stroke-width="12" stroke-linejoin="round"/>')
    s.append(f'<path d="M{x0 + 24},{y + 16} Q{cx},{y - 4} {x1 - 24},{y + 16}" fill="none" stroke="#FF8A7A" stroke-width="7" stroke-linecap="round" opacity="0.8"/>')
    return "".join(s)


L = []
L.append(outlined_text(W / 2, LY + 118, "BUILD YOUR", 120, "#FFD84A", sw=26))
L.append(outlined_text(W / 2, LY + 112, "BUILD YOUR", 120, "#FFE98A", sw=0) if False else "")
L.append(ribbon(W / 2, LY + 150, 780, 150, "#E24B4B"))
L.append(outlined_text(W / 2 - 2, LY + 268, "DREAM ZOO!", 132, "#FFFFFF", sw=26))
L.append(sparkle(108, LY + 70, 30) + sparkle(930, LY + 96, 24, "#FFF3B0") + sparkle(170, LY + 340, 18, "#FFF3B0") + sparkle(880, LY + 352, 26))

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">'
       f'{"".join(S)}{"".join(L)}</svg>')
cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT + "loading_art.png", output_width=1024, output_height=1024)

# crisp versions for the game: the scene at 2048x1152 split into two 1024-wide halves (Roblox keeps images
# up to 1024 px), and the logo on its own
from PIL import Image  # noqa: E402
scene_svg = svg.replace('viewBox="0 0 1024 1024"', 'viewBox="0 0 1024 576"').replace('width="1024" height="1024"', 'width="2048" height="1152"')
cairosvg.svg2png(bytestring=scene_svg.encode(), write_to=OUT + "scene_2x.png", output_width=2048, output_height=1152)
big = Image.open(OUT + "scene_2x.png")
big.crop((0, 0, 1024, 1152)).save(OUT + "scene_left.png")
big.crop((1024, 0, 2048, 1152)).save(OUT + "scene_right.png")
logo_svg = svg.replace('viewBox="0 0 1024 1024"', 'viewBox="0 600 1024 400"').replace('width="1024" height="1024"', 'width="1024" height="400"')
cairosvg.svg2png(bytestring=logo_svg.encode(), write_to=OUT + "logo.png", output_width=1024, output_height=400)
print("wrote loading_art.png, scene_left/right.png, logo.png")
