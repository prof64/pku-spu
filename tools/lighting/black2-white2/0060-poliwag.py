# Poliwag: a tadpole. Thin, damp blue skin (frog skin); pink lips; the white belly is skin so thin the coiled
# insides show through it as the black swirl; a pale, thin tail fin round a dark blue tail.
SOURCE = "sources/black2-white2/0060-poliwag.spu"
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the blue skin: the navy contour (14) is its darkest shade; the front is painted mostly in 12, the back in 7
    dict(name="frog skin", shades=[14, 13, 7, 12, 11], base=2, finish=0.3, body=0.1),
    # the tail itself, inside its fin: the same skin, painted in the two navies only
    dict(name="frog skin, tail", shades=[14, 13], base=0, finish=0.3, body=0.1),
    # "its thick lips, which act like a suction cup" (Shield): the same skin, pink
    dict(name="frog skin, lips", shades=[10, 9, 8], base=0, finish=0.3, body=0.1),
    # the white belly: "Its skin is so thin, its internal organs are visible" (Black 2/White 2). Still skin, and
    # painted flat white and gray: with more light through it (Belly, 0.25) it stayed pale pink with the sun behind
    dict(name="frog skin, belly", shades=[4, 3, 2, 1], base=2, finish=0.3, body=0.1),
    # the swirl (the insides showing through) and its gray soft edge: color in the belly, never a crease
    dict(name="frog skin, belly swirl", shades=[], finish=0.3, body=0.1),
    # the tail fin: thin pale skin the art paints see-through; its dark gray upper edge is its darkest shade
    dict(name="fin", shades=[4, 3, 2, 1], base=3, finish=0.3, body=0.15),
    dict(name="eye (line art)", shades=[15, 4, 3, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("frog skin", [14, 13, 7, 12, 11]), **to("frog skin, lips", [10, 9, 8]),
          **to("frog skin, belly", [4, 3, 2, 1])}
EYE = to("eye (line art)", [15, 4, 3, 1])
SWIRL = to("frog skin, belly swirl", [15, 4])
RULES = [
    dict(drawings=["sipo", "tail01"], colors={**to("fin", [4, 3, 2, 1]), **to("frog skin, tail", [14, 13])}),
    # the swirl on the belly, row by row of the belly (the body's black outline runs just outside these)
    *[dict(view="front", drawings=["head"], rect=r, colors=SWIRL) for r in
      ([14, 14, 5, 1], [6, 15, 14, 2], [5, 17, 16, 6], [6, 23, 14, 1], [7, 24, 13, 1], [8, 25, 11, 1])],
    # from behind only the belly's edge shows, with the swirl's outer turn on it
    *[dict(view="back", drawings=["head01"], rect=r, colors=SWIRL) for r in ([27, 16, 1, 2], [26, 18, 1, 3], [25, 21, 1, 3])],
    # the eyes: white, the big black pupil, its gray reflection
    dict(view="front", drawings=["head"], rect=[5, 6, 4, 5], colors=EYE),
    dict(view="front", drawings=["head"], rect=[15, 5, 5, 6], colors=EYE),
    dict(drawings=["head-eyes-open", "head01-eyes-open"], colors=EYE),
]
