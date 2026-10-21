"""Game icon for Build Your Dream Zoo! (512x512)."""
import math
import sys

import cairosvg

sys.path.insert(0, "/tmp/claude-0/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/scratchpad/icons")
from make_icons import DARK, OUT, outlined_text, rays, sparkle  # noqa: E402

GOLD = "#F5B83D"
MANE = "#E0892E"
MANE_DARK = "#C46A1E"
FACE = "#FFD27A"
MUZZLE = "#FFF3DA"


def lion(cx, cy, r):
    s = []
    # mane: a ring of overlapping puffs
    for i in range(14):
        a = i / 14 * 2 * math.pi
        px, py = cx + math.cos(a) * r * 0.92, cy + math.sin(a) * r * 0.92
        s.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r * 0.36:.1f}" fill="{MANE_DARK if i % 2 else MANE}" stroke="{DARK}" stroke-width="10"/>')
    s.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 1.02:.1f}" fill="{MANE}"/>')
    # ears
    for sx in (-1, 1):
        ex, ey = cx + sx * r * 0.62, cy - r * 0.62
        s.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="{r * 0.24:.1f}" fill="{FACE}" stroke="{DARK}" stroke-width="10"/>')
        s.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="{r * 0.12:.1f}" fill="#F2A3A0"/>')
    # face
    s.append(f'<ellipse cx="{cx}" cy="{cy + r * 0.06:.1f}" rx="{r * 0.78:.1f}" ry="{r * 0.74:.1f}" fill="{FACE}" stroke="{DARK}" stroke-width="10"/>')
    # eyes with highlights
    for sx in (-1, 1):
        ex, ey = cx + sx * r * 0.3, cy - r * 0.08
        s.append(f'<ellipse cx="{ex:.1f}" cy="{ey:.1f}" rx="{r * 0.1:.1f}" ry="{r * 0.14:.1f}" fill="{DARK}"/>')
        s.append(f'<circle cx="{ex + r * 0.035:.1f}" cy="{ey - r * 0.05:.1f}" r="{r * 0.045:.1f}" fill="#FFFFFF"/>')
        # rosy cheeks
        s.append(f'<ellipse cx="{cx + sx * r * 0.52:.1f}" cy="{cy + r * 0.2:.1f}" rx="{r * 0.12:.1f}" ry="{r * 0.07:.1f}" fill="#F59A8C" opacity="0.8"/>')
    # muzzle
    for sx in (-1, 1):
        s.append(f'<ellipse cx="{cx + sx * r * 0.15:.1f}" cy="{cy + r * 0.3:.1f}" rx="{r * 0.2:.1f}" ry="{r * 0.16:.1f}" fill="{MUZZLE}" stroke="{DARK}" stroke-width="6"/>')
    # nose + smile
    nx, ny = cx, cy + r * 0.17
    s.append(f'<path d="M{nx - r * 0.13:.1f},{ny - r * 0.05:.1f} Q{nx},{ny - r * 0.1:.1f} {nx + r * 0.13:.1f},{ny - r * 0.05:.1f} '
             f'Q{nx + r * 0.08:.1f},{ny + r * 0.1:.1f} {nx},{ny + r * 0.12:.1f} Q{nx - r * 0.08:.1f},{ny + r * 0.1:.1f} {nx - r * 0.13:.1f},{ny - r * 0.05:.1f} Z" '
             f'fill="#8A4A3A" stroke="{DARK}" stroke-width="6" stroke-linejoin="round"/>')
    s.append(f'<path d="M{cx - r * 0.2:.1f},{cy + r * 0.45:.1f} Q{cx},{cy + r * 0.6:.1f} {cx + r * 0.2:.1f},{cy + r * 0.45:.1f}" '
             f'fill="none" stroke="{DARK}" stroke-width="7" stroke-linecap="round"/>')
    return "\n".join(s)


def giraffe(x, y, scale):
    """Neck rising from the bottom edge to a head at (x, y)."""
    yellow, spot = "#FFCB4A", "#C9822E"
    k = scale
    s = [f'<g transform="translate({x} {y}) scale({k}) rotate(-8)">']
    # neck
    s.append(f'<path d="M-30,30 L30,30 L48,330 L-48,330 Z" fill="{yellow}" stroke="{DARK}" stroke-width="10" stroke-linejoin="round"/>')
    for sx, sy, sr in ((-14, 80, 14), (16, 130, 12), (-10, 190, 15), (20, 250, 13), (-18, 290, 11)):
        s.append(f'<ellipse cx="{sx}" cy="{sy}" rx="{sr}" ry="{sr * 0.8}" fill="{spot}"/>')
    # ossicones
    for sx in (-20, 20):
        s.append(f'<line x1="{sx}" y1="-30" x2="{sx * 1.2}" y2="-70" stroke="{DARK}" stroke-width="18" stroke-linecap="round"/>')
        s.append(f'<line x1="{sx}" y1="-30" x2="{sx * 1.2}" y2="-70" stroke="{yellow}" stroke-width="8" stroke-linecap="round"/>')
        s.append(f'<circle cx="{sx * 1.2}" cy="-74" r="11" fill="{spot}" stroke="{DARK}" stroke-width="7"/>')
    # ears
    for sx in (-1, 1):
        s.append(f'<ellipse cx="{sx * 52}" cy="-12" rx="24" ry="12" transform="rotate({sx * 25} {sx * 52} -12)" fill="{yellow}" stroke="{DARK}" stroke-width="8"/>')
    # head
    s.append(f'<ellipse cx="0" cy="0" rx="46" ry="52" fill="{yellow}" stroke="{DARK}" stroke-width="10"/>')
    s.append(f'<ellipse cx="0" cy="32" rx="34" ry="24" fill="#FFE7A8" stroke="{DARK}" stroke-width="7"/>')
    for sx in (-1, 1):
        s.append(f'<ellipse cx="{sx * 18}" cy="-10" rx="7" ry="10" fill="{DARK}"/>')
        s.append(f'<circle cx="{sx * 18 + 2.5}" cy="-14" r="3.2" fill="#FFFFFF"/>')
        s.append(f'<circle cx="{sx * 11}" cy="32" r="4" fill="{DARK}"/>')
    s.append("</g>")
    return "\n".join(s)


def hills():
    return (
        '<path d="M-20,360 Q120,300 260,345 T540,330 L540,540 L-20,540 Z" fill="#7CCB5B" stroke="#3C2D23" stroke-width="10"/>'
        '<path d="M-20,400 Q160,350 330,395 T540,385 L540,540 L-20,540 Z" fill="#5DB24A"/>'
    )


def acacia(x, y, s):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-4,0 L4,0 L6,-60 L22,-88 L16,-92 L2,-70 L-12,-94 L-18,-90 L-4,-60 Z" fill="#7A4B2A"/>'
            f'<ellipse cx="0" cy="-98" rx="60" ry="14" fill="#5E8F3A"/>'
            f'<ellipse cx="-14" cy="-108" rx="38" ry="12" fill="#6FA247"/></g>')


banner = (
    f'<path d="M30,392 L482,392 L460,438 L482,484 L30,484 L52,438 Z" fill="#E24B4B" stroke="{DARK}" stroke-width="12" stroke-linejoin="round"/>'
    + outlined_text(256, 458, "DREAM ZOO!", 66, "#FFFFFF", sw=14)
)
top_text = outlined_text(256, 78, "BUILD YOUR", 50, "#FFD84A", sw=12)

inner = "\n".join([
    acacia(80, 345, 0.9),
    acacia(440, 330, 0.7),
    hills(),
    giraffe(392, 168, 0.95),
    lion(220, 236, 112),
    sparkle(70, 150, 22), sparkle(460, 70, 16, "#FFF3B0"), sparkle(120, 330, 12, "#FFF3B0"),
    top_text,
    banner,
])

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#5CB8F2"/><stop offset="100%" stop-color="#BFE8FF"/>
  </linearGradient>
  <clipPath id="clip"><rect x="0" y="0" width="512" height="512" rx="96"/></clipPath>
</defs>
<g clip-path="url(#clip)">
  <rect width="512" height="512" fill="url(#sky)"/>
  {rays(256, 220, 18, 560, "#FFFFFF", 0.16)}
  {inner}
</g>
<rect x="8" y="8" width="496" height="496" rx="90" fill="none" stroke="{DARK}" stroke-width="16"/>
</svg>'''

open(OUT + "game_icon.svg", "w").write(svg)
cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT + "game_icon.png", output_width=512, output_height=512)
print("wrote game_icon.png")
