SOURCE = "sources/black2-white2/0071-victreebel.spu"
# Victreebel is a plant all over: a bell of a body with its mouth on top, three leaves and a long brown vine.
# The official art paints every part flat and soft; only the eyes and the two fangs are white.
# The bell: thick plant flesh, matte, a little light through (the dials of Weepinbell's body, Sunkern's seed
# and Cacturne's trunk)
BODY = dict(finish=0.1, body=0.15)
MATERIALS = [
    # black; and the browns where they draw the body's contour on its lit side and the yellow vine tip's.
    # They are the vine's colors: as the yellow's darkest shades they turn the body tan (Bellsprout's head did)
    dict(name="outline", shades=[1, 4, 5], finish=0.1, body=0),
    # the yellow bell, and the yellow tip of the vine
    dict(name="plant body", shades=[6, 7, 8], base=0, **BODY),
    # the green spots: pigment in the body, painted in the leaves' greens (the lighter one where the body is lit)
    dict(name="plant body, spots", shades=[13, 14], base=0, **BODY),
    # the red lips around the mouth, and their outer side seen from behind: color in the same body
    dict(name="plant body, lips", shades=[9, 10, 11], base=1, **BODY),
    dict(name="leaf", shades=[12, 13, 14, 15], base=1, finish=0.15, body=0.35),
    # the long brown vine from its head: dry and matte, like a trunk
    dict(name="vine", shades=[4, 5], base=0, finish=-0.45, body=0.05),
    # the two fangs: white and its gray
    dict(name="claws and teeth", shades=[2, 3], base=0, finish=0.7, body=0.05),
    # what shows inside the open mouth, where the fluid pools
    dict(name="mouth", shades=[4], base=0, finish=0.8, body=0),
    # leaf midribs, the shadow line under the lip, the shut eyes' lines: tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    # white and its gray, the black pupil, the brown lid lines
    dict(name="eye (line art)", shades=[1, 2, 3, 4, 5], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("vine", [4, 5]), **to("plant body", [6, 7, 8]), **to("plant body, lips", [9, 10, 11]),
          **to("leaf", [12, 13, 14, 15]), **to("claws and teeth", [2, 3])}
EYE = to("eye (line art)", [1, 2, 3, 4, 5])
RULES = [
    # the body: brown there is line, green is a spot
    dict(drawings=["head*", "body"], colors={**to("outline", [4, 5]), **to("plant body, spots", [13, 14])}),
    # the eyes sit just under the lip. On the head itself they are always covered by the eye drawing
    dict(view="front", drawings=["head"], colors=to("eye (line art)", [2, 3])),
    dict(drawings=["head-eyes-open"], rect=[2, 2, 4, 5], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[9, 2, 7, 6], colors=EYE),
    # the shadow line under the lip between the eyes, and the lines of the shut eyes: drawn on the one body
    dict(drawings=["head-eyes-open"], rect=[6, 3, 3, 2], colors={4: INNER}),
    dict(drawings=["head-eyes-closed"], rect=[2, 3, 14, 5], colors={4: INNER, 5: INNER}),
    # inside the mouth
    dict(drawings=["mouse"], colors={4: "mouth"}),
    # the vine's yellow tip: brown around it is its contour, not vine
    dict(view="front", drawings=["tuta2"], rect=[8, 13, 16, 3], colors=to("outline", [4, 5])),
    dict(view="front", drawings=["tuta2"], rect=[5, 16, 19, 8], colors=to("outline", [4, 5])),
    dict(drawings=["mi"], colors=to("outline", [4, 5])),
    dict(drawings=["mi"], rect=[4, 6, 2, 1], colors={4: "vine"}),
    # midribs drawn inside a leaf
    dict(view="front", drawings=["hand-l", "hand-r"], interior={12: ([13, 14, 15], INNER)}),
    dict(view="back", drawings=["leaf-l"], interior={1: ([12, 13], INNER)}),
]
