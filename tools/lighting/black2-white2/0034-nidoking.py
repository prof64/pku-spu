SOURCE = "sources/black2-white2/0034-nidoking.spu"
PALE = [4, 3, 2, 1]
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # "rock-hard hide" (FireRed), painted flat and matte: the line's own hide
    dict(name="hide", shades=[14, 13, 12, 11], base=1, finish=0.25, body=0.08),
    # the pale chest and belly; the black lines across it part one bulge from the next
    dict(name="hide, belly", shades=PALE, base=1, finish=0.25, body=0.08),
    dict(name="hide, ear center", shades=[10, 9, 8], base=1, finish=0.25, body=0.08),
    dict(name="spines", shades=[14, 13, 12, 11], base=1, finish=0.4, body=0),      # the horn, the head crest, the back spines
    dict(name="claws and teeth", shades=PALE, base=3, finish=0.7, body=0.05),
    dict(name="mouth", shades=[6, 5], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[3, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("hide", [14, 13, 12, 11]), **to("hide, belly", PALE),
          **to("hide, ear center", [10, 9, 8]), **to("mouth", [6, 5])}
SPINE = to("spines", [11, 12, 13, 14])
HARD = to("claws and teeth", PALE)
EYE = to("eye (line art)", [3, 1])
def rects(drawings, view, colors, *boxes):
    return [dict(view=view, drawings=drawings, rect=list(b), colors=colors) for b in boxes]
def spans(drawings, view, colors, y, *runs):      # one row after another from y down: (x, width)
    return [dict(view=view, drawings=drawings, rect=[x, y + i, w, 1], colors=colors) for i, (x, w) in enumerate(runs)]
RULES = [
    # white and gray on a hand, an arm or a foot is a claw; on the head it is a tooth
    dict(view="front", drawings=["hand*", "body-2", "foot*", "arm*", "head", "head-2"], colors=HARD),
    dict(view="back", drawings=["l-ude2", "l-ashi2", "atama", "karada-2", "*-eyes-*"], colors=HARD),
    # the eye: its white and the gray under it
    dict(view="front", drawings=["*-eyes-*"], colors=EYE),
    *rects(["head"], "front", EYE, [23, 24, 2, 3]), *rects(["head-2"], "front", EYE, [21, 19, 2, 3]),
    *rects(["*-eyes-*"], "back", EYE, [3, 3, 1, 2]),
    *rects(["atama"], "back", EYE, [30, 26, 1, 2]), *rects(["karada-2"], "back", EYE, [30, 18, 1, 2]),
    # the horn
    *spans(["head"], "front", SPINE, 20, (4, 10), (3, 10), (4, 9), (7, 5)),
    *spans(["head-2"], "front", SPINE, 15, (2, 10), (1, 10), (2, 9), (5, 5)),
    *spans(["atama"], "back", SPINE, 16, (37, 3), (34, 6), (31, 7), (28, 9), (27, 9)),
    *spans(["karada-2"], "back", SPINE, 8, (37, 3), (34, 6), (31, 7), (28, 9), (27, 9)),
    # the spikes on top of the head
    *rects(["head"], "front", SPINE, [17, 10, 4, 4], [21, 11, 3, 3], [25, 6, 3, 3], [25, 9, 2, 5]),
    *rects(["head-2"], "front", SPINE, [14, 1, 24, 8]),
    *rects(["atama"], "back", SPINE, [14, 10, 4, 6], [20, 11, 3, 3], [5, 14, 2, 1], [5, 15, 3, 1], [6, 16, 3, 1], [6, 17, 5, 1]),
    *rects(["karada-2"], "back", SPINE, [14, 2, 4, 6], [20, 3, 3, 3], [5, 6, 2, 1], [5, 7, 3, 1], [6, 8, 3, 1], [6, 9, 5, 1]),
    # the spines down the back
    dict(view="back", drawings=["toge*"], colors=SPINE),
    *spans(["body"], "front", SPINE, 4, (31, 2), (30, 3), (29, 4), (28, 4), (27, 5), (26, 5), (24, 7), (26, 5), (28, 2), (29, 1)),
    *spans(["body"], "front", SPINE, 12, (37, 2), (35, 4), (33, 6), (30, 8), (30, 8), (31, 6), (31, 6), (32, 4), (32, 4), (33, 2), (33, 2)),
    *spans(["body"], "front", SPINE, 20, (43, 2), (41, 4), (40, 5), (38, 6), (37, 7), (35, 8), (35, 7), (36, 6), (36, 5), (37, 3),
           (37, 3), (37, 2), (38, 1)),
]
# the lightest shade is a broad painted highlight (forehead, shoulders, knees, tail), not a glint
KEEP_TOP = ["hide", "spines"]
