SOURCE = "sources/black2-white2/0123-scyther.spu"
GREEN = [14, 13, 12, 11]
GRAY = [4, 3, 2, 1]
MATERIALS = [
    dict(name="outline", shades=[15, 14], finish=0.1, body=0),
    # head, thorax, abdomen, limbs, the back edge of each scythe and the leading edge of each wing: one hard
    # green shell; the dark green contour is its darkest shade
    dict(name="insect shell", shades=GREEN, base=1, finish=0.45, body=0),
    # the cream neck, hip and knee joints: soft skin between the plates, painted flat
    dict(name="insect body, joints", shades=[6, 5], base=1, finish=0.2, body=0.05),
    # the same dials as Beedrill's wings
    dict(name="insect wing", shades=[10, 8, 7], base=1, finish=0.4, body=0.3),
    # the blades: white with gray streaks, the dark gray along the cutting edge is their darkest shade
    dict(name="claws and teeth, scythes", shades=GRAY, base=2, finish=0.7, body=0.05),
    dict(name="claws and teeth", shades=GRAY, base=2, finish=0.7, body=0.05),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # wing veins: lines inside one sheet, never a crease
    dict(name="eye (line art)", shades=[15, 3, 2, 1], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
EYE = to("eye (line art)", [1, 2, 3])
COLORS = {15: "outline", **to("insect shell", GREEN), **to("insect body, joints", [6, 5]),
          **to("insect wing", [10, 8, 7]), **to("claws and teeth, scythes", GRAY)}
RULES = [
    # wings: the olive veins are lines inside one flat sheet (the black lines part one wing from the next: creases)
    dict(drawings=["hane*", "*-wings01"], interior={10: ([7, 8], INNER)}),
    # the abdomen's segments, the head's crests and jaw, the thigh's spur: the dark lines between them are creases
    dict(drawings=["karada2*", "body02*", "head01", "l-leg01"], interior={14: ([13, 12, 11], "outline")}),
    # toes
    dict(drawings=["asi01", "asi02", "r-foot01"], colors=to("claws and teeth", GRAY)),
    # one pale pixel at the corner of the jaw, seen from behind
    dict(view="back", drawings=["head01"], colors={2: "claws and teeth"}),
    # front eye: white, the black pupil, and the dark lid line above it; the mouth line
    dict(view="front", drawings=["atama"], rect=[9, 12, 4, 4], colors={**EYE, 15: "eye (line art)", 14: "outline"}),
    dict(view="front", drawings=["atama"], rect=[11, 16, 2, 2], colors={14: "outline"}),
    dict(drawings=["atama-eyes-open"], rect=[7, 2, 4, 4], colors={**EYE, 15: "eye (line art)", 14: "outline"}),
    dict(drawings=["atama-eyes-closed"], rect=[7, 2, 5, 4], colors={14: "outline"}),
    # back eye: a pale sliver at the side of the head, and its dark rim
    dict(drawings=["head01-eyes-open"], colors=EYE),
    dict(drawings=["head01-eyes-open"], rect=[2, 2, 1, 1], colors={14: "outline"}),
    dict(drawings=["head01-eyes-open"], rect=[3, 3, 1, 2], colors={14: "outline"}),
    dict(drawings=["head01-eyes-open"], rect=[4, 5, 1, 1], colors={14: "outline"}),
    # the far scythe's cutting edge is drawn in dark green: a line on the blade, not shell
    dict(view="front", drawings=["te02"], rect=[17, 9, 6, 5], colors={14: "outline"}),
    dict(view="front", drawings=["te02"], rect=[14, 14, 3, 3], colors={14: "outline"}),
]
# the pale green is the broad lit side of the head, shoulders and thighs (about 6% of the shell): left out of
# the row it stays pale on a body gone dark with the sun behind
KEEP_TOP = ["insect shell"]
