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
