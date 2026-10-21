"""Thumbnails v2 (1920x1080): new in-game shots (safari UI, new hub) with the new logo art."""
import io, sys
from PIL import Image
sys.path.insert(0, "/tmp/claude-0/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/scratchpad/icons")
from make_thumbnails import to_16x9, overlay, banner, SHOTS, W, H  # noqa: E402
from make_icons import sparkle  # noqa: E402
OUT = "/home/claude/dream-zoo-assets/thumbnails/"
LOGO = Image.open("/home/claude/dream-zoo-assets/ui/logo.png").convert("RGBA")

def logo(img, cx, top, width):
    l = LOGO.resize((width, round(LOGO.height * width / LOGO.width)), Image.LANCZOS)
    img.alpha_composite(l, (round(cx - width / 2), top))

shots = {
    "zoo": "mcp-remote-devices-blob-1792569127945-fuu6fn.jpg",
    "hub": "mcp-remote-devices-blob-1792569084547-fc2lst.jpg",
    "crates": "mcp-remote-devices-blob-1792569141245-ue88e1.jpg",
}
# 1) zoo: big logo up top
img = to_16x9(SHOTS + shots["zoo"]).convert("RGBA")
logo(img, W / 2, 30, 1100)
img.convert("RGB").save(OUT + "thumbnail_zoo.png", optimize=True)
# 2) hub: callout bottom + small logo top-left
img = to_16x9(SHOTS + shots["hub"]).convert("RGBA")
img.alpha_composite(overlay(banner(W / 2, 880, 1240, "HANG OUT IN THE HUB!", 84, "#7B55C9", "#FFD84A") + sparkle(380, 860, 30) + sparkle(1560, 1010, 22, "#FFF3B0")))
logo(img, 360, 24, 640)
img.convert("RGB").save(OUT + "thumbnail_hub.png", optimize=True)
# 3) crates: callout top-centre (the HUD stays visible around it)
img = Image.open(SHOTS + shots["crates"]).convert("RGB").resize((W, H), Image.LANCZOS).convert("RGBA")  # keep the whole HUD in frame
img.alpha_composite(overlay(banner(W / 2, 40, 1180, "OPEN CRATES, FIND RARES!", 80, "#E24B4B", "#FFFFFF") + sparkle(420, 50, 30) + sparkle(1500, 170, 24, "#FFF3B0")))
img.convert("RGB").save(OUT + "thumbnail_crates.png", optimize=True)
sheet = Image.new("RGB", (1920, 360))
for i, n in enumerate(["thumbnail_zoo", "thumbnail_hub", "thumbnail_crates"]):
    sheet.paste(Image.open(OUT + n + ".png").resize((640, 360)), (i * 640, 0))
sheet.save("/tmp/claude-0/-home-claude/f63f542f-bc7e-5f79-b1c9-e537d0e36108/scratchpad/thumb_sheet.png")
print("ok")
