"""5 alternative treatments of the name / title block on the back. Only this block changes."""
import json
from build_backs import *            # fs, band_r, ic, qr, T, mark, th, LOGO, WEB, hl, HAIR, C, INK, BLUE, GREY, W, H, X0, L ...
from inkalign import lsb, icon_x
E = L; IS = 0.095; TXT = E + 0.165; QRX = (W - X0) - 0.84
LEGAL = "SageRank Software Solutions FZ-LLC"
def TI(x, y, size, txt, fill, w=500, **k): return T(x - lsb(txt[0], w, size), y, size, txt, fill, w, **k)
def crow(y, name, txt, size, w): return ic(name, icon_x(name, E, IS), y-0.076, IS) + TI(TXT, y, size, txt, INK, w)
def lower(rows_y, y0, step):
    s = crow(rows_y[0], "mail", C["email"], 0.066, 600) + crow(rows_y[1], "phone", C["phone"], 0.066, 600) + crow(rows_y[2], "globe", WEB, 0.066, 600)
    s += crow(y0, "pin", LEGAL, 0.058, 700)
    for i, l in enumerate(C["addr"]): s += TI(TXT, y0+step*(i+1), 0.058, l, INK, 400)
    return s
def right(): return qr(QRX, 0.62, 0.84, 0.055, th) + T(QRX+0.42, 1.60, 0.046, "SCAN TO CONNECT", GREY, 700, "middle", 0.03)
base = lambda: band_r + mark(E, 0.425, 0.20, LOGO)
def v1():  # title under name, hairline under title
    return (base() + TI(E, 0.86, 0.17, C["name"], INK, 800, ls=-0.004) + TI(E, 1.00, 0.056, C["title"], BLUE, 700, ls=0.02)
            + hl(E, 1.075, 1.75) + lower((1.205, 1.31, 1.415), 1.555, 0.086) + right())
def v2():  # title under name, short blue accent rule
    return (base() + TI(E, 0.86, 0.17, C["name"], INK, 800, ls=-0.004) + TI(E, 1.00, 0.056, C["title"], BLUE, 700, ls=0.02)
            + f'<rect x="{E}" y="1.06" width="0.30" height="0.02" fill="{BLUE}"/>' + lower((1.205, 1.31, 1.415), 1.555, 0.086) + right())
def v3():  # title ABOVE the name (eyebrow)
    return (base() + TI(E, 0.76, 0.056, C["title"], BLUE, 700, ls=0.02) + TI(E, 0.99, 0.17, C["name"], INK, 800, ls=-0.004)
            + lower((1.20, 1.305, 1.41), 1.55, 0.086) + right())
def v4():  # soft sentence-case title, more air, no rule
    return (base() + TI(E, 0.86, 0.17, C["name"], INK, 800, ls=-0.004) + TI(E, 1.005, 0.078, "Founder & CEO", BLUE, 600, ls=0.004)
            + lower((1.20, 1.31, 1.42), 1.55, 0.086) + right())
def v5():  # eyebrow above + hairline below the name
    return (base() + TI(E, 0.76, 0.056, C["title"], BLUE, 700, ls=0.02) + TI(E, 0.99, 0.17, C["name"], INK, 800, ls=-0.004)
            + hl(E, 1.065, 1.75) + lower((1.215, 1.32, 1.425), 1.565, 0.085) + right())
V = [("1 Title under name + hairline", v1), ("2 Title under name + blue accent rule", v2), ("3 Title above name", v3), ("4 Soft sentence-case title", v4), ("5 Title above + hairline", v5)]
json.dump([dict(key=k, back_p=svg(f(), "#fff", True), back=svg(f(), "#fff")) for k, f in V], open("final/header-options/meta.json", "w"))
