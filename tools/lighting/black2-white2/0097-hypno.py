SOURCE = "sources/black2-white2/0097-hypno.spu"
MATERIALS = [
    # black, and the brown line the head and shoulder draw across the top of the ruff
    dict(name="outline", shades=[1, 7], finish=0.1, body=0),
    # the yellow skin: plain bare skin, painted flat; its brown and olive contour colors are its darkest shades
    dict(name="hide", shades=[7, 2, 8, 9, 3, 4, 5, 6], base=4, finish=0.25, body=0.08),
    dict(name="hide, ear insides", shades=[8, 9], base=0, finish=0.25, body=0.08),
    # the white ruff around the neck (longer on the female); its slate contour is its darkest shade
    dict(name="fur", shades=[10, 11, 12, 13, 14], base=4, finish=-0.7, body=0.05),
    # the pendulum's ring: "it polishes the pendulum", and its glitter is what hypnotizes
    dict(name="metal", shades=[10, 11, 12, 13, 14], base=1, finish=0.9, body=-1),
    # the thread the ring hangs from
    dict(name="string", shades=[11, 12, 13, 14], base=2, finish=0.1, body=0.05),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # the thread tied across the ring: a line on it, not a crease
    dict(name="eye (line art)", shades=[1, 13, 14], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
GRAYS = [10, 11, 12, 13, 14]
COLORS = {1: "outline", **to("hide", [7, 2, 8, 9, 3, 4, 5, 6]), **to("fur", GRAYS)}
EAR = to("hide, ear insides", [8, 9])
STRING = to("string", [11, 12, 13, 14])
def rects(drawing, view, colors, *boxes):
    return [dict(view=view, drawings=[drawing], rect=list(b), colors=colors) for b in boxes]
RULES = [
    # the brown inside of the ear that faces the viewer
    *rects("atama", "front", EAR, [25, 7, 1, 2], [24, 9, 2, 2], [22, 11, 2, 1], [20, 12, 3, 1], [21, 13, 3, 1], [23, 14, 1, 1]),
    # the eyes: white, its pale blue shade and the pupil (the shut eye's black line stays line)
    dict(drawings=["atama-eyes-open"], colors=to("eye (line art)", [1, 13, 14])),
    # the ruff, front: the brown strokes along its top are drawn line
    dict(view="front", drawings=["kubige*"], colors={7: "outline"}),
    # the pendulum: a metal ring on a thread
    dict(drawings=["kane", "image-10"], colors=to("metal", GRAYS)),
    *rects("kane", "front", STRING, [9, 0, 1, 13]),
    *rects("kane", "back", STRING, [9, 4, 1, 13]),
    *rects("image-10", "front", STRING, [6, 1, 2, 5], [8, 6, 1, 1], [9, 7, 1, 1], [10, 8, 3, 1]),
    # the thread tied through the hole lies on the ring
    *rects("kane", "front", {1: INNER}, [9, 14, 1, 4]),
    *rects("kane", "back", {1: INNER}, [9, 18, 1, 4]),
    *rects("image-10", "front", {1: INNER}, [13, 9, 5, 3]),
]
# the pale patches on the forehead and nose are broad soft shading, not glints: left out of the row they
# turned into gray-olive blotches under the studio lamp and in the cave
KEEP_TOP = ["hide"]
