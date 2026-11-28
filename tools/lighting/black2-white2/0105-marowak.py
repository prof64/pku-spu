SOURCE = "sources/black2-white2/0105-marowak.spu"
BONE = [4, 3, 2, 1]
H = dict(finish=0.25, body=0.08)
MATERIALS = [
    # black; and the dark gray-brown (5) where it edges a claw (on the skull it is the bone's own contour)
    dict(name="outline", shades=[6, 5], finish=0.1, body=0),
    # the skull, fused to the head, and the bone club: dry bone, painted in flat soft grays with no highlight,
    # so dull and solid. The dark gray-brown (5) is its contour and the ridge line from eye to snout. Base is
    # the mid gray (3), as on Cubone: the back of the skull and the club's shaft are painted in it
    dict(name="bone", shades=BONE, base=2, finish=0.2, body=0),
    # plain bare brown skin, painted flat; the dark brown (15) is its contour and the arm's shadowed underside
    dict(name="hide", shades=[15, 14, 13], base=1, **H),
    # the palest tan (12) on the front thigh and forearm: the same skin at its most lit, in its own row so it
    # darkens with the limb
    dict(name="hide, lit patches", shades=[15, 14, 13, 12], base=1, **H),
    # the cream stomach; the darker orange (11) draws the grooves across it
    dict(name="hide, belly", shades=[11, 10, 9], base=2, **H),
    # white claws, gray (3) in shade
    dict(name="claws and teeth", shades=[3, 1], base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[6, 7, 2, 1], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
COLORS = {6: "outline", 5: "outline", **to("bone", BONE), **to("hide", [15, 14, 13]), 12: "hide, lit patches", **to("hide, belly", [11, 10, 9])}
EYE = to("eye (line art)", [6, 7, 2, 1])
RULES = [
    # claws: every white and gray pixel on a foot or a hand (image-10 and parts01-2 are a foot and a hand too)
    dict(drawings=["*foot*", "*arm*", "image-10", "parts01-2"], colors={**to("claws and teeth", [3, 1]), 5: "outline"}),
    # the eye: pupil, red iris and the white beside them, drawn only in the open-eye picture (shut, the lid is skin)
    dict(view="front", drawings=["head01-eyes-open"], rect=[15, 7, 3, 2], colors=EYE),
    dict(view="front", drawings=["head01-eyes-open"], rect=[17, 6, 1, 1], colors=EYE),
    dict(view="front", drawings=["head01-eyes-open"], rect=[14, 8, 1, 1], colors=EYE),
]
