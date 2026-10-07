import json, re, shutil, base64
R = "final/PRINT-READY"; P = "final/PRINT-PACKAGE"
rd = lambda p: open(p).read()
art = {k: rd(f"{R}/svg/SageRank-card_{k}_bleed.svg") for k in ("front", "back")}
trim = {k: rd(f"{R}/svg/SageRank-card_{k}_trim.svg") for k in ("front", "back")}
for k in ("front", "back"):
    for t in ("bleed", "trim"):
        shutil.copy(f"{R}/svg/SageRank-card_{k}_{t}.svg", f"{P}/source-files/svg/")
        shutil.copy(f"{R}/png/SageRank-card_{k}_{t}_600dpi.png", f"{P}/source-files/png/")
def inner(svg, w, h):          # re-size an svg string to explicit inch width/height
    return re.sub(r'width="[^"]*in" height="[^"]*in"', f'width="{w}in" height="{h}in"', svg, count=1)
# ---- crop-marks PDF: page 4.25 x 2.75 in, art (3.75 x 2.25 with bleed) centred => trim starts 0.375 in from page edge
PW, PH, S = 4.25, 2.75, 0.25
def marks():
    t = 0.375; w, h = 3.5, 2.0; off, ln = 0.0625 + 0.125, 0.12      # marks start outside the bleed
    L = []
    for x in (t, t + w):
        L += [f'<line x1="{x}" y1="{t-off}" x2="{x}" y2="{t-off-ln}"/>', f'<line x1="{x}" y1="{t+h+off}" x2="{x}" y2="{t+h+off+ln}"/>']
    for y in (t, t + h):
        L += [f'<line x1="{t-off}" y1="{y}" x2="{t-off-ln}" y2="{y}"/>', f'<line x1="{t+w+off}" y1="{y}" x2="{t+w+off+ln}" y2="{y}"/>']
    return f'<g stroke="#000" stroke-width="0.006">{"".join(L)}</g>'
def cm_page(side):
    label = f'<text x="{PW/2}" y="{PH-0.09}" text-anchor="middle" font-family="Inter" font-size="0.062" fill="#555">SageRank business card - {side.upper()} - cut size 3.5 x 2 in (88.9 x 50.8 mm) - bleed 0.125 in (3.175 mm)</text>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {PW} {PH}" width="{PW}in" height="{PH}in"><rect width="{PW}" height="{PH}" fill="#fff"/>'
            f'<g transform="translate({S} {S})">{re.sub(r"^<svg[^>]*>|</svg>$", "", art[side].strip())}</g>{marks()}{label}</svg>')
css = lambda w, h: f'@page{{size:{w}in {h}in;margin:0}}html,body{{margin:0}}svg{{display:block;page-break-after:always}}'
open("_pkg/crop.html", "w").write(f'<!doctype html><meta charset=utf-8><style>{css(PW,PH)}</style>{cm_page("front")}{cm_page("back")}')
open("_pkg/trim.html", "w").write(f'<!doctype html><meta charset=utf-8><style>{css(3.5,2)}</style>{trim["front"]}{trim["back"]}')
# ---- layout guide: card with trim / bleed / safe overlays
def guide(side):
    k = 240; w, h = 3.75*k, 2.25*k
    def rect(inset, col, dash, wd=2.2): return f'<rect x="{inset*k}" y="{inset*k}" width="{w-2*inset*k}" height="{h-2*inset*k}" fill="none" stroke="{col}" stroke-width="{wd}" stroke-dasharray="{dash}"/>'
    a = re.sub(r'width="[^"]*in" height="[^"]*in"', f'width="{w}" height="{h}"', art[side], count=1)
    return (f'<div style="position:relative;width:{w}px;height:{h}px;box-shadow:0 4px 18px rgba(0,0,0,.25)">{a}'
            f'<svg style="position:absolute;inset:0" width="{w}" height="{h}">{rect(0.0,"#000","0",3)}{rect(0.125,"#e6007e","10 6")}{rect(0.425,"#0a8f4f","4 5")}</svg></div>')
open("_pkg/guide.html", "w").write(f'''<!doctype html><meta charset=utf-8><body style="margin:0;background:#fff;font-family:Inter,system-ui,sans-serif;width:2000px;padding:36px 40px">
<h1 style="font-size:34px;margin:0 0 6px">Layout guide: what the three lines mean</h1>
<p style="font-size:20px;margin:0 0 26px;color:#333">Same artwork as the print file, with guide lines drawn on top. The guide lines are NOT in the print file.</p>
<div style="display:flex;gap:40px">{guide("front")}{guide("back")}</div>
<div style="display:flex;gap:46px;margin-top:26px;font-size:21px;line-height:1.35">
<div><b style="color:#000">&#9632; Black outer edge = BLEED edge</b><br>File edge. 3.75 x 2.25 in (95.25 x 57.15 mm).<br>Colour (the blue bar) must reach this edge.<br>This outer 0.125 in is cut away.</div>
<div><b style="color:#e6007e">- - Pink dashed = TRIM (cut line)</b><br>Final card. 3.5 x 2 in (88.9 x 50.8 mm).<br>Cut exactly here.</div>
<div><b style="color:#0a8f4f">- - Green dashed = SAFE area</b><br>0.3 in (7.6 mm) inside the cut line.<br>All text, logo and QR code are inside it,<br>so nothing is cut off or touched by rounded corners.</div></div>''')
