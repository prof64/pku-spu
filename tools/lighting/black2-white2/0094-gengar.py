# Gengar: one soft dark body, a grin of white teeth, red eyes.
SOURCE = "sources/black2-white2/0094-gengar.spu"
BODY = [14, 13, 10, 12, 11]
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the whole body, ears, limbs and back spikes: the same stuff as Gastly's ball and Haunter, so their dials.
    # No entry names what it is made of (it "hides in shadows"); the art paints soft cloudy patches on the
    # forehead, belly and knee and no highlight. The back view is wholly the dark violet (13); the plum
    # contour (14) is its darkest shade.
    dict(name="ghost body", shades=BODY, base=1, finish=-0.1, body=0),
    # the grin: white, its gray at the corners
    dict(name="claws and teeth", shades=[7, 2, 1], base=2, finish=0.7, body=0.05),
    # the gray lines between the teeth, the black lines of the shut eyes: tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    # red, its pink light and the black slit pupils
    dict(name="eye (line art)", shades=[6, 5], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("ghost body", BODY), **to("claws and teeth", [7, 2, 1]), 3: INNER,
          **to("eye (line art)", [5, 6])}
RULES = [
    dict(drawings=["hand-r-eyes-open"], colors={15: "eye (line art)"}),
    dict(drawings=["hand-r-eyes-closed"], interior={15: (BODY, INNER)}),
]
# the pale lilac is the cloudy light the art paints on the forehead, ears, hands and knee: a real shade.
# Left out of the row those patches stayed pale on a body gone dark with the sun behind.
KEEP_TOP = ["ghost body"]
