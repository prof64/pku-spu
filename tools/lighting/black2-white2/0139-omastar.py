SOURCE = "sources/black2-white2/0139-omastar.spu"
# Palette: 1 black; 2 3 4 5 the blue body and tentacles, light to dark; 6 8 9 10 11 the shell, cream to dark brown
# (the beak, the eyelids and the eyes' shading too); 7 the eyes' yellow; 12 white (catchlights);
# 13 a dark gray that softens the black line. The unused first color is magenta, so nothing takes it as a shade.
SHELL = [11, 10, 9, 8, 6]
SPIKE = [11, 10, 9, 8]
SKIN = [5, 4, 3, 2]
LID = [11, 10, 9, 8, 7]
MATERIALS = [
    # black line; a dark gray softens it beside one tentacle, the shell's edge and the back view's eye
    dict(name="outline", shades=[1, 13], finish=0.1, body=0),
    # the spiral shell: "its heavy shell", "its spiral shell grew too large". Omanyte's, Cloyster's and Shellder's row.
    # The art paints it flat cream-gray with soft shading and no highlight: dull.
    # Base is the tan (10) most of both views is painted in; the back view is nearly all of it.
    dict(name="hard shell", shades=SHELL, base=1, finish=0.2, body=0),
    # the spikes on the shell (four in front, six behind): the same shell, as Cloyster's spikes
    dict(name="hard shell, spikes", shades=SPIKE, base=2, finish=0.2, body=0),
    # the soft body and tentacles: painted blue with broad soft lighter patches and no small highlight. Plain bare
    # skin, as Omanyte's. The front view is painted in the two light blues (2, 3) and the back view in the dark
    # one (4), so the base is the middle one (3): neither view falls off the end of its shades.
    dict(name="hide", shades=SKIN, base=2, finish=0.25, body=0.08),
    # the eyelids (painted in the shell's tans in front, in the eye's yellow behind) and the rim under each eye
    dict(name="hide, eyelids", shades=LID, base=3, finish=0.25, body=0.08),
    # "Sharp beaks ring its mouth": four cream plates around the black cross of the mouth. The art paints them
    # cream with soft shading and no highlight, like a bird's beak, so Beak, not Claw and tooth.
    dict(name="beak", shades=SHELL, base=4, finish=0.4, body=0.05),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[1, 11, 10, 9, 8, 7, 12], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
def runs(view, drawing, spans, colors):
    return [dict(view=view, drawings=[drawing], rect=[a, y, b - a + 1, 1], colors=colors) for y, (a, b) in spans.items()]
COLORS = {1: "outline", 13: "outline", **to("hard shell", SHELL), **to("hide", SKIN)}
EYE = to("eye (line art)", [1, 11, 10, 9, 8, 7, 12])
LIDS = to("hide, eyelids", LID)
SPIKES = {**to("hard shell, spikes", SPIKE), 1: "outline"}
RULES = [
    # the spiral and the rib lines drawn in black are lines on the one dome, not creases
    dict(drawings=["atama", "kai"], interior={1: (SHELL, INNER)}),
    # the spikes, row by row (first to last column); the black around a spike is where it overlaps the shell: a crease.
    # Front: the two on top, the one in the middle, the one above the eye.
    *runs("front", "atama", {3: (16, 17), 4: (16, 18), 5: (16, 19), 6: (16, 20), 7: (16, 21), 8: (16, 20), 9: (17, 18)}, SPIKES),
    *runs("front", "atama", {2: (25, 25), 3: (24, 26), 4: (23, 26), 5: (22, 27), 6: (21, 27)}, SPIKES),
    *runs("front", "atama", {10: (11, 12), 11: (11, 14), 12: (11, 15), 13: (11, 16), 14: (12, 17), 15: (12, 17), 16: (12, 16), 17: (13, 15)}, SPIKES),
    *runs("front", "atama", {21: (9, 11), 22: (9, 13), 23: (10, 14), 24: (10, 15), 25: (11, 15), 26: (11, 15), 27: (12, 14)}, SPIKES),
    # Back: the two on top, the left one, and three along the right edge.
    *runs("back", "kai", {1: (17, 17), 2: (16, 18), 3: (16, 18), 4: (16, 19), 5: (15, 19), 6: (15, 20), 7: (15, 20), 8: (16, 19)}, SPIKES),
    *runs("back", "kai", {2: (29, 30), 3: (28, 30), 4: (27, 30), 5: (26, 30), 6: (26, 29), 7: (26, 29)}, SPIKES),
    *runs("back", "kai", {7: (8, 9), 8: (8, 11), 9: (8, 12), 10: (8, 12), 11: (8, 12), 12: (8, 12), 13: (9, 11)}, SPIKES),
    *runs("back", "kai", {12: (32, 37), 13: (32, 37), 14: (32, 36), 15: (33, 35)}, SPIKES),
    *runs("back", "kai", {22: (36, 38), 23: (34, 38), 24: (35, 37)}, SPIKES),
    *runs("back", "kai", {26: (36, 36), 27: (36, 37), 28: (34, 37), 29: (35, 37), 30: (35, 36)}, SPIKES),
    dict(drawings=["kutit01*"], colors=to("beak", SHELL)),
    # Eyes: the yellow ball with its shading, slit pupil, catchlight and dark rim (five rows), in the eye drawing and
    # under it on the head; the row of tan below each is the lower lid. Shut, the whole ball is lid.
    dict(drawings=["atama-eyes-open"], rect=[9, 5, 6, 5], colors=EYE),
    dict(drawings=["atama-eyes-open"], rect=[20, 5, 6, 5], colors=EYE),
    dict(drawings=["atama-eyes-*"], rect=[10, 10, 4, 1], colors=LIDS),
    dict(drawings=["atama-eyes-*"], rect=[21, 10, 4, 1], colors=LIDS),
    dict(drawings=["atama-eyes-closed"], rect=[9, 5, 6, 5], colors=LIDS),
    dict(drawings=["atama-eyes-closed"], rect=[20, 5, 6, 5], colors=LIDS),
    dict(drawings=["atama"], rect=[5, 29, 6, 5], colors=EYE),
    dict(drawings=["atama"], rect=[16, 29, 6, 5], colors=EYE),
    dict(drawings=["atama"], rect=[6, 34, 4, 1], colors=LIDS),
    dict(drawings=["atama"], rect=[17, 34, 4, 1], colors=LIDS),
    # from behind one eye shows at the shell's edge
    dict(drawings=["me", "me-eyes-open"], colors={7: "eye (line art)", 1: "eye (line art)"}),
    dict(drawings=["me-eyes-closed"], colors={**LIDS, 1: "eye (line art)"}),
]
# The shell's cream (6) is the lit front band of the shell, front view only: a real shade (as on Cloyster and Omanyte).
KEEP_TOP = ["hard shell"]
