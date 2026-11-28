SOURCE = "sources/black2-white2/0104-cubone.spu"
BONE = [8, 7, 6, 5]
H = dict(finish=0.25, body=0.08)
MATERIALS = [
    # black; and the one dark olive pixel at the corner of the shut eye, part of its lid line
    dict(name="outline", shades=[15, 9], finish=0.1, body=0),
    # the skull helmet and the bone club: old dry bone, painted in flat soft grays with no highlight, so dull
    # and solid. Its olive contour (9, 8) is its own darkest shade. Base is the mid gray (7): the whole back of
    # the skull and most of the club are painted in it; the white (5) is the lit front of the skull
    dict(name="bone", shades=BONE, base=2, finish=0.2, body=0),
    # plain bare brown skin, painted flat; the dark brown (4) is its contour, the tan (2) its lit side
    dict(name="hide", shades=[4, 3, 2], base=1, **H),
    # the eight palest pixels (1) on the front thigh: the same skin at its most lit. In their own row so they
    # darken with the leg; left as a painted glint they would stay pale on a body in shade
    dict(name="hide, lit patches", shades=[4, 3, 2, 1], base=1, **H),
    # the cream stomach
    dict(name="hide, belly", shades=[12, 11], base=1, **H),
    # the white toe claws and thumb claw, shaded in the skull's pale grays
    dict(name="claws and teeth", shades=[7, 6, 5], base=2, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[15, 8, 6, 5], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", 9: "outline", **to("bone", BONE), **to("hide", [4, 3, 2]), 1: "hide, lit patches", **to("hide, belly", [12, 11])}
EYE = to("eye (line art)", [15, 8, 6, 5])
def rects(drawing, colors, *boxes):
    return [dict(view="front", drawings=[drawing], rect=list(b), colors=colors) for b in boxes]
RULES = [
    # claws: every white and pale gray pixel on a foot, and the thumb's on the near hand
    dict(drawings=["foot-*", "hand-l"], colors=to("claws and teeth", [7, 6, 5])),
    # the eye inside the socket: white, its gray shade and the pupil (the brown around it is skin)
    *rects("head-eyes-open", EYE, [9, 3, 2, 1], [8, 4, 3, 1], [7, 5, 4, 1]),
    *rects("head", EYE, [17, 15, 2, 1], [16, 16, 3, 1], [15, 17, 4, 1]),
    # the shut eye's line ends in one dark olive pixel
    *rects("head-eyes-closed", {9: "outline"}, [7, 5, 1, 1]),
]
