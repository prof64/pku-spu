SOURCE = "sources/black2-white2/0032-nidoran.spu"
MATERIALS = [
    dict(name="outline", shades=[2], finish=0.1, body=0),
    # the mid purple (9) is the hide's soft contour on the far ear, the far hand and the toes
    dict(name="hide", shades=[13, 9, 12, 11, 10], base=2, finish=0.25, body=0.08),
    # the haunch ring is painted in the mid purple from the front; from behind every spot is the dark purple
    dict(name="hide, spots", shades=[13, 9], base=0, finish=0.25, body=0.08),
    # the whole inside of the ear is one teal, shaded dark to light
    dict(name="hide, ear center", shades=[8, 7, 6], base=0, finish=0.25, body=0.08),
    dict(name="spines", shades=[13, 12, 11], base=1, finish=0.4, body=0),              # the crest of barbs on the back
    dict(name="spines, horn", shades=[13, 12, 11, 10], base=1, finish=0.4, body=0),    # the forehead horn, painted paler
    dict(name="claws and teeth", shades=[15, 14, 1], base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[5, 4, 3, 14, 1], finish=0.9, body=0),
]
# the palest lilac is a small highlight on the forehead and the ear rim: kept in the row so it darkens with the head
KEEP_TOP = ["hide"]
def to(name, colors): return {c: name for c in colors}
COLORS = {2: "outline", **to("hide", [13, 9, 12, 11, 10]), **to("hide, ear center", [8, 7, 6]),
          **to("claws and teeth", [15, 14, 1])}
EYE = to("eye (line art)", [5, 4, 3, 14, 1])
SPINE = to("spines", [13, 12, 11])
HORN = to("spines, horn", [13, 12, 11, 10])
SPOT = to("hide, spots", [13, 9])
def rects(drawing, view, colors, *boxes):
    return [dict(view=view, drawings=[drawing], rect=list(b), colors=colors) for b in boxes]
RULES = [
    # the eye is drawn on the head and again in the eye drawings; the same white and gray lower down is the incisor
    dict(drawings=["head-eyes-*"], colors=EYE),
    *rects("head", "front", EYE, [12, 11, 5, 5]),
    *rects("head", "back", EYE, [15, 9, 4, 5]),
    # the far eye, seen edge on, is drawn as a dark patch of lid under its brow line: shaded as a marking
    # (as line art it stayed bright purple on a head gone dark)
    *rects("head", "front", SPOT, [7, 14, 2, 2]),
    # the horn
    *rects("head", "front", HORN, [3, 7, 5, 1], [2, 8, 6, 1], [3, 9, 5, 1]),
    *rects("head", "back", HORN, [17, 5, 5, 1], [18, 6, 3, 1], [19, 7, 1, 1]),
    # the barbs: two tall ones behind the ear and a small one on the rump from the front, a crest of them from behind
    *rects("body2", "front", SPINE, [0, 0, 16, 8], [9, 8, 7, 2]),
    *rects("body", "front", SPINE, [9, 3, 2, 3]),
    dict(view="back", drawings=["hire-*"], colors=SPINE),
    # the dark spots
    *rects("body", "front", SPOT, [9, 7, 3, 2], [8, 9, 4, 1], [6, 10, 5, 2]),
    *rects("body", "back", SPOT, [22, 6, 4, 3], [18, 10, 4, 2]),
    *rects("head", "back", SPOT, [3, 13, 4, 3]),
    *rects("foot-fr", "back", SPOT, [4, 4, 2, 2]),
]
