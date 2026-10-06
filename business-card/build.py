"""Builds SageRank business card (front/back) -> PDF (print, with bleed) + PNG previews.
Edit CONFIG, run: python3 build.py && node render.mjs
"""
import segno, io, re

CONFIG = dict(
    name="Veera Venkatesh",
    title="FOUNDER",
    email="veera@sagerank.io",            # TODO confirm
    phone="+1 (000) 000-0000",            # TODO replace
    web="sagerank.io",
    addr1="Street Address, Suite #",      # TODO replace
    addr2="City, State ZIP",              # TODO replace
    qr_url="https://sagerank.io",
)
INK, SAGE, SAGE_LT, PAPER, MUTED = "#0A1511", "#8FB996", "#CFE6C8", "#F5F3EC", "#5C6B62"

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

def mark(x, y, s, c1=SAGE, c2=SAGE_LT):
    # three rising "leaf" bars: growth + rank
    hs, w, g, r, k = [40, 68, 100], 24, 8, 24, 3
    out = f'<g transform="translate({x} {y}) scale({s/100})">'
    for i, h in enumerate(hs):
        x0 = i * (w + g); y0 = 100 - h
        d = (f"M{x0+r} {y0}H{x0+w-k}Q{x0+w} {y0} {x0+w} {y0+k}V{100-r}"
             f"Q{x0+w} 100 {x0+w-r} 100H{x0+k}Q{x0} 100 {x0} {100-k}V{y0+r}Q{x0} {y0} {x0+r} {y0}Z")
        col = [c1, "#B4D4B6", c2][i]
        out += f'<path d="{d}" fill="{col}"/>'
    return out + '</g>'

B = 0.125  # bleed (in)
W, H = 3.5 + 2*B, 2.0 + 2*B
c = CONFIG

front = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}in" height="{H}in">
<defs><radialGradient id="glow" cx="50%" cy="48%" r="60%"><stop offset="0" stop-color="#16271E"/><stop offset="1" stop-color="{INK}"/></radialGradient></defs>
<rect width="{W}" height="{H}" fill="url(#glow)"/>
{mark(W/2-0.30, H/2-0.60, 0.60)}
<text x="{W/2}" y="{H/2+0.42}" text-anchor="middle" font-family="Inter" font-size="0.215" letter-spacing="-0.004" fill="{PAPER}"><tspan font-weight="300">Sage</tspan><tspan font-weight="700">Rank</tspan></text>
<text x="{W/2}" y="{H/2+0.66}" text-anchor="middle" font-family="Inter" font-weight="500" font-size="0.062" letter-spacing="0.032" fill="{SAGE}">SAGERANK.IO</text>
</svg>'''

qs = 0.88
qx, qy = B + 3.5 - 0.32 - qs, B + 0.46
lx = B + 0.32
back = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}in" height="{H}in">
<rect width="{W}" height="{H}" fill="{PAPER}"/>
<rect x="0" y="0" width="{W}" height="0" fill="none"/>
{mark(lx, B+0.32, 0.20, "#5E9470", "#9CC7A0")}
<text x="{lx}" y="{B+0.86}" font-family="Inter" font-weight="700" font-size="0.145" letter-spacing="-0.003" fill="{INK}">{c['name']}</text>
<text x="{lx}" y="{B+1.0}" font-family="Inter" font-weight="600" font-size="0.052" letter-spacing="0.03" fill="#5E9470">{c['title']}</text>
<g font-family="Inter" font-size="0.066" fill="{INK}" font-weight="400">
<text x="{lx}" y="{B+1.27}">{c['email']}</text>
<text x="{lx}" y="{B+1.40}">{c['phone']}</text>
<text x="{lx}" y="{B+1.53}" font-weight="600">{c['web']}</text>
<text x="{lx}" y="{B+1.66}" fill="{MUTED}">{c['addr1']}</text>
<text x="{lx}" y="{B+1.76}" fill="{MUTED}">{c['addr2']}</text>
</g>
<g transform="translate({qx} {qy})"><path d="{qr_path(c['qr_url'], qs)}" fill="{INK}"/></g>
<text x="{qx+qs/2}" y="{qy+qs+0.15}" text-anchor="middle" font-family="Inter" font-weight="600" font-size="0.048" letter-spacing="0.03" fill="{MUTED}">SCAN TO VISIT</text>
</svg>'''

# vertical positions on back: keep everything >=0.3in from trim
open("front.svg","w").write(front); open("back.svg","w").write(back)
page = lambda s: f'<!doctype html><meta charset="utf-8"><style>@page{{size:{W}in {H}in;margin:0}}html,body{{margin:0}}svg{{display:block}}</style>{s}'
open("front.html","w").write(page(front)); open("back.html","w").write(page(back))
open("both.html","w").write(f'<!doctype html><meta charset="utf-8"><style>@page{{size:{W}in {H}in;margin:0}}html,body{{margin:0}}svg{{display:block;page-break-after:always}}</style>{front}{back}')
