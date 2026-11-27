SOURCE = "sources/black2-white2/0033-nidorino.spu"
MATERIALS = [
    # black, and the dark lines where a barb stands on the back or lies over the next one
    dict(name="outline", shades=[9, 13], finish=0.1, body=0),
    dict(name="hide", shades=[13, 12, 11, 10], base=1, finish=0.25, body=0.08),
    # the dark patches are painted in one flat color
    dict(name="hide, spots", shades=[13], base=0, finish=0.25, body=0.08),
    dict(name="hide, ear center", shades=[7, 6], base=0, finish=0.25, body=0.08),
    dict(name="spines", shades=[13, 12, 11], base=1, finish=0.4, body=0),            # the barbs along the back
    dict(name="spines, horn", shades=[13, 11, 10], base=1, finish=0.4, body=0),      # the forehead horn, painted paler
    dict(name="claws and teeth", shades=[15, 14, 1], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[4, 3], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[8, 14, 1], finish=0.9, body=0),
]
# the palest lilac is a small highlight on the brow, snout and foreleg: kept in the row so it darkens with the body
KEEP_TOP = ["hide"]
def to(name, colors): return {c: name for c in colors}
COLORS = {9: "outline", **to("hide", [13, 12, 11, 10]), **to("hide, ear center", [7, 6]),
          **to("claws and teeth", [15, 14, 1]), **to("mouth", [4, 3])}
EYE = to("eye (line art)", [8, 14, 1])
SPINE = to("spines", [13, 12, 11])
HORN = to("spines, horn", [13, 11, 10])
SPOT = {13: "hide, spots"}
LINE = {13: "outline"}
def rects(drawing, view, colors, *boxes):
    return [dict(view=view, drawings=[drawing], rect=list(b), colors=colors) for b in boxes]
RULES = [
    # the eyes are drawn only in the eye drawings; the same white and gray on the head is the fang
    dict(drawings=["head-eyes-*", "head01-eyes-*"], colors=EYE),
    # the horn
    *rects("head", "front", HORN, [9, 9, 2, 1], [7, 10, 4, 1], [5, 11, 5, 1], [3, 12, 6, 1], [2, 13, 6, 1]),
    *rects("head01", "back", HORN, [23, 9, 3, 1], [23, 10, 6, 1], [23, 11, 7, 1], [23, 12, 6, 1], [24, 13, 3, 1], [24, 14, 1, 1]),
    # the barbs, down to the dark line they stand on; that line and the lines between barbs are lines
    *rects("body2", "front", SPINE, [0, 0, 40, 13], [6, 13, 6, 1], [14, 13, 12, 1], [14, 14, 11, 1], [18, 15, 7, 1],
           [20, 16, 5, 1], [22, 17, 2, 1], [27, 15, 5, 4]),
    *rects("body2", "front", LINE, [12, 13, 2, 1], [6, 14, 5, 1], [13, 14, 1, 1], [15, 15, 3, 1], [18, 16, 2, 1],
           [20, 17, 2, 1], [24, 17, 3, 1]),
    # from behind the barbs are one cluster along the back, with one more low on the rump
    *rects("body02", "back", SPINE, [10, 4, 26, 10], [12, 14, 26, 5], [3, 15, 8, 4]),
    *rects("body02", "back", LINE, [19, 14, 2, 1], [28, 14, 1, 1], [12, 17, 2, 1], [11, 18, 2, 1]),
    # the dark patches
    *rects("body1", "front", SPOT, [18, 7, 4, 3], [25, 12, 4, 3]),
    *rects("l-leg01", "front", SPOT, [10, 8, 3, 4]),
    *rects("foot-r-b", "front", SPOT, [11, 12, 3, 4]),
    *rects("body01", "back", SPOT, [26, 9, 6, 4], [21, 11, 3, 2], [29, 14, 4, 2], [35, 13, 6, 3], [18, 15, 4, 3]),
    *rects("pr-leg01", "back", SPOT, [11, 11, 4, 3], [14, 15, 2, 2]),
    *rects("br-leg01", "back", SPOT, [13, 6, 4, 3]),
]
