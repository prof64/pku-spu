SOURCE = "sources/black2-white2/0138-omanyte.spu"
# Palette: 1 black; 2 3 4 5 6 the blue body and tentacles, light to dark; 7 8 9 10 11 the shell, cream to dark
# brown (9 10 11 are the eyelids too); 12 white, 13 14 grays (the eyes).
SHELL = [11, 10, 9, 8, 7]
SKIN = [6, 5, 4, 3, 2]
MATERIALS = [
    dict(name="outline", shades=[1], finish=0.1, body=0),
    # the helix shell: "it withdraws itself inside its hard shell". Cloyster's and Shellder's row.
    # The art paints it flat cream with soft shading along the ribs and no highlight: dull.
    # Base is the tan (10) most of both views is painted in; the back view is nearly all of it.
    dict(name="hard shell", shades=SHELL, base=1, finish=0.2, body=0),
    # the soft body and its ten tentacles: painted flat blue with soft darker shading, no highlight. Plain bare
    # skin, as Tentacool's feelers. Base is the mid blue (4) the tentacles are painted in where they show.
    dict(name="hide", shades=SKIN, base=2, finish=0.25, body=0.08),
    # the eyelids (the whole ball when shut, its upper rim when open) are painted in the shell's tans, but are skin
    dict(name="hide, eyelids", shades=[11, 10, 9], base=2, finish=0.25, body=0.08),
    dict(name="seams and wrinkles", shades=[], finish=0, body=0),   # lines drawn inside a surface: tinted, never a crease
    dict(name="eye (line art)", shades=[1, 14, 13, 12], finish=0.9, body=0),
]
INNER = "seams and wrinkles"
def to(name, colors): return {c: name for c in colors}
COLORS = {1: "outline", **to("hard shell", SHELL), **to("hide", SKIN)}
RULES = [
    # the spiral and the rib lines drawn in black are lines on the one dome, not creases
    dict(drawings=["kara", "body01"], interior={1: (SHELL, INNER)}),
    dict(drawings=["me01-eyes-*"], colors=to("hide, eyelids", [11, 10, 9])),
    # white, its gray shade, the pupil and the black ring around the eye
    dict(drawings=["me01-eyes-open"], colors=to("eye (line art)", [1, 14, 13, 12])),
]
# The shell's cream (7) is the lit band of each rib in the front view: a real shade (as on Cloyster). The palest
# blue (2) is the lit tip of a tentacle, a few pixels; left out of the row it stays pale on tentacles gone dark
# with the sun behind.
KEEP_TOP = ["hard shell", "hide"]
