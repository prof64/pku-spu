# Mew: a coat of short, fine hair all over (Short fur), tail included; bare pads under the hind feet.
SOURCE = "sources/black2-white2/0151-mew.spu"
MATERIALS = [
    # black line, and the shut eye's line (drawn in the coat's darkest color)
    dict(name="outline", shades=[1, 6], finish=0.1, body=0),
    # the pink coat: its dark plum contour (6) is its darkest shade
    dict(name="short fur", shades=[6, 5, 4, 3, 2], base=2, finish=-0.2, body=0.05),
    # the oval pad under each hind foot (back view), painted in one color
    dict(name="hide, paw pads", shades=[13], base=0, finish=0.25, body=0.08),
    dict(name="eye (line art)", shades=[6, 11, 10, 9, 8, 7], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("short fur", [2, 3, 4, 5, 6]), 13: "hide, paw pads"}
RULES = [
    # the eye: white, blues, gray, and the dark rim at its inner edge
    dict(drawings=["head-eyes-open"], colors=to("eye (line art)", [7, 8, 9, 10, 11])),
    dict(drawings=["head-eyes-open"], rect=[3, 4, 1, 3], colors={6: "eye (line art)"}),
    # the shut eye is a drawn line
    dict(drawings=["head-eyes-closed"], rect=[4, 6, 3, 1], colors={6: "outline"}),
]
# the palest pink (forehead, tail tip) is few pixels; left out of the row it turned to gray blotches under the
# studio lamp and stayed pale on a body gone dark with the sun behind, so it stays in
KEEP_TOP = ["short fur"]
