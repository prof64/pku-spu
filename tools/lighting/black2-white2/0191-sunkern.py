SOURCE = "sources/black2-white2/0191-sunkern.spu"
# Sunkern is a seed with a sprout: every surface is plant, painted flat and soft in the official art.
# The only hard highlights in the art are the catchlights of the eyes.
# The seed itself: matte like the standard plant body (0.1), but denser than a bulb or a bud. At the plant
# body's 0.25 light through, the brown stripes washed out to pale tan in a field and the whole seed went
# orange with the sun behind it; at 0.15 the yellow stays yellow and the stripes stay brown.
SEED = dict(finish=0.1, body=0.15)
SPROUT = dict(finish=0.1, body=0.25)    # Plant body: the thin green stalk
MATERIALS = [
    dict(name="outline", shades=[13, 3], finish=0.1, body=0),
    # the yellow seed coat and its crown of points. The crown's olive-brown contour (color 3) is in the outline
    # row: the points overlap, and 3 is the stripes' color, so as the yellow's darkest shade it turned the
    # shadowed yellow stripe-brown
    dict(name="seed coat", shades=[4, 6, 7], base=2, **SEED),
    # the brown stripes and the patches around the eyes: color in the same seed coat
    dict(name="seed coat, stripes", shades=[2, 3], base=0, **SEED),
    dict(name="leaf", shades=[9, 10, 11, 12], base=2, finish=0.15, body=0.35),
    dict(name="stem", shades=[9, 10], base=1, **SPROUT),
    # two pixels inside the open mouth, painted in the seed coat's yellows (the palette has no pink)
    dict(name="mouth", shades=[4, 7], base=1, finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # the leaves' midribs: tinted, never a crease
    # black eyes, their white catchlights and gray reflections
    dict(name="eye (line art)", shades=[13, 14, 15], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {13: "outline", **to("seed coat", [4, 6, 7]), **to("seed coat, stripes", [2, 3]),
          **to("leaf", [9, 10, 11, 12]), **to("eye (line art)", [14, 15])}
HUSK_LINE = {3: "outline"}
EYE = {13: "eye (line art)"}
RULES = [
    # the crown: color 3 there is the line around and between its points, not a stripe
    dict(view="front", drawings=["head"], rect=[0, 0, 32, 12], colors=HUSK_LINE),
    dict(view="front", drawings=["head"], rect=[23, 13, 1, 1], colors=HUSK_LINE),
    dict(view="back", drawings=["head"], rect=[0, 0, 32, 14], colors=HUSK_LINE),
    dict(view="back", drawings=["head"], rect=[6, 14, 2, 3], colors=HUSK_LINE),
    dict(view="back", drawings=["head"], rect=[24, 16, 1, 1], colors=HUSK_LINE),
    # the eyes are black disks: their black is the eye, drawn on the head and again on the eye drawing
    dict(view="front", drawings=["head"], rect=[6, 13, 3, 4], colors=EYE),
    dict(view="front", drawings=["head"], rect=[14, 14, 5, 5], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[1, 2, 3, 4], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[9, 3, 5, 5], colors=EYE),
    dict(view="front", drawings=["head"], rect=[9, 19, 2, 1], colors=to("mouth", [4, 7])),
    # the sprout: the stalk, and the midrib drawn inside each leaf
    dict(drawings=["leaf-c"], colors=to("stem", [9, 10])),
    dict(drawings=["leaf-l", "leaf-r"], interior={10: ([9, 11, 12], INNER)}),
]
