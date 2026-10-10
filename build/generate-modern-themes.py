#!/usr/bin/env python3
"""
Generate Curated Modern Theme Suite for IRAM OS / Omarchy:
- Cyberpunk Neon
- Dracula
- Oxocarbon
- Vesper
- Material Ocean
- Aura Dark
- Rose Pine Moon
- Monokai Pro

Generates:
1. colors.toml (with full palette and hyprland_active_border)
2. icons.theme (Papirus-Dark)
3. chromium.theme (accent hex)
4. vscode.json
5. neovim.lua
6. backgrounds/1-wallpaper.webp (3840x2160 ultra-HD aesthetic wallpaper)
7. preview.png (1800x1012 visual card with frosted glass palette preview)
8. preview-unlock.png & unlock.png
"""

import os
import math
import shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

THEMES = {
    "cyberpunk-neon": {
        "title": "Cyberpunk Neon",
        "tagline": "Electric Obsidian & High-Voltage Neon",
        "colors": {
            "mode": "dark",
            "accent": "#00f0ff",
            "selection": "#2a153c",
            "muted": "#625e7a",
            "background": "#0d0f18",
            "dark_background": "#08090f",
            "darker_background": "#05050a",
            "lighter_background": "#181a27",
            "foreground": "#eaeefb",
            "dark_foreground": "#70799c",
            "light_foreground": "#f1f4fc",
            "bright_foreground": "#ffffff",
            "red": "#ff0055",
            "yellow": "#ffe600",
            "orange": "#ff7b00",
            "green": "#05ffa1",
            "cyan": "#00f0ff",
            "blue": "#3a86ff",
            "magenta": "#ff007f",
            "brown": "#9b4dca",
            "bright_red": "#ff3377",
            "bright_yellow": "#fff033",
            "bright_green": "#38ffb4",
            "bright_cyan": "#33f3ff",
            "bright_blue": "#619eff",
            "bright_magenta": "#ff3399",
            "hyprland_active_border": "rgb(00f0ff) rgb(ff007f) 45deg"
        },
        "vscode": {"name": "Cyberpunk", "extension": "endormi.2077-theme"},
        "neovim": "tokyonight-night",
        "style": "cyberpunk"
    },
    "dracula": {
        "title": "Dracula",
        "tagline": "Classic Vampire Midnight & Radiant Pastels",
        "colors": {
            "mode": "dark",
            "accent": "#bd93f9",
            "selection": "#44475a",
            "muted": "#6272a4",
            "background": "#282a36",
            "dark_background": "#21222c",
            "darker_background": "#191a21",
            "lighter_background": "#343746",
            "foreground": "#f8f8f2",
            "dark_foreground": "#6272a4",
            "light_foreground": "#f8f8f2",
            "bright_foreground": "#ffffff",
            "red": "#ff5555",
            "yellow": "#f1fa8c",
            "orange": "#ffb86c",
            "green": "#50fa7b",
            "cyan": "#8be9fd",
            "blue": "#bd93f9",
            "magenta": "#ff79c6",
            "brown": "#d6acff",
            "bright_red": "#ff6e6e",
            "bright_yellow": "#ffffa5",
            "bright_green": "#69ff94",
            "bright_cyan": "#a4ffff",
            "bright_blue": "#d1b2ff",
            "bright_magenta": "#ff92df",
            "hyprland_active_border": "rgb(bd93f9) rgb(ff79c6) 45deg"
        },
        "vscode": {"name": "Dracula Official", "extension": "dracula-theme.theme-dracula"},
        "neovim": "dracula",
        "style": "dracula"
    },
    "oxocarbon": {
        "title": "Oxocarbon",
        "tagline": "High-Tech IBM Design Monolith",
        "colors": {
            "mode": "dark",
            "accent": "#ff7eb6",
            "selection": "#262626",
            "muted": "#525252",
            "background": "#161616",
            "dark_background": "#121212",
            "darker_background": "#0c0c0c",
            "lighter_background": "#262626",
            "foreground": "#f4f4f4",
            "dark_foreground": "#787878",
            "light_foreground": "#f4f4f4",
            "bright_foreground": "#ffffff",
            "red": "#ee5396",
            "yellow": "#ffe97b",
            "orange": "#3ddbd9",
            "green": "#42be65",
            "cyan": "#33b1ff",
            "blue": "#82cfff",
            "magenta": "#be95ff",
            "brown": "#ff7eb6",
            "bright_red": "#ff65a8",
            "bright_yellow": "#fff2a6",
            "bright_green": "#5cd17d",
            "bright_cyan": "#66c5ff",
            "bright_blue": "#a1dbff",
            "bright_magenta": "#d0b3ff",
            "hyprland_active_border": "rgb(ff7eb6) rgb(33b1ff) 45deg"
        },
        "vscode": {"name": "Oxocarbon", "extension": "shaunsingh.oxocarbon"},
        "neovim": "oxocarbon",
        "style": "oxocarbon"
    },
    "vesper": {
        "title": "Vesper",
        "tagline": "Minimalist Pure Pitch Dark & Golden Amber",
        "colors": {
            "mode": "dark",
            "accent": "#ffc799",
            "selection": "#232323",
            "muted": "#505050",
            "background": "#101010",
            "dark_background": "#0a0a0a",
            "darker_background": "#050505",
            "lighter_background": "#1c1c1c",
            "foreground": "#ffffff",
            "dark_foreground": "#808080",
            "light_foreground": "#f0f0f0",
            "bright_foreground": "#ffffff",
            "red": "#f57d7d",
            "yellow": "#ffc799",
            "orange": "#fe8019",
            "green": "#99ffe4",
            "cyan": "#8de8fe",
            "blue": "#6cb6ff",
            "magenta": "#e5a5ff",
            "brown": "#cda07b",
            "bright_red": "#fa9494",
            "bright_yellow": "#ffd7b3",
            "bright_green": "#b3ffea",
            "bright_cyan": "#a8efff",
            "bright_blue": "#8bc5ff",
            "bright_magenta": "#edbaff",
            "hyprland_active_border": "rgb(ffc799) rgb(fe8019) 45deg"
        },
        "vscode": {"name": "Vesper", "extension": "raunofreiberg.vesper"},
        "neovim": "vesper",
        "style": "vesper"
    },
    "material-ocean": {
        "title": "Material Ocean",
        "tagline": "Bioluminescent Deep Oceanic Abyss",
        "colors": {
            "mode": "dark",
            "accent": "#80cbc4",
            "selection": "#1f2233",
            "muted": "#464b5d",
            "background": "#0f111a",
            "dark_background": "#090b10",
            "darker_background": "#050608",
            "lighter_background": "#1a1c25",
            "foreground": "#8f93a2",
            "dark_foreground": "#585b70",
            "light_foreground": "#c5c7d0",
            "bright_foreground": "#ffffff",
            "red": "#ff5370",
            "yellow": "#ffcb6b",
            "orange": "#f78c6c",
            "green": "#c3e88d",
            "cyan": "#89ddff",
            "blue": "#82aaff",
            "magenta": "#c792ea",
            "brown": "#916853",
            "bright_red": "#ff6b84",
            "bright_yellow": "#ffd685",
            "bright_green": "#d0f0a0",
            "bright_cyan": "#a4e5ff",
            "bright_blue": "#9bbaff",
            "bright_magenta": "#d4a6ef",
            "hyprland_active_border": "rgb(80cbc4) rgb(82aaff) 45deg"
        },
        "vscode": {"name": "Material Theme Ocean", "extension": "Equinusocio.vsc-material-theme"},
        "neovim": "material",
        "style": "material_ocean"
    },
    "aura-dark": {
        "title": "Aura Dark",
        "tagline": "Sleek Deep Violet & Neon Mint Aura",
        "colors": {
            "mode": "dark",
            "accent": "#a277ff",
            "selection": "#25223c",
            "muted": "#545070",
            "background": "#15141b",
            "dark_background": "#111016",
            "darker_background": "#0c0b10",
            "lighter_background": "#211f2d",
            "foreground": "#edecee",
            "dark_foreground": "#6d6d7c",
            "light_foreground": "#edecee",
            "bright_foreground": "#ffffff",
            "red": "#ff6767",
            "yellow": "#ffca85",
            "orange": "#ff9f66",
            "green": "#61ffca",
            "cyan": "#61ffca",
            "blue": "#82e2ff",
            "magenta": "#a277ff",
            "brown": "#f694ff",
            "bright_red": "#ff8585",
            "bright_yellow": "#ffd79e",
            "bright_green": "#82ffda",
            "bright_cyan": "#82ffda",
            "bright_blue": "#a1eaff",
            "bright_magenta": "#b894ff",
            "hyprland_active_border": "rgb(a277ff) rgb(61ffca) 45deg"
        },
        "vscode": {"name": "Aura Dark", "extension": "daltonmenezes.aura-theme"},
        "neovim": "aura-theme",
        "style": "aura_dark"
    },
    "rose-pine-moon": {
        "title": "Rosé Pine Moon",
        "tagline": "Gentle Midnight Slate, Rosé & Pine",
        "colors": {
            "mode": "dark",
            "accent": "#ea9a97",
            "selection": "#393552",
            "muted": "#56526e",
            "background": "#232136",
            "dark_background": "#1c1a2d",
            "darker_background": "#141320",
            "lighter_background": "#2a273f",
            "foreground": "#e0def4",
            "dark_foreground": "#6e6a86",
            "light_foreground": "#e0def4",
            "bright_foreground": "#f5f3ff",
            "red": "#eb6f92",
            "yellow": "#f6c177",
            "orange": "#ea9a97",
            "green": "#9ccfd8",
            "cyan": "#3e8fb0",
            "blue": "#3e8fb0",
            "magenta": "#c4a7e7",
            "brown": "#908caa",
            "bright_red": "#f083a2",
            "bright_yellow": "#f9cf92",
            "bright_green": "#b2dbe2",
            "bright_cyan": "#569fb9",
            "bright_blue": "#569fb9",
            "bright_magenta": "#d0b7ed",
            "hyprland_active_border": "rgb(ea9a97) rgb(c4a7e7) 45deg"
        },
        "vscode": {"name": "Rosé Pine Moon", "extension": "mvllow.rose-pine"},
        "neovim": "rose-pine",
        "style": "rose_pine_moon"
    },
    "monokai-pro": {
        "title": "Monokai Pro",
        "tagline": "Refined Dark Charcoal & Iconic Syntax Spectrum",
        "colors": {
            "mode": "dark",
            "accent": "#ffd866",
            "selection": "#3a383d",
            "muted": "#5b595c",
            "background": "#222222",
            "dark_background": "#19181a",
            "darker_background": "#131213",
            "lighter_background": "#2d2a2e",
            "foreground": "#fcfcfa",
            "dark_foreground": "#727072",
            "light_foreground": "#fcfcfa",
            "bright_foreground": "#ffffff",
            "red": "#ff6188",
            "yellow": "#ffd866",
            "orange": "#fc9867",
            "green": "#a9dc76",
            "cyan": "#78dce8",
            "blue": "#78dce8",
            "magenta": "#ab9df2",
            "brown": "#938aa9",
            "bright_red": "#ff7b9d",
            "bright_yellow": "#ffe085",
            "bright_green": "#bce393",
            "bright_cyan": "#94e4ee",
            "bright_blue": "#94e4ee",
            "bright_magenta": "#bfb5f5",
            "hyprland_active_border": "rgb(ffd866) rgb(ff6188) 45deg"
        },
        "vscode": {"name": "Monokai Pro", "extension": "monokai.theme-monokai-pro-vscode"},
        "neovim": "monokai-pro",
        "style": "monokai_pro"
    }
}


def hex_to_rgb(hex_code):
    h = hex_code.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def generate_wallpaper(theme_id, data, width=3840, height=2160):
    """Generate high-resolution aesthetic wallpapers tailored to each theme."""
    colors = data["colors"]
    bg_rgb = hex_to_rgb(colors["dark_background"])
    darker_rgb = hex_to_rgb(colors["darker_background"])
    acc_rgb = hex_to_rgb(colors["accent"])
    cyan_rgb = hex_to_rgb(colors["cyan"])
    red_rgb = hex_to_rgb(colors["red"])
    mag_rgb = hex_to_rgb(colors.get("magenta", colors["accent"]))
    green_rgb = hex_to_rgb(colors.get("green", colors["accent"]))
    yel_rgb = hex_to_rgb(colors.get("yellow", colors["accent"]))

    # Base gradient array
    y_coords = np.linspace(0, 1, height)[:, None]
    x_coords = np.linspace(0, 1, width)[None, :]
    
    # Smooth diagonal gradient base
    diag = (x_coords * 0.4 + y_coords * 0.6)
    base_r = (darker_rgb[0] * (1 - diag) + bg_rgb[0] * diag).astype(np.uint8)
    base_g = (darker_rgb[1] * (1 - diag) + bg_rgb[1] * diag).astype(np.uint8)
    base_b = (darker_rgb[2] * (1 - diag) + bg_rgb[2] * diag).astype(np.uint8)

    img = Image.fromarray(np.stack([base_r, base_g, base_b], axis=-1), mode="RGB")
    draw = ImageDraw.Draw(img, "RGBA")
    style = data["style"]

    if style == "cyberpunk":
        # Perspective synthwave grid + radiant glowing sun
        horizon_y = int(height * 0.58)
        
        # Sun with neon gradient
        sun_radius = 420
        sun_center = (width // 2, horizon_y - 80)
        sun_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        sun_draw = ImageDraw.Draw(sun_layer)
        for r in range(sun_radius, 0, -2):
            prog = r / sun_radius
            # Pink to yellow-red
            r_val = int(mag_rgb[0] * prog + yel_rgb[0] * (1 - prog))
            g_val = int(mag_rgb[1] * prog + yel_rgb[1] * (1 - prog))
            b_val = int(mag_rgb[2] * prog + yel_rgb[2] * (1 - prog))
            sun_draw.ellipse(
                [sun_center[0] - r, sun_center[1] - r, sun_center[0] + r, sun_center[1] + r],
                fill=(r_val, g_val, b_val, 160)
            )
        # Scanline cuts through the sun
        for sy in range(sun_center[1] - 40, horizon_y, 24):
            bar_h = int(4 + (sy - (sun_center[1] - 40)) * 0.15)
            sun_draw.rectangle([0, sy, width, sy + bar_h], fill=(bg_rgb[0], bg_rgb[1], bg_rgb[2], 255))
        img = Image.alpha_composite(img.convert("RGBA"), sun_layer).convert("RGB")
        draw = ImageDraw.Draw(img, "RGBA")

        # Ground perspective grid
        grid_lines = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(grid_lines)
        vanishing_pt = (width // 2, horizon_y)

        # Perspective rays
        for x in range(-width // 2, width + width // 2, 120):
            gdraw.line([vanishing_pt, (x, height)], fill=(cyan_rgb[0], cyan_rgb[1], cyan_rgb[2], 75), width=2)
        # Horizontal lines with exponential spacing
        for i in range(1, 28):
            py = horizon_y + int((height - horizon_y) * (math.pow(i / 27, 2.2)))
            alpha = int(30 + 180 * (i / 27))
            gdraw.line([(0, py), (width, py)], fill=(mag_rgb[0], mag_rgb[1], mag_rgb[2], alpha), width=2)

        # Bloom glow on horizon
        gdraw.rectangle([0, horizon_y - 2, width, horizon_y + 2], fill=(cyan_rgb[0], cyan_rgb[1], cyan_rgb[2], 220))
        grid_lines = grid_lines.filter(ImageFilter.GaussianBlur(1))
        img = Image.alpha_composite(img.convert("RGBA"), grid_lines).convert("RGB")

    elif style == "dracula":
        # Ethereal floating geometric portals & dual soft radiant blooms
        bloom_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        bdraw = ImageDraw.Draw(bloom_layer)
        # Purple bloom
        bdraw.ellipse([width * 0.25 - 500, height * 0.4 - 500, width * 0.25 + 500, height * 0.4 + 500],
                      fill=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 90))
        # Pink bloom
        bdraw.ellipse([width * 0.75 - 500, height * 0.6 - 500, width * 0.75 + 500, height * 0.6 + 500],
                      fill=(mag_rgb[0], mag_rgb[1], mag_rgb[2], 75))
        # Green subtle accent
        bdraw.ellipse([width * 0.5 - 300, height * 0.2 - 300, width * 0.5 + 300, height * 0.2 + 300],
                      fill=(green_rgb[0], green_rgb[1], green_rgb[2], 40))
        bloom_layer = bloom_layer.filter(ImageFilter.GaussianBlur(140))
        img = Image.alpha_composite(img.convert("RGBA"), bloom_layer)

        # Floating isometric rings & diamond runes
        geo_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(geo_layer)
        cx, cy = width // 2, height // 2
        for r, w, col in [(380, 3, acc_rgb), (520, 2, mag_rgb), (680, 1, cyan_rgb)]:
            gdraw.ellipse([cx - r, cy - int(r * 0.55), cx + r, cy + int(r * 0.55)],
                          outline=(col[0], col[1], col[2], 140), width=w)
        # Diamond center
        dsize = 140
        gdraw.polygon([(cx, cy - dsize), (cx + dsize, cy), (cx, cy + dsize), (cx - dsize, cy)],
                      outline=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 220), width=4)
        img = Image.alpha_composite(img, geo_layer).convert("RGB")

    elif style == "oxocarbon":
        # Monolithic angled architecture, minimalist razor-sharp planes
        plane_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        pdraw = ImageDraw.Draw(plane_layer)
        
        # Diagonal razor blade shards
        coords = [
            [(width * 0.1, 0), (width * 0.45, 0), (width * 0.25, height), (0, height)],
            [(width * 0.4, 0), (width * 0.8, 0), (width * 0.6, height), (width * 0.2, height)],
            [(width * 0.75, 0), (width, 0), (width, height * 0.7), (width * 0.55, height)]
        ]
        shades = [
            (bg_rgb[0] + 10, bg_rgb[1] + 10, bg_rgb[2] + 10, 160),
            (bg_rgb[0] + 20, bg_rgb[1] + 20, bg_rgb[2] + 20, 180),
            (bg_rgb[0] + 14, bg_rgb[1] + 14, bg_rgb[2] + 14, 150)
        ]
        for poly, sh in zip(coords, shades):
            pdraw.polygon(poly, fill=sh)

        # High-tech accent laser edges
        pdraw.line([(width * 0.45, 0), (width * 0.25, height)], fill=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 230), width=4)
        pdraw.line([(width * 0.8, 0), (width * 0.6, height)], fill=(cyan_rgb[0], cyan_rgb[1], cyan_rgb[2], 230), width=3)
        pdraw.line([(width * 0.75, 0), (width * 0.55, height)], fill=(mag_rgb[0], mag_rgb[1], mag_rgb[2], 160), width=2)
        
        # Fine grid pattern
        for x in range(0, width, 80):
            pdraw.line([(x, 0), (x, height)], fill=(255, 255, 255, 6), width=1)
        for y in range(0, height, 80):
            pdraw.line([(0, y), (width, y)], fill=(255, 255, 255, 6), width=1)

        img = Image.alpha_composite(img.convert("RGBA"), plane_layer).convert("RGB")

    elif style == "vesper":
        # Pure pitch dark obsidian with warm golden amber celestial eclipse & glow
        glow_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow_layer)
        cx, cy = int(width * 0.5), int(height * 0.48)
        
        # Deep amber atmospheric glow
        gdraw.ellipse([cx - 700, cy - 700, cx + 700, cy + 700], fill=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 85))
        gdraw.ellipse([cx - 450, cy - 450, cx + 450, cy + 450], fill=(yel_rgb[0], yel_rgb[1], yel_rgb[2], 110))
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(120))
        img = Image.alpha_composite(img.convert("RGBA"), glow_layer)

        # Eclipse ring
        ring_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        rdraw = ImageDraw.Draw(ring_layer)
        r = 340
        # Dark body blocking
        rdraw.ellipse([cx - r + 8, cy - r + 8, cx + r + 8, cy + r + 8], fill=(darker_rgb[0], darker_rgb[1], darker_rgb[2], 255))
        # Radiant gold rim
        rdraw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 240), width=5)
        # Inner fine ring
        rdraw.ellipse([cx - r - 40, cy - r - 40, cx + r + 40, cy + r + 40], outline=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 80), width=1)
        img = Image.alpha_composite(img, ring_layer).convert("RGB")

    elif style == "material_ocean":
        # Flowing bioluminescent oceanic topographic waves
        wave_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        wdraw = ImageDraw.Draw(wave_layer)
        
        # Ambient abyssal glows
        wdraw.ellipse([width * 0.2 - 600, height * 0.3 - 600, width * 0.2 + 600, height * 0.3 + 600],
                      fill=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 70))
        wdraw.ellipse([width * 0.8 - 600, height * 0.7 - 600, width * 0.8 + 600, height * 0.7 + 600],
                      fill=(cyan_rgb[0], cyan_rgb[1], cyan_rgb[2], 80))
        wave_layer = wave_layer.filter(ImageFilter.GaussianBlur(150))
        img = Image.alpha_composite(img.convert("RGBA"), wave_layer)

        # Multi-layered organic sine contour ribbons
        contour_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        cdraw = ImageDraw.Draw(contour_layer)
        
        for k in range(12):
            pts = []
            base_y = int(height * 0.35 + k * 110)
            alpha = int(40 + k * 14)
            color = acc_rgb if k % 2 == 0 else cyan_rgb
            for x in range(0, width + 50, 40):
                y = int(base_y + math.sin(x * 0.002 + k * 0.5) * 120 + math.cos(x * 0.001 - k * 0.3) * 60)
                pts.append((x, y))
            cdraw.line(pts, fill=(color[0], color[1], color[2], alpha), width=3)

        img = Image.alpha_composite(img, contour_layer).convert("RGB")

    elif style == "aura_dark":
        # Cosmic aura spheres blending neon purple and mint green
        aura_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        adraw = ImageDraw.Draw(aura_layer)

        # Orb 1: Violet/Purple
        adraw.ellipse([width * 0.35 - 550, height * 0.45 - 550, width * 0.35 + 550, height * 0.45 + 550],
                      fill=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 120))
        # Orb 2: Neon Mint Green
        adraw.ellipse([width * 0.65 - 500, height * 0.55 - 500, width * 0.65 + 500, height * 0.55 + 500],
                      fill=(green_rgb[0], green_rgb[1], green_rgb[2], 100))
        # Orb 3: Coral/Pink
        adraw.ellipse([width * 0.5 - 400, height * 0.25 - 400, width * 0.5 + 400, height * 0.25 + 400],
                      fill=(mag_rgb[0], mag_rgb[1], mag_rgb[2], 80))

        aura_layer = aura_layer.filter(ImageFilter.GaussianBlur(160))
        img = Image.alpha_composite(img.convert("RGBA"), aura_layer)

        # Modern orbital wireframes
        wire_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        wdraw = ImageDraw.Draw(wire_layer)
        cx, cy = width // 2, height // 2
        wdraw.ellipse([cx - 480, cy - 480, cx + 480, cy + 480],
                      outline=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 90), width=2)
        wdraw.ellipse([cx - 620, cy - 320, cx + 620, cy + 320],
                      outline=(green_rgb[0], green_rgb[1], green_rgb[2], 80), width=2)
        img = Image.alpha_composite(img, wire_layer).convert("RGB")

    elif style == "rose_pine_moon":
        # Serene twilight slate, gentle crescent moon & starry constellation
        sky_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        sdraw = ImageDraw.Draw(sky_layer)

        # Soft rose-pine ambient glows
        sdraw.ellipse([width * 0.7 - 500, height * 0.35 - 500, width * 0.7 + 500, height * 0.35 + 500],
                      fill=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 90))
        sdraw.ellipse([width * 0.3 - 500, height * 0.65 - 500, width * 0.3 + 500, height * 0.65 + 500],
                      fill=(cyan_rgb[0], cyan_rgb[1], cyan_rgb[2], 75))
        sky_layer = sky_layer.filter(ImageFilter.GaussianBlur(140))
        img = Image.alpha_composite(img.convert("RGBA"), sky_layer)

        # Crescent Moon
        moon_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        mdraw = ImageDraw.Draw(moon_layer)
        mx, my, mr = int(width * 0.72), int(height * 0.36), 200
        # Main glow
        mdraw.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 230))
        # Shadow overlay to create crescent
        mdraw.ellipse([mx - mr + 65, my - mr - 30, mx + mr + 65, my + mr - 30],
                      fill=(bg_rgb[0], bg_rgb[1], bg_rgb[2], 255))
        
        # Subtle constellation stars
        np.random.seed(42)
        star_x = np.random.randint(50, width - 50, 180)
        star_y = np.random.randint(50, height - 50, 180)
        for sx, sy in zip(star_x, star_y):
            salpha = np.random.randint(80, 220)
            mdraw.ellipse([sx - 2, sy - 2, sx + 2, sy + 2],
                          fill=(224, 222, 244, salpha))
        img = Image.alpha_composite(img, moon_layer).convert("RGB")

    elif style == "monokai_pro":
        # Modern diagonal geometric spectrum prisms
        prism_layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        pdraw = ImageDraw.Draw(prism_layer)

        # Diagonal color ribbons
        spectrum = [
            (yel_rgb, 0.25),
            (red_rgb, 0.38),
            (mag_rgb, 0.50),
            (cyan_rgb, 0.62),
            (green_rgb, 0.75),
        ]
        slant = width * 0.35
        for col, pos in spectrum:
            cx_top = int(width * pos)
            cx_bot = int(cx_top - slant)
            poly = [(cx_top - 60, 0), (cx_top + 60, 0), (cx_bot + 60, height), (cx_bot - 60, height)]
            pdraw.polygon(poly, fill=(col[0], col[1], col[2], 55))
            pdraw.line([(cx_top, 0), (cx_bot, height)], fill=(col[0], col[1], col[2], 210), width=4)

        # Sleek dark overlay in center to give depth
        pdraw.rectangle([0, height // 3, width, int(height * 0.66)], fill=(bg_rgb[0], bg_rgb[1], bg_rgb[2], 120))
        img = Image.alpha_composite(img.convert("RGBA"), prism_layer).convert("RGB")

    return img


def generate_preview_card(theme_id, data, wallpaper_img):
    """Generate high-impact 1800x1012 card for the theme switcher preview."""
    target_w, target_h = 1800, 1012
    # Resize wallpaper to fill
    card = wallpaper_img.copy().resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Soft vignette / dark glass overlay
    dark_overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 70))
    card = Image.alpha_composite(card.convert("RGBA"), dark_overlay)

    # Frosted acrylic glass card at the bottom center
    glass_w, glass_h = 1380, 260
    glass_x = (target_w - glass_w) // 2
    glass_y = target_h - glass_h - 70

    glass_layer = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glass_layer)

    # Glass container background + border
    bg_rgb = hex_to_rgb(data["colors"]["dark_background"])
    acc_rgb = hex_to_rgb(data["colors"]["accent"])

    gdraw.rectangle([glass_x, glass_y, glass_x + glass_w, glass_y + glass_h],
                    fill=(bg_rgb[0], bg_rgb[1], bg_rgb[2], 215),
                    outline=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 180),
                    width=3)

    # Accent top highlight line
    gdraw.line([(glass_x, glass_y), (glass_x + glass_w, glass_y)],
               fill=(acc_rgb[0], acc_rgb[1], acc_rgb[2], 255), width=4)

    card = Image.alpha_composite(card, glass_layer).convert("RGB")
    draw = ImageDraw.Draw(card)

    # Load system font
    font_title = None
    font_sub = None
    font_tag = None
    for fn in [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf"
    ]:
        if os.path.exists(fn):
            try:
                font_title = ImageFont.truetype(fn, 54)
                font_sub = ImageFont.truetype(fn.replace("-Bold", "-Regular").replace("-B", "-R"), 24)
                font_tag = ImageFont.truetype(fn, 20)
                break
            except Exception:
                pass
    if font_title is None:
        font_title = ImageFont.load_default()
        font_sub = font_title
        font_tag = font_title

    # Draw Title & Tagline
    draw.text((glass_x + 50, glass_y + 40), data["title"], font=font_title, fill=(255, 255, 255))
    draw.text((glass_x + 52, glass_y + 115), data["tagline"], font=font_sub,
              fill=hex_to_rgb(data["colors"]["light_foreground"]))
    draw.text((glass_x + 52, glass_y + 155), "IRAM OS NEXT-GEN THEME SUITE", font=font_tag, fill=acc_rgb)

    # Color Swatch Palette Row on the right
    colors_to_show = [
        ("ACC", data["colors"]["accent"]),
        ("BG", data["colors"]["background"]),
        ("RED", data["colors"]["red"]),
        ("GRN", data["colors"]["green"]),
        ("YEL", data["colors"]["yellow"]),
        ("BLU", data["colors"]["blue"]),
        ("MAG", data["colors"]["magenta"]),
        ("CYN", data["colors"]["cyan"]),
    ]
    swatch_x_start = glass_x + glass_w - 580
    swatch_y = glass_y + 60
    swatch_size = 54
    swatch_spacing = 68

    for idx, (label, hex_val) in enumerate(colors_to_show):
        sx = swatch_x_start + (idx % 4) * swatch_spacing
        sy = swatch_y + (idx // 4) * (swatch_size + 34)
        c_rgb = hex_to_rgb(hex_val)
        draw.rectangle([sx, sy, sx + swatch_size, sy + swatch_size],
                       fill=c_rgb, outline=(255, 255, 255, 120), width=2)
        draw.text((sx + 6, sy + swatch_size + 6), label, font=font_tag, fill=(200, 200, 200))

    return card


def build_colors_toml(data):
    lines = [f'mode = "{data["colors"]["mode"]}"', ""]
    lines.append(f'accent = "{data["colors"]["accent"]}"')
    lines.append(f'selection = "{data["colors"]["selection"]}"')
    lines.append(f'muted = "{data["colors"]["muted"]}"')
    lines.append("")
    lines.append(f'background = "{data["colors"]["background"]}"')
    lines.append(f'dark_background = "{data["colors"]["dark_background"]}"')
    lines.append(f'darker_background = "{data["colors"]["darker_background"]}"')
    lines.append(f'lighter_background = "{data["colors"]["lighter_background"]}"')
    lines.append("")
    lines.append(f'foreground = "{data["colors"]["foreground"]}"')
    lines.append(f'dark_foreground = "{data["colors"]["dark_foreground"]}"')
    lines.append(f'light_foreground = "{data["colors"]["light_foreground"]}"')
    lines.append(f'bright_foreground = "{data["colors"]["bright_foreground"]}"')
    lines.append("")
    for key in ["red", "yellow", "orange", "green", "cyan", "blue", "magenta", "brown"]:
        if key in data["colors"]:
            lines.append(f'{key} = "{data["colors"][key]}"')
    lines.append("")
    for key in ["bright_red", "bright_yellow", "bright_green", "bright_cyan", "bright_blue", "bright_magenta"]:
        if key in data["colors"]:
            lines.append(f'{key} = "{data["colors"][key]}"')
    lines.append("")
    if "hyprland_active_border" in data["colors"]:
        lines.append(f'hyprland_active_border = "{data["colors"]["hyprland_active_border"]}"')
    return "\n".join(lines) + "\n"


def build_vscode_json(data):
    v = data["vscode"]
    return f'{{\n  "name": "{v["name"]}",\n  "extension": "{v["extension"]}"\n}}\n'


def build_neovim_lua(data):
    nv = data["neovim"]
    return f"""return {{
  {{
    "LazyVim/LazyVim",
    opts = {{
      colorscheme = "{nv}",
    }},
  }},
}}
"""


def main():
    dest_dirs = [
        os.path.expanduser("~/.config/omarchy/themes"),
        "/home/apravint/iram-os/themes",
        "/home/apravint/iram-os/config/iram/themes"
    ]
    for d in dest_dirs:
        os.makedirs(d, exist_ok=True)

    print("🎨 Generating 8 Modern Curated Themes...")
    for theme_id, data in THEMES.items():
        print(f"\n✨ Building: {data['title']} ({theme_id})")

        # 1. Render Wallpaper (3840x2160)
        print("  -> Rendering Ultra-HD 4K Wallpaper (3840x2160)...")
        wall_img = generate_wallpaper(theme_id, data, width=3840, height=2160)

        # 2. Render Preview Card (1800x1012)
        print("  -> Rendering Acrylic Preview Card (1800x1012)...")
        prev_img = generate_preview_card(theme_id, data, wall_img)

        # Temporary local save
        tmp_dir = f"/tmp/iram_theme_{theme_id}"
        os.makedirs(os.path.join(tmp_dir, "backgrounds"), exist_ok=True)

        wall_path = os.path.join(tmp_dir, "backgrounds", "1-wallpaper.webp")
        wall_img.save(wall_path, "WEBP", quality=92)

        prev_path = os.path.join(tmp_dir, "preview.png")
        prev_img.save(prev_path, "PNG", optimize=True)

        # Unlock preview copies
        shutil.copyfile(prev_path, os.path.join(tmp_dir, "preview-unlock.png"))
        shutil.copyfile(prev_path, os.path.join(tmp_dir, "unlock.png"))

        # Metadata files
        with open(os.path.join(tmp_dir, "colors.toml"), "w") as f:
            f.write(build_colors_toml(data))
        with open(os.path.join(tmp_dir, "icons.theme"), "w") as f:
            f.write("Papirus-Dark\n")
        with open(os.path.join(tmp_dir, "chromium.theme"), "w") as f:
            f.write(f'{data["colors"]["accent"]}\n')
        with open(os.path.join(tmp_dir, "vscode.json"), "w") as f:
            f.write(build_vscode_json(data))
        with open(os.path.join(tmp_dir, "neovim.lua"), "w") as f:
            f.write(build_neovim_lua(data))

        # Copy to destination directories
        for base_dest in dest_dirs:
            target_theme_dir = os.path.join(base_dest, theme_id)
            if os.path.islink(target_theme_dir):
                os.unlink(target_theme_dir)
            elif os.path.isdir(target_theme_dir):
                shutil.rmtree(target_theme_dir)
            shutil.copytree(tmp_dir, target_theme_dir)
            print(f"  -> Installed to {target_theme_dir}")

        shutil.rmtree(tmp_dir)

    print("\n✅ All 8 modern themes successfully generated and installed!")


if __name__ == "__main__":
    main()
