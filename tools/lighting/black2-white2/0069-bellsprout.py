SOURCE = "sources/black2-white2/0069-bellsprout.spu"
# Bellsprout is a plant all over: a bud for a head, two leaves, a thin stem and root feet. The official
# art paints every part flat and soft; the only hard highlights are the catchlights of the eyes.
BUD = dict(finish=0.1, body=0.25)       # Bud and bulb: the head ("Its bud looks like a human face")
MATERIALS = [
    # black; and the browns where they draw the bud's contour on its lit side. They are the stem's colors:
    # as the yellow's darkest shades they turned the whole head tan in a field
    dict(name="outline", shades=[1, 2, 3, 4], finish=0.1, body=0),
    # the yellow bud; the white patch on top is a painted glint (the tool leaves it as painted)
    dict(name="bud", shades=[13, 14, 15], base=0, **BUD),
    # the pink lips around the mouth: color in the same bud
    dict(name="bud, lips", shades=[5, 6, 7, 8], base=1, **BUD),
    dict(name="leaf", shades=[9, 10, 11, 12], base=1, finish=0.15, body=0.35),
    # the brown stem and the root feet: dry and matte, like a trunk
    dict(name="stem and roots", shades=[2, 3, 4], base=0, finish=-0.45, body=0.05),
    # the dark red seen inside the ring of the lips
    dict(name="mouth", shades=[5], base=0, finish=0.8, body=0),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # leaf midribs, shut eyes: tinted, never a crease
    # black bead eyes, their white catchlight and the brown pixel under each
    dict(name="eye (line art)", shades=[1, 2, 3, 15], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("stem and roots", [2, 3, 4]), **to("bud", [13, 14, 15]), **to("bud, lips", [5, 6, 7, 8]),
          **to("leaf", [9, 10, 11, 12])}
EYE = to("eye (line art)", [1, 2, 3, 15])
LID = {2: INNER, 4: INNER}
RULES = [
    # the head: brown there is the line around the bud, not stem
    dict(drawings=["head", "head01", "head-eyes-*"], colors=to("outline", [2, 3, 4])),
    # the eyes (front only): a black bead with a catchlight; shut, a short brown line on the bud
    dict(drawings=["head-eyes-open"], rect=[5, 2, 2, 2], colors=EYE),
    dict(drawings=["head-eyes-open"], rect=[12, 3, 2, 2], colors=EYE),
    dict(drawings=["head-eyes-closed"], rect=[5, 3, 2, 1], colors=LID),
    dict(drawings=["head-eyes-closed"], rect=[12, 3, 3, 2], colors=LID),
    # inside the ring of the lips
    dict(view="front", drawings=["mouse"], rect=[6, 6, 2, 2], colors={5: "mouth"}),
    dict(view="front", drawings=["mouse"], rect=[7, 8, 1, 1], colors={5: "mouth"}),
    dict(view="front", drawings=["mouse"], rect=[8, 9, 1, 1], colors={5: "mouth"}),
    # the midrib drawn inside each leaf
    dict(drawings=["hand-*", "*-arm01"], interior={9: ([10, 11, 12], INNER)}),
]
