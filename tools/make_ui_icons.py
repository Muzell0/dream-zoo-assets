"""Icon sheet (1024x1024, 4x4 cells of 256) for Build Your Dream Zoo!: flat cartoon icons with dark outlines.
Cell order (row by row): Shop, Teleport, Index, Rewards, Codes, Settings, Build, Animals,
                          AutoCollect, Trophy, Ticket, Crate, Rebirth, Star, Lock, Home
Plus a tintable tile behind the menu buttons is drawn into the main sprite sheet's free space? No: the tile
lives in its own cell-free spot here would clash, so the tile is drawn by make_ui_atlas.py (Tile).
"""
import cairosvg

DARK = "#3C2D23"
OUT = "/tmp/claude-0/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/scratchpad/icons/"
SW = 10  # outline width at 256px
NAMES = ["Shop", "Teleport", "Index", "Rewards", "Codes", "Settings", "Build", "Animals",
         "AutoCollect", "Trophy", "Ticket", "Crate", "Rebirth", "Star", "Lock", "Home"]

DEFS = '''<defs>
<linearGradient id="gGold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE68A"/><stop offset="1" stop-color="#F4AE2C"/></linearGradient>
<linearGradient id="gRed" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF8577"/><stop offset="1" stop-color="#DB4B42"/></linearGradient>
<linearGradient id="gBlue" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8FD0FF"/><stop offset="1" stop-color="#4A9BE8"/></linearGradient>
<linearGradient id="gGreen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9BE37A"/><stop offset="1" stop-color="#4FAE4A"/></linearGradient>
<linearGradient id="gPurple" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C9A6FF"/><stop offset="1" stop-color="#8A5FD6"/></linearGradient>
<linearGradient id="gWood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E0A86A"/><stop offset="1" stop-color="#B57442"/></linearGradient>
<linearGradient id="gGrey" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D9DEE6"/><stop offset="1" stop-color="#9AA3B2"/></linearGradient>
<linearGradient id="gOrange" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFB27A"/><stop offset="1" stop-color="#FF7F4A"/></linearGradient>
<linearGradient id="gGlass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#CFEFFF"/><stop offset="1" stop-color="#9FD8F5"/></linearGradient>
</defs>'''


def st(w=SW):
    return f'stroke="{DARK}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"'


def shine(x, y, w, h, r=None):
    r = r if r is not None else h / 2
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="#FFFFFF" opacity="0.55"/>'


def shop():  # a shopping cart carrying a little crate
    return (f'<path d="M30,62 L64,62 L88,170 L200,170" fill="none" {st(14)}/>'
            f'<path d="M30,62 L64,62 L88,170 L200,170" fill="none" stroke="#8A97A8" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M70,82 L222,82 L204,152 L86,152 Z" fill="url(#gBlue)" {st()}/>'
            f'<path d="M104,92 L104,142 M140,92 L140,142 M176,92 L176,142" stroke="#2F6FB0" stroke-width="6" stroke-linecap="round"/>'
            f'<rect x="112" y="40" width="70" height="52" rx="6" fill="url(#gWood)" {st()}/>'
            f'<path d="M120,66 L174,66" stroke="#8A5530" stroke-width="5"/>'
            f'<circle cx="104" cy="204" r="20" fill="#5B5452" {st()}/><circle cx="104" cy="204" r="7" fill="#C9C1BC"/>'
            f'<circle cx="184" cy="204" r="20" fill="#5B5452" {st()}/><circle cx="184" cy="204" r="7" fill="#C9C1BC"/>')


def teleport():  # a signpost with two arrow boards
    return (f'<rect x="114" y="38" width="28" height="196" rx="8" fill="url(#gWood)" {st()}/>'
            f'<path d="M42,62 L178,62 L206,88 L178,114 L42,114 Z" fill="url(#gGreen)" {st()}/>'
            f'<path d="M214,130 L78,130 L50,156 L78,182 L214,182 Z" fill="url(#gOrange)" {st()}/>'
            + shine(54, 70, 110, 10) + shine(86, 138, 110, 10) +
            f'<circle cx="128" cy="40" r="12" fill="#FFD84A" {st(7)}/>'
            f'<path d="M84,236 Q128,214 172,236" fill="#6DBE4B" {st(8)}/>')


def index():  # a book with a paw on the cover
    return (f'<path d="M40,58 Q84,40 128,62 Q172,40 216,58 L216,206 Q172,190 128,210 Q84,190 40,206 Z" fill="#FFF6E2" {st()}/>'
            f'<path d="M48,50 Q86,30 128,52 L128,196 Q86,176 48,194 Z" fill="url(#gGreen)" {st()}/>'
            f'<path d="M128,52 Q170,30 208,50 L208,194 Q170,176 128,196 Z" fill="url(#gGreen)" {st()}/>'
            f'<line x1="128" y1="52" x2="128" y2="196" {st(8)}/>'
            + paw_shape(88, 118, 1.25, "#FFF6E2") +
            f'<path d="M150,90 L190,82 M150,114 L190,106 M150,138 L184,131" stroke="#FFF6E2" stroke-width="8" stroke-linecap="round" opacity="0.85"/>')


def paw_shape(cx, cy, s, fill):
    g = [f'<g transform="translate({cx} {cy}) scale({s})">', f'<ellipse cx="0" cy="10" rx="17" ry="14" fill="{fill}" {st(5 / s)}/>']
    for tx, ty in ((-19, -9), (-7, -20), (7, -20), (19, -9)):
        g.append(f'<ellipse cx="{tx}" cy="{ty}" rx="6.5" ry="8" fill="{fill}" {st(5 / s)}/>')
    g.append('</g>')
    return "".join(g)


def rewards():  # a gift box with a bow
    return (f'<rect x="40" y="112" width="176" height="110" rx="12" fill="url(#gRed)" {st()}/>'
            f'<rect x="30" y="82" width="196" height="44" rx="10" fill="url(#gRed)" {st()}/>'
            f'<rect x="110" y="82" width="36" height="140" fill="url(#gGold)" {st()}/>'
            f'<path d="M128,82 Q78,22 62,58 Q50,88 128,82 Z" fill="url(#gGold)" {st()}/>'
            f'<path d="M128,82 Q178,22 194,58 Q206,88 128,82 Z" fill="url(#gGold)" {st()}/>'
            f'<circle cx="128" cy="80" r="14" fill="#F4AE2C" {st(8)}/>' + shine(44, 90, 60, 10) + shine(52, 122, 46, 9))


def codes():  # a golden key: ring, straight shaft and teeth, all one rotated group
    return (f'<g transform="rotate(40 128 128)">'
            f'<rect x="112" y="40" width="34" height="170" rx="10" fill="url(#gGold)" {st()}/>'
            f'<path d="M146,160 L178,160 L178,178 L146,178 M146,190 L170,190 L170,206 L146,206" fill="url(#gGold)" {st()}/>'
            f'<circle cx="129" cy="62" r="50" fill="url(#gGold)" {st()}/>'
            f'<circle cx="129" cy="62" r="18" fill="#FFF6E2" {st(8)}/>'
            + shine(100, 30, 34, 12, 6) + '</g>'
            f'<path d="M48,34 L54,52 L72,58 L54,64 L48,82 L42,64 L24,58 L42,52 Z" fill="#FFFFFF" {st(5)}/>')


def settings():  # a gear
    import math
    teeth, r1, r2 = 9, 92, 72
    pts = []
    for i in range(teeth * 2):
        a = i / (teeth * 2) * math.tau
        r = r1 if i % 2 == 0 else r2
        for da in (-0.12, 0.12):
            pts.append(f"{128 + math.cos(a + da) * r:.1f},{128 + math.sin(a + da) * r:.1f}")
    return (f'<polygon points="{" ".join(pts)}" fill="url(#gGrey)" {st()}/>'
            f'<circle cx="128" cy="128" r="34" fill="#5B6472" {st()}/>'
            f'<circle cx="128" cy="128" r="14" fill="#C9D0DA"/>'
            f'<path d="M86,78 Q106,60 134,58" stroke="#FFFFFF" stroke-width="9" stroke-linecap="round" opacity="0.7" fill="none"/>')


def build():  # a hammer crossed with a little plank
    return (f'<rect x="40" y="168" width="150" height="34" rx="8" fill="url(#gWood)" {st()} transform="rotate(-14 115 185)"/>'
            f'<rect x="112" y="80" width="30" height="150" rx="10" fill="url(#gWood)" {st()} transform="rotate(38 127 155)"/>'
            f'<path d="M72,56 L156,30 Q178,24 184,46 L196,86 Q200,104 182,108 L98,134 Z" fill="url(#gGrey)" {st()} transform="rotate(8 134 82)"/>'
            f'<path d="M92,62 L160,42" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity="0.7"/>')


def animals():  # a paw print in a badge
    return (f'<circle cx="128" cy="128" r="100" fill="url(#gOrange)" {st()}/>'
            f'<circle cx="128" cy="128" r="80" fill="none" stroke="#FFD2B0" stroke-width="6" opacity="0.8"/>'
            + paw_shape(128, 136, 2.6, "#FFF6E2") + shine(76, 46, 70, 14))


def auto_collect():  # a ticket jar with tickets inside
    return (f'<rect x="58" y="60" width="140" height="170" rx="34" fill="url(#gGlass)" {st()}/>'
            f'<path d="M66,140 L190,140 L190,196 Q190,222 164,222 L92,222 Q66,222 66,196 Z" fill="url(#gOrange)"/>'
            f'<rect x="88" y="150" width="46" height="26" rx="5" fill="#FFB27A" {st(5)} transform="rotate(-14 111 163)"/>'
            f'<rect x="128" y="168" width="46" height="26" rx="5" fill="#FFB27A" {st(5)} transform="rotate(12 151 181)"/>'
            f'<rect x="58" y="60" width="140" height="170" rx="34" fill="none" {st()}/>'
            f'<rect x="46" y="34" width="164" height="38" rx="12" fill="url(#gGold)" {st()}/>'
            + shine(76, 84, 16, 80, 8))


def trophy():
    return (f'<path d="M70,44 L186,44 L178,120 Q170,160 128,164 Q86,160 78,120 Z" fill="url(#gGold)" {st()}/>'
            f'<path d="M72,64 Q30,64 38,100 Q46,132 84,132" fill="none" {st(12)}/><path d="M184,64 Q226,64 218,100 Q210,132 172,132" fill="none" {st(12)}/>'
            f'<path d="M72,64 Q30,64 38,100 Q46,132 84,132" fill="none" stroke="#F4AE2C" stroke-width="5"/><path d="M184,64 Q226,64 218,100 Q210,132 172,132" fill="none" stroke="#F4AE2C" stroke-width="5"/>'
            f'<rect x="112" y="160" width="32" height="30" fill="url(#gGold)" {st()}/>'
            f'<rect x="76" y="186" width="104" height="34" rx="8" fill="url(#gWood)" {st()}/>'
            f'<path d="M128,72 L136,92 L156,94 L140,106 L146,126 L128,114 L110,126 L116,106 L100,94 L120,92 Z" fill="#FFF3B0" {st(5)}/>'
            + shine(84, 52, 20, 50, 10))


def ticket():
    return (f'<g transform="rotate(-14 128 128)"><path d="M30,78 L226,78 L226,108 Q206,128 226,148 L226,178 L30,178 L30,148 Q50,128 30,108 Z" fill="url(#gOrange)" {st()}/>'
            f'<line x1="88" y1="90" x2="88" y2="166" stroke="#FFE3D0" stroke-width="7" stroke-dasharray="10 9"/>'
            f'<path d="M150,104 L158,122 L178,124 L162,136 L168,156 L150,144 L132,156 L138,136 L122,124 L142,122 Z" fill="#FFF3B0" {st(5)}/>'
            + shine(44, 88, 120, 10) + '</g>')


def crate():  # a wooden crate with planks and a big question mark
    return (f'<rect x="44" y="52" width="168" height="160" rx="14" fill="url(#gWood)" {st()}/>'
            f'<path d="M58,104 L198,104 M58,160 L198,160" stroke="#8A5530" stroke-width="7" opacity="0.7"/>'
            f'<rect x="44" y="52" width="168" height="160" rx="14" fill="none" stroke="#8A5530" stroke-width="18" opacity="0.6"/>'
            f'<rect x="44" y="52" width="168" height="160" rx="14" fill="none" {st()}/>'
            f'<text x="128" y="168" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="120" fill="#FFF6E2" stroke="{DARK}" stroke-width="11" paint-order="stroke">?</text>')


def rebirth():  # two curved arrows around a star
    return (f'<path d="M58,128 A70,70 0 0 1 182,84" fill="none" {st(30)}/><path d="M58,128 A70,70 0 0 1 182,84" fill="none" stroke="#B88CFF" stroke-width="16" stroke-linecap="round"/>'
            f'<path d="M198,128 A70,70 0 0 1 74,172" fill="none" {st(30)}/><path d="M198,128 A70,70 0 0 1 74,172" fill="none" stroke="#B88CFF" stroke-width="16" stroke-linecap="round"/>'
            f'<path d="M168,52 L212,82 L164,108 Z" fill="#B88CFF" {st(8)}/><path d="M88,204 L44,174 L92,148 Z" fill="#B88CFF" {st(8)}/>'
            f'<path d="M128,92 L138,116 L164,118 L144,134 L150,160 L128,146 L106,160 L112,134 L92,118 L118,116 Z" fill="url(#gGold)" {st(6)}/>')


def star():
    return (f'<path d="M128,28 L156,92 L226,98 L172,144 L188,214 L128,178 L68,214 L84,144 L30,98 L100,92 Z" fill="url(#gGold)" {st()}/>'
            + shine(96, 96, 40, 14))


def lock():
    return (f'<path d="M80,116 L80,84 Q80,36 128,36 Q176,36 176,84 L176,116" fill="none" {st(32)}/>'
            f'<path d="M80,116 L80,84 Q80,36 128,36 Q176,36 176,84 L176,116" fill="none" stroke="#B8C0CC" stroke-width="16"/>'
            f'<rect x="52" y="110" width="152" height="120" rx="20" fill="url(#gGold)" {st()}/>'
            f'<circle cx="128" cy="160" r="16" fill="{DARK}"/><rect x="121" y="166" width="14" height="32" rx="6" fill="{DARK}"/>'
            + shine(66, 122, 70, 12))


def home():  # a little zoo house with a green roof
    return (f'<rect x="56" y="112" width="144" height="110" rx="8" fill="#FFF6E2" {st()}/>'
            f'<path d="M34,124 L128,40 L222,124 Z" fill="url(#gGreen)" {st()}/>'
            f'<rect x="108" y="150" width="40" height="72" rx="8" fill="url(#gWood)" {st()}/>'
            f'<rect x="70" y="138" width="28" height="28" rx="4" fill="url(#gGlass)" {st(6)}/>'
            f'<rect x="158" y="138" width="28" height="28" rx="4" fill="url(#gGlass)" {st(6)}/>'
            + paw_shape(128, 98, 0.8, "#FFF6E2"))


DRAW = [shop, teleport, index, rewards, codes, settings, build, animals, auto_collect, trophy, ticket, crate, rebirth, star, lock, home]
cells = []
for i, fn in enumerate(DRAW):
    x, y = (i % 4) * 256, (i // 4) * 256
    cells.append(f'<g transform="translate({x} {y})">{fn()}</g>')
svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">{DEFS}{"".join(cells)}</svg>'
cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT + "ui_icons.png", output_width=1024, output_height=1024)
print("UI.Icons = { " + ", ".join(f"{n} = {{ {(i % 4) * 256}, {(i // 4) * 256} }}" for i, n in enumerate(NAMES)) + " } -- 256x256 cells")
