SOURCE = "sources/black2-white2/0143-snorlax.spu"
# Snorlax: a teal coat (head, ears, arms, back and sides), cream face, belly and feet, a brown pad on each
# sole, white claws and two fangs. Eyes are closed slits drawn in black. Rows follow Munchlax: the body's
# coat is fur, the head and face and feet a short coat, the pads bare skin.
# Palette: 1 black; 2 3 4 5 teal; 6 7 8 cream; 9 13 14 the browns that contour the cream (14 is also the pad
# and the inside of the open mouth); 10 11 12 white and grays (claws, fangs); 15 the pad's dark ring.
FUR = dict(finish=-0.1, body=0.05)        # fur over a whole body: -0.7 turns grainy on anything this big
SHORT = dict(finish=-0.2, body=0.05)
TEAL = [5, 4, 3]
CREAM = [8, 6, 7]
MATERIALS = [
    # black; the gray that softens the ends of the eye lines; three dark pixels under the left foot's claws;
    # and the thin brown contour of the cream (in the cream's rows it spread a muddy brown band over the
    # lower belly and speckled the feet)
    dict(name="outline", shades=[1, 12, 15, 9, 14, 13], finish=0.1, body=0),
    # body and arms. The dark teal (5) is its contour and its shadow; the lit side of both views is painted in 4
    dict(name="fur", shades=TEAL, base=1, **FUR),
    # the cream belly: the same coat, paler. Its base is the darker cream of its lower half: with the palest as
    # base, the lower belly (two shades down) was lit as if it faced the ground, and went olive in the field
    # and black in the cave
    dict(name="fur, belly", shades=CREAM, base=0, **FUR),
    # head and ears
    dict(name="short fur, head", shades=TEAL, base=1, **SHORT),
    # ten palest pixels (2) on the forehead: the same coat at its most lit, in their own row so they darken
    # with the head
    dict(name="short fur, head, lit patches", shades=TEAL + [2], base=1, **SHORT),
    dict(name="short fur, face", shades=CREAM, base=2, **SHORT),
    # the feet are mostly painted in the darker cream
    dict(name="short fur, feet", shades=CREAM, base=0, **SHORT),
    # the brown pad on each sole: bare skin, painted flat (as Munchlax)
    dict(name="dry hide, paw pads", shades=[15, 14], base=1, finish=0.05, body=0.03),
    dict(name="claws and teeth", shades=[12, 11, 10], base=2, finish=0.7, body=0.05),
    # the inside of the mouth when it yawns: one flat brown
    dict(name="mouth", shades=[14], base=0, finish=0.8, body=0),
]
def to(name, colors): return {c: name for c in colors}
HEAD, FACE, FEET, PAD = "short fur, head", "short fur, face", "short fur, feet", "dry hide, paw pads"
COLORS = {**to("outline", [1, 9, 13, 14]), **to("fur", TEAL), **to("fur, belly", CREAM),
          **to("claws and teeth", [12, 11, 10]), 15: PAD}
RULES = [
    # the head, and the eye and mouth drawings laid over it
    dict(drawings=["head", "eye*", "mouth*"], colors={**to(HEAD, TEAL), 2: "short fur, head, lit patches", **to(FACE, CREAM)}),
    # the eyes are closed slits: black lines with a gray pixel softening each end
    dict(drawings=["eye*"], colors={12: "outline"}),
    dict(drawings=["mouth-2"], colors={14: "mouth"}),
    # the feet: cream, and the pad (the back view's foot drawing also holds a piece of the body's coat)
    dict(drawings=["foot-*"], colors={**to(FEET, CREAM), 14: PAD, 15: PAD}),
    # three dark pixels under the left foot's claws: a line, not pad
    dict(view="front", drawings=["foot-l"], rect=[8, 11, 3, 1], colors={15: "outline"}),
]
