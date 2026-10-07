"""Optical alignment helpers: place elements so their INK (not their text box) starts on a given x."""
from fontTools.pens.boundsPen import BoundsPen
from outline import _font
def lsb(ch, weight, size):
    font, tt, gs, upm, order = _font(weight)
    g = tt.getBestCmap()[ord(ch)]; bp = BoundsPen(gs); gs[g].draw(bp)
    return (bp.bounds[0] if bp.bounds else 0) * size / upm
ICON_INK_LEFT = {"mail": 2.15, "phone": 2.15, "globe": 2.15, "pin": 4.15}    # left ink edge in the 24-unit icon box (incl. half stroke)
def icon_x(name, ink_x, size): return ink_x - ICON_INK_LEFT[name] * size / 24

import uharfbuzz as hb
def text_width(txt, weight, size, ls=0.0):
    font, tt, gs, upm, order = _font(weight)
    buf = hb.Buffer(); buf.add_str(txt); buf.guess_segment_properties(); hb.shape(font, buf, {"kern": True})
    return sum(p.x_advance for p in buf.glyph_positions) * size / upm + ls * len(txt)
