"""Final 5 patterns (all white, official logo, no boxes). python3 build_final.py && node final2.mjs"""
import json
from build25 import *          # helpers, brand constants, f1/b1/f2/b2 (patterns 1 & 2)
th = THEMES["light"]; GREY = "#5B6676"; HAIR = "#D3DAE6"
def hl(x, y, w, col=HAIR, h=0.008): return f'<rect x="{x:.3f}" y="{y:.3f}" width="{w:.3f}" height="{h}" fill="{col}"/>'
def vl(x, y, h, col=HAIR, w=0.008): return f'<rect x="{x:.3f}" y="{y:.3f}" width="{w}" height="{h:.3f}" fill="{col}"/>'
bar_b = f'<rect y="{H-0.215}" width="{W}" height="0.215" fill="{BLUE}"/>'
bar_t = f'<rect y="0" width="{W}" height="0.215" fill="{BLUE}"/>'
SERV = [("AEO", "Answer Engine Optimization"), ("GEO", "Generative Engine Optimization"), ("SECURITY", "Domain Security")]
CX = W/2

# ---- 03 CLASSIC: centred stack, blue base bar ----
def f3n():
    h = 0.56
    return (bar_b + mark(CX-MW(h)/2, 0.45, h, LOGO) + wm(CX, 1.31, 0.27, INK, BLUE, "middle") + hl(CX-0.25, 1.40, 0.5, BLUE, 0.016)
            + T(CX, 1.545, 0.056, "AI SEARCH VISIBILITY  ·  DOMAIN SECURITY", INK, 700, "middle", 0.018)
            + T(CX, 1.71, 0.056, C["tag"], GREY, 600, "middle", 0.012))
def b3n():
    s = bar_b + mark(L, TOP, 0.26, LOGO) + qr(R-0.55, TOP, 0.55, 0.04, th)
    s += T(CX, 0.98, 0.17, C["name"], INK, 800, "middle", -0.004) + T(CX, 1.09, 0.052, C["title"], BLUE, 700, "middle", 0.03)
    s += hl(CX-0.25, 1.15, 0.5) + T(CX, 1.26, 0.056, "AEO  ·  GEO  ·  DOMAIN SECURITY", INK, 700, "middle", 0.02)
    s += T(CX, 1.42, 0.068, f'{C["email"]}   |   {C["phone"]}', INK, 600, "middle")
    for i, l in enumerate(C["addr"]): s += T(CX, 1.54+0.09*i, 0.056, l, GREY, 500, "middle")
    return s

# ---- 04 SERVICES-FRONT: logo left, hairline, services list right ----
def f4n():
    h = 0.60
    s = bar_t + mark(L, 0.58, h, LOGO) + wm(L, 1.50, 0.265, INK, BLUE)
    s += T(L, 1.665, 0.052, C["tag1"], GREY, 600) + T(L, 1.735, 0.052, C["tag2"], GREY, 600)
    s += vl(1.98, 0.56, 1.20)
    for i, (hd, ds) in enumerate(SERV):
        y = 0.80 + 0.37*i
        s += T(2.16, y, 0.105, hd, BLUE, 800, ls=0.02) + T(2.16, y+0.115, 0.054, ds, INK, 500)
    return s
def b4n():
    s = bar_t + mark(L, 0.45, 0.24, LOGO) + T(L, 0.93, 0.17, C["name"], INK, 800, ls=-0.004) + T(L, 1.05, 0.052, C["title"], BLUE, 700, ls=0.03)
    s += contacts(L, 1.25, th)
    s += qr(R-0.82, 0.62, 0.82, 0.055, th, C["web"], INK)
    return s

# ---- 05 PILLARS: lockup top-left, hairline, three service columns ----
def f5n():
    h = 0.60
    s = mark(L, 0.52, h, LOGO) + wm(L+MW(h)+0.14, 0.93, 0.30, INK, BLUE) + T(L, 1.25, 0.062, C["tag"], GREY, 600, ls=0.01)
    s += hl(L, 1.41, R-L, BLUE, 0.014)
    for i, (hd, ds) in enumerate(SERV):
        x = L + 0.98*i
        s += T(x, 1.62, 0.088, hd, INK, 800, ls=0.03) + T(x, 1.735, 0.052, ds, GREY, 500)
    return s
def b5n():
    X = 1.68
    s = bar_t + mark(L, 0.45, 0.24, LOGO) + qr(L-0.03, 0.82, 0.80, 0.055, th, None)
    s += T(L-0.03+0.40, 1.78, 0.044, C["web"], GREY, 700, "middle", 0.03)
    s += T(X, 0.73, 0.17, C["name"], INK, 800, ls=-0.004) + T(X, 0.85, 0.052, C["title"], BLUE, 700, ls=0.03) + hl(X, 0.92, 0.3, INK, 0.012)
    s += contacts(X, 1.08, th, 0.11, size=0.064)
    s += T(X, 1.72, 0.054, "AEO  ·  GEO  ·  Domain Security", INK, 700)
    return s

PATTERNS = [("01-diagonal", f1, b1), ("02-slant-panel", f2, b2), ("03-classic", f3n, b3n), ("04-services", f4n, b4n), ("05-pillars", f5n, b5n)]
meta = []
for k, ff, bf in PATTERNS:
    fa = ff(th) if ff in (f1, f2) else ff(); ba = bf(th) if bf in (b1, b2) else bf()
    meta.append(dict(key=k, front=svg(fa, "#fff"), back=svg(ba, "#fff"), front_p=svg(fa, "#fff", True), back_p=svg(ba, "#fff", True)))
json.dump(meta, open("final/meta.json", "w")); print(len(meta), "patterns")
