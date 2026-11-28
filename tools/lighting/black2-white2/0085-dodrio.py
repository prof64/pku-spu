# Dodrio: three heads and a body of bristly brown down, black crest feathers, a black lower body and thighs, a fan
# of pink tail feathers with paler tips (all matte Feathers); horn beaks, two of them open; bare necks and legs (Dry hide; a male's
# necks are black, a female's the legs' cream); white claws.
# Colors: 14 black, 13 dark gray, 12 gray, 11 pale gray, 15 white; 4 3 2 1 the browns; 7 6 5 the creams; 10 9 8 the pinks.
SOURCE = "sources/black2-white2/0085-dodrio.spu"
F = dict(finish=-0.2, body=0.05)          # Feathers
DRY = dict(finish=0.05, body=0.03)        # Dry hide
MATERIALS = [
    dict(name="outline", shades=[14, 13, 10], finish=0.1, body=0),
    dict(name="feathers", shades=[4, 3, 2, 1], base=1, **F),                     # the down of the heads and the body
    # crests, lower body and thighs: painted dark gray inside the black line, a lighter gray where light catches them
    dict(name="feathers, black", shades=[13, 12], base=0, **F),
    dict(name="feathers, tail", shades=[10, 9], base=1, **F),
    dict(name="feathers, tail tips", shades=[9, 8], base=1, **F),                # the paler ends of the three tail feathers
    dict(name="beak", shades=[7, 6, 5], base=2, finish=0.4, body=0.05),
    dict(name="mouth", shades=[10], base=0, finish=0.8, body=0),                 # the red inside the two open beaks
    dict(name="dry hide, legs", shades=[7, 6, 5], base=2, **DRY),
    # a male's necks: painted black with a dark gray streak
    dict(name="dry hide, black necks", shades=[14, 13], base=0, **DRY),
    dict(name="dry hide, necks", shades=[7, 6, 5], base=1, **DRY),               # a female's necks: the legs' cream
    dict(name="claws and teeth", shades=[12, 11, 15], base=2, finish=0.7, body=0.05),
    dict(name="eye (line art)", shades=[14, 15, 11, 4], finish=0.9, body=0),
]
def to(name, colors): return {c: name for c in colors}
def eye(view, drawings, rect, colors):
    return dict(view=view, drawings=drawings, rect=rect, colors=to("eye (line art)", colors))
def each(stems, end): return [s + end for s in stems]

COLORS = {14: "outline", **to("feathers", [1, 2, 3, 4]), **to("feathers, black", [12, 13]),
          **to("feathers, tail", [9, 10]), 8: "feathers, tail tips", **to("dry hide, legs", [5, 6, 7]), **to("claws and teeth", [11, 15])}
MALE_NECKS = ["kubi01", "kubi02", "kubi03", "kubi-3", "kubi-2", "kubi"]
FEMALE_NECKS = ["kubi*-female"]
FEET = ["asi02", "asi03", "asi05", "asi-l2", "asi-l3", "asi-r2", "asi-r3"]
NECK = to("dry hide, necks", [5, 6, 7])
# the eye drawings of the back view, by the head they lie on (left, middle, right)
B3 = ["atama-3", "atama-3-2", "atama-3-female", "atama-3-2-female"]
B2 = ["atama-2", "atama-2-2", "atama-2-female", "atama-2-2-female"]
B1 = ["atama", "atama-2-2-2", "atama-female", "atama-2-2-female-2"]
BROW = [4, 14]                    # brows and lid lines: the down's dark brown and black
OPEN = [4, 11, 14, 15]
RULES = [
    # heads: everything cream is beak, the red inside an open beak is mouth
    dict(drawings=["atama*"], colors={**to("beak", [5, 6, 7]), 10: "mouth"}),
    # from behind a female's head drawings carry the top of her neck
    dict(view="back", drawings=["atama-3-female", "atama-3-2-female"], rect=[13, 25, 4, 2], colors=NECK),
    dict(view="back", drawings=["atama-2-female", "atama-2-2-female"], rect=[9, 22, 3, 2], colors=NECK),
    dict(view="back", drawings=["atama-female", "atama-2-2-female-2"], rect=[3, 11, 3, 4], colors=NECK),
    # eyes with their brows, and the lid lines of the closed look
    eye("front", ["atama01-eyes-open", "atama01-2-eyes-open"], [3, 3, 2, 3], OPEN),
    eye("front", ["atama01-eyes-open", "atama01-2-eyes-open"], [8, 2, 4, 4], OPEN),
    eye("front", ["atama01-eyes-closed", "atama01-2-eyes-closed"], [2, 4, 3, 2], BROW),
    eye("front", ["atama01-eyes-closed", "atama01-2-eyes-closed"], [9, 3, 4, 3], BROW),
    eye("front", ["atama02-eyes-open", "atama02-2-eyes-open"], [6, 0, 3, 3], OPEN),
    eye("front", ["atama02-eyes-open", "atama02-2-eyes-open"], [12, 0, 4, 3], OPEN),
    eye("front", ["atama02-eyes-closed", "atama02-2-eyes-closed"], [6, 3, 2, 1], BROW),
    eye("front", ["atama02-eyes-closed", "atama02-2-eyes-closed"], [13, 2, 3, 2], BROW),
    eye("front", ["atama03-eyes-open", "atama03-2-eyes-open"], [2, 1, 5, 4], OPEN),
    eye("front", ["atama03-eyes-closed", "atama03-2-eyes-closed"], [3, 3, 4, 2], BROW),
    eye("back", each(B3, "-eyes-open"), [3, 2, 3, 3], OPEN),
    eye("back", each(B3, "-eyes-closed"), [3, 2, 3, 4], BROW),
    eye("back", each(B2, "-eyes-open"), [3, 2, 2, 5], OPEN),
    eye("back", each(B2, "-eyes-closed"), [2, 3, 3, 4], BROW),
    eye("back", each(B2, "-eyes-closed"), [3, 2, 1, 1], BROW),
    eye("back", each(B1, "-eyes-open"), [3, 2, 2, 4], OPEN),
    eye("back", each(B1, "-eyes-closed"), [3, 2, 1, 4], BROW),
    # necks: bare skin. The brown bits at their lower ends are tufts of the body's down
    dict(drawings=MALE_NECKS, colors=to("dry hide, black necks", [13, 14])),
    dict(drawings=FEMALE_NECKS, colors=NECK),
    # feet: the claws are white, shaded pale gray and gray; the dark gray beside a leg or claw is its outline, softened
    dict(drawings=FEET, colors={12: "claws and teeth", 13: "outline"}),
    # tail: the dark pink lines inside the fan lie between its feathers (creases); the dark gray is its softened outline
    dict(drawings=["o"], colors={13: "outline"}, interior={10: ([8, 9], "outline")}),
]
