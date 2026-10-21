"""Game icon v2 (512x512): the safari look of the new UI. Savanna sunset, golden grass, acacias,
the lion + giraffe, inside a carved-wood frame with nails (like the menu panels)."""
import sys
import cairosvg
sys.path.insert(0, "/tmp/claude-0/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/scratchpad/icons")
from make_icons import DARK, OUT, outlined_text, rays, sparkle  # noqa: E402
import make_game_icon as v1  # noqa: E402  (reuses its lion / giraffe / acacia drawings)

def hills():
    return ('<path d="M-20,362 Q120,318 260,350 T540,336 L540,540 L-20,540 Z" fill="#E8B64C" stroke="#3C2D23" stroke-width="10"/>'
            '<path d="M-20,404 Q160,360 330,398 T540,392 L540,540 L-20,540 Z" fill="#D49A3A"/>'
            + "".join(f'<path d="M{x},{y} l6,-22 l6,22 M{x+10},{y} l7,-28 l7,28" fill="none" stroke="#B9802C" stroke-width="5" stroke-linecap="round"/>'
                      for x, y in ((40, 386), (150, 372), (300, 380), (420, 368))))

def frame():
    # carved wood ring around the picture, with grain and four nails
    s = ['<path fill-rule="evenodd" d="M0,0 H512 V512 H0 Z M40,40 H472 V472 H40 Z" fill="#B97A45"/>',
         '<rect x="40" y="40" width="432" height="432" rx="40" fill="none" stroke="#3C2D23" stroke-width="12"/>']
    for y in (18, 26):
        s.append(f'<path d="M70,{y} H442" stroke="#9A6034" stroke-width="3" stroke-linecap="round" opacity="0.7"/>')
        s.append(f'<path d="M70,{512 - y} H442" stroke="#9A6034" stroke-width="3" stroke-linecap="round" opacity="0.7"/>')
        s.append(f'<path d="M{y},70 V442" stroke="#9A6034" stroke-width="3" stroke-linecap="round" opacity="0.7"/>')
        s.append(f'<path d="M{512 - y},70 V442" stroke="#9A6034" stroke-width="3" stroke-linecap="round" opacity="0.7"/>')
    for x, y in ((22, 22), (490, 22), (22, 490), (490, 490)):
        s.append(f'<circle cx="{x}" cy="{y}" r="9" fill="#6E6158" stroke="#3C2D23" stroke-width="4"/><circle cx="{x-2}" cy="{y-2}" r="3" fill="#A89A90"/>')
    return "\n".join(s)

banner = (f'<path d="M34,384 L478,384 L456,430 L478,476 L34,476 L56,430 Z" transform="translate(6 8)" fill="#000" opacity="0.25"/>'
          f'<path d="M34,384 L478,384 L456,430 L478,476 L34,476 L56,430 Z" fill="#E24B4B" stroke="{DARK}" stroke-width="12" stroke-linejoin="round"/>'
          + outlined_text(256, 450, "DREAM ZOO!", 64, "#FFFFFF", sw=14))
top_text = outlined_text(256, 108, "BUILD YOUR", 48, "#FFD84A", sw=12)

inner = "\n".join([
    '<circle cx="256" cy="330" r="120" fill="#FFE08A" opacity="0.9"/>',  # setting sun
    v1.acacia(96, 352, 0.9), v1.acacia(430, 338, 0.7),
    hills(),
    v1.giraffe(384, 186, 0.9),
    v1.lion(222, 246, 106),
    sparkle(84, 170, 20), sparkle(436, 96, 15, "#FFF3B0"), sparkle(110, 330, 11, "#FFF3B0"),
    top_text, banner,
])

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#4FA6E6"/><stop offset="55%" stop-color="#FFC27A"/><stop offset="100%" stop-color="#FFE3A8"/>
  </linearGradient>
  <clipPath id="pic"><rect x="40" y="40" width="432" height="432" rx="40"/></clipPath>
</defs>
<rect width="512" height="512" fill="url(#sky)"/>
<g clip-path="url(#pic)">
  <rect width="512" height="512" fill="url(#sky)"/>
  {rays(256, 320, 18, 560, "#FFFFFF", 0.14)}
  {inner}
</g>
{frame()}
{top_text}
{banner}
</svg>'''
open(OUT + "game_icon_v2.svg", "w").write(svg)
cairosvg.svg2png(bytestring=svg.encode(), write_to=OUT + "game_icon_v2.png", output_width=512, output_height=512)
print("wrote game_icon_v2.png")
