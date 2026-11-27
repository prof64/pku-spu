SOURCE = "sources/black2-white2/0030-nidorina.spu"
MATERIALS = [
    # black, and the dark lines where one barb lies over another or over the back
    dict(name="outline", shades=[15, 14, 13], finish=0.1, body=0),
    # the palette's palest blue is never drawn: it is the hide's own next lighter step
    dict(name="hide", shades=[14, 13, 12, 11, 10], base=2, finish=0.25, body=0.08),
    dict(name="hide, belly", shades=[14, 13, 12, 11], base=3, finish=0.25, body=0.08),
    dict(name="hide, spots", shades=[14, 13], base=0, finish=0.25, body=0.08),
    dict(name="hide, ear ring", shades=[6, 5], base=0, finish=0.25, body=0.08),
    dict(name="hide, ear center", shades=[5, 4], base=1, finish=0.25, body=0.08),
    dict(name="spines", shades=[14, 13, 12, 11], base=2, finish=0.4, body=0),       # the barbs on the back
    dict(name="claws and teeth", shades=[3, 2, 1], base=2, finish=0.7, body=0.05),
    dict(name="mouth", shades=[9, 8], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[9, 8, 7, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("hide", [14, 13, 12, 11, 10]), **to("hide, ear ring", [6, 5]), 4: "hide, ear center",
          **to("claws and teeth", [3, 2, 1]), **to("mouth", [9, 8]), 7: "eye (line art)"}
SPINE = to("spines", [11, 12, 13, 14])
SPINES = {**to("spines", [11, 12, 13]), 14: "outline"}      # a cluster: the dark lines part one barb from the next
LINE = {14: "outline", 13: "outline"}
SPOT = to("hide, spots", [13, 14])
BELLY = to("hide, belly", [11, 13, 14])
def rects(drawing, view, colors, *boxes):
    return [dict(view=view, drawings=[drawing], rect=list(b), colors=colors) for b in boxes]
RULES = [
    # the eyes are drawn only in the eye drawings; the same reds and white on the head are the mouth and a fang
    dict(drawings=["atama-eyes-*", "head01-eyes-*"], colors=to("eye (line art)", [9, 8, 7, 1, 2])),
    # the pale underside
    *rects("karada", "front", BELLY, [13, 20, 16, 10]),
    # the two barbs on the back, and the lines where they meet it
    *rects("karada", "front", SPINE, [25, 3, 7, 5], [25, 8, 6, 1], [26, 9, 5, 1], [27, 10, 4, 1], [28, 11, 3, 1],
           [33, 10, 2, 1], [31, 11, 5, 1], [32, 12, 3, 1], [33, 13, 2, 1], [33, 14, 2, 2]),
    *rects("karada", "front", LINE, [24, 9, 2, 1], [26, 10, 1, 1], [27, 11, 1, 1], [30, 12, 2, 1], [32, 13, 1, 1], [33, 14, 1, 2]),
    # from behind the barbs are a cluster along the back
    *rects("body01", "back", SPINE, [12, 3, 13, 3], [13, 6, 13, 1]),
    *rects("body01", "back", SPINES, [13, 7, 13, 1], [14, 8, 13, 2], [7, 9, 5, 5], [13, 10, 13, 1], [13, 11, 12, 1],
           [13, 12, 9, 1], [12, 13, 7, 1], [11, 14, 7, 1]),
    # the dark patches
    *rects("karada", "front", SPOT, [24, 13, 4, 3]),
    *rects("asi1", "front", SPOT, [5, 6, 4, 5], [4, 11, 3, 4]),
    *rects("body01", "back", SPOT, [22, 13, 6, 3]),
    *rects("r-leg01", "back", SPOT, [6, 6, 5, 5], [10, 11, 3, 3]),
]
