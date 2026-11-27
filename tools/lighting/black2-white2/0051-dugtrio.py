SOURCE = "sources/black2-white2/0051-dugtrio.spu"
ROCK = [9, 8, 7]
MATERIALS = [
    # black; the dark brown (15) the brows and the shut eyes are drawn in; one soft pixel (14) of a shut eye
    dict(name="outline", shades=[11, 15, 14], finish=0.1, body=0),
    # the brown skin of the three heads and their columns: plain bare skin, painted with flat soft shading
    # (the pale crown is the dome catching light, not a sheen). Its dark-brown contour (15) is its darkest shade
    dict(name="hide", shades=[15, 14, 13, 12], base=2, finish=0.25, body=0.08),
    # the noses: the painted art gives each, and nothing else, a crisp pale highlight
    dict(name="nose", shades=[5, 4, 3, 2], base=1, finish=0.45, body=0.08),
    # the dug-up earth and stones around them: dead matte and solid
    # (base is the mid olive: the light one is a little ahead in what shows, but as base it dropped every
    # shaded face to the darkest olive in the field and the cave, and the stones went blotchy)
    dict(name="rock", shades=ROCK, base=1, finish=0, body=0),
    # the pale tops (6) of the stones: the same stone at its most lit, in their own row so they darken with the rest
    dict(name="rock, lit faces", shades=ROCK + [6], base=1, finish=0, body=0),
    dict(name="eye (line art)", shades=[11, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {11: "outline", **to("hide", [15, 14, 13, 12]), **to("nose", [5, 4, 3, 2]), **to("rock", ROCK),
          6: "rock, lit faces", 1: "eye (line art)"}
KEEP_TOP = ["hide", "nose"]
RULES = [
    # the eyes: black ovals with a white catchlight under slanted brows drawn in the dark brown
    dict(drawings=["body-*-eyes-open"], colors={11: "eye (line art)", 1: "eye (line art)", 15: "outline"}),
    # shut, they are short drawn lines
    dict(drawings=["body-*-eyes-closed"], colors={15: "outline", 11: "outline"}),
    dict(drawings=["body-r-eyes-closed"], rect=[10, 6, 1, 1], colors={14: "outline"}),
]
