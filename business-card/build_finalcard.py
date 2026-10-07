"""FINAL card: confirmed front (blue bar LEFT) + back (blue bar RIGHT, same slant -> one continuous bar when flipped).
Back arrangement = icon column (variant A), mirrored. Services appear on the FRONT only."""
import json
from build_backs import *            # fs (front), band_r, irow, addr, ic, qr, T, mark, th, LOGO ...
X = L                                  # content starts at the left safe margin (mirror of front's right margin)
QRX = (W - X0) - 0.84                  # QR right edge = mirror of the front's left content edge
from inkalign import lsb, icon_x, text_width
LEGAL = "SageRank Software Solutions FZ-LLC"      # from the RAKEZ Certificate of Incorporation
E = X                                  # ONE left edge: logo, name, title, hairline and icons start their ink exactly here
IS = 0.095                             # one icon size for every row
TXT = E + 0.165                        # ONE text edge for every contact / address line
PITCH = 0.115                          # ONE vertical pitch between the four icons (mail, phone, web, address)
Y1 = 1.215                             # baseline of the first row
def TI(x, y, size, txt, fill, w=500, **k): return T(x - lsb(txt[0], w, size), y, size, txt, fill, w, **k)   # ink-aligned text
def crow(y, name, txt, size, w): return ic(name, icon_x(name, E, IS), y-0.076, IS) + TI(TXT, y, size, txt, INK, w)
lines = [(C["email"], 0.066, 600), (C["phone"], 0.066, 600), (WEB, 0.066, 600), (LEGAL, 0.058, 700)] + [(l, 0.058, 400) for l in C["addr"]]
RIGHT = TXT + max(text_width(s, w, z) for s, z, w in lines)       # right edge of the widest line -> the hairline ends exactly there
back = band_r + mark(E, 0.425, 0.20, LOGO)
back += TI(E, 0.86, 0.17, C["name"], INK, 800, ls=-0.004) + TI(E, 1.00, 0.056, C["title"], BLUE, 700, ls=0.02)
back += hl(E, 1.075, RIGHT - E)                                      # option 1: hairline under the title
for i, (nm, txt, z, w) in enumerate([("mail", C["email"], 0.066, 600), ("phone", C["phone"], 0.066, 600), ("globe", WEB, 0.066, 600), ("pin", LEGAL, 0.058, 700)]):
    back += crow(Y1 + PITCH*i, nm, txt, z, w)
for i, l in enumerate(C["addr"]): back += TI(TXT, Y1 + PITCH*3 + 0.086*(i+1), 0.058, l, INK, 400)
back += qr(QRX, 0.62, 0.84, 0.055, th) + T(QRX+0.42, 1.60, 0.046, "SCAN TO CONNECT", GREY, 700, "middle", 0.03)
json.dump(dict(front=svg(fs, "#fff"), back=svg(back, "#fff"), front_p=svg(fs, "#fff", True), back_p=svg(back, "#fff", True)), open("final/FINAL/meta.json", "w"))
