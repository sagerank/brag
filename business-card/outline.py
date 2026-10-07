"""Convert <text> in an SVG string to vector outlines (Inter), so files need no installed font."""
import re, html, uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FD = "/usr/share/fonts/opentype/inter/"
FILES = {400: "Inter-Regular.otf", 500: "Inter-Medium.otf", 600: "Inter-SemiBold.otf", 700: "Inter-Bold.otf", 800: "Inter-ExtraBold.otf"}
_c = {}
def _font(w):
    if w not in _c:
        p = FD + FILES[w]; face = hb.Face(hb.Blob.from_file_path(p)); tt = TTFont(p)
        _c[w] = (hb.Font(face), tt, tt.getGlyphSet(), tt["head"].unitsPerEm, tt.getGlyphOrder())
    return _c[w]
_n = lambda v: f"{v:.4f}".rstrip("0").rstrip(".")
def _runs(inner, base_fill):
    out, pos = [], 0
    for m in re.finditer(r'<tspan([^>]*)>(.*?)</tspan>', inner, re.S):
        if m.start() > pos: out.append((html.unescape(inner[pos:m.start()]), base_fill))
        f = re.search(r'fill="([^"]+)"', m.group(1)); out.append((html.unescape(m.group(2)), f.group(1) if f else base_fill)); pos = m.end()
    if pos < len(inner): out.append((html.unescape(inner[pos:]), base_fill))
    return [r for r in out if r[0] != ""]
def _text(m):
    a = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
    x, y, size = float(a["x"]), float(a["y"]), float(a["font-size"])
    w = int(a.get("font-weight", 400)); ls = float(a.get("letter-spacing", 0) or 0); anchor = a.get("text-anchor", "start"); base = a.get("fill", "#000")
    font, tt, gs, upm, order = _font(w); sc = size / upm
    glyphs = []                                    # (path d, fill)
    pen_x = 0.0; segs = []
    for txt, fill in _runs(m.group(2), base):
        buf = hb.Buffer(); buf.add_str(txt); buf.guess_segment_properties()
        hb.shape(font, buf, {"liga": ls == 0, "clig": ls == 0, "kern": True})
        seg = []
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            seg.append((order[info.codepoint], pen_x + pos.x_offset*sc, pos.y_offset*sc)); pen_x += pos.x_advance*sc + ls
        segs.append((seg, fill))
    shift = 0.0 if anchor == "start" else (-pen_x/2 if anchor == "middle" else -pen_x)
    out = []
    for seg, fill in segs:
        d = []
        for name, gx, gy in seg:
            p = SVGPathPen(gs, ntos=_n); gs[name].draw(TransformPen(p, (sc, 0, 0, -sc, x + shift + gx, y - gy))); d.append(p.getCommands())
        out.append(f'<path d="{"".join(d)}" fill="{fill}"/>')
    return "<g>" + "".join(out) + "</g>"
def outline_svg(svg):
    return re.sub(r'<text([^>]*)>(.*?)</text>', _text, svg, flags=re.S)
