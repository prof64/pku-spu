# Dratini: a smooth blue serpent that sheds its skin (Gold: "It repeatedly sheds its skin as it steadily grows
# longer"), white along the belly and over the snout, with a white fin at each side of the head. The painted
# art shades all of it flat and soft: one broad paler band along the back, no highlight anywhere.
# Palette: 1 black; 6 5 4 3 2 the blue (6 its navy contour); a 9 8 7 the gray-to-white of belly, snout and fins.
SOURCE = "sources/black2-white2/0147-dratini.spu"
BLUE, WHITE = [6, 5, 4, 3, 2], [10, 9, 8, 7]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # head, back and tail: the same dry serpent skin as Ekans's
    dict(name="snake scales", shades=BLUE, base=1, finish=0.15, body=0.05),
    # the white underside, the white snout it runs into, and the small white lump on the forehead
    # (Shield: "The small lump on a Dratini's forehead is actually a horn that's still coming in")
    dict(name="snake scales, belly and snout", shades=WHITE, base=2, finish=0.15, body=0.05),
    # the two head fins: thin skin on ribs, flat white in the art
    dict(name="fin", shades=WHITE, base=2, finish=0.3, body=0.15),
    dict(name="eye (line art)", shades=[1, 7, 9], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("snake scales", BLUE), **to("snake scales, belly and snout", WHITE)}
EYE = to("eye (line art)", [1, 7, 9])
RULES = [
    dict(drawings=["mimi0*", "*-ear01"], colors=to("fin", WHITE)),
    # one gray pixel on the head's top edge, where the far fin stands behind it
    dict(view="front", drawings=["atama"], rect=[13, 4, 1, 1], colors={10: "fin"}),
    # the eye: black, its white catchlight and one gray pixel; on the head and again on the eyes drawing
    dict(view="front", drawings=["atama"], rect=[10, 8, 5, 5], colors=EYE),
    dict(drawings=["atama-eyes-open"], rect=[2, 1, 5, 5], colors=EYE),
]
# the palest blue is the broad lit patch on the forehead: a real shade. Left out of the row it stayed pale on a
# head gone dark with the sun behind.
KEEP_TOP = ["snake scales"]
