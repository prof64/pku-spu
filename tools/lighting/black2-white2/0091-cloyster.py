SOURCE = "sources/black2-white2/0091-cloyster.spu"
# Palette: 1 2 4 5 (and 3) the purple shell; 6 7 8 9 the head; 10 11 12 13 grays shared by the shell's inside,
# its pale lip, the horn, the teeth and the eyes; 14 black; 15 white (horn tip, teeth, eye whites).
# The unused first color is a blue, not a pale gray, so no white takes it as a shade.
SHELL = [5, 3, 4, 2, 1]
MATERIALS = [
    dict(name="outline", shades=[14, 5, 12], finish=0.1, body=0),
    dict(name="hard shell", shades=SHELL, base=2, finish=0.2, body=0),
    dict(name="hard shell, spikes", shades=SHELL, base=2, finish=0.2, body=0),
    dict(name="hard shell, inside", shades=[13, 12], base=1, finish=0.2, body=0),
    dict(name="hard shell, inner lip", shades=[13, 11, 10], base=1, finish=0.2, body=0),
    dict(name="pearl", shades=[9, 8, 7, 6], base=0, finish=0.9, body=0.1),
    dict(name="claw and tooth, horn", shades=[13, 11, 10, 15], base=1, finish=0.7, body=0.05),
    dict(name="claw and tooth, teeth", shades=[11, 10, 15], base=2, finish=0.7, body=0.05),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[12, 11, 10, 15], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {14: "outline", **to("hard shell", SHELL), **to("pearl", [9, 8, 7, 6]),
          **to("hard shell, inner lip", [11, 10]), **to("hard shell, inside", [13, 12])}
EYE = to("eye (line art)", [12, 11, 10, 15])
RULES = [
    dict(drawings=["toge-*"], colors=to("hard shell, spikes", SHELL)),
    dict(drawings=["tuno"], colors=to("claw and tooth, horn", [13, 11, 10, 15])),
    # the left valve's inside: its dark gray is the lip's own contour along the outer edge
    dict(drawings=["kai-l2"], colors={13: "hard shell, inner lip"}),
    # one gray pixel on the left valve's edge beside the horn tip: a softened outline
    dict(view="front", drawings=["kai-l"], rect=[18, 7, 1, 1], colors={12: "outline"}),
    # the head: teeth below, eyes above; one stray shell-dark pixel on its edge is outline
    # (the two dark grays at the grin's corner soften its black line: outline)
    dict(drawings=["body"], colors={**to("claw and tooth, teeth", [11, 10, 15]), 12: "outline", 5: "outline"}),
    dict(drawings=["body"], rect=[0, 8, 32, 7], colors=EYE),
    dict(drawings=["body"], rect=[0, 15, 10, 1], colors=EYE),
    dict(drawings=["body-eyes-open"], colors=EYE),
    # closed eyelids are lines drawn on the one sphere, not creases in it
    dict(drawings=["body-eyes-closed"], interior={14: ([9, 8, 7, 6], INNER)}),
]
# The valves' lightest purple is their pale lip band and the lit top of the back: a real shade of the shell.
# Left out of the row, the lips stay bright lines on a shell gone dark when the light is behind it.
KEEP_TOP = ["hard shell"]
