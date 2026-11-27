SOURCE = "sources/black2-white2/0043-oddish.spu"
# Oddish is a root with a tuft of leaves: every surface is plant. The painted art shades the blue body flat
# and soft, so it is matte. Each leaf carries a pale patch in the art, and Ruby says "The more fertile the
# soil, the glossier its leaves become", so the leaves get a soft sheen (0.3) over the standard leaf's 0.15.
# Colors: 15 black; 14 13 12 11 the blues; 7 6 5 4 the greens; 2 3 red (mouth, eyes).
# The root: matte like the standard plant body (0.1), but thick and solid. At 0.15 light through (Cacturne's
# trunk) the blue washed out to gray with the sun behind it; at 0.1 it stays blue-gray.
ROOT = dict(finish=0.1, body=0.1)
MATERIALS = [
    # black; and the body's darkest blue where it draws the mouth line and the shut eyes
    dict(name="outline", shades=[15, 14], finish=0.1, body=0),
    # the round blue root and its two root feet
    dict(name="plant body", shades=[14, 13, 12], base=1, **ROOT),
    # the pale patch on the brow (front view), the same root. Its color is rare, so in the body's row the tool
    # leaves it out and it stayed pale on a body gone dark (sun behind); kept in that row (KEEP_TOP) the back
    # broke into a dark blotch in the cave. As its own row it darkens with the body.
    dict(name="plant body, highlight", shades=[13, 12, 11], base=2, **ROOT),
    dict(name="glossy leaves", shades=[7, 6, 5, 4], base=1, finish=0.3, body=0.35),
    dict(name="mouth", shades=[2, 3], base=0, finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # the leaves' midribs: tinted, never a crease
    dict(name="eye (line art)", shades=[3], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("plant body", [14, 13, 12]), 11: "plant body, highlight",
          **to("glossy leaves", [7, 6, 5, 4]), **to("mouth", [2, 3])}
RULES = [
    # the midrib drawn in the dark green inside each leaf (the same green along a leaf's edge is its darkest shade)
    dict(drawings=["hear*", "leaf[1-5]"], interior={7: ([4, 5, 6], INNER)}),
    # the mouth line (shut, and the upper lip of the open mouth) is drawn line; the red under it is the mouth
    dict(drawings=["mouse", "mouse-2", "mouse-3"], colors={14: "outline"}),
    # the eyes are one red pixel each; shut, they are lines
    dict(drawings=["body-eyes-open"], colors={3: "eye (line art)"}),
    dict(drawings=["body-eyes-closed"], colors={14: "outline"}),
]
