SOURCE = "sources/black2-white2/0048-venonat.spu"
MATERIALS = [
    # black, and the dark purple lines where one tuft of fur lies over another
    dict(name="outline", shades=[15, 14, 13], finish=0.1, body=0),
    # "a coat of thin, stiff hair that covers its entire body": shaggy in the art, no highlight anywhere.
    # The navy contour is its darkest shade; base is the purple most of both views is painted in
    dict(name="fur", shades=[14, 13, 12, 11], base=1, finish=-0.7, body=0.05),
    # white stalks with a club at the tip: the art paints them flat white with a soft gray shade, so matte
    dict(name="insect body, antennae", shades=[3, 2, 1], base=1, finish=0.2, body=0.05),
    # tan hands and feet: flat soft shading in the art, no light patch (unlike Butterfree's), so matte
    dict(name="insect body, hands and feet", shades=[10, 9, 8], base=1, finish=0.2, body=0.05),
    # the pink mouth between the fangs
    dict(name="mouth", shades=[6, 5, 4], base=1, finish=0.8, body=0),
    dict(name="claws and teeth", shades=[2, 1], base=1, finish=0.7, body=0.05),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # the line between two toes: tinted, never a crease
    # the compound eyes, whole: red, pink facets, dark red rim
    dict(name="eye (line art)", shades=[7, 6, 5, 4], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("fur", [14, 13, 12, 11]), **to("insect body, antennae", [3, 2, 1]),
          **to("insect body, hands and feet", [10, 9, 8]), **to("eye (line art)", [7, 6, 5, 4])}
def px(view, drawing, x, y, colors, w=1, h=1): return dict(view=view, drawings=[drawing], rect=[x, y, w, h], colors=colors)
RULES = [
    dict(drawings=["mouse"], colors={**to("mouth", [6, 5, 4]), **to("claws and teeth", [2, 1])}),
    # one tuft over another, a tuft over the body: those lines are creases
    px("front", "hear", 7, 9, {13: "outline"}, h=2),
    px("back", "parts01", 8, 11, {13: "outline"}, h=2),
    px("back", "parts01", 13, 13, {14: "outline"}, h=3),
    px("back", "parts01", 12, 16, {14: "outline"}, h=2),
    px("back", "body01", 31, 6, {14: "outline"}),
    # the line between two toes
    px("front", "foot-l", 4, 11, {10: INNER}),
    px("front", "foot-l", 3, 12, {10: INNER}, h=2),
    px("front", "foot-r", 8, 11, {10: INNER}),
    px("front", "foot-r", 9, 12, {10: INNER}, h=2),
]
