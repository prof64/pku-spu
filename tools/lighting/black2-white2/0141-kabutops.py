SOURCE = "sources/black2-white2/0141-kabutops.spu"
# Palette: 1 black; 2 3 4 5 6 the brown shell, light to dark; 7 8 9 white to warm gray: the scythes, the foot
# claws, the eye, and (9 and 7 only) the gray chest and abdomen; 10 slate: the blades' and claws' contour on
# their lit side, the line along each blade, the pupil; 11 a dark gray-brown that softens the black line.
# The unused first color is not needed: every white here has its own grays.
SHELL = [6, 5, 4, 3, 2]
PALE = [9, 8, 7]
MATERIALS = [
    # black; the gray-brown that softens it; on the chest, the dark brown lines between its plates; and the
    # slate contour of the blades and claws. The palette has no step between the pale gray and that slate, so
    # as the blades' darkest shade it turned a whole blade slate blue in the field; as line it stays a contour.
    dict(name="outline", shades=[1, 11, 6, 10], finish=0.1, body=0),
    # head shield, thorax, arms, legs, back spines and tail: one armor. The art paints it flat brown with soft
    # streaky paler washes and no highlight: dull. Kabuto's row.
    dict(name="hard shell", shades=SHELL, base=2, finish=0.2, body=0),
    # the light gray chest and abdomen: the same armor, pale. Kingler's row.
    dict(name="hard shell, underside", shades=[9, 7], base=0, finish=0.2, body=0),
    # the blades and the gray forearms that carry them. Scyther's row.
    dict(name="claws and teeth, scythes", shades=PALE, base=0, finish=0.7, body=0.05),
    dict(name="claws and teeth", shades=PALE, base=1, finish=0.7, body=0.05),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # the line along each blade: tinted, never a crease
    dict(name="eye (line art)", shades=[10, 8, 7], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", 11: "outline", 10: "outline", **to("hard shell", SHELL), **to("claws and teeth, scythes", PALE)}
RULES = [
    # each blade has a slate line drawn along it, between the flat and its edge: a line on the one blade
    dict(drawings=["kama", "kama2", "l-hand01", "r-hand01"], interior={10: (PALE, INNER)}),
    # chest and abdomen: its plates are parted by dark brown lines (creases)
    dict(drawings=["karada"], colors={**to("hard shell, underside", [9, 7]), 6: "outline"}),
    # feet: the two claws of each
    dict(drawings=["asi", "asi2", "r-foot01"], colors=to("claws and teeth", PALE)),
    # the eye: white, its slate pupil, the pale lower edge
    dict(view="front", drawings=["atama"], rect=[16, 21, 3, 3], colors=to("eye (line art)", [10, 8, 7])),
    dict(drawings=["atama-eyes-open"], rect=[3, 3, 3, 3], colors=to("eye (line art)", [10, 8, 7])),
]
KEEP_TOP = ["hard shell"]
