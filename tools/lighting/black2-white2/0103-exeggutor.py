SOURCE = "sources/black2-white2/0103-exeggutor.spu"
# A walking palm. FireRed: "Each of the nuts has a face and a will of its own." Crystal: "A head that drops off
# becomes an EXEGGCUTE", so a head is the same durable shell as an Exeggcute egg: dull, hard, solid.
# The painted art shades heads, trunk and fronds flat and soft; its only hard highlights are on the claws.
MATERIALS = [
    dict(name="outline", shades=[15], finish=0.1, body=0),
    # the three heads; their brown contours (lighter on the lit side, darker in shade) are the shell's dark shades
    dict(name="shell", shades=[5, 4, 3, 2, 1], base=2, finish=0.2, body=0),
    # the ringed trunk, legs and feet: bark, as Venusaur's trunk, but it is the whole body here and at Bark's
    # -0.45 it went grainy under a lamp; -0.1 keeps it dry and smooth, as the art paints it
    dict(name="trunk", shades=[8, 7, 6], base=1, finish=-0.1, body=0.05),
    dict(name="leaves", shades=[12, 11, 10], base=1, finish=0.15, body=0.35),
    dict(name="claws and teeth", shades=[14, 13], base=1, finish=0.7, body=0.05),
    # open mouths, painted in the heads' browns (the palette has no pink)
    dict(name="mouth", shades=[5, 4], base=0, finish=0.8, body=0),
    # eyelids, cheek and mouth lines, closed eyes: drawn inside a head, tinted, never a crease
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),
    dict(name="eye (line art)", shades=[15, 13], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("shell", [1, 2, 3, 4, 5]), **to("trunk", [6, 7, 8]), **to("leaves", [10, 11, 12]),
          **to("claws and teeth", [13, 14])}
EYE = {13: "eye (line art)", 15: "eye (line art)"}
MOUTH = to("mouth", [4, 5])
HEADS = ["head0*", "kao*"]
def eyes(drawing, *rects): return [dict(drawings=[drawing], rect=list(r), colors=EYE) for r in rects]
RULES = [
    # brown wholly inside a head (next to head, eye, tooth or black only) is a face line, not the contour
    dict(drawings=HEADS, interior={4: ([1, 2, 3, 5, 13, 15], INNER), 5: ([1, 2, 3, 4, 13, 15], INNER)}),
    # mouth interiors
    dict(drawings=["head01"], rect=[14, 15, 7, 1], colors=MOUTH),
    dict(drawings=["head01-eyes-*"], rect=[6, 7, 7, 1], colors=MOUTH),
    dict(drawings=["head02"], rect=[19, 14, 7, 3], colors=MOUTH),
    dict(drawings=["kao2"], rect=[14, 13, 3, 4], colors=MOUTH),
    # eyes: the white and the black pupil; every other white in a head drawing is a tooth
    *eyes("head01", [18, 10, 5, 3], [12, 11, 2, 2]), *eyes("head01-eyes-open", [10, 2, 5, 3], [4, 3, 2, 2]),
    *eyes("head02", [24, 8, 2, 2], [15, 10, 4, 2]), *eyes("head02-eyes-open", [13, 2, 2, 2], [4, 4, 4, 2]),
    *eyes("head03", [7, 8, 3, 2]), *eyes("head03-eyes-open", [2, 2, 3, 2]),
    *eyes("kao2", [11, 8, 5, 2]), *eyes("kao2-eyes-open", [1, 4, 5, 2]),
    # closed eyes drawn as black lines on the head
    dict(drawings=["head01-eyes-closed"], rect=[3, 3, 13, 3], colors={15: INNER}),
]
