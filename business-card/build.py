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

MW = 0.8 * 667.3 / 828.0   # mark width at 0.8in tall
front = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}in" height="{H}in">
<rect width="{W}" height="{H}" fill="#fff"/>
{mark(W/2-1.01, H/2-0.515, 0.80)}
<text x="{W/2-0.29}" y="{H/2-0.025}" font-family="Inter" font-size="0.30" letter-spacing="-0.008" fill="{INK}"><tspan font-weight="800">Sage</tspan><tspan font-weight="800" fill="{BLUE}">Rank</tspan></text>
<text x="{W/2}" y="{H/2+0.50}" text-anchor="middle" font-family="Inter" font-weight="500" font-size="0.076" letter-spacing="0.004" fill="#3A4452">{c['tagline']}</text>
</svg>'''

tile = 1.0; pad = 0.06; qs = tile - 2*pad
tx, ty = B + 3.5 - 0.30 - tile, B + 0.36
lx = B + 0.30
addr = "".join(f'<text x="{lx}" y="{B+1.40+i*0.095:.3f}">{l}</text>' for i, l in enumerate(c['addr']))
back = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}in" height="{H}in">
<rect width="{W}" height="{H}" fill="{BG_DARK}"/>
{mark(lx, B+0.30, 0.25, dark="#fff", light=BG_DARK, blue="#3B8BEB")}
<text x="{lx}" y="{B+0.80}" font-family="Inter" font-weight="700" font-size="0.15" letter-spacing="-0.003" fill="#fff">{c['name']}</text>
<text x="{lx}" y="{B+0.93}" font-family="Inter" font-weight="600" font-size="0.052" letter-spacing="0.03" fill="#3B8BEB">{c['title']}</text>
<g font-family="Inter" font-size="0.068" fill="#fff" font-weight="500">
<text x="{lx}" y="{B+1.12}">{c['email']}</text>
<text x="{lx}" y="{B+1.235}">{c['phone']}</text>
</g>
<g font-family="Inter" font-size="0.057" fill="{MUTED_D}" font-weight="400">{addr}</g>
<rect x="{tx}" y="{ty}" width="{tile}" height="{tile}" rx="0.07" fill="#fff"/>
<g transform="translate({tx+pad} {ty+pad})"><path d="{qr_path(c['qr_url'], qs)}" fill="{INK}"/></g>
<text x="{tx+tile/2}" y="{ty+tile+0.14}" text-anchor="middle" font-family="Inter" font-weight="600" font-size="0.048" letter-spacing="0.03" fill="{MUTED_D}">SAGERANK.IO</text>
</svg>'''

# vertical positions on back: keep everything >=0.3in from trim
open("front.svg","w").write(front); open("back.svg","w").write(back)
page = lambda s: f'<!doctype html><meta charset="utf-8"><style>@page{{size:{W}in {H}in;margin:0}}html,body{{margin:0}}svg{{display:block}}</style>{s}'
open("front.html","w").write(page(front)); open("back.html","w").write(page(back))
open("both.html","w").write(f'<!doctype html><meta charset="utf-8"><style>@page{{size:{W}in {H}in;margin:0}}html,body{{margin:0}}svg{{display:block;page-break-after:always}}</style>{front}{back}')
