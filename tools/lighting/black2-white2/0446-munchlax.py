SOURCE = "sources/black2-white2/0446-munchlax.spu"
MATERIALS = [
    dict(name="outline", shades=[14], finish=0.1, body=0),
    # body, arms and the ragged hem: the long fur the Pokédex names. Its dark teal contour is its darkest shade;
    # both views together are mostly painted in 3 (the back wholly)
    dict(name="fur", shades=[4, 3, 2, 1], base=1, finish=-0.7, body=0.05),
    # the cream spot on the chest: the same long coat, paler
    dict(name="fur, chest spot", shades=[6, 5], base=1, finish=-0.7, body=0.05),
    # head and ears: the same teal, but the art draws them smooth-edged with no tufts: a short coat
    dict(name="short fur, head", shades=[4, 3, 2, 1], base=1, finish=-0.2, body=0.05),
    # the cream jaw
    dict(name="short fur, face", shades=[7, 11, 6, 5], base=2, finish=-0.2, body=0.05),
    # the cream feet; the brown along a raised foot's edge is its contour
    dict(name="short fur, feet", shades=[7, 10, 6, 5], base=2, finish=-0.2, body=0.05),
    # the brown pad on each sole: bare skin, painted flat
    dict(name="dry hide, paw pads", shades=[10, 11], base=0, finish=0.05, body=0.03),
    dict(name="claws and teeth", shades=[13, 12, 15], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[9, 8], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[14, 12, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
HEAD, FACE, FEET, PAD = "short fur, head", "short fur, face", "short fur, feet", "dry hide, paw pads"
COLORS = {14: "outline", **to("fur", [4, 3, 2, 1]), **to("fur, chest spot", [6, 5]), **to(PAD, [10, 11]),
          **to("claws and teeth", [13, 12, 15]), **to("mouth", [9, 8])}
RULES = [
    # head (with the cream jaw) and ears, both views; the back view's two jaw-corner pixels are the jaw's
    dict(drawings=["atama", "atama-[23]", "atama*-eyes-*", "mimi-r", "mimi-l"],
         colors={**to(HEAD, [4, 3, 2, 1]), **to(FACE, [7, 11, 6, 5])}),
    # feet: at rest, and raised with the sole showing (those drawings carry other parts' names)
    dict(drawings=["foot-*", "hire-3-2", "hire-2-2"], colors=to(FEET, [7, 6, 5])),
    dict(view="back", drawings=["mimi-l-2", "mimi-r-3"], colors=to(FEET, [7, 6, 5])),
    dict(view="back", drawings=["mimi-l-2"], rect=[3, 3, 3, 2], colors={10: FEET}),
    dict(view="back", drawings=["mimi-r-3"], rect=[11, 10, 1, 1], colors={10: FEET}),
    # eyes: white, gray rim and pupil
    dict(drawings=["atama*-eyes-open"], colors=to("eye (line art)", [15, 12, 14])),
]
