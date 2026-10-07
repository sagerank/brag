from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
R = "final/PRINT-READY/pdf/"
def boxed(p):
    p.mediabox = RectangleObject([0,0,270,162]); p.bleedbox = RectangleObject([0,0,270,162]); p.cropbox = RectangleObject([0,0,270,162])
    p.trimbox = RectangleObject([9,9,261,153]); p.artbox = RectangleObject([9,9,261,153]); return p
f = PdfReader(R+"_front.pdf").pages[0]; b = PdfReader(R+"_back.pdf").pages[0]
for name, pages in (("SageRank-card_PRINT_front-and-back_bleed", [f, b]), ("SageRank-card_front_bleed", [f]), ("SageRank-card_back_bleed", [b])):
    w = PdfWriter()
    for p in pages: w.add_page(boxed(p))
    w.add_metadata({"/Title": "SageRank Software Solutions FZ-LLC - business card (Veera Venkatesh)"}); w.write(R+name+".pdf")
import os; os.remove(R+"_front.pdf"); os.remove(R+"_back.pdf")
