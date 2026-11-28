# Poliwhirl: a frog-like tadpole. Moist blue skin (frog skin); a white belly with the black swirl; white hands
# like gloves, which are its own skin. Its eyes sit in two bumps on top of the head.
SOURCE = "sources/black2-white2/0061-poliwhirl.spu"
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the blue skin: the navy contour (14) is its darkest shade. The front is painted in 12, the back almost wholly
    # in 13: the base is the shade between them (10, Poliwag's base too). With 13, the most used, the front came
    # out a step too dark under a lamp and in a field
    dict(name="frog skin", shades=[14, 13, 10, 12, 11], base=2, finish=0.3, body=0.1),
    # the white belly: "the skin on its belly spiral feels smooth" (Silver). Painted flat, white above and gray
    # below: the base is the pale gray between (with white, its lower half went dark olive in a field)
    dict(name="frog skin, belly", shades=[4, 3, 2, 1], base=2, finish=0.3, body=0.1),
    # the swirl, black and (where the belly turns up toward the light) dark gray: color in the belly, never a crease
    dict(name="frog skin, belly swirl", shades=[], finish=0.3, body=0.1),
    # the white hands: the same skin. Their gray contours (9 in front, 8 from behind) are their darkest shades;
    # white in front and gray (3) from behind, so the base is the pale gray between
    dict(name="frog skin, hands", shades=[9, 8, 4, 3, 2, 1], base=4, finish=0.3, body=0.1),
    dict(name="eye (line art)", shades=[15, 9, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("frog skin", [14, 13, 10, 12, 11]), **to("frog skin, hands", [9, 8, 4, 3, 2, 1])}
RULES = [
    dict(view="front", drawings=["body"], colors={**to("frog skin, belly", [4, 3, 2, 1]), 9: "frog skin, belly swirl"},
         interior={15: ([1, 2, 3, 4, 9], "frog skin, belly swirl")}),
    dict(drawings=["body2-eyes-open"], colors=to("eye (line art)", [15, 9, 2, 1])),
]
