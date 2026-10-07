import json, re
from outline import outline_svg
d = json.load(open("final/FINAL/meta.json"))
import os; os.makedirs("final/PRINT-READY/svg", exist_ok=True)
for side in ("front", "back"):
    for tag, key in (("bleed", side), ("trim", side + "_p")):
        s = outline_svg(d[key]); assert "<text" not in s
        open(f"final/PRINT-READY/svg/SageRank-card_{side}_{tag}.svg", "w").write(s)
print("svgs ok")
