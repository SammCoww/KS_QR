import os
import sys
from datetime import datetime

import qrcode
from PIL import ImageDraw, ImageFont

RED, GREEN = "#BF0D3E", "#215732"


def make_qr(link):
    # H correction survives ~30% damage, so the center logo stays scannable
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20)
    qr.add_data(link)
    img = qr.make_image().convert("RGB")

    code = qr.modules_count * qr.box_size  # code area without the quiet-zone border
    c = img.size[0] // 2
    bw, bh = int(code * 0.36), int(code * 0.22)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((c - bw // 2, c - bh // 2, c + bw // 2, c + bh // 2), radius=bh // 5, fill="white")
    font = ImageFont.truetype("verdanab.ttf", int(bh * 0.9))
    gap = bh // 20
    draw.text((c - gap, c), "Κ", font=font, fill=RED, anchor="rm")  # Kappa
    draw.text((c + gap, c), "Σ", font=font, fill=GREEN, anchor="lm")  # Sigma
    return img


if __name__ == "__main__":
    link = input("Enter link: ").strip()
    if not link:
        input("No link entered. Press Enter to close...")
        sys.exit(1)
    # shortcut: assumes Downloads is in its default spot, read the User Shell Folders registry key if anyone has moved it
    out = os.path.join(os.path.expanduser("~"), "Downloads", f"ks_qr_{datetime.now():%Y%m%d_%H%M%S}.png")
    make_qr(link).save(out)
    print("Saved", out)
    os.startfile(out)
    input("Press Enter to close...")
