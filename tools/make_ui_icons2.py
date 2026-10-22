"""Second icon sheet (1024x1024, 4x4 cells of 256), same flat cartoon style as make_ui_icons.py.
Cell order (row by row): Gem, Research, Friends, Gift, News, Stats, Calendar, Hex,
                          Question, Medal, BadgeFirstCrate, BadgeCrateCrazy, BadgeMillionaire,
                          BadgeLegendary, BadgeFirstRebirth, BadgeSavanna
Hex is drawn white so the game can tint it (ImageColor3) behind Research nodes.
The six badge cells are the badges/ art scaled down, so the in-game gallery matches the real badges.
"""
import base64
import io
import sys

import cairosvg
from PIL import Image

sys.path.insert(0, "/home/claude/dream-zoo-assets/tools")
from make_ui_icons import DARK, DEFS, paw_shape, shine, st  # noqa: E402

OUT = "/home/claude/dream-zoo-assets/ui/icons2.png"
BADGES = "/home/claude/dream-zoo-assets/badges/"


def gem():
    return (f'<path d="M68,70 L188,70 L224,112 L128,214 L32,112 Z" fill="url(#gPurple)" {st()}/>'
            f'<path d="M32,112 L224,112 M68,70 L100,112 L128,214 L156,112 L188,70 M100,112 L128,70 L156,112" fill="none" stroke="{DARK}" stroke-width="6" stroke-linejoin="round"/>'
            f'<path d="M78,80 L96,104 L54,104 Z" fill="#FFFFFF" opacity="0.6"/>'
            f'<path d="M128,80 L146,104 L110,104 Z" fill="#FFFFFF" opacity="0.35"/>')


def research():  # a round flask with bubbles
    return (f'<path d="M104,40 L152,40 L152,92 Q214,118 210,170 Q206,224 128,226 Q50,224 46,170 Q42,118 104,92 Z" fill="#E9F7FF" {st()}/>'
            f'<path d="M56,160 Q128,140 200,160 Q200,216 128,218 Q56,216 56,160 Z" fill="url(#gGreen)"/>'
            f'<path d="M104,40 L152,40 L152,92 Q214,118 210,170 Q206,224 128,226 Q50,224 46,170 Q42,118 104,92 Z" fill="none" {st()}/>'
            f'<rect x="94" y="30" width="68" height="20" rx="8" fill="url(#gWood)" {st(8)}/>'
            f'<circle cx="104" cy="178" r="11" fill="#FFFFFF" opacity="0.8"/><circle cx="144" cy="192" r="8" fill="#FFFFFF" opacity="0.8"/>'
            f'<circle cx="128" cy="120" r="7" fill="#9BE37A" {st(4)}/><circle cx="150" cy="100" r="5" fill="#9BE37A" {st(3)}/>'
            + shine(70, 116, 30, 10))


def person(cx, cy, s, fill):
    return (f'<g transform="translate({cx} {cy}) scale({s})">'
            f'<path d="M-46,70 Q-46,10 0,10 Q46,10 46,70 Z" fill="{fill}" {st(10 / s)}/>'
            f'<circle cx="0" cy="-24" r="30" fill="#FFD7A8" {st(10 / s)}/></g>')


def friends():  # two buddies and a plus
    return (person(92, 118, 1.0, "url(#gBlue)") + person(158, 128, 1.05, "url(#gGreen)")
            + f'<circle cx="206" cy="62" r="30" fill="url(#gGold)" {st(8)}/>'
            + f'<path d="M206,46 L206,78 M190,62 L222,62" stroke="{DARK}" stroke-width="9" stroke-linecap="round"/>')


def gift():  # a purple gift with a gold bow (Gift button)
    return (f'<rect x="44" y="114" width="168" height="106" rx="12" fill="url(#gPurple)" {st()}/>'
            f'<rect x="34" y="84" width="188" height="42" rx="10" fill="url(#gPurple)" {st()}/>'
            f'<rect x="110" y="84" width="36" height="136" fill="url(#gGold)" {st()}/>'
            f'<path d="M128,84 Q80,26 64,60 Q52,88 128,84 Z" fill="url(#gGold)" {st()}/>'
            f'<path d="M128,84 Q176,26 192,60 Q204,88 128,84 Z" fill="url(#gGold)" {st()}/>'
            + shine(48, 92, 56, 9))


def news():  # a scroll with lines and a red ribbon
    return (f'<rect x="58" y="44" width="150" height="176" rx="10" fill="#FFF6E2" {st()}/>'
            f'<rect x="44" y="34" width="168" height="30" rx="15" fill="url(#gWood)" {st()}/>'
            f'<rect x="44" y="200" width="168" height="30" rx="15" fill="url(#gWood)" {st()}/>'
            f'<path d="M82,92 L184,92 M82,120 L184,120 M82,148 L160,148 M82,176 L172,176" stroke="#B9967A" stroke-width="9" stroke-linecap="round"/>'
            f'<path d="M176,140 L214,140 L226,170 L196,162 L180,186 Z" fill="url(#gRed)" {st(7)}/>'
            f'<circle cx="196" cy="140" r="22" fill="url(#gRed)" {st(8)}/><path d="M188,140 L194,148 L206,132" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>')


def stats():  # a bar chart on a board
    return (f'<rect x="34" y="40" width="188" height="170" rx="14" fill="#FFF6E2" {st()}/>'
            f'<rect x="62" y="134" width="30" height="54" rx="5" fill="url(#gRed)" {st(7)}/>'
            f'<rect x="112" y="100" width="30" height="88" rx="5" fill="url(#gGold)" {st(7)}/>'
            f'<rect x="162" y="64" width="30" height="124" rx="5" fill="url(#gGreen)" {st(7)}/>'
            f'<path d="M54,188 L204,188" stroke="{DARK}" stroke-width="7" stroke-linecap="round"/>')


def calendar():
    return (f'<rect x="40" y="58" width="176" height="160" rx="16" fill="#FFF6E2" {st()}/>'
            f'<path d="M40,74 Q40,58 56,58 L200,58 Q216,58 216,74 L216,104 L40,104 Z" fill="url(#gRed)" {st()}/>'
            f'<rect x="78" y="38" width="16" height="40" rx="8" fill="#8A97A8" {st(6)}/><rect x="162" y="38" width="16" height="40" rx="8" fill="#8A97A8" {st(6)}/>'
            + "".join(f'<rect x="{66 + c * 44}" y="{122 + r * 40}" width="30" height="26" rx="5" fill="{"url(#gGold)" if (r, c) == (1, 2) else "#E4D6C2"}"/>'
                      for r in range(2) for c in range(3)))


def hex_tile():  # white, tinted in game
    import math
    pts = " ".join(f"{128 + 110 * math.cos(math.radians(60 * i + 30)):.1f},{128 + 110 * math.sin(math.radians(60 * i + 30)):.1f}" for i in range(6))
    inner = " ".join(f"{128 + 92 * math.cos(math.radians(60 * i + 30)):.1f},{128 + 92 * math.sin(math.radians(60 * i + 30)):.1f}" for i in range(6))
    return (f'<polygon points="{pts}" fill="#FFFFFF" stroke="#3C2D23" stroke-width="12" stroke-linejoin="round"/>'
            f'<polygon points="{inner}" fill="none" stroke="#000000" stroke-opacity="0.12" stroke-width="8"/>')


def question():  # a dark medallion with a question mark (locked badge)
    return (f'<circle cx="128" cy="128" r="104" fill="#4A4250" {st()}/>'
            f'<circle cx="128" cy="128" r="80" fill="#5E5566"/>'
            f'<text x="128" y="170" font-family="Arial Rounded MT Bold, Arial" font-weight="bold" font-size="130" text-anchor="middle" fill="#E9E1F0" stroke="{DARK}" stroke-width="8" paint-order="stroke">?</text>')


def medal():
    return (f'<path d="M84,30 L112,110 L144,110 L172,30 L140,30 L128,70 L116,30 Z" fill="url(#gRed)" {st(8)}/>'
            f'<circle cx="128" cy="160" r="70" fill="url(#gGold)" {st()}/>'
            f'<circle cx="128" cy="160" r="48" fill="none" stroke="#C98A1E" stroke-width="7"/>'
            + paw_shape(128, 162, 1.0, "#FFF6E2"))


def badge_image(name):
    im = Image.open(BADGES + name + ".png").convert("RGBA").resize((240, 240), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG")
    href = "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
    return lambda: f'<image href="{href}" x="8" y="8" width="240" height="240"/>'


DRAW = [gem, research, friends, gift, news, stats, calendar, hex_tile, question, medal,
        badge_image("first_crate"), badge_image("crate_crazy"), badge_image("millionaire"),
        badge_image("legendary"), badge_image("first_rebirth"), badge_image("savanna")]
NAMES = ["Gem", "Research", "Friends", "Gift", "News", "Stats", "Calendar", "Hex", "Question", "Medal",
         "BadgeFirstCrate", "BadgeCrateCrazy", "BadgeMillionaire", "BadgeLegendary", "BadgeFirstRebirth", "BadgeSavanna"]
cells = []
for i, fn in enumerate(DRAW):
    x, y = (i % 4) * 256, (i // 4) * 256
    cells.append(f'<g transform="translate({x} {y})">{fn()}</g>')
svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">{DEFS}{"".join(cells)}</svg>'
cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT, output_width=1024, output_height=1024)
print("UI.Icons2 = { " + ", ".join(f"{n} = {{ {(i % 4) * 256}, {(i // 4) * 256} }}" for i, n in enumerate(NAMES)) + " }")
