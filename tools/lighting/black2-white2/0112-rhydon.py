SOURCE = "sources/black2-white2/0112-rhydon.spu"
HIDE = [14, 13, 12]
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the gray armor-like hide: dry and matte, the same row and dials as Rhyhorn's. The dark gray (14) is its
    # contour on the lit side, the tail's ring lines and the limb folds
    dict(name="plated hide", shades=HIDE, base=1, finish=0.2, body=0.03),
    # the near-white (11) the art paints on the crest tips, a knee, a shoulder and the brow ridge: the same hide
    # at its most lit, in its own row so it darkens with the body (as on Rhyhorn)
    dict(name="plated hide, edge light", shades=HIDE + [11], base=1, finish=0.2, body=0.03),
    # the hollow of the far ear seen from behind, painted in one flat dark gray
    dict(name="plated hide, ear inside", shades=[14, 13], base=0, finish=0.2, body=0.03),
    # the cream ribbed belly (and its edge seen from behind): the same dry skin, pale; the brown (5) is its
    # contour and the lines between the ribs
    dict(name="dry hide, belly", shades=[5, 4, 3], base=1, finish=0.05, body=0.08),
    # the drill horn: bare cream horn with brown spiral grooves, polished
    dict(name="claws and teeth, horn", shades=[5, 4, 3, 2], base=1, finish=0.7, body=0.05),
    # white claws and the fang; their shade is the hide's light grays, their lit-side edge the mid gray
    dict(name="claws and teeth", shades=[13, 12, 11, 1], base=3, finish=0.7, body=0.05),
    dict(name="mouth", shades=[8, 7, 6], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[15, 14, 7, 6, 12, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("plated hide", HIDE), 11: "plated hide, edge light", **to("dry hide, belly", [3, 4, 5]),
          2: "claws and teeth, horn", **to("mouth", [8, 7, 6]), 1: "claws and teeth"}
CLAW = to("claws and teeth", [13, 12, 11, 1])
def claws(view, drawings, *rects): return [dict(view=view, drawings=drawings, rect=r, colors=CLAW) for r in rects]
RULES = [
    # the horn is drawn in the head pictures, in the belly's colors
    dict(drawings=["head", "head-female", "atama", "atama-female"], colors=to("claws and teeth, horn", [2, 3, 4, 5])),
    dict(view="back", drawings=["r-mimi"], rect=[7, 6, 5, 8], colors={14: "plated hide, ear inside"}),
    # the eye: white, red iris, black rim; from behind its white is shaded light gray and its lower rim dark gray
    dict(view="front", drawings=["head*-eyes-open"], colors=to("eye (line art)", [15, 7, 6, 1])),
    dict(view="back", drawings=["atama*-eyes-open"], rect=[3, 2, 3, 5], colors=to("eye (line art)", [15, 14, 6, 12, 1])),
    # the fang
    dict(view="front", drawings=["head", "head-female"], rect=[26, 22, 1, 3], colors=CLAW),
    dict(view="front", drawings=["head", "head-female"], rect=[25, 23, 1, 1], colors=CLAW),
    dict(view="back", drawings=["atama", "atama-female"], rect=[23, 23, 2, 2], colors=CLAW),
    # each claw with its gray shade
    *claws("front", ["hand-r"], [3, 13, 2, 3], [6, 18, 3, 2], [10, 19, 1, 1], [11, 18, 2, 2]),
    *claws("front", ["foot-l1"], [6, 8, 2, 1], [8, 9, 4, 2]),
    *claws("front", ["hand-l2"], [4, 11, 3, 2], [5, 14, 1, 2], [8, 16, 1, 2]),
    *claws("front", ["foot-r"], [8, 9, 4, 3], [16, 8, 2, 1], [15, 9, 5, 2]),
    *claws("back", ["r-ude"], [19, 8, 2, 2], [19, 13, 2, 2], [16, 16, 2, 2]),
    *claws("back", ["asi"], [20, 7, 3, 2]),
]
