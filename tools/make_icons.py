import math
import cairosvg

DARK = "#3C2D23"
OUT = "./"


def rays(cx, cy, n, r, color, opacity):
    parts = []
    for i in range(n):
        a0 = (i / n) * 2 * math.pi
        a1 = a0 + math.pi / n
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        parts.append(f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} L{x1:.1f},{y1:.1f} Z" fill="{color}" opacity="{opacity}"/>')
    return "\n".join(parts)


def outlined_text(x, y, text, size, fill, stroke=DARK, sw=14, anchor="middle", rotate=0):
    tr = f' transform="rotate({rotate} {x} {y})"' if rotate else ""
    common = f'x="{x}" y="{y}" font-family="Fredoka" font-weight="700" font-size="{size}" text-anchor="{anchor}"{tr}'
    return (f'<text {common} fill="{stroke}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round">{text}</text>'
            f'<text {common} fill="{fill}">{text}</text>')


def sparkle(x, y, s, color="#FFFFFF"):
    return (f'<path d="M{x},{y - s} Q{x + s * 0.18},{y - s * 0.18} {x + s},{y} Q{x + s * 0.18},{y + s * 0.18} {x},{y + s} '
            f'Q{x - s * 0.18},{y + s * 0.18} {x - s},{y} Q{x - s * 0.18},{y - s * 0.18} {x},{y - s} Z" fill="{color}"/>')


def crate(x, y, w, color="#D29A5C", plank="#B47A3E", edge="#8A5530", label=None, tilt=0):
    """A chunky wooden crate, top-left at (x, y)."""
    cx, cy = x + w / 2, y + w / 2
    t = w * 0.12
    s = [f'<g transform="rotate({tilt} {cx} {cy})">']
    # shadow
    s.append(f'<rect x="{x + 6}" y="{y + 10}" width="{w}" height="{w}" rx="{w * 0.08}" fill="#000" opacity="0.18"/>')
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{w}" rx="{w * 0.08}" fill="{color}" stroke="{DARK}" stroke-width="9"/>')
    # planks
    for k in (1, 2):
        py = y + w * k / 3
        s.append(f'<line x1="{x + t}" y1="{py}" x2="{x + w - t}" y2="{py}" stroke="{plank}" stroke-width="6"/>')
    # frame
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{w}" rx="{w * 0.08}" fill="none" stroke="{edge}" stroke-width="{t}" opacity="0.85"/>')
    s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{w}" rx="{w * 0.08}" fill="none" stroke="{DARK}" stroke-width="9"/>')
    # diagonal brace
    s.append(f'<line x1="{x + t}" y1="{y + w - t}" x2="{x + w - t}" y2="{y + t}" stroke="{edge}" stroke-width="{t * 0.7}" stroke-linecap="round"/>')
    if label:
        s.append(outlined_text(cx, cy + w * 0.17, label, w * 0.5, "#FFFFFF", sw=w * 0.07))
    s.append("</g>")
    return "\n".join(s)


def frame(inner, bg_a, bg_b, ray_color):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<defs>
  <radialGradient id="bg" cx="50%" cy="42%" r="70%">
    <stop offset="0%" stop-color="{bg_a}"/><stop offset="100%" stop-color="{bg_b}"/>
  </radialGradient>
  <clipPath id="clip"><rect x="0" y="0" width="512" height="512" rx="96"/></clipPath>
</defs>
<g clip-path="url(#clip)">
  <rect width="512" height="512" fill="url(#bg)"/>
  {rays(256, 230, 16, 520, ray_color, 0.18)}
  {inner}
</g>
<rect x="8" y="8" width="496" height="496" rx="90" fill="none" stroke="{DARK}" stroke-width="16"/>
</svg>'''


# ---------------------------------------------------------------- Multi Open
multi = "\n".join([
    crate(46, 150, 170, color="#C98E55", tilt=-10),
    crate(296, 150, 170, color="#C98E55", tilt=10),
    crate(141, 182, 230, color="#E0A865", label="?"),
    # burst + badge
    f'<circle cx="398" cy="118" r="78" fill="#E24B4B" stroke="{DARK}" stroke-width="12"/>',
    f'<circle cx="398" cy="118" r="62" fill="none" stroke="#FF8A7A" stroke-width="6" opacity="0.7"/>',
    outlined_text(398, 146, "x5", 82, "#FFFFFF", sw=14),
    sparkle(92, 92, 26), sparkle(150, 60, 14, "#FFF3B0"), sparkle(470, 300, 18, "#FFF3B0"),
    # banner
    f'<path d="M48,404 L464,404 L444,446 L464,488 L48,488 L68,446 Z" fill="#6E4FB0" stroke="{DARK}" stroke-width="12" stroke-linejoin="round"/>',
    outlined_text(256, 466, "MULTI OPEN", 52, "#FFD84A", sw=12),
])

# ---------------------------------------------------------------- Auto Collect
def ticket(x, y, angle, s=1.0):
    w, h = 72 * s, 44 * s
    return (f'<g transform="rotate({angle} {x} {y})">'
            f'<rect x="{x - w / 2}" y="{y - h / 2}" width="{w}" height="{h}" rx="{8 * s}" fill="#FF8A5C" stroke="{DARK}" stroke-width="{7 * s}"/>'
            f'<line x1="{x - w * 0.18}" y1="{y - h * 0.32}" x2="{x - w * 0.18}" y2="{y + h * 0.32}" stroke="#FFD9C4" stroke-width="{4 * s}" stroke-dasharray="{5 * s} {4 * s}"/>'
            f'<circle cx="{x + w * 0.16}" cy="{y}" r="{7 * s}" fill="#FFD9C4"/></g>')

jar_x, jar_y, jar_w, jar_h = 150, 150, 212, 250
auto = "\n".join([
    # curved "auto" arrows going around the jar
    f'<path d="M101.8,339.0 A178,178 0 0 1 105.0,155.7" fill="none" stroke="{DARK}" stroke-width="34" stroke-linecap="round"/>',
    f'<path d="M101.8,339.0 A178,178 0 0 1 105.0,155.7" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round"/>',
    f'<path d="M123.1,126.8 L127.1,169.5 L83.0,141.9 Z" fill="#FFFFFF" stroke="{DARK}" stroke-width="10" stroke-linejoin="round"/>',
    f'<path d="M410.2,161.0 A178,178 0 0 1 407.0,344.3" fill="none" stroke="{DARK}" stroke-width="34" stroke-linecap="round"/>',
    f'<path d="M410.2,161.0 A178,178 0 0 1 407.0,344.3" fill="none" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round"/>',
    f'<path d="M388.9,373.2 L384.9,330.5 L429.0,358.1 Z" fill="#FFFFFF" stroke="{DARK}" stroke-width="10" stroke-linejoin="round"/>',
    # jar body (glass) + tickets inside
    f'<rect x="{jar_x + 6}" y="{jar_y + 14}" width="{jar_w}" height="{jar_h}" rx="46" fill="#000" opacity="0.18"/>',
    f'<rect x="{jar_x}" y="{jar_y}" width="{jar_w}" height="{jar_h}" rx="46" fill="#DDF3FF" stroke="{DARK}" stroke-width="12"/>',
    f'<clipPath id="jarclip"><rect x="{jar_x + 8}" y="{jar_y + 8}" width="{jar_w - 16}" height="{jar_h - 16}" rx="40"/></clipPath>',
    '<g clip-path="url(#jarclip)">',
    f'<rect x="{jar_x}" y="{jar_y + 92}" width="{jar_w}" height="{jar_h}" fill="#FFB38A"/>',
    ticket(206, 262, -18, 0.9), ticket(300, 268, 14, 0.9), ticket(252, 314, 6, 0.95), ticket(196, 356, 20, 0.9),
    ticket(306, 352, -12, 0.9), ticket(252, 384, -4, 0.9),
    '</g>',
    # glass shine
    f'<rect x="{jar_x + 26}" y="{jar_y + 30}" width="22" height="150" rx="11" fill="#FFFFFF" opacity="0.75"/>',
    # lid
    f'<rect x="{jar_x - 14}" y="{jar_y - 34}" width="{jar_w + 28}" height="50" rx="16" fill="#FFCD45" stroke="{DARK}" stroke-width="12"/>',
    f'<rect x="{jar_x + 6}" y="{jar_y - 24}" width="{jar_w - 12}" height="12" rx="6" fill="#FFE79A"/>',
    # a ticket flying in
    ticket(372, 108, 24, 1.15),
    sparkle(452, 70, 20), sparkle(78, 420, 16, "#FFF3B0"), sparkle(110, 140, 12, "#FFF3B0"),
    # banner
    f'<path d="M48,404 L464,404 L444,446 L464,488 L48,488 L68,446 Z" fill="#E24B4B" stroke="{DARK}" stroke-width="12" stroke-linejoin="round"/>',
    outlined_text(256, 466, "AUTO COLLECT", 48, "#FFFFFF", sw=12),
])

for name, inner, a, b, rc in [
    ("multi_open", multi, "#FFE27A", "#F2A43A", "#FFFFFF"),
    ("auto_collect", auto, "#9BE38A", "#3FA46A", "#FFFFFF"),
]:
    svg = frame(inner, a, b, rc)
    open(OUT + name + ".svg", "w").write(svg)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT + name + ".png", output_width=512, output_height=512)
    print("wrote", name)
