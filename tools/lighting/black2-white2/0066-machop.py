# Machop: bare gray-blue skin over muscle (Hide) everywhere, tail included; the three ridges on its head are the
# same skin painted in the yellow-browns (as on Machamp). Nothing on it is hard, wet (but the mouth) or glowing.
SOURCE = "sources/black2-white2/0066-machop.spu"
H = dict(finish=0.25, body=0.08)          # Hide: plain bare skin
GOLD = [8, 9, 10, 11]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # the skin: its dark teal contour and muscle lines (2) are its darkest shade; the far leg is painted in 3
    dict(name="hide", shades=[2, 3, 4, 5, 6], base=2, **H),
    # "three brown ridges on its head": the same skin, painted in the yellow-browns
    dict(name="hide, head ridges", shades=GOLD, base=1, **H),
    dict(name="mouth", shades=[13, 14, 15], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[13, 14, 12], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("hide", [2, 3, 4, 5, 6]), **to("hide, head ridges", GOLD),
          **to("mouth", [13, 14, 15]), 12: "eye (line art)"}
EYE = to("eye (line art)", [12, 13, 14])
RULES = [
    # front head: the eyes sit above the open mouth and share its reds
    dict(view="front", drawings=["atama"], rect=[0, 13, 24, 7], colors=EYE),
    dict(drawings=["atama-eyes-*"], colors=EYE),
]
