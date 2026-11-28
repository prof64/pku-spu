# Poliwrath: the same frog, all muscle. Blue skin (frog skin); a white belly with the black swirl; white hands
# like gloves, which are its own skin. In this palette black is color 10.
SOURCE = "sources/black2-white2/0062-poliwrath.spu"
MATERIALS = [
    dict(name="outline", shades=[10], finish=0.1, body=0),
    # the blue skin: the navy contour (14) is its darkest shade. The front's lit side is painted in 12, the back
    # and everything in shade in 13: the base is the shade between them (7, the line's base). With 13, the most
    # used, the face came out a step too dark under a lamp and in a field
    dict(name="frog skin", shades=[14, 13, 7, 12, 11], base=2, finish=0.3, body=0.1),
    # the white belly, painted flat white and pale gray
    dict(name="frog skin, belly", shades=[3, 2, 1], base=1, finish=0.3, body=0.1),
    # the swirl, black with a dark gray soft edge: color in the belly, never a crease
    dict(name="frog skin, belly swirl", shades=[], finish=0.3, body=0.1),
    # the white hands: the same skin. Their dark gray contour (9) is their darkest shade; white in front and gray (3)
    # from behind, so the base is the pale gray between
    dict(name="frog skin, hands", shades=[9, 8, 3, 2, 1], base=3, finish=0.3, body=0.1),
    dict(name="eye (line art)", shades=[10, 4, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {10: "outline", **to("frog skin", [14, 13, 7, 12, 11]), **to("frog skin, hands", [9, 8, 4, 3, 2, 1])}
EYE = to("eye (line art)", [10, 4, 2, 1])
RULES = [
    dict(view="front", drawings=["body"], colors={**to("frog skin, belly", [3, 2, 1]), 9: "frog skin, belly swirl"},
         interior={10: ([1, 2, 3, 9], "frog skin, belly swirl")}),
    # the eyes: white, the black pupil and lid line, their gray corners (the nostrils between them stay line)
    dict(drawings=["body-eyes-open"], rect=[2, 6, 7, 6], colors=EYE),
    dict(drawings=["body-eyes-open"], rect=[22, 6, 8, 6], colors=EYE),
]
