SOURCE = "sources/black2-white2/0011-metapod.spu"
MATERIALS = [
    dict(name="outline", shades=[15, 1, 2], finish=0.1, body=0),
    # the whole cocoon is one hard shell; its dark contour colors (1, 2) are its darkest shades
    dict(name="insect shell", shades=[1, 2, 3, 4, 5, 6], base=2, finish=0.45, body=0),
    # white, pupil, and the back view's pupil pixel drawn in the dark green
    dict(name="eye (line art)", shades=[15, 1, 14], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("insect shell", [1, 2, 3, 4, 5, 6]), 14: "eye (line art)"}
EYE = {14: "eye (line art)", 15: "eye (line art)"}
RULES = [
    # the plates stand proud of one another and the tail's rings overlap like Caterpie's segments:
    # the dark lines wholly inside the shell are creases, so each plate and ring is shaped on its own
    dict(interior={1: ([2, 3, 4, 5, 6], "outline"), 2: ([1, 3, 4, 5, 6], "outline")}),
    # the eye sits against the black outline of the head, so it is picked by place
    dict(view="front", drawings=["part-0"], rect=[22, 18, 5, 3], colors=EYE),
    dict(view="front", drawings=["part-0-eyes-open"], rect=[2, 3, 5, 3], colors=EYE),
    dict(view="back", drawings=["head"], rect=[22, 21, 3, 3], colors=EYE),
    dict(view="back", drawings=["head"], rect=[23, 22, 1, 1], colors={1: "eye (line art)"}),
    dict(view="back", drawings=["head-eyes-open"], rect=[3, 4, 3, 3], colors=EYE),
    dict(view="back", drawings=["head-eyes-open"], rect=[4, 5, 1, 1], colors={1: "eye (line art)"}),
]
