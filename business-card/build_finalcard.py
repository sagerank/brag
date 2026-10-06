"""FINAL card: confirmed front (blue bar LEFT) + back (blue bar RIGHT, same slant -> one continuous bar when flipped).
Back arrangement = icon column (variant A), mirrored. Services appear on the FRONT only."""
import json
from build_backs import *            # fs (front), band_r, irow, addr, ic, qr, T, mark, th, LOGO ...
X = L                                  # content starts at the left safe margin (mirror of front's right margin)
QRX = (W - X0) - 0.84                  # QR right edge = mirror of the front's left content edge
back = band_r + mark(X, 0.45, 0.26, LOGO)
back += T(X, 0.93, 0.17, C["name"], INK, 800, ls=-0.004) + T(X, 1.05, 0.052, C["title"], BLUE, 700, ls=0.03)
back += irow(X, 1.25, "mail", C["email"], w=600) + irow(X, 1.365, "phone", C["phone"], w=600) + irow(X, 1.48, "globe", WEB, w=600)
back += addr(X, 1.605, size=0.060, step=0.088)
back += qr(QRX, 0.62, 0.84, 0.055, th) + T(QRX+0.42, 1.60, 0.046, "SCAN TO CONNECT", GREY, 700, "middle", 0.03)
json.dump(dict(front=svg(fs, "#fff"), back=svg(back, "#fff"), front_p=svg(fs, "#fff", True), back_p=svg(back, "#fff", True)), open("final/FINAL/meta.json", "w"))
