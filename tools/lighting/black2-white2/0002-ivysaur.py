SOURCE = "sources/black2-white2/0002-ivysaur.spu"
MATERIALS = [
    dict(name="outline", shades=[15, 14], finish=0.1, body=0),
    dict(name="frog skin", shades=[8, 7, 6, 5], base=2, finish=0.3, body=0.1),
    dict(name="frog skin, spots", shades=[8, 7, 6], base=1, finish=0.3, body=0.1),
    dict(name="leaves", shades=[12, 11, 10, 9], base=1, finish=0.15, body=0.35),
    dict(name="bud", shades=[14, 4, 3, 2], base=1, finish=0.1, body=0.25),
    # the palette has no gray: its unused first color (a pale warm gray) is the white's shade
    dict(name="claws and teeth", shades=[0, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[14, 4], base=1, finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[4, 3, 0, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("frog skin", [8, 7, 6, 5]), **to("leaves", [12, 11, 10, 9]), **to("bud", [14, 4, 3, 2]),
          1: "claws and teeth"}
SKIN = ["head*", "body*", "leg*", "foot*", "hip"]
RULES = [
    dict(drawings=["flower"], thin_all={14: "outline"}),    # the bud's petals overlap: their lines are creases
    dict(drawings=["head", "head-2"], colors={14: "mouth", 4: "mouth"}),
    dict(drawings=["head-eyes-*", "head-2-eyes-*"], colors={1: "eye (line art)", 4: "eye (line art)", 3: "eye (line art)"}),
]
MARKS = [
    dict(drawings=SKIN, color=8, on=[7, 6, 5], to="frog skin, spots", max=30, min=2),
    dict(drawings=SKIN, color=7, on=[6, 5], to="frog skin, spots", max=40, min=2),
]
