SOURCE = "sources/black2-white2/0099-kingler.spu"
# Palette: 1 2 3 4 the orange shell (4 its dark contour, 1 the pale patch on the pincers); 5 6 7 8 the cream
# jaw, arms and legs; 10 11 the dark inside of the pincers (11 is also the pupils); 13 15 the eyes; 14 black.
# The unused first color is a blue, not a pale gray; no white here needs a shade (only the eyes are white).
SHELL = [4, 3, 2, 1]
CREAM = [8, 7, 6, 5]
D = dict(finish=0.2, body=0)
MATERIALS = [
    dict(name="outline", shades=[14, 8, 4], finish=0.1, body=0),
    dict(name="hard shell", shades=SHELL, base=1, **D),
    dict(name="hard shell, underside", shades=CREAM, base=2, **D),
    dict(name="hard shell, legs", shades=CREAM, base=2, **D),
    dict(name="hard shell, pincer inside", shades=[11, 10], base=1, **D),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[11, 13, 15], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {14: "outline", **to("hard shell", SHELL), **to("hard shell, legs", CREAM),
          **to("hard shell, pincer inside", [11, 10]), **to("eye (line art)", [13, 15])}
RULES = [
    dict(drawings=["mouse", "body01"], colors=to("hard shell, underside", CREAM)),
    # brown pixels on the carapace's edge soften its black line: outline. Pupils are the dark brown.
    dict(drawings=["head", "head01", "head-eyes-*"], colors={8: "outline", 11: "eye (line art)"}),
    # one dark red pixel on the arm's edge: a softened outline
    dict(view="back", drawings=["r-arm01"], colors={4: "outline"}),
    # the black line across the big pincer is drawn on the one claw, not between two pieces
    dict(view="front", drawings=["hansami-r1"], interior={14: (SHELL, INNER)}),
]

# The pale peach on top of each pincer is the shell's own lit shade. Left out of the row as a glint, it
# stays pale on a pincer gone dark when the light is behind it.
KEEP_TOP = ["hard shell"]
