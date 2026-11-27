SOURCE = "sources/black2-white2/0047-parasect.spu"
SHELL = [14, 13, 12, 11]
CAP = [9, 8, 7, 6]
MATERIALS = [
    dict(name="outline", shades=[15, 14, 9, 13], finish=0.1, body=0),
    # body, pincers and legs: one hard shell; the dark brown is its contour and the body in the cap's shadow
    dict(name="insect shell", shades=SHELL, base=1, finish=0.45, body=0),
    # the big mushroom: painted flat and soft, no highlight
    dict(name="mushroom cap", shades=CAP, base=1, finish=0.1, body=0.1),
    dict(name="mushroom cap, spots", shades=[5, 4], base=0, finish=0.1, body=0.1),
    # the orange pixels blending a spot into the cap: only tinted. As shades of the spots they turned whole
    # spots orange in the field's back view while the cap around them did not change
    dict(name="mushroom cap, spot edges", shades=[], finish=0.1, body=0.1),
    dict(name="eye (line art)", shades=[3, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("insect shell", SHELL), **to("mushroom cap", CAP),
          **to("mushroom cap, spots", [5, 4]), **to("eye (line art)", [3, 2, 1])}
RULES = [
    dict(drawings=["kinoko", "head"], colors={**to("mushroom cap, spot edges", [12, 11]), 13: "outline"}),
    # a pincer's two jaws overlap: the dark line between them is a crease
    dict(drawings=["hand-r", "hand-l"], interior={14: ([13, 12, 11], "outline")}),
    dict(drawings=["eye"], colors={14: "outline"}),          # the eyes' dark ring
    dict(drawings=["foot-r1"], colors={9: "outline"}),       # one stray dark red pixel: stays as drawn
]
# the pincers' pale strip and the cap's pale top are broad lit sides, each just under 7% of its surface
KEEP_TOP = ["insect shell", "mushroom cap"]
