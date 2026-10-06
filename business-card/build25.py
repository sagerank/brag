"""25 SageRank card designs: 5 layouts x 5 colour treatments.  python3 build25.py && node render25.mjs"""
import segno, math, json, os
C = dict(name="Veera Venkatesh", title="FOUNDER & CEO", email="veer@sagerank.io", phone="+971 56 801 5996",
         addr=["CWEP8274, Compass Building, Al Shohada Road", "Al Hamra Industrial Zone-FZ", "Ras Al Khaimah, United Arab Emirates"],
         tag="Rise with Authority, Secure with Dominance", tag1="Rise with Authority,", tag2="Secure with Dominance",
         url="https://sagerank.io", web="SAGERANK.IO")
BLUE, INK, NAVY, LBLUE = "#1d70d1", "#0B0F17", "#0A1220", "#3B8BEB"
B = 0.125; W, H = 3.5 + 2*B, 2.0 + 2*B
L, R, TOP, BOT = B+0.3, W-B-0.3, B+0.3, H-B-0.3        # safe box (0.3in inside trim)
ANG = math.degrees(math.atan(184/414))                  # logo's own diagonal

THEMES = {
 "light":   dict(bg="#fff", fg=INK, sub="#5B6676", acc=BLUE, rank=BLUE, logo=(BLUE,"#000","#fff"), tile="#fff",
                 stripe=INK, wedge=BLUE, panel=BLUE, plogo=("#fff",INK,BLUE), pstripe=INK, pwedge="#4E90DE", pfg="#fff", psub="#DCE9F9"),
 "blue":    dict(bg=BLUE, fg="#fff", sub="#D6E6FA", acc="#fff", rank=INK, logo=("#fff",INK,BLUE), tile="#fff",
                 stripe=INK, wedge="#4A8DDB", panel=NAVY, plogo=(LBLUE,"#fff",NAVY), pstripe=LBLUE, pwedge="#16243A", pfg="#fff", psub="#9AA7B8"),
 "midnight":dict(bg=NAVY, fg="#fff", sub="#9AA7B8", acc=LBLUE, rank=LBLUE, logo=(LBLUE,"#fff",NAVY), tile="#fff",
                 stripe="#fff", wedge=BLUE, panel=BLUE, plogo=("#fff",INK,BLUE), pstripe=INK, pwedge="#4E90DE", pfg="#fff", psub="#DCE9F9"),
 "mist":    dict(bg="#EAF1FB", fg=INK, sub="#556070", acc=BLUE, rank=BLUE, logo=(BLUE,"#000","#EAF1FB"), tile="#fff",
                 stripe=INK, wedge=BLUE, panel=BLUE, plogo=("#fff",INK,BLUE), pstripe=INK, pwedge="#4E90DE", pfg="#fff", psub="#DCE9F9"),
}
VARIANTS = [("A-light", "light", "light"), ("B-blue", "blue", "blue"), ("C-midnight", "midnight", "midnight"),
            ("D-mist", "mist", "mist"), ("E-duo", "midnight", "light")]   # duo: dark front, light back

def qr_path(url, size):
    m = segno.make(url, error='h', micro=False).matrix; n = len(m); u = size/n; d = []
    for y, row in enumerate(m):
        x = 0
        while x < n:
            if row[x]:
                s = x
                while x < n and row[x]: x += 1
                d.append(f"M{s*u:.4f} {y*u:.4f}h{(x-s)*u:.4f}v{u:.4f}h{-(x-s)*u:.4f}z")
            else: x += 1
    return "".join(d)

def mark(x, y, h, cols):
    b, d, l = cols; s = h/828.0
    return (f'<g transform="translate({x:.4f} {y:.4f}) scale({s:.5f}) translate(-166.343 -86.038)">'
        f'<path d="M580.305,86.038l0,413.962l-413.962,183.983l0,-413.962l413.962,-183.983Z" fill="{b}"/>'
        f'<path d="M833.657,316.017l0,413.962l-413.962,183.983l0,-413.962l413.962,-183.983Z" fill="{b}"/>'
        f'<path d="M803.285,164.031l0,92.991l-474.707,210.981l0,-92.991l474.707,-210.981Z" fill="{d}"/>'
        f'<path d="M657.048,531.997l0,92.991l-474.707,210.981l0,-92.991l474.707,-210.981Z" fill="{d}"/>'
        f'<path d="M657.048,619.822l0,-89.575l-328.47,-145.987l0,89.575l328.47,145.987Z" fill="{l}"/></g>')
MW = lambda h: h*667.314/828.0

def corner(pos, stripe, wedge, d=0.55, clip="cv"):
    """diagonal stripe+wedge at the logo's angle, cutting a canvas corner ('br' or 'tl')"""
    if pos == "br":
        g = f'<g transform="translate({W} {H-d}) rotate({-ANG})"><rect x="-4" y="0" width="5" height="0.05" fill="{stripe}"/><rect x="-4" y="0.11" width="5" height="3" fill="{wedge}"/></g>'
    else:
        g = f'<g transform="translate(0 {d}) rotate({-ANG})"><rect x="-1" y="-0.05" width="5" height="0.05" fill="{stripe}"/><rect x="-1" y="-3.11" width="5" height="3" fill="{wedge}"/></g>'
    return f'<g clip-path="url(#{clip})">{g}</g>'

def T(x, y, size, txt, fill, w=500, anchor="start", ls=0, extra=""):
    return (f'<text x="{x:.3f}" y="{y:.3f}" font-family="Inter" font-weight="{w}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}" {extra}>{txt}</text>')
def wordmark(x, y, size, th, anchor="start"):
    return (f'<text x="{x:.3f}" y="{y:.3f}" text-anchor="{anchor}" font-family="Inter" font-weight="800" font-size="{size}" '
            f'letter-spacing="{-0.03*size:.4f}" fill="{th["fg"]}">Sage<tspan fill="{th["rank"]}">Rank</tspan></text>')
def row(x, y, label, val, th, w=500, size=0.066, fg=None, lab=None):
    return T(x, y, 0.05, label, lab or th["acc"], 800) + T(x+0.14, y, size, val, fg or th["fg"], w)
def contacts(x, y, th, step=0.11, fg=None, lab=None, size=0.066):
    s = row(x, y, "E", C["email"], th, 600, size, fg, lab) + row(x, y+step, "T", C["phone"], th, 600, size, fg, lab)
    ay = y + step*2 + 0.04
    s += row(x, ay, "A", C["addr"][0], th, 400, size, fg, lab)
    for i, l in enumerate(C["addr"][1:]):
        s += T(x+0.14, ay+0.095*(i+1), size, l, fg or th["fg"], 400)
    return s
def qr(x, y, tile, pad, th, caption=None, capfill=None, size=0.05):
    qs = tile - 2*pad
    s = f'<rect x="{x}" y="{y}" width="{tile}" height="{tile}" rx="0.06" fill="{th["tile"]}"/>'
    s += f'<g transform="translate({x+pad} {y+pad})"><path d="{qr_path(C["url"], qs)}" fill="{INK}"/></g>'
    if caption: s += T(x+tile/2, y+tile+0.16, size, caption, capfill or th["fg"], 700, "middle", 0.03)
    return s
def svg(inner, bg, preview=False):
    vb = f"{B} {B} 3.5 2" if preview else f"0 0 {W} {H}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{3.5 if preview else W}in" height="{2 if preview else H}in">'
            f'<defs><clipPath id="cv"><rect width="{W}" height="{H}"/></clipPath></defs><rect width="{W}" height="{H}" fill="{bg}"/>{inner}</svg>')

# ---------------- 1 DIAGONAL (the one you liked) ----------------
def f1(th):
    return (f'{corner("br", th["stripe"], th["wedge"])}{mark(W/2-1.01, H/2-0.60, 0.80, th["logo"])}'
            + wordmark(W/2-0.29, H/2-0.11, 0.30, th)
            + T(W/2-1.01, H/2+0.46, 0.066, C["tag"], th["sub"], 600, extra='textLength="2.156" lengthAdjust="spacing"'))
def b1(th):
    PX = B+2.25; tile = 0.86; tx = PX+(W-B-PX-tile)/2
    s = f'<rect x="{PX}" width="{W-PX}" height="{H}" fill="{th["panel"]}"/><clipPath id="pn"><rect x="{PX}" width="{W-PX}" height="{H}"/></clipPath>'
    s += corner("br", th["pstripe"], th["pwedge"], 0.45, "pn")
    s += mark(L, TOP, 0.30, th["logo"]) + T(L, B+0.92, 0.15, C["name"], th["fg"], 800, ls=-0.004) + T(L, B+1.05, 0.052, C["title"], th["acc"], 700, ls=0.03)
    s += f'<rect x="{L}" y="{B+1.13}" width="0.28" height="0.012" fill="{th["fg"]}"/>' + contacts(L, B+1.28, th)
    s += qr(tx, B+0.50, tile, 0.055, th, C["web"], th["pfg"]) + T(tx+tile/2, B+0.50+tile+0.255, 0.04, "SCAN TO VISIT", th["psub"], 500, "middle", 0.03)
    return s

# ---------------- 2 SLANT PANEL ----------------
SK = 0.28
def f2(th):
    px = B+1.25
    s = f'<polygon points="0,0 {px+SK},0 {px},{H} 0,{H}" fill="{th["panel"]}"/>'
    h = 0.95; s += mark((px+SK/2)/2-MW(h)/2+0.02, H/2-h/2, h, th["plogo"])
    x0 = px+0.52
    s += wordmark(x0, H/2-0.04, 0.27, th) + f'<rect x="{x0}" y="{H/2+0.06}" width="0.30" height="0.02" fill="{th["acc"]}"/>'
    s += T(x0, H/2+0.27, 0.064, C["tag1"], th["sub"], 600) + T(x0, H/2+0.36, 0.064, C["tag2"], th["sub"], 600)
    return s
def b2(th):
    L2 = B+0.55
    s = f'<polygon points="0,0 {B+0.30},0 {B+0.18},{H} 0,{H}" fill="{th["panel"]}"/>'
    s += mark(L2, TOP, 0.30, th["logo"]) + T(L2, B+0.98, 0.15, C["name"], th["fg"], 800, ls=-0.004) + T(L2, B+1.10, 0.052, C["title"], th["acc"], 700, ls=0.03)
    s += contacts(L2, B+1.34, th)
    s += qr(R-0.80, TOP, 0.80, 0.055, th, C["web"], th["fg"], 0.045)
    return s

# ---------------- 3 MINIMAL MARK ----------------
def f3(th):
    h = 0.78
    return (mark(W/2-MW(h)/2, H/2-0.70, h, th["logo"]) + wordmark(W/2, H/2+0.40, 0.21, th, "middle")
            + T(W/2, H/2+0.575, 0.058, C["tag"], th["sub"], 600, "middle", 0.012))
def b3(th):
    s = mark(L, TOP, 0.30, th["logo"]) + qr(R-0.74, TOP, 0.74, 0.05, th)
    s += T(L, 1.32, 0.17, C["name"], th["fg"], 800, ls=-0.005) + T(L, 1.43, 0.052, C["title"], th["acc"], 700, ls=0.03)
    s += row(L, 1.62, "E", C["email"], th, 600) + row(L, 1.73, "T", C["phone"], th, 600)
    s += row(1.80, 1.62, "A", C["addr"][0].split(", Al Shohada")[0] + ",", th, 400, 0.058) if False else ""
    s += row(1.62, 1.585, "A", C["addr"][0], th, 400, 0.058) + T(1.76, 1.675, 0.058, C["addr"][1], th["fg"], 400) + T(1.76, 1.765, 0.058, C["addr"][2], th["fg"], 400)
    return s

# ---------------- 4 BOLD CROP ----------------
def f4(th):
    h = 2.4
    s = mark(2.02, (H-h)/2, h, th["logo"])
    s += wordmark(L, H/2-0.02, 0.30, th) + f'<rect x="{L}" y="{H/2+0.10}" width="0.30" height="0.02" fill="{th["acc"]}"/>'
    s += T(L, H/2+0.32, 0.066, C["tag1"], th["sub"], 600) + T(L, H/2+0.41, 0.066, C["tag2"], th["sub"], 600)
    return s
def b4(th):
    s = corner("br", th["stripe"], th["wedge"], 0.40)
    s += T(L, 0.68, 0.21, "Veera", th["fg"], 800, ls=-0.006) + T(L, 0.90, 0.21, "Venkatesh", th["fg"], 800, ls=-0.006) + T(L, 1.03, 0.052, C["title"], th["acc"], 700, ls=0.03)
    s += qr(L, 1.135, 0.69, 0.05, th)
    X = 1.95
    def grp(y, lab, lines):
        o = T(X, y, 0.042, lab, th["sub"], 700, ls=0.06)
        for i, ln in enumerate(lines): o += T(X, y+0.105+0.095*i, 0.068, ln, th["fg"], 600 if i == 0 and len(lines) == 1 else 400)
        return o
    s += grp(0.60, "EMAIL", [C["email"]]) + grp(0.93, "PHONE", [C["phone"]]) + grp(1.26, "ADDRESS", ["CWEP8274, Compass Building,", "Al Shohada Road, Al Hamra", "Industrial Zone-FZ, Ras Al Khaimah,", "United Arab Emirates"])
    return s

# ---------------- 5 STRIPES (two corners) ----------------
def f5(th):
    h = 0.62
    return (corner("tl", th["stripe"], th["wedge"], 0.50) + corner("br", th["stripe"], th["wedge"], 0.50)
            + mark(W/2-MW(h)/2, 0.50, h, th["logo"]) + wordmark(W/2, 1.45, 0.25, th, "middle")
            + T(W/2, 1.63, 0.058, C["tag"], th["sub"], 600, "middle", 0.012))
def b5(th):
    tile = 0.86
    s = corner("tl", th["stripe"], th["wedge"], 0.48) + corner("br", th["stripe"], th["wedge"], 0.42)
    s += T(L, 0.98, 0.15, C["name"], th["fg"], 800, ls=-0.004) + T(L, 1.10, 0.052, C["title"], th["acc"], 700, ls=0.03) + contacts(L, 1.31, th)
    s += qr(R-tile-0.05, 0.60, tile, 0.055, th, C["web"], th["fg"]) 
    return s

CONCEPTS = [("01-diagonal", f1, b1), ("02-slant-panel", f2, b2), ("03-minimal-mark", f3, b3), ("04-bold-crop", f4, b4), ("05-stripes", f5, b5)]

meta = []
for cname, ff, bf in CONCEPTS:
    for vname, tf, tb in VARIANTS:
        thf, thb = THEMES[tf], THEMES[tb]
        fs, bs = ff(thf), bf(thb)
        key = f"{cname}_{vname}"
        meta.append(dict(key=key, concept=cname, variant=vname,
                         front=svg(fs, thf["bg"]), back=svg(bs, thb["bg"]),
                         front_p=svg(fs, thf["bg"], True), back_p=svg(bs, thb["bg"], True)))
json.dump(meta, open("designs/meta.json", "w"))
print(len(meta), "designs")
