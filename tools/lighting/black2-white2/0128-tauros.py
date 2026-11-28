SOURCE = "sources/black2-white2/0128-tauros.spu"
# Tauros: a tan coat, a shaggy brown mane around the neck, gray horns and three gray studs on the forehead,
# a dark bare muzzle, gray hooves, and three thin dark tails each ending in a gray tuft. The painted art
# shades coat, mane, muzzle, tails and tufts flat and soft; only the horns and studs carry pale highlight
# streaks. The hooves are painted in two flat planes with no highlight.
# Colors: 1 black; 6-2 the coat (6 its dark contour, 2 the pale side of the face); 15-12 the mane's browns
# (15 also the tail cords, 14 and 13 the muzzle); 11-7 grays (horns, studs, hooves, tufts; 8 and 7 the eye).
SHORT = dict(finish=-0.2, body=0.05)
MATERIALS = [
    # black; the brow and lid lines of the eye, drawn in the coat's dark brown; two contour pixels drawn in
    # the mane's dark brown on the coat
    dict(name="outline", shades=[1, 6, 15], finish=0.1, body=0),
    # the tan coat: its dark brown contour and the lines of the legs are its darkest shade. Both views
    # together are mostly painted in 4
    dict(name="short fur", shades=[6, 5, 4, 3, 2], base=2, **SHORT),
    # the legs on the far side, each painted in one flat dark brown: the same coat in the body's shadow
    dict(name="short fur, far legs", shades=[6, 5], base=0, **SHORT),
    # the three thin tails: an even dark line in the art
    dict(name="short fur, tails", shades=[15, 14], base=0, **SHORT),
    # the mane: long shaggy fur over a broad area, so -0.1 (at -0.7 a mane turns grainy)
    dict(name="fur", shades=[15, 14, 13, 12], base=1, finish=-0.1, body=0.05),
    # the tufts at the tail tips: brushes of the same long fur (at -0.7 they speckled pale under the lamp)
    dict(name="fur, tail tufts", shades=[11, 10, 9], base=2, finish=-0.1, body=0.05),
    # the bare dark muzzle: painted flat
    dict(name="hide, muzzle", shades=[14, 13], base=0, finish=0.25, body=0.08),
    # horns, their base rings and the three forehead studs: the art paints pale highlight streaks on each.
    # The one white pixel on a stud is a painted glint (with white in the row a lit horn went pure white)
    dict(name="claw and tooth, horns", shades=[11, 10, 9, 8], base=2, finish=0.7, body=0.05),
    # hooves: hard horn, painted in flat planes with no highlight (so less sheen than Ponyta's)
    dict(name="hooves", shades=[11, 10], base=0, finish=0.4, body=0),
    dict(name="eye (line art)", shades=[1, 8, 7], finish=0.9, body=0),
]
# the palest tan is few of the coat's pixels overall but the whole lit side of the face: a shade, not a glint
KEEP_TOP = ["short fur"]
def to(name, colors): return {c: name for c in colors}
HORN, EYE, FAR, LINE = "claw and tooth, horns", "eye (line art)", "short fur, far legs", "outline"
COLORS = {1: LINE, **to("short fur", [6, 5, 4, 3, 2]), **to("fur", [15, 14, 13, 12]), **to(HORN, [11, 10, 9, 8, 7])}
RULES = [
    # tails: thin cords and their tufts
    dict(drawings=["o0*", "tail-*"], colors={**to("fur, tail tufts", [11, 10, 9]), **to("short fur, tails", [15, 14])}),
    # hooves
    dict(drawings=["usiroasi-b", "asi02-b", "asi", "foot-*"], colors=to("hooves", [11, 10])),
    # the muzzle
    dict(drawings=["atama", "head"], colors=to("hide, muzzle", [14, 13])),
    # far legs. Front: the far foreleg, and the far hind leg drawn under the belly
    dict(view="front", drawings=["asi03"], colors={5: FAR}),
    dict(view="front", drawings=["usiroasi-a"], rect=[8, 21, 9, 11], colors={6: FAR}),
    dict(view="front", drawings=["usiroasi-b"], rect=[8, 0, 5, 2], colors={6: FAR}),
    # back: the far foreleg
    dict(view="back", drawings=["leg-fl", "foot-fl"], colors={6: FAR}),
    # contour pixels drawn in the mane's dark brown on the coat
    dict(view="back", drawings=["foot-fr*", "body"], colors={15: LINE}),
    # the eye: white, its gray shade, the pupil; the brow and lid lines
    dict(view="front", drawings=["atama"], rect=[15, 12, 4, 4], colors={6: LINE}),
    dict(view="front", drawings=["atama"], rect=[16, 12, 3, 4], colors=to(EYE, [1, 8, 7])),
    dict(view="front", drawings=["atama-eyes-*"], rect=[6, 2, 4, 4], colors={6: LINE}),
    dict(view="front", drawings=["atama-eyes-open"], rect=[7, 2, 3, 4], colors=to(EYE, [1, 8, 7])),
]
