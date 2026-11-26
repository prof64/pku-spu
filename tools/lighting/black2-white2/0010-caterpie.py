SOURCE = "sources/black2-white2/0010-caterpie.spu"
MATERIALS = [
    dict(name="outline", shades=[15, 1, 2], finish=0.1, body=0),
    dict(name="larval skin", shades=[1, 2, 3, 4, 5, 6], base=2, finish=0.45, body=0.15),
    # the cream underside, feet and tail tip, and the yellow rings along the sides: the same skin, paler
    dict(name="larval skin, pale parts", shades=[7, 8, 9, 10], base=2, finish=0.45, body=0.15),
    dict(name="larval skin, antenna", shades=[11, 12, 13, 14], base=1, finish=0.5, body=0.15),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[15, 7, 8, 9, 10], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("larval skin", [1, 2, 3, 4, 5, 6]), **to("larval skin, pale parts", [7, 8, 9, 10]),
          **to("larval skin, antenna", [11, 12, 13, 14])}
RULES = [
    # a caterpillar's segments are separate bulges: the lines between them are creases
    dict(thin_all={1: "outline", 2: "outline"}),
    dict(drawings=["atama", "head", "atama-eyes-*", "head-eyes-*"], colors={9: "eye (line art)", 10: "eye (line art)", 7: "eye (line art)", 8: "eye (line art)"}),
]
