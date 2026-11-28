SOURCE = "sources/black2-white2/0096-drowzee.spu"
MATERIALS = [
    # black, and the brown lines between the toes
    dict(name="outline", shades=[1, 3], finish=0.1, body=0),
    # the yellow upper half: plain bare skin, painted flat; its olive and dark brown contour are its darkest shades
    dict(name="hide", shades=[2, 6, 7, 8, 9, 10, 11], base=4, finish=0.25, body=0.08),
    # the brown lower half is the same skin in another color
    dict(name="hide, lower body", shades=[2, 3, 4, 5], base=1, finish=0.25, body=0.08),
    dict(name="hide, ear insides", shades=[2, 3, 4], base=1, finish=0.25, body=0.08),
    dict(name="mouth", shades=[13, 14], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[1, 12], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("hide, lower body", [2, 3, 4, 5]), **to("hide", [6, 7, 8, 9, 10, 11]),
          **to("mouth", [13, 14]), 12: "eye (line art)"}
RULES = [
    # the dark brown contour around the yellow chest and back belongs to the yellow
    dict(view="front", drawings=["karada"], rect=[0, 0, 36, 23], colors={2: "hide"}),
    dict(view="back", drawings=["body01"], rect=[0, 0, 40, 25], colors={2: "hide"}),
    # inside the ear
    dict(drawings=["atama", "head01"], colors=to("hide, ear insides", [2, 3, 4])),
    # the eye: white and pupil (the shut eye's black line stays line)
    dict(drawings=["atama-eyes-open", "head01-eyes-open"], colors={1: "eye (line art)"}),
    dict(view="back", drawings=["head01"], rect=[29, 15, 1, 1], colors={1: "eye (line art)"}),
    # lines between the yellow toes
    dict(view="front", drawings=["asi2"], rect=[11, 4, 1, 1], colors={3: "outline"}),
    dict(view="front", drawings=["asi4"], rect=[7, 3, 1, 1], colors={3: "outline"}),
    dict(view="front", drawings=["asi4"], rect=[6, 4, 1, 2], colors={3: "outline"}),
]
# the pale patch on the forehead and on each knee is a broad soft patch of shading, not a glint: left out of
# its row it stayed pale on a body gone dark and turned into a gray blotch under the studio lamp
KEEP_TOP = ["hide", "hide, lower body"]
