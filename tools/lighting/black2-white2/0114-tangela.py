# Tangela: a ball of blue vines around a body nobody has seen, two round eyes in the dark, two red feet.
# "The blue vines shrouding its body are covered in a growth of fine hair" (Platinum, Black, White);
# "wide vines that are similar to seaweed" (Red/Blue); "masses of thick, blue vines" (Yellow).
# The painted art shades every vine flat, with one soft paler streak along it and no highlight: matte.
SOURCE = "sources/black2-white2/0114-tangela.spu"
# contour and deep shadow between vines (4), the vine (3), its lit side (2), the pale streak (1)
VINES = [4, 3, 2, 1]
MATERIALS = [
    # black: the line around each vine and each foot; and the darkest blue where it draws the line
    # between two vines
    dict(name="outline", shades=[14, 4], finish=0.1, body=0),
    # every vine. Thick plant tissue with a fine fuzz: just below matte (the value fur takes on a large
    # area), and only a trace of light through, as the other thick plant bodies (Oddish's root).
    dict(name="hairy vines", shades=VINES, base=1, finish=-0.1, body=0.1),
    # the red feet: plain bare skin, painted flat in the art
    dict(name="hide, feet", shades=[7, 8, 6, 5], base=1, finish=0.25, body=0.08),
    # the body hidden behind the vines, drawn flat black: only tinted by light, and not a line
    dict(name="body in the dark", shades=[], finish=0, body=0),
    # the whites, their gray edge, the pupils, and the gray lid lines of the shut eyes
    dict(name="eye (line art)", shades=[14, 12, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {14: "outline", **to("hairy vines", VINES), **to("hide, feet", [7, 8, 6, 5]), **to("eye (line art)", [12, 15])}
DARK = "body in the dark"
RULES = [
    # the vines lie over one another: every one-pixel stroke of their darkest blue is the line between two
    # of them (as shades, a lamp in front washed those lines out and the tangle went to one flat mass).
    # Where that blue is painted broad it is a vine deep in shadow, and stays the row's darkest shade.
    dict(thin_all={4: "outline"}),
    # the black hole in the tangle: every black pixel with only black around it
    dict(view="front", drawings=["body"], interior={14: ([], DARK)}),
    # the patch the eyes sit on is all that dark; the pupils are the one black pixel inside each white
    dict(drawings=["part-1", "part-1-eyes-*"], colors={14: DARK}),
    dict(drawings=["part-1"], rect=[6, 9, 1, 1], colors={14: "eye (line art)"}),
    dict(drawings=["part-1"], rect=[15, 9, 1, 1], colors={14: "eye (line art)"}),
    dict(drawings=["part-1-eyes-open"], rect=[3, 3, 1, 1], colors={14: "eye (line art)"}),
    dict(drawings=["part-1-eyes-open"], rect=[12, 3, 1, 1], colors={14: "eye (line art)"}),
]
