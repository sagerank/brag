"""FINAL card: confirmed front (blue bar LEFT) + back (blue bar RIGHT, same slant -> one continuous bar when flipped).
Back arrangement = icon column (variant A), mirrored. Services appear on the FRONT only."""
import json
from build_backs import *            # fs (front), band_r, irow, addr, ic, qr, T, mark, th, LOGO ...
X = L                                  # content starts at the left safe margin (mirror of front's right margin)
QRX = (W - X0) - 0.84                  # QR right edge = mirror of the front's left content edge
from inkalign import lsb, icon_x
LEGAL = "SageRank Software Solutions FZ-LLC"      # from the RAKEZ Certificate of Incorporation
E = X                                  # ONE left edge: logo, name, title and icons all start their ink exactly here
IS = 0.095                             # one icon size for every row
TXT = E + 0.165                        # ONE text edge for every contact / address line
def TI(x, y, size, txt, fill, w=500, **k): return T(x - lsb(txt[0], w, size), y, size, txt, fill, w, **k)   # ink-aligned text
def crow(y, name, txt, size, w): return ic(name, icon_x(name, E, IS), y-0.076, IS) + TI(TXT, y, size, txt, INK, w)
back = band_r + mark(E, 0.42, 0.24, LOGO)
back += TI(E, 0.88, 0.17, C["name"], INK, 800, ls=-0.004) + TI(E, 1.00, 0.052, C["title"], BLUE, 700, ls=0.03)
back += crow(1.18, "mail", C["email"], 0.066, 600) + crow(1.29, "phone", C["phone"], 0.066, 600) + crow(1.40, "globe", WEB, 0.066, 600)
y0 = 1.535
back += crow(y0, "pin", LEGAL, 0.058, 700)
for i, l in enumerate(C["addr"]): back += TI(TXT, y0+0.088*(i+1), 0.058, l, INK, 400)
back += qr(QRX, 0.62, 0.84, 0.055, th) + T(QRX+0.42, 1.60, 0.046, "SCAN TO CONNECT", GREY, 700, "middle", 0.03)
json.dump(dict(front=svg(fs, "#fff"), back=svg(back, "#fff"), front_p=svg(fs, "#fff", True), back_p=svg(back, "#fff", True)), open("final/FINAL/meta.json", "w"))
