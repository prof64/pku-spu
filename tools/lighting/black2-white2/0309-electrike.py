SOURCE = "sources/black2-white2/0309-electrike.spu"
# Electrike: a green coat with yellow markings, an open mouth, small fangs, one eye. Nothing glows at rest
# (the sparks of the Pokédex entries come in dry air or before a storm, not as a standing light).
# The coat is fur by every entry ("long body hair", Ruby); the painted art draws it sleek, in flat soft
# shading with clean edges and no highlight, so it takes the sleek coat's dials (Short fur), not the fluffy one's.
FINISH, BODY = -0.2, 0.05
MATERIALS = [
    # black line, and the dark-green lines where one lobe of the head crest lies over the next
    dict(name="outline", shades=[11, 1], finish=0.1, body=0),
    # the green coat: its dark-green contour is its darkest shade. Most of it where it shows (the whole back
    # view, flanks, legs) is painted in 2; the head and shoulders seen from the front are a step lighter.
    dict(name="short fur", shades=[1, 2, 3, 4, 5], base=1, finish=FINISH, body=BODY),
    # the yellow of the snout, the crest's lightning mark, the back stripe, the tail tip, the leg bands
    dict(name="short fur, yellow markings", shades=[8, 7, 6], base=1, finish=FINISH, body=BODY),
    # the palette's own gray (drawn only in the eye) is the white fangs' shade
    dict(name="claws and teeth", shades=[14, 13], base=1, finish=0.7, body=0.05),
    dict(name="mouth", shades=[9, 10], base=0, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[11, 14, 13], finish=0.9, body=0),
]
# The palest green is few of the coat's pixels overall but a broad painted band along the head crest:
# a shade, not a glint. Left out of the row it stays pale on a crest that has gone dark (sun behind).
KEEP_TOP = ["short fur"]
def to(name, colors): return {c: name for c in colors}
COLORS = {11: "outline", **to("short fur", [1, 2, 3, 4, 5]), **to("short fur, yellow markings", [8, 7, 6]),
          13: "claws and teeth", 14: "eye (line art)", **to("mouth", [9, 10])}
EYE = to("eye (line art)", [11, 13, 14])
RULES = [
    # the eye: white, its gray shade, black pupil and rim
    dict(view="front", drawings=["head"], rect=[16, 13, 6, 3], colors=EYE),
    dict(view="front", drawings=["head-eyes-open"], rect=[0, 5, 6, 3], colors=EYE),
    # the upper crest lies over the lower lobe, the brow over the snout: those dark-green lines are creases
    dict(view="front", drawings=["head"], rect=[20, 7, 15, 6], colors={1: "outline"}),
    dict(view="front", drawings=["head"], rect=[14, 10, 3, 3], colors={1: "outline"}),
    dict(view="front", drawings=["head-eyes-*"], colors={1: "outline"}),
    dict(view="back", drawings=["head"], rect=[11, 7, 9, 3], colors={1: "outline"}),
]
