# Aerodactyl: plain gray hide all over, thin purple wing membrane, saw teeth, a wet open mouth.
SOURCE = "sources/black2-white2/0142-aerodactyl.spu"
GRAY, PURPLE = [5, 4, 3, 2], [9, 8, 7, 6]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # body, head, tail, legs and the wing's arm and fingers: plain bare skin, painted with flat soft shading
    dict(name="hide", shades=GRAY, base=1, finish=0.25, body=0.08),
    # the thin purple skin under the wing; its darkest purple is its drawn edge and folds
    dict(name="wing membrane", shades=PURPLE, base=1, finish=0.3, body=0.3),
    # a wing seen from its gray outer side (the back view's near wing, and the down-stroke pictures of both
    # views): arm and membrane are drawn as one gray sheet. Less light through than the purple side: at 0.3
    # the sheet turned pink in plain daylight and stayed brighter than the body in the cave
    dict(name="wing membrane, outer side", shades=GRAY, base=1, finish=0.3, body=0.2),
    # the saw teeth: white and the palette's gray
    dict(name="claws and teeth", shades=[15, 14], base=1, finish=0.7, body=0.05),
    # the inside of the open mouth (dark red) and the tongue (the two lighter reds)
    dict(name="mouth", shades=[12, 11, 10], base=0, finish=0.8, body=0),
    # green iris, white, its gray, and the dark pupil pixel drawn in the hide's contour color
    dict(name="eye (line art)", shades=[5, 13, 15, 14], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("hide", GRAY), **to("wing membrane", PURPLE), **to("claws and teeth", [15, 14]),
          **to("mouth", [12, 11, 10]), 13: "eye (line art)"}
EYE = to("eye (line art)", [5, 13, 15, 14])
OUTER = to("wing membrane, outer side", GRAY)
RULES = [
    dict(view="front", drawings=["wing-r-2", "wing-r-3", "wing-l-3"], colors=OUTER),
    dict(view="back", drawings=["wing-l", "wing-l-3", "wing-r-2", "wing-r-3"], colors=OUTER),
    dict(view="front", drawings=["head"], rect=[14, 11, 3, 2], colors=EYE),
    dict(view="front", drawings=["head"], rect=[16, 10, 1, 1], colors=EYE),
    dict(view="front", drawings=["head-eyes-open"], rect=[3, 3, 3, 2], colors=EYE),
    dict(view="front", drawings=["head-eyes-open"], rect=[5, 2, 1, 1], colors=EYE),
    dict(view="back", drawings=["atama"], rect=[14, 10, 2, 3], colors=EYE),
    dict(view="back", drawings=["atama-eyes-open"], rect=[4, 3, 2, 3], colors=EYE),
]
# the palest gray is the lit top of the snout, chest and tail: shading, not a glint (left out, it stayed pale on a body gone dark)
KEEP_TOP = ["hide"]
