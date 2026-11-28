SOURCE = "sources/black2-white2/0098-krabby.spu"
# Palette: 11 12 13 14 the orange shell (14 its dark contour); 4 5 6 7 8 the cream underside, arms and legs
# (8 is also the dark inside of each pincer); 1 2 the eyes; 15 black. Nothing else is white.
SHELL = [14, 13, 12, 11]
CREAM = [8, 7, 6, 5, 4]
D = dict(finish=0.2, body=0)
MATERIALS = [
    dict(name="outline", shades=[15, 14], finish=0.1, body=0),
    dict(name="hard shell", shades=SHELL, base=1, **D),
    dict(name="hard shell, underside", shades=CREAM, base=3, **D),
    dict(name="hard shell, legs", shades=CREAM, base=3, **D),
    dict(name="hard shell, pincer inside", shades=[8], base=0, **D),
    dict(name="eye (line art)", shades=[2, 1, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {15: "outline", **to("hard shell", SHELL), **to("hard shell, legs", CREAM), **to("eye (line art)", [1, 2])}
RULES = [
    dict(drawings=["body", "body-eyes-*"], colors=to("hard shell, underside", CREAM)),
    # the dark hollow of each pincer: all the dark brown in the upper claw (the arm below it uses the
    # same brown for its joints), and the dark brown along the lower finger
    dict(drawings=["hand-l2", "hand-r2", "hand-la", "hand-ra"], rect=[0, 0, 24, 18], colors={8: "hard shell, pincer inside"}),
    dict(drawings=["hand-l1", "hand-lb", "hand-rb"], colors={8: "hard shell, pincer inside"}),
    # three dark red pixels where a leg meets the shell: a softened outline
    dict(view="front", drawings=["foot-r2"], colors={14: "outline"}),
    # pupils (open: one pixel; closed: a two-pixel slit) are black like the outline
    dict(view="front", drawings=["body"], rect=[6, 12, 1, 1], colors={15: "eye (line art)"}),
    dict(view="front", drawings=["body"], rect=[15, 14, 1, 1], colors={15: "eye (line art)"}),
    dict(view="front", drawings=["body-eyes-*"], rect=[2, 4, 2, 1], colors={15: "eye (line art)"}),
    dict(view="front", drawings=["body-eyes-*"], rect=[12, 6, 2, 1], colors={15: "eye (line art)"}),
]
