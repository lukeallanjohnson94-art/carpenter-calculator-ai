"""
Generates the 1024x1024 High-DPI Bespoke Studio Emblem & 7-Layer LANCZOS Multi-Resolution .ico
for CutCoach AI (Warm Obsidian #131210 + Daylight Linen #F5F1EA + Burnt Copper #C86D2D + Warm Bronze #9B7A49 + Brass #D4AF37).
"""
from __future__ import annotations
import math
import pathlib
from PIL import Image, ImageDraw, ImageFilter

WORKSPACE = pathlib.Path(r"H:\My Drive\APEX\05_Active\personal\INSYGHT DIGITAL\CARPENTER-CALCULATOR-AI")
DIST_DIR = WORKSPACE / "dist"
BRAND_ICONS_DIR = pathlib.Path(r"H:\My Drive\APEX\03_Harness\agent-governance\brand-icons")
BRAIN_DIR = pathlib.Path(r"C:\Users\luke\.gemini\antigravity\brain\035237ef-668a-4b2b-ae07-abfbece05c83")


def generate_cutcoach_icon() -> dict:
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    BRAND_ICONS_DIR.mkdir(parents=True, exist_ok=True)
    BRAIN_DIR.mkdir(parents=True, exist_ok=True)

    # Render at 2048x2048 supersampled resolution for razor-sharp anti-aliased geometry
    ss = 2048
    img = Image.new("RGBA", (ss, ss), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    pad = 44
    radius = 420

    # 1. Outer Squircle Base (Warm Obsidian #131210 -> #1C1A17 subtle vertical gradient)
    mask = Image.new("L", (ss, ss), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle([pad, pad, ss - 1 - pad, ss - 1 - pad], radius=radius, fill=255)

    bg = Image.new("RGBA", (ss, ss), (19, 18, 16, 255))
    bg_draw = ImageDraw.Draw(bg)
    for y in range(pad, ss - pad, 4):
        t = (y - pad) / float(ss - 2 * pad)
        r = int(28 * (1 - t) + 17 * t)
        g = int(25 * (1 - t) + 16 * t)
        b = int(22 * (1 - t) + 14 * t)
        bg_draw.line([(pad, y), (ss - pad, y)], fill=(r, g, b, 255), width=4)

    # Subtle blueprint grid inside the squircle
    grid_step = 96
    for gx in range(pad + 64, ss - pad - 64, grid_step):
        bg_draw.line([(gx, pad + 64), (gx, ss - pad - 64)], fill=(155, 122, 73, 24), width=2)
    for gy in range(pad + 64, ss - pad - 64, grid_step):
        bg_draw.line([(pad + 64, gy), (ss - pad - 64, gy)], fill=(155, 122, 73, 24), width=2)

    img.paste(bg, (0, 0), mask)
    draw = ImageDraw.Draw(img)

    # 2. Concentric Recessed Instrument Well
    cx, cy = ss // 2, ss // 2
    well_r = 760
    draw.ellipse(
        [cx - well_r, cy - well_r, cx + well_r, cy + well_r],
        fill=(15, 14, 12, 235),
        outline=(155, 122, 73, 180),
        width=10,
    )
    draw.ellipse(
        [cx - well_r - 22, cy - well_r - 22, cx + well_r + 22, cy + well_r + 22],
        outline=(200, 109, 45, 110),
        width=6,
    )

    # 3. Precision Degree Protractor / Drop-Saw Turntable Ticks around perimeter
    for deg in range(0, 360, 5):
        rad = math.radians(deg)
        is_major = (deg % 15 == 0)
        r_outer = well_r - 24
        r_inner = well_r - (72 if is_major else 44)
        x1 = cx + r_inner * math.cos(rad)
        y1 = cy + r_inner * math.sin(rad)
        x2 = cx + r_outer * math.cos(rad)
        y2 = cy + r_outer * math.sin(rad)
        col = (212, 175, 55, 220) if is_major else (155, 122, 73, 130)
        draw.line([(x1, y1), (x2, y2)], fill=col, width=(8 if is_major else 4))

    # 4. Helical / Kerf-Slotted Timber Arc (Upper-Right Sweeping Arch)
    arc_bbox = [cx - 590, cy - 590, cx + 590, cy + 590]
    draw.arc(arc_bbox, start=200, end=350, fill=(200, 109, 45, 255), width=92)
    inner_arc_bbox = [cx - 510, cy - 510, cx + 510, cy + 510]
    draw.arc(inner_arc_bbox, start=200, end=350, fill=(245, 241, 234, 235), width=18)

    # Radial Kerf-Bending Slots cut into the Copper Timber Arch
    for k_deg in range(210, 345, 12):
        krad = math.radians(k_deg)
        kx1 = cx + 505 * math.cos(krad)
        ky1 = cy + 505 * math.sin(krad)
        kx2 = cx + 578 * math.cos(krad)
        ky2 = cy + 578 * math.sin(krad)
        draw.line([(kx1, ky1), (kx2, ky2)], fill=(19, 18, 16, 255), width=14)

    # 5. Hero Anodized Brass & Burnt Copper Speed-Square / Framing Rafter Triangle
    # Triangle vertices representing Run, Rise, and Rafter Hypotenuse with Birdsmouth Notch
    p_left = (cx - 470, cy + 390)
    p_right = (cx + 430, cy + 390)
    p_top = (cx + 430, cy - 410)

    # Outer solid framing square body
    poly_outer = [
        p_left,
        (cx - 210, cy + 390),
        # Birdsmouth heel/seat notch sculpted into bottom chord
        (cx - 210, cy + 325),
        (cx - 95, cy + 325),
        (cx - 95, cy + 390),
        p_right,
        p_top,
    ]
    draw.polygon(poly_outer, fill=(212, 175, 55, 255), outline=(245, 241, 234, 240))

    # Inner recessed triangle cutout (Warm Obsidian interior)
    poly_inner = [
        (cx - 195, cy + 255),
        (cx + 295, cy + 255),
        (cx + 295, cy - 180),
    ]
    draw.polygon(poly_inner, fill=(19, 18, 16, 255), outline=(200, 109, 45, 255))

    # Speed-square hip/valley slot cutout
    slot_pts = [
        (cx - 35, cy + 205),
        (cx + 225, cy - 25),
        (cx + 225, cy + 35),
        (cx + 25, cy + 205),
    ]
    draw.polygon(slot_pts, fill=(200, 109, 45, 255))

    # 6. Laser-Crisp Daylight Linen (#F5F1EA) Plumb & Mitre Saw Reticle Node
    node_x, node_y = cx - 95, cy + 325
    draw.ellipse(
        [node_x - 36, node_y - 36, node_x + 36, node_y + 36],
        fill=(224, 123, 57, 255),
        outline=(245, 241, 234, 255),
        width=10,
    )

    # 7. Concentric Squircle Outer Rim (Burnt Copper #C86D2D + Warm Bronze #9B7A49)
    draw.rounded_rectangle(
        [pad, pad, ss - 1 - pad, ss - 1 - pad],
        radius=radius,
        outline=(200, 109, 45, 250),
        width=30,
    )
    draw.rounded_rectangle(
        [pad + 28, pad + 28, ss - 1 - (pad + 28), ss - 1 - (pad + 28)],
        radius=radius - 24,
        outline=(155, 122, 73, 200),
        width=12,
    )

    # Downsample via LANCZOS to 1024x1024
    final_1024 = img.resize((1024, 1024), Image.Resampling.LANCZOS)

    png_dist = DIST_DIR / "CutCoachAI_1024.png"
    ico_dist = DIST_DIR / "CutCoachAI.ico"
    png_brand = BRAND_ICONS_DIR / "CutCoachAI_1024.png"
    jpg_brand = BRAND_ICONS_DIR / "CutCoachAI_1024_master.jpg"
    png_brain = BRAIN_DIR / "CutCoachAI_1024.png"

    final_1024.save(png_dist, format="PNG", optimize=True)
    final_1024.save(png_brand, format="PNG", optimize=True)
    final_1024.save(png_brain, format="PNG", optimize=True)
    final_1024.convert("RGB").save(jpg_brand, format="JPEG", quality=96)

    ico_base = final_1024.resize((256, 256), Image.Resampling.LANCZOS).filter(
        ImageFilter.UnsharpMask(radius=1.1, percent=115, threshold=2)
    )
    ico_sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (24, 24), (16, 16)]
    ico_base.save(ico_dist, format="ICO", sizes=ico_sizes)

    return {
        "ok": True,
        "png_1024": str(png_dist),
        "ico_multi": str(ico_dist),
        "brain_preview": str(png_brain),
        "sizes": ico_sizes,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(generate_cutcoach_icon(), indent=2))
