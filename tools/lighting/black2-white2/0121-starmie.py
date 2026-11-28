# Starmie: Staryu's surfaces again. Two matte starfish stars, a dull gold-colored casing, and the red
# core: a polished cut gem that shines.
SOURCE = "sources/black2-white2/0121-starmie.spu"
MATERIALS = [
    dict(name="outline", shades=[1, 6], finish=0.1, body=0),
    # both stars: flat brush-painted planes in the art, no highlight anywhere. The navy (6) is the contour
    # and the ridge down each arm: the skin's darkest shade, as on Staryu. Base is the blue-violet (5) that
    # most of both views is painted in (the whole rear star, and the front star's shaded faces)
    dict(name="starfish skin", shades=[6, 5, 4, 3, 2], base=1, finish=0.1, body=0.05),
    # the gold-colored fitting that holds the core, with its eight prongs: hard and dull; the art paints
    # lit faces and an olive shadow, no reflection
    dict(name="gold casing", shades=[11, 10, 9, 8, 7], base=2, finish=0.2, body=0),
    # the core: a polished red gem cut in faces, with a painted catchlight, and it shines (Black 2/White 2:
    # "Its core shines in many colors"). Body 0.6 as on Staryu. Base is the crimson (14) most faces are in
    dict(name="core gem", shades=[15, 14, 13, 12], base=1, finish=1, body=0.6),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("starfish skin", [6, 5, 4, 3, 2]), **to("gold casing", [11, 10, 9, 8, 7]),
          **to("core gem", [15, 14, 13, 12])}
RULES = [
    # one navy pixel at the tip of a prong, beside its black line: part of that line
    dict(drawings=["houseki"], colors={6: "outline"}),
]
# the palest lilac is the whole lit face of the upper arms, and the casing's pale color the lit face of
# each prong: shades, not glints
KEEP_TOP = ["starfish skin", "gold casing"]
# Staryu's two strengths, given the same way: the bright faces shine like a lamp, the darker faces less
GLOW = [
    dict(material="core gem", colors=[13, 12], glow=150, intent="the core shines: its bright faces"),
    dict(material="core gem", colors=[15, 14], glow=40, intent="the core's darker faces shine less"),
]
