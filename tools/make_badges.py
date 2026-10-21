"""Badge icons (512x512, Roblox shows them in a circle): a carved-wood medallion with a coloured,
sun-rayed centre, one of the drawn UI icons (or a little savanna scene), and a ribbon with the name."""
import base64, io, sys
import cairosvg
from PIL import Image
sys.path.insert(0, "/tmp/claude-0/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/scratchpad/icons")
from make_icons import DARK, outlined_text, rays, sparkle  # noqa: E402
import make_game_icon as v1  # noqa: E402

ICONS = Image.open("/home/claude/dream-zoo-assets/ui/icons.png").convert("RGBA")
CELLS = {"Crate": (768, 512), "Ticket": (512, 512), "Star": (256, 768), "Rebirth": (0, 768), "Trophy": (256, 512)}
OUT = "/home/claude/dream-zoo-assets/badges/"

def icon_href(name):
    x, y = CELLS[name]
    buf = io.BytesIO(); ICONS.crop((x, y, x + 256, y + 256)).save(buf, "PNG")
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()

def savanna():
    return ('<circle cx="256" cy="250" r="86" fill="#FFE08A"/>'
            + v1.acacia(256, 336, 2.1)
            + '<path d="M120,330 Q256,300 392,330 L392,400 L120,400 Z" fill="#E8B64C" stroke="#3C2D23" stroke-width="8"/>')

BADGES = [
    ("first_crate", "FIRST CRATE", "#5AA9E6", ("icon", "Crate"), None),
    ("crate_crazy", "CRATE CRAZY", "#F08A3C", ("icon", "Crate"), "100"),
    ("millionaire", "MILLIONAIRE", "#F2C230", ("icon", "Ticket"), "1M"),
    ("legendary", "LEGENDARY", "#F59E2B", ("icon", "Star"), None),
    ("first_rebirth", "FRESH START", "#9B6BE0", ("icon", "Rebirth"), None),
    ("savanna", "SAVANNA", "#E07A3C", ("scene", None), None),
]

for file, title, color, art, tag in BADGES:
    if art[0] == "icon":
        pic = f'<image href="{icon_href(art[1])}" x="116" y="110" width="280" height="280"/>'
    else:
        pic = savanna()
    tagsvg = ""
    if tag:
        tagsvg = (f'<circle cx="378" cy="150" r="54" fill="#E24B4B" stroke="{DARK}" stroke-width="10"/>'
                  + outlined_text(378, 150 + 17, tag, 46 if len(tag) < 3 else 40, "#FFFFFF", sw=10))
    ribbon = (f'<path d="M50,372 L462,372 L440,412 L462,452 L50,452 L72,412 Z" fill="#E24B4B" stroke="{DARK}" stroke-width="10" stroke-linejoin="round"/>'
              + outlined_text(256, 428, title, 50 if len(title) <= 10 else 44, "#FFFFFF", sw=11))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<defs><radialGradient id="g" cx="50%" cy="45%" r="60%"><stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.55"/><stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
<clipPath id="c"><circle cx="256" cy="256" r="196"/></clipPath></defs>
<circle cx="256" cy="256" r="246" fill="#B97A45" stroke="{DARK}" stroke-width="12"/>
<circle cx="256" cy="256" r="226" fill="none" stroke="#9A6034" stroke-width="4" opacity="0.7"/>
<circle cx="256" cy="256" r="196" fill="{color}" stroke="{DARK}" stroke-width="12"/>
<g clip-path="url(#c)">{rays(256, 256, 16, 300, "#FFFFFF", 0.18)}<circle cx="256" cy="230" r="200" fill="url(#g)"/>{pic}</g>
{tagsvg}
{sparkle(118, 132, 20)}{sparkle(400, 300, 13, "#FFF3B0")}
{ribbon}
</svg>'''
    cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT + file + ".png", output_width=512, output_height=512)
    print("wrote", file)

# contact sheet for checking
sheet = Image.new("RGBA", (6 * 260, 260), (60, 60, 60, 255))
for i, b in enumerate(BADGES):
    im = Image.open(OUT + b[0] + ".png").resize((256, 256), Image.LANCZOS)
    sheet.paste(im, (i * 260 + 2, 2), im)
sheet.save("/tmp/claude-0/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/scratchpad/badge_sheet.png")
