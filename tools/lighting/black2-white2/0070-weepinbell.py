SOURCE = "sources/black2-white2/0070-weepinbell.spu"
# Weepinbell is a plant all over: a hollow bell of a body, two leaves and a brown hook. The official art
# paints every part flat and soft; nothing on it has a highlight but the eyes.
# The bell: thick plant flesh, matte, a little light through. Like Sunkern's seed and Cacturne's trunk it is
# denser than a bud: at the bud's 0.25 the yellow went orange with the sun behind it and stayed bright in the cave.
BODY = dict(finish=0.1, body=0.15)
MATERIALS = [
    # black; and the browns where they draw the body's contour on its lit side, the ring under the hook
    # and the line around each eye's socket. They are the hook's colors: as the yellow's darkest shades
    # they turn the body tan in a field (Bellsprout's head did)
    dict(name="outline", shades=[1, 3, 4], finish=0.1, body=0),
    dict(name="plant body", shades=[5, 6, 7], base=0, **BODY),
    # the olive spots on the forehead: pigment in the body, painted in the leaves' greens
    dict(name="plant body, spots", shades=[13, 14], base=0, **BODY),
    # the pink lips: color in the same body
    dict(name="plant body, lips", shades=[8, 9, 10, 11], base=2, **BODY),
    dict(name="leaf", shades=[12, 13, 14, 15], base=1, finish=0.15, body=0.35),
    # the brown hook on its rear end: dry and matte, like a trunk
    dict(name="hook", shades=[3, 4], base=0, finish=-0.45, body=0.05),
    # the lit wall inside the open mouth
    dict(name="mouth", shades=[8, 9], base=1, finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # the shut eyes' lines: tinted, never a crease
    # white, black pupil, the brown ring around each eye and the brown glint lines in the pupil
    dict(name="eye (line art)", shades=[1, 2, 3, 4], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", 2: "eye (line art)", **to("hook", [3, 4]), **to("plant body", [5, 6, 7]),
          **to("plant body, lips", [8, 9, 10, 11]), **to("leaf", [12, 13, 14, 15])}
EYE = to("eye (line art)", [1, 2, 3, 4])
RULES = [
    # the body: brown there is line, green is a spot
    dict(drawings=["head*", "body*"], colors={**to("outline", [3, 4]), **to("plant body, spots", [13, 14])}),
    # the eyes, drawn on the head and again on the eye drawing (two pixels further right)
    dict(view="front", drawings=["head"], rect=[4, 5, 5, 7], colors=EYE),
    dict(view="front", drawings=["head"], rect=[13, 6, 8, 8], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[6, 5, 5, 7], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[15, 6, 8, 8], colors=EYE),
    # shut eyes: lines drawn on the one body
    dict(drawings=["head-eyes-closed"], rect=[6, 9, 5, 3], colors={3: INNER, 4: INNER}),
    dict(drawings=["head-eyes-closed"], rect=[15, 10, 7, 4], colors={1: INNER, 3: INNER, 4: INNER}),
    dict(view="front", drawings=["mouse"], colors={3: "outline"}),     # one brown pixel where the lip meets the eye's ring
    # the dark edge of the wall inside the mouth
    dict(view="front", drawings=["mouse"], rect=[11, 12, 4, 7], colors={8: "mouth"}),
]
FLOODS = [
    # inside the ring of the lips: the red wall of the mouth (the lips' upper contour is the same red)
    dict(view="front", drawing="mouse", seeds=[[12, 11]], through=[9], colors={9: "mouth"}),
]
