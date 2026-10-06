import segno
CONFIG = dict(
    name="Veera Venkatesh",
    title="FOUNDER & CEO",
    email="veer@sagerank.io",
    phone="+971 56 801 5996",
    web="sagerank.io",
    addr=["CWEP8274, Compass Building", "Al Shohada Road", "Al Hamra Industrial Zone-FZ", "Ras Al Khaimah, United Arab Emirates"],
    tagline="Rise with Authority, Secure with Dominance",
    qr_url="https://sagerank.io",
)
BLUE, INK, BG_DARK, MUTED_D = "#1d70d1", "#0B0F17", "#0B1018", "#9AA7B8"

def qr_path(url, size):
    q = segno.make(url, error='h', micro=False)
    m = q.matrix
    n = len(m); u = size / n
    d = []
    for y, row in enumerate(m):
        x = 0
        while x < n:
            if row[x]:
                s = x
                while x < n and row[x]: x += 1
                d.append(f"M{s*u:.4f} {y*u:.4f}h{(x-s)*u:.4f}v{u:.4f}h{-(x-s)*u:.4f}z")
            else: x += 1
    return "".join(d)

def mark(x, y, h, dark="#000", light="#fff", blue=BLUE):
    """Official SageRank mark (from logo/sagerank-logo.svg); bbox x166-834, y86-914. (stray green stroke dropped)"""
    s = h / 828.0
    return (f'<g transform="translate({x} {y}) scale({s}) translate(-166.343 -86.038)">'
        f'<path d="M580.305,86.038l0,413.962l-413.962,183.983l0,-413.962l413.962,-183.983Z" fill="{blue}"/>'
        f'<path d="M833.657,316.017l0,413.962l-413.962,183.983l0,-413.962l413.962,-183.983Z" fill="{blue}"/>'
        f'<path d="M803.285,164.031l0,92.991l-474.707,210.981l0,-92.991l474.707,-210.981Z" fill="{dark}"/>'
        f'<path d="M657.048,531.997l0,92.991l-474.707,210.981l0,-92.991l474.707,-210.981Z" fill="{dark}"/>'
        f'<path d="M657.048,619.822l0,-89.575l-328.47,-145.987l0,89.575l328.47,145.987Z" fill="{light}"/></g>')

B = 0.125  # bleed (in)
W, H = 3.5 + 2*B, 2.0 + 2*B
c = CONFIG

import math
T = math.degrees(math.atan(184/414))   # logo's own diagonal angle (~24 deg)
GREY = "#5B6676"
front = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}in" height="{H}in">
<defs><clipPath id="cv"><rect width="{W}" height="{H}"/></clipPath></defs>
<rect width="{W}" height="{H}" fill="#fff"/>
<g clip-path="url(#cv)"><g transform="translate({W} {H-0.60}) rotate({-T})">
  <rect x="-4" y="0" width="5" height="0.05" fill="{INK}"/>
  <rect x="-4" y="0.11" width="5" height="3" fill="{BLUE}"/></g></g>
{mark(W/2-1.01, H/2-0.60, 0.80)}
<text x="{W/2-0.29}" y="{H/2-0.11}" font-family="Inter" font-size="0.30" letter-spacing="-0.008" font-weight="800" fill="{INK}">Sage<tspan fill="{BLUE}">Rank</tspan></text>
<text x="{W/2-1.01}" y="{H/2+0.46}" font-family="Inter" font-weight="600" font-size="0.066" textLength="2.156" lengthAdjust="spacing" fill="{GREY}">Rise with Authority, Secure with Dominance</text>
</svg>'''

PX = B + 2.25                      # panel left edge
tile = 0.86; pad = 0.055; qs = tile - 2*pad
tx = PX + (B + 3.5 - PX - tile)/2 ; ty = B + 0.50
lx = B + 0.30
vx = lx + 0.14
def row(y, label, text, weight=500):
    return (f'<text x="{lx}" y="{y}" font-family="Inter" font-weight="800" font-size="0.05" fill="{BLUE}">{label}</text>'
            f'<text x="{vx}" y="{y}" font-family="Inter" font-weight="{weight}" font-size="0.066" fill="{INK}">{text}</text>')
addr = ["CWEP8274, Compass Building, Al Shohada Road", "Al Hamra Industrial Zone-FZ", "Ras Al Khaimah, United Arab Emirates"]
addr_svg = row(B+1.50, "A", addr[0], 400) + "".join(
    f'<text x="{vx}" y="{B+1.50+0.095*(i+1):.3f}" font-family="Inter" font-size="0.066" fill="{INK}">{l}</text>' for i, l in enumerate(addr[1:]))
back = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}in" height="{H}in">
<defs><clipPath id="pn"><rect x="{PX}" y="0" width="{W-PX}" height="{H}"/></clipPath></defs>
<rect width="{W}" height="{H}" fill="#fff"/>
<rect x="{PX}" y="0" width="{W-PX}" height="{H}" fill="{BLUE}"/>
<g clip-path="url(#pn)"><g transform="translate({W} {H-0.45}) rotate({-T})">
  <rect x="-4" y="0" width="5" height="0.04" fill="{INK}"/>
  <rect x="-4" y="0.09" width="5" height="3" fill="#fff" opacity="0.22"/></g></g>
{mark(lx, B+0.30, 0.30)}
<text x="{lx}" y="{B+0.92}" font-family="Inter" font-weight="800" font-size="0.15" letter-spacing="-0.004" fill="{INK}">{c['name']}</text>
<text x="{lx}" y="{B+1.05}" font-family="Inter" font-weight="700" font-size="0.052" letter-spacing="0.03" fill="{BLUE}">{c['title']}</text>
<rect x="{lx}" y="{B+1.13}" width="0.28" height="0.012" fill="{INK}"/>
{row(B+1.28, "E", c['email'], 600)}
{row(B+1.39, "T", c['phone'], 600)}
{addr_svg}
<rect x="{tx}" y="{ty}" width="{tile}" height="{tile}" rx="0.06" fill="#fff"/>
<g transform="translate({tx+pad} {ty+pad})"><path d="{qr_path(c['qr_url'], qs)}" fill="{INK}"/></g>
<text x="{tx+tile/2}" y="{ty+tile+0.16}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="0.05" letter-spacing="0.03" fill="#fff">SAGERANK.IO</text>
<text x="{tx+tile/2}" y="{ty+tile+0.255}" text-anchor="middle" font-family="Inter" font-weight="500" font-size="0.04" letter-spacing="0.03" fill="#DCE9F9">SCAN TO VISIT</text>
</svg>'''

# vertical positions on back: keep everything >=0.3in from trim
open("front.svg","w").write(front); open("back.svg","w").write(back)
page = lambda s: f'<!doctype html><meta charset="utf-8"><style>@page{{size:{W}in {H}in;margin:0}}html,body{{margin:0}}svg{{display:block}}</style>{s}'
open("front.html","w").write(page(front)); open("back.html","w").write(page(back))
open("both.html","w").write(f'<!doctype html><meta charset="utf-8"><style>@page{{size:{W}in {H}in;margin:0}}html,body{{margin:0}}svg{{display:block;page-break-after:always}}</style>{front}{back}')
