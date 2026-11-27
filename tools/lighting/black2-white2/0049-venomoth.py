SOURCE = "sources/black2-white2/0049-venomoth.spu"
# "The wings are covered with dustlike scales": powdery and thin, Butterfree's wing
WING = dict(finish=0.05, body=0.3)
LILAC = [15, 14, 13, 12, 11]
MATERIALS = [
    # black, and the dark purple lines where one horn stands in front of another
    dict(name="outline", shades=[10, 15], finish=0.1, body=0),
    # head, its three horns and the thorax: soft shading in the art, no highlight. Base is the lilac most of
    # it shows in (the darker dome of the head and the thorax are almost wholly behind the wings from the back)
    dict(name="insect body", shades=LILAC, base=2, finish=0.2, body=0.05),
    # the brown abdomen and the small legs folded against it, painted on one ramp
    dict(name="insect body, abdomen and legs", shades=[7, 6, 5, 4], base=1, finish=0.2, body=0.05),
    dict(name="butterfly wing", shades=LILAC, base=4, **WING),
    # the darker strip along the front edge of the two upper wings: one flat color, so light only tints it
    dict(name="butterfly wing, front edge", shades=[], **WING),
    # the fangs: white in front, pale blue-gray in the shade behind
    dict(name="claws and teeth", shades=[3, 2, 1], base=1, finish=0.7, body=0.05),
    # wing veins and the zigzag lines on the abdomen: lines inside one surface, tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    dict(name="eye (line art)", shades=[10, 3, 2], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
EDGE = "butterfly wing, front edge"
# the palest lilac is the lit side of the middle horn and of the thorax from behind, not a glint
KEEP_TOP = ["insect body"]
def to(name, colors): return {c: name for c in colors}
COLORS = {10: "outline", **to("butterfly wing", LILAC), **to("insect body, abdomen and legs", [7, 6, 5, 4]),
          **to("eye (line art)", [3, 2]), 1: "claws and teeth"}
BODY = ["head", "body", "atama", "body1"]
def px(view, drawing, x, y, colors, w=1, h=1): return dict(view=view, drawings=[drawing], rect=[x, y, w, h], colors=colors)
RULES = [
    dict(drawings=BODY, colors=to("insect body", LILAC)),
    # a wing is one flat sheet: its veins are lines on it
    dict(drawings=["wimg-r", "wing-r", "wing-l-2", "wing-l", "hane-r1", "hane-r2"], colors={14: INNER}),
    # the strip along the front edge, row by row: left of the first vein on the right wing...
    *[px("front", "wimg-r", 0, y, {14: EDGE}, w=w, h=h) for y, w, h in
      [(1, 24, 1), (2, 21, 3), (5, 19, 4), (9, 16, 4), (13, 13, 6), (19, 11, 6), (25, 9, 8), (33, 6, 12)]],
    # ...and right of the last vein on the left wing, which is seen almost edge on
    *[px("front", "wing-l-2", x, y, {14: EDGE}, w=32 - x, h=h) for x, y, h in
      [(0, 3, 3), (4, 6, 2), (5, 8, 3), (7, 11, 4), (10, 15, 3), (11, 18, 3), (13, 21, 2), (15, 23, 5), (17, 28, 2), (18, 30, 15)]],
    dict(drawings=["wing-l-2"], interior={15: ([12, 13, 14], INNER)}),     # the line where that strip begins
    # the near wings seen from behind are painted a shade darker: there the color is the wing's own shadow
    # where it is broad and a vein where it is one pixel wide
    dict(drawings=["hane-l1", "hane-l2"], thin_all={14: INNER}),
    px("back", "hane-l1", 25, 33, {14: INNER}, w=2, h=2),      # two veins crossing
    # the zigzag lines are drawn on one smooth abdomen
    dict(drawings=["body", "body1", "body2"], interior={10: ([4, 5, 6, 7], INNER)}),
    # one horn in front of another: those lines are creases
    px("front", "head", 11, 17, {15: "outline"}, h=2),
    px("front", "head", 17, 17, {15: "outline"}),
    px("front", "head", 18, 16, {15: "outline"}),
    px("back", "atama", 6, 19, {15: "outline"}),
    px("back", "atama", 11, 16, {15: "outline"}, h=2),
    px("back", "atama", 10, 18, {15: "outline"}),
    # the pupil of the eye that faces the viewer
    px("front", "head", 19, 23, {10: "eye (line art)"}, w=3, h=2),
    px("front", "head", 21, 22, {10: "eye (line art)"}),
    # the fangs under the head
    px("front", "head", 0, 27, {2: "claws and teeth"}, w=24, h=5),
    px("back", "atama", 0, 26, {3: "claws and teeth"}, w=24, h=4),
]
