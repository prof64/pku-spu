# Mewtwo: plain bare skin (Hide) everywhere. The purple belly and tail are the same skin in another color.
# Nothing on it is hard, wet or glowing; the art paints it with flat soft shading.
SOURCE = "sources/black2-white2/0150-mewtwo.spu"
H = dict(finish=0.25, body=0.08)          # Hide: plain bare skin
MATERIALS = [
    # black line, and the shut eye's line (drawn in the skin's darkest color)
    dict(name="outline", shades=[1, 6], finish=0.1, body=0),
    # the gray skin: its dark contour and muscle lines (6) are its darkest shade
    dict(name="hide", shades=[6, 5, 4, 3, 2], base=2, **H),
    dict(name="hide, belly and tail", shades=[12, 11, 10, 9], base=1, **H),
    dict(name="eye (line art)", shades=[6, 10, 7], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("hide", [2, 3, 4, 5, 6]), **to("hide, belly and tail", [9, 10, 11, 12])}
EYE = to("eye (line art)", [7, 10])
RULES = [
    # the eye: white, purple iris; in front its dark upper lid line too
    dict(view="back", drawings=["head01"], colors=EYE),
    dict(drawings=["head01-eyes-open"], colors=EYE),
    dict(view="front", drawings=["head01-eyes-open"], rect=[2, 2, 2, 3], colors={6: "eye (line art)"}),
    # the shut eye is a drawn line
    dict(view="front", drawings=["head01-eyes-closed"], rect=[1, 4, 5, 3], colors={6: "outline"}),
    dict(view="back", drawings=["head01-eyes-closed"], rect=[2, 4, 1, 1], colors={6: "outline"}),
]
# the palest gray (forehead, thigh) and the belly's bright patch are few pixels; left out of their rows they
# stayed pale on a body gone dark with the sun behind, so both stay in
KEEP_TOP = ["hide", "hide, belly and tail"]
