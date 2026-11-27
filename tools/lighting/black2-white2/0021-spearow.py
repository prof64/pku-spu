# Spearow: every coat is plumage (matte Feathers); the black back is feathers too, the beak and claws are horn.
SOURCE = "sources/black2-white2/0021-spearow.spu"
F = dict(finish=-0.2, body=0.05)          # Feathers
MATERIALS = [
    dict(name="outline", shades=[1, 5, 13, 12], finish=0.1, body=0),
    dict(name="feathers", shades=[9, 8, 7, 6], base=1, **F),                     # brown head, ruff and tail
    dict(name="feathers, black back", shades=[], **F),   # painted flat black: light only tints it
    dict(name="feathers, belly", shades=[5, 4, 3], base=1, **F),
    dict(name="feathers, belly stripes", shades=[1, 5], base=0, **F),
    dict(name="feathers, wings", shades=[14, 13, 12], base=2, **F),
    dict(name="feathers, wing tips", shades=[11, 10], base=1, **F),
    dict(name="dry hide, feet", shades=[14, 13, 12, 11], base=2, finish=0.05, body=0.03),
    dict(name="beak", shades=[14, 13, 12, 11, 10], base=3, finish=0.4, body=0.05),
    # the claws are white with the belly's gray-browns as their shade
    dict(name="claws and teeth", shades=[4, 3, 15], base=2, finish=0.7, body=0.05),
    dict(name="mouth", shades=[14, 12], base=1, finish=0.8, body=0),
    dict(name="eye (line art)", shades=[1, 2, 15], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
def px(view, drawing, points, colors):
    return [dict(view=view, drawings=[drawing], rect=[x, y, 1, 1], colors=colors) for x, y in points]

COLORS = {1: "outline", 2: "eye (line art)", 15: "claws and teeth", **to("feathers, belly", [3, 4, 5]), **to("feathers", [6, 7, 8, 9]),
          **to("feathers, wing tips", [10, 11]), **to("feathers, wings", [12, 13, 14])}
BEAK = to("beak", [10, 11, 12, 13, 14])
EYE = to("eye (line art)", [1, 2, 15])
FOOT = to("dry hide, feet", [11, 12, 13, 14])
CLAW = {**to("claws and teeth", [3, 4, 15]), 5: "outline"}       # 5 around a foot is its softened outline
LINE = {12: "outline", 13: "outline"}
RULES = [
    # head: beak, open mouth, eyes
    dict(drawings=["atama", "atama-eyes-*", "head01"], colors=BEAK),
    dict(drawings=["atama"], rect=[8, 15, 5, 4], colors=to("mouth", [12, 14])),
    dict(drawings=["atama-eyes-*"], rect=[8, 7, 5, 1], colors=to("mouth", [12, 14])),
    dict(drawings=["atama"], rect=[11, 11, 4, 3], colors=EYE),
    dict(drawings=["atama"], rect=[7, 11, 1, 2], colors=EYE),
    dict(drawings=["atama-eyes-*"], rect=[11, 3, 4, 3], colors=EYE),
    dict(drawings=["atama-eyes-*"], rect=[7, 3, 1, 2], colors=EYE),
    # the back is black plumage; one-pixel black strokes stay the drawn line
    dict(drawings=["head01"], colors=to("feathers, black back", [1, 5]), thin_all={1: "outline"}),
    dict(drawings=["body01"], colors={1: "feathers, black back"}, thin_all={1: "outline"}),
    # the two thin stripes across the belly
    *px("front", "karada", [(7, 16), (8, 17), (9, 17), (10, 17), (11, 17), (12, 17), (14, 18), (15, 18), (16, 18),
                            (7, 18), (8, 19), (9, 19), (10, 19), (11, 19), (12, 19), (13, 19)], to("feathers, belly stripes", [1, 5])),
    # legs: feathered thigh above, bare foot and claws below
    dict(drawings=["asi", "asi1", "l-leg01", "r-leg01"], colors=FOOT),
    dict(drawings=["asi"], rect=[0, 8, 16, 8], colors=CLAW),
    dict(drawings=["asi1"], rect=[0, 7, 16, 9], colors=CLAW),
    dict(drawings=["l-leg01"], rect=[0, 8, 16, 8], colors=CLAW),
    dict(drawings=["r-leg01"], rect=[8, 7, 8, 1], colors=CLAW),
    dict(drawings=["r-leg01"], rect=[0, 8, 16, 8], colors=CLAW),
    # wings: the lines between the big feathers are creases (the dark shadow under the wing is not a line)
    dict(drawings=["hane2", "r-wings01"], interior={13: ([10, 11, 12], "outline")}),
    dict(drawings=["hane2", "r-wings01"], rect=[0, 14, 24, 10], colors={13: "feathers, wings"}),
    *px("front", "hane2", [(16, 5), (17, 5), (15, 6)], LINE),
    *px("back", "r-wings01", [(8, 6), (9, 6), (10, 7), (11, 7), (6, 8), (8, 9), (9, 10), (10, 10)], LINE),
    *px("back", "l-wings01", [(12, 5), (13, 5)], LINE),
]
