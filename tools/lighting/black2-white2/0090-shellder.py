SOURCE = "sources/black2-white2/0090-shellder.spu"
# Palette: 5 4 3 2 1 the purple shell, dark to light (1 is the eye's pale edge too); 6 7 8 the tongue;
# 13 gray (eye edges, closed-eye lines); 14 black (the line and the whole soft body); 15 white (eyes).
SHELL = [5, 4, 3, 2, 1]
MATERIALS = [
    # black line; one gray pixel softens it under the upper valve's lip
    dict(name="outline", shades=[14, 13], finish=0.1, body=0),
    # both valves, their spikes and the hinge: "a shell that is harder than diamond". Cloyster's row.
    # The art paints soft broad lighter bands along the ribs and no highlight: dull.
    dict(name="hard shell", shades=SHELL, base=2, finish=0.2, body=0),
    # the soft body inside ("Inside, however, it is surprisingly tender"): painted one flat black,
    # so light only tints it. Not line art, so it is one round mass, not a hole.
    dict(name="hide, black body", shades=[], finish=0.25, body=0.08),
    # the tongue that "is always kept hanging out". Not the standard wet Mouth (0.8): the art paints it flat
    # pink with one soft pale wash and no highlight, and at 0.8 this big tongue went dark and blotchy under a lamp.
    # Plain bare flesh: Hide.
    dict(name="hide, tongue", shades=[8, 7, 6], base=1, finish=0.25, body=0.08),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # the shut eyes' lines: tinted, never a crease
    dict(name="eye (line art)", shades=[14, 13, 1, 15], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
def px(view, drawing, points, colors):
    return [dict(view=view, drawings=[drawing], rect=[x, y, 1, 1], colors=colors) for x, y in points]
COLORS = {14: "outline", 13: "outline", **to("hard shell", SHELL), **to("hide, tongue", [8, 7, 6])}
EYE = to("eye (line art)", [13, 1, 15])
RULES = [
    # the body is black like the line: the broad black is the body, one-pixel strokes stay the line
    dict(drawings=["body", "body01", "body-eyes-*"], colors={14: "hide, black body"}, thin_all={14: "outline"}),
    dict(drawings=["sita"], colors={14: "outline"}),
    # eyes: white, the pale lilac and gray of their edge, and the pupils
    dict(drawings=["body-eyes-open"], rect=[5, 5, 17, 7], colors=EYE),
    *px("front", "body-eyes-open", [(6, 8), (15, 9)], {14: "eye (line art)"}),
    # shut eyes: gray and dark purple strokes on the black body
    dict(drawings=["body-eyes-closed"], rect=[5, 9, 17, 3], colors={13: INNER, 5: INNER}),
]
# The palest lilac is the lit tips of the spikes: a real shade of the shell (as on Cloyster). Left out of the
# row, the tips stay bright on a shell gone dark when the light is behind it.
KEEP_TOP = ["hard shell"]
