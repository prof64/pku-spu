SOURCE = "sources/black2-white2/0108-lickitung.spu"
MATERIALS = [
    # black line; the shut eyes' lash line is drawn in the skin's dark maroon
    dict(name="outline", shades=[15, 14], finish=0.1, body=0),
    # the pink skin (head, body, arms, legs, tail): painted flat and soft in the official art, no highlight.
    # Its maroon contour is its darkest shade; both views together are mostly painted in 12
    dict(name="hide", shades=[14, 13, 12, 11, 10], base=2, finish=0.25, body=0.08),
    # the cream bands across the belly and the ring on each knee: color in the same skin
    dict(name="hide, belly bands and knee rings", shades=[5, 4, 3], base=1, finish=0.25, body=0.08),
    # the tongue: "saliva-covered" (Black 2/White 2), painted with one broad soft light patch and no hard
    # highlight: a wet sheen, kept below polished (at the mouth's 0.8 a tongue this big broke into specks under
    # the lamp and went half dark in the field). The front is painted in 7, the back in 8; 7 is most of it
    dict(name="tongue", shades=[9, 8, 7, 6], base=2, finish=0.5, body=0),
    # the nail on each hand and the white toes of each foot, with the palette's gray
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    # inside the open mouth, behind the tongue: one flat dark maroon
    dict(name="mouth", shades=[14], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[15, 14, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("hide", [14, 13, 12, 11, 10]), **to("hide, belly bands and knee rings", [5, 4, 3]),
          **to("tongue", [9, 8, 7, 6]), **to("claws and teeth", [2, 1])}
EYE = to("eye (line art)", [15, 14, 1])
LASH = {14: "outline"}
RULES = [
    # inside the mouth (front view); the jaw's own contour beside it stays skin
    dict(view="front", drawings=["atama"], rect=[10, 18, 11, 7], colors={14: "mouth"}),
    # the eyes: black pupil, white catchlight and the maroon ring around them
    dict(view="front", drawings=["atama"], rect=[19, 11, 4, 4], colors=EYE),
    dict(view="front", drawings=["atama"], rect=[7, 12, 2, 3], colors=EYE),
    dict(view="front", drawings=["atama-eyes-open"], rect=[16, 7, 4, 4], colors=EYE),
    dict(view="front", drawings=["atama-eyes-open"], rect=[4, 8, 2, 3], colors=EYE),
    dict(view="back", drawings=["head01"], rect=[25, 9, 3, 3], colors=EYE),
    dict(view="back", drawings=["head01-eyes-open"], rect=[3, 4, 3, 3], colors=EYE),
    # shut eyes: a drawn line
    dict(view="front", drawings=["atama-eyes-closed"], rect=[16, 8, 4, 3], colors=LASH),
    dict(view="front", drawings=["atama-eyes-closed"], rect=[4, 8, 3, 3], colors=LASH),
    dict(view="back", drawings=["head01-eyes-closed"], rect=[3, 5, 3, 2], colors=LASH),
]
# the pale patch on the head, tail and arms and the tongue's light strip are broad soft light, not glints
KEEP_TOP = ["hide", "tongue"]
