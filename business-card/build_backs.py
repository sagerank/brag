"""5 new back-side variations (front = confirmed combo front). python3 build_backs.py && node backs.mjs"""
import json
from build_combo import *       # th, helpers, fs (confirmed front), band, X0
ICON = {
 "mail":  '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>',
 "pin":   '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><ellipse cx="12" cy="12" rx="4" ry="9"/><path d="M3 12h18"/>',
 "AEO":   '<path d="M4 5h16v11H9l-5 4z"/><path d="M9 10.5l2 2 4-4"/>',
 "GEO":   '<path d="M12 3l2.2 6.8L21 12l-6.8 2.2L12 21l-2.2-6.8L3 12l6.8-2.2z"/>',
 "SEC":   '<path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
}
def ic(name, x, y, s=0.095, col=BLUE):
    return f'<g transform="translate({x:.3f} {y:.3f}) scale({s/24:.5f})" fill="none" stroke="{col}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</g>'
def irow(x, y, name, txt, size=0.066, w=500, col=INK):
    return ic(name, x, y-0.076) + T(x+0.16, y, size, txt, col, w)
def addr(x, y, lines=None, size=0.062, step=0.093, col=INK):
    lines = lines or C["addr"]
    s = ic("pin", x, y-0.076) + T(x+0.16, y, size, lines[0], col, 400)
    for i, l in enumerate(lines[1:]): s += T(x+0.16, y+step*(i+1), size, l, col, 400)
    return s
def sv(x, y, name, label, size=0.056):       # service icon + label
    return ic(name, x, y-0.094, 0.115) + T(x+0.16, y, size, label, INK, 800, ls=0.02)
WEB = "sagerank.io"
band_r = f'<polygon points="{W},0 {W-B-0.30},0 {W-B-0.18},{H} {W},{H}" fill="{BLUE}"/>'

def A():   # icon column, left slanted edge, QR right
    X = B+0.55
    s = band + mark(X, 0.45, 0.26, LOGO) + T(X, 0.93, 0.17, C["name"], INK, 800, ls=-0.004) + T(X, 1.05, 0.052, C["title"], BLUE, 700, ls=0.03)
    s += irow(X, 1.25, "mail", C["email"], w=600) + irow(X, 1.365, "phone", C["phone"], w=600) + irow(X, 1.48, "globe", WEB, w=600)
    s += addr(X, 1.605, size=0.060, step=0.088)
    s += qr(R-0.84, 0.62, 0.84, 0.055, th) + T(R-0.42, 1.60, 0.046, "SCAN TO CONNECT", GREY, 700, "middle", 0.03)
    return s
def Bk():  # mirrored: QR left, slanted edge on the right, service icons along the bottom
    X = 1.50
    s = band_r + mark(L, 0.45, 0.26, LOGO) + qr(L-0.03, 0.82, 0.84, 0.055, th) + T(L+0.39, 1.82, 0.045, "SCAN TO CONNECT", GREY, 700, "middle", 0.03)
    s += T(X, 0.72, 0.17, C["name"], INK, 800, ls=-0.004) + T(X, 0.84, 0.052, C["title"], BLUE, 700, ls=0.03) + hl(X, 0.92, 0.3, INK, 0.012)
    s += irow(X, 1.08, "mail", C["email"], w=600) + irow(X, 1.195, "phone", C["phone"], w=600) + irow(X, 1.31, "globe", WEB, w=600)
    s += addr(X, 1.44, size=0.058, step=0.086)
    s += sv(X, 1.77, "AEO", "AEO", 0.052) + sv(X+0.58, 1.77, "GEO", "GEO", 0.052) + sv(X+1.12, 1.77, "SEC", "SECURITY", 0.052)
    return s
def Cd():  # dossier: top bar, hairline, three columns
    s = bar_t + T(L, 0.80, 0.20, C["name"], INK, 800, ls=-0.005) + T(L, 0.92, 0.052, C["title"], BLUE, 700, ls=0.03)
    h = 0.30; s += mark(R-MW(h), 0.46, h, LOGO) + hl(L, 1.04, R-L)
    s += irow(L, 1.30, "mail", C["email"], 0.062, 600) + irow(L, 1.415, "phone", C["phone"], 0.062, 600) + irow(L, 1.53, "globe", WEB, 0.062, 600)
    s += addr(1.50, 1.30, ["CWEP8274, Compass Building,", "Al Shohada Road,", "Al Hamra Industrial Zone-FZ,", "Ras Al Khaimah,", "United Arab Emirates"], 0.056, 0.088)
    s += qr(R-0.66, 1.17, 0.66, 0.045, th)
    return s
def D():   # stair: rows step right like the logo's rise
    s = corner("br", INK, BLUE, 0.40) + mark(L, 0.43, 0.28, LOGO) + T(L, 0.93, 0.17, C["name"], INK, 800, ls=-0.004) + T(L, 1.05, 0.052, C["title"], BLUE, 700, ls=0.03)
    s += irow(L, 1.24, "mail", C["email"], w=600) + irow(L+0.10, 1.355, "phone", C["phone"], w=600) + irow(L+0.20, 1.47, "globe", WEB, w=600)
    s += addr(L+0.30, 1.595, size=0.060, step=0.088)
    s += qr(R-0.80, 0.62, 0.80, 0.055, th) + T(R-0.40, 1.58, 0.046, "SCAN TO CONNECT", GREY, 700, "middle", 0.03)
    return s
def E():   # service-icon feature row
    s = bar_t + mark(L, 0.42, 0.22, LOGO) + qr(R-0.60, 0.42, 0.60, 0.04, th)
    s += T(L, 0.92, 0.18, C["name"], INK, 800, ls=-0.004) + T(L, 1.03, 0.052, C["title"], BLUE, 700, ls=0.03)
    s += hl(L, 1.10, R-L) + sv(L, 1.29, "AEO", "AEO") + sv(L+0.98, 1.29, "GEO", "GEO") + sv(L+1.96, 1.29, "SEC", "SECURITY") + hl(L, 1.38, R-L)
    s += irow(L, 1.52, "mail", C["email"], 0.062, 600) + irow(L, 1.635, "phone", C["phone"], 0.062, 600) + irow(L, 1.75, "globe", WEB, 0.062, 600)
    s += addr(1.65, 1.52, size=0.056, step=0.088)
    return s

V = [("A-icon-column", A), ("B-mirror-qr-left", Bk), ("C-dossier", Cd), ("D-stair", D), ("E-service-icons", E)]
meta = [dict(key=k, front=svg(fs, "#fff"), back=svg(fn(), "#fff"), back_p=svg(fn(), "#fff", True)) for k, fn in V]
json.dump(dict(front_p=svg(fs, "#fff", True), items=meta), open("final/backs/meta.json", "w"))
