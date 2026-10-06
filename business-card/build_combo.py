"""Combo: front of 05-pillars + back of 02-slant-panel, unified by the slanted blue edge."""
import json
from build_final import *
X0 = B + 0.55
band = f'<polygon points="0,0 {B+0.30},0 {B+0.18},{H} 0,{H}" fill="{BLUE}"/>'
def front():
    h = 0.60
    s = band + mark(X0, 0.52, h, LOGO) + wm(X0+MW(h)+0.14, 0.93, 0.30, INK, BLUE) + T(X0, 1.25, 0.062, C["tag"], GREY, 600, ls=0.01)
    s += hl(X0, 1.41, R-X0, BLUE, 0.014)
    for i, (hd, ds) in enumerate(SERV):
        x = X0 + 0.98*i
        s += T(x, 1.62, 0.088, hd, INK, 800, ls=0.03) + T(x, 1.735, 0.052, ds, GREY, 500)
    return s
fs, bs = front(), b2(th)
json.dump(dict(front=svg(fs, "#fff"), back=svg(bs, "#fff"), front_p=svg(fs, "#fff", True), back_p=svg(bs, "#fff", True)), open("final/combo/meta.json", "w"))
