"""FINAL card: confirmed front (blue bar LEFT) + back (blue bar RIGHT, same slant -> one continuous bar when flipped).
Back arrangement = icon column (variant A), mirrored. Services appear on the FRONT only."""
import json
from build_backs import *            # fs (front), band_r, irow, addr, ic, qr, T, mark, th, LOGO ...
X = L                                  # content starts at the left safe margin (mirror of front's right margin)
QRX = (W - X0) - 0.80                  # QR right edge = mirror of the front's left content edge
LEGAL = "SageRank Software Solutions FZ-LLC"      # from the RAKEZ Certificate of Incorporation
def row2(x, y, name, txt, size, w=500):            # icon scaled to the text size
    si = size*1.44; return ic(name, x, y-1.15*size, si) + T(x+si+0.07, y, size, txt, INK, w)
back = band_r + mark(X, 0.425, 0.19, LOGO)
back += T(X, 0.815, 0.17, C["name"], INK, 800, ls=-0.004) + T(X, 0.92, 0.066, C["title"], BLUE, 700, ls=0.03)
back += row2(X, 1.105, "mail", C["email"], 0.088, 600) + row2(X, 1.225, "phone", C["phone"], 0.088, 600) + row2(X, 1.345, "globe", WEB, 0.088, 600)
si = 0.076*1.44; tx = X + si + 0.07
back += ic("pin", X, 1.545-1.15*0.076, si) + T(tx, 1.545, 0.076, LEGAL, INK, 700)
back += T(tx, 1.65, 0.076, "CWEP8274, Compass Building, Al Shohada Road,", INK, 400) + T(tx, 1.755, 0.076, "Al Hamra Industrial Zone-FZ, Ras Al Khaimah, UAE", INK, 400)
back += qr(QRX, 0.50, 0.80, 0.053, th) + T(QRX+0.40, 1.40, 0.064, "SCAN TO CONNECT", GREY, 700, "middle", 0.03)
json.dump(dict(front=svg(fs, "#fff"), back=svg(back, "#fff"), front_p=svg(fs, "#fff", True), back_p=svg(back, "#fff", True)), open("final/FINAL/meta.json", "w"))
