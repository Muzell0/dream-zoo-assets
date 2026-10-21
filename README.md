# Build Your Dream Zoo! assets

Public image assets for the Roblox game **Build Your Dream Zoo!** by The Den Interactive.
Studio uploads them into Roblox from their raw links; the game itself references the Roblox asset ids.

| File | What it is |
| --- | --- |
| `ui/sprites.png` | UI sprite sheet: wood panel, plank sign, buttons, close button, leaves, paw pattern, bars, gate door, rays |
| `ui/icons.png` | 16 icons (256 px cells): Shop, Teleport, Index, Rewards, Codes, Settings, Build, Animals, AutoCollect, Trophy, Ticket, Crate, Rebirth, Star, Lock, Home |
| `ui/loading_scene_left.png`, `ui/loading_scene_right.png` | Loading screen illustration, 2048x1152 split in two halves |
| `ui/logo.png` | Game logo |

`tools/` holds the Python scripts that draw every image (cairosvg + Pillow, Fredoka font).
Run them from inside `tools/`; each writes its PNGs to the current folder.

## Badges, game icon and thumbnails

| Folder | What | Where it goes |
|---|---|---|
| `badges/` | 6 badge icons (512x512): first_crate, crate_crazy, millionaire, legendary, first_rebirth, savanna | Creator Dashboard > Badges (one image per badge), then paste each badge ID into `Config.Badges` |
| `icon/game_icon.png` | the game icon (512x512), safari wood-frame version | Creator Dashboard > Places > Icon |
| `thumbnails/` | three 1920x1080 thumbnails: zoo, hub, crates | Creator Dashboard > Places > Thumbnails |

Drawn by `tools/make_badges.py`, `tools/make_game_icon_v2.py` and `tools/make_thumbnails_v2.py`
(the thumbnails start from in-game Studio screenshots).
