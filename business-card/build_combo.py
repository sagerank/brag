"""Combo: front of 05-pillars + back of 02-slant-panel, unified by the slanted blue edge."""
import json
from build_final import *
X0 = B + 0.55
band = f'<polygon points="0,0 {B+0.30},0 {B+0.18},{H} 0,{H}" fill="{BLUE}"/>'
SERV4 = [("SEO", "Search Engine", "Optimization"), ("AEO", "Answer Engine", "Optimization"),
         ("GEO", "Generative Engine", "Optimization"), ("SECURITY", "Domain", "Security")]
def front():
    h = 0.52
    s = band + mark(X0, 0.46, h, LOGO) + wm(X0+MW(h)+0.13, 0.815, 0.26, INK, BLUE)
    s += T(X0, 1.12, 0.078, C["tag"], GREY, 600, ls=0.012)
    s += hl(X0, 1.22, R-X0, BLUE, 0.014)
    cells = [(0, 0, "SEO", "Search Engine Optimization"), (1, 0, "AEO", "Answer Engine Optimization"),
             (0, 1, "GEO", "Generative Engine Optimization"), (1, 1, "SECURITY", "Domain Security")]
    for cx, cy, hd, ds in cells:
        x = X0 + 1.38*cx; y = 1.43 + 0.27*cy
        s += T(x, y, 0.095, hd, INK, 800, ls=0.02) + T(x, y+0.10, 0.076, ds, GREY, 500)
    return s
fs, bs = front(), b2(th)
json.dump(dict(front=svg(fs, "#fff"), back=svg(bs, "#fff"), front_p=svg(fs, "#fff", True), back_p=svg(bs, "#fff", True)), open("final/combo/meta.json", "w"))
