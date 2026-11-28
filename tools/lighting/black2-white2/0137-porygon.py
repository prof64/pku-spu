# Porygon: a man-made figure built of flat faces, in two colors. The art paints every face as one flat
# wash with no highlight, so it is matte and solid; a matte row is lit flat, which is what flat faces need.
SOURCE = "sources/black2-white2/0137-porygon.spu"
# a trace of light through, as skin has: with none the whole figure went a step dull in a field
BODY = dict(finish=0.1, body=0.05)
PINK = [5, 4, 3, 2, 12]
BLUE = [10, 9, 8, 7]
MATERIALS = [
    # black, and the softened line in maroon (6) and dark teal (11). Those two are never the fill of a face:
    # they draw the contour and the edges where two faces meet, so they are lines, and each face is lit on
    # its own. As the body's darkest shades the back of the head sank to flat maroon in a field
    dict(name="outline", shades=[1, 6, 11], finish=0.1, body=0),
    # head, back and chest. The front is painted in the pale pinks (3, 2), the back a step or two darker
    # (5); base is the shade between. With 5 the front's head went one flat dark pink in a field.
    # The white (12) is four pixels of lit edge down the front of the head
    dict(name="solid body, pink", shades=PINK, base=1, **BODY),
    # beak, belly, feet and tail
    dict(name="solid body, blue", shades=BLUE, base=0, **BODY),
    # the six-sided eye: white, its gray lower edge, the pupil, and the line of the closed look
    dict(name="eye (line art)", shades=[1, 13, 12], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
EYE = to("eye (line art)", [12, 13])
COLORS = {**to("outline", [1, 6, 11]), **to("solid body, pink", [5, 4, 3, 2]), **to("solid body, blue", BLUE), **EYE}
RULES = [
    dict(drawings=["head-eyes-*"], colors={**EYE, 1: "eye (line art)"}),
    # the white edge down the front of the head is the pink surface, not the eye
    dict(view="front", drawings=["head"], rect=[8, 10, 2, 4], colors={12: "solid body, pink"}),
]
# that white edge stayed bright on a head gone dark (cave, sun behind) when left out of its row
KEEP_TOP = ["solid body, pink"]
