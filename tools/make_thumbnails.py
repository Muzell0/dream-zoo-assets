"""Two 1920x1080 thumbnails from in-game screenshots, with a logo / callout overlay."""
import io
import sys

import cairosvg
from PIL import Image

sys.path.insert(0, "/tmp/claude-0/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/scratchpad/icons")
from make_icons import DARK, OUT, outlined_text, sparkle  # noqa: E402

SHOTS = "/root/.claude/projects/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/tool-results/"
W, H = 1920, 1080


def to_16x9(path):
    """Center-crop a screenshot to 16:9 and scale it to 1920x1080."""
    img = Image.open(path).convert("RGB")
    w, h = img.size
    target_w = round(h * 16 / 9)
    if target_w <= w:
        left = (w - target_w) // 2
        img = img.crop((left, 0, left + target_w, h))
    else:
        target_h = round(w * 9 / 16)
        top = (h - target_h) // 2
        img = img.crop((0, top, w, top + target_h))
    return img.resize((W, H), Image.LANCZOS)


def overlay(svg_inner):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{svg_inner}</svg>'
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=W, output_height=H)
    return Image.open(io.BytesIO(png)).convert("RGBA")


def banner(cx, y, width, text, size, color, text_color="#FFFFFF"):
    """The same notched ribbon as the game icon."""
    x0, x1, h = cx - width / 2, cx + width / 2, size * 1.45
    notch = h * 0.25
    path = (f"M{x0},{y} L{x1},{y} L{x1 - notch},{y + h / 2} L{x1},{y + h} L{x0},{y + h} L{x0 + notch},{y + h / 2} Z")
    return (f'<path d="{path}" transform="translate(10 14)" fill="#000" opacity="0.25"/>'
            f'<path d="{path}" fill="{color}" stroke="{DARK}" stroke-width="16" stroke-linejoin="round"/>'
            + outlined_text(cx, y + h * 0.72, text, size, text_color, sw=size * 0.22))


# 1) the zoo: logo across the top
zoo_logo = "\n".join([
    outlined_text(W / 2, 128, "BUILD YOUR", 92, "#FFD84A", sw=20),
    banner(W / 2, 150, 1060, "DREAM ZOO!", 118, "#E24B4B"),
    sparkle(W / 2 - 600, 120, 38), sparkle(W / 2 + 590, 250, 30, "#FFF3B0"),
])

# 2) the hub: a callout in the bottom-left corner
hub_callout = "\n".join([
    banner(650, 820, 1180, "EXPLORE NEW WORLDS!", 80, "#7B55C9", "#FFD84A"),
    sparkle(110, 790, 30), sparkle(1225, 960, 22, "#FFF3B0"),
])

for name, shot, svg in [
    ("thumbnail_zoo", "mcp-remote-devices-blob-1791336272555-qtdq1c.jpg", zoo_logo),
    ("thumbnail_worlds", "mcp-remote-devices-blob-1791336225745-5df72v.jpg", hub_callout),
]:
    base = to_16x9(SHOTS + shot).convert("RGBA")
    out = Image.alpha_composite(base, overlay(svg)).convert("RGB")
    out.save(OUT + name + ".png", optimize=True)
    print("wrote", name, out.size)
