SOURCE = "sources/black2-white2/0012-butterfree.spu"
# powdery and thin; 0.3 through, not 0.4: at 0.4 the white wings lose their shadows in the cave and look lit from inside
WING = dict(finish=0.05, body=0.3)
MATERIALS = [
    # black, and the antennae with the two dark colors of their club tips
    dict(name="outline", shades=[15, 1, 2], finish=0.1, body=0),
    # head, thorax and abdomen: painted with soft shading and no highlight; the navy contour is its darkest shade
    dict(name="insect body", shades=[1, 2, 3, 4], base=1, finish=0.2, body=0.05),
    # snout, hands and feet: the painted art puts a light patch on each
    dict(name="insect shell, hands and feet", shades=[1, 5, 6], base=1, finish=0.45, body=0),
    dict(name="butterfly wing", shades=[12, 13, 14], base=2, **WING),
    # the black margins and bands are drawn in one flat navy: no shades, so light only tints them
    dict(name="butterfly wing, black markings", shades=[], **WING),
    # the female's purple patches on the lower wings, with the navy as their shade
    dict(name="butterfly wing, female spots", shades=[1, 2], base=1, **WING),
    # the two fangs; the palette's first color is green, so the white's shade is the wings' pale lavender
    dict(name="claws and teeth", shades=[13, 14], base=1, finish=0.7, body=0.05),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[7, 8, 9, 10], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("insect body", [1, 2, 3, 4]), **to("insect shell, hands and feet", [5, 6]),
          **to("butterfly wing", [12, 13, 14]), **to("eye (line art)", [7, 8, 9, 10])}
WINGS = ["hane*", "*wings*"]
RULES = [
    # a wing is one flat sheet: its veins (and its soft upper edge) are lines on it, not creases between cells
    dict(drawings=WINGS, colors={1: "butterfly wing, black markings", **to(INNER, [2, 3, 4])}),
    dict(drawings=["*-female"], colors={2: "butterfly wing, female spots"}, thin_all={2: INNER}),
    dict(drawings=["kuti", "te0*", "asi0*", "*foot*"],
         colors={1: "insect shell, hands and feet", 2: "outline", 14: "claws and teeth"}),
    dict(drawings=["tuno0*", "parts0*"], colors={1: "outline", 2: "outline"}),
    # head and thorax are two balls in one drawing: the line where one overlaps the other is a crease
    dict(view="front", drawings=["atama"], rect=[6, 19, 1, 1], colors={1: "outline"}),
    dict(view="front", drawings=["atama"], rect=[12, 20, 2, 1], colors={1: "outline"}),
    dict(view="back", drawings=["head01"], rect=[9, 18, 6, 1], colors={1: "outline"}),
    dict(view="back", drawings=["head01"], rect=[8, 19, 1, 1], colors={1: "outline"}),
    dict(view="back", drawings=["head01"], rect=[15, 19, 2, 1], colors={1: "outline"}),
]
