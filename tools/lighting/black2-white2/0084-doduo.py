# Doduo: two round heads and a round body of bristly brown down (matte Feathers), two horn beaks, bare necks and
# legs (Dry hide; a male's necks are black, a female's the legs' cream), white claws.
# Colors: 14 black, 13 gray, 15 white; 8 7 6 5 the browns; 12 11 10 9 the creams.
SOURCE = "sources/black2-white2/0084-doduo.spu"
F = dict(finish=-0.2, body=0.05)          # Feathers
DRY = dict(finish=0.05, body=0.03)        # Dry hide
MATERIALS = [
    dict(name="outline", shades=[14, 8, 7], finish=0.1, body=0),
    dict(name="feathers", shades=[8, 7, 6, 5], base=1, **F),                     # the down of both heads and the body
    dict(name="beak", shades=[12, 11, 10, 9], base=3, finish=0.4, body=0.05),
    dict(name="dry hide, legs", shades=[12, 11, 10, 9], base=1, **DRY),
    # a male's necks: painted black with a gray streak along the top
    dict(name="dry hide, black necks", shades=[14, 13], base=0, **DRY),
    # a female's necks: the legs' cream, in the head's dark brown shadow where they meet it
    dict(name="dry hide, necks", shades=[8, 12, 11, 10, 9], base=2, **DRY),
    # white with the palette's gray as its shade and lit-side contour
    dict(name="claws and teeth", shades=[13, 15], base=1, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[14, 13, 15, 12, 8], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
def eye(view, drawings, rect, colors):
    return dict(view=view, drawings=drawings, rect=rect, colors=to("eye (line art)", colors))

COLORS = {14: "outline", **to("feathers", [5, 6, 7, 8]), **to("dry hide, legs", [9, 10, 11, 12]),
          **to("claws and teeth", [13, 15])}
HEADS = ["atama0*", "image-0*", "l-head01*", "image-2*", "r-head01*"]
MALE_NECKS = ["neck01", "neck02", "l-neck01", "r-neck01"]
FEMALE_NECKS = ["neck01-female", "neck02-female", "l-neck01-female", "r-neck01-female"]
LEGS = ["asi0*", "image-7", "l-leg01", "image-9", "r-leg01", "image-11", "foot01"]
RULES = [
    # heads: everything cream is beak
    dict(drawings=HEADS, colors=to("beak", [9, 10, 11, 12])),
    # eyes, and the lid lines of the closed look
    eye("front", ["atama01-eyes-open"], [3, 3, 3, 4], [13, 14, 15]),
    eye("front", ["atama01-eyes-closed"], [2, 5, 3, 2], [12, 14]),
    eye("front", ["atama02-eyes-open"], [1, 1, 2, 4], [13, 14, 15]),
    eye("front", ["atama02-eyes-open"], [8, 3, 3, 4], [13, 14, 15]),
    eye("front", ["atama02-eyes-closed"], [0, 3, 3, 2], [8, 14]),
    eye("front", ["atama02-eyes-closed"], [9, 5, 3, 2], [8, 14]),
    eye("back", ["image-0-eyes-open", "l-head01-eyes-open"], [3, 4, 1, 3], [14, 15]),
    eye("back", ["image-0-eyes-closed", "l-head01-eyes-closed"], [2, 5, 3, 2], [14]),
    eye("back", ["image-2-eyes-open", "r-head01-eyes-open"], [5, 3, 1, 4], [13, 14, 15]),
    eye("back", ["image-2-eyes-closed", "r-head01-eyes-closed"], [4, 4, 2, 3], [8, 14]),
    # necks: bare skin. The brown bits at their lower ends are tufts of the body's down
    dict(drawings=MALE_NECKS, colors=to("dry hide, black necks", [13, 14])),
    dict(drawings=["karada01"], rect=[18, 1, 1, 1], colors={13: "dry hide, black necks"}),   # where a neck leaves the body
    dict(drawings=FEMALE_NECKS, colors=to("dry hide, necks", [8, 9, 10, 11, 12])),
    dict(drawings=["neck01-female"], rect=[0, 13, 16, 11], colors={8: "feathers"}),
    dict(drawings=["neck02-female"], rect=[0, 9, 16, 2], colors={8: "feathers"}),
    dict(drawings=["neck02-female"], rect=[0, 4, 16, 2], colors={7: "outline"}),             # the contour, softened
    # legs: the dark brown beside a leg's top is its outline, softened where the down overhangs it
    dict(drawings=LEGS, colors={8: "outline"}),
]
